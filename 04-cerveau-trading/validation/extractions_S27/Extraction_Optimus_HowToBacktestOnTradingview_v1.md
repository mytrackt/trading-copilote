# Extraction Optimus — How To Backtest On TradingView
**Source :** `bundles/optimusfutures/how_to_backtest_on_tradingview.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8471 → D8486 · **Page :** https://optimusfutures.com/blog/how-to-backtest-on-tradingview/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : méthodologie de backtest rigoureuse pour valider les règles Belkhayate avant déploiement en mode Auto (Phase C du projet).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8471 — Le backtest permet de tester la viabilité d'une stratégie avant d'engager du capital réel
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Le backtest est le moyen de tester des stratégies de trading sur des données historiques pour valider leur viabilité avant d'engager du capital réel. Bien qu'il ne garantisse pas les résultats futurs, un backtest rigoureux peut éviter des erreurs coûteuses et valider l'intuition de trading.
**TRADEX-AI C1** : Principe fondamental pour la Phase C de TRADEX-AI : toute règle Belkhayate extraite de la KB doit être backtestée sur données NT8 (range bars) avant d'être activée dans le mode Auto. Pas de déploiement Auto sans backtest validé.
*Catégorie : configuration*

### D8472 — Définir clairement la durée et le type de données avant le backtest
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Avant de commencer un backtest, il faut décider de la durée et du type de données : pour les stratégies court terme (minute charts), quelques semaines peuvent suffire; pour les charts daily/weekly, plusieurs années de données sont préférables.
**TRADEX-AI C1** : Pour la Phase C de TRADEX-AI (range bars NT8), la durée minimale recommandée est de plusieurs années de données pour les 4 actifs tradables (GC, HG, CL, ZW) — les range bars ne sont pas des charts temporels standards, ce qui nécessite une quantité de données plus importante.
*Catégorie : configuration*

### D8473 — Définir les règles de stratégie de manière non ambiguë avant de backtester
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Les règles de stratégie (entrée, sortie, gestion du risque, stop-loss, take-profit) doivent être définies de manière cristalline et non ambiguë avant le backtest — toute vagueur génère des incohérences dans les résultats.
**TRADEX-AI C1** : Les règles Belkhayate de la KB doivent être formalisées en conditions logiques précises avant d'être intégrées dans le prompt Claude (niveau 3); les règles ambiguës restent dans A_VERIFIER_HUMAIN.md jusqu'à clarification par Abdelkrim.
*Catégorie : configuration*

### D8474 — Outil Bar Replay de TradingView : backtest manuel barre par barre
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : TradingView propose un outil « Bar Replay » (icône en haut à droite du chart) permettant le backtest manuel : définir un point de départ, avancer barre par barre avec les boutons lecture/avance, appliquer les règles de la stratégie pour décider des entrées/sorties, documenter chaque trade.
**TRADEX-AI C1** : Le Bar Replay TradingView peut être utilisé par Abdelkrim pour valider manuellement les setups Belkhayate sur données historiques avant la Phase C (backtest automatisé NT8) — méthode peu coûteuse pour un premier filtre qualitatif.
*Catégorie : configuration*

### D8475 — Pine Script + Strategy Tester : backtest automatisé sur TradingView
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : TradingView propose Pine Script (langage de script propriétaire) et le Strategy Tester pour le backtest automatisé. Le Strategy Tester affiche : Total Net Profit, Max Drawdown, Percentage of Profitable Trades, et visualise les entrées/sorties sur le graphique principal.
**TRADEX-AI C1** : Pine Script peut servir de prototype de backtest pour les règles Belkhayate AVANT l'implémentation en Python NT8; les métriques Strategy Tester (drawdown, win rate, profit net) sont les mêmes métriques cibles pour la Phase C de TRADEX-AI.
*Catégorie : configuration*

### D8476 — Documenter tous les trades du backtest : entrée, sortie, stop, target, résultat
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Lors d'un backtest manuel, il est impératif de documenter chaque trade : prix d'entrée, prix de sortie, stop-loss, take-profit et résultat du trade. Sans documentation rigoureuse, les résultats agrégés sont inexploitables.
**TRADEX-AI C1** : Le moteur TRADEX-AI doit logger automatiquement tous les signaux générés (même ceux non exécutés en mode Manuel) avec l'horodatage, la direction, le score /10, la confiance % et le R/R calculé — cette base de données constitue le journal de backtest forward pour la validation continue.
*Catégorie : configuration*

### D8477 — Utiliser une quantité de données suffisante pour des résultats représentatifs
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Backtester sur une période trop courte (quelques semaines) donne des résultats biaisés et non représentatifs. Un dataset complet couvrant différentes conditions de marché (tendance, range, volatilité) est nécessaire pour des conclusions fiables.
**TRADEX-AI C1** : La Phase C de TRADEX-AI doit backtester sur au moins 3 à 5 années de données NT8 pour GC, HG, CL, ZW — couvrant différents régimes de marché (bull, bear, range) afin de valider la robustesse des règles Belkhayate dans tous les contextes.
*Catégorie : configuration*

### D8478 — Intégrer le slippage et les commissions dans le backtest
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Le trading réel inclut des coûts de slippage et de commissions. Une stratégie doit rester profitable une fois ces coûts intégrés dans le backtest — si elle n'est profitable qu'avant coûts, elle n'est pas tradable réellement.
**TRADEX-AI C1** : La Phase C de TRADEX-AI doit paramétrer dans les calculs de R/R les coûts réels de commission Rithmic/NTB et le slippage moyen par actif (GC, HG, CL, ZW) — ces données doivent être disponibles dans settings.py (champ `COMMISSION_PER_CONTRACT` et `AVG_SLIPPAGE_TICKS`).
*Catégorie : gestion_risque_entree*

### D8479 — Risque d'overfitting (curve fitting) : stratégie trop ajustée aux données passées
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : L'overfitting survient quand une stratégie est trop ajustée aux données passées, la rendant inefficace sur des données nouvelles. Bonne pratique : diviser le dataset en deux parties — « training » (construction de la stratégie) et « testing » (validation).
**TRADEX-AI C1** : Les règles Belkhayate de la KB sont issues de la méthode de Mustapha Belkhayate (non optimisées sur les données de trading d'Abdelkrim) — ce qui réduit le risque d'overfitting intrinsèque. Cependant, la Phase C doit conserver un échantillon « out-of-sample » pour validation finale.
*Catégorie : configuration*

### D8480 — Diviser le dataset en training (construction) et testing (validation hors-échantillon)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Pour éviter le curve fitting, il est recommandé de diviser les données historiques : une partie pour construire et ajuster la stratégie (training set), une autre partie pour valider les résultats sans toucher aux paramètres (testing set, ou out-of-sample).
**TRADEX-AI C1** : Pour la Phase C, la division recommandée : 70% training (ex. 2018–2023) / 30% testing (ex. 2024–2025) sur les 4 actifs tradables; les règles Belkhayate ne sont ajustées QUE sur le training set, puis validées sans modification sur le testing set.
*Catégorie : configuration*

### D8481 — Réviser et mettre à jour la stratégie régulièrement (marchés évoluent)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Les marchés financiers évoluent. Il est recommandé de revoir et mettre à jour régulièrement la stratégie de trading pour s'assurer qu'elle reste efficace dans les conditions de marché actuelles.
**TRADEX-AI C1** : La KB Belkhayate doit être enrichie régulièrement (processus d'enrichissement inter-sessions via BACKLOG_ENRICHISSEMENTS.md); les règles KB validées en Phase C doivent faire l'objet d'une revue de performance trimestrielle une fois le mode Auto déployé.
*Catégorie : configuration*

### D8482 — Backtest insuffisant si données trop courtes : résultats biaisés
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Une des erreurs les plus courantes en backtesting est de tester sur une période trop courte. Cela donne des résultats statistiquement non significatifs et peut mener à faussement valider une stratégie qui ne fonctionne que dans certaines conditions de marché.
**TRADEX-AI C1** : Applicable directement au backtest COG mené en S11 (invalidé sur données daily) — la note du CLAUDE.md « timeframe ≠ range bars » confirme cette erreur de période de données trop courte/non adaptée; la Phase C corrigera cela avec les range bars NT8 sur plusieurs années.
*Catégorie : configuration*

### D8483 — Stratégies à backtester en priorité : Breakout, Breakdown, Mean-Reversion, Catalyst/News
🟡 **SYNTHÈSE** (Source : how_to_backtest_on_tradingview.md) : Les stratégies futures les plus couramment backtestées : (1) Breakout Trading — direction des cassures de niveaux avec momentum/volume; (2) Breakdown Trading — inverse du breakout (short); (3) Mean-Reversion — retour à la moyenne après déviation significative; (4) Catalyst/News Trading — réaction rapide aux actualités (FOMC, DOE, NFP).
**TRADEX-AI C1** : Ces 4 types de stratégies correspondent aux 4 types de configurations Belkhayate dans la KB (cassure pivot, retour au BGC, signal News Gate); chaque type doit avoir un sous-backtest dédié dans la Phase C pour mesurer les performances par type de setup.
*Catégorie : configuration*

### D8484 — Comprendre les forces fondamentales de chaque marché en complément de l'analyse technique
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Même en utilisant des outils techniques (indicateurs, support/résistance, price action), il est crucial de comprendre les forces fondamentales sous-jacentes qui propulsent chaque marché — les deux doivent être intégrées dans le processus de décision.
**TRADEX-AI C4** : Confirme la nécessité des cercles C3 (institutionnels/COT), C4 (macro) et C6 (géopolitique) dans TRADEX-AI — la méthode Belkhayate est fondamentalement technique, mais le News Gate et les données macro (DX, taux Fed, FOMC) filtrent les conditions fondamentales défavorables.
*Catégorie : macro_evenements*

### D8485 — TradingView + Optimus Futures : données temps réel disponibles sur compte démo
🔵 **ÉCOLE** (Source : how_to_backtest_on_tradingview.md) : Optimus Futures propose l'accès aux données temps réel TradingView via un compte démo gratuit — permettant de backtester avec des données complètes et de tester en temps réel simultanément.
**TRADEX-AI C1** : Le moteur TRADEX-AI utilise NinjaTrader 8 (NT8) avec données Rithmic pour les données temps réel — non TradingView. TradingView peut être utilisé comme outil de validation visuelle complémentaire par Abdelkrim, mais NT8 reste la source de données primaire pour les signaux Belkhayate.
*Catégorie : configuration*

### D8486 — Backtesting : première partie du développement de stratégie, pas une garantie de performance future
🟢 **FAIT VÉRIFIÉ** (Source : how_to_backtest_on_tradingview.md) : Le backtesting n'est qu'une composante du développement de stratégie. Les performances passées ne garantissent pas les résultats futurs — le backtest doit être suivi d'un forward testing (paper trading), d'une révision régulière et d'une gestion du risque rigoureuse.
**TRADEX-AI C1** : La progression validée pour TRADEX-AI : Phase C (backtest NT8 range bars) → paper trading mode Auto en observation → Mode Auto activable par Abdelkrim sur capital réduit → suivi de performance continu. Le mode Auto reste BLOQUÉ par défaut jusqu'à la fin de la Phase C validée.
*Catégorie : configuration*
