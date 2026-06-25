# Extraction StockCharts — P&F Bearish Breakdowns
**Source :** `bundles/stockcharts/p_and_f_bearish_breakdowns.md` (HTTP 200 · ~13 280 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D2811 → D2830 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bearish-breakdowns
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Double Bottom Breakdowns in P&F chart. | Double Bottom Breakdown | CERTIFIE (accord .md + HTML) |
| image_02.png | Triple Bottom Breakdown in a P&F chart. | Triple Bottom Breakdown | CERTIFIE (accord .md + HTML) |
| image_03.png | Spread Triple Bottom Breakdown in a P&F chart. | Spread Triple Bottom Breakdown | CERTIFIE (accord .md + HTML) |
| image_04.png | Descending Triple Bottom Breakdown in a P&F chart. | Descending Triple Bottom Breakdown | CERTIFIE (accord .md + HTML) |
| image_05.png | A Quadruple Bottom Breakdown in a P&F chart confirms the reversal. | Quadruple Bottom Breakdown | CERTIFIE (accord .md + HTML) |
| image_06.png | Downside price objectives of four bearish breakdown patterns. | Measuring Techniques | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2811 — Cinq patterns de breakdown baissier (largeur croissante)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_bearish_breakdowns.md) : Il existe cinq patterns de breakdown baissier en P&F, opposés des cinq patterns de breakout haussier. Le signal de vente P&F le plus basique est le Double Bottom Breakdown (une O-Column casse sous le low de la O-Column précédente). À partir de ce pattern de base, les patterns s'élargissent et se complexifient. Plus le pattern est large, mieux établi est le support et plus important est le breakdown subséquent.
**TRADEX-AI C1** : Famille de 5 patterns structurels baissiers ordonnés par largeur/fiabilité ; la largeur = proxy de force du support cassé. Base pour un détecteur de structure P&F.
*Catégorie : structure_marche*

---

### D2812 — Double Bottom Breakdown : définition (vs Double Bottom en barres)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_01) : En P&F, un Double Bottom Breakdown est BAISSIER, confirmé par une cassure de support. (En charts à barres, à l'inverse, un Double Bottom est HAUSSIER, confirmé par une cassure de résistance — patterns différents aux noms similaires.) Le signal le plus fondamental : une O-Column casse sous le low de la O-Column précédente, séparées par une X-Column. La 1re O-Column descendante établit la direction, la X-Column du milieu est un rebond établissant la résistance, la 3e O-Column déclenche le lower low.
**TRADEX-AI C1** : Définition structurelle précise (3 colonnes : O descendante / X rebond / O cassante). Garde-fou nomenclature — ne PAS confondre avec le Double Bottom haussier des charts à barres.
*Catégorie : structure_marche*

---

### D2813 — Double Bottom Breakdown : le plus commun ET le plus sujet au whipsaw
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_01) : Les Double Bottom Breakdowns sont le signal le PLUS COMMON de l'univers P&F et le plus enclin au whipsaw et à l'échec. Ils doivent être lus dans le contexte d'ensemble. Important d'employer d'autres aspects de l'AT pour des signaux aussi communs. Exemple Avery Dennison (AVY) avec plusieurs Double Bottom Breakdowns.
**TRADEX-AI C1** : Garde-fou — signal fréquent mais peu fiable seul ; pondérer faiblement / exiger confluence. Cohérent avec « jamais standalone ».
*Catégorie : signal*

---

### D2814 — Triple Bottom Breakdown : définition (5 colonnes)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_02) : Le Triple Bottom Breakdown pousse le Double Bottom un cran plus loin en ajoutant une colonne de support. Deux O-Columns consécutives définissent le support avec deux lows égaux ; la 3e O-Column casse sous les lows des deux précédentes. Classiquement 5 colonnes de large : trois O-Columns et deux X-Columns.
**TRADEX-AI C1** : Pattern à géométrie fixe (3 O + 2 X = 5 colonnes, deux lows égaux). Détectable algorithmiquement ; plus fiable que le Double (support plus établi).
*Catégorie : structure_marche*

---

### D2815 — Reversal vs Continuation déterminé par le mouvement préalable
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_02) : Ces patterns marquent des breakdowns de RENVERSEMENT ou de CONTINUATION. La distinction dépend du mouvement préalable : un Triple Bottom Breakdown formé comme TOP après une avance = pattern de renversement ; formé comme consolidation après un déclin = pattern de continuation. Exemple : reversal au 1er semestre 2008, continuation au 2nd. Le Triple Bottom Breakdown reste facile à identifier (cassure de support nette).
**TRADEX-AI C1** : Le contexte (avance vs déclin préalable) classe le pattern reversal/continuation. Feature contextuelle obligatoire pour interpréter tout breakdown.
*Catégorie : structure_marche*

