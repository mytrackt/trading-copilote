# -*- coding: utf-8 -*-
"""Fige les plages D### de tous les bundles bulk (deterministe, reprenable).
Sortie : assignment_bulk.tsv -> idx\tsource\tnom\tchemin\td_start\td_end\tout_filename
D_start = 451 + idx*20. Stable tant que worklist_bulk.tsv ne change pas.
"""
import os
BASE = os.path.dirname(os.path.abspath(__file__))
LABEL = {"stockcharts": "StockCharts", "adamgrimes": "AdamGrimes",
         "ninjatrader": "NinjaTrader", "optimusfutures": "Optimus",
         "sierrachart": "SierraChart", "cftc": "CFTC"}
D0, STEP = 451, 20

rows = [l.split("\t") for l in
        open(os.path.join(BASE, "worklist_bulk.tsv"), encoding="utf-8").read().splitlines() if l.strip()]


def camel(nom):
    parts = [p for p in nom.replace("-", "_").split("_") if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)[:48]


with open(os.path.join(BASE, "assignment_bulk.tsv"), "w", encoding="utf-8") as f:
    for i, (src, nom, path) in enumerate(rows):
        ds = D0 + i * STEP
        de = ds + STEP - 1
        out = f"Extraction_{LABEL[src]}_{camel(nom)}_v1.md"
        f.write(f"{i}\t{src}\t{nom}\t{path}\t{ds}\t{de}\t{out}\n")

print(f"assignment_bulk.tsv : {len(rows)} bundles | D{D0} -> D{D0 + (len(rows)-1)*STEP + STEP - 1}")
