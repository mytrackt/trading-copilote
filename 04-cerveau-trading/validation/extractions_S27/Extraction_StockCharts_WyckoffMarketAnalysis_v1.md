# Extraction StockCharts — Wyckoff Market Analysis
**Source :** `bundles/stockcharts/wyckoff_market_analysis.md` (HTTP 200) + 9 images certifiées
**Méthode images :** double ancrage · 9/9 certifiées · 0 à vérifier
**Décisions :** D4931 → D4950 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-market-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Structure de tendance (hauts/bas), tops/bottoms et positions dans le trend — applicable à GC/CL/ZW pour timing d'entrée et confirmation ES/VX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/ygqkP8vQcpNlQ7yqUlj3 | Richard D. Wyckoff (portrait) | About | D4931 |
| /files/MI0pKXoBj9FfFGeiXmjP | Wyckoff (portrait 2) | About | D4931 |
| /files/ZLkfyjOkUbrZcMAUbLKT | Wyckoff Uptrend Chart | Broad Market Trend | D4932 |
| /files/wNGJLX9mGk6o90xhKWhR | Wyckoff Downtrend Chart | Broad Market Trend | D4932 |
| /files/4jJjhJ1DwHZB0O2QH4bP | Wyckoff Chart 1 — Selling Climax | Major Tops and Bottoms | D4934 |
| /files/SqbNDh3UnDThS5QmdPFy | Wyckoff Chart 2 — Distribution Top 2007 | Major Tops and Bottoms | D4936 |
| /files/AMbrhLZXFykvTqqUXIFx | Wyckoff P&F Price Projection Top | Price Projections | D4938 |
| /files/RsUzzRB9KOetgMEIuh6Q | Wyckoff P&F Price Projection Bottom 2009 | Price Projections | D4939 |
| /files/SE31oFKoTTyaryabsIT0 | Wyckoff Position in Trend — Accumulation/Markup | Position in Trend | D4941 |

## DÉCISIONS

### D4931 — Règle 1 Wyckoff : le marché ne se répète jamais exactement
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Wyckoff règle fondamentale — le marché est un artiste, pas un ordinateur. Il a un répertoire de comportements de base qu'il modifie subtilement. Aucun pattern identique ne se reproduit à l'identique.
**TRADEX-AI C1** : Le moteur TRADEX ne doit jamais s'appuyer sur une reproduction exacte d'un pattern passé sur GC/HG/CL/ZW — chaque signal requiert réévaluation en contexte actuel.
*Catégorie : structure_marche*

### D4932 — Règle 2 Wyckoff : le comportement actuel n'a de sens que par comparaison au passé
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Tout ce que fait le marché aujourd'hui doit être comparé à ce qu'il a fait avant — hier, la semaine dernière, le mois dernier. Pas de niveaux prédéfinis ne faillant jamais.
**TRADEX-AI C1** : La grille de score TRADEX doit intégrer une comparaison relative (tendance récente GC vs tendance historique) et non des seuils absolus fixes.
*Catégorie : structure_marche*

### D4933 — Définition de la tendance : hausse/baisse/range via pics et creux
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/ZLkfyjOkUbrZcMAUbLKT, /files/wNGJLX9mGk6o90xhKWhR) : Uptrend = série de pics et creux croissants. Downtrend = série de pics et creux décroissants. Trading range = pics et creux égaux → attendre la cassure pour déterminer la direction.
**TRADEX-AI C1** : Condition préalable obligatoire pour tout signal TRADEX sur GC/HG/CL/ZW : identifier le régime de tendance (up/down/range) sur le timeframe de référence avant d'évaluer les 7 cercles.
*Catégorie : structure_marche*

### D4934 — Position dans la tendance : suracheté vs survendu dicte le ratio R/R
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : En uptrend, acheter en zone de survente (repli/correction) offre le meilleur ratio R/R. Acheter en surachat dans un uptrend dégrade le R/R. En downtrend, shorter en surachat est préférable. Shorter en survente dans un downtrend est risqué.
**TRADEX-AI C1** : La règle R/R ≥ 1:2 du CLAUDE.md est directement soutenue par Wyckoff : ne jamais initier un trade GC/HG/CL/ZW quand l'actif est en zone extrême par rapport à la tendance dominante.
*Catégorie : gestion_risque_entree*

### D4935 — Bottom Wyckoff : selling climax + spring sur volume élevé
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/4jJjhJ1DwHZB0O2QH4bP) : Les marchés baissiers se terminent souvent par un selling climax ou un spring (cassure de support avortée). Cassure d'un support clé sur forte vente → renversement brutal par le "smart money" → clôture bien au-dessus des bas. Le volume élevé valide la validité du renversement.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, un spring (cassure de support + reprise rapide) avec expansion de volume ATAS (footprint, delta) constitue un signal d'entrée long fort — à intégrer dans la grille C2.
*Catégorie : configuration*

