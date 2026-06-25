# Extraction StockCharts — Double Bottom Reversal
**Source :** `bundles/stockcharts/double_bottom_reversal.md` (HTTP 200 · ~4 600 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1531 → D1542 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/double-bottom-reversal
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a double bottom reversal. | Double Bottom Reversal | CERTIFIE (accord .md + HTML) |
| image_02.png | A double bottom reversal in PFE stock. | Double Bottom Reversal | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1531 — Nature du Double Bottom Reversal
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md, image_01) : Le Double Bottom Reversal est une figure de retournement haussière typiquement trouvée sur graphiques en barres, en lignes et en chandeliers. Comme son nom l'indique, la figure comprend deux creux consécutifs à peu près égaux, avec un sommet modéré entre les deux. Classiquement, elle marque un changement de tendance intermédiaire ou de long terme.
**TRADEX-AI C1** : Pattern de retournement haussier de structure de marché. À traiter comme configuration de retournement, à confirmer (cassure de résistance) avant tout signal.
*Catégorie : configuration*

---

### D1532 — Distinction vs Double Bottom Breakdown (P&F)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Un Double Bottom Reversal sur graphique en barres ou en lignes est différent d'un Double Bottom Breakdown sur graphique Point & Figure (P&F). Les Double Bottom Breakdowns sur P&F sont des figures BAISSIÈRES qui marquent une cassure de support à la baisse.
**TRADEX-AI C1** : Garde-fou de nommage : ne pas confondre le pattern haussier (barres/lignes) avec la figure baissière P&F homonyme. Distinction à coder si jamais des règles P&F coexistent.
*Catégorie : configuration*

---

### D1533 — Tendance préalable requise (downtrend significatif)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Avec toute figure de retournement, il doit exister une tendance préalable à inverser. Pour le Double Bottom Reversal, un downtrend significatif de plusieurs mois doit être en place. De nombreux pseudo double bottoms peuvent se former pendant un downtrend, mais tant que la résistance clé n'est pas cassée, le retournement ne peut être confirmé.
**TRADEX-AI C1** : Condition contextuelle obligatoire : downtrend de plusieurs mois en amont. Sans cassure de résistance, pas de retournement confirmé → pas de signal.
*Catégorie : structure_marche*

---

### D1534 — Premier creux
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Le premier creux doit marquer le point le plus bas de la tendance courante. Il est assez normal, et le downtrend reste fermement en place à ce stade.
**TRADEX-AI C1** : Repère structurel : le premier creux = plus bas de la tendance en cours. Pas de signal à ce stade. Élément de détection de pattern.
*Catégorie : structure_marche*

---

### D1535 — Sommet intermédiaire (rebond 10-20 %, volume faible)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Après le premier creux, une avance suit généralement, de l'ordre de 10 à 20 %. Le volume sur cette avance est habituellement insignifiant, mais une hausse pourrait signaler une accumulation précoce. Le sommet est parfois arrondi/étiré par l'hésitation à repartir à la baisse, indiquant une demande croissante mais pas encore assez forte pour une cassure.
**TRADEX-AI C2** : Paramètre quantitatif : rebond 10-20 % entre creux. Le volume du rebond, s'il augmente, est un indice précoce d'accumulation (lecture ATAS/volume). Mesure utilisable dans la détection.
*Catégorie : structure_marche*

---

### D1536 — Second creux (support du précédent, dans 3 %, espacement)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Le déclin depuis le sommet de réaction se fait habituellement sur volume faible et rencontre le support du précédent plus bas. Même après l'établissement du support, seule la possibilité d'un Double Bottom Reversal existe (encore à confirmer). Le temps entre creux varie de quelques semaines à plusieurs mois, la norme étant 1 à 3 mois. Des creux exacts sont préférables, mais un creux dans les 3 % de son prédécesseur est considéré comme valide.
**TRADEX-AI C1** : Critères quantitatifs de validation : 2e creux ≤ 3 % d'écart du 1er, espacement typique 1-3 mois, déclin sur volume faible. Tolérance 3 % codable directement dans le détecteur.
*Catégorie : configuration*

---

### D1537 — Avance depuis le second creux (volume/pression acheteuse en accélération)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Le volume est plus important pour le Double Bottom Reversal que pour le double top. Il doit y avoir une preuve claire que le volume et la pression acheteuse accélèrent durant l'avance depuis le second creux. Une ascension accélérée, éventuellement marquée d'un ou deux gaps, indique aussi un possible changement de sentiment.
**TRADEX-AI C2** : Confirmation volumétrique essentielle : avance post-2e creux DOIT s'accompagner d'un volume/pression acheteuse en accélération (lecture ATAS/delta). Critère discriminant du pattern.
*Catégorie : signal*

---

### D1538 — Cassure de résistance (validation de la figure)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Même après être remonté jusqu'à la résistance, le retournement reste incomplet. La cassure de la résistance — le point le plus haut entre les deux creux — complète le Double Bottom Reversal. Comme les avances, elle doit se produire avec un volume accru et/ou une ascension accélérée. La figure n'est complète que lorsque le précédent sommet de réaction est franchi.
**TRADEX-AI C2** : Déclencheur de validation : cassure du sommet inter-creux + volume accru. C'est LE point de confirmation — aucun signal avant. Condition booléenne nette pour le moteur.
*Catégorie : signal*

---

