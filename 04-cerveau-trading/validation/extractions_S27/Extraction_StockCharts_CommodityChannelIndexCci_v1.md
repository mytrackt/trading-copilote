# Extraction StockCharts — Commodity Channel Index (CCI)
**Source :** `bundles/stockcharts/commodity_channel_index_cci.md` (HTTP 200 · ~10 500 car.) + 9 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 9/9 certifiées
**Décisions :** D1331 → D1350 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/commodity-channel-index-cci
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.png | What Is the Commodity Channel Index? | What Is the Commodity Channel Index? [SECTION-FALLBACK] |
| image_02.png | CCI calculation example | Calculating CCI |
| image_03.png | Chart showing CCI values calculated in the spreadsheet example | Calculating CCI |
| image_04.png | Extreme CCI values can signal a change in trend | Identifying New Trends Emerging |
| image_05.png | CCI moves outside of more extreme levels (+/-200) when a stock is overbought or oversold | Overbought/Oversold Conditions |
| image_06.png | Divergences with CCI, confirmed by a zero-line crossover, can indicate a trend reversal | Identifying Bullish/Bearish Divergences |
| image_07.png | Using CCI on a SharpChart | Using with SharpCharts |
| image_08.png | CCI settings on the SharpCharts Workbench | Using with SharpCharts |
| image_09.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] |

## DÉCISIONS

### D1331 — Origine et nature du CCI
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_01) : « Developed by Donald Lambert and featured in *Commodities* magazine in 1980, the Commodity Channel Index (CCI) is a versatile indicator that can identify a new trend or warn of extreme conditions. »
**TRADEX-AI C3** : Indicateur de momentum historiquement conçu pour les commodities (matières premières) — directement pertinent pour GC/HG/CL/ZW. À traiter comme oscillateur de momentum/régime, pas comme déclencheur isolé.
*Catégorie : indicateurs_momentum*
---

### D1332 — Ce que mesure le CCI
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « CCI measures the current price level relative to an average price level over a given period. CCI is relatively high when prices are far above their average, but is relatively low when prices are far below their average. In this manner, CCI can be used to identify overbought and oversold levels. »
**TRADEX-AI C3** : Mesure l'écart prix vs moyenne sur N périodes → utilisable pour détecter conditions de surachat/survente sur l'actif tradé.
*Catégorie : indicateurs_momentum*
---

### D1333 — Applicabilité multi-actifs
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « While Lambert originally developed CCI to identify cyclical turns in commodities, the indicator can be successfully applied to indices, ETFs, stocks, and other securities. »
**TRADEX-AI C3** : CCI applicable indistinctement aux 4 actifs trading (GC/HG/CL/ZW) et aux confirmations (ES/VX). Pas de restriction d'instrument.
*Catégorie : indicateurs_momentum*
---

### D1334 — Formule de calcul du CCI
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_02) : « CCI = (Typical Price - 20-period SMA of TP) / (.015 x Mean Deviation) ; Typical Price (TP) = (High + Low + Close)/3 ; Constant = .015 ». L'exemple est basé sur un calcul CCI à 20 périodes.
**TRADEX-AI C3** : Formule déterministe codable côté Python (niveau 1, coût 0$). TP = (H+L+C)/3, SMA 20 du TP, déviation moyenne, constante 0,015. Période par défaut = 20.
*Catégorie : indicateurs_momentum*
---