---

### D2816 — Spread Triple Bottom Breakdown : ≥ 7 colonnes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_03) : Le Spread Triple Bottom Breakdown est une version élargie du Triple Bottom Breakdown, contenant au moins deux colonnes supplémentaires (donc ≥ 7 colonnes de large). Une X-Column et une O-Column supplémentaires forment des lows AU-DESSUS du niveau de support / point de breakdown, ajoutant de l'espace. Confirmé comme un Triple Bottom normal : cassure sous les lows des deux O-Columns. Idéalement 2 colonnes en plus, mais peut en avoir davantage.
**TRADEX-AI C1** : Variante large (≥7 colonnes) ; même point de confirmation (cassure sous les deux lows). Largeur accrue = support mieux établi.
*Catégorie : structure_marche*

---

### D2817 — Descending Triple Bottom Breakdown : back-to-back Double Bottoms
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_04) : Le Descending Triple Bottom Breakdown = essentiellement deux Double Bottom Breakdowns dos-à-dos. Trois O-Columns descendant de plus en plus bas à chaque breakdown. Comme il y a 3 O-Columns et 2 X-Columns, le pattern est aussi large qu'un Triple Bottom classique. La capacité à forger des lower lows successifs montre une faiblesse sous-jacente (downtrend). Peut être continuation ou reversal.
**TRADEX-AI C1** : Variante à lows DÉCROISSANTS (vs lows égaux du Triple classique) ; signature de downtrend établi. Détectable par la pente descendante des O-Columns.
*Catégorie : structure_marche*

---

### D2818 — Exemple Descending Triple Bottom + cas de whipsaw (International Paper)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_04) : Sur International Paper, deux Spread Triple Bottom Breakdowns : le 1er (2008) marque une continuation du downtrend ; le 2nd (août 2010) résulte en WHIPSAW (mauvais signal) — le breakdown n'a pas tenu longtemps et la X-Column suivante a cassé au-dessus du high de la colonne de breakdown (O-Column).
**TRADEX-AI C1** : Cas concret d'échec ; règle d'invalidation observable — une X-Column repassant au-dessus du high de la colonne de breakdown invalide le signal (clé pour le stop, cf. D2826).
*Catégorie : signal*

---

### D2819 — Exemple Descending Triple Bottom (Monsanto) : continuation puis reversal
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_04) : Sur Monsanto (MON), trois Descending Triple Bottom Breakdowns. Les deux premiers surviennent après des Triple Bottom Breakdowns (lignes bleues) → patterns de continuation. Le troisième se forme après une avance ayant culminé début 2011 → pattern de reversal.
**TRADEX-AI C1** : Illustration de la règle contextuelle D2815 sur un cas réel ; même pattern classé différemment selon le mouvement préalable.
*Catégorie : structure_marche*

---

### D2820 — Quadruple Bottom Breakdown : 7 colonnes (4 O + 3 X)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_05) : Le Quadruple Bottom Breakdown est comme le Triple mais avec une O-Column supplémentaire (support) et une X-Column supplémentaire (largeur). Trois O-Columns consécutives définissent le support avec trois lows égaux ; la 4e O-Column casse sous les lows des trois précédentes. Sept colonnes de large (4 O-Columns, 3 X-Columns). Reversal ou continuation possible.
**TRADEX-AI C1** : Pattern à géométrie fixe (4 O + 3 X = 7 colonnes, 3 lows égaux). Le plus large des breakdowns « bottom » → support le mieux établi.
*Catégorie : structure_marche*

---

### D2821 — Quadruple Bottom ressemble à un head-and-shoulders (exemple mai 2010)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_05) : Exemple d'un Quadruple Bottom Breakdown de renversement en mai 2010, ressemblant à un head-and-shoulders : highs relativement égaux pour les épaules, spike high pour la tête. Confirmation nette avec le Quadruple Bottom Breakdown.
**TRADEX-AI C1** : Pont vers un pattern de barres connu (H&S) ; aide à reconnaître un top de renversement. Confluence possible entre détecteurs P&F et patterns classiques.
*Catégorie : structure_marche*

---

