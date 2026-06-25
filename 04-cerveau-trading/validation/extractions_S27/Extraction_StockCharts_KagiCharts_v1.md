# Extraction StockCharts — Kagi Charts

**Source :** `bundles/stockcharts/kagi_charts.md` (HTTP 200 · ~13 628 car.) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 10/10 certifiées
**Décisions :** D2371 → D2390 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/kagi-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | Green arrows = upside reversals, red arrows = downside reversals | Reversal Amount | CERTIFIÉ |
| image_02.png | Chart showing close-only prices (vs Kagi) | Reversal Amount | CERTIFIÉ |
| image_03.png | A close-only chart | Fixed Amount versus ATR | CERTIFIÉ |
| image_04.png | Kagi chart | Fixed Amount versus ATR | CERTIFIÉ |
| image_05.png | Yin (thin red) and yang (thick black) lines on a Kagi chart | Yin and Yang | CERTIFIÉ |
| image_06.png | Advancing/declining periods, waists mark support zone | Signals | CERTIFIÉ |
| image_07.png | Inverted three Buddha bottoms | Signals | CERTIFIÉ |
| image_08.png | Trendline and multi-level breaks | Signals | CERTIFIÉ |
| image_09.png | Kagi chart for QQQ | Kagi Charts In SharpCharts | CERTIFIÉ |
| image_10.png | SharpChart settings for Kagi charts | Kagi Charts In SharpCharts | CERTIFIÉ |

## DÉCISIONS

### D2371 — Nature des Kagi charts : prix pur, temps ignoré
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : « Kagi charts are based strictly on price action. They ignore time. » Ce sont des graphes en ligne qui changent de direction quand le prix bouge d'un montant requis, similaires aux Point & Figure.
**TRADEX-AI C1** : Type de graphe filtrant le bruit par seuil de mouvement prix ; non implémenté côté NT8 (NT8 fournit OHLC/range bars, pas de Kagi natif requis).
*Catégorie : structure_marche*

---

### D2372 — Origine historique (Steve Nison)
🔵 **ÉCOLE** (Source : kagi_charts.md) : Selon Steve Nison (auteur de *Beyond Candlesticks*), les Kagi ont été inventés à la fin du 19e siècle au Japon. La notion yin/yang s'ajoute via l'épaisseur des lignes lors des cassures de plus-haut/plus-bas.
**TRADEX-AI C1** : Contexte d'école japonaise (Nison) ; sert de cadre conceptuel, pas de règle exécutable.
*Catégorie : structure_marche*

---

### D2373 — Reversal Amount : paramètre fondateur
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : « The reversal amount is the minimum price change required for the Kagi line to reverse direction. » Il peut être un nombre de points fixe, un pourcentage, ou un ATR variable. Basé sur clôtures ou sur l'amplitude haut-bas.
**TRADEX-AI C1** : Notion de seuil de retournement paramétrable ; analogue conceptuel au seuil minimal de mouvement utilisable comme filtre de bruit.
*Catégorie : configuration*

---

### D2374 — Exemple chiffré du seuil (20 points S&P 500)
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Avec un reversal de 20 points : si la ligne Kagi monte et le S&P atteint 1951, elle ne se retourne pas tant que l'indice ne descend pas à 1931 ou moins (≥20 points). Inversement, en baisse à 1900, pas de retournement avant remontée à 1920 ou plus.
**TRADEX-AI C1** : Illustration du mécanisme de seuil symétrique ; non concerné par les actifs trading (exemple sur indice).
*Catégorie : configuration*

---

### D2375 — Axe des dates irrégulier (focus prix)
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_01, image_02) : La ligne Kagi ignore les changements de date et monte verticalement car basée uniquement sur le prix ; l'axe X (dates) est irrégulier. La date ne change qu'à un retournement. Un graphe ligne/barre a un axe X uniforme.
**TRADEX-AI C1** : Conséquence visuelle ; distinction prix-pur vs temps-uniforme, pertinente pour comprendre les transformations type Renko/range bars.
*Catégorie : structure_marche*

---

