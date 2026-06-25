# Extraction AdamGrimes — How to Trade Support and Resistance Levels
**Source :** `bundles/adamgrimes/how_to_trade_support_and_resistance_levels.md` (HTTP 200) + 0 images certifiées
**Méthode images :** images référencées dans le texte (schémas + exemples marché) mais non disponibles dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6091 → D6108 · **Page :** https://www.adamhgrimes.com/how-to-trade-support-and-resistance-levels/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Taxonomie des 6 trades autour des niveaux S/R — applicable aux pivots Belkhayate (C1) et aux niveaux institutionnels (C3) sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune disponible dans le bundle) | — | — | — |

## DÉCISIONS

### D6091 — Niveaux pertinents : qualité prime sur quantité
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : La majorité des niveaux sur lesquels les traders se concentrent n'ont pas de réel avantage statistique. Les moyennes mobiles et les nombres ronds sont explicitement cités comme niveaux à faible edge. Il faut identifier des niveaux qui "façonnent réellement le price action" : hauts/bas de la veille, VWAP intraday, pivots hauts/bas significatifs sur daily/weekly, niveaux de pinning options.
**TRADEX-AI C1** : Dans la grille scoring /10, les pivots Belkhayate (BGC, pivots NT8) doivent être préférés aux niveaux arbitraires (MAs, nombres ronds). Documenter dans la KB pourquoi chaque type de niveau Belkhayate est retenu.
*Catégorie : structure_marche*

### D6092 — Langage probabiliste obligatoire : "anticipated" S/R
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Grimes insiste sur l'utilisation du mot "anticipated" (anticipé) devant "support" et "résistance". Ce mot impose automatiquement une pensée probabiliste ("peut-être" plutôt que "doit" ou "va"). Sans ce cadrage, le trader pense en termes certains et ne gère pas le risque correctement.
**TRADEX-AI C5** : Dans les prompts `claude_brain.py` et les sorties de signal TRADEX, toujours formuler : "support anticipé" / "résistance anticipée". Interdire les formulations absolues ("le prix VA rebondir sur...").
*Catégorie : psychologie*

### D6093 — Trade 1 Polarity : résistance cassée → support
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Principe classique de polarité : une résistance valide, une fois cassée, devient support sur le retest depuis le dessus. Inversement, un support cassé devient résistance. Ce principe fonctionne également à l'envers (support cassé → résistance). Les tests sont souvent "messy" (imprécis) mais le principe reste valide.
**TRADEX-AI C1** : Intégrer la polarité comme règle de confirmation dans le scoring C1. Sur GC : si un pivot Belkhayate Daily a été résistance puis est cassé, la première réaction sur ce niveau en support = signal de confirmation long (+0.5 point scoring).
*Catégorie : structure_marche*

### D6094 — Trade 2 PowerPull : attraction magnétique d'un niveau actif
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Quand un niveau est "actif" et fonctionnel, plus le marché s'en approche, plus l'attraction est forte. Le momentum peut augmenter à l'approche du niveau — comportement décrit comme "magnétique". Particulièrement visible sur charts daily quand les indices s'approchent de leurs ATH.
**TRADEX-AI C1** : Signal PowerPull détectable : acceleration du momentum (volume + delta order flow) quand le prix est à moins de 0.3 ATR d'un pivot Belkhayate fort. Ajouter ce pattern dans les règles C2 (Order Flow confirme l'attraction vers le niveau).
*Catégorie : structure_marche*

### D6095 — Trade 3 PowerPush : ouverture près d'un niveau → high/low du jour
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Si le marché ouvre près d'un niveau fort et s'en éloigne avec momentum, il y a une forte probabilité que le high ou low de la session vienne d'être établi. Nuances : parfois breakout net, parfois nécessite une plage d'ouverture puis breakout, parfois le move initial est faux et on trade le retournement.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW : si l'ouverture de session est à moins de 0.2 ATR d'un pivot Belkhayate ET le 1er quart d'heure s'éloigne du niveau avec volume > moyenne, probabilité élevée que l'extrême de session soit établi. Règle de filtrage pour le mode Auto.
*Catégorie : timing*

