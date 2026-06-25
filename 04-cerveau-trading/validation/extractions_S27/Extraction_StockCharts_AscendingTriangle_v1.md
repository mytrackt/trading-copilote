# Extraction StockCharts — Ascending Triangle
**Source :** `bundles/stockcharts/ascending_triangle.md` (HTTP 200 · ~6 100 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D731 → D742 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/ascending-triangle
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of an Ascending Triangle chart pattern. | What Is an Ascending Triangle Pattern? | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of Ascending Triangle pattern in Primus Telecom. | Is an Ascending Triangle Bullish? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D731 — Nature : figure haussière de continuation indiquant l'accumulation
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : « The ascending triangle is a bullish formation that usually forms as a continuation pattern during an uptrend. » Il peut parfois se former en figure de retournement à la fin d'une tendance baissière, mais c'est typiquement une continuation. « Regardless of where they form, ascending triangles are bullish patterns that indicate accumulation. »
**TRADEX-AI C1** : Figure de continuation haussière candidate ; biais directionnel à intégrer comme configuration analytique, jamais comme ordre automatique.
*Catégorie : configuration*

---

### D732 — Géométrie : ligne horizontale haute + trend line ascendante (triangle rectangle)
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md, image_01) : À cause de sa forme, la figure est aussi appelée triangle rectangle. Deux plus hauts égaux (ou plus) forment une ligne horizontale au sommet ; deux creux montants (ou plus) forment une ligne de tendance ascendante qui converge vers l'horizontale en montant. Étendues vers la droite, la trend line ascendante jouerait l'hypoténuse d'un triangle rectangle.
**TRADEX-AI C1** : Définition géométrique déterministe (résistance plate + supports montants) détectable algorithmiquement par régression sur sommets/creux.
*Catégorie : structure_marche*

---

### D733 — Tendance préalable requise mais robustesse de la figure prime
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : « To qualify as a continuation pattern, an established trend should exist. However, because the ascending triangle is a bullish pattern, the length and duration of the current trend are not as important as the robustness of the formation, which is paramount. »
**TRADEX-AI C1** : Le critère de qualité = robustesse de la formation (pas la durée de la tendance) ; à pondérer dans un score de fiabilité de figure.
*Catégorie : configuration*

---

### D734 — Ligne horizontale haute : ≥ 2 reaction highs proches
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : Au moins 2 reaction highs sont requis pour former la ligne horizontale supérieure. Les sommets n'ont pas à être exacts mais doivent rester raisonnablement proches, avec une certaine distance entre eux et un reaction low entre eux.
**TRADEX-AI C1** : Condition de détection (≥2 sommets quasi-égaux séparés par un creux) codable comme garde-fou de validité de la résistance.
*Catégorie : structure_marche*

---

### D735 — Trend line basse : ≥ 2 reaction lows successivement plus hauts (critère d'invalidation)
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : Au moins deux reaction lows sont requis pour la trend line ascendante ; ils doivent être successivement plus hauts, avec une certaine distance entre eux. « ***If a more recent reaction low is equal to or less than the previous reaction low, then the ascending triangle is not valid***. »
**TRADEX-AI C1** : Règle d'invalidation NETTE et déterministe : tout nouveau creux ≤ creux précédent annule la figure — codable directement comme test booléen.
*Catégorie : structure_marche*

---

### D736 — Durée typique : quelques semaines à plusieurs mois (moyenne 1-3 mois)
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : « The pattern length can range from a few weeks to many months, with the average pattern lasting from one to three months. »
**TRADEX-AI C1** : Fenêtre temporelle de détection à adapter au timeframe ; valeur de référence pour borner la recherche de figure.
*Catégorie : timing*

---

### D737 — Volume : contraction durant la formation, expansion à la cassure (préférée, non obligatoire)
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : « As the pattern develops, volume usually contracts. When the upside breakout occurs, there should be an expansion of volume to confirm the breakout. While volume confirmation is ***preferred***, it is not always necessary. »
**TRADEX-AI C2** : Confirmation par expansion de volume à la cassure = filtre order flow (ATAS) ; préférée mais pas éliminatoire selon la source.
*Catégorie : signal*

---

### D738 — Retour au point de cassure : résistance devient support
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : Principe de base de l'AT : la résistance devient support et inversement. Quand la ligne de résistance horizontale est cassée, elle devient support. Il y a parfois un retour vers ce niveau de support avant que le mouvement ne démarre.
**TRADEX-AI C1** : Logique de retest (résistance cassée → support) exploitable comme zone d'entrée secondaire et de placement de stop.
*Catégorie : configuration*

---

