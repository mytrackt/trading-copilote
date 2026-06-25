# Extraction StockCharts — Introduction to Candlesticks
**Source :** `bundles/stockcharts/introduction_to_candlesticks.md` (HTTP 200 · ~34 033 car.) + 23 images certifiées
**Méthode images :** double ancrage · 23/23 certifiées
**Décisions :** D2211 → D2230 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/introduction-to-candlesticks
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| # | Fichier | Légende | Section |
|---|---------|---------|---------|
| 01 | image_01.webp | Candlestick formation examples from StockCharts.com | Formation of Candlestick Charts |
| 02 | image_02.png | Comparing candlestick charts and bar charts. | Formation of Candlestick Charts |
| 03 | image_03.webp | Long versus short candlesticks. | Long Versus Short Bodies |
| 04 | image_04.webp | White and black Marubozu candlesticks. | Long Versus Short Bodies |
| 05 | image_05.webp | Long upper and lower shadows in candlestick bars. | Long Versus Short Shadows |
| 06 | image_06.webp | Spinning Tops candlestick pattern. | Long Versus Short Shadows |
| 07 | image_07.webp | Examples of Doji candlesticks. | Doji |
| 08 | image_08.webp | Example of a Doji candlestick with a thin line. | Doji |
| 09 | image_09.webp | A long white candle plus a doji (significant after long white) | Doji and Trend |
| 10 | image_10.webp | A long black candlestick plus a doji candlestick. | Doji and Trend |
| 11 | image_11.webp | Example of a long-legged doji. | Long-Legged Doji |
| 12 | image_12.webp | Example of a dragonfly doji and gravestone doji. | Dragonfly and Gravestone Doji |
| 13 | image_13.webp | The six types of Bull vs. Bears candlesticks. | Bulls Versus Bears |
| 14 | image_14.webp | Example of two possible High Low sequences. | What Candlesticks Don't Tell You |
| 15 | image_15.webp | A Star Position gaps away from the previous candlestick. | Star Position |
| 16 | image_16.webp | Harami position (forms within real body of previous candle) | Harami Position |
| 17 | image_17.webp | Hammer and Hanging Man candlesticks. | Hammer and Hanging Man |
| 18 | image_18.webp | Hammer and Hanging Man [SECTION-FALLBACK] | Hammer and Hanging Man |
| 19 | image_19.webp | Inverted Hammer and Shooting Star. | Inverted Hammer and Shooting Star |
| 20 | image_20.webp | Inverted Hammer and Shooting Star reversal patterns. | Inverted Hammer and Shooting Star |
| 21 | image_21.webp | Bullish Engulfing blends into hammer / Bearish Engulfing into shooting star | Blending Candlesticks |
| 22 | image_22.webp | Blending Piercing Pattern → Hammer / Dark Cloud Cover → Shooting Star | Blending Candlesticks |
| 23 | image_23.webp | Three White Soldiers → long white / Three Black Crows → long black | Blending Candlesticks |

## DÉCISIONS

### D2211 — Principes communs de l'analyse technique (origine japonaise)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md) : Les Japonais utilisaient l'analyse technique pour trader le riz au 17e siècle ; principes : « le "quoi" (price action) est plus important que le "pourquoi" », « toute l'information connue est reflétée dans le prix », « acheteurs et vendeurs meuvent les marchés sur attentes et émotions (peur et avidité) », « les marchés fluctuent », « le prix réel peut ne pas refléter la valeur sous-jacente ».
**TRADEX-AI C1** : Socle conceptuel price-action — cohérent avec la priorité Belkhayate au prix ; aucun calcul direct, contexte d'école.
*Catégorie : structure_marche*
🔵 ÉCOLE
---

### D2212 — Construction d'une bougie (corps, ombres, OHLC)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_01) : Une bougie nécessite open/high/low/close. La partie pleine ou creuse est « le corps » (real body) ; les fines lignes au-dessus/dessous sont les « ombres » (wicks/tails). Le haut est marqué par le sommet de l'ombre supérieure, le bas par le bas de l'ombre inférieure.
**TRADEX-AI C1** : Définition de la primitive OHLC utilisée par le lecteur de bougies NT8 (range bars / 15 min).
*Catégorie : structure_marche*
---

### D2213 — Bougie creuse vs pleine (pression acheteuse/vendeuse)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_02) : Si la clôture est supérieure à l'ouverture → bougie creuse (hollow), bas du corps = ouverture, haut = clôture. Si clôture < ouverture → bougie pleine (filled), haut du corps = ouverture, bas = clôture. « Hollow candlesticks … indicate buying pressure. Filled candlesticks … indicate selling pressure. »
**TRADEX-AI C1** : Règle binaire de pression — signal directionnel élémentaire pour la lecture BGC/Direction Belkhayate.
*Catégorie : signal*
---

