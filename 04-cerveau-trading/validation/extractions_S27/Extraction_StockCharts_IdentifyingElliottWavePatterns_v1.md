# Extraction StockCharts — Identifying Elliott Wave Patterns

**Source :** `bundles/stockcharts/identifying_elliott_wave_patterns.md` (HTTP 200 · ~10 600 car.) + 12 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 12/12 certifiées
**Décisions :** D2191 → D2210 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/elliott-wave-analysis-articles/identifying-elliott-wave-patterns
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🔵 **PERTINENCE FUTURES : PARTIELLE (C1) — ÉCOLE Elliott** — théorie de structure de marché (motrices/correctives) applicable aux futures (GC/HG/CL/ZW) comme cadre de lecture de tendance, MAIS subjective (comptage discrétionnaire). Méthode externe (école Elliott / Frost-Prechter) → tag 🔵 ÉCOLE. Les 3 règles inviolables de l'impulsion (D2194) sont déterministes ; le reste reste interprétatif → à pondérer prudemment. Belkhayate NON CONCERNÉ (⚫).

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Décision |
|-------|-------|---------|----------|
| image_01.png | Labeling Wave Degrees | Labeling Wave Degrees [SECTION-FALLBACK] | D2191 |
| image_02.png | Impulse Waves | Impulse Waves [SECTION-FALLBACK] | D2195 |
| image_03.png | Wave Extensions | Wave Extensions [SECTION-FALLBACK] | D2196 |
| image_04.png | Wave Extensions | Wave Extensions [SECTION-FALLBACK] | D2196 |
| image_05.png | Impulse Wave Truncation (Truncated Fifth) | Impulse Wave Truncation [SECTION-FALLBACK] | D2197 |
| image_06.png | Ending Diagonals | Ending Diagonals [SECTION-FALLBACK] | D2199 |
| image_07.png | Zigzag Corrections | Zigzag Corrections [SECTION-FALLBACK] | D2202 |
| image_08.png | Flat Corrections | Flat Corrections [SECTION-FALLBACK] | D2203 |
| image_09.png | Flat Corrections | Flat Corrections [SECTION-FALLBACK] | D2204 |
| image_10.png | Horizontal Triangles | Horizontal Triangles [SECTION-FALLBACK] | D2206 |
| image_11.png | Correction Combinations | Correction Combinations [SECTION-FALLBACK] | D2208 |
| image_12.png | Correction Combinations | Correction Combinations [SECTION-FALLBACK] | D2208 |

## DÉCISIONS

### D2191 — Étiquetage des degrés de vagues
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_01) : « smaller wave structures are labeled differently than the larger wave structures to help distinguish between the degrees of the waves. (...) The uppercase Roman numerals represent the large-degree waves, the simple numbers represent the medium-degree waves and the lowercase Roman numerals represent the small-degree waves. (...) Wave 1 of (1) would indicate that Wave 1 is part of a larger degree Wave (1). »
**TRADEX-AI C1** : convention de notation des degrés (romaines majuscules > chiffres > romaines minuscules). Cadre de lecture multi-échelle de la tendance. Note structurelle, pas un signal.
*Catégorie : structure_marche*

---

### D2192 — Usage pratique : 1 à 3 degrés seulement
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « most chartists will only use 1-3 wave degrees on their charts. It can get quite complicated trying to apply all nine wave degrees on one chart! » Convention : romaines majuscules (I,II,III,IV,V,a,b,c) / chiffres (1,2,3,4,5,A,B,C) / romaines minuscules (i,ii,iii,iv,v,a,b,c).
**TRADEX-AI C1** : garde-fou de simplicité — limiter à 1-3 degrés. Pour TRADEX, l'analyse Elliott complète (9 degrés) est trop complexe/subjective ; usage restreint recommandé.
*Catégorie : structure_marche*

---

### D2193 — Deux types de vagues motrices
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « There are two types of motive waves: the Impulse and the Diagonal. »
**TRADEX-AI C1** : taxonomie de base des vagues motrices (Impulsion + Diagonale). Cadre de classification structurelle.
*Catégorie : structure_marche*

---