### D4936 — Top Wyckoff : distribution prolongée → cassure support sur volume croissant
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/SqbNDh3UnDThS5QmdPFy) : Les tops de marché = longues périodes de consolidation latérale (distribution). Pattern : 1) breakout raté au-dessus du pic précédent, 2) retour au support, 3) rebond + pic inférieur (demande diminuée), 4) cassure finale du support sur volume croissant. Volume en baisse sur les jours de hausse et en hausse sur les jours de baisse valide la distribution.
**TRADEX-AI C2/C3** : Reconnaître un pattern de distribution sur ES (C3 institutionnels) comme signal macro de risque pour les trades longs sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D4937 — Les tops durent plus longtemps que les bottoms
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Les tops de marché sont des affaires longues et étalées (consolidation de distribution). Les bottoms sont relativement courts et violents. Cette asymétrie est une caractéristique répétable des marchés selon Wyckoff.
**TRADEX-AI C5** : Sur ES/VX, un top qui s'étire dans le temps avec volume déclinant sur les hausses est un signal de vigilance accru — renforcer la pondération du VIX dans la grille de score lors de telles configurations.
*Catégorie : structure_marche*

### D4938 — Projections de prix via comptage horizontal P&F (largeur du pattern)
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/AMbrhLZXFykvTqqUXIFx) : Wyckoff utilise le comptage horizontal P&F pour projeter l'amplitude d'un mouvement. Plus le pattern est large (nombre de colonnes), plus l'objectif est élevé. Formule : colonnes × taille de reversal × valeur de boîte. Exemple S&P 500 top 2007 : 34 colonnes × 3 × 10 = 1020 points de déclin projeté.
**TRADEX-AI C1** : Méthode de projection applicable sur GC/HG/CL/ZW via P&F pour estimer les objectifs de prix après cassure d'un range ou pattern de distribution/accumulation — composante du calcul R/R.
*Catégorie : gestion_risque_entree*

### D4939 — Projections à prendre comme guidelines, non comme cibles absolues
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/RsUzzRB9KOetgMEIuh6Q) : Wyckoff lui-même mettait en garde contre une prise trop sérieuse des projections P&F. Certains comptages n'atteignent pas leur cible, d'autres les dépassent. La situation technique peut changer avant que la cible soit atteinte.
**TRADEX-AI C1** : Les objectifs de prix calculés pour GC/HG/CL/ZW doivent être réévalués dynamiquement au fil du mouvement — le moteur TRADEX ne doit pas bloquer la sortie si la cible n'est pas atteinte.
*Catégorie : gestion_position_active*

### D4940 — Phase accumulation → markup : 5 points d'achat potentiels
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md, /files/SE31oFKoTTyaryabsIT0) : Dans un uptrend, Wyckoff identifie 5 points d'achat : 1) Spring/selling climax (risque élevé), 2) Cassure de résistance sur volume, 3) Throwback sur ancienne résistance devenue support, 4) Correction dans le markup (re-accumulation), 5) Pullback à 50% du dernier up-leg.
**TRADEX-AI C1** : La règle d'entrée TRADEX "3/4 trading + 2/3 confirmation alignés" doit être croisée avec la position dans la structure Wyckoff — les entrées en points 2 et 3 offrent le meilleur équilibre risque/rendement sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D4941 — Phase distribution → markdown : 5 points de vente potentiels
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Dans un downtrend, Wyckoff identifie 5 points de vente/short : 1) Pic inférieur dans la distribution (risque élevé), 2) Cassure du support sur volume, 3) Throwback sur ancienne résistance, 4) Re-distribution (consolidation dans le markdown), 5) Rebond oversold à 50% du dernier down-leg.
**TRADEX-AI C1** : Sur CL (Pétrole), en tendance baissière, attendre le throwback (point 3) après la cassure de support pour maximiser le R/R sur les signaux VENDRE — les entrées agressives (point 1) sont interdites en mode Auto.
*Catégorie : gestion_risque_entree*

### D4942 — Re-accumulation et re-distribution : consolidations dans la tendance
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Dans un uptrend établi, les consolidations plates = phases de re-accumulation. Cassure au-dessus de la résistance de consolidation = continuation du markup. Dans un downtrend, les consolidations plates = re-distribution. Cassure sous le support = continuation du markdown.
**TRADEX-AI C1** : Reconnaître une re-accumulation sur GC/ZW (consolidation après hausse) comme signal de continuation — ne pas confondre avec un top. Utiliser le volume et la relation avec DX (C4) pour discriminer.
*Catégorie : structure_marche*

