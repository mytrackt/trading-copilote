# Extraction StockCharts — Advance-Decline Volume Line

**Source :** `bundles/stockcharts/advance_decline_volume_line.md` (HTTP 200 · ~9 100 car.) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées
**Décisions :** D531 → D539 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/advance-decline-volume-line
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | How Do You Calculate the AD Volume Line? | How Do You Calculate the AD Volume Line? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | How Do You Calculate the AD Volume Line? | How Do You Calculate the AD Volume Line? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Bullish Divergence | Bullish Divergence [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Bearish Divergence | Bearish Divergence [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | Large-Cap Bias | Large-Cap Bias [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | SharpCharts | SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | SharpCharts | SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D531 — Définition : AD Volume Line = breadth basé sur Net Advancing Volume
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md) : « The Advance-Decline Volume Line (AD Volume Line) is a breadth indicator based on Net Advancing Volume, which is the volume of advancing stocks less the volume of declining stocks. Net Advancing Volume is positive when advancing volume exceeds declining volume and negative when declining volume exceeds advancing volume. »
**TRADEX-AI C5** : Indicateur de souffle de marché actions (sentiment interne) ; alimente potentiellement C5 comme proxy de pression acheteuse/vendeuse macro-actions. *Pertinence limitée futures GC/HG/CL/ZW* : basé sur les volumes d'actions NYSE/Nasdaq, non transposable directement aux contrats à terme matières premières ; utilisable au mieux comme contexte d'appétit risque (lien ES).
*Catégorie : indicateurs_tendance*

---

### D532 — Calcul cumulatif : running total de Net Advancing Volume
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_01, image_02) : « AD Volume Line (previous value) + Net Advancing Volume (current value) » — « As a cumulative indicator, the AD Volume Line is a running total of each period's Net Advancing Volume. The actual value [...] depends on the starting point [...]. The shape and direction of the AD Volume Line are important, not the actual value. » Exemple : 1er jour +1144, 2e jour -1150 → ligne à -6.
**TRADEX-AI C5** : Formule reproductible (cumul) ; seule la forme/direction compte, pas la valeur absolue (donc pas de seuil fixe exploitable). *Pertinence limitée futures* : calcul dépend de statistiques advance-decline d'un univers d'actions inexistant pour un contrat futures isolé ; non implémentable tel quel sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D533 — Lecture : pression acheteuse vs vendeuse, confirmation de l'indice
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md) : « the AD Volume Line measures the buying and selling pressure behind an advance or a decline. The volume behind advancing stocks represents buying pressure, while the volume behind declining stocks represents selling pressure. » « An AD Volume Line that rises and records new highs along with the underlying index shows strong buying pressure. This is bullish. »
**TRADEX-AI C2/C5** : Logique volume-confirme-tendance (lien C2 order flow conceptuel) ; sert à valider/invalider un mouvement de l'indice sous-jacent. *Pertinence limitée futures* : transposable seulement comme analogie au footprint/delta ATAS sur le futures, pas comme indicateur direct ; signal pertinent au niveau indice actions (ES) uniquement.
*Catégorie : structure_marche*

---

### D534 — Divergence haussière : ligne ne fait pas de plus-bas alors que l'indice oui
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_03) : « A bullish divergence forms when the AD Volume Line fails to record a lower low along with the index. This means selling pressure is waning and the decline may be nearing an end. » Exemple Nasdaq janv.-févr. 2010 : indice sous son plus-bas de janvier, ligne en plus-haut → bas important de février, +10 % jusqu'au sommet d'avril.
**TRADEX-AI C5** : Schéma divergence breadth = essoufflement de la pression vendeuse, alerte de retournement à confirmer par une autre analyse. *Pertinence limitée futures* : applicable à l'indice ES (confirmation marchés), pas en signal d'entrée sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D535 — Divergence baissière : ligne fait un plus-bas-plus-haut alors que l'indice fait un plus-haut
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_04) : « Chart 3 shows a bearish divergence [...] in October 2007. The AD Volume Line peaked in early October, but the Nasdaq forged a higher high in late October. The lower high in the AD Volume Line showed weakness in buying pressure [...]. Notice that the AD Volume Line broke support a day before the Nasdaq broke its corresponding support level. »
**TRADEX-AI C5** : Divergence baissière breadth = affaiblissement de la pression acheteuse précédant la baisse ; la ligne peut casser support avant l'indice (signal anticipé). *Pertinence limitée futures* : valable comme alerte sur ES, non transposable en ordre sur futures matières premières.
*Catégorie : signal*

---

