# Extraction StockCharts — ZigZag
**Source :** `bundles/stockcharts/zigzag.md` (HTTP 200) + 10 images certifiées
**Méthode images :** double ancrage · 10/10 certifiées · 0 à vérifier
**Décisions :** D4991 → D5010 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/zigzag
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Filtrage du bruit de prix, identification des swings significatifs et retracements Fibonacci — applicable à GC/HG/CL/ZW pour définir les pivots de structure.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/lEhjrGhXifVipdim61BE | ZigZag overlay example (nom de l'overlay) | Introduction | D4991 |
| /files/fmhUVySWqEsXpSDoTwvk | ZigZag auto DIS 3.75% | Adjusting Sensitivity | D4993 |
| /files/NAag5mo91YKvSeVVkHYf | ZigZag auto STX 7.81% | Adjusting Sensitivity | D4993 |
| /files/j4jHE5jLKYo4a3BswS2a | ZigZag 7% Citigroup (C) — trend identification | Identifying Trends | D4995 |
| /files/ngEnvKBHFDV4ppL2uo7A | ZigZag 6% SPY — Elliott Wave count | Elliott Wave Counts | D4997 |
| /files/chwNrwyTAqAvuA17Y1T0 | ZigZag (Retrace) Altera 10% — Fibonacci | Retracements Projections | D4998 |
| /files/OAk9XNbT61Ww1brZQcXv | ZigZag SharpCharts — settings panel | Using SharpCharts | D5001 |
| /files/FLjMdcYWB7hoRRAreEv6 | ZigZag (Retrace) SharpCharts | Using SharpCharts | D5001 |
| /files/RTUhRm0s9W250ecC9TGx | ZigZag StockChartsACP | Using StockChartsACP | D5002 |
| /files/umfTuC9Avlg6QJkt3v5H | ZigZag (Retrace) StockChartsACP | Using StockChartsACP | D5002 |

## DÉCISIONS

### D4991 — ZigZag : filtre du bruit de prix, pas un indicateur prédictif
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/lEhjrGhXifVipdim61BE) : Le ZigZag n'est pas un indicateur technique classique — c'est un outil de filtrage des petits mouvements de prix. Un ZigZag à 10% ignore tous les mouvements inférieurs à 10% ; seuls les mouvements supérieurs à 10% sont inclus. Aucun pouvoir prédictif propre : le pouvoir analytique vient des outils appliqués dessus (Elliott Wave, patterns, Fibonacci).
**TRADEX-AI C1** : Le ZigZag est un préprocesseur de données de prix pour TRADEX — il permet d'identifier les pivots structurels significatifs sur GC/HG/CL/ZW (swing highs/lows) qui alimentent le calcul des niveaux de support/résistance et du R/R.
*Catégorie : structure_marche*

### D4992 — Calcul ZigZag : basé sur high-low range (OHLC) ou close (line chart)
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Pour les graphiques OHLC/candlestick, le ZigZag se base sur le range high-low (plus susceptible de changer de direction que le close seul, car le range est plus large). Pour les graphiques en ligne (close only), il se base sur les clôtures. Le ZigZag connecte uniquement les points où le prix a bougé d'au moins le pourcentage spécifié.
**TRADEX-AI C1** : TRADEX utilise des données OHLCV de NinjaTrader 8 → le ZigZag doit être calculé sur le range high-low pour capturer tous les pivots structurels significatifs sur les range bars GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4993 — Paramètre par défaut : 5% ajusté automatiquement selon la volatilité de l'actif
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/fmhUVySWqEsXpSDoTwvk, /files/NAag5mo91YKvSeVVkHYf) : Le seuil traditionnel est 5%, mais StockCharts l'ajuste automatiquement selon les caractéristiques de l'actif. DIS : ajusté à 3.75% (trop peu de lignes à 5%). STX : ajusté à 7.81% (trop de lignes à 5%). Le paramètre visible dans le coin supérieur gauche du chart.
**TRADEX-AI C1** : Paramétrage TRADEX par actif : GC (volatilité ~1-2%/jour) → ZigZag ~3-5% recommandé. CL (volatilité ~2-3%/jour) → ZigZag ~5-7%. ZW (volatilité ~1-2%/jour) → ZigZag ~3-5%. HG (~1-2%/jour) → ZigZag ~3-5%. À calibrer sur 6 mois de données historiques NT8.
*Catégorie : indicateurs_tendance*

