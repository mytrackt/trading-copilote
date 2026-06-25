# Extraction AdamGrimes — Trendlines 101
**Source :** `bundles/adamgrimes/trendlines_101.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle (références à des figures sans fichiers joints) · 0/0 certifiées · 0 à vérifier
**Décisions :** D7211 → D7230 · **Page :** https://www.adamhgrimes.com/trendlines-101/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Règles de tracé et de validité des lignes de tendance — critères objectifs pour identifier quand une ligne de tendance est significative ou non.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune — figures mentionnées dans le texte mais non incluses dans le bundle) | — | — | — |

## DÉCISIONS

### D7211 — Une ligne de tendance haussière se trace entre les points bas successifs croissants
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Une ligne de tendance haussière standard (uptrend line) se trace entre des points bas successifs de plus en plus hauts (higher lows) en uptrend. Wyckoff l'appelait "demand line" car elle marque les zones où les acheteurs sont intervenus à la hausse. La ligne de tendance baissière standard (downtrend line / supply line) se trace entre des points hauts successifs de plus en plus bas (lower highs).
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, les lignes de tendance doivent suivre cette convention stricte : uptrend line sous les prix reliant les higher lows, downtrend line au-dessus reliant les lower highs. Ce tracé est cohérent avec la structure Belkhayate (pivots + direction).
*Catégorie : structure_marche*

### D7212 — Une ligne de tendance haussière doit être tracée sous les prix, une baissière au-dessus
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Les lignes de tendance haussières se tracent sous les prix (zones de support potentiel). Les lignes de tendance baissières se tracent au-dessus des prix (zones de résistance potentielle). Ce positionnement est une règle non négociable de la définition standard.
**TRADEX-AI C1** : Règle de tracé à appliquer dans l'analyse graphique TRADEX — une ligne de tendance haussière tracée au-dessus des prix ou une baissière en dessous est non standard et n'a pas de valeur de signal.
*Catégorie : structure_marche*

### D7213 — Ces 5 configurations de lignes de tendance sont non standard et peu fiables
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Cinq types de lignes non standard sont identifiés : (A) tracée entre points bas en downtrend au lieu des points hauts, (B) tracée entre points bas en downtrend en ignorant un spike pour ajuster la ligne aux données ultérieures, (C) ligne best-fit tracée au centre des prix (freehand ou régression linéaire), (D) tracée entre points hauts en uptrend au lieu des points bas, (E) tracée là où il n'y a pas de swings définis sur le timeframe.
**TRADEX-AI C1** : Lors de l'analyse manuelle ou automatique de structure de marché pour GC/HG/CL/ZW, rejeter toute ligne de tendance appartenant à l'une de ces 5 catégories — elle ne génère pas de signal fiable.
*Catégorie : structure_marche*

### D7214 — Une ligne de tendance ne doit pas "couper" les prix entre ses deux points d'ancrage
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Si la ligne de tendance passe à travers des prix situés entre ses deux points d'ancrage (i.e., elle a déjà été violée lors de son tracé initial), sa signification future est très réduite. La logique : une ligne déjà violée ne peut pas être considérée comme significative lors d'un prochain contact. Il faut tracer la ligne de façon à ce qu'elle soit potentiellement significative lors de son prochain test.
**TRADEX-AI C1** : Pour tout niveau de support/résistance dynamique tracé dans TRADEX, vérifier que la ligne n'a pas déjà été violée entre ses deux points d'ancrage — sinon son niveau de confiance est dégradé.
*Catégorie : structure_marche*

### D7215 — Sur les chandeliers, éviter de tracer les lignes sur les corps en ignorant les mèches
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Pour les traders utilisant des chandeliers japonais, il est tentant de tracer les lignes de tendance en touchant les corps des bougies tout en coupant les mèches. C'est une pratique imprécise à éviter, sauf si l'on exécute uniquement sur la clôture de la barre (auquel cas les pénétrations intrabar n'ont pas d'importance).
**TRADEX-AI C1** : TRADEX utilise des range bars NT8 — les lignes de tendance doivent inclure les extrêmes hauts/bas de chaque barre, pas uniquement les corps. Toute pénétration d'un extrême constitue une violation potentielle à surveiller.
*Catégorie : structure_marche*

### D7216 — Une ligne de tendance nécessite l'existence de swings définis sur le timeframe analysé
🟢 **FAIT VÉRIFIÉ** (Source : trendlines_101.md) : Les lignes de tendance sont des outils pour définir la relation entre les swings. Si le marché est plat et sans swings identifiables, il n'y a pas de ligne de tendance valide à tracer. Tracer une ligne sur une série de barres consécutives sans swings produit un niveau facilement violé sans action de prix fiable après la pénétration.
**TRADEX-AI C1** : Pour TRADEX, ne générer de signal sur rupture de ligne de tendance que si des swings clairement définis ont été préalablement identifiés sur le timeframe de référence (range bars NT8). En consolidation plate, pas de signal trendline.
*Catégorie : structure_marche*

### D7217 — L'évaluation objective des lignes de tendance est quasi impossible — subjectivité inhérente
🟡 **SYNTHÈSE** (Source : trendlines_101.md) : Les lignes de tendance sont généralement tracées subjectivement, ce qui rend leur évaluation objective impossible. L'action des prix autour de lignes de tendance aléatoires peut sembler convaincante en raison du caractère partiellement aléatoire des marchés. Il n'existe pas de règle universellement acceptée pour déterminer où et comment tracer une ligne de tendance — même la définition précise fait débat.
**TRADEX-AI C1** : Les lignes de tendance ne peuvent pas être le seul critère d'un signal TRADEX — elles constituent un élément de contexte parmi d'autres (structure Belkhayate, pivots, alignement des actifs).
*Catégorie : structure_marche*

### D7218 — Les lignes de tendance internes (tracées au milieu des prix) ont un statut différent
🔵 **ÉCOLE** (Source : trendlines_101.md) : Les lignes de tendance "internes" (tracées à travers le milieu des barres de prix, type best-fit ou régression linéaire) constituent une catégorie séparée des lignes de tendance standard. Elles peuvent être tracées n'importe où et leur signification est différente de celle des lignes standard reliant les swings.
**TRADEX-AI C1** : Les droites de régression linéaire (COG Belkhayate) appliquées dans TRADEX sont de nature différente des trendlines standard — elles ne doivent pas être confondues avec des niveaux de support/résistance dynamique issus de swings.
*Catégorie : indicateurs_tendance*
