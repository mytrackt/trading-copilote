# -*- coding: utf-8 -*-
"""File Adam Grimes : matche la liste curee (CARTOGRAPHIE section 9) au sitemap.

On ne garde QUE les articles evergreen listes (118), via fragments distinctifs.
Rejet implicite de tout le reste (chart-of-the-day, analyses datees, podcast...).
Sortie : queue_adamgrimes.tsv  + rapport de matching pour revue.
"""
import re

slugs = sorted(set(
    re.sub(r"https?://(www\.)?adamhgrimes\.com/", "", l).strip("/")
    for l in re.findall(r"<loc>(.*?)</loc>", open("_ag_posts.xml", encoding="utf-8").read())))
slugs = [s for s in slugs if s and "/" not in s]

# Fragments distinctifs (substring unique) de la liste curee cartographie sec.9
FRAGMENTS = [
    "first-principles-of-technical-analysis",  # 5 parties
    "two-modes", "toward-a-simple-model-of-price-behavior", "the-two-forces",
    # volatilite
    "volatility-compression", "compression-and-expansion", "volatility-clustering",
    "forecasting-volatility", "the-volatility-game", "calculate-volatility-in-excel",
    "calculate-sigmaspikes", "spikes-in-the-vix",
    # tendance
    "200-day-moving-average", "moving-averages-digging-deeper", "death-cross",
    "trend-indicator", "efficiency-ratio", "trend-day", "trend-days",
    "trend-following-futures", "trend-is-your-friend",
    # patterns / price action
    "failure-test", "trade-pullbacks", "nested-pullback", "choosing-best-pullbacks",
    "complex-consolidations", "the-power-channel", "inside-bar", "nr7",
    "free-bars", "ranges-and-measured-moves", "the-anti", "using-highs-and-lows",
    "reading-inside-the-bars",
    # trendlines / niveaux
    "draw-trend-lines", "trendlines-101", "trendlines-djia", "along-the-bands",
    "support-and-resistance", "price-levels",
    # breakouts
    "how-breakouts-work", "breakouts-and-breakout-failures",
    # momentum / indicateurs
    "what-is-momentum", "putting-momentum", "is-vwap-useful", "overbought-oversold",
    "how-to-learn-about-indicators", "market-stress-index", "from-noise-to-signal",
    # fibonacci
    "whats-wrong-fibonacci", "testing-fibonacci", "fibonacci-thinking-deeper",
    "fibonacci-conclusions",
    # correlations / intermarche
    "careful-with-correlations", "correlated-risk", "intermarket-scatterplots",
    "relative-performance", "four-reasons", "using-spread-charts",
    # risk management
    "know-your-risk", "six-keys", "cutting-losses", "position-size-matters",
    "riskreward", "trailing-stops", "adding-to-positions", "trade-exits",
    "short-volatility", "slippage", "futures-rolls",
    # quant / backtest
    "quant-101", "quant-primer", "common-sense-checks", "backtesting-in-excel",
    "how-to-backtest", "trading-edge", "bad-statistics", "law-of-small-numbers",
    "what-are-the-odds", "market-stats", "streaks", "when-percents-fail",
    "understanding-returns", "human-vs-machine", "co-authored-paper",
    # intraday / saisonnalite
    "map-the-trading-day", "intraday-tendencies", "activity-by-time-of-day",
    "currencies-time-of-day", "daytrading-sp-500-structure", "roadmap-for-the-trading-day",
    "post-big-down-day", "seasonality", "paid-to-hold-overnight",
    # setups / divers
    "avoid-some-losses", "avoid-bad-trades", "good-setups-go-bad", "gap-and-go",
    "gaps-and-context", "managing-gap-openings", "multi-timeframe", "thinking-in-categories",
    "manipulation", "liquidity", "reader-question-volume", "sigmaspikes-ethereum",
]

matched, report = {}, []
for fr in FRAGMENTS:
    hits = [s for s in slugs if fr in s]
    report.append((fr, hits))
    for h in hits:
        matched[h] = True

garde = sorted(matched)
with open("queue_adamgrimes.tsv", "w", encoding="utf-8") as f:
    for s in garde:
        f.write(f"https://www.adamhgrimes.com/{s}/\t{re.sub(r'[^a-z0-9]+','_',s)[:60].strip('_')}\n")

zero = [fr for fr, h in report if not h]
multi = [(fr, len(h)) for fr, h in report if len(h) > 3]
print(f"posts sitemap : {len(slugs)} | fragments : {len(FRAGMENTS)} | articles matches (uniques) : {len(garde)}")
print(f"fragments SANS match ({len(zero)}) : {zero}")
print(f"fragments TROP larges >3 ({len(multi)}) : {multi}")
