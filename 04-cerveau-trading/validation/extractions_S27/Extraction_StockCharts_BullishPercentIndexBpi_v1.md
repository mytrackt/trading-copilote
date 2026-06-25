# Extraction StockCharts — Bullish Percent Index (BPI)
**Source :** `bundles/stockcharts/bullish_percent_index_bpi.md` (HTTP 200 · ~9 100 car.) + 8 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 8/8 certifiées
**Décisions :** D971 → D984 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/bullish-percent-index-bpi
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : le BPI est un indicateur de **largeur de marché actions** (breadth, basé sur les signaux P&F des composantes d'un indice). Pertinence DIRECTE LIMITÉE pour le trading futures GC/HG/CL/ZW (pas de « composantes »). Rôle utile = cercle C5 (sentiment/contexte marché), via les indices ES/$SPX, jamais comme déclencheur d'ordre sur une matière première.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Bullish Percent Index - Chart 1 | P&F Patterns | CERTIFIE (accord .md + HTML) |
| image_02.png | Bullish Percent Index - Chart 2 | P&F Patterns | CERTIFIE (accord .md + HTML) |
| image_03.png | Bullish Percent Index - Chart 3 | Bull/Bear Alert | CERTIFIE (accord .md + HTML) |
| image_04.png | Bullish Percent Index - Chart 4 | Bull/Bear Confirmed | CERTIFIE (accord .md + HTML) |
| image_05.png | Bullish Percent Index - Chart 5 | Bull/Bear Confirmed | CERTIFIE (accord .md + HTML) |
| image_06.png | Bullish Percent Index - Chart 6 | Bull/Bear Correction | CERTIFIE (accord .md + HTML) |
| image_07.png | Bullish Percent Index - Chart 7 | Bull/Bear Correction | CERTIFIE (accord .md + HTML) |
| image_08.png | Bullish Percent Index - SharpCharts | SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D971 — Nature et origine du Bullish Percent Index
🔵 **ÉCOLE (Cohen/Blumenthal/Burke)** (Source : bullish_percent_index_bpi.md) : Le BPI est un indicateur de largeur (breadth) basé sur le nombre d'actions sur signaux d'achat Point & Figure au sein d'un indice. Il révèle la santé interne d'un indice. Développé par Abe Cohen au milieu des années 1950 (initialement sur actions NYSE) ; Cohen fut le premier éditeur de ChartCraft (devenu Investors Intelligence). Earl Blumenthal a affiné les signaux au milieu des années 70, Mike Burke au début des années 80. Comme une action est soit sur un signal P&F d'achat soit de vente, il n'y a aucune ambiguïté ; six signaux : bull/bear confirmed, bull/bear alerts, bull/bear correction.
**TRADEX-AI C5** : Indicateur de breadth d'indice ; utilisable comme contexte sentiment via ES/$SPX, NON applicable à un futures de matière première isolé.
*Catégorie : indicateurs_momentum*

---

### D972 — Calcul du BPI
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md) : Calcul simple :
```
Number of stocks on P&F Buy signals / total number of stocks
```
Les calculs utilisent un dimensionnement de boîtes traditionnel et des charts P&F à renversement de 3 boîtes (3-box reversal).
**TRADEX-AI C5** : Formule déterministe mais nécessite un univers d'actions composantes (inexistant pour GC/HG/CL/ZW) ; calculable seulement sur indices comme $BPSPX.
*Catégorie : indicateurs_momentum*

---

### D973 — Signaux P&F sous-jacents (Buy / Sell)
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_01) : Parmi la douzaine de signaux P&F, seuls deux comptent pour le BPI. Les X représentent les colonnes en progression, les O les colonnes en déclin ; les colonnes alternent à chaque renversement. Un signal P&F d'achat (Buy) survient quand une colonne de X dépasse la colonne de X précédente. Un signal P&F de vente (Sell) survient quand une colonne de O dépasse la colonne de O précédente.
**TRADEX-AI C5** : Définition binaire sans ambiguïté ; base logique du décompte breadth.
*Catégorie : signal*

---

### D974 — Échelle P&F 3-box / boîte de 2% / renversement 6%
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_02) : StockCharts utilise des charts P&F 3-box reversal pour les BPI. Chaque boîte représente 2%. Il faut donc au moins un mouvement de 6% du BPI pour un renversement (3 × 2% = 6%) — par ex. de 42% à 48% ou de 64% à 58%. Ce 6% ne désigne pas le changement de pourcentage réel. Une colonne de O ne se renverse qu'avec une avance de 6% (nouvelle colonne de 3 X) ; une colonne de X qu'avec un déclin de 6% (nouvelle colonne de 3 O).
**TRADEX-AI C5** : Mécanique de renversement codable (seuil 6% / 3 boîtes de 2%) si univers d'actions disponible.
*Catégorie : indicateurs_momentum*

---