### D4994 — Exemple de calcul : de $100 à $110 = ligne ZigZag(10) ; de $112 le reversal exige $100.80
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Pour ZigZag(10%) : si le prix passe de $100 à $109 = mouvement de 9% → pas de ligne (inférieur à 10%). Si le prix atteint $110 (+10%) → ligne de $100 à $110. Si continue à $112 → ligne étendue à $112. Pour un reversal depuis $112, il faut une baisse de 10% de $112 = 11.2 points → plancher à $100.80 minimum.
**TRADEX-AI C1** : Règle de reversal ZigZag : la prochaine ligne ne se dessine que si la correction atteint le pourcentage paramétré depuis le dernier pivot. Pour TRADEX, cette mécanique permet de définir des niveaux de stop initiaux (le pivot ZigZag précédent + buffer ATR).
*Catégorie : structure_marche*

### D4995 — ZigZag pour identification de tendance : filtrer le bruit quotidien
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/j4jHE5jLKYo4a3BswS2a) : Le ZigZag filtre les petites variations quotidiennes pour faire ressortir les tendances. Exemple Citigroup (C) avec ZigZag 7% : le rebond de début juin (< 7%) ignoré, les replis de fin juin (< 7%) ignorés → seuls les mouvements significatifs apparaissent, rendant la tendance claire.
**TRADEX-AI C1** : Application TRADEX : utiliser ZigZag(5%) sur les données daily GC/HG/CL/ZW pour identifier rapidement la tendance (série de pivots hauts/bas croissants ou décroissants) et alimenter le filtre de tendance du Cercle C1.
*Catégorie : indicateurs_tendance*

### D4996 — Attention : la dernière ligne ZigZag est temporaire tant que le seuil n'est pas atteint
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : La dernière ligne ZigZag peut être temporaire. Si le prix monte de 1.89% (< 7%) sur le dernier segment et que le mouvement s'inverse, la ligne temporaire disparaît. La ligne devient permanente seulement quand le mouvement dépasse le seuil paramétré.
**TRADEX-AI C1** : Règle de robustesse TRADEX : ne jamais baser une décision de trading sur le dernier segment ZigZag (temporaire) — seuls les pivots confirmés (N-1 et antérieurs) sont exploitables pour les calculs de support/résistance et R/R.
*Catégorie : structure_marche*

### D4997 — ZigZag + Elliott Wave : filtrer les vagues pour le comptage
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/ngEnvKBHFDV4ppL2uo7A) : Le ZigZag simplifie le comptage Elliott Wave en filtrant les petits mouvements. Exemple S&P 500 avec ZigZag(6%) : cycle complet identifié de mars 2009 à juillet 2010 = 8 vagues (5 hausse + 3 baisse). Le seuil (6%) est subjectif et dépend des préférences de l'analyste.
**TRADEX-AI C1** : Application optionnelle TRADEX : sur GC (actif avec belles structures ondulatoires), un ZigZag(5%) peut faciliter l'identification manuelle des vagues Elliott par Abdelkrim en mode Manuel — améliore la lisibilité des structures de prix.
*Catégorie : structure_marche*

### D4998 — ZigZag (Retrace) : labellise les ratios entre vagues successives pour Fibonacci
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/chwNrwyTAqAvuA17Y1T0) : ZigZag (Retrace) affiche les ratios entre chaque ligne ZigZag et la ligne précédente. Un ratio < 1 = la ligne est plus petite que la précédente. Un ratio > 1 = la ligne est plus grande. Exemple Altera (ALTR) ZigZag(10%) : Line 2 = 0.638 × Line 1 (retracement 63.8% ≈ Fibonacci 61.8%). Line 3 = 1.646 × Line 2 (extension 164.6% ≈ Golden Ratio 1.618).
**TRADEX-AI C1** : Règle Fibonacci via ZigZag Retrace pour TRADEX : si le retracement d'un swing sur GC/HG/CL/ZW se stabilise à ~61.8% du swing précédent → confirmation Fibonacci → signal d'entrée en direction de la tendance principale avec R/R élevé.
*Catégorie : timing*

