# Extraction StockCharts — P&F Bullish Breakouts
**Source :** `bundles/stockcharts/p_and_f_bullish_breakouts.md` (HTTP 200 · ~12 701 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D2851 → D2870 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bullish-breakouts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | P&F chart with double top breakouts. | Double Top Breakout | CERTIFIE (accord .md + HTML) |
| image_02.png | A Triple Top Breakout in a P&F chart. | Triple Top Breakout | CERTIFIE (accord .md + HTML) |
| image_03.png | P&F chart with two Spread Triple Top Breakouts. | Spread Triple Top Breakout | CERTIFIE (accord .md + HTML) |
| image_04.png | A P&F chart with an Ascending Triple Top Breakout. | Ascending Triple Top Breakout | CERTIFIE (accord .md + HTML) |
| image_05.png | A P&F chart with a Quadruple Top Breakout. | Quadruple Top Breakout | CERTIFIE (accord .md + HTML) |
| image_06.png | A P&F chart with three patterns and price objectives. | Measuring Techniques | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2851 — Cinq patterns de breakout haussier P&F (largeur = importance)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md) : Il existe cinq patterns de breakout haussier en P&F. Le plus basique est le Double Top Breakout. À partir de ce pattern, les autres deviennent plus complexes et plus larges. Plus le pattern est large, mieux le niveau de résistance est établi et plus le breakout est important.
**TRADEX-AI C1** : Famille de signaux d'achat P&F hiérarchisée par largeur ; la largeur du pattern pondère la fiabilité du breakout. Base d'un classificateur de breakouts haussiers.
*Catégorie : structure_marche*

---

### D2852 — Double Top Breakout : définition (X-Column casse le high de la X-Column précédente)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_01) : Le signal d'achat P&F le plus fondamental survient quand une X-Column casse au-dessus du high de la X-Column antérieure. Ces deux X-Columns sont séparées par une O-Column. La première X-Column établit la direction, la O-Column centrale représente un repli qui établit le support, et la troisième X-Column déclenche le higher high.
**TRADEX-AI C1** : Définition codable du Double Top Breakout — structure X / O / X avec X3 > high(X1). Brique élémentaire de tout détecteur de breakout haussier P&F.
*Catégorie : signal*

---

### D2853 — Double Top P&F ≠ Double Top en bar chart (patterns opposés homonymes)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_bullish_breakouts.md) : En P&F, les Double Top Breakouts sont des patterns HAUSSIERS confirmés par une cassure de résistance. Sur un bar chart, au contraire, les Double Top sont des patterns BAISSIERS confirmés par une cassure de support. Ce ne sont pas des patterns contradictoires : ce sont simplement des patterns différents portant des noms similaires.
**TRADEX-AI C1** : Garde-fou sémantique — ne PAS confondre Double Top P&F (achat) et Double Top bar chart (vente). Évite une inversion de signal lors du codage.
*Catégorie : structure_marche*

---

### D2854 — Double Top Breakout : signal le plus fréquent donc le plus sujet au whipsaw
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_01) : Étant le signal le plus commun de l'univers P&F, les Double Top Breakouts sont aussi les plus sujets au whipsaw et à l'échec. Ces breakouts doivent être considérés dans le contexte d'un tableau d'ensemble plus large. Il est important d'employer d'autres aspects de l'analyse technique avec un signal aussi commun.
**TRADEX-AI C1** : Pondération de fiabilité — le Double Top Breakout seul est faible ; exiger confirmation contextuelle (autres cercles). N'active pas un signal fort isolé.
*Catégorie : gestion_risque_entree*

---

### D2855 — Triple Top Breakout : définition (3 X-Columns, 5 colonnes de large)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_02) : Le Triple Top Breakout étend le Double Top en ajoutant une colonne de résistance. Deux X-Columns consécutives définissent la résistance avec deux reaction highs égaux. La 3e X-Column casse au-dessus des deux précédentes. Les Triple Top Breakouts classiques font cinq colonnes de large : trois X-Columns et deux O-Columns.
**TRADEX-AI C1** : Pattern codable — 3 X-Columns à highs égaux + cassure de la 3e ; largeur fixe = 5 colonnes (paramètre du horizontal count, voir D2866).
*Catégorie : structure_marche*

---

### D2856 — Triple Top Breakout : reversal vs continuation selon le mouvement antérieur
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_02) : Ces patterns peuvent marquer des breakouts de retournement (reversal) ou de continuation. La distinction dépend du mouvement antérieur : un Triple Top Breakout formant une base après un déclin est un pattern de reversal ; formant une consolidation après une avance, c'est un pattern de continuation. Le Triple Top Breakout reste facile à identifier.
**TRADEX-AI C1** : Classification contextuelle — étiqueter le breakout reversal/continuation d'après la tendance amont. Métadonnée utile pour la grille de score.
*Catégorie : structure_marche*

---

