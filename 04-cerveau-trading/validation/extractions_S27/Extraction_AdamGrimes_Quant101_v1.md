# Extraction AdamGrimes — Quant 101
**Source :** `bundles/adamgrimes/quant_101.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6391 → D6408 · **Page :** https://www.adamhgrimes.com/quant-101/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Fondements de l'analyse quantitative — définir une edge, tester des conditions, valider statistiquement → cadre méthodologique pour la Knowledge Base Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| *(aucune image dans ce bundle)* | — | — | — |

## DÉCISIONS

### D6391 — Principe fondamental : toute décision de trading est une probabilité
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Quelle que soit la méthode utilisée, prendre une décision de trading signifie implicitement estimer qu'un outcome est plus probable qu'un autre. Ce n'est jamais une certitude — au mieux, c'est "légèrement plus probable". Penser en termes de "x DOIT arriver" ou "x VA arriver" est dangereux.
**TRADEX-AI C1** : Le moteur TRADEX doit toujours exprimer les signaux avec un pourcentage de confiance (ex. "ACHETER — confiance 78%"), jamais comme une certitude. Intégré dans `claude_brain.py` (format de réponse Claude).
*Catégorie : psychologie*

### D6392 — Edge définie : condition + outcome statistiquement vérifiés
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Une "edge" en trading se définit précisément comme : une condition (ou ensemble de conditions) dont on a vérifié statistiquement qu'elle est corrélée à un outcome spécifique plus souvent que le hasard ne le ferait. Sans cette vérification, on n'a pas d'edge.
**TRADEX-AI C1** : Chaque règle dans `KNOWLEDGE_BASE_MASTER.json` devrait idéalement mentionner sa base statistique. Les règles sans validation empirique sont marquées ⚫ HYPOTHÈSE PROJET dans la KB.
*Catégorie : configuration*

### D6393 — Analyse quantitative : définir condition → tester → analyser résultats
🔵 **ÉCOLE** (Source : quant_101.md) : Le pipeline quantitatif complet est : (1) définir précisément une condition, (2) trouver toutes les occurrences historiques, (3) observer ce qui s'est passé après chaque occurrence, (4) comparer aux données de marché générales pour mesurer si la condition a un pouvoir prédictif.
**TRADEX-AI C1** : Ce pipeline est le cadre de validation pour la KB Belkhayate. Avant d'élever une règle de HYPOTHÈSE à FAIT VÉRIFIÉ, elle doit passer ce pipeline (backtest sur données NT8 GC/HG/CL/ZW).
*Catégorie : configuration*

### D6394 — Conditions testables : prix, indicateurs, fondamentaux, macro, sentiment
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Les conditions testables quantitativement incluent : patterns de prix, indicateurs techniques (MACD, etc.), facteurs fondamentaux, données économiques macros, données de sentiment. La seule contrainte : être définie précisément et reproductible sur des centaines/milliers d'occurrences.
**TRADEX-AI C7** : Les 7 cercles TRADEX (Prix, OrderFlow, Institutionnels, Macro, Sentiment, Géopolitique, Corrélations) correspondent exactement aux catégories de conditions testables d'Adam Grimes. Architecture validée.
*Catégorie : configuration*

### D6395 — Données de marché : nettoyage obligatoire avant toute analyse
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : La préparation des données est plus difficile qu'anticipé — dividendes, splits pour actions, rolls pour futures, erreurs dans toutes les sources de données. Le "data wrangling" consomme une part significative du temps d'analyse quantitative.
**TRADEX-AI C1** : Pour NT8 (GC/HG/CL/ZW futures), la gestion des rolls de contrats est critique. Le `data_reader.py` doit gérer le continuous contract adjustment. À documenter dans `DETTE_TECHNIQUE.md` si non géré.
*Catégorie : volume_liquidite*

### D6396 — Timeframe et univers de données : décisions explicites avant le test
🔵 **ÉCOLE** (Source : quant_101.md) : Avant tout test quantitatif, décider explicitement : (1) timeframe (daily, weekly, 1min), (2) marchés inclus, (3) période historique couverte (récente ? 5 ans ? 50 ans ?). Ces choix influencent fortement les résultats et doivent être documentés.
**TRADEX-AI C1** : Pour TRADEX, paramètres standardisés : timeframe = range bars NT8 (décision verrouillée), marchés = GC/HG/CL/ZW, période = minimum 3 ans de données. À fixer dans `settings.py`.
*Catégorie : configuration*

### D6397 — Python : outil recommandé pour l'analyse quantitative sérieuse
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Adam Grimes recommande Python comme outil final pour l'analyse quantitative robuste, après avoir progressé du papier/crayon vers Excel vers des combinaisons d'outils vers Python. Python est justifié par sa flexibilité, sa communauté, et ses bibliothèques analytiques.
**TRADEX-AI C1** : Confirme le choix technologique TRADEX (Python 3.11 + FastAPI). Le moteur d'analyse en `05-saas/` est bien positionné pour intégrer des analyses quantitatives via numpy/pandas.
*Catégorie : configuration*

### D6398 — Analyse quantitative : accessible sans mathématiques avancées
🔵 **ÉCOLE** (Source : quant_101.md) : L'analyse quantitative de base ne nécessite pas de régression linéaire ni d'analyse en composantes principales — ces outils ont leur place mais ne sont pas nécessaires pour la majorité de l'analyse. La méthode "condition → test → résultats" est suffisante pour beaucoup de travaux.
**TRADEX-AI C1** : La grille de scoring /10 de TRADEX (décision D2 verrouillée) est une forme d'analyse quantitative accessible. Pas besoin de ML complexe pour valider les règles Belkhayate de base.
*Catégorie : configuration*

### D6399 — Marchés compétitifs : l'edge doit être comprise et validée
🟡 **SYNTHÈSE** (Source : quant_101.md) : Dans des marchés de plus en plus compétitifs, avoir une edge ne suffit pas — il faut la comprendre profondément. Comprendre une edge signifie savoir pourquoi elle fonctionne, pas seulement qu'elle a fonctionné historiquement.
**TRADEX-AI C1** : Pour chaque règle Belkhayate dans la KB, documenter non seulement "quoi" (la règle) mais "pourquoi" (le mécanisme économique/comportemental sous-jacent). Enrichit la qualité de l'analyse Claude.
*Catégorie : psychologie*

### D6400 — Raisonnement probabiliste : éviter "x doit arriver"
🔵 **ÉCOLE** (Source : quant_101.md) : La pensée dangereuse en trading est celle qui dit "x DOIT arriver", "x VA arriver", "x EST OBLIGÉ d'arriver". Au mieux, x est légèrement plus probable. Ce mindset erroné conduit à des tailles de position inadaptées et à ignorer les stops.
**TRADEX-AI C1** : Le disclaimer légal permanent dans l'interface TRADEX doit inclure : "Chaque signal est une probabilité, jamais une certitude". Le Mode Auto ne dépasse jamais le seuil de confiance minimum défini (≥ 7.0/10 + R/R ≥ 1:2).
*Catégorie : psychologie*

### D6401 — Test statistique : comparer les résultats post-condition aux données générales
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : L'étape clé du test quantitatif est la comparaison : les outcomes après une condition doivent être comparés aux outcomes sur l'ensemble des données sans condition. Si la différence n'est pas significative, la condition n'a pas de pouvoir prédictif réel.
**TRADEX-AI C1** : Pour valider les règles Belkhayate (COG, Énergie, Timing), le backtest doit inclure un groupe contrôle (entrées aléatoires aux mêmes dates) pour mesurer l'alpha réel de la méthode.
*Catégorie : configuration*

### D6402 — Progressivité des outils : crayon→Excel→Python
🔵 **ÉCOLE** (Source : quant_101.md) : Adam Grimes a progressé du crayon/papier vers Excel vers des combinaisons d'outils vers Python. Cette progression suggère qu'il est valide de commencer simplement et d'augmenter la sophistication au fur et à mesure que les besoins l'exigent.
**TRADEX-AI C1** : Pour TRADEX Phase C (collecteurs NT8), commencer par des analyses simples en Python (rolling returns, win rate par condition) avant d'investir dans des frameworks de backtest complexes.
*Catégorie : configuration*

### D6403 — Condition précise : requis pour tester sur centaines d'occurrences
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Pour être testable quantitativement, une condition doit être définie avec une précision suffisante pour être identifiable de manière reproductible sur des centaines ou milliers d'occurrences historiques. Les définitions vagues ("fort momentum", "bonne structure") ne sont pas testables.
**TRADEX-AI C1** : Les règles Belkhayate dans la KB doivent être rédigées avec des valeurs numériques précises (ex. "COG(180,3) > prix actuel" plutôt que "COG au-dessus du prix"). Améliore la testabilité et la qualité des signaux Claude.
*Catégorie : configuration*

### D6404 — Probabilité : paradigme unique et suffisant pour le trading
🟡 **SYNTHÈSE** (Source : quant_101.md) : Indépendamment de la méthode utilisée (TA, fondamentale, quantitative, macro), tous les traders et investisseurs font la même chose : estimer qu'un outcome est plus probable qu'un autre. La méthode change, le paradigme probabiliste reste constant.
**TRADEX-AI C1** : Unifie la méthode Belkhayate (discrétionnaire) avec le moteur TRADEX (quantitatif) : les deux expriment des probabilités. Le score /10 quantifie la probabilité Belkhayate de manière comparable.
*Catégorie : psychologie*

### D6405 — Données futures vs données historiques : hypothèse de stationnarité
🟡 **SYNTHÈSE** (Source : quant_101.md) : L'analyse quantitative repose sur un "petit saut de foi" : supposer que les conditions qui ont prédit certains outcomes dans le passé continueront à le faire dans le futur (si le travail est bien fait). Cette hypothèse n'est pas garantie mais est la base du trading systématique.
**TRADEX-AI C1** : La KB Belkhayate (~1313 règles) repose sur cette même hypothèse de stationnarité des comportements de marché. À mentionner dans le disclaimer du Mode Auto.
*Catégorie : psychologie*

### D6406 — Analyse quantitative : pas intimidante dans sa forme de base
🔵 **ÉCOLE** (Source : quant_101.md) : Malgré son image technique complexe, l'analyse quantitative dans sa forme de base est simple : "définir une condition, la tester, analyser les résultats". Cette forme de base est accessible à la plupart des traders motivés.
**TRADEX-AI C1** : La validation des règles KB Belkhayate peut commencer par des analyses simples (win rate sur signaux simples dans NT8 Strategy Analyzer) avant le déploiement du moteur Python complet.
*Catégorie : configuration*

### D6407 — Données futures : sélection de la période historique critique
🟡 **SYNTHÈSE** (Source : quant_101.md) : Le choix de la période historique (récente vs 5 ans vs 50 ans) impacte les résultats et doit être explicite et justifié. Une période trop courte donne peu d'occurrences (non statistiquement significatif) ; une période trop longue peut inclure des régimes de marché non représentatifs.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, recommandation : utiliser minimum 5 ans de données journalières (couverture de plusieurs cycles de marché incluant haussier, baissier, range). À documenter dans `settings.py`.
*Catégorie : configuration*

### D6408 — Gestion des données futures : dividendes/splits/rolls comme problème réel
🟢 **FAIT VÉRIFIÉ** (Source : quant_101.md) : Les erreurs dans les données et les ajustements nécessaires (dividendes, splits actions, rolls futures) représentent un problème réel et significatif qui consomme "trop" de temps selon l'auteur. Toutes les sources de données ont des erreurs.
**TRADEX-AI C1** : Pour les futures GC/HG/CL/ZW via NT8/Rithmic, documenter la politique de roll contract dans `data_reader.py`. Utiliser les "continuous contracts" NT8 avec back-adjustment pour la cohérence des séries historiques.
*Catégorie : volume_liquidite*
