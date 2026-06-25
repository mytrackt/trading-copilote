# Extraction StockCharts — Triple Bottom Reversal
**Source :** `bundles/stockcharts/triple_bottom_reversal.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D4611 → D4630 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/triple-bottom-reversal.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : pattern de retournement haussier applicable à GC/HG/CL/ZW pour détecter des fonds triples sur support et valider une entrée longue.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/IPQzr3mrQDVVnz7OpYHS | Example of a triple bottom chart reversal pattern from StockCharts.com | Présentation générale | D4611 |
| /files/NLwNx6Tmoo40Q096sUW8 | Example of a triple bottom reversal pattern from StockCharts.com (ANDW) | Exemple concret | D4616 |

## DÉCISIONS

### D4611 — Triple Bottom : tendance préalable obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md, image_IPQzr3mrQDVVnz7OpYHS) : Un Triple Bottom Reversal exige une tendance baissière claire préexistante avant la formation du pattern ; sans downtrend préalable, le pattern n'est pas valide.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ne chercher un Triple Bottom que si un downtrend est identifié sur le timeframe analysé ; rejeter le signal si le marché est en range ou en uptrend.
*Catégorie : structure_marche*

### D4612 — Triple Bottom : trois creux approximativement égaux
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Les trois creux doivent être raisonnablement égaux, bien espacés, et marquer des points de retournement significatifs ; ils n'ont pas à être exactement identiques mais doivent être équivalents.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, valider le pattern si les trois lows sont dans une fourchette de tolérance raisonnable ; ne pas exiger une égalité parfaite au tick près.
*Catégorie : structure_marche*

### D4613 — Triple Bottom : déclin du volume pendant la formation
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Pendant le développement du Triple Bottom, le niveau général du volume décline habituellement. Le volume peut augmenter à proximité des creux. Après le troisième creux, une expansion du volume sur la remontée et à la cassure de résistance renforce fortement la validité du pattern.
**TRADEX-AI C2** : Pour GC/HG/CL/ZW, surveiller le volume sur la cassure : expansion nette au franchissement de la résistance = confirmation forte ; faible volume à la cassure = signal douteux, attendre.
*Catégorie : volume_liquidite*

### D4614 — Triple Bottom : cassure de résistance obligatoire pour valider
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Le Triple Bottom Reversal est incomplet tant que la résistance n'est pas cassée. Le point le plus haut de la formation (le plus haut des hauts intermédiaires) constitue la résistance à surveiller.
**TRADEX-AI C1** : Ne pas entrer long sur GC/HG/CL/ZW avant la cassure effective de la résistance ; un fond triple sans cassure reste un pattern neutre, pas un signal d'achat.
*Catégorie : gestion_risque_entree*

### D4615 — Triple Bottom : résistance cassée devient support
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Après la cassure de résistance, le niveau devient un support potentiel. Il y a parfois un test de ce nouveau support lors de la première correction.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, après cassure haussière d'un Triple Bottom, le niveau de résistance brisé peut servir de zone d'appui pour recalibrer le stop ou ajouter une position en cas de pullback.
*Catégorie : gestion_position_active*

### D4616 — Triple Bottom : objectif de prix mesuré
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md, image_NLwNx6Tmoo40Q096sUW8) : L'objectif de prix se calcule en mesurant la distance entre la cassure de résistance et les creux, puis en ajoutant cette distance à la cassure. Pour les patterns de 6 mois ou plus, l'objectif devient moins fiable.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, appliquer l'objectif mesuré comme premier target ; pour les patterns longs (6 mois+), préférer d'autres méthodes de projection (pivots Belkhayate, niveaux COG).
*Catégorie : gestion_position_active*

### D4617 — Triple Bottom : durée de formation et significance
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Les Triple Bottom Reversals se forment généralement sur une période de 3 à 6 mois. Les patterns de 6 mois ou plus représentent des fonds majeurs.
**TRADEX-AI C1** : Sur GC (Or) en particulier, un Triple Bottom de 6 mois+ signale un retournement majeur de tendance ; pondérer fortement ce signal dans la grille de décision TRADEX.
*Catégorie : timing*

### D4618 — Triple Bottom : pattern neutre avant cassure
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Avant la cassure de résistance, le Triple Bottom doit être traité comme un pattern neutre. La capacité à maintenir le support est haussière, mais la demande n'a pas gagné tant que la résistance n'est pas brisée.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ne pas anticiper la cassure ; attendre la confirmation effective avant de déclencher un signal ACHETER en mode Auto.
*Catégorie : gestion_risque_entree*

### D4619 — Triple Bottom : confusion possible avec Triangle Descendant
🔵 **ÉCOLE** (Source : triple_bottom_reversal.md) : Trois creux égaux peuvent ressembler à un Triangle Descendant ou à un Rectangle. Seul le Triangle Descendant a des implications baissières ; les autres sont neutres avant cassure.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, distinguer le Triple Bottom (trois creux + cassure haussière) du Triangle Descendant (trois creux + plafond descendant = baissier) ; l'orientation de la résistance est la clé.
*Catégorie : structure_marche*

### D4620 — Triple Bottom : volume sur troisième creux et signal précoce
🟢 **FAIT VÉRIFIÉ** (Source : triple_bottom_reversal.md) : Un volume croissant et un momentum fort sur la remontée depuis le troisième creux augmentent les probabilités de cassure imminente, même avant que celle-ci ne se produise.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, surveiller l'expansion de volume et du momentum sur la remontée post-troisième creux comme signal précurseur d'une cassure ; renforcer l'alerte niveau 2 si cette condition est remplie.
*Catégorie : volume_liquidite*