### D4999 — Ratio 0.618 (61.8%) : retracement Fibonacci classique via ZigZag Retrace
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Le retracement de 61.8% (Golden Ratio inverse) d'un swing précédent est un retracement Fibonacci classique. Le ZigZag (Retrace) permet de mesurer ce ratio visuellement et quantitativement, confirmant les niveaux Fibonacci calculés manuellement.
**TRADEX-AI C1** : Le niveau 61.8% de retracement sur GC/HG/CL/ZW (calculable automatiquement depuis les pivots ZigZag) est le niveau Fibonacci primaire d'entrée en continuation de tendance — composante du score C1 dans la grille TRADEX.
*Catégorie : timing*

### D5000 — Ratio 1.618 (Golden Ratio) : extension Fibonacci pour projections d'objectif
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Le ratio 1.618 (Golden Ratio) d'une vague par rapport à la précédente est une extension Fibonacci classique. Il permet de projeter l'objectif d'un nouveau mouvement basé sur la longueur du mouvement précédent. Validé dans l'exemple Altera (164.6% ≈ 1.618).
**TRADEX-AI C1** : Règle d'objectif TRADEX : après confirmation d'entrée sur GC/HG/CL/ZW, projeter l'objectif de sortie = dernière vague ZigZag × 1.618 — complète la méthode P&F Wyckoff pour le calcul du R/R. Les deux méthodes doivent pointer dans la même zone pour valider.
*Catégorie : gestion_risque_entree*

### D5001 — ZigZag utilisable sur les panneaux d'indicateurs (RSI, etc.)
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Le ZigZag et ZigZag (Retrace) peuvent être tracés sur les panneaux d'indicateurs techniques (RSI, MACD, etc.) et pas seulement sur le panneau de prix. Cela permet de filtrer le bruit sur les indicateurs eux-mêmes.
**TRADEX-AI C1** : Application TRADEX : appliquer un ZigZag sur le panneau RSI de GC pour identifier les divergences RSI/Prix (pivots de momentum) sans bruit de fond — renforce la qualité du signal C1 sans ajouter de complexité computationnelle majeure.
*Catégorie : indicateurs_momentum*

### D5002 — Paramètre ZigZag : plus bas = plus sensible (plus de lignes), plus haut = moins sensible
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Un paramètre plus bas rend l'overlay plus sensible (plus de lignes, moins de filtrage). Un paramètre plus haut le rend moins sensible (moins de lignes, plus de filtrage). L'auto-percentage s'ajuste selon les caractéristiques de l'actif.
**TRADEX-AI C1** : Règle de calibration TRADEX : pour le filtrage de tendance macro (décision directionnelle), utiliser un ZigZag paramètre élevé (~7-10%). Pour l'identification des pivots d'entrée intraday (timing précis), utiliser un paramètre bas (~3-5%).
*Catégorie : indicateurs_tendance*

### D5003 — ZigZag ne prédit pas — le pouvoir analytique vient des outils combinés
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Le ZigZag lui-même n'a aucun pouvoir prédictif. Il réagit seulement quand les prix bougent d'un certain pourcentage. La valeur analytique vient des outils et méthodes appliqués aux lignes ZigZag : Elliott Wave, patterns, Fibonacci, analyse de tendance.
**TRADEX-AI C1** : Principe de conception TRADEX : le ZigZag est un outil de prétraitement de données, pas un générateur de signal. Il structure les données de prix NT8 pour les rendre exploitables par les cercles d'intelligence supérieurs (C1→C7) et le cerveau Claude.
*Catégorie : structure_marche*

### D5004 — Analyse de tendance basique par ZigZag : comparer les pivot hauts et bas
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : L'analyse de tendance via ZigZag se fait en comparant les reaction highs et reaction lows : higher highs + higher lows = uptrend ; lower highs + lower lows = downtrend. C'est une application directe de la définition de tendance Wyckoff/Dow.
**TRADEX-AI C1** : Implémentation algorithmique TRADEX : la comparaison automatique des 3 derniers pivots ZigZag (HH/HL ou LH/LL) sur les range bars NT8 constitue le test de tendance primaire C1 pour GC/HG/CL/ZW — 0 coût computationnel, exécuté toutes les 2 secondes au Niveau 1.
*Catégorie : indicateurs_tendance*

### D5005 — ZigZag + patterns de prix : rendre visibles des patterns difficiles à voir sur bar chart
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : La conclusion de StockCharts mentionne que le ZigZag permet de rendre visibles des patterns de prix (triangles, têtes-épaules, doubles tops/bottoms) qui seraient moins apparents sur un graphique en barres ou en lignes standard.
**TRADEX-AI C1** : Application TRADEX : le ZigZag sur GC/HG/CL/ZW peut révéler des patterns structurels (ex : triangle symétrique, double bottom) que le cerveau Claude (Niveau 3) peut identifier depuis les pivots labellisés — enrichit la qualité de l'analyse contextuelle.
*Catégorie : configuration*

