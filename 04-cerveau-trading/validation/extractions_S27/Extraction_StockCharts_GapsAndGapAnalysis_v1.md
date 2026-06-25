# Extraction StockCharts — Gaps and Gap Analysis
**Source :** `bundles/stockcharts/gaps_and_gap_analysis.md` (HTTP 200 · ~16 506 car.) + 5 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D1891 → D1910 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/gaps-and-gap-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of up and down price gaps. | What Are Price Gaps? | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of common gaps in a stock price chart. | What Are Common Gaps? | CERTIFIE (accord .md + HTML) |
| image_03.jpg | Example of a breakaway gap in a stock's price chart. | What Are Breakaway Gaps? | CERTIFIE (accord .md + HTML) |
| image_04.png | Example of a runaway gap. | What Are Runaway Gaps? | CERTIFIE (accord .md + HTML) |
| image_05.jpg | Example of an exhaustion gap. | What Are Exhaustion Gaps? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1891 — Définition d'un gap de prix
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md, image_01) : « Price charts often have blank spaces known as gaps, representing times when no shares were traded within a particular price range. Usually this occurs between the market close and the next trading day's open. There are two primary kinds of gaps—up gaps and down gaps. »
**TRADEX-AI C1** : Un gap = espace vide sur le chart (aucun échange dans une plage de prix), typiquement entre clôture et ouverture suivante ; deux types primaires : up gap / down gap.
*Catégorie : structure_marche*
---

### D1892 — Condition de formation up gap / down gap
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « For an up gap to form, the low price after the market closes must be higher than the high price of the previous day. Up gaps are generally considered bullish. A down gap is the opposite of an up gap; the high price after the market closes must be lower than the low price of the previous day. Down gaps are usually considered bearish. »
**TRADEX-AI C1** : Détection déterministe codable — up gap : low(jour) > high(veille) → biais haussier ; down gap : high(jour) < low(veille) → biais baissier. Applicable GC/HG/CL/ZW.
*Catégorie : signal*
---

### D1893 — Cause fondamentale des gaps (déséquilibre offre/demande)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Gaps result from extraordinary buying or selling interests often developing while the market is closed... This results in an imbalance between supply and demand... Gaps can offer evidence that something important has happened to the fundamentals or psychology of the crowd. »
**TRADEX-AI C1** : Un gap signale un déséquilibre offre/demande né hors séance — preuve d'un événement fondamental ou psychologique. Brique de contexte (lien news gate / sentiment).
*Catégorie : structure_marche*
---

### D1894 — Significativité d'un gap = volume au-dessus de la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Up and down gaps can form on daily, weekly, or monthly charts and are considered significant when accompanied by above average volume. »
**TRADEX-AI C1** : Filtre de qualité — ne retenir un gap comme significatif que si volume > moyenne. Confirmation par volume requise avant tout usage en signal.
*Catégorie : signal*
---

### D1895 — Fréquence des gaps selon le timeframe
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Gaps appear more frequently on daily charts... Gaps on weekly or monthly charts are rare. If you're looking at a weekly chart, the gap would have to occur between Friday's close and Monday's open. »
**TRADEX-AI C7** : Les gaps daily sont fréquents ; weekly/monthly rares. À pondérer selon les timeframes Belkhayate (Standard 15min vs daily).
*Catégorie : timing*
---

### D1896 — Gaps quotidiens = titre peu liquide à éviter ; gaps intraday non significatifs
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « A price chart with gaps that occur almost daily is typical for thinly-traded securities and should probably be avoided... Such temporary intraday gaps should not be considered as having any more significance than normal market volatility. »
**TRADEX-AI C1** : Filtre de liquidité — un actif qui gappe quasi quotidiennement est peu liquide (à éviter) ; gaps intraday éphémères = simple volatilité, à ignorer.
*Catégorie : gestion_risque_entree*
---

### D1897 — Les quatre catégories de gaps
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Gaps can be subdivided into four basic categories: Common Gaps, Breakaway Gaps, Runaway Gaps, and Exhaustion Gaps. »
**TRADEX-AI C1** : Taxonomie en 4 classes (Common / Breakaway / Runaway / Exhaustion) ; base de la classification d'un gap détecté.
*Catégorie : structure_marche*
---

### D1898 — Common Gap (gap de zone / trading gap)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md, image_02) : « This type of gap is sometimes referred to as a trading gap or an area gap. Common gaps are usually uneventful... and usually get filled fairly quickly... A common gap usually appears in a trading range or congestion area, reinforcing the apparent lack of interest... it's doubtful that they will produce trading opportunities. »
**TRADEX-AI C1** : Common gap = sans intérêt, en range/congestion, comblé rapidement, volume faible. À NE PAS trader.
*Catégorie : signal*
---

### D1899 — Définition de « gap fill » (comblement)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « "Getting filled" means that the price action at a later time (a few days to a few weeks) usually retraces, at the least, to the last day before the gap. This is also known as closing the gap. »
**TRADEX-AI C1** : Un gap est « comblé » quand le prix retrace au moins au dernier jour avant le gap. Notion d'objectif de retracement codable.
*Catégorie : structure_marche*
---

### D1900 — Breakaway Gap (sortie de range avec volume)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md, image_03) : « These occur when the price action is breaking out of a trading range or congestion area... Volume will (should) pick up significantly... The point of the breakout now becomes the new support (if it's an upside breakout) or resistance (if it's a downside breakout). Avoid falling into the trap of thinking this type of gap... will be filled soon. »
**TRADEX-AI C1** : Breakaway gap = cassure de range/congestion avec hausse de volume ; le point de cassure devient support (haussier) ou résistance (baissier) ; ne PAS attendre son comblement.
*Catégorie : signal*
---

