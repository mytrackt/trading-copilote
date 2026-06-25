# Extraction NinjaTrader — Momentum as Indicator in Futures Trading
**Source :** `bundles/ninjatrader/momentum_as_indicator_in_futures_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7951 → D7970 · **Page :** https://ninjatrader.com/learn/technical-analysis/momentum-as-indicator-in-futures-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : indicateurs momentum RSI/Stochastiques/CCI pour détecter épuisement de tendance et zones sur/sous-achetées sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D7951 — Momentum mesure le taux de changement des prix
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Les indicateurs de momentum mesurent le taux auquel les prix changent ou accélèrent, et fournissent une indication sur le moment où une tendance pourrait se terminer ou les prix potentiellement s'inverser.
**TRADEX-AI C1** : Intégrer la lecture de momentum comme filtre secondaire dans le moteur de signal — un momentum décroissant sur GC/HG/CL/ZW signale un possible essoufflement avant retournement.
*Catégorie : indicateurs_momentum*

### D7952 — RSI : seuils 30/70 sur futures
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Le RSI est borné 0–100. Seuil 30 = survente (trading bien en dessous de la moyenne récente). Seuil 70 = surachat (trading bien au-dessus). Les niveaux extrêmes suggèrent une tendance sur-étendue pouvant s'épuiser ou s'inverser.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un RSI < 30 ou > 70 renforce (ou affaiblit) le score de signal Belkhayate — à pondérer dans la grille /10 comme indicateur de confirmation de momentum.
*Catégorie : indicateurs_momentum*

### D7953 — RSI comparaison cross-marchés possible
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Puisque le RSI a la même échelle de valeur quel que soit le prix de l'instrument, il est possible de comparer les valeurs RSI entre plusieurs marchés futures pour identifier lesquels sont en surachat ou survente.
**TRADEX-AI C7** : Utiliser RSI en cross-asset pour comparer simultanément GC/HG/CL/ZW et identifier quel actif tradable est en position la plus extrême — donnée d'entrée utile pour la matrice de corrélations C7.
*Catégorie : correlations*

### D7954 — Stochastiques : calcul %K et %D
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : %K = (prix_actuel − Bas_période) / (HH − LL) sur 14 barres. %D = moyenne mobile 3 périodes de %K. Borné 0–100. Survente < 20 en tendance baissière, surachat > 80 en tendance haussière.
**TRADEX-AI C1** : Paramètres fixes Stochastiques (14, 3) à utiliser comme indicateur momentum dans les alertes visuelles du dashboard TRADEX — seuils 20/80 pour futures commodités.
*Catégorie : indicateurs_momentum*

### D7955 — Croisement %K/%D : signal de changement directionnel
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Quand la ligne %K croise la ligne %D, cela peut signaler un changement directionnel potentiel. Le signal est plus fort quand ce croisement se produit en zone surachat ou survente.
**TRADEX-AI C1** : Un croisement %K/%D en zone extrême (< 20 ou > 80) sur GC/HG/CL/ZW constitue un signal de momentum de C1 — à intégrer comme brique de confirmation dans la grille de score /10.
*Catégorie : indicateurs_momentum*

### D7956 — CCI : indicateur non borné, adapté aux commodités
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Le CCI mesure la différence entre le prix typique d'une barre et sa moyenne mobile, divisée par la déviation moyenne. Contrairement aux autres indicateurs de momentum, le CCI n'est PAS borné. Les niveaux extrêmes varient selon le marché et l'intervalle de barres utilisé.
**TRADEX-AI C1** : Sur les commodités (GC/HG/CL/ZW), les niveaux extrêmes CCI sont à calibrer par actif — ne pas appliquer de seuils fixes universels. Nécessite une phase de calibration par instrument.
*Catégorie : indicateurs_momentum*

### D7957 — CCI : divergence prix/indicateur comme signal de retournement
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : Le CCI peut aider à identifier et confirmer des retournements de tendance, ainsi que des divergences de prix par rapport au CCI, qui peuvent indiquer que le prix suivra potentiellement la direction du CCI.
**TRADEX-AI C1** : Une divergence entre le prix de GC/HG/CL/ZW et le CCI est un signal d'alerte de retournement potentiel — à inclure comme critère dans la surveillance du moteur Python (Niveau 1).
*Catégorie : indicateurs_momentum*

### D7958 — Momentum : utile pour identifier fin de tendance et début de retournement
🟡 **SYNTHÈSE** (Source : momentum_as_indicator_in_futures_trading.md) : Incorporer des indicateurs de momentum dans le trading futures est un moyen d'analyser la force et la direction de la tendance actuelle, et de détecter quand la tendance pourrait se terminer ou s'inverser.
**TRADEX-AI C1** : Le moteur TRADEX doit lire le momentum (RSI, Stochastiques, CCI) non pas pour déclencher un signal seul, mais comme couche de confirmation de la méthode Belkhayate — momentum confirme, Belkhayate décide.
*Catégorie : indicateurs_momentum*

### D7959 — RSI : identification surachat/survente inter-instruments pour commodités futures
🔵 **ÉCOLE** (Source : momentum_as_indicator_in_futures_trading.md) : Le RSI permet de comparer la force relative de plusieurs marchés futures sur la même échelle. Utile pour identifier quel contrat commodité est le plus vulnérable à un retournement.
**TRADEX-AI C7** : Ajouter une couche RSI cross-marchés dans correlations.py — quand GC RSI > 70 et DX RSI < 30 simultanément, signal de divergence macro à signaler dans C4/C7.
*Catégorie : correlations*

### D7960 — Stochastiques en tendance : comportement asymétrique haussier/baissier
🟢 **FAIT VÉRIFIÉ** (Source : momentum_as_indicator_in_futures_trading.md) : En tendance baissière, les Stochastiques restent davantage en zone survente (< 20). En tendance haussière, elles restent davantage en zone surachat (> 80). Ce comportement asymétrique est caractéristique d'un marché tendanciel.
**TRADEX-AI C1** : Un Stochastique collé en zone extrême confirme la tendance Belkhayate — ne pas contre-trader un Stochastique > 80 dans une tendance haussière Belkhayate validée sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*
