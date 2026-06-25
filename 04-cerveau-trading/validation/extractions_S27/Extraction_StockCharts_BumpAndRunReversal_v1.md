# Extraction StockCharts — Bump and Run Reversal (BARR)
**Source :** `bundles/stockcharts/bump_and_run_reversal.md` (HTTP 200 · ~5 000 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D991 → D1002 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/bump-and-run-reversal
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : pattern chartiste pur (figure de retournement) → catégorie dominante `structure_marche`.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Bump and Run Reversal (BARR) pattern. | Bump and Run Reversal | CERTIFIE (accord .md + HTML) |
| image_02.png | Bump and Run Reversal pattern after prices advance in a spec[ulative frenzy in 2000] | Bump and Run Reversal | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D991 — Nature et origine du Bump and Run Reversal
🔵 **ÉCOLE (Bulkowski)** (Source : bump_and_run_reversal.md, image_01) : Le Bump and Run Reversal (BARR) est une figure de retournement qui se forme après qu'une spéculation excessive a fait monter les prix trop loin, trop vite. Développée par Thomas Bulkowski, introduite dans le numéro de juin 1997 de *Technical Analysis of Stocks and Commodities* et incluse dans son *Encyclopedia of Chart Patterns*. Nommée à l'origine « Bump and Run Formation » (BARF), renommée par Bulkowski faute d'acronyme acceptable. Trois phases principales : **lead-in, bump et run**.
**TRADEX-AI C1** : Figure de retournement après emballement spéculatif ; couche analytique structurelle, jamais déclencheur d'ordre.
*Catégorie : structure_marche*

---

### D992 — Phase Lead-in
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : La phase de lead-in (entrée) est la première partie, pouvant durer un mois ou plus, et sert de base au tracé de la ligne de tendance. L'avance des prix y est ordonnée, sans excès spéculatif. La ligne de tendance doit être modérément pentue : trop raide, le bump ultérieur risque d'être insuffisant ; pas assez raide, la cassure de ligne surviendra trop tard. Bulkowski recommande un angle de 30 à 45 degrés. L'angle dépend de l'échelle (semi-log ou arithmétique) et de la taille du chart ; une évaluation visuelle est généralement plus simple.
**TRADEX-AI C1** : Base géométrique (ligne de tendance modérée 30-45°) ; angle dépendant de l'échelle, donc non absolu — évaluation contextuelle requise.
*Catégorie : structure_marche*

---

### D993 — Phase Bump
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Le bump (bosse) se forme par une avance brutale, les prix s'éloignant davantage de la ligne de tendance du lead-in. Idéalement, l'angle de la ligne de tendance de l'avance du bump devrait être environ 50% plus grand que celui de la ligne de tendance du lead-in — soit grossièrement un angle entre 45 et 60 degrés. À défaut de mesurer les angles, une évaluation visuelle suffit.
**TRADEX-AI C1** : Critère d'accélération codable (pente du bump ≈ 1,5× pente du lead-in) ; sinon évaluation visuelle.
*Catégorie : configuration*

---

### D994 — Validité du Bump (règle des 2×)
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Le bump doit représenter une avance spéculative non soutenable. Bulkowski a développé une technique de mesure « arbitraire » pour valider le niveau de spéculation : la distance entre le plus haut du bump et la ligne de tendance du lead-in doit être au moins DEUX fois la distance entre le plus haut du lead-in et cette même ligne. Ces distances se mesurent par des lignes verticales des plus hauts vers la ligne de tendance.
**TRADEX-AI C1** : Règle de validation quantitative (ratio ≥ 2× des distances verticales à la ligne de tendance) implémentable géométriquement.
*Catégorie : configuration*

---

### D995 — Bump Rollover (formation du sommet)
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Après l'extinction de la spéculation, les prix culminent et un sommet se forme. Parfois un petit double top ou une série de sommets descendants se forme à la place. Les prix déclinent ensuite vers la ligne de tendance du lead-in, formant le côté droit du bump.
**TRADEX-AI C1** : Phase de bascule (rollover) ; signal précoce de retournement, à confirmer par la cassure (D997).
*Catégorie : structure_marche*

---

### D996 — Volume
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Pendant la phase de lead-in, le volume est généralement moyen, parfois faible. Quand l'avance spéculative commence à former le côté gauche du bump, le volume s'étend à mesure que l'avance accélère.
**TRADEX-AI C2** : Confirmation par expansion de volume sur le côté gauche du bump ; recoupe l'order flow (ATAS) comme validation d'emballement.
*Catégorie : structure_marche*

---

### D997 — Phase Run et cassure de la ligne de tendance
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : La phase de run commence quand la figure casse le support de la ligne de tendance du lead-in. Les prix hésitent ou rebondissent parfois sur la ligne avant de la percer. Une fois la cassure réalisée, la phase de run prend le relais et le déclin se poursuit.
**TRADEX-AI C1** : Déclencheur structurel = cassure confirmée de la ligne de tendance lead-in (support) ; signal de retournement baissier.
*Catégorie : signal*

---

### D998 — Support devenu résistance (retracement)
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Après la cassure de la ligne de tendance, un retracement teste parfois le niveau de résistance renouvelé. Des niveaux potentiels de support-devenu-résistance peuvent aussi être identifiés à partir des creux de réaction (reaction lows) à l'intérieur du bump.
**TRADEX-AI C1** : Niveaux support→résistance exploitables pour placement de stop/entrée sur pullback ; cohérent avec l'analyse de pivots.
*Catégorie : gestion_risque_entree*

---

### D999 — Applicabilité multi-timeframe et ampleur du déclin
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md) : Le BARR s'applique aux graphiques journaliers, hebdomadaires ou mensuels. Il est conçu pour identifier les avances spéculatives non soutenables de long terme. Comme les prix montent rapidement pour former le côté gauche du bump, le déclin ultérieur peut être tout aussi féroce.
**TRADEX-AI C1** : Figure multi-timeframe ; ampleur du déclin proportionnelle à l'emballement haussier — utile pour dimensionner objectif/risque.
*Catégorie : structure_marche*

