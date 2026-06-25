# Extraction StockCharts — Pring's Know Sure Thing (KST)
**Source :** `bundles/stockcharts/prings_know_sure_thing_kst.md` (HTTP 200 · ~7 700 car.) + 11 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D3251 → D3270 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-know-sure-thing-kst
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.png | Chart 1 | SharpCharts Calculation |
| image_02.png | Spreadsheet | SharpCharts Calculation |
| image_03.png | Chart 2 | Interpretating KST |
| image_04.png | Chart 3 | Divergences |
| image_05.png | Chart 4 | Strong Trends |
| image_06.png | Chart 5 | Timeframes |
| image_07.png | Chart 6 | Timeframes |
| image_08.png | Chart 7 | Timeframes |
| image_09.png | Chart 8 | Further Tweaks |
| image_10.png | Chart 9 | Using with SharpCharts |
| image_11.png | Chart 10 | Using with SharpCharts |

## DÉCISIONS

### D3251 — Origine et définition du KST
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « Developed by Martin Pring, Know Sure Thing (KST) is a momentum oscillator based on the smoothed rate-of-change for four different timeframes. Pring first described the indicator in the 1992 "Summed Rate of Change (KST)" in *Stocks & Commodities* magazine. In short, KST measures price momentum for four different price cycles, combining them into a single momentum oscillator. »
**TRADEX-AI C3** : Oscillateur de momentum Pring agrégeant le rate-of-change lissé de 4 cycles de prix en une seule courbe. Brique momentum école Pring.
*Catégorie : indicateurs_momentum*
---

### D3252 — Usages prévus par Pring
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « Like any other unbound momentum oscillator, chartists can use KST to look for divergences, signal line crossovers, and centerline crossovers. Pring frequently applied trend lines to KST. Although trend line signals do not occur often, Pring notes that such breaks reinforce signal line crossovers. »
**TRADEX-AI C3** : Trois familles de signaux — divergences, croisements de ligne de signal, croisements de la ligne zéro. Les cassures de trend lines tracées sur le KST renforcent les croisements de signal.
*Catégorie : signal*
---

### D3253 — Formule KST (4 RCMA pondérés)
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_01) : « RCMA1 = 10-Period SMA of 10-Period Rate-of-Change ; RCMA2 = 10-Period SMA of 15-Period Rate-of-Change ; RCMA3 = 10-Period SMA of 20-Period Rate-of-Change ; RCMA4 = 15-Period SMA of 30-Period Rate-of-Change. KST = (RCMA1 x 1) + (RCMA2 x 2) + (RCMA3 x 3) + (RCMA4 x 4). Signal Line = 9-period SMA of KST. »
**TRADEX-AI C3** : Formule déterministe codable (niveau 1, 0$) : 4 rate-of-change (10/15/20/30) lissés par SMA puis pondérés 1/2/3/4 et sommés ; ligne de signal = SMA 9 du KST.
*Catégorie : indicateurs_momentum*
---

### D3254 — Pondération croissante des cycles
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « These combinations are then weighted and summed. The shortest timeframe carries the least weight (1) and the longest timeframe carries the most weight (4). A 9-period simple moving average is added as a signal line. »
**TRADEX-AI C3** : Le cycle le plus court pèse le moins (1), le plus long le plus (4) → le KST privilégie le momentum de fond. Logique de pondération à respecter dans toute réimplémentation.
*Catégorie : indicateurs_momentum*
---

### D3255 — Paramètres par défaut KST(10,15,20,30,10,10,10,15,9)
🟡 **CONVENTION** (Source : prings_know_sure_thing_kst.md) : « The default parameters are as follows: KST(10,15,20,30,10,10,10,15,9). The first four numbers represent the rate-of-change settings, the second four represent the moving averages for these rate-of-change indicators, and the last number is the signal line moving average. »
**TRADEX-AI C3** : Convention de paramétrage par défaut (daily). Décodage : 4 ROC + 4 SMA de lissage + 1 SMA signal. Point de départ avant tout calibrage.
*Catégorie : configuration*
---

### D3256 — Interprétation de base (zéro = arbitre bulls/bears)
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_03) : « KST fluctuates above/below the zero line. At its most basic, momentum favors the bulls when KST is positive and favors the bears when KST is negative. A positive reading means the weighted and smoothed rate-of-change values are mostly positive, and prices are moving higher. A negative reading indicates that prices are moving lower. »
**TRADEX-AI C3** : Lecture binaire — KST positif = momentum haussier, négatif = momentum baissier. Filtre directionnel simple pour le scoring.
*Catégorie : signal*
---