### D1335 — Calcul de la Mean Deviation
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_03) : « There are four steps to calculating the Mean Deviation: 1. Subtract the most recent 20-period average of the typical price from each period's typical price. 2. Take the absolute values of these numbers. 3. Sum the absolute values. 4. Divide by the total number of periods (20). »
**TRADEX-AI C3** : Procédure exacte de la déviation moyenne (moyenne des écarts absolus, PAS l'écart-type standard). Indispensable pour implémentation fidèle.
*Catégorie : indicateurs_momentum*
---

### D1336 — Rôle de la constante 0,015
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « Lambert set the constant at .015 to ensure that approximately 70 to 80 percent of CCI values would fall between -100 and +100. This percentage also depends on the look-back period. »
**TRADEX-AI C3** : La constante 0,015 calibre la bande ±100 pour contenir ~70-80% des valeurs → justifie les seuils ±100 comme « normaux ».
*Catégorie : configuration*
---

### D1337 — Effet de la période sur la volatilité du CCI
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « A shorter CCI (10 periods) will be more volatile with a smaller percentage of values between +100 and -100. Conversely, a longer CCI (40 periods) will have a higher percentage of values between +100 and -100. »
**TRADEX-AI C3** : Période courte (10) = plus de signaux extrêmes/bruit ; période longue (40) = plus lisse. Paramètre à régler selon mode (Standard 15min vs Rapide range bar).
*Catégorie : configuration*
---

### D1338 — Lecture positive/négative
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « High positive readings indicate that prices are well above their average—a show of strength. Low negative readings indicate that prices are well below their average—a show of weakness. »
**TRADEX-AI C3** : CCI positif = force ; CCI négatif = faiblesse. Lecture directionnelle de base pour le scoring momentum.
*Catégorie : indicateurs_momentum*
---

### D1339 — CCI comme indicateur coïncident
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « As a coincident indicator. When CCI surges above +100, it reflects strong price action that can signal the start of an uptrend. When CCI plunges below -100, it reflects weak price action that can signal the start of a downtrend. »
**TRADEX-AI C3** : Franchissement +100 → départ possible de tendance haussière ; franchissement -100 → départ possible de tendance baissière. Signal de tendance émergente.
*Catégorie : signal*
---

### D1340 — CCI comme indicateur avancé (mean reversion + divergences)
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « As a leading indicator. Use the CCI to identify overbought or oversold conditions that may foreshadow a mean reversion. Bullish and bearish divergences can be used to detect early momentum shifts and anticipate trend reversals. »
**TRADEX-AI C3** : Double usage — détection surachat/survente (retour à la moyenne) et divergences pour anticiper retournement. Deux modes de lecture distincts à ne pas confondre.
*Catégorie : signal*
---

### D1341 — Seuils ±100 comme filtres anti-whipsaw
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_04) : « using simple zero-line crossovers can result in many whipsaws. Although entry points will lag more, requiring a move above +100 for a bullish signal and a move below -100 for a bearish signal reduces whipsaws. »
**TRADEX-AI C3** : Préférer le franchissement ±100 (et non 0) comme déclencheur → moins de faux signaux, au prix d'un léger retard. Garde-fou anti-whipsaw côté niveau 1.
*Catégorie : signal*
---

### D1342 — CCI ne capture pas l'extrême exact
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_04) : « CCI doesn't catch the exact top or bottom, but it can help filter out insignificant moves and focus on the larger trend. » (Exemple CAT, CCI 20 jours : top 11 jan, CCI < -100 le 22 jan ; bottom 8 fév, CCI > +100 le 17 fév.)
**TRADEX-AI C3** : Délai typique observé de 6-8 jours entre extrême prix et signal CCI. CCI = filtre de tendance, pas timing exact d'entrée. Ne pas l'utiliser seul pour le point d'entrée précis.
*Catégorie : timing*
---

### D1343 — Combiner signal de tendance et setup reward/risk
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « With the bullish signal in force, the focus would have been on bullish setups with a good reward-to-risk ratio. » (Exemple CAT : retracement ~62% puis falling flag, surge au-dessus de la trendline = nouveau signal CCI toujours en mode bull.)
**TRADEX-AI C3** : Une fois CCI en mode haussier, chercher des setups d'entrée avec R/R favorable (cohérent avec la règle TRADEX R/R ≥ 1:2). CCI = filtre de biais directionnel, pas le déclencheur d'entrée final.
*Catégorie : gestion_risque_entree*
---

### D1344 — CCI est un oscillateur non borné
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « CCI is an unbound oscillator. Theoretically, there are no upside or downside limits. This makes an overbought or oversold assessment subjective. Second, securities can continue moving higher after an indicator becomes overbought. »
**TRADEX-AI C3** : Pas de plafond/plancher fixe → un actif peut rester « suracheté » longtemps. Ne jamais traiter un CCI extrême comme signal de retournement automatique.
*Catégorie : indicateurs_momentum*
---

