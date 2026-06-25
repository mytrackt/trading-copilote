# Extraction StockCharts — Head and Shoulders Bottom
**Source :** `bundles/stockcharts/head_and_shoulders_bottom.md` (HTTP 200 · ~13 424 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D1971 → D1990 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/head-and-shoulders-bottom
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Head and Shoulders Bottom pattern. | Head and Shoulders Bottom | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a Head and Shoulders Bottom pattern in the chart (ALK) | Head and Shoulders Bottom | CERTIFIE (accord .md + HTML) |
| image_03.png | Example of a Head and Shoulders bottom with shallow shoulders (AT&T) | Head and Shoulders Bottom | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1971 — Définition : retournement majeur après downtrend
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md, image_01) : « The Head and Shoulders Bottom is a major reversal pattern that forms after a downtrend. A completion of the pattern marks a trend change. »
**TRADEX-AI C1** : Figure de retournement haussier majeur ; n'a de sens qu'à la fin d'une tendance baissière. Sert à détecter un changement de régime sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D1972 — Anatomie : 3 creux, tête plus profonde
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « The pattern contains three successive troughs with the middle trough (head) being the deepest and the two outside troughs (shoulders) being shallower. Ideally, the two shoulders would be equal in height and width. »
**TRADEX-AI C1** : Reconnaissance structurelle = 3 creux successifs, creux central (tête) le plus bas, épaules plus hautes et idéalement symétriques.
*Catégorie : structure_marche*

---

### D1973 — Neckline = ligne des réactions hautes
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « The reaction highs in the middle of the pattern can be connected to form resistance, or a neckline. »
**TRADEX-AI C1** : La neckline (résistance) se trace en reliant les deux sommets de réaction internes ; c'est le niveau-clé de validation.
*Catégorie : structure_marche*

---

### D1974 — Le volume est le facteur différenciant vs le Top
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « Volume action is the main difference between the two... While an increase in volume on the neckline breakout for a Head and Shoulders Top is welcomed, it is absolutely required for a bottom. »
**TRADEX-AI C2** : Pour un bottom, l'expansion de volume au breakout est OBLIGATOIRE (pas seulement bienvenue). Critère éliminatoire potentiel de la grille /10 si volume absent.
*Catégorie : signal*

---

### D1975 — Pré-requis : downtrend antérieur établi
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « For this to be a reversal pattern, it is important to establish the existence of a prior downtrend. Without a prior downtrend to reverse, there cannot be a Head and Shoulders Bottom formation. »
**TRADEX-AI C1** : Garde-fou de validation : refuser le pattern si aucun downtrend préalable n'est identifié.
*Catégorie : structure_marche*

---

### D1976 — Épaule gauche : creux + rebond, tendance baissière intacte
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « the left shoulder forms a trough that marks a new reaction low in the current trend. After forming this trough, an advance ensues... The high of the decline usually remains below any longer trend line, thus keeping the downtrend intact. »
**TRADEX-AI C1** : Épaule gauche = nouveau plus-bas suivi d'un rebond restant sous la trendline baissière longue.
*Catégorie : structure_marche*

---

### D1977 — Tête : plus-bas excédant le précédent, 2e point neckline
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « a decline begins that exceeds the previous low and forms the low point of the head. After making a bottom, the high of the subsequent advance forms the second point of the neckline (2). The high... sometimes breaks a downtrend line. »
**TRADEX-AI C1** : Tête = creux le plus profond ; le rebond qui suit fixe le 2e point de neckline et peut casser la downtrend line.
*Catégorie : structure_marche*

---

### D1978 — Épaule droite : creux plus haut que la tête, breakout = complétion
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « This low is always higher than the head and is usually in line with the low of the left shoulder... When the advance from the low of the right shoulder breaks the neckline, the Head and Shoulders Bottom reversal is complete. »
**TRADEX-AI C1** : Épaule droite = creux supérieur à la tête, aligné avec l'épaule gauche ; la cassure de neckline complète le retournement.
*Catégorie : signal*

---

### D1979 — Asymétrie tolérée des épaules
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « While symmetry is preferred, sometimes the shoulders can be out of whack, and the right shoulder will be higher, lower, wider, or narrower. »
**TRADEX-AI C1** : La symétrie est préférée mais non obligatoire ; tolérer des épaules de hauteur/largeur différentes lors de la détection.
*Catégorie : structure_marche*

---

### D1980 — Pente de la neckline et degré de hausse
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « the neckline can slope up, slope down, or be horizontal. The slope of the neckline will affect the pattern's degree of bullishness: an upward slope is more bullish than a downward slope. »
**TRADEX-AI C1** : Pondérer la confiance : neckline en pente montante = plus haussier que pente descendante. Entrée dans le score /10.
*Catégorie : signal*

---