### D4943 — Correction à 50% comme niveau de support/résistance clé dans une tendance
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Wyckoff cherchait des signes de support ou de renversement quand la correction retraitait 50% du dernier mouvement haussier (ou baissier). Le retracement de 50% est le niveau de survente/surachat dans la tendance.
**TRADEX-AI C1** : Le niveau 50% de retracement est un filtre d'entrée valide pour GC/HG/CL/ZW — un signal généré exactement sur ce niveau a un R/R supérieur. Intégrer dans le calcul du score TRADEX comme bonus de timing.
*Catégorie : timing*

### D4944 — Volume valide les mouvements : cassures sur fort volume = fiables
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Wyckoff utilisait le volume pour confirmer la validité d'un renversement, d'une cassure ou d'une tendance. Un volume élevé montre une participation croissante (institutions). Un volume faible sur une cassure augmente les chances d'échec.
**TRADEX-AI C2** : Règle obligatoire TRADEX : tout signal sur GC/HG/CL/ZW nécessite confirmation volume via ATAS (Cercle C2). Un signal généré sans expansion de volume reçoit un score C2 = 0/1 dans la grille.
*Catégorie : volume_liquidite*

### D4945 — Smart money vs dumb money : la distribution précède les krachs
🔵 **ÉCOLE** (Source : wyckoff_market_analysis.md) : Les institutions (smart money) vendent leurs positions aux particuliers (dumb money) pendant la phase de distribution, juste avant que le marché s'effondre. Le top n'est souvent pas clair avant que la deuxième moitié du pattern se déploie.
**TRADEX-AI C3** : Le monitoring COT (C3 institutionnels) dans TRADEX est directement justifié par cette observation Wyckoff — les positions nettes des commerciaux sur GC/ZW signalent la fin de distribution avant la cassure.
*Catégorie : macro_evenements*

### D4946 — Les grandes tendances commencent par une accumulation, pas un signal immédiat
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Une tendance haussière débute par une phase d'accumulation (smart money achète en silence), puis passe en markup. Les joueurs agressifs entrent sur le spring/selling climax ; les trend-followers entrent sur la cassure de résistance.
**TRADEX-AI C1** : Le système TRADEX en mode Manuel permet à Abdelkrim de se positionner tôt (spring) avec risque élevé, ou d'attendre la cassure validée (signal sûr) — les deux sont légitimes selon Wyckoff.
*Catégorie : gestion_risque_entree*

### D4947 — Composite index (wave chart) : utiliser un indice agrégé pour la tendance macro
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Wyckoff utilisait un "wave chart" (moyenne composite de 5+ actions) pour analyser la tendance de marché globale. Aujourd'hui : S&P 500, Nasdaq, Russell 2000 sont les équivalents modernes.
**TRADEX-AI C4/C7** : ES (S&P 500) joue le rôle du wave chart Wyckoff dans TRADEX — sa tendance détermine le biais directionnel macro pour GC/HG/CL/ZW (Cercle C4 Macro + C7 Corrélations).
*Catégorie : correlations*

### D4948 — Les bars prix quotidiens (high/low/close) suffisent pour la tendance medium-term
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Wyckoff utilisait les prix journaliers (high, low, close) pour construire ses graphiques en barres et analyser la tendance medium-term. Les timeframes courts sont inutiles pour l'identification de la tendance directionnelle.
**TRADEX-AI C1** : Les données NT8 daily (OHLCV) sur GC/HG/CL/ZW sont suffisantes pour le filtre de tendance Wyckoff — le moteur n'a pas besoin d'analyse intraday pour valider le régime macro.
*Catégorie : structure_marche*

### D4949 — Conclusion : 4 éléments clés de la méthode Wyckoff marché
🟡 **SYNTHÈSE** (Source : wyckoff_market_analysis.md) : Les 4 piliers de l'analyse Wyckoff macro : 1) Identification de tendance, 2) Patterns de renversement (tops/bottoms), 3) Projections de prix (P&F), 4) Position dans la tendance (overbought/oversold). Le jugement final reste humain.
**TRADEX-AI C1** : Ces 4 piliers correspondent directement aux 4 dimensions de la grille de score TRADEX pour le Cercle C1 — chaque dimension doit être évaluée avant émission d'un signal sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4950 — Indices disponibles comme proxies wave chart Wyckoff
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_market_analysis.md) : Les indices modernes utilisables comme wave chart : S&P 500, S&P 100, Nasdaq, NYSE Composite, Russell 2000. Chacun reflète un univers légèrement différent du marché boursier américain.
**TRADEX-AI C4** : ES (S&P 500 futures) est le proxy primaire TRADEX pour le wave chart Wyckoff. VX (VIX) complète l'analyse de sentiment de l'indice composite — les deux sont dans la catégorie CONFIRMATION du CLAUDE.md.
*Catégorie : macro_evenements*
