# Extraction StockCharts — P&F Triangles

**Source :** `bundles/stockcharts/p_and_f_triangles.md` (HTTP 200 · ~5 600 car.) + 4 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D3011 → D3030 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-triangles
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | P&F chart with a triangle formation. | Triangle Breakout | CERTIFIÉ (accord .md + HTML) |
| image_02.png | A triangle formed after a sharp advance, which represented a consolidation within an uptrend | Triangle Breakout | CERTIFIÉ (accord .md + HTML) |
| image_03.png | P&F Triangle Breakdown. | Triangle Breakdown | CERTIFIÉ (accord .md + HTML) |
| image_04.png | A breakdown from the triangle formation resulted in the stock falling lower. | Triangle Breakdown | CERTIFIÉ (accord .md + HTML) |

## DÉCISIONS

### D3011 — Définition du triangle P&F (contraction des prix)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Triangles form as prices contract on a P&F chart. The X-Columns (up) form successive lower highs as the O-Columns (down) form successive higher lows. »
**TRADEX-AI C1** : motif de compression de range identifiable sur graphe Point & Figure ; X-colonnes = sommets décroissants, O-colonnes = creux croissants.
*Catégorie : configuration*

---

### D3012 — Le standoff acheteurs/vendeurs résolu par le signal suivant
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « The inability of prices to break from this contracting range reflects a standoff between buying pressure and selling pressure. This standoff is resolved with the next P&F signal. »
**TRADEX-AI C1** : tant que le range se resserre, ne pas trader ; attendre la résolution (le prochain signal P&F) avant toute prise de position.
*Catégorie : structure_marche*

---

### D3013 — Polarité du triangle déterminée par le breakout/breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « A Double Top Breakout makes the triangle bullish, while a Double Bottom Breakdown makes the triangle bearish. »
**TRADEX-AI C1** : le triangle est neutre jusqu'à preuve du contraire — c'est la cassure (Double Top Breakout = haussier / Double Bottom Breakdown = baissier) qui fixe le biais directionnel.
*Catégorie : signal*

---

### D3014 — Largeur minimale : cinq colonnes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Triangles have at least five columns. The first four columns form the triangle and the fifth column marks the breakout or breakdown. »
**TRADEX-AI C1** : critère de comptage structurel — 4 colonnes pour former le triangle + 1 colonne de résolution = 5 colonnes minimum.
*Catégorie : configuration*

---

### D3015 — Structure interne : ≥2 X-colonnes (lower high) et ≥2 O-colonnes (higher low)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « There are at least two X-Columns with the second column forming a lower high. There are at least two O-Columns with the second column forming a higher low. »
**TRADEX-AI C1** : règle déterministe de reconnaissance — au moins 2 X-colonnes (2e plus bas) et 2 O-colonnes (2e plus haut).
*Catégorie : configuration*

---

### D3016 — Extension possible au-delà de quatre colonnes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Triangles can extend more than four columns as long as subsequent X-Columns continue forming lower highs and subsequent O-Columns form a higher low. »
**TRADEX-AI C1** : le motif reste valide tant que la contraction se poursuit (X toujours plus bas, O toujours plus hauts).
*Catégorie : configuration*

---

### D3017 — Le triangle est un motif neutre dépendant de la cassure
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Triangles are neutral patterns dependent on the breakout or breakdown for the signal. »
**TRADEX-AI C1** : ne JAMAIS anticiper la direction d'un triangle ; attendre la confirmation par cassure avant tout signal.
*Catégorie : signal*

---

### D3018 — Breakout haussier = Double Top Breakout (pas une simple cassure de trendline)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « A Double Top Breakout signals a bullish resolution to the triangle pattern. Note that a trend line break is not enough. A basic P&F buy signal, such as a Double Top Breakout, is required to complete the triangle and trigger the bullish signal. »
**TRADEX-AI C1** : filtre anti-faux-signal — la rupture d'une ligne de tendance ne suffit pas ; exiger un vrai signal d'achat P&F (Double Top Breakout).
*Catégorie : signal*

---

### D3019 — Exemple breakout haussier CHK 2010
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md, image_01) : « Chesapeake Energy (CHK) with a triangle forming in 2010 [...] two O-Columns with higher lows and one X-Column with a lower high. This pattern turned bullish with the Double Top Breakout at 25. »
**TRADEX-AI C1** : cas pédagogique — la cassure à 25 (Double Top Breakout) confirme le triangle haussier.
*Catégorie : configuration*

---

### D3020 — Triangle de continuation dans une tendance haussière (QLD)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md, image_02) : « ProShares Ultra QQQ Fund (QLD) with a triangle forming after a sharp advance [...] Even though such consolidations are typically continuation patterns, they depend on a breakout before turning bullish. »
**TRADEX-AI C1** : même un triangle de continuation reste subordonné à la cassure pour devenir haussier — pas de signal anticipé.
*Catégorie : configuration*

---

