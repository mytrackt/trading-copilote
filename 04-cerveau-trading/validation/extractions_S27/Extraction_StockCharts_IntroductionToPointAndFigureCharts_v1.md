# Extraction StockCharts — Introduction to Point & Figure Charts
**Source :** `bundles/stockcharts/introduction_to_point_and_figure_charts.md` (HTTP 200 · ~21 500 car.) + 18 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 18/18 certifiées
**Décisions :** D2291 → D2310 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics/introduction-to-point-and-figure-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | P&F chart of AMZN | Creating a P&F Chart | CERTIFIE (accord .md + HTML) |
| image_02.png | Box Scaling | Box Scaling [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Example of a P&F chart showing action during different months | Month Markings | CERTIFIE (accord .md + HTML) |
| image_04.png | A P&F chart using the high/low method | High-Low Method | CERTIFIE (accord .md + HTML) |
| image_05.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_10.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_11.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_12.png | P&F Chart Construction Example | P&F Chart Construction Example [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_13.png | Basic P&F Analysis | Basic P&F Analysis [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_14.png | Basic P&F Analysis | Basic P&F Analysis [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_15.png | Basic P&F Analysis | Basic P&F Analysis [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_16.png | Basic P&F Analysis | Basic P&F Analysis [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_17.png | P&F pattern scans available in StockCharts.com | P&F Scans | CERTIFIE (accord .md + HTML) |
| image_18.png | The P&F scan component available in StockCharts.com | P&F Scans | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2291 — Définition : P&F = colonnes de X et O représentant des mouvements de prix filtrés
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_01) : « Point & Figure charts consist of columns of X's and O's that represent filtered price movements. X-Columns represent rising prices and O-Columns represent falling prices. Each price box represents a specific value that price must reach to warrant an X or an O. Time is not a factor in P&F charting; these charts evolve as prices move. No movement in price means no change in the P&F chart. »
**TRADEX-AI C1** : Représentation de prix alternative qui filtre le bruit et supprime l'axe temps — X = hausse, O = baisse. Outil structurel candidat pour visualiser support/résistance sur GC/HG/CL/ZW, indépendant des range bars NT8.
*Catégorie : structure_marche*
---

### D2292 — Méthode standard : reversal 3 cases (3-box Reversal Method)
🟡 **CONVENTION** (Source : introduction_to_point_and_figure_charts.md) : « The 3-box Reversal Method is the most popular P&F charting method. In classic 3-box reversal charts, column reversals are further filtered requiring a 3-box minimum to reverse the current column. Articles in the StockCharts.com ChartSchool are based on this method. »
**TRADEX-AI C1** : Convention de référence — il faut un mouvement minimum de 3 cases en sens inverse pour ouvrir une nouvelle colonne. Baseline de paramétrage avant adaptation aux actifs TRADEX.
*Catégorie : structure_marche*
---

### D2293 — Avantages revendiqués du P&F (5 points)
🔵 **ÉCOLE** (StockCharts / A.W. Cohen) (Source : introduction_to_point_and_figure_charts.md) : « P&F charts: Filter insignificant price movements and noise · Focus on important price movements · Remove the time aspect from the analysis process · Make support/resistance levels much easier to identify · Provide automatic and subjective trend lines »
**TRADEX-AI C1** : Bénéfices selon l'école P&F — filtrage du bruit, focalisation sur les mouvements significatifs, lecture facilitée des supports/résistances et lignes de tendance automatiques. Revendications d'école, à valider sur nos actifs.
*Catégorie : structure_marche*
---

### D2294 — Box Size et Reversal Amount : les deux réglages fondamentaux
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_02) : « Each chart has a setting called the Box Size, which defines the price range for each box. Each chart has a second setting called the Reversal Amount, which determines the amount a stock needs to move in the opposite direction to warrant a column reversal. Whenever this reversal threshold is crossed, a new column is started right next to the previous one, but moving in the opposite direction. »
**TRADEX-AI C1** : Deux paramètres à coder — Box Size (taille de case = plage de prix) et Reversal Amount (nombre de cases pour inverser). Définissent entièrement la granularité du graphe P&F.
*Catégorie : structure_marche*
---

### D2295 — Distance de reversal = Box Size × Reversal Amount
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « The "reversal distance" is the box size multiplied by the reversal amount. A box size of one and the reversal amount of three would require a three-point move to warrant a reversal (1 x 3). An X-Column extends as long as price does not move down more than the "reversal distance." »
**TRADEX-AI C1** : Formule exacte codable — reversal_distance = box_size × reversal_amount. Une colonne X se prolonge tant que le prix ne recule pas de cette distance.
*Catégorie : structure_marche*
---

### D2296 — Quatre méthodes de Box Scaling (traditional, percentage, dynamic ATR, user-defined)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « The P&F charts at StockCharts.com allow users to select traditional, percentage, dynamic (ATR), or user-defined box scaling. Traditional box scaling uses a predefined table of price ranges... Percentage box scaling uses box sizes that are a fixed percentage of the stock's price... Dynamic (ATR) scaling bases the box size on the daily Average True Range (ATR). The default is set at 20 days... User-defined box scaling allows users to set the box size. »
**TRADEX-AI C1** : Quatre modes de calibrage de case à implémenter. Le mode Dynamic (ATR 20j) est pertinent pour des actifs volatils (GC/CL) mais ATTENTION : les signaux antérieurs peuvent disparaître quand l'ATR change la taille de case.
*Catégorie : structure_marche*
---

### D2297 — Trade-off taille de case : grande case = plus de filtrage, moins de reversals
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « A larger box size will result in more filtered price movements and fewer reversals. A smaller box size will result in less filtered price movements and more reversals. »
**TRADEX-AI C1** : Règle de sensibilité — case large = signaux rares/lissés ; case étroite = signaux fréquents/bruités. Paramètre d'arbitrage sensibilité/robustesse à régler par actif.
*Catégorie : structure_marche*
---

### D2298 — Month Markings : temps non linéaire, repères mensuels par chiffres/lettres
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_03) : « P&F charts do not show time linearly... Numbers and letters on the chart indicate when a new month has begun. For instance, the number "2" shows where February started. The letters "A," "B," and "C" are used to indicate the beginning of October, November, and December. »
**TRADEX-AI C1** : Le temps est marqué par chiffres (1–9 = janv–sept) et lettres (A/B/C = oct/nov/déc) sur la colonne en cours. Repère de datation, non un axe temps régulier.
*Catégorie : structure_marche*
---

### D2299 — High-Low Method : règles de sélection du prix (X-Column montante)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_04) : « When the current column is an X-Column (rising): Use the high when another X can be drawn and then ignore the low. Use the low when another X cannot be drawn and the low triggers a 3-box reversal. Ignore both when the high does not warrant another X and the low does not trigger a 3-box reversal. »
**TRADEX-AI C1** : Algorithme de décision en colonne montante — priorité au high pour prolonger la colonne ; sinon test du low pour reversal 3 cases ; sinon aucune action. Logique de mise à jour barre par barre à coder.
*Catégorie : structure_marche*
---

### D2300 — High-Low Method : règles de sélection du prix (O-Column descendante)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « When the current column is an O-Column (falling): Use the low when another O can be drawn and then ignore the high. Use the high when another O cannot be drawn and the high triggers a 3-box reversal. Ignore both when the low does not warrant another O and the high does not trigger a 3-box reversal. »
**TRADEX-AI C1** : Algorithme symétrique en colonne descendante — priorité au low pour prolonger ; sinon test du high pour reversal ; sinon rien. Complète D2299 pour une implémentation complète High-Low.
*Catégorie : structure_marche*
---

### D2301 — Varying Box Ranges : une case = plage, asymétrique selon X ou O
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « A P&F Box does not represent a single price, but rather a price range... For a rising X-Column... a box marked with a 12 would range from 12 to 12.99... It works a little differently when the current column is a falling O-Column. A move to 12 would warrant an O in the 12 box. This O would remain as long as prices range from 11.01 to 12. »
**TRADEX-AI C1** : Subtilité d'implémentation — la plage d'une case dépend de la direction : X(12) = [12 ; 12.99], O(12) = [11.01 ; 12]. À coder précisément pour éviter les erreurs de placement de case.
*Catégorie : structure_marche*
---

### D2302 — Reversal X→O : exemple chiffré (high ≥ box + reversal_distance)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_08) : « Day 4 High = 14.10... We then see if the high is greater than or equal to current box value (11) plus the reversal distance (3). The high is 14.10, which is greater than the current box value plus the reversal distance (11 + 3 = 14). This means a three box reversal is warranted and we add three X's starting one above the low of the previous column. »
**TRADEX-AI C1** : Condition de reversal haussier codable — si high ≥ box_value + reversal_distance, ouvrir colonne X de 3 cases en partant d'une case au-dessus du plus bas de la colonne précédente.
*Catégorie : signal*
---

### D2303 — Reversal O→X : exemple chiffré (low ≤ box − reversal_distance)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_12) : « Day 6 High = 15.90; Low = 12.00... See if the low is less than or equal to current box value (15) less the reversal distance (3). The low is 12.00, which is less than the current box value less the reversal distance (15 - 3 = 12). This means a three-box reversal is warranted and we add three O's starting one below the high of the previous column. »
**TRADEX-AI C1** : Condition de reversal baissier symétrique — si low ≤ box_value − reversal_distance, ouvrir colonne O de 3 cases en partant d'une case sous le plus haut de la colonne précédente. Complète D2302.
*Catégorie : signal*
---

### D2304 — Chaque marque P&F est significative (temps non linéaire)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « P&F charts do not show time in a linear fashion. Each column can represent one day, or many days, depending on the price movement. Because P&F charts filter out the noise associated with more traditional charting methods, every mark on the chart is significant. »
**TRADEX-AI C1** : Propriété structurelle — l'absence d'axe temps régulier signifie que chaque X/O traduit un mouvement réel filtré. Aucune barre « vide » de bruit.
*Catégorie : structure_marche*
---

### D2305 — Quatre éléments d'analyse de base : support, résistance, lignes haussières/baissières
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « There are four things to look for on a Point & Figure chart: Support levels · Resistance levels · Upward trend lines · Downward trend lines. »
**TRADEX-AI C1** : Grille de lecture P&F en 4 axes — supports, résistances, lignes de tendance haussières et baissières. Cadre d'analyse de base à exploiter en confirmation.
*Catégorie : structure_marche*
---

### D2306 — Support / résistance P&F : O-lows égaux = support, X-highs égaux = résistance
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_13) : « Support is the price level at which demand is thought to be strong enough to prevent the price from declining further... a sequence of O-Columns with equal lows marks a clear support level. Resistance is the price level at which selling is thought to be strong enough to prevent the price from rising further... a sequence of X-Columns with equal highs marks a clear resistance level. »
**TRADEX-AI C1** : Détection objective et codable — support = suite de colonnes O à bas égaux ; résistance = suite de colonnes X à hauts égaux. Niveaux exploitables comme zones de décision sur GC/HG/CL/ZW.
*Catégorie : structure_marche*
---

### D2307 — Bullish Support Line (45°) et séquence 5-3 nécessaire
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_15) : « An upward-sloping trend line is called a Bullish Support Line... Bullish Support Lines slope up at 45 degrees and start from an important low. At a minimum, it takes a column sequence of 5-3-5-3-5-3 to produce an advance steep enough to maintain this angle. X-Columns need to be at least 5 boxes with O-Columns a maximum of 3 boxes. »
**TRADEX-AI C1** : Ligne de tendance haussière automatique à 45° depuis un plus bas important ; structure minimale X≥5 / O≤3. Critère géométrique objectif de tendance haussière.
*Catégorie : indicateurs_tendance*
---

### D2308 — Bearish Resistance Line (135°) et séquence 5-3 symétrique
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_16) : « Bearish Resistance Lines slope down at 135 degrees (180 - 45 = 135) and start from an important high... A column sequence of 5-3-5-3-5-3 is needed to maintain the slope. O-Columns need to be at least 5 boxes with X-Columns a maximum of 3 boxes. »
**TRADEX-AI C1** : Ligne de tendance baissière automatique à 135° depuis un plus haut important ; structure minimale O≥5 / X≤3. Symétrique de D2307, critère objectif de tendance baissière.
*Catégorie : indicateurs_tendance*
---

