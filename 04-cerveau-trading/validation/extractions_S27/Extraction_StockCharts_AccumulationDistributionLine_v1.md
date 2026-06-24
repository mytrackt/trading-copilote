# Extraction StockCharts — Accumulation/Distribution Line (ADL)
**Source :** `bundles/stockcharts/accumulation_distribution_line.md` (HTTP 200 · ~11 200 car.) + 9 images certifiées
**Méthode images :** double ancrage · 9/9 certifiées
**Décisions :** D451 → D463 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/accumulation-distribution-line
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Table | Image | Label certifié | Section | Décision liée |
|-------|-------|----------------|---------|---------------|
| — | image_01.png | Chart 1 - Accumulation Distribution Line | Calculating the Accumulation Distribution Line | D453 |
| — | image_02.png | Table 1 - Accumulation Distribution Line | Calculating the Accumulation Distribution Line | D453 |
| — | image_03.png | Chart 2 - Accumulation Distribution Line | ADL versus OBV | D456 |
| — | image_04.png | Chart 3 - Accumulation Distribution Line | Using the ADL for Trend Confirmation | D457 |
| — | image_05.png | Chart 4 - Accumulation Distribution Line | ADL Divergences | D458 |
| — | image_06.png | Chart 5 - Accumulation Distribution Line | ADL Divergences | D459 |
| — | image_07.png | Chart 6 - Accumulation Distribution Line | Disconnect with Prices | D460 |
| — | image_08.png | Chart 7 - Accumulation Distribution Line | Using with SharpCharts | D462 |
| — | image_09.png | SharpCharts - Accumulation Distribution Line | Using with SharpCharts | D462 |

## DÉCISIONS

### D451 — Définition et auteur de l'ADL
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : « The Accumulation Distribution Line is a volume-based indicator developed by Marc Chaikin to measure the cumulative flow of money into and out of a security. » Chaikin l'a d'abord appelé la « Cumulative Money Flow Line ».
**TRADEX-AI C2** : ADL = indicateur de flux de volume cumulé (order flow proxy), à intégrer au cercle C2 comme jauge de pression acheteuse/vendeuse sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*
---

### D452 — Formule de calcul en 3 étapes
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : « 1. Money Flow Multiplier = [(Close - Low) - (High - Close)] / (High - Low) ; 2. Money Flow Volume = Money Flow Multiplier x Volume for the Period ; 3. ADL = Previous ADL + Current Period's Money Flow Volume ».
**TRADEX-AI C2** : Formule déterministe codable directement à partir des barres NT8 (High/Low/Close/Volume) — aucun paramètre libre, reproductible.
*Catégorie : indicateurs_momentum*
---

### D453 — Comportement du Money Flow Multiplier
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_01, image_02) : « The Money Flow Multiplier fluctuates between +1 and -1. (…) The multiplier is positive when the close is in the upper half of the high-low range and negative when in the lower half. (…) The multiplier is +1 when the close is on the high and -1 when the close is on the low. (…) At 0.50, only half of the volume translates into the period's Money Flow Volume. »
**TRADEX-AI C2** : Le multiplicateur pondère le volume selon la position de la clôture dans le range — proche de la lecture Belkhayate « force de clôture ». Clôture haute = accumulation, clôture basse = distribution.
*Catégorie : indicateurs_momentum*
---

### D454 — Rôle interprétatif : confirmer ou contredire la tendance
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : « Money Flow Volume accumulates to form a line that either confirms or contradicts the underlying price trend. (…) the indicator is used to either reinforce the underlying trend or cast doubts on its sustainability. »
**TRADEX-AI C2** : ADL sert de filtre de confirmation de tendance, à croiser avec la lecture de direction du cercle C1 (prix Belkhayate) avant validation d'un signal.
*Catégorie : indicateurs_tendance*
---

### D455 — Divergence prix/ADL = signal de retournement potentiel
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : « An uptrend in prices with a downtrend in the Accumulation Distribution Line suggests underlying selling pressure (distribution) that could foreshadow a bearish reversal (…). A downtrend in prices with an uptrend in the Accumulation Distribution Line indicates underlying buying pressure (accumulation) that could foreshadow a bullish price reversal. »
**TRADEX-AI C2** : Divergence ADL = alerte de retournement à intégrer comme critère de pondération dans la grille /10 (non éliminatoire, signal d'attention).
*Catégorie : divergence*
---

### D456 — ADL vs OBV : différence de formule
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_03) : « OBV adds a period's total volume when the close is up and subtracts it when the close is down (…). Chaikin took a different approach by completely ignoring the change from one period to the next. Instead, the Accumulation Distribution Line focuses on the level of the close relative to the high-low range. » Exemple Clorox (CLX) : gap baissier mais clôture proche du haut → OBV chute, ADL monte.
**TRADEX-AI C2** : ADL et OBV peuvent diverger ; ADL capte mieux la qualité de clôture intra-range. Ne pas les confondre — choisir ADL pour cohérence avec la logique de clôture Belkhayate.
*Catégorie : indicateurs_momentum*
---

