# Extraction StockCharts — Point & Figure Indicators
**Source :** `bundles/stockcharts/point_and_figure_indicators.md` (HTTP 200 · ~5 100 car.) + 7 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D3151 → D3170 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-indicators
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | A one-period moving average is overlaid on a P&F chart. | Moving Averages | CERTIFIE (accord .md + HTML) |
| image_02.png | A P&F chart with a one-period and five-period simple moving average overlay. | Moving Averages | CERTIFIE (accord .md + HTML) |
| image_03.png | Moving average crossovers in a P&F chart. | Moving Averages | CERTIFIE (accord .md + HTML) |
| image_04.png | P&F charts showing narrowing Bollinger Bands before a breakout. | Bollinger Bands | CERTIFIE (accord .md + HTML) |
| image_05.png | Example of P&F chart with a move above the upper band (walking up the upper band). | Bollinger Bands | CERTIFIE (accord .md + HTML) |
| image_06.png | Volume-by-Price bars on a P&F chart showing potential resistance level. | Volume-by-Price | CERTIFIE (accord .md + HTML) |
| image_07.png | Volume-by-Price bars on a P&F chart showing potential support level. | Volume-by-Price | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3151 — Indicateurs sur P&F : base = prix moyen de chaque colonne
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : On peut appliquer moyennes mobiles, Bollinger Bands et Volume-by-Price aux P&F. Les FORMULES restent inchangées, mais les indicateurs sur P&F sont calculés différemment : au lieu des clôtures quotidiennes/hebdomadaires comme base de données, les P&F utilisent le PRIX MOYEN DE CHAQUE COLONNE. Malgré cette différence, ces indicateurs s'utilisent comme sur des barres.
**TRADEX-AI C1** : Garde-fou d'implémentation crucial — un indicateur sur P&F prend en entrée la série « prix moyen de colonne », PAS la série des clôtures. Toute réutilisation de code MA/BB doit changer la source de données.
*Catégorie : configuration*

---

### D3152 — Moyenne mobile P&F : moyenne des moyennes de colonnes
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Les moyennes mobiles sur P&F sont basées sur le prix moyen de chaque colonne (vs clôture de chaque période sur barres). Une SMA10 sur barres = moyenne des 10 dernières clôtures ; une SMA10 périodes sur P&F = moyenne des 10 dernières moyennes de colonnes.
**TRADEX-AI C1** : Définition opérationnelle de la MA P&F. Période exprimée en COLONNES (pas en jours). À implémenter sur la série des moyennes de colonnes.
*Catégorie : indicateurs_tendance*

---

### D3153 — Exemple SMA 1 période : (low + high de la colonne)/2
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_01) : Exemple simple : une SMA 1 période. Si une colonne de X s'étend de 43 à 50, la SMA 1 période = (43 + 50)/2 = 46,5. Sur Agilent, huit X de 43 à 50 dans la dernière colonne ; la SMA 1 jour (bleue) se situe au MILIEU de la colonne (entre le 4e et le 5e X).
**TRADEX-AI C1** : Cas-test chiffré — la SMA 1 période d'une colonne = milieu de son range (low+high)/2. Vérifie une implémentation de « prix moyen de colonne ».
*Catégorie : indicateurs_tendance*

---

### D3154 — SMA 5 périodes : moyenne des 5 dernières colonnes, retard accru
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_02) : Une SMA 5 périodes sur P&F = moyenne des 5 dernières colonnes. Sur Agilent : SMA 1 période (bleue) et SMA 5 périodes (rouge). Comme sur barres, ces moyennes RETARDENT le prix ; plus la moyenne est longue, plus le retard est grand.
**TRADEX-AI C1** : Confirme le comportement laggant des MA P&F (identique aux MA classiques). Arbitrage longueur/réactivité conservé.
*Catégorie : indicateurs_tendance*

---