### D3257 — Croisements de ligne de signal et direction
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « After basic centerline crossovers, chartists can look for signal line crossovers and gauge general direction. KST generally rises when above its signal line and falls when below its signal line. A rising and negative KST line indicates that downside momentum is waning. Conversely, a falling and positive KST line indicates that upside momentum is waning. »
**TRADEX-AI C3** : KST > signal = direction haussante ; KST < signal = baissante. Un KST négatif mais montant = momentum baissier en essoufflement (alerte précoce de retournement).
*Catégorie : signal*
---

### D3258 — Signaux les plus robustes = zéro + ligne de signal
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « Even though many different signals are possible with KST, the basic centerline and signal line crossovers are usually the most robust. »
**TRADEX-AI C3** : Hiérarchie de fiabilité — privilégier les croisements de la ligne zéro et de la ligne de signal aux autres lectures. Cœur déclencheur à coder en priorité.
*Catégorie : signal*
---

### D3259 — KST non borné → inadapté surachat/survente
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md) : « Unlike the Relative Strength Index (RSI) and Stochastic Oscillator, KST does not have upper or lower limits. This makes it relatively ill-suited for overbought and oversold signals. »
**TRADEX-AI C3** : Garde-fou — oscillateur non borné, ne PAS l'utiliser pour des seuils surachat/survente (contrairement à RSI/Stochastique). Réserver au momentum directionnel.
*Catégorie : indicateurs_momentum*
---

### D3260 — Divergences possibles mais à filtrer
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_04) : « Bullish and bearish divergences are also possible for signals, but chartists must be selective when using these. Most divergences in the basic rate-of-change indicator do not result in price reversals. Similarly, divergences in MACD and RSI are also prone to failure. It is probably best to use divergences when there is a large and blatant divergence. »
**TRADEX-AI C3** : Garde-fou divergences — la plupart ne donnent pas de retournement (vrai aussi pour ROC/MACD/RSI). N'exploiter que les divergences larges et flagrantes.
*Catégorie : divergence*
---

### D3261 — Divergences confirmées par croisement de signal
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_04) : « The example below shows a chart with a large bearish and bullish divergence. These divergences were finalized with subsequent signal line crossovers (red and green arrows). »
**TRADEX-AI C3** : Bonne pratique — attendre que la divergence soit "finalisée" par un croisement de ligne de signal avant d'agir. Réduit les faux signaux de divergence.
*Catégorie : divergence*
---

### D3262 — Tendances fortes : crossovers baissiers piégeux
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_05) : « Chartists should be careful with bearish signal line crossovers in strong uptrends and bullish signal line crossovers in strong downtrends. KST can move into positive territory and remain in positive territory for an extended period during a strong uptrend. The indicator will reach a relatively high level and then turn down but never move into negative territory. This simply signals that upside momentum is slowing; it is still stronger than downside momentum but not as strong as in previous periods. »
**TRADEX-AI C3** : Garde-fou tendance forte — en uptrend marqué, un croisement baissier du signal = simple ralentissement du momentum, PAS un retournement. Ne pas inverser la position sur ce seul signal.
*Catégorie : structure_marche*
---

### D3263 — Exemple SHW : KST reste positif tout l'uptrend
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_05) : « The example below shows Sherwin Williams (SHW) with a strong uptrend from November 2011 to August 2012. Even though KST fluctuated up and down, it never broke below zero and remained in positive territory the entire time. The bearish signal line crossovers indicated a slowing in upside momentum, not a trend change. »
**TRADEX-AI C3** : Cas historique illustrant D3262 — KST resté positif toute la durée de l'uptrend. La ligne zéro non franchie = tendance intacte malgré croisements de signal baissiers.
*Catégorie : structure_marche*
---

### D3264 — Trois jeux de réglages par horizon (court/moyen/long)
🟡 **CONVENTION** (Source : prings_know_sure_thing_kst.md, image_06) : « Short-term Daily = KST(10,15,20,30,10,10,10,15,9) ; Medium-term Weekly = KST(10,13,15,20,10,13,15,20,9) ; Long-term Monthly = KST(9,12,18,24,6,6,6,9,9). »
**TRADEX-AI C3** : Trois paramétrages distincts selon l'horizon. Pour TRADEX (intraday/daily), le jeu court-terme daily est la référence de départ.
*Catégorie : configuration*
---

