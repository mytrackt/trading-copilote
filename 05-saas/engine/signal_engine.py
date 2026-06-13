"""
signal_engine.py -- Moteur de signal TRADEX-AI (agent A4).

Logique ENTIEREMENT DETERMINISTE (calculee depuis les JSON NT8 ; Claude n'intervient que pour
l'analyse KB). Source : 00-pilotage/STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md, PARTIE 4.

Pipeline :
  1. Etape 0 -- pre-condition ELIMINATOIRE : 3/4 TRADING + 2/3 CONFIRMATION alignes (doc l.181-190).
  2. NON-TRADE absolus (doc l.215-221).
  3. Score 0-10 deterministe (grille doc l.196-208 ; COG aligne = eliminatoire).
  4. Decision : >= 7.0 -> SIGNAL ; 5.0-6.9 -> SURVEILLER ; < 5.0 -> IGNORER.

INDEPENDANCE ENERGIE : le score n'appelle JAMAIS belkhayate_formulas.energie() (stub non code).
Les criteres "volume" (>= 1.2x moy20) et "ATR normal" sont des entrees BRUTES independantes,
pas la formule composite Energie. Le module n'importe pas belkhayate_formulas.

Champ JSON absent / perime -> NON_DETECTE -> NON-TRADE (doc l.217).
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# GRILLE DE SCORE  (source : STRATEGIE_CORRIGEE l.196-208) -- total = 10.0
# COG : couleur alignee = ELIMINATOIRE (hors total ; score force a 0 si non aligne).
# =============================================================================
SCORE_GRID = {
    "prix_bande_2_3":         2.0,   # R2 : prix en bande 2 ou 3, cloture dedans
    "timing_ok":              2.0,   # R3 : Timing dans [4;8] / [-8;-4]
    "bandes_resserrees":      1.0,   # R4 : largeur < mediane 100 barres
    "biais_h4_aligne":        1.5,   # Couche 2
    "volume_ok":              1.0,   # Couche 1 : Volume >= 1.2x moyenne 20
    "atr_normal":             0.5,   # Couche 1 : pas de choc
    "structure_non_cassee":   0.5,   # Couche 1
    "confirmation_favorable": 1.0,   # Couche 6 : DX/ES/VX favorable ou neutre
    "news_clean":             0.5,   # aucun evenement +/-30min avant / 15min apres
}
SCORE_MAX = round(sum(SCORE_GRID.values()), 2)   # = 10.0

SEUIL_SIGNAL = 7.0       # [HYPOTHESE TESTABLE] doc l.211
SEUIL_SURVEILLER = 5.0   # [HYPOTHESE TESTABLE] doc l.212
RR_MIN = 2.0             # R/R >= 1:2 (doc l.211/218)

# Seuils des criteres calcules (sources citees) :
VOLUME_RATIO_MIN = 1.2   # doc l.203
ATR_CHOC_MULT = 2.0      # ATR > 2x mediane = choc (doc l.104) -> atr_normal si < 2.0
TIMING_ZONE_ACHAT = (-8.0, -4.0)   # doc l.39 / l.200
TIMING_ZONE_VENTE = (4.0, 8.0)

# Champs obligatoires du contexte (absence -> NON_DETECTE -> NON-TRADE).
_CHAMPS_OBLIGATOIRES = (
    "sens", "trading_cog", "confirmation", "cog_couleur", "timing",
    "prix_bande_2_ou_3", "bandes_resserrees", "biais_h4_aligne",
    "volume_ratio", "atr_ratio", "structure_non_cassee", "news_clean",
    "rr", "taille_contrats", "in_news_window",
)


def _non_trade(raison: str, **extra) -> dict:
    return {"decision": "NON_TRADE", "raison": raison, "score": 0.0, **extra}


def timing_in_zone(timing: float, sens: str) -> bool:
    """R3 : Timing dans la zone d'entree selon le sens (achat zone basse, vente zone haute)."""
    lo, hi = TIMING_ZONE_ACHAT if sens == "ACHAT" else TIMING_ZONE_VENTE
    return lo <= timing <= hi


def precondition_etape0(trading_cog: dict, confirmation: dict, sens: str) -> dict:
    """
    Etape 0 ELIMINATOIRE (doc l.181-190).
    - trading_cog : {"GC": "bleu"|"rouge"|None, "HG":..., "CL":..., "ZW":...}
    - confirmation : {"DX": bool, "ES": bool, "VX": bool}  (favorable au sens du trade, evalue en amont)
    Renvoie {ok, nb_trading, nb_confirmation, raison}.
    """
    couleur_attendue = "bleu" if sens == "ACHAT" else "rouge"
    nb_trading = sum(1 for a in ("GC", "HG", "CL", "ZW") if trading_cog.get(a) == couleur_attendue)
    nb_conf = sum(1 for a in ("DX", "ES", "VX") if confirmation.get(a) is True)
    ok = nb_trading >= 3 and nb_conf >= 2
    raison = "OK" if ok else f"Etape 0 KO : {nb_trading}/4 trading, {nb_conf}/3 confirmation (requis 3 + 2)"
    return {"ok": ok, "nb_trading": nb_trading, "nb_confirmation": nb_conf, "raison": raison}


