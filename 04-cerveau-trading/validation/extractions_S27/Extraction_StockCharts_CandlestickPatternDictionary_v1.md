# Extraction StockCharts — Candlestick Pattern Dictionary

**Source :** `bundles/stockcharts/candlestick_pattern_dictionary.md` (HTTP 200 · ~7 800 car.) + 32 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 32/32 certifiées
**Décisions :** D1031 → D1044 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlestick-pattern-dictionary
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> ℹ️ Dictionnaire de ~38 figures synthétisé par familles (≤14 décisions, consigne Agent 2). Chaque famille regroupe plusieurs entrées littérales de la source.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.jpg | Abandoned Baby | Abandoned Baby | CERTIFIE |
| image_02.jpg | Dark Cloud Cover | Dark Cloud Cover | CERTIFIE |
| image_03.jpg | Doji | Doji | CERTIFIE |
| image_04.jpg | Downside Tasuki Gap | Downside Tasuki Gap | CERTIFIE |
| image_05.jpg | Dragonfly Doji | Dragonfly Doji | CERTIFIE |
| image_06.jpg | Engulfing Pattern | Engulfing Pattern | CERTIFIE |
| image_07.jpg | Evening Doji Star | Evening Doji Star | CERTIFIE |
| image_08.jpg | Evening Star | Evening Star | CERTIFIE |
| image_09.jpg | Falling Three Methods | Falling Three Methods | CERTIFIE |
| image_10.jpg | Gravestone Doji | Gravestone Doji | CERTIFIE |
| image_11.jpg | Hammer | Hammer | CERTIFIE |
| image_12.jpg | Hanging Man | Hanging Man | CERTIFIE |
| image_13.jpg | Harami | Harami | CERTIFIE |
| image_14.jpg | Harami Cross | Harami Cross | CERTIFIE |
| image_15.jpg | Inverted Hammer | Inverted Hammer | CERTIFIE |
| image_16.jpg | Long Body / Long Day | Long Body / Long Day | CERTIFIE |
| image_17.jpg | Long-Legged Doji | Long-Legged Doji | CERTIFIE |
| image_18.jpg | Long Shadows | Long Shadows | CERTIFIE |
| image_19.jpg | Marubozu | Marubozu | CERTIFIE |
| image_20.jpg | Morning Doji Star | Morning Doji Star | CERTIFIE |
| image_21.jpg | Morning Star | Morning Star | CERTIFIE |
| image_22.jpg | Piercing Line | Piercing Line | CERTIFIE |
| image_23.jpg | Rising Three Methods | Rising Three Methods | CERTIFIE |
| image_24.jpg | Shooting Star | Shooting Star | CERTIFIE |
| image_25.jpg | Short Body / Short Day | Short Body / Short Day | CERTIFIE |
| image_26.jpg | Spinning Top | Spinning Top | CERTIFIE |
| image_27.jpg | Stars | Stars | CERTIFIE |
| image_28.jpg | Stick Sandwich | Stick Sandwich | CERTIFIE |
| image_29.jpg | Three Black Crows | Three Black Crows | CERTIFIE |
| image_30.jpg | Three White Soldiers | Three White Soldiers | CERTIFIE |
| image_31.jpg | Upside Gap Two Crows | Upside Gap Two Crows | CERTIFIE |
| image_32.jpg | Upside Tasuki Gap | Upside Tasuki Gap | CERTIFIE |

## DÉCISIONS

### D1031 — Objet du dictionnaire
🟢 **FAIT VÉRIFIÉ** (Source : candlestick_pattern_dictionary.md) : « The StockCharts Candlestick Pattern Dictionary provides brief descriptions of many common candlestick patterns. » StockCharts maintient aussi une liste de scans prédéfinis (Predefined Scan Results → section Candlestick Patterns) mise à jour en séance.
**TRADEX-AI C1** : Source = référentiel de définitions des figures pour le moteur de reconnaissance C1 ; l'existence de scans temps réel confirme que ces figures sont algorithmiquement détectables.
*Catégorie : configuration*
---

### D1032 — Famille Doji (indécision)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_03, image_17) : « Doji form when the open and close of a security are virtually equal (…) convey a sense of indecision or tug-of-war between buyers and sellers. » Le Long-Legged Doji a de longues ombres haut et bas avec le doji au milieu du range, reflétant clairement l'indécision.
**TRADEX-AI C1+C5** : Le doji = corps quasi nul (open≈close) → neutralité/indécision ; signal contextuel (à un sommet/creux il annonce une bascule potentielle). Détectable par seuil « |close-open| ≈ 0 ».
*Catégorie : signal*
---

