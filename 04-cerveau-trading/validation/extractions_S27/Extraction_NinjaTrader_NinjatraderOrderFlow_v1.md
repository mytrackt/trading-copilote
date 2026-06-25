# Extraction NinjaTrader — Footprint Charts & Order Flow with NinjaTrader
**Source :** `bundles/ninjatrader/ninjatrader_order_flow.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image exploitable extraite · 0/0 certifiées · 0 à vérifier
**Décisions :** D7991 → D8010 · **Page :** https://ninjatrader.com/futures/blogs/ninjatrader-order-flow/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : footprint (volumetric bars) + cumulative delta = Circle C2 Order Flow pour confirmer signaux Belkhayate sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image exploitable dans ce bundle | — | — |

## DÉCISIONS

### D7991 — Footprint chart = volume acheteur/vendeur à chaque niveau de prix
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Un footprint chart (appelé "volumetric bars" dans NinjaTrader) affiche le volume d'achat et de vente exécuté à chaque niveau de prix individuel au sein d'une barre. Contrairement à une bougie standard (OHLC), il révèle QUI initie les transactions (acheteurs ou vendeurs) à chaque prix.
**TRADEX-AI C2** : Les volumetric bars NT8 constituent la source primaire de données order flow pour le cercle C2 de TRADEX-AI — données accessibles via ATAS Pro connecté Rithmic sur GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D7992 — Footprint vs bougie standard : 4 différences clés
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Footprint chart : (1) montre volume achat/vente à chaque niveau, (2) révèle qui initie (acheteur/vendeur), (3) met en évidence déséquilibres, absorption et épuisement, (4) optimal pour intraday et scalping. Bougie standard : (1) OHLC seulement, (2) pas d'initiation visible, (3) aucune visibilité directe order flow, (4) utile sur tous timeframes.
**TRADEX-AI C2** : Pour TRADEX-AI, les footprints sont utilisés en confirmation de signal (C2) — jamais comme signal primaire. La méthode Belkhayate reste la source du signal.
*Catégorie : volume_liquidite*

### D7993 — Order flow crucial pour traders actifs : réagir au présent pas au passé
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Quand les marchés bougent vite, le prix seul peut être trompeur. L'order flow aide les traders à réagir à ce que fait le marché maintenant, pas ce qu'il a fait plusieurs barres auparavant. Particulièrement important pour day traders, scalpers et stratégies court-terme.
**TRADEX-AI C2** : Le moteur Python TRADEX surveille les fichiers JSON NT8/ATAS toutes les 2 secondes — cette fréquence est alignée avec l'approche order flow temps réel pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D7994 — 4 usages concrets de l'order flow
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : L'order flow permet : (1) repérer où se produisent les vrais achats ou ventes, (2) confirmer si un breakout a de la force derrière lui, (3) identifier quand un côté du marché perd du momentum, (4) évaluer la qualité des niveaux de support/résistance basée sur la participation réelle.
**TRADEX-AI C2** : Ces 4 usages correspondent aux 4 confirmations order flow que TRADEX-AI doit valider dans la grille de score /10 — chaque item renforce ou diminue la confiance du signal Belkhayate.
*Catégorie : structure_marche*

### D7995 — Footprint = volumetric bars dans NinjaTrader (terminologie)
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : "Footprint chart" est le terme standard de l'industrie. "Volumetric bars" est le terme NinjaTrader dans l'UI. Ils désignent la même chose : chart affichant volume achat/vente à chaque niveau de prix au sein d'une barre.
**TRADEX-AI C2** : Dans le code TRADEX (data_reader.py), utiliser le terme "volumetric_bars" pour référencer les données ATAS/NT8 — aligner la nomenclature sur le vocabulaire NinjaTrader.
*Catégorie : configuration*

### D7996 — Volumetric bars : 4 métriques affichables
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Les volumetric bars dans NT8 permettent d'afficher : (1) volume bid vs ask, (2) delta par niveau de prix, (3) métriques pondérées par volume, (4) indices visuels pour grands déséquilibres ou zones haute activité. Personnalisables selon les besoins du trader.
**TRADEX-AI C2** : Pour TRADEX-AI, les métriques prioritaires à extraire via ATAS : delta par niveau de prix + volume bid/ask — les plus directement utilisables par claude_brain.py pour la confirmation C2.
*Catégorie : volume_liquidite*

### D7997 — Cumulative Delta : différence cumulée acheteurs moins vendeurs dans le temps
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Le Cumulative Delta calcule la différence nette entre acheteurs (volume à l'ask) et vendeurs (volume au bid) au fil du temps. Utilisations : (1) confirmer les mouvements directionnels (delta montant en uptrend = forte pression achat), (2) repérer les divergences (prix fait nouveaux hauts mais delta non = demande affaiblie), (3) évaluer la force de la tendance (delta positif/négatif soutenu = momentum directionnel).
**TRADEX-AI C2** : Cumulative Delta est le premier indicateur order flow à intégrer dans la grille de confirmation C2 — divergence Delta/prix sur GC/HG/CL/ZW = alerte retournement potentiel.
*Catégorie : indicateurs_momentum*

### D7998 — Stratégie 1 : retournement à résistance avec épuisement acheteurs
🔵 **ÉCOLE** (Source : ninjatrader_order_flow.md) : Scénario : prix approche une résistance connue. Sur volumetric chart : gros volume achat empilé aux hauts mais prix ne perce pas. Cumulative delta ralentit ou décline (manque de suivi). Signal : vendre le marché au début du retournement, stop au-dessus de la zone à fort volume. Les acheteurs piégés fournissent le carburant pour un mouvement baissier.
**TRADEX-AI C2** : Ce pattern "épuisement acheteurs à résistance" doit être reconnu comme signal bearish C2 pour GC/HG/CL/ZW — combiné avec zone de résistance Belkhayate BGC, confiance signal augmente.
*Catégorie : structure_marche*

### D7999 — Stratégie 2 : breakout avec confirmation delta
🔵 **ÉCOLE** (Source : ninjatrader_order_flow.md) : Scénario : prix sort d'une zone étroite sur volume croissant. Cumulative delta montre une forte poussée haussière, confirmant des achats agressifs. Signal : entrer sur le breakout avec confiance, trailing stop derrière les clusters de volume du footprint chart. Sortir si delta diverge du prix.
**TRADEX-AI C2** : Ce pattern "breakout + delta confirmation" renforce le score C2 dans la grille /10 — un breakout Belkhayate sans confirmation delta reste un signal de moindre confiance (confiance < seuil 7.0).
*Catégorie : gestion_risque_entree*

### D8000 — Stratégie 3 : traders piégés détectés par déséquilibre de volume
🔵 **ÉCOLE** (Source : ninjatrader_order_flow.md) : Scénario : pendant un pullback, une barre montre de la vente lourde sur le footprint, mais le marché tient son niveau puis rebondit fortement. Signal : les vendeurs ont été absorbés et sont piégés. Entrée long sur le retournement, stop au bas de la barre footprint. Chercher continuation alors que les vendeurs piégés couvrent leurs positions.
**TRADEX-AI C2** : Ce pattern "absorption + piège vendeurs" est un signal C2 haussier fort — particulièrement pertinent sur GC (Or) aux niveaux de support Belkhayate importants.
*Catégorie : structure_marche*

### D8001 — Erreur commune : réagir à chaque déséquilibre sans contexte
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Erreurs fréquentes avec l'order flow : (1) réagir à chaque pic de volume = pas chaque déséquilibre est un signal — utiliser contexte et confluence. (2) Surpondérer le delta seul — delta ne détermine pas seul la direction, l'utiliser pour confirmer pas dicter. (3) Ignorer tendance et structure — l'order flow soutient l'analyse macro, ne la remplace pas. (4) Sauter la pratique — ces outils demandent du temps pour maîtriser.
**TRADEX-AI C2** : L'order flow dans TRADEX-AI est un CONFIRMATEUR, jamais un déclencheur primaire — la règle "3/4 actifs trading + 2/3 confirmation alignés" reste la condition de déclenchement principale.
*Catégorie : gestion_risque_entree*

### D8002 — Order Flow + : volumetric bars + cumulative delta + volume profile
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : La suite NinjaTrader Order Flow+ inclut : (1) volumetric bars (footprint), (2) cumulative delta, (3) volume profile. Ces outils ensemble offrent une vue en couches de l'activité order flow en temps réel. Disponible avec un compte Lifetime NinjaTrader ou en add-on mensuel.
**TRADEX-AI C2** : Les 3 composantes Order Flow+ (footprint, delta, profile) correspondent aux 3 sources de données C2 dans TRADEX-AI — à terme, data_reader.py doit lire les 3 depuis ATAS Pro via JSON.
*Catégorie : configuration*

### D8003 — Marchés futures : données bid/ask centralisées et standardisées à l'échange
🟢 **FAIT VÉRIFIÉ** (Source : ninjatrader_order_flow.md) : Sur les marchés futures, l'analyse footprint est particulièrement efficace car les données de trading sont centralisées et standardisées au niveau de la bourse, rendant les décompositions volume bid/ask précises et utilisables en intraday.
**TRADEX-AI C2** : La fiabilité des données order flow sur GC/HG/CL/ZW (CME/CBOT) est garantie par la centralisation des échanges — justification supplémentaire pour l'utilisation de footprints comme couche de confirmation dans TRADEX-AI.
*Catégorie : volume_liquidite*
