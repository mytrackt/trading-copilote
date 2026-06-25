# Extraction StockCharts — Quadrant Lines
**Source :** `bundles/stockcharts/quadrant_lines.md` (HTTP 200 · ~4 100 car.) + 6 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D3291 → D3310 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/quadrant-lines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.jpg | Quadrant Lines help to identify potential highs and lows. | Interpreting Quadrant Lines |
| image_02.png | Log scale chart showing Quadrant Lines. | Log Scaling |
| image_03.png | Arithmetic scale chart showing Quadrant Lines. | Log Scaling |
| image_04.png | Quadrant Lines help identify how deep pullbacks can go… | Quadrant Lines To Identify Pullback Depths |
| image_05.png | Quadrant Lines can be used to identify resistance levels… | Quadrant Lines To Identify Pullback Depths |
| image_06.png | Adding Quadrant Lines in SharpCharts. | SharpCharts |

## DÉCISIONS

### D3291 — Définition : 5 lignes, 4 quadrants
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Lines divide the high-low range into four equal sections. There are five lines and four quadrants. The *top line* marks the **high**, the *bottom line* marks the **low,** and the other three lines form the quadrants. The *middle line* marks the **midpoint** of the range. »
**TRADEX-AI C1** : Outil de structure découpant le range haut-bas en 4 sections égales (5 lignes). Ligne du milieu = mi-range. Repère visuel de position du prix dans son range.
*Catégorie : structure_marche*
---

### D3292 — Nature : règle de mesure, pas un indicateur
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Lines are not an indicator as such. Instead, they are used as a measuring stick for price action. Quadrant Lines allow you to visually quantify price levels relative to the defined range. »
**TRADEX-AI C1** : Outil d'annotation/mesure (pas un oscillateur). Sert à quantifier visuellement où se situe le prix dans un range défini. À traiter comme structure, pas comme signal autonome.
*Catégorie : structure_marche*
---

### D3293 — Formule de calcul des quadrants
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Range: High to Low ; Quadrant Size: (High - Low)/4. Bottom Line = Low ; First Line = Low + Quadrant Size ; Middle Line = First Line + Quadrant Size ; Third Line = Middle Line + Quadrant Size ; Top Line = High. »
**TRADEX-AI C1** : Formule déterministe (niveau 1, 0$) : pas de quadrant = (Haut − Bas)/4 ; lignes empilées Bas, Bas+1q, mi, mi+1q, Haut. Codable directement à partir d'un range choisi.
*Catégorie : structure_marche*
---

### D3294 — Exemple chiffré 60/40
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Range: 60 to 40 ; Quadrant Size: (60 - 40)/4 = 5. Bottom Line = 40 ; First Line = 45 ; Middle Line = 50 ; Third Line = 55 ; Top Line = 60. »
**TRADEX-AI C1** : Exemple numérique validant la formule (range 20 → pas de 5). Sert de test unitaire pour une implémentation TRADEX.
*Catégorie : configuration*
---

### D3295 — Lecture : retracements 25/50/75 %
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_01) : « quadrants are the same size because each equals 1/4 or 25% of the high-low range. After an advance, Quadrant Lines allow you to quickly identify price points that retrace 25%, 50%, and 75%. Prices have retraced 50% when they reach the middle quadrant line. »
**TRADEX-AI C1** : Chaque quadrant = 25 % du range → lignes = retracements 25/50/75 %. La ligne médiane = retracement 50 %. Repérage rapide de la profondeur d'un pullback.
*Catégorie : structure_marche*
---

### D3296 — Symétrie : retracements d'un déclin
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_01) : « Corresponding retracements can also be seen when drawing Quadrant Lines over a decline. These lines help you quickly identify advances that retrace 25%, 50%, or 75% of the defined decline. »
**TRADEX-AI C1** : Outil symétrique — tracé sur un déclin, il mesure de la même façon les rebonds (25/50/75 %). Applicable haussier comme baissier.
*Catégorie : structure_marche*
---

