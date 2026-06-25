# Extraction StockCharts — Broadening Top / Megaphone Top
**Source :** `bundles/stockcharts/broadening_top_or_megaphone_top.md` (HTTP 200 · ~4 200 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 1/1 certifiée
**Décisions :** D951 → D960 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/broadening-top-or-megaphone-top
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> NB : pattern chartiste pur → catégorie dominante `structure_marche`.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.jpg | Illustration of broadening top or megaphone top pattern. | Are Broadening Tops Bearish or Bullish? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D951 — Définition du Broadening Top
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md, image_01) : Le Broadening Top est une figure chartiste caractérisée par des sommets successifs plus hauts et des creux successifs plus bas. En traçant une ligne de tendance sur les hauts et les bas du mouvement, la figure ressemble à un mégaphone ou à un triangle inversé (reverse triangle).
**TRADEX-AI C1** : Figure de structure de prix identifiable géométriquement (HH + LL divergents) ; couche analytique, jamais déclencheur d'ordre.
*Catégorie : structure_marche*

---

### D952 — Signification : désaccord volatil entre acheteurs et vendeurs
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : L'indication la plus fiable de toute formation en élargissement (Top ou Bottom) est un désaccord volatil entre investisseurs haussiers et baissiers. Les haussiers poussent les prix à la hausse, les baissiers vendent (ou vendent à découvert), provoquant une série de plus hauts plus hauts (HH) et de plus bas plus bas (LL).
**TRADEX-AI C5** : Lecture de sentiment / instabilité ; signale incertitude de marché, à corréler avec VIX.
*Catégorie : structure_marche*

---

### D953 — Caractère ambigu : ni clairement haussier ni baissier
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Bien que beaucoup d'investisseurs long terme considèrent le Broadening Top comme baissier (volatilité et incertitude tendant à être baissières), sa performance historique est ambiguë : (1) performance historique faible comme figure haussière ou baissière, car il revient (pull back) dans la plage de la figure plus de 60% du temps ; (2) malgré son nom de figure de « sommet », il tend statistiquement à monter plus qu'à descendre, ce qui en fait davantage une figure de continuation qu'une figure de retournement ; (3) il reste tradable mais avec des fluctuations larges post-cassure.
**TRADEX-AI C1** : Figure à faible fiabilité directionnelle ; à traiter comme signal de prudence, jamais comme biais directionnel fort.
*Catégorie : structure_marche*

---