### D3155 — Double lissage : moyennes plus courtes utilisables sur P&F
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Le DOUBLE LISSAGE permet des moyennes plus courtes. Prendre la moyenne de la colonne lisse le prix une 1re fois ; une moyenne > 2 périodes lisse une 2e fois. Sur P&F, une SMA 5 périodes est une SMA 5 périodes d'une SMA 1 période. Ce double lissage permet d'utiliser des moyennes plus courtes : une SMA 5 jours sur P&F peut produire des signaux similaires à une SMA 50 jours sur barres.
**TRADEX-AI C1** : Garde-fou de paramétrage critique — NE PAS transposer directement les périodes barres→P&F. Une SMA5 P&F ≈ SMA50 barres (double lissage). Recalibrer toutes les fenêtres.
*Catégorie : configuration*

---

### D3156 — Signal MA #1 : croisement prix / moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_03) : Premier des trois signaux de moyenne mobile possibles : chercher le croisement du PRIX et de la moyenne. Un passage AU-DESSUS de la moyenne est haussier, un passage EN DESSOUS est baissier.
**TRADEX-AI C1** : Feature codable — signe de (prix − MA). Signal de base de croisement prix/MA sur P&F.
*Catégorie : signal*

---

### D3157 — Signal MA #2 : direction de la moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_03) : Deuxième signal : identifier la DIRECTION de la moyenne. Une moyenne montante est haussière, une moyenne descendante est baissière.
**TRADEX-AI C1** : Feature de pente de la MA (signe de la dérivée) ; confirme l'orientation de tendance. Complément au croisement prix/MA.
*Catégorie : signal*

---

### D3158 — Signal MA #3 : croisement de deux moyennes (bull/bear)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_03) : Troisième signal : utiliser DEUX moyennes. Signal HAUSSIER quand la moyenne courte croise AU-DESSUS de la longue ; signal BAISSIER quand la courte croise EN DESSOUS de la longue.
**TRADEX-AI C1** : Feature de croisement de MA (golden/death cross adapté P&F) ; signe de (MA_courte − MA_longue). Trois features MA combinables.
*Catégorie : signal*

---

### D3159 — Bollinger Bands P&F : (20,2) par défaut, écart-type
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Les Bollinger Bands sont des bandes d'écart-type placées au-dessus/en dessous d'une moyenne. BB(20,2) = réglage par défaut (20 périodes pour la moyenne, 2 pour l'écart-type). Bande supérieure = moyenne + 2 écarts-types ; bande inférieure = moyenne − 2 écarts-types. Comme les moyennes P&F sont double-lissées, il peut falloir raccourcir la période à 5 ou 10 selon le titre (essais-erreurs requis).
**TRADEX-AI C1** : Formule BB standard appliquée à la série prix moyen de colonne ; garde-fou — raccourcir la fenêtre (5/10) à cause du double lissage P&F. À calibrer par actif.
*Catégorie : indicateurs_tendance*

---

### D3160 — BB P&F : signaux identiques aux barres, bandes resserrées
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_04) : L'analyse et les signaux BB sont les MÊMES sur P&F et sur barres. Trois signaux de base : des bandes qui SE RESSERRENT (narrowing) indiquent une consolidation pouvant mener à un breakout (haut ou bas). Comme sur barres, ce resserrement ne donne PAS d'indice de direction ; chercher le prochain signal P&F pour établir la direction.
**TRADEX-AI C1** : Feature « squeeze » (bandwidth en baisse) = alerte de breakout imminent SANS direction. Exiger un signal P&F directionnel (cassure X/O) pour trancher. Évite les entrées prématurées.
*Catégorie : signal*

---

### D3161 — BB comme filtre des cassures de moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Les Bollinger Bands offrent un FILTRE naturel pour les cassures de moyenne mobile. Comme le prix franchit fréquemment les moyennes sur P&F, les BB servent à filtrer ces signaux (réduire les faux signaux de croisement prix/MA).
**TRADEX-AI C1** : Architecture de filtrage — combiner croisement prix/MA (D3156) avec une condition BB pour réduire le bruit ; cohérent avec une approche multi-confirmation.
*Catégorie : signal*

---

### D3162 — « Walking the bands » : force/faiblesse via bandes ±2σ
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_05) : Une moyenne 5 périodes avec BB à ±2 écarts-types fournit un obstacle de prix supplémentaire. Un passage AU-DESSUS de la bande supérieure montre de la FORCE (uptrend) ; un passage SOUS la bande inférieure montre de la FAIBLESSE (downtrend). Bollinger appelle cela « walking the bands ».
**TRADEX-AI C1** : Feature de régime fort — clôtures de colonnes hors bandes = tendance forte (haussière si bande haute, baissière si bande basse). Filtre de qualité de tendance.
*Catégorie : signal*

