# Extraction StockCharts — P&F Price Objectives : Breakout and Reversal Method
**Source :** `bundles/stockcharts/p_and_f_price_objectives_breakout_and_reversal_method.md` (HTTP 200 · ~22 343 car.) + 12 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 12/12 certifiées
**Décisions :** D2911 → D2930 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/p-and-f-price-objectives/p-and-f-price-objectives-breakout-and-reversal-method
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Basic P&F signals. | Basic P&F Signals | CERTIFIE (accord .md + HTML) |
| image_02.png | Calculating Bullish Price Objective. | Breakout Method: Bullish | CERTIFIE (accord .md + HTML) |
| image_03.png | A tentative Bullish Price Objective. | Breakout Method: Bullish | CERTIFIE (accord .md + HTML) |
| image_04.png | Example of how to calculate a Bearish Price Objective. | Breakout Method: Bearish | CERTIFIE (accord .md + HTML) |
| image_05.png | Example of a tentative Bearish Price Objective in a P&F chart. | Breakout Method: Bearish | CERTIFIE (accord .md + HTML) |
| image_06.png | Bullish Reversal method for calculating Price Objectives in a P&F chart. | Reversal Method: Bullish | CERTIFIE (accord .md + HTML) |
| image_07.png | Example of a tentative Bullish Reversal price objective. | Reversal Method: Bullish | CERTIFIE (accord .md + HTML) |
| image_08.png | Reversal Method: Bearish | Reversal Method: Bearish [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | An example of a tentative Bearish Price Objective. | Reversal Method: Bearish | CERTIFIE (accord .md + HTML) |
| image_10.png | Tentative Bullish Price Objective | Met Price Objectives | CERTIFIE (accord .md + HTML) |
| image_11.png | The Bullish Price Objective was met as indicated by the MET! | Met Price Objectives | CERTIFIE (accord .md + HTML) |
| image_12.png | Activating price objectives in SharpCharts | Activating Price Objectives | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2911 — Deux méthodes automatisées : Breakout et Reversal (basées sur la Measure Column)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md) : StockCharts automatise les Price Objectives P&F via la Breakout Method et la Reversal Method. Les deux reposent sur la longueur verticale (hauteur) d'une Measure Column. Plus la Measure Column est longue, plus le price objective est haut (haussier) ou bas (baissier). L'identification de la colonne dépend de la méthode choisie (Breakout ou Reversal).
**TRADEX-AI C1** : Deux algorithmes d'objectif fondés sur la hauteur d'une Measure Column ; la sélection de la colonne diffère selon la méthode. Cadre du module price objectives.
*Catégorie : gestion_risque_entree*

---

### D2912 — Price Objective = guide, pas niveau dur (extrême de la range, à surveiller)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md) : Avertissement : les Price Objectives P&F sont des cibles haut/bas issues d'un signal d'achat/vente P&F. Ils ne doivent PAS être l'unique raison d'acheter/vendre ; ce sont des guides généraux selon la force du mouvement initial. L'objectif représente l'EXTRÊME de la range : certains titres l'atteignent, d'autres se retournent avant. Il faut surveiller en continu la situation technique pour valider/invalider l'objectif.
**TRADEX-AI C1** : Garde-fou — PO = extrême de fourchette, jamais un déclencheur d'ordre isolé. Surveillance continue requise. Aucune exécution automatique sur PO seul.
*Catégorie : gestion_risque_entree*

---

### D2913 — Le scaling affecte les Price Objectives (traditional / ATR / percentage)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md) : Différentes méthodes de scaling affectent les Price Objectives. Le traditional scaling = ½ point/box sous 20, 1 point entre 20 et 100, 2 points entre 100 et 200, 4 points entre 200 et 400. Les objectifs changent avec le dynamic ATR scaling et le percentage scaling. Pour calculer, le « user-defined » scaling (box size uniforme) facilite les calculs. Les objectifs sont des « soft areas », pas des « hard levels » ; le header du chart montre les niveaux extrêmes de la range.
**TRADEX-AI C1** : Paramètre critique — la box size dépend du scaling et du niveau de prix ; figer un scaling uniforme pour des calculs reproductibles. Affecte directement la formule de PO.
*Catégorie : configuration*

---

### D2914 — Breakout/Reversal ignorent les patterns classiques (utilisent signaux basiques)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_01) : Les méthodes Breakout et Reversal ne tiennent PAS compte des patterns P&F classiques (Triple Top Breakouts, Triple Bottom Breakdowns, High-Pole Reversals). Ces patterns peuvent être présents mais n'entrent pas dans les calculs. À la place, elles utilisent les signaux d'achat/vente P&F basiques.
**TRADEX-AI C1** : Garde-fou de calcul — pour ces deux méthodes, n'utiliser QUE les Double Top Breakout / Double Bottom Breakdown, ignorer les patterns larges. Évite une mauvaise sélection de colonne.
*Catégorie : gestion_risque_entree*