### D2822 — Mise en garde sur les objectifs de prix (guidelines, pas certitudes)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : Avant tout, être prudent avec les objectifs de prix : ce ne sont que des guidelines approximatives. Les chartistes doivent utiliser d'autres aspects de l'AT pour confirmer les objectifs et surveiller continuellement l'état de la tendance/du breakdown.
**TRADEX-AI C1** : Garde-fou — les objectifs P&F sont indicatifs, jamais des cibles dures ; ne pas dimensionner un trade sur le seul objectif.
*Catégorie : gestion_risque_entree*

---

### D2823 — Horizontal count : largeur × box × (2/3 reversal), soustrait du high
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_06) : La méthode horizontal count s'applique aux Triple Bottom, Descending Triple Bottom, Spread Triple Bottom et Quadruple Bottom Breakdowns. Mesurer la largeur du pattern, multiplier par la taille de box puis par 2/3 du reversal amount. Tom Dorsey et A.W. Cohen préconisent 2/3, mais certains chartistes utilisent le reversal complet. SOUSTRAIRE ce total du HIGH du pattern pour l'objectif. Plus le pattern est large, plus le mouvement attendu est grand. (Triple = 5 colonnes ; Quadruple = 7 ; Spread Triple = 7 minimum.)
**TRADEX-AI C1** : Formule déterministe d'objectif baissier (horizontal count) implémentable. Paramètre 2/3 (Dorsey/Cohen) vs reversal complet à trancher. S'applique aux patterns LARGES.
*Catégorie : gestion_risque_entree*

---

### D2824 — Vertical count : pour le Double Bottom Breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : La méthode vertical count s'applique au Double Bottom Breakdown. Après le breakdown, attendre un reversal 3-box pour FIXER la hauteur de la colonne de breakdown (elle reste modifiable jusqu'au reversal ; ce reversal est un simple rebond s'il ne va pas trop loin). Compter les boxes remplies de la colonne de breakdown, multiplier par la taille de box puis par 2/3 du reversal amount. Soustraire ce produit du HIGH du pattern pour l'objectif baissier.
**TRADEX-AI C1** : Formule déterministe d'objectif baissier (vertical count) pour le Double Bottom ; nécessite d'attendre un reversal 3-box avant calcul. Complément du horizontal count (D2823).
*Catégorie : gestion_risque_entree*

---

### D2825 — Exemple 4 objectifs : Double Bottom vertical count rate d'une box
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_06) : Le graphique montre quatre patterns de breakdown et leurs objectifs ; les flèches bleues marquent le high du pattern d'où l'estimation est soustraite. (1) Descending Triple Bottom après un Triple Bottom = continuation. (2) Triple Bottom au prior high = reversal clair. (3) Double Bottom dans un downtrend : vertical count → objectif 44, manquant le bottom d'une seule box. (4) Descending Triple Bottom avec objectif baissier de 65.
**TRADEX-AI C1** : Cas-test chiffré validant les méthodes de comptage ; illustre l'imprécision réelle (objectif à ±1 box).
*Catégorie : gestion_risque_entree*

---

### D2826 — Risque : worst-case = box juste au-dessus du high du pattern
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : Un objectif ne couvre que le côté reward du risk-reward. Étudier aussi le risque : un mouvement au-dessus de la résistance ou du high du pattern négocierait clairement le breakdown. La box juste AU-DESSUS du high du pattern marque souvent le niveau worst-case d'un échec. De même, un Double Top Breakout ou un pattern P&F contradictoire imposerait une réévaluation. Des indices d'échec apparaissent parfois avant ce niveau worst-case.
**TRADEX-AI C1** : Définit le STOP structurel (box au-dessus du high du pattern) et les signaux d'invalidation (Double Top Breakout / pattern contradictoire). Directement exploitable pour le placement de stop.
*Catégorie : gestion_risque_entree*

---

### D2827 — Employer d'autres techniques pour mesurer le risque et suivre la tendance
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : Les chartistes doivent employer d'autres techniques d'analyse technique pour mesurer le risque et surveiller la tendance en cours. La page renvoie vers les articles Horizontal Counts, Vertical Counts et Timeframes pour P&F.
**TRADEX-AI C1** : Règle architecturale — breakdown P&F = couche structure (C1), confirmé/géré avec d'autres outils ; jamais standalone. Renvois vers méthodes de comptage dédiées.
*Catégorie : signal*

---

### D2828 — Reversal forme un top après avance ; continuation = repos après déclin
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : Le signal de vente P&F le plus basique vient du Double Bottom Breakdown. À partir de là, les patterns classiques s'élargissent en consolidations à supports bien définis. Les patterns de RENVERSEMENT se forment comme top après une avance prolongée ; les patterns de CONTINUATION agissent comme un repos après un déclin significatif.
**TRADEX-AI C1** : Synthèse de la taxonomie reversal/continuation (recoupe D2815) ; une consolidation à support défini précède le breakdown. Cadre d'interprétation directionnelle.
*Catégorie : structure_marche*