---

### D1000 — Exemple LVLT : contexte et lead-in chiffrés
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md, image_02) : Level Three Communications (LVLT) a formé un BARR après une avance en frénésie spéculative début 2000 (prix de 72 à 132 en 2 mois, avance jugée non soutenable). Le lead-in s'est formé sur trois mois (début oct 1999 à début janv 2000), volume relativement modéré et en déclin durant l'avance nov-déc. La ligne de tendance montant des creux du lead-in formait un angle de 34 degrés (ni trop raide ni trop plat à l'évaluation visuelle).
**TRADEX-AI C1** : Cas pédagogique confirmant les paramètres lead-in (angle ~34°, volume modéré) ; valeur illustrative, aucun paramètre nouveau.
*Catégorie : configuration*

---

### D1001 — Exemple LVLT : bump validé par la règle des 2× (≈3×)
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md, image_02) : Le bump de LVLT a commencé début janvier (accélération avec forte hausse de volume) ; une ligne de tendance tracée prudemment formait un angle de 51 degrés, exactement 50% plus grand que l'angle du lead-in. La distance du plus haut du lead-in à la ligne de tendance était de 13 ; celle du plus haut du bump à la ligne était de 38 — soit près de trois fois plus, validant les excès spéculatifs du bump.
**TRADEX-AI C1** : Illustration numérique de la règle de validation (38 vs 13 ≈ 2,9×, > seuil 2×) et de la règle d'angle (51° = 1,5 × 34°).
*Catégorie : configuration*

---

### D1002 — Exemple LVLT : phase run et retracement chiffrés
🟢 **FAIT VÉRIFIÉ** (Source : bump_and_run_reversal.md, image_02) : Après un plus haut autour de 132$, les prix ont décliné fortement et rebondi sur la ligne de tendance du lead-in. Un plus haut plus bas s'est formé autour de 115$ (flèche rouge) avant la cassure de la ligne de tendance. Le déclin s'est poursuivi jusqu'à 67$ avant un rallye de réaction (avance jusqu'à ~95$, juste sous la ligne de support horizontale) puis une rechute vers de nouveaux plus bas.
**TRADEX-AI C1** : Confirme la séquence rollover → lower high → cassure → run → retracement sous résistance ; trame opératoire de la figure.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D991 | Nature et origine BARR | 🔵 ÉCOLE | C1 | structure_marche |
| D992 | Phase Lead-in (angle 30-45°) | 🟢 | C1 | structure_marche |
| D993 | Phase Bump (pente ≈ 1,5×) | 🟢 | C1 | configuration |
| D994 | Validité du bump (règle 2×) | 🟢 | C1 | configuration |
| D995 | Bump Rollover (sommet) | 🟢 | C1 | structure_marche |
| D996 | Volume (expansion sur le bump) | 🟢 | C2 | structure_marche |
| D997 | Phase Run / cassure ligne tendance | 🟢 | C1 | signal |
| D998 | Support devenu résistance | 🟢 | C1 | gestion_risque_entree |
| D999 | Multi-timeframe / ampleur déclin | 🟢 | C1 | structure_marche |
| D1000 | Exemple LVLT (lead-in 34°) | 🟢 | C1 | configuration |
| D1001 | Exemple LVLT (bump 51°, 38 vs 13) | 🟢 | C1 | configuration |
| D1002 | Exemple LVLT (run / retracement) | 🟢 | C1 | configuration |

**Liens Belkhayate :** Le Bump and Run Reversal n'est PAS une figure Belkhayate (⚫). Lien indirect : sa logique « avance spéculative non soutenable → retournement » et l'usage de support-devenu-résistance recoupent l'analyse de pivots et la prudence face aux extensions excessives ; à utiliser comme lecture de structure, jamais comme signal autonome.

**À vérifier (humain) :**
- D992/D993 — les angles (30-45°, 45-60°) dépendent de l'échelle (semi-log/arithmétique) et de la taille du chart ; NON absolus, non codables en dur sans normalisation. Bulkowski lui-même privilégie l'évaluation visuelle.
- D994/D1001 — la « règle des 2× » est une mesure « arbitraire » (terme de la source) ; heuristique à backtester sur GC/HG/CL/ZW avant toute implémentation d'objectif/validation automatique.
- Tous les chiffres LVLT (72→132, 13, 38, 67, 95, 115) sont des exemples sur action 2000, NON des seuils transposables aux futures cibles.
- Figure chartiste discrétionnaire : détection automatique fiable (3 phases, angles, ratio) non triviale ; validation visuelle humaine recommandée.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
