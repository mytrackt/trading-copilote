# Extraction StockCharts — TA 101 Part 5
**Source :** `bundles/stockcharts/ta_101_part_5.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D4251 → D4270 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-5
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : lecture des chandeliers japonais — applicable directement à GC/HG/CL/ZW pour l'identification de la pression acheteuse/vendeuse et des signaux de retournement.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Candlestick Charts | Candlestick Charts | D4251 |
| image_02 | Candlestick Colors | Candlestick Colors | D4255 |
| image_03 | Candlestick Colors | Candlestick Colors | D4257 |
| image_04 | Candlestick Colors | Candlestick Colors | D4258 |
| image_05 | Candlestick Colors | Candlestick Colors | D4259 |
| image_06 | Candlestick Colors | Candlestick Colors | D4261 |

## DÉCISIONS

### D4251 — Chandeliers japonais : plus visuels que OHLC, plus faciles à interpréter
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_01) : Comparés aux graphiques OHLC traditionnels, de nombreux traders considèrent les chandeliers japonais plus visuellement attrayants et plus faciles à interpréter. Chaque chandelier fournit une image facile à déchiffrer de l'action des prix. L'analyste peut comprendre rapidement la relation entre les prix d'ouverture et de clôture ainsi que le plus haut et le plus bas.
**TRADEX-AI C1** : Le dashboard TRADEX utilise des chandeliers pour GC/HG/CL/ZW — justification standard; la lisibilité rapide est critique pour le Mode Manuel où Abdelkrim doit décider vite.
*Catégorie : structure_marche*

### D4252 — Corps creux du chandelier : pression acheteuse
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_01) : Les chandeliers avec des corps creux (hollow bodies) indiquent une pression acheteuse (buying pressure).
**TRADEX-AI C1** : Sur range bars NT8 pour GC/HG/CL/ZW, corps creux = Close > Open = acheteurs dominants sur la barre — signal de continuation haussière si dans le sens de la tendance.
*Catégorie : structure_marche*

### D4253 — Corps plein du chandelier : pression vendeuse
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_01) : Les chandeliers avec des corps pleins (filled bodies) indiquent une pression vendeuse (selling pressure).
**TRADEX-AI C1** : Corps plein sur GC/HG/CL/ZW = Open > Close = vendeurs dominants sur la barre — signal de continuation baissière si dans le sens de la tendance.
*Catégorie : structure_marche*

### D4254 — Longues mèches : retournement intraday, signal de dynamique
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : Des mèches supérieures ou inférieures longues se forment quand le marché se déplace significativement dans une direction particulière pendant la journée puis se retourne avant la fin. Conséquence : des mèches inférieures longues peuvent inférer du bullishness tandis que des mèches supérieures longues peuvent inférer un marché bearish.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, longue mèche inférieure = rejet du bas par les acheteurs → signal haussier potentiel; longue mèche supérieure = rejet du haut par les vendeurs → signal baissier potentiel. Intégrable dans le scoring C1.
*Catégorie : indicateurs_momentum*

### D4255 — Longue mèche inférieure : bullish inference
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_02) : Des mèches inférieures longues peuvent "infer bullishness" — le marché a testé des niveaux bas mais est revenu à la hausse, indiquant que les acheteurs ont absorbé la pression vendeuse.
🟡 **SYNTHÈSE** : C'est l'équivalent chandelier d'un "hammer" (marteau) ou "dragonfly doji" — patterns de retournement haussier bien documentés en AT.
**TRADEX-AI C1** : Longue mèche inférieure sur GC/HG/CL/ZW près d'un pivot Belkhayate = confirmation de support + signal d'entrée LONG potentiel (à confirmer C2 order flow).
*Catégorie : indicateurs_momentum*

### D4256 — Longue mèche supérieure : bearish inference
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : Des mèches supérieures longues peuvent "infer a bearish market" — le marché a testé des niveaux hauts mais est revenu à la baisse, indiquant que les vendeurs ont résisté.
🟡 **SYNTHÈSE** : Équivalent chandelier d'un "shooting star" ou "gravestone doji" — patterns de retournement baissier classiques.
**TRADEX-AI C1** : Longue mèche supérieure sur GC/HG/CL/ZW près d'un pivot Belkhayate = confirmation de résistance + signal d'entrée SHORT potentiel (à confirmer C2 order flow).
*Catégorie : indicateurs_momentum*

### D4257 — Coloration chandelier : règle Close > Open = corps creux
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_03) : Si le prix de clôture est plus haut que le prix d'ouverture, le corps sera affiché creux (hollow).
**TRADEX-AI C1** : Règle de coloration de base — corps creux sur range bar NT8 pour GC/HG/CL/ZW = confirmation visuelle immédiate de barre haussière.
*Catégorie : structure_marche*

### D4258 — Coloration chandelier : règle Close < Open = corps plein rouge, avec exception
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_04) : Si le prix de clôture est inférieur au prix d'ouverture, le corps sera rempli en rouge — AVEC l'exception suivante : si le prix de clôture est plus haut que la clôture du jour précédent, le corps sera rempli en noir.
🟡 **SYNTHÈSE** : Cette exception crée le chandelier "Down Day, Higher Close" (barre noire à corps plein) — un chandelier rare mais significatif.
**TRADEX-AI C1** : L'exception de coloration révèle un gap up en ouverture suivi d'un retournement intraday qui reste au-dessus de la veille — signal d'affaiblissement potentiel à surveiller sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4259 — Coloration mèches et contour : basée sur Close vs clôture précédente
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_05) : Les mèches du chandelier et le contour du corps sont colorés en noir ou rouge selon que le prix de clôture se situe par rapport à la clôture du jour précédent. Close > Close précédente → mèches et contour noirs. Close < Close précédente → mèches et contour rouges.
**TRADEX-AI C1** : Le color-coding des mèches est un signal de momentum inter-séance indépendant du body — une mèche noire longue sur un corps rouge indique que le retournement reste positif par rapport à hier.
*Catégorie : structure_marche*

### D4260 — Up Day Higher Close : greed dominant, buying pressure forte
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : "Up Day, Higher Close" — résulte typiquement d'attentes de prix plus élevés (greed) dépassant les attentes de prix plus bas (fear). La longueur du corps du chandelier indique un achat particulièrement fort.
**TRADEX-AI C5** : La longueur du corps comme proxy de l'intensité de la greed — corps long haussier sur GC dans contexte d'Or safe-haven = signal fort à intégrer dans le scoring C5.
*Catégorie : psychologie*

### D4261 — Down Day Lower Close : fear dominant, selling urgency forte
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md, image_06) : "Down Day, Lower Close" — les attentes de prix plus bas (fear) sont plus fortes que celles de prix plus élevés (greed). Un corps de chandelier plus long infère une plus grande urgence des investisseurs à vendre leurs parts.
**TRADEX-AI C5** : Corps baissier long sur GC/CL = urgence vendeuse — associé à VIX élevé (peur systémique), doublement baissier. Intégrer dans le scoring C5 TRADEX.
*Catégorie : psychologie*

### D4262 — Down Day Higher Close : gap up en ouverture + retournement intraday
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : "Down Day, Higher Close" — un chandelier rare qui commence avec un gap up en prix depuis la clôture du jour précédent mais se termine en baisse pour la journée. Un gap est défini comme une plage de prix où aucun trading n'a lieu, résultat d'un changement significatif de demande (gap up) ou d'offre (gap down) avant que le trading ne commence. Dans ce cas, un achat fort en début de journée s'est retourné mais a quand même clôturé plus haut que la veille.
🟢 **FAIT VÉRIFIÉ** : "C'est un signe baissier quand il survient bien dans un mouvement de prix ascendant."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ce pattern en milieu de tendance haussière = signal d'affaiblissement → déclencher une vérification C2 order flow pour confirmation avant de poursuivre les LONG.
*Catégorie : gestion_risque_entree*

### D4263 — Up Day Lower Close : gap down en ouverture + rebond intraday = bullish en downtrend
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : "Up Day, Lower Close" — un autre chandelier rare qui commence avec un gap down en prix depuis la clôture précédente mais se termine en hausse pour la journée. "Cette action de prix peut être considérée comme haussière pendant un mouvement de prix descendant puisque la forte vente initiale de la journée devient épuisée et que les acheteurs poussent le prix plus haut à la clôture."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en tendance baissière, ce pattern = absorption de la pression vendeuse + rebond → potentiel point de retournement; signal LONG opportuniste à confirmer avec C2 order flow et pivot Belkhayate.
*Catégorie : gestion_risque_entree*

### D4264 — Les chandeliers forment des patterns reconnaissables lors des retournements
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : "Quand l'équilibre entre acheteurs et vendeurs change, les chandeliers forment souvent des patterns reconnaissables signalant le changement. Ces patterns de chandeliers seront discutés dans un article ultérieur."
**TRADEX-AI C1** : La KB Belkhayate (1313 règles) contient des patterns chandelier spécifiques — les 4 cas de base décrits ici (D4260-D4263) sont les briques atomiques de ces patterns composites.
*Catégorie : configuration*

### D4265 — Analyse comparative des 3 types de charts : line / OHLC / candlestick
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : La source présente les 3 types de charts en comparaison visuelle : line chart (direction), OHLC (volatilité + conviction), candlestick (tout + psychologie). Les up/down days sont "readily apparent" avec les chandeliers.
🟡 **SYNTHÈSE** : La progression line → OHLC → candlestick représente une progression dans la densité d'information psychologique encodée visuellement.
**TRADEX-AI C1** : Le dashboard TRADEX doit utiliser les chandeliers comme format principal pour GC/HG/CL/ZW — maximum d'information psychologique visible en un coup d'oeil pour le Mode Manuel.
*Catégorie : structure_marche*

### D4266 — Corps du chandelier : longueur proportionnelle à la conviction directionnelle
🟡 **SYNTHÈSE** (Source : ta_101_part_5.md) : La source mentionne à deux reprises que "la longueur du corps du chandelier indique" l'intensité de l'achat (D4260) ou de la vente (D4261). Un corps long = forte conviction directionnelle; un corps court = faible conviction ou indécision.
**TRADEX-AI C1** : Ratio corps/range total pour GC/HG/CL/ZW : >70% = forte conviction (bon signal), <30% = indécision (signal peu fiable, attendre confirmation). Utilisable comme pondérateur dans le scoring /10 TRADEX.
*Catégorie : indicateurs_momentum*

### D4267 — Mèches et corps : deux informations distinctes sur la même barre
🟡 **SYNTHÈSE** (Source : ta_101_part_5.md) : Corps = bilan de la session (Open vs Close). Mèches = tentatives rejetées dans les deux directions. Les deux ensemble racontent l'histoire complète de la session : où les deux camps ont tenté d'aller et où le consensus a finalement abouti.
**TRADEX-AI C2** : L'order flow ATAS décompose exactement ce que les mèches et le corps encodent visuellement : les mèches = zones d'absorption par le camp opposé (visible dans le footprint), le corps = résultat net du combat acheteurs/vendeurs.
*Catégorie : volume_liquidite*

### D4268 — Indécision du marché : corps court + mèches longues des deux côtés
🟡 **SYNTHÈSE** (Source : ta_101_part_5.md) : De la logique des mèches et corps exposée, on déduit : corps court (Close ≈ Open) + mèches longues des deux côtés = marché indécis, ni acheteurs ni vendeurs n'ont pu maintenir leur prise de contrôle = doji.
**TRADEX-AI C1** : Doji ou spinning top sur GC/HG/CL/ZW à un niveau de pivot Belkhayate = signal d'indécision → attendre la barre de confirmation suivante avant d'entrer — réduire le scoring de conviction.
*Catégorie : gestion_risque_entree*

### D4269 — Les chandeliers encodent 4 états de marché distincts
🟡 **SYNTHÈSE** (Source : ta_101_part_5.md) : Les 4 cas énoncés (D4260-D4263) couvrent les 4 combinaisons possibles de (up/down day) × (higher/lower close) et leur psychologie associée — une taxonomie complète des états de marché à la barre.
**TRADEX-AI C1** : Framework d'état de barre pour TRADEX : état 1 = force pure (D4260), état 2 = faiblesse pure (D4261), état 3 = piège haussier (D4262, rare mais critique), état 4 = absorption vendeuse (D4263, rare, opportunité). Classification automatisable dans le moteur Python.
*Catégorie : configuration*

### D4270 — Comparaison visuelle 3 formats : les chandeliers révèlent le mieux les points de retournement
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_5.md) : "Quand l'équilibre entre acheteurs et vendeurs change, les chandeliers forment souvent des patterns reconnaissables signalant le changement." Le line chart et l'OHLC ne fournissent pas cette visibilité des retournements.
**TRADEX-AI C1** : Format chandelier obligatoire dans l'interface TRADEX pour GC/HG/CL/ZW — les patterns de retournement Belkhayate sont plus visibles sur chandeliers que sur OHLC; Mode Manuel optimisé pour décision rapide d'Abdelkrim.
*Catégorie : configuration*
