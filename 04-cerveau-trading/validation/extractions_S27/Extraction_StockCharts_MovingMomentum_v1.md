# Extraction StockCharts — Moving Momentum
**Source :** `bundles/stockcharts/moving_momentum.md` (HTTP 200 · ~9 894 car.) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées
**Décisions :** D2711 → D2722 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-momentum
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Table | Image | Label certifié | Section | Décision liée |
|-------|-------|----------------|---------|---------------|
| — | image_01.png | Chart 1 - Moving Momentum Trading Strategy | Defining the Indicators | D2712 |
| — | image_02.png | Chart 2 - Moving Momentum Trading Strategy | Buy Signal | D2715 |
| — | image_03.png | Chart 3 - Moving Momentum Trading Strategy | Sell Signal | D2716 |
| — | image_04.png | Chart 4 - Moving Momentum Trading Strategy | Trading Example | D2718 |
| — | image_05.png | Chart 5 - Moving Momentum Trading Strategy | Tweaking | D2719 |

## DÉCISIONS

### D2711 — Processus en 3 étapes (biais → correction → renversement)
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md) : « Many trading strategies are based on a process, not a single signal. (…) First establish a trading bias or long-term perspective. Second, chartists wait for pullbacks or bounces that will improve the risk-reward ratio. Third, chartists look for a reversal that indicates a subsequent upturn or downturn in price. The strategy (…) uses moving average to define the trend, the Stochastic Oscillator to identify corrections within that trend and the MACD-Histogram to signal short-term reversals. »
**TRADEX-AI C1** : Architecture de signal en cascade (biais MM → correction Stochastique → renversement MACD-H) directement transposable à la logique événementielle TRADEX-AI : tendance d'abord, timing ensuite. Renforce la règle « process, pas signal unique ».
*Catégorie : signal*
---

### D2712 — MM = indicateur retardé mais lisseur de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_01) : « Moving averages are trend-following indicators that lag price. This means the actual trend changes before the moving averages generate a signal. (…) Moving averages smooth prices and provide chartists with a cleaner price plot, which makes it easier to identify the general trend. »
**TRADEX-AI C1** : Accepter le lag des MM comme prix à payer pour un trend propre ; ne pas chercher l'entrée sur la MM elle-même mais sur le déclencheur (étape 3). Garde-fou anti-faux-signal.
*Catégorie : indicateurs_tendance*
---

### D2713 — Biais de tendance par deux MM (20/150 SMA)
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md) : « This strategy employs two moving averages to define the trading bias. The bias is bullish when the shorter-moving average moves above the longer moving average. The bias is bearish when the shorter-moving average moves below the longer moving average. (…) this article uses the 20-day SMA and the 150-day SMA. »
**TRADEX-AI C1** : Biais directionnel binaire (20 SMA vs 150 SMA) = filtre de fond. Périodes paramétrables ; pour TRADEX-AI, à recalibrer sur range bars NT8 (les 20/150 jours daily ne s'appliquent pas tels quels aux timeframes Belkhayate).
*Catégorie : indicateurs_tendance*
---

### D2714 — Oscillateur Stochastique pour identifier la correction
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md) : « The Stochastic Oscillator (…) fluctuates between 0 and 100 (…). A move below 20 signals a pullback in prices, while a move above 80 signals a bounce in prices. »
**TRADEX-AI C3** : Stochastique <20 = pullback (zone d'achat potentiel en tendance haussière), >80 = bounce (zone de vente potentielle en tendance baissière). Seuils 20/80 figés. Attention multicollinéarité (cf. extraction Multicollinearity) : ne pas empiler plusieurs oscillateurs momentum redondants.
*Catégorie : indicateurs_momentum*
---

### D2715 — MACD-Histogram comme déclencheur de renversement
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_02) : « The MACD-Histogram measures the difference between MACD and its signal line. (…) The MACD-Histogram turns positive when prices turn up, and turns negative when prices turn down. »
**TRADEX-AI C1** : MACD-H = déclencheur de timing (étape 3). Passage en territoire positif = fin du pullback → entrée long ; passage négatif = fin du bounce → entrée short. Codable depuis MACD(12,26,9).
*Catégorie : indicateurs_momentum*
---

### D2716 — Règle d'achat complète (3 conditions)
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_02) : « Buy Signal: Moving averages show a bullish trading bias, with the 20-day SMA trading above the 150-day SMA. Stochastic Oscillator moves below 20 to signal a pullback. (…) Chartists then turn to the MACD-Histogram to signal an end to the pullback with a move into positive territory. (…) it's important to wait for confirmation of an upturn. »
**TRADEX-AI C1** : Signal ACHETER = biais MM haussier ET Stoch <20 ET MACD-H repassant positif. Configuration multi-critères alignés — cohérent avec la grille /10 (plusieurs conditions concordantes requises). Attendre la confirmation MACD-H, ne pas anticiper.
*Catégorie : configuration*
---

