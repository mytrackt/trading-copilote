# Extraction NinjaTrader — How to Read a Futures Trading Chart
**Source :** `bundles/ninjatrader/how_to_read_a_futures_trading_chart.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7771 → D7790 · **Page :** https://ninjatrader.com/futures/blogs/how-to-read-a-futures-trading-chart/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Fondamentaux de lecture de chart futures — bases structurelles pour l'interprétation des données NT8 en Cercle C1.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7771 — Un chart futures = représentation visuelle du comportement de marché en temps réel
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Un chart de trading futures est une représentation visuelle de l'action des prix dans le temps. Il affiche les données de marché (prix, volume, intervalles de temps) pour observer les tendances, identifier les patterns et décider des points d'entrée/sortie. Objectif : simplifier les données de prix complexes pour extraire des insights actionnables.
**TRADEX-AI C1** : TRADEX-AI lit les données NT8 en JSON (non screenshot) — le chart est la représentation visuelle des mêmes données structurées que le moteur Python traite en temps réel.
*Catégorie : structure_marche*

### D7772 — Line chart : connecte les clôtures — idéal pour identifier rapidement la tendance générale
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Le line chart est le type le plus simple — il relie les prix de clôture sur une période avec une ligne continue. Idéal pour une identification rapide de la tendance générale, sans le détail intra-barre.
**TRADEX-AI C1** : Utilité limitée pour TRADEX-AI (insuffisant pour Belkhayate) — mais utile pour visualiser rapidement la tendance macro des actifs de confirmation (DX/ES/VX).
*Catégorie : indicateurs_tendance*

### D7773 — Bar chart : affiche OHLC — plus de détail qu'un line chart
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Le bar chart affiche ouverture, haut, bas et clôture (OHLC) pour chaque intervalle de temps. Fournit plus de détail qu'un line chart en montrant la plage complète de prix de chaque période.
**TRADEX-AI C1** : OHLC = données fondamentales lues par NT8 pour GC/HG/CL/ZW — chaque barre JSON contient ces 4 valeurs pour le moteur Python.
*Catégorie : structure_marche*

### D7774 — Candlestick chart : affiche OHLC de façon intuitive — type le plus utilisé par les traders futures
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_a_futures_trading_chart.md) : Le candlestick est le type de chart le plus populaire parmi les traders futures. Comme le bar chart, il affiche les données OHLC mais de façon intuitive (corps + mèches) facilitant l'identification des tendances et patterns.
**TRADEX-AI C1** : NT8 génère des données candlestick — les patterns de bougies (patterns Belkhayate inclus) sont analysables depuis les données JSON OHLC.
*Catégorie : structure_marche*

### D7775 — Volume chart : volume tracé avec le prix pour mesurer la force d'un mouvement
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_a_futures_trading_chart.md) : Le volume chart trace le volume de trading en parallèle de l'action des prix, permettant aux traders d'évaluer la force derrière un mouvement de prix. Un mouvement accompagné de volume fort est plus fiable qu'un mouvement en faible volume.
**TRADEX-AI C2** : Données volume NT8/ATAS (Cercle C2) — obligatoires pour valider la conviction des signaux Belkhayate C1.
*Catégorie : volume_liquidite*

### D7776 — Axe vertical (prix) à droite, axe horizontal (temps) en bas — structure universelle
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Structure standard d'un chart futures : axe de prix sur le côté droit (niveaux de prix actuels), axe de temps en bas (intervalles sélectionnés — 5 min, horaire, journalier). Cette structure est universelle sur toutes les plateformes.
**TRADEX-AI C1** : Structure de référence pour l'interface dashboard TRADEX-AI (maquettes F1-F8 dans 05-saas/maquettes/) — l'axe de prix droit correspond au format standard NT8.
*Catégorie : structure_marche*

### D7777 — Chaque barre/bougie représente une période : Open (début), High/Low (extrêmes), Close (fin)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_a_futures_trading_chart.md) : Chaque barre ou bougie représente une seule période selon le timeframe sélectionné. Les 4 valeurs : Open = prix de début de période, High = prix maximum, Low = prix minimum, Close = prix de fin de période.
**TRADEX-AI C1** : Données OHLC = structure de base de chaque message JSON NT8 — le moteur Python lit ces 4 valeurs pour calculer les indicateurs Belkhayate (BGC, Direction, Énergie, Pivots).
*Catégorie : structure_marche*

### D7778 — Moving Average : lisse l'action des prix et identifie la tendance
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : La moyenne mobile est un indicateur technique commun qui lisse l'action des prix pour aider à identifier la direction de la tendance. Réduit le bruit à court terme pour mettre en évidence la direction globale.
**TRADEX-AI C1** : Belkhayate utilise ses propres indicateurs (BGC, COG) en lieu et place des MAs classiques — mais le principe de lissage est identique.
*Catégorie : indicateurs_tendance*

### D7779 — RSI : mesure le momentum et les conditions de surachat/survente
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Le RSI (Relative Strength Index) mesure le momentum des prix et identifie les conditions de surachat (généralement au-dessus de 70) ou de survente (généralement en-dessous de 30). Indicateur d'oscillateur borné entre 0 et 100.
**TRADEX-AI C1** : L'Énergie Belkhayate (stub en attente de validation Trading Geek) joue un rôle similaire au RSI comme oscillateur de momentum — non codée mais conceptuellement alignée.
*Catégorie : indicateurs_momentum*

### D7780 — Volume indicator : montre l'intérêt pour un mouvement de prix spécifique
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : L'indicateur de volume montre l'intérêt du marché pour un mouvement de prix particulier. Un mouvement de prix avec volume élevé indique une forte participation ; avec faible volume, il peut manquer de conviction.
**TRADEX-AI C2** : Règle TRADEX : volume indicator (Cercle C2) = critère de confirmation obligatoire avant validation d'un signal Belkhayate C1.
*Catégorie : volume_liquidite*

### D7781 — Tendance haussière / baissière / range : 3 états fondamentaux du marché
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_a_futures_trading_chart.md) : Reconnaître la tendance est l'usage le plus fondamental d'un chart. 3 états : (1) Uptrend = direction générale haussière (hauts et bas de plus en plus élevés), (2) Downtrend = direction baissière (hauts et bas de plus en plus bas), (3) Consolidation/Range = mouvement latéral sans direction claire.
**TRADEX-AI C1** : Direction Belkhayate (Cercle C1) identifie ces 3 états — base du filtre de tendance pour les 4 actifs tradables GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D7782 — Patterns chartistes (triangles, tête-épaules, double tops/bottoms) = signaux de continuation ou retournement
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Les patterns chartistes comme les triangles, la formation tête-épaules, et les doubles tops/bottoms signalent des points potentiels de continuation ou de retournement. Ils ne garantissent pas un résultat mais aident à évaluer les probabilités et définir des niveaux d'entrée/sortie stratégiques.
**TRADEX-AI C1** : BGC Belkhayate (Cercle C1) — les patterns chartistes classiques sont des confirmations secondaires ; la méthode Belkhayate prime sur les patterns visuels standards.
*Catégorie : configuration*

### D7783 — Timeframe court (1-15 min) = décisions rapides pour day traders
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Les traders court terme préfèrent des charts 1 à 15 minutes pour des décisions rapides. Plus de "bruit" dans les données mais plus de réactivité aux mouvements intraday.
**TRADEX-AI C1** : NT8 utilise des range bars (non time-based) pour TRADEX-AI — décision verrouillée. Les range bars filtrent le bruit temporel mieux que les timeframes fixes en minutes.
*Catégorie : timing*

### D7784 — Timeframe horaire/journalier = swing traders (plusieurs jours de tenue)
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Les swing traders utilisent des charts horaires ou journaliers pour suivre les mouvements de prix sur plusieurs jours. Moins de bruit, décisions moins fréquentes mais avec tenue de position plus longue.
**TRADEX-AI C1** : Les actifs de confirmation DX/ES/VX sont analysés sur timeframes plus longs pour le contexte macro (Cercle C4) — complément à la granularité range bars des actifs tradables.
*Catégorie : timing*

### D7785 — Multi-timeframe analysis : combiner plusieurs unités de temps pour une image complète
🟡 **SYNTHÈSE** (Source : how_to_read_a_futures_trading_chart.md) : Il est courant pour les traders de référencer plusieurs unités de temps pour obtenir une image plus complète du marché. Le timeframe plus long donne le contexte de tendance ; le timeframe plus court affine l'entrée.
**TRADEX-AI C1** : Approche Belkhayate multi-timeframe : tendance sur daily/weekly (direction macro) + entrée sur range bars NT8 (timing précis) — alignement obligatoire pour signal valide.
*Catégorie : timing*

### D7786 — Lire un chart = comprendre le contexte marché, pas prédire le futur
🟡 **SYNTHÈSE** (Source : how_to_read_a_futures_trading_chart.md) : La lecture d'un chart ne consiste pas à prédire le marché — il s'agit de lire ce que le chart dit en temps réel. Comprendre le contexte de marché, repérer les setups et gérer le risque est l'objectif.
**TRADEX-AI C1** : Philosophie alignée avec Belkhayate — le signal TRADEX-AI est une lecture probabiliste du contexte actuel, pas une prédiction. Mode Manuel = Abdelkrim décide toujours.
*Catégorie : psychologie*

### D7787 — Personnalisation du chart : timeframes, indicateurs, styles — adapter à son propre style
🔵 **ÉCOLE** (Source : how_to_read_a_futures_trading_chart.md) : Les charts futures sont hautement personnalisables — timeframes, indicateurs, styles visuels. L'objectif reste constant : simplifier les données complexes et extraire des insights actionnables adaptés à son style de trading.
**TRADEX-AI C1** : Configuration NT8 pour TRADEX-AI : range bars + indicateurs Belkhayate (BGC, COG, Direction, Énergie stub, Pivots) — configuration verrouillée dans settings.py.
*Catégorie : configuration*