### D3265 — Adapter les réglages plutôt que changer de TF
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_07) : « As noted in Pring's articles, KST can be used on a short-term, medium-term or long-term timeframe. Instead of just shifting between daily, weekly and monthly charts, Pring suggested changing the settings to suit each timeframe. KST is even smoother when using the weekly and monthly settings. »
**TRADEX-AI C3** : Pring recommande d'ajuster les paramètres KST à l'horizon visé plutôt que de seulement changer de timeframe. Réglages weekly/monthly = courbe encore plus lissée.
*Catégorie : configuration*
---

### D3266 — Sur weekly/monthly : préférer les croisements de signal
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_08) : « This means chartists should use signal line crossovers to detect directional changes in price. The lag for centerline crossovers is often too great. »
**TRADEX-AI C3** : Sur horizons longs, les croisements de ligne de signal priment ; le croisement de ligne zéro a trop de retard. Choix du déclencheur dépend de l'horizon.
*Catégorie : signal*
---

### D3267 — Personnalisation et mixage des réglages
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_09) : « Pring encourages chartists to try different settings because one size does not fit all. Utility and consumer staples are less volatile and may require more sensitive settings, while technology stocks are more volatile and may require less sensitive settings. Chartists can also mix and match the rate-of-change and moving average settings. »
**TRADEX-AI C3** : Réglages à adapter à la volatilité de l'actif — actif peu volatil = réglages plus sensibles, actif volatil = moins sensibles. Pertinent pour calibrer par actif GC/HG/CL/ZW.
*Catégorie : configuration*
---

### D3268 — KST pondéré court terme (variante)
🟡 **CONVENTION** (Source : prings_know_sure_thing_kst.md, image_09) : « Instead of KST(10,15,20,30,10,10,10,15,9) the second window shows KST(30,20,15,10,10,10,10,10,9). The first rate-of-change setting carries the least weight and the fourth one carries the most weight. »
**TRADEX-AI C3** : Variante inversant l'ordre des ROC (30,20,15,10) pour donner le plus de poids au cycle court → KST plus réactif. Option de configuration documentée.
*Catégorie : configuration*
---

### D3269 — Positionnement KST et synthèse usage
🔵 **ÉCOLE (Pring)** (Source : prings_know_sure_thing_kst.md, image_10) : « KST can be used like other unbound momentum oscillators, such as MACD, the Percentage Price Oscillator (PPO), and TRIX. KST closely resembles TRIX. Because it is unbound, KST is not well suited for identifying overbought and oversold conditions. KST's creator, Martin Pring, favors signal line crossovers and trend line breaks for signals. As with all indicators, KST should be combined with other analysis techniques. »
**TRADEX-AI C3** : Famille MACD/PPO/TRIX, proche de TRIX. Signaux privilégiés par Pring = croisements de signal + cassures de trend line. À combiner avec d'autres analyses (cohérent avec règle 3/4+2/3).
*Catégorie : indicateurs_momentum*
---

### D3270 — Scans bullish/bearish KST avec filtres liquidité
🟡 **CONVENTION** (Source : prings_know_sure_thing_kst.md) : Scan bullish — « [KST > 0] AND [KST x KST Signal] » avec filtres `[type = stock] AND [country = US] AND [Daily SMA(20,Daily Volume) > 40000] AND [Daily SMA(60,Daily Close) > 20]`. Scan bearish — « [KST < 0] AND [KST Signal x KST] » mêmes filtres.
**TRADEX-AI C7** : Bonne pratique de screening — exiger KST côté zéro cohérent (positif pour achat, négatif pour vente) ET croisement de signal, avec filtres de liquidité/prix. Le filtre volume/prix renvoie au contrôle de liquidité (cohérent order flow C2).
*Catégorie : signal*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3251 → D3270 (20 décisions) |
| Images certifiées | 11/11 |
| Cercle dominant | C3 (momentum) · renvois C7/screening (D3270) |
| Tags | 🔵 ÉCOLE Pring ×15 · 🟡 CONVENTION ×5 (D3255, D3264, D3268, D3270) |
| Catégories | indicateurs_momentum, signal, configuration, divergence, structure_marche |
| Actifs concernés | GC · HG · CL · ZW (applicable tous TF, calibrage par volatilité d'actif) |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Paramètres clés | Daily KST(10,15,20,30,10,10,10,15,9) · Weekly (10,13,15,20,…,9) · Monthly (9,12,18,24,6,6,6,9,9) · signal = SMA 9 |
| À vérifier | Aucun cas — 11/11 images certifiées, texte complet |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
