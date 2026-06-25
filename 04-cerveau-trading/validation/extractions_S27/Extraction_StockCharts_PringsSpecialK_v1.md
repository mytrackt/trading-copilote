# Extraction StockCharts — Pring's Special K
**Source :** `bundles/stockcharts/prings_special_k.md` (HTTP 200 · ~8 100 car.) + 8 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 8/8 certifiées
**Décisions :** D3271 → D3290 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/prings-special-k
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.png | Short-, intermediate-, and long-term trends. | What Is Pring's Special K Indicator? |
| image_02.png | Primary trend and Special K. | What Is Pring's Special K Indicator? |
| image_03.png | Identifying Long-Term Price Movements With Special K | Identifying Long-Term Price Movements [SECTION-FALLBACK] |
| image_04.png | Identifying Long-Term Price Movements With Special K | Identifying Long-Term Price Movements [SECTION-FALLBACK] |
| image_05.png | Identifying Long-Term Price Movements With Special K | Identifying Long-Term Price Movements [SECTION-FALLBACK] |
| image_06.png | Identifying Pro-Trend Short-Term Buy and Sell Signals | Identifying Pro-Trend Short-Term Signals [SECTION-FALLBACK] |
| image_07.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] |
| image_08.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] |

## DÉCISIONS

### D3271 — Origine et double fonction du Special K
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_01) : « Created by Martin Pring, Special K is a momentum indicator that combines short-, intermediate-, and long-term velocity into one complete series, thereby giving us truly summed cyclicality. It has two functions. They are: 1. Identify primary trend reversals at a relatively early stage. 2. Use that information to time short-term pro-trend price moves. »
**TRADEX-AI C3** : Oscillateur Pring sommant la vélocité court/moyen/long terme. Double usage : (1) repérer tôt les retournements de tendance primaire, (2) timer des trades court terme dans le sens de la tendance.
*Catégorie : indicateurs_momentum*
---

### D3272 — Idéal : pics/creux synchrones avec le prix
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_02) : « In an ideal world, the Special K peaks and troughs more or less simultaneously with the price at bull and bear market turning points. In most situations, that happens. When it does, you need to identify these turning points as quickly as possible, after the fact. »
**TRADEX-AI C3** : Le Special K vise des pics/creux quasi simultanés aux retournements de marché. Enjeu opérationnel = identifier ces points de retournement le plus vite possible.
*Catégorie : structure_marche*
---

### D3273 — Hypothèse du cycle économique 4 ans
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « The formula assumes that prices are revolving around the four-year business cycle. As a result, when a linear uptrend, such as the 1990s secular bull market in equities develops, the Special K leads turning points. Alternatively, when the cycle is truncated, as was the case for the 1987 crash, the indicator is late. »
**TRADEX-AI C4** : La formule présuppose un cycle économique de 4 ans. Conséquence : en tendance linéaire le Special K anticipe ; en cycle tronqué (krach) il retarde. Limite structurelle à connaître.
*Catégorie : structure_marche*
---

### D3274 — Fonction primaire = retournements de tendance primaire
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « The prime function of the Special K then is to identify primary trend turning points. Since this indicator also includes short-term data in its calculation, a subsidiary benefit lies in the identification of smaller trends, for trading purposes, and putting that in context with the direction and maturity of the primary trend. »
**TRADEX-AI C3** : Fonction première = retournements de tendance primaire ; bénéfice secondaire = repérer les petites tendances et les situer dans la maturité de la tendance de fond.
*Catégorie : structure_marche*
---

### D3275 — Formule complète (12 ROC lissés et pondérés)
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « Special K = 10 SMA of ROC(10)*1 + 10 SMA of ROC(15)*2 + 10 SMA of ROC(20)*3 + 15 SMA of ROC(30)*4 + 50 SMA of ROC(40)*1 + 65 SMA of ROC(65)*2 + 75 SMA of ROC(75)*3 + 100 SMA of ROC(100)*4 + 130 SMA of ROC(195)*1 + 130 SMA of ROC(265)*2 + 130 SMA of ROC(390)*3 + 195 SMA of ROC(530)*4. The periods and weightings were selected based on years of market observations. »
**TRADEX-AI C3** : Formule déterministe (niveau 1, 0$) mais lourde : 12 rate-of-change (court→long) lissés par SMA puis pondérés 1/2/3/4 par groupe et sommés. Extension long-terme du KST.
*Catégorie : indicateurs_momentum*
---

