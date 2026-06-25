# Extraction SierraChart — Point and Figure Box Count
**Source :** `bundles/sierrachart/sierra_408_point_figure_box_count.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9311 → D9313 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=408
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : comptage des boîtes P&F par barre — indicateur structure de marché C1, exclusivement sur barres Point & Figure.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9311 — Définition et rôle du Box Count P&F
🟢 **FAIT VÉRIFIÉ** (Source : sierra_408_point_figure_box_count.md) : Cette étude affiche en sous-graphique le nombre de boîtes (boxes) pour chaque barre d'un graphique Point and Figure. Le Box Count représente l'amplitude du mouvement de prix en unités de boîtes P&F pour chaque colonne X (hausse) ou O (baisse).
**TRADEX-AI C1** : Le Box Count P&F mesure la force relative de chaque mouvement directionnel sans référence au temps — compatible avec l'approche Belkhayate de filtrage du bruit temporel. Sur GC (or), un Box Count élevé sur une colonne X (>=3 boîtes) confirme une poussée haussière significative.
*Catégorie : structure_marche*

### D9312 — Contrainte de Bar Period Type
🟢 **FAIT VÉRIFIÉ** (Source : sierra_408_point_figure_box_count.md) : L'étude n'est significative QUE lorsque le Bar Period Type est configuré sur Point and Figure Bar. Sur tout autre type de barre (time-based, tick, volume, range), l'étude produit des résultats non interprétables.
**TRADEX-AI C1** : Dans TRADEX-AI, les barres NT8 sont de type Range Bar (méthode Belkhayate). Le Point and Figure Box Count est donc inapplicable directement sur le flux NT8 principal. Usage limité à l'analyse P&F complémentaire dans Sierra Chart — ne pas intégrer dans data_reader.py pour le moteur de signal temps réel.
*Catégorie : structure_marche*

### D9313 — Absence d'inputs configurables
🟢 **FAIT VÉRIFIÉ** (Source : sierra_408_point_figure_box_count.md) : Cette étude n'a aucun paramètre d'entrée utilisateur. Le Box Count est calculé automatiquement à partir de la structure P&F du graphique (taille de boîte et nombre de reversal définis au niveau du chart, pas de l'étude).
**TRADEX-AI C1** : La taille de boîte (box size) et le reversal count sont des paramètres du graphique P&F sous-jacent, non de l'étude. Pour GC, une box size de 1 point et 3-box reversal est standard — mais ces valeurs se configurent dans le Bar Period Settings de Sierra Chart, pas dans cette étude.
*Catégorie : structure_marche*
