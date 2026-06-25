# Extraction StockCharts — Trading the Death Cross
**Source :** `bundles/stockcharts/trading_the_death_cross.md` (HTTP 200) + 3 images certifiées
**Méthode images :** double ancrage · 3/3 certifiées · 0 à vérifier
**Décisions :** D4531 → D4550 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/trading-the-death-cross
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Identification de retournements baissiers sur GC/HG/CL/ZW via croisement SMA50/SMA200 — signal de confirmation de tendance descendante.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/OXXyoKisqQaxA3pw8I1q | Example of a Death Cross | What is a Death Cross | D4531 |
| /files/f0nZI8jcAtmpirXViWEj | Type 1 Crossing — Death Cross (prix étendu du point de croisement) | Not All Crossovers Are the Same | D4538 |
| /files/1deyYuv94WYswcUcNG5x | Type 2 Crossing — reprise de tendance après croisement | Not All Crossovers Are the Same | D4539 |

## DÉCISIONS

### D4531 — Définition du Death Cross
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md, image_OXXyoKisqQaxA3pw8I1q) : Le Death Cross est un pattern baissier formé quand la SMA courte terme (typiquement SMA50) croise sous la SMA long terme (typiquement SMA200).
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un croisement SMA50 < SMA200 constitue un signal baissier à intégrer dans la grille de score /10.
*Catégorie : indicateurs_tendance*

### D4532 — Conditions bullish/bearish générales
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md) : Quand la SMA50 est au-dessus de la SMA200 → conditions généralement haussières. Quand la SMA50 est en dessous de la SMA200 → conditions généralement baissières. Ces états ne confirment pas un trend défini, ils indiquent le contexte.
**TRADEX-AI C1** : Le positionnement relatif SMA50/SMA200 sur GC/HG/CL/ZW constitue un filtre de contexte de marché (bullish/bearish) pour valider ou invalider l'entrée.
*Catégorie : indicateurs_tendance*

### D4533 — Signaux potentiels après un Death Cross
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md) : Un Death Cross peut indiquer : (1) l'uptrend a atteint un sommet relatif ou significatif, (2) les prix ont décliné avec assez de consistance/momentum pour amener la MA rapide sous la lente, (3) l'activité vendeuse s'est intensifiée, (4) le sentiment est de plus en plus baissier.
**TRADEX-AI C1** : Plusieurs de ces facteurs simultanés sur GC/HG/CL/ZW renforcent le score de signal VENTE dans la grille /10.
*Catégorie : indicateurs_tendance*

### D4534 — Death Cross comme signal de confirmation
🔵 **ÉCOLE** (Source : trading_the_death_cross.md) : Utilisation du Death Cross comme signal de confirmation : les traders cherchant une vue plus large des conditions de tendance utilisent l'événement de croisement comme indicateur significatif que l'environnement de marché devient baissier.
**TRADEX-AI C1** : Le Death Cross sur ES (S&P500) ou DX (Dollar) renforce la lecture macro baissière pour les actifs de confirmation TRADEX.
*Catégorie : indicateurs_tendance*

### D4535 — Death Cross comme signal de réduction d'exposition
🔵 **ÉCOLE** (Source : trading_the_death_cross.md) : Les investisseurs long terme qui rééquilibrent activement leurs portefeuilles utilisent couramment le croisement comme signal de réduction potentielle d'exposition aux actifs exhibant ce pattern.
**TRADEX-AI C7** : En mode Auto TRADEX, un Death Cross sur GC/HG/CL/ZW peut déclencher la réduction de la taille de position ou bloquer de nouvelles entrées LONG.
*Catégorie : gestion_position_active*

### D4536 — Death Cross comme signal d'entrée short
🔵 **ÉCOLE** (Source : trading_the_death_cross.md) : Les traders cherchant à vendre à découvert peuvent utiliser le Death Cross comme précondition pour une stratégie "short".
**TRADEX-AI C1** : Sur TRADEX, le Death Cross peut être intégré comme condition préalable (filtre) pour autoriser un signal VENTE — jamais seul, mais en conjonction avec les 7 cercles.
*Catégorie : gestion_risque_entree*

### D4537 — Death Cross comme niveau de stop-loss
🔵 **ÉCOLE** (Source : trading_the_death_cross.md) : Les traders en position courte peuvent utiliser le prix/range du Death Cross pour déterminer des niveaux de stop-loss appropriés.
**TRADEX-AI C1** : Le niveau de croisement SMA50/SMA200 sur GC/HG/CL/ZW constitue une référence structurelle pour placer un stop sur une position VENTE.
*Catégorie : gestion_risque_entree*

### D4538 — Type 1 Crossing : prix étendu du point de croisement
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md, image_f0nZI8jcAtmpirXViWEj) : Type 1 Crossing (McClellan) : les prix sont étendus loin du point de croisement réel dans la direction du croisement — peut marquer un retournement temporaire ou plus significatif.
**TRADEX-AI C1** : Un Death Cross de Type 1 sur GC/HG/CL/ZW (prix déjà très bas au moment du croisement) indique un retournement potentiel — signal moins fiable car arrivant en retard.
*Catégorie : indicateurs_tendance*

### D4539 — Type 2 Crossing : reprise de tendance précédente
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md, image_1deyYuv94YswcUcNG5x) : Type 2 Crossing (McClellan) : les prix reviennent au prix réel du point de croisement — indique souvent une reprise de la tendance précédant le croisement.
**TRADEX-AI C1** : Un Death Cross de Type 2 sur GC/HG/CL/ZW (prix revenant au niveau du croisement) peut indiquer un faux signal baissier — renforce la nécessité de confirmation multi-indicateurs.
*Catégorie : indicateurs_tendance*

### D4540 — Prix haussier après Death Cross = signal potentiellement non suivi
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md) : Si l'action des prix montre des indications de hausse après un Death Cross (prix montant ou spikant vers le haut), cela indique que l'indication baissière peut ne pas se confirmer. Des baisses sur faible volume indiquent un manque de conviction des vendeurs.
**TRADEX-AI C2** : Sur TRADEX, un Death Cross suivi d'un volume décroissant (C2 OrderFlow) réduit la fiabilité du signal VENTE — condition d'invalidation à intégrer dans le circuit de décision.
*Catégorie : volume_liquidite*

### D4541 — Death Cross et Golden Cross peuvent échouer
🟢 **FAIT VÉRIFIÉ** (Source : trading_the_death_cross.md) : Les événements Death Cross et Golden Cross échouent parfois à se confirmer. Il est important d'obtenir un maximum d'informations de marché et économiques pour contextualiser l'action des prix, notamment quand le marché manifeste une indécision après ces signaux majeurs.
**TRADEX-AI C1** : Le Death Cross seul est insuffisant pour TRADEX — il doit être validé par les 7 cercles (C1 à C7) et ne compte que pour une partie du score /10.
*Catégorie : gestion_risque_entree*

### D4542 — Death Cross requiert une interprétation nuancée
🟡 **SYNTHÈSE** (Source : trading_the_death_cross.md) : Le Death Cross est généralement considéré comme un signal de fin des conditions haussières d'un actif — mais beaucoup plus de nuance entre dans l'interprétation. Le trader doit affiner les insights dans une lecture plus précise du marché.
**TRADEX-AI C1** : Dans la grille de score TRADEX /10, le Death Cross (SMA50 < SMA200) est un facteur parmi d'autres — sa présence seule ne génère jamais un signal d'exécution.
*Catégorie : indicateurs_tendance*
