import pandas as pd
from datetime import datetime

BARS_PER_DAY_ESTIMATES = {
    "GC":  150,
    "ES":  200,
    "CL":  180,
    "6J":  120,
    "HG":  100,
    "MBT": 160,
}

CORRELATION_PAIRS = [
    ("GC","DX"), ("ES","VX"), ("BTC","ES"),
    ("CL","DX"), ("HG","ES"), ("6J","VX"),
]

def calculate_live_correlations(
    historical_data: dict,
    window_days: int = 30,
    actif_principal: str = "ES"
) -> dict:
    closes = pd.DataFrame({
        actif: data['close'] for actif, data in historical_data.items()
    })
    bars_day = BARS_PER_DAY_ESTIMATES.get(actif_principal, 160)
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
                "error": f"Actif {a} ou {b} absent"
            }
    return result

def check_portfolio_correlation(
    new_trade: dict,
    open_trades: list,
    live_correlations: dict
) -> bool:
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