### D2376 — Montant fixe (points/pourcentage) = constant
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Avec points ou pourcentage, le reversal amount reste constant à mesure que de nouvelles données arrivent (montant fixe qui ne change pas).
**TRADEX-AI C1** : Mode de seuil stable, déterministe ; cohérent avec une grille déterministe.
*Catégorie : configuration*

---

### D2377 — Reversal basé ATR : variable et volatil
⏳ **VOLATILE** (Source : kagi_charts.md, image_03, image_04) : Avec l'ATR (mesure de volatilité, défaut 14 périodes), le reversal amount fluctue avec la volatilité du prix et change quand de nouvelles données arrivent ; l'apparence du Kagi change en conséquence.
**TRADEX-AI C1** : Seuil adaptatif à la volatilité (ATR-driven) ; pertinent pour adapter les filtres aux régimes GC/HG/CL/ZW.
*Catégorie : configuration*

---

### D2378 — ATR du Kagi ≠ ATR d'un graphe à axe uniforme
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_03, image_04) : Les valeurs ATR sur un graphe ligne/barre se basent sur les vraies périodes de trading (14 jours/semaines/mois). Donc les valeurs ATR sur un Kagi ne correspondent pas aux ATR d'un graphe à axe-date uniforme. L'ATR du close-only chart sert à fixer le reversal du Kagi.
**TRADEX-AI C1** : Avertissement de cohérence : ne pas confondre ATR Kagi et ATR temporel ; impact sur tout calcul ATR croisé.
*Catégorie : configuration*

---

### D2379 — Yin et Yang : épaisseur/couleur des lignes
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_05) : Lignes épaisses noires = yang ; lignes fines rouges = yin. Un pic/creux Kagi se forme à chaque retournement (petite ligne horizontale). Une ligne yang se forme quand le Kagi casse au-dessus du pic précédent ; une ligne yin quand il casse sous le creux précédent.
**TRADEX-AI C1** : Encodage visuel de la dominance haussière/baissière par cassure de structure.
*Catégorie : structure_marche*

---

### D2380 — Bascule yang↔yin au point de cassure
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_05) : Une ligne noire épaisse (yang) reste active jusqu'à une cassure sous le creux le plus récent, où elle devient fine rouge. La ligne rouge (yin) reste active jusqu'à une cassure au-dessus du pic le plus récent, où elle redevient noire épaisse.
**TRADEX-AI C1** : Règle de bascule d'état directionnel sur cassure de niveau ; logique d'état trend up/down.
*Catégorie : signal*

---

### D2381 — Signaux Nison : buy yang / sell yin et setups
🔵 **ÉCOLE** (Source : kagi_charts.md) : Dans *Beyond Candlesticks*, Nison liste : acheter sur nouvelle ligne yang, vendre sur nouvelle ligne yin, acheter rising shoulders, vendre falling waists, multi-level breaks, double windows, trend line breaks, tweezers, three Buddha reversals et record sessions.
**TRADEX-AI C1** : Catalogue de setups d'école Nison ; usage conceptuel, non transposé en règle automatique.
*Catégorie : signal*

---

### D2382 — Shoulders/Waists : vocabulaire et définition de tendance
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Un pic Kagi est aussi appelé « shoulder » (épaule), un creux « waist » (taille). Nison note qu'une série de rising shoulders définit une avance, une série de falling waists définit un déclin. Les 3 graphes suivants utilisent le pourcentage pour le reversal et l'amplitude haut-bas pour le champ prix.
**TRADEX-AI C1** : Définition opérationnelle de tendance par séquence de pics/creux (HH/HL vs LL/LH).
*Catégorie : structure_marche*

---

### D2383 — Trend lines et support via waists
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_06) : Le graphe CVS montre une avance oct.–nov. et un déclin en janvier ; des trend lines peuvent être tracées et les creux (waists) de mars–avril servent à marquer une zone de support.
**TRADEX-AI C1** : Méthode de support/résistance via troughs Kagi ; alimente la cartographie des niveaux.
*Catégorie : structure_marche*

---

### D2384 — Inverted three Buddha bottoms (≈ inverse H&S)
🔵 **ÉCOLE** (Source : kagi_charts.md, image_07) : Le motif « inverted three Buddha bottom » ressemble à un inverse head-and-shoulders : la waist gauche forme le premier creux, la tête de Buddha le creux médian (le plus bas), la waist droite le 3e creux. Une cassure au-dessus de la résistance confirme le retournement.
**TRADEX-AI C1** : Motif de retournement haussier à confirmation par cassure ; analogue à l'inverse H&S.
*Catégorie : configuration*

