# Extraction StockCharts — Descending Triangle
**Source :** `bundles/stockcharts/descending_triangle.md` (HTTP 200 · ~6 100 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1471 → D1484 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/descending-triangle
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Descending Triangle pattern. | What Is a Descending Triangle? | CERTIFIE (accord .md + HTML) |
| image_02.png | An example of a Descending Triangle chart pattern. | Characteristics of a Descending Triangle | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1471 — Nature du triangle descendant
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md, image_01) : Le triangle descendant est une formation **baissière**. Il se forme généralement durant une tendance baissière et est une figure de continuation, bien que parfois il forme une figure de retournement à la fin d'une tendance haussière. Quel que soit l'endroit où ils se forment, les triangles descendants sont des **figures baissières** indiquant une distribution.
**TRADEX-AI structure_marche** : Figure chartiste baissière candidate pour qualifier une continuation/retournement baissier sur GC/HG/CL/ZW ; couche analytique structurelle, jamais déclencheur d'ordre.
*Catégorie : structure_marche*

---

### D1472 — Géométrie (triangle rectangle)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : En raison de sa forme, la figure peut aussi être appelée triangle à angle droit. Deux plus bas comparables ou plus forment une ligne horizontale en bas. Deux pics déclinants ou plus forment une ligne de tendance descendante au-dessus de l'horizontale, qui converge vers celle-ci en descendant. Si les deux lignes étaient étendues, la trend line descendante agirait comme l'hypoténuse d'un triangle rectangle.
**TRADEX-AI structure_marche** : Définition géométrique précise (horizontale basse + droite descendante convergente) ; détectable par régression sur les pivots hauts/bas.
*Catégorie : structure_marche*

---

### D1473 — Condition de tendance préalable
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Pour qualifier comme figure de continuation, une tendance établie devrait exister. Cependant, parce que le triangle descendant est une figure baissière, la longueur et la durée de la tendance courante sont moins importantes que la robustesse de la formation.
**TRADEX-AI configuration** : La robustesse de la formation prime sur l'ancienneté de la tendance ; critère de pondération à intégrer dans un score de qualité de figure.
*Catégorie : configuration*

---

### D1474 — Ligne horizontale basse (support)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Au moins deux reaction lows sont requis pour former la ligne horizontale basse. Les plus bas n'ont pas à être exacts mais doivent être raisonnablement proches. Il devrait y avoir une certaine distance séparant les plus bas, avec un reaction high entre eux.
**TRADEX-AI structure_marche** : Critère de détection du support (≥ 2 plus bas proches espacés) ; tolérance non-stricte sur l'alignement — codable avec une bande de tolérance.
*Catégorie : configuration*

---

### D1475 — Ligne de tendance descendante haute (résistance)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Au moins deux reaction highs sont requis pour former la trend line descendante haute. Ces reaction highs doivent être successivement plus bas, avec une distance entre eux. Si un reaction high plus récent égale ou dépasse le précédent, alors le triangle descendant est **invalide**.
**TRADEX-AI structure_marche** : Condition d'invalidation explicite (un plus haut ≥ au précédent casse la figure) ; règle de rejet déterministe essentielle.
*Catégorie : configuration*

---

### D1476 — Durée de la figure
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : La longueur de la figure peut aller de quelques semaines à plusieurs mois, la figure moyenne durant d'un à trois mois.
**TRADEX-AI structure_marche** : Borne temporelle indicative ; à transposer selon le timeframe Belkhayate (15min / Range Bar) plutôt que copier les durées en semaines/mois.
*Catégorie : configuration*

---

### D1477 — Comportement du volume
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : À mesure que la figure se développe, le volume se contracte généralement. Mais lors du break baissier, idéalement il devrait y avoir une expansion de volume pour confirmer la figure. La confirmation par le volume n'est pas nécessaire mais préférée.
**TRADEX-AI structure_marche** : Contraction de volume pendant la formation + expansion au break = signature volumétrique ; mappable sur les données order-flow ATAS comme confirmation.
*Catégorie : signal*

---

### D1478 — Retour au breakout (support→résistance)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Principe de base de l'analyse technique : un support cassé devient résistance et vice-versa. Quand la ligne de support horizontale du triangle descendant est cassée, elle devient résistance. Parfois il y aura un retour à ce niveau de résistance renouvelée avant que le mouvement baissier ne commence vraiment.
**TRADEX-AI structure_marche** : Phénomène de polarité support/résistance ; le pullback de retest offre un point d'entrée short à risque défini.
*Catégorie : configuration*

---