### D975 — Plage 0-100% et dépendance au nombre de composantes
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md) : Le BPI fluctue entre 0% et 100%. Sa plage et sa volatilité dépendent du nombre d'actions de l'indice sous-jacent. Un indice de 30 actions ou moins (Gold Miners Index, Dow Industrials, Dow Transports) peut atteindre 0% ou 100%. Les indices de plus de 2000 actions (Nasdaq, NYSE) ne les atteignent quasiment jamais. Moins d'actions = plus de volatilité (il faut moins d'actions pour bouger le BPI).
**TRADEX-AI C5** : Volatilité du BPI dépendante de l'indice ; à interpréter relativement selon l'univers ($BPSPX vs $BPGDM).
*Catégorie : indicateurs_momentum*

---

### D976 — Seuils de base : 50% (biais), 70% (surachat), 30% (survente)
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md) : Dans sa forme la plus simple, le BPI favorise les haussiers au-dessus de 50% et les baissiers en-dessous de 50% (les haussiers ont l'avantage quand >50% des actions sont sur signal P&F d'achat). Le BPI est considéré suracheté au-dessus de 70% et survendu en-dessous de 30%. Cohen, Blumenthal et Burke utilisaient aussi des niveaux précis : 30%, 49%, 50%, 52%, 68%, 70%.
**TRADEX-AI C5** : Seuils 30/50/70 utilisables comme jauge de sentiment de marché actions ; transposables uniquement aux indices, pas aux futures matières premières.
*Catégorie : signal*

---

### D977 — Bull Alert et Bear Alert
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_03) : **Bull Alert** : le BPI est sous 30% (survente généralisée) PUIS forme une nouvelle colonne de X (rebond ≥ 6%) — la largeur s'améliore depuis des conditions de survente ; peut préfigurer un creux (ex. oct 2002, mars 2003, mars 2009 sur $BPNYA). Le BPI doit être survendu ET commencer à monter (pas seulement survendu). **Bear Alert** (inverse) : le BPI dépasse 70% (surachat) PUIS un déclin de 6% forme une nouvelle colonne de O — alerte de faiblesse possible (pas un signal de vente ; ex. juillet 2007 a préfiguré de plus grands déclins).
**TRADEX-AI C5** : Signaux d'alerte de retournement de breadth ; contexte de sentiment, jamais ordre direct.
*Catégorie : signal*

---

### D978 — Bull Confirmed et Bear Confirmed
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_04, image_05) : **Bull Confirmed** : signal le plus fort — BPI sur un signal P&F d'achat ET en hausse (colonne de X à l'extrême droite ; un achat = colonne de X dépassant le plus haut de la colonne de X précédente, soit un plus haut plus haut). Reste en vigueur jusqu'à ce qu'une colonne de O dépasse le bas de la colonne de O précédente (signal P&F de vente). Exemple Nasdaq ($BPCOMPQ) : achat P&F déc 2009, Bull Confirmed au rebond. **Bear Confirmed** : signal le plus faible — BPI sur signal P&F de vente ET en baisse ; reste en vigueur jusqu'à annulation par un achat. Exemple Consumer Discretionary ($BPDISC) août 2010.
**TRADEX-AI C5** : États de tendance de breadth (confirmé) ; le plus fiable des six états pour qualifier le régime du marché actions.
*Catégorie : signal*

---

### D979 — Bull Correction et Bear Correction
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_06, image_07) : **Bull Correction** : BPI sur signal P&F d'achat MAIS en déclin (colonne de O courante) — correction après un achat ; le signal d'achat reste en vigueur jusqu'à renversement. Exemple $BPOEX (S&P 100) : achat juillet 2010, pic ~66%, déclin sous 50%. **Bear Correction** : BPI sur signal P&F de vente MAIS en hausse (colonne de X courante) — toute avance reste une correction jusqu'à cassure annulant la vente. Exemple $BPINDU (Dow) : vente en mai, trois tentatives de rallye échouées à casser le plus haut.
**TRADEX-AI C5** : États intermédiaires (correction dans une tendance breadth) ; nuance le sentiment sans inverser le biais dominant.
*Catégorie : signal*

---

### D980 — Synthèse opératoire (The Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md) : Le BPI sert plusieurs profils : les chasseurs de creux cherchent des renversements haussiers sous 30%, les chasseurs de sommets des renversements baissiers au-dessus de 70% (entrées plus risquées car tops/bottoms peuvent s'étendre). Les suiveurs de tendance cherchent des renversements haussiers au-dessus de 50% (biais haussier déjà présent quand >50% des actions sont sur achat P&F). Les traders peuvent définir un biais directionnel via le BPI avant de sélectionner actions/ETF : signaux d'achat préférés quand le BPI favorise les haussiers, signaux de vente quand il favorise les baissiers. Utiliser le BPI avec d'autres indicateurs est important.
**TRADEX-AI C5** : BPI = filtre de biais de marché (risk-on / risk-off) ; à utiliser comme toile de fond, jamais comme générateur d'ordre isolé.
*Catégorie : signal*

---

