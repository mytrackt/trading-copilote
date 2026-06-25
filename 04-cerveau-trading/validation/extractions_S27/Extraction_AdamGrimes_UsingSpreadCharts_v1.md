# Extraction AdamGrimes — Using Spread Charts
**Source :** `bundles/adamgrimes/using_spread_charts.md` (HTTP 200) + 0 images certifiées
**Méthode images :** descriptions de charts présentes mais images non extractibles · 0/0 certifiées · 0 à vérifier
**Décisions :** D7291 → D7310 · **Page :** https://www.adamhgrimes.com/using-spread-charts/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthode rigoureuse pour tracker les performances relatives entre actifs — applicable au Cercle C7 (corrélations) pour GC/HG/CL/ZW/ES/DX/VX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image extractible) | — | — | — |

## DÉCISIONS

### D7291 — Définition : deux méthodes de calcul du spread
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Un spread mesure la relation de prix entre deux marchés. Deux méthodes : (1) Spread différentiel = Prix actif A − Prix actif B ; (2) Spread ratio = Prix actif A / Prix actif B.
**TRADEX-AI C7** : Le module correlations.py de TRADEX doit implémenter les deux méthodes et choisir la bonne selon le type de données (futures ratio-ajustés → ratio spread ; Panama canal → différence spread).
*Catégorie : correlations*

### D7292 — Règle critique : le choix du spread dépend de la méthode d'ajustement des futures
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Pour les traders futures, le choix spread différentiel vs ratio spread dépend directement de la méthode de rétro-ajustement utilisée : ratio-back-adjustment → ratio spread obligatoire ; méthode Panama Canal (différences) → difference spread obligatoire. Erreur fréquente même dans des publications payantes.
**TRADEX-AI C7** : Les données NT8 pour GC, HG, CL, ZW utilisent un ajustement spécifique — documenter dans settings.py quelle méthode d'ajustement NT8 est utilisée pour choisir le bon calcul de spread dans correlations.py.
*Catégorie : correlations*

### D7293 — Alerte : le ratio spread devient problématique quand une série approche de zéro
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Le ratio spread (A/B) devient mathématiquement instable et visuellement trompeur quand l'une des séries de prix s'approche de zéro ou la croise, ce qui est courant avec des futures rétro-ajustés via la méthode Panama Canal.
**TRADEX-AI C7** : correlations.py doit inclure une vérification de sécurité : si le prix d'un actif rétro-ajusté approche de zéro (< seuil minimal), bloquer le calcul de ratio spread et alerter.
*Catégorie : correlations*

### D7294 — Principe : comparer des "pommes avec des pommes" — 3 catégories de prix
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Les prix se répartissent en 3 grandes catégories : (1) actifs versant des dividendes/distributions, (2) futures (incluant des coûts de portage), (3) prix spot. Mélanger des catégories différentes dans un spread chart produit des illusions et des erreurs d'analyse.
**TRADEX-AI C7** : La matrice de corrélations TRADEX doit documenter la catégorie de chaque actif (GC/HG/CL/ZW = futures ; DX = cash-equivalent ; ES = futures ; VX = futures) pour éviter les comparaisons inter-catégories trompeuses.
*Catégorie : correlations*

### D7295 — Alerte : futures vs cash index = illusion de trend dans le spread
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Comparer un contrat futures S&P 500 continu au cash index SPX produit un chart de spread avec une tendance régulière apparente — mais c'est une illusion représentant uniquement la "décroissance naturelle" du futures vers le spot à l'expiration.
**TRADEX-AI C7** : Ne jamais comparer ES (futures) à SPX cash dans les spreads TRADEX — utiliser ES vs ES uniquement, ou SPY vs SPY. La comparaison DX (futures proxy) vs GC doit être documentée avec cette mise en garde.
*Catégorie : correlations*

### D7296 — Alerte : stock vs index cash = distorsion par les dividendes
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Comparer le prix d'une action (ex : PFE) à l'index cash SPX crée une distorsion dans le spread chart due à l'accumulation et au versement périodique des dividendes. Règle : comparer PFE à SPY (ETF incluant dividendes) plutôt qu'à SPX.
**TRADEX-AI C7** : Dans TRADEX, toute corrélation impliquant des actifs versant des dividendes doit utiliser des instruments ajustés dividendes, ou cette limitation doit être documentée dans le prompt Claude.
*Catégorie : correlations*

