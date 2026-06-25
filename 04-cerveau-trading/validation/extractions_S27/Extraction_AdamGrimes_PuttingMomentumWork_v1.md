# Extraction AdamGrimes — Putting Momentum Work
**Source :** `bundles/adamgrimes/putting_momentum_work.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6371 → D6387 · **Page :** https://www.adamhgrimes.com/putting-momentum-work/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Momentum = dérivée première des prix + stratégie pullback sur extrêmes momentum → filtre directionnel C1/C7.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| *(aucune image dans ce bundle)* | — | — | — |

## DÉCISIONS

### D6371 — Momentum TA vs momentum académique : définitions distinctes
🔵 **ÉCOLE** (Source : putting_momentum_work.md) : Le "momentum" en analyse technique (oscillateur = prix actuel / prix N jours avant) est fondamentalement différent du "momentum" académique (force relative inter-actifs sur période de lookback). Les confondre conduit à des erreurs d'interprétation.
**TRADEX-AI C1** : Dans le moteur de signal, distinguer explicitement (1) l'oscillateur momentum intra-actif (dérivée des prix) des (2) corrélations inter-marchés C7. Ne jamais utiliser le terme "momentum" sans préciser lequel.
*Catégorie : indicateurs_momentum*

### D6372 — Momentum = première dérivée des prix
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : Le momentum en analyse technique est mathématiquement la première dérivée des prix — le taux de variation du prix de l'actif. Rate of Change (ROC = prix_t / prix_{t-n}) et Momentum (prix_t - prix_{t-n}) produisent la même forme de courbe, valeurs différentes, interchangeables visuellement.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, le calcul `close / close[10]` donne un ROC 10 jours utilisable comme filtre directionnel. Implémentable dans `05-saas/engine/` sans coût API.
*Catégorie : indicateurs_momentum*

### D6373 — Signal momentum : entrer sur pullback après extrême
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : Règle opérationnelle — quand un actif fait un nouveau plus haut (ou plus bas) sur l'oscillateur momentum sur N jours, attendre le pullback/consolidation PUIS entrer dans la direction du momentum. Ce n'est pas un signal d'entrée immédiat, c'est un filtre de direction.
**TRADEX-AI C1** : Compatible avec la règle d'entrée Belkhayate 3/4 + 2/3. Le momentum extrême sur 40 jours constitue un filtre directionnel supplémentaire à intégrer dans la grille /10.
*Catégorie : configuration*

### D6374 — Calcul des canaux momentum : highs/lows sur 40 jours
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : Règle technique précise — tracer les canaux highs/lows du momentum sur 40 jours. Nouveau high du canal momentum → chercher longs sur premier pullback. Nouveau low du canal momentum → chercher shorts sur premier pullback. Code EasyLanguage fourni : `mom = c / c[len1]` avec len1=10, len2=40.
**TRADEX-AI C1** : Paramètres opérationnels : ROC(10) avec canaux Highest/Lowest(40). Applicable sur GC/HG/CL/ZW en données journalières NT8.
*Catégorie : indicateurs_momentum*

### D6375 — Mouvement climax : annule le signal momentum
🟡 **SYNTHÈSE** (Source : putting_momentum_work.md) : Un mouvement de momentum doit être annulé comme signal si les barres génératrices du signal s'étendent très loin hors des Keltner Channels — cela signale un mouvement climax (épuisement probable) plutôt qu'un momentum sain.
**TRADEX-AI C1** : Garde-fou : si la barre de momentum extrême est aussi une bougie climax (extension > 2x ATR hors Keltner), déclasser le signal. À intégrer comme critère éliminatoire dans la grille /10.
*Catégorie : gestion_risque_entree*

### D6376 — Signal contradictoire inverse : invalide le momentum initial
🟡 **SYNTHÈSE** (Source : putting_momentum_work.md) : Si un nouveau signal momentum dans le sens opposé apparaît rapidement après un premier signal, le premier signal est invalidé. Exemple : signal court suivi 9 barres plus tard d'un signal long → le court est annulé.
**TRADEX-AI C1** : Règle de cohérence : si un signal VENDRE sur momentum est contredit par un signal ACHETER sur momentum dans les 10 barres suivantes sur le même actif, le moteur émet ATTENDRE automatiquement.
*Catégorie : gestion_risque_entree*

### D6377 — Le momentum seul est incomplet : stops, targets, sizing requis
🔵 **ÉCOLE** (Source : putting_momentum_work.md) : Un filtre momentum ne constitue pas un système complet. Il faut obligatoirement : stop loss défini, profit target ou règle de sortie, position sizing, trigger d'entrée précis.
**TRADEX-AI C1** : Confirme l'architecture TRADEX : le momentum est un filtre C1 parmi les 7 cercles, pas un système autonome. Le Risk Manager (`05-saas/engine/risk_manager.py`) gère stops et sizing.
*Catégorie : gestion_position_active*

### D6378 — Anomalie momentum académique : actifs forts restent forts
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : L'anomalie momentum académique (force relative) est une anomalie de marché reconnue scientifiquement : les actifs les plus forts sur une période de lookback tendent à surperformer, les plus faibles tendent à sous-performer.
**TRADEX-AI C7** : Pour la matrice de corrélations C7, intégrer le classement de force relative entre GC/HG/CL/ZW comme signal de confirmation inter-marchés. L'actif le plus fort du groupe mérite un biais haussier additionnel.
*Catégorie : correlations*

### D6379 — Utilité pour traders discrétionnaires et quantitatifs
🔵 **ÉCOLE** (Source : putting_momentum_work.md) : Le filtre momentum (canaux highs/lows) est utilisable à la fois dans des systèmes quantitatifs automatisés ET par des traders discrétionnaires comme structure d'analyse. Il est "timeframe-agnostique" — applicable du intraday au hebdomadaire.
**TRADEX-AI C1** : Compatible avec les deux modes TRADEX (Manuel et Auto). En mode Manuel, le filtre momentum s'affiche sur le dashboard comme indicateur de biais directionnel.
*Catégorie : configuration*

### D6380 — Consolidation après momentum = zone d'entrée préférentielle
🟡 **SYNTHÈSE** (Source : putting_momentum_work.md) : La structure optimale est : (1) fort mouvement momentum, (2) consolidation/pullback, (3) entrée dans la direction du momentum. Cette structure est supérieure à une entrée immédiate sur le breakout momentum.
**TRADEX-AI C1** : Aligné avec la méthode Belkhayate (attendre le retour sur zone après l'impulsion). Le filtre momentum confirme la direction, l'entrée se fait sur la structure Belkhayate (BGC, pivots).
*Catégorie : configuration*

### D6381 — Marchés financiers : complexité nécessite simplification ciblée
⚫ **HYPOTHÈSE PROJET** (Source : putting_momentum_work.md) : Les outils de mesure du momentum permettent de "filtrer le bruit" et de se concentrer sur les structures de prix les plus significatives dans des marchés complexes (reversals soudains, fausses cassures, périodes de stagnation).
**TRADEX-AI C1** : Justifie l'utilisation de l'oscillateur momentum comme pré-filtre niveau 1 (Python, 0$) avant l'analyse Claude API niveau 3.
*Catégorie : psychologie*

### D6382 — Paramètre lookback momentum : 10 jours pour le calcul de base
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : Adam Grimes utilise un lookback de 10 jours pour le calcul du momentum de base (`c / c[10]`), qualifié de "one month return" approximatif. Ce paramètre est explicitement codé dans l'exemple EasyLanguage.
**TRADEX-AI C1** : Paramètre de référence pour GC/HG/CL/ZW : ROC(10) journalier. À stocker dans `05-saas/config/settings.py` sous `MOMENTUM_LOOKBACK = 10`.
*Catégorie : indicateurs_momentum*

### D6383 — Paramètre canal momentum : 40 jours pour highs/lows
🟢 **FAIT VÉRIFIÉ** (Source : putting_momentum_work.md) : Le canal momentum (highs et lows) est calculé sur 40 jours : `hh = highest(mom, 40)` et `ll = lowest(mom, 40)`. Un nouveau high du canal déclenche un biais haussier, un nouveau low déclenche un biais baissier.
**TRADEX-AI C1** : Paramètre de référence : canal momentum 40 jours. À stocker dans `05-saas/config/settings.py` sous `MOMENTUM_CHANNEL_PERIOD = 40`.
*Catégorie : indicateurs_momentum*

### D6384 — Momentum ≠ signal immédiat, momentum = filtre de direction
🟡 **SYNTHÈSE** (Source : putting_momentum_work.md) : La flèche sur un momentum extrême n'est PAS un point d'entrée — c'est le point de départ d'une recherche d'entrée dans cette direction. La distinction est fondamentale pour éviter les entrées sur momentum climax.
**TRADEX-AI C1** : Dans le prompt Claude (niveau 3), préciser : "le momentum extrême indique la direction de recherche, pas l'entrée". Intégrer dans les instructions système de `claude_brain.py`.
*Catégorie : gestion_risque_entree*

### D6385 — Oscillateurs momentum : applicables à tout marché et timeframe
🔵 **ÉCOLE** (Source : putting_momentum_work.md) : Le concept de momentum (ROC + canaux highs/lows) est applicable à "any timeframe or any market" — explicitement mentionné par l'auteur pour l'exemple intraday transposable au daily ou weekly.
**TRADEX-AI C1** : Pour TRADEX, appliquer le filtre momentum en timeframe daily (données NT8 daily) pour GC/HG/CL/ZW. Ne pas multiplier les timeframes pour éviter la suroptimisation.
*Catégorie : configuration*

### D6386 — Keltner Channels comme référence d'extension anormale
🟡 **SYNTHÈSE** (Source : putting_momentum_work.md) : Les Keltner Channels servent de référence pour identifier les extensions anormales de momentum (barres "extended far below/above the lower/upper channel"). Une extension extrême hors des Keltner est un signal d'alerte climax.
**TRADEX-AI C1** : Intégrer les Keltner Channels comme filtre anti-climax dans le moteur Python (niveau 1, 0$). Si la barre de signal est > 2 ATR hors du Keltner Channel moyen, ajouter le flag `POTENTIAL_CLIMAX` au signal.
*Catégorie : indicateurs_momentum*

### D6387 — Système momentum : outil structurant pour traders débutants
🔵 **ÉCOLE** (Source : putting_momentum_work.md) : Le filtre momentum (highs/lows 40 jours sur ROC 10 jours) est présenté comme un bon cadre structurant pour les traders en développement — il met plus souvent du bon côté du marché sans nécessiter d'analyse discrétionnaire complexe.
**TRADEX-AI C1** : Pertinent pour le Mode Manuel TRADEX (Abdelkrim décide) : afficher le biais momentum comme indicateur visuel simple sur le dashboard pour orienter la décision sans la remplacer.
*Catégorie : psychologie*