### D1981 — Volume : 2e moitié plus déterminante que la 1re
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « Volume levels during the first half of the pattern are less important than in the second half... subsequent volume patterns should be watched carefully to look for expansion during the advances. »
**TRADEX-AI C2** : Surpondérer l'analyse de volume sur la seconde moitié du pattern (tête→épaule droite→breakout).
*Catégorie : signal*

---

### D1982 — Avance depuis la tête : volume + CMF/OBV en hausse
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « The advance from the low of the head should show an increase in volume and/or better indicator readings, e.g., Chaikin Money Flow (CMF) > 0 or a rise in OBV. »
**TRADEX-AI C2** : Confirmation par indicateurs de flux : CMF > 0 ou OBV montant sur l'avance post-tête.
*Catégorie : indicateurs_tendance*

---

### D1983 — Épaule droite : repli sur volume léger = sain
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « the right shoulder's decline should be accompanied by light volume... With light volume on the pullback, indicators like CMF and OBV should remain strong. »
**TRADEX-AI C2** : Volume léger sur le repli de l'épaule droite distingue la prise de bénéfices normale d'une pression vendeuse réelle.
*Catégorie : signal*

---

### D1984 — Moment-clé : expansion volume sur l'avance depuis l'épaule droite
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « The most important moment for volume occurs on the advance from the low of the right shoulder. For a breakout to be considered valid, there needs to be a volume expansion on the price advance and during the breakout. »
**TRADEX-AI C2** : Le déclencheur de validité = expansion de volume sur l'avance finale + au breakout. Condition d'entrée niveau 2/3 du moteur.
*Catégorie : gestion_risque_entree*

---

### D1985 — Pattern incomplet tant que la neckline n'est pas cassée
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « The Head and Shoulders Bottom pattern is incomplete (and the downtrend is not reversed) until the neckline resistance is broken. For a Head and Shoulders Bottom, this must occur convincingly, with an expansion of volume. »
**TRADEX-AI C1** : Aucun signal d'achat avant cassure convaincante de la neckline avec expansion de volume. Garde-fou anti-anticipation.
*Catégorie : gestion_risque_entree*

---

### D1986 — Résistance cassée devient support (2e chance d'achat)
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « Once resistance is broken, it is common for this same resistance level to turn into support. Often, the price will return to the resistance break and offer a second chance to buy. »
**TRADEX-AI C1** : Le pullback sur l'ancienne résistance (devenue support) offre un point d'entrée secondaire avec stop plus serré.
*Catégorie : gestion_risque_entree*

---

### D1987 — Objectif de prix : distance neckline↔tête projetée vers le haut
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « the projected advance is found by measuring the distance from the neckline to the bottom of the head. This distance is then added to the neckline to reach a price target. »
**TRADEX-AI C1** : Cible = (neckline − bas de tête) ajoutée à la neckline. Sert au calcul R/R ≥ 1:2 de la grille.
*Catégorie : gestion_risque_entree*

---

### D1988 — Objectif = guide approximatif, pondérer d'autres facteurs
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md) : « Any price target should serve as a rough guide, and other factors should also be considered. These factors might include previous resistance levels, Fibonacci retracements, or long-term moving averages. »
**TRADEX-AI C1** : Ne pas traiter la cible mesurée comme absolue ; croiser avec résistances antérieures, Fibonacci, MM longues.
*Catégorie : gestion_risque_entree*

---

### D1989 — Exemple ALK : convention couleurs barres de volume
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md, image_02) : « The low of the left shoulder formed with a large spike in volume... Gray bars denote advancing days, black bars declining days, and the thin red horizontal is the 60-day Exponential Moving Average. »
**TRADEX-AI C2** : 🟡 CONVENTION graphique StockCharts (barres grises = hausse, noires = baisse, ligne rouge = EMA 60). Cas réel ALK : neckline en pente descendante, expansion volume + gap up sur l'avance depuis la tête.
*Catégorie : configuration*

---

### D1990 — Fiabilité et nature « art » de l'analyse
🟢 **FAIT VÉRIFIÉ** (Source : head_and_shoulders_bottom.md, image_03) : « Head and Shoulder Bottoms are among the most common and reliable reversal formations... usually mark a major trend reversal when complete... technical analysis is more of an art than a science. » (exemple AT&T : neckline plate, épaules peu profondes mais tête bien marquée)
**TRADEX-AI C1** : Pattern parmi les plus fiables, mais détection imparfaite : prévoir une marge de tolérance et confirmation humaine (mode Manuel).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1971 → D1990 (20 décisions) |
| Cercles couverts | C1 (structure prix), C2 (order flow / volume) |
| Catégories | structure_marche, signal, indicateurs_tendance, gestion_risque_entree, configuration |
| Images certifiées | 3/3 |
| Lien Belkhayate | NON CONCERNÉ (figure classique d'AT, non spécifique méthode Belkhayate) |
| Cas à vérifier | Aucun 🔴/🟡 critique. D1989 = 🟡 convention propre à StockCharts (couleurs/EMA), à ne pas généraliser. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, attend OK utilisateur avant fusion KB.
