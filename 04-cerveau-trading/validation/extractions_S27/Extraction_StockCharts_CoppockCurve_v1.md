# Extraction StockCharts — Coppock Curve
**Source :** `bundles/stockcharts/coppock_curve.md` (HTTP 200 · ~6 600 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D1371 → D1390 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/coppock-curve
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.png | Chart 1 | SharpCharts Calculation |
| image_02.png | Spreadsheet 1 | SharpCharts Calculation |
| image_03.png | Chart 2 | Signals |
| image_04.png | Chart 3 | Flexibility |
| image_05.png | Chart 4 | Flexibility |
| image_06.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] |
| image_07.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] |

## DÉCISIONS

### D1371 — Origine et objectif de la Coppock Curve
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « The Coppock Curve is a momentum indicator developed by Edwin "Sedge" Coppock, who was an economist by training. Coppock introduced the indicator in *Barron's* in October 1965. The goal of this indicator is to identify long-term buying opportunities in the S&P 500 and Dow Industrials. »
**TRADEX-AI C3** : Indicateur de momentum long terme, conçu pour repérer des opportunités d'ACHAT sur indices (S&P 500, Dow). Orienté investissement long terme à l'origine.
*Catégorie : indicateurs_momentum*
---

### D1372 — Signal d'origine : passage en territoire positif
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « Coppock used monthly data to identify buying opportunities when the indicator moved from negative territory to positive territory. Although Coppock did not use it for sell signals, many technical analysts consider a cross from positive to negative territory as a sell signal. »
**TRADEX-AI C3** : Signal achat = franchissement haussier du zéro (négatif→positif) sur données mensuelles. Le signal vente (positif→négatif) est un ajout des analystes, pas de Coppock lui-même.
*Catégorie : signal*
---

### D1373 — Formule de la Coppock Curve
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_01) : « Coppock Curve = 10-period WMA of (14-period RoC + 11-period RoC) ; WMA = Weighted Moving Average ; RoC = Rate-of-Change. »
**TRADEX-AI C3** : Formule déterministe codable (niveau 1, 0$) : WMA 10 périodes de la somme (RoC 14 + RoC 11). Réutilise le Rate-of-Change déjà documenté.
*Catégorie : indicateurs_momentum*
---

### D1374 — Origine des périodes 11 et 14
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « Coppock used 11 and 14 periods because, according to an Episcopal priest, this was the average mourning period when grieving the loss of a loved one. Coppock theorized that the recovery period for stock market losses would be similar to this timeframe. »
**TRADEX-AI C3** : Justification des périodes 11/14 anecdotique/heuristique (deuil moyen), non statistique. À traiter comme convention historique, pas comme optimum prouvé.
*Catégorie : indicateurs_momentum*
---

### D1375 — Pondération du WMA (poids sur données récentes)
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_02) : « a weighted moving average puts more weight on recent data and less weight on older data. For example, a three-period WMA would multiply the first data point by one, the second by two, and the third by three. The sum of these three numbers is then divided by six. »
**TRADEX-AI C3** : Le WMA pondère linéairement (1,2,3…) puis divise par la somme des poids. Logique exacte du lissage final de la Coppock Curve.
*Catégorie : indicateurs_momentum*
---

### D1376 — Rareté des signaux mensuels
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_03) : « Using monthly data, this indicator will not trigger very many signals... Unsurprisingly, there have been only five signals since the late 1980s... The first signal triggered in 1988, which was after the 1987 crash. »
**TRADEX-AI C3** : En mensuel, ~5 signaux seulement depuis fin années 1980 → outil de régime de fond, pas de timing fréquent. Inadapté au trading intraday tel quel.
*Catégorie : timing*
---

### D1377 — Performance des signaux de vente (évitement de bear markets)
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « Chartists following the two sell signals would have avoided the last two bear markets. The February 2001 sell signal would have avoided most of the bear market from 2000 to 2002. The June 2008 sell signal would have gotten investors out before the market plunge in the second half of 2008. »
**TRADEX-AI C4** : Exemples historiques — les croisements baissiers ont précédé les bear markets 2000-2002 et 2008. Utile comme filtre macro de régime (sortie cash), pas comme déclencheur d'ordre intraday.
*Catégorie : structure_marche*
---

### D1378 — Nature : oscillateur de momentum lissé
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « the Coppock Curve is simply a smoothed momentum oscillator. The Rate-of-Change indicator measures momentum and the weighted moving average smooths the data. »
**TRADEX-AI C3** : Conceptuellement = RoC (momentum) + WMA (lissage). Pas de magie : un oscillateur de momentum amorti.
*Catégorie : indicateurs_momentum*
---

### D1379 — Applicable à tous les timeframes
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_04) : « This means the indicator can be used on any timeframe. Intraday, daily and weekly data can be used to fit one's trading/investing style and time horizon. The chart below shows the Coppock Curve using weekly data on the Dow Industrials. As expected, the weekly chart produced many more signals than the monthly chart. »
**TRADEX-AI C3** : Malgré son origine mensuelle, la Coppock Curve est applicable intraday/daily/weekly. Timeframe plus court = plus de signaux. Possible en mode Standard 15min TRADEX.
*Catégorie : configuration*
---

