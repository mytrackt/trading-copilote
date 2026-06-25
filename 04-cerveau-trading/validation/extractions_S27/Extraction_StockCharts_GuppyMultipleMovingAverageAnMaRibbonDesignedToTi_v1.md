# Extraction StockCharts — Guppy Multiple Moving Average (GMMA)
**Source :** `bundles/stockcharts/guppy_multiple_moving_average_an_ma_ribbon_designed_to_tip_the_markets_hand.md` (HTTP 200 · ~9 010 car.) + 4 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D1931 → D1950 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/guppy-multiple-moving-average-an-ma-ribbon-designed-to-tip-the-markets-hand
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : indicateur du créateur Daryl Guppy (ruban de moyennes mobiles, C1) → règles taguées 🔵 ÉCOLE.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Guppy Multiple Moving Averages using StockCharts | What are the Components of a GMMA? | CERTIFIE (accord .md + HTML) |
| image_02.png | Trading trends using Guppy Multiple Moving Average | How to Trade a Trend Using the GMMA | CERTIFIE (accord .md + HTML) |
| image_03.png | Trading trends using Guppy Multiple Moving Average | Sell Signal | CERTIFIE (accord .md + HTML) |
| image_04.png | Identifying sideways breakouts using Guppy Multiple Moving A | Sideways Breakout | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1931 — Définition GMMA = ruban de 12 EMA
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « The Guppy Multiple Moving Average is a moving average ribbon that combines 12 exponential moving averages... a set of 12 moving averages designed to track short-term and long-term market sentiment. »
**TRADEX-AI C1** : GMMA = ruban de 12 EMA (overlay tendance), conçu pour suivre le sentiment court ET long terme. Brique de contexte de tendance.
*Catégorie : indicateurs_tendance*
---

### D1932 — Deux « moitiés » = proxy court terme / long terme
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « The two "halves" of the GMMA serve as a proxy for short-term and long-term market participants... The two sets of ribbons are virtual "proxies" for shorter-term traders and longer-term investors. »
**TRADEX-AI C1** : Les deux rubans = proxy des traders court terme (spéculateurs) vs investisseurs/institutionnels long terme. Lecture de la dynamique entre acteurs.
*Catégorie : structure_marche*
---

### D1933 — Composition du ruban court terme (6 EMA)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « The short-term EMA ribbon includes the 3, 5, 8, 10, 12, and 15-day EMAs. This ribbon is your proxy for the traders who trade the shorter-term trends. »
**TRADEX-AI C1** : Ruban court terme = EMA(3,5,8,10,12,15). Paramètres déterministes codables. Proxy traders court terme.
*Catégorie : indicateurs_tendance*
---

### D1934 — Composition du ruban long terme (6 EMA)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « The long-term EMA ribbon comprises 30, 35, 40, 45, 50, and 60-day EMAs. This ribbon represents investor and institutional sentiment. »
**TRADEX-AI C1** : Ruban long terme = EMA(30,35,40,45,50,60). Paramètres déterministes codables. Proxy sentiment institutionnel.
*Catégorie : indicateurs_tendance*
---

### D1935 — Le « gap » entre EMA 15 et EMA 30
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_01) : « Note that the "gap" between the 15-day EMA and the 30-day EMA. This gap helps separate the two proxies, and the distance between them in a chart can help you assess the overall strength and momentum of a stock's trend. »
**TRADEX-AI C1** : L'espace EMA15↔EMA30 sépare les deux rubans ; sa largeur mesure la force/momentum de la tendance. Métrique de force codable.
*Catégorie : indicateurs_tendance*
---

### D1936 — Trois conditions visibles sur le GMMA
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « Three conditions can appear clearly when viewing a GMMA on a chart. » (Bullish / Bearish / Sideways — détaillées ci-après.)
**TRADEX-AI C1** : Le GMMA produit 3 états distincts (haussier / baissier / latéral). Machine à états codable pour qualifier le régime.
*Catégorie : signal*
---

### D1937 — Condition haussière (croisement court > long)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « When the short-term ribbon crosses above the long-term ribbon, an uptrend may be emerging. The more "spread-out" the ribbons, the stronger the trend. This means that the shorter-term traders are taking action to exploit the rally ahead of the longer-term investors. »
**TRADEX-AI C1** : Ruban court CROISE AU-DESSUS du long ⇒ uptrend émergent ; écartement ↑ = tendance plus forte. Signal haussier + jauge de force. Applicable GC/HG/CL/ZW.
*Catégorie : signal*
---

### D1938 — Condition baissière (croisement court < long)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « When the short-term ribbon crosses below the long-term ribbon, a downtrend may be emerging... the shorter-term traders are taking early action to sell the stock while longer-term investors are still deciding on their positions. Again, ribbons in "full-sail" indicate a stronger trend. »
**TRADEX-AI C1** : Ruban court CROISE SOUS le long ⇒ downtrend émergent ; rubans « toutes voiles dehors » = tendance plus forte. Signal baissier + jauge de force.
*Catégorie : signal*
---

### D1939 — Condition latérale (convergence des rubans)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « When the shorter-term ribbon converges into the longer-term ribbon, this means that both short-term traders and long-term investors are in "agreement" on the value of a stock. This also means that there is no trend for the time being. »
**TRADEX-AI C1** : Convergence des deux rubans = consensus court/long terme = absence de tendance. État « no-trade tendance » à filtrer.
*Catégorie : structure_marche*
---

### D1940 — Règle d'entrée dépend de la stratégie (pas universelle)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « Like all indicators, your specific entry and exit rules depend on your strategy. However, here's one simple way to trade GMMA ribbons. »
**TRADEX-AI C1** : Les règles d'entrée/sortie GMMA dépendent de la stratégie ; ce qui suit n'est qu'UN exemple, non une règle absolue. Prudence avant codage en déclencheur dur.
*Catégorie : gestion_risque_entree*
---

