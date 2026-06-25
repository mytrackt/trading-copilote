# Extraction StockCharts — Moving Average Trading Strategies
**Source :** `bundles/stockcharts/moving_average_trading_strategies.md` (HTTP 200 · ~8 594 car.) + 0 image certifiée
**Méthode images :** double ancrage · 0/0 certifiées (manifest : alignement impossible .md=0 vs HTML=0 → à vérifier manuellement)
**Décisions :** D2691 → D2701 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
Aucune image certifiée. (Manifest : intégrité .md=0 figures vs HTML=0 images → alignement impossible, à vérifier manuellement. Aucune image n'est citée dans cette extraction.)

## DÉCISIONS

### D2691 — Trois familles de stratégies de moyennes mobiles
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « Three ways to trade with moving averages are moving average crossovers, support & resistance levels, and moving average ribbons. (…) Crossovers can help identify entry and exit points. Support and resistance levels help identify turning points in trends. »
**TRADEX-AI C1** : Cadre de trois usages des MM (croisements, support/résistance, rubans) à cabler dans la lecture de tendance du cercle C1 sur GC/HG/CL/ZW. Chaque famille devient un module de signal distinct.
*Catégorie : indicateurs_tendance*
---

### D2692 — Justification : analyse simplifiée du bruit de marché
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « Moving averages can help eliminate market noise, making it easier to interpret and analyze market direction. »
**TRADEX-AI C1** : Les MM servent de filtre de bruit pour stabiliser la lecture de direction ; utiliser comme lissage avant l'évaluation de tendance, pas comme déclencheur seul.
*Catégorie : indicateurs_tendance*
---

### D2693 — Support/résistance dynamiques et adaptatifs
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « Moving averages dynamically adjust based on new price data. This makes support and resistance more fluid and adaptable to changing market conditions. »
**TRADEX-AI C1** : MM comme support/résistance dynamique, à distinguer des pivots Belkhayate statiques (PP + Gan + clôture veille). Niveau mobile complémentaire, non substitut aux pivots.
*Catégorie : structure_marche*
---

### D2694 — Repère visuel de force de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « Moving averages, in relation to price or other moving averages (e.g., ribbons), can provide a graphical representation of trend direction and strength. »
**TRADEX-AI C1** : L'écart prix/MM et MM/MM encode la force de tendance — exploitable comme variable de pondération dans la grille /10 (renfort de direction C1).
*Catégorie : indicateurs_tendance*
---

### D2695 — Croisement prix/MM : signal directionnel de base
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « When the price crosses above a moving average, it could be bullish. When price moves below a moving average, it could be considered a bearish signal. But a lot depends on what moving average you use and if that price crossover is a follow-through move. »
**TRADEX-AI C1** : Croisement prix/MM = signal directionnel conditionnel — exige un « follow-through » (confirmation de suivi) avant validation. Garde-fou : ne pas trader le croisement brut.
*Catégorie : signal*
---

### D2696 — Aligner le croisement avec la tendance majeure
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « "The trend is your friend until it bends." Based on this premise, you could combine a price crossover with the major trend so your trading aligns with the trend. »
**TRADEX-AI C1** : Filtrer les croisements prix/MM par la tendance majeure (MM longue) — n'accepter que les signaux dans le sens de la tendance dominante. Critère de cohérence directionnelle.
*Catégorie : signal*
---

### D2697 — Croisement de moyennes mobiles (50/100)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « Moving average crossovers occur when one moving average crosses another. Say you have a 50-day simple moving average (SMA) and a 100-day SMA overlaid on your price chart. »
**TRADEX-AI C1** : Croisement deux-MM (ex. 50/100 SMA) = signal de changement de régime de tendance. Codable de façon déterministe ; paramètres de périodes à figer (cf. règle COGParams projet).
*Catégorie : indicateurs_tendance*
---

### D2698 — Golden Cross / Death Cross
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « A bullish crossover is when the shorter moving average crosses above the longer one (…) called a Golden Cross. A bearish crossover, or a Death Cross, is when the shorter moving average crosses below the longer SMA. »
**TRADEX-AI C1** : Golden Cross (haussier) / Death Cross (baissier) = croisements MM courte/MM longue nommés. À traiter comme régime de fond, non comme déclencheur d'entrée immédiat (signal retardé).
*Catégorie : signal*
---

### D2699 — Croisement 5-8-13 EMA pour le court terme
🔵 **ÉCOLE** (Source : moving_average_trading_strategies.md) : « Moving average crossovers can also be used for short-term trading. The 5-8-13 EMA crossover is a popular strategy among short-term traders. The crossovers between the three exponential moving averages (EMAs) can indicate price moves in the near term. »
**TRADEX-AI C1** : Triplet EMA 5-8-13 = approche court terme, pertinente pour le mode Rapide (Range Bar) / Scalping Belkhayate. Réactivité accrue au prix du carré de l'EMA courte.
*Catégorie : indicateurs_tendance*
---

### D2700 — MM comme support/résistance (rebond du prix)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « You may notice that prices often bounce off a moving average. The moving average is acting as a support level. Sometimes, prices are reluctant to move beyond a moving average. That's when a moving average acts as a resistance level. Traders often use the levels to identify entry and exit points. »
**TRADEX-AI C1** : Rebond/rejet sur MM = zone d'entrée/sortie dynamique. Combiner avec pivots Belkhayate pour confluence (MM + pivot statique aligné = renfort de score).
*Catégorie : gestion_risque_entree*
---

### D2701 — Rubans de moyennes mobiles (ribbons) et Guppy
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_trading_strategies.md) : « You can use Moving Average Ribbons to identify long and short-term trend direction, trend strength, and trend reversals. The width of the ribbon (…) the distance between the moving averages, also helps to identify trend strength, the end of a trend, and the beginning of a trend. (…) The Guppy Multiple Moving Average is a popular method which combines 12 exponential moving averages. »
**TRADEX-AI C1** : Largeur de ruban = force de tendance ; ruban qui s'élargit = tendance en accélération, qui se resserre = essoufflement. Le Guppy (12 EMA) est une variante. Exploitable comme proxy de momentum directionnel C1.
*Catégorie : indicateurs_tendance*
---

## SYNTHÈSE
| Champ | Valeur |
|-------|--------|
| Décisions ajoutées | 11 (D2691 → D2701) |
| Images citées | 0/0 certifiées (manifest : alignement impossible → à vérifier manuellement) |
| Catégories | indicateurs_tendance, structure_marche, signal, gestion_risque_entree |
| Tags | 🟢 FAIT VÉRIFIÉ ×9 · 🔵 ÉCOLE ×2 |
| Cercle dominant | C1 (prix / tendance) |
| Belkhayate | Aucun lien affirmé par la source. Rapprochement possible « MM support/résistance dynamique vs pivots statiques Belkhayate » (D2693, D2700) ⚫🔴 hypothèse projet, non affirmée par la source. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, NON fusionnée dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur.
