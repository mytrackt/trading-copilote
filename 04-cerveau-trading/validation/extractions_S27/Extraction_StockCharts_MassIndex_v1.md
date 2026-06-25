# Extraction StockCharts — Mass Index

**Source :** `bundles/stockcharts/mass_index.md` (HTTP 200 · ~7 400 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 · 7/7 certifiées
**Décisions :** D2551 → D2563 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/mass-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Mass Index? | What Is the Mass Index? [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_02.png | Spreadsheet 1 | Mass Index Calculation | CERTIFIÉ (.md + HTML) |
| image_03.png | Reversal bulge signals in an uptrend | Trend Reversal Signals | CERTIFIÉ (.md + HTML) |
| image_04.png | Reversal bulge signals in a downtrend | Adjusting the Signal Threshold | CERTIFIÉ (.md + HTML) |
| image_05.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_06.png | SharpCharts Settings for the Mass Index | Using with SharpCharts | CERTIFIÉ (.md + HTML) |
| image_07.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |

## DÉCISIONS

### D2551 — Origine et nature du Mass Index
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_01) : « Developed by Donald Dorsey, the Mass Index uses the high-low range to identify trend reversals based on range expansions. (…) the Mass Index is a volatility indicator that does not have a directional bias. Instead, the Mass Index identifies range bulges that can foreshadow a reversal of the current trend. »
**TRADEX-AI C1** : indicateur de volatilité (amplitude haut-bas) SANS biais directionnel ; détecte un renflement de range annonçant un possible retournement, à confirmer par ailleurs.
*Catégorie : indicateurs_tendance*

---

### D2552 — Calcul en quatre étapes (EMA 9 du H-L, double EMA, ratio, somme 25)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « Single EMA = 9-period EMA of the high-low differential ; Double EMA = 9-period EMA of the 9-period EMA of the high-low differential ; EMA Ratio = Single EMA divided by Double EMA ; Mass Index = 25-period sum of the EMA Ratio. »
**TRADEX-AI C1** : formule déterministe entièrement reproductible (H-L → EMA9 → EMA9 de l'EMA9 → ratio → somme glissante 25). Codable en l'état si l'indicateur est retenu.
*Catégorie : indicateurs_tendance*

---

### D2553 — Logique du calcul : normalisation et lissage du range
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_02) : le ratio des deux EMA « normalizes the data series (…) shows when the Single EMA becomes large relative to the Double EMA. The final step, a 25-period summation, acts like a moving average to further smooth (…). Overall, the Mass Index rises as the high-low range widens and falls as the high-low range narrows. »
**TRADEX-AI C1** : le Mass Index MONTE quand l'amplitude H-L s'élargit, BAISSE quand elle se resserre — c'est un thermomètre d'expansion de volatilité lissé. Image_02 = exemple tableur de référence.
*Catégorie : indicateurs_tendance*

---

### D2554 — Signal du « reversal bulge » de Dorsey (>27 puis <26,50)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « a bulge occurs when the Mass Index moves above 27. This initial bulge does not complete the signal (…). Dorsey waited for this bulge to reverse with a move back below 26.50. Once the reversal bulge is complete, traders should use other analysis techniques to determine the direction of the next move. »
**TRADEX-AI C1** : signal en DEUX temps — (1) franchissement >27, (2) repli <26,50 = renflement complété. Le signal ne donne PAS la direction ; un autre outil doit la déterminer.
*Catégorie : signal*

---

### D2555 — Direction du retournement dépend de la tendance préexistante
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_03) : « Ideally, a downtrend followed by a reversal bulge would suggest a bullish trend reversal. Conversely, an uptrend followed by a reversal bulge would suggest a bearish trend reversal. »
**TRADEX-AI C1** : le biais directionnel est CONTEXTUEL — renflement en tendance baissière → retournement haussier attendu ; en tendance haussière → retournement baissier. Image_03 illustre des renflements en uptrend (signal baissier attendu).
*Catégorie : signal*

---

### D2556 — Le seuil 27 est rarement atteint
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « Chartists looking for signals will most likely have to relax Dorsey's requirements (…) because the Mass Index rarely exceeds 27. It takes exceptional volatility to push the index above this level. »
**TRADEX-AI C1** : le seuil canonique de 27 produit très peu de signaux ; en l'état il faut une volatilité exceptionnelle — limite opérationnelle à connaître avant tout usage.
*Catégorie : signal*

---

### D2557 — Abaisser le seuil et comparer aux extrêmes historiques
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_04) : « Chartists can lower the threshold (…). One size does not fit all when it comes to volatility (…) chartists may need to compare Mass Index levels over time to identify historical highs and lows. A move that nears the high end of the historical range would suggest a volatility bulge that could foreshadow a reversal. » Exemple International Paper : seuil 26 jugé plus adapté que 27.
**TRADEX-AI C1** : le seuil doit être CALIBRÉ par instrument selon sa plage historique de Mass Index (volatilité propre) ; un seuil unique 27 n'est pas universel. Image_04 = renflements en downtrend.
*Catégorie : signal*

---

### D2558 — Outlier de volatilité août 2011 (prudence sur lectures extrêmes)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « August 2011 was an extremely volatile period for the entire stock market and this reading looks like an outlier. »
**TRADEX-AI C1** : un pic de Mass Index pendant un choc de marché généralisé peut être un outlier non exploitable — garde-fou contre la sur-interprétation d'un renflement en période de stress systémique.
*Catégorie : signal*

