# Extraction Optimus — Backtesting Trading Strategies In Futures Markets
**Source :** `bundles/optimusfutures/backtesting_trading_strategies_in_futures_markets.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption locale · 0/0 certifiées · 0 décoratives (aucune figure HTML sur la page)
**Décisions :** D8271 → D8290 · **Page :** https://optimusfutures.com/blog/backtesting-trading-strategies-in-futures-markets/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthodologie de validation des stratégies de trading par backtesting — applicable à la validation des règles Belkhayate avant déploiement TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune image certifiée — aucune figure HTML sur la page)*

## DÉCISIONS

### D8271 — Définition backtesting : évaluation historique d'une stratégie
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Le backtesting est une méthode d'évaluation qui simule comment une stratégie aurait performé dans le passé. La performance passée "POURRAIT" ressembler aux résultats futurs, mais ne les garantit jamais. Disclaimer obligatoire : "past performance doesn't necessarily indicate future results."
**TRADEX-AI C1** : Toute règle Belkhayate intégrée dans la KB TRADEX-AI doit avoir subi un backtesting (même manuel) avant d'être activée en mode Auto. Le disclaimer légal est visible en permanence dans l'interface — conforme à cette règle.
*Catégorie : gestion_risque_entree*

### D8272 — Ordres réels ≠ ordres backtest : slippage et fills manqués
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : En live, les ordres ne sont pas tous exécutés comme en backtest. Les variances négatives = slippage coûteux ou trades manqués. Les émotions (peur, hésitation) absentes du backtest sont présentes en live et peuvent changer radicalement les résultats.
**TRADEX-AI C1** : En mode Manuel, Abdelkrim peut ne pas exécuter un signal Belkhayate valide à cause des émotions. Le dashboard TRADEX-AI doit afficher le signal avec confiance % et R/R pour faciliter la décision rationnelle. Le mode Auto évite ce biais, mais uniquement si score ≥ 7.0 ET pas de critère éliminatoire.
*Catégorie : psychologie*

### D8273 — Taille d'échantillon critique : semaines insuffisantes, années nécessaires
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Une semaine de données produit des résultats non fiables. Ajouter une semaine change les résultats significativement. Des années voire des décennies de données donnent une image plus précise. Plus l'échantillon est grand, plus le backtesting est réaliste.
**TRADEX-AI C1** : La KB Belkhayate doit être validée sur des données historiques suffisantes (minimum 1 an de données NT8 range bars). Le backtest daily COG déjà réalisé en S11 (invalide — mauvaise timeframe) illustre exactement ce problème. Phase C : collecter au minimum 2 ans de données range bars sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D8274 — Curve fitting : optimiser sur une période = stratégie fragile hors période
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Sur-optimiser une stratégie sur une période spécifique (curve fitting) la rend inefficace sur d'autres périodes. Comme "étudier pour réussir le test" vs "étudier la matière" — le premier est étroit et fragile, le second est robuste et généraliste.
**TRADEX-AI C1** : Les règles Belkhayate dans la KB doivent être robustes sur TOUTES les conditions de marché (trend, range, volatil). Ne jamais ajuster les paramètres COG (180/3/0.618/1.618 déjà figés) pour optimiser sur une période spécifique. Les paramètres figés en S11 respectent ce principe.
*Catégorie : configuration*

### D8275 — Backtest vs Market Replay : résultats instantanés vs émotions simulées
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Backtesting automatisé = résultats en secondes sur des années de données, sans émotions. Market Replay = simulation quasi-temps-réel sur données historiques, avec contrôle (pause, avance, recul barre par barre), proche des émotions réelles mais chronophage.
**TRADEX-AI C1** : Pour valider les règles Belkhayate, utiliser d'abord le backtesting automatisé (années de données rapides) puis Market Replay sur les setups critiques (COG, Timing) pour vérifier l'exécution émotionnelle. NinjaTrader 8 offre ces deux outils nativement.
*Catégorie : configuration*

### D8276 — Agrégation ticks : plus granulaire pour HFT, 1-minute pour hebdomadaire
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Agrégation ticks = plus détaillée, idéale pour stratégies haute fréquence. Agrégation 1 minute = meilleure pour tests hebdomadaires et accélère le processus. Agrégation 1 jour = idéale pour tests longs (mois/années) et changements saisonniers.
**TRADEX-AI C1** : TRADEX-AI opère sur range bars NT8 (non conforme au daily backtest S11 — erreur corrigée). Les tests de validation Phase C doivent utiliser range bars (ou ticks) pour respecter la timeframe réelle d'opération.
*Catégorie : configuration*

### D8277 — Métriques clés backtest : profit factor, win rate, drawdown
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Les métriques essentielles à analyser sont : profit factor, win/loss rate, profit et loss moyens, max drawdown, distribution des profits et pertes. Formule R/R simplifiée : (Win% × Taille_Gain_Moyen) − (Loss% × Taille_Perte_Moyenne).
**TRADEX-AI C1** : Intégrer ces métriques dans le rapport de validation Phase C. Seuil minimum acceptable : profit factor > 1.5, max drawdown < 15% du capital, win rate > 45% avec R/R ≥ 1:2. Ces seuils sont cohérents avec la règle R/R ≥ 1:2 déjà verrouillée dans TRADEX-AI.
*Catégorie : gestion_risque_entree*

### D8278 — Commissions incluses : les frais changent la rentabilité réelle
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Le champ "fee per side" dans le backtesting permet d'inclure commissions et frais dans chaque trade. Les résultats sans frais peuvent être trompeurs — une stratégie rentable brute peut devenir perdante nette des commissions.
**TRADEX-AI C1** : Dans le backtesting Phase C, inclure les frais Rithmic/NTB par trade (roundturn). Pour GC : ~$5-8/roundturn. Cette inclusion est obligatoire pour obtenir des métriques réalistes et ne pas surestimer la rentabilité Belkhayate.
*Catégorie : gestion_risque_entree*

### D8279 — Netting : une seule position nette par symbole avec plusieurs stratégies
🔵 **ÉCOLE** (Source : backtesting_trading_strategies_in_futures_markets.md) : Le netting permet de voir le résultat cumulatif en temps réel quand plusieurs stratégies tournent simultanément sur le même symbole. Utile pour quantifier l'exposition nette globale sur un actif.
**TRADEX-AI C1** : TRADEX-AI ne trade qu'une stratégie à la fois par actif (règle verrouillée). Le netting n'est pas applicable dans la configuration actuelle, mais à garder en tête si futures versions multi-stratégies.
*Catégorie : configuration*

### D8280 — OHLC vs Open-only vs Close-only : schémas de modélisation
🔵 **ÉCOLE** (Source : backtesting_trading_strategies_in_futures_markets.md) : Le "modeling scheme" détermine comment les cotations sont générées pendant le backtest. OHLC = complet (recommandé). Open only ou Close only = simplifiés, moins précis mais plus rapides.
**TRADEX-AI C1** : Pour la validation des règles Belkhayate sur range bars, utiliser impérativement le schéma OHLC (le plus précis). Les règles Belkhayate analysent high/low/close explicitement (BGC, Timing, COG).
*Catégorie : configuration*

### D8281 — Backtesting = art + science : compétences spécifiques requises
🟡 **SYNTHÈSE** (Source : backtesting_trading_strategies_in_futures_markets.md) : Le backtesting requiert : choisir les bonnes données historiques, tweaker sans curve-fitter, interpréter l'écart simulation/réalité. C'est une compétence distincte du trading lui-même. La simulation est le plus proche du live sans risquer du capital.
**TRADEX-AI C1** : La validation des règles KB Belkhayate par backtesting est une étape obligatoire avant déploiement en mode Auto. Abdelkrim doit d'abord valider les signaux en mode Manuel pendant au moins 2 semaines avant d'activer le mode Auto sur un actif donné.
*Catégorie : psychologie*

### D8282 — Market Replay : tester plusieurs instruments simultanément
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Market Replay permet de tester plusieurs instruments financiers simultanément, sur des types de charts variés (Heiken Ashi, Tick, Point & Figure, Range, Renko), avec Depth of Market et TPO Profile Charts.
**TRADEX-AI C1** : La validation multi-actifs (GC + HG + CL + ZW simultanément) est possible avec Market Replay NT8. Important pour tester la règle 3/4 actifs trading alignés — condition nécessaire au déclenchement niveau 1 TRADEX-AI.
*Catégorie : configuration*

### D8283 — Mode interactif vs quick backtest : visualisation vs vitesse maximale
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Mode interactif = voir le processus en cours (slider vitesse), utile pour comprendre chaque trade. Quick backtest (mode interactif OFF) = résultats immédiats à vitesse maximale, sans visualisation du processus.
**TRADEX-AI C1** : Pour les validations bulk des règles KB (>500 trades), utiliser le quick backtest. Pour la vérification fine des signaux Belkhayate sur setups spécifiques (COG divergence, Timing aligné), utiliser le mode interactif NT8.
*Catégorie : configuration*

### D8284 — Peur absente en backtest = biais de performance positif
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : L'absence de peur en backtest est un désavantage majeur car ces émotions impactent fortement le trading live. Les traders ferment des trades prématurément ou refusent de prendre des trades par peur — comportements absents en simulation.
**TRADEX-AI C1** : Le mode Manuel TRADEX-AI avec affichage du signal Belkhayate (confiance % + R/R) réduit ce biais en fournissant un ancrage rationnel à la décision. Le journal de trading doit documenter les trades refusés malgré un signal valide pour mesurer ce biais psychologique.
*Catégorie : psychologie*

### D8285 — Export Excel : analyse approfondie des résultats hors plateforme
🟢 **FAIT VÉRIFIÉ** (Source : backtesting_trading_strategies_in_futures_markets.md) : Market Replay permet d'exporter l'historique des transactions en Excel pour analyse approfondie (profit factor, distribution gains/pertes, win rate, drawdowns). Cet export est disponible via le panneau "Trades".
**TRADEX-AI C1** : Intégrer un export CSV automatique des performances TRADEX-AI (signaux générés, trades exécutés, résultats) pour analyse périodique. Stocker dans 05-saas/data/ (dossier à créer Phase C). Format compatible avec les métriques de backtesting NT8.
*Catégorie : configuration*
