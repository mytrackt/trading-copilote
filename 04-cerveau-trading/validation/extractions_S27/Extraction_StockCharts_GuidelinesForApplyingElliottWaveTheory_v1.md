# Extraction StockCharts — Guidelines for Applying Elliott Wave Theory
**Source :** `bundles/stockcharts/guidelines_for_applying_elliott_wave_theory.md` (HTTP 200 · ~16 303 car.) + 4 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D1911 → D1930 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/elliott-wave-analysis-articles/guidelines-for-applying-elliott-wave-theory
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : théorie d'Elliott (R.N. Elliott / Frost & Prechter) → règles taguées 🔵 ÉCOLE.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Guideline of Equality | Guideline of Equality [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Guideline of Alternation Within an Impulse | Guideline of Alternation Within an Impulse [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Guideline of Depth of Corrective Waves | Guideline of Depth of Corrective Waves [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Adding Elliott Wave Notation to SharpCharts | Adding Elliott Wave Notation to SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1911 — Une « guideline » n'est pas une règle dure
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « A guideline is not a hard and fast rule that can't be broken. It is a tendency - something that happens so often that it can almost qualify as a rule, but at times doesn't work as expected... they may not work out every time. »
**TRADEX-AI C1** : Les guidelines Elliott sont des tendances probabilistes, non des règles déterministes ; à traiter comme du contexte, pas comme un déclencheur dur.
*Catégorie : structure_marche*
---

### D1912 — Guideline d'égalité (Equality)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md, image_01) : « The Guideline of Equality says that two of the motive sub-waves in a five wave sequence will tend toward equality... when Wave 3 of an impulse wave is the extended wave, Wave 5 will approximately equal Wave 1 in price. This is useful for potentially projecting the end of Wave 5. »
**TRADEX-AI C1** : Si Wave 3 est l'onde étendue, Wave 5 ≈ Wave 1 en prix → projection de la fin de Wave 5. Outil de projection de cible.
*Catégorie : timing*
---

### D1913 — Alternance au sein d'une impulsion (Wave 2 vs Wave 4)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md, image_02) : « The forms for Wave 2 and Wave 4 will alternate. If Wave 2 is a sharp style of correction, Wave 4 will be a sideways style of correction. If Wave 2 is sideways, Wave 4 will be sharp. This is useful for anticipating the end of a Wave 4 correction. »
**TRADEX-AI C1** : Wave 2 et Wave 4 alternent de forme (sharp ↔ sideways) ; aide à anticiper la fin de Wave 4. Contexte structurel.
*Catégorie : structure_marche*
---

### D1914 — Alternance au sein d'une correction (Wave A vs Wave B)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « The forms for Wave A and Wave B will alternate within a 3-wave correction. If Wave A is a flat type of correction, Wave B may be a zigzag... if the correction begins with a more simple wave for Wave A, expect the following Waves B and C to be more complex. »
**TRADEX-AI C1** : Dans une correction 3-ondes, A et B alternent (flat ↔ zigzag) ; A simple ⇒ B et C plus complexes. Contexte structurel correctif.
*Catégorie : structure_marche*
---

### D1915 — Profondeur des ondes correctives (territoire du Wave 4 précédent)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md, image_03) : « When the market goes into a correction, it often will correct to the territory of the previous Wave 4 of lesser degree... This is often a good place for a market to find support (or resistance) before the trend moves on. »
**TRADEX-AI C1** : Une correction vise souvent le territoire du Wave 4 de degré inférieur = zone probable de support/résistance. Niveau de référence d'entrée.
*Catégorie : gestion_risque_entree*
---

### D1916 — Guideline de canalisation (Channeling) — principe
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « The Guideline of Channeling is a technique to project the potential end of waves within impulses... Elliott noticed that channel lines often mark their boundaries with sometimes dramatic precision... They all require three points... This technique can be used for projecting the ends of Waves 3, 4 and 5. »
**TRADEX-AI C1** : Canalisation = projection de la fin des ondes 3/4/5 via lignes parallèles sur 3 points. Outil graphique de projection.
*Catégorie : timing*
---