---

### D2915 — Signal basique d'achat = Double Top Breakout ; de vente = Double Bottom Breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_01) : Un signal d'achat P&F basique = Double Top Breakout (une X-Column dépasse le high de la X-Column antérieure ; higher high, présent en uptrends). Un signal de vente P&F basique = Double Bottom Breakdown (une O-Column dépasse le low de la O-Column antérieure ; lower low, présent en downtrends). Ce sont les signaux les plus prolifiques.
**TRADEX-AI C1** : Définitions codables des signaux basiques (achat/vente) servant de base aux deux méthodes. Cohérent avec D2852.
*Catégorie : signal*

---

### D2916 — Signal actif unique : toujours un seul (achat OU vente, jamais les deux)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_01) : La flèche bleue met en évidence le signal courant (actif). Il y a TOUJOURS un signal courant/actif en jeu sur un chart P&F : soit un signal d'achat actif, soit un signal de vente actif. C'est l'un ou l'autre, jamais les deux.
**TRADEX-AI C1** : Invariant d'état codable — état P&F binaire (achat actif XOR vente actif) à tout instant. Pilote l'affichage haussier/baissier du PO. Machine à états simple.
*Catégorie : structure_marche*

---

### D2917 — Breakout Method Bullish : 4 étapes (sell signal → buy signal reverseur = Measure Column)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_02) : Breakout Bullish (signal actif = achat). (1) De droite à gauche, trouver le Double Bottom Breakdown (sell signal) le plus récent. (2) À droite de ce sell signal, trouver le prochain Double Top Breakout (buy signal) : la colonne qui le produit a renversé le sell signal et devient la Measure Column (pas forcément le buy signal le plus récent). (3) Hauteur de la Measure Column × reversal amount (soit high−low, soit nb boxes remplies × box size × reversal, typiquement 3). (4) Ajouter au low de la colonne juste avant la Measure Column (une O-Column).
**TRADEX-AI C1** : Algorithme codable — PO_bullish = low(colonne avant Measure) + hauteur(Measure) × 3. La Measure Column = celle qui a renversé le dernier sell signal. Cible haussière.
*Catégorie : gestion_risque_entree*

---

### D2918 — Breakout Bullish : exemple Citrix (PO = 74) figé après 3-box reversal
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_02) : Exemple Citrix (CTXS), Bullish PO = 74. Le buy signal de février a renversé le sell signal et devient Measure Column : hauteur 5 boxes (high 65 − low 60 = 5), × reversal 3 = 15, ajouté au low de l'O-Column antérieure (59 + 15 = 74). Le Measure Column est figé car un 3-box reversal a verrouillé la hauteur ; malgré des O-Columns en repli, le buy signal et le PO restent en vigueur jusqu'à un sell signal P&F.
**TRADEX-AI C1** : Cas numérique de référence (validation du calcul). Le PO reste valide jusqu'à inversion de signal, indépendamment de petits replis. Test unitaire possible.
*Catégorie : gestion_risque_entree*

---

### D2919 — Breakout Bullish : PO « tentative » tant que la Measure Column n'est pas figée
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_03) : Exemple General Motors (GM) — Bullish PO « tentative » de 48. Le PO est tentative car la Measure Column n'est pas encore figée et peut changer si les prix montent (un mouvement au-dessus de 39 ajoute un X, augmente la hauteur, donc le PO). La colonne ne sera figée qu'après un 3-box reversal (O-Column de 3 boxes). Un tel mouvement n'annule PAS le buy signal ; le PO reste valide jusqu'à un sell signal.
**TRADEX-AI C1** : État codable — flag « tentative » du PO tant que pas de 3-box reversal ; le PO peut croître. Distinguer PO fixe vs tentative dans l'affichage.
*Catégorie : gestion_risque_entree*

---

### D2920 — Breakout Method Bearish : 4 étapes + facteur 2/3 (Cohen/Dorsey)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_04) : Breakout Bearish (signal actif = vente). (1) De droite à gauche, trouver le dernier buy signal. (2) À droite, trouver le prochain sell signal : la colonne qui le produit (assez forte pour renverser le buy signal) = Measure Column. (3) Hauteur × 2/3 du reversal amount (typiquement 3) — l'usage de 2/3 pour les comptes baissiers est préconisé par A.W. Cohen et Tom Dorsey. (4) Soustraire ce total du high de la colonne juste avant la Measure Column (une X-Column).
**TRADEX-AI C1** : Algorithme codable ASYMÉTRIQUE — PO_bearish = high(colonne avant Measure) − hauteur × (2/3 × 3). Le facteur 2/3 est spécifique aux objectifs baissiers. Garde-fou : ne PAS symétriser naïvement le calcul haussier.
*Catégorie : gestion_risque_entree*

