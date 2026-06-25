# Extraction StockCharts — McClellan Summation Index

**Source :** `bundles/stockcharts/mcclellan_summation_index.md` (HTTP 200 · ~8 200 car.) + 8 images certifiées
**Méthode images :** double ancrage v3 · 8/8 certifiées
**Décisions :** D2591 → D2603 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/mcclellan-summation-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

> Pertinence futures LIMITÉE : indicateur de breadth ACTIONS (NYSE/Nasdaq), version moyen/long terme du McClellan Oscillator. Pour TRADEX-AI, valeur = sentiment/confirmation marché actions US via ES (C5) ; aucun ordre direct sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Calculating the McClellan Summation Index | Calculating the McClellan Summation Index [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_02.png | Nasdaq Negative Bias | Nasdaq Negative Bias [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_03.png | Nasdaq Negative Bias | Nasdaq Negative Bias [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_04.png | Positive vs. Negative | Positive vs. Negative [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_05.png | Positive vs. Negative | Positive vs. Negative [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_06.png | Directional Movement | Directional Movement [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_07.png | Divergences | Divergences [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |
| image_08.png | SharpCharts | SharpCharts [SECTION-FALLBACK] | CERTIFIÉ (.md + HTML) |

## DÉCISIONS

### D2591 — Nature : cumul du McClellan Oscillator
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « Developed by Sherman and Marian McClellan, the McClellan Summation Index is a breadth indicator derived from the McClellan Oscillator (…). The Summation Index is simply a running total of the McClellan Oscillator values. Even though it is called a Summation Index, the indicator is really an oscillator that fluctuates above and below the zero line. »
**TRADEX-AI C5** : total courant (cumul) du McClellan Oscillator → oscillateur de breadth oscillant autour de zéro. Vision lissée du sentiment marché actions.
*Catégorie : signal*

---

### D2592 — Calcul cumulatif (somme précédente + oscillateur du jour)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_01) : « Previous day's Summation Index + current day McClellan Oscillator. The very first Summation Index is simply the value of the McClellan Oscillator. »
**TRADEX-AI C5** : formule déterministe simple — cumul récursif. Reproductible une fois le McClellan Oscillator disponible. image_01 = exemple de calcul.
*Catégorie : signal*

---

### D2593 — Deux variantes : traditionnelle vs ratio-ajustée
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « StockCharts.com provides two options (…) unadjusted and ratio-adjusted. (…) Ratio-adjusted Net Advances equals Net Advances divided by advances plus declines (…) makes it possible to compare values over a long period. This article focuses on the Ratio-adjusted Summation Index. »
**TRADEX-AI C5** : version ratio-ajustée privilégiée (comparable sur longue période), cohérente avec le McClellan Oscillator ratio-ajusté (cf. extraction dédiée).
*Catégorie : structure_marche*

---

### D2594 — Horizon moyen/long terme (plus lent, moins de signaux)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « Because of its cumulative nature, the Summation Index is a slower version of the McClellan Oscillator. The index crosses the zero line fewer times, forms divergences less often, and produces fewer signals (…). the Summation Index is generally used for medium-term and long-term timing. »
**TRADEX-AI C5** : Summation Index = timing moyen/long terme (lent, peu de signaux), complément du McClellan Oscillator (court/moyen terme). Lecture de régime de fond.
*Catégorie : timing*

---

### D2595 — Trois signaux de base (biais, divergences, mouvement directionnel)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « First, the Summation Index generally favors the bulls when positive and the bears when negative. Second, chartists can look for bullish and bearish divergences (…). Third, chartists can identify directional movement to define a bullish or bearish bias. »
**TRADEX-AI C5** : taxonomie des signaux = (1) signe positif/négatif = biais, (2) divergences, (3) mouvement directionnel. Cadre sentiment de fond.
*Catégorie : signal*

---

### D2596 — Biais baissier structurel du Nasdaq Summation Index
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_02, image_03) : « the Nasdaq Summation Index has a long-term downward bias. This is because the Nasdaq AD Line also has a long-term downward bias. This bias stems from listing requirements that are not as stringent as NYSE (…). Companies that fail are ultimately removed from the index, but their negative effect on these breadth indicators remains. »
**TRADEX-AI C5** : garde-fou — le Summation Index Nasdaq porte un biais baissier de long terme (delistings) ; comparer NYSE et Nasdaq, ne pas lire un négatif Nasdaq comme un signal baissier brut. images 02/03 = $NASI vs $NYSI 2002-2010.
*Catégorie : structure_marche*

---

### D2597 — Le biais n'affecte pas le court/moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « This negative bias does not affect short-term or medium-term movements, but it is clearly visible on long-term charts. (…) the Nasdaq Summation Index spent more time in negative territory (…) despite a multi-year uptrend in the Nasdaq. »
**TRADEX-AI C5** : le biais Nasdaq est un artefact LONG terme ; les mouvements court/moyen terme restent exploitables. Nuance d'interprétation.
*Catégorie : structure_marche*

---

### D2598 — Biais bull/bear via la ligne zéro (persistance requise)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_04) : « the Summation Index provides a bullish or bearish bias when it is above or below its center line (zero). (…) It takes more than one positive/negative reading to push the Summation Index into positive/negative territory (…) usually takes several positive readings (…). This is why the Summation Index is better suited for medium-term or long-term analysis. »
**TRADEX-AI C5** : franchissement de zéro = bascule de biais, mais nécessite une accumulation de lectures de même signe → signal de fond, peu réactif.
*Catégorie : signal*

---

### D2599 — Seuils ±500 : moins de signaux, captures de tendances longues
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_05) : « the bullish threshold is set at +500 and the bearish threshold is set at -500. A long-term bull signal is triggered when (…) above +500 and remains valid until (…) below -500 (…). Instead of 10 signals in three years using the zero cross, there were only two signals using the +500/-500 cross. » Zones 300-500 jouant résistance, -300/-500 jouant support.
**TRADEX-AI C5** : seuils alternatifs ±500 (au lieu de zéro) = filtre fort réduisant fortement le nombre de signaux et capturant les tendances longues. Paramètre de régime.
*Catégorie : signal*

---

### D2600 — Mouvement directionnel via moyenne mobile (5 j vs 20 j)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_06) : « A moving average can be applied to the Summation Index to identify upturns and downturns. A short moving average (5-days) will generate quicker signals, but there will be more whipsaws. A longer moving average (20-days) will lag (…) fewer whipsaws. (…) The orange areas highlight whipsaws when there were three moving average crosses within a relatively short timeframe. »
**TRADEX-AI C5** : appliquer une MA (5 j rapide/bruitée, 20 j lente/propre) pour timer les retournements du Summation Index — arbitrage vitesse/whipsaws classique.
*Catégorie : timing*

---

### D2601 — Divergences : définition et filtrage (robustes vs faibles)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_07) : « A bullish divergence occurs when the Summation Index forms a higher low and the index forms a lower low (…). A bearish divergence forms when the Summation Index records a lower high and the index forges a higher high (…). bearish divergences in a strong uptrend are more likely to fail (…). Shallow divergences that form over a few weeks are more suspect than steep divergences that form over 1-4 months. »
**TRADEX-AI C5** : divergences = breadth améliorant/détériorant vs prix ; ne retenir que les divergences raides sur 1-4 mois, confirmées (ex. franchissement de la SMA 20 j). Garde-fou anti-faux-signaux.
*Catégorie : signal*

---

### D2602 — Trois dérivées de calcul (recul vs Net Advances) — « Bottom Line »
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md) : « it takes three separate calculations to produce Summation Index values. The first derivatives are the 19-day EMA and 39-day EMA of Net Advances. The second derivative is the McClellan Oscillator (…). The third derivative is the Summation Index (…). Each additional calculation changes Net Advances from its original form. (…) Summation Index signals should be confirmed with other indicators. »
**TRADEX-AI C5** : le Summation Index est à TROIS dérivées des Net Advances → très éloigné de la donnée brute ; à confirmer par d'autres outils. Garde-fou d'usage.
*Catégorie : signal*

---

### D2603 — Symboles SharpCharts ($NYSI/$NASI ; $NYSIT/$NASIT) et plot + SMA 20
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_summation_index.md, image_08) : « plot the Ratio-Adjusted Summation Index for the NYSE ($NYSI) or the Nasdaq ($NASI). The traditional (unadjusted) Summation Index symbols are $NYSIT and $NASIT (…). A 20-day SMA was added to the Summation Index to identify turns. »
**TRADEX-AI C5** : tickers — $NYSI/$NASI (ratio-ajustés) vs $NYSIT/$NASIT (traditionnels) ; affichage standard avec SMA 20 j pour repérer les retournements. Détail outillage/données.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| # | Décision | Cercle | Catégorie | Tag |
|---|----------|--------|-----------|-----|
| D2591 | Nature : cumul du McClellan Oscillator | C5 | signal | 🟢 |
| D2592 | Calcul cumulatif (somme veille + oscillateur jour) | C5 | signal | 🟢 |
| D2593 | Variantes traditionnelle vs ratio-ajustée | C5 | structure_marche | 🟢 |
| D2594 | Horizon moyen/long terme (lent) | C5 | timing | 🟢 |
| D2595 | 3 signaux : biais / divergences / directionnel | C5 | signal | 🟢 |
| D2596 | Biais baissier structurel Nasdaq | C5 | structure_marche | 🟢 |
| D2597 | Biais sans effet court/moyen terme | C5 | structure_marche | 🟢 |
| D2598 | Biais via ligne zéro (persistance requise) | C5 | signal | 🟢 |
| D2599 | Seuils ±500 (filtre tendances longues) | C5 | signal | 🟢 |
| D2600 | MA 5 j vs 20 j pour timer les retournements | C5 | timing | 🟢 |
| D2601 | Divergences : filtrer raides 1-4 mois | C5 | signal | 🟢 |
| D2602 | Trois dérivées des Net Advances (confirmer) | C5 | signal | 🟢 |
| D2603 | Tickers $NYSI/$NASI + SMA 20 | C5 | structure_marche | 🟢 |

**Note de portée :** indicateur de breadth/sentiment ACTIONS moyen/long terme (C5). Pour TRADEX-AI (futures), valeur = confirmation du régime de sentiment marché actions US via ES uniquement ; aucun lien direct avec GC/HG/CL/ZW ni avec la méthode Belkhayate (⚫🔴 non concerné). Garde-fou clé : biais baissier structurel Nasdaq (D2596). 13 décisions, 8/8 images certifiées.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
