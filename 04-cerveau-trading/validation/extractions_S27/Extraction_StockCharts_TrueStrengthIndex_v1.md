# Extraction StockCharts — True Strength Index
**Source :** `bundles/stockcharts/true_strength_index.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D4711 → D4730 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-strength-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : TSI est un oscillateur momentum double-lissé particulièrement adapté aux tendances prolongées sur GC/HG/CL — filtre le bruit mieux que RSI ou Stochastique standard.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/MvUfKZkqFo3ySH4yTc77 | Chart 1 — Formule de calcul TSI | Calculating TSI | D4712 |
| /files/pnXzWOpdkAKyJdejTS34 | Chart 2 — Centerline crossover Nike | Center Line Crossover | D4715 |
| /files/lo5BrMFyyPRoKfUqfjmW | Chart 3 — Trend lines TSI Citigroup | Trend Lines | D4716 |
| /files/qoQsL2ZOAYKJFP5xZ3nv | Chart 4 — TSI deux timeframes QQQ | Overbought/Oversold | D4718 |
| /files/eqnmcqaN72Ccxc9R3q9M | Chart 5 — Signal line crossovers TSI hebdo | Signal Line Crossovers | D4720 |
| /files/a3tYF218PJgw2EYjgxLv | Chart 6 — SharpCharts TSI setup | Using with SharpCharts | D4729 |
| /files/TgmLOd73QoMu4HSlKCD3 | Chart 7 — SharpCharts TSI example | Using with SharpCharts | D4729 |

## DÉCISIONS

### D4711 — Définition TSI : oscillateur momentum à double lissage
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Le True Strength Index (TSI) est un oscillateur momentum basé sur un double lissage des variations de prix. Développé par William Blau, introduit dans *Stocks & Commodities Magazine*. Il filtre le bruit tout en capturant les flux et reflux de l'action des prix avec une ligne plus stable que les oscillateurs simples.
**TRADEX-AI C1** : Sur GC et CL (forte tendance possible sur plusieurs semaines), le TSI offre un signal momentum plus fiable que des oscillateurs rapides — pertinent pour confirmer la direction de la tendance en C1.
*Catégorie : indicateurs_momentum*

### D4712 — Formule de calcul TSI en trois étapes
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md, image Chart 1) : Calcul en 3 étapes : (1) PC = Prix courant − Prix précédent ; (2) Double lissage : EMA25 de PC puis EMA13 de ce résultat ; (3) Même double lissage sur |PC| ; TSI = 100 × (Double Smoothed PC / Double Smoothed |PC|). Paramètres par défaut : 25, 13.
**TRADEX-AI C1** : Paramètres 25/13 sont les valeurs de référence pour GC/HG/CL/ZW sur timeframe daily. Pour range bars NT8, une adaptation des périodes peut être nécessaire (à tester en Phase C).
*Catégorie : indicateurs_momentum*

### D4713 — Interprétation : zone positive vs zone négative
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : TSI > 0 : momentum positif, prix généralement en hausse (avantage haussier). TSI < 0 : momentum négatif, prix généralement en baisse (avantage baissier). La ligne zéro est le pivot central de l'indicateur, analogue au MACD.
**TRADEX-AI C1** : Dans le scoring TRADEX /10, TSI > 0 pour GC/HG/CL/ZW peut contribuer comme confirmation de tendance C1 — règle binaire claire, facile à coder dans claude_brain.py.
*Catégorie : indicateurs_momentum*

### D4714 — Ligne de signal (EMA du TSI)
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Une ligne de signal est une EMA du TSI lui-même. Les croisements TSI/signal sont les signaux les plus fréquents. Paramètre typique : EMA10 du TSI (TSI(40,20,10) en configuration étendue).
**TRADEX-AI C1** : Les croisements ligne de signal sont très fréquents — nécessitent un filtre supplémentaire (confirmer avec d'autres cercles TRADEX) pour éviter les faux signaux sur GC/CL.
*Catégorie : indicateurs_momentum*

### D4715 — Croisement de la ligne zéro : signal le plus pur
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md, image Chart 2) : Le croisement de la ligne zéro est qualifié de "signal le plus pur" du TSI. Passage au-dessus = signal haussier ; passage en-dessous = signal baissier. Exemple Nike 2011 : TSI croisant en territoire positif → hausse soutenue jusqu'au printemps 2012.
**TRADEX-AI C1** : Pour GC (Or), un croisement zéro TSI coïncidant avec un signal BGC Belkhayate renforce la conviction d'entrée — pertinent pour la règle 3/4 actifs trading alignés.
*Catégorie : indicateurs_momentum*

### D4716 — Lignes de tendance sur le TSI lui-même
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md, image Chart 3) : Le TSI suit suffisamment fidèlement les prix pour que des lignes de tendance, niveaux de support et résistance puissent être tracés directement sur l'oscillateur. Les cassures de ces lignes sur le TSI génèrent des signaux d'entrée/sortie.
**TRADEX-AI C1** : Caractéristique unique du TSI parmi les oscillateurs — applicable sur GC/HG pour identifier des structures de consolidation du momentum avant un breakout directionnel.
*Catégorie : structure_marche*

### D4717 — Niveaux overbought/oversold variables selon volatilité
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Les niveaux overbought/oversold du TSI ne sont PAS fixes — ils varient selon la volatilité de l'actif et les paramètres de lissage. Exemples : TSI(40,20,7) → niveaux ±20 ; TSI(13,7,7) → niveaux ±50. Périodes plus courtes = plage plus large et plus volatile.
**TRADEX-AI C2** : Sur CL (Pétrole, forte volatilité) les niveaux overbought/oversold seront plus éloignés du zéro que sur ZW (Blé) — les seuils doivent être calibrés par actif, pas universels.
*Catégorie : indicateurs_momentum*

### D4718 — OB/OS ne signalent pas un retournement immédiat
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md, image Chart 4) : Un niveau overbought ou oversold sur TSI ne constitue pas en soi un signal de retournement. Il indique seulement que les prix ont bougé trop vite. Un signal de confirmation (cassure de ligne de tendance, croisement) est requis pour agir.
**TRADEX-AI C1** : Règle de prudence essentielle pour TRADEX : ne pas entrer VENTE uniquement parce que TSI est overbought sur GC — attendre confirmation structurelle additionnelle.
*Catégorie : gestion_risque_entree*

### D4719 — Tradeoff période courte vs période longue
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Périodes courtes : signaux plus rapides, moins de lag, mais plus de whipsaws et faux signaux. Périodes longues : moins de whipsaws, mais lag accru et ratio reward-to-risk moins favorable. C'est le compromis classique en analyse technique.
**TRADEX-AI C1** : Pour TRADEX en mode Auto (exécution rapide), favoriser des paramètres TSI plus courts ; en mode Manuel (Abdelkrim décide), des paramètres plus longs réduisent les faux signaux présentés à l'écran.
*Catégorie : configuration*

### D4720 — Croisements ligne de signal : fréquents, nécessitent filtre
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md, image Chart 5) : Les croisements TSI/signal line sont très fréquents (exemple : au moins 12 croisements de 2007 à 2012 sur chart hebdomadaire). Ils génèrent des signaux bons, mauvais et inutilisables. Un filtrage supplémentaire est indispensable.
**TRADEX-AI C1** : Dans le moteur TRADEX, un croisement TSI/signal isolé NE SUFFIT PAS pour déclencher le Niveau 3 (appel Claude API) — il doit être combiné avec d'autres critères de la règle 3/4 + 2/3.
*Catégorie : gestion_risque_entree*

### D4721 — TSI sur graphiques hebdomadaires pour réduire le bruit
🟡 **SYNTHÈSE** (Source : true_strength_index.md) : L'utilisation du TSI sur timeframe hebdomadaire avec des paramètres étendus (ex. TSI(40,20,10)) réduit significativement les faux signaux par rapport au daily, au coût d'un lag plus important.
**TRADEX-AI C4** : Pour l'analyse macro de confirmation (DX, ES en C4), un TSI hebdomadaire peut filtrer les oscillations de court terme et donner une vue de la tendance de fond — pertinent pour le contexte macro du signal TRADEX.
*Catégorie : indicateurs_tendance*

### D4722 — TSI capte les tendances prolongées (peaks et troughs alignés)
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Le TSI est qualifié d'"unique" car il suit bien les prix sur des mouvements prolongés. Les pics et creux de l'oscillateur correspondent souvent aux pics et creux des prix — ce qui n'est pas le cas de beaucoup d'oscillateurs qui divergent vite.
**TRADEX-AI C1** : Sur GC (tendances séculaires Or), cette propriété du TSI est précieuse — les pics/creux TSI peuvent signaler des points de retournement majeurs avec confirmation visuelle directe.
*Catégorie : indicateurs_momentum*

### D4723 — Divergences haussières et baissières
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Comme la plupart des oscillateurs momentum, le TSI permet d'identifier des divergences haussières (prix fait un nouveau bas, TSI ne confirme pas) et baissières (prix fait un nouveau haut, TSI ne confirme pas). Attention : les divergences peuvent être trompeuses en tendance forte.
**TRADEX-AI C1** : Divergence baissière TSI sur GC (Or fait nouveau haut mais TSI en baisse) = signal d'alerte précoce de retournement — à intégrer comme critère dans le Cercle C1 du scoring TRADEX.
*Catégorie : configuration*

### D4724 — Confirmation multi-indicateurs obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : true_strength_index.md) : Le texte conclut explicitement : "TSI signals should be confirmed with other indicators and analysis techniques." Aucun signal TSI ne doit être utilisé seul.
**TRADEX-AI C1** : Aligne parfaitement avec la règle TRADEX 3/4 trading + 2/3 confirmation — le TSI est un composant parmi d'autres, jamais un signal autonome.
*Catégorie : gestion_risque_entree*

### D4725 — Scan haussier TSI : croisement en territoire positif
🔵 **ÉCOLE** (Source : true_strength_index.md) : Scan standard bullish TSI : TSI(40,20,10) > 0 ET TSI crosses above its signal line. Double condition (territoire positif + croisement) pour réduire les faux signaux.
**TRADEX-AI C1** : Cette double condition (position absolue + croisement) peut servir de filtre technique codé dans le Niveau 1 Python de TRADEX pour les actifs GC/HG/CL/ZW.
*Catégorie : configuration*

### D4726 — Scan baissier TSI : croisement en territoire négatif
🔵 **ÉCOLE** (Source : true_strength_index.md) : Scan standard bearish TSI : TSI(40,20,10) < 0 ET TSI Signal crosses above TSI (ligne signal croise au-dessus de TSI). Symétrique du scan haussier.
**TRADEX-AI C1** : Condition de short sur GC/HG/CL/ZW : TSI négatif ET croisement baissier — à coder comme filtre Niveau 1 dans le moteur Python TRADEX.
*Catégorie : configuration*

### D4727 — Paramètres par défaut recommandés StockCharts
🔵 **ÉCOLE** (Source : true_strength_index.md) : Paramètres par défaut sur StockCharts : TSI(25,13) pour le calcul de base ; TSI(40,20,10) pour une version plus lissée sur timeframes longs. Le troisième paramètre est la période de la ligne de signal (EMA).
**TRADEX-AI C1** : Pour TRADEX, commencer avec TSI(25,13,9) sur range bars NT8 — à backtester sur historique GC/HG avant de verrouiller les paramètres.
*Catégorie : configuration*

### D4728 — TSI et support/résistance sur l'oscillateur
🟡 **SYNTHÈSE** (Source : true_strength_index.md) : Les niveaux de support et résistance que le TSI établit sur lui-même (plateaux, consolidations) peuvent être utilisés pour identifier des cassures ou ruptures de momentum avant même que le prix ne les confirme.
**TRADEX-AI C1** : Cette propriété avancée du TSI peut servir d'alerte précoce pour TRADEX : si TSI casse un support horizontal sur GC, préparer signal VENTE avant que le prix ne confirme.
*Catégorie : structure_marche*

### D4729 — Configuration SharpCharts : placement flexible
🔵 **ÉCOLE** (Source : true_strength_index.md, images Chart 6 et Chart 7) : Le TSI peut être placé au-dessus, en-dessous ou derrière le graphique de prix dans SharpCharts. Des lignes horizontales OB/OS personnalisées peuvent être ajoutées via "advanced options".
**TRADEX-AI C1** : Information de référence pour l'implémentation dans le dashboard React TRADEX — le TSI devrait être affiché sous le graphique prix principal pour chaque actif TRADING.
*Catégorie : configuration*

### D4730 — Confirmation multi-timeframes pour signaux plus forts
🟡 **SYNTHÈSE** (Source : true_strength_index.md) : Le TSI peut être utilisé sur de multiples timeframes. Bien que cela soit mentionné pour le TTM Squeeze dans la source, la logique de confirmation multi-timeframe est un principe général explicite dans la documentation StockCharts.
**TRADEX-AI C1** : Un signal TSI aligné sur daily ET sur le timeframe range bars NT8 pour GC/CL constitue une confirmation plus forte qu'un signal sur un seul timeframe — à pondérer dans le scoring /10.
*Catégorie : configuration*
