# Extraction StockCharts — Fibonacci Arcs

**Source :** `bundles/stockcharts/fibonacci_arcs.md` (HTTP 200 · ~9 600 car.) + 9 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 9/9 certifiées
**Décisions :** D1731 → D1750 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-arcs
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | Fibonacci Arcs with a Base Line from trough to peak. | How Do You Calculate Fibonacci Arcs? | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart displaying Fibonacci Retracements and Fibonacci Arcs. | How Do You Interpret Fibonacci Arcs? | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart of NVDA with two Fibonacci Arcs. | Support Example | CERTIFIE (accord .md + HTML) |
| image_04.png | After bouncing off the 38% arc in mid-May, the stock reversed… | Support Example | CERTIFIE (accord .md + HTML) |
| image_05.png | The stock hit resistance at the 62% Fibonacci arc (orange box)… | Resistance Example | CERTIFIE (accord .md + HTML) |
| image_06.png | The stock price hit resistance at the 62% Fibonacci Arc and… | Resistance Example | CERTIFIE (accord .md + HTML) |
| image_07.png | Adding extra bars to your chart will help project support and… | Extending the Dateline | CERTIFIE (accord .md + HTML) |
| image_08.png | Extra Bars setting for SharpCharts | Extending the Dateline | CERTIFIE (accord .md + HTML) |
| image_09.png | Chart with Fibonacci Arcs applied using the Annotation tool… | SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1731 — Définition des Fibonacci Arcs (demi-cercles support/résistance)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « Fibonacci Arcs are half circles that extend out from a trend line. » Ils identifient des niveaux de support et de résistance dans un marché changeant en incorporant une composante temps (« incorporating a time component »).
**TRADEX-AI C1** : Outil de structure de marché projetant des zones S/R dynamiques sur GC·HG·CL·ZW — entre dans le cercle Prix (C1).
*Catégorie : structure_marche*

---

### D1732 — Les trois ratios constitutifs des arcs (0,382 / 0,50 / 0,618)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « The first and third arcs are based on the Fibonacci ratios 0.382 (38.2%) and 0.618 (61.8%), respectively, often rounded to 38% and 62%. The middle arc is set at 0.50 or 50%. »
🔵 ÉCOLE (Fibonacci) : ratios issus de la suite/du nombre d'or, standard de l'école Fibonacci.
⚫🔴 (écho COG 0,618) : convergence de ratio avec le COG Belkhayate (COGParams figés 0,618/1,618), non affirmée par la source — StockCharts ne fait aucun lien avec Belkhayate.
**TRADEX-AI C1** : ratios de zonage S/R candidats pour la grille de structure ; à confronter aux niveaux Belkhayate sans présumer d'équivalence.
*Catégorie : structure_marche*

---

### D1733 — Construction par Base Line trough→peak (après une hausse)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_01) : « After an advance, Fibonacci Arcs are measured using a **Base Line** that extends from trough to peak. Arcs are drawn along this line with radii that measure 0.382, 0.50, and 0.618 of the Base Line. » Ces arcs marquent des zones potentielles de support/retournement au pullback.
**TRADEX-AI C1** : règle de tracé directionnelle (hausse) pour projeter des supports après un mouvement haussier identifié.
*Catégorie : structure_marche*

---

### D1734 — Construction par Base Line peak→trough (après une baisse)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « After a decline, Fibonacci Arcs are used to anticipate resistance or reversal zones for the counter-trend bounce. » La Base Line s'étend alors de pic à creux (pente négative).
**TRADEX-AI C1** : règle symétrique (baisse) pour anticiper des résistances sur un rebond contre-tendance.
*Catégorie : structure_marche*

---

### D1735 — Base du ratio 1,618 / 0,618 dans la suite de Fibonacci
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « A number divided by the previous number approximates 1.618… A number divided by the next highest number approximates .6180… This is the basis for the 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : dérivation mathématique standard de la suite 0,1,1,2,3,5,8,13…
⚫🔴 (écho COG 0,618) : convergence de ratio avec le COG Belkhayate (0,618/1,618), non affirmée par la source.
**TRADEX-AI C1** : trace la provenance des ratios employés ; aucune validation que Belkhayate utilise les arcs.
*Catégorie : structure_marche*