---

### D2921 — Breakout Bearish : exemple numérique (hauteur 10 → PO = 71)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_04) : Exemple — dernier buy signal en décembre 2014 (red C), sell signal suivi de la longue O-Column de janvier 2015, figée après le bounce contre-tendance (X-Column red 2). Colonne = 10 boxes × box 1 × reversal 3 = 30 (ou high 91 − low 81 = 10, × 3). Prendre 2/3 du total (30 × 2/3 = 20) et soustraire du high de la X-Column avant la Measure Column (91 − 20 = 71). PO inchangé jusqu'à un buy signal.
**TRADEX-AI C1** : Cas numérique de référence baissier (validation du facteur 2/3). Test unitaire possible. PO baissier figé jusqu'à inversion.
*Catégorie : gestion_risque_entree*

---

### D2922 — Breakout Bearish : PO « tentative » jusqu'au 3-box reversal haussier
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_05) : Exemple Garmin (GRMN) — sell signal actif et Bearish PO « tentative » car la hauteur de la Measure Column n'est pas encore figée (la colonne pourrait s'étendre plus bas). La colonne se fige lors d'un 3-box reversal avec X-Column montant de 3 boxes. Même avec ce mouvement contraire, le Bearish PO reste valide jusqu'à un buy signal P&F.
**TRADEX-AI C1** : État codable miroir de D2919 — flag « tentative » baissier jusqu'au 3-box reversal haussier. Le PO peut descendre tant que non figé.
*Catégorie : gestion_risque_entree*

---

### D2923 — Reversal Method Bullish : 3 étapes (X-Column voisine du sell signal = Measure Column)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_06) : Reversal Bullish (signal actif = achat). (1) De droite à gauche, trouver le dernier sell signal ; la X-Column voisine du sell signal = premier rebond après le sell signal et devient la Measure Column. (2) Hauteur de la Measure Column × reversal amount. (3) Ajouter au low de la colonne juste avant la Measure Column (celle qui a produit le dernier sell signal).
**TRADEX-AI C1** : Algorithme codable — diffère du Breakout par la SÉLECTION de la Measure Column (ici la X-Column de rebond adjacente au sell signal). PO_bullish = low(colonne du sell) + hauteur × 3.
*Catégorie : gestion_risque_entree*

---

### D2924 — Reversal Bullish : exemple Mosaic (hauteur 8 → PO = 64)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_06) : Exemple Mosaic (MOS), Bullish PO = 64 par la Reversal Method. La colonne voisine du sell signal = Measure Column, hauteur 8. × reversal 3 = 24, ajouté au low de la colonne avant la Measure Column : 40 + 24 = 64. (NB : le .md écrit « 40 = 24 = 64 », typo source pour « 40 + 24 = 64 ».)
**TRADEX-AI C1** : Cas numérique de référence Reversal bullish (validation). La somme 40 + 24 = 64 confirme la formule. Test unitaire possible.
*Catégorie : gestion_risque_entree*

---

### D2925 — Reversal Bullish : PO « tentative » si la X-Column de droite déclenche un buy signal
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_07) : La Reversal Method est aussi sujette à des Bullish PO « tentatives » quand la Measure Column n'est pas figée — cela survient quand la X-Column à droite du sell signal déclenche un buy signal. Exemple LyondellBasell (LYB) : sell signal (O-column, mars), reversal (X-column), buy signal en avril (red 4), colonne étendue à 94 ; si les prix montent, un X supplémentaire affectera le PO. La colonne se fige au 3-box reversal (O-Column) ; cela n'annule pas le buy signal et le PO reste valide jusqu'à un sell signal.
**TRADEX-AI C1** : État codable — flag « tentative » Reversal bullish jusqu'au 3-box reversal. Cohérent avec D2919. Le PO peut croître.
*Catégorie : gestion_risque_entree*

---

### D2926 — Reversal Method Bearish : 3 étapes + facteur 2/3 (O-Column voisine du buy signal)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_08) : Reversal Bearish (signal actif = vente). (1) De droite à gauche, trouver le dernier buy signal ; l'O-Column voisine = premier déclin après le buy signal et devient la Measure Column. (2) Hauteur × 2/3 du reversal amount. (3) Soustraire ce total du high de la colonne juste avant la Measure Column (celle qui a produit le dernier buy signal).
**TRADEX-AI C1** : Algorithme codable — miroir de D2923 avec facteur 2/3 (comme Breakout bearish). PO_bearish = high(colonne du buy) − hauteur × (2/3 × 3). Garde-fou asymétrie maintenu.
*Catégorie : gestion_risque_entree*

