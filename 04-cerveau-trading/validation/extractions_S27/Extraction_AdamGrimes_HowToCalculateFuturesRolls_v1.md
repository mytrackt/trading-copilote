# Extraction AdamGrimes — How To Calculate Futures Rolls
**Source :** `bundles/adamgrimes/how_to_calculate_futures_rolls.md` (HTTP 200) + 0 images certifiées
**Méthode images :** N/A · 0/0 certifiées · 0 à vérifier
**Décisions :** D6031 → D6050 · **Page :** https://www.adamhgrimes.com/how-to-calculate-futures-rolls/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Directement applicable à GC/CL/HG/ZW — le roll des contrats futures affecte les données historiques (backtests, niveaux support/résistance, corrélations 30j). Critique pour la fiabilité des signaux TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6031 — Les futures ont des mois de livraison différents avec des prix différents
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Chaque contrat futures trade pour une livraison à un moment spécifique (delivery month). Sur le crude oil, chaque mois a un prix différent. "The price of crude oil" n'est pas une valeur unique : il y a le spot price et le front month. Les mois lointains tradent généralement à des prix plus élevés que les mois proches (contango) en raison des coûts de stockage.
**TRADEX-AI C1** : Sur CL (Pétrole), GC (Or), HG (Cuivre), ZW (Blé), le data_reader.py doit lire le prix du front month actif (le mois avec le plus grand open interest/volume). Le "prix" utilisé pour les signaux doit toujours être le front month, pas un mois expiré ou éloigné.
*Catégorie : volume_liquidite*

### D6032 — Les coûts de stockage, l'offre/demande et les facteurs saisonniers influencent la structure des prix
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Les facteurs principaux influençant la relation entre les mois d'une même matière première : coût de stockage (warehouse, assurance), offre et demande, facteurs saisonniers. Chaque produit a ses propres influences. Il serait inhabituel que deux mois tradent au même prix.
**TRADEX-AI C4** : Pour ZW (Blé), les facteurs saisonniers (récoltes) créent une structure de terme complexe. Pour CL (Pétrole), les coûts de stockage dominent. Ces structures doivent être comprises dans le contexte macro du Cercle C4 pour interpréter correctement les signaux.
*Catégorie : saisonnalite*

### D6033 — Le P&L d'un roll est nul pour le trader qui reste positionné
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Quand on roule un contrat (vente du mois expirant, achat du mois suivant), le P&L de la transaction de roll est zéro. On vend quelque chose à un prix et achète quelque chose de différent à un autre prix. La différence entre les deux prix n'est pas du P&L — c'est juste la différence entre deux contrats distincts.
**TRADEX-AI C2** : Dans le calcul du R/R et du P&L sur les positions GC/CL/HG/ZW, le coût de roll (différentiel entre mois) ne doit pas être compté comme une perte ou un gain réel. À neutraliser dans le risk_manager.py lors du calcul des métriques de performance.
*Catégorie : gestion_position_active*

### D6034 — Sans ajustement de roll, les charts montrent de faux gaps
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Si on assemble les contrats historiques sans ajustement (unadjusted), on voit des sauts de prix (gaps) qui ne se sont jamais produits réellement. Ces gaps artificiels faussent toute analyse historique, tout backtest et toute lecture de chart.
**TRADEX-AI C1** : Les données historiques NT8 pour GC/CL/HG/ZW doivent être des séries back-adjustées. Les niveaux de support/résistance tracés sur charts non ajustés sont potentiellement fictifs. Vérifier la méthode d'ajustement de NinjaTrader 8 avant tout backtest.
*Catégorie : structure_marche*

### D6035 — Les prix back-adjustés ne correspondent pas aux prix réels auxquels le marché a tradé
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Quand on ajuste les prix futures historiques (back-adjustment), les prix affichés sur les charts historiques NE correspondent PAS aux prix auxquels l'instrument a réellement tradé. "This is an important point: when we adjust futures contracts, prices you see on your historical charts are not the prices at which the instrument actually traded."
**TRADEX-AI C1** : Implication critique pour les supports/résistances dans TRADEX-AI : un niveau de support affiché sur un chart back-adjusté (ex. GC à 1200$) peut ne jamais avoir été tradé à ce prix en réalité. Les niveaux clés Belkhayate doivent être validés sur les prix réels (unadjusted) en parallèle des charts ajustés.
*Catégorie : structure_marche*

