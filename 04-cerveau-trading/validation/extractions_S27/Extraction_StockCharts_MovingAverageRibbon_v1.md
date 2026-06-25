# Extraction StockCharts — Moving Average Ribbon

**Source :** `bundles/stockcharts/moving_average_ribbon.md` (HTTP 200 · ~4 900 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D2671 → D2681 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-ribbon
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of Moving Average Ribbon overlaid on a price chart. | What Is the Moving Average Ribbon? | CERTIFIE (accord .md + HTML) |
| image_02.png | The Moving Average Ribbon overlay applied to a chart using StockChartsACP. | Using with StockChartsACP | CERTIFIE (accord .md + HTML) |
| image_03.png | Example of the Moving Average Ribbon overlay applied to SharpCharts. | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2671 — Définition : empilement de MA multiples
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md, image_01) : Un Moving Average Ribbon est une représentation graphique de plusieurs moyennes mobiles à périodes de lookback variées tracées sur le même graphique. Il apparaît comme un ruban se déplaçant à travers le graphique, d'où son nom. Ces MA peuvent être analysées séparément ou en groupe pour l'identification de tendance et les signaux de changement de tendance.
**TRADEX-AI C1** : Overlay = faisceau de MA de longueurs croissantes ; lecture de tendance et de retournement par groupe. Implémentable comme overlay multi-MA sur NT8.
*Catégorie : indicateurs_tendance*

---

### D2672 — Calcul : aucune formule spéciale
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Il n'y a pas de formule spéciale ; le ribbon est une méthode rapide pour ajouter plusieurs MA. On détermine le nombre de MA et le nombre de périodes de chacune. Dans StockChartsACP : spécifier les périodes de la MA la plus courte, l'incrément de périodes entre chaque MA, et le nombre total de MA. On peut choisir le type (SMA ou EMA). Exemple : 8 EMA sur graphique daily, incréments de 10 périodes, de 10 à 80 jours. Chaque MA est calculée avec les formules SMA/EMA standard.
**TRADEX-AI C1** : Paramétrage = (période min, incrément, nombre de MA, type) ; chaque ligne suit la formule MA standard. Directement codable.
*Catégorie : configuration*

---

### D2673 — Interprétation : alignement directionnel = force de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Si toutes les MA se déplacent dans la même direction, cela indique une tendance forte — les lignes court- et long-terme s'accordent sur la direction. Si toutes les lignes du ribbon montent, les prix augmentent sur tous les horizons et le titre est probablement en uptrend (et inversement).
**TRADEX-AI C1** : Signal de force de tendance par consensus directionnel de toutes les MA ; exploitable comme critère de la grille /10.
*Catégorie : indicateurs_tendance*

---

### D2674 — Croisements court/long terme = changement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Si les lignes court-terme croisent au-dessus des lignes long-terme, cela signale un nouvel uptrend ; un downtrend est indiqué quand les MA court-terme croisent sous les long-terme. Les chartistes peuvent aussi guetter les barres de prix croisant au-dessus/au-dessous des diverses MA du ribbon.
**TRADEX-AI signal** : Signal de changement de tendance par croisement court↑/long (haussier) ou court↓/long (baissier) ; candidat marqueur, jamais déclencheur direct d'ordre.
*Catégorie : signal*

---

### D2675 — Lignes parallèles = tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Quand toutes les lignes du ribbon sont parallèles (espacées régulièrement dans le temps), cela indique une tendance forte.
**TRADEX-AI C1** : Le parallélisme et l'espacement régulier des lignes = signature de tendance forte ; mesurable par l'écart-type des écarts inter-MA.
*Catégorie : indicateurs_tendance*

---

### D2676 — Expansion du ruban = possible fin de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Si le ribbon s'élargit (les MA s'éloignent dans le temps), cela peut marquer la fin de la tendance courante.
**TRADEX-AI signal** : L'expansion (divergence) du ruban = signal d'épuisement potentiel de tendance ; à confirmer.
*Catégorie : signal*

