# -*- coding: utf-8 -*-
"""File Optimus : slugs explicites cartographie sec.13 (sitemap incomplet).
3 entrees a ellipse non reconstructibles -> ecartees (traitement manuel).
footprint-charts deja fait -> exclu.
"""
import re
B = "https://optimusfutures.com/blog/"
SLUGS = [
    "order-flow-trading", "order-flow-analysis", "order-flow-software",
    "best-order-flow-indicators", "order-flow-imbalance",
    "technical-analysis-with-order-flow",
    "how-to-set-up-your-trading-charts-for-order-flow-trading",
    "order-flow-in-tradingview", "volume-profile-trading",
    "tpo-charts-explained-for-beginners-market-profile-guide",
    "volume-and-open-interest", "anchored-vwap",
    "best-indicators-for-day-trading-futures", "average-true-range-indicator",
    "best-tradingview-indicators", "support-and-resistance-trading-guide",
    "breakout-trading", "day-trading-chart-patterns", "gap-trading-strategies",
    "how-to-trade-fair-value-gaps", "mean-reversion-trading",
    "end-of-day-trading-strategies", "futures-trading-scalping-strategy",
    "stop-loss-orders-in-futures-trading", "day-trading-risk-management",
    "backtesting-trading-strategies-in-futures-markets", "how-to-backtest-on-tradingview",
    "vix-futures-guide", "what-es-futures-tell-you-before-market-opens",
    "how-to-read-stock-market-futures", "tradingview-tick-charts", "index-futures-trading",
]
with open("queue_optimus.tsv", "w", encoding="utf-8") as f:
    for s in SLUGS:
        f.write(f"{B}{s}/\t{re.sub(r'[^a-z0-9]+','_',s)}\n")
print(f"queue_optimus.tsv : {len(SLUGS)} pages (3 ellipses ecartees)")