### D3276 — Exigence de profondeur de données (≥725 points)
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « Note that at least 725 data points are required to accurately calculate this indicator. If less data is available, then the final line of the calculation is skipped. »
**TRADEX-AI C3** : Garde-fou technique — calcul exact exige ≥725 points ; sinon la dernière ligne (ROC 530) est omise. Contrainte d'historique à gérer avant d'afficher le Special K.
*Catégorie : configuration*
---

### D3277 — Technique 1 : trend lines sur indicateur jagged
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « Since the Special K is a jagged indicator, it lends itself best to trend line construction. For example, if a trend line of nine months or more is violated, that usually means the Special K's primary trend has reversed and when the indicator changes trend so usually does the price. »
**TRADEX-AI C1** : Le Special K étant accidenté, il se prête aux trend lines. Cassure d'une trend line de ≥9 mois = retournement probable de la tendance primaire (indicateur puis prix).
*Catégorie : signal*
---

### D3278 — Technique 2 : moyenne mobile (défaut 100/100)
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « It is normal to run a moving average through the Special K. The default is a 100-day smoothed by a 100-day SMA. Crossovers of the average typically signal a reversal in the direction of the primary trend. Occasionally, as with all moving average situations, whipsaws are triggered. When combined with a trend line break, though, a stronger and more reliable signal is triggered. »
**TRADEX-AI C3** : MA par défaut = 100 jours lissée par SMA 100. Croisement = retournement de tendance primaire. Garde-fou whipsaws → confirmer par cassure de trend line (signal combiné plus fiable).
*Catégorie : signal*
---

### D3279 — Exemples MA+trendline simultanés (2003, 2009)
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « Examples at the 2003 and 2009 bottoms for US equities are shown in the first chart above, where MA crosses and trendline violations develop more or less simultaneously. »
**TRADEX-AI C4** : Cas historiques — creux 2003 et 2009 où croisement de MA et cassure de trend line ont coïncidé. Confluence des deux = signal de retournement renforcé.
*Catégorie : structure_marche*
---

### D3280 — Technique 3 : figures de prix sur le Special K
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_03) : « Occasionally, the Special K traces out price patterns. When they are confirmed by some kind of trend reversal in the price itself, this usually represents a valid indication of a reversal in the prevailing primary trend. The GLD chart below offers two examples. »
**TRADEX-AI C1** : Le Special K peut dessiner des figures chartistes ; valides seulement si confirmées par un retournement du prix lui-même. Exemples sur GLD (Or — actif TRADING GC).
*Catégorie : configuration*
---

### D3281 — Profondeur de recul pour apprécier le long terme
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « It's important to note that calculating the initial plot of the Special K involves several years of data. To really appreciate the long-term perspective offered by this indicator, around 5–10 years of additional data are required. That way, it's possible to see if the security in question is experiencing the expected cyclical swings. »
**TRADEX-AI C3** : Au-delà des 725 points, 5–10 ans d'historique supplémentaires sont nécessaires pour juger si l'actif suit bien les oscillations cycliques attendues. Outil de fond, pas intraday.
*Catégorie : configuration*
---

### D3282 — Principe pro-tendance pour le court terme
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « It's important for short-term traders to understand that trades executed in the direction of the main trend are more likely to be successful than those generated in a counter-cyclical way. An objective method of determining the direction of the primary trend is to use the Special K. »
**TRADEX-AI C3** : Principe — trader dans le sens de la tendance primaire augmente la probabilité de succès. Le Special K sert de filtre directionnel objectif pour les trades court terme.
*Catégorie : structure_marche*
---

### D3283 — Détermination du régime via la MA 10 jours
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md) : « One solution is to determine its position relative to its 10-day MA. Positive readings (i.e., above the MA) would indicate a primary bull market and vice versa. »
**TRADEX-AI C3** : Proxy temps réel du régime — Special K au-dessus de sa MA 10 jours = bull primaire, en-dessous = bear primaire. Filtre de direction codable.
*Catégorie : signal*
---

### D3284 — Système d'entrées pro-tendance
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_06) : « When the direction of the primary trend has been determined to be bullish, trades from the long side would be initiated when the Special K itself crosses above its 10-day MA. These are shown with orange, upward arrows on the chart below. The green vertical line represents the start of a bull market phase as defined by the Special K/10-day MA relationship. »
**TRADEX-AI C3** : Règle d'entrée — en régime bull (déterminé par la MA longue), entrer long quand le Special K croise au-dessus de sa MA 10 jours. Double filtre régime + déclencheur.
*Catégorie : signal*
---