### D6096 — Trade 4 Yo-yo : signal de non-trading
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Quand le marché manque de momentum et oscille alternativement au-dessus et en-dessous d'un niveau (yo-yo), c'est un signal pour NE PAS trader. C'est un environnement de noise, pas de signal. MAIS : placer des alertes aux limites du pattern — un breakout de ce range mène souvent à une extension propre vers le niveau suivant.
**TRADEX-AI C1** : Implémenter une détection de "yo-yo" : si le prix traverse le même niveau Belkhayate 3+ fois en moins de 2 heures sans direction nette → bloquer le signal, passer en ATTENDRE. Peut alimenter le circuit breaker de l'engine.
*Catégorie : gestion_risque_entree*

### D6097 — Trade 5 Pong : rebond entre deux niveaux proches
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Quand deux niveaux sont proches, le marché peut rebondir proprement entre les deux (comme une balle de ping-pong). En pratique, c'est souvent plus bruyant avec des faux breakouts. Les compétences de trading en range (range trading) s'appliquent ici.
**TRADEX-AI C1** : Si deux pivots Belkhayate sont séparés de moins de 1 ATR → identifier une zone "Pong". Les signaux directionnels dans cette zone ont une fiabilité réduite. Réduire la confiance du signal de 20% quand le prix est entre deux pivots rapprochés.
*Catégorie : gestion_risque_entree*

### D6098 — Trade 6 Clear Air : extension au-delà du niveau extrême
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Quand le marché dépasse le niveau le plus extrême de la session lors d'un jour en tendance, il y a une edge statistique pour une extension vers la clôture de la session. Fonctionne sur les charts intraday (niveaux dérivés du daily) comme sur les charts daily (niveaux dérivés du weekly). Nécessite un trailing stop car rien ne fonctionne à 100%.
**TRADEX-AI C1** : Règle "Clear Air" pour GC/HG/CL/ZW : si le prix dépasse le pivot Belkhayate extrême du jour lors d'un jour en tendance forte (SigmaSpike > 1.5) → probabilité d'extension jusqu'à la clôture. Allonger l'objectif de profit en mode Auto.
*Catégorie : gestion_position_active*

### D6099 — Biais cognitif : le cerveau crée des patterns illusoires
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Même en l'absence de pattern réel, le cerveau humain va en créer. Même des niveaux sans edge statistique semblent convaincants sur un chart. La conviction subjective ("je vois clairement que ça marche") n'est pas une preuve. Les niveaux inappropriés ou insignifiants sont une cause majeure d'échec pour les traders utilisant le S/R.
**TRADEX-AI C5** : Dans le dashboard TRADEX, afficher uniquement les niveaux Belkhayate validés quantitativement. Interdire l'affichage de niveaux "manuels" non validés qui pourraient induire des biais cognitifs chez Abdelkrim.
*Catégorie : psychologie*

### D6100 — Framework des 4 comportements possibles d'un niveau
🔵 **ÉCOLE** (Source : how_to_trade_support_and_resistance_levels.md) : Face à un niveau, il n'y a que 4 comportements possibles du marché : (1) Le niveau arrête les prix (temporairement). (2) Le niveau attire les prix. (3) Le niveau repousse les prix. (4) Le niveau n'a aucune influence — le prix agit comme si le niveau n'existait pas. Structurer sa pensée autour de ces 4 cas évite la surprise.
**TRADEX-AI C1** : Implémenter ce framework dans `claude_brain.py` : lors de l'analyse d'un niveau Belkhayate, le prompt doit demander à Claude d'identifier lequel des 4 comportements est en cours, avant de générer un signal.
*Catégorie : structure_marche*

### D6101 — VWAP intraday : niveau de référence institutionnel
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Le VWAP intraday fait partie des niveaux qui ont un edge réel selon Grimes (aux côtés des hauts/bas de la veille, des pivots daily/weekly significatifs, et des niveaux de pinning options).
**TRADEX-AI C2** : Le VWAP est un niveau institutionnel (C2 Order Flow). L'intégrer dans les données ATAS disponibles pour TRADEX. La position du prix par rapport au VWAP est un signal de confirmation pour les trades intraday sur GC/CL.
*Catégorie : volume_liquidite*

### D6102 — Hauts/bas de la veille : niveaux à edge statistique réel
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Les hauts et bas de la session précédente (PDH/PDL : Previous Day High/Low) font partie des niveaux ayant un edge statistique réel sur les marchés financiers.
**TRADEX-AI C1** : Les PDH/PDL doivent être inclus dans les niveaux que `data_reader.py` extrait des données NT8 pour GC, HG, CL, ZW. Ce sont des niveaux de référence C1 complémentaires aux pivots Belkhayate.
*Catégorie : structure_marche*

