# Extraction StockCharts — Percentage Price Oscillator (PPO)

**Source :** `bundles/stockcharts/percentage_price_oscillator_ppo.md` (HTTP 200 · ~8 400 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D3071 → D3090 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-price-oscillator-ppo
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | PPO - Chart 1 | How Do You Calculate the PPO? | CERTIFIÉ |
| image_02.png | PPO - Chart 2 | MACD, PPO, and Price | CERTIFIÉ |
| image_03.png | PPO - Chart 3 | PPO: A Solution to MACD Sensitivity to Large Price Changes | CERTIFIÉ |
| image_04.png | PPO - Chart 4 | Using PPO To Compare Different Securities | CERTIFIÉ |
| image_05.png | PPO - Chart 5 | Using PPO To Compare Different Securities | CERTIFIÉ |
| image_06.png | PPO - Chart 6 | Using with SharpCharts | CERTIFIÉ |
| image_07.png | PPO - Chart 7 | Using with SharpCharts | CERTIFIÉ |

## DÉCISIONS

### D3071 — PPO : oscillateur de momentum = écart entre 2 MM en % de la plus longue
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « The Percentage Price Oscillator (PPO) is a momentum oscillator that measures the difference between two moving averages as a percentage of the larger moving average. It's used to identify price trend direction, momentum, and potential buy and sell signals. »
**TRADEX-AI C3** : indicateur de momentum mesurant l'écart relatif (en %) entre deux moyennes mobiles ; sert direction de tendance, momentum, signaux.
*Catégorie : indicateurs_momentum*

---

### D3072 — PPO affiché comme MACD : ligne de signal, histogramme, centerline
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « As with its cousin, MACD, the PPO is shown with a signal line, a histogram, and a centerline. Trading signals are generated with signal line crossovers, centerline crossovers, and divergences. »
**TRADEX-AI C3** : signaux identiques au MACD — croisements ligne de signal, croisements de la centerline, divergences.
*Catégorie : indicateurs_momentum*

---

### D3073 — Avantage 1 : PPO indépendant du niveau de prix du titre
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « First, PPO readings are not subject to the price level of the security. Second, PPO readings for different securities can be compared, even when there are large differences in the price. »
**TRADEX-AI C7** : propriété clé pour le comparatif inter-marché — le PPO est normalisé, donc comparable entre actifs de prix très différents (utile matrice corrélations GC/HG/CL/ZW).
*Catégorie : indicateurs_momentum*

---

### D3074 — Formule du PPO
🟡 **CONVENTION** (Source : percentage_price_oscillator_ppo.md) : « Percentage Price Oscillator (PPO): {(12-day EMA - 26-day EMA)/26-day EMA} x 100 »
**TRADEX-AI C3** : formule déterministe — PPO = (EMA12 − EMA26) / EMA26 × 100.
*Catégorie : indicateurs_momentum*

---

### D3075 — Ligne de signal = EMA 9 jours du PPO
🟡 **CONVENTION** (Source : percentage_price_oscillator_ppo.md) : « Signal Line: 9-day EMA of PPO »
**TRADEX-AI C3** : ligne de signal = moyenne mobile exponentielle 9 périodes du PPO.
*Catégorie : indicateurs_momentum*

---

### D3076 — Histogramme PPO = PPO − ligne de signal
🟡 **CONVENTION** (Source : percentage_price_oscillator_ppo.md) : « PPO Histogram: PPO - Signal Line »
**TRADEX-AI C3** : histogramme = différence PPO − ligne de signal ; positif quand PPO > EMA9, négatif sinon.
*Catégorie : indicateurs_momentum*

---

### D3077 — PPO = MACD divisé par la MM lente (valeur relative vs absolue)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « While MACD measures the absolute difference between two moving averages, PPO makes this a relative value by dividing the difference by the slower moving average (26-day EMA). PPO is the MACD value divided by the longer moving average. »
**TRADEX-AI C3** : distinction fondamentale — MACD = écart absolu ; PPO = écart relatif (MACD / EMA26 × 100). Exemple INTC : MACD −44c à +64c ⇒ PPO −2.01 % à +2.85 %.
*Catégorie : indicateurs_momentum*

---

### D3078 — Paramètres standard 12/26/9 modifiables, basés sur clôtures
🟡 **CONVENTION** (Source : percentage_price_oscillator_ppo.md) : « Standard PPO is based on the 12-day Exponential Moving Average (EMA) and the 26-day EMA, but these parameters can be changed according to investor or trader preferences. Closing prices are used to calculate the moving averages [...] A 9-day EMA of PPO is plotted as a signal line. »
**TRADEX-AI C3** : réglages 12/26/9 par défaut, ajustables ; signaux à mesurer contre les clôtures.
*Catégorie : configuration*

---

### D3079 — PPO positif = MM courte au-dessus de la MM longue (momentum haussier)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « PPO is positive when the shorter moving average is above the longer moving average. The indicator moves further into positive territory as the shorter moving average distances itself from the longer moving average. This reflects strong upside momentum. »
**TRADEX-AI C3** : lecture haussière — PPO > 0 et croissant ⇒ MM courte s'éloigne au-dessus de la MM longue (momentum haussier fort).
*Catégorie : indicateurs_momentum*

---

### D3080 — PPO négatif = MM courte sous la MM longue (momentum baissier)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « The PPO is negative when the shorter moving average is below the longer moving average. Negative readings grow when the shorter moving average distances itself from the longer moving average (goes further negative). This reflects strong downside momentum. »
**TRADEX-AI C3** : lecture baissière — PPO < 0 et décroissant ⇒ momentum baissier fort.
*Catégorie : indicateurs_momentum*

---

### D3081 — Histogramme PPO anticipe les croisements de la ligne de signal
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « The histogram is positive when PPO is above its 9-day EMA and negative when PPO is below its 9-day EMA. The PPO-Histogram can be used to anticipate signal line crossovers in the PPO. »
**TRADEX-AI C3** : l'histogramme sert d'indicateur avancé des croisements ligne de signal (mêmes règles que MACD Histogram).
*Catégorie : indicateurs_momentum*

---

### D3082 — MACD sensible au prix : valeurs élevées sur titres chers
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md, image_02) : « MACD levels are affected by the price of a security. A high-priced security will have higher or lower MACD values than a low-priced security, even if volatility is basically equal. [...] MACD for the Dow Industrials, which is above 10,000, hits triple digits on a regular basis. However, the PPO ranges from -2 to +2. »
**TRADEX-AI C3** : limite du MACD que le PPO corrige — les niveaux MACD dépendent du prix nominal ; le PPO reste dans une plage définissable.
*Catégorie : indicateurs_momentum*

