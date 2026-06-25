# Extraction StockCharts — TA 101 Part 9 (Price Channels & Trend Changes)
**Source :** `bundles/stockcharts/ta_101_part_9.md` (HTTP 200) + 3 images certifiées
**Méthode images :** double ancrage · 3/3 certifiées · 0 à vérifier
**Décisions :** D4331 → D4350 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-9
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Canaux de prix et reconnaissance des changements de tendance — directement applicable COG Belkhayate sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Price Channels | Price Channels | D4331 |
| image_02.png | Trend Changes | Trend Changes | D4336 |
| image_03.png | Uncheck the Adjust For Dividends box to view charts with data unadjusted | Price and Volume Data Adjustments | D4343 |

## DÉCISIONS

### D4331 — Canal de prix : prix bornés par deux lignes de tendance parallèles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_9.md, image_01.png) : Les prix en tendance forment souvent un canal où ils sont délimités en haut et en bas par des lignes de tendance parallèles (price channel). Quand un canal se forme, il est utile de tracer les lignes haute et basse et de surveiller comment les prix restent dans le canal.
**TRADEX-AI C1** : Le COG (Centre of Gravity) Belkhayate est un canal de prix dynamique. Les bandes haute et basse du COG (coefficients 0,618 / 1,618) définissent les bornes du canal sur GC/HG/CL/ZW — directement applicable à cette règle.
*Catégorie : indicateurs_tendance*

### D4332 — Uptrend channel : échec à atteindre la borne haute = affaiblissement
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_9.md, image_01.png) : Si les prix en uptrend n'arrivent pas à atteindre la ligne haute du canal, l'uptrend pourrait s'affaiblir et se préparer à s'inverser. C'est un signal d'alerte précoce avant même la cassure de la borne basse du canal.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, si le prix en uptrend ne parvient pas à toucher la borne haute du COG Belkhayate lors d'un rebond, réduire la taille de position Long et resserrer le stop. Critère d'affaiblissement à intégrer dans la grille /10.
*Catégorie : gestion_position_active*

### D4333 — Cassure au-dessus de la borne haute du canal haussier : deux interprétations
🟡 **SYNTHÈSE** (Source : ta_101_part_9.md) : Si les prix cassent soudainement au-dessus de la borne haute du canal haussier, deux interprétations sont possibles : (1) l'uptrend s'épuise et va s'inverser (extension finale), ou (2) une nouvelle tendance plus abrupte commence. Cette ambiguïté nécessite une confirmation supplémentaire.
**TRADEX-AI C1/C2** : Sur GC/HG/CL/ZW, une cassure de la borne COG haute doit être validée par C2 (volume Order Flow confirme l'élan) avant d'être traitée comme accélération plutôt que comme retournement. Sans volume, présumer l'épuisement.
*Catégorie : gestion_position_active*

### D4334 — Canal baissier : même logique d'affaiblissement et de cassure
🔵 **ÉCOLE** (Source : ta_101_part_9.md) : Un comportement similaire se produit dans les canaux de prix baissiers (downtrend price channels). Un échec à atteindre la borne basse du canal signale un affaiblissement du downtrend. Une cassure sous la borne basse peut signifier soit un épuisement soit une accélération.
**TRADEX-AI C1** : Règle symétrique au canal haussier pour les positions Short sur GC/HG/CL/ZW. Si le prix en downtrend ne touche pas la borne basse du COG, réduire la position Short et surveiller le signal de retournement.
*Catégorie : gestion_position_active*

### D4335 — Les prix en tendance ne peuvent évoluer que dans 3 directions
🔵 **ÉCOLE** (Source : ta_101_part_9.md) : Les prix en tendance ne peuvent que : (1) continuer dans la direction de la tendance, (2) basculer en trading range, ou (3) inverser la direction. Cette trichotomie épuise logiquement toutes les possibilités de sortie d'une tendance.
**TRADEX-AI C1** : Prérequis analytique pour TRADEX-AI : à chaque signal, le système doit évaluer laquelle des 3 trajectoires est la plus probable (score /10). La grille Belkhayate pondère explicitement cette évaluation sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4336 — Début de changement d'uptrend : nouveau sommet similaire ou inférieur au précédent
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_9.md, image_02.png) : Un changement d'uptrend commence quand un nouveau sommet de prix est similaire ou inférieur au sommet précédent. Ce premier signal doit être confirmé par le creux suivant : si ce creux est similaire ou inférieur au creux précédent, le changement de tendance est confirmé.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, surveiller les structures de double top ou de sommet décalé vers le bas comme premier signal de renversement. La confirmation (creux plus bas) déclenche la sortie Long ou l'entrée Short dans TRADEX-AI.
*Catégorie : gestion_position_active*

### D4337 — Confirmation du changement de tendance : le creux suivant valide le retournement
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_9.md, image_02.png) : La règle de confirmation s'applique aussi aux changements de downtrend et de trading range. De nouveaux sommets ou creux rompent le schéma des précédents, et le pic ou creux suivant confirme le changement. Sans cette confirmation, le signal reste ambigu.
**TRADEX-AI C1** : Dans TRADEX-AI, ne pas signaler un changement de tendance sur GC/HG/CL/ZW sans la confirmation du 2e point (peak ou trough suivant). Évite les faux signaux en zone de consolidation.
*Catégorie : gestion_risque_entree*

### D4338 — Changements de downtrend et trading range : même mécanisme de confirmation
🔵 **ÉCOLE** (Source : ta_101_part_9.md) : Les changements de downtrend et de trading range suivent le même principe : un nouveau sommet ou creux rompt le schéma, puis le suivant confirme. Le mécanisme est universel quel que soit le type de tendance précédent.
**TRADEX-AI C1** : Règle universelle applicable sur tous les actifs TRADEX (GC/HG/CL/ZW/ES/DX). La Direction Belkhayate doit changer de signe ET le 2e peak/trough doit confirmer avant de valider le changement de tendance dans la grille /10.
*Catégorie : indicateurs_tendance*

### D4339 — Ajustement des données prix/volume lors de dividendes et distributions
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_9.md, image_03.png) : Quand une entreprise verse un dividende (ex-dividend date), le prix de l'action baisse du montant du dividende. Ce changement artificiel rend les indicateurs techniques invalides si les données ne sont pas ajustées. Les analystes techniques utilisent généralement des données de prix ajustées.
**TRADEX-AI C1** : Pour les futures commodités (GC/HG/CL/ZW), les roll dates (expiration contrats) créent un effet similaire. Les données NT8 doivent être en "continuous adjusted" pour que les indicateurs Belkhayate (COG, BGC) soient valides sur les données historiques.
*Catégorie : volume_liquidite*

### D4340 — Le canal de prix est un outil de surveillance de la santé de la tendance
🟡 **SYNTHÈSE** (Source : ta_101_part_9.md) : Surveiller si les prix restent bien dans le canal (bouncing entre borne basse et borne haute) est un outil de surveillance de la santé de la tendance. Un canal bien respecté indique une tendance saine ; un canal de plus en plus mal respecté indique une dégradation progressive.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, monitorer en temps réel la position du prix dans le canal COG Belkhayate (staleness_monitor équivalent de santé de tendance). Signal ATTENDRE si le prix oscille sans toucher les bandes depuis plus de N barres.
*Catégorie : indicateurs_tendance*