### D2857 — Spread Triple Top Breakout : version élargie (≥ 7 colonnes)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_03) : Le Spread Triple Top Breakout est une version élargie du Triple Top. Il contient au moins deux colonnes supplémentaires (≥ 7 colonnes de large) : une O-Column et une X-Column additionnelles forment des highs SOUS le niveau de breakout/résistance, ajoutant de la largeur. Comme le Triple Top normal, il est confirmé par une cassure au-dessus des highs des deux X-Columns. Idéalement il forme un Triple Top avec deux colonnes en plus, mais peut en avoir davantage.
**TRADEX-AI C1** : Pattern codable — Triple Top + ≥2 colonnes intercalaires (highs sous résistance). Largeur ≥ 7 → horizontal count plus grand (D2866).
*Catégorie : structure_marche*

---

### D2858 — Spread Triple Top : qualité selon la distance et la tendance entre colonnes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_03) : Exemple Monsanto avec deux Spread Triple Top Breakouts. Le premier (2009) est suspect à cause de la distance entre les deux premières X-Columns et la X-Column de breakout — il y a un downtrend clair entre ces colonnes. Le second est un pattern de continuation car formé après une longue X-Column ; large de sept colonnes, longueur idéale.
**TRADEX-AI C1** : Critère de qualité — un Spread Triple Top avec downtrend interne entre colonnes est suspect ; largeur 7 + amont haussier = idéal. Filtre de fiabilité.
*Catégorie : gestion_risque_entree*

---

### D2859 — Ascending Triple Top Breakout : deux Double Top Breakouts dos-à-dos
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_04) : Un Ascending Triple Top Breakout est constitué de Double Top Breakouts dos-à-dos. Trois X-Columns ascendantes montent à chaque breakout. Avec trois X-Columns et deux O-Columns, le pattern est aussi large qu'un Triple Top classique. Forger des higher highs dos-à-dos montre une force sous-jacente indicative d'un uptrend. Il peut être continuation ou reversal.
**TRADEX-AI C1** : Pattern codable — deux Double Top Breakouts successifs avec X-Columns croissantes ; signal de force d'uptrend. Largeur = 5 colonnes (comme Triple Top).
*Catégorie : structure_marche*

---

### D2860 — Ascending Triple Top : support égal renforce le pattern
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_04) : Exemple Rockwell Collins (COL) début 2010 — les lignes rouges marquent des Double Top Breakouts dos-à-dos. Le titre a établi un support avec deux O-Columns égales pendant la formation. La combinaison d'un support solide et de higher highs a renforcé la force du pattern. Un Spread Triple Top Breakout échoué figure à l'extrême gauche.
**TRADEX-AI C1** : Critère de renforcement — support à O-Columns égales + higher highs = pattern haussier consolidé. Pondération de confiance positive.
*Catégorie : structure_marche*

---

### D2861 — Quadruple Top Breakout : 4 X-Columns, 7 colonnes de large
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_05) : Le Quadruple Top Breakout est comme le Triple Top mais avec une X-Column de résistance et une O-Column supplémentaires. Trois X-Columns consécutives définissent la résistance avec trois highs égaux, et la 4e X-Column casse au-dessus des trois précédentes. Au total : sept colonnes de large, quatre X-Columns et trois O-Columns. Peut être reversal ou continuation.
**TRADEX-AI C1** : Pattern codable — 3 X-Columns à highs égaux + cassure de la 4e ; largeur 7. Niveau de résistance le plus net de la famille.
*Catégorie : structure_marche*

---

### D2862 — Quadruple Top Breakout : ressemblance avec inverse head-and-shoulders
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_05) : Exemple Corning (GLW) — Quadruple Top Breakout de reversal en février 2009, ressemblant aussi à un pattern inverse head-and-shoulders. Le second Quadruple Top Breakout est un pattern de continuation haussier. Continuation ou reversal, les niveaux de résistance sont clairs et le point de breakout est définitif.
**TRADEX-AI C1** : Correspondance inter-pattern — un Quadruple Top de reversal peut coïncider avec un inverse H&S (cohérence cross-méthode). Point de breakout net = entrée précise.
*Catégorie : structure_marche*

---

### D2863 — Prudence sur les price objectives (guides approximatifs)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_bullish_breakouts.md) : Avant tout, être prudent avec les price objectives : ce ne sont que des guides approximatifs. Il est bon d'utiliser d'autres aspects de l'analyse technique pour confirmer les objectifs et surveiller en continu l'état de la tendance/du breakout.
**TRADEX-AI C1** : Garde-fou — les objectifs P&F sont des cibles indicatives, jamais des niveaux durs ; les croiser avec d'autres cercles. Aucune exécution automatique sur un PO seul.
*Catégorie : gestion_risque_entree*

---

### D2864 — Horizontal count : applicable aux patterns larges (Triple/Spread/Ascending/Quadruple)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_06) : La méthode du horizontal count s'applique aux Triple Top Breakouts, Ascending Triple Top Breakouts, Spread Triple Top Breakouts et Quadruple Top Breakouts. On mesure la largeur du pattern, on la multiplie par la taille de box puis par le reversal amount, et on ajoute ce total au low du pattern pour obtenir un Price Objective. Plus le pattern est large, plus le mouvement attendu est grand.
**TRADEX-AI C1** : Formule codable — PO = low_pattern + (largeur × box_size × reversal_amount). Sortie de cible haussière pour patterns larges.
*Catégorie : gestion_risque_entree*

