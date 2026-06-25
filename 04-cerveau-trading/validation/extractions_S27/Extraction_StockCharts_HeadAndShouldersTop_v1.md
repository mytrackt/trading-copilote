# Extraction StockCharts — Head and Shoulders Top
**Source :** `bundles/stockcharts/head_and_shoulders_top.md` (HTTP 200 · ~8 581 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1991 → D2010 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/head-and-shoulders-top
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | An example of a Head and Shoulders Top chart pattern. | Head and Shoulders Top | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a Head and Shoulders Top reversal pattern. (ADM) | Head and Shoulders Top | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1991 — Définition : retournement baissier après uptrend
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md, image_01) : « A Head and Shoulders Top reversal pattern forms after an uptrend. Its completion marks a trend reversal. »
**TRADEX-AI C1** : Figure de retournement baissier majeur ; n'a de sens qu'à la fin d'une tendance haussière. Détecte un changement de régime sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D1992 — Anatomie : 3 sommets, tête la plus haute
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The pattern contains three successive peaks, with the middle peak (head) being the highest and the two outside peaks (shoulders) being low and roughly equal. »
**TRADEX-AI C1** : Reconnaissance structurelle = 3 sommets successifs, sommet central (tête) le plus haut, épaules plus basses et à peu près égales.
*Catégorie : structure_marche*

---

### D1993 — Neckline = ligne des réactions basses (support)
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The reaction lows of each peak can be connected to form support or a neckline. »
**TRADEX-AI C1** : La neckline (support) se trace en reliant les deux creux de réaction ; niveau-clé de validation à la baisse.
*Catégorie : structure_marche*

---

### D1994 — Pré-requis : uptrend antérieur établi
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « For this to be a reversal pattern, it is important to establish the existence of a prior uptrend. Without a prior uptrend to reverse, there cannot be a Head and Shoulders reversal pattern. »
**TRADEX-AI C1** : Garde-fou de validation : refuser le pattern si aucun uptrend préalable n'est identifié.
*Catégorie : structure_marche*

---

### D1995 — Épaule gauche : pic + repli, tendance haussière intacte
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « the left shoulder forms a peak that marks the high point of the current trend. After this peak, a decline ensues to complete the shoulder formation (1). The low of the decline usually remains above the trend line, keeping the uptrend intact. »
**TRADEX-AI C1** : Épaule gauche = nouveau plus-haut suivi d'un repli restant au-dessus de la trendline haussière.
*Catégorie : structure_marche*

---

### D1996 — Tête : plus-haut excédant le précédent, 2e point neckline
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « an advance begins that exceeds the previous high and marks the top of the head. After peaking, the low of the subsequent decline marks the second point of the neckline (2). The low of the decline generally breaks below the uptrend line, which jeopardizes the uptrend. »
**TRADEX-AI C1** : Tête = sommet le plus haut ; le repli qui suit fixe le 2e point de neckline et casse généralement l'uptrend line.
*Catégorie : structure_marche*

---

### D1997 — Épaule droite : sommet plus bas (lower high), repli = cassure
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The advance from the low (2) forms the right shoulder. This peak is lower than the head (a lower high) and usually in line with the high of the left shoulder... The decline from the peak of the right shoulder should break the neckline. »
**TRADEX-AI C1** : Épaule droite = sommet inférieur à la tête (lower high), aligné avec l'épaule gauche ; son repli doit casser la neckline.
*Catégorie : signal*

---

### D1998 — Asymétrie tolérée des épaules
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « While symmetry is preferred, sometimes the shoulders can be out of whack. »
**TRADEX-AI C1** : Symétrie préférée mais non obligatoire ; tolérer des épaules de tailles différentes lors de la détection.
*Catégorie : structure_marche*

---

### D1999 — Pente de la neckline et degré de baisse
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The slope of the neckline will affect the pattern's degree of bearishness—a downward slope is more bearish than an upward slope. In some cases, multiple low points can be used to form the neckline. »
**TRADEX-AI C1** : Pondérer la confiance : neckline en pente descendante = plus baissier que pente montante. Plusieurs creux possibles pour la tracer.
*Catégorie : signal*

---

