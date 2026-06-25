# Extraction StockCharts — Bollinger Bands
**Source :** `bundles/stockcharts/bollinger_bands.md` (HTTP 200 · ~20 033 car.) + 13 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 13/13 certifiées
**Décisions :** D911 → D925 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/bollinger-bands
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : page du créateur (John Bollinger) → règles taguées 🔵 ÉCOLE.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Are Bollinger Bands? | What Are Bollinger Bands? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 1 | Formulas | CERTIFIE (accord .md + HTML) |
| image_03.png | Formulas | Formulas [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 2 | Confirming W-Bottom Chart Patterns | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 3 | Confirming W-Bottom Chart Patterns | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 4 | Confirming M-Top Chart Patterns | CERTIFIE (accord .md + HTML) |
| image_07.png | Chart 5 | Confirming M-Top Chart Patterns | CERTIFIE (accord .md + HTML) |
| image_08.png | Chart 6 | Measuring Trend Strength: Walking the Bands | CERTIFIE (accord .md + HTML) |
| image_09.png | Chart 7 | Measuring Trend Strength: Walking the Bands | CERTIFIE (accord .md + HTML) |
| image_10.png | Chart 8 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_11.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_12.png | Chart 9 | Using With StockChartsACP | CERTIFIE (accord .md + HTML) |
| image_13.png | Chart 10 | Using With P&F Charts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D911 — Définition et nature des Bollinger Bands
🔵 **ÉCOLE** (Source : bollinger_bands.md, image_01) : « Developed by John Bollinger, Bollinger Bands® are volatility bands placed above and below a moving average. Volatility is based on the standard deviation... The bands automatically widen when volatility increases and contract when volatility decreases. Their dynamic nature allows them to be used on different securities with the standard settings. »
**TRADEX-AI C1** : Overlay de volatilité auto-adaptatif, utilisable avec réglages standard sur GC/HG/CL/ZW ; brique de contexte de volatilité.
*Catégorie : indicateurs_tendance*
---

### D912 — Formules des trois bandes
🔵 **ÉCOLE** (Source : bollinger_bands.md, image_02, image_03) : « Middle Band = 20-day simple moving average (SMA) · Upper Band = 20-day SMA + (20-day standard deviation of price x 2) · Lower Band = 20-day SMA - (20-day standard deviation of price x 2). » « A simple moving average is used because the standard deviation formula also uses a simple moving average. »
**TRADEX-AI C1** : Formules déterministes codables directement ; SMA(20) au centre, ±2σ pour les bandes (σ sur la même fenêtre 20).
*Catégorie : indicateurs_tendance*
---

### D913 — Réglage du multiplicateur d'écart-type selon la période
🟡 **CONVENTION** (Source : bollinger_bands.md) : « Bollinger recommends making small incremental adjustments to the standard deviation multiplier... With a 20-day SMA... the multiplier is set at 2. Bollinger suggests increasing the standard deviation multiplier to 2.1 for a 50-period SMA and decreasing the standard deviation multiplier to 1.9 for a 10-period SMA. »
**TRADEX-AI C1** : Table de réglage : (10, 1.9) / (20, 2) / (50, 2.1) ; à appliquer si l'on change la période sur un timeframe Belkhayate.
*Catégorie : indicateurs_tendance*
---

### D914 — Usages principaux (M-Tops, W-Bottoms, force de tendance)
🔵 **ÉCOLE** (Source : bollinger_bands.md) : « They can be used to confirm M-Tops and W-Bottoms or to determine the trend's strength. Signals based on the distance between the upper and lower band, including the popular Bollinger Band Squeeze, are identified using the related Bollinger BandWidth indicator. »
**TRADEX-AI C1** : Trois usages : confirmation W-Bottom, confirmation M-Top, mesure de force de tendance (walking the bands) ; le squeeze relève de BandWidth.
*Catégorie : signal*
---

### D915 — Confirmation d'un W-Bottom (4 étapes)
🔵 **ÉCOLE** (Source : bollinger_bands.md, image_04, image_05) : « First, a reaction low forms. This low is usually, but not always, below the lower band. Second, there is a bounce towards the middle band. Third, there is a new price low... This low holds **above** the lower band... Fourth, the pattern is confirmed with a strong move off the second low and a resistance break. » Exemples Nordstrom (JWN) et Sandisk.
**TRADEX-AI C1** : Configuration de retournement haussier en 4 étapes ; le 2e creux tenant AU-DESSUS de la bande inférieure = clé (moins de faiblesse).
*Catégorie : configuration*
---

### D916 — Confirmation d'un M-Top (non-confirmation en 3 étapes)
🔵 **ÉCOLE** (Source : bollinger_bands.md, image_06, image_07) : « First, a security creates a reaction high above the upper band. Second, there is a pullback towards the middle band. Third, prices move above the prior high but fail to reach the upper band. This is a warning sign... waning momentum... Final confirmation comes with a support break or bearish indicator signal. » Exemples Exxon Mobil (XOM, + divergence MACD) et Pulte Homes (PHM, head-and-shoulders).
**TRADEX-AI C1** : Configuration de retournement baissier ; nouveau sommet n'atteignant PAS la bande supérieure = momentum déclinant, à confirmer par cassure de support / signal baissier.
*Catégorie : configuration*
---

### D917 — Les bandes sont « tags », pas signaux ; clôtures vs intraday
🔵 **ÉCOLE** (Source : bollinger_bands.md) : « moves that touch or exceed the bands are not signals, but rather "tags". On the face of it, a move to the upper band shows strength, while a sharp move to the lower band shows weakness. » (M-Top XOM) « it did not CLOSE above the upper band » — les signaux se lisent en clôture.
**TRADEX-AI C1** : Un contact de bande n'est PAS un signal d'entrée/sortie ; privilégier les clôtures vs les mèches intraday — garde-fou anti-faux-signal.
*Catégorie : signal*
---

### D918 — Walking the Bands (force de tendance)
🔵 **ÉCOLE** (Source : bollinger_bands.md, image_08) : « prices can "walk the band" with numerous touches during a strong uptrend... it is also common for prices to never reach the lower band during an uptrend. The 20-day SMA sometimes acts as support... dips below the 20-day SMA sometimes provide buying opportunities before the next tag of the upper band. »
**TRADEX-AI C1** : En tendance forte, contacts répétés de la bande = force (pas surachat) ; la SMA(20) sert de support dynamique et de zone d'achat sur repli.
*Catégorie : indicateurs_tendance*
---

### D919 — Surachat ≠ baissier (contacts en tendance)
🔵 **ÉCOLE** (Source : bollinger_bands.md) : « Overbought is not necessarily bullish. It takes strength to reach overbought levels and overbought conditions can extend in a strong uptrend... An upper band touch that occurs after a Bollinger Band confirmed W-Bottom would signal the start of an uptrend. »
**TRADEX-AI C1** : Aligné avec Bob Farrell R4 (surachat ≠ top en tendance forte) ; un contact de bande supérieure après W-Bottom confirmé = début de tendance, pas signal de vente.
*Catégorie : indicateurs_tendance*
---

### D920 — Exemple APD : Bollinger + CCI (combinaison d'oscillateur)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md, image_08) : Air Products (APD) — « APD closed above the upper band at least five times over a four-month period... the 10-period Commodity Channel Index (CCI). Dips below -100 are deemed oversold and moves back above -100 signal the start of an oversold bounce. The upper band tag and breakout started the uptrend. CCI then identified tradable pullbacks. »
**TRADEX-AI C1** : Méthode combinée : Bollinger pour la tendance + CCI(10) pour timer les replis (repli sous -100 puis retour) ; archétype « overlay + oscillateur ».
*Catégorie : signal*
---

### D921 — Exemple MON : walk down la bande inférieure
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md, image_09) : Monsanto (MON) — « a walk down the lower band... closed below the lower band at least five times... did not close above the upper band once during this period. The support break and initial close below the lower band signaled a downtrend... CCI... A move above +100 is overbought. A move back below +100 signals a resumption of the downtrend. »
**TRADEX-AI C1** : Version baissière symétrique du walking the bands ; CCI(10) sert à timer les rebonds short (>+100 puis retour <+100) en downtrend.
*Catégorie : signal*
---

