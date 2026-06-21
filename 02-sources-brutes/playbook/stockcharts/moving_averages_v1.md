# Extraction TRADEX-AI — Moving Averages (Simple & Exponential)

> **Source brute** : `01-pipeline/bundles/stockcharts/moving_averages.md`
> (page ChartSchool « Moving Averages - Simple and Exponential »)
> **Images** : 6 fichiers tracés dans `moving_averages_manifest.txt`
> **Agent 2** : analyse native (aucun appel API externe — Phase 1)

### Légende des TAGS anti-hallucination
- 🟢 **FAIT VÉRIFIÉ** — visible dans le texte/image officiel du bundle
- 🟡 **CONVENTION** — règle d'analyse technique classique
- 🔵 **ÉCOLE** — méthodologie propre à StockCharts
- ⏳ **VOLATILE** — chiffre/réglage susceptible de changer
- 🔴 **NON VÉRIFIÉ** — à confirmer

### Étiquetage `categorie` (champ réel de la KB)
Chaque décision porte une `categorie` issue **exactement** de la liste officielle de
`04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json` :
`saisonnalite · correlations · timing · indicateurs_tendance · indicateurs_momentum ·
gestion_risque_entree · gestion_position_active · structure_marche · macro_evenements ·
volume_liquidite · psychologie`.
*(Décision S18 : aucune notion de « couche » — non implémentée dans la KB.)*

---

### D1 — Moyenne mobile : nature et rôle
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : une moyenne mobile est la moyenne de points de données (généralement le prix) sur une période donnée. Elle **lisse** le prix et **suit la tendance** (« trend-following »). Elle **ne prédit pas** la direction : elle **définit la direction actuelle**, et **retarde** (« lag ») car basée sur les prix passés.
**TRADEX-AI [categorie: indicateurs_tendance]** : utiliser la MA comme filtre de direction de fond sur NQ/ES/Gold, jamais comme prédicteur ; tout signal doit tenir compte du retard structurel.

### D2 — SMA vs EMA : pondération et réactivité
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md / image_01 / image_02) : la **SMA** moyenne également tous les prix de la période ; l'**EMA** donne plus de poids aux prix récents, **retarde moins** et **tourne avant** la SMA. `image_01` montre SMA et EMA 10 jours superposées sur INTC ; `image_02` montre que la EMA 50 j (verte) sur XLK a chuté plus tôt et est repartie à la hausse bien avant la SMA 50 j (rouge).
**TRADEX-AI [categorie: indicateurs_tendance]** : pour un déclencheur réactif sur Gold/NQ, préférer l'EMA ; pour cartographier des zones de support/résistance stables, préférer la SMA (voir D14).

### D3 — Facteur de retard (lag) selon longueur et type
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : plus la moyenne est longue, plus le retard est grand. Une MA 10 j « colle » au prix (comme un hors-bord) ; une MA 100 j est lente à changer (comme un pétrolier). Une EMA retarde moins qu'une SMA de même longueur.
**TRADEX-AI [categorie: indicateurs_tendance]** : choisir la longueur selon l'horizon de trade (scalping vs swing) ; documenter le compromis réactivité/faux signaux par actif.

### D4 — Calcul de la SMA
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : SMA = somme des clôtures sur N périodes ÷ N. Exemple texte d'une SMA 5 j sur les clôtures 11,12,13,14,15,16,17 → jour 1 = (11+12+13+14+15)/5 = **13**, jour 2 = **14**, jour 3 = **15**. À chaque pas, la donnée la plus ancienne est retirée et la nouvelle ajoutée.
**TRADEX-AI [categorie: indicateurs_tendance]** : implémenter le calcul SMA sur clôtures par défaut, source de vérité = barres NT8.

### D5 — Calcul de l'EMA et multiplicateur
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : EMA en 3 étapes — (1) SMA initiale comme amorce, (2) multiplicateur = `2 / (périodes + 1)`, (3) `EMA = (Close − EMA_veille) × multiplicateur + EMA_veille`. Une EMA 10 périodes pondère le dernier prix à **18,18 %** ; une EMA 20 périodes à **9,52 %**. La pondération est divisée par deux quand la période double.
**TRADEX-AI [categorie: indicateurs_tendance]** : amorcer l'EMA par une SMA et conserver l'historique ; le multiplicateur est déterministe (pas de réglage caché).