### D1901 — Volume idéalement après le gap (continuation)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « It's better if the increase in volume happens after the gap occurs. This means that the new change in market direction has a chance of continuing. »
**TRADEX-AI C2** : Pour un breakaway, le volume montant APRÈS le gap renforce la probabilité de continuation. Critère de confirmation order-flow (ATAS).
*Catégorie : signal*
---

### D1902 — Gaps + patterns classiques = signal renforcé
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Price gaps associated with classic chart patterns tend to be stronger than those that aren't. For example, an ascending triangle with a breakaway gap to the upside can be a much better trade than a breakaway gap without a good chart pattern. »
**TRADEX-AI C1** : Pondération — un gap couplé à un pattern classique (ex. triangle ascendant) est plus fort. Confluence pattern + gap = bonus de score.
*Catégorie : signal*
---

### D1903 — Runaway Gap (gap d'accélération de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md, image_04) : « Runaway gaps are best described as gaps caused by increased interest in the stock. Runaway gaps to the upside typically represent traders who didn't get in during the initial move... This type of runaway gap represents a near-panic state in traders... note the significant increase in volume during and after the runaway gap. »
**TRADEX-AI C1** : Runaway gap = accélération en pleine tendance, état de quasi-panique, volume élevé pendant/après. Confirme la poursuite de tendance.
*Catégorie : signal*
---

### D1904 — Measuring Gap (gap à mi-parcours du mouvement)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « The term measuring gap is also used for runaway gaps... The theory is that the measuring gap will occur in the middle of, or halfway through, the move. »
**TRADEX-AI C1** : Synonyme « measuring gap » du runaway — théorie : il se produit au milieu du mouvement (≈ projection de l'amplitude restante). Outil de projection de cible.
*Catégorie : timing*
---

### D1905 — Runaway gaps en futures (limites de l'échange)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Sometimes, the futures market will have runaway gaps caused by trading limits imposed by the exchanges. Getting caught on the wrong side of the trend when you have these limit moves in futures can be horrifying... These are not common occurrences in the futures market. »
**TRADEX-AI C1** : Spécifique futures (GC/HG/CL/ZW) — les limites de cotation (limit moves) peuvent générer des runaway gaps ; risque sévère si position du mauvais côté. Garde-fou risque.
*Catégorie : gestion_risque_entree*
---

### D1906 — Exhaustion Gap (gap d'épuisement de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md, image_05) : « Exhaustion gaps happen near the end of a good up or downtrend... identified by high volume and a large price difference between the previous day's close and the new opening price. They can easily be mistaken for runaway gaps if you overlook the exceptionally high volume. Exhaustion gaps are quickly filled as prices reverse their trend. »
**TRADEX-AI C1** : Exhaustion gap = fin de tendance, volume exceptionnellement haut + grand écart close→open, comblé rapidement avec retournement. Signal d'alerte de fin de mouvement.
*Catégorie : signal*
---

### D1907 — Implications par type de gap (stratégie/risque)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Each type signifies different market conditions, with implications for strategy and risk management... Gaps provide valuable insights into market sentiment and potential trading opportunities. »
**TRADEX-AI C1** : La classification du gap conditionne la stratégie et la gestion du risque ; chaque type porte un message de sentiment distinct.
*Catégorie : gestion_risque_entree*
---

### D1908 — L'adage « tous les gaps se comblent » est faux pour Breakaway/Runaway
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « The adage that all gaps eventually get filled might not always hold true, especially in the case of Breakaway and Runaway gaps. Waiting for breakout or runaway gaps to be filled can devastate your portfolio. Similarly, waiting for prices to fill a gap before getting on board a trend might make you miss a big move. »
**TRADEX-AI C1** : NE PAS appliquer la règle « gap toujours comblé » aux Breakaway/Runaway ; attendre le comblement = risque de rater le mouvement ou de subir des pertes. Anti-biais.
*Catégorie : gestion_risque_entree*
---

### D1909 — Gaps non comblés comme support/résistance
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Some traders believe that unfilled gaps act as areas of support and resistance and expect the price to revisit those levels in the future. When the price eventually returns to fill the gap, it is considered a gap fill. »
**TRADEX-AI C1** : Un gap non comblé peut servir de zone de support/résistance future. Niveau de référence pour entrées/stops (complémentaire des pivots Belkhayate).
*Catégorie : structure_marche*
---

### D1910 — Gaps comme signaux de trading (renvoi stratégies gap)
🟢 **FAIT VÉRIFIÉ** (Source : gaps_and_gap_analysis.md) : « Price gaps can be used as trading signals. There are various gap trading strategies you can explore... Traders often analyze the size, volume, and location of the gap within the price chart to determine its significance. »
**TRADEX-AI C1** : Trois critères d'analyse d'un gap = taille, volume, localisation. Triplet déterministe à coder pour qualifier tout gap détecté.
*Catégorie : signal*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1891 → D1910 (20) |
| Images | 5/5 certifiées |
| Tags | 🟢 ×20 (tout littéral, école StockCharts/Edwards-Magee classique) |
| Cercles | C1 (majorité, prix/structure), C2 (volume order-flow ×2), C7 (timeframe ×1) |
| Catégories | structure_marche ×5, signal ×8, gestion_risque_entree ×4, timing ×2, (D1910 signal) |
| Lien Belkhayate | NON CONCERNÉ directement ; gaps non comblés = niveaux S/R complémentaires des pivots |
| Cas à vérifier | Aucun — manifest 5/5 certifié, intégrité .md=HTML OK |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. BRUT, non fusionné.
