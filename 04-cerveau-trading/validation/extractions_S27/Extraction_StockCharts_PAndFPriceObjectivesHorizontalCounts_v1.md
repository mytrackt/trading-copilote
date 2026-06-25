# Extraction StockCharts — P&F Price Objectives : Horizontal Counts

**Source :** `bundles/stockcharts/p_and_f_price_objectives_horizontal_counts.md` (HTTP 200 · ~15 228 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D2931 → D2950 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-horizontal-counts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | A Quadruple Top marked a congestion pattern in this P&F chart | Congestion Patterns | CERTIFIE |
| image_02.png | Spread Triple Bottom Breakdowns mark a congestion area | Congestion Patterns | CERTIFIE |
| image_03.png | Measuring pattern width after a spread Triple Bottom Breakdown | Classic Patterns | CERTIFIE |
| image_04.png | Bullish reversal pattern and a bearish continuation congestion pattern | Extended Congestions | CERTIFIE |
| image_05.png | An example of a congestion pattern in a P&F chart | Extended Congestions | CERTIFIE |
| image_06.png | Example of a chart with bearish and bullish continuation congestion patterns | Extended Congestions | CERTIFIE |
| image_07.png | Signal Frequency | Signal Frequency [SECTION-FALLBACK] | CERTIFIE |

## DÉCISIONS

### D2931 — Principe du comptage horizontal
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « Point & Figure (P&F) price objectives can be determined using the horizontal count method with a consolidation or congestion pattern. This counting method is based on the width of the congestion pattern. The wider the congestion pattern, the higher the price objective upon the pattern break. »
**TRADEX-AI C1** : Objectif de prix dérivé de la LARGEUR d'une congestion P&F (plus large = objectif plus élevé) — méthode de projection complémentaire au comptage vertical.
*Catégorie : structure_marche*

---

### D2932 — Fin de congestion = rupture + estimation Extension
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « A congestion pattern ends with a break above the pattern high or below the pattern low. Chartists can then use a simple formula to estimate a price Extension and apply this extension to the consolidation high or low for a Price Objective. »
**TRADEX-AI C1** : La congestion se clôt par une cassure haute/basse ; l'Extension calculée s'applique au haut (cassure baissière) ou au bas (cassure haussière) pour obtenir l'objectif.
*Catégorie : structure_marche*

---

### D2933 — Objectifs = estimations approximatives sans garantie
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « Keep in mind that these Price Objectives are rough estimates based on P&F charting techniques. There is no guarantee that prices will reach the objective. »
**TRADEX-AI C1** : Garde-fou — un objectif horizontal est une estimation grossière, jamais une cible garantie ; ne pas en faire un critère de décision dur.
*Catégorie : gestion_risque_entree*

---

### D2934 — Patterns qualifiant comme congestion
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « These include Triple Top Breakouts and Triple Bottom Breakdowns, Spread Triple Top Breakouts and Spread Triple Bottom Breakdowns as well as Quadruple Top Breakouts and Quadruple Bottom Breakdowns. These classic P&F patterns clearly mark a congestion period that ends with a subsequent support or resistance break. »
**TRADEX-AI C1** : Patterns éligibles au comptage horizontal — Triple/Spread Triple/Quadruple Top et Bottom — qui délimitent une période de congestion close par une cassure.
*Catégorie : configuration*

---

### D2935 — Exemple Quadruple Top (JP Morgan)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_01) : « The chart below shows JP Morgan with a Quadruple Top Breakout in the upper right-hand corner. This Quadruple Top marked a congestion pattern as prices moved sideways from June (red 6) to December (red C). Notice that three reaction highs established a clear resistance level broken with the current column of X's. »
**TRADEX-AI C1** : Un Quadruple Top = mouvement latéral avec trois sommets de réaction formant une résistance claire, cassée par la colonne de X courante.
*Catégorie : configuration*

---

### D2936 — Spread Triple Bottom Breakdown (Equinix)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_02) : « The chart below shows Equinix (EQIX) with a pair of Spread Triple Bottom Breakdowns. This is just a Triple Bottom with a couple extra columns that spread the pattern a little wider. (...) EQIX broke Spread Triple Bottom support with a move below the prior two columns of O's. »
**TRADEX-AI C1** : Un Spread Triple Bottom = Triple Bottom avec colonnes supplémentaires l'élargissant ; la cassure se fait sous les deux colonnes de O précédentes.
*Catégorie : configuration*

---

### D2937 — Critères minimaux d'une congestion non classique
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « There needs to be a definable congestion pattern that is at least five columns wide and a column that breaks this congestion. A clear support or resistance level should also be visible. The congestion ends when a column breaks above resistance or below support. Once broken, the width of the congestion is fixed and chartists can start the counting process. »
**TRADEX-AI C1** : Congestion valide = au moins 5 colonnes de large + niveau support/résistance net + colonne de cassure ; la largeur se fige à la cassure puis on compte.
*Catégorie : structure_marche*

---

### D2938 — Largeur du Triple Top Breakout = 5 colonnes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « A Triple Top Breakout, for example, consists of five columns—three columns of X's and two columns of O's. The first two X columns establish Triple Top resistance, and the intervening O columns represent the two pullbacks. The third column of X's forges the breakout. »
**TRADEX-AI C1** : Largeur de comptage d'un Triple Top = 5 colonnes (3 X + 2 O) ; le 3e X réalise la cassure.
*Catégorie : structure_marche*

---

### D2939 — Formule de l'Extension horizontale
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « Once the breakout occurs, multiply the pattern width by the box size and the reversal amount to estimate the price extension. This extension is then added to the low of the pattern for a target. »
**TRADEX-AI C1** : Extension horizontale = largeur du pattern × taille de boîte × montant de retournement ; ajoutée au bas du pattern pour cible haussière.
*Catégorie : structure_marche*

---

### D2940 — Exemple chiffré baissier (Chevron, largeur 7)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_03) : « The width of this pattern is seven columns (...). The width (7) is multiplied by the box size (1) and the reversal amount (3) for a projected Extension (7 x 1 x 3 = 21). This Extension is subtracted from the high of the pattern for a bearish Price Objective (69 - 21 = 48). »
**TRADEX-AI C1** : Cas baissier — Extension = 7×1×3 = 21, soustraite du haut (69) → objectif 48. La cassure de support fige la largeur (elle ne change plus après).
*Catégorie : structure_marche*

---

### D2941 — Variante 2/3 d'A.W. Cohen pour objectifs baissiers
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « As with the vertical count, some schools of thought only use 2/3 of the projected Extension for bearish Price Objectives. A.W. Cohen, a pioneer in P&F charting, advocated a 2/3 Extension for bearish counts. This probably has something to do with the bullish nature of stocks. »
**TRADEX-AI C1** : 🟡 CONVENTION — certaines écoles (A.W. Cohen) n'utilisent que 2/3 de l'Extension pour les objectifs baissiers, par biais haussier structurel des actions.
*Catégorie : structure_marche*

---

### D2942 — Exemple chiffré haussier (Triple Top, largeur 5)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « The width of the pattern (5) is multiplied by the box size (1) and the reversal amount (3) for an Extension estimate (5 x 1 x 3 = 15). This amount is then added to the low of the column for a bullish Price Objective (80 + 15 = 95). »
**TRADEX-AI C1** : Cas haussier — Extension = 5×1×3 = 15, ajoutée au bas (80) → objectif 95.
*Catégorie : structure_marche*

---

### D2943 — Comptage des congestions étendues
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « Counts for extended congestions include the column leading in, the actual congestion pattern, and a column leading out. Also, note that some P&F practitioners include the columns leading in with the classic reversal patterns (...) thus making the estimated Extension a little larger. »
**TRADEX-AI C1** : Congestion étendue = colonne d'entrée + congestion + colonne de sortie incluses dans le comptage ; certains incluent aussi l'entrée pour les patterns classiques (Extension un peu plus grande).
*Catégorie : structure_marche*

---

### D2944 — Les quatre types de congestions étendues
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « 1. A bullish reversal forms with a decline, congestion base, and an upside reversal breakout. 2. A bearish reversal that forms with an advance, congestion top, and reversal breakdown. 3. A bullish continuation (...) advance, congestion pattern, and continuation breakout to the upside. 4. A bearish continuation forms with a decline, congestion pattern, and continuation break to the downside. »
**TRADEX-AI C1** : 4 types — reversal haussier, reversal baissier, continuation haussière, continuation baissière — chacun défini par mouvement d'entrée + congestion + cassure.
*Catégorie : configuration*

---

### D2945 — Sens des colonnes lead-in / lead-out (reversals)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « For the two reversal patterns, the column leading into the congestion and the column leading out will be in different directions. A bullish reversal forms with a column of O's leading in (decline), a congestion base, and a column of X's leading out that breaks congestion resistance. »
**TRADEX-AI C1** : Pour les reversals, colonnes d'entrée et de sortie de directions OPPOSÉES (ex : reversal haussier = O en entrée, X en sortie).
*Catégorie : configuration*

---

### D2946 — Exemple reversal haussier étendu (Coca-Cola, largeur 18)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_04) : « The congestion extends for 16 columns, ending with the breakout column leading out. All told, the width is 18 columns, which is exceptionally long. Using the formula above, the Price Objective would be 90 (18 x 1 x 3 = 54, 36 + 54 = 90). Again, take these price objectives with a grain of salt and employ other aspects of technical analysis for confirmation. »
**TRADEX-AI C1** : Largeur 18 (16 congestion + entrée + sortie) → Extension 54, objectif 90. Garde-fou réaffirmé : prudence + confirmation par autre analyse technique.
*Catégorie : structure_marche*

---

### D2947 — Reversal baissier étendu et option 2/3 (State Street)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_05) : « Congestion support was broken when the column of O's exited the pattern to fix the width at eight (one column leading in, six for the congestion, and one column leading out). (...) A full Extension targets a move to 31. A 2/3 Extension targets a move to 39. »
**TRADEX-AI C1** : Reversal baissier largeur 8 (1 entrée + 6 congestion + 1 sortie) ; Extension pleine → 31, Extension 2/3 → 39.
*Catégorie : structure_marche*

---

### D2948 — Sens des colonnes lead-in / lead-out (continuations)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_06) : « The lead-in and lead-out columns for continuation patterns are in the same direction. A bullish continuation consists of an advance with a column of X's leading in, a congestion, and an upside breakout (...). A bearish continuation consists of a decline with a column of O's leading in, a congestion, and a continuation lower with a congestion support break. »
**TRADEX-AI C1** : Pour les continuations, colonnes d'entrée et de sortie de MÊME direction (haussière = X/X, baissière = O/O).
*Catégorie : configuration*

---

### D2949 — Fréquence des signaux et tailles de boîte
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md, image_07) : « Securities priced from 5.01 to 20 have 50-cent boxes, and securities priced from 20.01 to 100 have $1 boxes. (...) If you prefer looking for more signals, try smaller box sizes and using intraday price data, such as 60-minute data. A 20–50 cent box size with 60-minute data works well for the three to six months. »
**TRADEX-AI C1** : Tailles de boîte standard par prix (0,50 pour 5-20 ; 1 pour 20-100) ; boîtes plus petites + données intraday 60 min = plus de signaux sur 3-6 mois.
*Catégorie : configuration*

---

### D2950 — Évaluation du risque et objectifs irréalistes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_horizontal_counts.md) : « For bullish patterns and upside price objectives, a move below support or the pattern low would negate a breakout. The box below the pattern low often marks the worst-case level for a pattern failure. (...) horizontal counts that produce negative Price Objectives are best ignored. (...) a Price Objective that forecasts a 300% advance should also be taken with a grain of salt. »
**TRADEX-AI C1** : Niveau d'invalidation = boîte sous le bas (haussier) / au-dessus du haut (baissier) du pattern, marquant le pire-cas. Ignorer objectifs négatifs ou aberrants (ex : +300 %).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D2931 → D2950 |
| Nb décisions | 20 |
| Images certifiées | 7/7 |
| Cas à vérifier | 0 |
| Cercle TRADEX-AI | C1 (structure P&F) |
| Catégories | structure_marche · configuration · gestion_risque_entree |
| Tags dominants | 🟢 FAIT VÉRIFIÉ · 🟡 CONVENTION (D2941) |
| Lien Belkhayate | NON CONCERNÉ (P&F hors méthode Belkhayate) |
| Actifs | GC · HG · CL · ZW (objectif éducatif uniquement) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, non fusionné dans KNOWLEDGE_BASE_MASTER.json.
