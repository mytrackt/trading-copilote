# Extraction StockCharts — Triple Top Reversal
**Source :** `bundles/stockcharts/triple_top_reversal.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D4651 → D4670 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/triple-top-reversal.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : pattern de retournement baissier applicable à GC/HG/CL/ZW pour détecter des triples tops sur résistance et valider une entrée courte ou une sortie de position longue.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/bLrgGxMxxmBVWRpO170C | Example of a triple top reversal pattern using StockCharts.com | Présentation générale | D4651 |
| /files/GXRsW9asTE8PONziEoc5 | Triple Top reversal in Rockwell Automation (ROK) | Exemple concret | D4656 |

## DÉCISIONS

### D4651 — Triple Top : tendance haussière préalable obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md, image_bLrgGxMxxmBVWRpO170C) : Le Triple Top Reversal est un pattern de retournement baissier. Une uptrend préalable est obligatoire ; sans tendance haussière établie, le pattern n'est pas valide.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ne chercher un Triple Top que lors d'une uptrend établie ; rejeter le signal si le marché est déjà en downtrend ou en range.
*Catégorie : structure_marche*

### D4652 — Triple Top : trois sommets approximativement égaux
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Les trois sommets doivent être raisonnablement égaux, bien espacés, et marquer clairement des points de retournement établissant une résistance. Ils n'ont pas à être exactement égaux mais doivent être raisonnablement équivalents.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, valider le pattern si les trois highs sont dans une fourchette de tolérance raisonnable ; appliquer le même principe de tolérance que pour les Double Top.
*Catégorie : structure_marche*

### D4653 — Triple Top : déclin du volume pendant la formation
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Pendant le développement du Triple Top, le niveau général du volume décline habituellement. Le volume peut augmenter près des sommets. Après le troisième sommet, une expansion du volume sur le déclin et à la cassure du support renforce fortement la validité du pattern.
**TRADEX-AI C2** : Pour GC/HG/CL/ZW, surveiller le volume sur la cassure support : expansion nette = confirmation forte du retournement baissier ; faible volume = signal peu fiable.
*Catégorie : volume_liquidite*

### D4654 — Triple Top : cassure de support obligatoire pour valider
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Le Triple Top Reversal n'est pas complet tant que le support n'est pas cassé. Le point le plus bas de la formation (le plus bas des lows intermédiaires) marque ce niveau de support clé.
**TRADEX-AI C1** : Ne pas entrer short sur GC/HG/CL/ZW avant la cassure effective du support ; un triple sommet sans cassure reste neutre, pas un signal de vente.
*Catégorie : gestion_risque_entree*

### D4655 — Triple Top : support cassé devient résistance
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Après la cassure du support, le niveau devient une résistance potentielle. Il y a parfois un test de cette nouvelle résistance lors d'un rally de réaction.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, après cassure baissière d'un Triple Top, le niveau de support brisé peut servir de résistance pour placer un stop ou définir un niveau de rebond attendu.
*Catégorie : gestion_position_active*

### D4656 — Triple Top : objectif de prix mesuré
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md, image_GXRsW9asTE8PONziEoc5) : L'objectif de prix se calcule en mesurant la distance entre la cassure du support et les sommets, puis en soustrayant cette distance de la cassure. Pour les patterns de 6 mois ou plus, l'objectif devient moins fiable.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, appliquer l'objectif mesuré comme premier target baissier ; pour les patterns longs (6 mois+), utiliser les pivots Belkhayate ou niveaux COG comme cibles alternatives.
*Catégorie : gestion_position_active*

### D4657 — Triple Top : durée de formation et significance
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Les Triple Top Reversals se forment généralement sur 3 à 6 mois. Les patterns de 6 mois ou plus représentent des tops majeurs.
**TRADEX-AI C1** : Sur GC (Or) en particulier, un Triple Top de 6 mois+ signale un retournement majeur de tendance à long terme ; pondérer ce signal en conséquence dans la grille TRADEX /10.
*Catégorie : timing*

### D4658 — Triple Top : pattern neutre avant cassure
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Avant la cassure du support, le Triple Top doit être traité comme un pattern neutre. L'incapacité à casser la résistance est baissière, mais les bears n'ont pas gagné tant que le support n'est pas brisé.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ne pas anticiper la cassure baissière ; attendre la confirmation effective avant tout signal VENDRE en mode Auto.
*Catégorie : gestion_risque_entree*

### D4659 — Triple Top : volume sur dernier déclin comme signal précoce
🟢 **FAIT VÉRIFIÉ** (Source : triple_top_reversal.md) : Une forte augmentation du volume et du momentum sur le déclin depuis la troisième résistance augmente les probabilités d'une cassure imminente du support.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, surveiller l'expansion de volume sur le déclin post-troisième sommet comme signal précurseur d'une cassure baissière ; renforcer l'alerte niveau 2 si cette condition est présente.
*Catégorie : volume_liquidite*

### D4660 — Triple Top : art vs science en analyse technique
🔵 **ÉCOLE** (Source : triple_top_reversal.md) : L'analyse technique est plus un art qu'une science. Les interprétations de patterns doivent être suffisamment spécifiques mais pas excessivement exactes. Un pattern peut ne pas correspondre exactement à la description mais en capture l'esprit (trois tentatives sur résistance, puis cassure du support avec confirmation volume).
**TRADEX-AI C1** : Dans le moteur TRADEX-AI, appliquer une tolérance raisonnable sur les niveaux de sommet pour GC/HG/CL/ZW ; l'esprit du pattern (3 tests résistance + cassure + volume) prime sur l'égalité exacte des prix.
*Catégorie : structure_marche*
