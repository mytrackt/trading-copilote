# Extraction StockCharts — Advance-Decline Volume Percent

**Source :** `bundles/stockcharts/advance_decline_volume_percent.md` (HTTP 200 · ~8 700 car.) + 5 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D551 → D560 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-volume-percent
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | How Do You Calculate Advance-Decline Volume Percent? | How Do You Calculate… [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | AD Volume Line | AD Volume Line [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Moving Averages | Moving Averages [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | SharpCharts | SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | SharpCharts | SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D551 — Nature de l'indicateur : breadth de volume
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md) : « Advance-Decline Volume Percent is a breadth indicator designed to measure the percentage of Net Advancing Volume. » Il sert de fondation à un oscillateur de breadth ou à l'AD Volume Line, et complète l'analyse du titre sous-jacent (ex. le SPDR XLY).
**TRADEX-AI C5/C7** : indicateur de largeur de marché (breadth) sur un panier d'actions/secteur. Pertinence DIRECTE futures GC/HG/CL/ZW = très limitée : ce sont des contrats uniques, pas des paniers. Usage possible UNIQUEMENT en confirmation indirecte via ES (S&P 500) — sentiment marché actions.
*Catégorie : structure_marche*

---

### D552 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_01) : `AD Volume Percent = (Advancing Volume Less Declining Volume) / Total Volume`. Exemples chiffrés : (36m – 5m)/41m = +75,60 % ; (7m – 36m)/43m = -67,44 %.
**TRADEX-AI C5** : formule déterministe, bornée [-100 % ; +100 %], zéro = ligne médiane. Reproductible si l'on dispose des volumes advancing/declining d'un indice. Note : requiert un panier (constituants d'indice) — NON applicable à un futur isolé GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D553 — Bornes et lecture extrême
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_01) : « AD Volume Percent fluctuates between -100% and +100% with zero as the middle line. A +100% reading means all volume went to advancing stocks… A -100% reading means all volume went to declining stocks. Extreme readings are the exception rather than the norm. »
**TRADEX-AI C5** : +100 % = totalité du volume sur titres en hausse ; -100 % = totalité sur titres en baisse. Les extrêmes sont rares. Pertinence futures limitée (mesure interne d'un panier actions).
*Catégorie : structure_marche*

---

### D554 — Seuils de pression acheteuse/vendeuse (±70 %)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md) : « An advance with AD Volume Percent exceeding 70% shows strong buying pressure… a decline with AD Volume Percent dipping below -70% reflects strong selling pressure. »
**TRADEX-AI C5** : seuils littéraux >+70 % = forte pression acheteuse, <-70 % = forte pression vendeuse, comme proxy de money flow. Convention StockCharts. Note pertinence limitée futures : exploitable seulement sur ES comme filtre de sentiment actions, jamais comme signal direct GC/HG/CL/ZW.
*Catégorie : signal*

---

### D555 — Données brutes choppy : comparer jours +/-
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md) : « The raw data fluctuates with the up and down days, creating a rather choppy-looking chart. Nevertheless, chartists can compare the positive and negative days to assess buying and selling pressure. » Une moyenne mobile peut en faire un oscillateur ; une AD Volume Line peut servir à la tendance et aux divergences.
**TRADEX-AI C5** : la série brute est bruitée (histogramme jour par jour) ; lissage requis pour exploitation. Note : applicable à des indices/paniers actions seulement.
*Catégorie : indicateurs_tendance*

---

### D556 — AD Volume Line (cumul) et divergences
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_02) : l'AD Volume Line est la mesure cumulée de l'AD Volume Percent (ex. $XLKUDP) ; elle monte quand le pourcentage est positif, baisse quand il est négatif. L'échelle de droite n'a pas d'importance (dépend de la date de départ) ; se concentrer sur les mouvements de ligne.
**TRADEX-AI C7** : ligne cumulative type AD Line, lecture par mouvements (pas par valeurs absolues). Outil de détection de divergences breadth/prix. Pertinence futures indirecte (panier actions → ES).
*Catégorie : indicateurs_tendance*

---

### D557 — Divergences breadth/prix (exemples XLK)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_02) : divergence baissière août-septembre (XLK nouveau plus haut en septembre, AD Volume Line plus bas plus haut = pression acheteuse plus faible) ; divergence haussière avril (XLK casse son plus bas début avril, AD Volume Line forme un plus bas plus haut = pression vendeuse faible, prélude au rebond).
**TRADEX-AI C7** : la divergence breadth précède parfois le retournement de prix (« changes sometimes occur on the inside first »). Méthode de confirmation/anticipation. Note pertinence limitée futures : transposable conceptuellement mais l'instrument reste un panier actions.
*Catégorie : signal*

---

### D558 — Oscillateur par moyenne mobile (seuils ±5 %)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_03) : une moyenne mobile (ex. SMA 21 jours sur $XLYUDP, plot brut rendu invisible) crée un oscillateur autour de zéro. Lignes horizontales à +5 %, 0 %, -5 %. Les croisements de la ligne zéro sont sujets aux whipsaws ; mieux vaut des seuils légèrement au-dessus/dessous : >+5 % = haussier, <-5 % = baissier.
**TRADEX-AI C5** : utiliser des seuils décalés (±5 %) plutôt que le croisement de zéro pour réduire les faux signaux. « All oscillator systems will produce their share of whipsaws and bad signals. » Note futures : applicable seulement aux paniers/indices actions (proxy ES).
*Catégorie : signal*

---

### D559 — Construction SharpChart (histogramme / invisible / cumulative)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md, image_04, image_05) : données brutes en « histogram » (rouge) ; oscillateur de breadth via type « invisible » + moyenne mobile en Overlays (la MM devient le tracé principal) ; AD Volume Line via type « cumulative » (noir). Symbole AD Volume Percent ajoutable à tout SharpChart.
**TRADEX-AI** : détails d'implémentation plateforme StockCharts (3 modes de tracé). Valeur documentaire pour reproduire l'indicateur ; non transposable tel quel hors StockCharts. Pertinence futures limitée.
*Catégorie : indicateurs_tendance*

---

### D560 — Synthèse interne vs externe + liste de symboles
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_percent.md) : « The underlying security price reflects what is happening on the outside. AD Volume Percent for XLK ($XLKUDP) shows what is happening on the inside. » StockCharts calcule l'indicateur après clôture pour les neuf SPDR sectoriels et plusieurs indices ; symboles type $XLKUDP / $XLYUDP. Les constituants des paniers changent dans le temps (prudence sur le long terme).
**TRADEX-AI C7** : le breadth = vue « interne » du panier, complémentaire du prix « externe ». Couverture = secteurs SPDR + indices US (actions). Note pertinence limitée futures : AUCUN symbole GC/HG/CL/ZW ; au mieux exploitable via secteurs/indices liés (énergie XLE pour CL, matériaux XLB pour HG, mais lien indirect, NON confirmé par la source).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D551 → D560 (10) |
| Indicateur | Advance-Decline Volume Percent (breadth de volume) |
| Formule | (Vol. avançant − Vol. déclinant) / Vol. total · borné [-100 %; +100 %] |
| Seuils clés | ±70 % (pression forte) · oscillateur MM ±5 % (réduction whipsaws) |
| Dérivés | AD Volume Line (cumulatif) · oscillateur MM (ex. SMA 21j) |
| Usage | Divergences breadth/prix · pression acheteuse/vendeuse interne |
| Cercles | C5 (sentiment/money flow) · C7 (corrélations/divergences) |
| Couverture native | 9 SPDR sectoriels + indices US (actions uniquement) |
| Pertinence futures GC/HG/CL/ZW | TRÈS LIMITÉE — instrument = panier actions ; usage indirect via ES seulement |
| Images | 5/5 certifiées |
| Belkhayate | NON CONCERNÉ (breadth actions, hors méthode Belkhayate) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Indicateur conçu pour des paniers d'actions/indices — sa transposition aux futures TRADING (GC/HG/CL/ZW) n'est PAS supportée par la source et ne doit servir, au mieux, que de signal de confirmation indirect via ES (C2/C5).