### D922 — Les bandes contiennent 88-89 % de l'action des prix
🔵 **ÉCOLE** (Source : bollinger_bands.md) : « According to Bollinger, the bands should contain 88-89% of price action, which makes a move outside the bands significant. Technically, prices are relatively high when they're above the upper band and relatively low when below the lower band. »
**TRADEX-AI C1** : Repère statistique : ~88-89 % du prix dans les bandes ; une sortie de bande est statistiquement notable (mais ≠ signal d'achat/vente direct).
*Catégorie : indicateurs_tendance*
---

### D923 — « Relativement haut/bas » ≠ signal ; jamais en standalone
🔵 **ÉCOLE** (Source : bollinger_bands.md) : « "relatively high" should not be regarded as bearish or a sell signal. Likewise, "relatively low" should not be considered bullish or a buy signal. Prices are high or low for a reason... Bollinger Bands are not meant to be used as a stand-alone tool. Chartists should combine Bollinger Bands with basic trend analysis and other indicators for confirmation. »
**TRADEX-AI C1** : Garde-fou explicite du créateur : ne jamais utiliser les BB seules ; confirmation par tendance + autres indicateurs obligatoire → cohérent avec la grille /10 multi-cercles.
*Catégorie : gestion_risque_entree*
---

### D924 — Paramétrage chartiste (SharpCharts / ACP / P&F)
🟡 **CONVENTION** (Source : bollinger_bands.md, image_10, image_11, image_12, image_13) : « default setting... (20,2). The first number (20) sets the periods for the simple moving average and the standard deviation. The second number (2) sets the standard deviation multiplier... A Bollinger Band overlay can be set at (50,2.1) for a longer timeframe or at (10,1.9) for a shorter timeframe. » Sur P&F : « since P&F moving averages are double smoothed, it may be necessary to shorten the moving average period. »
**TRADEX-AI C1** : Paramètres (20,2) par défaut, (50,2.1) long terme, (10,1.9) court terme ; pour usage TRADEX-AI seuls les paramètres comptent (les plateformes citées ne s'appliquent pas à NT8).
*Catégorie : indicateurs_tendance*
---

### D925 — Scans de croisement de bande (bullish / bearish)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bands.md) : Scan bullish `[Daily Close x Daily Upper BB(20,2.0)]` (clôture passe au-dessus de la bande sup) et bearish `[Daily Lower BB(20,2.0) x Daily Close]` (clôture passe sous la bande inf), avec filtres `Daily SMA(20,Daily Volume) > 40000` et `Daily SMA(60,Daily Close) > 5` ; « This scan is just a starting point. Further refinement and analysis are required. »
**TRADEX-AI C1** : Logique de détection programmable du franchissement de bande en clôture ; point de départ à raffiner (jamais signal autonome, cf. D923).
*Catégorie : signal*
---

## SYNTHÈSE

| Plage | Décisions | Images | Tags dominants | Cercle |
|-------|-----------|--------|----------------|--------|
| D911→D925 | 15 | 13/13 certifiées | 🔵 ÉCOLE (11) · 🟢 (3) · 🟡 (2) | C1 (dominant) |

Page du créateur John Bollinger → règles 🔵 ÉCOLE. Points durs codables : formules des 3 bandes (SMA20 ±2σ), tables de réglage (10,1.9)/(20,2)/(50,2.1), repère 88-89 %, scans de croisement en clôture. Configurations exploitables : W-Bottom (4 étapes, haussier) et M-Top (3 étapes, baissier). Garde-fous forts et alignés TRADEX-AI : contacts = « tags » pas signaux (D917), lire en clôture pas intraday (D917), surachat ≠ baissier en tendance (D919 ↔ Farrell R4), JAMAIS en standalone (D923 ↔ grille multi-cercles). Méthode combinée BB + CCI(10) documentée (D920/D921). Aucun lien Belkhayate explicite. Aucun cas ambigu, aucune image à vérifier.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