### D457 — Usage en confirmation de tendance
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_04) : « An uptrend in the Accumulation Distribution Line reinforces an uptrend on the price chart and vice versa. » Exemple Freeport McMoran (FCX) : ADL a confirmé chaque phase de tendance (hausse fév.-mars, baisse avril-juin, hausse juil.-janv.).
**TRADEX-AI C2** : Concordance prix/ADL = renfort de confiance sur la tendance ; à utiliser comme bonus de score quand la direction C1 et l'ADL pointent dans le même sens.
*Catégorie : indicateurs_tendance*
---

### D458 — Divergence haussière (bullish)
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_05) : « A bullish divergence forms when price moves to new lows, but the Accumulation Distribution Line does not confirm these lows and moves higher. (…) Based on the theory that volume precedes price, chartists should be on alert for a bullish reversal. » Exemple Nordstrom (JWN) : ADL a creusé en juillet puis remonté, nouveau plus-bas prix en août, retournement haussier confirmé par gap up sur gros volume.
**TRADEX-AI C2** : Divergence haussière = stealth buying ; exige une confirmation prix (catalyseur) avant entrée — ne jamais trader la divergence seule.
*Catégorie : divergence*
---

### D459 — Divergence baissière (bearish)
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_06) : « A bearish divergence forms when price moves to new highs, but the Accumulation Distribution Line does not confirm and moves lower. This shows distribution or underlying selling pressure that can foreshadow a bearish reversal. » Exemple Southwest Airlines (LUV) : ADL a culminé deux mois avant les prix, faiblesse confirmée par cassure de support et RSI passant sous 40.
**TRADEX-AI C2** : Divergence baissière = distribution ; confirmer par cassure de structure C1 (support) avant de valider un signal VENDRE.
*Catégorie : divergence*
---

### D460 — Limites : déconnexion possible prix/indicateur
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md, image_07) : « This makes it at least two steps removed from the actual price (…). The Money Flow Multiplier does not take into account price changes from period to period. As such, it cannot be expected to always affirm price action or successfully predict price reversals with divergences. Sometimes the Accumulation Distribution Line simply doesn't work. »
**TRADEX-AI C2** : Garde-fou — l'ADL ignore les gaps inter-périodes et peut se déconnecter du prix. Ne jamais l'utiliser comme critère unique ; toujours pondérer dans la grille, jamais en éliminatoire isolé.
*Catégorie : gestion_risque_entree*
---

### D461 — Conclusion : indicateur non autonome
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : « An uptrend indicates that buying pressure is prevailing (…) while a downtrend indicates that selling pressure is prevailing. Bullish and bearish divergences serve as alerts for a potential reversal (…). It is not a standalone indicator. »
**TRADEX-AI C2** : ADL = jauge de pression de volume + détecteur de divergence, à combiner obligatoirement avec C1 (prix) et autres indicateurs. Confirme la règle projet « jamais de signal sur un seul critère ».
*Catégorie : signal*
---

### D462 — Paramétrage SharpCharts (positionnement + MA)
🔵 **ÉCOLE** (Source : accumulation_distribution_line.md, image_08, image_09) : « The indicator can be positioned above, below or behind the price (…). Positioning "behind price" makes it easy to compare with the underlying security. Chartists can also add a moving average to the indicator by using the advanced options. »
**TRADEX-AI C2** : Méthodologie d'affichage propre à SharpCharts ; pour TRADEX-AI, calculer une MA sur l'ADL pour générer un signal de croisement (cf. scans AccDist Signal 20/65).
*Catégorie : configuration*
---

### D463 — Scans de divergence (seuils opérationnels)
🟢 **FAIT VÉRIFIÉ** (Source : accumulation_distribution_line.md) : Scan divergence haussière — base ≥ 10$ et ≥ 100 000 de volume/jour sur 60 jours, prix sous SMA(65) et SMA(20) mais « Daily AccDist > Daily AccDist Signal (65) » et « > Daily AccDist Signal (20) » (idem OBV). Scan baissier = conditions inversées. Note : « For scanning purposes, daily volume data is incomplete during the trading day (…) base the scan on the "Last Market Close." »
**TRADEX-AI C2** : Logique de scan transposable — comparer ADL à sa propre moyenne signal (20 et 65 périodes). Garde-fou staleness : volume intra-journalier incomplet → calculer sur clôture confirmée uniquement, cohérent avec le Staleness Monitor.
*Catégorie : signal*
---

## SYNTHÈSE
| Champ | Valeur |
|-------|--------|
| Décisions ajoutées | 13 (D451 → D463) |
| Images citées | 9/9 certifiées |
| Catégories | indicateurs_momentum, indicateurs_tendance, divergence, signal, configuration, gestion_risque_entree |
| Tags | 🟢 FAIT VÉRIFIÉ ×12 · 🔵 ÉCOLE ×1 |
| Cercle dominant | C2 (order flow / volume) |
| Belkhayate | Aucun lien affirmé par la source. Rapprochement possible « force de clôture dans le range » (D453) ⚫🔴 hypothèse projet, non affirmée par la source. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, NON fusionnée dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur.