### D2194 — Les 3 règles inviolables de l'impulsion
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : structure 5-3-5-3-5 ; « three unbreakable rules : 1. Wave 2 cannot retrace more than 100% of Wave 1. 2. Wave 3 can never be the shortest of waves 1, 3, and 5. 3. Wave 4 can never overlap Wave 1. If one of these rules is violated, then the structure is not an impulse wave. »
**TRADEX-AI C1** : **3 règles DÉTERMINISTES** (les seules vraiment codables d'Elliott) — validité d'une impulsion vérifiable algorithmiquement. Utilisable comme filtre objectif de structure (invalidation d'un comptage).
*Catégorie : structure_marche*

---

### D2195 — Caractéristiques de l'impulsion (Vague 3)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_02) : « Wave 4 does not cross into the price territory of Wave 2, nor does Wave 2 correct below the beginning of Wave 1. (...) Wave 3 is not the shortest (...) it is usually the longest of the five waves and the most likely to extend. Sub-wave 3 of an impulse wave will always be another impulse-type motive wave. A break in price below the low of Wave 1 would invalidate the suspected wave-count. »
**TRADEX-AI C1** : précisions sur l'impulsion — Vague 3 souvent la plus longue, sous-vague 3 toujours motrice ; cassure sous le creux de Vague 1 = invalidation. Niveaux d'invalidation exploitables comme stops structurels.
*Catégorie : structure_marche*

---

### D2196 — Extensions de vagues
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_03, image_04) : « impulse waves will exhibit (...) an "extension" (...). This can happen in either Wave 1, 3 or 5, typically (...) in only one of said waves. (...) if the potential Wave 1 and Wave 5 (...) look equal in length, then it is most likely Wave 3 which is extended. (...) extensions can occur within extensions. »
**TRADEX-AI C1** : notion d'extension (une seule des vagues 1/3/5 s'allonge, le plus souvent la 3). Heuristique d'identification ; subjective. Note structurelle.
*Catégorie : structure_marche*

---

### D2197 — Troncature de la cinquième (Truncated Fifth)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_05) : « there is a chance that the last wave (...) Wave 5, will not reach the end of Wave 3 before the market starts correcting (...). This condition is often called a "failure" or a "Truncation." (...) consists of 5 sub-waves (...). It often occurs after a particularly strong third wave. »
**TRADEX-AI C1** : signal d'épuisement — Vague 5 tronquée (n'atteint pas le sommet de Vague 3) après une Vague 3 très forte = avertissement de retournement imminent. Indice de fin de tendance.
*Catégorie : structure_marche*

---

### D2198 — Vagues diagonales (wedge)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « A Diagonal Wave is the second type of motive wave. (...) the diagonal looks like a wedge - either expanding or contracting. (...) each actionary sub-wave (...) never fully retraces the previous actionary sub-wave; (...) sub-wave 3 of the diagonal can never be the shortest wave. »
**TRADEX-AI C1** : diagonale = motrice en forme de biseau (wedge). Mêmes règles partielles que l'impulsion (sous-vague 3 jamais la plus courte). Note structurelle.
*Catégorie : structure_marche*

---

### D2199 — Diagonale terminale (Ending Diagonal) 3-3-3-3-3
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_06) : « The ending diagonal (...) occurs in Wave 5 of an impulse, or the last wave of a correction (Wave C). (...) structure count of 3-3-3-3-3 (...) indicating exhaustion of the larger degree trend. (...) Wave 2 and Wave 4 may overlap. Most ending diagonals have a wedge shape. »
**TRADEX-AI C1** : signal d'épuisement de tendance — diagonale terminale (biseau, 3-3-3-3-3) en Vague 5 ou Vague C = fin du mouvement de degré supérieur. Indice de retournement majeur.
*Catégorie : structure_marche*

---

### D2200 — Diagonale d'amorce (Leading Diagonal) 5-3-5-3-5
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « Leading diagonals (...) are found in either the Wave 1 position of an impulse wave or in the Wave A position of a zigzag correction. They have a 5-3-5-3-5 wave structure (...) Wave 2 and Wave 4 overlap and form a wedge. (...) this pattern indicates continuation of the trend. »
**TRADEX-AI C1** : diagonale d'amorce (Vague 1 ou Vague A, 5-3-5-3-5) = signe de CONTINUATION de tendance (à l'inverse de la terminale qui marque la fin). Distinction structurelle importante.
*Catégorie : structure_marche*

---

### D2201 — Deux styles de corrections
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « There are two styles of corrective waves, the "sharp" correction and the "sideways" correction. The sharp corrections move steeply against the trend (...), while the sideways correction appears to form a flat type of structure (...). the market can correct up or down, depending on the trend of higher degree. »
**TRADEX-AI C1** : taxonomie des corrections (vive vs latérale). La correction peut être haussière ou baissière selon la tendance de degré supérieur — garde-fou de lecture directionnelle.
*Catégorie : structure_marche*

