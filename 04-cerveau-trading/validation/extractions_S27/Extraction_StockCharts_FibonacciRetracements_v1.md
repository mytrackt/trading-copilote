# Extraction StockCharts — Fibonacci Retracements

**Source :** `bundles/stockcharts/fibonacci_retracements.md` (HTTP 200 · ~9 100 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D1771 → D1790 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/fibonacci-retracements
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | Example of a stock retracing around 50% of its previous advance. | Fibonacci Retracements as Alert Zones | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a stock retracing around 50% of its previous decline. | Fibonacci Retracements as Alert Zones | CERTIFIE (accord .md + HTML) |
| image_03.png | A 38% Fibonacci retracement and a falling wedge marked a correction… | Moderate Retracements | CERTIFIE (accord .md + HTML) |
| image_04.png | A moderate 38% Fibonacci retracement combined with other technical… | Moderate Retracements | CERTIFIE (accord .md + HTML) |
| image_05.png | A bottoming close to the 62% Fibonacci retracement level with… | Golden Retracements | CERTIFIE (accord .md + HTML) |
| image_06.png | The stock price topped close to the 62% Fibonacci retracement… | Golden Retracements | CERTIFIE (accord .md + HTML) |
| image_07.png | Add Fibonacci Retracement lines to SharpCharts with the annotation tool. | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1771 — Définition des niveaux de retracement Fibonacci
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « Fibonacci retracement levels are based on ratios used to identify potential reversal points on a price chart. The most popular Fibonacci retracements are 61.8% and 38.2%. Note that 38.2% is often rounded to 38%, and 61.8 is rounded to 62%. »
**TRADEX-AI C1** : outil de structure central projetant des niveaux S/R horizontaux sur GC·HG·CL·ZW.
*Catégorie : structure_marche*

---

### D1772 — Application après hausse et après baisse
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « After an advance, chartists apply Fibonacci ratios to define retracement levels and forecast the extent of a correction or pullback. Fibonacci retracement levels can also be applied after a decline to forecast the length of a counter-trend bounce. »
**TRADEX-AI C1** : règle d'usage bidirectionnelle (pullback haussier / rebond baissier).
*Catégorie : structure_marche*

---

### D1773 — Base mathématique 1,618 / 0,618 (61,8 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « A number divided by the previous number approximates 1.618… A number divided by the next highest number approximates 0.6180… This is the basis for the 61.8% retracement. »
🔵 ÉCOLE (Fibonacci) : dérivation standard de la suite.
⚫🔴 (écho COG 0,618) : convergence du couple 0,618/1,618 avec les COGParams figés Belkhayate — écho conceptuel, non affirmé par la source (StockCharts ne mentionne pas Belkhayate).
**TRADEX-AI C1** : ratio S/R principal ; traçabilité du 0,618.
*Catégorie : structure_marche*

---

### D1774 — Base du ratio 0,382 (38,2 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « A number divided by another two places higher approximates 0.3820… This is the basis for the 38.2% retracement. Also, note that 1 - 0.618 = 0.382 »
🔵 ÉCOLE (Fibonacci) : dérivation standard.
**TRADEX-AI C1** : ratio S/R secondaire.
*Catégorie : structure_marche*

---

### D1775 — Base du ratio 0,236 (23,6 %)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « A number divided by another three places higher approximates 0.2360… This is the basis for the 23.6% retracement. »
🔵 ÉCOLE (Fibonacci) : dérivation standard.
**TRADEX-AI C1** : ratio de retracement peu profond (flags / pullbacks courts).
*Catégorie : structure_marche*

---

### D1776 — Le nombre d'or (Phi) et la « golden retracement »
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « 1.618 refers to the Golden Ratio or Golden Mean, also called Phi. The inverse of 1.618 is .618. » Le 61,8 % est appelé « golden retracement » car fondé sur le nombre d'or.
🔵 ÉCOLE (Fibonacci) : contexte théorique.
⚫🔴 (écho COG 0,618) : Phi (1,618) et son inverse (0,618) recoupent les COGParams Belkhayate — convergence non affirmée par la source.
**TRADEX-AI C1** : qualifie le 61,8 % comme niveau privilégié.
*Catégorie : structure_marche*

---

### D1777 — Retracements = zones d'alerte, pas points de retournement durs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « Retracement levels alert traders or investors of a potential trend reversal, resistance area, or support area… As the correction approaches these retracements, chartists should become more alert for a potential bullish reversal. »
**TRADEX-AI C1** : statut d'« alerte » et non de signal — à combiner avec confirmation.
*Catégorie : structure_marche*

---

### D1778 — Exemple support HD : retracement ~50 % de l'avance
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_01) : « The chart below shows Home Depot retracing around 50% of its prior advance. »
**TRADEX-AI C1** : illustration d'un pullback à 50 % comme zone de support potentielle.
*Catégorie : signal*

---

### D1779 — Exemple résistance MMM : retracement ~50 % de la baisse
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_02) : « The chart below shows 3M (MMM) retracing around 50% of its prior decline. » Symétrie pour un rebond correctif après baisse.
**TRADEX-AI C1** : illustration d'un rebond à 50 % comme zone de résistance potentielle.
*Catégorie : signal*

---

### D1780 — Confirmation requise par d'autres outils techniques
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « These retracement levels are not hard reversal points. Instead, they serve as alert zones for a potential reversal. At this point, traders should employ other aspects of technical analysis… candlesticks, price patterns, momentum oscillators, or moving averages. »
**TRADEX-AI C3** : exige confirmation multi-outils — cohérent avec la règle 3/4 + 2/3 alignés (confirmation).
*Catégorie : gestion_risque_entree*

