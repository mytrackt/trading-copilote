# Extraction Optimus — Breakout Trading
**Source :** `bundles/optimusfutures/breakout_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8351 → D8370 · **Page :** https://optimusfutures.com/blog/breakout-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : stratégie breakout complète (réels vs faux) + 7 techniques de confirmation — applicables entrées GC/CL via Cercle C1/C2.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans le bundle) | — | — | — |

## DÉCISIONS

### D8351 — Définition : breakout = dépassement support/résistance par déséquilibre offre/demande
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un breakout est un phénomène où le prix d'un actif dépasse un niveau de support ou résistance. L'un des côtés (acheteurs ou vendeurs) l'emporte sur l'autre, causant un mouvement de prix souvent violent. Une fois la résistance franchie en bullish, elle tend à devenir un nouveau support (et inversement).
**TRADEX-AI C1** : Le breakout est une configuration d'entrée valide pour TRADEX-AI. La règle Belkhayate "résistance rompue = nouveau support" est confirmée par cette source. À intégrer dans le scoring C1 : breakout confirmé = +1 point.
*Catégorie : structure_marche*

### D8352 — Bullish breakout : dépassement résistance + conversion résistance→support
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un breakout bullish survient quand le prix monte au-delà d'un niveau de résistance, suggérant une nouvelle tendance ou la continuation d'une tendance haussière. La résistance franchie tend à se transformer en nouveau niveau de support.
**TRADEX-AI C1** : Dans claude_brain.py, la détection d'un breakout bullish sur GC (Or) avec conversion résistance→support visible est un signal de ACHETER de haute confiance, aligné Belkhayate. Nécessite confirmation volume C2.
*Catégorie : gestion_risque_entree*

### D8353 — Bearish breakout : cassure du support + conversion support→résistance
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un breakout bearish survient quand le prix descend sous un niveau de support, indiquant une nouvelle tendance ou continuation baissière. Le support précédent peut alors agir comme nouvelle résistance.
**TRADEX-AI C1** : Pour CL (Pétrole) et ZW (Blé), un breakout bearish sous support pivot avec conversion support→résistance est un signal VENDRE valide. Vérifier la confirmation via DX (Dollar) C4 : Dollar fort = confirmation baisse CL/ZW.
*Catégorie : gestion_risque_entree*

### D8354 — Trois drivers de breakouts : fondamentaux, techniques, psychologie collective
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Les principaux drivers de breakouts sont : (1) Facteurs fondamentaux — nouvelles économiques, rapports macro ; (2) Facteurs techniques — stop orders concentrés à un niveau, déclenchant une réaction en chaîne ; (3) Psychologie de marché — la conviction collective sur un niveau clé peut provoquer un breakout violent quand les participants agissent contre ce niveau.
**TRADEX-AI C4/C6** : Les drivers fondamentaux (NFP, FOMC, CPI) sont couverts par le News Gate. Les stop orders concentrés (driver technique) sont visibles via l'Order Flow ATAS (C2). La psychologie collective (driver C5) peut être croisée avec Fear&Greed Index.
*Catégorie : macro_evenements*

### D8355 — Volume comme condition nécessaire pour valider un breakout
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Pour trader les breakouts efficacement : identifier les niveaux S/R clés, chercher les breakouts sur volume croissant (le volume valide la participation du marché). Un spike de volume pendant un breakout indique une forte participation et une probabilité plus haute de continuation.
**TRADEX-AI C2** : Règle non négociable dans TRADEX-AI : tout signal de breakout (ACHETER ou VENDRE) sans confirmation volume via ATAS Order Flow est dégradé à confiance MAX 65% (fallback local). Volume croissant = condition requise pour Mode Auto.
*Catégorie : volume_liquidite*

### D8356 — Mesure de profit cible : distance swing high/low projetée depuis le breakout
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Pour les breakouts sur support/résistance historique, une méthode de target est de mesurer la distance entre le dernier swing high et le niveau de support, puis de projeter cette même distance sous le niveau de breakout. Exemple concret sur Micro Gold (MGC) Optimus Flow.
**TRADEX-AI C1** : Dans risk_manager.py, implémenter la règle R/R : target = distance swing projection depuis breakout. Le seuil TRADEX-AI est R/R ≥ 1:2 (STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md, Partie 4). La mesure swing projection satisfait naturellement ce ratio si le setup est correct.
*Catégorie : gestion_position_active*

### D8357 — Breakout sur pattern : mesure target = hauteur du pattern + point de breakout
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Pour les breakouts de patterns chartistes (ex : rectangle), mesurer la hauteur du pattern et l'ajouter au niveau de breakout pour déterminer le target de profit. Exemple sur Micro Emini S&P 500 (ES) avec rectangle pattern : acheter au-dessus du breakout, stop sous le pattern.
**TRADEX-AI C1** : Pour les patterns rectangulaires sur GC ou CL, utiliser la hauteur pattern comme target initial dans le calcul R/R. Si 52-week high est plus proche, c'est une cible alternative valide (approche Optimus confirmée).
*Catégorie : gestion_position_active*

### D8358 — Breakout en price channel : rester dans la direction de la tendance dominante
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Les breakouts de price channel sont délicats. Si le prix trend fortement à la hausse, un breakout vers le bas peut être une simple correction, pas un retournement. Rester du côté de la tendance et attendre que le prix se brise à nouveau dans la direction de la tendance dominante (exemple sur CL Crude Oil).
**TRADEX-AI C1** : Dans TRADEX-AI, la tendance dominante Belkhayate (Direction Belkhayate) prime sur tout signal de breakout contre-tendance. Un breakout de channel contre la tendance Belkhayate est automatiquement écarté ou classé ATTENDRE.
*Catégorie : indicateurs_tendance*

### D8359 — Faux breakout (fakeout) : définition et impact
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un faux breakout (fakeout) induit les traders en croyant que le prix va continuer dans la direction du breakout, alors qu'il repart dans l'autre sens, causant souvent des pertes. Les fakeouts se produisent quand un côté du marché surpasse l'autre à un niveau critique. Les institutionnels initialisent parfois de gros volumes que les retail suivent, sans réaliser que c'est un fakeout stratégique.
**TRADEX-AI C2/C5** : La détection des fakeouts institutionnels passe par l'Order Flow ATAS (delta imbalance, absorption). Une absorption visible sur footprint chart = signe de fakeout potentiel. Confirmation sentiment C5 (VIX en hausse = fakeouts plus fréquents).
*Catégorie : structure_marche*

### D8360 — Signal 1 anti-fakeout : approche progressive (pullbacks) vers le niveau S/R
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un breakout réel est précédé d'une approche typique avec pullbacks réguliers indiquant un engagement équilibré acheteurs/vendeurs. Une approche trop rapide et verticale vers un niveau de résistance/support peut en réalité signaler une préparation au retournement plutôt qu'un breakout.
**TRADEX-AI C1** : Dans le prompt Claude KB, ajouter la règle : si le prix approche le niveau S/R en chandelier unique sans pullbacks préalables (mouvement vertical), signaler comme alerte anti-fakeout. Réduire le score signal de -0.5 point.
*Catégorie : configuration*

### D8361 — Signal 2 anti-fakeout : pullback retardé + résistance/support ne se convertit pas
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Un indicateur de fakeout est quand un niveau de support ne devient pas résistance (ou l'inverse) après le breakout initial. Si le prix revient facilement au-dessus du point de breakout et l'utilise comme support après une cassure baissière, c'est un fakeout classique. La série de chandeliers baissiers + désintérêt des traders pour pousser au-delà confirme le breakout réel.
**TRADEX-AI C1** : Règle de confirmation KB : après breakout, attendre 1-2 barres pour vérifier que l'ancien S/R fait sa conversion. Si le prix repasse facilement de l'autre côté = fakeout → signal ATTENDRE automatique. Ne pas entrer sans cette confirmation.
*Catégorie : gestion_risque_entree*

### D8362 — Signal 3 anti-fakeout : contexte large et obstacles proches du point de breakout
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Une erreur fréquente est de se concentrer uniquement sur le point de breakout immédiat sans analyser le contexte plus large. Examiner les S/R proches, lignes de tendance, pivot points, Fibonacci, et analyser les multiples timeframes peut révéler des obstacles qui feront échouer le breakout.
**TRADEX-AI C1** : Dans le prompt Claude, vérifier les obstacles dans un rayon de 1 ATR au-delà du point de breakout. Si un HVN (Volume Profile) ou un pivot Belkhayate majeur bloque le chemin → score réduit. C'est la vérification "trafic au-delà du breakout".
*Catégorie : configuration*

### D8363 — Tip 1 : Pullback et retest du niveau de breakout = entrée plus sûre
🔵 **ÉCOLE** (Source : breakout_trading.md) : Les breakouts réels voient souvent le prix revenir tester le niveau de breakout initial — ce pullback/retest fournit un point d'entrée plus sécurisé et protège contre les fakeouts potentiels.
**TRADEX-AI C1** : Dans TRADEX-AI Mode Manuel, présenter toujours le niveau de retest comme point d'entrée secondaire sécurisé. En Mode Auto, l'entrée se fait uniquement au retest si le breakout initial n'a pas été capturé (filtre de latence).
*Catégorie : gestion_risque_entree*

### D8364 — Tip 2 : aligner le breakout avec la direction de la tendance majeure
🔵 **ÉCOLE** (Source : breakout_trading.md) : Toujours considérer la tendance globale avant de trader un breakout. Aligner les trades avec la direction de la tendance majeure augmente la probabilité de succès.
**TRADEX-AI C1** : Règle verrouillée Belkhayate confirmée : la Direction Belkhayate (BGC) détermine la tendance majeure. Un breakout dans la direction de la Direction Belkhayate = signal VALIDE. Contre la Direction Belkhayate = signal écarté ou dégradé.
*Catégorie : indicateurs_tendance*

### D8365 — Tip 3 : Bollinger Bands — breakouts en bordure de bande plus fiables
🔵 **ÉCOLE** (Source : breakout_trading.md) : Les Bollinger Bands aident à identifier les tendances fortes et les taux de réussite des breakouts potentiels. Les breakouts survenant près des bords des bandes sont plus susceptibles de continuer dans la direction de la tendance.
**TRADEX-AI C1** : Dans le scoring TRADEX-AI, un breakout se produisant à proximité de la bande Bollinger extérieure reçoit un bonus de confirmation (+0.5 point score). Combinaison Belkhayate Direction + Bollinger bord = signal fort.
*Catégorie : configuration*

### D8366 — Tip 4 : Volume spike pendant breakout = participation forte + continuation probable
🔵 **ÉCOLE** (Source : breakout_trading.md) : Les pics de volume pendant un breakout indiquent une forte participation du marché et une probabilité plus haute que le breakout sustienne sa direction.
**TRADEX-AI C2** : La règle volume spike est critique : dans data_reader.py, monitorer le ratio volume_actuel / volume_moyen_20barres. Si ratio > 1.5 lors d'un breakout S/R → marquer comme breakout confirmé. En dessous de 1.2 → breakout non confirmé, rester à ATTENDRE.
*Catégorie : volume_liquidite*

### D8367 — Tip 5 : Triangle patterns — consolidation précédant mouvement significatif
🔵 **ÉCOLE** (Source : breakout_trading.md) : Les patterns en triangle signifient une consolidation et des points potentiels de breakout. L'aboutissement du pattern conduit souvent à des mouvements de prix significatifs.
**TRADEX-AI C1** : Ajouter la détection des triangles dans les patterns KB Belkhayate. Un triangle symétrique en formation sur GC avec réduction progressive de l'ATR = signal de compression → préparer ordre conditionnel dans Mode Auto.
*Catégorie : configuration*

### D8368 — Tip 6 : Spring Pattern (Wyckoff) — faux breakout précédant le vrai
🟢 **FAIT VÉRIFIÉ** (Source : breakout_trading.md) : Le Spring Pattern (Richard Wyckoff) décrit un faux breakout précédant un vrai breakout. Il souligne l'importance de la patience et de l'observation. Ce pattern est connu parmi les analystes techniques.
**TRADEX-AI C2** : Le Spring Pattern Wyckoff est déjà documenté dans la KB (Couche 3 Wyckoff D99-D111). Dans TRADEX-AI, un Spring détecté sur footprint ATAS (absorption sous support + reprise rapide au-dessus) = signal d'accumulation institutionnelle → ACHETER fort.
*Catégorie : structure_marche*

### D8369 — Tip 7 : Indicateurs momentum (RSI, MFI, ADX, Stochastic) pour évaluer la force du breakout
🔵 **ÉCOLE** (Source : breakout_trading.md) : Utiliser des indicateurs comme RSI, MFI, ADX ou Stochastic Oscillator pour jauger la force qui conduit un breakout. Cela aide à décider si prendre une position, quand l'entrer, et quelle taille prendre.
**TRADEX-AI C1** : Dans le Niveau 1 Python TRADEX-AI, calculer ADX sur les actifs TRADING. ADX > 25 = tendance forte → breakout plus fiable. ADX < 20 = marché sans direction → éviter breakouts, risque fakeout élevé. Paramètre configurable dans settings.py.
*Catégorie : indicateurs_momentum*

### D8370 — Plan B obligatoire : préparer une sortie pour les faux breakouts
🟡 **SYNTHÈSE** (Source : breakout_trading.md) : Il est extrêmement difficile de prédire un faux breakout. Il est donc indispensable d'avoir un plan de contingence pour les fakeouts et de gérer les positions quand ils surviennent. Aucune méthode ne garantit une détection parfaite — combiner les techniques avec l'expérience et la pratique améliore significativement les capacités d'anticipation.
**TRADEX-AI C1** : Dans TRADEX-AI, le plan B pour faux breakout est implémenté via le Circuit Breaker (cb_NT8) et le Risk Manager : si le prix revient au-delà du S/R en sens inverse dans les 3 barres suivant l'entrée → suspension automatique + alerte Mode Manuel. Ne jamais laisser un fakeout progresser sans réaction.
*Catégorie : gestion_risque_entree*