### D1033 — Doji directionnels (Dragonfly / Gravestone)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_05, image_10) : Dragonfly Doji = doji dont open et close sont au plus haut du jour (longue ombre basse) ; « normally appears at market turning points ». Gravestone Doji = doji au plus bas du jour (longue ombre haute).
**TRADEX-AI C1** : Dragonfly = rejet du bas (biais haussier potentiel) ; Gravestone = rejet du haut (biais baissier potentiel) — lecture par position du corps dans le range, utile aux retournements sur support/résistance.
*Catégorie : signal*
---

### D1034 — Famille Hammer / Hanging Man (même forme, contexte opposé)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_11, image_12) : Hammer et Hanging Man se forment « when a security moves significantly lower after the open but rallies to close well above the intraday low » (longue ombre basse, petit corps). En déclin → **Hammer** (haussier) ; en avance → **Hanging Man** (baissier).
**TRADEX-AI C1+C3** : Même morphologie, signal opposé selon la **tendance préalable** → la détection seule ne suffit pas, le contexte de tendance est obligatoire (garde-fou anti-faux-signal).
*Catégorie : signal*
---

### D1035 — Inverted Hammer / Shooting Star (même forme, contexte opposé)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_15, image_24) : Inverted Hammer = retournement haussier 1 jour en downtrend (ouvre bas, monte, clôture près de l'open → ombre haute longue). Shooting Star = même forme en uptrend mais baissier, « looks just like the Inverted Hammer, except it's bearish ».
**TRADEX-AI C1+C3** : Paire symétrique à longue ombre haute ; signal dépend de la tendance préalable (downtrend→bullish, uptrend→bearish). Confirmation requise (gap/clôture suivante).
*Catégorie : signal*
---

### D1036 — Engulfing Pattern (englobement open/close)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_06) : Figure de retournement bullish (fin de downtrend) ou bearish (fin d'uptrend) ; jour 2 « completely engulfs the previous day's body and closes in the opposite direction of the trend ». Proche de l'outside reversal mais n'exige que l'englobement open/close (pas tout le range).
**TRADEX-AI C1** : Détection = corps J2 ⊃ corps J1 + clôture opposée à la tendance ; signal de retournement fort (2 jours). Critère précis (open/close, pas high/low).
*Catégorie : signal*
---

### D1037 — Harami / Harami Cross (corps inclus, indécision)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_13, image_14) : Harami = figure 2 jours, petit corps « completely contained within the range of the previous body » et de couleur opposée. Harami Cross = identique mais J2 est un Doji.
**TRADEX-AI C1** : Inverse géométrique de l'engulfing (corps J2 ⊂ corps J1) → essoufflement de la tendance ; Harami Cross (doji) = variante plus forte d'indécision. Signal de retournement plus faible que l'engulfing, à confirmer.
*Catégorie : signal*
---

### D1038 — Famille Stars (gap d'isolement) — Morning/Evening
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_27, image_21, image_08, image_20, image_07) : « A candlestick that gaps away from the previous candlestick is said to be in a star position. » Morning Star = retournement haussier 3 jours (long noir → petit corps gapé bas → long blanc clôturant au-dessus du milieu du 1er) ; Evening Star = symétrique baissier. Variantes Doji (Morning/Evening Doji Star) : le corps central est un Doji.
**TRADEX-AI C1+C5** : Figures 3 bougies à gap central ; Morning=signal long, Evening=signal short ; la clôture au-delà du milieu du 1er corps est le critère de validation. Variantes Doji = indécision renforcée au pivot.
*Catégorie : signal*
---

