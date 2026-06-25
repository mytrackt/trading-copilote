# Extraction StockCharts — P&F Catapults
**Source :** `bundles/stockcharts/p_and_f_catapults.md` (HTTP 200 · ~9 143 car.) + 4 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D2871 → D2890 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-catapults
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Bullish Catapults can be reversal or continuation patterns. | Bullish Catapult | CERTIFIE (accord .md + HTML) |
| image_02.png | Bearish Catapult pattern consisting of a Triple Top Breakdown and a Double Bottom Breakdown. | Bearish Catapult | CERTIFIE (accord .md + HTML) |
| image_03.png | A classic Bearish Catapult P&F pattern. | Bearish Catapult | CERTIFIE (accord .md + HTML) |
| image_04.png | A possible Bearish Catapult P&F pattern unfolding. | The Takeaway | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2871 — Catapult P&F : définition (deux signaux consécutifs dans la même direction)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md) : Les P&F Catapults se forment avec deux signaux P&F consécutifs dans la même direction. Un Bullish Catapult typique forme un Triple Top Breakout, un pullback, puis un Double Top Breakout. Un Bearish Catapult typique forme un Triple Bottom Breakdown, un rebond (bounce), puis un Double Bottom Breakdown. La capacité à continuer dans la direction après le repli montre la force (haussier) ou la pression vendeuse renouvelée (baissier).
**TRADEX-AI C1** : Pattern composite codable — deux signaux P&F même sens séparés par un repli contraire. Confirmation de signal renforcée. Base d'un détecteur de catapult.
*Catégorie : structure_marche*

---

### D2872 — Bullish Catapult : structure (breakout initial + pullback + 2nd breakout)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_01) : Un Bullish Catapult se forme avec un breakout initial, un court pullback, et un second breakout. L'idéal débute par un Triple Top Breakout, mais Quadruple Top ou Multiple Top Breakouts sont aussi possibles. Le breakout initial est généralement de seulement 1-3 boxes : les prix montent juste assez pour casser la résistance, avec peu de hausse ensuite.
**TRADEX-AI C1** : Séquence codable — breakout (Triple/Quadruple/Multiple Top) de 1-3 boxes, puis pullback, puis Double Top Breakout. Conditions de détection.
*Catégorie : structure_marche*

---

### D2873 — Bullish Catapult : le pullback ne casse PAS le low du pattern
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_01) : Après le Triple Top Breakout initial, un 3-box reversal forme une nouvelle O-Column qui redescend DANS le pattern Triple Top. Ce n'est qu'un pullback car la O-Column ne casse PAS sous le low du pattern et ne forge PAS de Double Bottom Breakdown. Les prix repartent ensuite à la hausse avec une nouvelle X-Column dépassant la X-Column antérieure pour compléter le catapult (Double Top Breakout).
**TRADEX-AI C1** : Critère d'invalidation/validation — le pullback doit rester au-dessus du low du pattern (sinon ce n'est plus un catapult mais un échec). Le 2e Double Top Breakout complète le pattern.
*Catégorie : structure_marche*

---

### D2874 — Bullish Catapult : sens psychologique (indécision surmontée)
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_catapults.md) : Le pullback dans le pattern représente l'indécision parmi les acheteurs (bulls). La capacité à surmonter cette indécision avec un autre breakout montre une force renouvelée.
**TRADEX-AI C5/C1** : Lecture psychologique — le catapult traduit une indécision résolue en faveur des acheteurs ; renforce la conviction du signal haussier. Métadonnée de confiance.
*Catégorie : structure_marche*

---

