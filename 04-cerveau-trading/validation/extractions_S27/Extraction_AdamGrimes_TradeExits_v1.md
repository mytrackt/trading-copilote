# Extraction AdamGrimes — Exits: know when to hold 'em, know when to fold 'em
**Source :** `bundles/adamgrimes/trade_exits.md` (HTTP 200) + 0 images certifiées
**Méthode images :** N/A · 0/0 certifiées · 0 à vérifier
**Décisions :** D7071 → D7090 · **Page :** https://www.adamhgrimes.com/trade-exits/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Taxonomie complète des sorties de trades (stops initiaux, stops réduits, targets, trailing stops) — applicable au risk_manager.py et à la gestion de position active.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle (graphique book p.242-243 mentionné mais non inclus) | — | — |

## DÉCISIONS

### D7071 — Avoir un stop de sortie défini avant d'entrer est non-négociable
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "The most important thing about initial stops is that you have one." Et "know where you're getting out before you get in" est qualifié d'axiome universel (contrairement à beaucoup d'autres qui ne le sont pas). Chaque trade doit avoir une perte maximale clairement définie.
**TRADEX-AI C1** : Règle fondamentale du risk_manager.py TRADEX : aucun ordre d'entrée sans ordre stop simultané. Le stop doit être calculé AVANT l'exécution. En mode Auto, l'ATI NT8 doit soumettre les deux ordres ensemble.
*Catégorie : gestion_risque_entree*

### D7072 — Les stops trop serrés ne fonctionnent pas en pratique
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "I've never seen anyone trade successfully with stops that are a few ticks wide." Les stops trop serrés génèrent des stops-out prématurés sur le bruit normal du marché.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, les stops doivent être dimensionnés pour absorber la volatilité normale. Paramètre ATR-based obligatoire dans risk_manager.py. Ne jamais utiliser un stop en ticks fixes indépendamment de la volatilité de l'actif.
*Catégorie : gestion_risque_entree*

