# Rapport Validation Scraper v3 — TRADEX-AI
Date : 2026-06-22

> ✅ **VALIDATION RÉUSSIE** — T1, T2 et T3 PASS après application du correctif
> Option 2 (`images_html()` ne retient que les images de contenu, alignement
> 14/14 avec les `<figure>` du `.md`). Scraper v3.1 prêt pour production.

## Note préalable — URLs & correctif appliqué
- L'URL Moving Averages de la mission était un 404 déguisé
  (`.../technical-overlays/moving-averages.md`). URL correcte retrouvée via
  `llms.txt` : `.../technical-overlays/moving-averages-simple-and-exponential.md`.
- **Échec initial T1** : `.md`=14 `<figure>` vs HTML=20 images → garde-fou
  intégrité → 0 certifiée. Cause : 6 images décoratives répétées (séparateur)
  présentes en HTML hors `<figure>`.
- **Correctif Option 2 (avec accord utilisateur)** : dans `images_html()`, les
  images rendues `class="inline ..."` (décoratives répétées) sont ignorées ;
  seules les images de contenu (`class="block ..."`) sont retenues. Résultat :
  HTML=14, aligné sur les 14 `<figure>` du `.md`. `py_compile` OK.
- Discriminant `inline` validé : il isole exactement les 6 décoratives sur la
  page MA (positions HTML 2,4,8,15,18,20). Aucune signature codée en dur.

## T1 — Moving Averages (non-régression)
- URL utilisée : https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-averages-simple-and-exponential.md
- Bilan : **14 certifiées | 0 à vérifier | 0 décoratives**
- Résultat v2 attendu : 6 certifiées | 0 à vérifier
- Verdict : ✅ **PASS** — les 6 images certifiées en v2 sont **toutes préservées**
  (v2 img1→01, img2→04, img3→05, img4→07, img5→08, img6→13). Les 8 images
  supplémentaires proviennent du double-ancrage v3 (4 via figcaption que la
  méthode `alt` de v2 ratait + 4 via section-fallback). Aucune perte, 0 à
  vérifier : non-régression respectée, gain v3 confirmé.
- Détail manifest :
```
# Bilan : 14 certifiee(s) | 0 a verifier | 0 decorative(s)
image_01.png | label : Example of a Simple Moving Average (SMA) and Exponential Mov | section : What Is a Moving Average?
image_02.png | label : The 10-day EMA in the chart follows price more closely than  | section : The Lag Factor in Moving Averages
image_03.png | label : EMA Accuracy | section : EMA Accuracy [SECTION-FALLBACK]
image_04.png | label : The decline in the 50-day EMA (green) was sharper than the 5 | section : Simple vs Exponential Moving Averages
image_05.png | label : Moving averages can be applied to volume bars and the RSI as | section : Base Data
image_06.png | label : The chart shows that moving averages are effective during st | section : Identifying Trends
image_07.png | label : Example of moving average crossovers. | section : Double Moving Average Crossovers
image_08.png | label : Adding the MACD indicator to a chart can help to quantify EM | section : Double Moving Average Crossovers
image_09.png | label : Price Crossovers | section : Price Crossovers [SECTION-FALLBACK]
image_10.png | label : Identifying Support and Resistance | section : Identifying Support and Resistance [SECTION-FALLBACK]
image_11.png | label : Using with SharpCharts | section : Using with SharpCharts [SECTION-FALLBACK]
image_12.png | label : SharpChart settings for moving averages. | section : Using with SharpCharts
image_13.png | label : Example of charting SMA and EMA with StockChartsACP. | section : Using with StockChartsACP
image_14.png | label : Overlaying a Simple Moving Average on a P&F chart. | section : Using With P&F Charts
```

## T2 — RSI (non-régression)
- URL utilisée : https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi.md
- Bilan : **16 certifiées | 0 à vérifier | 0 décoratives**
- Résultat v2 attendu : 15 certifiées | 0 à vérifier
- Verdict : ✅ **PASS** — les 15 images certifiées en v2 sont **toutes préservées**
  (décalées +1). L'image +1 (`image_01`) est l'ancienne décorative du rang 1
  (`What Is the RSI?`), désormais certifiée via section-fallback. Aucune
  régression, gain v3 confirmé.
