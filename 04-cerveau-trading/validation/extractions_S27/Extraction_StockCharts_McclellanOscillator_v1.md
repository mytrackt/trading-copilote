# Extraction StockCharts — McClellan Oscillator

**Source :** `bundles/stockcharts/mcclellan_oscillator.md` (HTTP 200 · ~8 500 car.) + 8 images certifiées
**Méthode images :** double ancrage v3 · 8/8 certifiées
**Décisions :** D2571 → D2583 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/mcclellan-oscillator
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

> Pertinence futures LIMITÉE : indicateur de breadth ACTIONS (NYSE/Nasdaq). Pour TRADEX-AI, valeur = sentiment/confirmation marché actions US via ES (C5) ; aucun ordre direct sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | McClellan Oscillator - Chart 1 | Calculating the McClellan Oscillator | CERTIFIÉ (.md + HTML) |
| image_02.png | McClellan Oscillator - Chart 2 | Positive vs. Negative | CERTIFIÉ (.md + HTML) |
| image_03.png | McClellan Oscillator - Chart 3 | Positive vs. Negative | CERTIFIÉ (.md + HTML) |
| image_04.png | McClellan Oscillator - SharpCharts | Breadth Thrusts | CERTIFIÉ (.md + HTML) |
| image_05.png | McClellan Oscillator - SharpCharts | Breadth Thrusts | CERTIFIÉ (.md + HTML) |
| image_06.png | McClellan Oscillator - SharpCharts | Divergences | CERTIFIÉ (.md + HTML) |
| image_07.png | McClellan Oscillator - Chart 7 | SharpCharts | CERTIFIÉ (.md + HTML) |
| image_08.png | McClellan Oscillator - SharpCharts | SharpCharts | CERTIFIÉ (.md + HTML) |

## DÉCISIONS

### D2571 — Origine et nature : breadth momentum dérivé des Net Advances
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md) : « Developed by Sherman and Marian McClellan, the McClellan Oscillator is a breadth indicator derived from Net Advances, which is the number of advancing issues less the number of declining issues. Subtracting the 39-day EMA of Net Advances from the 19-day EMA of Net Advances forms the oscillator. (…) the McClellan Oscillator is a momentum indicator that works similar to MACD. »
**TRADEX-AI C5** : oscillateur de largeur de marché (momentum des avances-déclins), construction type MACD sur Net Advances. Mesure de sentiment marché actions, pas signal futures.
*Catégorie : signal*

---

### D2572 — Trois familles de signaux (thrusts, croisements centerline, divergences)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md) : « McClellan Oscillator signals can be generated with breadth thrusts, centerline crossovers and divergences. »
**TRADEX-AI C5** : taxonomie des signaux = (1) breadth thrusts, (2) croisements de la ligne zéro, (3) divergences. Cadre de lecture sentiment.
*Catégorie : signal*

---

### D2573 — Ratio-ajustement (RANA) pour comparabilité temporelle
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md) : « ratio-adjusted (…). Instead of using Net Advances, StockCharts.com calculates Net Advances as a percentage of advances plus declines. The result is then multiplied by 1000 (…). This ratio adjustment makes it possible to compare McClellan Oscillator levels over a period of time. » (le total NYSE est passé de ~2000 titres en 1990-91 à 3000-3600 entre 1998-2010).
**TRADEX-AI C5** : la version ratio-ajustée (RANA) normalise pour le nombre changeant de titres → seuils comparables dans le temps. Version recommandée par StockCharts.
*Catégorie : structure_marche*

---

### D2574 — Formule de calcul (RANA, EMA 19 et 39, facteurs 0,10 / 0,05)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_01) : « RANA : (Advances - Declines)/(Advances + Declines) ; McClellan Oscillator : 19-day EMA of RANA - 39-day EMA of RANA ; 19-day EMA = (Current RANA - Prior EMA) * .10 + Prior EMA ; 39-day EMA = (Current RANA - Prior EMA) * .05 + Prior EMA ; The first EMA calculation is a simple average. » Note : le graphique image_01 utilise $NYAD:$NYTOT en décimal (sans ×1000).
**TRADEX-AI C5** : formule déterministe reproductible (facteurs de lissage 0,10 et 0,05). Codable si breadth NYSE/Nasdaq intégré comme proxy sentiment.
*Catégorie : signal*

---

### D2575 — Lecture type MACD de l'AD Line (positif/négatif)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md) : « Think of the McClellan Oscillator as the MACD for the AD Line (…). positive when the 19-day EMA is above the 39-day EMA. This signals that advances are gaining the upper hand. Conversely, (…) negative when the 19-day EMA is below the 39-day EMA. This signals that declining issues are dominating. (…) generally favors the bulls when positive and the bears when negative. »
**TRADEX-AI C5** : signe de l'oscillateur = biais directionnel du breadth (positif → avances dominent/haussier ; négatif → déclins dominent/baissier). Lecture sentiment marché.
*Catégorie : signal*

---

### D2576 — Persistance positive/négative en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_02, image_03) : « Even though the McClellan Oscillator can be quite volatile, it can also remain positive or negative for extended periods during a strong uptrend or downtrend. » Exemple : positif ~6 semaines fin 2008 (uptrend NY Composite) ; les « blips » faibles ne dépassant pas +50 et durant <2 jours sont jugés non significatifs.
**TRADEX-AI C5** : en régime de tendance forte, l'oscillateur peut rester durablement d'un côté ; les incursions faibles (<±50, <2 j) sont du bruit. Filtre d'interprétation.
*Catégorie : indicateurs_tendance*

---

