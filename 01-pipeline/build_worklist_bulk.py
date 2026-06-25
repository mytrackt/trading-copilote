# -*- coding: utf-8 -*-
"""Liste de travail BULK : bundles a extraire (hors prioritaires + doublons master).
Sortie : worklist_bulk.tsv  ->  source<TAB>nom<TAB>chemin_md  (par source, trie)
"""
import os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bundles")
SOURCES = ["stockcharts", "adamgrimes", "ninjatrader", "optimusfutures", "sierrachart", "cftc"]

# Deja extraits en master (sessions precedentes) + tests
EXCL = {
    "moving_averages", "moving_averages_test", "rsi", "rsi_test", "macd", "macd_test",
    "adx", "candlestick_bullish", "candlestick_bearish", "wyckoff",       # stockcharts doublons
    "footprint",                                                          # optimus doublon
    "volume_profile_shapes",                                             # ninjatrader doublon
    "trend_gold",                                                        # adamgrimes doublon
    "cot_explanatory",                                                   # cftc doublon
    # prioritaires deja extraits S27 :
    "money_flow_index_mfi", "pivot_points", "volume_weighted_average_price_vwap",
    "anchored_vwap", "volume_by_price", "put_call_ratio", "volatility_indices",
    "intermarket_analysis", "cme_futures_and_spot_prices",
    "order_flow_indicators", "what_is_cumulative_delta_in_order_flow_trading",
    "what_is_volume_weighted_average_price_vwap",
    "numbers_bars_footprint", "sierra_141_volume_by_price", "sierra_292_cumulative_delta_volume",
}

rows, par_source = [], {}
for src in SOURCES:
    d = os.path.join(BASE, src)
    if not os.path.isdir(d):
        continue
    noms = sorted(f[:-3] for f in os.listdir(d)
                  if f.endswith(".md") and not f.endswith("_test.md"))
    keep = [n for n in noms if n not in EXCL]
    par_source[src] = len(keep)
    for n in keep:
        rows.append((src, n, os.path.join(d, n + ".md")))

with open(os.path.join(os.path.dirname(__file__) or ".", "worklist_bulk.tsv"), "w", encoding="utf-8") as f:
    for src, n, p in rows:
        f.write(f"{src}\t{n}\t{p}\n")

print("RESTANT A EXTRAIRE (bulk) par source :")
for s in SOURCES:
    print(f"  {par_source.get(s,0):4d}  {s}")
print(f"  ----")
print(f"  {len(rows):4d}  TOTAL")