### D6036 — Méthode 1 — Chart non ajusté (Unadjusted)
🔵 **ÉCOLE** (Source : how_to_calculate_futures_rolls.md) : Un chart non ajusté montre simplement les prix du contrat actif à chaque date, sans correction. Il montre correctement les niveaux de prix historiques réels, mais distord les variations de prix (price changes). Génère de nombreux faux gaps. Utile pour voir les niveaux absolus, pas pour les backtests.
**TRADEX-AI C1** : Usage recommandé pour TRADEX-AI : utiliser les prix unadjusted pour identifier les niveaux de support/résistance importants sur GC/CL/HG/ZW (prix auxquels le marché a réellement tradé). Combiner avec la méthode difference-adjusted pour les calculs dynamiques.
*Catégorie : structure_marche*

### D6037 — Méthode 2 — Ajustement par différence (Difference-adjusted)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : L'ajustement par différence : calculer le différentiel de roll (nouveau contrat - ancien contrat), accumuler ce différentiel en remontant dans le temps, et l'ajouter aux prix historiques du front month. Résultat : les variations de prix en points/ticks sont correctes. Standard de facto chez la plupart des fournisseurs de données. Inconvénient : les prix peuvent devenir négatifs et les variations en pourcentage sont sérieusement distordues.
**TRADEX-AI C7** : La matrice de corrélations 30j dans correlations.py utilise probablement des données difference-adjusted de NinjaTrader 8 (standard de facto). Vérifier que les rendements en % sont calculés sur les returns (variation relative) et non sur les niveaux absolus, qui peuvent être négatifs sur charts difference-adjusted.
*Catégorie : correlations*

### D6038 — Méthode 3 — Ajustement par ratio (Ratio-adjusted)
🔵 **ÉCOLE** (Source : how_to_calculate_futures_rolls.md) : L'ajustement par ratio : diviser les prix historiques par le ratio entre le nouveau et l'ancien contrat. Préserve les variations percentuelles (returns) mais distord les variations en points. Impossible de préserver simultanément les variations en points ET en pourcentage — le choix dépend de la métrique de P&L utilisée.
**TRADEX-AI C7** : Si les calculs de corrélations ou de volatilité dans TRADEX-AI utilisent des retours en %, le ratio-adjusted est la méthode correcte. Si les stop-loss et targets sont définis en ticks/points (standard NinjaTrader ATI), le difference-adjusted est préférable. Vérifier la cohérence dans settings.py.
*Catégorie : indicateurs_momentum*

### D6039 — Règle de choix de la méthode d'ajustement : aligner avec le calcul de P&L
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : "If you're doing backtesting, you must use the methodology that relates to your chosen P&L reporting method." P&L en ticks → difference-adjusted. P&L en pourcentages → ratio-adjusted. Utiliser la mauvaise méthode peut produire des variations de prix en milliers de pourcentages ou des erreurs division par zéro.
**TRADEX-AI C1** : Dans TRADEX-AI, les ordres NT8 ATI sont définis en ticks (standard NinjaTrader). Par cohérence, les backtests doivent utiliser des données difference-adjusted. Le risk_manager.py calcule le R/R en points — cohérent avec difference-adjusted.
*Catégorie : gestion_risque_entree*

### D6040 — L'argument "support/résistance a une mémoire de prix" est fragilisé par le back-adjustment
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : "The argument that price has a memory and this is why support and resistance works… does this argument hold water if the levels do not correspond to past prices? I would argue probably not." Le back-adjustment déplace les niveaux historiques. Un niveau de support affiché à un prix X peut ne jamais avoir été tradé à ce prix.
**TRADEX-AI C1** : Impact direct sur la méthode Belkhayate : les pivots calculés sur des données back-adjustées peuvent ne pas correspondre à des prix réels de marché. Pour les pivots sur GC/CL/HG/ZW, utiliser les prix unadjusted ou vérifier que NinjaTrader 8 utilise le contrat actif réel pour les calculs de pivots.
*Catégorie : structure_marche*

