# Extraction StockCharts — Measured Move Bearish

**Source :** `bundles/stockcharts/measured_move_bearish.md` (HTTP 200 · ~5 600 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D2611 → D2622 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/measured-move-bearish
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Bearish Measured Move. | Measured Move—Bearish | CERTIFIE (accord .md + HTML) |
| image_02.webp | Example of the different components of a Bearish Measured Move. | Measured Move—Bearish | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2611 — Nature : formation en trois parties
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md, image_01) : Le Measured Move est une formation en trois parties qui commence comme figure de retournement et reprend comme figure de continuation. Le Measured Move baissier se compose d'un **déclin de retournement, d'une consolidation/retracement et d'un déclin de continuation**. Comme il ne peut être confirmé qu'après la période de consolidation/retracement, il est catégorisé comme figure de continuation. La figure est généralement long-terme et se forme sur plusieurs mois.
**TRADEX-AI structure_marche** : Figure chartiste baissière à 3 segments (déclin 1 → rebond → déclin 2) ; couche analytique structurelle, jamais déclencheur d'ordre. Durée long-terme à transposer au timeframe Belkhayate.
*Catégorie : structure_marche*

---

### D2612 — Tendance préalable (prior trend)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Pour que le premier déclin qualifie comme retournement, il doit y avoir l'évidence d'une tendance haussière préalable à inverser. Comme le Measured Move baissier peut survenir dans le cadre d'une avance plus large, la longueur et la sévérité du déclin préalable peuvent varier de quelques semaines à plusieurs mois.
**TRADEX-AI configuration** : Pré-condition de détection (hausse préalable identifiée) ; durée variable non normative.
*Catégorie : configuration*

---

### D2613 — Déclin de retournement (reversal decline)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Le premier déclin commence habituellement près des hauts établis de l'avance précédente et s'étend sur quelques semaines à plusieurs mois. Idéalement le déclin est assez ordonné et long, avec des pics et creux déclinants pouvant former un price channel. Un nouveau downtrend est établi par de nouveaux reaction lows ou une cassure sous le support. Les déclins moins erratiques sont satisfaisants mais risquent de devenir une figure différente.
**TRADEX-AI structure_marche** : Segment 1 = déclin ordonné depuis les hauts (pics/creux déclinants, éventuel price channel) ; confirmation par nouveaux reaction lows / cassure de support.
*Catégorie : structure_marche*

---

