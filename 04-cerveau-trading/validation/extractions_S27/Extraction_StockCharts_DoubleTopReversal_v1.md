# Extraction StockCharts — Double Top Reversal

**Source :** `bundles/stockcharts/double_top_reversal.md` (HTTP 200 · ~9 000 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 3/3 certifiées · 0 à vérifier
**Décisions :** D1571 → D1583 · **Page :** chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/double-top-reversal
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **PERTINENCE FUTURES** : configuration de retournement baissier de **structure de marché (C1)** universelle aux barres/lignes/chandeliers. Directement applicable aux actifs TRADING (GC·HG·CL·ZW) sur n'importe quel timeframe. Aucun lien Belkhayate affirmé par la source.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié (manifest) | Section .md | Décision liée |
|-------|---------------------------|-------------|---------------|
| image_01 | Example of a classic Double Top Reversal pattern. | Double Top Reversal | D1571 |
| image_02 | An example of a double top formation that took five months to form. | Double Top Reversal | D1582 |
| image_03 | A closer look at the support turned resistance level in Ford Motor Co. (F). | Double Top Reversal | D1583 |

---

## DÉCISIONS

### D1571 — Définition et nature du Double Top Reversal
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md, image_01) : Le Double Top Reversal est un **patron de retournement baissier** que l'on trouve typiquement sur les graphiques en barres, en lignes et en chandeliers. Il présente **deux pics consécutifs à peu près égaux**, séparés par un **creux modéré**. Le patron classique marque au moins un changement de tendance de moyen terme, du haussier vers le baissier.
🟡 **CONVENTION** (Source : double_top_reversal.md) : Un Double Top Reversal sur graphique en barres/lignes **diffère** d'un Double Top Breakout sur graphique P&F (point & figure), qui est lui un patron **haussier** marquant une cassure de résistance vers le haut. (Convention de nomenclature StockCharts, pas un fait de prix.)
**TRADEX-AI C1** : Brique de structure de marché — signal de retournement haussier→baissier. Applicable GC·HG·CL·ZW. Ne pas confondre avec la variante P&F.
*Catégorie : structure_marche*

---

### D1572 — Prérequis : tendance préalable (uptrend de plusieurs mois)
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Comme tout patron de retournement, il **doit exister une tendance à inverser**. Pour le Double Top Reversal, une **tendance haussière significative de plusieurs mois** doit être en place.
**TRADEX-AI C1** : Filtre de validité — ne reconnaître un Double Top que si une tendance haussière établie précède la formation.
*Catégorie : configuration*

---

### D1573 — Premier pic
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Le **premier pic** doit marquer le point le plus haut de la tendance courante. À ce stade il est tout à fait normal et la tendance haussière n'est **pas** en danger ni remise en question.
**TRADEX-AI C1** : Le premier pic seul n'est pas un signal — ne déclenche aucune alerte de retournement.
*Catégorie : structure_marche*

---

### D1574 — Creux : déclin 10-20 %, volume négligeable, demande tiède
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Après le premier pic, il y a généralement un **déclin de 10 à 20 %**. Le **volume** sur ce déclin est habituellement **négligeable**. Les plus-bas sont parfois arrondis ou étirés, ce qui peut signaler une **demande tiède**.
**TRADEX-AI C1+C2** : Le creux apporte une brique volume (C2) — un creux long et traînant à demande faible renforce la probabilité du retournement.
*Catégorie : structure_marche*

---

### D1575 — Deuxième pic : retour vers le sommet précédent, tolérance ~3 %
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : L'avance depuis le creux se fait généralement à **faible volume** et remonte vers le sommet précédent ; une **résistance** au niveau de l'ancien sommet est attendue. Ce n'est qu'après avoir rencontré cette résistance qu'un Double Top devient possible (toujours non confirmé). Le délai entre les deux pics varie de quelques semaines à plusieurs mois (**norme : 1 à 3 mois**). Des pics exacts sont préférables mais un **deuxième pic à moins de 3 % de l'ancien sommet est généralement adéquat**.
**TRADEX-AI C1** : Tolérance opérationnelle codable : écart entre pics ≤ ~3 %. Faible volume sur le 2e pic = signe de demande affaiblie.
*Catégorie : configuration*

---

### D1576 — Déclin depuis le 2e pic : expansion de volume / descente accélérée
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Le déclin depuis le deuxième pic devrait s'accompagner d'une **expansion du volume** et/ou d'une **descente accélérée**, parfois marquée par un ou deux gaps. Cela montre que les forces de la demande sont plus faibles que l'offre et qu'un test du support est imminent.
**TRADEX-AI C1+C2** : Confirmation par volume croissant à la baisse — brique C2 couplée à la structure C1.
*Catégorie : signal*

---

### D1577 — Cassure du support = complétion du patron
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Même après avoir retracé jusqu'au support, le retournement reste **incomplet**. C'est la **cassure du support** (le point le plus bas entre les deux pics, la « neckline ») qui **complète** le Double Top Reversal. Cette cassure devrait survenir avec **volume accru et/ou descente accélérée**.
**TRADEX-AI C1** : Critère DÉCLENCHEUR du signal — aucun signal valide tant que le support entre les pics n'est pas cassé.
*Catégorie : signal*

---

