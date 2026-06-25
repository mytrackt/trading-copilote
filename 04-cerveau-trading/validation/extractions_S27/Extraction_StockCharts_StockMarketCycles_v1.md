# Extraction StockCharts — Stock Market Cycles
**Source :** `bundles/stockcharts/stock_market_cycles.md` (HTTP 200) + 8 images certifiées
**Méthode images :** double ancrage · 8/8 certifiées · 0 à vérifier
**Décisions :** D3931 → D3950 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/stock-market-cycles
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : théorie des cycles de marché applicable à ES/GC/CL pour anticiper les points de retournement et aligner timing avec cycles saisonniers (C1 + C4 + saisonnalite).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | A hypothetically perfect market cycle | The Perfect Market Cycle | D3932 |
| image_02 | An example of an arithmetic scale chart | Steps to Find Cycles (Log Scale) | D3936 |
| image_03 | The same chart as the one above but in a log scale | Steps to Find Cycles (Log Scale) | D3936 |
| image_04 | A five-day moving average is overlaid on the price chart to smooth the price series | Steps to Find Cycles (SMA 5j) | D3937 |
| image_05 | Chart of S&P 500 with the DPO and Cycle Lines tool | Steps to Find Cycles (DPO) | D3938 |
| image_06 | Example of the Presidential Cycle applied to the S&P 500 from 1981 to 2009 | Examples of Market Cycles | D3940 |
| image_07 | The six-month cycle applied to the S&P 500 | Examples of Market Cycles | D3941 |
| image_08 | Example of a chart annotated with Cycle Lines | Using Cycles With SharpCharts | D3948 |

## DÉCISIONS

### D3931 — Définition du cycle de marché
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Un cycle de marché est un événement (tel qu'un haut ou bas de prix) qui se répète régulièrement. Les cycles existent dans l'économie, dans la nature et sur les marchés financiers. Le cycle économique de base comprend : déclin économique, creux, reprise économique, sommet.
**TRADEX-AI C4** : Intégrer la phase du cycle économique (expansion/contraction) comme facteur macro dans le score /10 — pertinent pour GC (valeur refuge en récession) et CL (demande cyclique).
*Catégorie : saisonnalite*

### D3932 — Vocabulaire du cycle parfait : définitions des composantes
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_01) : Vocabulaire normalisé : Crest (haut du cycle), Trough (bas du cycle), Phase (position du cycle à un moment donné), Inflection Point (croisement de la ligne X), Amplitude (hauteur de la X-axis au pic ou creux), Length (distance entre deux hauts ou deux bas de cycles consécutifs). Exemple : cycle parfait de 100 jours, pic à 25j et 125j, creux à 75j et 175j.
**TRADEX-AI C1** : Vocabulaire à utiliser dans les prompts KB pour décrire les cycles temporels sur GC/ES — facilitera la cohérence de la KB Belkhayate avec la théorie des cycles.
*Catégorie : timing*

### D3933 — Lows utilisés pour définir la longueur du cycle
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : La longueur d'un cycle est définie et projetée dans le futur à partir des bas (Troughs), pas des hauts. Un haut de cycle peut être anticipé quelque part entre les bas de cycles.
**TRADEX-AI C1** : Sur GC/CL/ZW, mesurer les cycles depuis les creux — aligne avec la méthode Belkhayate (recherche des Troughs pour estimer le prochain creux et le prochain sommet).
*Catégorie : timing*

### D3934 — Translation : les cycles ne piquent pas exactement au milieu
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Translation : les cycles atteignent rarement leur pic exactement au milieu. Right translation = tendance des prix à piquer dans la seconde moitié du cycle lors des bull markets. Left translation = tendance des prix à piquer dans la première moitié du cycle lors des bear markets. Les prix tendent à piquer plus tard dans les bull markets et plus tôt dans les bear markets.
**TRADEX-AI C1** : Sur GC/ES, right translation = bull market confirmé ; left translation = bear market — indicateur de phase de marché pour le score /10.
*Catégorie : timing*

### D3935 — Harmoniques : décomposition des grands cycles en petits cycles égaux
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Les grands cycles peuvent être décomposés en cycles plus petits et égaux : un cycle 40 semaines → deux cycles de 20 semaines → deux cycles de 10 semaines chacun. L'inverse est aussi vrai : les petits cycles peuvent se multiplier en grands cycles. Un cycle de 10 semaines peut faire partie d'un cycle de 20 semaines et d'un cycle encore plus grand de 40 semaines.
**TRADEX-AI C7** : Sur GC/ES, identifier les alignements harmoniques 10w/20w/40w pour détecter les confluences cycliques majeures — renforcent la validité d'un signal TRADEX.
*Catégorie : timing*

