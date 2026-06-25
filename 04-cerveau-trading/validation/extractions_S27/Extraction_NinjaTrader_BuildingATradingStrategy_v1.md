# Extraction NinjaTrader — Building a Trading Strategy
**Source :** `bundles/ninjatrader/building_a_trading_strategy.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7611 → D7630 · **Page :** https://ninjatrader.com/learn/building-a-trading-strategy/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Architecture d'une stratégie de trading structurée (entrée/sortie/risque/backtest/automation) — valide le design TRADEX-AI à 3 niveaux et les garde-fous obligatoires.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7611 — Stratégie de trading : framework à règles pour entrées et sorties
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Une stratégie de trading est un framework à règles définissant quand entrer et sortir du marché. Ces règles sont développées et évaluées sur des données historiques (backtesting) et affinées dans le temps. L'objectif est de supprimer les suppositions et de prendre des décisions objectives en accord avec la tolérance au risque et la vision de marché.
**TRADEX-AI C1** : La méthode Belkhayate avec la règle 3/4 trading + 2/3 confirmation = signal valide est exactement ce framework à règles. TRADEX-AI l'encode en logic Python déterministe au Niveau 1.
*Catégorie : configuration*

### D7612 — Filtres et déclencheurs : distinction fondamentale dans les règles d'entrée
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Les règles d'entrée comprennent deux composants :
- **Filtres** : définissent le contexte de marché large (ex. tendance haussière sur MA, niveau de volatilité minimum).
- **Déclencheurs** : signalent le moment précis d'entrée (ex. cassure d'une résistance, croisement MA, changement de momentum RSI).
Séparer filtres et déclencheurs permet de se concentrer sur les setups à plus haute probabilité et d'éviter de trader dans des conditions défavorables.
**TRADEX-AI C1** : Architecture TRADEX en écho : Niveau 1 = filtres (3/4 + 2/3 alignés). Niveau 2 = filtres macro (News Gate, VIX, staleness). Niveau 3 = déclencheur final (Claude analyse la KB et produit ACHETER/VENDRE/ATTENDRE).
*Catégorie : configuration*

### D7613 — Sorties techniques vs règles de gestion monétaire : les deux sont obligatoires
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Les règles de sortie incluent :
- **Sorties techniques** : basées sur le price action ou des indicateurs (retournement de tendance, ralentissement du momentum).
- **Règles de gestion monétaire** : stop-loss prédéfinis, take-profit, trailing stops.
Une stratégie utilisant uniquement des sorties techniques peut produire des drawdowns dépassant les limites de marge. Les règles de gestion monétaire sont une nécessité pour des résultats réalistes.
**TRADEX-AI C1** : Le risk_manager.py de TRADEX doit implémenter les deux types de sortie. Le stop-loss fixe (règle monétaire) est non-négociable même si le signal technique suggère de tenir la position.
*Catégorie : gestion_position_active*

### D7614 — Stop-loss, take-profit et trailing stop : gestion obligatoire de la position
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Des stops et cibles prédéfinis gèrent l'exposition à la baisse et évitent les hésitations dans des marchés futures en mouvement rapide. Les stops protègent contre des pertes excessives ; les trailing stops verrouillent les gains.
**TRADEX-AI C1** : Chaque signal TRADEX (ACHETER/VENDRE) doit inclure : (1) niveau de stop-loss calculé, (2) target TP1 et TP2, (3) ratio R/R ≥ 1:2 obligatoire (règle verrouillée CLAUDE.md). Aucun signal sans ces trois éléments.
*Catégorie : gestion_position_active*

### D7615 — Gestion du risque au niveau du compte : % fixe par trade
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : La gestion du risque va au-delà des trades individuels. La stratégie doit définir le % du capital risqué par position. Risquer un % fixe et faible du compte sur chaque trade limite les drawdowns lors des séries perdantes et crée une base plus stable pour évaluer la performance.
**TRADEX-AI C1** : Le risk_manager.py doit calculer la taille de position en fonction du capital disponible et du % de risque paramétré par Abdelkrim. Règle par défaut : ≤ 2% du capital par trade.
*Catégorie : gestion_risque_entree*

### D7616 — Règles temporelles et sessions de marché : aligner stratégie sur les horaires de trading
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Les marchés futures tradent ~24h/jour, 6 jours/semaine. Certaines stratégies sont conçues pour des sessions spécifiques (ex. heures du matin US), des jours de la semaine, ou des fenêtres d'impact de news. Des règles de temps peuvent définir quand les positions doivent être fermées (ex. avant la fin de session).
**TRADEX-AI C4** : Les règles temporelles de TRADEX incluent : (a) News Gate 30min avant NFP/FOMC/CPI ; (b) sessions principales des actifs (GC pit = 8h20–13h30 ET, CME Globex = presque 24h). Ces fenêtres sont déjà codées dans settings.py.
*Catégorie : timing*

### D7617 — Choix du marché et du timeframe : stratégie ciblée sur un contrat + timeframe spécifique
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Les stratégies ne fonctionnent pas de manière universelle sur tous les marchés. Un setup conçu pour ES peut se comporter différemment sur le pétrole ou les micro-contrats. Chaque stratégie doit être développée pour un contrat spécifique, un timeframe défini et un biais directionnel (long/short/les deux).
**TRADEX-AI C1** : TRADEX est construit sur 4 actifs TRADING (GC/HG/CL/ZW) avec des paramètres potentiellement différents par actif. Les range bars NT8 (vs daily) sont le timeframe spécifique Belkhayate. Jamais de paramètres universels copiés-collés.
*Catégorie : configuration*

### D7618 — Backtesting : évaluation sur données historiques avant déploiement
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Le backtesting applique la stratégie à des données historiques pour voir comment elle aurait performé. L'optimisation teste différentes valeurs de paramètres pour évaluer la sensibilité de la stratégie aux changements.
**TRADEX-AI C1** : Les résultats du backtest COG/Timing Belkhayate (S11) sur daily bars ont montré que le timeframe daily n'est pas valide pour la méthode (range bars NT8 requis). Cette décision reste verrouillée.
*Catégorie : configuration*

### D7619 — Walk-forward testing et out-of-sample : robustesse de la stratégie
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Le walk-forward testing évalue la performance sur plusieurs segments de temps pour estimer la robustesse. L'out-of-sample testing valide la stratégie sur des données non utilisées lors du développement. Les performances passées ne garantissent pas les résultats futurs.
**TRADEX-AI C1** : Avant tout déploiement en Mode Auto, TRADEX doit être validé en walk-forward sur au moins 3 mois de données range bars NT8. Un test out-of-sample sur 1 mois séparé est obligatoire (règle de garde-fou à ajouter à GARDE_FOUS_PROPOSES.md).
*Catégorie : configuration*

### D7620 — Test en simulation avant live : validation en conditions réelles sans risque
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Le forward testing dans un environnement simulé permet d'observer le comportement de la stratégie en conditions temps réel avant de passer au live. Les systèmes qui performent bien en backtest peuvent se comporter différemment en live.
**TRADEX-AI C1** : Mode Manuel TRADEX = équivalent du forward testing : Abdelkrim observe les signaux et décide lui-même, accumulant de l'expérience avant d'activer le Mode Auto. Le Mode Auto reste BLOQUÉ jusqu'à validation explicite par Abdelkrim.
*Catégorie : psychologie*

### D7621 — Automation de la stratégie : exécution sans intervention manuelle
🟢 **FAIT VÉRIFIÉ** (Source : building_a_trading_strategy.md) : Une fois la stratégie construite et testée, elle peut être automatisée. Les systèmes de trading automatisés exécutent des trades selon des règles prédéfinies sans intervention manuelle. L'automation réduit les biais émotionnels et garantit l'application cohérente des règles.
**TRADEX-AI C1** : Le Mode Auto TRADEX (Niveau ATI NT8, port 36973) est précisément ce système. Il est BLOQUÉ par défaut et ne peut être activé qu'avec confiance ≥ seuil ET aucun critère éliminatoire ET R/R ≥ 1:2. La décision d'activer reste chez Abdelkrim.
*Catégorie : configuration*

### D7622 — Amélioration continue : adaptation aux marchés en évolution
🟡 **SYNTHÈSE** (Source : building_a_trading_strategy.md) : Les marchés évoluent. La volatilité change. Les niveaux de prix changent. Une stratégie qui a bien performé dans certaines conditions peut nécessiter des ajustements. Développer, tester et affiner des stratégies construit de l'expérience et des insights sur le comportement des marchés. L'objectif n'est pas la perfection mais le progrès.
**TRADEX-AI C1** : TRADEX doit prévoir un cycle de révision périodique (mensuel) : vérifier que les paramètres COG/Timing, les seuils de confiance et les garde-fous sont encore adaptés aux conditions de marché actuelles. Cette révision est une responsabilité d'Abdelkrim (Mode Manuel).
*Catégorie : psychologie*

### D7623 — Stratégie structurée = decisions plus objectives et moins émotionnelles
🔵 **ÉCOLE** (Source : building_a_trading_strategy.md) : Un plan de trading bien défini aide à rester discipliné, à s'adapter aux conditions changeantes de marché et à prendre des décisions plus objectives. Au lieu de réagir émotionnellement aux fluctuations de prix, le trader suit des règles prédéfinies alignées avec sa tolérance au risque.
**TRADEX-AI C1** : C'est la valeur fondamentale de TRADEX-AI : encoder la méthode Belkhayate en règles objectives pour qu'Abdelkrim dispose d'un signal structuré, éliminant le biais émotionnel du day trading. Le Mode Manuel maintient le contrôle humain tout en bénéficiant de la rigueur algorithmique.
*Catégorie : psychologie*
