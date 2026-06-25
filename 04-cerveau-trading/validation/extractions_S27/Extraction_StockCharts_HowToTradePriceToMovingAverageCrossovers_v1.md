# Extraction StockCharts — How To Trade Price-to-Moving Average Crossovers

**Source :** `bundles/stockcharts/how_to_trade_price_to_moving_average_crossovers.md` (HTTP 200 · ~7 900 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D2091 → D2110 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/how-to-trade-price-to-moving-average-crossovers
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🟢 **PERTINENCE FUTURES : OUI (C1)** — stratégie de croisement prix/moyenne mobile, directement transposable aux actifs tradables (GC/HG/CL/ZW) comme brique de tendance/signal, sous réserve de recalibrer les périodes sur le timeframe TRADEX (15min / Range Bar). Les exemples chiffrés (TSLA, périodes 20/50/200) sont pédagogiques sur actions et NE doivent PAS être codés tels quels. Belkhayate NON CONCERNÉ (le croisement prix/MM n'est pas un outil de la méthode), lien indirect ⚫🔴 via la règle « pas de trade en range ».

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Trading moving average crossovers in StockCharts | Example of Trading a Moving Average Crossover | CERTIFIE (accord .md + HTML) |
| image_02.png | Trading moving average crossovers in StockCharts | Example of Bearish Price Crossover | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2091 — Key Takeaways de la stratégie
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « A price-to-moving average crossover identifies entry and exit points by focusing on price movement at the time price intersects with a moving average. The moving average periods you use depends on how long you intend to hold the position. You can trade bullish or bearish moving average crossovers depending on stock market conditions. »
**TRADEX-AI C1** : définition du croisement prix/MM comme mécanisme d'entrée/sortie ; périodes liées à l'horizon de détention. Transposable aux futures comme feature de signal.
*Catégorie : signal*

---

### D2092 — Lecture de tendance par position prix vs SMA 50
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « If prices are above the 50-day SMA and both are rising, you can assume that a stock is in an uptrend. If prices are below the 50-day SMA and both fall, it's likely a downtrend. When both are flat and price moves above and below a flat SMA, the market is probably going sideways. »
**TRADEX-AI C1** : règle déterministe de régime (uptrend / downtrend / range) selon position et pente prix vs SMA. Codable comme classifieur de tendance. Période 50 = exemple, à recalibrer.
*Catégorie : indicateurs_tendance*

---

### D2093 — Le croisement comme entrée agressive précoce
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « to exploit a trading opportunity early on, you might have to wait until prices and their corresponding moving average cross (...) take advantage of a bullish or bearish price and moving average crossover to make a more aggressive market entry. »
**TRADEX-AI C1** : le croisement sert d'entrée anticipée vs attendre une confirmation de tendance établie. Compromis réactivité/risque.
*Catégorie : signal*

---

### D2094 — Définition du Bullish Crossover
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Bullish Crossover. This is when the price moves above its moving average. It often suggests that the stock's momentum is starting to move upward, indicating a potential buying opportunity. »
**TRADEX-AI C1** : prix > MM = signal d'achat potentiel. Règle binaire codable. « Rule of thumb », dépend du contexte (cf. D2096).
*Catégorie : signal*

---

### D2095 — Définition du Bearish Crossover
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Bearish Crossover. When the stock's price falls below its moving average, it's generally considered bearish. It tells you that the stock has lost bullish momentum and is either pulling back (...) or entering a downtrend (...) it suggests a selling or short-selling opportunity. »
**TRADEX-AI C1** : prix < MM = signal de vente/short potentiel. Symétrique de D2094.
*Catégorie : signal*

---

### D2096 — Règles de pouce, pas règles dures + bruit des MM courtes
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « these are not "hard" rules but rules of thumb that depend on the larger context (...) longer-term moving averages may be a bit less vulnerable to "market noise," which can result in giving you more false (bullish or bearish) signals. »
**TRADEX-AI C1** : garde-fou — MM courtes = plus de faux signaux ; le croisement dépend du contexte global, jamais appliqué mécaniquement.
*Catégorie : configuration*

---

### D2097 — Choix de période selon l'horizon de trade
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : Short-term → SMA 5 ou 10 jours ; Intermediate-term → SMA 20 ou 50 (« the 50-day SMA (...) serves as a critical support or resistance level ») ; Long-term → SMA 100 ou 200. « experiment with different settings to find the best MA period. »
**TRADEX-AI C1** : grille de périodes par horizon. Note futures : valeurs en « jours » sur actions ; à reparamétrer selon timeframe TRADEX (15min / Range Bar). SMA 50 souvent support/résistance.
*Catégorie : configuration*

---

### D2098 — Bullish trade Step 1 : confirmer le croisement (clôture)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 1. Confirm the Crossover. (...) ensure the price has conclusively crossed above the moving average. So, if you're using candlestick charts, you'll have to wait for a full candle close above the SMA. »
**TRADEX-AI C1** : exiger une CLÔTURE de bougie au-dessus de la MM avant de valider = filtre anti-faux-signal codable. Cohérent avec l'analyse en clôture du projet.
*Catégorie : signal*

---

### D2099 — Bullish trade Step 2 : confluence d'indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 2. Check Supporting Context and Indicators. Look for confluence (...) the RSI might indicate the asset is not yet overbought, or the Stochastic Oscillator could be showing a bullish crossover. If the SMA is rising, then it's a bullish sign; but if the SMA is falling, you should have a good reason to take a bullishly contrarian position. »
**TRADEX-AI C1** : exiger une confluence (RSI/Stochastic + pente SMA) avant l'entrée. Aligné avec la logique de score multi-cercles.
*Catégorie : configuration*

---

### D2100 — Bullish trade Step 3 : confirmer par le volume
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 3. Check the Trading Volume. A significant increase in volume shows bullish trend strength. If not, then tread carefully, as your chances of acting on a false signal are much greater. »
**TRADEX-AI C2** : volume en hausse = confirmation de force ; volume faible = risque de faux signal. Mappable sur l'order flow ATAS (C2). Note : volume futures (contrats) ≠ volume actions.
*Catégorie : signal*

---

### D2101 — Bullish trade Step 4 : point d'entrée
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 4. Determine Your Entry Point. Enter a long position after confirming the crossover and other signals. (...) Some traders prefer entering immediately upon confirmation, while others might wait for a breakout above the crossover candle or a retest of the moving average as support. »
**TRADEX-AI C1** : trois modes d'entrée (immédiat / breakout de la bougie / retest MM-support). Options paramétrables d'exécution.
*Catégorie : gestion_risque_entree*

---

### D2102 — Bullish trade Step 5 : stop-loss
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 5. Set Your Stop-Loss. Place your stop-loss slightly below the SMA or the most recent swing low. This step ensures limited loss in case the crossover was a false signal. »
**TRADEX-AI C7** : stop sous la SMA ou le dernier swing low = règle de placement de stop concrète et codable. Gestion du risque obligatoire.
*Catégorie : gestion_risque_entree*

---

### D2103 — Bullish trade Step 6 : objectif de profit
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 6. Determine Your Profit Target. Set a take-profit based on a resistance level, a measured move, a trailing stop, or any strategically determined target approach. You want to catch as much upside as possible while minimizing your downside risk. »
**TRADEX-AI C7** : cibles de TP (résistance / measured move / trailing stop). Cohérent avec l'exigence R/R ≥ 1:2 du projet.
*Catégorie : gestion_risque_entree*

---

### D2104 — Exemple haussier TSLA (SMA 20 + RSI + Stochastic + Fib)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md, image_01) : sur TSLA, le passage au-dessus de la SMA 20 confirmé par RSI et Stochastic a donné un long favorable, sorti à la clôture sous la SMA 20. Un Fibonacci Retracement (creux janvier → sommet février) plaçait la « buying range » entre 38,2 % et 61,8 % ; sortir au croisement sous la SMA 20 aurait été inutile vu le retracement.
**TRADEX-AI C1** : exemple concret combinant croisement + oscillateurs + Fibonacci pour filtrer les sorties prématurées. Paramètres TSLA = illustratifs, non à coder.
*Catégorie : signal*

---

### D2105 — Bearish trade Step 1-2 : confirmer + confluence
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 1. Confirm the Crossover (...) price has conclusively crossed below the moving average. Step 2. (...) the RSI might indicate the asset is not yet oversold, or the Stochastic (...) bearish crossover. If the SMA is falling, it's a bearish sign; but if the MA is rising, you should have a reason to take a bearish contrarian position. »
**TRADEX-AI C1** : version baissière symétrique — clôture sous la MM + confluence RSI/Stochastic + pente SMA descendante.
*Catégorie : signal*

---

### D2106 — Bearish trade Step 3-4 : volume + entrée short
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 3. (...) A significant increase in volume shows bearish trend strength. Step 4. (...) You can sell your long position or enter a short position after confirming the crossover (...) wait for a breakout below the crossover candle or a retest of the moving average as resistance. »
**TRADEX-AI C2/C1** : volume confirme la force baissière (C2 order flow) ; entrée short immédiate / breakout bas / retest MM-résistance.
*Catégorie : gestion_risque_entree*

---

### D2107 — Bearish trade Step 5-6 : stop + cible
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Step 5. Place your stop-loss slightly above the SMA or the most recent swing high. Step 6. Set a take-profit based on a support level, a measured move, a trailing stop. »
**TRADEX-AI C7** : placement de stop au-dessus de la SMA / dernier swing high ; cibles sur support. Symétrique du cas haussier.
*Catégorie : gestion_risque_entree*

---

### D2108 — CAVEAT : risque illimité en short
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « CAVEAT: When going short, your risk is technically unlimited (unlike going long). So be extra careful when shorting stocks. »
**TRADEX-AI C7** : garde-fou explicite sur le risque asymétrique du short. À relayer dans la gestion du risque du moteur (taille de position, stop obligatoire).
*Catégorie : gestion_risque_entree*

---

### D2109 — Exemple baissier (sell-stop sous swing lows)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md, image_02) : exemple hypothétique de trois short trades, déclenchés non au croisement sous la SMA 20 mais via un sell-stop order sur cassure de chaque swing low ; stop au sommet du swing high précédent. Selon la règle de sortie (TP 100 % du risque vs sortie au croisement au-dessus de la SMA 20), les résultats diffèrent (1er et 3e profitables, 2e break-even/perte avec frais).
**TRADEX-AI C1** : filtrage des entrées par sell-stop sur cassure de structure ; la règle de sortie change le résultat. Paramètres illustratifs.
*Catégorie : gestion_risque_entree*

---

### D2110 — Pièges et garde-fous (faux signaux, lag, conditions de marché)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_price_to_moving_average_crossovers.md) : « Beware False Signals (...) especially true in sideways markets, where you'll likely get whipsawed. Lagging Indicator (...) moving averages (...) lag the market (...) a significant part of the movement might already have happened. Market Conditions. Crossovers work best in trending markets (...). In sideways markets (...) crossover signals are more uncertain and less reliable. »
**TRADEX-AI C1** : garde-fou central — croisements efficaces en TENDANCE, mauvais en RANGE (whipsaws) + retard intrinsèque. ⚫🔴 Recoupe la logique « pas de trade en range » de la méthode (hypothèse projet, non affirmée par la source).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2091 | Key Takeaways | 🟢 | C1 | signal |
| D2092 | Régime via prix vs SMA 50 | 🟢 | C1 | indicateurs_tendance |
| D2093 | Croisement = entrée agressive | 🟢 | C1 | signal |
| D2094 | Bullish Crossover | 🟢 | C1 | signal |
| D2095 | Bearish Crossover | 🟢 | C1 | signal |
| D2096 | Rules of thumb + bruit MM courtes | 🟢 | C1 | configuration |
| D2097 | Périodes selon horizon (5/10/20/50/100/200) | 🟢 | C1 | configuration |
| D2098 | Bull Step 1 : confirmer (clôture) | 🟢 | C1 | signal |
| D2099 | Bull Step 2 : confluence indicateurs | 🟢 | C1 | configuration |
| D2100 | Bull Step 3 : volume | 🟢 | C2 | signal |
| D2101 | Bull Step 4 : point d'entrée | 🟢 | C1 | gestion_risque_entree |
| D2102 | Bull Step 5 : stop-loss | 🟢 | C7 | gestion_risque_entree |
| D2103 | Bull Step 6 : profit target | 🟢 | C7 | gestion_risque_entree |
| D2104 | Exemple TSLA (SMA 20 + Fib) | 🟢 | C1 | signal |
| D2105 | Bear Step 1-2 : confirmer + confluence | 🟢 | C1 | signal |
| D2106 | Bear Step 3-4 : volume + entrée short | 🟢 | C2/C1 | gestion_risque_entree |
| D2107 | Bear Step 5-6 : stop + cible | 🟢 | C7 | gestion_risque_entree |
| D2108 | CAVEAT risque illimité short | 🟢 | C7 | gestion_risque_entree |
| D2109 | Exemple baissier (sell-stop) | 🟢 | C1 | gestion_risque_entree |
| D2110 | Pièges : faux signaux / lag / range | 🟢 | C1 | structure_marche |

| Élément | Valeur |
|---------|--------|
| Décisions | D2091 → D2110 (20) |
| Images certifiées | 2/2 |
| Cercles | C1 (tendance/signal, dominant) · C2 (volume) · C7 (gestion risque) |
| Catégories | signal · indicateurs_tendance · configuration · gestion_risque_entree · structure_marche |
| Actif applicable | GC/HG/CL/ZW (TRADING) + ES — stratégie transposable, périodes à recalibrer |
| Belkhayate | NON CONCERNÉ (croisement prix/MM ≠ outil Belkhayate) ; lien indirect ⚫🔴 « pas de trade en range » |
| Pertinence futures | OUI (C1) — brique de tendance/signal directement utile au moteur |
| Cas « à vérifier » | (1) Périodes 5/10/20/50/100/200 et exemple TSLA : pédagogiques sur actions US daily, NE PAS coder tels quels — recalibrer sur timeframe TRADEX. (2) D2100/D2106 volume : volume futures (contrats) ≠ volume actions, mapper sur ATAS (C2). (3) D2110 lien Belkhayate « range » = hypothèse projet ⚫🔴, à confirmer humain. |

**Liens Belkhayate :** Le croisement prix/moyenne mobile n'est PAS un outil de la méthode Belkhayate (⚫). Seul lien indirect : la règle « crossovers inefficaces en range » recoupe la logique « ne pas trader en range » du projet, mais l'attribuer à Belkhayate serait une hypothèse projet non affirmée par la source (⚫🔴). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