### D3285 — Achats seulement en bull, ventes seulement en bear
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_06) : « No buy signals are generated during the bearish periods, only sell signals (brown, downward arrows). The "Example Sell Point" was subpar because it developed during a bull market, but, unfortunately, the system was still in a bearish mode because the Special K was below its 10-day MA. This illustrates how this approach is far from perfect. »
**TRADEX-AI C3** : Asymétrie — en régime bear, uniquement signaux de vente ; en bull, uniquement achats. Avertissement Pring : le système est imparfait (signal de vente subpar en plein bull).
*Catégorie : signal*
---

### D3286 — "Weight of the evidence" : alerte, pas mécanique aveugle
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_06) : « As with all technical indicators, rather than blindly using this approach as a mechanical system, it's better to use pro trend signals as an alert and then use other indicators as a filter in a "weight of the evidence" approach. - Martin Pring »
**TRADEX-AI C3** : Garde-fou Pring — ne pas exécuter mécaniquement ; traiter les signaux pro-tendance comme une alerte, filtrée par d'autres indicateurs (faisceau de preuves). Cohérent règle 3/4+2/3 TRADEX.
*Catégorie : signal*
---

### D3287 — Deux lignes : Special K brut + signal double-lissé
🔵 **ÉCOLE (Pring)** (Source : prings_special_k.md, image_07) : « The first line in the indicator is the raw Special K value. The second line is a double-smoothed moving average of the raw Special K value, which acts as a signal line. »
**TRADEX-AI C3** : L'affichage SharpCharts comporte le Special K brut + une ligne de signal (MA double-lissée). Le croisement des deux lignes = déclencheur secondaire.
*Catégorie : configuration*
---

### D3288 — Paramètres de la ligne de signal (défaut 100,100)
🟡 **CONVENTION** (Source : prings_special_k.md, image_08) : « Users can adjust the signal line settings by changing the numbers in the Parameters box. The two parameters specify the number of periods in the two simple moving averages used for smoothing. The default parameter values are 100,100. Users can also apply "Advanced Options" to add a horizontal line. »
**TRADEX-AI C3** : Convention par défaut de la ligne de signal = (100,100) → deux SMA de lissage. Paramétrable. Confirme l'orientation long terme de l'outil.
*Catégorie : configuration*
---

### D3289 — Scan bullish short-term cross
🟡 **CONVENTION** (Source : prings_special_k.md) : Scan bullish — « [Special K > Special K Signal(100,100)] AND [Special K x SMA(10,Special K)] » avec filtres `[type = stock] AND [country = US] AND [Daily SMA(20,Daily Volume) > 40000] AND [Daily SMA(60,Daily Close) > 20]`.
**TRADEX-AI C7** : Bonne pratique screening — exiger régime bull (Special K > signal 100,100) ET croisement haussier de la MA 10 jours, avec filtres liquidité/prix. Double condition régime + déclencheur.
*Catégorie : signal*
---

### D3290 — Scan bearish short-term cross
🟡 **CONVENTION** (Source : prings_special_k.md) : Scan bearish — « [Special K < Special K Signal(100,100)] AND [SMA(10,Special K) x Special K] » mêmes filtres de liquidité/prix.
**TRADEX-AI C7** : Symétrique baissier — régime bear (Special K < signal) ET croisement baissier de la MA 10 jours. Confirme l'asymétrie achats-en-bull / ventes-en-bear (D3285).
*Catégorie : signal*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3271 → D3290 (20 décisions) |
| Images certifiées | 8/8 |
| Cercle dominant | C3 (momentum) · renvois C1/trend lines (D3277, D3280) · C4/macro cycle (D3273, D3279) · C7/screening (D3289, D3290) |
| Tags | 🔵 ÉCOLE Pring ×17 · 🟡 CONVENTION ×3 (D3288, D3289, D3290) |
| Catégories | indicateurs_momentum, structure_marche, signal, configuration |
| Actifs concernés | GC · HG · CL · ZW (exemple GLD = Or) — usage long terme, exige historique profond |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Paramètres clés | 12 ROC pondérés ; ≥725 points requis ; régime via MA 10j ; signal (100,100) ; achats en bull / ventes en bear |
| À vérifier | Aucun cas — 8/8 images certifiées, texte complet (figcaptions vides côté .md mais légendes HTML résolues par section-fallback) |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