### D1917 — Channeling — projections de la fin des Waves 3, 4 et 5
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Projecting the end of Wave 3: Draw a trend line from the beginning of Wave 1 to the end of Wave 2. Project a parallel line off the end of Wave 1... Wave 4: trend line from beginning of Wave 2 to end of Wave 3, parallel off end of Wave 2... Wave 5: trend line from beginning of Wave 3 to end of Wave 4, parallel off end of Wave 3. »
**TRADEX-AI C1** : Procédure déterministe de tracé : 3 jeux de lignes parallèles pour projeter fin Wave 3 / 4 / 5. Codable comme aide à la projection.
*Catégorie : timing*
---

### D1918 — Guideline d'échelle (arithmétique + semi-log)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « One should use both an arithmetic scale chart and a semi-log scale chart... Arithmetic scale charts are good for looking at waves on lower degrees, but semi-log scale charts are good for bringing large trends (higher degrees) into perspective. A channel may work nicely on a semi-log scale, whereas on an arithmetic scale it may not work as well. »
**TRADEX-AI C1** : Recommandation d'utiliser arithmétique (bas degré) ET semi-log (haut degré) pour valider canaux/ondes. Paramètre d'affichage chart.
*Catégorie : structure_marche*
---

### D1919 — Personnalité des ondes = psychologie de masse
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Wave "personality" is the reflection of mass psychology acting in the market - the emotions that flow from optimism to pessimism... The personality of each wave type is the same whether it is a higher-degree wave or a lesser one. »
**TRADEX-AI C5** : Chaque onde porte une « personnalité » = empreinte de psychologie de masse, fractale (même à tout degré). Lien sentiment.
*Catégorie : structure_marche*
---

### D1920 — Wave 1 (premières ondes)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « About half of the first waves... are part of the basing process and tend to be heavily corrected by Wave 2... The other 50%... rise from large basing... These tend to be dynamic and only moderately retraced. This is a good probable spot to have a Wave 1 extension. »
**TRADEX-AI C1** : Wave 1 : ~50 % issues du basing (fortement corrigées par W2), ~50 % dynamiques (peu retracées, candidates à extension). Contexte de début de tendance.
*Catégorie : structure_marche*
---

### D1921 — Wave 2 (secondes ondes)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Second waves tend to retrace so much of Wave 1 that most of the profits gained are eroded, usually ending on low volume and low volatility... most investors are convinced that the bear market is here to stay. »
**TRADEX-AI C2** : Wave 2 retrace fortement W1, fin sur volume + volatilité faibles ; sentiment pessimiste dominant = piège. Confluence volume/sentiment.
*Catégorie : structure_marche*
---