### D6041 — Le back-adjustment fausse aussi la magnitude des swings historiques
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Les charts ajustés distordent la magnitude des swings passés, parfois de manière très sérieuse. Appliquer des ratios (ex. retracement de Fibonacci) sur des swings dont la magnitude est distorte par le back-adjustment est une source d'erreur analytique.
**TRADEX-AI C1** : Pour les mesures de swing (ATR, range, amplitude de mouvement) sur GC/CL/HG/ZW, préférer les données du contrat courant ou unadjusted pour mesurer la volatilité réelle. L'Énergie Belkhayate (stub actuellement) devra utiliser des données de volatilité fiables non distordues par les rolls.
*Catégorie : indicateurs_momentum*

### D6042 — Quand rouler : suivre le déplacement de l'open interest
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Le roll se fait généralement quand l'open interest se déplace vers le nouveau contrat (rolling of open interest). Pour les données historiques, rouler quand l'open interest passe au nouveau mois. Autres méthodes : calendrier fixe, combinaison OI+volume, troisième jour où l'OI du nouveau mois dépasse celui de l'ancien.
**TRADEX-AI C1** : Le data_reader.py doit suivre le contrat avec le plus grand open interest pour GC/CL/HG/ZW. Lors d'un roll, il faut s'assurer que le front month change automatiquement dans le système, pas seulement le prix. À implémenter dans la Phase C des collecteurs NT8.
*Catégorie : volume_liquidite*

### D6043 — Certains produits ont des structures irrégulières (mois préférentiels)
🟡 **SYNTHÈSE** (Source : how_to_calculate_futures_rolls.md) : L'open interest peut être distordu et certains produits sont plus actifs sur certains mois (ex. Septembre et Décembre sur un produit cité dans l'article). Le roulement sur calendrier fixe est moins efficace quand les structures ont changé sur des décennies.
**TRADEX-AI C1** : Pour ZW (Blé), les mois actifs sont décembre, mars, mai, juillet, septembre. Pour GC (Or), les mois principaux sont février, avril, juin, août, décembre. Le data_reader.py doit connaître ces structures spécifiques pour éviter de lire un mois illiquide par erreur.
*Catégorie : volume_liquidite*

### D6044 — La méthode de roll doit correspondre à la façon dont on va trader en live
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : "If you are doing this historically, it's important that your roll methodology matches, as much as possible, how you will trade." La cohérence entre la méthodologie historique et la méthodologie live est plus importante que le choix exact des critères de roll.
**TRADEX-AI C1** : Règle de cohérence TRADEX : la méthode de roll utilisée pour les backtests doit être identique à celle utilisée par NinjaTrader 8 en live. Vérifier les paramètres de roll dans NT8 (Settings > Data Series) et documenter dans settings.py.
*Catégorie : gestion_risque_entree*

### D6045 — Pour les chartistes : utiliser les prix spot pour les niveaux et les adjusted pour les backtests
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : Grimes recommande explicitement : utiliser les prix spot (ou unadjusted) pour les niveaux de support/résistance et les charts ajustés pour les backtests et la reconnaissance de patterns. Cette double approche contourne les problèmes des deux méthodes.
**TRADEX-AI C1** : Architecture recommandée pour TRADEX-AI : (1) Niveaux clés (pivots Belkhayate, support/résistance) → calculés sur prix unadjusted NT8. (2) Calculs dynamiques (corrélations, volatilité, patterns) → calculés sur données difference-adjusted. À documenter dans settings.py et data_reader.py.
*Catégorie : structure_marche*

### D6046 — Comprendre la méthode d'ajustement du fournisseur de données est obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : how_to_calculate_futures_rolls.md) : "At the very least, you need to understand the roll methodology your data vendor is applying." De plus en plus de fournisseurs rendent cette information transparente et permettent de définir ses propres critères. Le choix de la date de roll, des mois à inclure et de la méthode d'ajustement peut produire des centaines de charts différents pour le même marché.
**TRADEX-AI C1** : Action requise Phase C : documenter précisément la méthode de roll et d'ajustement utilisée par NinjaTrader 8 (via Rithmic/NTB) pour GC/CL/HG/ZW. Cette information doit figurer dans les commentaires de data_reader.py et settings.py.
*Catégorie : volume_liquidite*