### D1578 — Support devenu résistance (retest / reaction rally)
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Le support cassé devient une **résistance potentielle**. Ce nouveau niveau de résistance est parfois retesté par un **reaction rally**. Ce retest offre une seconde chance de sortir d'une position ou d'initier une vente à découvert.
**TRADEX-AI C1** : Brique de gestion d'entrée — le retest du support cassé est un point d'entrée short alternatif.
*Catégorie : gestion_risque_entree*

---

### D1579 — Objectif de prix (hauteur du patron projetée vers le bas)
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Objectif = **soustraire la distance entre la cassure du support et le sommet** au niveau de cassure. Donc plus la formation est grande, plus le déclin potentiel est important.
**TRADEX-AI C1** : Brique objectif/cible projetée — calcul déterministe codable pour estimer le take-profit théorique.
*Catégorie : gestion_risque_entree*

---

### D1580 — Garde-fous anti-faux-signaux : espacement et profondeur du creux
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : Les pics devraient être **séparés d'environ un mois** ; trop proches, ils représentent une simple résistance plutôt qu'un vrai changement offre/demande. Le creux entre les pics doit baisser **d'au moins 10 %** ; un déclin sous 10 % peut ne pas traduire une hausse significative de la pression vendeuse.
**TRADEX-AI C1** : Filtres de qualité codables : espacement pics ≈ 1 mois ET profondeur creux ≥ 10 %.
*Catégorie : configuration*

---

### D1581 — Filtres de validation : ne pas anticiper la cassure (prix / temps)
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md) : L'aspect le plus important est de **ne pas brûler les étapes** : attendre que le support soit cassé avec expansion de volume. On peut appliquer un **filtre de prix** (ex. exiger une cassure de **3 %** du support avant validation) ou un **filtre de temps** (ex. la cassure doit tenir **3 jours** pour être valide). La tendance reste en vigueur tant qu'elle n'est pas invalidée : tant que le support n'est pas cassé de façon convaincante, la tendance demeure haussière.
**TRADEX-AI C1** : Garde-fou anti-faux-signal directement codable : filtre prix 3 % OU filtre temps 3 jours avant de valider un signal de retournement.
*Catégorie : gestion_risque_entree*

---

### D1582 — Exemple Ford (F) : formation sur cinq mois
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md, image_02) : Exemple Ford : titre avancé d'un plus-bas près de 10 (mars 1997) à 36 (déc. 1998), déclin d'environ **15 %** du 1er pic vers le creux, creux long et traînant (plus-bas près de 30½ début février, pas de rebond avant début avril) = demande tiède. Déclin depuis 36,80 $ avec **deux gaps** baissiers et volume accru ; le **Chaikin Money Flow** est passé sous -10 % puis sous -20 %, traduisant une forte hausse de la pression vendeuse. Le support a été cassé début juin sous 28,50 $ (> 3 % sous le support de 30,50 $).
**TRADEX-AI C1+C2** : Illustre l'usage conjoint structure (C1) + flux monétaire/volume (C2, ici CMF) pour confirmer un Double Top.
*Catégorie : configuration*

---

### D1583 — Exemple Ford : support devenu résistance et suite baissière
🟢 **FAIT VÉRIFIÉ** (Source : double_top_reversal.md, image_03) : Sur Ford, **30,75 $** a marqué le niveau support-devenu-résistance et **31 $** un retracement de 50 % du déclin de 36,80 $ à 25 $ ; une **zone de résistance entre 31 et 32 $** pouvait être établie. Le titre a ensuite formé un **lower high à 30 $** (jan. 2000) puis décliné vers ~22 $ à mi-mars.
**TRADEX-AI C1** : Confirme empiriquement le mécanisme support→résistance (D1578) et la poursuite baissière post-complétion.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie | Actifs |
|---|----------|-----|--------|-----------|--------|
| D1571 | Définition / nature baissière | 🟢🟡 | C1 | structure_marche | GC·HG·CL·ZW |
| D1572 | Prérequis tendance haussière | 🟢 | C1 | configuration | GC·HG·CL·ZW |
| D1573 | Premier pic | 🟢 | C1 | structure_marche | GC·HG·CL·ZW |
| D1574 | Creux 10-20 %, volume faible | 🟢 | C1·C2 | structure_marche | GC·HG·CL·ZW |
| D1575 | Deuxième pic, tolérance ~3 % | 🟢 | C1 | configuration | GC·HG·CL·ZW |
| D1576 | Déclin 2e pic + volume | 🟢 | C1·C2 | signal | GC·HG·CL·ZW |
| D1577 | Cassure support = complétion | 🟢 | C1 | signal | GC·HG·CL·ZW |
| D1578 | Support→résistance / retest | 🟢 | C1 | gestion_risque_entree | GC·HG·CL·ZW |
| D1579 | Objectif de prix | 🟢 | C1 | gestion_risque_entree | GC·HG·CL·ZW |
| D1580 | Garde-fous espacement/profondeur | 🟢 | C1 | configuration | GC·HG·CL·ZW |
| D1581 | Filtres prix 3 % / temps 3 jours | 🟢 | C1 | gestion_risque_entree | GC·HG·CL·ZW |
| D1582 | Exemple Ford (5 mois) | 🟢 | C1·C2 | configuration | GC·HG·CL·ZW |
| D1583 | Ford : support→résistance | 🟢 | C1 | structure_marche | GC·HG·CL·ZW |

**Total : 13 décisions (D1571→D1583) · 3/3 images certifiées · 0 cas à vérifier.**
Lien Belkhayate : **NON CONCERNÉ** (la source ne mentionne pas Belkhayate).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