---

### D3083 — Subtilité : divergence PPO vs MACD (momentum baissier élargi, Google)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « In the Google example, notice how the PPO broke below the February low, but MACD has yet to break its February low. The lower low in the PPO shows expanding downside momentum. »
**TRADEX-AI C3** : le PPO peut révéler des divergences plus tôt/différemment que le MACD ; un plus-bas PPO non confirmé par MACD = momentum baissier en expansion.
*Catégorie : divergence*

---

### D3084 — PPO résout la sensibilité du MACD aux grandes variations de prix (BIDU)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md, image_03) : « If a stock advances from 20 to 100, its MACD levels will be considerably smaller, closer to 20 than 100. The PPO solves this problem by showing MACD values in percentage terms. [...] Baidu becomes overbought when the PPO exceeds +5. »
**TRADEX-AI C3** : sur un titre qui passe de 25 à 75, MACD se distord alors que le PPO reste cohérent ; ex. seuil de surachat PPO > +5 sur BIDU.
*Catégorie : indicateurs_momentum*

---

### D3085 — PPO permet de comparer le momentum entre titres (DELL vs HPQ)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md, image_04/image_05) : « we can apply the Percentage Price Oscillator (PPO) to compare momentum. [...] the PPO for DELL ranges from -4 to +4 [...] The PPO for HPQ ranges from -3 to +2 [...] we can see that DELL is more volatile than HPQ because its PPO range is greater. »
**TRADEX-AI C7** : usage inter-marché — comparer les amplitudes PPO révèle la volatilité et la force de momentum relatives entre actifs.
*Catégorie : indicateurs_momentum*

