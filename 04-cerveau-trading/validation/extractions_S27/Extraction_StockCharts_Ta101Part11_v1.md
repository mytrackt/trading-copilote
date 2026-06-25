# Extraction StockCharts — TA 101 Part 11 (Price Patterns)
**Source :** `bundles/stockcharts/ta_101_part_11.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D4051 → D4070 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-11.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Patterns de prix (Rectangle, Triangle) directement applicables à GC/HG/CL/ZW pour identifier consolidations et breakouts avec confirmation volume.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | (sans alt) — Rectangle Pattern illustration | Price Patterns | D4051 |
| image_02 | (sans alt) — Rectangle breakout volume anticipation | Price Patterns | D4053 |
| image_03 | (sans alt) — Descending Triangle Pattern | Price Patterns | D4057 |
| image_04 | (sans alt) — Rising Triangle Pattern | Price Patterns | D4058 |

## DÉCISIONS

### D4051 — Rectangle Pattern : définition et conditions de validité
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md, image_01) : Un Rectangle Pattern se forme lorsque le prix oscille entre deux lignes horizontales de support et de résistance. Pour être valide, chaque ligne doit être touchée au moins deux fois. Le pattern peut durer de quelques jours à plusieurs mois et se termine lorsque l'une des lignes est cassée.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un range latéral avec au moins 2 touches de support ET 2 touches de résistance constitue un Rectangle valide — signal de breakout potentiel à surveiller.
*Catégorie : structure_marche*

### D4052 — Rectangle Pattern : les participants et la dynamique psychologique
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Les patterns Rectangle montrent clairement le combat entre haussiers et baissiers — les bulls achètent systématiquement sur le support, les bears vendent systématiquement sur la résistance. À un moment, un camp gagne et le prix sort du pattern.
**TRADEX-AI C1/C5** : La durée du range dans GC/HG/CL/ZW est proportionnelle à l'ampleur du breakout — plus le range dure longtemps, plus le mouvement consécutif sera important (C5 psychologie de masse).
*Catégorie : psychologie*

### D4053 — Rectangle Pattern : anticipation de breakout haussier via volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md, image_02) : Un breakout haussier peut être anticipé si le volume s'étend quand les prix montent ET se contracte quand les prix baissent à l'intérieur du rectangle. Un breakout imminent au-dessus de la résistance peut exister si les prix ne retombent pas jusqu'à la ligne de support avant de remonter.
**TRADEX-AI C1/C2** : Sur GC, si le volume (ATAS footprint) confirme les montées et s'affaiblit sur les baisses dans un range, anticiper breakout haussier avant la résistance.
*Catégorie : volume_liquidite*

### D4054 — Rectangle Pattern : anticipation de breakout baissier via volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Un breakout baissier peut être anticipé si le volume s'étend quand les prix baissent ET se contracte quand les prix montent à l'intérieur du rectangle. Un breakout imminent sous le support peut exister si les prix ne remontent pas jusqu'à la résistance avant de re-baisser.
**TRADEX-AI C1/C2** : Sur HG/CL, si le delta ATAS est négatif sur les montées et positif sur les baisses dans un range, anticiper le breakout baissier.
*Catégorie : volume_liquidite*

### D4055 — Rectangle Pattern : inversion support/résistance après breakout
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Dès que le pattern se casse, le haut (ou le bas) du rectangle se transforme en ligne de support (ou résistance) pour l'instrument. Ce principe de role-reversal est illustré directement.
**TRADEX-AI C1** : Après breakout d'un range sur GC/ZW, l'ancien plafond devient support à surveiller pour retest — confirme entrée en mode tendance.
*Catégorie : structure_marche*

### D4056 — Rectangle vs Triangle : définition du Triangle Pattern
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Le Triangle Pattern est très similaire au Rectangle sauf que les lignes de tendance supérieure et/ou inférieure définissant le pattern sont inclinées plutôt qu'horizontales. Il existe 3 variantes : Descending Triangle, Rising Triangle, Symmetric Triangle.
**TRADEX-AI C1** : Les triangles sont fréquents sur les contrats futures en période de compression de volatilité (VX en baisse) — à identifier sur GC/HG avant les grandes décisions macro.
*Catégorie : structure_marche*

### D4057 — Descending Triangle : interprétation baissière
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md, image_03) : Le Descending Triangle se forme quand de plus en plus de vendeurs n'attendent plus le retour à la résistance pour vendre — ils vendent plus tôt. Cela crée une ligne de résistance descendante tandis que le support reste horizontal. Sentiment baissier croissant.
**TRADEX-AI C1/C5** : Sur CL/HG, un Descending Triangle avec résistance descendante et support plat signale une pression vendeuse croissante — alerte bearish à combiner avec DX haussier.
*Catégorie : structure_marche*

### D4058 — Rising Triangle : interprétation haussière
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md, image_04) : Le Rising Triangle se forme quand les acheteurs deviennent impatients et commencent à acheter avant le retour à la ligne de support — ils achètent plus tôt. Cela crée un support ascendant tandis que la résistance reste horizontale. Sentiment haussier croissant.
**TRADEX-AI C1/C5** : Sur GC/ZW, un Rising Triangle avec support montant et résistance plate signale une demande croissante — contexte favorable signal ACHETER si ES confirme.
*Catégorie : structure_marche*

### D4059 — Symmetric Triangle : coil et direction indéterminée
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Un Symmetric Triangle (aussi appelé "coil") se forme quand les bulls deviennent plus haussiers ET les bears plus baissiers simultanément — les deux lignes sont inclinées. Plus les lignes convergent, plus l'énergie s'accumule comme un ressort. Le breakout est inévitable mais la direction est incertaine. Généralement le breakout survient bien avant l'apex du triangle.
**TRADEX-AI C1/C5** : Sur GC avant NFP/FOMC, un Symmetric Triangle comprime l'énergie — augmenter la vigilance sur le signal du news gate et attendre la direction du breakout post-événement.
*Catégorie : structure_marche*

### D4060 — Triangle : sens du breakout lié à la tendance précédente
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Deux indices pour anticiper la direction du breakout d'un triangle : (1) Si l'instrument était en uptrend avant le triangle, bonne chance pour un breakout haussier continuant l'uptrend. (2) Les Rising Triangles tendent à casser à la hausse, les Descending Triangles souvent à la baisse. (3) Les Symmetric Triangles pointent souvent dans la direction du breakout selon que le support ou la résistance est plus fort.
**TRADEX-AI C1** : Règle de contexte tendance : valider la tendance précédente sur GC/HG avant d'interpréter un triangle — un triangle dans un uptrend fort est majoritairement une consolidation continue.
*Catégorie : structure_marche*

### D4061 — Price Patterns : nature probabiliste comme météo
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Les chart patterns indiquent souvent (mais pas toujours) les futurs mouvements de prix. Ils sont comparés aux prévisions météo — souvent justes mais parfois incorrects. Ce sont les "restes visuels" d'une bataille entre bulls et bears.
🟡 **SYNTHÈSE** : L'analogie météorologique souligne le caractère probabiliste, jamais certain, de l'analyse technique des patterns.
**TRADEX-AI C1** : Intégrer les patterns de prix comme un signal parmi d'autres dans la grille /10 — jamais comme signal unique suffisant pour exécuter un ordre sur GC/CL.
*Catégorie : gestion_risque_entree*

### D4062 — Rectangle et Triangle : patterns de continuation/consolidation
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Les Rectangle et Triangle Patterns sont des exemples de Consolidation Patterns (aussi appelés Continuation Patterns). Après leur complétion, les prix reprennent généralement la tendance qui précédait leur formation. Ces patterns représentent une dispute à court terme peu convaincante — "la vue d'ensemble ne change pas vraiment."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un Rectangle ou Triangle en cours de formation dans un uptrend est un signal d'attente — ne pas shorter contre la tendance principale avant la cassure.
*Catégorie : timing*

### D4063 — Durée du pattern et amplitude du breakout
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : "The longer prices have been in the pattern, then the larger the breakout move will be and the more significant the new support/resistance line becomes."
**TRADEX-AI C1** : Un range long sur GC (plusieurs semaines) génère un breakout de plus grande amplitude qu'un range court — calibrer la taille de position et les objectifs en conséquence.
*Catégorie : gestion_position_active*

### D4064 — Symmetric Triangle : le breakout survient avant l'apex
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : "Typically, triangle patterns have a breakout well before the apex of the triangle is reached." Le breakout ne se produit pas tout à la fin quand les lignes convergent, mais généralement à mi-chemin environ.
**TRADEX-AI C1** : Ne pas attendre la pointe ultime du triangle sur CL/ZW — surveiller le breakout dès que les lignes sont à 60-70% de convergence.
*Catégorie : timing*

### D4065 — Price Patterns : rôle du volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : Le contenu annonce : "In part 12 we'll look at how to confirm these patterns with volume." Cela confirme que le volume est le principal outil de confirmation des patterns de prix dans cette méthodologie.
**TRADEX-AI C2** : Le volume (ATAS) est l'outil primaire de confirmation des patterns — sans confirmation volume, tout signal de breakout est à traiter avec précaution (confiance réduite).
*Catégorie : volume_liquidite*

### D4066 — Rectangle Pattern : range de prix étroit ou large
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : "Rectangle patterns have a narrow or wide price range and last from days to months." Le pattern est valide indépendamment de l'amplitude du range — la largeur importe moins que la structure horizontale.
**TRADEX-AI C1** : Sur GC/HG, les rectangles peuvent être étroits (consolidation courte) ou larges (accumulation longue) — les deux sont valides si les 2 touches minimum sont respectées de chaque côté.
*Catégorie : structure_marche*

### D4067 — Triangle asymétrique : lecture de la force relative
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : "The support side may be stronger than the resistance side making the triangle point up or, if the support side is weaker, point down. In that case, the triangle often breaks in the direction it is pointing."
**TRADEX-AI C1/C5** : L'asymétrie d'un triangle sur ES peut annoncer la direction du marché actions — utiliser comme signal de confirmation C5 pour GC (corrélation inverse).
*Catégorie : correlations*

### D4068 — Descending Triangle : vendeurs de plus en plus impatients
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : La psychologie du Descending Triangle est explicitement décrite — les vendeurs ne veulent plus attendre le retour à la résistance. Ce comportement crée la ligne de résistance descendante caractéristique.
⚫ **HYPOTHÈSE PROJET** : En termes Belkhayate, ce comportement correspond à une "énergie baissière croissante" qui se traduit dans l'indicateur d'Énergie avant le breakout.
**TRADEX-AI C1/C5** : Descending Triangle sur HG (cuivre) + DX haussier = confluence baissière forte sur les matières premières — alerte signal VENDRE.
*Catégorie : psychologie*

### D4069 — Price Patterns : fondement (lignes de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : "At their core, most price patterns are combinations of several trend lines. The simplest pattern is the Rectangle Pattern." Tous les patterns de prix complexes sont décomposables en lignes de tendance simples.
**TRADEX-AI C1** : Les pivots Belkhayate (support/résistance) sont les briques fondamentales de tous les patterns — la détection automatique des lignes de tendance dans NT8 doit être alignée avec cette logique.
*Catégorie : structure_marche*

### D4070 — Rising Triangle : acheteurs de plus en plus impatients
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_11.md) : La psychologie du Rising Triangle est explicitement décrite — les acheteurs deviennent impatients et achètent avant que le prix ne revienne à la ligne de support. Ce comportement crée le support ascendant caractéristique.
⚫ **HYPOTHÈSE PROJET** : En termes Belkhayate, ce comportement reflète une "énergie haussière croissante" — les acheteurs institutionnels accumulent à des niveaux de plus en plus élevés.
**TRADEX-AI C1/C3** : Rising Triangle sur GC avec volume institutionnel (COT longs croissants) = confirmation C3 d'accumulation — signal haussier fort pour GC.
*Catégorie : psychologie*
