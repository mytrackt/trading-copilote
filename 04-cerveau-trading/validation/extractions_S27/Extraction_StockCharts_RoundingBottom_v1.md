# Extraction StockCharts — Rounding Bottom
**Source :** `bundles/stockcharts/rounding_bottom.md` (HTTP 200 · ~4 300 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D3491 → D3502 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/rounding-bottom
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Rounding Bottom. | Rounding Bottom | CERTIFIE (accord .md + HTML) |
| image_02.png | An example of a rounding bottom is in the chart of Amgen, Inc. | Rounding Bottom | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3491 — Nature du Rounding Bottom (saucer bottom)
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md, image_01) : Le Rounding Bottom est une figure de retournement de LONG TERME, mieux adaptée aux graphiques hebdomadaires. Aussi appelé « saucer bottom » (creux en soucoupe), il représente une longue période de consolidation qui passe d'un biais baissier à un biais haussier.
**TRADEX-AI C1** : Pattern de retournement haussier de structure de marché, à horizon long terme (hebdomadaire). Échelle temporelle très éloignée des modes intraday TRADEX (Range Bars / 15 min / 15 s) → pertinence opérationnelle à pondérer fortement.
*Catégorie : structure_marche*

---

### D3492 — Tendance préalable requise (prior trend)
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : Pour qu'une figure de retournement existe, il doit y avoir une tendance préalable à inverser. Idéalement, le plus bas du rounding bottom marque un nouveau plus bas ou un plus bas de réaction. En pratique, le plus bas peut avoir été enregistré plusieurs mois auparavant, le titre tradant à plat avant de former la figure ; à la formation du pattern, son plus bas peut ne pas être le plus bas absolu des derniers mois.
**TRADEX-AI C1** : Condition contextuelle : tendance baissière préalable. Garde-fou : le plus bas de la figure n'est pas nécessairement le plus bas absolu de la période — la détection ne doit pas exiger un minimum global strict.
*Catégorie : structure_marche*

---

### D3493 — Décline (première moitié du pattern)
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : La première portion du rounding bottom est le déclin qui mène au plus bas de la figure. Ce déclin peut prendre différentes formes : certains sont très accidentés, avec plusieurs hauts et bas de réaction, d'autres baissent de manière plus linéaire.
**TRADEX-AI C1** : Repère structurel : phase de déclin = moitié gauche de la soucoupe. Forme variable (accidentée ou linéaire) → détecteur tolérant sur la régularité du déclin.
*Catégorie : structure_marche*

---

### D3494 — Le plus bas (low) : forme arrondie, pas trop pointue
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : Le plus bas peut ressembler à un creux en « V » mais ne doit pas être trop pointu. Il devrait prendre quelques semaines à se former. Comme les prix sont en déclin de long terme, la possibilité d'un climax de vente (selling climax) existe, pouvant créer une pointe basse.
**TRADEX-AI C1** : Critère de forme : creux arrondi (pas un « V » pointu), durée de quelques semaines. Un pic baissier de climax de vente est toléré. Critère de forme codable, mais calibré sur échelle hebdomadaire.
*Catégorie : structure_marche*

---

### D3495 — L'avance (advance) : symétrie temporelle avec le déclin
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : L'avance depuis les plus bas forme la moitié droite du pattern et devrait prendre à peu près le même temps que le déclin préalable. Si l'avance est trop brusque, la validité du rounding bottom peut être remise en cause.
**TRADEX-AI C1** : Paramètre de symétrie : durée(avance) ≈ durée(déclin). Une avance trop verticale invalide le pattern → filtre anti-faux-signal codable.
*Catégorie : structure_marche*

---

### D3496 — Breakout (confirmation haussière)
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : La confirmation haussière vient lorsque la figure casse au-dessus du plus haut de réaction (le début du déclin au commencement du pattern). Comme la plupart des cassures de résistance, ce niveau peut devenir un support. Toutefois, comme le rounding bottom représente un retournement de long terme, ce nouveau support peut ne pas être très significatif.
**TRADEX-AI C2** : Déclencheur de validation : cassure du plus haut de réaction (début du déclin). Aucun signal avant la cassure. La résistance cassée → support potentiel, mais d'importance limitée selon la source.
*Catégorie : signal*

---

### D3497 — Volume : profil suivant la forme de la soucoupe
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : Dans un pattern idéal, les niveaux de volume suivent la forme du rounding bottom : élevés au début du déclin, faibles à la fin du déclin, et croissants durant l'avance. Le volume est peu important pendant le déclin, mais il devrait augmenter sur l'avance et de préférence sur le breakout.
**TRADEX-AI C2** : Confirmation volumétrique : volume en U (haut→bas→haut), augmentation requise sur l'avance et idéalement sur la cassure (lecture ATAS/volume). Critère discriminant utilisable.
*Catégorie : signal*

---

### D3498 — Parenté avec le Head and Shoulders Bottom
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : Un rounding bottom peut être vu comme un Head and Shoulders Bottom sans épaules identifiables. La « tête » représente le plus bas, assez central à la figure. Les niveaux de volume imitent ceux du H&S bottom ; la confirmation vient avec une cassure de résistance.
**TRADEX-AI C1** : Lien de parenté structurelle avec le H&S bottom (figure déjà connue de la KB). Mutualisation possible de la logique de détection (creux central + cassure de résistance + profil de volume).
*Catégorie : structure_marche*