---

### D3163 — Volume-by-Price sur P&F : volume par tranche de prix
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Le Volume-by-Price montre le volume pour une tranche de prix donnée. C'est PARFAIT pour les P&F car chaque box représente une tranche de prix spécifique. Les barres Volume-by-Price sont horizontales sur le côté GAUCHE du graphique, alignées sur la tranche de prix.
**TRADEX-AI C2** : Indicateur de volume STRUCTUREL (volume par niveau de prix) — proche d'un volume profile. Adéquation naturelle avec la grille de boxes P&F. Candidat couche C2/structure.
*Catégorie : indicateurs_momentum*

---

### D3164 — Volume-by-Price : subdivision volume positif/négatif
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Le volume est subdivisé en volumes POSITIF et NÉGATIF. Volume positif (vert) quand le prix monte dans la tranche ; volume négatif quand le prix baisse dans la tranche.
**TRADEX-AI C2** : Décomposition haussier/baissier du volume par niveau de prix ; feature de pression directionnelle par tranche. Utile pour qualifier un niveau S/R (accumulation vs distribution).
*Catégorie : indicateurs_momentum*

---

### D3165 — Volume-by-Price : zones de résistance (barres au-dessus du prix)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_06) : Le Volume-by-Price sert à identifier des zones de support/résistance. De LONGUES barres Volume-by-Price AU-DESSUS du prix courant constituent une zone de RÉSISTANCE potentielle.
**TRADEX-AI C2** : Feature S/R par volume — barres longues au-dessus = résistance attendue. Niveau d'intérêt pour stops/cibles sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D3166 — Volume-by-Price : zones de support (barres en dessous du prix)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md, image_07) : À l'inverse, de longues barres Volume-by-Price AU-DESSUS ou AU NIVEAU des prix courants peuvent être un support potentiel quand elles sont situées EN DESSOUS du prix courant — de longues barres sous le prix = zone de SUPPORT potentielle.
**TRADEX-AI C2** : Symétrique de D3165 — barres longues en dessous = support attendu. Combiner les deux pour cartographier les niveaux d'intérêt par volume.
*Catégorie : structure_marche*

---

### D3167 — Indicateurs P&F : confirmer le signal avec un signal P&F
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Même si les calculs de base sont les mêmes, les indicateurs sur P&F diffèrent légèrement de leurs cousins sur barres. Il faut du temps pour comprendre comment ils réagissent aux mouvements de prix sur P&F. Comme pour tous les indicateurs, il est important de CONFIRMER les signaux d'indicateur avec un SIGNAL P&F — ex. un croisement haussier de moyenne mobile doit être confirmé par un breakout P&F (double ou triple top breakout).
**TRADEX-AI C1** : Règle architecturale — indicateur P&F JAMAIS standalone ; exiger confirmation par un signal P&F natif (double/triple top breakout). Cohérent avec la logique multi-confirmation du projet (3/4 + 2/3).
*Catégorie : signal*

---

### D3168 — Avertissement : indicateurs P&F, perspective différente
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : Les indicateurs basés sur P&F donnent une PERSPECTIVE DIFFÉRENTE de l'action des prix. Le temps passé à les comprendre peut être rentable car les P&F offrent une vue distincte de celle des barres.
**TRADEX-AI C1** : Garde-fou interprétatif — ne pas lire un indicateur P&F comme son équivalent barre ; la base de calcul (moyennes de colonnes, pas de temps) change la signification des signaux.
*Catégorie : configuration*

---

### D3169 — Référence d'approfondissement : Thomas Dorsey (P&F Charting)
🔵 **ÉCOLE (Dorsey)** (Source : point_and_figure_indicators.md) : Thomas Dorsey, *Point & Figure Charting*, examine les idées de base et patterns clés des P&F. Disciple de la force relative (relative strength), il consacre un chapitre à ces concepts via P&F, liés aux indicateurs de marché et outils de rotation sectorielle ; il intègre l'usage des P&F avec les ETF.
**TRADEX-AI C1** : Source bibliographique de référence pour approfondir les patterns P&F et la force relative. Hors périmètre direct (ETF/rotation), mais utile pour les patterns de cassure.
*Catégorie : structure_marche*

