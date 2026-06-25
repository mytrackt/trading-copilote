# Extraction NinjaTrader — The Ultimate Guide to Price Action Trading Strategies
**Source :** `bundles/ninjatrader/price_action_trading_strategies.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8031 → D8050 · **Page :** https://ninjatrader.com/futures/blogs/price-action-trading-strategies/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Price action — lire les structures de marché brutes (support/résistance, tendance, breakout) sans indicateurs retardataires.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D8031 — Price action : définition opérationnelle
🟢 **FAIT VÉRIFIÉ** (Source : price_action_trading_strategies.md) : La price action consiste à analyser les marchés financiers via le mouvement brut du prix sur le graphique — sans indicateurs retardataires — en identifiant des configurations, des tendances et des niveaux clés de support/résistance.
**TRADEX-AI C1** : Le cerveau Belkhayate s'appuie sur la price action comme couche primaire (BGC, pivots, direction). Ce principe confirme que les indicateurs sont secondaires au comportement du prix.
*Catégorie : structure_marche*

### D8032 — Support et résistance : zones de pause ou de retournement
🟢 **FAIT VÉRIFIÉ** (Source : price_action_trading_strategies.md) : Le support est une zone où le prix tend à s'arrêter ou à rebondir à la hausse ; la résistance est une zone où le prix tend à s'arrêter ou à se retourner à la baisse.
**TRADEX-AI C1** : Les pivots Belkhayate (PP, S1-S3, R1-R3) matérialisent ces zones ; les prix autour des pivots signalent des points d'entrée/sortie prioritaires.
*Catégorie : structure_marche*

### D8033 — Tendance : structure hausse et baisse
🟢 **FAIT VÉRIFIÉ** (Source : price_action_trading_strategies.md) : Un marché en tendance haussière produit des plus hauts successifs (higher highs) et des plus bas successifs (higher lows) ; un marché en tendance baissière produit des plus bas successifs (lower lows) et des plus hauts successifs (lower highs).
**TRADEX-AI C1** : La direction Belkhayate (BGC direction) doit être alignée avec la structure HH/HL ou LL/LH avant de valider un signal — règle 3/4 trading.
*Catégorie : indicateurs_tendance*

### D8034 — Breakout : cassure avec momentum
🟢 **FAIT VÉRIFIÉ** (Source : price_action_trading_strategies.md) : Un breakout se produit lorsque le prix franchit un niveau de support ou de résistance avec de la force (momentum). Un retest du niveau cassé en tant que nouveau support/résistance est considéré comme une zone d'entrée potentielle.
**TRADEX-AI C1** : Un breakout confirmé suivi d'un retest constitue une opportunité d'entrée valide dans TRADEX ; la force du breakout peut être mesurée via l'énergie Belkhayate (en attente de codage).
*Catégorie : configuration*

### D8035 — Rejection : échec de cassure
🟢 **FAIT VÉRIFIÉ** (Source : price_action_trading_strategies.md) : Une rejection se produit quand le prix teste un niveau clé mais échoue à le franchir et repart dans la direction opposée.
**TRADEX-AI C1** : Un pin bar ou une mèche longue au niveau d'un pivot Belkhayate constitue une rejection exploitable comme signal d'entrée en contre-tendance (avec confirmation 2/3).
*Catégorie : configuration*

### D8036 — Pin bar : signal de renversement visuel
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : Le pin bar est un pattern de chandelier à longue mèche et petit corps, indiquant un rejet du prix à un niveau clé. Le contexte de formation (à un support, une résistance, un pivot) détermine sa validité.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un pin bar formé exactement sur un pivot Belkhayate renforce la probabilité d'un signal ACHETER ou VENDRE.
*Catégorie : configuration*

### D8037 — Flux de travail price action en 4 étapes
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : Workflow recommandé : (1) Identifier la tendance sur une unité de temps supérieure, (2) marquer les niveaux de support/résistance importants, (3) attendre qu'un pattern se forme à ces niveaux, (4) planifier l'entrée, le stop et la cible avant de prendre le trade.
**TRADEX-AI C1** : Ce workflow est intégré dans l'architecture TRADEX à 3 niveaux : niveau 1 (Python surveille alignment 3/4 + 2/3), niveau 2 (filtres news/VIX/staleness), niveau 3 (Claude API analyse via KB).
*Catégorie : gestion_risque_entree*

### D8038 — Contexte de formation d'un pattern : facteur dominant
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : Où un pattern se forme est aussi important — souvent plus — que le pattern lui-même. Un pin bar isolé en milieu de range a peu de valeur ; le même pattern sur un support majeur ou un pivot a une valeur significativement plus haute.
**TRADEX-AI C1** : La KB Belkhayate intègre cette règle : tout signal requiert une confluence de niveaux (pivot + énergie + BGC direction) avant validation.
*Catégorie : configuration*

### D8039 — Plan de trading price action : composantes essentielles
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : Un plan de trading price action inclut : (1) marchés tradés, (2) unités de temps suivies, (3) patterns recherchés, (4) règles de gestion du risque, (5) processus de revue post-trade.
**TRADEX-AI C1** : TRADEX implémente ce plan : GC/HG/CL/ZW (actifs), range bars NT8 (timeframe), configurations Belkhayate (patterns), risk_manager.py (gestion risque), logs SQLite (revue).
*Catégorie : gestion_risque_entree*

### D8040 — Analyse multi-marchés en futures : E-mini et Micro
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : En futures, la price action est particulièrement utile sur les marchés actifs comme les E-mini (ES, NQ) et Micro futures, en raison de leur liquidité élevée et de leur réactivité aux flux institutionnels.
**TRADEX-AI C2** : ES est un actif de CONFIRMATION dans TRADEX (cercle C4 macro). La liquidité élevée de l'ES renforce la fiabilité des signaux price action comme filtre de confirmation.
*Catégorie : volume_liquidite*

### D8041 — Order flow comme complément à la price action
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : NinjaTrader recommande de combiner la reconnaissance de patterns de chandeliers, les outils de dessin de tendance et les données d'order flow pour construire une approche complète sans indicateurs lourds.
**TRADEX-AI C2** : ATAS (cercle C2) fournit le footprint, le delta et les big trades — confirmation directe des patterns price action identifiés par C1.
*Catégorie : volume_liquidite*

### D8042 — Revue des trades : apprentissage continu
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : Suivre ses trades dans le temps permet d'identifier ce qui fonctionne et ce qui doit être ajusté. La revue post-trade est un composant clé pour améliorer la cohérence de l'approche.
**TRADEX-AI C1** : Les logs SQLite de TRADEX permettent la revue des signaux générés et des résultats, alimentant l'amélioration continue de la KB.
*Catégorie : psychologie*

### D8043 — Simulateur : pratique sans risque capital
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : NinjaTrader fournit un simulateur de trading permettant de pratiquer des stratégies price action sans risquer de capital. Cela inclut des outils de graphiques personnalisables et des types de graphiques variés.
**TRADEX-AI C1** : Le mode simulation de TRADEX (Mode Manuel sans exécution automatique activée) remplit un rôle équivalent pour Abdelkrim.
*Catégorie : psychologie*

### D8044 — Tendance multi-timeframe : filtre prioritaire
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : Identifier la tendance sur une unité de temps supérieure avant d'opérer sur une unité inférieure est présenté comme la première étape d'un workflow price action structuré.
**TRADEX-AI C1** : Dans TRADEX, la direction Belkhayate (BGC) est évaluée en premier ; les signaux contre la direction dominante sont filtrés ou requièrent une confluence de confirmation renforcée.
*Catégorie : indicateurs_tendance*

### D8045 — Retest d'un niveau cassé : entrée structurée
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : Après un breakout d'une résistance, le retest de ce niveau (devenu support) est considéré comme une zone d'entrée potentielle. Cette approche est présentée comme un exemple concret de structuration d'un trade.
**TRADEX-AI C1** : Dans TRADEX, un retest de pivot Belkhayate post-cassure, confirmé par un signal d'énergie et d'order flow, constitue une entrée haute probabilité alignée sur ce principe.
*Catégorie : gestion_risque_entree*

### D8046 — Consistance via structure : répétabilité
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : La price action bien structurée (patterns + niveaux clés + plan) peut amener plus de consistance dans l'approche des trades. La structure compense le manque d'indicateurs.
**TRADEX-AI C1** : La grille déterministe /10 de TRADEX (score ≥ 7,0 + R/R ≥ 1:2) opérationnalise cette recherche de consistance via des critères objectifs.
*Catégorie : gestion_risque_entree*

### D8047 — Marchés actifs : meilleure lisibilité price action
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : En futures, la price action reflète comment les traders réagissent aux nouvelles, à la liquidité et au momentum. Elle est particulièrement utile sur les marchés actifs.
**TRADEX-AI C1** : GC (Or) et CL (Pétrole) sont des marchés actifs avec forte réactivité aux news macro (NFP, FOMC) — le news gate de TRADEX bloque les signaux 30 min avant ces événements.
*Catégorie : macro_evenements*

### D8048 — Patterns communs : signal probabiliste, pas certitude
🔵 **ÉCOLE** (Source : price_action_trading_strategies.md) : Les patterns de price action indiquent ce que le marché pourrait faire ensuite. Ils ne garantissent pas un résultat mais aident à formuler des scénarios probables.
**TRADEX-AI C1** : La KB Belkhayate quantifie ces probabilités via un score /10 ; un score < 7,0 n'est pas tradé même si un pattern valide est présent.
*Catégorie : psychologie*

### D8049 — Indicateurs : rôle secondaire au prix
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : La price action propose une approche "indicator-light" — les indicateurs peuvent compléter mais ne doivent pas remplacer la lecture directe du prix.
**TRADEX-AI C1** : La méthode Belkhayate utilise des indicateurs propriétaires (BGC, énergie) comme lecture directe du prix, pas comme filtre retardataire. Ce principe est cohérent avec la philosophie TRADEX.
*Catégorie : indicateurs_tendance*

### D8050 — Breakout avec force : qualité du mouvement
🟡 **SYNTHÈSE** (Source : price_action_trading_strategies.md) : Un breakout de qualité se distingue par la force du mouvement — le prix franchit le niveau avec un momentum clair, sans hésitation. Un breakout faible (prix colle au niveau sans accélération) est un signal de moindre qualité.
**TRADEX-AI C1** : L'énergie Belkhayate (stub en attente de codage) sera le proxy quantitatif de cette "force" de breakout dans TRADEX.
*Catégorie : configuration*