def compute_score(ctx: dict) -> dict:
    """
    Score 0-10 deterministe (grille SCORE_GRID). COG non aligne au sens -> eliminatoire (score 0).
    Renvoie {score, eliminatoire, breakdown}.
    N'utilise jamais l'Energie : volume_ok et atr_normal sont des criteres independants.
    """
    sens = ctx["sens"]
    cog_aligne = ((ctx["cog_couleur"] == "bleu" and sens == "ACHAT")
                  or (ctx["cog_couleur"] == "rouge" and sens == "VENTE"))
    if not cog_aligne:
        return {"score": 0.0, "eliminatoire": True, "breakdown": {}}

    nb_conf = sum(1 for a in ("DX", "ES", "VX") if ctx["confirmation"].get(a) is True)
    conditions = {
        "prix_bande_2_3":         bool(ctx["prix_bande_2_ou_3"]),
        "timing_ok":              timing_in_zone(ctx["timing"], sens),
        "bandes_resserrees":      bool(ctx["bandes_resserrees"]),
        "biais_h4_aligne":        bool(ctx["biais_h4_aligne"]),
        "volume_ok":              ctx["volume_ratio"] >= VOLUME_RATIO_MIN,
        "atr_normal":             ctx["atr_ratio"] < ATR_CHOC_MULT,
        "structure_non_cassee":   bool(ctx["structure_non_cassee"]),
        "confirmation_favorable": nb_conf >= 2,
        "news_clean":             bool(ctx["news_clean"]),
    }
    breakdown = {k: (SCORE_GRID[k] if cond else 0.0) for k, cond in conditions.items()}
    score = round(sum(breakdown.values()), 2)
    return {"score": score, "eliminatoire": False, "breakdown": breakdown}


def evaluate_signal(ctx: dict) -> dict:
    """
    Point d'entree A4. Renvoie un dict {decision, score, ...}.
    decision in : NON_TRADE / SIGNAL / SURVEILLER / IGNORER.
    SIGNAL exige validation humaine obligatoire en mode Manuel (mode Auto reste bloque ailleurs).
    """
    # 1. NON_DETECTE : un champ obligatoire absent ou None -> NON-TRADE (doc l.217)
    manquants = [c for c in _CHAMPS_OBLIGATOIRES if ctx.get(c) is None]
    if manquants:
        return _non_trade("NON_DETECTE", champs_manquants=manquants)

    sens = ctx["sens"]
    if sens not in ("ACHAT", "VENTE"):
        return _non_trade("SENS_INVALIDE", details=sens)

    # 2. Etape 0 eliminatoire
    e0 = precondition_etape0(ctx["trading_cog"], ctx["confirmation"], sens)
    if not e0["ok"]:
        return _non_trade("ETAPE_0_KO", details=e0["raison"])

    # 3. NON-TRADE absolus (doc l.215-221) cote signal
    if ctx["in_news_window"]:
        return _non_trade("NEWS_WINDOW")
    if ctx["rr"] < RR_MIN:
        return _non_trade("RR_INSUFFISANT", rr=ctx["rr"], rr_min=RR_MIN)
    if ctx["taille_contrats"] <= 0:
        return _non_trade("TAILLE_ZERO")

    # 4. Score (Etape 0 validee)
    s = compute_score(ctx)
    if s["eliminatoire"]:
        return _non_trade("COG_NON_ALIGNE", breakdown=s["breakdown"])

    # 5. Decision
    if s["score"] >= SEUIL_SIGNAL and ctx["rr"] >= RR_MIN:
        decision = "SIGNAL"
    elif s["score"] >= SEUIL_SURVEILLER:
        decision = "SURVEILLER"
    else:
        decision = "IGNORER"

    return {
        "decision": decision,
        "score": s["score"],
        "score_max": SCORE_MAX,
        "breakdown": s["breakdown"],
        "etape_0": e0,
        "rr": ctx["rr"],
        "validation_humaine_requise": decision == "SIGNAL",
    }


# =============================================================================
# INVALIDATIONS R8-R10 (position OUVERTE) -- doc l.61-63
# =============================================================================
def check_invalidations(pos: dict) -> dict:
    """
    Verifie les invalidations sur une position ouverte.
    - R8 : COG change de couleur AVANT TP1 -> sortie immediate.
    - R9 : cloture AU-DELA de la 3e bande -> sortie (echec mean reversion, pas de moyenne a la baisse).
    - R10: news majeure imprevue -> fermeture ou reduction immediate.
    Renvoie {invalidations: [(code, raison, action)], action_globale}.
    """
    inval = []
    if not pos.get("tp1_atteint", False) and pos.get("cog_couleur_courante") != pos.get("cog_couleur_entree"):
        inval.append(("R8", "COG a change de couleur avant TP1", "SORTIE_IMMEDIATE"))
    if pos.get("cloture_au_dela_bande3", False):
        inval.append(("R9", "Cloture au-dela de la 3e bande", "SORTIE_IMMEDIATE"))
    if pos.get("news_majeure_imprevue", False):
        inval.append(("R10", "News majeure imprevue", "FERMETURE_OU_REDUCTION"))

    if any(code in ("R8", "R9") for code, _, _ in inval):
        action_globale = "SORTIE_IMMEDIATE"
    elif inval:
        action_globale = "FERMETURE_OU_REDUCTION"
    else:
        action_globale = "AUCUNE"
    return {"invalidations": inval, "action_globale": action_globale}