---

### D3499 — Symétrie préférable mais non stricte
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md) : Bien que la symétrie soit préférable sur le rounding bottom, les côtés gauche et droit ne doivent pas être égaux en temps ou en pente. L'important est de capturer l'essence de la figure.
**TRADEX-AI C1** : Tolérance : symétrie souhaitable mais non obligatoire (temps/pente). Le détecteur doit accepter une asymétrie modérée — éviter un critère de symétrie trop rigide.
*Catégorie : structure_marche*

---

### D3500 — Exemple AMGN : contexte et décline
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md, image_02) : Amgen (AMGN) forme un rounding bottom après une longue consolidation. En 1996, le titre tradait dans un range étroit borné par 16,63 $ et 12,83 $. La cassure du support à 12,83 $ a marqué un nouveau plus bas 52 semaines (downtrend). Le titre a décliné de 17 $ vers un plus bas de 11,22 $, et une paire de marteaux (hammers) en octobre 1998 a marqué la fin du déclin.
**TRADEX-AI C1** : Illustration : cassure de support → downtrend → fin de déclin signalée par des hammers (chandeliers). Confirme la mécanique du déclin (D3493) sur cas réel hebdomadaire.
*Catégorie : structure_marche*

---

### D3501 — Exemple AMGN : low, avance et second plus bas
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md, image_02) : Avant les hammers, AMGN tradait autour de 12 $ depuis 6 semaines. Un gap up à fort volume après les hammers a suggéré qu'un plus bas était formé. Après un court rallye, un test du plus bas a formé un plus bas plus haut (higher low) à 11,66 $. Depuis ce second plus bas, l'avance a démarré sérieusement avec un volume croissant ; en mars, une forte avance avec le plus gros volume en 4 mois.
**TRADEX-AI C2** : Illustration : higher low à 11,66 $ + volume croissant sur l'avance = confirmation d'accumulation (lecture volume/ATAS). Confirme D3497 (volume montant sur l'avance).
*Catégorie : structure_marche*

---

### D3502 — Exemple AMGN : breakout, OBV et retest
🟢 **FAIT VÉRIFIÉ** (Source : rounding_bottom.md, image_02) : La résistance de mai 1997 à 17 $ a servi de ligne de confirmation. AMGN a cassé cette résistance en juillet 1998 avec une expansion de volume, confirmée par un nouveau plus haut sur l'OBV. Après la cassure, un test de support a vu le titre retomber brièvement sous 17 $. Le titre avait avancé de 11,66 $ à 19,84 $ en 6 mois ; un pullback était attendu.
**TRADEX-AI C2** : Illustration : cassure de la ligne de confirmation (17 $) + expansion de volume + confirmation OBV (nouveau plus haut). Retest du niveau cassé = pullback normal. Confirme D3496/D3497 sur cas réel.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3491 | Nature (retournement long terme, hebdo) | 🟢 | C1 | structure_marche |
| D3492 | Tendance préalable requise | 🟢 | C1 | structure_marche |
| D3493 | Décline (moitié gauche) | 🟢 | C1 | structure_marche |
| D3494 | Le plus bas (arrondi, non pointu) | 🟢 | C1 | structure_marche |
| D3495 | Avance (symétrie temporelle) | 🟢 | C1 | structure_marche |
| D3496 | Breakout (confirmation haussière) | 🟢 | C2 | signal |
| D3497 | Volume (profil en U) | 🟢 | C2 | signal |
| D3498 | Parenté avec H&S Bottom | 🟢 | C1 | structure_marche |
| D3499 | Symétrie préférable, non stricte | 🟢 | C1 | structure_marche |
| D3500 | Exemple AMGN (contexte + décline) | 🟢 | C1 | structure_marche |
| D3501 | Exemple AMGN (low + avance) | 🟢 | C2 | structure_marche |
| D3502 | Exemple AMGN (breakout + OBV + retest) | 🟢 | C2 | signal |

**Liens Belkhayate :** le Rounding Bottom n'est PAS un pattern Belkhayate (⚫). Aucun lien direct revendiqué. Pertinence projet **faible à modérée** : figure de retournement haussier classique à critères qualitatifs (forme en soucoupe, symétrie, volume en U, cassure de résistance) transposables en détecteur de structure (C1/C2), MAIS calibrée long terme (hebdomadaire) — l'horizon est largement plus long que les modes intraday TRADEX (Range Bars 4-5t / 15 min / 15 s). À traiter en complément, non en substitution, des règles d'entrée Belkhayate (Pivots/BGC/Direction/Énergie). Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D3491 / D3494 / D3495 — échelle temporelle (figure « long terme » hebdomadaire, plus bas formé en « quelques semaines », symétrie temps) : sur futures GC/HG/CL/ZW en Range Bars / 15 min / 15 s, le pattern perd largement son sens. Ré-évaluer la pertinence avant tout usage intraday.
- D3496 / D3497 / D3502 — confirmation par cassure + volume + OBV à mapper sur les flux ATAS/volume réels avant intégration.
- D3498 — mutualisation possible avec le détecteur Head and Shoulders Bottom déjà en KB : à valider pour éviter doublon de logique.
- Cohérence projet : valider que ce pattern de retournement long terme ne contredit pas et ne dilue pas la logique d'entrée Belkhayate déjà figée avant toute fusion.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