### D3021 — Breakdown baissier = Double Bottom Breakdown (pas une simple cassure de trendline)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « A Double Bottom Breakdown signals a bearish resolution to the triangle pattern. Note that a trend line break is not enough. A basic P&F sell signal, such as a Double Bottom Breakdown, is required to complete the triangle and trigger the bearish signal. »
**TRADEX-AI C1** : symétrique de D3018 — exiger un vrai signal de vente P&F (Double Bottom Breakdown), une cassure de trendline ne suffit pas.
*Catégorie : signal*

---

### D3022 — Exemple breakdown baissier Atlas Air (AAWW)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md, image_03) : « Atlas Air (AWWW) with a long X-Column and then a triangle [...] After two lower highs and a higher low, the triangle broke to the downside with a Double Bottom Breakdown. »
**TRADEX-AI C1** : cas pédagogique de résolution baissière — un motif d'apparence haussière (continuation) peut casser à la baisse ; attendre confirmation.
*Catégorie : configuration*

---

### D3023 — Exemple breakdown F5 Networks (FFIV) après Triple Top Breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md, image_04) : « F5 Networks (FFIV) with a long O-Column that forged a Triple Top Breakdown [...] After a higher low and lower high, the stock continued lower with a Double Bottom Breakdown to turn the triangle bearish. »
**TRADEX-AI C1** : cas pédagogique — consolidation après chute, puis poursuite baissière confirmée par Double Bottom Breakdown.
*Catégorie : configuration*

---

### D3024 — Objectifs de prix via Horizontal Count ou Vertical Count
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Chartists can use the Horizontal Count Method or the Vertical Count Method to establish Price Objectives. »
**TRADEX-AI C1** : deux méthodes P&F de projection d'objectif disponibles (comptage horizontal / vertical).
*Catégorie : configuration*

---

### D3025 — Les objectifs de prix ne sont pas des cibles fermes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Price Objectives are not hard targets. Instead, they simply provide a guesstimate for an upside or downside objective. »
**TRADEX-AI C1** : traiter tout objectif P&F comme une estimation indicative, pas comme un take-profit rigide.
*Catégorie : gestion_risque_entree*

---

### D3026 — Invalidation d'un breakout haussier = passage sous le low de la dernière O-colonne
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « After an upside breakout, a move below the low of the last O-Column would produce a Double Bottom Breakdown and invalidate a triangle breakout. »
**TRADEX-AI C1** : niveau d'invalidation explicite et déterministe — sous le plus bas de la dernière O-colonne, le breakout haussier est annulé (sert de référence de stop).
*Catégorie : gestion_risque_entree*

---

### D3027 — Compléter par d'autres techniques d'analyse pour le risque
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Chartists should also employ other technical analysis techniques to measure risk and monitor the unfolding trend. »
**TRADEX-AI C7** : le triangle P&F ne suffit pas seul ; croiser avec d'autres outils (alignement multi-cercles TRADEX) pour mesurer le risque.
*Catégorie : gestion_risque_entree*

---

### D3028 — Analogie avec le resserrement des Bollinger Bands (volatilité)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « This coiling of prices is similar to the tightening of Bollinger Bands. Volatility declines as the Bands narrow and as a Triangle coils tighter. A volatility contraction is often followed by volatility expansion, which produces the breakout or the breakdown. »
**TRADEX-AI C1** : la contraction du triangle = baisse de volatilité ; une expansion de volatilité suit souvent et déclenche la cassure (logique squeeze→expansion).
*Catégorie : structure_marche*

---

### D3029 — Taille du triangle : court (continuation) vs grand (renversement)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Short triangles (4 columns) after a sharp advance or decline are more likely to be continuation patterns. Large triangles (6+ columns) are more likely to mark a reversal. »
**TRADEX-AI C1** : heuristique de classification — triangle court (4 col.) après mouvement fort ⇒ continuation probable ; grand triangle (6+ col.) ⇒ renversement probable.
*Catégorie : configuration*

---

### D3030 — Aucune confirmation sans Double Bottom Breakdown ou Double Top Breakout
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_triangles.md) : « Regardless of the bias, a triangle is not confirmed until the Double Bottom Breakdown or Double Top Breakout. »
**TRADEX-AI C1** : règle de clôture — quel que soit le biais supposé, aucun triangle n'est confirmé tant que la cassure (Double Top Breakout / Double Bottom Breakdown) n'est pas survenue.
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3011 → D3030 (20) |
| Images certifiées | 4/4 |
| Tag dominant | 🟢 FAIT VÉRIFIÉ (toutes) |
| Cercle | C1 (Prix/structure) ; D3027 → C7 (corrélations) |
| Catégories | configuration, structure_marche, signal, gestion_risque_entree |
| Belkhayate | NON CONCERNÉ (pas de lien MFI/Énergie) |
| Actifs | Applicable GC·HG·CL·ZW (motif générique P&F) |
| Cas à vérifier | Aucun — 0 image à vérifier, 0 fait NON VÉRIFIÉ |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Tags : 🟢 = fait littéral de la source. Aucune école/convention/non-vérifié dans ce bundle.