### D1479 — Calcul de l'objectif de prix (target)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Une fois le breakout survenu, la projection de prix se trouve en mesurant la plus grande distance de la figure et en la soustrayant du breakout du support.
**TRADEX-AI structure_marche** : Règle de projection déterministe (hauteur max du triangle reportée vers le bas depuis le support cassé) ; utilisable pour pré-calculer un take-profit et le R/R.
*Catégorie : gestion_risque_entree*

---

### D1480 — Biais baissier vs triangle symétrique
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Contrairement au triangle symétrique, le triangle descendant a un biais **baissier** défini avant le break réel. Le triangle symétrique est une formation neutre qui dépend du breakout imminent pour dicter la direction. La ligne horizontale représente une demande empêchant le titre de décliner sous un certain niveau (comme un gros ordre d'achat en exécution lente), mais les reaction highs continuent de décliner — ces plus bas plus hauts indiquent une pression vendeuse accrue donnant le biais baissier.
**TRADEX-AI structure_marche** : Distinction directionnelle clé (biais baissier pré-établi vs neutralité du symétrique) ; permet d'anticiper la direction avant la cassure, contrairement au symétrique.
*Catégorie : structure_marche*

---

### D1481 — Exemple NUE : contexte et formation
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md, image_02) : Nucor Corp. (NUE) — après un plus haut plus bas juste sous 60 $ en décembre 1999, NUE a formé un triangle descendant début 2000. Le titre a décliné de plus de 60 $ vers les bas 40 $, trouvé un support et monté un rallye de réaction qui a calé juste sous 50 $, démarrant une série de reaction highs plus bas. La tendance long-terme était baissière → figure classée comme continuation.
**TRADEX-AI structure_marche** : Illustration empirique d'un triangle descendant de continuation en tendance baissière ; sert d'exemple de calibration visuelle.
*Catégorie : configuration*

---

### D1482 — Exemple NUE : support et trend line
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md, image_02) : Le support à 45 $ fut d'abord établi par un rebond en février ; le titre a touché ce niveau deux fois avant de casser. Après le second touch en mars, la ligne de support basse fut tracée. Après chaque rebond sur le support, un plus haut plus bas s'est formé : les reaction highs aux points 2, 4 et 6 ont formé la trend line descendante. La figure n'est pas complète tant que le support n'est pas cassé (« potentiel » avant cassure). Durée : un peu moins de trois mois.
**TRADEX-AI structure_marche** : Démonstration de la construction progressive (support + 3 pics déclinants) et du caractère « potentiel » avant validation par cassure — la figure n'existe qu'une fois le support rompu.
*Catégorie : configuration*

---

### D1483 — Exemple NUE : cassure et confirmation
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Le dernier touch du support à 45 $ a eu lieu fin avril ; le titre a spiké sous le support mais clôturé au-dessus. La cassure finale est survenue quelques jours plus tard avec un gap down, une grande bougie noire et une expansion de volume (le volume a bondi au plus haut depuis des mois, money flows sous -10 %). Cassure « convaincante » et non « légère ». Projection : déclin initial de 9 points (54-45) soustrait du support à 45 → cible ~36 $ (atteinte fin juin).
**TRADEX-AI structure_marche** : Faisceau de confirmation (gap + grande bougie + volume record + money flow < -10 %) et application concrète du calcul de target ; modèle de multi-confirmation transposable à la grille /10.
*Catégorie : signal*

---

### D1484 — Protocole de trading et limites du target (FAQ + Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : descending_triangle.md) : Une fois la figure confirmée par un breakout (idéalement avec hausse de volume), cela peut signaler de vendre/shorter le titre. La cible (plus grande distance soustraite du support) est une ligne directrice, pas absolue — utiliser d'autres outils d'AT pour décider quand couvrir un short ou acheter. Le triangle descendant porte un biais baissier distinct, contrairement au symétrique neutre jusqu'à la cassure.
**TRADEX-AI structure_marche** : Règle d'entrée explicite (attendre la cassure confirmée + volume avant short) ; cible traitée comme guide non-absolu — cohérent avec l'exigence projet de confirmation et de R/R ≥ 1:2.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1471 → D1484 (14 décisions) |
| Images certifiées | 2/2 |
| Catégories couvertes | structure_marche · configuration · signal · gestion_risque_entree |
| Cercle dominant | structure_marche (figure chartiste) |
| Lien Belkhayate | NON CONCERNÉ (figure d'analyse technique classique, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées ; règle d'invalidation D1475 (plus haut ≥ précédent) à coder strictement |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Figure d'analyse technique classique (StockCharts ChartSchool), aucun rapport affirmé avec la méthode Belkhayate.