---

### D1736 — Base du ratio 0,382 (38,2 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « A number divided by another two places higher approximates .3820… This is the basis for the 38.2% retracement. Also, note that 1 - .618 = .382 »
🔵 ÉCOLE (Fibonacci) : dérivation standard.
**TRADEX-AI C1** : ratio secondaire de zonage S/R.
*Catégorie : structure_marche*

---

### D1737 — Le nombre d'or (Phi) et son rôle culturel
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « 1.618 refers to the Golden Ratio or Golden Mean, also called Phi. The inverse of 1.618 is .618. »
🔵 ÉCOLE (Fibonacci) : contexte théorique.
⚫🔴 (écho COG 0,618) : le couple Phi/inverse (1,618 et 0,618) recoupe les COGParams figés Belkhayate — écho conceptuel, non affirmé par la source.
**TRADEX-AI C1** : contextualise les constantes ; pas d'implication opérationnelle directe.
*Catégorie : structure_marche*

---

### D1738 — Procédure de calcul : 3 rayons sur la Base Line
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_01) : « Base Line: A line from point A to point B · First Arc: Radius = 0.382 of Base Line · Second Arc: Radius = 0.500 of Base Line · Third Arc: Radius = 0.618 of Base Line ». Trois demi-cercles sont tracés selon ces rayons.
**TRADEX-AI C1** : spécification géométrique reproductible pour un éventuel tracé applicatif des zones S/R.
*Catégorie : structure_marche*

---

### D1739 — Composante temps : arcs vs retracements verticaux
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_02) : « Fibonacci Arcs add a time element to Fibonacci retracements. The Fibonacci Retracements Tool is based on a vertical line… It is only concerned with the price change. In contrast, a Base Line… extends… at an angle dependent on elapsed time. »
**TRADEX-AI C1** : distingue zones statiques (retracements) de zones dynamiques (arcs) ; pertinent pour timing combiné prix/temps.
*Catégorie : timing*

---

### D1740 — Dimension des arcs proportionnelle à l'amplitude prix×temps
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « A big price movement over a long period of time produces a long Base Line with wide arcs. Conversely, a small price change over a short period produces a short Base Line with narrow arcs. »
**TRADEX-AI C1** : la largeur des zones S/R dépend de l'amplitude du swing — paramètre d'échelle à respecter par actif/timeframe.
*Catégorie : structure_marche*

---

### D1741 — Zones dynamiques : supports montants / résistances descendantes
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « Fibonacci Arcs drawn after a decline slowly work their way lower, which denotes falling resistance zones. Fibonacci Arcs drawn after an advance slowly work their way higher, which denotes rising support zones. »
**TRADEX-AI C1** : zones S/R évolutives dans le temps, à réévaluer à chaque barre — différent d'un niveau fixe.
*Catégorie : structure_marche*

---

### D1742 — Exemple support NVDA : rebond entre arcs 50 % et 62 %
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_03) : « NVDA declined sharply from the early May high but reversed course between the 50% and 62% arcs. » Un second jeu d'arcs (creux mai → pic juin), plus court, donne des arcs moins larges ; support trouvé près de l'arc 62 %.
**TRADEX-AI C1** : illustration de zone de retournement entre deux arcs ; usage en confirmation de support.
*Catégorie : signal*

---

### D1743 — Exemple support : rebonds successifs sur arcs 38 % puis 62 %
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_04) : « The stock bounced off the 38% arc in mid-May and then bounced off the 62% arc in early July. » Une seconde opportunité d'entrée est apparue via un flag/breakout en septembre.
**TRADEX-AI C1** : montre l'enchaînement de zones de support comme repères d'entrée échelonnés.
*Catégorie : signal*

---