### D6103 — Niveaux de pinning options : behaviour institutionnel
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Les niveaux de pinning sur les expirations d'options font partie des niveaux à edge réel. Ce phénomène existe parce que les market makers hedgent leurs positions gamma, créant une "gravité" vers les strikes à fort open interest à l'expiration.
**TRADEX-AI C3** : Intégrer les niveaux de pinning options pour GC (Gold options COMEX) dans le Cercle C3 (Institutionnels). L'open interest par strike est disponible via CME. À intégrer dans le pipeline de données macro.
*Catégorie : volume_liquidite*

### D6104 — Pivots daily/weekly significatifs : niveaux majeurs
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_support_and_resistance_levels.md) : Les hauts et bas pivots significatifs sur les charts daily et weekly ont un edge statistique réel. La significativité est implicitement liée au volume de touches et à la "propreté" du bounce.
**TRADEX-AI C1** : Les pivots Belkhayate calculés sur les range bars NT8 correspondent à cette catégorie. Documenter dans la KB le critère de "significativité" d'un pivot Belkhayate (nb de touches min, magnitude du rejet, etc.).
*Catégorie : structure_marche*

### D6105 — Yo-yo comme signal d'alerte breakout imminent
🟡 **SYNTHÈSE** (Source : how_to_trade_support_and_resistance_levels.md) : Un pattern yo-yo n'est pas seulement un signal de non-trading — il est aussi une alerte que le prochain breakout de ce range sera probablement clean et étendu, jusqu'au niveau suivant. La compression d'énergie autour du niveau prépare un mouvement directionnel.
**TRADEX-AI C1** : Pattern combiné : après détection yo-yo (>3 traversées du niveau en 2h) → placer un ordre stop au-dessus/dessous des extrêmes du range. Le breakout qui suit a une probabilité plus élevée de reaching le niveau Belkhayate suivant.
*Catégorie : configuration*

### D6106 — Résumé des 6 trades : grille décisionnelle
🟡 **SYNTHÈSE** (Source : how_to_trade_support_and_resistance_levels.md) : Les 6 trades autour des niveaux (Polarity, PowerPull, PowerPush, Yo-yo, Pong, Clear Air) forment une taxonomie exhaustive des comportements de marché autour d'un niveau. Maîtriser ces 6 cas permet d'être préparé à toute configuration.
**TRADEX-AI C1** : Intégrer les 6 trades comme patterns nommés dans la KB TRADEX. Lors de l'analyse `claude_brain.py`, le modèle doit identifier le pattern en cours parmi ces 6 pour contextualiser le signal.
*Catégorie : configuration*

### D6107 — Problème des niveaux inappropriés : cause d'échec majeure
🟡 **SYNTHÈSE** (Source : how_to_trade_support_and_resistance_levels.md) : Beaucoup de traders échouent à trader le S/R non pas à cause de mauvaises techniques de trade mais parce qu'ils utilisent des niveaux sans edge (MAs, nombres ronds, Fibonacci arbitraires). La qualité des niveaux est déterminante.
**TRADEX-AI C1** : Le guard-rail G11-G20 (GARDE_FOUS_PROPOSES.md) doit inclure un garde-fou sur la qualité des niveaux : interdire l'utilisation de niveaux non validés quantitativement dans le signal TRADEX. Seuls PDH/PDL, VWAP, pivots Belkhayate NT8 sont autorisés.
*Catégorie : gestion_risque_entree*

### D6108 — Extension du framework à tout type de niveau
🟡 **SYNTHÈSE** (Source : how_to_trade_support_and_resistance_levels.md) : Bien que l'article se concentre sur les "MarketLife PowerLevels" de Grimes, l'auteur explicite que tous les concepts et les 6 trades s'appliquent à tout niveau ayant un edge réel (VWAP, PDH/PDL, pivots options, etc.) — "without any loss of generality."
**TRADEX-AI C1** : Les 6 trades de Grimes sont applicables aux pivots Belkhayate NT8. Cette généralisation valide l'intégration de cette taxonomie dans la KB TRADEX sans restriction au système Grimes spécifique.
*Catégorie : structure_marche*