### D3297 — Lignes équidistantes en absolu (pas en log)
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Lines might not look equidistant on the log scale, but they are equidistant in absolute terms. Log scaling shows price movements in percentage terms. »
**TRADEX-AI C1** : Garde-fou affichage — les lignes sont équidistantes en termes absolus (points), pas forcément à l'œil sur échelle log. Distinction à intégrer si rendu graphique.
*Catégorie : structure_marche*
---

### D3298 — Absolu vs pourcentage (exemple 65→75 / 100→110)
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_02) : « An advance from $65 to $75 is 10 points in absolute terms or 15.3% in percentage terms. An advance from $100 to $110 is also 10 points, but much less in percentage terms (just 10%). »
**TRADEX-AI C1** : Rappel — un même mouvement en points = un % différent selon le point de départ. Pertinent pour comparer des amplitudes entre actifs/prix.
*Catégorie : structure_marche*
---

### D3299 — Effet du log sur l'aspect des quadrants
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_03) : « For this reason, the bottom quadrant may appear bigger than the top quadrant when using log scaling… an equal advance from a lower starting point produces a bigger percentage gain, which is reflected in the log chart. »
**TRADEX-AI C1** : Sur échelle log, le quadrant bas paraît plus grand (même nb de points = % plus fort en bas). Effet visuel à connaître ; n'altère pas le calcul absolu.
*Catégorie : structure_marche*
---

### D3300 — Cas IBM : appui au retracement 75 %
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_04) : « The chart below shows IBM with the Quadrant Lines covering an advance from late October to mid-January. The stock firmed near the 75% retracement, the top of the lowest quadrant. This is not an argument for 75% as a key retracement that you should watch carefully. Quadrant Lines simply help quantify the depth of the pullback. »
**TRADEX-AI C1** : Cas — IBM s'est stabilisé près du retracement 75 %. Garde-fou : ce n'est PAS un niveau-clé en soi ; les Quadrant Lines ne font que quantifier la profondeur du pullback.
*Catégorie : structure_marche*
---

### D3301 — Cas GOOG : rebond entre 50 % et 75 %
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_05) : « The chart below shows Google (GOOG) with the Quadrant Lines covering the decline from early January to late February. GOOG exceeded the 25% and 50% retracements with the advance above $590 but did not exceed the 75% retracement. »
**TRADEX-AI C1** : Cas baissier — rebond GOOG ayant dépassé 25/50 % mais buté sous 75 %. Illustre l'usage en résistance lors d'un rebond dans un déclin.
*Catégorie : structure_marche*
---

### D3302 — Double usage : retracement + localisation relative
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Quadrant Lines can identify retracements or determine the relative location of current prices within a given high-low range. »
**TRADEX-AI C1** : Deux usages — (1) mesurer un retracement, (2) situer le prix courant dans son range. Brique de contexte structurel pour le scoring.
*Catégorie : structure_marche*
---

### D3303 — 25 % = repli superficiel (signe de force)
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « After an advance, a decline that retraces only 25% would be deemed shallow and could be used as a sign of strength. »
**TRADEX-AI C1** : Lecture — après une hausse, un repli limité à 25 % = correction superficielle = signe de force du sous-jacent. Élément de qualification de pullback.
*Catégorie : configuration*
---

### D3304 — 75 % = repli excessif (dernier point de retournement)
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « A decline that retraces 75% could be deemed excessive, and the most one could expect from a correction. This could be viewed as the last reversal point before the move returns back to the original low. »
**TRADEX-AI C1** : Lecture — un repli de 75 % = correction excessive, dernier point de retournement plausible avant retour vers le bas d'origine. Seuil d'alerte de retournement potentiel.
*Catégorie : configuration*
---

