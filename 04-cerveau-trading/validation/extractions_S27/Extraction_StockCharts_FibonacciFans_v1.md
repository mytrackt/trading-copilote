# Extraction StockCharts — Fibonacci Fans

**Source :** `bundles/stockcharts/fibonacci_fans.md` (HTTP 200 · ~10 200 car.) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 10/10 certifiées
**Décisions :** D1751 → D1770 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-fans
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | Rising Fibonacci Fan lines based on the March 2009 trough to… | Rising Fibonacci Fan | CERTIFIE (accord .md + HTML) |
| image_02.png | Falling Fibonacci Fan Lines drawn from the April 2010 peak to… | Falling Fibonacci Fan | CERTIFIE (accord .md + HTML) |
| image_03.png | The stock price reversed from the 61.8% fan line in December… | Rising Fan Lines | CERTIFIE (accord .md + HTML) |
| image_04.png | The stock found support at the 50% Fibonacci Fan line twice… | Rising Fan Lines | CERTIFIE (accord .md + HTML) |
| image_05.png | Falling Fan Lines | Falling Fan Lines [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Falling Fan Lines | Falling Fan Lines [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | Log versus Arithmetic Charts | Log versus Arithmetic Charts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | Log versus Arithmetic Charts | Log versus Arithmetic Charts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | Extending the number of bars in SharpCharts to project price… | Extending the Dateline | CERTIFIE (accord .md + HTML) |
| image_10.png | Example of a chart with Fibonacci Fan lines using SharpCharts… | Using Fibonacci Fans With SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1751 — Définition des Fibonacci Fans (lignes de tendance sur points de retracement)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « Fibonacci Fan lines are trend lines based on Fibonacci retracement points. » Lignes montantes depuis un creux (estiment des supports), lignes descendantes depuis un pic (estiment des résistances).
**TRADEX-AI C1** : outil de structure projetant des S/R obliques (lignes) — complément aux niveaux horizontaux sur GC·HG·CL·ZW.
*Catégorie : structure_marche*

---

### D1752 — Lignes montantes : du creux vers les retracements de l'avance
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_01) : « Rising fan lines extend up from a trough and pass through retracement based on the advance (trough to peak). These fan lines can then estimate support levels or potential reversal zones. »
**TRADEX-AI C1** : règle de tracé haussière pour projeter des supports dynamiques obliques.
*Catégorie : structure_marche*

---

### D1753 — Lignes descendantes : du pic vers les retracements de la baisse
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_02) : « Falling fan lines extend down from a peak and pass through retracements based on the decline (peak to trough). These fan lines can then estimate resistance levels or potential reversal zones. »
**TRADEX-AI C1** : règle de tracé baissière pour projeter des résistances dynamiques obliques.
*Catégorie : structure_marche*

---

### D1754 — Les trois lignes du Rising Fan (38,2 / 50 / 61,8 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_01) : « Fan Line 1: Trough to 38.2% retracement · Fan Line 2: Trough to 50% retracement · Fan Line 3: Trough to 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : ratios standard de l'école Fibonacci.
⚫🔴 (écho COG 0,618) : le ratio 0,618 (61,8 %) recoupe les COGParams figés Belkhayate (0,618/1,618) — convergence de ratio, non affirmée par la source.
**TRADEX-AI C1** : spécification des trois pentes S/R pour configuration haussière.
*Catégorie : structure_marche*

---

### D1755 — Les trois lignes du Falling Fan (38,2 / 50 / 61,8 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_02) : « Fan Line 1: Peak to 38.2% retracement · Fan Line 2: Peak to 50% retracement · Fan Line 3: Peak to 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : ratios standard.
⚫🔴 (écho COG 0,618) : convergence du 0,618 avec le COG Belkhayate, non affirmée par la source.
**TRADEX-AI C1** : spécification des trois pentes S/R pour configuration baissière.
*Catégorie : structure_marche*

---

### D1756 — Construction géométrique : deux points par ligne
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « It takes two points to draw a line. The first point for each fan line is based on the low [resp. high]. The second point is based on the Fibonacci retracements. » Les lignes partent du creux/pic et traversent les retracements.
**TRADEX-AI C1** : procédure reproductible de tracé applicatif des fan lines.
*Catégorie : structure_marche*

---

### D1757 — Base mathématique 1,618 / 0,618 (suite de Fibonacci)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « A number divided by the previous number approximates 1.618… A number divided by the next highest number approximates .6180… This is the basis for the 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : dérivation standard.
⚫🔴 (écho COG 0,618) : convergence de ratio (0,618/1,618) avec le COG Belkhayate, non affirmée par la source.
**TRADEX-AI C1** : traçabilité des ratios employés.
*Catégorie : structure_marche*

---

### D1758 — Base du ratio 0,382 et nombre d'or (Phi)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « This is the basis for the 38.2% retracement. Also, note that 1 - .618 = .382 » et « 1.618 refers to the Golden Ratio or Golden Mean, also called Phi. The inverse of 1.618 is .618. »
🔵 ÉCOLE (Fibonacci) : contexte théorique.
**TRADEX-AI C1** : contextualise les constantes secondaires de l'outil.
*Catégorie : structure_marche*

---

### D1759 — Nature dynamique des zones S/R (extension avec les lignes)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « As with regular trend lines, support or resistance zones extend as the Fibonacci Fan lines extend, which makes them dynamic, not static. »
**TRADEX-AI C1** : S/R obliques évoluant dans le temps — à recalculer à chaque barre, comme une trend line.
*Catégorie : structure_marche*

---