### D2717 — Règle de vente complète (3 conditions)
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_03) : « Sell Signal: Moving averages show a bearish trading bias, with the 20-day SMA trading below the 150-day SMA. Stochastic Oscillator moves above 80 to signal a bounce. (…) Acting on a move above 80 can result in a losing trade because it can sometimes take a week or two for prices to turn back down. The third and final signal occurs when the MACD-Histogram turns negative. »
**TRADEX-AI C1** : Signal VENDRE = biais MM baissier ET Stoch >80 ET MACD-H repassant négatif. Garde-fou explicite : ne pas agir sur le seul Stoch >80 (risque de perte) — attendre le déclencheur MACD-H.
*Catégorie : configuration*
---

### D2718 — Filtrage des signaux contraires au biais
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_04) : « Bearish signals are ignored when the bias is bullish. Bullish signals are ignored when the bias is bearish. (…) chartists setting a stop-loss at resistance would have remained in the position and caught the big decline. »
**TRADEX-AI C1** : Régle de filtrage directionnel strict — ignorer tout signal opposé au biais MM en cours. Évite les contre-tendances. Stop-loss placé sur niveau de structure (support/résistance).
*Catégorie : gestion_risque_entree*
---

### D2719 — Réglage de la sensibilité selon la volatilité de l'actif
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_05) : « Stocks with lower volatility, such as those in the utilities and consumer staples sectors, would warrant more sensitive settings. Stocks with higher volatility, such as those in the technology and biotech sectors, may warrant less sensitive settings. The trick is to find the setting that produces enough signals, but not too many. »
**TRADEX-AI C7** : Calibrer les périodes (MM/oscillateurs) selon la volatilité propre de l'actif. Pour GC/HG/CL/ZW, chaque future a sa volatilité → réglages potentiellement distincts par actif. Lien avec la matrice de corrélations 30j (C7).
*Catégorie : configuration*
---

### D2720 — Tweak : sensibilité des oscillateurs et du MACD-H
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md) : « A 10-day Stochastic Oscillator would become overbought/oversold more often than a 20-day Stochastic Oscillator. Similarly, the MACD-Histogram (5,30,9) would cross the zero line more often than the MACD-Histogram used with the default settings (12,26,9). »
**TRADEX-AI C1** : Raccourcir les périodes = plus de signaux (plus de bruit) ; allonger = moins de signaux (plus retardés). Paramètres MACD-H par défaut 12,26,9. Arbitrage fréquence/fiabilité à figer avant déploiement.
*Catégorie : configuration*
---

### D2721 — Réalité du trading : whipsaws et imperfection
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md, image_04) : « This is not the most ideal example, but it does provide some insights into real-world trading, which is often not ideal. (…) These did not last long or work out well because trading was quite choppy. (…) After a couple more whipsaws (4 and 5), the strategy triggered a nice bullish signal in early December. »
**TRADEX-AI C1** : Reconnaissance explicite que la stratégie produit des whipsaws en marché choppy. Garde-fou : la gestion du stop-loss (sur structure) est ce qui sauve la performance, pas la précision du signal. Renforce l'importance du risk_manager.
*Catégorie : gestion_risque_entree*
---

### D2722 — Conclusion : trader dans le sens de la grande tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_momentum.md) : « This "Moving Momentum" strategy provides charts with a means to trade in the direction of the bigger trend. (…) The moving average sets the tone, bullish or bearish. The Stochastic Oscillator is used to identify pullbacks within bigger uptrends and bounces within bigger downtrends. The MACD-Histogram is used to signal the end of a pullback or bounce. (…) this article is designed as a starting point for trading system development. »
**TRADEX-AI C1** : Synthèse opérationnelle : MM = tonalité, Stochastique = correction, MACD-H = timing. Modèle de référence pour structurer la décision de signal dans le sens de la tendance ; point de départ, à valider en backtest sur range bars.
*Catégorie : signal*
---

## SYNTHÈSE
| Champ | Valeur |
|-------|--------|
| Décisions ajoutées | 12 (D2711 → D2722) |
| Images citées | 5/5 certifiées |
| Catégories | signal, indicateurs_tendance, indicateurs_momentum, configuration, gestion_risque_entree |
| Cercle dominant | C1 (prix / tendance) avec apports C3 (momentum) et C7 (calibrage volatilité) |
| Tags | 🟢 FAIT VÉRIFIÉ ×12 |
| Belkhayate | Aucun lien affirmé par la source. Le séquençage tendance→correction→déclencheur fait écho à l'ordre d'analyse 4 étapes Belkhayate (Pivots→BGC→Direction→Énergie/Déclencheur) ⚫🔴 hypothèse projet, non affirmée par la source. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, NON fusionnée dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur.
