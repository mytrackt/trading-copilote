# Extraction StockCharts — P&F Price Objectives : Vertical Counts

**Source :** `bundles/stockcharts/p_and_f_price_objectives_vertical_counts.md` (HTTP 200 · ~12 898 car.) + 0 image certifiée
**Méthode images :** double ancrage v3 — INTÉGRITÉ ÉCHOUÉE (.md=5 figures vs HTML=6 images) · 0/6 certifiées · alignement impossible → **aucune image citée**, texte exploitable uniquement
**Décisions :** D2951 → D2970 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-vertical-counts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée. Le manifest signale une rupture d'intégrité (5 figures dans le .md contre 6 images en HTML — désalignement). Conformément à la consigne, AUCUNE image n'est citée ; seul le texte exploitable est extrait.

## DÉCISIONS

### D2951 — Principe du comptage vertical
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Point & Figure (P&F) price objectives can be determined using the vertical count method, which is based on the length of an important column. This can be the column that triggers a breakout or one that forges an important high or low. »
**TRADEX-AI C1** : Objectif vertical dérivé de la LONGUEUR d'une colonne importante (cassure, ou sommet/creux majeur) — par opposition au comptage horizontal basé sur la largeur.
*Catégorie : structure_marche*

---

### D2952 — Objectifs = estimations approximatives sans garantie
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Once the column is complete, you can apply a simple formula to estimate an Extension and then apply this extension to the column high or low for a Price Objective. These Price Objectives are rough estimates based on P&F charting techniques. There is no guarantee prices will reach the objective. »
**TRADEX-AI C1** : Garde-fou — l'objectif vertical reste une estimation grossière sans garantie d'atteinte ; jamais un critère de décision dur.
*Catégorie : gestion_risque_entree*

---

### D2953 — Choix de la Count Column (colonne de comptage)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « The first step is to choose the column in which to base the count, which we will call the Count Column. (...) this column should signal some type of reversal or continuation move with an upside or downside breakdown. »
**TRADEX-AI C1** : La Count Column doit être significative — elle signale un retournement ou une continuation avec cassure haut/bas. Premier pas du comptage vertical.
*Catégorie : structure_marche*

---

### D2954 — Signaux de base établissant la Count Column
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Double Top Breakouts and Double Bottom Breakdowns are the most basic P&F signals required to establish a Count Column. »
**TRADEX-AI C1** : Les Double Top Breakout / Double Bottom Breakdown sont les signaux minimaux pour fonder une Count Column.
*Catégorie : configuration*

---

### D2955 — Liste des Bullish Breakouts utilisables
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Bullish Breakouts. Ascending Triple Top, Bear Trap, Bearish Signal Reversal, Bullish Catapult, Bullish Triangle, Quadruple Top, Spread Triple Top, Triple Top »
**TRADEX-AI C1** : Patterns haussiers pouvant fonder une Count Column — Ascending Triple Top, Bear Trap, Bearish Signal Reversal, Bullish Catapult, Bullish Triangle, Quadruple Top, Spread Triple Top, Triple Top.
*Catégorie : configuration*

---

### D2956 — Liste des Bearish Breakdowns utilisables
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Bearish Breakdowns. Bearish Catapult, Bearish Triangle, Bull Trap, Bullish Signal Reversal, Descending Triple Bottom, Quadruple Bottom, Spread Triple Bottom, Triple Bottom »
**TRADEX-AI C1** : Patterns baissiers pouvant fonder une Count Column — Bearish Catapult, Bearish Triangle, Bull Trap, Bullish Signal Reversal, Descending Triple Bottom, Quadruple Bottom, Spread Triple Bottom, Triple Bottom.
*Catégorie : configuration*

---

### D2957 — Complétion de la Count Column par retournement 3 boîtes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « The number of filled boxes in a column is not fixed until there is a 3-box reversal. Keep in mind that a column of X's is subject to change until a 3-box reversal forms with three O's in a new column. Once this column is reversed, the number of boxes is fixed, and you can set the count in motion. »
**TRADEX-AI C1** : La longueur de la Count Column ne se fige qu'après un retournement de 3 boîtes (3 O après X, ou 3 X après O) — condition pour démarrer le comptage.
*Catégorie : structure_marche*

---