### D1760 — Exemple Rising Fan APC : retournements sur la 3e ligne (61,8 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_03) : Anadarko (APC), fan du creux juillet au pic octobre 2009 : « The stock bounced off the 38.2% fan line in late October and then moved to the 61.8% fan line in December. APC ended its correction at the third fan line. » Cassure sous la 61,8 % en avril → chute rapide.
**TRADEX-AI C1** : la 3e ligne (61,8 %) agit comme support majeur ; sa cassure = signal de poursuite baissière.
*Catégorie : signal*

---

### D1761 — Exemple Rising Fan SLE : support double sur la ligne 50 %
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_04) : Sara Lee (SLE), fan creux mars → pic juillet 2009 : « found support at the 50% line later that month. The first bounce… was short-lived, but the stock found support again at the 50% line in early September. » (échelle arithmétique)
**TRADEX-AI C1** : la ligne 50 % comme zone de support testée plusieurs fois avant breakout.
*Catégorie : signal*

---

### D1762 — Exemple Falling Fan JWN : résistance entre lignes 50 % et 62 %
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_05, image_06) : Nordstrom (JWN), fan pic avril → creux mai : « JWN subsequently met resistance between the 50% and 62% fan lines. » (échelle log)
**TRADEX-AI C1** : zone de résistance encadrée par deux fan lines successives.
*Catégorie : signal*

---

### D1763 — Redessiner le fan après un nouveau plus-bas
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_06) : « Once the prior low is taken out, it is usually necessary to redraw the Fibonacci Fan lines based on the new low. » Le second tracé montre JWN butant à nouveau entre 50 % et 62 %.
**TRADEX-AI C1** : règle de maintenance — réinitialiser l'ancrage quand la structure casse. Garde-fou validité.
*Catégorie : structure_marche*

---

### D1764 — Effet de l'échelle log vs arithmétique sur la pente
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_07, image_08) : « Scaling choice can change the slope of the Fibonacci Fan lines and alter potential support, resistance, and reversal levels. » Log = variations en %, arithmétique = variation absolue.
**TRADEX-AI C1** : le choix d'échelle modifie les niveaux projetés — paramètre à figer par convention pour reproductibilité.
*Catégorie : structure_marche*

---

### D1765 — Recommandation d'échelle selon l'horizon
🟡 CONVENTION (Source : fibonacci_fans.md) : « Log scaling is generally preferred for longer periods… Scaling makes little difference with relatively small price movements over short periods… It boils down to a personal preference. »
**TRADEX-AI C1** : convention d'usage (non une règle dure) — privilégier log sur les longs horizons, choix libre sinon.
*Catégorie : structure_marche*

---

### D1766 — Démonstration AA : la cassure de la ligne 50 % dépend de l'échelle
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_07, image_08) : Alcoa (AA) — « the Fibonacci Fan lines on the log chart are steeper, and Alcoa broke the 50% line in mid-April. The Fibonacci Fan lines on the arithmetic chart are less steep, and Alcoa broke the 50% line in the beginning of May. »
**TRADEX-AI C1** : le timing d'un signal de cassure varie selon l'échelle — risque de divergence à documenter avant tout backtest.
*Catégorie : signal*

---

### D1767 — Extension de la dateline (Extra Bars) pour projeter S/R futurs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md, image_09) : Fan pic avril → creux juillet : « These lines are valid as long as the July low holds. An extra 70 bars were added to extend these lines and see future resistance levels. » Réglage via **Extra Bars** sous Chart Attributes.
**TRADEX-AI C1** : projection temporelle des S/R obliques ; validité conditionnée au maintien de l'ancrage. Timing.
*Catégorie : timing*

---

### D1768 — Hypothèse corrective sous-jacente
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « these reversal points assume the move is corrective. A pullback after an advance is deemed a correction that will find support well above the initial trough. A bounce after a decline is deemed a counter-trend rally that will hit resistance well below the initial peak. »
**TRADEX-AI C1** : condition de validité — outil pertinent en contexte de correction, pas de retournement de fond.
*Catégorie : structure_marche*

---

### D1769 — Avertissement : non-autonomie et faux signaux
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : « Fibonacci Fan lines are not meant as a standalone system. Just because prices approach an arc [ligne] does not mean they will reverse. Prices move right through these lines in many cases. No indicator is perfect. »
**TRADEX-AI C3** : confirmation par d'autres outils obligatoire — critère d'élimination des faux positifs (confirmation).
*Catégorie : gestion_risque_entree*

---

### D1770 — Synthèse FAQ : rôle et limites des fan lines
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_fans.md) : FAQ — « Fibonacci Fan lines are trend lines based on Fibonacci retracement points that help to estimate support and resistance levels or potential reversal zones. » Rising depuis un creux (avance), Falling depuis un pic (déclin) ; pas de garantie de retournement.
**TRADEX-AI C1** : récapitulatif décisionnel pour l'intégration de l'outil dans la grille de structure.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1751 → D1770 (20) |
| Images certifiées | 10/10 |
| Tags dominants | 🟢 littéral · 🔵 ÉCOLE Fibonacci · 🟡 CONVENTION (D1765) · ⚫🔴 écho COG 0,618 (D1754, D1755, D1757) |
| Cercles TRADEX | C1 (structure/S-R) · C3 (confirmation : D1769) |
| Catégories | structure_marche · signal · timing · gestion_risque_entree |
| Actifs cibles | GC · HG · CL · ZW |
| Cas à vérifier | Aucun (0 image à vérifier) ; 4 images en SECTION-FALLBACK (image_05–08, légende = titre de section, déjà certifiées) ; ⚫🔴 écho COG = arbitrage humain, NE PAS fusionner comme équivalence Belkhayate |

> ⚠️ Outil éducatif (StockCharts ChartSchool) · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
