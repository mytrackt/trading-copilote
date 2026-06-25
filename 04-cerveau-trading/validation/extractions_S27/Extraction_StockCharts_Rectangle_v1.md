# Extraction StockCharts — Rectangle (Trading Range)
**Source :** `bundles/stockcharts/rectangle.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D3371 → D3382 · **Page :** chartschool.stockcharts.com/.../chart-patterns/rectangle
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Exemple de Rectangle | Rectangle | D3371 |
| image_02 | Rectangle dans Micron (MU) | Rectangle | D3380 |

## DÉCISIONS

### D3371 — Rectangle : définition
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md, image_01) : Pattern de **continuation** se formant durant une pause de tendance. Identifiable par deux plus-hauts comparables et deux plus-bas comparables reliés en deux lignes parallèles (sommet/base). Aussi appelé trading range, zone de consolidation ou congestion.
**TRADEX-AI C1** : Range délimité par S/R horizontaux, codable sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D3372 — Pattern neutre jusqu'à la cassure
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Comme le triangle symétrique, le rectangle est incomplet jusqu'à la cassure ; la direction n'est généralement PAS déterminable à l'avance (biais neutre).
**TRADEX-AI C3** : Ne pas anticiper la direction ; attendre la cassure confirmée.
*Catégorie : structure_marche*

### D3373 — Tendance préalable
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Pour qualifier en continuation, une tendance préalable doit exister (idéalement quelques mois, pas trop mature). Plus la tendance est mature, moins la continuation est probable.
**TRADEX-AI C1** : Filtrer par existence + maturité de la tendance amont.
*Catégorie : structure_marche*

### D3374 — Quatre points
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Au moins 2 plus-hauts de réaction équivalents (résistance) et 2 plus-bas équivalents (support), raisonnablement proches (pas exactement égaux). Alternance highs/lows préférable.
**TRADEX-AI C1** : Détection = 2 touches min sur chaque borne.
*Catégorie : structure_marche*

### D3375 — Volume non standard
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Contrairement aux triangles symétriques, les rectangles n'ont pas de profil volume standard. Le volume peut décliner ou être choppy ; rarement croissant à maturité. Si le volume décline, chercher une expansion à la cassure pour confirmation.
**TRADEX-AI C2** : Évaluer le volume directionnel (vers résistance vs support) pour anticiper la cassure.
*Catégorie : signal*

### D3376 — Durée
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Quelques semaines à plusieurs mois ; < 3 semaines = plutôt un flag. Idéalement ~3 mois. Plus le pattern est long, plus la cassure est significative.
**TRADEX-AI C1** : Pondérer le signal par la durée (3 mois → cible atteinte, 6 mois → cible dépassée).
*Catégorie : structure_marche*

### D3377 — Confirmation de cassure
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Cassure valide = sur base de clôture. Certains appliquent un filtre prix (3 %), temps (3 jours) ou volume (expansion) pour confirmer.
**TRADEX-AI C3** : Exiger clôture hors range + filtre (3 %/3 jours/volume).
*Catégorie : gestion_risque_entree*

### D3378 — Retour au breakout
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Le support cassé devient résistance potentielle (et inverse). Après cassure, retour fréquent vers le niveau = seconde occasion d'entrée.
**TRADEX-AI C3** : Le pullback vers la cassure = point d'entrée secondaire (à confirmer).
*Catégorie : gestion_risque_entree*

### D3379 — Cible = hauteur du rectangle
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Mouvement estimé = mesurer la hauteur du rectangle et l'appliquer au point de cassure.
**TRADEX-AI C1** : Objectif projeté = hauteur du range reportée depuis la cassure.
*Catégorie : structure_marche*

### D3380 — Exemple MU : CMF confirme la cassure
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md, image_02) : Exemple Micron — durant la baisse de 38 à 31 $, le Chaikin Money Flow n'est pas passé sous -10 % puis est devenu positif (CMF +20 % au franchissement) ; cassure avec forte expansion de volume.
**TRADEX-AI C2** : Confluence volume (CMF) + cassure de range augmente la fiabilité.
*Catégorie : signal*

### D3381 — Range = combat bulls/bears
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Le rectangle oppose acheteurs (achètent près du support) et vendeurs (vendent près de la résistance) ; un groupe finit par s'épuiser, le vainqueur émerge à la cassure. Possible de scalper les rebonds support→résistance.
**TRADEX-AI C1** : Stratégie range (acheter support/vendre résistance) tant qu'aucune cassure.
*Catégorie : signal*

### D3382 — Cible ordinaire parfois inutile
🟢 **FAIT VÉRIFIÉ** (Source : rectangle.md) : Si la cassure est exceptionnelle (durée, force, expansion de volume, nouveaux plus-hauts), une cible « ordinaire » (hauteur) peut être inutile (MU a largement dépassé l'objectif).
**TRADEX-AI C3** : Ne pas plafonner la sortie sur la cible mesurée si la cassure est puissante.
*Catégorie : gestion_risque_entree*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3371 → D3382 (12) |
| Images citées | 2/2 |
| Catégories | structure_marche · signal · gestion_risque_entree |
| Tags | 🟢 FAIT VÉRIFIÉ |
| Belkhayate | NON CONCERNÉ |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