### D2214 — Longueur du corps = intensité de la pression
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_03) : « the longer the body is, the more intense the buying or selling pressure. » Bougies courtes = peu de mouvement = consolidation.
**TRADEX-AI C1** : Heuristique d'intensité directionnelle utilisable comme pondération qualitative ; non éliminatoire.
*Catégorie : signal*
---

### D2215 — Grandes bougies blanches/noires (contexte de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md) : « Long white candlesticks show strong buying pressure » ; après un long déclin elles peuvent marquer un retournement/support. « Long black candlesticks show strong selling pressure » ; après une longue avance elles peuvent annoncer un retournement/résistance, après un long déclin un panique/capitulation.
**TRADEX-AI C1** : La portée du signal dépend du contexte de tendance — impose de coupler la bougie au filtre de tendance avant tout signal.
*Catégorie : signal*
---

### D2216 — Marubozu (contrôle total acheteur/vendeur)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_04) : Le Marubozu n'a pas d'ombres ; high et low = open ou close. White Marubozu : open = low et close = high → acheteurs ont contrôlé du premier au dernier trade. Black Marubozu : open = high et close = low → vendeurs ont contrôlé.
**TRADEX-AI C1** : Cas extrême de pression directionnelle — détection par égalité OHLC (open=low/close=high ou inverse).
*Catégorie : configuration*
---

### D2217 — Lecture des ombres (longues vs courtes)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_05) : Ombre supérieure = haut de séance, inférieure = bas de séance. Longue ombre supérieure + courte inférieure → acheteurs ont dominé puis vendeurs ont repoussé les prix vers le bas. Longue ombre inférieure + courte supérieure → vendeurs ont dominé puis acheteurs ont fait remonter en clôture.
**TRADEX-AI C1** : Signature de rejet de niveau (mèche) — utile pour confirmation aux pivots Belkhayate.
*Catégorie : signal*
---

### D2218 — Spinning Tops (indécision)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_06) : Longue ombre haute + longue ombre basse + petit corps réel = spinning top. « Spinning tops represent indecision. » Après une longue avance/longue blanche → faiblesse des bulls ; après un long déclin/longue noire → faiblesse des bears ; changement/interruption de tendance potentiel.
**TRADEX-AI C1** : Marqueur d'indécision — critère d'attente plutôt que de signal.
*Catégorie : configuration*
---

### D2219 — Doji (ouverture ≈ clôture, neutre)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_07) : Un doji se forme quand open et close sont quasi égaux ; aspect croix/croix inversée/signe plus. « Alone, doji are neutral patterns. » Tout biais haussier/baissier dépend du price action précédent et de la confirmation future.
**TRADEX-AI C1** : Configuration neutre nécessitant contexte + confirmation — jamais un signal seul.
*Catégorie : configuration*
---

### D2220 — Robustesse d'un doji (relatif au prix/volatilité)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_08) : La robustesse dépend du prix, de la volatilité récente et des bougies précédentes (ex. action à 20 $ vs 200 $). Nison : un doji parmi d'autres petits corps n'est pas important ; parmi de longs corps il est significatif. Le corps doit apparaître comme une fine ligne.
**TRADEX-AI C1** : Seuil de doji = relatif, non absolu — implique une normalisation par volatilité (ATR) avant détection.
*Catégorie : configuration*
🟡 CONVENTION
---

### D2221 — Doji et tendance (affaiblissement de pression)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_09, image_10) : Après une avance/longue blanche, un doji signale que la pression acheteuse s'affaiblit ; après un déclin/longue noire, que la pression vendeuse diminue. « On their own, doji are not enough to mark a reversal. You'll need further confirmation. » Surveiller evening doji star (haut) / morning doji star (bas).
**TRADEX-AI C1** : Doji = pré-alerte de retournement, jamais déclencheur — règle de confirmation obligatoire.
*Catégorie : signal*
---

### D2222 — Long-Legged Doji (indécision marquée)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_11) : Le long-legged doji a de longues ombres haute et basse quasi égales. Les prix ont largement dépassé l'ouverture dans les deux sens mais clôturent ≈ open ; « After a whole lot of yelling and screaming, the result showed little change from the initial open. »
**TRADEX-AI C1** : Forte volatilité intra-période sans direction — critère d'attente.
*Catégorie : configuration*
---

### D2223 — Dragonfly & Gravestone Doji
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_12) : Dragonfly : open=high=close, longue ombre basse (forme « T ») ; vendeurs ont dominé puis acheteurs ont ramené au plus haut/ouverture. Gravestone : open=low=close, longue ombre haute (« T » inversé) ; acheteurs ont dominé puis vendeurs ont ramené au plus bas/ouverture. Implications de retournement dépendent du contexte et de la confirmation.
**TRADEX-AI C1** : Deux dojis directionnels par position des ombres — détection par égalité OHLC partielle ; confirmation requise.
*Catégorie : configuration*
---