---

### D2865 — Largeurs de référence pour le horizontal count
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md) : Les Triple Top Breakouts font cinq colonnes de large (3 X-Columns et 2 O-Columns), les Quadruple Top Breakouts sept colonnes, et les Spread Triple Top Breakouts sept colonnes minimum.
**TRADEX-AI C1** : Constantes de largeur pour le horizontal count (5 / 7 / ≥7). Paramètres directs de la formule D2864.
*Catégorie : gestion_risque_entree*

---

### D2866 — Vertical count : applicable au Double Top Breakout (après 3-box reversal)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_06) : La méthode du vertical count s'applique au Double Top Breakout. Après le breakout, il faut attendre un 3-box reversal pour fixer la hauteur de la colonne de breakout (celle-ci reste modifiable jusqu'au reversal — considéré comme un pullback tant qu'il ne descend pas trop profond). On compte les boxes remplies de la colonne de breakout, on multiplie par la box size puis par le reversal amount, et on ajoute au low du pattern pour un Price Objective haussier.
**TRADEX-AI C1** : Formule codable — PO = low_pattern + (boxes_remplies × box_size × reversal_amount) ; nécessite un 3-box reversal pour figer la hauteur. Cible du Double Top.
*Catégorie : gestion_risque_entree*

---

### D2867 — Box size variable : mesurer la hauteur par high − low de la colonne
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md, image_06) : Exemple Double Top Breakout — la colonne de breakout fait sept boxes mais de tailles différentes (50 cents sous 20, 1 $ au-dessus de 20). On doit donc soustraire le high du low de la colonne pour mesurer la hauteur (23 − 18,5 = 4,5), multiplier par le reversal amount (3), et ajouter au low du pattern (O-Column la plus basse) pour l'objectif.
**TRADEX-AI C1** : Garde-fou de calcul — quand les box sizes diffèrent (scaling), mesurer la hauteur par (high − low) plutôt qu'en comptant les boxes. Évite une erreur de PO.
*Catégorie : gestion_risque_entree*

---

### D2868 — Worst-case level : box juste sous le low du pattern
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md) : Établir un Price Objective ne couvre que le côté reward. Il faut aussi évaluer le risque : un mouvement sous le support ou le low du pattern annule clairement le breakout. La box juste sous le low du pattern marque souvent le niveau worst-case d'un échec de pattern. De même, un Double Bottom Breakdown ou un pattern P&F contradictoire imposent une réévaluation.
**TRADEX-AI C1** : Niveau d'invalidation codable — stop / worst-case = box sous le low du pattern. Un Double Bottom Breakdown opposé invalide le signal. Base du R/R.
*Catégorie : gestion_risque_entree*

---

### D2869 — Indices d'échec parfois avant le worst-case + autres outils AT
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_bullish_breakouts.md) : Il y a parfois des indications d'échec potentiel avant que le prix n'atteigne le niveau worst-case. Les chartistes doivent aussi employer d'autres techniques d'analyse technique pour mesurer le risque et surveiller la tendance qui se déroule (voir les articles sur Horizontal Counts, Vertical Counts et Timeframes P&F).
**TRADEX-AI C1** : Logique de sortie anticipée — surveiller des signaux d'échec avant le stop dur ; croiser avec d'autres cercles. Renvoie vers les modules counts/timeframes.
*Catégorie : gestion_risque_entree*

---

### D2870 — Synthèse : du Double Top aux patterns larges à résistance définie
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bullish_breakouts.md) : Le signal d'achat P&F le plus basique vient du Double Top Breakout. Les patterns classiques s'élargissent ensuite pour former des consolidations à résistance bien définie. Les patterns de reversal forment une base après un déclin prolongé, les patterns de continuation servent de repos après une avance prolongée. Un peu de congestion, un niveau de résistance clair et un point de breakout définitif rendent ces patterns relativement faciles à repérer.
**TRADEX-AI C1** : Vue d'ensemble pour la grille — la famille haussière P&F = continuation après avance ou reversal après déclin, avec résistance + breakout nets. Cadre de classification.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2851 → D2870 (20) |
| Images certifiées | 6/6 |
| Cercle | C1 (structure de marché / prix) |
| Catégories | structure_marche (11) · signal (2) · gestion_risque_entree (7) |
| Actifs concernés | GC · HG · CL · ZW (patterns P&F génériques applicables) |
| Lien Belkhayate | NON CONCERNÉ (P&F = méthode A.W. Cohen/Dorsey, hors corpus Belkhayate) |
| Tags utilisés | 🟢 FAIT VÉRIFIÉ (17) · 🔵 ÉCOLE (3) |
| Cas à vérifier | Aucun — 6/6 images certifiées, contenu littéral sans ambiguïté |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