### D7297 — Problème : les taux de change peuvent fausser les spreads inter-marchés
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Pour des actifs libellés dans des devises différentes, la question clé est : va-t-on couvrir l'exposition de change ou la laisser faire partie du trade ? La réponse change la nature du spread à calculer et à analyser.
**TRADEX-AI C7** : GC (Or en USD) vs un actif en autre devise — TRADEX doit noter l'exposition de change potentielle dans le prompt Claude. En pratique, GC/HG/CL/ZW sont tous en USD → ce risque est faible pour les actifs core TRADEX.
*Catégorie : correlations*

### D7298 — Règle pratique : choisir l'instrument qui correspond à l'implémentation réelle du trade
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : La bonne façon de calculer un spread dépend de comment le trade sera réellement exécuté. Si on trade des actions européennes vs US, la relation à analyser doit être VGK vs SPY (instruments réellement tradables), pas Euro Stoxx vs SPX.
**TRADEX-AI C7** : La matrice de corrélations TRADEX doit utiliser exactement les mêmes instruments que ceux tradés via NT8 : GC1!, HG1!, CL1!, ZW1! (contrats continus NT8) — pas les prix spot ou indices cash.
*Catégorie : correlations*

### D7299 — Outil : chart de spread avec moyenne mobile 20 périodes + bandes ±2,5 écarts-types
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : L'auteur affiche les spreads avec : (1) la valeur du spread en ligne noire épaisse, (2) une moyenne mobile 20 périodes en orange, (3) des bandes placées à ±2,5 écarts-types autour de cette moyenne. Cet affichage permet d'évaluer : caractère (trend vs mean-reversion) et si le spread est étiré ou proche de sa valeur historique.
**TRADEX-AI C7** : correlations.py doit calculer pour chaque paire d'actifs TRADEX : le spread courant, sa MA20, et sa position en nombre d'écarts-types — exposer ces métriques dans le prompt Claude pour le cercle C7.
*Catégorie : correlations*

### D7300 — Principe : un spread "tendu" (étiré) n'implique pas un retour à la moyenne — peut être trending
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : Une erreur d'analyse courante : supposer qu'un spread "devrait" trader à un certain ratio. Beaucoup de relations de spread sont des tendances (trending), pas des mean-reverting. Il ne faut pas supposer de retour à la moyenne sans vérification du caractère du spread.
**TRADEX-AI C7** : Avant d'interpréter un spread étiré entre GC et HG (ou CL et GC) comme "anormal", TRADEX doit d'abord qualifier le caractère historique du spread (trending vs mean-reverting) sur 60+ jours.
*Catégorie : correlations*

### D7301 — Méthode : les bandes d'écarts-types révèlent si un spread est en tendance ou mean-revertant
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : L'utilisation des bandes à ±2,5 écarts-types autour de la MA20 permet de visualiser visuellement si un spread a un comportement "tendanciel" (se déplace continuellement vers une extrémité) ou "mean-revertant" (oscille autour de sa moyenne).
**TRADEX-AI C7** : Le module correlations.py doit classifier automatiquement chaque paire comme "trending_spread" ou "mean_reverting_spread" en calculant le ratio (distance à la MA / écart-type moyen) sur 60 derniers jours.
*Catégorie : correlations*

### D7302 — Contexte : les spreads sont le troisième outil de suivi de performance relative (après % changes et ranking)
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : Cet article s'inscrit dans une série sur le suivi de performance relative. Les spreads complètent deux autres méthodes : (1) variation % depuis un point de swing structurellement significatif, (2) variation % depuis un lookback arbitraire + ranking. Chaque méthode donne une perspective différente.
**TRADEX-AI C7** : TRADEX doit implémenter les 3 méthodes pour la matrice C7 : (1) % depuis dernier swing, (2) % depuis 30j + ranking, (3) spread chart MA20 + bandes. Cela donne une vue complète des corrélations inter-marchés.
*Catégorie : correlations*