---

### D2559 — Direction confirmée par un oscillateur (TRIX / MACD / PPO)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « Once the reversal bulge is in place and the trading bias established, chartists can use the TRIX (or similar indicators, such as the MACD or PPO) to generate a directional signal. (…) The green arrows show when the TRIX moved above its signal line to signal an upturn in prices. »
**TRADEX-AI C1** : workflow recommandé = Mass Index pour DÉTECTER le retournement potentiel + oscillateur (TRIX/MACD/PPO) pour TIMER la direction. Combinaison à deux indicateurs.
*Catégorie : signal*

---

### D2560 — Synthèse interprétative (« The Bottom Line »)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : « The indicator typically fluctuates in the mid-20s ; readings near the high end of the historical range suggest increasing volatility, which increases the chances for a trend reversal (…). The directional bias depends on the existing trend. As with all indicators, chartists should use other analysis techniques to complement the Mass Index. »
**TRADEX-AI C1** : l'indicateur oscille typiquement dans les ~20 ; proximité du haut de plage = hausse de volatilité = probabilité accrue de retournement, direction toujours dépendante de la tendance. Outil de complément, jamais autonome.
*Catégorie : indicateurs_tendance*

---

### D2561 — Paramétrage SharpCharts (somme 25 par défaut, lignes 26,5 et 27)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_05, image_06) : « a Mass Index indicator is added (…) with the default setting of 25 summation periods. Users can adjust the summation periods (…). a blue line was added at 26.5 and a red line at 27, to set the thresholds for the reversal bulge signal. »
**TRADEX-AI C1** : paramètre par défaut = 25 périodes de sommation ; lignes horizontales de référence 26,5 (repli) et 27 (renflement). Réglage standard reproductible. image_06 = panneau de réglages.
*Catégorie : timing*

---

### D2562 — Disponibilité StockChartsACP (même défaut 25 périodes)
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md, image_07) : « This indicator can be added from the Chart Settings panel for your StockChartsACP chart (…). By default, the indicator uses 25 summation periods. This parameter can be adjusted to meet your technical analysis needs. »
**TRADEX-AI C1** : disponible aussi sur la plateforme ACP avec le même défaut (25) ; détail outillage, sans incidence sur la formule.
*Catégorie : indicateurs_tendance*

---

### D2563 — Scans bull/bear : Mass Index <26,5 filtré par tendance SMA 200
🟢 **FAIT VÉRIFIÉ** (Source : mass_index.md) : scan « Bullish Reversal » = `[Daily Close < Daily SMA(200,Daily Close)] AND [26.5 x Daily MASS(25)]` (downtrend long terme + Mass passant sous 26,5) ; scan « Bearish Reversal » = même critère avec `[Daily Close > Daily SMA(200,Daily Close)]` (uptrend long terme).
**TRADEX-AI C1** : règle opérationnelle codifiée — le repli sous 26,5 (`x` = croisement descendant) combiné à la position vs SMA(200) donne le sens : sous SMA200 → reversal haussier ; au-dessus → reversal baissier. Transposable comme filtre, à valider sur futures.
*Catégorie : signal*

---

## SYNTHÈSE

| # | Décision | Cercle | Catégorie | Tag |
|---|----------|--------|-----------|-----|
| D2551 | Nature : volatilité sans biais directionnel (Dorsey) | C1 | indicateurs_tendance | 🟢 |
| D2552 | Calcul 4 étapes (EMA9 H-L → double EMA → ratio → somme 25) | C1 | indicateurs_tendance | 🟢 |
| D2553 | Logique : monte si range s'élargit | C1 | indicateurs_tendance | 🟢 |
| D2554 | Reversal bulge : >27 puis <26,50 | C1 | signal | 🟢 |
| D2555 | Direction = fonction de la tendance préexistante | C1 | signal | 🟢 |
| D2556 | Seuil 27 rarement atteint | C1 | signal | 🟢 |
| D2557 | Abaisser/calibrer seuil sur plage historique | C1 | signal | 🟢 |
| D2558 | Outlier août 2011 (prudence stress) | C1 | signal | 🟢 |
| D2559 | Direction confirmée par TRIX/MACD/PPO | C1 | signal | 🟢 |
| D2560 | Synthèse : oscille mid-20, complément seulement | C1 | indicateurs_tendance | 🟢 |
| D2561 | SharpCharts : somme 25, lignes 26,5/27 | C1 | timing | 🟢 |
| D2562 | StockChartsACP : défaut 25 | C1 | indicateurs_tendance | 🟢 |
| D2563 | Scans bull/bear : <26,5 filtré SMA200 | C1 | signal | 🟢 |

**Note de portée :** indicateur de volatilité/retournement (C1) applicable à tout instrument, donc potentiellement aux futures GC/HG/CL/ZW (détection d'expansion de range avant retournement). Lien Belkhayate : aucun direct (la méthode n'utilise pas le Mass Index → ⚫🔴 non concerné). Seuils 26,5/27 à recalibrer obligatoirement par actif (D2557). 13 décisions, 7/7 images certifiées.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