### D3936 — Étape 1 : utiliser l'échelle logarithmique pour l'analyse des cycles
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_02, image_03) : Pour l'analyse des cycles, utiliser l'échelle logarithmique (log scale) pour voir les variations de prix en termes percentuels plutôt qu'absolus. Sur une échelle arithmétique, une avance de 100 à 200 semble identique à une avance de 300 à 400. Sur log scale, la hausse de 100% (+100 à 200) apparaît 3 fois plus grande que la hausse de 33% (+300 à 400). Indispensable pour comparer l'action des prix sur des périodes étendues avec de grands changements de prix.
**TRADEX-AI C1** : Sur GC/CL (grands mouvements en valeur absolue), utiliser log scale pour l'analyse cyclique — évite de biaiser les cycles sur les grands mouvements de prix.
*Catégorie : timing*

### D3937 — Étape 2 : lisser la série de prix avec SMA courte
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_04) : Lisser la série de prix avec une SMA simple courte (5 jours est souvent suffisant) pour éliminer le bruit aléatoire et se concentrer sur les mouvements généraux. Le lissage aide aussi à définir les creux de réaction quand la volatilité est élevée (ex : oct-nov 2008).
**TRADEX-AI C1** : Sur GC/CL/ZW, SMA 5j pour identifier les creux cycliques avec moins de bruit — applicable dans le moteur Python pour la détection cyclique.
*Catégorie : timing*

### D3938 — Étape 3/4 : identifier les cycles visuellement puis détrendre avec DPO
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_05) : Méthode en 2 temps : (1) analyser visuellement les graphiques pour trouver des creux avec la même longueur de cycle et projeter ce cycle dans le futur ; (2) utiliser le Detrended Price Oscillator (DPO) pour détrender la série. Le DPO est basé sur une moyenne mobile déplacée vers la gauche de N/2+1 périodes. Exemple : DPO 20j = clôture - SMA 20j déplacée de 11j vers la gauche (passé).
**TRADEX-AI C1** : Sur GC/ES, DPO = outil de confirmation cyclique — les plongées du DPO en négatif confirment les creux cycliques récurrents.
*Catégorie : timing*

### D3939 — Cycle S&P 500 : cycle de 65 jours illustré par DPO
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_05) : Une analyse visuelle du S&P 500 ($SPX) suggère un cycle de 3 mois. Le DPO est réglé à 65 jours pour confirmer le cycle anticipé. Le DPO devient négatif tous les quelques mois, confirmant un cycle récurrent. Les lignes de cycle sont ensuite appliquées pour répartir uniformément les cycles et projeter dans le futur.
**TRADEX-AI C5** : Sur ES (confirmation TRADEX), surveiller les creux DPO(65) tous les ~3 mois pour anticiper les retournements de sentiment favorables à GC.
*Catégorie : timing*

### D3940 — Cycle présidentiel américain 4 ans : deuxième moitié plus haussière
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_06) : Le cycle présidentiel (basé sur le mandat de 4 ans du président américain) a produit de bons résultats sur les 50 dernières années. Le S&P 500 monte généralement, mais davantage pendant la deuxième moitié du mandat que la première.
**TRADEX-AI C4** : Facteur macro à intégrer : deuxième moitié du mandat présidentiel US = contexte macro plus favorable pour ES — influence indirecte sur GC (corrélation inverse partielle ES/GC).
*Catégorie : macro_evenements*

