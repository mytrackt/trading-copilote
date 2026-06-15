"""
cog_backtest.py — Backtest HOSTILE des parametres COG Belkhayate.

Mission : VALIDER ou REFUTER (periode=180, ordre=3, coeffs=[0.618, 1.618])
sur GC (Or), HG (Cuivre), ZW (Ble) avec des donnees publiques yfinance (5 ans daily).
Aucune confiance a priori : on compare contre 3 jeux de parametres alternatifs.

Methodo : COG = regression polynomiale (numpy.polyfit) sur N dernieres bougies ;
endpoint = valeur de la regression a t=N-1 ; bandes = endpoint +/- coeff*std(residus).
Signal = close franchit la bande ; reversion = retour DANS la bande sous REVERSION_WINDOW bougies.

LIMITES (voir rapport) : daily (pas range bars 5 ticks), pas de slippage/spread,
"reversion sous 10 bougies" est un test permissif. Confirme la FORMULE, pas le TIMING.

Lint : py -m py_compile cog_backtest.py
Run  : py cog_backtest.py
"""
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

try:
    import yfinance as yf
except ImportError:
    print("ERREUR : yfinance manquant. Installer : py -m pip install yfinance")
    sys.exit(1)

# ===================== ETAPE 0 — CONFIG =====================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # = 05-saas
OUTPUT_CSV = os.path.abspath(os.path.join(BASE_DIR, "..", "cog_backtest_results.csv"))
OUTPUT_MD = os.path.abspath(os.path.join(BASE_DIR, "..", "cog_backtest_rapport.md"))

ASSETS = {
    "GC": "GC=F",   # Or
    "HG": "HG=F",   # Cuivre
    "ZW": "ZW=F",   # Ble
}

PARAMS_BELKHAYATE = {"periode": 180, "ordre": 3, "coeffs": [0.618, 1.618]}
PARAMS_ALTERNATIVES = [
    {"periode": 100, "ordre": 3, "coeffs": [0.618, 1.618]},
    {"periode": 125, "ordre": 2, "coeffs": [0.618, 1.618]},
    {"periode": 250, "ordre": 3, "coeffs": [0.618, 1.618]},
]
TOUS_PARAMS = [PARAMS_BELKHAYATE] + PARAMS_ALTERNATIVES

PERIOD_DATA = "5y"
REVERSION_WINDOW = 10

# Seuils verdict
SEUIL_REV_CONFIRME = 55.0
SEUIL_REV_AREVISER = 45.0
SEUIL_NB_SIGNAUX = 30
SEUIL_R2 = 0.3


def label_params(p: dict) -> str:
    return f'{p["periode"]}/{p["ordre"]}'


# ===================== ETAPE 1 — DONNEES =====================
def telecharger(asset_code: str, ticker: str) -> pd.Series:
    """Telecharge le Close daily, renvoie une Series propre (datetime -> float)."""
    df = yf.download(ticker, period=PERIOD_DATA, interval="1d",
                     auto_adjust=True, progress=False)
    if df is None or len(df) == 0:
        raise RuntimeError(f"DONNEES INSUFFISANTES : aucune donnee pour {asset_code} ({ticker})")
    close = df["Close"]
    if isinstance(close, pd.DataFrame):   # MultiIndex single-ticker -> DataFrame 1 colonne
        close = close.iloc[:, 0]
    close = close.dropna()
    if len(close) < 500:
        raise RuntimeError(f"DONNEES INSUFFISANTES : {asset_code} a {len(close)} bougies (< 500)")
    if close.isna().any():
        raise RuntimeError(f"DONNEES INVALIDES : NaN dans Close {asset_code}")
    d0 = close.index[0].strftime("%Y-%m-%d")
    d1 = close.index[-1].strftime("%Y-%m-%d")
    print(f"  OK {asset_code} : {len(close)} bougies telechargees ({d0} -> {d1})")
    return close


