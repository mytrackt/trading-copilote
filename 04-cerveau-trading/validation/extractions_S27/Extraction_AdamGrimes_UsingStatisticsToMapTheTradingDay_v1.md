# Extraction AdamGrimes — Using Statistics to Map the Trading Day
**Source :** `bundles/adamgrimes/using_statistics_to_map_the_trading_day.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7311 → D7326 · **Page :** https://www.adamhgrimes.com/using-statistics-to-map-the-trading-day/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Exploitation statistique du NYSE TICK comme indicateur de sentiment intraday — quantification des percentiles extrêmes pour détecter des conditions de marché anormales (C5/C2).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D7311 — Outil : NYSE TICK comme indicateur de sentiment intraday de la première minute
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Le NYSE TICK (différence entre le nombre d'actions en tick haussier et baissier à un instant T) peut être mesuré sur la première minute de trading pour évaluer l'extrémité des conditions d'ouverture. L'auteur utilise des données historiques depuis 1997 sur 2,2 millions d'observations de barres TICK d'1 minute.
**TRADEX-AI C5** : Pour ES (actif de confirmation), inclure le NYSE TICK de la première minute dans les données de sentiment (C5) envoyées au prompt Claude — c'est un signal précoce de l'état du marché dès l'ouverture.
*Catégorie : indicateurs_momentum*

### D7312 — Statistique de référence : moyenne NYSE TICK première minute = -37, écart-type = 446
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Sur 2,2 millions d'observations (1997 à date de l'article), la moyenne du NYSE TICK sur la première minute de trading est de -37, avec un écart-type de 446. Ces chiffres constituent une référence de normalité statistique.
**TRADEX-AI C5** : Ces valeurs de référence (moyenne -37, σ=446) doivent être stockées dans settings.py comme benchmark TICK pour qualifier les lectures extrêmes — un TICK < -530 (25ème percentile) est déjà une condition de faiblesse notable.
*Catégorie : indicateurs_momentum*

### D7313 — Statistique : percentiles NYSE TICK première minute (données historiques 1997+)
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Percentiles du NYSE TICK sur la première minute : P75 non mentionné, P25 = -177, P10 = -532, P5 = -885, P1 = -1318. La lecture de -1309 dans l'article est proche du 1er percentile (seulement 44 jours sur toute l'histoire).
**TRADEX-AI C5** : Implémenter une classification du TICK en percentile dans TRADEX : normal (P25-P75), attention (P10-P25 ou P75-P90), alerte (P5-P10 ou P90-P95), extrême (< P5 ou > P95). Chaque niveau influence le score C5.
*Catégorie : indicateurs_momentum*

### D7314 — Règle statistique : TICK extrême négatif en première minute → seulement 18% de clôtures positives vs veille
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Les jours avec un TICK de première minute ≤ -1309 (≈ P1, 44 jours sur l'historique) : seulement 18% des journées ont clôturé en hausse par rapport à la clôture précédente. Explication : ces lectures extrêmes sont souvent accompagnées de gaps baissiers.
**TRADEX-AI C5** : Un NYSE TICK de première minute < P5 est un signal baissier fort pour ES et par corrélation pour GC (qui peut réagir en refuge) — à intégrer dans la pondération du score C5 dans la grille /10.
*Catégorie : indicateurs_momentum*

### D7315 — Règle statistique clé : TICK extrême négatif → seulement 34% de clôtures positives vs ouverture
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Pour les mêmes 44 jours de TICK extrême négatif (≤ -1309) : seulement 34% des journées ont clôturé en hausse par rapport à l'ouverture du jour même (pas la clôture précédente). Cette statistique est "significative et représente probablement un avantage pour le jour en cours."
**TRADEX-AI C5** : Un TICK extrême négatif à l'ouverture donne un edge baissier intraday réel — dans TRADEX, cela peut renforcer un signal VENDRE sur CL ou GC si les autres cercles confirment. À documenter dans le prompt Claude comme "TICK_EXTREME_BEARISH".
*Catégorie : indicateurs_momentum*

### D7316 — Donnée de référence : 53% des jours ferment en hausse depuis l'ouverture (tous jours confondus)
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Sur tous les jours (baseline), 53% clôturent en hausse depuis l'ouverture du même jour, avec une performance moyenne de +0,02% et un écart-type de 1,15%. C'est le benchmark de normalité pour comparer les conditions extrêmes.
**TRADEX-AI C5** : Cette baseline (53% hausse, +0,02% moyen, σ=1,15%) est la référence "marché normal" pour ES. Toute condition qui fait descendre ce taux en dessous de ~40% est un signal d'anomalie significative à signaler dans C5.
*Catégorie : indicateurs_momentum*

### D7317 — Alerte : l'écart-type est élevé → les résultats individuels sont très variables
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Pour les jours de TICK extrême négatif, la perte moyenne depuis l'ouverture est de -0,41%, mais l'écart-type est de 1,24% — ce qui signifie qu'il y a une grande variabilité des résultats individuels malgré l'edge statistique global.
**TRADEX-AI C5** : Un signal basé sur le TICK extrême n'est pas un signal "certain" — c'est un edge probabiliste. En mode Manuel TRADEX, afficher cette variabilité (σ=1,24%) à Abdelkrim pour qu'il comprenne le risque réel. En mode Auto, ce signal seul est insuffisant.
*Catégorie : psychologie*

### D7318 — Méthode : l'analyse statistique du TICK nécessite des millions d'observations — Excel insuffisant
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : L'analyse de 2,2 millions d'observations de barres TICK d'1 minute dépasse les capacités d'Excel. Ce type de travail statistique sur des données de marché haute fréquence nécessite des outils adaptés (Python, R, bases de données).
**TRADEX-AI C2** : La future base de données de backtesting de TRADEX (SQLite) devra stocker les données TICK historiques en format compressé — la lecture via Python (pandas) est obligatoire pour les analyses statistiques à grande échelle.
*Catégorie : configuration*

### D7319 — Application : statistiques rapides en live pour orienter le biais intraday du jour
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : L'auteur illustre qu'il est possible de calculer des statistiques rapides en quelques minutes au début de la journée pour établir un biais probabiliste sur la direction du jour. Ce n'est pas une certitude mais un "edge" quantifié.
**TRADEX-AI C5** : TRADEX doit calculer en début de session (première barre de 1 min) le percentile du NYSE TICK et afficher le biais intraday statistique associé — c'est une donnée de contexte utile pour Abdelkrim avant ses premières décisions du jour.
*Catégorie : indicateurs_momentum*

### D7320 — Concept : mapping statistique de la journée de trading
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : L'idée centrale est de "mapper statistiquement" la journée de trading — utiliser des données historiques pour comprendre ce qui est normal et ce qui est anormal, et agir sur les anomalies détectées.
**TRADEX-AI C5** : La section C5 (sentiment) de TRADEX doit inclure non seulement le VIX mais aussi ce mapping statistique intraday (percentile TICK, ratio P&L moyen vs baseline) pour qualifier la journée comme "normale", "atypique_haussière" ou "atypique_baissière".
*Catégorie : indicateurs_momentum*

### D7321 — Règle : le TICK extrême négatif est souvent causé par des gaps baissiers
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : Les lectures de TICK de première minute très négatives sont typiquement associées à des gaps baissiers à l'ouverture — ce qui explique pourquoi peu de ces journées récupèrent la clôture précédente (le gap lui-même est difficile à combler).
**TRADEX-AI C5** : Corréler les données de gap ouverture ES (champ "gap_ouverture" à créer dans data_reader.py) avec le TICK de première minute — les deux signaux combinés constituent un signal de biais baissier fort pour la journée.
*Catégorie : structure_marche*

### D7322 — Méthode : calculer les statistiques de percentile comme outil de décision rapide
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : La méthode de calcul de percentiles historiques d'un indicateur (ici le TICK) est un outil de décision rapide applicable à de nombreux autres indicateurs : VIX, volumes, range de la première barre, etc.
**TRADEX-AI C5** : Appliquer la même méthode de percentile à : (1) VIX (actif VX), (2) volume première heure vs moyenne 20j, (3) range de la première barre vs ATR14j — pour quantifier l'état du marché au-delà des seuls seuils fixes.
*Catégorie : indicateurs_momentum*

### D7323 — Alerte pratique : ne pas sur-interpréter l'edge — le stdev est trop large pour un trade certain
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : Même avec un TICK à P1 et un edge baissier statistique réel, la perte moyenne de -0,41% avec un σ de 1,24% signifie que la distribution est trop large pour considérer ce signal comme un trade systématique à lui seul.
**TRADEX-AI C5** : Dans la grille /10, le signal TICK extrême contribue au score C5 mais ne peut pas à lui seul valider un trade en mode Auto — il doit être confirmé par au moins 2 autres cercles (ex : C1 structure baissière + C2 delta négatif).
*Catégorie : gestion_risque_entree*

### D7324 — Valeur de référence : 44 jours seulement sur 25+ ans d'histoire = événement rarissime
🟢 **FAIT VÉRIFIÉ** (Source : using_statistics_to_map_the_trading_day.md) : Sur toute la période 1997 à la date de l'article, seulement 44 journées ont présenté un NYSE TICK de première minute ≤ -1309. C'est un événement extrêmement rare (< 1% des jours de trading).
**TRADEX-AI C5** : Les événements de TICK < P1 sont des événements "queue de distribution" — en mode Manuel TRADEX, les afficher avec une alerte visuelle spéciale "ÉVÉNEMENT EXTRÊME" pour attirer l'attention d'Abdelkrim sur l'anomalie.
*Catégorie : indicateurs_momentum*

### D7325 — Principe méthodologique : toujours comparer les conditions actuelles à leur percentile historique
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : La valeur absolue d'un indicateur (ex : TICK = -1309) n'a pas de sens sans la référence à sa distribution historique. -1309 est "extrême" seulement parce qu'il est < P1 — sans cette référence, c'est juste un nombre.
**TRADEX-AI C5** : TRADEX doit systématiquement exprimer les valeurs d'indicateurs de sentiment en percentile de leur distribution historique (30j, 90j, 1an) plutôt qu'en valeur absolue — c'est plus informatif pour la prise de décision.
*Catégorie : indicateurs_momentum*

### D7326 — Principe général : la statistique est un outil de carte du marché, pas une boule de cristal
🟡 **SYNTHÈSE** (Source : using_statistics_to_map_the_trading_day.md) : L'auteur conclut par "juste quelques stats à réfléchir pendant que la journée se déroule" — la statistique donne un contexte probabiliste, pas une certitude. Elle aide à orienter le regard mais n'élimine pas l'incertitude.
**TRADEX-AI C5** : Chaque signal statistique dans TRADEX (TICK percentile, VIX percentile, etc.) doit s'afficher avec un niveau de confiance probabiliste (ex : "34% des jours similaires ont clôturé en hausse"), jamais comme une certitude. Mode Manuel oblige.
*Catégorie : psychologie*
