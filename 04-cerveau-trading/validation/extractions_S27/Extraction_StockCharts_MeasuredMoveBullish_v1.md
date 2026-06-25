# Extraction StockCharts — Measured Move Bullish

**Source :** `bundles/stockcharts/measured_move_bullish.md` (HTTP 200 · ~5 100 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D2631 → D2642 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/measured-move-bullish
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Bullish Measured Move. | Measured Move—Bullish | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a Bullish Measured Move in Intel Corp's stock. | Measured Move—Bullish | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2631 — Nature : formation en trois parties
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md, image_01) : Le Measured Move est une formation en trois parties qui commence comme figure de retournement et reprend comme figure de continuation. Le Measured Move haussier se compose d'une **avance de retournement, d'une correction/consolidation et d'une continuation**. Comme il ne peut être correctement identifié qu'après la période de correction/consolidation, il est catégorisé comme figure de continuation. La figure est généralement long-terme et se forme sur plusieurs mois.
**TRADEX-AI structure_marche** : Figure chartiste haussière à 3 segments (avance 1 → correction → avance 2) ; couche analytique structurelle, jamais déclencheur d'ordre. Durée long-terme à transposer au timeframe Belkhayate.
*Catégorie : structure_marche*

---

### D2632 — Tendance préalable (prior trend)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Pour que la première avance qualifie comme retournement, il doit y avoir l'évidence d'une tendance baissière préalable à inverser. Comme le Measured Move haussier peut survenir dans le cadre d'une avance plus large, la longueur et la sévérité du déclin préalable peuvent varier de quelques semaines à plusieurs mois.
**TRADEX-AI configuration** : Pré-condition de détection (baisse préalable identifiée) ; durée variable non normative.
*Catégorie : configuration*

---

### D2633 — Avance de retournement (reversal advance)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : La première avance commence habituellement près des bas établis du déclin précédent et s'étend sur quelques semaines à plusieurs mois. Le nouvel uptrend est établi par de nouveaux reaction highs ou une cassure au-dessus de la résistance. Idéalement l'avance est assez ordonnée et longue, avec une série de pics et creux montants pouvant former un price channel. Les avances moins erratiques sont satisfaisantes mais risquent de former une figure différente.
**TRADEX-AI structure_marche** : Segment 1 = avance ordonnée depuis les bas (pics/creux montants, éventuel price channel) ; confirmation par nouveaux reaction highs / cassure de résistance.
*Catégorie : structure_marche*

---

### D2634 — Consolidation / correction (33 % à 67 %)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Après une avance étendue, une consolidation ou correction est attendue. En consolidation : figure de continuation type rectangle ou triangle ascendant. En correction : retracement de **33 % à 67 %** de l'avance précédente, avec figures possibles type grand flag descendant ou falling wedge. Généralement, plus l'avance est grande, plus la correction est grande : une avance de 100 % peut voir une correction de 62 %, une avance de 50 % seulement 33 %.
**TRADEX-AI structure_marche** : Segment 2 = correction de 33–67 % (proportionnelle à l'ampleur de l'avance) ; sous-figures candidates : rectangle, triangle ascendant, flag descendant, falling wedge.
*Catégorie : structure_marche*

---

### D2635 — Calcul de la longueur de l'avance de continuation
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : La distance du bas au haut de la première avance peut être appliquée au bas de la consolidation/retracement pour estimer l'avance projetée. Méthode en points : si la première avance va de 30 $ à 50 $ (mouvement de 20 $) et la correction à 40 $, la cible du second leg est 60 $ (50 - 30 = 20 ; 40 + 20 = 60). Méthode en pourcentage : avance de 30 à 50 = 66 % ; depuis 40 $ → cible 66,40 (40 × 66 % = 26,40 ; 40 + 26,40 = 66,40).
**TRADEX-AI structure_marche** : Règle de projection déterministe (report de l'amplitude de l'avance 1 depuis le bas de la correction), méthode points OU pourcentage ; pré-calcul de take-profit et de R/R.
*Catégorie : gestion_risque_entree*

---

### D2636 — Entrée sur l'avance de continuation
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Si la consolidation/correction comprend une figure de continuation, les points d'entrée de second leg s'identifient via les règles de breakout normales. Sinon, un autre signal de breakout de continuation doit être cherché : mesurer les retracements potentiels (33 %, 50 % ou 62 %) et guetter des figures de retournement court-terme pour de bons points reward-to-risk ; ou attendre une cassure au-dessus du reaction high de la première avance comme confirmation (entrée tardive mais figure confirmée).
**TRADEX-AI gestion_risque_entree** : Deux protocoles d'entrée long — (a) figure de continuation + retracement Fibo + retournement court-terme (bon R/R) ; (b) cassure du reaction high (confirmation tardive). Cohérent avec l'exigence de confirmation projet.
*Catégorie : gestion_risque_entree*

