# Extraction StockCharts — TA 101 Part 7 (Support & Resistance)
**Source :** `bundles/stockcharts/ta_101_part_7.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D4291 → D4310 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-7
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Support/Résistance fondamentaux pour GC/HG/CL/ZW — zones d'entrée/sortie et confirmation DX/ES.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Chart Analysis - Support and Resistance | Chart Analysis - Support and Resistance | D4291 |
| image_02.png | Chart Analysis - Support and Resistance | Chart Analysis - Support and Resistance | D4294 |
| image_03.png | Chart Analysis - Support and Resistance | Chart Analysis - Support and Resistance | D4296 |
| image_04.png | Chart Analysis - Support and Resistance | Chart Analysis - Support and Resistance | D4299 |

## DÉCISIONS

### D4291 — Psychologie du marché : peur et avidité pilotent les prix
🔵 **ÉCOLE** (Source : ta_101_part_7.md) : Les prix sont gouvernés par deux émotions humaines fondamentales — la peur et l'avidité (greed). Quand la peur domine, les prix baissent ; quand l'avidité domine, les prix montent. Ce phénomène est appelé "Market Psychology". L'équilibre entre les deux détermine la direction des prix.
**TRADEX-AI C5** : Le VIX mesure directement le niveau de peur du marché — un VIX élevé renforce la probabilité de repli sur GC (refuge) et pression sur CL/HG. À intégrer dans la grille /10 via C5 sentiment.
*Catégorie : psychologie*

### D4292 — Définition du support : zone où les acheteurs entrent pour stopper la baisse
🔵 **ÉCOLE** (Source : ta_101_part_7.md) : Le support est le niveau de prix où des acheteurs "avides" entrent sur le marché pour empêcher une baisse supplémentaire. Le support peut se former à un niveau de prix précis ou, plus fréquemment, dans une zone de prix. Les zones de support peuvent persister plusieurs mois.
**TRADEX-AI C1** : Les pivots Belkhayate et le BGC définissent des zones de support sur GC/HG/CL/ZW. Un test de support avec volume croissant = signal d'entrée Long potentiel (C2 Order Flow confirme).
*Catégorie : structure_marche*

### D4293 — Inversion support→résistance après cassure baissière
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_7.md, image_01.png) : Après la cassure d'un support, les traders qui avaient acheté dans cette zone détiennent des pertes latentes. Pour récupérer leur mise, ils vendent dès que les prix reviennent au niveau de leur achat initial. L'ancienne zone de support devient ainsi une zone de résistance.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, après une cassure baissière d'un pivot Belkhayate, ce niveau devient résistance. Lors d'un rebond technique, ne pas initier de Long si les prix sont bloqués sous ce niveau retourné.
*Catégorie : structure_marche*

### D4294 — Volume by Price : confirmation de la force du support/résistance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_7.md, image_02.png) : L'overlay "Volume by Price" (volume échangé par tranche de prix) illustre concrètement comment un fort support à 24 sur Dover Corp. est devenu une résistance significative quand l'avidité s'est transformée en peur. Plus le volume historique est dense à un niveau, plus le support/résistance est fort.
**TRADEX-AI C2** : Sur ATAS, le profil de volume (Volume Profile) confirme les zones de support/résistance identifiées par les pivots Belkhayate. Un niveau avec fort Volume by Price = zone de confluence haute priorité pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D4295 — Définition de la résistance : zone où les vendeurs entrent pour stopper la hausse
🔵 **ÉCOLE** (Source : ta_101_part_7.md) : La résistance est le niveau de prix où des vendeurs "apeurés" entrent soudainement sur le marché et empêchent les prix de monter davantage. Comme le support, la résistance peut se former à un niveau précis ou dans une zone, et peut tenir plusieurs mois.
**TRADEX-AI C1** : Les zones de résistance Belkhayate (COG upper band, pivots hauts) sur GC/HG/CL/ZW définissent les objectifs de prise de profit pour les positions Long et les niveaux d'entrée pour les positions Short.
*Catégorie : structure_marche*

### D4296 — Inversion résistance→support après cassure haussière
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_7.md, image_03.png) : Si la résistance est cassée, la psychologie de marché fait que l'ancienne zone de résistance devient un support. Les détenteurs qui ont vendu dans la zone de résistance regrettent et souhaitent racheter dès que les prix reviennent à ce niveau. Ce qui semblait trop cher apparaît maintenant comme une opportunité.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, après cassure haussière d'une résistance Belkhayate, le pullback sur ce niveau retourné en support offre une entrée Long à risque maîtrisé. Confirmation requise : C2 (volume du pullback faible) + C1 (BGC haussier).
*Catégorie : gestion_risque_entree*

### D4297 — Volume by Price : vérification du potentiel acheteur sur ancienne résistance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_7.md, image_04.png) : Le SharpChart de Parker Hannifin Corp. illustre la résistance devenant support. Le Volume by Price indique le nombre potentiel d'anciens vendeurs prêts à racheter si l'occasion se présente. Plus ce volume est dense, plus la zone est un support solide.
**TRADEX-AI C2** : Sur ATAS, le profil de volume historique sur une ancienne résistance cassée de GC/HG/CL/ZW valide la solidité du nouveau support. Entrée Long optimale : retest de ce niveau avec volume faible + absorption visible dans le footprint.
*Catégorie : gestion_risque_entree*

### D4298 — Les zones de support/résistance sont plus fiables que les niveaux ponctuels
🔵 **ÉCOLE** (Source : ta_101_part_7.md) : Le support et la résistance se forment plus communément dans une zone de prix (price zone) plutôt qu'à un niveau de prix exact. Cette distinction est fondamentale : chercher une zone, pas un niveau précis, évite les faux signaux causés par les dépassements temporaires (wicks, spikes).
**TRADEX-AI C1** : Les pivots Belkhayate définissent des zones, non des prix exacts. Sur GC/HG/CL/ZW, une tolérance de ±0,1% à ±0,3% autour d'un pivot est nécessaire pour filtrer les faux dépassements intraday.
*Catégorie : gestion_risque_entree*

### D4299 — Durabilité des zones : support/résistance peut tenir plusieurs mois
🔵 **ÉCOLE** (Source : ta_101_part_7.md) : Les zones de support et de résistance peuvent persister pendant plusieurs mois. Cette durabilité dans le temps augmente leur fiabilité — plus une zone a été testée et tenue longtemps, plus elle est significative.
**TRADEX-AI C1** : Sur les marchés de commodités (GC/HG/CL/ZW), les grands niveaux de support/résistance mensuels et trimestriels ont un poids supérieur aux niveaux intraday. Les pivots Belkhayate sur timeframe hebdomadaire ou mensuel sont prioritaires dans la grille /10.
*Catégorie : structure_marche*

### D4300 — La psychologie explique le mécanisme de retournement des niveaux
🟡 **SYNTHÈSE** (Source : ta_101_part_7.md) : L'ensemble du mécanisme support↔résistance est expliqué par la psychologie des participants — les pertes latentes (vendeurs/acheteurs coincés) créent des ordres en attente qui alimentent le retournement des niveaux. Sans cette psychologie collective, les niveaux techniques n'auraient pas de raison de fonctionner.
**TRADEX-AI C5** : Intégrer dans la grille /10 : les niveaux de support/résistance ayant un fort historique de volume représentent des "masses d'ordres latents". Le Volume Profile ATAS (C2) + psychologie marché (C5) convergent pour valider ces niveaux sur GC/HG/CL/ZW.
*Catégorie : psychologie*