### D2224 — Métaphore Bulls vs Bears (6 types)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_13) : Six types de bougies selon la position de la clôture. Long white = bulls ont contrôlé ; long black = bears ; petite bougie = aucun camp ; longue ombre basse = bears ont contrôlé puis bulls reviennent ; longue ombre haute = bulls puis bears reviennent ; longues ombres haute+basse = standoff.
**TRADEX-AI C1** : Taxonomie de lecture rapide de la dominance acheteur/vendeur par bougie.
*Catégorie : structure_marche*
---

### D2225 — Limite des bougies (séquence intra-période inconnue)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_14) : « Candlesticks don't reflect the sequence of events between the open and close. » Le high et le low sont indiscutables mais on ne sait pas lequel est arrivé en premier ; une même bougie peut résulter de centaines de séquences high/low différentes.
**TRADEX-AI C1** : Limite structurelle — justifie le complément order flow (C2 ATAS footprint) pour reconstituer la séquence intra-bougie.
*Catégorie : structure_marche*
---

### D2226 — Tendance préalable requise pour un retournement
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md) : Greg Morris : pour qu'un motif soit un retournement, il faut une tendance préalable à inverser. Retournement haussier ⇒ downtrend préalable ; baissier ⇒ uptrend préalable. Tendance déterminée par trend lines, moyennes mobiles, analyse pics/creux. Bougies court terme : considérer les **1 à 4 dernières semaines**.
**TRADEX-AI C1** : Garde-fou — un signal de retournement bougie est invalide sans tendance préalable identifiée.
*Catégorie : signal*
---

### D2227 — Positions Star et Harami
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_15, image_16) : Star position : une bougie qui gappe à l'écart de la précédente (1re grand corps, 2e petit corps). Harami position : bougie formée à l'intérieur du corps réel de la précédente (« harami » = enceinte en japonais). Doji, hammers, shooting stars, spinning tops peuvent occuper ces positions.
**TRADEX-AI C1** : Définitions positionnelles servant de briques aux motifs 2-3 bougies.
*Catégorie : configuration*
---

### D2228 — Hammer & Hanging Man (mêmes bougies, contexte opposé)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_17, image_18) : Petits corps, longues ombres basses, ombres hautes courtes/absentes. Hammer = retournement haussier après déclin (peut marquer bas/support) ; Hanging Man = retournement baissier après avance (peut marquer haut/résistance). Les deux exigent confirmation (gap ou longue bougie sur fort volume). Ombre longue ≥ 2× le corps réel.
**TRADEX-AI C1** : Paire de motifs dont le sens dépend ENTIÈREMENT du contexte de tendance + confirmation ; volume renforce.
*Catégorie : configuration*
---

### D2229 — Inverted Hammer & Shooting Star
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_19, image_20) : Petits corps, longues ombres hautes, ombres basses courtes/absentes. Shooting Star = retournement baissier après avance (en star position) ; Inverted Hammer = retournement haussier après déclin. Ombre supérieure ≥ 2× le corps. Confirmation requise (gap down/long black à fort volume pour Shooting Star ; gap up/long white pour Inverted Hammer).
**TRADEX-AI C1** : Paire miroir de D2228 — détection par ratio ombre haute/corps + contexte de tendance.
*Catégorie : configuration*
---

### D2230 — Blending (fusion de bougies)
🟢 **FAIT VÉRIFIÉ** (Source : introduction_to_candlesticks.md, image_21, image_22, image_23) : Un motif multi-bougies peut être fusionné en une seule bougie : open de la 1re, close de la dernière, high/low du motif. Bullish Engulfing/Piercing → Hammer ; Bearish Engulfing/Dark Cloud Cover → Shooting Star ; Three White Soldiers → longue blanche ; Three Black Crows → longue noire.
**TRADEX-AI C1** : Technique de réduction d'un motif en primitive unique — utile pour normaliser la détection multi-bougies en un seul signal.
*Catégorie : configuration*
---

## SYNTHÈSE

| Plage | Décisions | Images | Catégories dominantes | Tags |
|-------|-----------|--------|-----------------------|------|
| D2211–D2230 | 20 | 23/23 certifiées | configuration, signal, structure_marche | 🟢 ×20 · 🔵 ×1 (D2211, D2215n/a) · 🟡 ×1 (D2220) |

**Cercle principal :** C1 (Prix / structure de bougie). Aucune image non certifiée.
**Lien Belkhayate :** NON CONCERNÉ directement (méthode bougie générique TA ; complète la lecture price-action mais n'est pas la méthode Belkhayate propriétaire).
**Cas à vérifier :** Aucun. 23/23 images certifiées (double ancrage .md + HTML), incluant image_18 par SECTION-FALLBACK (déjà certifiée).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
