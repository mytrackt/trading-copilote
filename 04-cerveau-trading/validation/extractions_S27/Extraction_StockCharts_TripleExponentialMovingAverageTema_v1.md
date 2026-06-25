# Extraction StockCharts — Triple Exponential Moving Average (TEMA)
**Source :** `bundles/stockcharts/triple_exponential_moving_average_tema.md` (HTTP 200) + 3 images certifiées
**Méthode images :** double ancrage · 3/3 certifiées · 0 à vérifier
**Décisions :** D4631 → D4650 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/triple-exponential-moving-average-tema.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : overlay de tendance à faible lag applicable sur GC/HG/CL/ZW pour détecter des changements de tendance plus tôt que les EMA/DEMA classiques.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/grlIvnrkgwu4lCvcoV7L | Chart showing two TEMA overlays on a price chart | Présentation générale | D4631 |
| /files/4rVzP8v17g9Z4a8FwbF9 | TEMA crossovers take place earlier than DEMA or EMA crossovers | Interprétation | D4635 |
| /files/WbCGCJz1h5Coc8enEI2n | Add TEMA to StockChartsACP after installing Advanced Indicator Pack | Charting TEMA | D4644 |

## DÉCISIONS

### D4631 — TEMA : définition et objectif
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md, image_grlIvnrkgwu4lCvcoV7L) : Le TEMA (Triple Exponential Moving Average) réduit le lag des EMA traditionnelles, le rendant plus réactif et mieux adapté au trading à court terme. Il a été créé par Patrick Mulloy peu après le DEMA (1994).
**TRADEX-AI C1** : Le TEMA peut être utilisé sur GC/HG/CL/ZW comme overlay de tendance à la place d'une EMA classique pour obtenir des signaux de retournement plus précoces.
*Catégorie : indicateurs_tendance*

### D4632 — TEMA : formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md) : La formule TEMA est : EMA1 = EMA(prix) ; EMA2 = EMA(EMA1) ; EMA3 = EMA(EMA2) ; TEMA = (3 × EMA1) − (3 × EMA2) + EMA3. La formule surpondère les EMA à faible lag.
**TRADEX-AI C1** : Implémenter TEMA dans le moteur Python avec cette formule exacte pour GC/HG/CL/ZW ; paramètre par défaut = 20 périodes, ajustable selon le timeframe NT8.
*Catégorie : indicateurs_tendance*

### D4633 — TEMA vs DEMA : différence principale
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md) : TEMA utilise une EMA triple-lissée en plus des EMA simple et double utilisées dans DEMA. Cela produit une moyenne mobile plus proche des barres de prix que DEMA.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, TEMA sera plus collant au prix que DEMA ; préférer TEMA quand une réactivité maximale est requise, DEMA quand un léger filtrage du bruit est souhaité.
*Catégorie : indicateurs_tendance*

### D4634 — TEMA : usage pour confirmer les tendances
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md) : TEMA est interprété similairement aux EMA traditionnelles mais répond plus vite. Il peut confirmer les tendances et détecter les changements de tendance.
**TRADEX-AI C1** : Dans le cercle C1 de TRADEX-AI, TEMA sur GC/HG/CL/ZW peut servir de filtre directionnel : prix au-dessus du TEMA = tendance haussière, prix en dessous = tendance baissière.
*Catégorie : indicateurs_tendance*

### D4635 — TEMA : croisement comme signal principal
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md, image_4rVzP8v17g9Z4a8FwbF9) : Le signal le plus couramment utilisé est le croisement TEMA. Surveiller le TEMA qui croise les barres de prix ou un TEMA court-terme croisant un TEMA long-terme pour indiquer un changement de tendance. Ex : TEMA 20j au-dessus du TEMA 50j = signal haussier.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un croisement TEMA court/long aligné avec d'autres signaux Belkhayate renforce le score de décision ; intégrer dans la grille /10 comme critère tendance.
*Catégorie : indicateurs_tendance*

### D4636 — TEMA : croisements plus précoces que DEMA ou EMA
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md, image_4rVzP8v17g9Z4a8FwbF9) : Les croisements TEMA (sur le prix ou sur un autre TEMA) se produisent typiquement bien plus tôt que les croisements DEMA ou EMA correspondants.
**TRADEX-AI C1** : Avantage opérationnel sur GC/HG/CL/ZW : un signal TEMA en avance sur l'EMA laisse plus de marge de temps pour préparer l'ordre avant l'entrée optimale selon Belkhayate.
*Catégorie : timing*

### D4637 — TEMA : adaptation des stratégies nécessaire
🔵 **ÉCOLE** (Source : triple_exponential_moving_average_tema.md) : Parce que TEMA réagit plus vite que les EMA traditionnelles, les stratégies de trading doivent être adaptées pour une utilisation avec TEMA.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, calibrer les seuils de confirmation et les timeouts du moteur Python en tenant compte de la réactivité accrue du TEMA ; éviter les faux signaux par sur-réactivité.
*Catégorie : gestion_risque_entree*

### D4638 — TEMA : compromis lag vs bruit
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md) : La réduction du lag et la réactivité accrue rendent TEMA attractif pour les traders court terme. Cependant, un certain lag aide à filtrer le bruit. Les investisseurs long terme préfèrent une moyenne mobile avec plus de lag et moins de bruit.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en intraday (range bars NT8), TEMA est adapté ; sur des timeframes daily ou hebdo pour analyse macro, une EMA ou SMA classique restera préférable pour filtrer le bruit.
*Catégorie : indicateurs_tendance*

### D4639 — TEMA : paramètre par défaut 20 périodes
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md, image_WbCGCJz1h5Coc8enEI2n) : Par défaut, TEMA est calculé sur 20 périodes, mais ce nombre peut être ajusté selon les besoins d'analyse technique.
**TRADEX-AI C1** : Dans les settings TRADEX-AI (`config/settings.py`), paramétrer TEMA_PERIOD = 20 comme défaut pour GC/HG/CL/ZW, avec possibilité d'override par actif.
*Catégorie : indicateurs_tendance*

### D4640 — TEMA : combinaison avec d'autres indicateurs obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : triple_exponential_moving_average_tema.md) : Comme tous les indicateurs techniques, les traders doivent utiliser TEMA en combinaison avec d'autres indicateurs et techniques d'analyse.
**TRADEX-AI C1** : TEMA seul ne constitue pas un signal valide dans TRADEX-AI ; il doit être combiné avec au minimum 2 autres confirmations des 7 cercles pour atteindre le seuil de score ≥ 7,0/10.
*Catégorie : gestion_risque_entree*
