# Extraction StockCharts — Force Index
**Source :** `bundles/stockcharts/force_index.md` (HTTP 200 · ~15 770 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D1851 → D1870 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/force-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Table 1 - Force Index | Calculating the Force Index | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 1 - Force Index | Calculating the Force Index | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 2 - Force Index | Trend Identification | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 3 - Force Index | Divergences | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 4 - Force Index | Identifying Corrections | CERTIFIE (accord .md + HTML) |
| image_06.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | SharpCharts - Force Index | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1851 — Définition et auteur du Force Index (Elder)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « The Force Index is an indicator that uses price and volume to assess the power behind a move or identify possible turning points. Developed by Alexander Elder, the Force Index was introduced in his classic book, Trading for a Living. »
**TRADEX-AI C2** : oscillateur prix+volume d'Alexander Elder mesurant la puissance d'un mouvement ; indicateur volume/momentum (C2 order flow).
*Catégorie : indicateurs_momentum*
---

### D1852 — Trois éléments du mouvement de prix : direction, ampleur, volume
🔵 **ÉCOLE** (Source : force_index.md) : « there are three essential elements to a stock's price movement: direction, extent and volume. The Force Index combines all three as an oscillator that fluctuates in positive and negative territory as the balance of power shifts. »
**TRADEX-AI C2** : le Force Index agrège direction + ampleur + volume en un oscillateur de rapport de force.
*Catégorie : indicateurs_momentum*
---

### D1853 — Trois usages : confirmer tendance, corrections, divergences
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « The Force Index can be used to reinforce the overall trend, identify playable corrections or foreshadow reversals with divergences. »
**TRADEX-AI C2** : trois cas d'usage = confirmation de tendance, repérage de corrections jouables, divergences annonçant un retournement.
*Catégorie : indicateurs_momentum*
---

### D1854 — Formule du Force Index 1 période
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_01) : « Force Index(1) = {Close (current period) - Close (prior period)} x Volume. »
**TRADEX-AI C2** : FI(1) = (clôture actuelle − clôture précédente) × volume. Formule directement codable.
*Catégorie : indicateurs_momentum*
---

### D1855 — Formule du Force Index lissé (EMA 13)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « Force Index(13) = 13-period EMA of Force Index(1)... a 13-period Force Index is a 13-period EMA of the 1-period Force Index values for the last 13 periods. »
**TRADEX-AI C2** : FI(13) = EMA 13 périodes du FI(1) ; lissage par défaut recommandé par Elder.
*Catégorie : indicateurs_momentum*
---

### D1856 — Trois facteurs déterminant la valeur du Force Index
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_01) : « the Force Index is positive when the current close is above the prior close... negative when... below... the extent of the move determines the volume multiplier... A big move on big volume produces high Force Index values. »
**TRADEX-AI C2** : signe = sens de clôture ; magnitude = ampleur × volume. Gros mouvement + gros volume = valeur extrême.
*Catégorie : indicateurs_momentum*
---

### D1857 — Le FI(1) est bruité, l'EMA 13 réduit les croisements
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_02) : « the 1-period Force Index fluctuates above/below the zero line and looks quite jagged. Elder recommends smoothing the indicator with a 13-period EMA to reduce the positive-negative crossovers. »
**TRADEX-AI C2** : FI(1) trop bruité → lisser en EMA13 pour limiter les faux croisements de la ligne zéro.
*Catégorie : indicateurs_momentum*
---

### D1858 — Interprétation : signe = qui domine acheteurs/vendeurs
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « A positive price change signals that buyers were stronger than sellers, while a negative price change signals that sellers were stronger than buyers. »
**TRADEX-AI C2** : FI positif = acheteurs dominants ; FI négatif = vendeurs dominants.
*Catégorie : indicateurs_momentum*
---

### D1859 — Le volume mesure l'engagement (commitment)
🔵 **ÉCOLE** (Source : force_index.md) : « volume, which, according to Elder, measures commitment... A big advance on heavy volume shows a strong commitment from buyers. Likewise, a big decline on heavy volume shows a strong commitment from sellers. »
**TRADEX-AI C2** : le volume traduit l'engagement des participants ; fort volume = forte conviction directionnelle.
*Catégorie : indicateurs_momentum*
---

### D1860 — Identification de tendance via paramètres longs (100 jours)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_03) : « the 100-day Force Index is smoother and crosses the zero line fewer times... can be used to determine the medium- or long-term trend... a resistance breakout on the price chart corresponds to a resistance breakout on the 100-day Force Index. »
**TRADEX-AI C2** : FI(100) lissé pour tendance moyen/long terme ; les cassures S/R du prix et du FI se confirment mutuellement.
*Catégorie : indicateurs_tendance*
---

### D1861 — Le FI(100) confirme cassures de support et résistance
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_03) : « The 100-day Force Index moved into positive territory and broke resistance in mid-February... turned negative in mid-May. The early June support break on the price chart was confirmed with a support break in the Force Index. »
**TRADEX-AI C2** : passage du FI(100) en territoire positif/négatif valide les cassures de prix correspondantes.
*Catégorie : signal*
---