### D2309 — P&F Pattern Scans : alertes quotidiennes sur 15+ patterns (Triple Top Breakout, etc.)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md, image_17, image_18) : « StockCharts.com provides daily alerts for over 15 P&F patterns on various exchanges... there were over 100 NYSE stocks with Triple Top Breakouts. Chartists can also scan for specific P&F patterns using daily data... Over 20 P&F patterns and criteria are included in this drop-down menu. »
**TRADEX-AI C3** : Existence d'un catalogue de patterns P&F (Triple Top Breakout, etc.) scannables sur données quotidiennes. Source d'idées de configurations de confirmation, non un signal d'ordre direct.
*Catégorie : signal*
---

### D2310 — Price Objectives P&F : Horizontal Count et Vertical Count
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_point_and_figure_charts.md) : « Chartists may also wish to calculate Price Objectives using the Horizontal or Vertical Count... [Horizontal Count] [Vertical Count] » et « StockCharts.com computes Price Objectives based on specific Point & Figure charts. »
**TRADEX-AI C3** : Les graphes P&F fournissent des objectifs de prix calculés (Horizontal/Vertical Count) — utiles comme niveaux de cible (take-profit) en confirmation. Méthodes détaillées dans des articles séparés (hors périmètre de cette page).
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie |
|---|----------|-----|--------|-----------|
| D2291 | Définition P&F (colonnes X/O filtrées, pas de temps) | 🟢 | C1 | structure_marche |
| D2292 | Méthode standard reversal 3 cases | 🟡 | C1 | structure_marche |
| D2293 | 5 avantages revendiqués du P&F | 🔵 | C1 | structure_marche |
| D2294 | Box Size + Reversal Amount (2 réglages) | 🟢 | C1 | structure_marche |
| D2295 | Reversal distance = box × reversal amount | 🟢 | C1 | structure_marche |
| D2296 | 4 modes de box scaling (dont ATR 20j) | 🟢 | C1 | structure_marche |
| D2297 | Trade-off taille de case sensibilité/filtrage | 🟢 | C1 | structure_marche |
| D2298 | Month markings (temps non linéaire) | 🟢 | C1 | structure_marche |
| D2299 | High-Low Method (colonne X montante) | 🟢 | C1 | structure_marche |
| D2300 | High-Low Method (colonne O descendante) | 🟢 | C1 | structure_marche |
| D2301 | Plages de case asymétriques X vs O | 🟢 | C1 | structure_marche |
| D2302 | Reversal X→O (high ≥ box + distance) | 🟢 | C1 | signal |
| D2303 | Reversal O→X (low ≤ box − distance) | 🟢 | C1 | signal |
| D2304 | Chaque marque P&F significative | 🟢 | C1 | structure_marche |
| D2305 | 4 éléments d'analyse de base | 🟢 | C1 | structure_marche |
| D2306 | Support O-lows égaux / résistance X-highs égaux | 🟢 | C1 | structure_marche |
| D2307 | Bullish Support Line 45° (séquence 5-3) | 🟢 | C1 | indicateurs_tendance |
| D2308 | Bearish Resistance Line 135° (séquence 5-3) | 🟢 | C1 | indicateurs_tendance |
| D2309 | P&F Pattern Scans (15+ patterns) | 🟢 | C3 | signal |
| D2310 | Price Objectives (Horizontal/Vertical Count) | 🟢 | C3 | gestion_risque_entree |

**Lien Belkhayate :** NON CONCERNÉ (méthode de graphage Point & Figure indépendante ; ne touche ni aux pivots Belkhayate, ni au BGC, ni à l'Énergie/MFI de la méthode verrouillée). Outil structurel auxiliaire éventuel pour support/résistance.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, non fusionnée dans KNOWLEDGE_BASE_MASTER.json.