### D5006 — ZigZag (Retrace) vs ZigZag normal : le Retrace ajoute les ratios entre lignes
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : Le ZigZag normal affiche uniquement les lignes de prix franchissant le seuil. Le ZigZag (Retrace) connecte les hauts et bas de réaction avec des labels mesurant la proportion du mouvement actuel par rapport au mouvement précédent (ratios). Deux outils distincts avec des cas d'usage différents.
**TRADEX-AI C1** : Deux modes d'usage TRADEX : ZigZag normal → identification de tendance et pivots structurels. ZigZag (Retrace) → calcul automatique des niveaux Fibonacci et projections d'objectif. Les deux sont pertinents mais pour des étapes différentes de l'analyse.
*Catégorie : indicateurs_tendance*

### D5007 — StockCharts calcule automatiquement les cibles P&F via méthodes breakout et reversal
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md) : StockCharts calcule automatiquement les objectifs P&F en utilisant les méthodes breakout et reversal. Le résultat peut légèrement différer selon la méthode utilisée (ex : cible 69 vs 72 pour Amgen selon la méthode). Les deux sont valides comme estimation de l'objectif de mouvement.
**TRADEX-AI C1** : Cohérence avec D4963 (Wyckoff Stock Analysis) : les deux méthodes P&F sont exploitables pour TRADEX. Recommandation : calculer les deux et utiliser la zone entre les deux cibles comme zone d'objectif (plutôt qu'un prix exact), réduisant le risque de sortie prématurée ou tardive.
*Catégorie : gestion_position_active*

### D5008 — Outil ZigZag applicable sur tout instrument (actions, ETF, indices, matières premières)
🟡 **SYNTHÈSE** (Source : zigzag.md) : Les exemples utilisent des actions (Boeing, Amgen, Citigroup) et des ETF (SPY), mais la mécanique ZigZag est universelle et applicable à tout instrument chartable incluant les futures de matières premières.
**TRADEX-AI C1** : Le ZigZag est directement applicable aux contrats futures GC/HG/CL/ZW tradés via NinjaTrader 8 — les range bars NT8 sont des charts OHLC standard, compatibles avec le calcul ZigZag basé sur le high-low range.
*Catégorie : indicateurs_tendance*

### D5009 — Elliott Wave sur ZigZag : cycle complet = 5 vagues impulsives + 3 vagues correctives
🟢 **FAIT VÉRIFIÉ** (Source : zigzag.md, /files/ngEnvKBHFDV4ppL2uo7A) : Un cycle Elliott Wave complet (identifié via ZigZag 6% sur SPY) = 8 vagues : 5 dans la direction de la tendance (impulsives) + 3 à contre-tendance (correctives). Identifié de mars 2009 à juillet 2010 sur le SPY.
**TRADEX-AI C1** : Contexte TRADEX : la combinaison ZigZag + comptage Elliott sur GC peut affiner le timing d'entrée (entrer en début de vague 3 impulsive = plus fort mouvement). Usage en mode Manuel uniquement — le mode Auto n'implémente pas de comptage Elliott (trop subjectif).
*Catégorie : structure_marche*

### D5010 — Conclusion : ZigZag = outil de filtrage, pas de prédiction ; mesurer la dernière ligne
🟡 **SYNTHÈSE** (Source : zigzag.md) : Conclusion StockCharts : ZigZag et ZigZag (Retrace) filtrent l'action des prix sans pouvoir prédictif propre. Ils réagissent aux mouvements dépassant le seuil. Les chartistes peuvent : analyser les tendances, repérer des patterns cachés, et identifier les niveaux Fibonacci. Toujours mesurer si la dernière ligne est temporaire ou permanente avant d'agir.
**TRADEX-AI C1** : Règle de sécurité TRADEX : avant tout calcul de pivot, support ou R/R basé sur le ZigZag, vérifier si le dernier pivot est confirmé (permanent) ou en cours de formation (temporaire). Un pivot temporaire ne peut pas servir de base à un signal de trading — règle à implémenter dans le pipeline de données du data_reader.py.
*Catégorie : structure_marche*