### D7073 — Stop initial recommandé : environ 3-4 ATR du point d'entrée
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "For me, initial stops usually end up somewhere around 3-4 ATRs from the entry." Ces stops sont larges et inconfortables pour beaucoup de traders, mais la solution est de réduire la taille de position pour contrôler la perte nominale.
**TRADEX-AI C1** : Paramètre initial stop TRADEX : 3 à 4 ATR (selon l'actif et le timeframe NT8 range bars). À ajuster en Phase C lors des backtests sur GC/HG/CL/ZW. Réduire le sizing plutôt que serrer le stop.
*Catégorie : gestion_risque_entree*

### D7074 — Les gaps peuvent causer des pertes bien supérieures au stop initial
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Bad things will happen. You will have the (hopefully rare) experience of a nasty gap beyond your stop, and sometimes will see losses that are whole number multiples of your initial trade risk." L'auteur cite un exemple réel de perte à -4.5x le risque initial (YHOO).
**TRADEX-AI C1** : Le risk_manager.py doit limiter le risque par trade à 1-2% max du capital. Une perte à 4.5x sur 1% = 4.5% de drawdown, gérable. Sur 10% par trade = catastrophe. La règle de max 1-2% par trade est absolue dans TRADEX.
*Catégorie : gestion_risque_entree*

### D7075 — Déplacer le stop rapidement si le trade n'avance pas dans le bon sens
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : Après le stop initial, "many traders find it effective to move that stop rather quickly." Le concept de stop réduit intervient quand le trade ne progresse pas suffisamment rapidement dans le bon sens.
**TRADEX-AI C1** : Règle de gestion de position TRADEX : si après N bougies (à définir par actif en Phase C), le trade n'a pas progressé d'au moins 1 ATR favorable, resserrer le stop au breakeven ou à un niveau réduit. Limite le risque sans sortir trop tôt.
*Catégorie : gestion_position_active*

### D7076 — Time stop : limiter le risque si le trade ne se développe pas dans le temps défini
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Another possibility to consider is the time stop, in which we take steps to limit the position risk if the trade does not move in some defined time." Options : serrer le stop, réduire la taille, sortir complètement.
**TRADEX-AI C1** : Implémenter un time stop dans TRADEX : si un trade en mode Auto ne progresse pas dans le sens attendu après X minutes (paramètre à calibrer par actif), déclencher automatiquement le passage au breakeven stop. Pertinent pour les sessions NT8 en heures actives.
*Catégorie : gestion_position_active*

### D7077 — Réduire la position à perte "délèvere" le P&L dans l'espace des pertes
🟡 **SYNTHÈSE** (Source : trade_exits.md) : L'auteur déconseille de réduire la position à perte car cela "effectively 'deleverages' your P&L in the 'loss space.'" Il préfère prendre des pertes entières mais plus petites. Mais reconnaît que "your experience may be different."
**TRADEX-AI C1** : En mode Auto TRADEX, la règle par défaut est de sortir la position entière (pas de sortie partielle à perte). En mode Manuel, Abdelkrim peut adapter. Le risk_manager.py implémente cette règle par défaut.
*Catégorie : gestion_position_active*

### D7078 — Les composantes du système de trading sont interdépendantes : changer une change tout
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "All of this — entry, exit, position size, moving stops, taking targets, re entries, adding to positions, partial exits, etc. — all of this must work together. You change one piece, and the whole system will change."
**TRADEX-AI C1** : Principe d'architecture TRADEX : les règles de CLAUDE.md (DÉCISIONS VERROUILLÉES) ne peuvent pas être modifiées en isolation. Toute modification d'un paramètre (ex: seuil grille /10) nécessite une re-validation complète du système. Cohérent avec le protocole de non-réouverture des décisions verrouillées.
*Catégorie : gestion_position_active*

### D7079 — Pour les traders de tendance : laisser courir les gains
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "For trend traders, we must let our profits run." Contradiction avec la prise de targets rapides ; la réconciliation dépend du style de trading. Trend trading = laisser courir. Countertrend trading = prendre des profits rapides à des niveaux prédéfinis.
**TRADEX-AI C1** : TRADEX est principalement un système de trend following (méthode Belkhayate = suivre la direction). La stratégie de sortie par défaut doit donc être le trailing stop, pas le target fixe. Cohérent avec les décisions verrouillées.
*Catégorie : gestion_position_active*

### D7080 — Traders countertrend : targets fixes à 1x le risque initial de l'autre côté
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "I have not found chart patterns or points to be any more effective than simply setting a target 1X my initial risk on the 'other side' of the entry." Pour les setups countertrend, target simple à 1:1 R/R est aussi efficace que les pivots et trendlines.
**TRADEX-AI C1** : Pour les rares setups de retournement sur GC/HG (mean reversion extrême), target initial à 1:1. Note : la règle TRADEX impose R/R ≥ 1:2 pour les signaux valides — un target 1:1 est donc sous le seuil requis pour déclencher un signal auto.
*Catégorie : gestion_position_active*

### D7081 — Hauts et bas de journée méritent respect pour les traders intraday
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "For intraday traders, highs and lows of the day do deserve respect." Contrairement aux pivots et trendlines en général, les extremes de la journée ont une valeur technique réelle pour les timeframes courts.
**TRADEX-AI C1** : Sur NT8 en range bars (intraday), les high/low du jour sont des niveaux de résistance/support valides pour placer targets ou stops. À intégrer dans les règles de gestion active de position pour GC/HG/CL/ZW.
*Catégorie : gestion_position_active*

### D7082 — Trailing stops très efficaces dans de nombreux types de trading
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Trailing stops can be managed in many ways, and I have found these to be very effective in many types of trading." Plusieurs méthodes : volatility-adjusted, stop au low de la veille, stop très serré pour forcer la sortie.
**TRADEX-AI C1** : TRADEX doit implémenter des trailing stops volatility-adjusted (ATR-based) comme méthode principale de sortie en profit. Le paramètre de trailing doit être calibré par actif en Phase C. Option : trailing au low/high de la session précédente pour les positions multi-jours sur GC.
*Catégorie : gestion_position_active*

### D7083 — Trailing serré peut forcer la sortie sur des profits — c'est délibéré
🟡 **SYNTHÈSE** (Source : trade_exits.md) : "There are even times we trail a very tight stop, effectively hoping to be taken out of the trade." Cette technique est utilisée pour sortir d'une position profitable sans avoir à décider activement du moment de sortie.
**TRADEX-AI C1** : Technique applicable en mode Manuel quand Abdelkrim veut sécuriser un profit sur GC sans surveiller en permanence. En mode Auto, le risk_manager.py peut déclencher un trailing serré après un profit > X ATR.
*Catégorie : gestion_position_active*

### D7084 — Un trade qui s'étend semaine après semaine sans raison de sortir est une bonne surprise
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Sometimes you may trail a stop at yesterday's low, and be shocked as the trade grinds in your favor week after week — there's nothing to be done in these cases but be forced to stay in the trade and make more money." Ces situations de tendance longue sont rares mais existent.
**TRADEX-AI C1** : Sur GC en forte tendance Belkhayate (BGC persistant), le trailing stop au low/high de la veille peut maintenir une position gagnante plusieurs jours/semaines. TRADEX ne doit pas fermer une position artificielle par timeout si le trailing stop n'est pas atteint.
*Catégorie : gestion_position_active*

### D7085 — Guetter la fin brutale d'un move climactique (hubris risk)
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Guard against hubris: many of the times this has happened to me I have been properly positioned into a climax move. When these moves end, they often end dramatically, so simply ring the register and step away from the market."
**TRADEX-AI C1** : Signal de sortie TRADEX : un move extrême sur GC/HG/CL/ZW avec accélération de la vitesse + VIX en spike + divergence BGC = potentiel climax. Resserrer le trailing stop significativement. Cohérent avec la règle de suspension_auto après profit anormal.
*Catégorie : gestion_position_active*

### D7086 — Combiner target partiel + trailing stop sur le reste = approche optimale swing trading
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : L'auteur recommande : "combining these techniques, using a pre-defined target for part of the trade, trailing the stop on the rest, and moving quickly to reduce initial risk on my rather wide initial stops, this works very well for swing trading."
**TRADEX-AI C1** : Structure de sortie TRADEX recommandée pour swing trading (GC/HG/CL/ZW) : sortie partielle (50%) à 1x le risque initial + trailing stop ATR-based sur le solde. À implémenter dans risk_manager.py en Phase C.
*Catégorie : gestion_position_active*

### D7087 — Profit targets = ordres limites ; stops = ordres stop (distinction opérationnelle)
🔵 **ÉCOLE** (Source : trade_exits.md) : "Profit targets are usually limit orders, as opposed to stops (which, not surprisingly, are usually stop orders.)" Pour les marchés 24h, placer les limites de prise de profit en dehors des heures actives est pertinent — les gens font des erreurs afterhours et fournissent des liquidités à bon prix.
**TRADEX-AI C1** : Pour l'ATI NT8 (port 36973), distinction technique obligatoire : ordres de sortie en profit = Limit orders ; ordres de stop loss = Stop Market orders. Le code d'exécution TRADEX doit implémenter cette distinction correctement pour éviter le slippage.
*Catégorie : gestion_position_active*

### D7088 — Ne pas travailler de stops en afterhours sur les marchés 24h
🟡 **SYNTHÈSE** (Source : trade_exits.md) : L'auteur indique qu'il place des limites de prise de profit en afterhours mais "may not wish to work stops in the same after hours environments" — le risque de gap et de comportements anormaux en dehors des heures actives est plus élevé.
**TRADEX-AI C1** : Pour GC/CL sur CME (presque 24h), le staleness_monitor doit identifier les plages horaires à faible liquidité. En dehors des heures actives principales, désactiver les stops automatiques ou passer en mode Manuel obligatoire.
*Catégorie : gestion_position_active*

### D7089 — La cohérence dans un système efficace est indispensable ; la cohérence dans un mauvais système est destructrice
🟢 **FAIT VÉRIFIÉ** (Source : trade_exits.md) : "Consistency certainly matters, but consistently doing something that works will, not surprisingly, lead to consistently losing money." La discipline de respecter un système ne vaut que si le système a un edge réel. Les deux conditions sont nécessaires : (1) edge + (2) discipline.
**TRADEX-AI C1** : TRADEX doit valider l'edge de chaque règle KB avant de l'intégrer (pipeline validation/ + audit automatique). La discipline d'Abdelkrim à respecter les règles n'a de valeur que si les règles ont été rigoureusement validées.
*Catégorie : psychologie*

### D7090 — Surveiller sa propre performance pour valider l'edge en temps réel
🔵 **ÉCOLE** (Source : trade_exits.md) : "Monitor your performance accordingly." Un système doit être suivi avec des métriques de performance réelles. Un système avec edge théorique qui ne se matérialise pas en live nécessite une révision.
**TRADEX-AI C1** : TRADEX doit logger chaque signal (entrée, sortie, résultat) dans SQLite pour suivi de performance. Métriques clés : win rate, R/R moyen réalisé, profit factor, max drawdown. Tableau de bord React doit afficher ces métriques pour Abdelkrim.
*Catégorie : gestion_position_active*