### D2000 — Volume : décroissance comme signal d'alerte précoce
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « Ideally, but not always, volume during the advance of the left shoulder should be higher than during the advance of the head. Together, the volume decrease and the head's new high serve as a warning sign. »
**TRADEX-AI C2** : Divergence volume (nouveau plus-haut de la tête sur volume plus faible que l'épaule gauche) = signal d'alerte précoce de retournement.
*Catégorie : signal*

---

### D2001 — Séquence volume : hausse au repli tête, baisse à l'avance épaule droite
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The next warning sign comes when volume increases on the decline from the peak of the head, then decreases during the advance of the right shoulder. Final confirmation comes when volume further increases during the right shoulder's decline. »
**TRADEX-AI C2** : Séquence type = volume↑ au repli de la tête, volume↓ à l'avance épaule droite, volume↑ au repli épaule droite (confirmation finale).
*Catégorie : signal*

---

### D2002 — Volume au breakout : bienvenu (≠ obligatoire pour le top)
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « the uptrend is not reversed until the neckline support is broken. Ideally, this should also occur in a convincing manner, with an expansion in volume. »
**TRADEX-AI C2** : Pour le Top, l'expansion de volume au breakout est idéale/convaincante mais non strictement obligatoire (contraste avec le Bottom où elle est requise — cf. D1974).
*Catégorie : signal*

---

### D2003 — Pattern incomplet tant que la neckline n'est pas cassée
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The head and shoulders pattern isn't complete, and the uptrend is not reversed until the neckline support is broken. »
**TRADEX-AI C1** : Aucun signal de vente avant cassure de la neckline support. Garde-fou anti-anticipation.
*Catégorie : gestion_risque_entree*

---

### D2004 — Support cassé devient résistance (2e chance de vente)
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « Once support is broken, it is common for this same support level to turn into resistance. Sometimes, but certainly not always, the price will return to the support break and offer a second chance to sell. »
**TRADEX-AI C1** : Le pullback sur l'ancien support (devenu résistance) offre un point d'entrée short secondaire — mais moins fiable que pour le Bottom.
*Catégorie : gestion_risque_entree*

---

### D2005 — Objectif de prix : distance neckline↔tête projetée vers le bas
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « the projected price decline is found by measuring the distance from the neckline to the top of the head. This distance is then subtracted from the neckline to reach a price target. »
**TRADEX-AI C1** : Cible = (haut de tête − neckline) soustraite de la neckline. Sert au calcul R/R ≥ 1:2 de la grille.
*Catégorie : gestion_risque_entree*

---

### D2006 — Objectif = guide approximatif, croiser d'autres facteurs
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « Any price target should serve as a rough guide, and other factors should also be considered. These factors might include previous support levels, Fibonacci retracements, or long-term moving averages. »
**TRADEX-AI C1** : Ne pas traiter la cible mesurée comme absolue ; croiser avec supports antérieurs, Fibonacci, MM longues.
*Catégorie : gestion_risque_entree*

---

### D2007 — Exemple ADM : tapering du volume jusqu'au breakout
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md, image_02) : « During the advance to $20.50, volume was still high but not as high as during the left shoulder advance... volume tapered off significantly... Volume continued to decline until the breaking of the neckline. »
**TRADEX-AI C2** : Cas réel ADM (neckline légèrement montante) : déclin progressif du volume jusqu'à la cassure, illustrant la divergence baissière.
*Catégorie : configuration*

---

### D2008 — Exemple ADM : confirmation par CMF négatif au breakout
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « During the decline of the right shoulder and neckline break, volume expanded (red oval), and Chaikin Money Flow (CMF) turned negative. After the initial decline, there was a return to the neckline break... CMF remained negative. »
**TRADEX-AI C2** : Confirmation par CMF passant en négatif au repli/breakout et y restant pendant le pullback. Croisement order-flow utile au score /10.
*Catégorie : indicateurs_tendance*

---

### D2009 — Mesure de l'objectif sur l'exemple ADM
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « The measurement from the neckline to the top of the head was 3. With the neckline break at $17.50, this would imply a move to around $14.50. The July 1998 low was $13.50. »
**TRADEX-AI C1** : Illustration chiffrée : amplitude 3 → neckline 17,50 → cible ≈ 14,50, proche du plus-bas historique. Valide la méthode de projection D2005.
*Catégorie : gestion_risque_entree*

---

### D2010 — Fiabilité, identification neckline/volume primordiale
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_top.md) : « one of the most common reversal formations... usually marks a major trend reversal when complete. The most critical factor is identifying neckline support and volume confirmation on the break... sometimes there is no second chance return to the support break. »
**TRADEX-AI C1** : Facteurs critiques = identification de la neckline + confirmation volume. Risque d'absence de second test (entrée plus pressée que pour le Bottom).
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1991 → D2010 (20 décisions) |
| Cercles couverts | C1 (structure prix), C2 (order flow / volume) |
| Catégories | structure_marche, signal, indicateurs_tendance, gestion_risque_entree, configuration |
| Images certifiées | 2/2 |
| Lien Belkhayate | NON CONCERNÉ (figure classique d'AT, non spécifique méthode Belkhayate) |
| Cas à vérifier | Aucun 🔴/🟡 critique. Contraste-clé à retenir : volume au breakout OBLIGATOIRE pour le Bottom (D1974) mais seulement « idéal » pour le Top (D2002). |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, attend OK utilisateur avant fusion KB.