---

### D1781 — Les quatre niveaux communs de l'outil StockCharts
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « The Fibonacci Retracements Tool at StockCharts shows four common retracements: 23.6%, 38.2%, 50%, and 61.8%. »
🔵 ÉCOLE (Fibonacci) : grille standard de l'outil.
**TRADEX-AI C1** : ensemble de niveaux à matérialiser dans la grille de structure.
*Catégorie : structure_marche*

---

### D1782 — Le 50 % n'est pas un nombre de Fibonacci (Dow Theory)
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « The 50% retracement is not based on a Fibonacci number. Instead, this number stems from Dow Theory's assertion that the Averages often retrace half their prior move. »
**TRADEX-AI C1** : distinction d'origine — le 50 % vient de la théorie de Dow, pas de Fibonacci. À documenter pour éviter une confusion d'école.
*Catégorie : structure_marche*

---

### D1783 — Classification des retracements par profondeur
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « 23.6% retracement to be relatively shallow… Retracements in the 38.2%-50% range would be considered moderate… the 61.8% retracement can be called golden retracement. »
**TRADEX-AI C1** : taxonomie shallow/moderate/golden — utile pour qualifier la profondeur d'un pullback.
*Catégorie : structure_marche*

---

### D1784 — Exemple TGT : retracement 38 % + falling wedge + CMF
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_03) : Target (TGT) a retracé 38 % de l'avance avec un falling wedge ; « Chaikin Money Flow turned positive… but this first reversal attempt failed… The second reversal in mid-July was successful. »
**TRADEX-AI C3** : confluence 38 % + figure + CMF ; illustre aussi qu'une première tentative peut échouer (gestion du faux signal). Confirmation.
*Catégorie : signal*

---

### D1785 — Exemple PETM : retracement 38 % + support cassé devenu résistance + Williams %R
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_04) : Petsmart (PETM) — « In addition to the 38% retracement, notice that broken support turned into resistance in this area… The Williams %R was trading above -20% and overbought. » Confirmation par %R repassant sous -20 % + flag cassé.
**TRADEX-AI C3** : illustration de confluence multi-signaux validant un retournement. Confirmation.
*Catégorie : signal*

---

### D1786 — Exemple PFE : creux près du 62 % + marteau sur fort volume
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_05) : Pfizer (PFE) « bottoming near the 62% retracement level. Before this successful bounce, there was a failed bounce near the 50% retracement. The successful reversal occurred with a hammer on high volume… »
**TRADEX-AI C1** : le 62 % comme support « golden » confirmé par bougie + volume ; un test à 50 % peut d'abord échouer.
*Catégorie : signal*

---

### D1787 — Exemple JPM : sommet près du 62 % + MACD + bougie rouge/gap
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md, image_06) : JP Morgan (JPM) « topping near the 62% retracement level… resistance suddenly appeared with a reversal confirmation from the MACD (5,35,5). The red candlestick and gap down affirmed resistance near the 62% retracement. »
**TRADEX-AI C1** : le 62 % comme résistance confirmée par MACD + structure de bougie.
*Catégorie : signal*

---

### D1788 — Zone 38,2–61,8 % comme principale zone d'alerte de retournement
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « While short 23.6% retracements occur, the 38.2-61.8% zone covers the most possibilities (with 50% in the middle). This zone may seem big, but it's just a reversal alert zone. »
**TRADEX-AI C1** : délimite la fourchette de surveillance prioritaire pour un retournement.
*Catégorie : structure_marche*

---

### D1789 — Robustesse proportionnelle au nombre de facteurs confirmants
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : « Other technical signals are needed to confirm a reversal. Reversals can be confirmed with candlesticks, momentum indicators, volume, or chart patterns. **The more confirming factors, the more robust the signal.** »
**TRADEX-AI C3** : principe de confluence quantitative — aligné avec la grille déterministe /10 et la règle 3/4 + 2/3. Confirmation.
*Catégorie : gestion_risque_entree*

---

### D1790 — Synthèse FAQ : niveaux populaires et combinaison d'indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : fibonacci_retracements.md) : FAQ — « The most popular… are 61.8% and 38.2%… The other two 'common' retracements include 23.6% and 50% (though 50% is not part of the Fibonacci sequence). » et « Fibonacci retracements can be combined with other indicators such as candlesticks, price patterns, momentum oscillators, or moving averages… »
**TRADEX-AI C1** : récapitulatif décisionnel pour l'intégration dans la grille de structure.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1771 → D1790 (20) |
| Images certifiées | 7/7 |
| Tags dominants | 🟢 littéral · 🔵 ÉCOLE Fibonacci · ⚫🔴 écho COG 0,618 (D1773, D1776) |
| Cercles TRADEX | C1 (structure/S-R) · C3 (confirmation : D1780, D1789) |
| Catégories | structure_marche · signal · gestion_risque_entree |
| Actifs cibles | GC · HG · CL · ZW |
| Cas à vérifier | Aucun (0 image à vérifier, 0 fait NON VÉRIFIÉ) ; note D1782 : 50 % = Dow Theory, NON Fibonacci (à conserver pour éviter confusion d'école) ; ⚫🔴 écho COG = arbitrage humain, NE PAS fusionner comme équivalence Belkhayate |

> ⚠️ Outil éducatif (StockCharts ChartSchool) · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
