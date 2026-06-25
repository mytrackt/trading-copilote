# Extraction AdamGrimes — Basic Backtesting in Excel: Conditions, Logic, and Stats
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_conditions_logic_and_stats.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5191 → D5205 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-conditions-logic-and-stats/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthodologie de test des conditions de marché (indicateurs binaires, logique AND/OR) — directement applicable à la construction et validation des règles de signal du moteur TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5191 — Variable indicatrice binaire pour condition de marché
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Une condition de marché (ex : prix > MA20) peut être encodée comme une variable indicatrice binaire (1=vrai, 0=faux). La moyenne de cette colonne donne directement le pourcentage de temps où la condition est vraie. Pour SPY (8/1/05–10/19/15), le prix est au-dessus de la MA20 à 62,6% du temps.
**TRADEX-AI C1** : Le moteur de scoring /10 encode chaque condition Belkhayate (BGC haussier, Direction positive, Énergie > seuil…) en variable binaire avant agrégation. Ce principe est la fondation du scoring déterministe.
*Catégorie : indicateurs_tendance*

### D5192 — Le prix est au-dessus de la MA plus de 50% du temps en marché haussier
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Dans un marché à biais haussier long terme (SPY 2005–2015), le prix clôture au-dessus de la MA20 62,6% du temps. Ce résultat contre-intuitif s'explique par l'asymétrie des marchés : les phases de tendance haussière sont plus longues que les corrections.
**TRADEX-AI C1** : En marché de tendance (GC, CL…), le signal Belkhayate « prix au-dessus de la MA Belkhayate » a naturellement une fréquence de 60%+ sans être prédictif per se. Le critère Belkhayate doit être combiné avec d'autres conditions (Direction, BGC, Énergie) pour obtenir un edge réel.
*Catégorie : indicateurs_tendance*

### D5193 — Erreur de logique : la troisième condition (égalité)
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Tester uniquement « prix > MA » puis supposer que « prix ≤ MA » = (1 - % au-dessus) est une erreur. Il existe une troisième condition : prix = MA (clôture à l'identique). La pratique correcte est de tester séparément « au-dessus » et « en dessous » et de vérifier que le résidu (ni l'un ni l'autre) correspond aux périodes égales.
**TRADEX-AI C1** : Dans le scoring /10, les conditions de signal doivent avoir 3 états : positif (+), négatif (−), neutre (=). Un score neutre ne doit pas être assimilé à un score positif ou négatif. Le moteur de scoring doit gérer explicitement les cas limites.
*Catégorie : configuration*

### D5194 — Test de conditions complexes avec logique AND/OR
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Les conditions de marché complexes (ex : SPY en hausse 2 jours consécutifs) se construisent avec des opérateurs logiques AND, OR, NOT. Ces opérateurs permettent de construire n'importe quel test. La formule exemple : IF(AND(B21>B20, B20>B19), 1, 0) teste deux conditions simultanées.
**TRADEX-AI C1** : La règle d'entrée TRADEX-AI (3/4 actifs trading alignés ET 2/3 confirmation alignés) est exactement une logique AND imbriquée. Ce principe est la fondation de la validation des conditions d'entrée au niveau 1 du moteur événementiel.
*Catégorie : gestion_risque_entree*

### D5195 — Généralisation paramétrique des conditions (N jours consécutifs)
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Une condition comme « N jours haussiers consécutifs » peut être généralisée avec la fonction OFFSET() pour tester différentes valeurs de N sans modifier la formule de base. Ceci permet une analyse de sensibilité rapide.
**TRADEX-AI C1** : Lors de la validation des seuils Belkhayate (période COG=180, ordre=3, coefficients 0,618/1,618), une analyse de sensibilité paramétrique ±20% doit être conduite pour confirmer la robustesse. Les paramètres figés en S11 doivent être retenus uniquement si les résultats sont stables autour de ces valeurs.
*Catégorie : configuration*

### D5196 — Apprendre par la pratique, pas par la lecture seule
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : La compétence en analyse quantitative s'acquiert uniquement par la pratique répétée (faire des erreurs, se tromper, corriger). Lire des exemples ne suffit pas. La répétition 4–5 fois du même exercice sur des actifs différents est la méthode d'apprentissage recommandée.
**TRADEX-AI C1** : Le pipeline TRANSVIDEO (transcription → extraction → audit → fusion) est conçu pour être répété sur chaque source, pas exécuté une seule fois. La robustesse de la KB s'obtient par l'accumulation de règles validées sur des sources multiples et indépendantes.
*Catégorie : psychologie*

### D5197 — Le pourcentage « au-dessus de la MA » comme métrique de tendance
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Calculer le pourcentage de temps où le prix est au-dessus de la MA est une mesure simple mais utile de l'état de tendance d'un actif. Un pourcentage > 60% indique un régime haussier structurel ; un pourcentage < 40% indique un régime baissier.
**TRADEX-AI C1** : Pour les 4 actifs tradables (GC, HG, CL, ZW), monitorer le % du temps au-dessus de la MA Belkhayate (période adaptée) donne un indicateur de régime de marché rapide. À intégrer dans le contexte d'analyse du Cercle C1 (Prix).
*Catégorie : indicateurs_tendance*

### D5198 — Médiane vs moyenne : test de l'asymétrie de distribution
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Comparer la moyenne et la médiane d'une série de prix ou de retours permet de détecter une asymétrie de distribution. Si moyenne > médiane, la distribution est asymétrique à droite (queue haussière). Ce test simple peut révéler des propriétés importantes d'un actif.
**TRADEX-AI C1** : Les retours de l'Or (GC) sont connus pour une asymétrie négative dans certaines configurations (fuite vers la sécurité). Tester médiane vs moyenne des retours GC sur range bars NT8 permettra de calibrer les attentes de performance du moteur sur cet actif.
*Catégorie : structure_marche*

### D5199 — Importance des labels et commentaires dans les feuilles de calcul
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Ne pas labelliser les colonnes de calcul conduit inévitablement à devoir tout refaire après quelques jours. Les notes et labels sont un investissement en temps qui se rentabilise immédiatement lors de la relecture ou du débogage.
**TRADEX-AI C1** : Chaque décision KB dans KNOWLEDGE_BASE_MASTER.json doit avoir un champ `source`, `categorie`, `cercle`, et `statut` renseignés. Les 45 règles AMBIGU sans contexte suffisant dans A_VERIFIER_HUMAIN.md illustrent le coût du manque de documentation.
*Catégorie : configuration*

### D5200 — Vérifier que les résultats ont du sens avant de les utiliser
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_conditions_logic_and_stats.md) : Après chaque calcul statistique, s'arrêter et vérifier que le résultat est cohérent avec la réalité. Un résultat surprenant peut signifier : (a) une erreur de calcul, (b) une hypothèse incorrecte, (c) un insight réel. Explorer les trois pistes avant de conclure.
**TRADEX-AI C1** : Le moteur Claude API (claude_brain.py) génère un signal avec un niveau de confiance. Si la confiance est > 80% pour un actif en consolidation, c'est suspect. Le circuit breaker et le staleness monitor jouent ce rôle de vérification de cohérence avant exécution.
*Catégorie : gestion_risque_entree*
