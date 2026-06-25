# Extraction StockCharts — P&F Trend Lines
**Source :** `bundles/stockcharts/p_and_f_trend_lines.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D2991 → D3000 · **Page :** chartschool.stockcharts.com/.../point-and-figure-basics/p-and-f-trend-lines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Bearish/Bullish Resistance Lines (NE) | Changing Trend Lines | D2993 |
| image_02 | Bullish Support Line + Triple Top + Bearish Signal Reversed (A) | Bullish Support Line | D2994 |
| image_03 | Bearish Resistance Line + Triple Bottom/Top (QCOM) | Bearish Resistance Line | D2995 |
| image_04 | 3 touches sans cassure → ligne décalée (MCD) | Trend Line Adjustments | D2996 |
| image_05 | Bearish Resistance Line jamais cassée (CME) | Trend Line Adjustments | D2997 |
| image_06 | Réglages SharpCharts P&F Trendlines | Creating P&F Trend Lines | D2999 |
| image_07 | Réglages overlay Trendlines P&F | Creating P&F Trend Lines | D2999 |

## DÉCISIONS

### D2991 — P&F Trend Lines : angles 45°/135°
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md) : Sur P&F 3-box Reversal, les lignes de tendance sont tracées à 45° à la hausse (Bullish Support Line) et 135° à la baisse (Bearish Resistance Line). Tracées à angle fixe, elles représentent un taux d'ascension/descente spécifique.
🔵 **ÉCOLE** : Objectivité propre au P&F (angles imposés).
**TRADEX-AI C1** : Lignes déterministes (angle fixe) calculables sur P&F GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D2992 — Toujours une ligne en vigueur
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md) : Il y a toujours une Bullish Support Line OU une Bearish Resistance Line active. Après cassure d'une Bearish Resistance Line, une Bullish Support Line est tracée depuis un bas important (45°) et reste en vigueur jusqu'à cassure ; puis une nouvelle Bearish Resistance Line (135°) depuis un haut proche de la cassure.
**TRADEX-AI C1** : Système d'état binaire (biais haussier/baissier) selon la ligne active.
*Catégorie : structure_marche*

### D2993 — Alternance des lignes (exemple NE)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md, image_01) : Exemple Noble Drilling — alternance Bearish Resistance Line (cassée 2009) → Bullish Support Line (cassée avr. 2010) → nouvelle Bearish Resistance Line.
**TRADEX-AI C1** : Suivi du basculement de ligne = changement de biais directionnel.
*Catégorie : signal*

### D2994 — Bullish Support Line : règle directionnelle
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md, image_02) : Uptrend présent quand les prix dépassent la Bullish Support Line (45°). Selon la théorie P&F : prendre les signaux haussiers au-dessus de cette ligne et **ignorer les signaux baissiers** = trader dans le sens de la tendance majeure.
**TRADEX-AI C3** : Filtre directionnel — n'accepter que les signaux alignés sur la ligne active.
*Catégorie : gestion_risque_entree*

### D2995 — Bearish Resistance Line : règle directionnelle
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md, image_03) : Downtrend présent quand les prix restent sous la Bearish Resistance Line (135° = 180-45). Signaux baissiers préférés sous la ligne ; signaux haussiers ignorés ou utilisés pour prendre des profits sur shorts.
**TRADEX-AI C3** : Miroir baissier du filtre directionnel.
*Catégorie : gestion_risque_entree*

### D2996 — « It ain't broken until it's broken »
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md, image_04) : Un O-Column qui descend jusqu'à la ligne puis repart à la hausse n'est PAS une cassure ; une nouvelle ligne est requise pour refléter ce test (décalée d'une box pour ajuster le taux d'ascension).
**TRADEX-AI C1** : Ne déclencher la cassure que sur franchissement effectif, pas sur simple test.
*Catégorie : structure_marche*

### D2997 — Ajustement Bearish Resistance Line
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md, image_05) : Idem pour la Bearish Resistance Line — une avancée jusqu'à la même box sans cassure entraîne, après repli, une nouvelle ligne tracée une square plus haut (exemple CME).
**TRADEX-AI C1** : Logique d'ajustement symétrique à coder.
*Catégorie : structure_marche*

### D2998 — Plus objectif que sur bar chart
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md) : Les lignes P&F (3-box Reversal) sont plus objectives que sur bar/line charts ; biais haussier si la ligne active est une Bullish Support Line, baissier si Bearish Resistance Line.
**TRADEX-AI C3** : Avantage = objectivité du biais (réduit la subjectivité du tracé).
*Catégorie : structure_marche*

### D2999 — Implémentation SharpCharts
🔵 **ÉCOLE** (Source : p_and_f_trend_lines.md, image_06, image_07) : Ajout via l'overlay « Trend Lines » du P&F Chart Workbench.
**TRADEX-AI C0** : Référence outillage ; à recréer côté NT8 si P&F implémenté.
*Catégorie : configuration*

### D3000 — Multi-temporalité P&F
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_trend_lines.md) : P&F daily = timeframe long → biais de grande tendance ; puis 30-min P&F pour chercher des signaux en harmonie avec ce biais.
**TRADEX-AI C3** : Combiner biais daily + signaux intraday alignés (cohérent timeframes Belkhayate).
*Catégorie : timing*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2991 → D3000 (10) |
| Images citées | 7/7 |
| Catégories | structure_marche · signal · gestion_risque_entree · configuration · timing |
| Tags | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE |
| Belkhayate | NON CONCERNÉ (filtre directionnel = thème proche « Direction », non affirmé) |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