---

### D2677 — Contraction du ruban = possible nouvelle tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Si le ribbon se contracte (les MA se rapprochent ou se croisent), cela peut indiquer le début d'une nouvelle tendance.
**TRADEX-AI signal** : La contraction/convergence du ruban = signal de naissance de tendance (souvent zone de croisements) ; à confirmer.
*Catégorie : signal*

---

### D2678 — Réglage de la réactivité (type + périodes)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : La réactivité du ribbon s'ajuste en changeant le type de MA (les EMA répondent plus vite que les SMA équivalentes) et le nombre de périodes (les MA à moins de périodes réagissent plus vite que celles à plus de périodes).
**TRADEX-AI C1** : Deux leviers de réactivité (EMA > SMA en vitesse ; périodes courtes > longues) ; à calibrer selon le mode Belkhayate (Standard 15min / Rapide Range Bar / Scalping).
*Catégorie : configuration*

---

### D2679 — Synthèse d'usage : lecture multi-horizon + multi-indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : Le ribbon permet de voir d'un coup d'œil ce qui se passe en long- et court-terme via tendances et croisements sur diverses périodes ; les expansions/contractions de largeur indiquent force de tendance et changements possibles. Comme tout indicateur technique, le Moving Average Ribbon doit être utilisé **avec d'autres indicateurs et techniques d'analyse**.
**TRADEX-AI C1** : Garde-fou explicite — ne jamais utiliser seul ; combiner avec d'autres signaux dans la grille /10. Lecture multi-horizon en un seul overlay.
*Catégorie : indicateurs_tendance*

---

### D2680 — Paramètres par défaut (ACP et SharpCharts)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md, image_02, image_03) : Sur StockChartsACP l'overlay utilise par défaut **10 SMA, espacées de 5 périodes, de 20 à 65 périodes** ; le type (SMA/EMA), la période la plus courte, le pas (Step) et le nombre de MA sont ajustables. Couleurs par défaut en arc-en-ciel (MA la plus courte en rouge, etc.). SharpCharts n'offre pas d'indicateur ribbon intégré mais on crée le sien en ajoutant plusieurs MA de périodes et couleurs différentes.
**TRADEX-AI C1** : Défauts de référence (10 SMA, pas 5, 20→65) et nomenclature ; base d'implémentation NT8 (recréation manuelle multi-MA si pas d'overlay natif).
*Catégorie : configuration*

---

### D2681 — FAQ : réglages courants et types de MA
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_ribbon.md) : FAQ — un réglage courant est **6 à 8 MA** de longueurs différentes (ex. 10, 20, 30, 40, 50, 60 périodes), les meilleurs réglages variant selon le marché et les préférences du trader. On peut utiliser des SMA ou des EMA. Nouvel uptrend signalé quand les MA court-terme croisent au-dessus des long-terme ; downtrend dans le cas inverse. Réactivité ajustable par type de MA (EMA plus rapide) et nombre de périodes.
**TRADEX-AI configuration** : Plage de réglage usuelle (6-8 MA, ex. 10→60 par pas de 10) confirmée par la FAQ ; redondance utile pour fixer un défaut robuste par actif.
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D2671 → D2681 (11 décisions) |
| Images certifiées | 3/3 |
| Catégories couvertes | indicateurs_tendance · configuration · signal |
| Cercle dominant | C1 (overlay de prix multi-MA / suivi de tendance) |
| Lien Belkhayate | NON CONCERNÉ (overlay MA classique StockCharts ChartSchool, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées. Garde-fou explicite (D2679) : ne jamais utiliser seul, combiner à d'autres signaux. Pas d'overlay ribbon natif SharpCharts/NT8 → recréation manuelle multi-MA |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Overlay d'analyse technique classique (StockCharts ChartSchool), aucun rapport affirmé avec la méthode Belkhayate.