### D6 — Profondeur de données et précision de l'EMA
🔵 **ÉCOLE** (Source : moving_averages.md / image non téléchargée : tableur, `alt` vide) : l'EMA dépend de toutes les valeurs antérieures ; plus on remonte loin, plus elle est précise. StockCharts calcule sur **au moins 250 périodes** (souvent davantage), pour une précision « à la fraction de centime près ». Un exemple sur 30 périodes seulement est jugé peu précis.
**TRADEX-AI [categorie: indicateurs_tendance]** : exiger un historique suffisant (≥250 barres) avant de fier l'EMA pour un signal Auto.

### D7 — Longueurs et horizons usuels
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : court terme **5-20** périodes, moyen terme **20-60**, long terme **100+**. La **200 j** est la plus populaire (long terme), la **50 j** populaire pour le moyen terme ; beaucoup combinent **50 j + 200 j**.
🟡 **CONVENTION** : le couple 50/200 est un standard AT répandu.
**TRADEX-AI [categorie: indicateurs_tendance]** : proposer un jeu par défaut par horizon et par actif, paramétrable, sans verrouiller une longueur unique.

### D8 — Donnée de base (pas seulement le prix)
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md / image_03) : les MA s'appliquent par défaut à la **clôture**, mais aussi à open/high/low, au **volume**, ou à d'autres indicateurs. `image_03` montre une SMA 50 j sur le volume et une EMA 20 j sur le RSI (XLY).
**TRADEX-AI [categorie: indicateurs_tendance]** : autoriser une MA sur volume/indicateur (ex. lisser le RSI) comme couche de confluence, pas comme signal isolé.

### D9 — Identifier la tendance par la direction de la MA
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md) : une MA qui **monte** = prix globalement en hausse (tendance haussière) ; qui **descend** = tendance baissière. Les MA sont « très efficaces » en tendance forte. Exemple texte : la EMA 150 j a mis un repli de **15 %** pour inverser sa direction (retard assumé des indicateurs).
**TRADEX-AI [categorie: indicateurs_tendance]** : utiliser la pente de la MA long terme comme état de tendance de fond ; ne pas attendre d'elle un timing précis de retournement.

### D10 — Croisements doubles : golden cross / death cross
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md / image_04) : croisement **haussier** = la MA courte passe **au-dessus** de la MA longue = **golden cross** (achat potentiel) ; croisement **baissier** = MA courte **sous** MA longue = **death cross** (vente potentielle). Méthode du « double crossover » attribuée à John Murphy. `image_04` illustre EMA 10 j vs EMA 50 j sur HD.
**TRADEX-AI [categorie: indicateurs_tendance]** : croisement de MA = déclencheur candidat, à confirmer par la grille de score (jamais signal autonome).

### D11 — Croisements : retard et whipsaws, filtres
🔵 **ÉCOLE** (Source : moving_averages.md / image_04 / image_05) : les croisements produisent des signaux **tardifs** et de nombreux **whipsaws** hors tendance forte. `image_04` (HD) montre 3 faux signaux avant un bon trade ; `image_05` (ORCL) annote explicitement un **« whipsaw »**. Filtres proposés : exiger un croisement maintenu **3 jours**, ou un écart minimal entre les deux MA.
**TRADEX-AI [categorie: indicateurs_tendance]** : intégrer un filtre anti-whipsaw (persistance et/ou écart) avant de valider un croisement en mode Auto.

### D12 — Quantifier les croisements avec le MACD
🟢 **FAIT VÉRIFIÉ** (Source : moving_averages.md / image_05) : le **MACD(10,50,1)** trace la différence entre deux EMA ; il est **positif** lors d'un golden cross et **négatif** lors d'un death cross. Le PPO fait de même en pourcentage. MACD/PPO reposent sur des EMA et **ne correspondent pas** aux SMA. `image_05` montre ORCL avec EMA 50/200 et MACD(50,200,1).
**TRADEX-AI [categorie: indicateurs_momentum]** : utiliser MACD comme mesure de confluence d'un croisement EMA, en cohérence (EMA↔EMA).