# ===================== ETAPE 2 — COG =====================
def _fit(y: np.ndarray, periode: int, ordre: int):
    """Regression poly sur les `periode` dernieres valeurs.
    Renvoie (endpoint, r2, std_residus). Coeur interne (un seul polyfit)."""
    if len(y) < periode:
        raise ValueError(f"len(close)={len(y)} < periode={periode}")
    yy = np.asarray(y[-periode:], dtype=float)
    x = np.arange(periode)
    creg = np.polyfit(x, yy, ordre)
    fit = np.polyval(creg, x)
    ss_res = float(np.sum((yy - fit) ** 2))
    ss_tot = float(np.sum((yy - yy.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    endpoint = float(np.polyval(creg, periode - 1))
    std_resid = float(np.std(yy - fit, ddof=0))
    return endpoint, r2, std_resid


def calculer_cog_endpoint(close_series, periode: int, ordre: int) -> float:
    """API spec : endpoint de la regression. HOSTILE : ValueError si len<periode ou R2<=0."""
    endpoint, r2, _ = _fit(np.asarray(close_series, dtype=float), periode, ordre)
    if r2 <= 0.0:
        raise ValueError("R2 <= 0 — regression degeneree")
    return endpoint


def calculer_bandes(close_series, endpoint: float, periode: int, coeffs, ordre: int = 3):
    """API spec : bandes endpoint +/- coeff*std(residus). HOSTILE : ValueError si std==0."""
    _, _, std_resid = _fit(np.asarray(close_series, dtype=float), periode, ordre)
    if std_resid == 0:
        raise ValueError("std residus nul — donnees plates")
    return {
        coeffs[0]: (endpoint - coeffs[0] * std_resid, endpoint + coeffs[0] * std_resid),
        coeffs[1]: (endpoint - coeffs[1] * std_resid, endpoint + coeffs[1] * std_resid),
    }, std_resid


# ===================== ETAPE 3-4 — BACKTEST + METRIQUES =====================
def backtester(close: pd.Series, params: dict) -> dict:
    """Backtest rolling pour un asset et un jeu de parametres."""
    periode = params["periode"]
    ordre = params["ordre"]
    k1, k2 = params["coeffs"]

    arr = close.to_numpy(dtype=float)
    n = len(arr)

    nb_b1 = succ_b1 = 0
    nb_b2 = succ_b2 = 0
    r2_list = []
    degenerees = 0

    t_max = n - 1 - REVERSION_WINDOW   # besoin d'une fenetre future complete
    for t in range(periode, t_max + 1):
        window = arr[t - periode:t]    # passe seulement (pas de look-ahead)
        try:
            endpoint, r2, s = _fit(window, periode, ordre)
        except ValueError:
            degenerees += 1
            continue
        if s == 0:
            degenerees += 1
            continue
        r2_list.append(r2)

        price = arr[t]
        low1, high1 = endpoint - k1 * s, endpoint + k1 * s
        low2, high2 = endpoint - k2 * s, endpoint + k2 * s
        future = arr[t + 1:t + 1 + REVERSION_WINDOW]

        # --- Bande 1 (0.618) ---
        if price < low1:
            nb_b1 += 1
            if future.max() >= low1:
                succ_b1 += 1
        elif price > high1:
            nb_b1 += 1
            if future.min() <= high1:
                succ_b1 += 1

        # --- Bande 2 (1.618) ---
        if price < low2:
            nb_b2 += 1
            if future.max() >= low2:
                succ_b2 += 1
        elif price > high2:
            nb_b2 += 1
            if future.min() <= high2:
                succ_b2 += 1

    taux_b1 = (succ_b1 / nb_b1 * 100.0) if nb_b1 else 0.0
    taux_b2 = (succ_b2 / nb_b2 * 100.0) if nb_b2 else 0.0
    r2_moyen = float(np.mean(r2_list)) if r2_list else 0.0

    # Verdict strict
    if taux_b1 >= SEUIL_REV_CONFIRME and nb_b1 >= SEUIL_NB_SIGNAUX and r2_moyen >= SEUIL_R2:
        verdict = "CONFIRME"
    elif taux_b1 >= SEUIL_REV_AREVISER and nb_b1 >= SEUIL_NB_SIGNAUX:
        verdict = "A_REVISER"
    else:
        verdict = "REJETE"

    return {
        "params_label": label_params(params),
        "periode": periode, "ordre": ordre,
        "nb_signaux": nb_b1, "nb_signaux_b2": nb_b2,
        "taux_reversion_b1": round(taux_b1, 1),
        "taux_reversion_b2": round(taux_b2, 1),
        "R2_moyen": round(r2_moyen, 3),
        "degenerees": degenerees,
        "verdict": verdict,
    }


VERDICT_EMOJI = {"CONFIRME": "✅", "A_REVISER": "⚠️", "REJETE": "❌"}


def coche(ok: bool) -> str:
    return "✅" if ok else "❌"


# ===================== ETAPE 5 — SORTIES =====================
def main() -> int:
    print("=" * 60)
    print("COG BACKTEST HOSTILE — TRADEX-AI")
    print("=" * 60)

    resultats = {}   # asset -> list[dict] (1 par params)
    series = {}
    print("\n[1] Telechargement donnees yfinance (5 ans daily)...")
    for asset, ticker in ASSETS.items():
        try:
            series[asset] = telecharger(asset, ticker)
        except Exception as e:
            print(f"  ECHEC {asset} : {e}")
            return 1

    for asset, close in series.items():
        print("\n" + "=" * 60)
        print(f"COG BACKTEST — {asset} ({ASSETS[asset]})")
        print("=" * 60)
        res_list = []
        for params in TOUS_PARAMS:
            r = backtester(close, params)
            res_list.append(r)

        resultats[asset] = res_list
        belk = res_list[0]

        print(f"Parametres Belkhayate ({belk['params_label']}/0.618-1.618) :")
        print(f"  Signaux detectes            : {belk['nb_signaux']}")
        print(f"  Taux reversion bande 0.618  : {belk['taux_reversion_b1']}% "
              f"{coche(belk['taux_reversion_b1'] >= SEUIL_REV_CONFIRME)}")
        print(f"  Taux reversion bande 1.618  : {belk['taux_reversion_b2']}%")
        print(f"  R2 moyen rolling            : {belk['R2_moyen']} "
              f"{coche(belk['R2_moyen'] >= SEUIL_R2)}")
        print(f"  Verdict : {VERDICT_EMOJI[belk['verdict']]} {belk['verdict']}")

        print("Comparaison alternatives :")
        for alt in res_list[1:]:
            delta = alt["taux_reversion_b1"] - belk["taux_reversion_b1"]
            print(f"  [{alt['params_label']}] taux reversion : {alt['taux_reversion_b1']}%  "
                  f"-> {delta:+.1f} pts vs Belkhayate")
        best = max(res_list, key=lambda r: r["taux_reversion_b1"])
        if best is belk or best["taux_reversion_b1"] == belk["taux_reversion_b1"]:
            print(f"  -> Belkhayate {belk['params_label']} = MEILLEUR (ou egal)")
        else:
            print(f"  -> PAS optimal : {best['params_label']} meilleur "
                  f"({best['taux_reversion_b1']}%)")

    # ---------- CSV ----------
    lignes_csv = ["asset,params_label,nb_signaux,taux_reversion_b1,taux_reversion_b2,R2_moyen,verdict"]
    for asset, res_list in resultats.items():
        for r in res_list:
            lignes_csv.append(
                f"{asset},{r['params_label']},{r['nb_signaux']},"
                f"{r['taux_reversion_b1']},{r['taux_reversion_b2']},{r['R2_moyen']},{r['verdict']}"
            )
    with open(OUTPUT_CSV, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes_csv) + "\n")
    print(f"\nCSV ecrit ({len(lignes_csv) - 1} lignes) : {OUTPUT_CSV}")

    # ---------- Markdown ----------
    md = generer_rapport(resultats)
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Rapport ecrit : {OUTPUT_MD}")

    # ---------- Recap final ----------
    nb_belk_best = 0
    for asset, res_list in resultats.items():
        belk = res_list[0]
        best = max(res_list, key=lambda r: r["taux_reversion_b1"])
        if belk["taux_reversion_b1"] >= best["taux_reversion_b1"]:
            nb_belk_best += 1

    print("\n" + "=" * 60)
    print("RECAP")
    print("=" * 60)
    for asset, res_list in resultats.items():
        b = res_list[0]
        print(f"  {asset} : {VERDICT_EMOJI[b['verdict']]} {b['verdict']} "
              f"(rev {b['taux_reversion_b1']}% | R2 {b['R2_moyen']} | n={b['nb_signaux']})")
    print(f"  Belkhayate 180/3 = meilleur sur {nb_belk_best}/3 assets")
    return 0


def generer_rapport(resultats: dict) -> str:
    L = []
    L.append("# COG BACKTEST HOSTILE — TRADEX-AI")
    L.append(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    L.append("Parametres testes : Belkhayate (180/3) vs 3 alternatives (100/3, 125/2, 250/3)")
    L.append(f"Donnees : yfinance {PERIOD_DATA} journalier | reversion window = {REVERSION_WINDOW} bougies")
    L.append("")
    L.append("## Verdict global")
    L.append("| Asset | Verdict | Taux reversion 0.618 | R2 moyen | Meilleurs params |")
    L.append("|---|---|---|---|---|")
    for asset, res_list in resultats.items():
        b = res_list[0]
        best = max(res_list, key=lambda r: r["taux_reversion_b1"])
        meilleur = b["params_label"] if b["taux_reversion_b1"] >= best["taux_reversion_b1"] \
            else f'{best["params_label"]} ({best["taux_reversion_b1"]}%)'
        L.append(f"| {asset} | {VERDICT_EMOJI[b['verdict']]} {b['verdict']} | "
                 f"{b['taux_reversion_b1']}% | {b['R2_moyen']} | {meilleur} |")
    L.append("")
    L.append("## Analyse par asset")
    for asset, res_list in resultats.items():
        L.append(f"\n### {asset} ({ASSETS[asset]})")
        L.append("| Params | nb signaux | rev 0.618 | rev 1.618 | R2 moyen | verdict |")
        L.append("|---|---|---|---|---|---|")
        for r in res_list:
            tag = " **(Belkhayate)**" if r["params_label"] == "180/3" else ""
            L.append(f"| {r['params_label']}{tag} | {r['nb_signaux']} | "
                     f"{r['taux_reversion_b1']}% | {r['taux_reversion_b2']}% | "
                     f"{r['R2_moyen']} | {r['verdict']} |")
    L.append("")
    L.append("## Decision recommandee")
    L.extend(decision(resultats))
    L.append("")
    L.append("## ⚠️ Limites de ce backtest")
    L.append("- Donnees journalieres (NT8 utilise des range bars 5 ticks) : biais possible.")
    L.append("- Aucun slippage ni spread modelise.")
    L.append("- Belkhayate a valide CL (petrole) sur range bars : comparaison imparfaite sur daily.")
    L.append("- Test de reversion 'retour dans la bande sous 10 bougies' = permissif (mean-reversion triviale).")
    L.append("- Ce backtest evalue la FORMULE COG, PAS le TIMING d'execution ni la rentabilite reelle.")
    L.append("")
    return "\n".join(L)


def decision(resultats: dict) -> list:
    out = []
    verdicts = {a: rl[0]["verdict"] for a, rl in resultats.items()}
    nb_conf = sum(1 for v in verdicts.values() if v == "CONFIRME")
    for asset, rl in resultats.items():
        b = rl[0]
        best = max(rl, key=lambda r: r["taux_reversion_b1"])
        if b["verdict"] == "CONFIRME":
            out.append(f"- **{asset}** : parametres 180/3 CONFIRMES "
                       f"(reversion {b['taux_reversion_b1']}%, R2 {b['R2_moyen']}). Conserver.")
        elif b["verdict"] == "A_REVISER":
            note = "" if best is b else f" ; tester {best['params_label']} ({best['taux_reversion_b1']}%)"
            out.append(f"- **{asset}** : A REVISER (reversion {b['taux_reversion_b1']}%{note}).")
        else:
            out.append(f"- **{asset}** : REJETE sur daily "
                       f"(reversion {b['taux_reversion_b1']}%, n={b['nb_signaux']}, R2 {b['R2_moyen']}). "
                       f"Ne pas s'appuyer sur ces parametres en daily.")
    out.append("")
    if nb_conf == 3:
        out.append("**Conclusion** : 180/3 confirme sur les 3 actifs en daily. "
                   "Reste a valider sur range bars 5 ticks (timeframe reel NT8).")
    elif nb_conf == 0:
        out.append("**Conclusion** : 180/3 NON confirme en daily sur aucun actif. "
                   "Le backtest daily ne valide PAS la formule ; la validation Belkhayate "
                   "porte sur range bars (CL) — re-tester sur le bon timeframe avant tout usage reel.")
    else:
        out.append(f"**Conclusion** : 180/3 confirme sur {nb_conf}/3 actifs en daily. "
                   "Resultat mixte : ne pas generaliser ; re-tester sur range bars 5 ticks.")
    return out


if __name__ == "__main__":
    sys.exit(main())
