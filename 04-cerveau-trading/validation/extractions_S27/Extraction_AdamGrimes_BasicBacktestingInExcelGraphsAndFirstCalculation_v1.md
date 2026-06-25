# Extraction AdamGrimes — Basic Backtesting in Excel: Graphs and First Calculations
**Source :** `bundles/adamgrimes/basic_backtesting_in_excel_graphs_and_first_calculations.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5231 → D5245 · **Page :** https://www.adamhgrimes.com/basic-backtesting-in-excel-graphs-and-first-calculations/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Calcul des retours, corrélations inter-actifs et construction progressive de calculs complexes — base méthodologique pour la matrice de corrélations live 30j de TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5231 — Calcul du retour journalier par ratio prix(J)/prix(J-1) - 1
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : La formule standard pour le retour journalier en pourcentage est : retour(J) = prix(J) / prix(J-1) - 1. Cette formule est la brique de base de toute analyse quantitative de performance. Elle permet le calcul de retours normalisés comparables entre actifs de niveaux de prix différents.
**TRADEX-AI C7** : La matrice de corrélations live 30j (GC/HG/CL/ZW/ES/VX/MBT/6J) dans correlations.py utilise des retours normalisés et non des prix bruts. Cette normalisation est essentielle pour que la corrélation GC/CL soit comparable à la corrélation ES/VX sans biais de niveau de prix.
*Catégorie : correlations*

### D5232 — La puissance de la réplication de formule dans un tableur
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : Copier une formule vers le bas (ou vers la droite) dans Excel adapte automatiquement les références de cellules. Calculer des retours pour SPY puis copier vers la droite donne les mêmes retours pour TLT avec le même code. Cette réplicabilité est le fondement de l'efficacité d'un tableur.
**TRADEX-AI C7** : Le module correlations.py implémente ce même principe : une seule formule de corrélation appliquée à toutes les paires d'actifs (28 paires pour 8 actifs). La maintenance du code est réduite car une correction dans la formule se propage à toutes les paires.
*Catégorie : correlations*

### D5233 — Décomposer les calculs complexes en étapes intermédiaires
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : Une formule comme « excès de retour TLT sur SPY » peut être calculée en une seule expression complexe ou en deux étapes avec colonnes intermédiaires. La meilleure pratique est de décomposer en étapes : calcul SPY_ret, calcul TLT_ret, puis TLT_ret - SPY_ret. Cela facilite le débogage et la compréhension.
**TRADEX-AI C7** : Dans correlations.py, chaque étape de calcul (normalisation, fenêtre glissante, matrice de covariance, normalisation en corrélation) doit être une fonction séparée avec un nom explicite. Un bug dans le calcul de corrélation GC/CL doit pouvoir être isolé rapidement.
*Catégorie : correlations*

### D5234 — L'excès de retour : métrique de performance relative inter-actifs
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : L'excès de retour d'un actif A sur un actif B (retour_A - retour_B) mesure la performance relative. Si TLT sur-performe SPY, l'excès de retour est positif. Cette métrique est fondamentale pour analyser la rotation entre actifs (flight-to-safety, risk-on/risk-off).
**TRADEX-AI C5** : L'excès de retour de VX (VIX) sur ES (S&P 500) est un signal de sentiment clé du Cercle C5. Quand VX sur-performe fortement, c'est un signal risk-off qui doit déclencher une revue du Mode Auto. Cette métrique est à intégrer dans la vérification niveau 2 du moteur événementiel.
*Catégorie : indicateurs_momentum*

### D5235 — L'obligation de labelliser toutes les colonnes de calcul
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : Ne pas labelliser les colonnes de calcul conduit à ne plus comprendre son propre travail après quelques jours. « Weeks later? Forget it; you're basically starting over. » Adam Grimes recommande des noms explicites (ex : SPY_ret, TLT_ret) et des notes dans les feuilles.
**TRADEX-AI C1** : Chaque clé du JSON KNOWLEDGE_BASE_MASTER.json doit avoir un nom explicite et non ambigu. Les 45 règles dans A_VERIFIER_HUMAIN.md sont précisément celles dont la source ou la signification est ambiguë — un problème de labellisation.
*Catégorie : configuration*

### D5236 — Visualisation graphique comme outil de validation des données
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : La visualisation graphique permet de détecter rapidement des anomalies dans les données (gaps, valeurs aberrantes, erreurs de saisie) qu'une analyse numérique seule peut manquer. Excel permet de créer des graphiques basiques rapidement pour une validation visuelle initiale.
**TRADEX-AI C1** : Le dashboard React (05-saas/) affiche les données NT8 en temps réel précisément pour permettre cette validation visuelle. Une anomalie visible dans le graphique (saut de prix inexplicable, zéro soudain) doit déclencher le staleness_monitor avant tout signal.
*Catégorie : structure_marche*

### D5237 — La MA mobile comme premier calcul sur série de prix
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : La moyenne mobile (MA) est le premier calcul quantitatif utile sur une série de prix. Elle se calcule avec AVERAGE(cellule_début:cellule_fin) sur une fenêtre glissante de N périodes. La MA20 de SPY est donnée comme exercice pratique de base.
**TRADEX-AI C1** : La MA Belkhayate (COG, Belkhayate Center of Gravity) est une moyenne pondérée centrée, plus sophistiquée qu'une simple MA. Son calcul en Python (engine/) suit le même principe de fenêtre glissante, avec les paramètres figés : période=180, ordre=3, coefficients 0,618/1,618.
*Catégorie : indicateurs_tendance*

### D5238 — L'ordre des opérations et les parenthèses dans les formules
🔵 **ÉCOLE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : L'ordre normal des opérations mathématiques s'applique dans Excel. Pour tout calcul plus complexe qu'une seule opération, l'utilisation de parenthèses explicites est recommandée pour éviter les erreurs d'interprétation : (C3/C2-1)-(B3/B2-1) est correct ; C3/C2-1-B3/B2-1 est ambigu.
**TRADEX-AI C1** : Les formules Python du moteur (claude_brain.py, correlations.py) doivent utiliser des parenthèses explicites pour tous les calculs multi-étapes. La lisibilité prime sur la concision pour faciliter le débogage.
*Catégorie : configuration*

### D5239 — La corrélation négative obligatoire GC/DX comme validation de données
🟢 **FAIT VÉRIFIÉ** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : L'excès de retour entre actifs corrélés négativement (comme or/dollar) est un outil de validation des données. Si les retours journaliers de GC et DX sont positicement corrélés sur une longue période, c'est une anomalie qui signale un problème dans les données.
**TRADEX-AI C7** : La corrélation GC/DX dans la matrice 30j doit être structurellement négative (typiquement -0,5 à -0,8). Une corrélation positive persistante GC/DX doit déclencher une alerte dans correlations.py car elle signale soit une anomalie de marché extrême, soit un problème de données.
*Catégorie : correlations*

### D5240 — La visualisation permet de distinguer tendance de bruit
🟡 **SYNTHÈSE** (Source : basic_backtesting_in_excel_graphs_and_first_calculations.md) : Tracer une série de prix et sa MA mobile ensemble permet de distinguer visuellement la tendance (filtrée par la MA) du bruit court terme (oscillations autour de la MA). Ce principe visuel est la fondation de l'analyse de tendance.
**TRADEX-AI C1** : L'affichage dans le dashboard React de la MA Belkhayate (COG) superposée au prix NT8 permettra à Abdelkrim de distinguer la structure de tendance du bruit intraday. Ceci est la validation visuelle primaire avant toute décision en Mode Manuel.
*Catégorie : structure_marche*