---

### D2829 — Critères de repérage : congestion + support clair + point de breakdown net
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md) : Un peu de congestion, un niveau de support clair et un point de breakdown définitif rendent ces patterns relativement faciles à repérer.
**TRADEX-AI C1** : Trois critères de détection (zone de congestion, support identifiable, point de cassure net) → spécification d'un détecteur de breakdown P&F.
*Catégorie : structure_marche*

---

### D2830 — Hiérarchie de fiabilité : largeur du pattern = importance du breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bearish_breakdowns.md, image_06) : Récurrent dans la page : plus le pattern est large, mieux établi est le support et plus important / plus grand est le mouvement attendu après breakdown. Double (le plus étroit/le plus faible) < Triple (5 col.) < Quadruple / Spread Triple (7 col.).
**TRADEX-AI C1** : Règle de pondération — attribuer un poids croissant au signal selon la largeur du pattern (Double faible → Quadruple/Spread fort). Exploitable comme score de confiance structurel.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2811 | 5 patterns breakdown baissier | 🔵 ÉCOLE | C1 | structure_marche |
| D2812 | Double Bottom Breakdown (déf.) | 🟢 | C1 | structure_marche |
| D2813 | Double Bottom : commun + whipsaw | 🟢 | C1 | signal |
| D2814 | Triple Bottom Breakdown (5 col.) | 🟢 | C1 | structure_marche |
| D2815 | Reversal vs continuation (contexte) | 🟢 | C1 | structure_marche |
| D2816 | Spread Triple Bottom (≥7 col.) | 🟢 | C1 | structure_marche |
| D2817 | Descending Triple Bottom | 🟢 | C1 | structure_marche |
| D2818 | Exemple whipsaw (Int. Paper) | 🟢 | C1 | signal |
| D2819 | Exemple Monsanto (cont./rev.) | 🟢 | C1 | structure_marche |
| D2820 | Quadruple Bottom (7 col.) | 🟢 | C1 | structure_marche |
| D2821 | Quadruple ≈ head-and-shoulders | 🟢 | C1 | structure_marche |
| D2822 | Objectifs = guidelines | 🟢 | C1 | gestion_risque_entree |
| D2823 | Horizontal count (formule) | 🟢 | C1 | gestion_risque_entree |
| D2824 | Vertical count (Double Bottom) | 🟢 | C1 | gestion_risque_entree |
| D2825 | Exemple 4 objectifs (±1 box) | 🟢 | C1 | gestion_risque_entree |
| D2826 | Worst-case = box au-dessus high | 🟢 | C1 | gestion_risque_entree |
| D2827 | Autres techniques requises | 🟢 | C1 | signal |
| D2828 | Reversal=top / continuation=repos | 🟢 | C1 | structure_marche |
| D2829 | Critères de repérage | 🟢 | C1 | structure_marche |
| D2830 | Largeur = fiabilité/poids | 🟢 | C1 | signal |

**Liens Belkhayate :** les patterns de breakdown Point & Figure ne sont PAS des outils Belkhayate (⚫). La méthode Belkhayate repose sur Pivots + BGC + Direction + Énergie (MFI), pas sur le Point & Figure. Aucun lien direct revendiqué. Rapprochement très indirect (non affirmé) : la notion de cassure de support / niveau structurel recoupe l'usage des Pivots Belkhayate comme niveaux, mais la mécanique P&F (colonnes O/X, box, reversal) est étrangère à Belkhayate. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D2823 / D2824 — paramètre du comptage : 2/3 du reversal (Dorsey/Cohen) VS reversal complet (autres chartistes). Trancher avant codage de l'objectif de prix.
- D2822 / D2825 — les objectifs sont approximatifs (exemple à ±1 box) : ne jamais dimensionner un trade sur le seul objectif P&F.
- D2813 — le Double Bottom Breakdown est le plus fréquent mais le plus faible : exiger une confluence (pondération par largeur, cf. D2830) avant tout signal.
- Tous — patterns illustrés sur actions US (échelle/box journalières) ; le choix de la taille de box et du reversal sur futures GC/HG/CL/ZW conditionne entièrement la détection et doit être calibré.
- D2826 — formaliser le stop structurel (box au-dessus du high du pattern) et les invalidations (Double Top Breakout) dans le moteur.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