### D2875 — Bullish Catapult : reversal ou continuation selon la tendance antérieure
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_01) : Comme la plupart des patterns P&F, les catapults peuvent être reversal ou continuation selon la tendance antérieure. Exemple : le premier Bullish Catapult a renversé un downtrend (Spread Triple Top Breakout en février 2009 + Double Top Breakout en mars ; breakout 1-box, pullback tenu au-dessus du low de l'O-Column précédente). Le second : Multiple Top Breakout + pullback de 4 boxes + Double Top Breakout. Le troisième : catapult classique dans un uptrend = continuation.
**TRADEX-AI C1** : Classification contextuelle — étiqueter le catapult reversal/continuation d'après l'amont. Plusieurs variantes de breakout initial admises (Spread/Multiple).
*Catégorie : structure_marche*

---

### D2876 — Bearish Catapult : structure (breakdown initial + bounce + 2nd breakdown)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_02) : Un Bearish Catapult se forme avec un breakdown initial, un court rebond (bounce), et un second breakdown. L'idéal débute par un Triple Bottom Breakdown, mais Quadruple ou Multiple Bottom Breakdowns sont possibles. Le breakdown initial est généralement de 1-3 boxes seulement. Un 3-box reversal forme alors une nouvelle X-Column qui remonte dans le pattern Triple Bottom.
**TRADEX-AI C1** : Symétrique baissier de D2872 — breakdown (Triple/Quadruple/Multiple Bottom) 1-3 boxes, bounce, puis Double Bottom Breakdown. Conditions miroir.
*Catégorie : structure_marche*

---

### D2877 — Bearish Catapult : le bounce est faible (ne casse PAS le high du pattern)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_02) : Le rebond est faible car la X-Column ne casse PAS au-dessus du high du pattern et ne forge PAS de Double Top Breakout. Les prix repartent ensuite à la baisse avec une nouvelle O-Column dépassant la O-Column antérieure pour compléter le catapult (Double Bottom Breakdown). Le bounce montre les acheteurs tentant un dernier essai ; sa faiblesse + le 2e breakdown mettent les vendeurs en plein contrôle.
**TRADEX-AI C1** : Critère codable — le bounce doit rester sous le high du pattern (sinon le catapult est annulé). Le 2e Double Bottom Breakdown confirme le contrôle baissier.
*Catégorie : structure_marche*

---

### D2878 — Bearish Catapult : exemple reversal FedEx (inclut le high → reversal)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_02) : Exemple FedEx (FDX) — Bearish Catapult composé d'un Triple Top Breakdown et d'un Double Bottom Breakdown. Parce que le pattern inclut le high à 97, il est considéré comme un pattern de reversal. Le bounce a porté jusqu'au high antérieur (X-Column) sans le dépasser, ce qui aurait annulé le pattern.
**TRADEX-AI C1** : Cas concret reversal — le catapult est reversal s'il englobe le high majeur ; le bounce touchant sans dépasser le high antérieur valide le pattern. Critère de classification.
*Catégorie : structure_marche*

---

### D2879 — Bearish Catapult : exemple continuation Unum Group
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_03) : Exemple Unum Group (UNM) — Bearish Catapult classique considéré comme pattern de continuation baissière, car les breakdowns sont survenus après quelques Double Bottom Breakdowns et le high s'est formé avant ce pattern.
**TRADEX-AI C1** : Cas concret continuation — catapult baissier précédé de Double Bottom Breakdowns et high formé en amont = continuation. Complète D2878 (paire reversal/continuation).
*Catégorie : structure_marche*

---

### D2880 — Catapult : Horizontal Count = méthode d'objectif préférée
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md) : La Horizontal Count Method est la méthode préférée pour ces patterns. La largeur du pattern est multipliée par la box size et le reversal amount pour former une extension estimée. Ce résultat est ajouté au low d'un Bullish Catapult, ou soustrait du high d'un Bearish Catapult, pour obtenir un Price Objective. Les Price Objectives ne sont pas des cibles dures : ce sont des estimations approximatives (guesstimate).
**TRADEX-AI C1** : Formule codable — PO_haussier = low + (largeur × box × reversal) ; PO_baissier = high − (largeur × box × reversal). Cible directionnelle du catapult.
*Catégorie : gestion_risque_entree*

---