---

### D2385 — Levels : zones de support/résistance et seuil 2+ niveaux
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Pics (shoulders) et creux (waists) sont aussi appelés « levels ». Une série de shoulders marque une zone de résistance, une série de waists une zone de support. On peut chercher une cassure de deux niveaux ou plus pour déclencher un changement de tendance.
**TRADEX-AI C1** : Règle de confirmation multi-niveaux (≥2 levels cassés) ; critère de robustesse d'un signal de tendance.
*Catégorie : signal*

---

### D2386 — Exemple multi-level + trend line breaks (KLAC)
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md, image_08) : KLA-Tencor casse au-dessus de 3 niveaux et de la trend line d'octobre en février ; après avance au-dessus de 71, casse sous la trend line de début février et sous 3 niveaux début avril ; à droite, nouvelle cassure de trend line et passage au-dessus de 3 niveaux avec surge au-dessus de 64.
**TRADEX-AI C1** : Cas d'usage combinant cassures de niveaux et de lignes de tendance ; illustration de confluence.
*Catégorie : configuration*

---

### D2387 — Filtrage du bruit (famille Renko/Three Line Break)
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Comme Renko et Three Line Break, les Kagi filtrent le bruit en se concentrant sur les changements de prix minimaux ; comme les Point & Figure, ils facilitent le repérage des hauts/bas importants et des niveaux clés de support/résistance.
**TRADEX-AI C1** : Positionnement dans la famille des graphes prix-pur anti-bruit ; utile pour réduire les faux signaux.
*Catégorie : structure_marche*

---

### D2388 — Définition uptrend/downtrend et confirmation multi-outils
🟢 **FAIT VÉRIFIÉ** (Source : kagi_charts.md) : Avec ces infos, le chartiste définit des uptrends (HH + HL) ou downtrends (LL + LH). « As with all charting techniques, chartists should employ other technical analysis tools to confirm or refute their findings on Kagi charts. »
**TRADEX-AI C1** : Principe de confirmation croisée obligatoire ; cohérent avec la grille multi-cercles TRADEX.
*Catégorie : signal*

---

### D2389 — Réglages SharpCharts (Chart Type Kagi)
🟡 **CONVENTION** (Source : kagi_charts.md, image_09, image_10) : Dans Attributes des Chart Settings, sélectionner Kagi comme Chart Type. Choix points/pourcentage/ATR pour le reversal ; Price Field = close ou high-low range. High-low range = plus de sensibilité/reversals ; close = focus end-of-day. Couleurs yin/yang via Up/Down Color.
**TRADEX-AI C1** : Paramétrage outil propriétaire StockCharts ; informationnel, non porté dans NT8.
*Catégorie : configuration*

---

### D2390 — Référence livre (Beyond Candlesticks, Nison)
🔵 **ÉCOLE** (Source : kagi_charts.md) : *Beyond Candlesticks* de Steve Nison consacre un chapitre entier aux Kagi et couvre aussi Three Line Break, Renko, et l'usage japonais des moyennes mobiles.
**TRADEX-AI C1** : Source bibliographique d'école Nison ; traçabilité documentaire.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2371 → D2390 (20) |
| Images | 10/10 certifiées |
| Tags dominants | 🟢 littéral (14) · 🔵 ÉCOLE Nison (4) · 🟡 convention (1) · ⏳ volatile (1) |
| Cercle | C1 (structure de prix / type de graphe) |
| Belkhayate | NON CONCERNÉ (aucun lien Kagi ↔ méthode Belkhayate) |
| Actifs | Exemples sur indices/actions US ; aucun GC/HG/CL/ZW direct |
| Cas à vérifier | Aucun image à verifier. Conceptuel uniquement : Kagi non natif NT8 — décider si transformation prix-pur (reversal ATR) vaut une implémentation, ou si range bars suffisent. |

> ⚠️ Extraction BRUT, zone validation/, NON fusionnée. Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
