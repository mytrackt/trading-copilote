# Extraction StockCharts — Williams Alligator
**Source :** `bundles/stockcharts/alligator.md` (HTTP 200 · ~7 600 car.) + 6 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D571 → D582 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/alligator
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Alligator Overlay? | What Is the Alligator Overlay? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Fractals added to a chart with the Alligator Overlay | Fractal Identification | CERTIFIE (accord .md + HTML) |
| image_03.png | Sleeping, Awakening, and Hungry phases of the Alligator overlay | The Hungry Alligator | CERTIFIE (accord .md + HTML) |
| image_04.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | SharpCharts settings for the Alligator overlay | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_06.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D571 — Définition de l'Alligator (3 SMMA décalées, périodes Fibonacci 13/8/5)
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md, image_01) : « The Alligator overlay, developed by Bill Williams, is a technical analysis tool based on three offset smoothed moving averages (SMMAs) set at three Fibonacci-based periods - 13, 8, and 5. The three lines - Jaw, Teeth, and Lips - make up the Alligator's mouth, and the relationship between these lines helps to identify trend presence, direction, and potential market entries and exits. »
**TRADEX-AI C1** : Indicateur de tendance candidat sur GC/HG/CL/ZW basé sur 3 moyennes mobiles lissées décalées ; mesure présence/direction de tendance. À traiter comme outil auxiliaire, hors méthode Belkhayate (NON CONCERNÉ par les pivots/BGC).
*Catégorie : indicateurs_tendance*
---

### D572 — Prémisse Bill Williams : les tendances n'apparaissent que 15–30 % du temps
🔵 **ÉCOLE** (Bill Williams) (Source : alligator.md) : « Williams created this overlay on the premise that trends occur only 15% to 30% of the time, with the remaining periods consisting of sideways or non-trending movements. The Alligator was, therefore, designed to signal the "awakening" of a new trend from its non-trending, or "sleeping," state. »
**TRADEX-AI C1** : Hypothèse fondatrice de l'école Williams — le marché est majoritairement en range. Justifie un filtre de tendance avant signal sur GC/HG/CL/ZW ; reste une convention d'école, non un fait mesuré sur nos actifs.
*Catégorie : structure_marche*
---

### D573 — Jaw (ligne bleue) : SMMA 13 du midpoint, décalée +8 barres
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « Jaw (Blue Line): This line is calculated as a 13-period SMMA of the midpoint prices (average of the high and low prices), shifted forward (into the future) by eight bars. »
**TRADEX-AI C1** : Paramètre de calcul exact à coder — Jaw = SMMA(13) sur (high+low)/2, offset +8. Le midpoint = moyenne haut/bas de chaque barre.
*Catégorie : indicateurs_tendance*
---

### D574 — Teeth (ligne rouge) : SMMA 8 du midpoint, décalée +5 barres
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « Teeth (Red Line): This line is calculated as an eight-period SMMA of the midpoint prices, shifted forward by five bars. »
**TRADEX-AI C1** : Paramètre exact — Teeth = SMMA(8) sur midpoint, offset +5.
*Catégorie : indicateurs_tendance*
---

### D575 — Lips (ligne verte) : SMMA 5 du midpoint, décalée +3 barres
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « Lips (Green Line): This line is calculated as a five-period SMMA of the midpoint prices, shifted forward by three bars. »
**TRADEX-AI C1** : Paramètre exact — Lips = SMMA(5) sur midpoint, offset +3. Triplet complet 13,8,5 / offsets 8,5,3 (param SharpCharts : 13,8,8,5,5,3).
*Catégorie : indicateurs_tendance*
---

### D576 — Nature du SMMA (lissé, retard supérieur à SMA et EMA)
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « The SMMA uses more historical data than a simple moving average (SMA), but recent data is not weighted as heavily as with an exponential moving average (EMA). The resulting line is smoother than either the SMA or EMA, but lags both. »
**TRADEX-AI C1** : Le SMMA est plus lisse mais plus en retard que SMA/EMA. Implication : signaux Alligator tardifs → à utiliser comme confirmation de tendance, pas comme déclencheur précoce d'entrée.
*Catégorie : indicateurs_tendance*
---

### D577 — Fractales : patterns 5 barres (bullish = plus bas low central, bearish = plus haut high central)
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md, image_02) : « With Bullish Fractals, the center bar has the lowest low of the five, with the surrounding bars showing higher lows. The arrow appears below the center bar. Bearish Fractals are the opposite: the center bar has the highest high of the five, with the surrounding bars showing lower highs. The arrow appears above the center bar. »
**TRADEX-AI C1** : Fractale = pattern structurel de 5 barres servant de niveau de déclenchement. Bullish = creux local (low central plus bas que ses 2 voisins de chaque côté) ; Bearish = sommet local. Utilisable comme niveau d'entrée/sortie sur GC/HG/CL/ZW.
*Catégorie : structure_marche*
---

