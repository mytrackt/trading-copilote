# Extraction StockCharts — Flag, Pennant
**Source :** `bundles/stockcharts/flag_pennant.md` (HTTP 200 · ~7 430 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1831 → D1844 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/flag-pennant
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Pennant chart pattern. | What Are Flag and Pennant Chart Patterns? | CERTIFIE (accord .md + HTML) |
| image_02.png | A Flag pattern in the chart of HPQ. | How Do You Identify Flags and Pennants? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1831 — Flags et pennants = patterns de continuation court terme
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md, image_01) : « Flags and Pennants are short-term continuation patterns that mark a small consolidation before the previous move resumes... and mark a midpoint of the move. »
**TRADEX-AI C1** : patterns de continuation marquant un mi-parcours du mouvement ; signal de reprise de tendance.
*Catégorie : structure_marche*
---

### D1832 — Prérequis : mouvement initial fort sur volume élevé
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « Flags and pennants require evidence of a sharp advance or decline in heavy volume. These moves usually occur on heavy volume and can contain gaps... the flag/pennant is merely a pause. »
**TRADEX-AI C2** : condition de validité = mouvement initial brusque sur fort volume (peut contenir des gaps). Le volume (C2 order flow) est central.
*Catégorie : structure_marche*
---

### D1833 — Le flagpole se mesure de la cassure au sommet/creux du pattern
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « The flagpole is the distance from the first resistance or support break to the high or low of the flag/pennant... A line extending up from this break to the high of the flag/pennant forms the flagpole. »
**TRADEX-AI C1** : le mât (flagpole) = distance de la cassure S/R au sommet/creux du fanion ; sert au calcul de cible.
*Catégorie : structure_marche*
---

### D1834 — Le flag = petit rectangle incliné contre la tendance
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md, image_02) : « A flag is a small rectangle pattern that slopes against the previous trend. If the previous move was trending up, then the flag would slope down... the price action needs to be contained within two parallel trend lines. »
**TRADEX-AI C1** : flag = canal parallèle incliné à contre-tendance (haussier → flag descendant).
*Catégorie : structure_marche*
---

### D1835 — Le pennant = petit triangle symétrique convergent
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « A pennant is a small symmetrical triangle that begins wide and converges as the pattern matures (like a cone). The slope is usually neutral... contained within the converging trend lines. »
**TRADEX-AI C1** : pennant = triangle symétrique convergent, pente neutre, prix contenu dans lignes convergentes.
*Catégorie : structure_marche*
---

### D1836 — Durée : 1 à 12 semaines, idéal 1 à 4 semaines
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « Flags and pennants are short-term patterns lasting from one to 12 weeks... Ideally, these patterns will form between one and four weeks. Once a flag is over 12 weeks old, it would be classified as a rectangle. A pennant more than 12 weeks old would turn into a symmetrical triangle. »
**TRADEX-AI C1** : fenêtre de validité 1–12 semaines (idéal 1–4) ; au-delà de 12 sem. → rectangle / triangle symétrique. Fiabilité 8–12 sem. débattue.
*Catégorie : timing*
---

### D1837 — Signal de cassure : au-dessus résistance (bull) / sous support (bear)
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « For a bullish flag or pennant, a break above resistance signals that the previous advance has resumed. For a bearish flag or pennant, a break below support signals that the previous decline has resumed. »
**TRADEX-AI C1** : déclencheur = cassure de résistance (long) ou de support (short) du fanion.
*Catégorie : signal*
---

### D1838 — Le volume légitime le mouvement et l'expansion confirme la cassure
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « Volume should be heavy during the advance or decline that forms the flagpole... An expansion of volume on the resistance (support) break lends credence to the validity of the formation and the likelihood of continuation. »
**TRADEX-AI C2** : volume fort sur le mât + expansion de volume à la cassure = confirmation (filtre order flow ATAS).
*Catégorie : structure_marche*
---

### D1839 — Cible : projeter la longueur du flagpole depuis la cassure
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « The flagpole length can be applied to the resistance break or support break of the flag/pennant to estimate the advance or decline. »
**TRADEX-AI C1** : objectif de prix = longueur du mât reportée depuis le point de cassure (measured move).
*Catégorie : gestion_risque_entree*
---

### D1840 — Identification : sans mouvement brusque préalable, fiabilité douteuse
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « Flags and pennants must be preceded by a sharp advance or decline. Without a sharp move, the formation's reliability becomes questionable, and trading could carry added risk. »
**TRADEX-AI C1** : critère éliminatoire — absence de mouvement brusque préalable → pattern non fiable, risque accru.
*Catégorie : signal*
---

### D1841 — Triple confirmation par le volume (move/consolidation/reprise)
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « Look for volume confirmation on the initial move, consolidation, and resumption to augment the robustness of pattern identification. »
**TRADEX-AI C2** : profil de volume idéal = expansion (move) → contraction (consolidation) → expansion (reprise).
*Catégorie : structure_marche*
---

### D1842 — Exemple HPQ : flag après avance brusque, mât de 10 points
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md, image_02) : « After consolidating for three months, HPQ broke above resistance at $28... advanced from $28 to $38 in four weeks... The flagpole length measured 10 points... to project a price target at $46. »
**TRADEX-AI C1** : cas illustratif — cassure $28, mât 10 pts ($28→$38), cible $46 (report depuis cassure $36).
*Catégorie : signal*
---

### D1843 — Le profil de volume de l'exemple HPQ (expand/contract/expand)
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « volume expanded on the sharp advance to form the flagpole, contracted during the flag's formation, and expanded right after the resistance breakout. »
**TRADEX-AI C2** : validation empirique du schéma de volume attendu sur un flag réel.
*Catégorie : structure_marche*
---

### D1844 — Cassure initiale sans volume puis gap haussier confirmant
🟢 **FAIT VÉRIFIÉ** (Source : flag_pennant.md) : « The first break above the flag's upper trend line occurred on June 21 without volume expansion. However, the stock gapped up a week later and closed strong with above-average volume. »
**TRADEX-AI C1** : une cassure sans volume reste fragile ; un gap haussier ultérieur avec volume au-dessus de la moyenne confirme (lien gap → bundle gap_trading).
*Catégorie : signal*
---

## SYNTHÈSE

| Plage | Décisions | Images | Cercles | Catégories dominantes |
|-------|-----------|--------|---------|-----------------------|
| D1831→D1844 | 14 | 2/2 certifiées | C1 (majoritaire), C2 (volume) | structure_marche, signal, timing, gestion_risque_entree |

Tags : 🟢 14 · 🔵 0 · 🟡 0 · ⏳ 0 · 🔴 0 · ⚫ 0. Patterns de continuation classiques ; volume = pivot order flow (C2 ATAS). Lien Belkhayate : NON CONCERNÉ. Actifs visés : GC·HG·CL·ZW. NB : plage arrêtée à D1844 (contenu épuisé, AUCUN padding jusqu'à D1850).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
