"""
belkhayate_formulas.py -- Formules Belkhayate pour TRADEX-AI (agent A1).

PERIMETRE : COG + Timing uniquement. Energie = stub non code (arbitrage utilisateur 13/06/2026).

SOURCE : 00-pilotage/STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md, section 1.1 (Piliers 1-2).
STATUT  : [RECONSTRUCTION -- non verifie]. La formule officielle Belkhayate n'a JAMAIS ete
          divulguee (cf. doc l.23). Tous les parametres (N, degre, k, n) sont CONFIGURABLES
          pour permettre le backtest (lookback 100-125 vs 250 barres) -- jamais codes en dur
          comme verite.
ANTI-REPAINT : mode ENDPOINT FIGE obligatoire -- on ne conserve que la valeur ajustee a la
          derniere barre cloturee ; aucune barre future n'entre dans un calcul (doc l.32-33).

Donnees lues depuis les JSON NinjaTrader 8 (VERROUILLE C5). Champ absent/perime -> NON_DETECTE
-> NON-TRADE (gere en amont par data_reader / staleness_monitor, pas ici).
"""
import os
from dataclasses import dataclass

import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Etiquette commune a toutes les sorties de ce module.
RECONSTRUCTION = "[RECONSTRUCTION -- non verifie]"


# =============================================================================
# PARAMETRES CONFIGURABLES  [RECONSTRUCTION -- non verifie]
# Valeurs de depart issues de STRATEGIE_CORRIGEE l.155 (HYPOTHESE TESTABLE).
# A backtester : lookback_N 250 (Admiral) vs 100-125 (communaute).
# =============================================================================
@dataclass
class COGParams:
    lookback_N: int = 250                       # nombre de barres de la fenetre de regression
    degree: int = 2                             # degre du polynome (2 par defaut, plus stable a
                                                # l'endpoint ; 3 disponible via le parametre)
    k_bands: tuple = (1.618, 2.618, 4.236)      # coefficients (nombre d'or et derives)


@dataclass
class TimingParams:
    lookback_n: int = 50                        # range de normalisation
    scale: float = 10.0                         # echelle de l'oscillateur (+/- scale)


# =============================================================================
# PILIER 1 -- COG (Centre de Gravite), mode ENDPOINT FIGE
# =============================================================================
def cog_bands(cog_value: float, sigma: float, k_bands) -> dict:
    """Bandes ŷ +/- k.sigma pour chaque coefficient k (doc l.31)."""
    bands = {}
    for k in k_bands:
        bands[f"+{k}"] = cog_value + k * sigma
        bands[f"-{k}"] = cog_value - k * sigma
    return bands


def cog_endpoint(closes, params: COGParams = None):
    """
    COG en mode ENDPOINT FIGE.

    Ajuste un polynome (moindres carres, degre `params.degree`) sur les `params.lookback_N`
    dernieres cloturees, puis renvoie UNIQUEMENT la valeur ajustee a la derniere barre
    (endpoint) -> supprime le repaint et rend le backtest honnete (doc l.32-33).

    Renvoie un dict {cog, sigma, slope, couleur, bandes, params, statut} ou None si la
    fenetre n'a pas assez de barres (le gestionnaire amont traduit None -> NON_DETECTE).

    [RECONSTRUCTION -- non verifie]
    """
    params = params or COGParams()
    n = params.lookback_N
    if closes is None or len(closes) < n:
        return None

    y = np.asarray(closes[-n:], dtype=float)
    # x centre autour de 0 pour la stabilite numerique de polyfit (Vandermonde mieux conditionne).
    x = np.arange(n, dtype=float)
    x = x - x.mean()

    coeffs = np.polyfit(x, y, params.degree)        # moindres carres
    poly = np.poly1d(coeffs)
    yhat = poly(x)
    sigma = float(np.std(y - yhat))                 # ecart-type des residus (doc l.30)

    x_end = x[-1]                                    # endpoint = derniere barre cloturee
    cog_value = float(poly(x_end))
    slope = float(np.polyder(poly)(x_end))          # pente a l'endpoint

    # [RECONSTRUCTION -- non verifie] couleur = signe de la pente a l'endpoint
    # (le doc parle de ligne bleue=haussier / rouge=baissier sans donner le calcul exact).
    couleur = "bleu" if slope > 0 else "rouge"

    return {
        "cog": cog_value,
        "sigma": sigma,
        "slope": slope,
        "couleur": couleur,
        "bandes": cog_bands(cog_value, sigma, params.k_bands),
        "params": {"N": n, "degre": params.degree, "k": params.k_bands},
        "statut": RECONSTRUCTION,
    }


def cog_series_endpoint(closes, params: COGParams = None) -> list:
    """
    Serie COG ANTI-REPAINT : pour chaque barre t, COG calcule uniquement sur la fenetre
    fermee a t (closes[:t+1]). La valeur en t ne change jamais quand des barres futures
    arrivent -> propriete verifiee par les tests. Renvoie une liste (None tant que t+1 < N).
    """
    params = params or COGParams()
    return [cog_endpoint(closes[: t + 1], params) for t in range(len(closes))]


# =============================================================================
# PILIER 2 -- TIMING (oscillateur, echelle +/- scale)
# =============================================================================
def timing_oscillator(highs, lows, params: TimingParams = None):
    """
    Timing Belkhayate [RECONSTRUCTION -- non verifie] (ports LazyBear/MBFX, doc l.40).

    Prix median (H+L)/2 de la barre courante, normalise par le range (plus-haut / plus-bas)
    des `params.lookback_n` dernieres barres, projete sur [-scale ; +scale] -- analogue a un
    stochastique non lisse. Centre 0 = zone neutre. Entree valide : [4;8] (vente) / [-8;-4] (achat).

    Renvoie un float dans [-scale ; +scale], ou None si pas assez de barres.
    """
    params = params or TimingParams()
    n = params.lookback_n
    if highs is None or lows is None or len(highs) < n or len(lows) < n:
        return None

    h = np.asarray(highs[-n:], dtype=float)
    l = np.asarray(lows[-n:], dtype=float)
    hh = float(np.max(h))
    ll = float(np.min(l))

    median_courant = (float(highs[-1]) + float(lows[-1])) / 2.0
    if hh == ll:                                     # range nul -> neutre
        return 0.0

    pos = (median_courant - ll) / (hh - ll)         # position dans le range [0 ; 1]
    return float((pos * 2.0 - 1.0) * params.scale)  # projection sur [-scale ; +scale]


# =============================================================================
# PILIER 3 -- ENERGIE : NON CODEE (arbitrage utilisateur 13/06/2026)
# =============================================================================
def energie(*args, **kwargs):
    """Energie Belkhayate -- NON CODEE. Deux pistes en conflit non tranche (MFI 20/80 vs
    proxy ATR/volume). Decision : attendre les vrais transcripts Whisper avant de coder."""
    raise NotImplementedError("[NON DOCUMENTE] -- attendre transcripts Whisper")