---

### D2927 — Reversal Bearish : exemple KLA-Tencor (hauteur 10 → PO = 50)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_09) : Exemple KLA-Tencor (KLAC) — sell signal actif. De droite à gauche, le premier buy signal montre une X-column à high 70. L'O-column suivante = Measure Column, hauteur 10, × reversal × 2/3 (10 × 3 × 2/3 = 20), soustraite du high du buy signal (70 − 20 = 50). Exemple Hewlett Packard (HPQ) : buy signal en novembre puis O-column reverseuse = Bearish PO « tentative » (O-column non figée ; un déclin sous 31 ajoute un O et ajuste le PO).
**TRADEX-AI C1** : Cas numérique de référence Reversal bearish (validation du facteur 2/3). Test unitaire possible. Flag « tentative » jusqu'à figeage.
*Catégorie : gestion_risque_entree*

---

### D2928 — MET! : objectif atteint → pas de nouveau PO avant un nouveau setup
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_10, image_11) : Quand un titre atteint son price objective, « MET! » apparaît à côté du Price Objective (coin supérieur gauche). Après avoir atteint l'objectif, aucun nouveau price objective n'apparaît tant que le titre ne génère pas un nouveau setup haussier ou baissier. Exemple Amazon : Bullish PO tentative de 375 (box 372, chaque box = 4 points couvrant 372-375), puis Bullish PO MET!.
**TRADEX-AI C1** : État codable « MET » — désactiver le PO atteint jusqu'à un nouveau signal. Note de scaling : une box de 4 points couvre une plage (ex. 372→375). Logique de cycle d'objectif.
*Catégorie : gestion_risque_entree*

---

### D2929 — Takeaway : PO = guides, croiser avec d'autres outils (bar chart / indicateurs)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md) : Les Price Objectives donnent une cible générale basée sur la longueur verticale de la Measure Column (plus longue = PO plus haut/bas). Tout PO (Reversal, Breakout ou autre) est à prendre avec prudence — des guides larges. Les titres n'atteignent pas toujours leur cible ; certains se retournent et déclenchent des signaux P&F contradictoires avant. Un signal + une cible ne sont qu'un point de départ : surveiller la formation, et employer d'autres outils AT (analyse de tendance sur bar chart, indicateurs) pour confirmer/réfuter.
**TRADEX-AI C1** : Garde-fou de synthèse — PO indicatif, à confirmer/réfuter par d'autres cercles (bar chart, indicateurs). Aucune exécution automatique sur PO seul.
*Catégorie : gestion_risque_entree*

---

### D2930 — Activation : sélecteur Reversal/Breakout dans SharpCharts + scans prédéfinis
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_price_objectives_breakout_and_reversal_method.md, image_12) : Les utilisateurs StockCharts accèdent aux P&F Price Objectives en sélectionnant Reversal ou Breakout dans la liste « Price Objective » (sous le chart, à droite) puis « update » ; le PO de la méthode choisie apparaît. Les signaux de patterns P&F figurent au bas de la Predefined Scans Page (plus de 15 patterns P&F). Le livre de Dorsey *Point & Figure Charting* est cité comme référence (force relative, rotation sectorielle, ETFs).
**TRADEX-AI C1** : Métadonnée outil — paramétrage de la méthode de PO (UI StockCharts) et existence de scans P&F prédéfinis (>15 patterns). Référence Dorsey pour enrichissement. Pas une règle de trading directe.
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2911 → D2930 (20) |
| Images certifiées | 12/12 |
| Cercle | C1 (structure de marché / prix) |
| Catégories | gestion_risque_entree (15) · structure_marche (1) · signal (1) · configuration (3) |
| Actifs concernés | GC · HG · CL · ZW (méthodes d'objectif P&F génériques) |
| Lien Belkhayate | NON CONCERNÉ (P&F = méthode Cohen/Dorsey, hors corpus Belkhayate) |
| Tags utilisés | 🟢 FAIT VÉRIFIÉ (17) · 🔵 ÉCOLE (3) |
| Cas à vérifier | (1) Typo source au D2924 : le .md écrit « 40 = 24 = 64 » pour « 40 + 24 = 64 » — interprété et signalé, valeur correcte 64. (2) Asymétrie haussier/baissier (facteur 2/3 baissier, D2920/D2926) à respecter strictement au codage. (3) image_08 ancrée par SECTION-FALLBACK (légende vide en source) — certifiée par section, label = nom de section. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
