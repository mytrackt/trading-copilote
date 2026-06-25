# Extraction NinjaTrader — Z-Score Futures Trading Strategy
**Source :** `bundles/ninjatrader/z_score_futures_trading_strategy.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8231 → D8250 · **Page :** https://ninjatrader.com/futures/blogs/z-score-futures-trading-strategy/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Z-Score VWAP comme oscillateur statistique de mean reversion — enrichit C1/C2 pour détecter les extensions extrêmes de prix sur GC/HG/CL/ZW avec fondement mathématique.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8231 — Z-Score : définition et formule de base
🔵 **ÉCOLE** (Source : z_score_futures_trading_strategy.md) : Le Z-score mesure combien d'écarts-types une valeur se situe au-dessus ou en dessous de la moyenne d'un dataset. Formule : z = (x − μ) / σ, où x = prix actuel, μ = moyenne sur la période lookback, σ = écart-type sur la même période. Z=0 = prix à la moyenne ; Z=+2 = prix 2 écarts-types au-dessus ; Z=−2 = prix 2 écarts-types en dessous.
**TRADEX-AI C1** : Le Z-score traduit en chiffre objectif ce que Belkhayate appelle "éloignement du centre de gravité". Un Z-score ±2 est l'équivalent statistique d'un prix extrêmement écarté de son COG — signal de mean reversion.
*Catégorie : indicateurs_momentum*

### D8232 — Z-score vs Bollinger Bands : différence clé
🔵 **ÉCOLE** (Source : z_score_futures_trading_strategy.md) : Les Bollinger Bands et le Z-score mesurent tous deux l'écart-type par rapport à une moyenne. Différence : les Bollinger Bands s'affichent sur le chart prix sous forme de bandes visuelles ; le Z-score est un oscillateur séparé exprimant la même relation en valeur numérique unique. Le Z-score est plus facile à comparer entre marchés et timeframes.
**TRADEX-AI C1** : TRADEX-AI peut utiliser le Z-score comme couche numérique complémentaire aux niveaux COG Belkhayate (analogues aux Bollinger Bands). Z-score > +2 sur GC = prix statistiquement étendu → prudence sur signal ACHETER, opportunité pour VENDRE.
*Catégorie : indicateurs_momentum*

### D8233 — Principe de mean reversion : base mathématique du Z-score
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : La mean reversion stipule que les prix d'actifs, après s'être significativement écartés de leur moyenne historique, tendent à y revenir. Le Z-score donne à ce principe une fondation mathématique précise en convertissant l'observation générale en signal quantifiable.
**TRADEX-AI C1** : La mean reversion est cohérente avec la méthode Belkhayate (retour vers le COG). Le Z-score quantifie cet écart. En TRADEX-AI : Z-score extrême + niveau Belkhayate significatif = double confirmation de mean reversion.
*Catégorie : structure_marche*

### D8234 — Seuil ±2 écarts-types : zone statistiquement rare
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Dans une distribution normale, environ 95% des valeurs se situent dans ±2 écarts-types de la moyenne. Un Z-score au-delà de ±2 est donc statistiquement rare (se produit seulement ~5% du temps) et constitue une zone d'intérêt pour les traders mean reversion.
**TRADEX-AI C1** : Règle opérationnelle : Z-score ≥ +2 ou ≤ −2 sur un actif tradable = condition suffisante pour déclencher l'analyse complète TRADEX-AI (passage niveau 1→2→3). Valide pour GC/HG/CL/ZW en conditions de marché non-trending.
*Catégorie : gestion_risque_entree*

### D8235 — VWAP Z-score : combinaison volume + écart statistique
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Le VWAP Z-score combine le VWAP (prix moyen pondéré par volume = "juste valeur") avec le calcul Z-score pour mesurer si le prix actuel est extrêmement écarté de cette juste valeur de session. Formule appliquée : z = (prix actuel − VWAP) / σ(prix sur lookback).
**TRADEX-AI C2** : VWAP Z-score est un indicateur C2 (Order Flow + Volume) de haute valeur pour TRADEX-AI. Il quantifie l'écart du prix par rapport à la "juste valeur" institutionnelle de la session — directement cohérent avec la philosophie Belkhayate de retour vers l'équilibre.
*Catégorie : indicateurs_momentum*

### D8236 — VWAP reset de session : pertinence intraday
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Le VWAP se réinitialise à chaque début de session, gardant la baseline statistique pertinente par rapport aux conditions actuelles du marché. Cette caractéristique le rend particulièrement adapté aux day traders futures car il reflète l'offre et la demande réelles de la journée.
**TRADEX-AI C2** : Pour les signaux intraday sur GC/CL, le VWAP de session est la référence de "juste valeur" du jour. Intégrer dans data_reader.py le calcul VWAP reset quotidien pour les actifs tradables.
*Catégorie : timing*

### D8237 — Lookback period : calibrage de la sensibilité Z-score
🔵 **ÉCOLE** (Source : z_score_futures_trading_strategy.md) : Le lookback period détermine la sensibilité du Z-score. Lookback court (10-15 barres) = signaux plus fréquents mais plus de bruit. Lookback long (20-30 barres) = moins de signaux mais plus de robustesse statistique. Pas de réglage universel : dépend du timeframe, du rythme du marché et de la tolérance au risque.
**TRADEX-AI C1** : Recommandation initiale pour TRADEX-AI : lookback 20 barres comme point de départ sur les range bars NT8, à affiner par marché (GC vs CL vs ZW peuvent nécessiter des paramètres différents selon leur volatilité).
*Catégorie : indicateurs_momentum*

### D8238 — Règles d'entrée longue et courte sur Z-score VWAP
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Règles d'entrée Z-score VWAP : Long : Z-score ≤ −2 (prix à discount extrême vs VWAP) + attendre que Z-score commence à remonter vers zéro avant d'entrer (confirmation de retournement de momentum). Court : Z-score ≥ +2 (prix à premium extrême vs VWAP) + attendre que Z-score commence à baisser vers zéro.
**TRADEX-AI C1/C2** : Ces règles d'entrée sont directement intégrables dans la grille de décision TRADEX-AI. Condition Z-score ≤ −2 en retournement = point favorable pour signal ACHETER. Z-score ≥ +2 en retournement = point favorable pour signal VENDRE. À croiser avec C1 Belkhayate.
*Catégorie : gestion_risque_entree*

### D8239 — Cibles de sortie Z-score : zéro et ±1
🔵 **ÉCOLE** (Source : z_score_futures_trading_strategy.md) : Les cibles de sortie naturelles pour une stratégie mean reversion Z-score sont : (1) cible principale = ligne zéro (retour complet au VWAP) ; (2) prise de profit partielle à ±1 avec trailing du reste vers zéro. Le contexte horaire (fin de session) ajoute un risque supplémentaire pour les positions non résolues.
**TRADEX-AI C1** : Intégrer dans la grille R/R TRADEX-AI : target naturelle = VWAP (retour à zéro) pour les trades mean reversion. Ce niveau est cohérent avec le COG Belkhayate comme objectif de retour. R/R ≥ 1:2 requis (CLAUDE.md).
*Catégorie : gestion_position_active*

### D8240 — Z-score invalide en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Le risque principal du Z-score est de fader (contrer) une tendance forte. En conditions trending, le Z-score peut rester à des niveaux extrêmes prolongés tandis que le prix continue d'étendre. Toujours évaluer le contexte de marché (range vs trending) avant d'agir sur un Z-score extrême.
**TRADEX-AI C1** : Garde-fou obligatoire pour TRADEX-AI : avant d'utiliser un signal Z-score mean reversion, vérifier la direction Belkhayate (BGC + Direction). Si la Direction Belkhayate est fortement orientée, le signal Z-score est inhibé (le Z-score peut rester extrême longtemps en tendance).
*Catégorie : gestion_risque_entree*

### D8241 — Stop-loss obligatoire sur trades Z-score
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Même si Z-score ±2 est statistiquement étendu, le prix peut toujours s'étendre davantage, particulièrement en période de forte volatilité. Un stop-loss dur est non-négociable sur tous les trades basés sur Z-score.
**TRADEX-AI C1** : Cohérent avec les règles TRADEX-AI existantes (gestion_risque_entree). Sur les trades mean reversion identifiés par Z-score, le stop doit être placé au-delà de ±3 écarts-types (extension statistiquement très rare) pour éviter les stops prématurés tout en limitant l'exposition.
*Catégorie : gestion_risque_entree*

### D8242 — Marchés optimal pour Z-score : liquides et mean-reverting
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Les stratégies Z-score performent mieux sur des marchés liquides à comportement mean-reverting, en conditions non-trending. Marchés cités : indices équités (ES, NQ, RTY), taux d'intérêt, devises futures. L'or et les matières premières sont implicitement inclus dans les marchés liquides à terme.
**TRADEX-AI C1** : GC (Or) est un marché liquide avec des phases mean-reverting fréquentes → Z-score VWAP particulièrement adapté. CL (Pétrole) en période de basse volatilité géopolitique aussi. HG et ZW à valider selon leur régime de marché actuel.
*Catégorie : correlations*

### D8243 — Limiter le nombre de signaux Z-score par session
🟢 **FAIT VÉRIFIÉ** (Source : z_score_futures_trading_strategy.md) : Les multiples extrêmes Z-score dans une session peuvent pousser au surtrading. Les premiers 1 ou 2 extrêmes propres de la journée ont statistiquement le plus de poids ; prioriser la qualité sur la quantité.
**TRADEX-AI C7** : Dans la logique d'architecture événementielle TRADEX-AI (max 1 analyse/10s, niveau 1 filtrant), limiter à 2 signaux Z-score actionnables par session et par actif. Le 3ème signal Z-score de la journée sur le même actif = score réduit automatiquement de 1 point dans la grille /10.
*Catégorie : gestion_position_active*

### D8244 — Z-score comme filtre d'invalidation dans la grille TRADEX
🟡 **SYNTHÈSE** (Source : z_score_futures_trading_strategy.md) : Le Z-score n'est pas une stratégie isolée mais un outil de filtre et de contexte. Il distingue les niveaux de prix avec un avantage statistique réel des niveaux qui ne sont que du bruit quotidien ordinaire.
**TRADEX-AI C1** : Dans la grille de décision /10 TRADEX-AI, le Z-score VWAP contribue à C1 (Prix) : Z-score ±2 en retournement = +1 point ; Z-score neutre (entre −1 et +1) = 0 point ; Z-score extrême en continuation de tendance = −0.5 point (signal contrarian à contre-courant non justifié).
*Catégorie : indicateurs_momentum*