### D1922 — Wave 3 (troisièmes ondes — la plus forte)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Third waves tend to be strong and broad... Wave 3 usually generates the most volume and price movement, and they are the most likely wave to extend... price breakouts, continuation gaps, volume expansions and increased breadth will accompany it... nearly all stocks will participate. »
**TRADEX-AI C1** : Wave 3 = la plus puissante (volume max, plus susceptible de s'étendre), accompagnée de breakouts, continuation gaps, expansion de volume/breadth. Onde cible pour entrer en tendance. Écho gaps (D1903).
*Catégorie : signal*
---

### D1923 — Wave 4 (quatrièmes ondes)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Fourth waves can be predictable in both depth and form because of the guideline of alternation. They tend to differ with the previous Wave 2... They often trend sideways, building a base for the final Wave 5 to spring from. »
**TRADEX-AI C1** : Wave 4 souvent latérale, prévisible via l'alternance (diffère de W2), construit la base de W5. Contexte de consolidation pré-W5.
*Catégorie : structure_marche*
---

### D1924 — Wave 5 (cinquièmes ondes)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Fifth waves tend to be less dynamic and display slower speed of price change... accompanied by lesser volume and breadth... In advancing fifth waves, optimism is extremely high despite a narrowing of breadth... the fifth wave of an extended fifth will lack the change... and give clues about a change in direction. »
**TRADEX-AI C2** : Wave 5 = moins dynamique, volume/breadth en baisse, optimisme extrême + breadth en rétrécissement = divergence annonçant un retournement. Alerte fin de tendance.
*Catégorie : signal*
---

### D1925 — Wave A
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « During Wave A, the public is convinced that this is just a correction of the previous trend... If Wave A is divided into five sub-waves, it will be a zigzag. If it is divided into three sub-waves, it will be a flat or triangle. »
**TRADEX-AI C1** : Wave A : public encore convaincu de la tendance précédente ; structure interne (5 sous-ondes ⇒ zigzag ; 3 ⇒ flat/triangle) classe la correction.
*Catégorie : structure_marche*
---

### D1926 — Wave B (piège)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Wave B catches people in the wrong direction. It performs the task of enticing the suckers to jump into the market. This is where bear or bull traps happen. As a general rule, B Waves tend to show lower volume. »
**TRADEX-AI C2** : Wave B = piège (bull/bear trap), volume généralement plus faible ; signal de prudence anti-faux-départ. Confluence volume/sentiment.
*Catégorie : gestion_risque_entree*
---

### D1927 — Wave C
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Wave C tends to break the illusions of Wave A and Wave B. In a declining market, it can be devastating and fear takes over with broad participation. An advancing Wave C... can be just as dynamic, fooling investors... The fact that Wave C may do this in five sub-waves helps the deception. »
**TRADEX-AI C5** : Wave C = mouvement dynamique et « brutal », forte participation/peur ; peut leurrer (5 sous-ondes). Contexte sentiment.
*Catégorie : structure_marche*
---

### D1928 — Wave D (triangles horizontaux)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Wave D shows up in horizontal triangles. If the triangle is contracting, it is often accompanied by an increase in volume... it does not fully retrace the previous wave and is moving in the direction that the market is about to take after the following Wave E. »
**TRADEX-AI C1** : Wave D apparaît dans les triangles horizontaux ; triangle contractant + volume montant ; indique la direction post-Wave E. Contexte de triangle.
*Catégorie : structure_marche*
---

### D1929 — Wave E (faux break du triangle)
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md) : « Wave E shows up as the last wave in horizontal triangles. It will often stage a false break of the trend line... before the market takes off in the opposite direction. If the triangle was a Wave 4 in a rising impulse, it would instill a bearish conviction before the market shot up to produce Wave 5. »
**TRADEX-AI C1** : Wave E = dernière onde du triangle, fait souvent un faux break avant le mouvement inverse ; piège émotionnel. Garde-fou anti-faux-break.
*Catégorie : gestion_risque_entree*
---

### D1930 — Pratique itérative et Fibonacci non couvert ici
🔵 **ÉCOLE** (Source : guidelines_for_applying_elliott_wave_theory.md, image_04) : « You will often find that it is necessary to adjust the count you made to conform to new data... One subject that has not been discussed is the application of Fibonacci counts and ratios to Elliott Waves. This is a broad and important subject... too large to cover here. »
**TRADEX-AI C1** : Le comptage Elliott est itératif (ajusté aux nouvelles données) ; l'usage des ratios Fibonacci sur les ondes existe mais n'est PAS traité dans cette page — écho possible COG 0,618 (⚫🔴 à valider hors source).
*Catégorie : structure_marche*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1911 → D1930 (20) |
| Images | 4/4 certifiées (toutes SECTION-FALLBACK, figcaption vide → label = titre de section) |
| Tags | 🔵 ÉCOLE ×20 (théorie d'Elliott / Frost & Prechter) |
| Cercles | C1 (majorité, structure de marché), C2 (volume ×3), C5 (sentiment ×2) |
| Catégories | structure_marche ×13, timing ×3, gestion_risque_entree ×3, signal ×2 |
| Lien Belkhayate | ⚫🔴 indirect : D1930 mentionne Fibonacci sur ondes (écho COG 0,618) mais NON développé dans la source → à valider hors page |
| Cas à vérifier | Manifest 4 images mais .md contient des figcaption VIDES (figures décoratives) ; les 4 sont certifiées par accord section. Aucun blocage. Lien COG/Fibonacci NON sourcé sur cette page (ne pas fusionner comme fait Belkhayate) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. BRUT, non fusionné.
