import os
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Estimation bars/jour — à calibrer semaine 9 (paper trading)
# Catégorie TRADING (ordres possibles)
BARS_PER_DAY_ESTIMATES = {
    "GC":  150,   # Or
    "HG":  100,   # Cuivre
    "CL":  180,   # Pétrole WTI
    "ZW":  80,    # Blé (CBOT)
    # Catégorie CONFIRMATION (analyse uniquement)
    "ES":  200,   # S&P 500
    "VX":  90,    # VIX
    "DX":  120,   # Dollar Index
    # Catégorie REFERENCE inter-marché (corrélations uniquement)
    "MBT": 160,   # Bitcoin Micro — no trade
    "6J":  120,   # Yen — no trade
}

# Paires de corrélations inter-marchés
# GC/HG/CL/ZW = actifs tradables
# DX/ES/VX = confirmation
# MBT/6J = référence non-tradable
CORRELATION_PAIRS = [
    ("GC",  "DX"),   # Or vs Dollar — corrélation inverse classique
    ("GC",  "ES"),   # Or vs SP500 — risk on/off
    ("HG",  "ES"),   # Cuivre vs SP500 — indicateur croissance
    ("CL",  "DX"),   # Pétrole vs Dollar — corrélation inverse
    ("ZW",  "DX"),   # Blé vs Dollar
    ("ES",  "VX"),   # SP500 vs VIX — toujours inverse
    ("GC",  "MBT"),  # Or vs BTC — refuge inter-marché (référence seul)
    ("DX",  "6J"),   # Dollar vs Yen — refuge devise (référence seul)
]


def calculate_live_correlations(
    historical_data: dict,
    window_days: int = 30,
    actif_principal: str = "GC"
) -> dict:
    """
    Calcule les corrélations live sur 30j et 7j pour toutes les paires.
    Retourne un dict avec value, short, unstable, as_of.
    """
    closes = pd.DataFrame({
        actif: data['close'] for actif, data in historical_data.items()
    })
    bars_day = BARS_PER_DAY_ESTIMATES.get(actif_principal, 150)
    w30 = window_days * bars_day
    w7  = 7 * bars_day
    corr_30j = closes.tail(w30).corr()
    corr_7j  = closes.tail(w7).corr()
    result = {}
    for a, b in CORRELATION_PAIRS:
        try:
            v30 = round(corr_30j.loc[a, b], 3)
            v7  = round(corr_7j.loc[a, b], 3)
            result[f"{a}_{b}"] = {
                "value":    v30,
                "short":    v7,
                "unstable": abs(v30 - v7) > 0.20,
                "as_of":    datetime.utcnow().isoformat(),
            }
        except KeyError:
            result[f"{a}_{b}"] = {
                "value": 0, "unstable": True,
                "error": f"Actif {a} ou {b} absent des données historiques"
            }
    return result


def check_portfolio_correlation(
    new_trade: dict,
    open_trades: list,
    live_correlations: dict
) -> bool:
    """
    Retourne False si un trade ouvert est corrélé > 0.60 avec new_trade.
    Protège contre le risque de portefeuille corrélé.
    IMPORTANT : ne vérifie que les actifs TRADABLES (GC/HG/CL/ZW).
    """
    for open_trade in open_trades:
        k1 = f"{new_trade['actif']}_{open_trade['actif']}"
        k2 = f"{open_trade['actif']}_{new_trade['actif']}"
        corr = abs(
            live_correlations.get(k1, live_correlations.get(k2, {}))
            .get('value', 0)
        )
        if corr > 0.60:
            return False
    return True