### D1862 — Divergences haussières et baissières définies
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_04) : « A bullish divergence forms when the indicator moves higher as the security moves lower... A bearish divergence forms when the indicator moves lower as the security moves higher... This discrepancy can foreshadow a [bearish/bullish] trend reversal. »
**TRADEX-AI C2** : divergence haussière = FI monte / prix baisse ; baissière = FI baisse / prix monte ; annonce de retournement potentiel.
*Catégorie : signal*
---

### D1863 — Confirmation obligatoire des divergences
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « confirmation from the indicator or price chart is needed. A bullish divergence can be confirmed with the Force Index moving into positive territory or a resistance breakout on the price chart. A bearish divergence can be confirmed with the Force Index moving into negative territory or a support break. »
**TRADEX-AI C2** : ne jamais trader une divergence seule ; exiger passage FI en territoire positif/négatif ou cassure S/R du prix.
*Catégorie : signal*
---

### D1864 — Exemple BBY : confirmation des divergences FI(39)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_04) : « A bullish divergence is confirmed when the Force Index (39) crosses into positive territory (green dotted lines). A bearish divergence is confirmed when the Force Index (39) crosses into negative territory. »
**TRADEX-AI C2** : cas illustratif Best Buy — FI(39) confirme les divergences par croisement de la ligne zéro.
*Catégorie : signal*
---

### D1865 — FI(13) court terme vs FI(39) moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « The Force Index (13) captures short-term fluctuations and is more sensitive. The Force Index (39) captures medium-term fluctuations and is smoother... There is no right or wrong answer for these settings. »
**TRADEX-AI C2** : choix de période = arbitrage sensibilité/lissage selon horizon ; pas de réglage universel.
*Catégorie : indicateurs_momentum*
---

### D1866 — Identifier corrections : EMA 22 + FI 2 jours (Elder)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_05) : « Alexander Elder recommends using a 22-day EMA for trend identification and a 2-day Force Index to identify corrections. The trend is up when the 22-day EMA is moving higher, which means the 2-day Force Index would be used to identify short-term pullbacks for buying. »
**TRADEX-AI C2** : système Elder — EMA22 pour la tendance, FI(2) pour repérer pullbacks (achat en up) / rebonds (vente en down).
*Catégorie : timing*
---

### D1867 — Variante moyen terme : EMA 100 + FI 10 jours
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « This is an aggressive strategy best suited for active traders. The timeframe can be adjusted... medium-term traders might experiment with a 100-day EMA and 10-day Force Index. »
**TRADEX-AI C2** : la stratégie EMA22/FI2 est agressive (traders actifs) ; déclinable en EMA100/FI10 pour le moyen terme.
*Catégorie : timing*
---

### D1868 — Deux écoles d'entrée sur correction (agir tôt vs attendre la fin)
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md, image_05) : « Traders can act when the Force Index turns negative or wait for it to move back into positive territory. Acting when negative may improve the reward-to-risk ratio, but the correction could extend... Waiting for the Force Index to turn positive again shows some strength. »
**TRADEX-AI C2** : choix d'entrée — agir au FI négatif (meilleur R/R mais risque d'extension) ou attendre retour positif (confirmation de fin de correction).
*Catégorie : gestion_risque_entree*
---

### D1869 — Synthèse : FI long terme donne le biais directionnel
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « The bulls have the edge when the 100-day Force Index is positive. The bears have the edge when the 100-day Force Index is negative... traders can then look for short-term setups in harmony with the larger trend. »
**TRADEX-AI C2** : FI(100) positif = biais haussier, négatif = biais baissier ; chercher setups court terme alignés au biais.
*Catégorie : indicateurs_tendance*
---

### D1870 — Avertissement scans : volume incomplet en séance
🟢 **FAIT VÉRIFIÉ** (Source : force_index.md) : « daily volume data is incomplete during the trading day. When running scans with volume-based indicators like the Force Index, base the scan on the "Last Market Close." » + « traders should use the Force Index in conjunction with other indicators. »
**TRADEX-AI C2** : garde-fou data — le volume intraday est incomplet ; baser les calculs FI sur la clôture confirmée. Ne pas utiliser le FI seul.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Plage | Décisions | Images | Cercles | Catégories dominantes |
|-------|-----------|--------|---------|-----------------------|
| D1851→D1870 | 20 | 7/7 certifiées | C2 (majoritaire — volume/momentum Elder), C1 | indicateurs_momentum, indicateurs_tendance, signal, timing, gestion_risque_entree |

Tags : 🟢 17 · 🔵 3 · 🟡 0 · ⏳ 0 · 🔴 0 · ⚫ 0. Force Index = indicateur volume/momentum d'Elder → Cercle C2 (order flow / engagement volume). Lien Belkhayate : NON CONCERNÉ (indicateur Elder, distinct du MFI = Énergie Belkhayate). Actifs visés : GC·HG·CL·ZW (formule FI directement implémentable).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
