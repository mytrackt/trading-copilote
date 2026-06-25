# Extraction StockCharts — Trading Strategies (Index)
**Source :** `bundles/stockcharts/trading_strategies.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D4511 → D4530 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : page index listant 22 stratégies de trading StockCharts — plusieurs directement applicables à TRADEX (Bollinger, CCI, VIX CVR3, MACD, RSI2, Moving Average) ; carte complète des stratégies disponibles pour enrichissement futur de la KB.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

## DÉCISIONS

### D4511 — Bollinger Band Squeeze : contraction de volatilité précède un mouvement significatif
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie Bollinger Band Squeeze utilise les Bollinger Bands pour identifier la contraction de volatilité (bandes se rapprochent = Bandwidth faible) qui peut précéder une avance ou un déclin significatif. Quand la volatilité comprime, le marché se prépare à un mouvement directionnel fort.
**TRADEX-AI C1** : Applicable à GC/HG/CL/ZW — une compression de volatilité sur les Bollinger Bands précède souvent des breakouts. À intégrer comme signal de préparation au trade dans C1 (Prix/Belkhayate) en conjonction avec l'Énergie Belkhayate (stub actuel).
*Catégorie : indicateurs_tendance*

### D4512 — CCI Correction : CCI hebdomadaire = biais directionnel, CCI journalier = signal d'entrée
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie CCI Correction utilise le CCI (Commodity Channel Index) hebdomadaire pour définir le biais de trading (tendance de fond) et le CCI journalier pour générer les signaux d'achat et vente. Double temporalité : tendance long terme filtre les signaux court terme.
**TRADEX-AI C1** : Double timeframe CCI = technique multi-temporelle alignée avec Belkhayate (timeframe supérieur donne le biais, inférieur donne l'entrée). Pour GC/HG/CL/ZW : CCI hebdo > 0 = biais long, CCI journalier en pullback = entrée. À évaluer pour enrichissement KB.
*Catégorie : indicateurs_momentum*

### D4513 — CVR3 VIX Market Timing : lectures extrêmes du VIX génèrent signaux S&P 500
🟢 **FAIT VÉRIFIÉ** (Source : trading_strategies.md) : Développée par Larry Connors et Dave Landry, CVR3 utilise les lectures extrêmes du CBOE Volatility Index ($VIX) pour générer des signaux d'achat et vente sur le S&P 500. Les pics de VIX (peur extrême) génèrent des signaux d'achat ; les creux de VIX (complaisance extrême) génèrent des signaux de vente.
**TRADEX-AI C5** : VIX = Cercle 5 (Sentiment) dans TRADEX. La stratégie CVR3 valide l'usage du VX comme indicateur de sentiment contrarian pour ES. Si VIX extrêmement élevé → signal d'achat potentiel ES (confirmation C5 pour TRADEX). Déjà intégré dans le concept des 7 cercles.
*Catégorie : indicateurs_momentum*

### D4514 — Faber Sector Rotation : achat des secteurs les plus performants, rééquilibrage mensuel
🔵 **ÉCOLE** (Source : trading_strategies.md) : Basée sur les recherches de Mebane Faber, cette stratégie de rotation sectorielle achète les secteurs les plus performants et rééquilibre une fois par mois. Principe : les tendances sectorielles persistent sur plusieurs mois (momentum sectoriel).
**TRADEX-AI C4** : Macro — la rotation sectorielle affecte les commodités (GC/HG/CL/ZW). Quand l'énergie surperforme → CL haussier ; quand les métaux précieux surperforment → GC haussier. Pertinent pour le biais macro mensuel de TRADEX.
*Catégorie : correlations*

### D4515 — Gap Trading Strategies : diverses stratégies basées sur les gaps d'ouverture
🔵 **ÉCOLE** (Source : trading_strategies.md) : Les Gap Trading Strategies couvrent diverses approches pour trader les gaps (écarts de prix à l'ouverture). Les gaps peuvent être des zones de continuation (gap and go) ou de retournement (gap fill). Différents types de gaps ont des implications différentes.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW (futures CME/CBOT), les gaps overnight entre la clôture NYMEX et l'ouverture asiatique créent des opportunités. À intégrer dans la détection de structure de marché (C1) pour les actifs TRADEX.
*Catégorie : structure_marche*

### D4516 — Harmonic Patterns : avantages et inconvénients des patterns harmoniques
🔵 **ÉCOLE** (Source : trading_strategies.md) : Les Harmonic Patterns (Gartley, Butterfly, Bat, Crab) utilisent des ratios de Fibonacci pour identifier des points de retournement précis. Avantages : points d'entrée et de sortie objectifs. Inconvénients : subjectivité dans l'identification et faible fréquence des setups.
**TRADEX-AI C1** : Les ratios de Fibonacci sont utilisés dans la méthode Belkhayate (coefficients 0.618/1.618 du COG). Les Harmonic Patterns peuvent renforcer les niveaux Belkhayate sur GC/HG/CL/ZW en définissant des zones de confluences.
*Catégorie : configuration*

### D4517 — Hindenburg Omen : signal de risque de retournement boursier global
🔵 **ÉCOLE** (Source : trading_strategies.md) : L'Hindenburg Omen est un pattern technique qui indique le risque potentiel d'un déclin boursier. Signal de marché global (macro), pas d'actif individuel. Utilisé pour calibrer l'exposition globale au risque.
**TRADEX-AI C5** : Sentiment/risque macro — l'Hindenburg Omen est un signal de risque système. Quand actif, réduire l'exposition sur tous les actifs TRADEX (GC/HG/CL/ZW). À intégrer dans le macro_evenements comme garde-fou global.
*Catégorie : macro_evenements*

### D4518 — Ichimoku Cloud : biais de trading, corrections, points de retournement court terme
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie Ichimoku Cloud utilise le nuage Ichimoku pour : (1) définir le biais de trading (au-dessus du nuage = bullish) ; (2) identifier les corrections dans la tendance ; (3) signaler les retournements court terme (croisements Tenkan/Kijun).
**TRADEX-AI C1** : Ichimoku = système complet incluant tendance + momentum + support/résistance. Sur GC (Or), l'Ichimoku Cloud est très utilisé. Peut servir de confirmation C1 supplémentaire dans TRADEX, en complément de la BGC et Direction Belkhayate.
*Catégorie : indicateurs_tendance*

### D4519 — Last Stochastic Technique : réduction des whipsaws, signaux achat/vente plus précis
🔵 **ÉCOLE** (Source : trading_strategies.md) : Cette stratégie utilise le Stochastic Oscillator lent pour réduire les faux signaux (whipsaws) et fournir des signaux plus précis. La technique "Last" référence un point spécifique du stochastique pour améliorer le timing.
**TRADEX-AI C1** : Réduction des whipsaws = objectif principal de TRADEX (signal seulement quand 3/4 + 2/3 alignés). La logique anti-whipsaw du Stochastic "Last" peut inspirer des améliorations du filtre de confirmation dans le moteur Python.
*Catégorie : indicateurs_momentum*

### D4520 — MACD Zero-Line Crosses avec Swing Points : combinaison MACD et analyse swings
🔵 **ÉCOLE** (Source : trading_strategies.md) : Cette stratégie applique le croisement de la ligne zéro du MACD aux swing points. Le MACD zéro-line cross identifie les changements de momentum ; les swing points confirment la structure de marché. Combinaison des deux améliore la précision.
**TRADEX-AI C1** : MACD zero-line + swing points = double confirmation de momentum et structure. Pour GC/HG : le MACD peut servir d'indicateur momentum C1 en confirmation des signaux Belkhayate.
*Catégorie : indicateurs_momentum*

### D4521 — Moving Average Trading Strategies : crossovers, support/résistance, Ribbons
🟢 **FAIT VÉRIFIÉ** (Source : trading_strategies.md) : Les stratégies Moving Average couvrent : (1) croisements de moyennes mobiles ; (2) moyennes mobiles comme support et résistance ; (3) Moving Average Ribbons pour identifier direction, force et retournement de tendance. Ces 3 applications distinctes sont validées.
**TRADEX-AI C1** : Les moyennes mobiles sont fondamentales dans l'analyse Belkhayate. Le Moving Average Ribbon (multiple MAs) peut être utilisé pour quantifier la force de tendance sur GC/HG/CL/ZW — information complémentaire à la Bande Belkhayate.
*Catégorie : indicateurs_tendance*

### D4522 — Moving Momentum : 3 étapes (tendance → correction → retournement de correction)
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie Moving Momentum utilise un processus en 3 étapes : (1) identifier la tendance ; (2) attendre les corrections dans cette tendance ; (3) identifier les retournements qui signalent la fin de la correction. Entrée dans le sens de la tendance après correction validée.
**TRADEX-AI C1** : Les 3 étapes de Moving Momentum correspondent exactement à la philosophie Belkhayate : tendance établie → retrait → reprise. Pour GC/HG/CL/ZW : attendre les corrections pour entrer dans le sens de la tendance principale.
*Catégorie : gestion_risque_entree*

### D4523 — Narrow Range Day NR7 : contraction de range précède expansion
🔵 **ÉCOLE** (Source : trading_strategies.md) : Développée par Tony Crabel, la stratégie NR7 cherche les contractions de range pour prédire les expansions futures. Un jour NR7 = range le plus étroit des 7 derniers jours. Variante avancée inclut des qualificateurs Aroon et CCI.
**TRADEX-AI C1** : NR7 sur GC/HG/CL/ZW = signal de compression de volatilité précédant un breakout. Complémentaire au Bollinger Band Squeeze (D4511). À intégrer comme signal de préparation dans le moteur Python TRADEX.
*Catégorie : indicateurs_tendance*

### D4524 — RSI(2) : stratégie mean reversion Larry Connors sur RSI 2 périodes
🟢 **FAIT VÉRIFIÉ** (Source : trading_strategies.md) : La stratégie RSI(2) de Larry Connors est une stratégie de mean reversion utilisant le RSI sur 2 périodes. RSI(2) très bas = survente extrême → signal d'achat à court terme ; RSI(2) très haut = surachat extrême → signal de vente. Stratégie validée empiriquement par Connors.
**TRADEX-AI C1** : RSI(2) est un outil de timing court terme efficace pour GC/HG/CL/ZW. Peut servir de déclencheur d'entrée précis après que les conditions Belkhayate de tendance sont remplies (filtre tendance → RSI2 pour timing exact).
*Catégorie : indicateurs_momentum*

### D4525 — Six-Month Cycle MACD : Sy Harding combine cycle bull-bear 6 mois et MACD
🔵 **ÉCOLE** (Source : trading_strategies.md) : Développée par Sy Harding, cette stratégie combine le cycle saisonnier "Sell in May" (cycle bull-bear de 6 mois : novembre-avril haussier, mai-octobre baissier) avec des signaux MACD pour le timing précis d'entrée/sortie.
**TRADEX-AI C4** : Saisonnalité macro — le cycle "Sell in May" affecte aussi les commodités (GC, CL en particulier). À intégrer dans le biais saisonnier macro de TRADEX : novembre-avril → biais haussier sur métaux précieux (GC/HG).
*Catégorie : saisonnalite*

### D4526 — Percent Above 50-day SMA : breadth indicator pour définir le ton du marché
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie utilise l'indicateur de breadth "percent above 50-day MA" pour définir le ton général du marché et identifier les corrections. Quand le % est élevé → marché sain ; quand il tombe → correction ou risque accru.
**TRADEX-AI C4** : Breadth = confirmation de l'état du marché actions (ES). Pour TRADEX : si breadth marché actions faible → prudence sur les trades commodités (GC/HG/CL/ZW) car risk-off général peut tout impacter.
*Catégorie : macro_evenements*

### D4527 — Percent B Money Flow : %B + MFI pour identifier début de nouvelle tendance
🔵 **ÉCOLE** (Source : trading_strategies.md) : La stratégie Percent B Money Flow combine l'indicateur %B (position du prix dans les Bollinger Bands) et le Money Flow Index (MFI) pour identifier le début d'une nouvelle tendance quand les deux atteignent un seuil haussier ou baissier simultanément.
**TRADEX-AI C2** : Money Flow = proxy du flux de capitaux (order flow). Pour GC/HG : %B > 0.8 + MFI > 80 = pression acheteuse forte = confirmation C2. Potentielle règle de confirmation à ajouter à la KB pour les 4 actifs tradables.
*Catégorie : volume_liquidite*

### D4528 — Slope Performance Trend : indicateur slope pour quantifier tendance long terme
🔵 **ÉCOLE** (Source : trading_strategies.md) : L'indicateur Slope quantifie la tendance long terme et mesure la performance relative entre les 9 secteurs SPDRs. Le slope positif d'une courbe de performance = tendance haussière claire ; slope négatif = tendance baissière.
**TRADEX-AI C1** : La pente (slope) d'une tendance est un quantificateur objectif. Pour GC/HG/CL/ZW : mesurer le slope de la MA principale pour quantifier la force de tendance et calibrer la taille de position (tendance forte = taille maximale autorisée).
*Catégorie : indicateurs_tendance*

### D4529 — Stochastic Pop and Drop : ADX + Stochastic pour identifier breakouts de prix
🔵 **ÉCOLE** (Source : trading_strategies.md) : Développée par Jake Berstein et modifiée par David Steckler, cette stratégie combine l'ADX (Average Directional Index) et le Stochastic Oscillator pour identifier les "pops" de prix (breakouts) et les conditions de rupture. ADX identifie la force de tendance ; Stochastic identifie le momentum.
**TRADEX-AI C1** : ADX + Stochastic = combinaison tendance + momentum, identique à la logique Belkhayate (BGC pour tendance + Énergie pour momentum). La stratégie Pop and Drop peut valider la pertinence de combiner ces deux dimensions dans TRADEX.
*Catégorie : indicateurs_tendance*

### D4530 — Swing Charting : profiter des conditions de marché spécifiques par le swing trading
🔵 **ÉCOLE** (Source : trading_strategies.md) : Le Swing Charting est une vue d'ensemble du swing trading et de son utilisation pour profiter dans des conditions de marché spécifiques. Le swing trading capture les mouvements de prix à moyen terme (plusieurs jours à quelques semaines).
**TRADEX-AI C1** : Le swing trading sur les futures commodités (GC/HG/CL/ZW) est le mode opératoire naturel de TRADEX (pas du scalping, pas du buy-and-hold). Les techniques de Swing Charting sont directement applicables au timeframe visé par la méthode Belkhayate.
*Catégorie : gestion_risque_entree*