### D3305 — Comparaison avec l'outil Fibonacci
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « there are some similarities with the Fibonacci Retracements Tool, which uses 38.2%, 50%, and 61.8% retracements. »
**TRADEX-AI C1** : Parenté avec Fibonacci (38,2/50/61,8 %) mais grille différente (25/50/75 %). Deux familles de retracement à ne pas confondre dans le moteur.
*Catégorie : structure_marche*
---

### D3306 — Combiner avec d'autres analyses
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « As with all indicators and line studies, Quadrant Lines should be used in conjunction with other aspects of technical analysis. »
**TRADEX-AI C1** : Garde-fou — outil à combiner avec le reste de l'analyse, jamais isolé. Cohérent avec la règle multi-confirmation 3/4+2/3 TRADEX.
*Catégorie : configuration*
---

### D3307 — Tracé via l'outil ChartNotes
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md, image_06) : « You can use our ChartNotes annotation tool to add Quadrant Lines to your charts. Below, you'll find an example of a chart annotated with Quadrant Lines. »
**TRADEX-AI C1** : Outil purement d'annotation manuelle dans SharpCharts (ChartNotes). Dans TRADEX, l'équivalent serait un calcul automatique de 5 lignes sur un range choisi.
*Catégorie : configuration*
---

### D3308 — [RECONSTRUCTION] Application TRADEX au range de session
🔴 **NON VÉRIFIÉ** (déduction, non présent dans la source) : Les Quadrant Lines pourraient être appliquées au range haut-bas d'une session NT8 (GC/HG/CL/ZW) pour situer le prix courant et qualifier la profondeur des pullbacks intraday.
**TRADEX-AI C1** : Piste d'implémentation — calculer les 5 lignes sur le range de session range-bars. À VALIDER : non décrit par la source (la page n'évoque ni intraday ni futures).
*Catégorie : configuration*
---

### D3309 — [RECONSTRUCTION] Quadrant médian comme proxy de mi-range
🔴 **NON VÉRIFIÉ** (déduction, non présent dans la source) : La ligne médiane (50 %) pourrait servir de proxy de "valeur" mi-range, à rapprocher d'autres notions de point d'équilibre (Pivots Belkhayate, VWAP, point of control).
**TRADEX-AI C1** : Hypothèse de rapprochement structurel non étayée par la source. ⚫🔴 Lien Belkhayate (mi-range vs pivots) NON affirmé par StockCharts — à trancher humainement.
*Catégorie : structure_marche*
---

### D3310 — Synthèse de positionnement
🟢 **FAIT VÉRIFIÉ** (Source : quadrant_lines.md) : « Even though these lines are not indicators per se… Quadrant Lines can identify retracements or determine the relative location of current prices within a given high-low range. » (combiné aux seuils 25 % superficiel / 75 % excessif.)
**TRADEX-AI C1** : Positionnement final — règle de mesure de range/retracement, complémentaire à Fibonacci, à utiliser comme contexte structurel et non comme déclencheur d'ordre.
*Catégorie : structure_marche*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3291 → D3310 (20 décisions) |
| Images certifiées | 6/6 |
| Cercle dominant | C1 (prix/structure) |
| Tags | 🟢 littéral ×18 · 🔴 NON VÉRIFIÉ ×2 (D3308, D3309 — reconstructions) |
| Catégories | structure_marche, configuration |
| Actifs concernés | GC · HG · CL · ZW (outil générique de range, exemples IBM/GOOG actions) |
| Belkhayate | ⚫🔴 lien POSSIBLE mais NON affirmé par la source (mi-range/50 % vs Pivots Belkhayate — D3309 à trancher humainement) |
| Paramètres clés | Pas de quadrant = (Haut−Bas)/4 ; 5 lignes ; seuils 25 % superficiel / 50 % médian / 75 % excessif ; distinct de Fibonacci 38,2/50/61,8 |
| À vérifier | D3308 + D3309 (reconstructions TRADEX/Belkhayate non sourcées) |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
