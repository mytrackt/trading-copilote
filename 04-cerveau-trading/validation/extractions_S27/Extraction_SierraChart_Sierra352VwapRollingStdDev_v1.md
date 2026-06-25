# Extraction SierraChart — Volume Weighted Average Price (VWAP) - Rolling with Standard Deviation Lines
**Source :** `bundles/sierrachart/sierra_352_vwap_rolling_std_dev.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9231 → D9250 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=352
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : VWAP Rolling = niveau de juste valeur institutionnelle dynamique, utilisable comme confirmation C2/C3 pour identifier zones d'équilibre et déséquilibre sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9231 — Définition VWAP Rolling Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Le VWAP Rolling calcule le prix moyen pondéré par le volume sur une période de temps spécifiée, de manière continue (rolling). Pour chaque bar, la fenêtre de calcul recule dans le temps du même nombre de périodes — contrairement au VWAP standard qui repart de zéro à chaque segment de temps.
**TRADEX-AI C2** : Le VWAP Rolling constitue un niveau de juste valeur dynamique — un prix au-dessus du VWAP Rolling est potentiellement surévalué (vendeurs en position de force), en dessous sous-évalué (acheteurs). Applicable à GC, CL, HG, ZW comme niveau de référence institutionnel.
*Catégorie : structure_marche*

### D9232 — Différence fondamentale VWAP Rolling vs VWAP Standard
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Le VWAP Standard segmente le temps total par période définie et repart à zéro à chaque nouveau segment (ex: chaque jour). Le VWAP Rolling calcule sur une fenêtre glissante bar par bar sans reset — la fenêtre se déplace continuellement. Les valeurs calculées seront différentes entre les deux versions.
**TRADEX-AI C2** : Pour TRADEX-AI, le choix entre VWAP standard (reset journalier = vision intraday) et VWAP Rolling (fenêtre glissante = vision multi-sessions) dépend du contexte — le VWAP Rolling est plus adapté pour les analyses multi-jours sur GC ou CL.
*Catégorie : structure_marche*

### D9233 — Input Data : types de prix valides
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Pour cet indicateur, les seuls types d'Input Data valides sont Open, High, Low, Last/Close. Les volumes ne peuvent pas être utilisés comme Input Data.
**TRADEX-AI C2** : Utiliser Last/Close par défaut — cohérent avec la méthode Belkhayate. Le High ou Low peut être utilisé pour calculer des VWAP de bande haute/basse si nécessaire.
*Catégorie : indicateurs_tendance*

### D9234 — Input Volume Type : Total, Bid ou Ask Volume
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : L'input Volume Type détermine le type de volume utilisé dans le calcul : Total Volume (défaut), Bid Volume, ou Ask Volume. Quand Bid Volume ou Ask Volume est sélectionné, l'option Base on Underlying Data doit être à Yes, sinon le calcul se base sur le Total Volume.
**TRADEX-AI C2** : La possibilité d'utiliser Ask Volume ou Bid Volume pour pondérer le VWAP permet de créer un VWAP biaisé acheteur (Ask) ou vendeur (Bid) — outil avancé pour détecter déséquilibres institutionnels sur GC/CL intraday.
*Catégorie : volume_liquidite*

### D9235 — Input Base on Underlying Data : données sous-jacentes détaillées
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Quand Base on Underlying Data est à Yes, les calculs utilisent les données de prix et volume sous-jacentes plus détaillées que les bars du graphique. Une configuration Tick by Tick Data est recommandée. Le graphique peut être rechargé automatiquement pour charger les données Volume at Price détaillées. S'applique uniquement aux graphiques Intraday.
**TRADEX-AI C2** : Même contrainte que le CDB (D9194) — le VWAP Rolling le plus précis requiert des données tick by tick via Rithmic. Pour TRADEX-AI, activer Base on Underlying Data = Yes avec validation staleness_monitor sur la disponibilité tick.
*Catégorie : gestion_risque_entree*

### D9236 — Time Period Type : 4 modes de fenêtre temporelle
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : 4 modes disponibles : (1) Days - Trading Days : rolling jour par jour (pas bar par bar), inclut les N jours de trading précédents ; (2) Days - 24 Hour Period : rolling bar par bar sur N périodes de 24h ; (3) Minutes : rolling bar par bar sur N minutes ; (4) Bars : rolling sur N bars.
**TRADEX-AI C2** : Pour TRADEX-AI intraday sur futures (GC/CL range bars) : utiliser Bars ou Minutes pour un VWAP Rolling bar par bar fluide. Days - Trading Days = préférable pour les analyses multi-sessions (confirmation C3 institutionnels).
*Catégorie : indicateurs_tendance*

### D9237 — Days - Trading Days : comportement spécifique
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Avec Days - Trading Days, la fenêtre de calcul change jour par jour (pas bar par bar). Exemple avec Length=3 : pour tout bar d'un jour donné, le VWAP inclut ce jour + les 2 jours de trading précédents. Lors du changement de jour, un saut visible dans la valeur VWAP peut apparaître car le jour le plus ancien sort de la fenêtre.
**TRADEX-AI C2** : Le saut visible à chaque début de jour en mode Days - Trading Days est un comportement attendu, non un bug — à documenter pour Abdelkrim afin d'éviter des faux signaux interprétés comme des gaps de prix.
*Catégorie : indicateurs_tendance*

### D9238 — Time Period Length et Number of Days to Calculate
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Time Period Length fixe la durée de la fenêtre rolling (ex: 1 pour 1 jour). Number of Days to Calculate (défaut=10) fixe le nombre de jours historiques sur lesquels les calculs sont effectués — distinct de Time Period Length. Recommandation Sierra : régler Number of Days to Calculate à au moins 2x Time Period Length pour garantir des données suffisantes.
**TRADEX-AI C2** : Règle opérationnelle : Number of Days to Calculate ≥ 2 × Time Period Length. Pour un VWAP Rolling 3 jours, régler Number of Days to Calculate ≥ 6. Cette règle évite les résultats VWAP incorrects en début de période de calcul.
*Catégorie : gestion_risque_entree*

### D9239 — Bandes d'écart-type : jusqu'à 4 bandes configurables
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : L'indicateur supporte jusqu'à 4 bandes d'écart-type au-dessus et en dessous du VWAP (Top Band 1-4 et Bottom Band 1-4). Pour afficher une bande, régler son Draw Style à Dash dans l'onglet Subgraphs. Pour la masquer, régler sur Ignore.
**TRADEX-AI C2** : Les bandes VWAP ±1σ et ±2σ sont des niveaux de support/résistance dynamiques institutionnels — comparables aux bandes de Bollinger mais pondérées par le volume. Sur GC, le retour au VWAP depuis ±2σ est un signal de mean-reversion à fort R/R.
*Catégorie : structure_marche*

### D9240 — Standard Deviation Band Calculation Method : 4 méthodes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : 4 méthodes de calcul des bandes disponibles via Standard Deviation Band Calculation Method : VWAP Variance, Fixed Offset, Standard Deviation, Percentage.
**TRADEX-AI C2** : Méthode recommandée pour TRADEX-AI : Standard Deviation ou VWAP Variance — ces deux méthodes s'adaptent dynamiquement à la volatilité du marché. Fixed Offset et Percentage sont statiques et moins adaptés aux marchés de futures volatils (GC, CL).
*Catégorie : indicateurs_tendance*

### D9241 — Multiplicateur des bandes : Band # Std. Deviation Multiplier
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : L'input Band # Std. Deviation Multiplier/Fixed Offset contrôle l'écartement des bandes. En mode VWAP Variance ou Standard Deviation : la bande est décalée de (multiplicateur × écart-type). Exemple : valeur 2.0 = bande à ±2 écarts-types du VWAP. En mode Fixed Offset : offset fixe en points. En mode Percentage : offset en % du VWAP.
**TRADEX-AI C2** : Configuration standard pour TRADEX-AI : Band 1 = 1.0σ (zone d'équilibre), Band 2 = 2.0σ (zone d'extension), Band 3 = 3.0σ (zone extrême — signal de retournement fort). Ces seuils sont les niveaux institutionnels de référence pour le VWAP trading.
*Catégorie : gestion_risque_entree*

### D9242 — Exclude Weekends in Date Look Back
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Quand Exclude Weekends in Date Look Back est à Yes, les samedis et dimanches sont ignorés dans le comptage des jours pour Time Period Length. S'applique pour les modes Days - Trading Days et Days - 24 Hour Period. Attention : pour les fuseaux horaires d'Extrême-Orient où le samedi peut être un jour de trading, mettre à No.
**TRADEX-AI C2** : Pour les futures US (GC, CL, HG, ZW) en timezone ET, régler Exclude Weekends = Yes — les weekends sont sans trading actif significatif. Exception possible pour GC qui peut avoir du volume Sunday evening (ouverture session asiatique).
*Catégorie : indicateurs_tendance*

### D9243 — Minimum Required Time Period as Percent for Skip Days
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Cet input contrôle la logique de gestion des jours à données insuffisantes (jours fériés, trading dominical). Si les données d'un jour représentent moins que ce pourcentage du nombre de bars requis pour une période, ce jour est ignoré et le calcul remonte plus loin. Recommandation Sierra : ne pas mettre 100 (déclenche des sauts inutiles) ; adapter à la proportion de session réellement disponible dans le graphique.
**TRADEX-AI C2** : Pour TRADEX-AI avec sessions partielles (day session only sur NT8), régler ce paramètre entre 30% et 50% pour éviter les sauts de calcul sur les jours fériés US (Thanksgiving, Noël) qui impactent GC/CL/ZW. À documenter dans settings.py.
*Catégorie : gestion_risque_entree*

### D9244 — Start Date-Time : démarrage optionnel des calculs
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : L'input Start Date-Time permet de définir optionnellement une date et heure de début pour les calculs VWAP. Pour désactiver cet input, régler une date antérieure au premier bar du graphique.
**TRADEX-AI C2** : Utile pour aligner le début du VWAP Rolling sur un événement majeur (ex: début d'une tendance post-NFP, début d'une semaine de trading) — permet à Abdelkrim d'ancrer le VWAP sur un point de référence spécifique pour les analyses Belkhayate.
*Catégorie : timing*

### D9245 — VWAP Rolling comme niveau institutionnel de référence
🔵 **ÉCOLE** (Source : sierra_352_vwap_rolling_std_dev.md) : Le VWAP est le niveau de prix auquel les institutions ont échangé en moyenne sur la période. Un prix au-dessus du VWAP signifie que les acheteurs ont eu le dessus en moyenne ; en dessous, les vendeurs. Le retour au VWAP est souvent un objectif de mean-reversion pour les market-makers.
**TRADEX-AI C2/C3** : Dans la grille TRADEX-AI, le VWAP Rolling sert de niveau institutionnel C3 — un signal Belkhayate confirmé par une position au-dessus du VWAP Rolling (pour un achat) ou en dessous (pour une vente) renforce le score. Constitue une convergence C2+C3 si le volume confirme.
*Catégorie : structure_marche*

### D9246 — Zones VWAP ±2σ comme zones de surachat/survente
🔵 **ÉCOLE** (Source : sierra_352_vwap_rolling_std_dev.md) : Les bandes à ±2 écarts-types du VWAP délimitent statistiquement les zones où 95% des échanges se sont produits. Un prix en dehors de ces bandes indique une condition de sur-extension — retour probable vers le VWAP (mean reversion).
**TRADEX-AI C1/C2** : Signal de mean-reversion haute probabilité pour TRADEX-AI : prix GC/CL en dehors de VWAP ±2σ + signal Belkhayate dans la direction du retour = configuration R/R favorable. Renforce le score grille vers 7+/10.
*Catégorie : configuration*

### D9247 — Recommandation paramétrage VWAP Rolling TRADEX-AI intraday
🟡 **SYNTHÈSE** (Source : sierra_352_vwap_rolling_std_dev.md) : Configuration recommandée pour TRADEX-AI intraday futures : Time Period Type = Days - Trading Days, Time Period Length = 1 (VWAP de la session courante comme niveau de base) ou 3 (VWAP 3 jours pour confirmation multi-sessions). Number of Days to Calculate = 2× Length. Bandes : ±1σ et ±2σ en mode Standard Deviation. Base on Underlying Data = Yes avec tick data Rithmic.
**TRADEX-AI C2** : Ces paramètres constituent la configuration VWAP Rolling opérationnelle pour TRADEX-AI. Le VWAP 1-jour est le niveau de référence intraday ; le VWAP 3-jours est la référence de moyen terme pour la confirmation C3 institutionnelle sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D9248 — Interaction entre VWAP Rolling et niveaux Belkhayate
🟡 **SYNTHÈSE** (Source : sierra_352_vwap_rolling_std_dev.md) : Le VWAP Rolling fournit des niveaux de juste valeur dynamiques pondérés par le volume — complémentaires aux pivots Belkhayate (qui sont statiques et géométriques). Une confluence VWAP Rolling + pivot Belkhayate crée une zone de support/résistance à très haute probabilité.
**TRADEX-AI C1/C2** : Dans la grille /10, la confluence VWAP Rolling + pivot Belkhayate = double confirmation de niveau. Si le prix revient sur un pivot Belkhayate qui coïncide avec le VWAP Rolling ±1σ, la probabilité d'un rebond est significativement accrue — priorité dans l'analyse.
*Catégorie : structure_marche*

### D9249 — Différences de valeur entre timeframes pour VWAP et ses bandes
🟢 **FAIT VÉRIFIÉ** (Source : sierra_352_vwap_rolling_std_dev.md) : Les valeurs calculées pour le VWAP Rolling et ses bandes d'écart-type seront différentes selon le timeframe du graphique (1 min vs 5 min vs range bars). Cela est dû au fait qu'une période de temps rolling est utilisée sans reset à chaque segment.
**TRADEX-AI C2** : Pour la cohérence des signaux TRADEX-AI, le VWAP Rolling doit être calculé sur le même timeframe que celui utilisé pour les indicateurs Belkhayate (range bars NT8) — les valeurs sur range bars 100/200 ticks seront différentes des valeurs sur bars temporels standards.
*Catégorie : indicateurs_tendance*

### D9250 — Calcul de l'écart-type : pondération par le volume
🔵 **ÉCOLE** (Source : sierra_352_vwap_rolling_std_dev.md) : Le calcul de l'écart-type pour les bandes VWAP est basé sur la différence pondérée par le volume entre le prix sélectionné (Input Data) et la valeur VWAP. Cette pondération volumique différencie les bandes VWAP des bandes de Bollinger classiques (non pondérées par le volume).
**TRADEX-AI C2** : La pondération volumique des bandes VWAP les rend plus robustes que les bandes de Bollinger pour les futures — les zones haute volume (footprint ATAS) concentrent les bandes, rendant les extremes à ±2σ statistiquement plus significatifs sur GC/CL.
*Catégorie : structure_marche*
