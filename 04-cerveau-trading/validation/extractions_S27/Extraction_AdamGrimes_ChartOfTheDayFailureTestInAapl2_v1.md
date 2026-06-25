# Extraction AdamGrimes — Chart Of The Day: Failure Test In AAPL (2)
**Source :** `bundles/adamgrimes/chart_of_the_day_failure_test_in_aapl_2.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5471 → D5482 · **Page :** https://www.adamhgrimes.com/chart-of-the-day-failure-test-in-aapl-2/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : failure test LONG (bear trap / 2B entry) — entrée, stop, gestion risque gap, attentes réalistes du pattern — applicable aux futures GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

---

## DÉCISIONS

### D5471 — Le failure test LONG (bear trap / 2B) : sonde sous support suivie d'un retournement rapide
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Le failure test LONG (aussi appelé bear trap ou 2B entry) est un des patterns les plus fiables d'Adam Grimes. Le marché effectue une sonde sous (pour un support) ou au-dessus (pour une résistance) d'un niveau important, puis se retourne rapidement sans conviction au-delà du niveau. Conceptuellement, le marché a "run the stops" mais n'a pas trouvé de conviction au-delà du niveau.
**TRADEX-AI C1** : Sur GC ou ZW, si le prix casse brièvement sous un support clé (ex. creux d'une consolidation précédente) puis remonte immédiatement au-dessus en 1-2 bougies, c'est un failure test LONG (bear trap). Entrée LONG avec stop sous le plus bas de la sonde. Ce pattern est à scorer positivement dans la grille TRADEX.
*Catégorie : configuration*

---

### D5472 — Le failure test est le premier pattern statistiquement examiné par Grimes dans son livre
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Le failure test a été le premier pattern de trading sélectionné pour une analyse statistique dans "The Art & Science of Technical Analysis" (Adam Grimes) en raison de sa simplicité et de sa fiabilité. Il possède une base statistique solide.
**TRADEX-AI C1** : Statut KB : ce pattern bénéficie d'une validation statistique formelle dans la littérature technique — son inclusion dans TRADEX est justifiée avec badge 🟢 FAIT VÉRIFIÉ et non 🔵 ÉCOLE.
*Catégorie : configuration*

---

### D5473 — Entrée LONG sur failure test : clôture du jour de sonde avec stop sous le plus bas
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : L'entrée correcte sur le failure test LONG est d'entrer long à la clôture du jour de sonde, avec un stop sous le plus bas de ce jour. Cette mécanique s'applique au marché analysé (AAPL, transposable à tout actif).
**TRADEX-AI C1** : Sur CL ou HG, règle d'entrée failure test LONG : entrer long à la clôture de la bougie de sonde sous support. Stop = plus bas de la sonde - 1 tick. Cette règle d'entrée doit être codée dans le module de configuration des setups du moteur TRADEX.
*Catégorie : gestion_risque_entree*

---

### D5474 — Risque de gap overnight sur failure test : utiliser une taille de position réduite
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Il existe toujours un risque de gap down à l'ouverture qui ne remonte pas. Dans ce scénario, la perte réelle peut être plusieurs fois l'anticipation initiale. Il est souvent recommandé de trader ce pattern avec un risque plus faible que les autres trades habituels.
**TRADEX-AI C2** : Règle de gestion TRADEX pour failure test : la taille de position est automatiquement plafonnée à 50% de la taille standard lorsque ce pattern est le signal primaire. Le risk_manager.py doit implémenter ce cas particulier. Cette règle s'applique à GC/CL/HG/ZW.
*Catégorie : gestion_risque_entree*

---

### D5475 — Le failure test seul n'est pas suffisant pour marquer une inflexion majeure
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Le failure test seul n'est généralement pas un pattern qui, isolément, peut déclencher une inflexion majeure de tendance (bien qu'il puisse en marquer une si d'autres facteurs le soutiennent). Les attentes doivent être calibrées : c'est un pattern de mouvement court-terme, pas un signal de retournement de tendance majeur.
**TRADEX-AI C1** : Dans la grille de score /10 TRADEX, le failure test ne peut pas à lui seul justifier un score ≥ 7,0. Il doit être confirmé par au moins un autre cercle d'intelligence (C2 Order Flow, C4 Macro, C7 Corrélations) pour atteindre le seuil de signal valide.
*Catégorie : configuration*

---

### D5476 — En contexte baissier, le failure test LONG est un trade contrariant à objectif limité
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Quand la prépondérance des preuves pointe vers la baisse, un failure test LONG doit être utilisé pour initier un trade contrariant nimble (agile) à court terme, ou pour prendre des profits partiels sur des positions SHORT existantes — pas pour un renversement de tendance.
**TRADEX-AI C1** : Sur GC ou CL en tendance baissière confirmée (score directionnel baissier dominant), un failure test LONG détecté doit déclencher une alerte "PRISE DE PROFIT PARTIELLE SHORT" plutôt qu'un signal LONG à pleine taille. Le moteur doit adapter le label du signal au contexte directionnel dominant.
*Catégorie : gestion_position_active*

---

### D5477 — L'essence du failure test est l'absence de conviction au-delà du niveau clé
🔵 **ÉCOLE** (Source : chart_of_the_day_failure_test_in_aapl_2.md) : Conceptuellement, le failure test représente un marché qui a "run the stops" (déclenché les stops des participants) mais n'a pas trouvé de conviction réelle au-delà du niveau de support/résistance. Ce manque de conviction est le signal de la réversion.
**TRADEX-AI C2** : En Order Flow (ATAS), le failure test doit être confirmé par l'absence de delta positif significatif lors de la sonde (pas de pression acheteuse réelle malgré la cassure). Si le delta est fortement positif lors de la cassure sous support, invalider le failure test — ce n'est pas un piège mais une vraie cassure.
*Catégorie : volume_liquidite*
