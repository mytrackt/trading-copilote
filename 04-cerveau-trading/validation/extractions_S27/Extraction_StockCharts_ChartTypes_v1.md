# Extraction StockCharts — Chart Types (page index)

**Source :** `bundles/stockcharts/chart_types.md` (HTTP 200 · ~3 771 car.) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées (.md=0 figures vs HTML=0 images)
**Décisions :** D1271 → D1276 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

> **NATURE DE LA PAGE :** page d'INDEX (liste de 12 types de graphiques avec une phrase de description chacun). Aucun contenu opératoire. NON PADDÉ — chaque décision regroupe ce qui est littéralement présent. Pages dédiées (Renko, Heikin-Ashi, etc.) hors bundle.

## INVENTAIRE IMAGES CERTIFIÉES
Aucune image certifiée (manifest : .md=0 figures vs HTML=0 images — alignement impossible).

## DÉCISIONS

### D1271 — Types fusionnant prix et volume (CandleVolume / Arms / EquiVolume)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « Arms CandleVolume : merges traditional candlesticks with EquiVolume boxes » · « CandleVolume : merges traditional candlesticks with volume » · « EquiVolume : Price boxes that are sized based on their trading volume ».
**TRADEX-AI C2** : Familles de graphiques qui encodent le volume dans la géométrie de la bougie/box. Pertinent pour le cercle order flow (C2) — alternative visuelle au footprint ATAS pour repérer les pics de volume sur GC·HG·CL·ZW.
*Catégorie : indicateurs_tendance*

---

### D1272 — Elder Impulse System (coloration des barres par signaux)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « Elder Impulse System : A charting system developed by Alexander Elder that colors price bars based on simple technical signals. »
**TRADEX-AI C1** : Système de coloration de barres selon des signaux techniques combinés (tendance + momentum). Concept de filtre directionnel visuel ; à rapprocher des indicateurs de tendance du moteur.
*Catégorie : indicateurs_tendance*

---

### D1273 — Heikin-Ashi (bougies lissées sur deux périodes)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « Heikin-Ashi : A candlestick method that uses price data from two periods instead of one. »
**TRADEX-AI C1** : Méthode de lissage des bougies réduisant le bruit pour mieux visualiser la tendance. Utile comme couche de confirmation de direction, mais introduit un décalage (deux périodes) — à noter pour le réglage des timeframes.
*Catégorie : indicateurs_tendance*

---

### D1274 — Graphiques japonais filtrant le temps (Kagi, Renko, Three Line Break)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « Kagi : based on volatility and reversal amounts » · « Renko : boxes rise and fall in 45-degree patterns » · « Three Line Break : ignores time and only represents change in terms of price movements ».
**TRADEX-AI C1** : Famille de graphiques basés sur le mouvement de prix (volatilité/seuil de renversement) et non sur le temps. Cohérent avec l'usage des range bars NT8 du projet (Phase C) : filtrent le bruit temporel pour la lecture de structure.
*Catégorie : structure_marche*

---

### D1275 — Outils de scan/visualisation de groupes (MarketCarpets, RRG)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « MarketCarpets : visually scan large groups of securities » · « Relative Rotation Graphs (RRG) : A visualization tool for relative strength and momentum analysis. »
**TRADEX-AI C7** : Outils de force relative / rotation inter-marché. Concept pertinent pour le cercle corrélations (C7) — visualiser la force relative entre GC/HG/CL/ZW/ES/VX.
*Catégorie : structure_marche*

---

### D1276 — Outils macro / cycle (Seasonality, Yield Curve)
🟢 **FAIT VÉRIFIÉ** (Source : chart_types.md) : « Seasonality Charts : identifying monthly seasonal patterns » · « Yield Curve : using bond yields to analyze market conditions and the economic cycle. »
**TRADEX-AI C4** : Outils de lecture saisonnière et de cycle économique (courbe des taux). Pertinents pour le cercle macro (C4) — contexte de cycle pour GC·HG·CL·ZW, complément du suivi DX/Fed.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Sujet | Cercle | Catégorie | Tag |
|------|-------|--------|-----------|-----|
| D1271 | Prix+volume (CandleVolume/EquiVolume) | C2 | indicateurs_tendance | 🟢 |
| D1272 | Elder Impulse System | C1 | indicateurs_tendance | 🟢 |
| D1273 | Heikin-Ashi | C1 | indicateurs_tendance | 🟢 |
| D1274 | Kagi/Renko/3-Line-Break (sans temps) | C1 | structure_marche | 🟢 |
| D1275 | MarketCarpets / RRG (force relative) | C7 | structure_marche | 🟢 |
| D1276 | Seasonality / Yield Curve (macro) | C4 | structure_marche | 🟢 |

**Lien Belkhayate :** NON CONCERNÉ explicitement. NOTE ⚫🔴 : la famille Renko/range bars (D1274) recoupe l'usage range bars NT8 du projet, mais aucun lien Belkhayate n'est affirmé par la source (NON VÉRIFIÉ — ne pas inventer).
**Images :** 0/0. **Cas à vérifier :** aucun (page index, 6 décisions, non paddée).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
