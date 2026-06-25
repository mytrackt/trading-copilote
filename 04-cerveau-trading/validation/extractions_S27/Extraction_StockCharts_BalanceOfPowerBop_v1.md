# Extraction StockCharts — Balance of Power (BOP)
**Source :** `bundles/stockcharts/balance_of_power_bop.md` (HTTP 200 · ~9 271 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D851 → D862 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/balance-of-power-bop
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Balance of Power? | What Is the Balance of Power? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Charting with the Balance of Power Indicator | Charting with the Balance of Power Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D851 — Définition et nature de l'oscillateur BOP
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md, image_01) : « Balance of Power (BOP) is an oscillator that measures the strength of buying and selling pressure. Introduced by Igor Levshin in the August 2001 issue of *Technical Analysis of Stocks & Commodities* magazine, this indicator compares the power of buyers to push prices to higher extremes with the power of sellers to move prices to lower extremes. »
**TRADEX-AI C2** : Indicateur order-flow approximé par le prix (pas par le volume) ; candidat à C2 (pression acheteuse/vendeuse) en complément du footprint ATAS.
*Catégorie : indicateurs_momentum*
---

### D852 — Interprétation positif/négatif et ligne zéro
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « When the indicator is in positive territory, the bulls are in charge, and sellers dominate when the indicator is negative. A reading near the zero line indicates a balance between the two and can mean a trend reversal. »
**TRADEX-AI C1** : Lecture directionnelle simple (>0 haussier / <0 baissier / ≈0 équilibre = possible renversement) exploitable comme brique de confirmation.
*Catégorie : signal*
---

### D853 — Alias BMP
🟡 **CONVENTION** (Source : balance_of_power_bop.md) : « This indicator is sometimes referred to as the Balance of Market Power (BMP). »
**TRADEX-AI C2** : Synonyme à reconnaître lors du parsing de sources externes (BOP = BMP).
*Catégorie : indicateurs_momentum*
---

### D854 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : Formule simplifiée de Livshin : `BOP = (Close - Open) / (High - Low)`.
**TRADEX-AI C1** : Formule déterministe codable directement à partir des barres OHLC NT8 (aucune donnée volume requise).
*Catégorie : indicateurs_momentum*
---

### D855 — Lissage par moyenne mobile (SMA 14)
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « using these raw daily values makes for a choppy oscillator, so the values are typically smoothed with a moving average. Livshin recommends smoothing with a 14-period SMA, but the number of periods can be modified to fit the timeframe being charted. »
**TRADEX-AI C1** : Paramètre par défaut SMA(14) ; période ajustable selon le timeframe (15 min standard / range bars Belkhayate).
*Catégorie : indicateurs_momentum*
---

### D856 — Bornes -1 / +1 et signification des extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « The resulting indicator oscillates between -1 and +1. A positive value indicates a Security that is closing above its open... A maximum value of +1 would indicate that the security opened at the low and closed at the high value for every time period included in the moving average. »
**TRADEX-AI C1** : Échelle normalisée [-1 ; +1] facilitant un seuil fixe inter-actifs (GC/HG/CL/ZW).
*Catégorie : indicateurs_momentum*
---

### D857 — Usages globaux de l'indicateur
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « the Balance of Power indicator can be used to identify trends, divergences from price, and overbought/oversold conditions. Zero-line crossovers provide buying and selling signals. »
**TRADEX-AI C1** : Quatre usages : tendance, divergence, surachat/survente, croisement de zéro — à mapper sur la grille de score /10.
*Catégorie : signal*
---

### D858 — Croisements de la ligne zéro (signaux achat/vente)
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « A cross above the center line generates a buy signal, and a cross below generates a sell signal. The data is smoothed with a moving average in order to reduce the number of whipsaws. An SMA with more periods reduces the number of false crossover signals, but also reduces the responsiveness of the indicator. »
**TRADEX-AI C1** : Croisement haussier de 0 = signal d'achat ; baissier = signal de vente. Arbitrage réactivité/whipsaws via la période SMA (jamais signal isolé pour mode AUTO).
*Catégorie : signal*
---

### D859 — Identification de tendance
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « A rising BOP line indicates an upward trend and a falling BOP line indicates a downward trend. The zero-line crossover confirms the trend change. »
**TRADEX-AI C1** : Pente du BOP = proxy directionnel ; le croisement de zéro confirme le changement de tendance.
*Catégorie : indicateurs_tendance*
---

### D860 — Divergences avec le prix
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « When price makes new highs but BOP doesn't, that is a negative divergence; when price makes new lows but BOP doesn't, that is a positive divergence. These divergences can foreshadow a change in trend. »
**TRADEX-AI C1** : Divergence prix/BOP comme signal avancé de renversement ; brique « divergence » de la grille de score.
*Catégorie : divergence*
---

### D861 — Conditions de surachat/survente (calibrage par actif)
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : « Chartists will need to look at historical levels for the security they are studying to determine what should be considered overbought/oversold for that security. Once those overbought/oversold levels have been established for that security, then look for dips beyond those levels. »
**TRADEX-AI C1** : Pas de seuil universel surachat/survente ; calibrage historique par actif requis (GC ≠ HG ≠ CL ≠ ZW) avant usage.
*Catégorie : indicateurs_momentum*
---

### D862 — Scans bullish/bearish de croisement de zéro
🟢 **FAIT VÉRIFIÉ** (Source : balance_of_power_bop.md) : Scan bullish `[BOP(14) x 0]` (croise au-dessus de zéro) et bearish `[0 x BOP(14)]` (croise sous zéro), avec filtres liquidité `Daily SMA(20,Daily Volume) > 40000` et prix `Daily SMA(60,Daily Close) > 20` ; la page précise « This scan is just a starting point. Further refinement and analysis are required. »
**TRADEX-AI C1** : Syntaxe de détection programmable du croisement de zéro ; à adapter aux futures (volume/prix non transposables tels quels).
*Catégorie : signal*
---

## SYNTHÈSE

| Plage | Décisions | Images | Tags dominants | Cercle |
|-------|-----------|--------|----------------|--------|
| D851→D862 | 12 | 2/2 certifiées | 🟢 (11) · 🟡 (1) | C1 / C2 |

Indicateur BOP entièrement déterministe et codable depuis OHLC (sans volume) : formule `(Close-Open)/(High-Low)` lissée SMA(14), borné [-1;+1]. Usages : croisement de zéro (signal), pente (tendance), divergences, surachat/survente calibré par actif. Aucun lien Belkhayate explicite dans la source → non rattaché à la méthode. Aucun cas ambigu, aucune image à vérifier.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
