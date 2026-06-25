# Extraction Optimus — Average True Range Indicator
**Source :** `bundles/optimusfutures/average_true_range_indicator.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption locale · 0/0 certifiées · 3 décoratives ignorées
**Décisions :** D8251 → D8270 · **Page :** https://optimusfutures.com/blog/average-true-range-indicator/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : ATR = mesure de volatilité utilisable pour calibrer stop-loss et profit targets sur GC/HG/CL/ZW en mode C2/C1.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune image certifiée — 3 décoratives ignorées)*

## DÉCISIONS

### D8251 — Définition ATR : plus grande valeur parmi 3 calculs
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : L'ATR (Average True Range) mesure le True Range = max(High-Low, |High-ClosePrev|, |Low-ClosePrev|). La valeur ATR standard est la moyenne sur 14 périodes.
**TRADEX-AI C1** : Pour calibrer les stops/targets sur GC, HG, CL, ZW, utiliser l'ATR 14 périodes comme référence de volatilité intrinsèque du marché sur la timeframe active.
*Catégorie : gestion_risque_entree*

### D8252 — ATR ne fournit pas de signal directionnel
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : L'ATR ne génère pas de signal d'achat ou de vente. Il mesure uniquement l'amplitude des mouvements, pas leur direction.
**TRADEX-AI C1** : Dans TRADEX-AI, l'ATR est un outil de sizing (calibrage) et non un signal d'entrée. Ne jamais utiliser ATR seul comme déclencheur — toujours associé aux signaux Belkhayate (BGC, Direction, Énergie, Pivots).
*Catégorie : indicateurs_tendance*

### D8253 — ATR faible = contraction précédant une explosion de volatilité
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : Quand l'ATR descend à des niveaux extrêmement bas, un mouvement explosif dans un sens ou l'autre est probable. Exemple ES Futures : ATR bas dans deux boîtes bleues → mouvement violent à la baisse suivi.
**TRADEX-AI C1** : Surveiller les compressions ATR sur GC/CL comme signal préparatoire — une faible volatilité sur plusieurs barres précède souvent un breakout Belkhayate à haute énergie. Intégrer dans le filtre C1 (Énergie).
*Catégorie : structure_marche*

### D8254 — Stop-loss long = prix entrée − (ATR × multiplicateur)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : Pour une position longue, stop = prix_entrée − (ATR × N). Pour une position courte, stop = prix_entrée + (ATR × N). Multiplicateur typique : 1x à 3x selon tolérance au risque et volatilité du marché.
**TRADEX-AI C1/gestion_risque** : Sur GC/HG/CL/ZW, appliquer stop = entrée ± (ATR14 × 2) par défaut. Ajuster le multiplicateur si VIX (C5) est élevé : passer à 2.5x ou 3x en période de forte volatilité.
*Catégorie : gestion_risque_entree*

### D8255 — Trailing stop ATR : ajuster le stop au fur et à mesure que l'ATR décline
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : Exemple YM Futures : entrée breakout 34000, ATR = 423 pts → stop initial à 33577. Au fur et à mesure que l'ATR décline (de 423 à 300), le trailing stop suit la baisse d'ATR pour protéger les profits.
**TRADEX-AI C1** : En mode Manuel, afficher l'ATR courant dans le dashboard pour permettre à Abdelkrim d'ajuster manuellement le trailing stop lors de la compression de volatilité post-entrée. En mode Auto, implémenter trailing = entrée + (ATR_courant × 2) recalculé toutes les 2s.
*Catégorie : gestion_position_active*

### D8256 — Profit target = prix entrée + (ATR × N) combiné à la structure marché
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : Le target ATR se calcule : target1 = entrée + ATR, target2 = entrée + (ATR × 2). Ces niveaux doivent rester EN DESSOUS des résistances de structure identifiées. Si résistances à +100, +250, +400 pts et ATR = 300, choisir +250 (sous ATR journalier mais avec résistance réelle).
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, calculer T1 = entrée + ATR14 et T2 = entrée + (ATR14 × 2). Croiser avec les pivots Belkhayate (R1/R2) pour sélectionner le target le plus conservateur. Privilégier T1 si R/R ≥ 1:2, T2 si R/R ≥ 1:3.
*Catégorie : gestion_position_active*

### D8257 — ATR croissant + tendance haussière = possible fin de tendance
🟡 **SYNTHÈSE** (Source : average_true_range_indicator.md) : Si ATR monte PENDANT une tendance haussière, la volatilité croissante peut signaler la FIN imminente de cette tendance (épuisement). Inversement, ATR décroissant en tendance baissière peut signaler une stabilisation et rebond potentiel.
**TRADEX-AI C1** : Intégrer ce filtre dans le score Belkhayate : si ATR > ATR_MA20 × 1.5 en milieu de tendance → réduire la confiance du signal de 10% (signal d'épuisement potentiel).
*Catégorie : indicateurs_tendance*

### D8258 — ATR comme filtre de confirmation pour signaux RSI/Stochastique
🟡 **SYNTHÈSE** (Source : average_true_range_indicator.md) : Un signal oversold RSI + ATR faible = moins fiable (marché pas vraiment en mouvement). Un signal RSI + ATR en hausse = plus fiable (volatilité confirme l'impulsion). ATR faible peut fausser les lectures momentum.
**TRADEX-AI C1/C2** : Dans la grille /10 TRADEX, pondérer les signaux momentum (RSI, Stochastique, MFI) par le niveau ATR relatif. ATR < 50% de sa moyenne 20 périodes → baisser la pondération du signal momentum d'un cran.
*Catégorie : indicateurs_momentum*

### D8259 — ATR + niveaux support/résistance : attendre hausse ATR avant d'agir
🟡 **SYNTHÈSE** (Source : average_true_range_indicator.md) : Si le prix approche un niveau S/R clé, attendre que l'ATR commence à monter avant d'entrer confirme que la volatilité augmente autour de ce niveau — confirmation d'intérêt accru du marché.
**TRADEX-AI C1** : Pour les niveaux pivot Belkhayate (S1/R1/S2/R2), condition supplémentaire de validation : ATR_courant > ATR_1_barre_avant. Cette montée de l'ATR valide l'intérêt du marché autour du pivot.
*Catégorie : configuration*

### D8260 — ATR + Parabolic SAR : combinaison direction + volatilité
🔵 **ÉCOLE** (Source : average_true_range_indicator.md) : Le Parabolic SAR (créé par le même auteur, Welles Wilder) indique la direction du marché. Combiné à l'ATR (volatilité), il offre une vision complète : direction + amplitude probable du mouvement.
**TRADEX-AI C1** : Indicateur de référence éducatif. Le Parabolic SAR peut être utilisé comme proxy de direction dans les phases d'absence de signal Belkhayate clair, mais il est inférieur au BGC (Belkhayate Gravity Center) en précision.
*Catégorie : indicateurs_tendance*

### D8261 — ATR est un indicateur retardé : ne pas l'utiliser seul pour prédire
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : L'ATR est un indicateur lagging — il reflète la volatilité passée. Ne jamais l'utiliser seul à des fins prédictives. Son rôle est de CONFIRMER d'autres signaux ou de GÉRER le risque selon la volatilité actuelle.
**TRADEX-AI C1** : Règle ferme dans TRADEX-AI : l'ATR ne déclenche aucun signal de niveau 3 (appel Claude). Son usage est limité au calibrage des stops/targets (niveau 1-2 Python, 0$).
*Catégorie : gestion_risque_entree*

### D8262 — Période ATR : plus courte = plus sensible, plus longue = plus lisse
🔵 **ÉCOLE** (Source : average_true_range_indicator.md) : La période standard est 14. Une période plus courte amplifie les variations d'ATR (plus adapté au scalping). Une période plus longue lisse les variations (plus adapté au swing trading).
**TRADEX-AI C1** : Sur les actifs TRADEX (GC/HG/CL/ZW), conserver ATR14 comme référence standard. Pour les signaux intraday à haute fréquence (range bars NT8), envisager ATR7 pour plus de réactivité — à valider en Phase C.
*Catégorie : indicateurs_tendance*

### D8263 — ATR + MACD : ATR pour sortie, MACD pour entrée
🟡 **SYNTHÈSE** (Source : average_true_range_indicator.md) : Le MACD identifie les entrées et changements de momentum. L'ATR complète en fournissant une stratégie de sortie basée sur la volatilité. Les deux se complètent dans l'identification des retournements/continuations.
**TRADEX-AI C1/C2** : Architecture recommandée TRADEX : MACD + BGC Belkhayate pour le signal d'entrée → ATR pour calibrer le stop et le target en sortie. Ne pas utiliser MACD comme signal primaire (inférieur à la méthode Belkhayate).
*Catégorie : configuration*

### D8264 — ATR position sizing : aligner la taille de position avec le risque ATR
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_indicator.md) : Le niveau de stop-loss ATR doit être aligné avec la stratégie globale de gestion du risque et la taille du compte. La taille de position doit être ajustée pour que le stop ATR corresponde au risque max accepté par trade (ex: 1-2% du capital).
**TRADEX-AI C1/gestion_risque** : Intégrer dans risk_manager.py : taille_position = (capital × risque_pct) / (ATR14 × multiplicateur_stop). Ce calcul automatique garantit que chaque trade respecte la règle de risque indépendamment de la volatilité du marché.
*Catégorie : gestion_risque_entree*

### D8265 — Bollinger Bands + ATR : contraction BB précède breakout, ATR confirme
🟡 **SYNTHÈSE** (Source : average_true_range_indicator.md) : L'ATR peut corroborer les signaux des Bollinger Bands. Dans le premier graphique (Chart 1), l'ATR se contractait pendant que le prix approchait d'une résistance BB → fort breakout baissier confirmé par montée de l'ATR.
**TRADEX-AI C1** : Pattern de haute fiabilité pour GC/CL : compression BB + ATR bas → surveiller breakout. Si breakout directionnellement aligné avec Belkhayate (BGC + Direction), signal de haute confiance. Ajouter 0.5 point au score /10.
*Catégorie : configuration*