### D1345 — Seuils ±200 pour vrais extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_05) : « ±100 may work in a trading range, but more extreme levels are needed for other situations. ±200 is a much harder level to reach and more representative of a true extreme. Selection of overbought/oversold levels also depends on the volatility of the underlying security. »
**TRADEX-AI C3** : Adapter les seuils à la volatilité de l'actif. ±100 en range, ±200 pour extrêmes véritables. GC/CL (plus volatils) peuvent justifier ±200 ; un ETF indiciel a une amplitude CCI plus réduite.
*Catégorie : configuration*
---

### D1346 — Attendre le re-franchissement des seuils extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_05) : « It is important to wait for these crosses to reduce whipsaws should the trend extend... Notice how Google kept on moving higher even after CCI became overbought in mid-September and moved below 200. » (GOOG CCI 20, lignes ±200, >5 dépassements fév-oct 2010.)
**TRADEX-AI C3** : Pour un signal de retour à la moyenne, attendre que le CCI repasse SOUS +200 (vente) ou AU-DESSUS de -200 (achat), pas le simple dépassement. Système non infaillible.
*Catégorie : timing*
---

### D1347 — Définition des divergences haussières/baissières
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « A bullish divergence occurs when the underlying security makes a lower low and CCI forms a higher low, which shows less downside momentum. A bearish divergence forms when the security records a higher high and CCI forms a lower high, which shows less upside momentum. »
**TRADEX-AI C3** : Divergence haussière = prix LL + CCI HL ; divergence baissière = prix HH + CCI LH. Définitions codables pour détection automatique de divergence.
*Catégorie : divergence*
---

### D1348 — Divergences trompeuses en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « divergences can be misleading in a strong trend. A strong uptrend can show numerous bearish divergences before a top actually materializes. Conversely, bullish divergences often appear in extended downtrends. »
**TRADEX-AI C3** : Garde-fou — en tendance forte, ignorer/pondérer faiblement les divergences CCI isolées (nombreux faux signaux avant le vrai retournement).
*Catégorie : divergence*
---

### D1349 — Confirmation obligatoire des divergences
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md, image_06) : « A bearish divergence can be confirmed with a break below zero in CCI or a support break on the price chart. Conversely, a bullish divergence can be confirmed with a break above zero in CCI or a resistance break on the price chart... Not all divergences produce good signals. »
**TRADEX-AI C3** : Ne valider une divergence qu'après confirmation (croisement du zéro CCI OU cassure support/résistance prix). Exige une double validation avant scoring positif.
*Catégorie : divergence*
---

### D1350 — Combiner le CCI avec un indicateur de volume (pas un autre momentum)
🟢 **FAIT VÉRIFIÉ** (Source : commodity_channel_index_cci.md) : « chartists should use CCI in conjunction with other indicators or price analysis. Another momentum oscillator would be redundant, but On Balance Volume (OBV) or the Accumulation Distribution Line can add value to CCI signals. »
**TRADEX-AI C7** : Ne pas empiler un autre oscillateur de momentum (redondant). Compléter le CCI par un indicateur de volume (OBV / Accumulation-Distribution) → cohérent avec l'order flow ATAS du cercle C2.
*Catégorie : configuration*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1331 → D1350 (20 décisions) |
| Images certifiées | 9/9 |
| Cercle dominant | C3 (momentum) · 1 renvoi C7/C2 (D1350) |
| Tags | 🟢 littéral ×20 |
| Catégories | indicateurs_momentum, configuration, signal, timing, divergence, gestion_risque_entree |
| Actifs concernés | GC · HG · CL · ZW (commodities — conçu pour) + ES/VX en confirmation |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Paramètres clés | Période 20 (défaut), TP=(H+L+C)/3, constante 0,015, seuils ±100 (range) / ±200 (extrêmes) |
| À vérifier | Aucun cas — 9/9 images certifiées, texte complet |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