### D1941 — Signal d'achat (Buy)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_02) : « Buy Signal: When the short-term ribbons cross above the long-term ribbons, it signals a green light for long positions. Entering the trade should be in accordance with your trading approach. »
**TRADEX-AI C1** : Buy = croisement ruban court au-dessus du long → feu vert long, à confirmer selon l'approche. Déclencheur long candidat.
*Catégorie : signal*
---

### D1942 — Ruban bas (long terme) comme support potentiel
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_02) : « You might have entered a long trade on the breakout of the candle testing the lower ribbon. Remember that the lower half of the ribbon is a proxy for longer-term investors, making it a potentially effective support level. You wait for the breakout to confirm your "support" thesis. »
**TRADEX-AI C1** : Le ruban bas (long terme) agit comme support potentiel ; entrée long sur breakout de la bougie qui le teste, après confirmation. Niveau de référence + confirmation. Complémentaire pivots Belkhayate (⚫🔴 à valider).
*Catégorie : gestion_risque_entree*
---

### D1943 — Signal de vente (Sell / short)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_03) : « The same can be said for a short position (sell entry). Take a look at the next example. » (Symétrique du Buy : croisement court sous long → entrée short.)
**TRADEX-AI C1** : Sell = symétrique du Buy → croisement ruban court sous le long pour entrée short, mêmes conditions de confirmation. Déclencheur short candidat.
*Catégorie : signal*
---

### D1944 — Compression des rubans = faible volatilité (analogie Bollinger)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_04) : « Similar to a low-volatility reading using Bollinger Bands, a convergence or "compression" of both sets of ribbons typically happens when there's little volatility. That's because everyone seems to agree with the price of a stock. »
**TRADEX-AI C1** : Compression/convergence des rubans = faible volatilité (analogue squeeze Bollinger), consensus de prix. Détecteur de basse volatilité.
*Catégorie : structure_marche*
---

### D1945 — Compression annonce un breakout imminent
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_04) : « But this also indicates that a breakout in either direction may soon occur. After all, no stock can hold the same price or hover at the same range forever. »
**TRADEX-AI C1** : La compression annonce un breakout imminent (direction non déterminée). Pré-signal de mouvement, à coupler avec la direction.
*Catégorie : signal*
---

### D1946 — Contextualiser le price action (forest vs trees)
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_04) : « What's important in this case is to contextualize the price action from a broader perspective. Here's one example illustrating how not to "miss the forest for the trees." »
**TRADEX-AI C1** : Ne pas se focaliser sur la micro-position des rubans (les « arbres ») et rater la tendance globale (la « forêt »). Garde-fou de lecture multi-échelle.
*Catégorie : gestion_risque_entree*
---

### D1947 — Confirmation breakout par structure HH/HL
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md, image_04) : « The uptrend began with a breakout of a local swing high (red dotted line), and from that point on, you can see the series of higher highs (HH) and higher lows (HL) that formed into a sustained uptrend. »
**TRADEX-AI C1** : Breakout d'un swing high local + série HH/HL confirme un uptrend soutenu. Confirmation structurelle (structure de marché) du signal GMMA.
*Catégorie : structure_marche*
---

### D1948 — GMMA = jauge de sentiment via deux groupes d'acteurs
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « The Guppy Multiple Moving Average (GMMA) is a moving average ribbon that can help you gauge market sentiment by serving as a visual proxy for short-term traders and long-term investors. By visualizing the interplay of these two groups, you can identify potential trends and reversals. »
**TRADEX-AI C5** : Synthèse — le GMMA jauge le sentiment via l'interaction court/long terme ; identifie tendances ET retournements potentiels. Lien sentiment.
*Catégorie : structure_marche*
---

### D1949 — GMMA à combiner avec d'autres outils
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « Remember that while the GMMA provides valuable information, it can be used with other tools to analyze the broader market context better. »
**TRADEX-AI C1** : Le GMMA n'est pas auto-suffisant ; à combiner avec d'autres outils pour le contexte. À traiter comme brique de confluence, pas signal isolé.
*Catégorie : gestion_risque_entree*
---

### D1950 — Finalité : moyennes mobiles pour identifier les tendances
🔵 **ÉCOLE** (Source : guppy...the_markets_hand.md) : « Moving averages, at their most basic function, are designed to help you identify trends. From that, you can assess market sentiment, decide on the likely course of price action, and determine trading opportunities and risks. »
**TRADEX-AI C1** : Fondement — les MM servent d'abord à identifier les tendances, d'où dérivent sentiment, anticipation du price action et opportunités/risques. Cadre général du GMMA.
*Catégorie : indicateurs_tendance*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1931 → D1950 (20) |
| Images | 4/4 certifiées |
| Tags | 🔵 ÉCOLE ×20 (Daryl Guppy / ruban EMA) |
| Cercles | C1 (majorité, ruban MA = prix/tendance), C5 (sentiment ×1 synthèse) |
| Catégories | indicateurs_tendance ×6, signal ×6, structure_marche ×5, gestion_risque_entree ×5 |
| Paramètres clés | court : EMA(3,5,8,10,12,15) · long : EMA(30,35,40,45,50,60) · gap EMA15↔EMA30 = force de tendance |
| Lien Belkhayate | ⚫🔴 indirect : ruban bas = support potentiel, à comparer aux pivots Belkhayate (PP+Gan+clôture veille) — à valider hors source, ne pas fusionner comme fait Belkhayate |
| Cas à vérifier | Aucun blocage manifest (4/4). D1940 rappelle que les règles d'entrée ne sont qu'UN exemple → ne pas coder en déclencheur dur sans backtest |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. BRUT, non fusionné.