### D2577 — Zones de conviction ±30 / ±50 / ±100
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_03) : exemple Nasdaq — phase « indécise » où l'oscillateur « did not exceed +30 on the upside or -30 on the downside (…) not much conviction either way » ; phase de vente forte « plunges below -100 (…) signaled the start of an extended decline ».
**TRADEX-AI C5** : repères empiriques d'amplitude — ±30 = indécision, dépassement ±50 = conviction, plongée sous -100 = pression vendeuse extrême annonçant un déclin prolongé.
*Catégorie : signal*

---

### D2578 — Breadth thrust : passage de < -50 à > +50 (~+100 pts)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_04) : « A breadth thrust occurs when the McClellan Oscillator surges from deep negative readings to strong positive readings. Typically, the indicator will move from below -50 and exceed +50 for a +100 point thrust. (…) most important lows are marked by a sharp surge in breadth. A bullish breadth thrust is enhanced when preceded by a bullish divergence. »
**TRADEX-AI C5** : signal de creux majeur = poussée de breadth (< -50 → > +50, ~+100 pts), renforcée si précédée d'une divergence haussière. Marqueur de bottom marché actions.
*Catégorie : signal*

---

### D2579 — Comportement post-thrust : divergences baissières normales
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_05) : « Lower highs after a breadth surge are normal. One cannot expect the oscillator to remain exceptionally strong (above +50) (…). It is sufficient for the McClellan Oscillator to remain positive to keep the bulls going. » Exemple : thrust -70 → +50 (+120) confirmant un retournement après divergence haussière.
**TRADEX-AI C5** : après un thrust, des sommets décroissants (divergence baissière) sont attendus et non alarmants — tant que l'oscillateur reste positif, le biais haussier tient.
*Catégorie : signal*

---

### D2580 — Divergences : confirmation et netteté requises
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_06) : « chartists should not look too hard for such divergences. There will be many divergences and most will not result in reversals (…). a divergence should be confirmed with a strong supporting move. A bullish divergence is confirmed with a strong move into positive territory (…). divergences should be sharp. »
**TRADEX-AI C5** : filtrer les divergences — n'en retenir que les nettes, confirmées par un mouvement franc dans le territoire correspondant. Garde-fou anti-faux-signaux.
*Catégorie : signal*

---

### D2581 — Pièges momentum et nécessité de confirmation (« Bottom Line »)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md) : « As a momentum oscillator, it is prone to the pitfalls of normal momentum oscillators, such as MACD (…) these signals are certainly not fail-proof (…). Signals should be confirmed or refuted with other technical indicators and chart analysis. »
**TRADEX-AI C5** : oscillateur volatil produisant de nombreux signaux non infaillibles ; usage uniquement en confirmation, jamais en déclencheur autonome.
*Catégorie : signal*

---

### D2582 — Symboles SharpCharts ($NYMO/$NAMO ratio-ajustés ; $NYMOT/$NAMOT traditionnels)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_07) : « plot the ratio-adjusted McClellan Oscillator for the NYSE ($NYMO) or the Nasdaq ($NAMO). Users can also plot the un-adjusted McClellan Oscillator for the NYSE ($NYMOT) and Nasdaq ($NAMOT). The unadjusted (…) are based on Net Advances (as opposed to ratio-adjusted Net Advances). »
**TRADEX-AI C5** : tickers de récupération — $NYMO/$NAMO (ratio-ajustés, recommandés) vs $NYMOT/$NAMOT (traditionnels). Données accessibles si intégration breadth.
*Catégorie : structure_marche*

---

### D2583 — Lignes de niveau et superposition de l'indice (paramétrage)
🟢 **FAIT VÉRIFIÉ** (Source : mcclellan_oscillator.md, image_08) : « add horizontal lines as an overlay (…). Two levels can be added by separating the values with a comma in the parameters box (50,-50). The underlying index can be added in an indicator window below. »
**TRADEX-AI C5** : réglage standard = lignes ±50 (seuils de conviction) + indice sous-jacent en fenêtre pour comparer breadth et prix. Détail outillage.
*Catégorie : timing*

---

## SYNTHÈSE

| # | Décision | Cercle | Catégorie | Tag |
|---|----------|--------|-----------|-----|
| D2571 | Nature : breadth momentum des Net Advances (type MACD) | C5 | signal | 🟢 |
| D2572 | 3 signaux : thrusts / centerline / divergences | C5 | signal | 🟢 |
| D2573 | Ratio-ajustement (RANA) pour comparabilité | C5 | structure_marche | 🟢 |
| D2574 | Formule (RANA, EMA 19/39, facteurs 0,10/0,05) | C5 | signal | 🟢 |
| D2575 | Signe = biais directionnel breadth | C5 | signal | 🟢 |
| D2576 | Persistance positive/négative en tendance forte | C5 | indicateurs_tendance | 🟢 |
| D2577 | Zones conviction ±30/±50/±100 | C5 | signal | 🟢 |
| D2578 | Breadth thrust : < -50 → > +50 (~+100) | C5 | signal | 🟢 |
| D2579 | Divergences baissières post-thrust normales | C5 | signal | 🟢 |
| D2580 | Divergences : confirmées + nettes seulement | C5 | signal | 🟢 |
| D2581 | Pièges momentum, confirmation obligatoire | C5 | signal | 🟢 |
| D2582 | Tickers $NYMO/$NAMO vs $NYMOT/$NAMOT | C5 | structure_marche | 🟢 |
| D2583 | Lignes ±50 + indice superposé | C5 | timing | 🟢 |

**Note de portée :** indicateur de breadth/sentiment ACTIONS (C5). Pour TRADEX-AI (futures), valeur = confirmation du sentiment marché actions US via ES uniquement ; aucun lien direct avec GC/HG/CL/ZW ni avec la méthode Belkhayate (⚫🔴 non concerné). 13 décisions, 8/8 images certifiées.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
