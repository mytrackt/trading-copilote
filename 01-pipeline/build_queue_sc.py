# -*- coding: utf-8 -*-
"""Construit la file d'extraction StockCharts (GARDER) depuis _llms.txt.

Sortie : queue_stockcharts.tsv  ->  <url><TAB><nom_page>
Regles de rejet alignees sur CARTOGRAPHIE_SOURCES_COMPLETE.md section 1.
"""
import re

BASE = "https://chartschool.stockcharts.com/table-of-contents/"
t = open("_llms.txt", encoding="utf-8").read()
slugs = sorted(set(re.findall(
    r"https://chartschool\.stockcharts\.com/table-of-contents/([^)\s]+)\.md", t)))

# --- DEJA SCRAPE (7 doublons) ---
DEJA = {
    "technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential",
    "technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi",
    "technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator",
    "technical-indicators-and-overlays/technical-indicators/average-directional-index-adx",
    "chart-analysis/candlestick-charts/candlestick-bullish-reversal-patterns",
    "chart-analysis/candlestick-charts/candlestick-bearish-reversal-patterns",
    "market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial",
}

# --- REJETS exacts (slug complet) ---
REJET_EXACT = {
    # overview hors scope
    "overview/why-analyze-securities", "overview/fundamental-analysis",
    "overview/asset-allocation-and-diversification", "overview/options-trading",
    "overview/options-trading/introduction-to-options",
    "overview/options-trading/options-pricing-and-options-chains",
    "overview/options-trading/options-trading-strategies",
    "overview/john-murphys-charting-made-easy-ebook",
    # market-indicators : DecisionPoint/Pring/breadth equites niche
    "market-indicators/decisionpoint-intermediate-term-breadth-momentum-oscillator-itbm",
    "market-indicators/decisionpoint-intermediate-term-volume-momentum-oscillator-itvm",
    "market-indicators/decisionpoint-swenlin-trading-oscillator-sto",
    "market-indicators/prings-bottom-fisher", "market-indicators/prings-diffusion-indicators",
    "market-indicators/prings-inflation-and-deflation-indexes",
    "market-indicators/prings-net-new-high-indicators",
    "market-indicators/net-new-52-week-highs", "market-indicators/record-high-percent",
    "market-indicators/percent-above-moving-average",
    # market-analysis niche
    "market-analysis/decisionpoint-rydex-asset-analysis",
    "market-analysis/the-decisionpoint-chart-gallery",
    # technical-indicators : proprietaires StockCharts / equity-rank / blocs price triviaux
    "technical-indicators-and-overlays/technical-indicators/distance-from-highs",
    "technical-indicators-and-overlays/technical-indicators/distance-from-lows",
    "technical-indicators-and-overlays/technical-indicators/distance-from-moving-average",
    "technical-indicators-and-overlays/technical-indicators/distance-to-highs",
    "technical-indicators-and-overlays/technical-indicators/distance-to-lows",
    "technical-indicators-and-overlays/technical-indicators/traffic-light",
    "technical-indicators-and-overlays/technical-indicators/performance-spread",
    "technical-indicators-and-overlays/technical-indicators/stockcharts-technical-rank-sctr",
    "technical-indicators-and-overlays/technical-indicators/gopalakrishnan-range-index",
    "technical-indicators-and-overlays/technical-indicators/rrg-relative-strength",
    "technical-indicators-and-overlays/technical-indicators/high-minus-low",
    "technical-indicators-and-overlays/technical-indicators/median-price",
    "technical-indicators-and-overlays/technical-indicators/typical-price",
    "technical-indicators-and-overlays/technical-indicators/weighted-close",
    "technical-indicators-and-overlays/technical-indicators/cmb-composite-index",
    "technical-indicators-and-overlays/technical-overlays/highest-high-value",
    "technical-indicators-and-overlays/technical-overlays/lowest-low-value",
    "technical-indicators-and-overlays/technical-overlays/linear-regression-intercept",
    "technical-indicators-and-overlays/technical-indicators/linear-regression-r2",
    # chart-types / scans : outil plateforme equites
    "chart-analysis/chart-types/marketcarpets",
    "chart-analysis/point-and-figure-charts/p-and-f-scans-and-alerts",
    "chart-analysis/point-and-figure-charts/p-and-f-scans-and-alerts/p-and-f-pattern-alerts",
    # trading-strategies : equity-only / breadth / niche
    "trading-strategies-and-models/decisionpoint-trend-model",
    "trading-strategies-and-models/trading-strategies/hindenburg-omen",
    "trading-strategies-and-models/trading-strategies/fabers-sector-rotation-trading-strategy",
    "trading-strategies-and-models/trading-strategies/percent-above-50-day-sma",
    "trading-strategies-and-models/trading-strategies/slope-performance-trend",
}

# index-and-market-indicator-catalog : ne garder que ces 5
CATALOG_KEEP = {
    "index-and-market-indicator-catalog/cme-futures-and-spot-prices",
    "index-and-market-indicator-catalog/ice-futures-and-spot-prices",
    "index-and-market-indicator-catalog/s-and-p-gsci-indices",
    "index-and-market-indicator-catalog/us-treasury-yields",
    "index-and-market-indicator-catalog/economic-indicators",
}


def rejete(s):
    if "/" not in s:               # stubs de section (overview, chart-analysis...)
        return True
    if s.startswith("glossary"):
        return True
    if s in DEJA or s in REJET_EXACT:
        return True
    if s.startswith("index-and-market-indicator-catalog/"):
        return s not in CATALOG_KEEP
    return False


garde = [s for s in slugs if not rejete(s)]

# nom_page : dernier segment, anti-collision via prefixe parent
noms, used = {}, {}
for s in garde:
    seg = s.split("/")
    base = re.sub(r"[^a-z0-9]+", "_", seg[-1].lower()).strip("_")
    nom = base
    if nom in used and used[nom] != s:
        nom = re.sub(r"[^a-z0-9]+", "_", (seg[-2] + "_" + seg[-1]).lower()).strip("_")
    used[nom] = s
    noms[s] = nom

with open("queue_stockcharts.tsv", "w", encoding="utf-8") as f:
    for s in garde:
        f.write(f"{BASE}{s}.md\t{noms[s]}\n")

print(f"TOTAL slugs llms.txt : {len(slugs)}")
print(f"GARDER (file)        : {len(garde)}")
print(f"Rejetes/doublons     : {len(slugs) - len(garde)}")
# verif collisions de nom_page
from collections import Counter
col = [n for n, c in Counter(noms.values()).items() if c > 1]
print(f"Collisions nom_page  : {col if col else 'aucune'}")