### D1380 — Réglage de la sensibilité via le RoC
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_05) : « A shorter Rate-of-Change setting will make the Coppock Curve more sensitive and faster, while a longer setting will make it less sensitive and slower. The chart below shows daily bars for the Nasdaq 100 ETF (QQQ) and the Coppock Curve (20,10,10). »
**TRADEX-AI C3** : RoC court = plus réactif/bruyant ; RoC long = plus lent/lissé. Réglage (20,10,10) cité pour graphiques daily moins sensibles.
*Catégorie : configuration*
---

### D1381 — Signaux principaux = croisements du zéro
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « The main signals are generated with crosses above and below the zero line. »
**TRADEX-AI C3** : Déclencheurs cœur = franchissement de la ligne zéro (au-dessus = achat, en-dessous = vente). Logique binaire codable.
*Catégorie : signal*
---

### D1382 — Divergences pour anticiper les croisements
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « More aggressive chartists can consider looking for bullish and bearish divergences to anticipate such crossovers. »
**TRADEX-AI C3** : Option avancée — divergences pour anticiper le croisement du zéro avant qu'il ne survienne. Approche plus agressive (plus tôt, moins fiable).
*Catégorie : divergence*
---

### D1383 — Garde-fou divergences (pas toujours un retournement)
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « Use caution, however. Divergences do not always result in trend reversals because the trend can simply slow and continue in the same direction. »
**TRADEX-AI C3** : Garde-fou — une divergence peut signaler un simple ralentissement, pas un retournement. Ne pas la traiter comme signal de retournement automatique.
*Catégorie : divergence*
---

### D1384 — Placement et ajout d'une ligne de signal
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_06) : « The indicator can then be positioned "behind price," "above" the main window or "below" the main window... Chartists can also add a moving average using the "advanced" options. This moving average acts like a signal line, similar to MACD. »
**TRADEX-AI C3** : Possibilité d'ajouter une moyenne mobile sur la courbe comme ligne de signal (analogie MACD) → croisement courbe/signal comme déclencheur complémentaire.
*Catégorie : configuration*
---

### D1385 — Paramétrage via la boîte Parameters
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md, image_07) : « The Coppock Curve can be found in the Indicators section below the chart. Users can adjust the settings by changing the numbers in the Parameters box. »
**TRADEX-AI C3** : Indicateur configurable (Parameters box SharpCharts). Confirme que les trois paramètres (RoC long, RoC court, WMA) sont ajustables.
*Catégorie : configuration*
---

### D1386 — Scan croisement haussier du zéro avec confirmation volume
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : Scan « Coppock Curve Crosses above Zero » : `[Daily Coppock(20,10,10) crosses 0] AND [Daily Volume > Daily SMA(50,Daily Volume)]` — « the bullish crossover occurred with expanding volume. »
**TRADEX-AI C7** : Bonne pratique — coupler le croisement haussier à un volume au-dessus de sa SMA 50 (volume en expansion confirme). Cohérent avec l'order flow C2.
*Catégorie : signal*
---

### D1387 — Scan croisement baissier du zéro avec confirmation volume
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : Scan « Coppock Curve Crosses below Zero » : `[0 crosses Daily Coppock(20,10,10)] AND [Daily Volume > Daily SMA(50,Daily Volume)]` — « the bearish crossover occurred with expanding volume. »
**TRADEX-AI C7** : Symétrique baissier — croisement sous zéro confirmé par volume en expansion. Le volume comme filtre de qualité du signal Coppock.
*Catégorie : signal*
---

### D1388 — Paramètre de scan par défaut Coppock(20,10,10)
🟡 **CONVENTION** (Source : coppock_curve.md) : Les deux scans suggérés utilisent `Coppock(20,10,10)` (RoC long 20, RoC court 10, WMA 10).
**TRADEX-AI C3** : Convention StockCharts pour scans daily = (20,10,10), distincte de l'original (14,11,10). Paramétrage par défaut à retenir comme point de départ daily.
*Catégorie : configuration*
---

### D1389 — Polyvalence et adaptation au style
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « Even though it was originally designed for monthly charts and long-term analysis, it can be used on intraday, daily or weekly charts and the settings can be adjusted to suit one's style. »
**TRADEX-AI C3** : Synthèse — indicateur adaptable au style et à l'horizon de l'opérateur. Flexibilité paramétrique assumée.
*Catégorie : indicateurs_momentum*
---

### D1390 — Positionnement Coppock vs RoC pur
🟢 **FAIT VÉRIFIÉ** (Source : coppock_curve.md) : « The Rate-of-Change indicator measures momentum and the weighted moving average smooths the data. » (Coppock = RoC sommé + WMA, par opposition au RoC nu plus bruité.)
**TRADEX-AI C3** : La Coppock Curve apporte un lissage par rapport au RoC brut → moins de bruit, plus de retard. Choix RoC-pur vs Coppock = compromis réactivité/bruit dans le scoring momentum.
*Catégorie : indicateurs_momentum*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1371 → D1390 (20 décisions) |
| Images certifiées | 7/7 |
| Cercle dominant | C3 (momentum) · renvois C4/structure (D1377) · C7/volume (D1386, D1387) |
| Tags | 🟢 littéral ×19 · 🟡 convention ×1 (D1388) |
| Catégories | indicateurs_momentum, configuration, signal, divergence, timing, structure_marche |
| Actifs concernés | GC · HG · CL · ZW (applicable tous TF) + ES indices (usage d'origine) |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Paramètres clés | Original (14,11,10) ; scans daily (20,10,10) ; signal = croisement zéro + volume > SMA50 |
| À vérifier | Aucun cas — 7/7 images certifiées, texte complet |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