### D2958 — Comptes préliminaires modifiables
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « You can, however, make preliminary Column Counts based on the initial breakout. Remember, these Price Objectives are subject to change until the Count Column is fixed with a 3-box reversal. »
**TRADEX-AI C1** : Garde-fou — un comptage avant figement (3-box reversal) est PRÉLIMINAIRE et susceptible de changer ; ne pas le traiter comme définitif.
*Catégorie : gestion_risque_entree*

---

### D2959 — Formule de l'Extension verticale
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « This count is multiplied by the box size and the reversal amount to define the Extension. For example, a column of 10 X's on a 1 x 3 P&F chart would yield 30 (10 x 1 x 3 = 30). Remember, a 1 x 3 chart implies 1 point per box and 3 boxes for a reversal. »
**TRADEX-AI C1** : Extension verticale = nombre de boîtes de la colonne × taille de boîte × montant de retournement (ex : 10×1×3 = 30 sur un graphique 1×3).
*Catégorie : structure_marche*

---

### D2960 — Application haussière de l'Extension
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « For bullish breakouts, you would add the projected Extension (30) to the low of the Count Column to attain an upside target. In the chart below, the fixed Count Column measures 14 boxes. Each box is 0.50, and the reversal amount is 3. The total Extension is 21 (14 x 0.5 x 3 = 21). This amount is added to the low of the column for an upside target. »
**TRADEX-AI C1** : Cassure haussière — Extension ajoutée au BAS de la Count Column (ex : 14×0,5×3 = 21 ajouté au bas).
*Catégorie : structure_marche*

---

### D2961 — Application baissière de l'Extension (Computer Sciences)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « For bearish breakdowns, the total is subtracted from the high of the Count Column (...). Notice that this column became fixed at 14 when the stock rebounded to 47 with a column of X's. The length multiplied by the box size (0.50) and reversal amount (3) gives us the Extension (21). Subtracting this number from the high of the Count Column yields a downside Price Objective of 29. (...) Tom Dorsey advocates using 2/3 of the reversal amount (...) which yields a downside target of 36. »
**TRADEX-AI C1** : Cassure baissière — Extension soustraite du HAUT de la Count Column (14×0,5×3 = 21 → objectif 29) ; variante Dorsey 2/3 → 36.
*Catégorie : structure_marche*

---

### D2962 — Variante 2/3 de Tom Dorsey (objectifs baissiers)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « In his book Point & Figure Charting, Tom Dorsey advocates a smaller multiplier for bearish Price Objectives. (...) Dorsey's method multiplies the Count Column by the box size and then by 2/3 of the reversal amount, which would be 2 for a 3-box reversal chart. The total Extension is then subtracted from the value of the box at the top of the Count Column. »
**TRADEX-AI C1** : 🟡 CONVENTION — méthode Dorsey : pour les objectifs baissiers, multiplicateur réduit (2/3 du retournement, soit 2 sur graphique 3-box). C'est la méthode utilisée par StockCharts.com pour les comptes verticaux baissiers.
*Catégorie : structure_marche*

---

### D2963 — Point d'activation de du Plessis
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « In his book, The Definitive Guide to Point & Figure, Jeremy du Plessis suggests establishing an activation point for vertical counts. Once the Count Column is completed, you should use the high of that column as the activation point for an Upside Extension. A break above this high activates the count, which makes it valid. Conversely, the low of the Count Column becomes the activation point for a downside Extension. »
**TRADEX-AI C1** : 🔵 ÉCOLE (du Plessis) — un comptage n'est VALIDE qu'après franchissement d'un point d'activation : haut de la Count Column (haussier) / bas (baissier).
*Catégorie : gestion_risque_entree*

---

### D2964 — Colonnes verticales significatives hors pattern (du Plessis)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « du Plessis also suggests that vertical counts can be made from any vertical column that forges an important high/low or marks the first move from a significant peak/trough. This could be an exceptionally long column that is not part of a breakout, breakdown, or reversal pattern. High-pole patterns could also be considered significant columns for a vertical count. »
**TRADEX-AI C1** : 🔵 ÉCOLE (du Plessis) — le comptage vertical peut partir de toute colonne longue marquant un sommet/creux majeur, même hors pattern de cassure ; les High-pole comptent aussi.
*Catégorie : configuration*

---