---

### D2637 — Comportement du volume
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Le volume devrait **augmenter** au début de l'avance de retournement, **diminuer** en fin de consolidation/correction, et **augmenter à nouveau** au début de l'avance de continuation.
**TRADEX-AI signal** : Signature volumétrique idéale (haut-bas-haut) ; mappable sur l'order-flow ATAS comme confirmation.
*Catégorie : signal*

---

### D2638 — Patterns imbriqués et séries multi-années
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Le Measured Move haussier peut être composé de plusieurs figures : un double bottom pour démarrer l'avance de retournement, un price channel durant l'avance, un triangle ascendant pour la consolidation, et un autre price channel pour la continuation. Une série de Measured Moves haussiers peut se former durant des marchés haussiers (ou baissiers) pluriannuels.
**TRADEX-AI structure_marche** : Composabilité de figures (double bottom, price channel, triangle ascendant) et récursivité multi-années ; structure fractale pour détecteur hiérarchique.
*Catégorie : structure_marche*

---

### D2639 — Limites des cibles (overshoot / shortfall)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Bien que les projections de l'avance de continuation soient utiles comme cibles, elles ne doivent servir que de **lignes directrices approximatives**. Les titres peuvent dépasser leurs cibles mais aussi rester en deçà — l'évaluation technique doit être continue.
**TRADEX-AI gestion_risque_entree** : Cible = guide non-absolu (overshoot/shortfall possibles) ; réévaluation continue requise — cohérent avec l'exigence projet de R/R ≥ 1:2 et confirmation.
*Catégorie : gestion_risque_entree*

---

### D2640 — Exemple INTC : tendance préalable et cassure
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md, image_02) : Intel (INTC) — après un large trading range descendant sur l'essentiel de 1997-1998, le titre a cassé au-dessus de la résistance début novembre (flèches bleues) et démarré le premier leg d'un Measured Move haussier. La cassure est survenue avec un fort mouvement au-dessus de la résistance à 22 $ avec deux semaines de fort volume (flèches vertes). L'avance a débuté à 17,44 $ et s'est terminée à 35,92 $.
**TRADEX-AI structure_marche** : Illustration empirique du segment 1 (sortie de range, cassure de résistance à 22 $, amplitude 17,44 → 35,92 $) ; cas de calibration visuelle.
*Catégorie : configuration*

---

### D2641 — Exemple INTC : correction (descending flag, 54 %)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Après l'avance étendue, le titre a décliné dans une fourchette ressemblant à un grand descending flag. Le déclin a retracé environ **54 %** de l'avance précédente.
**TRADEX-AI structure_marche** : Segment 2 empirique (descending flag, retracement 54 % — dans la plage 33-67 %) ; confirme la sous-figure de correction haussière.
*Catégorie : configuration*

---

### D2642 — Exemple INTC : projection, entrée et volume
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bullish.md) : Longueur estimée de l'avance = 18,48 points depuis le bas de juin à 25,94 $ → cible 44,42 $. Le haut réel fut 44,75 $ pour une avance de 18,81 $. Entrée fondée sur la cassure de la ligne de résistance (flèche rouge), la correction ayant formé une figure de continuation. Volume accru début novembre (début de l'avance de retournement), décru de mars à mai 1999, puis accru à nouveau au début de l'avance de continuation (flèches vertes).
**TRADEX-AI gestion_risque_entree** : Application concrète de la projection (cible 44,42 $ vs réel 44,75 $, écart minime) et de l'entrée sur cassure + confirmation volume ; modèle reproductible pour pré-calculer cible et R/R.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D2631 → D2642 (12 décisions) |
| Images certifiées | 2/2 |
| Catégories couvertes | structure_marche · configuration · signal · gestion_risque_entree |
| Cercle dominant | structure_marche (figure de projection chartiste) |
| Lien Belkhayate | NON CONCERNÉ (figure d'AT classique StockCharts ChartSchool, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées. Note : durées en semaines/mois à transposer aux timeframes Belkhayate (15min / Range Bar) ; ne pas copier les valeurs en mois |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Figure d'analyse technique classique (StockCharts ChartSchool), aucun rapport affirmé avec la méthode Belkhayate.
