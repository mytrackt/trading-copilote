# Extraction StockCharts — Introduction to Technical Indicators and Oscillators
**Source :** `bundles/stockcharts/introduction_to_technical_indicators_and_oscillators.md` (HTTP 200 · ~44 600 car.) + 0 image certifiée
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 0/16 certifiées (manifest « À VÉRIFIER » : intégrité .md=15 figures vs HTML=16 images → alignement impossible)
**Décisions :** D2311 → D2330 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/introduction-to-technical-indicators-and-oscillators
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée. Le manifest signale un désalignement d'intégrité (.md = 15 figures vs HTML = 16 images, alignement impossible → 16 images « À VÉRIFIER », 0 certifiée). Aucune image n'est citée dans les décisions ci-dessous ; le **texte reste pleinement exploitable** et seul le texte est utilisé comme source.

## DÉCISIONS

### D2311 — Définition : un indicateur technique = formule appliquée aux données de prix
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « A technical indicator is a series of data points that are derived by applying a formula to the price data of a security. Price data includes any combination of the open, high, low or close over a period of time. Some indicators may use only the closing prices, while others incorporate volume and open interest into their formulas. »
**TRADEX-AI C1** : Définition de base — un indicateur dérive d'une formule sur OHLC (parfois volume/OI). Cadre conceptuel pour tout indicateur codé sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*
---

### D2312 — Trois fonctions des indicateurs : alerter, confirmer, prédire
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Indicators serve three broad functions: to alert, to confirm and to predict. An indicator can act as an alert to study price action a little more closely... Indicators can be used to confirm other technical analysis tools... According to some investors and traders, indicators can be used to predict the direction of future prices. »
**TRADEX-AI C1** : Rôle d'un indicateur dans TRADEX = alerter (niveau 1 surveillance) et confirmer (grille /10) ; la fonction « prédire » est présentée comme opinion, à traiter avec prudence.
*Catégorie : signal*
---