### D739 — Objectif de prix : largeur maximale de la figure projetée depuis la cassure
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : Une fois la cassure survenue, la projection de prix s'obtient en mesurant la distance la plus large de la figure et en l'appliquant à la cassure de résistance.
**TRADEX-AI C1** : Calcul de cible déterministe (cible = niveau de cassure + hauteur max de la figure) ; utile pour estimer le R/R requis (≥ 1:2).
*Catégorie : gestion_risque_entree*

---

### D740 — Biais haussier intrinsèque vs triangle symétrique (offre/demande)
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md, image_02) : Contrairement au triangle symétrique (formation neutre dont la direction dépend de la cassure), l'ascending triangle a un biais haussier défini AVANT la cassure réelle. La ligne horizontale représente une offre excédentaire (overhead supply) bloquant le titre à un niveau, comme un gros ordre de vente en cours d'exécution sur plusieurs semaines/mois ; les creux montants traduisent une pression acheteuse croissante, d'où le biais haussier.
**TRADEX-AI C2** : Lecture offre/demande (gros vendeur passif au plafond vs acheteurs de plus en plus agressifs) recoupe la logique order flow ; le biais haussier pré-cassure distingue l'AT du triangle symétrique.
*Catégorie : structure_marche*

---

### D741 — Exemple Primus Telecom (PRTL) : figure 6 mois, cassure avec expansion de volume
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md, image_02) : PRTL a formé un ascending triangle sur ~6 mois avant de casser la résistance avec expansion de volume. Résistance multiple touchée vers 23-24 (rebonds ≥3 fois en 5 mois) ; creux progressivement plus hauts formant la trend line. Cassure de 24 début novembre avec volume au-dessus de la moyenne 7 des 10 jours autour de la cassure (les 7 étant des jours haussiers). Support retrouvé au-dessus de l'ancienne résistance = force sous-jacente.
**TRADEX-AI C1** : Cas pédagogique confirmant la séquence contraction → cassure volume → retest ; valeur illustrative, aucun paramètre nouveau.
*Catégorie : configuration*

---

### D742 — Cible atteinte et caractère indicatif des projections
🟢 **FAIT VÉRIFIÉ** (Source : ascending_triangle.md) : Sur PRTL, l'avance projetée était de 10 points (24 - 14 = 10) depuis la cassure à 24, soit une cible de 34, atteinte en 2 mois (le titre est ensuite monté à 50). « Targets are only meant to be used as guidelines, and other aspects of technical analysis should also be employed for deciding when to sell. » Les FAQ confirment : figure utilisable sur divers timeframes (plus le timeframe est grand, plus la figure est significative) ; fiable surtout en uptrend confirmé avec volume élevé, mais non infaillible.
**TRADEX-AI C1** : La cible est une borne indicative, pas un take-profit dur ; à combiner avec d'autres outils (cohérent avec la prudence du projet sur les signaux isolés).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D731 | Figure haussière de continuation (accumulation) | 🟢 | C1 | configuration |
| D732 | Géométrie horizontale + trend line ascendante | 🟢 | C1 | structure_marche |
| D733 | Tendance préalable mais robustesse prime | 🟢 | C1 | configuration |
| D734 | ≥ 2 reaction highs proches | 🟢 | C1 | structure_marche |
| D735 | ≥ 2 lows montants (critère d'invalidation) | 🟢 | C1 | structure_marche |
| D736 | Durée typique 1-3 mois | 🟢 | C1 | timing |
| D737 | Volume : contraction puis expansion à la cassure | 🟢 | C2 | signal |
| D738 | Retest : résistance devient support | 🟢 | C1 | configuration |
| D739 | Cible = largeur max projetée | 🟢 | C1 | gestion_risque_entree |
| D740 | Biais haussier intrinsèque (offre/demande) | 🟢 | C2 | structure_marche |
| D741 | Exemple Primus Telecom (PRTL) | 🟢 | C1 | configuration |
| D742 | Cible indicative, pas TP dur | 🟢 | C1 | gestion_risque_entree |

**Liens Belkhayate :** L'ascending triangle est une figure chartiste classique (StockCharts), PAS un élément de la méthode Belkhayate (⚫). Lien indirect possible : la zone de cassure et le retest recoupent l'usage des pivots/zones comme niveaux opératoires, mais l'attribuer à Belkhayate serait « hypothèse projet, non affirmée par la source » (⚫🔴). Sinon NON CONCERNÉ.

**À vérifier (humain) :**
- D741/D742 — chiffres PRTL (24, 14, cible 34, montée à 50) : valeurs historiques illustratives propres à l'exemple, non transposables comme paramètres.
- D737 — confirmation volume « préférée mais pas nécessaire » : à arbitrer si TRADEX en fait un critère éliminatoire ou un simple bonus de score.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
