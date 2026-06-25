# Extraction AdamGrimes — Adding To Positions A Simple Rule
**Source :** `bundles/adamgrimes/adding_to_positions_a_simple_rule.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5091 → D5100 · **Page :** https://www.adamhgrimes.com/adding-to-positions-a-simple-rule/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Règles d'ajout de position et de réduction de risque applicables à GC/HG/CL/ZW en mode Auto et Manuel.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5091 — Règle d'ajout de position : sortir plus qu'on a ajouté
🟢 **FAIT VÉRIFIÉ** (Source : adding_to_positions_a_simple_rule.md) : Si on ajoute à une position existante et que le trade ne se développe pas comme attendu, on doit sortir PLUS que ce qu'on a ajouté. Exemple : ajout de 2 000 unités → sortir au moins 4 000 si le trade échoue, revenant sous la taille de position initiale.
**TRADEX-AI C2** : En mode Auto sur GC/HG/CL/ZW, tout ajout de position déclenché par un signal fort impose une règle asymétrique de sortie : réduction ≥ 2× la taille ajoutée si le prix revient sous le niveau d'ajout.
*Catégorie : gestion_position_active*

### D5092 — Agressivité sur bon trade = risque psychologique amplifié
🟢 **FAIT VÉRIFIÉ** (Source : adding_to_positions_a_simple_rule.md) : Passer d'une position agressive (après ajout) à une position perdante crée l'un des défis psychologiques les plus difficiles du trading. Beaucoup d'erreurs surviennent dans cet espace émotionnel élevé.
**TRADEX-AI C5** : Le mode Manuel doit afficher un avertissement visuel quand une position agrandie revient en perte : "POSITION RENFORCÉE EN PERTE — Appliquer règle asymétrique de sortie."
*Catégorie : psychologie*

### D5093 — La règle de sortie asymétrique protège le trader de lui-même
🔵 **ÉCOLE** (Source : adding_to_positions_a_simple_rule.md) : La règle "sortir plus qu'on a ajouté" est simple mais efficace : elle force à réduire le risque précisément quand la conviction émotionnelle est la plus forte (trade en cours de détérioration après renforcement).
**TRADEX-AI C1** : Dans le moteur TRADEX, la logique de position active doit tracker l'historique des ajouts. Si un ajout est détecté et que le prix franchit le niveau d'ajout à rebours, déclencher alerte de réduction obligatoire.
*Catégorie : gestion_position_active*

### D5094 — L'ajout de position augmente le risque total pris
🟢 **FAIT VÉRIFIÉ** (Source : adding_to_positions_a_simple_rule.md) : Être agressif et "presser" sur un bon trade peut améliorer le P&L, mais crée un compromis direct : plus d'agressivité = plus de risque pris. Cette augmentation de risque doit être consciente et planifiée.
**TRADEX-AI C1** : Le risk_manager.py doit recalculer l'exposition totale après chaque ajout de position et vérifier que le risque cumulé ne dépasse pas le seuil de risque maximal défini dans settings.py.
*Catégorie : gestion_risque_entree*

### D5095 — La règle s'applique au trading directionnel technique simple
🔵 **ÉCOLE** (Source : adding_to_positions_a_simple_rule.md) : Cette règle de sortie asymétrique est spécifiquement adaptée au trading directionnel technique. Elle peut ne pas convenir aux stratégies de "scaling in" où l'on ajoute intentionnellement lorsque le prix va contre l'entrée.
**TRADEX-AI C1** : TRADEX-AI étant un système directionnel basé sur la méthode Belkhayate (trend-following), cette règle s'applique intégralement. L'ajout contre le sens du trade est interdit par les garde-fous existants.
*Catégorie : gestion_position_active*

### D5096 — Éviter la séquence : ajout → trade perdant → grosse perte
🟢 **FAIT VÉRIFIÉ** (Source : adding_to_positions_a_simple_rule.md) : L'une des erreurs classiques de trading est d'avoir un trade gagnant, d'ajouter de manière inappropriée, et de voir ce trade devenir perdant. La règle asymétrique prévient spécifiquement ce scénario.
**TRADEX-AI C5** : Le dashboard doit afficher l'historique des ajouts sur chaque position ouverte, avec le P&L de la portion ajoutée clairement séparé du P&L de la position initiale.
*Catégorie : gestion_position_active*
