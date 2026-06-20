# Extraction KB — ChartSchool : Technical Analysis 101 (Parts 1 à 6)
**Sources :**
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-1
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-2
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-3
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-4
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-5
- https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-6

**Version :** v1 enrichie (texte intégral 6 pages + 17 images analysées)
**Date extraction :** 20/06/2026
**Tagger :** Claude Sonnet 4.6
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)
**Pertinence TRADEX :** 🟡 MODÉRÉE — Fondations conceptuelles + anatomie des charts + scaling critique pour trendlines long terme
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS
| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur chart/source |
| 🔵 | Règle générale ChartSchool |
| 🟡 | Application TRADEX déduite |
| ⏳ | À implémenter |

---

## PARTIE 1 — DÉFINITION ET PHILOSOPHIE DE L'ANALYSE TECHNIQUE

### 1.1 Définition fondamentale

🔵 **L'analyse technique = étude des variations de prix et de volume dans le temps.** Elle utilise des graphiques financiers comme outil principal.

🔵 **L'AT étudie le comportement humain** — spécifiquement la réaction collective à la peur et à la cupidité. Le prix d'une action reflète l'état émotionnel des investisseurs qui constituent "le marché" pour ce titre.

🔵 **Citation TA-101 Part 1 :** *"A stock's price change over time is the most accurate record of the emotional state — fear and greed — of the market for that stock."*

### 1.2 Analogie météorologique (limites de l'AT)