- Détail manifest :
```
# Bilan : 16 certifiee(s) | 0 a verifier | 0 decorative(s)
image_01.png | label : What Is the Relative Strength Index (RSI)? | [SECTION-FALLBACK]
image_02.png | label : RS vs. RSI Plots
image_03.png | label : RSI Calculation Example
image_04.png | label : Overbought and Oversold RSI
image_05.png | label : Overbought/Oversold RSI in a Trading Range
image_06.png | label : RSI Divergences
image_07.png | label : RSI Divergences in a strong trend
image_08.png | label : Bullish RSI Failure Swing
image_09.png | label : Bearish RSI Failure Swing
image_10.png | label : Using RSI to identify an uptrend
image_11.png | label : Using RSI to identify a downtrend
image_12.png | label : Identifying a positive reversal with RSI
image_13.png | label : Identifying a negative reversal with RSI
image_14.png | label : Using RSI on a SharpChart
image_15.png | label : RSI Settings on the SharpCharts Workbench
image_16.png | label : Using RSI on an ACP chart
```

## T3 — MACD (nouveau — section-fallback)
- URL utilisée : https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-moving-average-convergence-divergence-oscillator.md
- Bilan : **11 certifiées | 0 à vérifier | 0 décoratives**
- Résultat v2 : 1 certifiée | 10 décoratives
- Résultat v3 attendu : 11 certifiées | 0 décoratives
- Verdict : ✅ **PASS** — résultat exactement conforme. 1 Pattern A
  (`StockCharts MACD interpretation` = l'unique certifiée v2) + 10 récupérées
  via section-fallback.
- Détail manifest :
```
# Bilan : 11 certifiee(s) | 0 a verifier | 0 decorative(s)
image_01.jpg | label : What Is the Moving Average Convergence/Divergence Oscillator | [SECTION-FALLBACK]
image_02.jpg | label : StockCharts MACD interpretation | section : Oscillator   (Pattern A)
image_03.png | label : Signal Line Crossovers | [SECTION-FALLBACK]
image_04.png | label : Centerline Crossovers | [SECTION-FALLBACK]
image_05.png | label : Centerline Crossovers | [SECTION-FALLBACK]
image_06.png | label : Centerline Crossovers | [SECTION-FALLBACK]
image_07.png | label : Divergences | [SECTION-FALLBACK]
image_08.png | label : Divergences | [SECTION-FALLBACK]
image_09.png | label : Divergences | [SECTION-FALLBACK]
image_10.png | label : Using MACD With SharpCharts | [SECTION-FALLBACK]
image_11.png | label : Using MACD With SharpCharts | [SECTION-FALLBACK]
```

## Verdict global
[X] ✅ **SCRAPER V3 VALIDÉ — prêt pour production**
[ ] ❌ ÉCHEC

Les 3 tests passent (T1 14/14, T2 16/16, T3 11/11), aucune image « à vérifier »,
aucune perte par rapport à v2, gain section-fallback confirmé. Correctif Option 2
appliqué et compilé.

## Images [SECTION-FALLBACK] détectées (T3 MACD)
10 images certifiées via section-fallback (figcaption vide → titre de section) :
- image_01.jpg — « What Is the Moving Average Convergence/Divergence Oscillator? »
- image_03.png — « Signal Line Crossovers »
- image_04.png / image_05.png / image_06.png — « Centerline Crossovers »
- image_07.png / image_08.png / image_09.png — « Divergences »
- image_10.png / image_11.png — « Using MACD With SharpCharts »

(image_02.jpg « StockCharts MACD interpretation » est certifiée en Pattern A, pas
en fallback — c'est l'unique image que v2 certifiait déjà.)

## Observation (non bloquante)
Le section-fallback produit des labels **non uniques** quand une section contient
plusieurs images sans légende (ex. MACD : 3× « Centerline Crossovers », 3×
« Divergences », 2× « Using MACD With SharpCharts »). Les images restent
correctement certifiées et téléchargées ; à prévoir côté Agent 2 (analyse/KB) une
désambiguïsation (ex. suffixe rang) si un label unique est requis. N'affecte pas
la validation du scraper.
```