---

### D2202 — Corrections en zigzag (5-3-5)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_07) : « A single zigzag is a three-wave corrective structure (...) labeled as A-B-C. The sub-wave sequence is 5-3-5. The A and C waves are motive waves (...), while the B wave is corrective. The zigzag (...) usually shows up in the second wave position. (...) double (or triple) zigzag. »
**TRADEX-AI C1** : zigzag = correction vive A-B-C (5-3-5), typiquement en Vague 2. Note structurelle ; peut se combiner en double/triple.
*Catégorie : structure_marche*

---

### D2203 — Corrections à plat (Flat) 3-3-5
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_08) : « The flat correction is another three-wave correction where the sub-waves form a 3-3-5 structure (...) labeled as A-B-C. (...) Waves A and B are corrective and Wave C is motive. It is called a "flat" because the pattern moves in a sideways direction. Within an impulse wave, the fourth wave often has a flat. »
**TRADEX-AI C1** : flat = correction latérale A-B-C (3-3-5), souvent en Vague 4. Note structurelle.
*Catégorie : structure_marche*

---

### D2204 — Flats étendus et running flats
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_09) : « A flat that has the B wave terminate beyond the start of the A wave and the C wave terminate beyond the start of the B wave is called an expanded flat. This is actually more common (...). A running flat (...) will have Wave B terminate beyond the beginning of Wave A, but Wave C will fail to reach the beginning of Wave A (...) usually forms in strong trends. »
**TRADEX-AI C1** : variantes du flat (expanded = plus courant ; running = en tendance forte). Le running flat, où C n'atteint pas le début de A, signale une tendance sous-jacente forte.
*Catégorie : structure_marche*

---

### D2205 — Les corrections peuvent monter ou descendre
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « although corrections are often seen as declining in price, the reality is that the market can correct up or down, depending on the trend of higher degree. » (rappel transversal de la section corrective.)
**TRADEX-AI C1** : garde-fou directionnel — ne pas assimiler « correction » à « baisse ». La direction dépend de la tendance de degré supérieur. Important pour ne pas mal orienter un signal.
*Catégorie : structure_marche*

---

### D2206 — Triangles horizontaux (3-3-3-3-3, A-B-C-D-E)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_10) : « The horizontal triangle (...) consists of five sub-waves that form a 3-3-3-3-3 structure, labeled as A-B-C-D-E. (...) reflects a balance of forces and travels in a sideways pattern. (...) can either be expanding (...) or contracting, forming a wedge (...) symmetrical, descending or ascending. »
**TRADEX-AI C1** : triangle horizontal = équilibre des forces, mouvement latéral (A-B-C-D-E, 3-3-3-3-3). Recoupe les patterns chartistes triangle (symétrique/ascendant/descendant) déjà en KB.
*Catégorie : structure_marche*

---

### D2207 — Position des triangles = avant le dernier mouvement
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « horizontal triangles (...) always appear in the position prior to the final move of the pattern, or as the final pattern in a combination. (...) they will appear as Wave 4 in an impulse wave or as Wave B in a zigzag. This one fact can help alert an analyst to a change in trend. »
**TRADEX-AI C1** : heuristique de timing — un triangle horizontal précède le DERNIER mouvement (Vague 4 / Vague B) → alerte de changement de tendance proche. Indice anticipatif exploitable.
*Catégorie : timing*

---

### D2208 — Combinaisons correctives (W-X-Y, W-X-Y-X-Z)
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md, image_11, image_12) : « a combination (...) is composed of the corrective waves seen above (...). Combinations are mostly sideways (...). labeled as W-X-Y, for a double combination, or as W-X-Y-X-Z for a triple combination. Wave W is any flat or zigzag, Wave X is usually a flat or zigzag (...). watch out for the horizontal triangle, which can be either in the last position or the next to the last position. »
**TRADEX-AI C1** : structures correctives complexes (combinaisons W-X-Y / W-X-Y-X-Z), majoritairement latérales. Niveau de complexité élevé → forte subjectivité, usage prudent.
*Catégorie : structure_marche*

---

