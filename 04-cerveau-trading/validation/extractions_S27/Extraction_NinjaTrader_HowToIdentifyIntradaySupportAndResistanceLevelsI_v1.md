# Extraction NinjaTrader — How to Identify Intraday Support and Resistance Levels
**Source :** `bundles/ninjatrader/how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** figures mentionnées (Fig 1-4) mais non incluses dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7751 → D7770 · **Page :** https://ninjatrader.com/futures/blogs/how-to-identify-intraday-support-and-resistance-levels-in-your-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Méthodes d'identification des S/R intraday (Prior OHLC, Pivot Points, Opening Range, VWAP) — cadre de référence structurel pour Cercle C1.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune — figures référencées mais non incluses dans le bundle) | — | — | — |

## DÉCISIONS

### D7751 — Principe 1 S/R : Role reversal (support cassé → devient résistance, et vice versa)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Premier principe fondamental du S/R — quand un niveau de support est cassé à la baisse, il se transforme en nouveau niveau de résistance ; et inversement. Principe d'inversion des rôles.
**TRADEX-AI C1** : Signaux Belkhayate doivent intégrer le role reversal — un ancien pivot haut cassé devient support sur pullback. Valide la règle d'entrée sur retest.
*Catégorie : structure_marche*

### D7752 — Principe 2 S/R : Testing (les niveaux sont testés plusieurs fois avant de tenir ou casser)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Deuxième principe — les niveaux de S/R sont fréquemment testés plusieurs fois avant soit de tenir ferme, soit d'être franchis. Les tests multiples renforcent la signification du niveau.
**TRADEX-AI C1** : Un niveau Belkhayate testé 2+ fois sans cassure = niveau fort — priorité d'entrée sur 3e test avec alignement 3/4 + 2/3.
*Catégorie : structure_marche*

### D7753 — Principe 3 S/R : Retracement (après cassure d'un niveau, pullback fréquent avant nouvelle tendance)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Troisième principe — après la cassure d'un niveau de S/R clé, le prix revient souvent tester ce même niveau une ou plusieurs fois avant d'amorcer une nouvelle tendance étendue.
**TRADEX-AI C1** : Pullback post-breakout sur niveau Belkhayate cassé = zone d'entrée dans la direction du breakout — confirmation role reversal.
*Catégorie : structure_marche*

### D7754 — Prior Day OHLC : haut/bas/clôture de la veille = S/R intraday naturels
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Les 3 points les plus importants d'une barre journalière sont : le haut (où les acheteurs n'ont plus pu surpasser les vendeurs), le bas (où les vendeurs n'ont plus pu surpasser les acheteurs), la clôture (accord final acheteurs/vendeurs). Ces niveaux agissent souvent comme S/R forts pour la session intraday suivante.
**TRADEX-AI C1** : Prior Day OHLC disponible sur NT8 — intégrer dans le scan initial de chaque session pour GC/HG/CL/ZW comme niveaux de référence structurels.
*Catégorie : structure_marche*

### D7755 — Prior Day High = niveau où les acheteurs ont été vaincus par les vendeurs
🔵 **ÉCOLE** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Le haut de la journée précédente représente exactement le point où les acheteurs n'ont plus pu surmonter la pression vendeuse. Ce niveau est psychologiquement et structurellement significatif.
**TRADEX-AI C1** : Signal haussier TRADEX au-dessus du Prior Day High = cassure de résistance forte — confirmation volume C2 obligatoire pour éviter faux breakout.
*Catégorie : structure_marche*

### D7756 — Pivot Points (Floor Trader Pivots) : 7 niveaux calculés sur High/Low/Close de la veille
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Les Floor Trader Pivots génèrent 7 niveaux S/R calculés sur la base de la plage de trading de la veille et du prix moyen de clôture. Le Pivot central = moyenne (H+L+C) de la veille. Au-dessus : R1, R2, R3. En-dessous : S1, S2, S3. Ces niveaux précalculés servaient de cibles et stops pour les floor traders avant l'ère électronique.
**TRADEX-AI C1** : Pivots Belkhayate (Cercle C1) alignés avec les Floor Trader Pivots = confluence forte — priorité de signal quand les deux systèmes pointent vers le même niveau.
*Catégorie : indicateurs_tendance*

### D7757 — Calcul Pivot Point central : (Haut + Bas + Clôture veille) / 3
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Formule exacte du pivot central : PP = (High_veille + Low_veille + Close_veille) / 3. Les niveaux R1/R2/R3 et S1/S2/S3 sont dérivés de la distance entre PP et la plage de la veille.
**TRADEX-AI C1** : Formule de référence — confirme que les Pivots Belkhayate sont cohérents avec les pivots classiques de la méthode des floor traders.
*Catégorie : indicateurs_tendance*

### D7758 — En journée de news, le prix peut traverser plusieurs niveaux pivots avant de consolider à un extrême
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Lors des jours à forte actualité ou rapports économiques, il est fréquent de voir le prix traverser un ou plusieurs niveaux pivots avant de consolider à un niveau extrême (R3 ou S3).
**TRADEX-AI C4** : News Gate — lors des journées NFP/FOMC/CPI, les pivots perdent temporairement leur fonction S/R. Les signaux basés sur pivots sont invalides 30 min autour des événements majeurs.
*Catégorie : macro_evenements*

### D7759 — Opening Range (30 premières minutes) = hauts/bas critiques pour la session
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : L'Opening Range (tranche de 30 minutes à l'ouverture) correspond à la période où les institutionnels sont les plus actifs et la volatilité des prix est maximale. Le haut et le bas de l'Opening Range deviennent des S/R clés pour le reste de la session. Souvent l'un d'eux devient le haut ou le bas de toute la session.
**TRADEX-AI C2** : Opening Range à surveiller pour GC/CL (actifs institutionnels) — forte participation institutionnelle (Cercle C2) dans les 30 premières minutes.
*Catégorie : timing*

### D7760 — Breakout de l'Opening Range = signal de tendance directionnelle pour la session
🟡 **SYNTHÈSE** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Quand le prix casse au-dessus du haut ou en-dessous du bas de l'Opening Range, cela signale un potentiel trade tendanciel. En l'absence de breakout, le prix oscille souvent entre les deux extrêmes de l'Opening Range.
**TRADEX-AI C1** : Stratégie d'ouverture TRADEX : attendre la formation de l'Opening Range (30 min) avant le premier signal de la session — évite les faux départs.
*Catégorie : timing*

### D7761 — VWAP avec bandes d'écart-type = S/R dynamiques ajustés à la volatilité
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Calcul VWAP : somme(prix × volume de chaque trade) / volume total = prix moyen pondéré en cours de session. L'ajout de bandes d'écart-type (SD) au-dessus/en-dessous du VWAP fournit des niveaux de S/R dynamiques qui s'ajustent automatiquement aux changements de volatilité.
**TRADEX-AI C2** : VWAP + SD disponibles sur NT8 — les bandes d'écart-type constituent des zones de mean reversion que le Cercle C1 (COG Belkhayate) peut confirmer.
*Catégorie : indicateurs_tendance*

### D7762 — Principe de convergence : plusieurs indicateurs S/R sur le même niveau = niveau plus fort
🟢 **FAIT VÉRIFIÉ** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Un élément commun à tous ces indicateurs : les niveaux de S/R se produisent généralement aux mêmes prix, quelle que soit l'unité de temps du graphique. Quand plusieurs indicateurs différents convergent vers le même niveau de prix, ce niveau est considéré comme plus fort.
**TRADEX-AI C1** : Règle de confluence TRADEX : un niveau où Prior OHLC + Pivot + VWAP + Belkhayate convergent = zone d'entrée prioritaire. Score de confiance élevé pour Claude API.
*Catégorie : structure_marche*

### D7763 — Niveaux S/R = éléments critiques pour déterminer entrées et sorties
🔵 **ÉCOLE** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Que l'on soit day trader ou swing trader, comprendre les niveaux de S/R est fondamental pour déterminer les points d'entrée et de sortie. L'analyse S/R aide à identifier les ruptures et retournements potentiels.
**TRADEX-AI C1** : Les niveaux S/R sont la base structurelle du Cercle C1 de TRADEX-AI — tout signal Belkhayate est ancré sur un niveau de S/R identifié.
*Catégorie : structure_marche*

### D7764 — Prior Day Low = niveau où les vendeurs ont été vaincus par les acheteurs
🔵 **ÉCOLE** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Le bas de la journée précédente représente le point où les vendeurs n'ont plus pu surpasser la pression acheteuse. Niveau de support structurel naturel pour la session suivante.
**TRADEX-AI C1** : Signal baissier TRADEX en-dessous du Prior Day Low = cassure de support fort — confirmation volume C2 obligatoire avant entrée short sur GC/HG/CL.
*Catégorie : structure_marche*

### D7765 — Pivot Points : originellement calculés par les floor traders avant l'ère électronique
🔵 **ÉCOLE** (Source : how_to_identify_intraday_support_and_resistance_levels_in_your_trading.md) : Les Pivot Points sont nés sur les parquets de trading (floor traders) qui calculaient manuellement les niveaux du lendemain avec les données H/L/C de la veille. Ces niveaux précalculés servaient de cibles et stops dès l'ouverture du marché suivant.
**TRADEX-AI C1** : Valeur historique des Pivots confirmée par leur persistance dans le temps — leur efficacité ne repose pas sur l'informatique mais sur la psychologie collective des traders qui y réagissent.
*Catégorie : psychologie*
