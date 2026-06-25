# Extraction NinjaTrader — Futures Trading Risk Management (Margin, Leverage, Stops, Position Sizing)
**Source :** `bundles/ninjatrader/futures_trading_risk_management_margin_leverage_stops_position_sizing.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7691 → D7710 · **Page :** https://ninjatrader.com/futures/blogs/futures-trading-risk-management-margin-leverage-stops-position-sizing/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : 4 piliers du risk management futures (margin, leverage, stops, position sizing) — fondements du risk_manager.py et des garde-fous TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune image sur la page source)*

---

## DÉCISIONS

### D7691 — Priorité risk management sur stratégie en futures : règle fondamentale
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : En futures, la gestion du risque doit primer sur la stratégie — le levier amplifie à la fois les opportunités et les risques. Sans structure de risk management, les traders sur-exposent leur compte, sur-dimensionnent les positions, bougent les stops émotionnellement et sous-estiment la volatilité.
**TRADEX-AI C1** : La règle fondamentale de TRADEX : le risk_manager.py est le premier module consulté avant tout signal — même un signal Belkhayate parfait ne passe pas si le risk manager bloque (VIX élevé, perte récente, marges insuffisantes).
*Catégorie : gestion_risque_entree*

### D7692 — Définition marge futures : dépôt de bonne foi, pas un frais
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : La marge futures n'est PAS un frais — c'est un dépôt de bonne foi (collatéral) requis pour ouvrir et maintenir une position. Marge initiale = pour ouvrir. Marge de maintenance = minimum requis pour maintenir. Il est possible de perdre plus que la marge initiale.
**TRADEX-AI C1** : risk_manager.py doit vérifier : (1) marge initiale disponible avant tout ordre, (2) cushion au-dessus de la maintenance margin pour éviter les liquidations forcées — bloquer le mode Auto si marge insuffisante.
*Catégorie : gestion_risque_entree*

### D7693 — Levier futures : contrôler une grande valeur notionnelle avec peu de capital
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Le levier permet de contrôler la valeur totale du contrat avec une fraction de ce capital. Exemple : contrat contrôlant 100 000$ de valeur notionnelle avec 5 000$ de marge = levier 20:1. Gains ET pertes sont magnifiés par ce ratio.
**TRADEX-AI C1** : Dans le prompt Claude Brain, le levier réel doit être communiqué pour contextualiser le risque : "Position GC = X contrats → valeur notionnelle Y$ → exposition réelle vs account Z$" — Abdelkrim doit visualiser l'exposition complète en mode Manuel.
*Catégorie : gestion_risque_entree*

### D7694 — Stop-loss : définir le risque AVANT l'entrée, pas après
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Le stop-loss est l'outil le plus important du risk management futures. Il doit : définir le risque avant l'entrée, automatiser les sorties, supprimer l'émotion. Les stops ne doivent PAS être aléatoires — ils doivent être structurés (au-delà de support/résistance, en dehors des value areas, au-delà des swing highs/lows récents, basés sur la volatilité).
**TRADEX-AI C1** : Règle implémentation TRADEX : chaque signal généré par Claude Brain DOIT inclure le niveau de stop-loss structuré calculé automatiquement — jamais de signal sans stop défini. Le stop est basé sur la structure de marché Belkhayate, pas sur un pourcentage arbitraire.
*Catégorie : gestion_risque_entree*

### D7695 — Question clé du stop : "où mon idée est-elle invalidée ?"
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : La vraie question pour placer un stop : "Où mon idée de trade est-elle invalidée ?" Si le prix atteint ce point, la prémisse est fausse — la protection du capital passe en priorité absolue. Les stops ne sont pas pessimistes, ils sont préparatoires.
**TRADEX-AI C1** : Claude Brain doit explicitement formuler dans sa réponse : "L'idée de trade est invalidée si prix atteint [niveau X]" — ce niveau devient automatiquement le stop-loss proposé en mode Manuel et le stop automatique en mode Auto.
*Catégorie : gestion_risque_entree*

### D7696 — Position sizing : formule mathématique risque/stop/contrat
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Formule de position sizing : Nombre de contrats = (Account size × % risque par trade) ÷ (Stop distance en ticks × valeur par tick). Exemple : compte 20 000$, risque 1% = 200$, stop 10 ticks, tick value 5$ → 200 ÷ (5 × 10) = 4 contrats.
**TRADEX-AI C1** : Implémenter dans risk_manager.py : calculer automatiquement le nombre de contrats pour chaque signal en fonction du compte, du % risque configuré et du stop défini — afficher le résultat en mode Manuel, appliquer automatiquement en mode Auto.
*Catégorie : gestion_position_active*

### D7697 — Position sizing relie stop placement au compte pour limiter l'impact d'un trade
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Le position sizing connecte le placement du stop au compte pour qu'aucun trade individuel n'ait un impact disproportionné. Les micro-contrats permettent de fine-tuner le risque pour que la taille de position reflète la tolérance réelle, pas les émotions.
**TRADEX-AI C1** : Les micro-contrats (MES, MGC, MHG, MCL) disponibles en NT8 permettent à Abdelkrim de calibrer finement le risque TRADEX — à intégrer dans les paramètres de settings.py avec les tick values correspondantes.
*Catégorie : gestion_position_active*

### D7698 — 6 erreurs de risk management à éviter impérativement
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Les 6 erreurs principales : (1) pourcentages de risque incohérents par trade, (2) augmenter la taille après des pertes, (3) bouger les stops plus loin, (4) ignorer les exigences de marge, (5) trader trop de positions corrélées, (6) négliger l'impact des commissions et frais.
**TRADEX-AI C1** : Ces 6 erreurs doivent être des garde-fous codés dans risk_manager.py : (2) bloquer augmentation de taille post-perte, (3) interdire modification de stop en mode Auto, (4) vérifier marges avant ordre, (5) limiter les positions simultanées corrélées GC/HG/CL.
*Catégorie : gestion_risque_entree*

### D7699 — Maximum daily loss : seuil strict d'arrêt de trading
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Un plan de risk management doit inclure une perte quotidienne maximale — point de coupure clair, arrêt de trading immédiat une fois atteint. Protège contre les spirales émotionnelles.
**TRADEX-AI C1** : risk_manager.py : implémenter MAX_DAILY_LOSS paramétrable dans settings.py — quand la perte journalière atteint ce seuil, désactiver le mode Auto ET afficher un avertissement bloquant en mode Manuel jusqu'à reset du lendemain.
*Catégorie : gestion_risque_entree*

### D7700 — Maintain cushion au-dessus de la maintenance margin
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Éviter le sur-levier — maintenir un coussin de capital au-dessus de la maintenance margin pour réduire le risque de liquidations forcées par le broker.
**TRADEX-AI C1** : Paramètre MARGIN_CUSHION_PCT dans settings.py : définir le pourcentage minimum de buffer au-dessus de la maintenance margin — si l'account tombe en dessous de (maintenance_margin × (1 + MARGIN_CUSHION_PCT)), bloquer le mode Auto.
*Catégorie : gestion_risque_entree*

### D7701 — Stops structurés : ne jamais les déplacer par émotion
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Les stops doivent être structurés et placés selon la structure de marché — jamais déplacés émotionnellement (plus loin pour "donner plus de chance"). Les décisions objectives protègent la cohérence du système.
**TRADEX-AI C1** : En mode Auto TRADEX : interdiction absolue de modifier un stop-loss une fois posé — l'ATI NT8 ne reçoit une instruction de modification de stop que si le risk_manager.py génère un trailing stop basé sur des règles objectives prédéfinies.
*Catégorie : gestion_position_active*

### D7702 — Periodic review : suivre drawdowns et ajuster la taille uniquement sur données
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Le plan de risk management doit inclure une revue périodique : suivre les drawdowns, monitorer le risque moyen par trade, ajuster la taille uniquement sur base de données. La revue transforme l'expérience en amélioration.
**TRADEX-AI C1** : TRADEX doit logguer chaque trade (entrée, sortie, stop réel, P&L, % risque) dans SQLite pour permettre la revue périodique d'Abdelkrim — base de la boucle d'amélioration continue du système.
*Catégorie : gestion_position_active*

### D7703 — Les commissions et frais affectent le breakeven : à intégrer dans le calcul
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Les commissions et frais affectent le point de breakeven réel — ils doivent être intégrés dans la planification. Les petites inefficacités répétées se cumulent et creusent le drawdown.
**TRADEX-AI C1** : risk_manager.py doit inclure COMMISSION_PER_CONTRACT dans settings.py — intégrer le coût réel dans le calcul de R/R minimum requis (R/R ≥ 1:2 APRÈS commissions) pour chaque signal TRADEX.
*Catégorie : gestion_risque_entree*

### D7704 — Les 4 piliers du risk management futures : synthèse
🟡 **SYNTHÈSE** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Les 4 piliers indissociables : Marge = accès. Levier = exposition. Stops = définition du risque baissier. Position sizing = détermine l'impact. Ensemble ils créent un cadre qui protège le capital tout en permettant la croissance. Le risk management ne limite pas la croissance — il la rend durable.
**TRADEX-AI C1** : Architecture risk_manager.py en 4 modules alignés : (1) MarginChecker, (2) LeverageCalculator, (3) StopManager, (4) PositionSizer — chacun s'exécute séquentiellement avant tout signal Auto pour garantir l'intégrité du système TRADEX.
*Catégorie : configuration*

### D7705 — Risquer des pourcentages incohérents : erreur de variabilité critique
🟢 **FAIT VÉRIFIÉ** (Source : futures_trading_risk_management_margin_leverage_stops_position_sizing.md) : Risquer des pourcentages variables par trade augmente la variabilité des résultats et accroît les drawdowns. La cohérence du pourcentage de risque par trade est la base de la reproductibilité des résultats.
**TRADEX-AI C1** : settings.py : RISK_PCT_PER_TRADE fixé en configuration — non modifiable en cours de session. Abdelkrim ne peut changer ce paramètre qu'entre sessions via fichier de config, jamais à chaud.
*Catégorie : gestion_risque_entree*

