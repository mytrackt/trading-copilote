# Extraction StockCharts — TA 101 Part 8 (Trend Lines & Trend Psychology)
**Source :** `bundles/stockcharts/ta_101_part_8.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D4311 → D4330 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-8
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Tendances et lignes de tendance — fondamentaux pour identifier direction sur GC/HG/CL/ZW et confirmer via ES/DX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Trending | Trending | D4311 |
| image_02.png | Trend lines | Trend lines | D4315 |
| image_03.png | Trend lines | Trend lines | D4317 |
| image_04.png | Trend lines | Trend lines | D4319 |

## DÉCISIONS

### D4311 — Définition d'une tendance : mouvement directionnel soutenu des prix
🔵 **ÉCOLE** (Source : ta_101_part_8.md, image_01.png) : Une tendance (trend) est un mouvement de prix directionnel soutenu. Elle peut être vue comme une zone de support/résistance inclinée. Une tendance persiste tant que la peur ou l'avidité domine le marché. Les tendances s'affaiblissent ou changent de direction quand l'équilibre peur/avidité se modifie.
**TRADEX-AI C1** : La Direction Belkhayate (indicateur NT8) mesure directement cette notion de tendance soutenue sur GC/HG/CL/ZW. La présence d'une tendance claire est un prérequis au signal — ATTENDRE en l'absence de tendance définie.
*Catégorie : indicateurs_tendance*

### D4312 — Uptrend : sommets et creux successifs ascendants
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_8.md) : Une tendance haussière (uptrend) est caractérisée par des sommets (peaks) et des creux (troughs) successifs plus hauts. Chaque nouveau sommet dépasse le précédent ; chaque nouveau creux est plus haut que le précédent.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, valider l'uptrend par l'analyse peak/trough en plus de la Direction Belkhayate. Condition nécessaire pour signal Long : le dernier creux doit être plus haut que l'avant-dernier.
*Catégorie : structure_marche*

### D4313 — Downtrend : sommets et creux successifs descendants
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_8.md) : Une tendance baissière (downtrend) est caractérisée par des sommets et des creux successifs plus bas. Chaque nouveau sommet est plus bas que le précédent ; chaque nouveau creux est plus bas que le précédent.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, valider le downtrend par la séquence de peaks/troughs descendants. Condition nécessaire pour signal Short : le dernier sommet doit être plus bas que l'avant-dernier.
*Catégorie : structure_marche*

### D4314 — Trading range : sommets et creux horizontaux
🔵 **ÉCOLE** (Source : ta_101_part_8.md) : Un "trading range" est caractérisé par des sommets et des creux approximativement horizontaux dans le temps. Ce n'est ni une tendance haussière ni baissière — les prix oscillent dans une fourchette latérale. L'avidité et la peur sont en équilibre.
**TRADEX-AI C1** : En trading range sur GC/HG/CL/ZW, le signal TRADEX doit être ATTENDRE sauf en cas de breakout confirmé. La règle 3/4 actifs alignés + 2/3 confirmation évite les faux signaux en range.
*Catégorie : structure_marche*

### D4315 — Classification des tendances par durée : majeure, intermédiaire, mineure
🔵 **ÉCOLE** (Source : ta_101_part_8.md, image_01.png) : Les tendances sont classifiées en trois catégories selon leur durée : majeure (> 6 mois), intermédiaire (1 à 6 mois), mineure (< 1 mois). Les investisseurs long terme s'intéressent aux tendances majeures ; les traders court terme aux tendances mineures et intermédiaires.
**TRADEX-AI C1** : TRADEX-AI opère principalement en tendance intermédiaire et mineure. La tendance majeure sert de filtre directionnel (C1 Belkhayate sur timeframe hebdomadaire). Ne jamais trader contre la tendance majeure sur GC/HG/CL/ZW sauf signal de retournement très fort.
*Catégorie : indicateurs_tendance*

### D4316 — Définition de la ligne de tendance : droite reliant 2+ points extrêmes
🔵 **ÉCOLE** (Source : ta_101_part_8.md, image_02.png) : Une ligne de tendance (trend line) est une droite reliant deux points extrêmes ou plus (bas pour uptrend, hauts pour downtrend) qui s'étend vers le futur pour agir comme support ou résistance. Les deux premiers points établissent la ligne ; les points additionnels la valident.
**TRADEX-AI C1** : Les lignes de tendance Belkhayate (COG channel) sur GC/HG/CL/ZW sont des trend lines dynamiques. La validation par un 3e point augmente significativement la fiabilité du signal d'entrée sur ce niveau.
*Catégorie : indicateurs_tendance*

### D4317 — Ligne de tendance haussière : support dynamique incliné
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_8.md, image_03.png) : Une ligne de tendance haussière (uptrend line) a une pente positive et est formée en reliant 2+ creux ascendants. Elle agit comme support dynamique. Tant que les prix restent au-dessus de la ligne, l'uptrend est intact. Une cassure en dessous signale un affaiblissement de la demande et un possible changement de tendance.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une cassure sous la ligne de tendance haussière (uptrend line Belkhayate) est un signal d'alerte pour clôturer une position Long active. Combiné à Direction Belkhayate basculant négatif = signal de sortie fort.
*Catégorie : gestion_position_active*

### D4318 — Cassure de l'uptrend line : signal de changement de tendance possible
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_8.md, image_03.png) : Une cassure en dessous de la ligne de tendance haussière indique que la demande (buyers) s'est affaiblie et qu'un changement de tendance pourrait être imminent. Ce n'est pas une certitude mais un signal d'alerte fort nécessitant confirmation.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, la cassure de l'uptrend line doit être confirmée par : (1) clôture sous la ligne, (2) volume de la cassure > moyenne, (3) Direction Belkhayate en baisse. Les 3 conditions = signal de sortie/Short validé.
*Catégorie : gestion_position_active*

### D4319 — Ligne de tendance baissière : résistance dynamique inclinée
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_8.md, image_04.png) : Une ligne de tendance baissière (downtrend line) a une pente négative et est formée en reliant 2+ sommets descendants. Elle agit comme résistance dynamique. Tant que les prix restent sous la ligne, le downtrend est intact. Une cassure au-dessus signale une diminution de l'offre et un possible changement de tendance.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une cassure au-dessus de la downtrend line Belkhayate est un signal d'alerte pour couvrir une position Short active. À confirmer avec Direction Belkhayate basculant positif et volume de cassure élevé.
*Catégorie : gestion_position_active*

### D4320 — La vitesse de la tendance révèle l'intensité de la peur/avidité
🟡 **SYNTHÈSE** (Source : ta_101_part_8.md) : L'étendue de la peur et de l'avidité sur un marché peut être observée par la rapidité avec laquelle les prix évoluent en tendance. Une tendance haussière très rapide indique une avidité intense ; une chute rapide indique une peur intense. Les deux extrêmes précèdent généralement un retournement ou un ralentissement.
**TRADEX-AI C1/C5** : Sur GC/HG/CL/ZW, une tendance qui s'accélère brutalement (pente très forte) doit déclencher une vigilance accrue sur le Risk Manager. L'Énergie Belkhayate (stub) capturera cette notion d'intensité. En attendant, utiliser la pente de l'uptrend line comme proxy.
*Catégorie : gestion_risque_entree*