### D7303 — Alerte : le logiciel de trading peut facilement induire en erreur sur le choix du spread
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : Les logiciels de trading permettent facilement de créer des charts de spread sans vérifier la cohérence méthodologique (ratio vs différence, ajustement des données, catégorie d'actif). Il faut comprendre ses données avant d'interpréter un spread.
**TRADEX-AI C7** : La documentation de correlations.py doit inclure les paramètres de calcul (méthode ratio ou différence, ajustement utilisé) pour chaque paire afin que Abdelkrim puisse vérifier et valider les hypothèses.
*Catégorie : configuration*

### D7304 — Exemple : US vs Europe — choix d'implémentation détermine l'expression du spread
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : Pour trader US stocks vs Europe, plusieurs expressions sont possibles : panier d'actions européennes vs US, VGK vs SPY. L'expression choisie doit correspondre exactement à l'implémentation réelle. Il n'y a pas d'option "juste" par défaut.
**TRADEX-AI C7** : Pour le spread Or (GC) vs Pétrole (CL) dans TRADEX : toujours utiliser GC1! vs CL1! (contrats continus NT8), en ratio spread si NT8 utilise ratio-back-adjustment — documenter ce choix dans settings.py.
*Catégorie : correlations*

### D7305 — Principe : les spreads évitent de nombreuses erreurs d'analyse naïve
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : L'utilisation rigoureuse des charts de spread (avec MA + bandes) "évite beaucoup de bêtises" selon l'auteur. Sans ce cadre, on risque d'interpréter des mouvements normaux comme des opportunités, ou de manquer des divergences réelles.
**TRADEX-AI C7** : Le dashboard TRADEX doit afficher les principaux spreads (GC/HG, GC/CL, HG/ZW) avec leur MA20 et bandes ±2σ — cela permet à Abdelkrim de visualiser immédiatement si les corrélations inter-marchés sont dans la norme ou anormales.
*Catégorie : correlations*

### D7306 — Note méthodologique : la suite de la série abordera le trading des spreads
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : L'article annonce une suite sur comment trader réellement ces relations de spread — il reste donc une partie à explorer sur l'exploitation opérationnelle des spreads comme stratégie.
**TRADEX-AI C7** : Identifier et scraper l'article suivant de la série Adam Grimes sur le trading des spreads — il pourrait contenir des règles d'entrée/sortie sur les spreads directement applicables à GC/HG/CL/ZW.
*Catégorie : configuration*

### D7307 — Règle : le spread Europe/US en USD montre une relation instructive sur longue période
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : Le spread entre les indices boursiers européens et américains (exprimé en USD) peut montrer une relation trending sur longue période — cet exemple illustre que même des marchés "liés" peuvent diverger structurellement sur des années.
**TRADEX-AI C7** : Pour GC vs HG (corrélation classique métaux industriels vs métaux précieux), TRADEX doit analyser si le spread est structurellement trending sur 252j ou mean-reverting — cela change l'interprétation d'un écartement actuel.
*Catégorie : correlations*

### D7308 — Concept : le spread montre le caractère qualitatif de la relation entre deux marchés
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : Au-delà du calcul quantitatif, le chart de spread avec MA et bandes donne une évaluation qualitative de la relation : est-elle stable ? En train de changer ? Sous tension ? Ce caractère qualitatif complète le signal quantitatif.
**TRADEX-AI C7** : Dans le prompt Claude envoyé par TRADEX, inclure non seulement les valeurs numériques des spreads mais aussi leur caractère qualitatif (stable/en_tension/divergeant) basé sur la position en nb d'écarts-types.
*Catégorie : correlations*

### D7309 — Alerte : n'importe quel actif peut être mis en spread contre n'importe quel autre — cela ne veut pas dire que c'est pertinent
🟡 **SYNTHÈSE** (Source : using_spread_charts.md) : La facilité technique de construire un spread entre deux actifs quelconques ne signifie pas que la relation est économiquement ou analytiquement pertinente. Il faut toujours questionner : "est-ce que cette comparaison fait sens ?"
**TRADEX-AI C7** : La liste des paires de spreads à calculer dans correlations.py doit être limitée à des paires économiquement justifiées : GC/HG (métaux), GC/CL (refuge vs énergie), GC/DX (or vs dollar), CL/HG (énergie vs industrie), ZW/CL (agriculture vs énergie).
*Catégorie : correlations*

### D7310 — Principe général : comprendre ses données avant de les mettre en chart
🟢 **FAIT VÉRIFIÉ** (Source : using_spread_charts.md) : "Il y a plus que des lignes sur un écran" — comprendre la nature des données (type d'ajustement, catégorie d'actif, exposition devise, dividendes) est un prérequis à toute analyse de spread valide.
**TRADEX-AI C7** : correlations.py doit inclure un bloc de commentaires "DATA_ASSUMPTIONS" documentant pour chaque actif : type (futures continu NT8), méthode d'ajustement, devise (USD), et si dividendes/distributions s'appliquent.
*Catégorie : configuration*
