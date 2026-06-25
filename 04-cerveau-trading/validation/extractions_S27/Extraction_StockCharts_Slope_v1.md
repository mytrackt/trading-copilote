# Extraction StockCharts — Slope
**Source :** `bundles/stockcharts/slope.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D3611 → D3630 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/slope
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Indicateur de tendance et de force directement applicable sur GC/HG/CL/ZW pour qualifier la direction et l'intensité du trend, et pour comparaisons de force relative entre actifs.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Slope - Chart 1 (SPY 3 périodes 20j, canaux Raff Regression) | Calculating the Slope | D3611 |
| image_02 | Slope - Chart 2 (Dow Industrials 52-week Slope) | Trend Identification | D3614 |
| image_03 | Slope - Chart 3 (Nasdaq 100 QQQQ 100-day Slope + SMA 20j) | Trend Strength | D3616 |
| image_04 | Slope - Chart 4 (Apple 100-day Slope + Williams %R 10j) | Trade Bias | D3618 |
| image_05 | Slope - Chart 5 (Amazon AMZN + S&P 500, 20-day Slope comparé) | Relative Strength | D3620 |
| image_06 | (sans légende — SharpCharts UI screenshot) | Using with SharpCharts | D3628 |

## DÉCISIONS

### D3611 — Définition Slope : rise-over-run de la régression linéaire (line of best fit)
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_01) : « The slope indicator measures the rise-over-run of a linear regression, which is the line of best fit for a price series. » — Ex. : rise +4pts / run 2 jours = slope 2 ; rise -6pts / run 2 = slope -3.
**TRADEX-AI C1** : Slope = pente de régression linéaire sur N jours — indicateur quantitatif de direction et de vitesse du trend applicable sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D3612 — Slope positif = uptrend ; Slope négatif = downtrend
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « In general, an advancing period has a positive slope and a declining period has a negative slope. The steepness depends on the sharpness of the advance or decline. »
**TRADEX-AI C1** : Règle directionnelle de base : Slope > 0 → biais haussier ; Slope < 0 → biais baissier — à utiliser comme confirmateur de tendance Belkhayate (Direction).
*Catégorie : indicateurs_tendance*

### D3613 — Slope fluctue autour de zéro sans limites d'overbought/oversold — pas adapté pour ces niveaux
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « Fluctuating above and below zero, the Slope indicator best resembles a momentum oscillator without boundaries. It is not well suited for overbought/oversold levels, but can measure the direction and strength of a trend. »
**TRADEX-AI C1** : Ne pas utiliser le Slope comme oscillateur de surachat/survente — son usage est la direction et la force du trend, non les extrêmes.
*Catégorie : indicateurs_tendance*

### D3614 — Slope 52 semaines (1 an) comme identificateur de tendance long terme — lag inévitable
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_02) : « The 52-week Slope was positive for around two years (2006-2007) and then turned negative in February 2008. Even though the Dow bottomed in March 2009 and moved sharply higher, the 52-week Slope did not cross back into positive territory until September 2009. Notice that the slope does not predict the trend. Instead, it follows the trend or the price points. This means there will be some lag. »
**TRADEX-AI C1** : Slope 52 semaines = filtre de tendance long terme avec lag — utile pour définir le contexte macro de GC/CL/HG/ZW mais ne pas l'utiliser pour le timing précis d'entrée.
*Catégorie : indicateurs_tendance*

### D3615 — Slope ne prédit pas la tendance — il suit les prix avec un certain retard
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « the slope does not predict the trend. Instead, it follows the trend or the price points. This means there will be some lag. »
**TRADEX-AI C1** : Garde-fou important : le Slope est un indicateur retardé — ne pas l'utiliser seul pour les entrées, toujours combiner avec des indicateurs avancés (pivot Belkhayate, COG).
*Catégorie : gestion_risque_entree*

### D3616 — Analyse de la force du trend : Slope négatif + montant = amélioration dans downtrend ; Slope positif + baissant = détérioration dans uptrend
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_03) : « A negative and rising slope shows improvement within a downtrend. A positive and falling slope shows deterioration within an uptrend. »
**TRADEX-AI C1** : Nuance importante : la direction du Slope ET son niveau absolu sont tous deux informatifs — un Slope négatif qui monte signale une possible reprise imminente sur GC/CL.
*Catégorie : indicateurs_tendance*

### D3617 — SMA 20j appliquée sur le Slope comme leading indication de retournement
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_03) : « A 20-day simple moving average was added to identify upturns and downturns. A Slope is rising when above its 20-day SMA and falling when below. [...] the crossovers occurred before the Slope turned negative or positive. This is like a leading indication for the Slope. »
**TRADEX-AI C1** : Technique opérationnelle : appliquer SMA 20 sur le Slope — le croisement Slope/SMA précède le retournement du Slope lui-même → signal avancé de changement de tendance.
*Catégorie : indicateurs_tendance*

### D3618 — Utilisation du Slope pour établir un biais de trading (Trade Bias)
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_04) : « Slope can be used for trend identification to establish a trading bias. A positive slope dictates a bullish bias, while a negative Slope dictates a bearish bias. »
**TRADEX-AI C1** : Application directe : Slope(100) > 0 sur GC → biais haussier → ne prendre que les signaux ACHETER de Belkhayate ; Slope(100) < 0 → biais baissier → ne prendre que les signaux VENDRE.
*Catégorie : gestion_risque_entree*

### D3619 — Combinaison Slope (tendance) + oscillateur momentum (entrées) : paramètre Slope >> paramètre oscillateur
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « The look-back period for the Slope should be significantly longer than the look-back period for the momentum oscillator. The Slope defines the bigger trend, while the momentum oscillator represents a subset of that trend. »
🔵 **ÉCOLE** : Exemple : Slope 100j + Williams %R 10j sur Apple.
**TRADEX-AI C1** : Règle de paramétrage : utiliser Slope(100) comme filtre tendance long terme, puis oscillateur court terme (10-20j) pour les points d'entrée — cohérent avec la structure BGC/Direction Belkhayate.
*Catégorie : configuration*

### D3620 — Slope(100) passe au-dessus de zéro = établit un biais haussier → ne prendre QUE les signaux haussiers de l'oscillateur
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_04) : « Chart 4 shows the 100-day Slope moving above zero in July to establish a bullish bias. Only bullish signals are considered for the momentum oscillator. These include oversold readings, centerline crossovers, or signal line crossovers. »
**TRADEX-AI C1** : Règle de filtrage : Slope(100) > 0 → n'accepter que les signaux haussiers de l'oscillateur (survendu, croisement centerline, croisement signal line) — filtre tendance majeur.
*Catégorie : gestion_risque_entree*

### D3621 — Williams %R(10) < -80 = lecture survendue = pullback de court terme dans uptrend
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « The blue dotted lines show when 10-day Williams %R moves below -80% to become oversold. Notice that these readings correspond with short pullbacks in the stock. Except for the last oversold reading in early December, Apple resumed its uptrend soon after these oversold readings. »
**TRADEX-AI C1** : Williams %R(10) < -80 dans un uptrend (Slope > 0) = point d'entrée long potentiel sur pullback — applicable pour entrer sur GC/CL/HG lors de corrections dans tendance haussière.
*Catégorie : indicateurs_momentum*

### D3622 — Force relative via Slope : comparer Slope de deux actifs pour identifier force/faiblesse relative
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_05) : « The Slope of two (or more) securities can be compared to identify relative strength and relative weakness. [...] Amazon had a positive Slope and the S&P 500 had a negative Slope. Amazon was clearly outperforming the S&P 500 at this time. »
**TRADEX-AI C7** : Technique de force relative applicable entre actifs TRADEX : comparer Slope(20) de GC vs CL vs HG pour identifier quel actif est le plus fort → allouer le capital au plus fort.
*Catégorie : correlations*

### D3623 — Slope(20) d'Amazon positif en novembre + S&P négatif → Amazon en force relative évidente
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_05) : « when the S&P 500 bottomed in early November, Amazon led the way higher with a move from 117 to 143. Notice that Amazon moved higher even as the Slope moved lower. »
🟡 **SYNTHÈSE** : Un actif peut monter pendant que son Slope se réduit — la direction du mouvement prime sur la valeur absolue du Slope à court terme.
**TRADEX-AI C7** : Pour GC/HG/CL : un Slope positif mais décroissant ne signifie pas renversement immédiat — la montée peut continuer avec un Slope positif décroissant.
*Catégorie : indicateurs_tendance*

### D3624 — Timeframes du Slope : 10j = tendance court terme ; 100j = tendance moyen terme ; 250j = tendance long terme
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « 10 days covers a short-term trend, 100 days a medium-term trend, and 250 days a long-term trend. »
**TRADEX-AI C1** : Mapping des timeframes : Slope(10) pour signaux court terme, Slope(100) pour filtre moyen terme, Slope(250) pour contexte long terme — applicable sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D3625 — Slope, comme les moyennes mobiles, utile avec indicateurs momentum pour participer à une tendance en cours
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « As with moving averages, Slope can be used with momentum indicators to participate in an ongoing trend. »
**TRADEX-AI C1** : Slope = outil de participation au trend (non de prédiction) — combinaison systématique avec indicateurs momentum Belkhayate (BGC, Énergie) recommandée.
*Catégorie : configuration*

### D3626 — Scan "Oversold in Uptrend" : Slope(100) > 0 ET Williams %R(10) < -80
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : Scan défini : `[Daily Slope(100,Daily Close) > 0] AND [Daily Williams %R(10) < -80]`
⚫ **HYPOTHÈSE PROJET** : Ce scan peut être adapté pour filtrer les opportunités d'achat sur GC/HG/CL/ZW : Slope(100) > 0 + oscillateur Belkhayate en zone oversold.
**TRADEX-AI C1** : Logique du scan transposable pour TRADEX : trend positif 100j + momentum en pullback = zone d'entrée long optimale.
*Catégorie : gestion_risque_entree*

### D3627 — Scan "Overbought in Downtrend" : Slope(100) < 0 ET Williams %R(10) > -20
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : Scan défini : `[Daily Slope(100,Daily Close) < 0] AND [Daily Williams %R(10) > -20]`
⚫ **HYPOTHÈSE PROJET** : Transposable pour identifier les opportunités short sur GC/CL/HG/ZW : Slope(100) < 0 + oscillateur en zone overbought = zone d'entrée short optimale.
**TRADEX-AI C1** : Logique inverse du scan uptrend — utile pour valider les signaux VENDRE Belkhayate en contexte de downtrend confirmé.
*Catégorie : gestion_risque_entree*

### D3628 — Slope disponible dans SharpCharts avec paramètre par défaut 20 — modifiable
🟢 **FAIT VÉRIFIÉ** (Source : slope.md, image_06) : « Slope can be found near the bottom of the indicator list on SharpCharts. The default parameters (20) can be changed to suit the desired timeframe. »
**TRADEX-AI C1** : Paramètre par défaut = 20 jours, mais ajuster selon le timeframe requis (10/100/250) — NinjaTrader 8 peut calculer ce même indicateur sur les range bars.
*Catégorie : configuration*

### D3629 — Slope peut être positionné au-dessus, derrière ou en dessous du graphique prix
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « Like all indicators, Slope can be positioned above the price plot, behind the price plot or below the price plot. »
**TRADEX-AI C1** : Flexibilité d'affichage — recommandé en panneau séparé en dessous du prix pour lecture claire de la valeur et des croisements.
*Catégorie : configuration*

### D3630 — SMA ou autre indicateur peut être appliqué sur le Slope (advanced options)
🟢 **FAIT VÉRIFIÉ** (Source : slope.md) : « users can click the green arrow next to advanced options to apply a moving average or another indicator to Slope. »
⚫ **HYPOTHÈSE PROJET** : Appliquer une EMA(9) ou SMA(20) sur le Slope de GC/CL pour générer des croisements Slope/SMA comme signaux de renforcement de tendance.
**TRADEX-AI C1** : Technique d'amélioration : Slope + SMA(20) sur le Slope = détection précoce de changements de tendance — à tester en backtesting sur range bars NT8.
*Catégorie : indicateurs_tendance*
