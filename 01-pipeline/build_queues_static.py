# -*- coding: utf-8 -*-
"""Genere les files NinjaTrader et Sierra Chart depuis la cartographie.
URLs stables (chemins explicites / IDs d'etudes). Sortie : <src>.tsv
"""
import re

NT = "https://ninjatrader.com"
NT_PATHS = [
    "/futures/blogs/ninjatrader-order-flow/",
    "/futures/blogs/footprint-charts-guide/",
    "/learn/order-flow-indicators/",
    "/futures/blogs/what-is-cumulative-delta-in-order-flow-trading/",
    "/futures/blogs/track-buying-selling-pressure-with-order-flow-cumulative-delta/",
    "/futures/blogs/order-flow-trading-with-volumetric-bars/",
    "/futures/blogs/use-volume-profile-to-track-order-flow-on-charts/",
    "/futures/blogs/how-to-trade-with-volume-profile-part-1/",
    "/futures/blogs/what-is-volume-weighted-average-price-vwap/",
    "/futures/blogs/volume-analysis-in-futures-trading/",
    "/futures/blogs/how-to-identify-entry-zones-with-volume-analysis-trading-guide/",
    "/learn/technical-analysis/analyze-volume-in-futures-markets/",
    "/futures/blogs/volume-spread-analysis-and-fomo-of-strong-directional-moves/",
    "/futures/blogs/best-futures-trading-indicators/",
    "/futures/blogs/5-key-indicators-for-day-trading-futures/",
    "/futures/blogs/common-mistakes-when-using-rsi-indicators-in-futures/",
    "/learn/technical-analysis/momentum-as-indicator-in-futures-trading/",
    "/learn/technical-analysis/use-volatility-as-indicator-in-futures-trading/",
    "/learn/technical-analysis/identifying-trends-in-futures-markets/",
    "/learn/technical-analysis/identify-chart-patterns-on-futures-trading-charts/",
    "/futures/blogs/chart-patterns-trading/",
    "/futures/blogs/price-action-trading-strategies/",
    "/futures/blogs/how-to-identify-intraday-support-and-resistance-levels-in-your-trading/",
    "/futures/blogs/supply-demand-zones-futures/",
    "/futures/blogs/trade-trend-reversals-futures/",
    "/futures/blogs/how-to-trade-liquidity-traps-in-futures/",
    "/futures/blogs/futures-trading-risk-management-margin-leverage-stops-position-sizing/",
    "/futures/blogs/mastering-risk-management-in-futures-trading/",
    "/futures/blogs/stop-loss-strategies/",
    "/futures/futures-trading-basics/risk-management/",
    "/futures/blogs/how-to-use-the-superdom-price-ladder-for-order-entry/",
    "/futures/blogs/intro-to-the-ninjatrader-desktop-superdom/",
    "/futures/blogs/ninjascript-best-practices/",
    "/futures/blogs/z-score-futures-trading-strategy/",
    "/futures/blogs/how-to-read-a-futures-trading-chart/",
    "/learn/building-a-trading-strategy/",
    "/futures/blogs/how-to-use-automated-trade-management-strategies-on-ninjatrader/",
    "/futures/blogs/futures-trading-strategies-ranked-difficulty/",
]

SC = "https://www.sierrachart.com/index.php?page="
SC_HUBS = [
    ("doc/TechnicalStudiesReference.php", "hub_studies_reference"),
    ("doc/NumbersBars.php", "numbers_bars_footprint"),
    ("doc/StudiesReference/TimePriceOpportunityCharts.html", "tpo_market_profile"),
]
SC_IDS = {
    292: "cumulative_delta_volume", 296: "cumulative_delta_trades",
    323: "cumulative_delta_tick", 444: "bar_delta_below_bar",
    368: "numbers_bars_avg_vol_per_price", 141: "volume_by_price",
    209: "volume_value_area_lines", 471: "volume_va_for_bars",
    158: "tpo_value_area_lines", 108: "vwap_std_dev", 352: "vwap_rolling_std_dev",
    38: "rsi", 504: "connors_rsi", 180: "stochrsi", 500: "laguerre_rsi",
    32: "macd", 248: "volume_weighted_macd", 13: "adx", 16: "adxr", 197: "dmi",
    19: "atr", 428: "normalized_atr", 14: "bollinger_bands", 135: "bollinger_bandwidth",
    221: "bollinger_squeeze", 35: "momentum", 188: "chande_momentum",
    435: "pmo", 255: "rmi", 62: "momentum_trend", 408: "point_figure_box_count",
}


def write(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for url, nom in rows:
            f.write(f"{url}\t{nom}\n")
    print(f"{path}: {len(rows)} pages")


def nom_from_path(p):
    return re.sub(r"[^a-z0-9]+", "_", p.strip("/").split("/")[-1].lower()).strip("_")


write("queue_ninjatrader.tsv", [(NT + p, nom_from_path(p)) for p in NT_PATHS])
write("queue_sierrachart.tsv",
      [(SC + slug, nom) for slug, nom in SC_HUBS] +
      [(f"{SC}doc/StudiesReference.php&ID={i}", f"sierra_{i}_{nom}")
       for i, nom in SC_IDS.items()])
