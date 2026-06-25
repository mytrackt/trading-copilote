# Extraction AdamGrimes — Basic Backtesting In Excel Statistical Tests
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_statistical_tests.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5331 → D5345 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-statistical-tests/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthode rigoureuse pour valider des conditions de signal via tests statistiques conditionnels et études d'événements.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5331 — Deux types de questions statistiques pour backtest
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Il existe deux façons distinctes d'interroger les données de marché : (1) les rendements conditionnels — "quels rendements ont été observés QUAND la condition X était vraie ?" — et (2) l'étude d'événements — "qu'est-ce que le marché a FAIT APRÈS que X s'est produit ?". Ce sont des questions fondamentalement différentes qui nécessitent des outils différents.
**TRADEX-AI C1** : Lors du backtesting de conditions de signal Belkhayate (ex. : prix au-dessus de la BGC), distinguer explicitement si l'on teste la performance PENDANT la condition (rendements conditionnels) ou APRÈS un croisement/événement (étude d'événements). Ne pas mélanger les deux types de tests.
*Catégorie : configuration*

### D5332 — Rendements conditionnels vs rendements inconditionnels
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Dans un exemple SPY sur 20 SMA, les rendements conditionnels (prix au-dessus de la MA) étaient de 0.263%/jour (94% annualisé) vs rendements inconditionnels 0.028%/jour (7.4% annualisé) — ordre de grandeur de différence. Ce type de résultat spectaculaire doit immédiatement déclencher un test TLAR (trop beau = erreur probable).
**TRADEX-AI C1** : Tout signal Belkhayate montrant des rendements conditionnels 10x supérieurs aux rendements inconditionnels doit être soumis à un audit TLAR avant intégration dans la KB. Un résultat spectaculaire est un signal d'alarme, pas de validation.
*Catégorie : gestion_risque_entree*

### D5333 — Le test TLAR (That Looks About Right)
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Le test TLAR est un garde-fou systématique : chaque résultat numérique ou statistique doit être évalué selon "est-ce raisonnable ou trop beau pour être vrai ?". Si un résultat semble trop bon, c'est une erreur dans le test, pas un alpha réel. Ce test est la première ligne de défense contre les biais de données.
**TRADEX-AI C1** : Intégrer le test TLAR comme étape obligatoire dans le pipeline de validation KB (validation/). Tout résultat de backtest dépassant 2x la performance attendue doit être refusé automatiquement et marqué A_VERIFIER_HUMAIN avant toute intégration dans KNOWLEDGE_BASE_MASTER.json.
*Catégorie : gestion_risque_entree*

### D5334 — Étude d'événements : définition d'un croisement de moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Un croisement de MA est défini précisément comme : "aujourd'hui prix ferme AU-DESSUS de la MA ET hier prix fermait EN-DESSOUS ou SUR la MA". Cette double condition (ET logique) est nécessaire — définir "au-dessus seulement" sans la condition temporelle passée capture tous les jours en tendance, pas le point d'entrée.
**TRADEX-AI C1** : Pour les signaux Belkhayate basés sur un croisement (ex. : BGC, Direction), la condition d'entrée doit être une DOUBLE condition temporelle : état aujourd'hui ET état différent hier. Un signal "est actuellement au-dessus de X" sans vérification du changement d'état constitue une erreur de définition.
*Catégorie : configuration*

### D5335 — Horizon temporel d'étude d'événements : 5 et 10 jours
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Les horizons standard pour une étude d'événements en trading : 5 jours de trading ≈ 1 semaine, 20 jours ≈ 1 mois, 60 jours ≈ 1 trimestre, 252 jours ≈ 1 an. Les mois à 5 semaines et jours fériés rendent ces chiffres ronds approximatifs.
**TRADEX-AI C1** : Pour les backtests de signaux TRADEX-AI, utiliser les horizons 5J et 10J comme horizons de mesure standard des rendements post-signal. L'horizon 20J est pertinent pour les actifs GC/HG/CL/ZW en tant qu'horizon mensuel.
*Catégorie : configuration*

### D5336 — Cohérence des formules dans tout le backtest
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Une erreur fréquente en backtesting : modifier une condition dans une cellule sans propager le changement à toute la colonne. Tout changement de formule ou de condition doit être appliqué uniformément sur toute la série de données — une incohérence partielle biaise l'ensemble du test.
**TRADEX-AI C1** : Dans tout script de backtest Python pour TRADEX-AI, les conditions de signal doivent être définies comme fonctions vectorisées appliquées à l'ensemble de la série temporelle, jamais comme valeurs ponctuelles. Utiliser pandas.Series.apply() ou opérations vectorielles numpy pour garantir la cohérence.
*Catégorie : configuration*

### D5337 — Apprentissage itératif du backtesting
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_statistical_tests.md) : Grimes insiste que le backtesting est un processus d'apprentissage progressif : il ne faut pas se précipiter. Comprendre POURQUOI les résultats apparaissent demande du temps d'expérimentation — manipuler, modifier les paramètres, trouver différentes façons d'interroger les mêmes données avant de conclure.
**TRADEX-AI C1** : La validation KB ne doit pas être précipitée. Un ticket "À TRAITER" reste en A_VERIFIER_HUMAIN jusqu'à ce qu'Abdelkrim ait eu le temps de valider manuellement les règles extraites — pas de fusion automatique même si l'audit algorithmique passe.
*Catégorie : psychologie*

### D5338 — Transition du backtest au système de trading appliqué
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_statistical_tests.md) : Il y a plusieurs étapes entre un backtest statistique valide et un système de trading opérationnel : vérifier les erreurs du test, identifier les autres statistiques pertinentes, interpréter correctement les stats, continuer à apprendre et développer les compétences, et seulement ensuite appliquer au trading réel.
**TRADEX-AI C1** : Le pipeline TRADEX-AI suit ce même principe : une règle validée en backtest (04-cerveau-trading/validation/) ne passe en KNOWLEDGE_BASE_MASTER.json qu'après validation humaine (OK utilisateur). La validation statistique n'est qu'une étape, pas la conclusion.
*Catégorie : configuration*