### D954 — Critère d'identification : nombre de touches (≥ 5)
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Il doit y avoir au moins cinq touches au total. Trois peuvent être des sommets ou creux touchant la ligne de tendance associée ; deux touches ou plus doivent toucher l'autre ligne de tendance. Une « touche » diffère d'une « approche » (qui s'approche sans toucher). Idéalement, la deuxième touche doit faire contact avec la ligne de tendance.
**TRADEX-AI C1** : Critère de validation géométrique codable (compter touches confirmées des deux lignes divergentes) ; distinguer touche vs approche.
*Catégorie : configuration*

---

### D955 — Critère d'identification : espaces remplis (filled spaces)
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Les prix doivent traverser la figure d'un côté à l'autre, remplissant la zone de mouvement de prix. Il ne doit pas y avoir de larges « espaces blancs » dans la figure témoignant d'un manque d'activité de prix.
**TRADEX-AI C1** : Critère de qualité de la figure (densité de remplissage) ; filtre anti-faux-pattern.
*Catégorie : configuration*

---

### D956 — Critère : cassure possible dans n'importe quelle direction
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Une cassure (breakout) peut survenir dans n'importe quelle direction et se produit quand le prix perce une ligne de tendance ou dépasse au-dessus/en-dessous de la hauteur de la formation.
**TRADEX-AI C1** : Direction non déterminée a priori ; attendre la cassure effective, ne pas anticiper le sens.
*Catégorie : signal*

---

### D957 — Trading : objectif de prix par hauteur de la figure
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Calculer la hauteur = différence entre le plus haut sommet et le plus bas creux. Cassure haussière → ajouter la hauteur au sommet de la formation pour l'objectif (prise de profit à ~100% de la hauteur). Cassure baissière → soustraire la hauteur du bas de la formation pour l'objectif (prise de profit à ~100% de la hauteur).
**TRADEX-AI C1** : Calcul d'objectif déterministe (mesure de hauteur projetée) implémentable ; même logique haut/bas selon le sens de cassure.
*Catégorie : gestion_risque_entree*

---

### D958 — Trading : stop loss à l'extrémité opposée
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Placer un stop loss à l'extrémité opposée de la figure, c'est-à-dire au swing high ou swing low opposé selon que l'on est long ou short.
**TRADEX-AI C1** : Règle de placement de stop codable ; aligne le stop sur l'extrême structurel opposé.
*Catégorie : gestion_risque_entree*

---

### D959 — Avertissement : pullbacks fréquents (>60%) et stratégie intra-figure risquée
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Une fois la position ouverte (long ou short), les prix reviennent dans la plage de la figure plus de 60% du temps, dépassant le point d'entrée dans le sens opposé. Avertissement (hint danger) : les swing traders peuvent prendre le sens opposé à l'intérieur de la formation (long ou short dans la séquence des cinq touches) — opportunité tradable mais stratégie à haut risque. Indicateurs d'aide : RSI, Stochastique, Bollinger Bands (surachat/survente), niveaux de support/résistance, retracements de Fibonacci, Chaikin Money Flow (pression acheteuse/vendeuse), Rate of Change (force/momentum de cassure).
**TRADEX-AI C1** : Garde-fou anti-pullback obligatoire (>60% de retour) ; signaux à confirmer par indicateurs de surachat/survente avant exécution.
*Catégorie : gestion_risque_entree*

---

### D960 — Contexte macro/politique sous-jacent et synthèse
🟢 **FAIT VÉRIFIÉ** (Source : broadening_top_or_megaphone_top.md) : Avertissement (hint important) : les formations en élargissement résultent souvent de désaccords entre participants, généralement à base fondamentale (perception de risques économiques, parfois politiques). On peut les trader techniquement mais il aide d'être conscient du contexte économique/politique. Synthèse : figure ressemblant à un triangle inversé/mégaphone, signalant une volatilité et un désaccord significatifs ; souvent perçue baissière mais performance ambiguë ; à aborder avec prudence et bonne tolérance au risque.
**TRADEX-AI C6** : Recouper la figure avec le contexte macro/news (NFP/FOMC/CPI) ; cohérent avec le News Gate du système.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D951 | Définition Broadening Top | 🟢 | C1 | structure_marche |
| D952 | Désaccord volatil acheteurs/vendeurs | 🟢 | C5 | structure_marche |
| D953 | Caractère ambigu (continuation > retournement) | 🟢 | C1 | structure_marche |
| D954 | Critère ≥ 5 touches | 🟢 | C1 | configuration |
| D955 | Critère espaces remplis | 🟢 | C1 | configuration |
| D956 | Cassure dans n'importe quelle direction | 🟢 | C1 | signal |
| D957 | Objectif par hauteur projetée | 🟢 | C1 | gestion_risque_entree |
| D958 | Stop à l'extrémité opposée | 🟢 | C1 | gestion_risque_entree |
| D959 | Pullbacks >60% / confirmation indicateurs | 🟢 | C1 | gestion_risque_entree |
| D960 | Contexte macro/politique + synthèse | 🟢 | C6 | structure_marche |

**Liens Belkhayate :** Le Broadening Top n'est PAS une figure Belkhayate (⚫). Lien indirect : sa lecture comme zone de désaccord/volatilité élevée recoupe la prudence « ne pas trader dans le chaos » ; à utiliser comme contexte de structure, jamais comme signal autonome.

**À vérifier (humain) :**
- D953/D959 — statistiques « >60% pullback » et « monte plus qu'il ne descend » issues d'études sur actions (Bulkowski-like, non sourcées chiffrées ici) ; non validées sur futures GC/HG/CL/ZW → traiter comme indicatif, pas comme paramètre dur.
- D957 — la projection de hauteur à 100% est une heuristique chartiste, pas une garantie ; à backtester sur les actifs cibles avant toute implémentation d'objectif automatique.
- Figure chartiste discrétionnaire : la détection automatique fiable (touches, espaces remplis) est non triviale et demande validation visuelle humaine.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
