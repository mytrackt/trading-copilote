# Extraction NinjaTrader — Identifying Trends in Futures Markets
**Source :** `bundles/ninjatrader/identifying_trends_in_futures_markets.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7891 → D7910 · **Page :** https://ninjatrader.com/learn/technical-analysis/identifying-trends-in-futures-markets/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Identification de tendance par trendlines, moyennes mobiles et DMI/ADX — socle C1 du scoring Belkhayate pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

## DÉCISIONS

### D7891 — Tendance : définition de base
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : La tendance est la direction générale dans laquelle un marché évolue au fil du temps. En futures, la tendance peut être exploitée dans les deux sens : long (buy low, sell high) en uptrend, short (sell high, buy low) en downtrend.
**TRADEX-AI C1** : Le sens de la tendance dominante est le premier filtre de TRADEX-AI avant tout signal ; un signal contre-tendance nécessite un score C1 plus élevé pour être validé.
*Catégorie : indicateurs_tendance*

### D7892 — Trendline en uptrend : connexion des pivot lows
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : En uptrend, la trendline est tracée en reliant deux pivot lows (le plus bas parmi plusieurs barres avant et après ce bas) ; elle identifie le support de tendance. Un croisement ou cassure de cette ligne peut indiquer un retournement.
**TRADEX-AI C1** : La trendline haussière sur GC/CL constitue un niveau de support dynamique ; si le prix teste cette ligne et rebondit en conjonction avec un signal Belkhayate, le score C1 est renforcé.
*Catégorie : indicateurs_tendance*

### D7893 — Trendline en downtrend : connexion des pivot highs
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : En downtrend, la trendline est tracée en reliant les pivot highs ; elle identifie la résistance de tendance. Une cassure au-dessus de cette ligne peut signaler un retournement du downtrend.
**TRADEX-AI C1** : Sur ZW/HG en downtrend, la cassure de la trendline de résistance est une condition de confirmation supplémentaire avant de valider un signal ACHETER Belkhayate.
*Catégorie : indicateurs_tendance*

### D7894 — Moyenne mobile : définition et principe de calcul
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : La moyenne mobile calcule la moyenne d'un nombre défini de barres pour normaliser les données et faciliter l'identification de la tendance générale. Elle est "mobile" car à chaque nouvelle barre, la donnée la plus ancienne sort du calcul et la nouvelle moyenne s'ajoute.
**TRADEX-AI C1** : Les MAs sont utilisées comme indicateurs de tendance dans le cercle C1 de TRADEX-AI ; elles constituent un input de base pour le scoring Belkhayate.
*Catégorie : indicateurs_tendance*

### D7895 — Périodes de moyenne mobile standard
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Périodes courantes sur graphiques journaliers : 50, 100 et 200. Sur graphiques intraday : 5, 10 et 20. Le choix de la période permet d'identifier les tendances sur différents horizons temporels.
**TRADEX-AI C1** : Sur range bars NT8 pour GC/HG/CL/ZW, les périodes intraday (5, 10, 20) sont plus adaptées ; la MA 200 daily sert de filtre de biais directionnel macro dans C1.
*Catégorie : indicateurs_tendance*

### D7896 — Identification de tendance par la pente de la MA
🟢 **FAIT VÉRIFIÉ** (Source : identifying_trends_in_futures_markets.md) : La pente d'une moyenne mobile est l'une des meilleures méthodes pour déterminer la direction de la tendance : pente montante = bullish, pente descendante = bearish. En ajustant la période, on peut identifier des tendances sur différents horizons.
**TRADEX-AI C1** : La pente de la MA principale entre dans le score C1 de TRADEX-AI ; une MA en pente ascendante sur l'actif tradé renforce le score d'un signal ACHETER.
*Catégorie : indicateurs_tendance*

### D7897 — Sentiment de marché via position des barres par rapport à la MA
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Biais haussier = les barres de prix sont au-dessus de la moyenne mobile. Biais baissier = les barres de prix sont en dessous de la moyenne mobile.
**TRADEX-AI C1** : Règle de filtrage rapide : si le prix est sous la MA principale, les signaux ACHETER reçoivent un malus de score C1 ; l'inverse s'applique pour les signaux VENDRE.
*Catégorie : indicateurs_tendance*

### D7898 — MA comme support et résistance dynamique
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Les lignes de moyennes mobiles agissent souvent comme des niveaux de support et de résistance à mesure que les prix s'en approchent. Prix venant d'au-dessus → support potentiel ; prix venant d'en dessous → résistance potentielle.
**TRADEX-AI C1** : La MA sert de niveau de référence pour le placement du stop loss dans TRADEX-AI ; un stop sous la MA (long) ou au-dessus (short) est une pratique conforme à la méthode Belkhayate.
*Catégorie : gestion_risque_entree*

### D7899 — Croisement de prix avec MA : signal directionnel
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Le prix qui croise au-dessus de la MA = signal haussier. Le prix qui croise en dessous de la MA = signal baissier.
**TRADEX-AI C1** : Un croisement de prix avec la MA sur l'actif tradé dans le sens du signal Belkhayate renforce la confirmation C1 ; un croisement inverse constitue un signal d'alerte.
*Catégorie : indicateurs_tendance*

### D7900 — Golden Cross et Death Cross des MAs
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : MA courte terme croisant au-dessus de la MA long terme = golden cross (tendance haussière possible). MA courte terme croisant en dessous de la MA long terme = death cross (tendance baissière indiquée).
**TRADEX-AI C1** : Un golden/death cross entre MA20 et MA50 sur range bars NT8 constitue un signal de tendance moyen terme qui renforce ou atténue le score C1 selon l'alignement avec le signal Belkhayate.
*Catégorie : indicateurs_tendance*

### D7901 — DMI DI+ et DI- : direction de la tendance
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Le DMI compare les variations de highs et lows d'une barre à l'autre pour déterminer si un mouvement est positif ou négatif, produisant deux lignes : DI+ (vert) et DI- (rouge). DI+ > DI- = tendance haussière ; DI- > DI+ = tendance baissière ; croisement des lignes = possible changement de tendance.
**TRADEX-AI C1** : DI+/DI- du DMI est un indicateur de direction compatible avec TRADEX-AI ; son alignement avec la direction du signal Belkhayate renforce le score C1.
*Catégorie : indicateurs_tendance*

### D7902 — ADX : mesure de la force de la tendance
🟢 **FAIT VÉRIFIÉ** (Source : identifying_trends_in_futures_markets.md) : L'ADX (dérivé du DMI) mesure la force de la tendance. ADX ≤ 25 = absence de tendance (range). ADX > 25 = tendance en place. Plus l'ADX est élevé au-dessus de 25, plus la tendance est forte. Seuil de surveillance : croisement de 25 à la hausse ou à la baisse.
**TRADEX-AI C1** : Règle de filtrage TRADEX-AI : ADX < 25 sur l'actif tradé = marché en range → score C1 réduit → signal moins probable d'atteindre le seuil ≥ 7,0/10 requis.
*Catégorie : indicateurs_tendance*

### D7903 — ADX seuil 25 : frontière range/tendance
🟢 **FAIT VÉRIFIÉ** (Source : identifying_trends_in_futures_markets.md) : Il est généralement admis qu'un ADX inférieur ou égal à 25 indique l'absence de tendance, tandis que des valeurs supérieures à 25 indiquent une tendance établie.
**TRADEX-AI C1** : Le seuil 25 de l'ADX est un garde-fou codable dans le moteur Python de TRADEX-AI : si ADX < 25, le niveau 1 de l'architecture événementielle peut bloquer la montée au niveau 3 (appel Claude).
*Catégorie : indicateurs_tendance*

### D7904 — Pivot low : définition technique
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Un pivot low est défini comme le plus bas d'une série de barres adjacentes (le plus bas parmi plusieurs barres avant et après ce bas).
**TRADEX-AI C1** : Les pivot lows sont les ancrages naturels des Pivots Belkhayate dans NT8 ; leur identification précise est fondamentale pour tracer la trendline de support.
*Catégorie : structure_marche*

### D7905 — Utilité des trendlines : cassure = signal de retournement
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : En downtrend, si les prix cassent à la hausse la trendline de résistance, cela peut indiquer que le downtrend pourrait s'inverser.
**TRADEX-AI C1** : La cassure de trendline dans le sens du signal Belkhayate est un déclencheur de confirmation ; elle renforce le score C1 à la condition que le volume valide le breakout (C2).
*Catégorie : structure_marche*

### D7906 — Complémentarité MA et autres outils d'analyse
🟡 **SYNTHÈSE** (Source : identifying_trends_in_futures_markets.md) : La compréhension de la tendance de marché est un concept fondamental qui ouvre la voie à l'univers plus large des outils d'analyse technique disponibles pour mesurer le comportement du marché.
**TRADEX-AI C1** : Dans TRADEX-AI, les MAs et DMI/ADX constituent la couche de base du cercle C1 ; ils sont complétés par les indicateurs Belkhayate propriétaires (BGC, Direction, Energie, Pivots) pour le score final.
*Catégorie : indicateurs_tendance*

### D7907 — Direction de trading en downtrend : sell high, buy low
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : En futures, les traders bénéficient de la possibilité de renverser le principe "buy low, sell high" en "sell high, buy low" lorsque la tendance est baissière, grâce à la facilité de vente à découvert.
**TRADEX-AI C1** : TRADEX-AI gère les signaux VENDRE (short) de la même façon que les signaux ACHETER ; la tendance dominante valide quelle direction favoriser.
*Catégorie : gestion_risque_entree*

### D7908 — Prise de décision basée sur la tendance
🟡 **SYNTHÈSE** (Source : identifying_trends_in_futures_markets.md) : Comprendre et identifier la direction de la tendance actuelle, ou si cette tendance est en train de changer, aide à prendre de meilleures décisions de trading éclairées.
**TRADEX-AI C1** : Le cerveau Claude de TRADEX-AI doit d'abord établir le biais directionnel (C1) avant d'analyser les autres cercles ; un biais ambigu = signal ATTENDRE par défaut.
*Catégorie : psychologie*

### D7909 — Périodes MA intraday vs daily
🔵 **ÉCOLE** (Source : identifying_trends_in_futures_markets.md) : Les graphiques intraday utilisent des périodes de MA plus courtes (5, 10, 20) comparativement aux daily (50, 100, 200) pour s'adapter à la granularité temporelle.
**TRADEX-AI C1** : Paramètre de configuration TRADEX-AI : sur range bars NT8 (intraday), utiliser MA 5/10/20 pour le score C1 temps réel ; MA 50/200 daily comme filtre de biais macro.
*Catégorie : indicateurs_tendance*

### D7910 — Identification de tendance : étape fondamentale
🟡 **SYNTHÈSE** (Source : identifying_trends_in_futures_markets.md) : Reconnaître les patterns graphiques représentant un comportement potentiel du marché est une première étape clé de l'analyse technique pour les traders de futures ; combiné aux indicateurs de momentum, volatilité et volume, cela aide à identifier des opportunités de trading.
**TRADEX-AI C1** : Les 7 cercles d'intelligence de TRADEX-AI intègrent cette hiérarchie : C1 (prix/tendance) est le cercle de base, obligatoirement cohérent avec les autres cercles pour atteindre le score ≥ 7,0/10 requis.
*Catégorie : structure_marche*
