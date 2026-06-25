# Extraction StockCharts — Trend Quantification and Asset Allocation
**Source :** `bundles/stockcharts/trend_quantification_and_asset_allocation.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D4591 → D4610 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/trend-quantification-and-asset-allocation
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Quantification de la force de tendance sur GC/HG/CL/ZW via PPO multi-EMA et système d'allocation graduelle — approche systématique de scoring de tendance alignée avec la grille /10 TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/El0jW7MwuexhuGpLujwm | Long-term exponential moving averages applied to price chart (SPY) | Moving Averages | D4591 |
| /files/wekubX7BXX2eH3QbUpYy | Smoothing price data with exponential moving averages (DIA 50-day EMA) | Smoothing the Closing Price | D4593 |
| /files/s2JkCKveyI1YccRz9d8L | Four PPO versions comparing EMA(50) to longer-term EMAs | Using the PPO | D4595 |
| /files/nwh2pxvYbSfW38kQhbRB | PPO with fixed long-term EMA (150) and variable shorter EMAs | Fixing the Long-term EMA | D4596 |
| /files/jXCwzTKjsiC8vn6soBnj | PPO indicator for asset allocation (4 tranches) | Asset Allocation | D4597 |
| /files/rVbsL7SIsOsBe8oU0krP | Slope indicator (50, 75, 100, 125-day) as Trend Composite | Indicator Tweaks | D4599 |

## DÉCISIONS

### D4591 — Les retournements long terme sont des processus, pas des événements soudains
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_El0jW7MwuexhuGpLujwm) : Les retournements de tendance long terme sont souvent des processus, pas des événements soudains. La tendance long terme est comme un super-tanker qui nécessite du temps pour changer de direction. Les chartistes doivent considérer plus d'un timeframe long terme pour définir le trend long terme.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un retournement de tendance confirmé par plusieurs EMAs (125/150/175/200 jours) est plus fiable qu'un signal isolé — TRADEX doit attendre la convergence multi-EMA avant de scorer un retournement.
*Catégorie : indicateurs_tendance*

### D4592 — Les MAs seules produisent des faux signaux — utiliser plusieurs EMAs
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_El0jW7MwuexhuGpLujwm) : Les moyennes mobiles ont un décalage mais restent les indicateurs les plus populaires pour l'identification de tendance. Cependant, la tendance ne se renverse pas toujours quand les prix passent au-dessus ou en dessous d'une MA spécifique. Le SPY a cassé au-dessus de ses EMAs fin 2007 et début 2008 sans retournement réel — le trend a continué à la baisse.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une seule EMA croisée ne constitue pas un signal valide — TRADEX requiert la convergence de plusieurs EMAs (ou d'autres indicateurs) pour confirmer le changement de tendance dans la grille /10.
*Catégorie : indicateurs_tendance*

### D4593 — Lisser les données de prix réduit les whipsaws
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_wekubX7BXX2eH3QbUpYy) : Les données de prix quotidiennes peuvent être volatiles, rendant les cassures de MA sujettes aux faux signaux. Lisser les données de prix avec une EMA50 (puis appliquer les EMAs long terme à cette EMA50 lissée) augmente le lag mais réduit le nombre de whipsaws. Cette méthode fait une meilleure identification de tendance.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, appliquer les indicateurs de tendance sur une version lissée des prix (EMA50) plutôt que sur les prix bruts réduit les faux signaux en période de volatilité (ex : publications NFP/FOMC).
*Catégorie : indicateurs_tendance*

### D4594 — PPO (Percentage Price Oscillator) pour identifier les croisements de MA
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md) : Le PPO (50,200,1) mesure la différence en pourcentage entre la EMA50 et la EMA200. PPO positif = EMA courte > EMA longue. PPO négatif = EMA courte < EMA longue. Cet indicateur facilite l'identification des croisements de moyennes mobiles.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, le PPO(50,200) constitue une mesure quantifiée du signal Golden/Death Cross — plus facile à intégrer dans un système de scoring automatique que l'observation visuelle des croisements.
*Catégorie : indicateurs_tendance*

### D4595 — Système de 4 PPOs pour quantifier la force de tendance
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_s2JkCKveyI1YccRz9d8L) : 4 versions du PPO comparant l'EMA50 à des EMAs plus longues. Quand les 4 PPOs sont positifs → tendance forte et haussière. La tendance s'affaiblit progressivement quand les PPOs deviennent négatifs. Elle devient pleinement baissière quand les 4 sont négatifs. Les retournements de tendance sont un processus et prennent généralement quelques semaines.
**TRADEX-AI C1** : Ce concept de "score sur 4" est directement applicable à la grille TRADEX /10 — sur GC/HG/CL/ZW, compter combien de PPOs (ou d'EMAs) sont positifs donne une mesure quantifiée de la force de tendance.
*Catégorie : indicateurs_tendance*

### D4596 — EMA longue fixe avec EMAs courtes variables : approche alternative
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_nwh2pxvYbSfW38kQhbRB) : Alternative : fixer l'EMA long terme (ex : 150 jours) et rendre les EMAs plus courtes variables (20, 40, 60, 80 jours). PPO(20,150) le plus sensible et premier à changer. PPO(80,150) le moins sensible et dernier à changer. Tendance pleinement haussière quand les 4 PPOs sont positifs, pleinement baissière quand les 4 sont négatifs.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, utiliser une EMA fixe longue (150 ou 200 jours) comme référence stable et comparer plusieurs EMAs courtes (20/40/60/80) permet de construire un score de force tendancielle graduel.
*Catégorie : indicateurs_tendance*

### D4597 — Allocation d'actifs graduelle basée sur le score de PPO
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_jXCwzTKjsiC8vn6soBnj) : Stratégie d'allocation basée sur les 4 PPOs : chaque PPO représente 1/4 du trend et 1/4 de l'allocation. Quand 1 PPO positif → investir 25%. Quand 2 PPOs positifs → investir 50%. Etc. Investissement 100% quand les 4 sont positifs. Réduction progressive de 25% à chaque PPO qui passe négatif. Sorti du marché quand les 4 sont négatifs.
**TRADEX-AI C1** : Ce modèle d'exposition graduelle sur 4 niveaux est directement applicable à la gestion de position TRADEX — sur GC/HG/CL/ZW, la taille de la position peut être modulée selon le nombre d'indicateurs de tendance alignés.
*Catégorie : gestion_position_active*

### D4598 — Réduction progressive d'exposition quand les PPOs deviennent négatifs
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md) : Un investisseur peut réduire les positions longues de 25% quand le premier PPO passe négatif. L'exposition au marché est réduite progressivement au fur et à mesure que les autres PPOs deviennent négatifs — sorti du marché quand les 4 sont négatifs.
**TRADEX-AI C1** : En mode Auto TRADEX, ce mécanisme de réduction graduelle peut s'appliquer sur GC/HG/CL/ZW : chaque PPO/EMA passant en territoire négatif déclenche une réduction de 25% de la taille de position — protège contre les retournements progressifs.
*Catégorie : gestion_position_active*

### D4599 — Indicateur de pente (slope) comme alternative aux PPOs
🟢 **FAIT VÉRIFIÉ** (Source : trend_quantification_and_asset_allocation.md, image_rVbsL7SIsOsBe8oU0krP) : D'autres indicateurs peuvent aider à définir la tendance et déterminer l'allocation — ex : l'indicateur de pente (slope). 4 versions : 50, 75, 100, 125 jours. Tendance haussière quand la pente est positive, baissière quand négative. La force dépend du nombre de slope indicators positifs. Uptrend fort = 4 positifs, downtrend fort = 4 négatifs.
**TRADEX-AI C1** : L'indicateur de pente (slope) sur plusieurs périodes (50/75/100/125) sur GC/HG/CL/ZW constitue une alternative aux PPOs pour quantifier la force de tendance — s'intègre dans la grille /10 comme mesure C1.
*Catégorie : indicateurs_tendance*

### D4600 — Identification de tendance = point de départ de nombreuses stratégies
🟡 **SYNTHÈSE** (Source : trend_quantification_and_asset_allocation.md) : L'identification de tendance est souvent le point de départ de nombreuses stratégies de trading et d'investissement. Les investisseurs relativement passifs peuvent utiliser une stratégie de suivi de tendance long terme pour définir le trend et allouer les fonds en conséquence. Les traders actifs peuvent utiliser ces indicateurs pour définir le trend long terme puis chercher des trades dans la direction de ce trend.
**TRADEX-AI C1** : Dans TRADEX, la définition claire de la tendance long terme (bullish/bearish) sur GC/HG/CL/ZW via EMAs multiples est le filtre primaire de la grille /10 — seuls les signaux dans la direction du trend long terme sont considérés.
*Catégorie : indicateurs_tendance*

### D4601 — Paramètres ajustables selon le style de trading et les préférences de R/R
🔵 **ÉCOLE** (Source : trend_quantification_and_asset_allocation.md) : Les paramètres présentés (EMAs longues, PPOs) peuvent être ajustés selon le style de trading/investissement. Cet article est conçu comme un point de départ pour le développement de systèmes de trading — ces idées doivent être augmentées par le style, les préférences de risque/récompense et les jugements personnels du trader.
**TRADEX-AI C1** : Sur TRADEX, les paramètres EMAs utilisés pour le scoring de tendance sur GC/HG/CL/ZW doivent être calibrés sur les range bars NT8 (timeframe Belkhayate) — non pas sur les jours calendaires des exemples StockCharts.
*Catégorie : indicateurs_tendance*

### D4602 — Scans systématiques pour identifier les tendances long terme
🔵 **ÉCOLE** (Source : trend_quantification_and_asset_allocation.md) : Scan downtrend long terme : EMA(20,close) > EMA(150,close) ET EMA(40,close) > EMA(150,close) ET EMA(60,close) > EMA(150,close) ET EMA(80,close) > EMA(150,close). Scan uptrend long terme : toutes les EMAs courtes < EMA(150). Ces scans automatisés permettent de filtrer systématiquement les actifs selon leur tendance.
**TRADEX-AI C1** : Ces conditions de scan (4 EMAs courtes vs EMA150) peuvent être intégrées dans le moteur Python TRADEX comme filtre de contexte sur GC/HG/CL/ZW — à évaluer toutes les 2 secondes pour le monitoring de tendance.
*Catégorie : indicateurs_tendance*