### D2313 — Un indicateur est un dérivé : toujours le lire avec le price action
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Indicators filter price action with formulas. As such, they are derivatives and not direct reflections of the price action... Any analysis of an indicator should be taken with the price action in mind. »
**TRADEX-AI C1** : Garde-fou méthodologique — un indicateur ne remplace jamais la lecture du prix. Cohérent avec la priorité Belkhayate (prix d'abord). Tout signal indicateur doit être croisé au price action.
*Catégorie : signal*
---

### D2314 — Signaux d'indicateurs à recouper avec le contexte (exemple MACD + triangle descendant)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Even though it may be obvious when indicators generate buy and sell signals, the signals should be taken in context with other technical analysis tools. An indicator may flash a buy signal, but if the chart pattern shows a descending triangle with a series of declining peaks, it may be a false signal. »
**TRADEX-AI C1** : Une non-confirmation du prix (ex. divergence MACD haussière mais résistance non franchie) doit invalider le signal. Principe de non-confirmation à intégrer comme critère éliminatoire.
*Catégorie : signal*
---

### D2315 — Choisir peu d'indicateurs (2-3), complémentaires et non redondants
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Attempts to cover more than five indicators are usually futile; it is best to focus on two or three indicators and learn their intricacies inside and out. Try to choose indicators that complement each other, instead of those that move in unison... it would be redundant to use two indicators that are good for showing overbought and oversold levels, such as Stochastics and RSI. »
**TRADEX-AI C1** : Garde-fou de conception — limiter à 2-3 indicateurs complémentaires ; éviter la redondance (ex. RSI + Stochastique mesurent tous deux le momentum). Évite la sur-confirmation illusoire dans la grille /10.
*Catégorie : signal*
---

### D2316 — Indicateurs avançants (leading) : momentum sur lookback fixe
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « As their name implies, leading indicators are designed to lead price movements. Most represent a form of price momentum over a fixed lookback period... Some of the more popular leading indicators include Commodity Channel Index (CCI), Momentum, Relative Strength Index (RSI), Stochastic Oscillator, and Williams %R. »
**TRADEX-AI C1** : Famille des indicateurs avançants (CCI, Momentum, RSI, Stochastique, Williams %R) basés sur le momentum d'une fenêtre fixe. Catégorie d'outils candidats pour anticiper les retournements.
*Catégorie : indicateurs_tendance*
---

### D2317 — Momentum = taux de variation du prix (rate-of-change)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Generally speaking, momentum measures the rate-of-change of a security's price. As the price of a security rises, price momentum increases. The faster the security rises... the larger the increase in momentum. Once this rise begins to slow, momentum will also slow. »
**TRADEX-AI C1** : Définition opérationnelle du momentum = vitesse de variation du prix. Un ralentissement du momentum en trading latéral n'est pas forcément baissier (retour à un niveau médian). Nuance à coder pour éviter faux signaux.
*Catégorie : indicateurs_tendance*
---

### D2318 — RSI : compare gains moyens et pertes moyennes sur la période
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « RSI (a momentum indicator) compares the average price change of the advancing periods with the average change of the declining periods. »
**TRADEX-AI C1** : Principe de calcul du RSI exploitable — moyenne des variations haussières vs baissières. Indicateur de momentum candidat ; ne pas confondre avec l'Énergie/MFI Belkhayate (verrouillée).
*Catégorie : indicateurs_tendance*
---

### D2319 — Bénéfices/risques des leading : signaux précoces mais plus de faux signaux
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « they allow for early signaling for entry and exit. Leading indicators generate more signals and allow more opportunities to trade... More signals and earlier signals mean that the chances of false signals and whipsaws increase. False signals will increase the potential for losses. »
**TRADEX-AI C1** : Arbitrage des indicateurs avançants — entrées/sorties précoces au prix de plus de whipsaws. À utiliser de préférence dans le sens de la tendance majeure (achat sur survente en uptrend, vente sur surachat en downtrend).
*Catégorie : gestion_risque_entree*
---

### D2320 — Indicateurs retardés (lagging) : trend-following, efficaces en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « lagging indicators follow the price action and are commonly referred to as trend-following indicators... Trend-following indicators work best when markets or securities develop strong trends... they are not effective in trading or sideways markets. If used in trading markets, trend-following indicators will likely lead to many false signals and whipsaws. Some popular trend-following indicators include moving averages... and MACD. »
**TRADEX-AI C1** : Famille des indicateurs retardés (moyennes mobiles, MACD) — performants en tendance forte, désastreux en range. Critère : n'activer ces signaux que si une tendance est confirmée (cf. ADX D2330).
*Catégorie : indicateurs_tendance*
---

### D2321 — Croisement de moyennes mobiles : trade-off longueur/whipsaws
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Using a moving average crossover to generate the signals... Had these moving averages been longer (50- and 200-day moving averages), there would have been fewer whipsaws. Had these moving averages been shorter (10 and 50-day moving average), there would have been more whipsaws, more signals, and earlier signals. »
**TRADEX-AI C1** : Réglage des croisements MM — plus long = moins de whipsaws mais plus de retard ; plus court = plus de signaux/faux signaux. Paramètre d'arbitrage à calibrer sur range bars NT8.
*Catégorie : indicateurs_tendance*
---

### D2322 — Drawback lagging : entrées/sorties tardives biaisent le risk/reward
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « Another drawback of trend-following indicators is that signals tend to be late. By the time a moving average crossover occurs, a significant portion of the move has already occurred... Late entry and exit points can skew the risk/reward ratio. »
**TRADEX-AI C5** : Risque structurel des indicateurs retardés — l'entrée tardive dégrade le ratio R/R. Renforce l'exigence TRADEX R/R ≥ 1:2 : un signal lagging doit encore offrir un R/R acceptable au moment de l'entrée.
*Catégorie : gestion_risque_entree*
---

### D2323 — Trade-off fondamental : sensibilité vs cohérence
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « For technical indicators, there is a trade-off between sensitivity and consistency... If we increase the sensitivity by reducing the number of periods, an indicator will provide early signals, but the number of false signals will increase. If we decrease sensitivity by increasing the number of periods, then the number of false signals will decrease, but the signals will lag... A 14 period RSI will generate fewer signals than a 5 period RSI. »
**TRADEX-AI C1** : Loi générale de paramétrage — il n'existe pas de réglage parfait ; chaque période arbitre précocité contre fiabilité. Choix à fixer selon le style (range bars / scalping).
*Catégorie : indicateurs_tendance*
---

### D2324 — Définition d'un oscillateur : fluctue autour d'une ligne / entre des bornes
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « An oscillator is an indicator that fluctuates above and below a centerline or between set levels as its value changes over time. Oscillators can remain at extreme levels (overbought or oversold) for extended periods, but they cannot trend for a sustained period. »
**TRADEX-AI C1** : Définition structurelle de l'oscillateur — borné, ne « trende » pas durablement (contrairement à un indicateur cumulatif type OBV). Détermine quel outil convient à quel régime de marché.
*Catégorie : indicateurs_tendance*
---

### D2325 — Deux familles : oscillateurs centrés vs oscillateurs à bandes
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « centered oscillators which fluctuate above and below a center point or line and banded oscillators which fluctuate between overbought and oversold extremes. Generally, centered oscillators are best suited for analyzing the direction of price momentum, while banded oscillators are best suited for identifying overbought and oversold levels. »
**TRADEX-AI C1** : Taxonomie — oscillateurs centrés (direction du momentum) vs à bandes (surachat/survente). Oriente le choix d'outil selon qu'on cherche la direction ou les extrêmes.
*Catégorie : indicateurs_tendance*
---

### D2326 — MACD : oscillateur centré, à la fois retardé et avançant
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « MACD is the difference between the 12-day EMA and 26-day EMA of a security... MACD is unique in that it has lagging elements as well as leading elements. Moving averages are lagging indicators... However, by taking the differences in the moving averages, MACD incorporates aspects of momentum or leading elements... MACD has forged a unique spot among oscillators as both a lagging and a leading indicator. »
**TRADEX-AI C1** : MACD = EMA(12) − EMA(26), hybride retardé/avançant. Particularité utile : combine direction de tendance (MM) et momentum (différence) en un seul outil.
*Catégorie : indicateurs_tendance*
---

### D2327 — Seuils standard des oscillateurs à bandes (RSI 70/30, Stochastique 80/20, CCI ±100)
🟡 **CONVENTION** (Source : introduction_to_technical_indicators_and_oscillators.md) : « For RSI, the bands for overbought and oversold are usually set at 70 and 30 respectively... For the Stochastic Oscillator, a reading above 80 is overbought, while a reading below 20 is oversold... the majority of CCI values fall between -100 and +100... it can be used to determine overbought and oversold levels. »
**TRADEX-AI C1** : Seuils conventionnels surachat/survente — RSI 70/30, Stochastique 80/20, CCI ±100. Bornes par défaut ajustables selon la volatilité de l'actif (GC/CL plus volatils peuvent justifier un fine-tuning).
*Catégorie : signal*
---

### D2328 — Divergences positives/négatives = avertissement de retournement
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « a negative divergence is when an indicator declines while the underlying security advances. A positive divergence is when the indicator advances while the underlying security declines... A negative divergence occurs when the underlying security moves to a new high, but the indicator fails to record a new high... a positive divergence shows less downside momentum that can sometimes foreshadow a bullish reversal. Not all... divergences result in good signals, especially during a strong [up/down]trend. »
**TRADEX-AI C1** : Divergence = signal d'avertissement de retournement (négative = prix↑ / indic↓ ; positive = prix↓ / indic↑). NUANCE : peu fiable contre une tendance forte → à pondérer dans la grille, pas un signal autonome.
*Catégorie : signal*
---

### D2329 — Robustesse par confirmation multiple ; « la tendance est ton amie »
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « In a strong trend, oscillator signals against the direction of the underlying trend are less robust than those with the trend. The trend is your friend and it can be dangerous to fight it... To improve the robustness of oscillator signals, traders can look for multiple signals. A buy signal might be generated with an oversold reading, positive divergence, and bullish moving average crossover. »
**TRADEX-AI C1** : Principe directeur — combiner 3 signaux confirmants (ex. survente + divergence positive + croisement MM haussier) et ne jamais trader contre la tendance majeure. Cohérent avec la logique d'alignement multi-critères TRADEX (3/4 + 2/3).
*Catégorie : signal*
---

### D2330 — Banded oscillators : surachat ≠ signal de vente ; usage en range
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_technical_indicators_and_oscillators.md) : « overbought is not meant to act as a sell signal, and oversold is not meant to act as a buy signal. Overbought and oversold situations serve as an alert... When the trend is strong, banded oscillators can remain near overbought or oversold levels for extended periods... Banded oscillators are best used in trading ranges or with securities that are not trending. »
**TRADEX-AI C5** : Garde-fou crucial — un surachat/survente est une ALERTE, pas un ordre. En tendance forte l'oscillateur peut rester extrême longtemps. Les oscillateurs à bandes sont à privilégier en range, pas en tendance. Évite les entrées contre-tendance prématurées.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie |
|---|----------|-----|--------|-----------|
| D2311 | Définition indicateur = formule sur prix | 🟢 | C1 | indicateurs_tendance |
| D2312 | 3 fonctions : alerter / confirmer / prédire | 🟢 | C1 | signal |
| D2313 | Indicateur = dérivé, lire avec le prix | 🟢 | C1 | signal |
| D2314 | Recouper signaux au contexte (non-confirmation) | 🟢 | C1 | signal |
| D2315 | Limiter à 2-3 indicateurs complémentaires | 🟢 | C1 | signal |
| D2316 | Indicateurs avançants (CCI/RSI/Stoch/W%R) | 🟢 | C1 | indicateurs_tendance |
| D2317 | Momentum = rate-of-change du prix | 🟢 | C1 | indicateurs_tendance |
| D2318 | RSI = gains moyens vs pertes moyennes | 🟢 | C1 | indicateurs_tendance |
| D2319 | Leading : précoce mais plus de faux signaux | 🟢 | C1 | gestion_risque_entree |
| D2320 | Lagging trend-following, KO en range | 🟢 | C1 | indicateurs_tendance |
| D2321 | Croisement MM : trade-off longueur/whipsaws | 🟢 | C1 | indicateurs_tendance |
| D2322 | Lagging tardif biaise le R/R | 🟢 | C5 | gestion_risque_entree |
| D2323 | Trade-off sensibilité vs cohérence | 🟢 | C1 | indicateurs_tendance |
| D2324 | Définition oscillateur (borné, ne trende pas) | 🟢 | C1 | indicateurs_tendance |
| D2325 | Centrés vs à bandes | 🟢 | C1 | indicateurs_tendance |
| D2326 | MACD = EMA12−EMA26, hybride | 🟢 | C1 | indicateurs_tendance |
| D2327 | Seuils RSI 70/30, Stoch 80/20, CCI ±100 | 🟡 | C1 | signal |
| D2328 | Divergences positives/négatives | 🟢 | C1 | signal |
| D2329 | Confirmation multiple + sens de la tendance | 🟢 | C1 | signal |
| D2330 | Surachat ≠ vente ; oscillateurs en range | 🟢 | C5 | gestion_risque_entree |

**Lien Belkhayate :** NON CONCERNÉ globalement (article générique sur indicateurs/oscillateurs, école StockCharts). ⚫🔴 Point de vigilance : le RSI (D2318) et la notion de momentum (D2317) NE doivent PAS être confondus avec l'« Énergie » Belkhayate = MFI standard (verrouillée, non codée) — risque de doublon conceptuel à éviter lors d'une éventuelle implémentation.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, non fusionnée dans KNOWLEDGE_BASE_MASTER.json.
