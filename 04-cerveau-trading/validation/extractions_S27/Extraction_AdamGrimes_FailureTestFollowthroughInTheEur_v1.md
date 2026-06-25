# Extraction AdamGrimes — Failure Test Followthrough in the EUR
**Source :** `bundles/adamgrimes/failure_test_followthrough_in_the_eur.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image extraite dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5751 → D5763 · **Page :** https://www.adamhgrimes.com/failure-test-followthrough-in-the-eur/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Suivi concret d'un Failure Test sur marché de change — principes de gestion position et de lecture du range applicables aux commodities GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image extraite dans ce bundle | — | — |

## DÉCISIONS

### D5751 — L'analyse technique sur devises exige un état d'esprit différent
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : Les devises sont pilotées par l'offre/demande de chaque monnaie dans la paire, elle-même secondaire à des forces économiques primaires (balance commerciale, taux d'intérêt). Cela crée un environnement de trading légèrement différent des actions et des commodities — l'AT y est applicable mais requiert une adaptation.
**TRADEX-AI C4** : Pour l'actif DX (Dollar Index, Cercle Confirmation), tenir compte que les signaux AT purs sont filtrés par des forces macro (taux Fed, balance commerciale) — ne jamais traiter DX comme une commodity pure.
*Catégorie : macro_evenements*

### D5752 — Mean-reversion court terme amortie sur les devises
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : La mean-reversion court terme sur les devises est atténuée (muted) par rapport aux actions ou commodities. De même, le momentum long terme y est plus faible. Résultat : environnement de trading légèrement plus difficile.
**TRADEX-AI C7** : En corrélations, le DX ne réagit pas aussi franchement aux niveaux techniques que GC/CL — son rôle est de confirmation macro, pas de générateur de signal direct.
*Catégorie : correlations*

### D5753 — Failure Test valide même dans un environnement difficile
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : Même dans l'environnement difficile des devises, les outils simples et les patterns fonctionnent. L'EUR/USD a formé un Failure Test propre au sommet d'une semaine, avec suivi jusqu'au bas du range la semaine suivante.
**TRADEX-AI C1** : Confirmation empirique — le Failure Test est robuste même sur des marchés dont la mean-reversion est amortie. Sur GC/HG/CL/ZW (commodities, mean-reversion plus franche), l'efficacité attendue est supérieure.
*Catégorie : configuration*

### D5754 — Gestion obligatoire : couvrir une partie du short avant le bas du range
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : Grimes précise que "la gestion prudente du trade nécessite pratiquement que vous ayez déjà couvert une partie du short" avant que le prix atteigne le bas du range. Une prise de profit partielle en cours de route est non optionnelle sur ce type de trade.
**TRADEX-AI C1** : Règle gestion position — sur un Failure Test SHORT, prendre profit partiel au milieu du range (50% de la distance entre résistance et support) ; ne pas tenir la totalité de la position jusqu'au bas du range.
*Catégorie : gestion_position_active*

### D5755 — Surveiller un Failure Test miroir au bas du range
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : Après le suivi baissier du Failure Test haut, surveiller un possible Failure Test au bas du range : (a) signal d'entrée long dans la consolidation hebdomadaire (upside à venir), ou (b) continuation baissière sous le bas du range si le test échoue.
**TRADEX-AI C1** : Pattern de range TRADEX — après un Failure Test haut confirmé sur GC/HG/CL/ZW, placer une alerte sur le support inférieur ; le comportement du prix à ce niveau détermine la prochaine direction.
*Catégorie : structure_marche*

### D5756 — Le trading n'est pas de la prédiction : avoir un plan d'action
🔵 **ÉCOLE** (Source : failure_test_followthrough_in_the_eur.md) : L'objectif n'est pas de prédire ce qui va se passer, mais d'avoir un plan d'action (gameplan) permettant de prendre des décisions intelligentes au fur et à mesure que le marché évolue. Les patterns identifient des zones de probabilités favorables, pas des certitudes.
**TRADEX-AI C1** : Dans le cerveau Claude, le signal TRADEX doit toujours accompagner un plan conditionnel (si prix fait X → action Y ; si fait Z → action W), pas seulement un verdict binaire.
*Catégorie : psychologie*

### D5757 — Prise de décision en temps réel après déclenchement d'un Failure Test
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_followthrough_in_the_eur.md) : Une fois le Failure Test déclenché et le suivi en cours, la question active n'est plus "va-t-il fonctionner ?" mais "que faire maintenant ?" — surveiller le prochain niveau de résistance/support pour ajuster la position.
**TRADEX-AI C1** : En mode Manuel TRADEX, après déclenchement d'un signal Failure Test, afficher le niveau suivant (support ou résistance) comme cible et point de décision, pas seulement le signal initial.
*Catégorie : gestion_position_active*