### D1039 — Abandoned Baby (doji isolé par deux gaps)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_01) : « A rare reversal pattern characterized by a gap followed by a Doji, which is then followed by another gap in the opposite direction. The shadows on the Doji must completely gap below or above the shadows of the first and third day. »
**TRADEX-AI C1** : Retournement rare mais fort (doji totalement isolé par 2 gaps d'ombres) ; critère strict (ombres non chevauchantes) → faible fréquence, forte fiabilité quand présent.
*Catégorie : signal*
---

### D1040 — Dark Cloud Cover / Piercing Line (pénétration du milieu de corps)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_02, image_22) : Dark Cloud Cover (baissier) = en uptrend, J2 ouvre à un nouveau haut puis « closes below the midpoint of the body of the first day ». Piercing Line (haussier) = en downtrend, J2 ouvre à un nouveau bas puis clôture au-dessus du milieu du corps J1.
**TRADEX-AI C1** : Paire symétrique 2 jours ; critère mesurable = clôture J2 franchit le **milieu** du corps J1. Dark Cloud=short, Piercing=long.
*Catégorie : signal*
---

### D1041 — Triples bougies de continuation (Tasuki Gaps, Three Methods)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_32, image_04, image_23, image_09) : Upside/Downside Tasuki Gap = continuation : corps gapé puis bougie opposée qui rentre dans le gap « but does not close the gap ». Rising/Falling Three Methods = continuation : long corps + 3 petits corps contenus dans son range + 5e bougie à nouveau plus haut (rising) / plus bas (falling).
**TRADEX-AI C1+C3** : Figures de **continuation** (pas retournement) — confirment la tendance en cours ; le gap non comblé (Tasuki) et la consolidation contenue (Three Methods) signalent la reprise.
*Catégorie : signal*
---

### D1042 — Triples bougies de retournement (Crows / Soldiers / Upside Gap Two Crows / Stick Sandwich)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_29, image_30, image_31, image_28) : Three Black Crows = retournement baissier (3 longs corps noirs, chacun clôt près de son bas, ouvre dans le corps précédent). Three White Soldiers = symétrique haussier. Upside Gap Two Crows = figure baissière 3 jours en uptrend. Stick Sandwich = retournement haussier (2 corps noirs encadrant 1 blanc, clôtures des 2 noirs égales).
**TRADEX-AI C1** : Figures 3 bougies de retournement fort ; Crows=short, Soldiers=long. Détection par escalier directionnel + relation open/close successifs.
*Catégorie : signal*
---

### D1043 — Briques élémentaires (Marubozu, Long/Short Body, Long Shadows, Spinning Top)
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlestick_pattern_dictionary.md, image_19, image_16, image_25, image_18, image_26) : Marubozu = chandelier sans ombre (open ou close = extrême). Long Body = grand mouvement open→close (forte conviction) ; Short Body = petit mouvement. Long Shadows : longue ombre haute = acheteurs dominants en début de séance puis cédés ; longue ombre basse = vendeurs dominants. Spinning Top = petit corps + ombres dépassant le corps → indécision.
**TRADEX-AI C1+C2** : Vocabulaire de base de lecture d'une bougie unique : taille de corps = conviction, ombres = pression rejetée. Briques composant les figures multi-bougies ci-dessus ; directement paramétrables (ratios corps/ombre).
*Catégorie : structure_marche*
---

### D1044 — Détectabilité algorithmique (scans prédéfinis StockCharts)
🟢 **FAIT VÉRIFIÉ** (Source : candlestick_pattern_dictionary.md) : « StockCharts.com maintains a list of stocks with common candlestick patterns on their charts in the Predefined Scan Results area (…) updated throughout each trading day. »
**TRADEX-AI C1** : Confirme que ces figures sont détectables par règles déterministes sur OHLC — base d'implémentation d'un détecteur de patterns côté moteur C1 (sur données NT8/ATAS), sans dépendre de l'outil StockCharts.
*Catégorie : configuration*
---

## SYNTHÈSE

| Famille | Apport pour TRADEX-AI | Cercle | Tag |
|---------|------------------------|--------|-----|
| Doji (+ Long-Legged) | Indécision (open≈close), pivot potentiel | C1+C5 | 🔵 |
| Dragonfly / Gravestone | Rejet bas (haussier) / rejet haut (baissier) | C1 | 🔵 |
| Hammer / Hanging Man | Même forme, signal selon tendance préalable | C1+C3 | 🔵 |
| Inverted Hammer / Shooting Star | Longue ombre haute, signal selon tendance | C1+C3 | 🔵 |
| Engulfing | Corps J2 englobe J1 → retournement fort | C1 | 🔵 |
| Harami / Harami Cross | Corps J2 inclus → essoufflement | C1 | 🔵 |
| Stars (Morning/Evening + Doji) | Gap central, clôture > milieu = validation | C1+C5 | 🔵 |
| Abandoned Baby | Doji isolé 2 gaps, rare/fiable | C1 | 🔵 |
| Dark Cloud / Piercing | Franchit milieu du corps J1 | C1 | 🔵 |
| Tasuki / Three Methods | Continuation (gap non comblé / consolidation) | C1+C3 | 🔵 |
| Crows / Soldiers / Sandwich | Triples bougies de retournement | C1 | 🔵 |
| Briques (Marubozu, corps, ombres, spinning top) | Vocabulaire de base 1 bougie | C1+C2 | 🔵 |
| Détectabilité | Figures détectables par règles OHLC | C1 | 🟢 |

**Belkhayate :** ⚫ NON CONCERNÉ — aucun lien explicite avec la méthode Belkhayate dans la source.
**Actifs :** principe générique applicable à GC·HG·CL·ZW (détection chandelier sur OHLC NT8/ATAS) ; les figures à gap dépendent de la session/continuité du contrat futures.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Décisions BRUTES en zone validation/, non fusionnées dans KNOWLEDGE_BASE_MASTER.json.