### D2881 — Catapult : worst-case level = box sous le low du pattern
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md) : Les chartistes doivent aussi évaluer le risque : un mouvement sous le support ou le low du pattern annule clairement un breakout. La box juste sous le low du pattern marque souvent le niveau worst-case d'un échec. De même, un Double Bottom Breakdown ou un pattern P&F contradictoire imposent une réévaluation. Il y a parfois des indices d'échec avant d'atteindre le worst-case.
**TRADEX-AI C1** : Niveau d'invalidation/stop codable — box sous le low du pattern ; signal opposé ou pattern contradictoire = réévaluation. Base du R/R catapult.
*Catégorie : gestion_risque_entree*

---

### D2882 — Catapult : autres outils AT pour mesurer le risque
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_catapults.md) : Les chartistes doivent employer d'autres techniques d'analyse technique pour mesurer le risque et surveiller la tendance qui se déroule.
**TRADEX-AI C1** : Garde-fou — ne pas isoler le catapult ; croiser avec d'autres cercles d'intelligence pour le risque. Aucune exécution automatique sur catapult seul.
*Catégorie : gestion_risque_entree*

---

### D2883 — Catapult : largeur ≥ 7 colonnes (au-dessus de la moyenne P&F)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md) : Les Bullish et Bearish Catapults font au moins sept colonnes de large, ce qui les place au-dessus de la moyenne en largeur pour les patterns P&F. La largeur est un aspect important : des patterns plus larges indiquent une phase de congestion plus longue, rendant le breakout/breakdown subséquent plus important.
**TRADEX-AI C1** : Constante de largeur (≥ 7) → pondération de fiabilité élevée ; paramètre du horizontal count (D2880). Filtre de pertinence du pattern.
*Catégorie : structure_marche*

---

### D2884 — Catapult : anticipation possible via le 3-box reversal (7e colonne)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_catapults.md, image_04) : Il est parfois possible d'anticiper un catapult avec le 3-box reversal qui forme la dernière colonne — la 7e colonne d'un catapult classique. Exemple FedEx : après un Triple Top Breakdown, le titre rebondit dans le pattern avec une X-Column de 4 boxes ; le prochain 3-box reversal vers le bas (O-Column) peut servir à anticiper une faiblesse supplémentaire sous l'O-Column antérieure. Il faudrait une O-Column de 5 boxes pour forger un Double Bottom Breakdown et compléter le Bearish Catapult (red dots).
**TRADEX-AI C1** : Logique d'anticipation codable — détecter le 3-box reversal de la 7e colonne pour pré-signaler un catapult avant sa complétion. Signal précoce (à confirmer par le breakdown final).
*Catégorie : signal*

---

### D2885 — Catapult : référence livresque (Dorsey, Point & Figure Charting)
🟡 **CONVENTION (référence)** (Source : p_and_f_catapults.md) : Le livre de Thomas Dorsey, *Point & Figure Charting*, examine les idées de base et patterns clés des charts P&F, avec un chapitre complet sur la force relative (relative strength), liée aux indicateurs de marché et outils de rotation sectorielle ; il traite aussi de l'usage des charts P&F avec les ETFs.
**TRADEX-AI C1** : Source de référence canonique du P&F (Dorsey) ; piste d'enrichissement futur (relative strength, rotation sectorielle). Pas de règle directe.
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2871 → D2885 (15) |
| Images certifiées | 4/4 |
| Cercle | C1 (structure de marché / prix) — D2874 touche aussi C5 (sentiment) |
| Catégories | structure_marche (9) · gestion_risque_entree (4) · signal (1) · configuration (1) |
| Actifs concernés | GC · HG · CL · ZW (patterns P&F génériques applicables) |
| Lien Belkhayate | NON CONCERNÉ (P&F = méthode Dorsey/Cohen, hors corpus Belkhayate) |
| Tags utilisés | 🟢 FAIT VÉRIFIÉ (11) · 🔵 ÉCOLE (3) · 🟡 CONVENTION (1) |
| Cas à vérifier | Aucun — 4/4 images certifiées, contenu littéral sans ambiguïté |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