### D13 — Croisements de prix et trade dans la tendance
🔵 **ÉCOLE** (Source : moving_averages.md) : signal haussier quand le prix passe au-dessus de la MA, baissier en-dessous. Pour trader **dans le sens de la tendance** : la MA longue donne le ton, la MA courte donne le signal. Ex. prix au-dessus de la MA 200 j → ne retenir que les passages au-dessus de la MA 50 j ; les croisements baissiers sont alors lus comme simples pullbacks.
**TRADEX-AI [categorie: indicateurs_tendance]** : conditionner les déclencheurs de prix au régime de la MA long terme (filtre directionnel).

### D14 — Support et résistance dynamiques
🔵 **ÉCOLE** (Source : moving_averages.md) : les MA peuvent servir de **support** en tendance haussière et de **résistance** en tendance baissière. SMA **20 j** = support court terme (aussi base des Bollinger Bands) ; SMA **200 j** = support/résistance long terme (effet « prophétie auto-réalisatrice » car très suivie). Ne pas attendre des niveaux exacts mais des **zones**.
**TRADEX-AI [categorie: structure_marche]** : traiter les MA comme zones de S/R (tolérance), pas comme lignes exactes ; pondérer la 200 j pour son effet de masse.

### D15 — Réglages par défaut des plateformes
⏳ **VOLATILE** (Source : moving_averages.md / image_06) : sur **SharpCharts**, la SMA est à **50** périodes par défaut et l'EMA à **20** ; sur **StockChartsACP**, les deux sont à **20** par défaut. Champ de prix par défaut = **Close** ; décalage (offset) et « calculated from » paramétrables. `image_06` montre l'interface ACP (panneau « Moving Average - Simple » : Period, Offset, Calculated From) sur MSFT.
**TRADEX-AI [categorie: indicateurs_tendance]** : ne pas hériter aveuglément des défauts d'une plateforme tierce ; fixer nos propres défauts par actif/horizon.

### D16 — Scans bullish / bearish (syntaxe StockCharts)
🔵 **ÉCOLE** (Source : moving_averages.md) : scan **haussier** = SMA 150 j en hausse (`SMA(150) > SMA(150) il y a 5 j`) **et** croisement haussier EMA 5 j > EMA 35 j la veille inversée, **et** volume > SMA(200, Volume). Le scan **baissier** est le symétrique (SMA 150 j en baisse, EMA 5 j < EMA 35 j).
**TRADEX-AI [categorie: indicateurs_tendance]** : réutiliser cette logique (pente MA long terme + croisement EMA court + filtre volume) comme gabarit de précondition de signal.

### D17 — Limites et bonne pratique d'usage
🔵 **ÉCOLE** (Source : moving_averages.md) : les MA sont des indicateurs **retardés** ; efficaces en tendance, **inefficaces en range** (« trading ranges »). Ne pas espérer vendre au plus haut / acheter au plus bas. À utiliser **avec d'autres outils** (ex. MA pour la tendance + **RSI** pour surachat/survente).
**TRADEX-AI [categorie: indicateurs_tendance]** : interdire l'usage d'une MA seule pour un signal Auto ; exiger une confluence (tendance MA + oscillateur + score).

---

## Synthèse Phase 1
- **17 décisions** extraites (D1 → D17), repartant de zéro.
- **6 images** citées et reliées à leur section via le manifest (image_01 à image_06).
- **Étiquetage `categorie`** (champ réel KB) : 15 × `indicateurs_tendance`, 1 × `indicateurs_momentum` (D12), 1 × `structure_marche` (D14).
- Aucune valeur inventée : tous les chiffres (18,18 % ; 9,52 % ; 250 périodes ; 15 % ; défauts 50/20/20 ; longueurs 5-20/20-60/100+ ; scans SMA(150)/EMA(5,35)) proviennent du texte source.

---

> ⚠️ **Disclaimer** : outil **éducatif** d'aide à la décision. Ce document ne constitue **en aucun cas** un conseil financier, une recommandation d'investissement ou une incitation à trader. Le trading comporte un risque de perte en capital. Les décisions restent celles de l'utilisateur.