---

### D3086 — Une plus grande amplitude PPO = plus de volatilité
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « A security with a larger PPO range is generally more volatile than one with a smaller range. » (FAQ)
**TRADEX-AI C7** : règle d'interprétation de volatilité relative via l'amplitude PPO comparée entre titres.
*Catégorie : indicateurs_momentum*

---

### D3087 — PPO mêmes signaux que MACD + dimension % comparable dans le temps
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « The PPO generates the same signals as the MACD, but provides an added dimension as a percentage version of MACD. [...] PPO levels in one security can be compared over extended periods, even if the price has doubled or tripled. This is not the case for the MACD. »
**TRADEX-AI C3** : avantage temporel — les niveaux PPO d'un même titre restent comparables sur la durée malgré un doublement/triplement du prix.
*Catégorie : indicateurs_momentum*

---

### D3088 — Limite : PPO mal adapté au surachat/survente (mouvements illimités)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « the PPO is still not the best oscillator to identify overbought or oversold conditions because movements are unlimited (in theory). Levels for RSI and the Stochastic Oscillator are limited, making them better suited to identifying overbought and oversold levels. »
**TRADEX-AI C3** : limite d'usage — ne pas utiliser le PPO pour le surachat/survente ; préférer RSI ou Stochastique (bornés) à cet effet.
*Catégorie : indicateurs_momentum*

---

### D3089 — Scan haussier : Close > SMA200 + croisement haussier ligne signal PPO en zone < 0
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « PPO Bullish Signal Line Cross [...] trading above their 200-day moving average and have a bullish signal line crossover in the PPO. Notice that the PPO is required to be negative to ensure that this upturn occurs after a pullback. »
**TRADEX-AI C3** : critère déterministe long — Close > SMA200 ET croisement PPO au-dessus de sa ligne de signal ET PPO < 0 (cassure après pullback).
*Catégorie : signal*

---

### D3090 — Scan baissier : Close < SMA200 + croisement baissier ligne signal PPO en zone > 0
🟢 **FAIT VÉRIFIÉ** (Source : percentage_price_oscillator_ppo.md) : « PPO Bearish Signal Line Cross [...] trading below their 200-day moving average and have a bearish signal line crossover in PPO. Notice that the PPO is required to be positive to ensure that this downturn occurs after a bounce. »
**TRADEX-AI C3** : critère déterministe short — Close < SMA200 ET croisement PPO sous sa ligne de signal ET PPO > 0 (retournement après rebond).
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3071 → D3090 (20) |
| Images certifiées | 7/7 |
| Tags | 🟢 FAIT VÉRIFIÉ (majorité) · 🟡 CONVENTION (formules/réglages D3074–D3076, D3078) |
| Cercle | C3 (momentum) dominant ; C7 (comparaison inter-marché : D3073, D3085, D3086) |
| Catégories | indicateurs_momentum, configuration, divergence, signal |
| Point clé | PPO = MACD normalisé en % (D3077) ⇒ comparable entre actifs et dans le temps ; idéal pour la matrice corrélations/momentum TRADEX |
| Limite | Ne pas utiliser pour surachat/survente (D3088) — préférer RSI/Stochastique |
| Belkhayate | NON CONCERNÉ (pas de lien MFI/Énergie) |
| Actifs | GC·HG·CL·ZW — momentum normalisé comparable entre eux |
| Cas à vérifier | Aucun — 0 image à vérifier ; tags 🟡 = formules conventionnelles à valider en fusion, pas de fait litigieux |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. NB : le PPO normalise le momentum (C3) et le rend comparable entre actifs — atout direct pour le cercle C7 (corrélations inter-marché GC/HG/CL/ZW).