🔵 **L'AT ressemble à la météorologie :**
- Prépare pour ce qui est **probable**, pas pour ce qui est **certain**
- Les deux disciplines utilisent des données mesurées (prix/volume pour l'AT, température/pression pour la météo) pour inférer des facteurs causaux
- Les deux font appel à l'**expérience et l'intuition** du praticien
- Les deux sont plus fiables en **conditions stables** (marché en tendance claire) qu'en rupture soudaine
- Les deux fonctionnent mieux à une **échelle intermédiaire** : trop granulaire (seconde par seconde) = difficile ; trop global = inutile
- Les prévisions **journalières et hebdomadaires** sont plus fiables que l'intraday seconde par seconde

🔵 **Implication TRADEX :** un signal COG Belkhayate = probabilité, pas certitude. Le circuit breaker et le News Gate existent précisément pour les cas où "les conditions changent de manière imprévisible."

---

## PARTIE 2 — VALEUR ET USAGES CORRECTS DE L'AT

### 2.1 Pourquoi l'AT fonctionne

🔵 **Les mouvements de prix directionnels sont souvent soutenus dans le temps** → permet de les détecter et d'en profiter.

🔵 **L'AT répond à 3 questions fondamentales :**
1. **Quoi** investir ?
2. **Quand** acheter ?
3. **Quand** vendre ?

🔵 **L'AT réduit l'émotion** en établissant des règles "quoi et quand" à suivre systématiquement. Le trader sait toujours combien de risque il prend et quand sortir.

🔵 **Citation TA-101 Part 2 :** *"Rather than buying and hoping for the best, technical analysts always know how much risk they are taking and know when to get out while the getting is good."*

### 2.2 Données utilisées

🔵 **Seules les données historiques de prix et de volume** sont utilisées. Tout ce qui est connu (fondamentaux, résultats, ratings, management, politique, news) est considéré **déjà reflété dans le prix**.

🔵 **L'AT ne peut pas anticiper** les news events ni la réaction des investisseurs à ces événements.

🟡 **Application TRADEX :** cette philosophie justifie le News Gate. Avant une news majeure, le prix n'a pas encore intégré l'événement → les signaux AT sont invalides jusqu'à ce que le chart "se stabilise".

### 2.3 L'objectif de l'AT — Illustration ADI

🟢 **Chart ADI (Analog Devices) Daily (29-Jul-2008) :**
- Trois cercles annotés sur le chart :
  - **Cercle rouge (oct 2007) :** *"Beginning to move down - SELL"* → signal de vente
  - **Cercle vert (avr 2008) :** *"Beginning to move up - BUY"* → signal d'achat
  - **Cercle rouge (juil 2008) :** *"Beginning to move down - SELL"* → signal de vente
- Prix ADI 29-Jul-2008 : 22.22

🔵 **L'objectif de l'AT :** acheter quand le chart indique que les prix commencent à monter, vendre quand il indique qu'ils commencent à stagner ou baisser.

### 2.4 Abus et erreurs à éviter

🔵 **Le mythe du "système parfait" (Holy Grail) :**
- Un système de trading qui génère des profits constants avec peu de risque N'EXISTE PAS
- Le marché = personnes avec libre arbitre guidées par peur et cupidité → imprévisible par définition
- Les institutions financières détectent et exploitent les systèmes mécaniques systématiques → les neutralisent

🔵 **Méfiance des "Market Gurus" :** les vrais gurus comme Warren Buffet sont rarissimes et prouvent leur valeur sur des décennies, pas sur quelques coups chanceux.

🔴 **Erreurs émotionnelles à éviter :**
- "Ma trendline vient d'être cassée, mais ça va revenir..." (déni)
- "Ma trendline a été cassée ! L'AT ne vaut rien !" (abandon émotionnel)
- Les deux réponses sont guidées par l'émotion que l'AT cherche à éliminer.

---

## PARTIE 3 — DONNÉES ET HYPOTHÈSES CLÉS

### 3.1 Types de données

🔵 **Données de prix (tick data) :**
- Compilées sur différentes périodes → price bars (1 min, 5 min, 15 min, 30 min, 1h, journalier, hebdomadaire, mensuel)
- Chaque barre = Open + High + Low + Close + Volume pour la période

🔵 **Données d'indices :** non tradables, représentent des moyennes de marché, secteurs, commodités, devises, obligations. Ex : $INDU (Dow Jones), $NZD (New Zealand Dollar), $NAAD (NASDAQ Advance-Decline).

🔵 **Données de breadth :** mesurent combien d'instruments bougent dans un indice donné. Donnent des insights sur le sentiment des investisseurs.

### 3.2 Les 3 Hypothèses Clés (avant d'appliquer l'AT)

🔵 **H1 — Liquidité élevée :**
- L'actif doit être activement échangé pour que les signaux AT soient valides
- Actifs peu liquides : prix manipulables, exécution difficile (spread énorme), AT non fiable
- MSFT : très liquide → l'achat de 100 actions n'affecte pas le prix
- Actions < 1 centime : souvent manipulées → AT inutilisable

🔵 **H2 — Pas de changements de prix artificiels :**
- Les splits, dividendes, distributions créent des gaps artificiels dans les charts
- Ex : un split 2-pour-1 crée un gap baissier artificiel de -50% → tous les indicateurs donnent des signaux baissiers erronés
- Solution : ajuster les données historiques pour éliminer ces gaps avant l'analyse

🔵 **H3 — Pas de news extrêmes :**
- L'AT ne peut pas prédire les événements extrêmes (CEO qui décède, 11 septembre, etc.)
- Quand une news extrême arrive → attendre que le chart se stabilise et reflète la "nouvelle normalité"

🟡 **Application TRADEX — validation des 3 hypothèses :**
- H1 : Gold Futures (GC/MGC) et NQ Futures = très liquides ✅
- H2 : Futures ajustés en continu lors du rollover → à vérifier dans NinjaTrader ⏳
- H3 : News Gate TRADEX v2 couvre exactement H3 ✅

### 3.3 Anatomie d'un SharpChart — Zones annotées

🟢 **Chart MSFT Daily (4-Apr-2019) — Labels officiels :**

| Zone | Contenu |
|------|---------|
| **Ticker/Company/Exchange Date/Time** | En-tête : MSFT Microsoft Corp. Nasdaq GS, date, OHLC |
| **Price Data** | Prix affiché en haut à droite |
| **Price Plot Legend** | Légende des indicateurs overlays (MA50, MA200, Volume) |
| **Price Plot Area** | Zone centrale — bougies + overlays (MA50=111.40 bleue, MA200=107.34 rouge) |
| **Optional Overlay Value Axis** | Axe gauche pour les valeurs des overlays (Volume : 20M→120M) |
| **Ticker Price Axis** | Axe droit pour le prix ($94→$120) |
| **Indicator Panel** | Panneau inférieur — MACD(12,26,9) = 2.255, 2.319, -0.065 |
| **Indicator Panel Legend** | Légende du panneau indicateur |
| **Date/Time Axis** | Axe horizontal — dates (sept 2018 → avr 2019) |
| **Indicator Value Axis** | Axe droit du panneau indicateur (-2 à +3) |

🟢 **Données MSFT visibles :**
- Prix 4-Apr-2019 : Close 119.36 (Open: 120.10, High: 120.23, Low: 118.38, Volume: 20.0M)
- MA(50) = 111.40 ; MA(200) = 107.34 → prix au-dessus des deux = tendance haussière confirmée
- MACD positif (2.255 > 2.319 signal légèrement) = momentum haussier

---

## PARTIE 4 — TYPES DE GRAPHIQUES

### 4.1 Line Chart (Graphique en Ligne)

🔵 **Construction :** ligne reliant les **prix de clôture** uniquement pour chaque période.

🟢 **Chart AAPL Daily Line (20-Jun-2008) — Tendances annotées :**
- **"HIGHER Highs and Lows"** (traits verts) : mars→mi-mai 2008, prix fait successivement des hauts et des bas croissants → **uptrend**
- **"LOWER Highs and Lows"** (traits rouges) : mi-mai→juin 2008, prix fait successivement des hauts et des bas décroissants → **downtrend**
- Prix 20-Jun-2008 : 22.02 (Open: 22.53, High: 22.74, Low: 21.99, Volume: 252.4M)
- Label : **"Line Chart"**

🔵 **Règle tendance (définition visuelle) :**
- **Uptrend = succession de hauts ET de bas croissants**
- **Downtrend = succession de hauts ET de bas décroissants**
- Cette définition est la base de toute l'AT directionnelle

🔵 **Utilisation du Line Chart :** idéal pour visualiser rapidement la direction et l'étendue des rallyes/corrections. Perd l'info intraday (High, Low, Open).

🔵 **Cas obligatoires Line Chart :** fonds mutuels et certains indices → seul le prix de clôture est disponible.

### 4.2 OHLC Bar Chart (Graphique en Barres)

🟢 **Diagramme anatomie barre OHLC :**
- **"Up Day"** (gauche) : trait gauche = Opening price side ; trait droit = Closing price side → Close > Open
- **"Down Day"** (droite) : High price (sommet) et Low price (bas) clairement labelisés → Open > Close

🔵 **Avantage OHLC vs Line :** fournit l'information de **volatilité** (hauteur de la barre = range High-Low) et la **conviction** des acheteurs/vendeurs (écart Open-Close).

🟢 **Chart AAPL OHLC (20-Jun-2008) :**
- Label : **"OHLC Chart"**
- Barres rouges = Down bars ; Barres noires = Up bars
- Les swings intraday (High-Low) passent à travers les niveaux de référence verts/rouges du Line Chart → illustre pourquoi le Line Chart simplifie la vision directionnelle

### 4.3 Couleurs des barres OHLC (Règle StockCharts)

🟢 **Diagramme couleurs OHLC :**
- **Barre ROUGE :** closing price INFÉRIEUR au closing price de la veille (indépendamment de l'Open du jour)
- **Barre NOIRE :** closing price SUPÉRIEUR au closing price de la veille

🔵 **Règle critique : la couleur est basée sur le Close d'AUJOURD'HUI vs le Close d'HIER — pas sur l'Open d'aujourd'hui.** Il est donc possible d'avoir une barre noire avec Close < Open (Up Day mais Higher Close que la veille).

🟢 **Chart AAPL Colored OHLC :**
- Annotation rouge : *"Red since closing price is LOWER than previous day's closing price"*
- Annotation noire : *"Black since closing price is HIGHER than previous day's closing price"*

---

## PARTIE 5 — BOUGIES JAPONAISES (CANDLESTICKS)

### 5.1 Anatomie d'une bougie

🟢 **Diagramme anatomie bougie :**

**UP DAY (bougie haussière / corps vide) :**
- High → sommet de la mèche supérieure (Upper Shadow)
- Close → haut du corps (body) — trait fermé
- Body → corps de la bougie
- Open → bas du corps
- Low → bas de la mèche inférieure

**DOWN DAY (bougie baissière / corps plein) :**
- Upper Shadow → mèche supérieure
- Open → haut du corps (plein/noir)
- Close → bas du corps
- Lower Shadow → mèche inférieure

🔵 **Règle ombres (shadows) :**
- **Mèche inférieure longue** → le marché a fortement chuté pendant la session mais a récupéré → **signe haussier** potentiel
- **Mèche supérieure longue** → le marché a fortement monté mais a reculé → **signe baissier** potentiel
- **Corps long** → forte conviction directionnelle (acheteurs ou vendeurs dominants)

### 5.2 Les 4 Types de Bougies (avec signification psychologique)

🟢 **Diagramme 4 bougies :**

| Type | Couleur | Psychologie |
|------|---------|------------|
| **Up Day, Higher Close** | Corps vide/blanc | Greed > Fear. Corps long = achat très fort |
| **Down Day, Lower Close** | Corps plein/rouge | Fear > Greed. Corps long = vente urgente |
| **Down Day, Higher Close** | Corps plein/noir | Rare. Gap up à l'ouverture mais clôture en baisse du jour. **Signe BAISSIER** si survient haut d'un uptrend |
| **Up Day, Lower Close** | Corps vide/rouge | Rare. Gap down à l'ouverture mais clôture en hausse du jour. **Signe HAUSSIER** si survient bas d'un downtrend |

🟢 **Chart AAPL Candlestick (20-Jun-2008) — annotations réelles :**
- **"Down Day Higher Close (Bearish)"** : cerclé avr 2008 — gap up à l'ouverture, clôture baissière sur la journée mais plus haute que la veille → **corps noir plein**
- **"Up Day Lower Close (Bullish)"** : cerclé juin 2008 — gap down à l'ouverture, clôture haussière sur la journée mais plus basse que la veille → **corps rouge vide**
- Label : **"Candlestick Chart"**

### 5.3 Règle de couleur des bougies StockCharts

🔵 **Outline et shadows :**
- Close > Close(veille) → outline **noire**
- Close < Close(veille) → outline **rouge**

🔵 **Corps (body) :**
- Close > Open → corps **vide** (hollow)
- Close < Open ET Close < Close(veille) → corps **rouge plein**
- Close < Open ET Close > Close(veille) → corps **noir plein** (exception)

### 5.4 Comparaison des 3 types de charts sur AAPL même période

🟢 **Mêmes données AAPL (fév→juin 2008), 3 formats :**
- **Line Chart** : simple, direction visible immédiatement
- **OHLC Chart** : volatilité visible (hauteur des barres), couleurs rouge/noir
- **Candlestick Chart** : corps vides/pleins, ombres visibles → lecture la plus riche

---

## PARTIE 6 — ÉCHELLE ET VOLUME

### 6.1 Échelle Arithmétique vs Échelle Logarithmique (CRITIQUE)

🟢 **Chart CHD (Church & Dwight) Weekly — Échelle ARITHMÉTIQUE :**
- **"Arithmetic Scale"** label
- **"Multiple Trendlines"** : 4 trendlines tracées (1, 2, 3, 4) pour suivre la tendance
- L'espacement arithmétique signifie que $10→$20 = même hauteur visuelle que $20→$30 (progression absolue)
- Résultat : la trendline initiale devient trop inclinée à mesure que le prix monte → nécessite de REDESSINER la trendline plusieurs fois
- CHD Weekly 20-Jun-2008 : 11.95 (Open: 11.80, High: 12.23, Low: 11.68, Volume: 9.1M)

🟢 **Chart CHD Weekly — Échelle LOGARITHMIQUE :**
- **"Log Scale"** label
- **"Single Trendline"** : une seule trendline tracée depuis 2001 (point 1) → tient jusqu'en 2008 (point 4)
- L'espacement log signifie que $10→$20 (+100%) = même hauteur visuelle que $20→$40 (+100%)
- Résultat : **une seule trendline** suffit pour toute la hausse 2000-2008 car elle reflète des pourcentages constants

🔵 **Règle critique d'échelle (Murphy + ChartSchool) :**
- **Échelle Log = premier choix pour les trendlines**, surtout sur les long timeframes
- **Échelle arithmétique :** acceptable pour les charts courts terme où le range de prix est étroit
- Pour TRADEX : les charts Weekly/Monthly utilisés comme contexte de tendance primaire → **toujours vérifier en log scale**

### 6.2 Volume

🟢 **Chart AAPL + Volume (20-Jun-2008) — Volume panel :**
- Panneau de volume en bas : barres rouge/vert/noir
- Volume total AAPL : 252,443,024 actions échangées sur la période
- Pics de volume visibles en juin 2008 (~500M) corrélés à des mouvements de prix significatifs
- Option "Color Volume" : barres **noires** = up days, barres **rouges** = down days

🔵 **Règle volume StockCharts :** le volume coloré permet de voir rapidement où se concentre l'activité acheteur (noir) vs vendeur (rouge). Un pic de volume sur une bougie rouge = vente institutionnelle probable.

### 6.3 CandleVolume Charts

🔵 **CandleVolume = candlestick chart où la LARGEUR de chaque bougie est proportionnelle au volume.**
- Bougie large = fort volume ; Bougie étroite = faible volume
- Visualise l'activité volume "dans" le prix plutôt qu'en panneau séparé

🔴 **Limitation CandleVolume :** l'axe temporel n'est pas uniformément espacé (largeurs variables) → **les trendlines tracées sur CandleVolume doivent toujours être confirmées sur un chart candlestick ou OHLC standard.**

---

## SYNTHÈSE KB — RÈGLES CLÉS POUR TRADEX

🔵 **R1 — L'AT prépare, ne prédit pas :** tout signal TRADEX = probabilité. Le circuit breaker et le position sizing existent pour les cas d'erreur.

🔵 **R2 — 3 prérequis validés pour TRADEX :**
- Liquidité ✅ (futures NQ/ES/Gold = très liquides)
- Pas de prix artificiels ⏳ (vérifier ajustement rollover NinjaTrader)
- News Gate ✅ (architecture v2 déjà prévu)

🔵 **R3 — Uptrend = HH + HL ; Downtrend = LH + LL :** définition visuelle de base, applicable à toutes les Couches TRADEX.

🔵 **R4 — Couleur barre/bougie = Close vs Close(veille), pas Open vs Close :** ne pas confondre "bougie haussière" (Close > Open) et "Up Day" (Close > Close(veille)). Les deux ne coïncident pas toujours.

🔵 **R5 — Log Scale pour trendlines long terme :** les trendlines TRADEX tracées sur Weekly/Monthly doivent utiliser l'échelle log. En échelle arithmétique, une seule trendline ne tient pas sur plusieurs années.

🔵 **R6 — Volume coloré = lecture rapide institutionnelle :** pic de volume rouge = vente. Pic de volume noir = achat. À intégrer dans Couche 2 (algo volume).

---

## CE QUE CETTE SÉRIE NE COUVRE PAS (PARTS 7+)
⏳ Support & Resistance (Part 7) — à extraire
⏳ Trendlines avancées (Part suivante)
⏳ Indicateurs techniques spécifiques
⏳ Patterns de bougies japonaises (Doji, Hammer, etc.)

---

*Fin d'extraction — ChartSchool TA-101 Parts 1-6 — v1 enrichie (texte intégral + 17 images)*
*Source : StockCharts.com ChartSchool. Document éducatif uniquement.*
*Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
