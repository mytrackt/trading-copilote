# Extraction StockCharts — Rising Wedge (biseau ascendant)
**Source :** `bundles/stockcharts/rising_wedge.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D3471 → D3480 · **Page :** chartschool.stockcharts.com/.../chart-patterns/rising-wedge
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Exemple de Rising Wedge | Rising Wedge | D3471 |
| image_02 | Rising Wedge dans ANN | Rising Wedge | D3478 |

## DÉCISIONS

### D3471 — Rising Wedge : définition et biais
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md, image_01) : Pattern **baissier** qui débute large en bas et se contracte à mesure que les prix montent et que le range se resserre. Contrairement au triangle symétrique (sans pente/biais), le rising wedge pente vers le haut avec un biais baissier.
**TRADEX-AI C1** : Pattern à biais baissier malgré la pente haussière, codable sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D3472 — Reversal OU continuation, toujours baissier
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : En continuation, le wedge pente vers le haut contre un downtrend dominant ; en reversal, il pente avec la tendance. **Quel que soit le type, le rising wedge est baissier.**
**TRADEX-AI C3** : Toujours interpréter comme signal baissier (à confirmer).
*Catégorie : structure_marche*

### D3473 — Tendance préalable
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Pour qualifier en reversal, une tendance préalable à inverser doit exister. Se forme typiquement sur 3-6 mois ; peut marquer un retournement intermédiaire ou long terme.
**TRADEX-AI C1** : Filtrer par durée (3-6 mois) et contexte de tendance.
*Catégorie : structure_marche*

### D3474 — Ligne de résistance supérieure
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Au moins 2 plus-hauts de réaction (idéalement 3) pour la résistance supérieure ; chaque plus-haut supérieur au précédent.
**TRADEX-AI C1** : Détection = ≥2 plus-hauts montants.
*Catégorie : structure_marche*

### D3475 — Ligne de support inférieure
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Au moins 2 plus-bas de réaction pour le support inférieur ; chaque plus-bas supérieur au précédent.
**TRADEX-AI C1** : Détection = ≥2 plus-bas montants.
*Catégorie : structure_marche*

### D3476 — Contraction (clé du biais baissier)
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Les deux lignes convergent ; les avancées depuis les plus-bas deviennent de plus en plus courtes (rallyes peu convaincants). La résistance supérieure ne suit pas la pente du support → supply overhang.
**TRADEX-AI C1** : La pente résistance < pente support = signal d'affaiblissement du momentum.
*Catégorie : signal*

### D3477 — Cassure de support = confirmation
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Confirmation baissière seulement quand le support est cassé de façon convaincante (prudent d'attendre la cassure du plus-bas de réaction précédent). Possible reaction rally pour tester la nouvelle résistance.
**TRADEX-AI C3** : Exiger cassure confirmée du support avant le signal baissier.
*Catégorie : gestion_risque_entree*

### D3478 — Volume + exemple ANN (CMF)
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md, image_02) : Idéalement le volume décline pendant que les prix montent ; expansion de volume à la cassure = confirmation baissière. Exemple ANN — CMF négatif fin avril, bien sous -10 % à la cassure du support.
**TRADEX-AI C2** : Confluence CMF/volume + cassure renforce le signal.
*Catégorie : signal*

### D3479 — Difficulté de reconnaissance
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Un des patterns les plus difficiles à reconnaître/trader : c'est une consolidation, mais la perte de momentum à chaque plus-haut donne le biais baissier, alors que la série de plus-hauts/plus-bas montants garde la tendance intrinsèquement haussière. La cassure finale du support indique la victoire de l'offre.
**TRADEX-AI C3** : Garde — ambiguïté élevée, exiger confirmation forte (mode Manuel).
*Catégorie : gestion_risque_entree*

### D3480 — Pas de technique de mesure de cible
🟢 **FAIT VÉRIFIÉ** (Source : rising_wedge.md) : Il n'existe **aucune technique de mesure** pour estimer le déclin — utiliser d'autres aspects de l'analyse technique pour les objectifs.
**TRADEX-AI C1** : Pas d'objectif mécanique ; dériver la cible d'autres niveaux (S/R, pivots).
*Catégorie : structure_marche*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3471 → D3480 (10) |
| Images citées | 2/2 |
| Catégories | structure_marche · signal · gestion_risque_entree |
| Tags | 🟢 FAIT VÉRIFIÉ |
| Belkhayate | NON CONCERNÉ |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