### D578 — Trois phases de marché : sleeping / awakening / hungry
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md, image_03) : « The Alligator overlay shows three possible market phases - sleeping, awakening, and hungry - based on the relative position of the Alligator's three moving averages. » Sleeping = lignes entremêlées (non-trending, éviter de trader) ; Awakening = les Lips croisent Teeth et Jaw (tendance possible) ; Hungry = les 3 lignes s'écartent et s'expandent (tendance établie).
**TRADEX-AI C1** : Machine à 3 états dérivée de l'écartement/croisement des 3 SMMA. Sleeping → no-trade ; Awakening (croisement Lips) → alerte/entrée potentielle ; Hungry (expansion) → tendance forte. Direction du croisement = sens (haussier/baissier).
*Catégorie : signal*
---

### D579 — Signal d'entrée : phase "awakening", confirmation par passage en "hungry"
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « you might consider entering a trade (long or short) during the "awakening" phase. Ideally, you will want to see the Alligator shift into a "hungry" phase, which signals a strengthening trend. »
**TRADEX-AI C3** : Logique d'entrée auxiliaire — entrer pendant l'awakening, confirmer par le passage en hungry. Sert de couche de confirmation de tendance, jamais de seul critère d'ordre (à croiser avec Belkhayate + grille /10).
*Catégorie : configuration*
---

### D580 — Entrée via fractale haussière (cassure du plus haut high de la fractale)
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « In a bullish awakening phase (with the shorter SMMA on top), watch for a bullish fractal, then wait for price to break above the highest high of the fractal. »
**TRADEX-AI C3** : Règle d'entrée précise — en awakening haussier (Lips au-dessus), attendre une fractale haussière puis un breakout au-dessus du plus haut high de cette fractale. Niveau d'entrée objectif et codable.
*Catégorie : configuration*
---

### D581 — Sortie : convergence des lignes ; stop sous le plus bas de la fractale baissière
🟢 **FAIT VÉRIFIÉ** (Source : alligator.md) : « consider exiting your position when the lines begin to converge... Bearish fractals can be used to choose an exit point during this phase. Set your stop below the lowest low of the most recent bearish fractal. »
**TRADEX-AI C3** : Gestion de sortie/risque — sortir quand les 3 lignes convergent (retour vers sleeping = tendance qui faiblit) ; placer le stop sous le plus bas low de la fractale baissière la plus récente. Fournit un niveau de stop objectif.
*Catégorie : gestion_risque_entree*
---

### D582 — Paramétrage par défaut SharpCharts/ACP : 13,8,8,5,5,3 + option FRACTALS
🟡 **CONVENTION** (Source : alligator.md, image_05) : « The default settings for this overlay are 13,8,8,5,5,3. These lines represent the number of periods used in the calculation of each line and the number of periods each line is offset... To add the fractal markers to your chart, add the word FRACTALS as an optional seventh parameter. »
**TRADEX-AI C1** : Convention de configuration de référence (StockCharts) — séquence périodes/offsets 13/8, 8/5, 5/3 ; les fractales sont un module activable séparément. Sert de baseline avant tout réglage adapté aux range bars NT8.
*Catégorie : configuration*
---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie |
|---|----------|-----|--------|-----------|
| D571 | Définition Alligator (3 SMMA Fibo 13/8/5) | 🟢 | C1 | indicateurs_tendance |
| D572 | Prémisse tendances 15–30 % du temps | 🔵 | C1 | structure_marche |
| D573 | Jaw = SMMA13 midpoint offset +8 | 🟢 | C1 | indicateurs_tendance |
| D574 | Teeth = SMMA8 midpoint offset +5 | 🟢 | C1 | indicateurs_tendance |
| D575 | Lips = SMMA5 midpoint offset +3 | 🟢 | C1 | indicateurs_tendance |
| D576 | SMMA plus lisse mais plus retardé que SMA/EMA | 🟢 | C1 | indicateurs_tendance |
| D577 | Fractales 5 barres (bull/bear) | 🟢 | C1 | structure_marche |
| D578 | 3 phases sleeping/awakening/hungry | 🟢 | C1 | signal |
| D579 | Entrée awakening → confirmation hungry | 🟢 | C3 | configuration |
| D580 | Entrée fractale haussière (breakout high) | 🟢 | C3 | configuration |
| D581 | Sortie convergence + stop sous fractale baissière | 🟢 | C3 | gestion_risque_entree |
| D582 | Param défaut 13,8,8,5,5,3 + FRACTALS | 🟡 | C1 | configuration |

**Lien Belkhayate :** NON CONCERNÉ (indicateur Bill Williams indépendant ; ne touche ni aux pivots, ni au BGC, ni à l'Énergie/MFI de la méthode verrouillée).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, non fusionnée dans KNOWLEDGE_BASE_MASTER.json.