---

### D3170 — Synthèse : indicateurs P&F = perspective complémentaire, à confirmer
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_indicators.md) : La page établit que MA, Bollinger Bands et Volume-by-Price sont applicables aux P&F avec la même formule mais sur la base « prix moyen de colonne », qu'ils retardent/se comportent comme sur barres, mais nécessitent un recalibrage (double lissage) et une CONFIRMATION par signal P&F natif.
**TRADEX-AI C1** : Synthèse opérationnelle — trois familles d'indicateurs réutilisables sur P&F (MA, BB, VbP), sous réserve (1) source = moyennes de colonnes, (2) recalibrage des périodes, (3) confirmation P&F. Pour la fusion KB.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3151 | Base = prix moyen de colonne | 🟢 | C1 | configuration |
| D3152 | MA P&F = moyenne des colonnes | 🟢 | C1 | indicateurs_tendance |
| D3153 | SMA 1 période = milieu colonne | 🟢 | C1 | indicateurs_tendance |
| D3154 | SMA 5 périodes, retard | 🟢 | C1 | indicateurs_tendance |
| D3155 | Double lissage (SMA5≈SMA50) | 🟢 | C1 | configuration |
| D3156 | Signal MA #1 croisement prix/MA | 🟢 | C1 | signal |
| D3157 | Signal MA #2 direction MA | 🟢 | C1 | signal |
| D3158 | Signal MA #3 croisement 2 MA | 🟢 | C1 | signal |
| D3159 | BB P&F (20,2), raccourcir | 🟢 | C1 | indicateurs_tendance |
| D3160 | BB squeeze sans direction | 🟢 | C1 | signal |
| D3161 | BB filtre cassures MA | 🟢 | C1 | signal |
| D3162 | Walking the bands (force) | 🟢 | C1 | signal |
| D3163 | Volume-by-Price sur P&F | 🟢 | C2 | indicateurs_momentum |
| D3164 | Volume positif/négatif | 🟢 | C2 | indicateurs_momentum |
| D3165 | VbP résistance (barres au-dessus) | 🟢 | C2 | structure_marche |
| D3166 | VbP support (barres en dessous) | 🟢 | C2 | structure_marche |
| D3167 | Confirmer par signal P&F | 🟢 | C1 | signal |
| D3168 | Perspective différente | 🟢 | C1 | configuration |
| D3169 | Référence Dorsey | 🔵 ÉCOLE | C1 | structure_marche |
| D3170 | Synthèse 3 familles d'indicateurs | 🟢 | C1 | configuration |

**Liens Belkhayate :** ni le Point & Figure ni le Volume-by-Price ne sont des outils Belkhayate (⚫). Aucun lien direct revendiqué. Le Volume-by-Price est un indicateur de volume par niveau de prix dont l'esprit recoupe la notion d'« Énergie » Belkhayate ; or la mémoire projet établit que l'Énergie Belkhayate = MFI standard (oscillateur borné 0-100 prix+volume), DIFFÉRENT du Volume-by-Price (profil de volume par tranche de prix). Ne PAS assimiler. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D3151 / D3152 — base de calcul = « prix moyen de colonne » et non clôtures : impératif d'implémentation. Toute MA/BB/VbP sur P&F doit changer la série source, sinon résultats faux.
- D3155 / D3159 — double lissage P&F : NE PAS transposer les périodes barres→P&F (SMA5 P&F ≈ SMA50 barres) ; recalibrer toutes les fenêtres par walk-forward sur GC/HG/CL/ZW.
- D3156–D3158 / D3160–D3162 / D3167 — signaux MA/BB illustrés sur actions ; exiger confirmation par signal P&F natif (double/triple top breakout) avant tout signal automatique ; revalider sur futures.
- D3163–D3166 — Volume-by-Price suppose un flux volume fiable par tranche de prix (NT8/ATAS) ; les niveaux S/R par volume à recalibrer sur la microstructure des futures (séances, roll).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