### D3941 — Cycle des 6 mois (Six-Month Cycle) de Yale Hirsch
🔵 **ÉCOLE** (Source : stock_market_cycles.md, image_07) : Yale Hirsch (fondateur du *Stock Trader's Almanac*) a découvert le cycle de 6 mois en 1986. Période haussière : novembre à avril. Période baissière : mai à octobre. Adage : "go away and sell in May". Ce cycle est l'un des plus populaires à Wall Street.
**TRADEX-AI C4** : Sur ES (confirmation TRADEX), novembre-avril = biais haussier structurel ; mai-octobre = biais baissier — à intégrer dans le contexte saisonnier du score /10.
*Catégorie : saisonnalite*

### D3942 — Amélioration du cycle 6 mois par Sy Harding avec le MACD
🔵 **ÉCOLE** (Source : stock_market_cycles.md) : Sy Harding a combiné le cycle 6 mois et le cycle présidentiel avec le MACD pour le timing. Règle : Acheter quand les deux cycles sont haussiers ET que le MACD devient positif. Vendre quand les deux cycles sont baissiers ET que le MACD devient négatif. Exemple de combinaison indicateurs + cycles pour améliorer la performance.
**TRADEX-AI C4** : Modèle de confirmation croisé applicable à TRADEX : cycle saisonnier + cycle présidentiel + momentum (MACD ou Stochastique) = signal de tendance macro renforcé pour ES/GC.
*Catégorie : timing*

### D3943 — Nesting : signal renforcé quand plusieurs cycles convergent au même creux
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Un creux cyclique est renforcé (Nesting) quand plusieurs cycles signalent un Trough simultanément. Les cycles de 10 semaines, 20 semaines et 40 semaines sont "nestés" quand ils atteignent tous un creux en même temps. Les signaux sont amplifiés quand plusieurs cycles se nichent à un creux cyclique.
**TRADEX-AI C7** : Sur GC/ES, convergence des creux 10w + 20w + 40w = signal de retournement majeur — booste le score /10 TRADEX quand aligné avec la méthode Belkhayate.
*Catégorie : timing*

### D3944 — Inversions cycliques : quand le haut arrive à la place du bas
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Parfois, un haut de cycle apparaît là où un bas était attendu et vice versa. Les inversions se produisent quand un haut ou bas de cycle est sauté ou minimal. Dans une forte tendance haussière, le creux cyclique peut être court ou quasi inexistant. Les marchés peuvent baisser rapidement et sauter un haut cyclique. Les inversions sont plus fréquentes avec les cycles courts et moins communes avec les cycles longs.
**TRADEX-AI C1** : Sur GC/CL, une forte tendance peut "sauter" le creux prévu — ne pas attendre mécaniquement un creux cyclique si la tendance est très forte (G11-G20 TRADEX).
*Catégorie : timing*

### D3945 — Trois catégories de données dans un graphique de prix
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Les données d'un graphique peuvent être divisées en 3 catégories : (1) Trending : mouvement directionnel soutenu, (2) Cyclical : déviations récurrentes par rapport à la moyenne, (3) Random : bruit, généralement causé par la volatilité intraday ou quotidienne. Pour trouver les cycles, supprimer le trend et le bruit aléatoire.
**TRADEX-AI C1** : Framework d'analyse pour GC/CL : isoler la composante cyclique en lissant (SMA 5j) et détrendant (DPO) — les mouvements cycliques sont distincts de la tendance Belkhayate.
*Catégorie : structure_marche*

### D3946 — Cycles boursiers connus : 10, 20 et 40 semaines
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Le marché boursier est connu pour avoir des cycles de 10 semaines, 20 semaines et 40 semaines. Ces cycles peuvent être combinés avec le Cycle des 6 Mois et le Cycle Présidentiel pour une valeur ajoutée.
**TRADEX-AI C7** : Sur ES/GC, les cycles 10w/20w/40w sont des références standard à croiser avec les cycles saisonniers TRADEX — à documenter dans la KB Belkhayate comme cycles de timing.
*Catégorie : timing*

### D3947 — Utilisation conjointe cycles + tendance + oscillateurs
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Les cycles s'utilisent idéalement en conjonction avec d'autres outils d'analyse technique. La tendance établit la direction, les oscillateurs définissent le momentum, et les cycles anticipent les points de retournement. Chercher une confirmation avec le support/résistance ou un retournement d'un oscillateur de momentum clé.
**TRADEX-AI C1** : Alignement TRADEX : cycles = anticipation des turning points, Belkhayate COG = tendance, Stochastique/StochRSI = momentum — les 3 couches pour le score /10.
*Catégorie : timing*

### D3948 — Paramétrage SharpCharts pour l'analyse cyclique
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md, image_08) : Paramétrage recommandé pour l'analyse cyclique sur SharpCharts : Chart Type = Invisible (masque les barres de prix) · Log Scale activé · Extra Bars pour étendre les lignes cycliques dans le futur · SMA 5j déplacée comme overlay · DPO 20j en indicateur sous le graphique.
**TRADEX-AI C1** : Template d'analyse cyclique transposable sur NinjaTrader 8 pour GC/CL — SMA 5j + DPO comme base d'identification des cycles temporels.
*Catégorie : configuration*

### D3949 — Les cycles peuvent disparaître et se réinverter
🟢 **FAIT VÉRIFIÉ** (Source : stock_market_cycles.md) : Les cycles ont tendance à changer dans le temps et peuvent même disparaître temporairement, similairement aux tendances. Un trend disparaît quand le marché entre dans un trading range et s'inverse quand les prix changent de direction. Les cycles peuvent aussi disparaître et s'inverser. L'analyse cyclique n'est pas infaillible — certains cycles manqueront, d'autres disparaîtront, d'autres frapperont exactement.
**TRADEX-AI C1** : Sur GC/CL, ne pas se fier mécaniquement aux cycles seuls — toujours confirmer avec la méthode Belkhayate (C1) et le momentum (C5) avant de signaler.
*Catégorie : psychologie*

### D3950 — Cycles les plus utiles combinés : 6 mois + présidentiel + 10/20/40 semaines
🟡 **SYNTHÈSE** (Source : stock_market_cycles.md) : La combinaison des cycles les plus robustes inclut : Cycle des 6 Mois (saisonnier), Cycle Présidentiel (4 ans), et cycles harmoniques 10w/20w/40w. Quand plusieurs cycles se nichent (Nesting) à un creux, le signal de retournement est le plus fort.
**TRADEX-AI C4** : Framework macro pour ES (confirmation TRADEX) : aligner saisonnier (6 mois) + présidentiel + cycles techniques pour maximiser la qualité du contexte macro.
*Catégorie : saisonnalite*