### D2965 — Point de départ du comptage : Cohen vs Dorsey
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « A.W. Cohen, an early pioneer in P&F charting, advocated starting a count from the high or low of the pattern. Tom Dorsey advocates applying the Extension to the high or low of the Count Column, which is the method used at StockCharts.com. The difference in these two techniques is often negligible because the difference between the high/low of the pattern and the high/low of the Count Column is usually just one box. »
**TRADEX-AI C1** : 🟡 CONVENTION — divergence d'écoles : Cohen part du haut/bas du PATTERN, Dorsey (et StockCharts) du haut/bas de la COUNT COLUMN ; écart souvent négligeable (≈1 boîte).
*Catégorie : structure_marche*

---

### D2966 — Ajustement quand la taille de boîte change
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Sometimes the box size changes, which requires a counting adjustment. Instead of counting the number of boxes in a column and multiplying by the box size, chartists can simply subtract the column high from the column low. This sum can then be multiplied by the reversal or 2/3 the reversal amount to obtain the Extension estimate. »
**TRADEX-AI C1** : Si la taille de boîte varie dans la colonne — calculer (haut − bas de colonne) puis × retournement (ou 2/3) au lieu de compter les boîtes.
*Catégorie : structure_marche*

---

### D2967 — Trader dans le sens de la tendance (trend lines)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Rising (blue) trend lines are called Bullish Support Lines, and falling (red) trend lines are called Bearish Resistance Lines. (...) Many traders advocate trading in the direction of the underlying trend. This means taking bullish signals when the trend is up and prices are above the Bullish Support Line. Conversely, bearish signals are preferred when the trend is down and prices are below the Bearish Resistance Line. »
**TRADEX-AI C1** : Combiner comptage vertical et lignes de tendance — privilégier signaux haussiers au-dessus de la Bullish Support Line, baissiers sous la Bearish Resistance Line.
*Catégorie : signal*

---

### D2968 — Comptage préliminaire avec trendlines (Agilent)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Notice how the stock broke the Bearish Resistance Line and forged a Quadruple Top Breakout with the move above 30 in the last column of X's. This column is not yet fixed because we have yet to see a 3-box reversal. Price Objectives are preliminary until the column length is fixed. »
**TRADEX-AI C1** : Tant que la colonne n'a pas subi de retournement 3 boîtes, l'objectif reste préliminaire — même après cassure de trendline et Quadruple Top.
*Catégorie : gestion_risque_entree*

---

### D2969 — Évaluation du risque (niveau pire-cas)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « For bullish patterns and upside price objectives, a move below support or the pattern low would negate a breakout. The box below the pattern low often marks the worst-case level for a pattern failure. (...) For bearish patterns or downside price objectives, a move above resistance or the pattern high would negate a breakdown. The box just above the pattern high often marks the worst-case level for a pattern failure. »
**TRADEX-AI C1** : Invalidation — boîte sous le bas (haussier) / au-dessus du haut (baissier) marque le pire-cas ; un Double Bottom/Top contradictoire impose une réévaluation.
*Catégorie : gestion_risque_entree*

---

### D2970 — Objectifs = point de départ, à confirmer
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_vertical_counts.md) : « Price Objectives based on a vertical count, horizontal count, or any other count should always be taken with a grain of salt. (...) A P&F signal and a target are simply the starting point for analysis. Conditions change (...). Employing other technical analysis tools to confirm or refute a premise is also important. For example, chartists can apply basic trend analysis on a bar chart or use bar chart-based indicators to confirm the findings on the P&F chart. »
**TRADEX-AI C1** : Garde-fou final — un objectif (vertical ou horizontal) n'est qu'un point de départ ; surveillance continue + confirmation par d'autres outils (analyse de tendance sur bar chart, indicateurs) obligatoires.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D2951 → D2970 |
| Nb décisions | 20 |
| Images certifiées | 0/6 (intégrité échouée — aucune image citée) |
| Cas à vérifier | 6 images non alignées (.md=5 vs HTML=6) → vérification manuelle |
| Cercle TRADEX-AI | C1 (structure P&F) |
| Catégories | structure_marche · configuration · gestion_risque_entree · signal |
| Tags dominants | 🟢 FAIT VÉRIFIÉ · 🟡 CONVENTION (D2962, D2965) · 🔵 ÉCOLE (D2963, D2964) |
| Lien Belkhayate | NON CONCERNÉ (P&F hors méthode Belkhayate) |
| Actifs | GC · HG · CL · ZW (objectif éducatif uniquement) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, non fusionné dans KNOWLEDGE_BASE_MASTER.json. Images à revérifier manuellement (manifest signale désalignement .md/HTML).
