# Extraction NinjaTrader — Identify Chart Patterns on Futures Trading Charts
**Source :** `bundles/ninjatrader/identify_chart_patterns_on_futures_trading_charts.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7871 → D7890 · **Page :** https://ninjatrader.com/learn/technical-analysis/identify-chart-patterns-on-futures-trading-charts/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : 8 patterns de retournement et continuation utilisables pour confirmer les signaux Belkhayate sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

## DÉCISIONS

### D7871 — Inside Bar : définition et usage
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Un inside bar se forme quand le high et le low de la barre courante sont entièrement englobés par le range (wicks compris) de la barre précédente ; il signale un possible changement de direction à court terme.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un inside bar après un signal Belkhayate renforce la probabilité de retournement ; les extrêmes de la barre englobante servent de niveaux de breakout pour l'entrée.
*Catégorie : configuration*

### D7872 — Outside Bar : définition et usage
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Un outside bar se forme quand la barre courante englobe entièrement le high et le low de la barre précédente ; les extrêmes de la barre englobante constituent les niveaux de breakout.
**TRADEX-AI C1** : L'outside bar valide une expansion de range ; en conjonction avec les cercles C1 et C2, il confirme la pression directionnelle avant entrée sur les actifs TRADING.
*Catégorie : configuration*

### D7873 — Key Reversal Up : pattern deux barres haussier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Key reversal up = barre courante fait un plus bas significatif sous les barres précédentes puis clôture au-dessus de la clôture de la barre précédente ; apparaît idéalement au bas d'un downtrend.
**TRADEX-AI C1** : Confirmation d'un signal ACHETER Belkhayate : si la barre de signal forme un key reversal up au bas d'un cycle baissier, la probabilité de suivi haussier augmente significativement.
*Catégorie : configuration*

### D7874 — Key Reversal Down : pattern deux barres baissier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Key reversal down = barre courante fait un plus haut significatif au-dessus des barres précédentes puis clôture sous la clôture de la barre précédente ; apparaît idéalement au sommet d'un uptrend.
**TRADEX-AI C1** : Confirmation d'un signal VENDRE Belkhayate : si la barre de signal forme un key reversal down au sommet d'un cycle haussier, la probabilité de suivi baissier est renforcée.
*Catégorie : configuration*

### D7875 — Opening Gap : exhaustion vs continuation
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Gap d'épuisement = le gap comble la pression accumulée et le prix revient combler le gap. Gap de continuation/breakaway = le prix continue dans la direction du gap après une phase de consolidation.
**TRADEX-AI C1/C4** : Les gaps d'ouverture sur GC et CL surviennent souvent après des événements macro (NFP/FOMC/CPI) ; le News Gate doit bloquer les signaux pendant 30 min autour de ces ouvertures de session.
*Catégorie : macro_evenements*

### D7876 — Double Top : pattern de retournement baissier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Double top = pattern de retournement baissier formé après un uptrend ; deux sommets à niveau similaire suivis d'un breakdown ; la distance entre les sommets aide à définir l'objectif de prix.
**TRADEX-AI C1** : Sur GC, un double top aux niveaux pivots Belkhayate valide un signal VENDRE ; la distance entre les sommets définit l'objectif de prix pour le R/R (doit rester ≥ 1:2).
*Catégorie : configuration*

### D7877 — Double Bottom : pattern de retournement haussier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Double bottom = pattern de retournement haussier formé après un downtrend ; deux creux à niveau similaire suivis d'un breakout ; la distance entre les creux définit l'objectif de prix.
**TRADEX-AI C1** : Sur ZW/HG, un double bottom aux niveaux support Belkhayate confirme un signal ACHETER ; ampleur du pattern = base du calcul objectif pour satisfaire R/R ≥ 1:2.
*Catégorie : configuration*

### D7878 — V Top / V Bottom : retournement en V
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : V top (swing high) = pic aigu suivi d'un retournement rapide à la baisse ; V bottom (swing low) = creux aigu suivi d'un retournement rapide à la hausse. Règle : au moins 3 barres avant le high/low + 3 barres de confirmation de retournement.
**TRADEX-AI C1** : Le pattern en V est le signal le plus rapide mais le plus tardif ; dans TRADEX-AI, la confirmation de 3 barres de retournement post-V est requise avant tout signal pour limiter les faux positifs.
*Catégorie : configuration*

### D7879 — Broadening Top/Bottom (Megaphone) : indécision croissante
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Pattern mégaphone = volatilité croissante avec highs de plus en plus hauts et lows de plus en plus bas ; signale l'indécision entre acheteurs et vendeurs, souvent aux tops/bottoms de tendance. Les lignes de délimitation agissent comme support/résistance projetée.
**TRADEX-AI C1/C5** : Un mégaphone actif sur GC indique un régime de haute incertitude ; croiser avec C5 (VIX élevé) ; si VIX > seuil critique, suspendre le mode Auto conformément à la règle G11.
*Catégorie : structure_marche*

### D7880 — Triangle Symétrique : consolidation avant breakout indéfini
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Triangle symétrique = deux trendlines convergentes de pentes similaires ; signale une consolidation avant breakout haussier ou baissier.
**TRADEX-AI C1** : TRADEX-AI doit attendre la confirmation du breakout directionnel avant de scorer le signal ; l'entrée dans un triangle symétrique actif n'est pas éligible (score C1 insuffisant).
*Catégorie : configuration*

### D7881 — Triangle Ascendant : biais haussier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Triangle ascendant = trendline haute plate + trendline basse ascendante ; formation généralement haussière avec attente d'un breakout vers le haut.
**TRADEX-AI C1** : Sur CL/GC, un triangle ascendant renforce le score C1 d'un signal ACHETER Belkhayate ; le breakout de la résistance plate déclenche l'activation du signal.
*Catégorie : indicateurs_tendance*

### D7882 — Triangle Descendant : biais baissier
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Triangle descendant = trendline haute descendante + trendline basse plate ; formation généralement baissière avec attente d'un breakout vers le bas.
**TRADEX-AI C1** : Sur CL/GC, un triangle descendant renforce le score C1 d'un signal VENDRE ; le breakdown de la résistance plate valide l'entrée short.
*Catégorie : indicateurs_tendance*

### D7883 — Flag : continuation après fort mouvement
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Flag = consolidation en rectangle/parallélogramme légèrement opposé à la tendance, précédée d'un fort mouvement directionnel (mât). Le breakout de la consolidation reprend la direction initiale. Objectif de prix = hauteur du mât projetée depuis le breakout.
**TRADEX-AI C1** : Sur GC/CL, un flag en cours de formation après un fort mouvement Belkhayate est un contexte favorable ; l'objectif du mât sert de base pour valider le R/R ≥ 1:2 requis.
*Catégorie : configuration*

### D7884 — Combinaison de patterns avec indicateurs
🟡 **SYNTHÈSE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Les patterns de prix sont plus efficaces lorsqu'ils sont combinés avec des indicateurs de momentum, de volatilité et de volume pour identifier des opportunités de trading.
**TRADEX-AI C1/C2** : Dans TRADEX-AI, les patterns de structure (C1) doivent être confirmés par C2 (order flow : delta, footprint) avant de contribuer au score final /10.
*Catégorie : configuration*

### D7885 — Variation des patterns : jugement requis
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Tous les patterns ne correspondent pas exactement à leur description théorique ; les traders doivent exercer leur jugement et accepter les variations.
**TRADEX-AI C1** : Le cerveau Claude analysant les patterns doit signaler le degré de conformité du pattern dans le champ "confiance" du signal ; une variation significative réduit le score C1.
*Catégorie : psychologie*

### D7886 — Niveau de breakout des inside/outside bars
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Pour inside bar et outside bar, les extrêmes (high/low) de la barre englobante constituent généralement les niveaux de breakout pour les deux patterns.
**TRADEX-AI C1** : Utilisation directe dans le calcul du stop loss : le stop se place juste au-delà de l'extrême opposé de la barre englobante pour les entrées sur inside/outside bar.
*Catégorie : gestion_risque_entree*

### D7887 — Pattern fort = top uptrend / bottom downtrend
🟢 **FAIT VÉRIFIÉ** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Les patterns de retournement les plus forts se forment au sommet d'un uptrend ou au bas d'un downtrend, augmentant la probabilité et le potentiel de suivi directionnel.
**TRADEX-AI C1** : Règle de filtrage : un signal de retournement Belkhayate obtient un score C1 plus élevé si le pattern se forme à une extrémité de tendance confirmée (BGC, Direction NT8).
*Catégorie : configuration*

### D7888 — Gap et imbalance d'ordres à l'ouverture
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Les gaps d'ouverture résultent d'un déséquilibre d'ordres à l'ouverture de session, souvent causé par des news, un volume élevé ou une forte volatilité après la clôture de la session précédente.
**TRADEX-AI C2/C4** : Un gap d'ouverture sur un actif TRADING (GC/CL) indique un déséquilibre institutionnel à surveiller en C2 (order flow) ; croiser avec le News Gate pour vérifier la cause macro.
*Catégorie : macro_evenements*

### D7889 — Inside/Outside bars : usage sur daily/weekly
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Inside bars et outside bars sont typiquement identifiés sur des barres OHLC ou chandeliers journaliers ou hebdomadaires.
**TRADEX-AI C1** : Dans TRADEX-AI, ces patterns sur timeframe daily servent de filtre de contexte pour les entrées intraday sur range bars NT8 ; un inside bar daily = réduction de la taille de position.
*Catégorie : gestion_risque_entree*

### D7890 — Objectif de prix par projection du mât (flag)
🔵 **ÉCOLE** (Source : identify_chart_patterns_on_futures_trading_charts.md) : Pour les flags, l'objectif de prix est communément fixé en projetant la hauteur du mât depuis le point de breakout de la consolidation.
**TRADEX-AI C1** : Méthode de calcul de take profit applicable sur GC/CL/ZW : hauteur du mât = objectif minimum ; vérifier que R/R ≥ 1:2 est satisfait avant de valider le signal.
*Catégorie : gestion_position_active*