### D1744 — Exemple résistance DRI : arc 62 % comme plafond confirmé
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_05) : Fibonacci Arcs tracés du pic avril au creux mai (DRI) ; « the stock… hit resistance at the 62% arc in mid-June. After stalling a few days, the stock moved sharply lower with a long black candlestick. » Résistance confirmée par les pics mai–juin.
**TRADEX-AI C1** : zone de résistance confirmée par confluence (arc + structure de prix + bougie). Confluence multi-signaux.
*Catégorie : signal*

---

### D1745 — Exemple résistance PAYX : arc 62 % + rising wedge baissier
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_06) : « the advance hit resistance at the 62% arc. Also, notice that a potentially bearish rising wedge formed. Even though the stock moved outside the 62% arc, this sideways move is not considered a bullish breakout. »
**TRADEX-AI C1** : un débordement latéral hors de l'arc n'est PAS un breakout valide — garde-fou anti-faux signal.
*Catégorie : signal*

---

### D1746 — Extension de la dateline (Extra Bars) pour projeter le futur
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md, image_07, image_08) : Sur SPY, « 60 extra bars added. With these additional bars, you can see how the arcs evolve in the future. This can be done in SharpCharts… entering the number of extension periods in the **Extra Bars** box. »
**TRADEX-AI C1** : nécessité d'extrapoler temporellement les zones pour le forecasting — paramètre de projection. Timing.
*Catégorie : timing*

---

### D1747 — Hypothèse corrective sous-jacente
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « these reversal points assume that the move is corrective in nature. A pullback after an advance is deemed a correction that will find support above the beginning of the advance. A bounce after a decline is deemed a counter-trend rally that will hit resistance below the beginning of the decline. »
**TRADEX-AI C1** : l'outil suppose un contexte de correction (pas de retournement majeur) — condition de validité à vérifier avant usage.
*Catégorie : structure_marche*

---

### D1748 — Avertissement : pas de retournement garanti aux arcs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « **Just because prices approach an arc does not mean they will reverse.** Prices move right through these arcs in many cases. **No indicator is perfect.** »
**TRADEX-AI C3** : exige confirmation par d'autres outils avant tout signal — critère d'élimination des faux positifs (confirmation).
*Catégorie : gestion_risque_entree*

---

### D1749 — Non-autonomie : confirmation obligatoire par d'autres outils
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : « Like all annotation tools, Fibonacci Arcs are not meant as a standalone system… chartists must use other tools to confirm support, resistance, bullish reversals, and bearish reversals. »
**TRADEX-AI C3** : interdiction d'utiliser les arcs seuls pour décider — cohérent avec la règle 3/4 + 2/3 alignés (confirmation requise).
*Catégorie : gestion_risque_entree*

---

### D1750 — Différence opérationnelle arcs vs retracements (synthèse FAQ)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_arcs.md) : FAQ — « While Fibonacci Retracements focus solely on price changes, Fibonacci Arcs incorporate a time element. Arcs are based on an angled Base Line, considering price and time changes. » Pour le support : surveiller un retournement près d'un arc après une hausse ; pour la résistance : après une baisse.
**TRADEX-AI C1** : récapitulatif décisionnel — choisir arcs quand la dimension temps importe, retracements sinon.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1731 → D1750 (20) |
| Images certifiées | 9/9 |
| Tags dominants | 🟢 littéral · 🔵 ÉCOLE Fibonacci · ⚫🔴 écho COG 0,618 (D1732, D1735, D1737) |
| Cercles TRADEX | C1 (structure/S-R) · C3 (confirmation : D1748–D1749) |
| Catégories | structure_marche · signal · timing · gestion_risque_entree |
| Actifs cibles | GC · HG · CL · ZW |
| Cas à vérifier | Aucun (0 image à vérifier, 0 fait NON VÉRIFIÉ) ; ⚫🔴 écho COG = à arbitrer humainement, NE PAS fusionner comme équivalence Belkhayate |

> ⚠️ Outil éducatif (StockCharts ChartSchool) · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