### D981 — Symboles disponibles (univers de calcul StockCharts)
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md) : StockCharts calcule et publie les Bullish Percent Indices pour 7 indices majeurs, 11 secteurs et 2 groupes industriels. Ces indicateurs sont calculés en fin de séance, d'où le « (EOD) » dans leur nom. Visualisables en CandleGlance prédéfinis (Major BPI, Sector BPI) ou en charts individuels.
**TRADEX-AI C5** : Données EOD (fin de journée), donc latence d'un jour ; incompatible avec la surveillance temps réel 2s du moteur — usage contextuel uniquement.
*Catégorie : timing*

---

### D982 — Affichage SharpCharts (ligne ou P&F)
🟢 **FAIT VÉRIFIÉ** (Source : bullish_percent_index_bpi.md, image_08) : Les BPI se visualisent en charts en ligne « close-only » ou en charts P&F. En mode ligne, on peut ajouter des indicateurs ou des types « close only » (Renko, Kagi). En mode P&F, le « statut » s'affiche en haut (Bull Confirmed, Bear Correction, Bull Alert, etc.), facilitant la lecture de l'état courant.
**TRADEX-AI C5** : Le « statut » P&F fournit directement l'état des six signaux ; exploitable comme champ catégoriel si une source de données BPI est branchée.
*Catégorie : signal*

---

### D983 — Référence bibliographique (Dorsey, P&F Charting)
🟡 **CONVENTION** (Source : bullish_percent_index_bpi.md) : Pour approfondir, le livre *Point & Figure Charting* de Thomas Dorsey décrit pas à pas la création, la maintenance et l'interprétation des charts P&F (marchés, secteurs, titres individuels) et leur usage pour suivre/prévoir les prix et bâtir une stratégie.
**TRADEX-AI C5** : Référence externe (hors périmètre code) ; aucune règle directement implémentable.
*Catégorie : indicateurs_momentum*

---

### D984 — Limite d'applicabilité au périmètre TRADEX-AI (synthèse critique)
🔴 **NON VÉRIFIÉ (transposition futures)** (Source : déduction d'extraction, non littéral) : Le BPI repose intégralement sur un univers d'actions composantes et des signaux P&F EOD. Les actifs TRADING du système (GC/HG/CL/ZW) sont des futures individuels SANS composantes : le BPI ne s'y calcule PAS directement. Sa seule pertinence est comme proxy de sentiment via les indices actions (ES/$SPX → $BPSPX) dans le cercle C5, en données EOD (latence ≥ 1 jour).
**TRADEX-AI C5** : Marquer le BPI comme indicateur de CONTEXTE sentiment optionnel, EOD, applicable uniquement à ES/DX/VX-adjacents ; exclure de tout calcul direct sur matières premières et de toute logique temps réel.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D971 | Nature et origine BPI | 🔵 ÉCOLE | C5 | indicateurs_momentum |
| D972 | Calcul du BPI | 🟢 | C5 | indicateurs_momentum |
| D973 | Signaux P&F Buy/Sell | 🟢 | C5 | signal |
| D974 | Échelle 3-box / 2% / renversement 6% | 🟢 | C5 | indicateurs_momentum |
| D975 | Plage 0-100% / dépendance composantes | 🟢 | C5 | indicateurs_momentum |
| D976 | Seuils 30/50/70 | 🟢 | C5 | signal |
| D977 | Bull Alert / Bear Alert | 🟢 | C5 | signal |
| D978 | Bull Confirmed / Bear Confirmed | 🟢 | C5 | signal |
| D979 | Bull Correction / Bear Correction | 🟢 | C5 | signal |
| D980 | Synthèse opératoire | 🟢 | C5 | signal |
| D981 | Symboles disponibles (EOD) | 🟢 | C5 | timing |
| D982 | Affichage SharpCharts / statut P&F | 🟢 | C5 | signal |
| D983 | Référence Dorsey | 🟡 CONVENTION | C5 | indicateurs_momentum |
| D984 | Limite d'applicabilité futures | 🔴 NON VÉRIFIÉ | C5 | signal |

**Liens Belkhayate :** Le BPI n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct : la méthode Belkhayate s'applique à un actif/futures isolé, pas à une largeur d'indice. Le BPI ne peut intervenir que comme toile de fond sentiment du marché actions (C5), jamais dans l'analyse Pivots/BGC/Direction/Énergie d'une matière première.

**À vérifier (humain) :**
- D984 — **point critique** : confirmer que le BPI n'entre PAS dans la grille de score /10 des actifs TRADING (GC/HG/CL/ZW). Risque de mauvaise application si quelqu'un tente de le calculer sur un futures isolé (impossible : pas de composantes).
- D981 — données EOD : incompatibles avec la surveillance 2s ; n'utiliser que comme contexte journalier si une source $BPSPX est ajoutée.
- Pertinence générale LIMITÉE pour le périmètre futures : à classer « optionnel / contexte C5 » lors d'une éventuelle fusion KB, pas comme brique de signal.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
