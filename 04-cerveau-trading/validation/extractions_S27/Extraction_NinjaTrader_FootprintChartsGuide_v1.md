# Extraction NinjaTrader — Footprint Charts Guide
**Source :** `bundles/ninjatrader/footprint_charts_guide.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7671 → D7690 · **Page :** https://ninjatrader.com/futures/blogs/footprint-charts-guide/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : guide complet Order Flow via footprint (volumetric bars NT8) — absorption, delta, imbalance, delta divergence — fortement pertinent pour C2 TRADEX sur GC/CL/ES.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune image sur la page source)*

---

## DÉCISIONS

### D7671 — Définition du footprint chart : volume bid/ask par niveau de prix
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Un footprint chart est un chart spécialisé qui affiche le volume d'achat et de vente exécuté à chaque niveau de prix individuel au sein d'une bougie — révélant qui (acheteurs ou vendeurs) était le plus agressif à chaque prix tradé pendant la période.
**TRADEX-AI C2** : Dans TRADEX, les volumetric bars NT8 (Order Flow+) constituent la source primaire du cercle C2 — chaque barre montre le bid volume (vendeurs agressifs) et l'ask volume (acheteurs agressifs) à chaque tick pour GC, CL, ES.
*Catégorie : volume_liquidite*

### D7672 — Footprint vs candlestick : 5 points de différence clés
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Les candlesticks donnent 4 données par barre (OHLC). Les footprint charts (volumetric bars NT8) donnent en plus : bid/ask volume par niveau de prix, calcul delta, détection d'imbalance, contexte order flow complet.
**TRADEX-AI C2** : L'avantage TRADEX : les données NT8 JSON doivent inclure bid_volume, ask_volume et delta par barre pour que le cercle C2 soit pleinement opérationnel — à implémenter dans data_reader.py Phase C.
*Catégorie : volume_liquidite*

### D7673 — Marché futures = données centralisées et standardisées = footprint fiable
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Les footprint charts sont particulièrement efficaces en futures parce que les données de trade sont centralisées et standardisées au niveau de l'exchange — rendant les données bid/ask volume précises et actionnables pour les intraday traders. Ils sont moins fiables en equity ou forex (données fragmentées entre exchanges et dark pools).
**TRADEX-AI C2** : Confirmation : pour GC, HG, CL, ZW, ES sur CME/CBOT (actifs TRADEX), les footprint data sont fiables et actionnables — utiliser Order Flow+ NT8 comme source C2 canonique.
*Catégorie : volume_liquidite*

### D7674 — Delta : différence nette ask volume vs bid volume sur la barre complète
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Le delta est la différence nette entre ask volume et bid volume sur toute la barre. Delta positif = acheteurs plus agressifs. Delta négatif = vendeurs plus agressifs. Il indique la direction de la pression order flow, pas seulement où le prix a clôturé.
**TRADEX-AI C2** : Le delta doit être calculé et transmis dans le JSON NT8 à data_reader.py. Claude Brain l'utilise comme signal C2 primaire : delta positif en zone de support = signal d'achat potentiel ; delta négatif à résistance = signal de vente potentiel.
*Catégorie : volume_liquidite*

### D7675 — Imbalance : asymétrie ask/bid signalant agressivité unilatérale
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : L'imbalance se produit quand l'ask volume à un niveau de prix est significativement plus grand que le bid volume au niveau directement en dessous (ou vice versa). Ratio typique utilisé : 3:1 ou supérieur. Signale que l'un des côtés était massivement plus agressif — souvent indicateur de zone où le prix est susceptible de revenir.
**TRADEX-AI C2** : Implémenter dans data_reader.py : détecter les imbalances (ratio ≥ 3:1) au niveau tick sur les volumetric bars NT8 pour GC/CL — les transmettre au cerveau Claude comme signal C2 dans le prompt d'analyse.
*Catégorie : volume_liquidite*

### D7676 — Absorption : volume élevé à un niveau mais prix ne passe pas
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : L'absorption se produit quand un gros volume se print à un niveau de prix mais que le prix échoue à le franchir. Les acheteurs absorbent les vendeurs en support, ou les vendeurs absorbent les acheteurs en résistance. Le côté avec le plus gros ordre gagne et le prix reste ou se retourne.
**TRADEX-AI C2** : Signal d'absorption = défense institutionnelle d'un niveau. Sur GC en support clé, une absorption visible sur volumetric bars NT8 = signal C2 fort pour score /10 — à intégrer dans le prompt Claude Brain avec le niveau de prix précis.
*Catégorie : structure_marche*

### D7677 — Exhaustion : une partie pousse fort puis manque de carburant
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : L'exhaustion se produit quand un côté pousse de façon agressive et manque de carburant. Apparaît souvent comme un spike de delta aigu suivi d'un retournement — un côté a essayé, tout le monde l'a remarqué, et le mouvement s'est effondré.
**TRADEX-AI C2** : L'exhaustion est un signal C2 de retournement — un spike delta sur CL ou GC suivi d'une inversion immédiate = signal d'épuisement à transmettre à Claude Brain comme élément prioritaire d'analyse.
*Catégorie : structure_marche*

### D7678 — Pattern #1 : Rejet haute volume à un niveau clé
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Le rejet haute volume survient quand un volume significatif se print à ou près d'un niveau de prix clé mais que le prix se retourne rapidement. Sur le footprint : lignes avec bid ou ask volume très élevé concentré d'un côté, clôture proche du côté opposé. Signal : un côté a défendu le niveau avec une vraie taille — zone à surveiller lors d'un retest.
**TRADEX-AI C2** : Sur GC : rejet haute volume sur résistance Belkhayate = signal VENDRE potentiel fort. Sur retest de ce niveau, le cerveau Claude doit tenir compte de ce contexte order flow C2 pour renforcer le signal.
*Catégorie : structure_marche*

### D7679 — Pattern #2 : Delta divergence (prix nouveau high + delta négatif)
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : La delta divergence survient quand le prix fait un nouveau high (ou low) mais que le delta raconte une histoire différente. Prix nouveau high + delta fortement négatif (vendeurs plus agressifs malgré la clôture haute) = mouvement manquant de conviction institutionnelle. Le delta diverge du prix — souvent signal précoce de retournement avant qu'il n'apparaisse sur le candlestick.
**TRADEX-AI C2** : Règle delta divergence TRADEX : si GC fait un nouveau high ET que le delta barre est négatif → flag bearish divergence C2 → déclencher analyse Claude Brain avec ce signal comme argument de retournement prioritaire.
*Catégorie : indicateurs_momentum*

### D7680 — Cumulative delta : total running du delta sur plusieurs barres
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Le cumulative delta est le total cumulé du delta sur plusieurs barres — montre la direction à long terme de la pression order flow. Quand il diverge du prix, utiliser le footprint pour zoomer et voir exactement où se produit cette divergence.
**TRADEX-AI C2** : Le cumulative delta doit être calculé sur les sessions NT8 pour GC et CL — une divergence cumulative delta / prix sur plusieurs barres est un signal C2 majeur à transmettre dans le prompt Claude Brain pour renforcer ou invalider un signal.
*Catégorie : volume_liquidite*

### D7681 — Pattern #3 : Trapped traders via volume spike sur une seule barre
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Un volume spike sur une seule barre peut révéler des traders piégés — exemple classique : gros ask volume au high, prix se retourne immédiatement, clôture près du low. Ces acheteurs sont maintenant en perte et deviennent des vendeurs forcés au fur et à mesure que le prix baisse, ajoutant du momentum au mouvement baissier.
**TRADEX-AI C2** : Les traders piégés créent du momentum forcé — un single-bar volume spike suivi d'un retournement sur GC/CL doit être flaggé C2 par data_reader.py et transmis au cerveau Claude pour contextualiser le follow-through potentiel.
*Catégorie : psychologie*

### D7682 — Méthode d'intégration footprint : thèse claire avant lecture
🔵 **ÉCOLE** (Source : footprint_charts_guide.md) : Approche recommandée : commencer avec une thèse claire avant d'ouvrir un footprint chart (confirmer breakout ? absorption à un niveau clé ? timing d'entrée près d'un support ?). Ces charts sont denses en information — entrer sans focus les rend difficiles à lire.
**TRADEX-AI C2** : Le prompt Claude Brain pour analyse C2 doit formuler explicitement la question order flow avant de traiter les données footprint : "Ce breakout est-il confirmé par l'order flow ?" ou "Y a-t-il absorption au niveau X ?" — structurer l'analyse, pas l'inonder de données brutes.
*Catégorie : configuration*

### D7683 — Footprint + VWAP : défense institutionnelle du VWAP visible
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : VWAP est le benchmark que la plupart des institutionnels utilisent pour évaluer la qualité d'exécution. Quand le prix revient au VWAP après un mouvement de tendance, surveiller le footprint — une absorption là signale souvent une défense institutionnelle. VWAP traversé avec delta dominant d'un côté = tendance continue.
**TRADEX-AI C2/C4** : Règle VWAP-footprint : sur ES (actif de confirmation C4), retour au VWAP + absorption visible sur volumetric bars = signal de continuation probable — à transmettre au cerveau Claude comme contexte C2 pour valider la direction.
*Catégorie : structure_marche*

### D7684 — Footprint + Point of Control (POC) du Volume Profile
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Le Point of Control (POC) — niveau de prix avec le plus gros volume tradé sur une session — agit souvent comme zone magnétique et de décision. Utiliser le footprint pour évaluer ce qui se passe réellement quand le prix atteint ces nœuds haute volume : absorption ou percée avec conviction ?
**TRADEX-AI C2** : Le POC doit être identifié dans les données NT8 et fourni au cerveau Claude — quand GC ou CL approche le POC, la lecture footprint (absorption vs percée delta dominante) détermine la direction probable du signal.
*Catégorie : structure_marche*

### D7685 — Ne jamais trader les patterns footprint en isolation du contexte marché
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Même un signal d'absorption fort peut échouer si le contexte macro n'est pas favorable. Toujours intégrer : direction de tendance, volume global relatif à la moyenne et environnement macro avant d'agir sur un signal footprint.
**TRADEX-AI C2** : Garde-fou obligatoire TRADEX : aucun signal C2 seul (même absorption forte) ne déclenche un ordre en mode Auto — doit être validé par C1 (tendance Belkhayate) + C4 (macro/news gate) + score ≥ 7,0 /10 ET R/R ≥ 1:2.
*Catégorie : gestion_risque_entree*

### D7686 — Breakout réel vs stop hunt : distinguer via footprint
🟢 **FAIT VÉRIFIÉ** (Source : footprint_charts_guide.md) : Un candlestick dit seulement que le prix a franchi un niveau. Un footprint dit si de vrais achats l'ont propulsé ou si c'était une chasse aux stops à faible conviction. Breakout réel = ask volume dominant le bid volume + delta clairement positif. Faux breakout = ask volume modeste + delta tepid ou négatif.
**TRADEX-AI C1/C2** : Règle anti-faux-breakout TRADEX : avant de valider un breakout signal sur GC ou CL, vérifier le footprint — ask dominant + delta positif = breakout réel ; delta faible = filtrer le signal et afficher ATTENDRE.
*Catégorie : gestion_risque_entree*

### D7687 — Timeframe optimal footprint intraday : 1 à 5 minutes
🔵 **ÉCOLE** (Source : footprint_charts_guide.md) : La plupart des traders intraday futures trouvent que les volumetric bars de 1 à 5 minutes offrent un bon équilibre signal/bruit. Les scalpers descendent plus bas ; les day traders swing-oriented utilisent souvent 5 à 15 minutes. Tester le timeframe préféré en simulateur avant utilisation live.
**TRADEX-AI C2** : Pour TRADEX (surveillance 2 secondes sur NT8), les footprint à utiliser pour C2 : 1-3 min pour GC (or, volatile) et CL (pétrole, très volatile) ; 5 min pour ZW (blé, moins rapide) — à valider en Phase C lors de l'implémentation des collecteurs NT8.
*Catégorie : timing*