### D2614 — Consolidation / retracement (33 % à 67 %)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Après un déclin étendu, une consolidation ou un retracement est attendu. En tant que reaction rally, les prix pourraient récupérer **33 % à 67 %** du déclin précédent. Généralement, plus le déclin est grand, plus le reaction rally est grand. Certaines formations de retracement peuvent inclure un flag ascendant ou un rising wedge. Si c'est une consolidation, une figure de continuation comme un rectangle ou un triangle descendant peut se former.
**TRADEX-AI structure_marche** : Segment 2 = rebond de 33–67 % (proportionnel à l'ampleur du déclin) ; sous-figures candidates : flag ascendant, rising wedge, rectangle, triangle descendant.
*Catégorie : structure_marche*

---

### D2615 — Calcul de la longueur du déclin de continuation
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : La distance du haut au bas du premier déclin peut être appliquée au haut de la consolidation/retracement pour estimer la longueur du déclin suivant. Méthode en points : si un titre décline de 60 $ à 40 $ (20 points) et que le rebond le ramène à 50 $, alors 30 $ est la cible du second déclin (50 - 20 = 30). Méthode en pourcentage : déclin de 60 à 40 = -33 % ; projeté depuis 50 $ → 16,50 (50 × 33 % = 16,50 ; 50 - 16,5 = 33,50).
**TRADEX-AI structure_marche** : Règle de projection déterministe (report de l'amplitude du déclin 1 depuis le haut du rebond), méthode points OU pourcentage ; pré-calcul de take-profit et de R/R.
*Catégorie : gestion_risque_entree*

---

### D2616 — Entrée sur le déclin de continuation
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Si la consolidation/retracement forme une figure de continuation, un point d'entrée de second leg peut être identifié via les règles d'AT traditionnelles. Sinon, un autre signal doit être cherché : mesurer les retracements potentiels (33 %, 50 % ou 62 %) et guetter des figures de retournement court-terme ; ou attendre une cassure sous le reaction low du premier déclin comme confirmation de continuation (entrée tardive mais figure confirmée).
**TRADEX-AI gestion_risque_entree** : Deux protocoles d'entrée short — (a) figure de continuation + retracement Fibo + retournement court-terme ; (b) cassure du reaction low (confirmation tardive). Cohérent avec l'exigence de confirmation projet.
*Catégorie : gestion_risque_entree*

---

### D2617 — Comportement du volume
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Le volume devrait **augmenter** durant le déclin de retournement, **diminuer** en fin de consolidation/retracement, et **augmenter à nouveau** durant le déclin de continuation. C'est le schéma de volume idéal, mais la confirmation par le volume est moins importante pour les figures baissières que pour les figures haussières.
**TRADEX-AI signal** : Signature volumétrique idéale (haut-bas-haut) ; mappable sur l'order-flow ATAS, avec poids moindre côté baissier.
*Catégorie : signal*

---

### D2618 — Patterns imbriqués possibles
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Plusieurs figures peuvent coexister dans un Measured Move baissier : un double top peut marquer le premier retournement et déclin ; un price channel peut se former durant ce déclin ; un triangle descendant peut marquer la consolidation ; et un autre price channel peut se former durant la continuation du déclin.
**TRADEX-AI structure_marche** : Composabilité de figures (double top, price channel, triangle descendant) à l'intérieur du Measured Move — utile pour un détecteur hiérarchique.
*Catégorie : structure_marche*

---

### D2619 — Séries de Measured Moves en marchés long-terme
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Une série de Measured Moves baissiers peut se former durant des marchés baissiers (ou haussiers) pluriannuels. Un mouvement baissier de trois legs peut inclure : retournement et déclin (leg 1), retracement, déclin (leg 2), retracement, puis déclin du troisième leg.
**TRADEX-AI structure_marche** : Récursivité possible (Measured Moves enchaînés en 3 legs) ; structure fractale à borner par contexte.
*Catégorie : structure_marche*

---

### D2620 — Limites des cibles (overshoot / shortfall)
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Bien que les cibles de projection du déclin de continuation soient utiles, elles ne doivent servir que de **lignes directrices approximatives**. Les titres peuvent dépasser leurs cibles mais aussi rester en deçà. L'évaluation technique doit être continue. De plus, le second déclin peut être moins ordonné que le premier, surtout sur les titres volatils.
**TRADEX-AI gestion_risque_entree** : Cible = guide non-absolu (overshoot/shortfall possibles) ; réévaluation continue requise — cohérent avec l'exigence projet de R/R ≥ 1:2 et confirmation.
*Catégorie : gestion_risque_entree*

---

### D2621 — Exemple XIRC : déclin de retournement et amplitude
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md, image_02) : XIRC a atteint son plus haut historique à 69,69 $ le 31/12/1999. Le titre a cassé le support de trend line en janvier 2000 ; un lower low a été enregistré sous 45 $ en février 2000. Le déclin a mené le titre à 29,13 $ en avril 2000, soit **40,56 points** au total. Le rebond a récupéré ~50 % (jusqu'à 52,75 $) sur avril-mai-juin, formant un price channel parallèle (allure de grand flag) ; en excluant le pic, l'interprétation pouvait être un rising wedge — dans tous les cas, le support était la trend line basse.
**TRADEX-AI structure_marche** : Illustration empirique (amplitude 40,56 pts, rebond ~50 %, sous-figure flag/wedge) ; cas de calibration visuelle de la phase 1-2.
*Catégorie : configuration*

---

### D2622 — Exemple XIRC : projection, entrée et volume
🟢 **FAIT VÉRIFIÉ** (Source : measured_move_bearish.md) : Longueur estimée du déclin de continuation = 40,56 points depuis le haut de juin à 52,75 $ → cible 12,19 $. La méthode pourcentage peut être plus adaptée si la cible paraît anormalement basse : déclin de 69,69 à 29,13 = 58 % ; un -58 % depuis 52,75 → cible ~22,16 $. Entrée fondée sur la cassure de la trend line de support (flèches rouges). Volume accru avant la cassure de janvier 2000, à la cassure du reaction low précédent (flèches bleues), et lors de la cassure de la trend line en juillet (flèches rouges).
**TRADEX-AI gestion_risque_entree** : Application concrète des deux méthodes de projection (points vs %) et de l'entrée sur cassure + confirmation volume ; modèle reproductible pour pré-calculer cible et R/R.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D2611 → D2622 (12 décisions) |
| Images certifiées | 2/2 |
| Catégories couvertes | structure_marche · configuration · signal · gestion_risque_entree |
| Cercle dominant | structure_marche (figure de projection chartiste) |
| Lien Belkhayate | NON CONCERNÉ (figure d'AT classique StockCharts ChartSchool, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées. Note : durées en semaines/mois à transposer aux timeframes Belkhayate (15min / Range Bar) ; ne pas copier les valeurs en mois |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Figure d'analyse technique classique (StockCharts ChartSchool), aucun rapport affirmé avec la méthode Belkhayate.
