# Extraction AdamGrimes — Showing Relative Performance: Simple Price Charts
**Source :** `bundles/adamgrimes/showing_relative_performance_simple_price_charts.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6591 → D6605 · **Page :** https://www.adamhgrimes.com/showing-relative-performance-simple-price-charts/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : La performance relative entre actifs (GC/ES, CL/DX) doit être calculée en rendements %, jamais en prix absolus — règle fondamentale pour la matrice de corrélations C7.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6591 — La performance relative doit être calculée en rendements (%), jamais en prix absolus
🟢 **FAIT VÉRIFIÉ** (Source : showing_relative_performance_simple_price_charts.md) : Pour comparer la performance de deux actifs, il faut systématiquement convertir en rendements (variation %) et non en prix absolus. Formule : `return = ending_price / starting_price - 1`. Un actif à $10 +$10 = +100%, un actif à $500 +$10 = +2% : la différence est critique.
**TRADEX-AI C7** : La matrice de corrélations live 30j (correlations.py) doit calculer toutes les corrélations sur séries de rendements %, jamais sur séries de prix. Idem pour l'affichage relatif GC/HG/CL/ZW dans le dashboard.
*Catégorie : correlations*

### D6592 — INTERDIT : deux séries de prix sur le même graphique avec deux axes différents
🟢 **FAIT VÉRIFIÉ** (Source : showing_relative_performance_simple_price_charts.md) : Mettre deux séries de prix sur un même graphique avec deux axes de prix différents est une erreur fondamentale. L'échelle est arbitraire et on peut montrer n'importe quelle relation souhaitée. Grimes : "ne jamais mettre deux séries de prix sur le même graphique avec deux axes différents."
**TRADEX-AI C7** : Le dashboard React ne doit jamais afficher deux actifs en prix absolus avec deux axes Y distincts. Si un graphique multi-actifs est nécessaire, indexer tous les actifs à 0 à partir du même point de départ (rendements cumulés).
*Catégorie : correlations*

### D6593 — Méthode de visualisation : indexer tous les actifs à 0 à partir d'un pivot commun
🔵 **ÉCOLE** (Source : showing_relative_performance_simple_price_charts.md) : La méthode correcte pour visualiser la performance relative est d'indexer tous les actifs à 0 (ou 100) à partir d'un même point de départ (ex: un pivot structurel important), puis d'afficher les rendements cumulés. Cela permet de voir directement qui surperforme qui.
**TRADEX-AI C7** : Dans le module correlations.py, implémenter une fonction `relative_performance(assets, anchor_date)` qui indexe tous les actifs (GC/HG/CL/ZW/ES/VX) à 0 à partir d'une date pivot, pour visualisation dans le dashboard.
*Catégorie : correlations*

### D6594 — Le choix du point de départ (anchor) est subjectif et critique
🟢 **FAIT VÉRIFIÉ** (Source : showing_relative_performance_simple_price_charts.md) : Le choix du point d'ancrage (début du calcul de rendement) est subjectif et impacte dramatiquement les conclusions sur la performance relative. Des points d'ancrage différents peuvent montrer des résultats "diamétralement opposés". Anchorer sur un pivot structurel important est une bonne pratique mais introduit de la subjectivité.
**TRADEX-AI C7** : Dans le dashboard, afficher le point d'ancrage utilisé pour les graphiques de performance relative, et permettre à Abdelkrim de le modifier. Documenter que les conclusions dépendent du choix de ce point.
*Catégorie : correlations*

### D6595 — Performance relative GLD vs SPY : utiliser le pivot structurel comme point zéro
🔵 **ÉCOLE** (Source : showing_relative_performance_simple_price_charts.md) : Exemple concret de Grimes : GLD et SPY convertis en rendements, avec le pivot d'octobre de SPY comme "point zéro". Ce graphique montre clairement une période de sous-performance de GLD puis une surperformance apparente. Méthode applicable à GC/ES.
**TRADEX-AI C7** : Pour l'analyse de corrélation GC/ES (Or vs S&P 500), utiliser le dernier pivot structurel identifié sur ES comme point d'ancrage. La surperformance ou sous-performance de GC vs ES depuis ce pivot est un signal de flux institutionnel (C3).
*Catégorie : correlations*

### D6596 — La question de comparaison doit avoir un sens économique (pas juste technique)
🟡 **SYNTHÈSE** (Source : showing_relative_performance_simple_price_charts.md) : Grimes avertit : on peut mettre n'importe quoi sur le même graphique, mais "est-ce que ça a du sens ?" est la question essentielle. Comparer le prix du pétrole à la consommation de dentifrice en Argentine est techniquement possible mais économiquement sans signification.
**TRADEX-AI C7** : La matrice de corrélations TRADEX-AI ne doit inclure que des paires avec justification économique validée : GC/DX (corrélation inverse historique), CL/DX, GC/CL, HG/ES (risque industriel), ZW/DX. Exclure les corrélations sans fondement économique.
*Catégorie : correlations*

### D6597 — Standardiser en rendements est la "première tâche" de tout travail analytique
🟢 **FAIT VÉRIFIÉ** (Source : showing_relative_performance_simple_price_charts.md) : Grimes énonce que "dans la plupart des travaux analytiques, la première tâche est de convertir les prix en rendements." C'est une règle universelle de l'analyse quantitative de marchés, non optionnelle.
**TRADEX-AI C7** : Dans data_reader.py, la transformation prix → rendements doit être appliquée comme étape systématique avant toute analyse comparative. Jamais passer des prix absolus à correlations.py.
*Catégorie : correlations*

### D6598 — Performance relative = tracking d'un actif contre un autre ou contre un groupe d'actifs
🔵 **ÉCOLE** (Source : showing_relative_performance_simple_price_charts.md) : La performance relative mesure comment un marché a performé contre un autre marché, ou contre un ensemble d'autres marchés. Cette mesure est fondamentale pour identifier les leaders et laggards d'un groupe d'actifs corrélés.
**TRADEX-AI C7** : Parmi GC/HG/CL/ZW, l'actif le plus fort en performance relative (rendement cumulé le plus élevé depuis N jours) est candidat prioritaire pour un signal directionnel. L'actif le plus faible est candidat pour signal contra (mean reversion) ou renforcement de la direction.
*Catégorie : correlations*

### D6599 — Une erreur sur les axes révèle une incompréhension des fondamentaux de visualisation
🟡 **SYNTHÈSE** (Source : showing_relative_performance_simple_price_charts.md) : Grimes note que quand un graphique montre deux prix sur deux axes différents, "au mieux c'est trompeur, et cela montre que le producteur du graphique ne comprend pas les problèmes fondamentaux de visualisation des données de prix." Les erreurs de visualisation sont des signaux de qualité de l'analyste.
**TRADEX-AI C7** : Tout graphique produit par TRADEX-AI (dashboard ou rapports) doit respecter la règle des rendements. Un test automatique de validation des graphiques doit refuser l'affichage de prix multi-actifs avec axes multiples.
*Catégorie : correlations*