### D1539 — Résistance devenue support (retest, opportunité d'entrée)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : La résistance cassée devient un support potentiel, et parfois la première correction teste ce nouveau niveau. Un tel test peut offrir une seconde chance de clôturer une position courte ou d'initier une position longue.
**TRADEX-AI C1** : Le retest de la résistance-devenue-support = point d'entrée long à R/R amélioré. Logique d'entrée transposable (entrée sur pullback après cassure).
*Catégorie : gestion_risque_entree*

---

### D1540 — Objectif de prix (mesure de la figure)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : Pour estimer un objectif, la distance entre la cassure de résistance et le plus bas des creux est ajoutée au prix de la cassure. Cela implique que plus la figure est grande, plus l'avance potentielle est importante.
**TRADEX-AI C1** : Cible déterministe : objectif = prix de cassure + (cassure − plus bas des creux). Calcul direct utilisable pour fixer un take-profit et évaluer le R/R (≥ 1:2).
*Catégorie : gestion_risque_entree*

---

### D1541 — Cadre temporel et patience (≥ 4 semaines, indicateurs de volume)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md) : C'est une figure de retournement intermédiaire à long terme qui ne se forme pas en quelques jours ; au moins quatre semaines entre les plus bas sont préférables. Les creux mettent généralement plus de temps à se former que les sommets — la patience est une vertu. Rappel des critères : avance du 1er creux 10-20 %, 2e creux dans 3 % du précédent, volume en hausse sur l'avance suivante. Les indicateurs de volume Chaikin Money Flow (CMF), OBV et Accumulation/Distribution servent à repérer la pression acheteuse. Attendre la cassure de résistance est primordial.
**TRADEX-AI C2** : Contrainte temporelle (≥ 4 semaines entre creux) + outils de confirmation volume (CMF/OBV/A-D). Filtre anti-faux-signal : ne pas valider un « double bottom » trop rapide.
*Catégorie : configuration*

---

### D1542 — Exemple PFE (illustration des critères)
🟢 **FAIT VÉRIFIÉ** (Source : double_bottom_reversal.md, image_02) : Après ~1 an de baisse, Pfizer (PFE) a formé un Double Bottom Reversal et cassé la résistance avec une expansion de volume. Sommet ~50 $ (avril 1999) → 30 $ (déc. 1999, nouveau plus bas 52 sem.) ; rebond > 20 % vers ~37,50 $ avec volume étendu ; 2e creux à 30 $ (≈ 2 mois après le 1er) ; avance post-2e creux accélérée avec volume bien au-dessus de l'EMA 60 jours et CMF > +20 % en 6 jours ; cassure de 37,50 $ par un gap up et expansion de volume ; pullback vers 37,50 $ (résistance devenue support) offrant une entrée longue, puis avance rapide au-delà de 45 $.
**TRADEX-AI C2** : Exemple intégrant tous les critères (rebond, tolérance 2e creux, volume CMF/EMA, cassure sur gap, retest). Valeur illustrative — confirme la mécanique D1535→D1539.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1531 | Nature (retournement haussier) | 🟢 | C1 | configuration |
| D1532 | Distinction vs Double Bottom Breakdown P&F | 🟢 | C1 | configuration |
| D1533 | Downtrend préalable requis | 🟢 | C1 | structure_marche |
| D1534 | Premier creux | 🟢 | C1 | structure_marche |
| D1535 | Sommet (rebond 10-20 %, volume faible) | 🟢 | C2 | structure_marche |
| D1536 | Second creux (3 %, espacement 1-3 mois) | 🟢 | C1 | configuration |
| D1537 | Avance 2e creux (volume en accélération) | 🟢 | C2 | signal |
| D1538 | Cassure de résistance (validation) | 🟢 | C2 | signal |
| D1539 | Résistance devenue support (retest) | 🟢 | C1 | gestion_risque_entree |
| D1540 | Objectif de prix (mesure) | 🟢 | C1 | gestion_risque_entree |
| D1541 | Cadre temporel ≥ 4 sem. + CMF/OBV/A-D | 🟢 | C2 | configuration |
| D1542 | Exemple PFE | 🟢 | C2 | configuration |

**Liens Belkhayate :** le Double Bottom Reversal n'est PAS un pattern Belkhayate (⚫). Aucun lien direct revendiqué. Pertinence projet **modérée** : pattern de retournement haussier classique avec critères quantifiables (rebond 10-20 %, tolérance 3 %, cible par mesure, confirmation volume) transposables en détecteur de structure (C1/C2), en complément — non substitution — des règles d'entrée Belkhayate (Pivots/BGC/Direction/Énergie). Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D1533 / D1541 — cadre temporel (downtrend de plusieurs mois, ≥ 4 semaines entre creux) calibré sur graphiques journaliers actions : sur futures GC/HG/CL/ZW en Range Bars / 15 min / 15 s, l'échelle temporelle doit être ré-évaluée (le pattern « intermédiaire à long terme » peut perdre son sens en intraday rapide).
- D1536 / D1540 — la tolérance 3 % et la cible par mesure sont codables, mais à confronter au tick/volatilité de chaque actif (CL très volatil) avant usage.
- D1537 / D1538 — confirmation volume (accélération, CMF/OBV/A-D) à mapper sur les flux ATAS réels avant intégration.
- Cohérence projet : valider que ce pattern de retournement ne contredit pas la logique d'entrée Belkhayate déjà figée avant toute fusion.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