### D2209 — Subjectivité du comptage = garde-fou central
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : « Counting waves is a skill that comes with practice and proper application of the rules (...). It can get quite complicated (...). An analyst must exercise patience and flexibility when dealing with corrective waves. »
**TRADEX-AI C1** : garde-fou méthodologique — le comptage Elliott est discrétionnaire et requiert flexibilité. Pour TRADEX, ne JAMAIS automatiser un comptage complet ; n'utiliser que les règles déterministes (D2194) comme filtre. Brique de contexte, pas de signal mécanique.
*Catégorie : structure_marche*

---

### D2210 — Niveaux d'invalidation comme stops structurels
🔵 **ÉCOLE Elliott** (Source : identifying_elliott_wave_patterns.md) : règles d'invalidation littérales — « A break in price below the low of Wave 1 would invalidate the suspected wave-count » (D2195) ; « Wave 2 cannot move below the beginning of Wave 1 (...) if it retraces it completely, it is not a Wave 2. »
**TRADEX-AI C1** : usage pratique pour le risque — les seuils d'invalidation Elliott (creux de Vague 1, début de Vague 1) fournissent des niveaux de stop structurels objectifs, même sans automatiser le comptage. Seule exploitation robuste pour le moteur.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2191 | Étiquetage degrés de vagues | 🔵 | C1 | structure_marche |
| D2192 | Usage pratique 1-3 degrés | 🔵 | C1 | structure_marche |
| D2193 | Deux types de motrices | 🔵 | C1 | structure_marche |
| D2194 | 3 règles inviolables impulsion | 🔵 | C1 | structure_marche |
| D2195 | Caractéristiques Vague 3 | 🔵 | C1 | structure_marche |
| D2196 | Extensions de vagues | 🔵 | C1 | structure_marche |
| D2197 | Troncature de la 5e | 🔵 | C1 | structure_marche |
| D2198 | Vagues diagonales (wedge) | 🔵 | C1 | structure_marche |
| D2199 | Diagonale terminale 3-3-3-3-3 | 🔵 | C1 | structure_marche |
| D2200 | Diagonale d'amorce 5-3-5-3-5 | 🔵 | C1 | structure_marche |
| D2201 | Deux styles de corrections | 🔵 | C1 | structure_marche |
| D2202 | Zigzag 5-3-5 | 🔵 | C1 | structure_marche |
| D2203 | Flat 3-3-5 | 🔵 | C1 | structure_marche |
| D2204 | Expanded / running flats | 🔵 | C1 | structure_marche |
| D2205 | Corrections up ou down | 🔵 | C1 | structure_marche |
| D2206 | Triangles horizontaux 3-3-3-3-3 | 🔵 | C1 | structure_marche |
| D2207 | Triangle = avant dernier mouvement | 🔵 | C1 | timing |
| D2208 | Combinaisons W-X-Y / W-X-Y-X-Z | 🔵 | C1 | structure_marche |
| D2209 | Subjectivité du comptage | 🔵 | C1 | structure_marche |
| D2210 | Invalidations = stops structurels | 🔵 | C1 | gestion_risque_entree |

| Élément | Valeur |
|---------|--------|
| Décisions | D2191 → D2210 (20) |
| Images certifiées | 12/12 |
| Cercles | C1 (structure/tendance, exclusif) |
| Catégories | structure_marche · timing · gestion_risque_entree |
| Actif applicable | GC/HG/CL/ZW (TRADING) + ES — cadre de structure transposable, mais discrétionnaire |
| Belkhayate | NON CONCERNÉ (Elliott = école externe Frost-Prechter ⚫) |
| Pertinence futures | PARTIELLE (C1) — école Elliott ; seules les règles déterministes (D2194) et les niveaux d'invalidation (D2210) sont robustes |
| Cas « à vérifier » | (1) Tag 🔵 ÉCOLE (Elliott / Frost-Prechter), méthode externe NON Belkhayate. (2) RISQUE SUBJECTIVITÉ : le comptage Elliott est discrétionnaire (D2209) — NE JAMAIS automatiser un comptage complet dans le moteur. (3) Seules briques codables fiables : les 3 règles inviolables (D2194) comme filtre d'invalidation et les seuils d'invalidation comme stops structurels (D2210). (4) Le triangle horizontal (D2206) recoupe des patterns chartistes déjà en KB — vérifier la non-duplication avant fusion. (5) Page de cadre conceptuel : 0 formule de calcul, 0 paramètre numérique de timeframe (rien à recalibrer, mais rien de mécanique non plus). |

**Liens Belkhayate :** Aucun lien direct — la théorie des vagues d'Elliott n'appartient PAS à la méthode Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
