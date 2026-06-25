# Extraction StockCharts — Trading Using the Golden Cross
**Source :** `bundles/stockcharts/trading_using_the_golden_cross.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D4551 → D4570 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/trading-using-the-golden-cross
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Identification de retournements haussiers sur GC/HG/CL/ZW via croisement SMA50/SMA200 — signal de confirmation de tendance ascendante, complément symétrique au Death Cross.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/JcPE4fPLj8b21divdVDR | Example of a Golden Cross | Introduction | D4551 |
| /files/PO2ZlgqPvxFNMcQQUEar | Example of Type 1 Golden Cross | Not All Golden Crosses Are the Same | D4558 |
| /files/2QtWU85tvfNiEavxAZhI | Example of Type 1 and Type 2 Golden Crosses | Not All Golden Crosses Are the Same | D4559 |

## DÉCISIONS

### D4551 — Définition du Golden Cross
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md, image_JcPE4fPLj8b21divdVDR) : Le Golden Cross est un pattern haussier où une MA courte terme (rapide) croise au-dessus d'une MA long terme (lente). Le paramétrage le plus courant : SMA50 (rapide) contre SMA200 (lente).
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un croisement SMA50 > SMA200 constitue un signal haussier à intégrer dans la grille de score /10.
*Catégorie : indicateurs_tendance*

### D4552 — Golden Cross comme indicateur de retournement haussier potentiel
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md) : Le Golden Cross peut indiquer plusieurs potentialités haussières : (1) un downtrend peut avoir temporairement ou significativement atteint son fond, (2) les prix ont monté avec assez de consistance/momentum pour amener la MA rapide au-dessus de la lente, (3) l'activité acheteuse monte régulièrement, (4) le sentiment de marché est de plus en plus haussier.
**TRADEX-AI C1** : Ces facteurs simultanés sur GC/HG/CL/ZW renforcent le score ACHAT dans la grille /10.
*Catégorie : indicateurs_tendance*

### D4553 — Golden Cross comme signal de confirmation
🔵 **ÉCOLE** (Source : trading_using_the_golden_cross.md) : Le Golden Cross peut être utilisé pour confirmer la probabilité qu'un retournement de trend haussier, ou une fin de downtrend, est en cours. La plupart des traders utilisent d'autres indicateurs techniques (et fondamentaux) en plus du Golden Cross pour confirmer cette lecture.
**TRADEX-AI C1** : Le Golden Cross sur GC/HG/CL/ZW est un facteur de confirmation dans la grille /10 — jamais seul, toujours combiné avec les 7 cercles.
*Catégorie : indicateurs_tendance*

### D4554 — Golden Cross comme signal d'entrée long
🔵 **ÉCOLE** (Source : trading_using_the_golden_cross.md) : Le Golden Cross peut être utilisé comme signal d'entrée long dans le marché — bien que de nombreuses méthodes nuancées existent pour entrer en position longue.
**TRADEX-AI C1** : Sur TRADEX, le Golden Cross peut être intégré comme condition préalable (filtre) pour autoriser un signal ACHAT — jamais seul, mais en conjonction avec les 7 cercles.
*Catégorie : gestion_risque_entree*

### D4555 — SMA50 comme niveau de stop-loss
🔵 **ÉCOLE** (Source : trading_using_the_golden_cross.md) : De nombreux investisseurs utilisent la SMA50 comme niveau de stop-loss, supposant qu'une clôture sous la SMA50 peut signaler que le trend haussier d'un actif est remis en question. La même hypothèse s'applique à la SMA200 selon le timeframe.
**TRADEX-AI C1** : Sur TRADEX, la SMA50 et la SMA200 sur GC/HG/CL/ZW constituent des références de stop structurel — à utiliser avec d'autres indicateurs pour distinguer un retournement long terme d'une correction exagérée.
*Catégorie : gestion_risque_entree*

### D4556 — Importance du contexte et de l'action des prix
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md) : Les conditions de marché et l'action des prix entourant un Golden Cross sont aussi importantes que le signal lui-même. Tous les Golden Crosses ne sont pas identiques.
**TRADEX-AI C1** : Le contexte de marché (C4 Macro, C5 Sentiment, C6 Géopolitique) doit toujours entourer l'analyse d'un Golden Cross sur TRADEX — le signal isolé est insuffisant.
*Catégorie : gestion_risque_entree*

### D4557 — Attention au volume décroissant après Golden Cross
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md) : Si l'activité acheteuse et le volume se tarissent après un Golden Cross, il faut chercher à comprendre pourquoi le momentum haussier semble s'affaiblir — manque de conviction des bulls ? Plusieurs raisons techniques et fondamentales peuvent conduire à une réaction indécise.
**TRADEX-AI C2** : Un Golden Cross sur GC/HG/CL/ZW suivi d'un volume décroissant (C2 OrderFlow) réduit la fiabilité du signal ACHAT — condition d'invalidation partielle dans la grille /10.
*Catégorie : volume_liquidite*

### D4558 — Type 1 Golden Cross : prix étendu du point de croisement
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md, image_PO2ZlgqPvxFNMcQQUEar) : Type 1 Golden Cross (McClellan) : les prix sont étendus loin du point de croisement réel dans la direction du croisement — peut marquer un retournement temporaire ou plus significatif.
**TRADEX-AI C1** : Un Golden Cross de Type 1 sur GC/HG/CL/ZW (prix déjà très haut au moment du croisement) arrive en retard — signal moins fiable, potentiellement proche d'un retournement temporaire à la baisse.
*Catégorie : indicateurs_tendance*

### D4559 — Type 2 Golden Cross : reprise de tendance précédente
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md, image_2QtWU85tvfNiEavxAZhI) : Type 2 Golden Cross (McClellan) : les prix reviennent au prix réel du point de croisement — indique souvent une reprise du trend précédant le croisement.
**TRADEX-AI C1** : Un Golden Cross de Type 2 sur GC/HG/CL/ZW (prix revenant au niveau du croisement) peut signaler une continuation haussière solide après retour sur le point de croisement — signal plus fiable que le Type 1.
*Catégorie : indicateurs_tendance*

### D4560 — Golden Cross comme signal de début de tendance haussière depuis range ou downtrend
🟢 **FAIT VÉRIFIÉ** (Source : trading_using_the_golden_cross.md) : Quand un Golden Cross se produit, il signale qu'un uptrend peut émerger depuis un downtrend ou un range de trading latéral.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un Golden Cross après une période de range ou de baisse constitue un signal de changement de conditions de marché — à pondérer dans la grille /10.
*Catégorie : structure_marche*

### D4561 — Incapacité du Golden Cross à prédire avec fiabilité en début d'occurrence
🟡 **SYNTHÈSE** (Source : trading_using_the_golden_cross.md) : Tôt dans son occurrence, le Golden Cross ne peut pas prévoir la hausse avec un degré de précision fiable — il peut donner un signal précoce que l'environnement de marché plus haussier peut se matérialiser avec la bonne convergence de facteurs techniques et fondamentaux.
**TRADEX-AI C1** : Dans TRADEX, le Golden Cross récent (moins de 5 barres) est à pondérer avec prudence — attendre confirmation des autres cercles (C2 à C7) avant de valider un signal ACHAT.
*Catégorie : indicateurs_tendance*

### D4562 — Symétrie Death Cross / Golden Cross
🔵 **ÉCOLE** (Source : trading_using_the_golden_cross.md) : Le Golden Cross est la partie positive de son double négatif (le Death Cross), qui indique exactement l'opposé. Les deux patterns sont miroir l'un de l'autre dans leur interprétation.
**TRADEX-AI C1** : TRADEX utilise les deux patterns (Golden Cross et Death Cross) comme des filtres directionnels symétriques sur GC/HG/CL/ZW — haussier vs baissier selon la position relative SMA50/SMA200.
*Catégorie : indicateurs_tendance*
