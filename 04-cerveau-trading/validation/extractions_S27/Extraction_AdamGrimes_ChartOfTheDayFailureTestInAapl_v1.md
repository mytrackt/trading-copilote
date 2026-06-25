# Extraction AdamGrimes — Chart Of The Day: Failure Test In AAPL
**Source :** `bundles/adamgrimes/chart_of_the_day_failure_test_in_aapl.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5451 → D5460 · **Page :** https://www.adamhgrimes.com/chart-of-the-day-failure-test-in-aapl/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : pattern failure test SHORT (probe au-dessus résistance + retournement) — entrée, stop, gestion du risque de gap — applicable aux futures GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

---

## DÉCISIONS

### D5451 — Le failure test SHORT : sonde au-dessus de la résistance suivie d'un retournement immédiat
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl.md) : Le failure test (version short) est une brève sonde au-dessus d'un niveau de résistance, immédiatement suivie d'un échec (failure) et d'un fort retournement baissier. C'est le premier pattern de trading examiné statistiquement dans "The Art & Science of Technical Analysis" (Adam Grimes). Il existe une tendance statistique claire et forte en faveur de ce pattern.
**TRADEX-AI C1** : Sur GC, si le prix dépasse brièvement un précédent sommet significatif (ex. résistance hebdomadaire) puis clôture en dessous dans la même session, ce setup failure test SHORT est un signal d'entrée vendeuse exploitable avec stop au-dessus du plus haut de la sonde.
*Catégorie : configuration*

---

### D5452 — Entrée sur le failure test SHORT : clôture de la veille ou niveau équivalent en intraday
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl.md) : L'entrée SHORT sur ce pattern peut être initiée sur la clôture de la veille (J-1) ou dans la session suivante au même niveau ou plus haut, avec un stop placé au-dessus du plus haut de J-1 (la sonde de résistance).
**TRADEX-AI C1** : Sur CL ou HG, règle d'entrée failure test SHORT : entrer short à la clôture du jour de sonde ou le lendemain au même niveau. Stop = plus haut de la bougie de sonde + 1 tick. Cette mécanique doit être encodée comme règle d'entrée dans le module de configuration des setups TRADEX.
*Catégorie : gestion_risque_entree*

---

### D5453 — Le risque de gap est inhérent aux trades contrariants dans les marchés en forte tendance
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl.md) : La taille de position pour le failure test est problématique car dans les marchés en forte tendance haussière, un trade short contrariant expose à un risque de gap (gap à la hausse overnight). La position doit donc être dimensionnée prudemment.
**TRADEX-AI C2/C1** : Règle de gestion : dans un marché GC ou CL en forte tendance haussière (ex. 5+ séances consécutives haussières), les signaux SELL du failure test doivent automatiquement recevoir un coefficient de réduction de taille = 0,5 (demi-position standard). Le risk manager TRADEX doit implémenter ce paramètre.
*Catégorie : gestion_risque_entree*

---

### D5454 — La consolidation prolongée contre une résistance est favorable aux haussiers (pas aux baissiers)
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_failure_test_in_aapl.md) : La consolidation continue et la pression prolongée contre une résistance sont constructives pour les acheteurs, et non pour les vendeurs. Un failure test ne se valide que si le retournement est immédiat et net — une consolidation prolongée au niveau invalide le setup.
**TRADEX-AI C1** : Sur ZW ou GC, si le prix stagne 3+ sessions contre une résistance sans retournement net, invalider tout signal failure test SHORT potentiel. Ce filtre "consolidation au niveau = invalide" doit être intégré dans la détection automatique de ce pattern.
*Catégorie : configuration*

---

### D5455 — Le failure test exige une attention prioritaire même dans des contextes incertains
🔵 **ÉCOLE** (Source : chart_of_the_day_failure_test_in_aapl.md) : Même si de nombreux niveaux de support potentiels existent et que beaucoup de traders hésitent à shorter après un mouvement haussier, le failure test constitue un pattern "qui exige l'attention" (demands attention) — sa tendance statistique justifie une surveillance systématique.
**TRADEX-AI C1** : TRADEX doit inclure le failure test (SHORT et LONG) dans sa liste de patterns prioritaires à surveiller automatiquement sur GC/CL/HG/ZW — un alert spécifique "FAILURE TEST DÉTECTÉ" doit être affiché dans le dashboard Manuel même en l'absence de signal global ≥ 7,0.
*Catégorie : configuration*