### D536 — Analyse graphique classique applicable (MM, supports/résistances)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_03, image_04) : « Normal chart analysis can be applied to the AD Volume Line. Notice how the AD Volume Line broke resistance a few days ahead of the Nasdaq. » « A moving average can be overlaid on the indicator to identify upturns and downturns. Chartists can also use the AD Volume Line to confirm support or resistance breaks in the underlying index. »
**TRADEX-AI C5/C7** : La ligne se traite comme un prix (cassures S/R, moyennes mobiles) et confirme les cassures de l'indice. *Pertinence limitée futures* : technique de confirmation indice (ES), pas un input direct de la grille déterministe Belkhayate sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D537 — Biais large-cap : la ligne reflète surtout les grandes capitalisations
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_05) : « The advance-decline volume statistics favor large-cap stocks [...]. The largest companies account for the most volume. [...] NVIDIA averages over 50 million shares per day [...] a small-cap stock like Super Micro [...] averages just over 3 million shares per day. An advance in NVIDIA adds some 50 million shares to Net Advancing Volume, while an advance in SMCI will add just 3 million. »
**TRADEX-AI C5** : Limite structurelle — la ligne mesure la pression sur les leaders de volume (large caps), pas la largeur réelle du marché ; à interpréter comme proxy « money flow gros porteurs ». *Pertinence limitée futures* : caractéristique propre aux marchés actions ; aucun équivalent direct sur futures.
*Catégorie : structure_marche*

---

### D538 — AD Volume Line sans biais baissier long terme (contrairement à l'AD Line classique Nasdaq)
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md) : « While the Nasdaq AD Line has a long-term downward bias, the AD Volume Line does not share this characteristic. [...] The negative impact on the AD Volume Line is minimal because large caps drive the AD Volume Line. In contrast to small-caps and mid-caps, large-caps are much less likely to go out of business or fail to meet listing requirements. »
**TRADEX-AI C5** : L'AD Volume Line est plus fiable que l'AD Line nombre-de-titres pour le Nasdaq (pas de dérive baissière artificielle due aux radiations de small caps). *Pertinence limitée futures* : nuance interne aux indices actions, sans application aux contrats matières premières.
*Catégorie : indicateurs_tendance*

---

### D539 — Construction SharpCharts et symboles Net Advancing Volume
🟢 **FAIT VÉRIFIÉ** (Source : advance_decline_volume_line.md, image_06, image_07) : « The AD Volume Line can be created on SharpCharts for the Amex, Vancouver, Nasdaq, NYSE or Toronto stock exchanges. [...] enter the symbol for Net Advancing Volume. Second, change the chart "type" to "cumulative" [...]. » Symbole Nasdaq Net Advancing Volume = `$NAUD` (présent dans les liens chart). « Total volume is important, but the balance of volume is more important. »
**TRADEX-AI C5** : Procédure de reconstruction (type cumulatif sur symbole Net Advancing Volume, ex. `$NAUD`) ; principe clé = la balance des volumes prime sur le volume total. *Pertinence limitée futures* : symboles et exchanges propres aux actions ; reproductible seulement pour suivre le contexte indice (ES), pas pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Décision | Sujet | Cercle | Catégorie | Pertinence futures TRADEX |
|----------|-------|--------|-----------|---------------------------|
| D531 | Définition (Net Advancing Volume) | C5 | indicateurs_tendance | Limitée — proxy contexte risque (ES) |
| D532 | Calcul cumulatif | C5 | indicateurs_tendance | Limitée — non implémentable sur futures isolé |
| D533 | Lecture pression acheteuse/vendeuse | C2/C5 | structure_marche | Limitée — analogie footprint, niveau indice |
| D534 | Divergence haussière | C5 | signal | Limitée — alerte ES uniquement |
| D535 | Divergence baissière | C5 | signal | Limitée — alerte ES uniquement |
| D536 | Analyse graphique (MM, S/R) | C5/C7 | indicateurs_tendance | Limitée — confirmation indice |
| D537 | Biais large-cap | C5 | structure_marche | Limitée — propre aux actions |
| D538 | Pas de biais baissier LT | C5 | indicateurs_tendance | Limitée — interne indices actions |
| D539 | Construction SharpCharts / $NAUD | C5 | indicateurs_tendance | Limitée — symboles actions |

**Note transverse :** indicateur de BREADTH volume ACTIONS (NYSE/Nasdaq). Aucune application directe aux futures GC/HG/CL/ZW. Usage maximal = contexte d'appétit pour le risque via l'indice ES (Catégorie 2 CONFIRMATION). Belkhayate NON CONCERNÉ. Aucune décision n'introduit de seuil chiffré directement exploitable (la source insiste : « shape and direction [...] important, not the actual value »).

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. NON fusionné dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur + audit automatique.
