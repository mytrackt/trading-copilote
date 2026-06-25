# Extraction StockCharts — P&F Bull & Bear Traps
**Source :** `bundles/stockcharts/p_and_f_bull_and_bear_traps.md` (HTTP 200 · ~8 839 car.) + 4 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D2831 → D2850 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/classic-patterns/p-and-f-bull-and-bear-traps
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | An example of a P&F Bull Trap. | Bull Trap | CERTIFIE (accord .md + HTML) |
| image_02.png | Example of a P&F Bear Trap. | Bear Trap | CERTIFIE (accord .md + HTML) |
| image_03.png | After a Triple Top Breakout, the stock declined back into a congestion zone before the Bullish Catapult. | Bullish Catapults | CERTIFIE (accord .md + HTML) |
| image_04.png | A combination of a Triple Bottom Breakout and Double Bottom Breakout forged a Bearish Catapult. | Bearish Catapults | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2831 — Nature des Bull & Bear Traps : signaux P&F qui se retournent vite
🔵 **ÉCOLE (P&F classique)** (Source : p_and_f_bull_and_bear_traps.md) : Les Bull et Bear Traps sont des signaux P&F qui se retournent rapidement. Un Bull Trap est un Multiple Top Breakout qui se retourne après avoir dépassé les highs antérieurs d'UNE box. Un Bear Trap est un Multiple Bottom Breakdown qui se retourne après avoir dépassé les lows antérieurs d'UNE box. Ils donnent une indication rapide d'un échec de signal, mais attention à ne pas se faire piéger par un catapult.
**TRADEX-AI C1** : Famille de patterns d'ÉCHEC de breakout/breakdown (one-box) ; signal d'alerte précoce de retournement. Base d'un détecteur de faux signaux P&F.
*Catégorie : structure_marche*

---

### D2832 — Bull Trap : composition (Multiple Top Breakout one-box qui échoue)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_01) : Un Multiple Top Breakout inclut Triple Top Breakout, Quadruple Top Breakout et plus large. Triple Top Breakout : deux X-Columns successives forment des highs égaux et la X-Column suivante casse au-dessus. Quadruple : trois X-Columns successives forment des highs égaux. Pour qu'un Bull Trap soit possible, ce breakout ne peut être QUE d'une box ; les breakouts de deux boxes ou plus au-dessus de la résistance ne qualifient PAS.
**TRADEX-AI C1** : Critère de détection précis — un Bull Trap exige un breakout d'EXACTEMENT une box. Un breakout ≥2 boxes est « franc » et ne piège pas. Condition codable.
*Catégorie : structure_marche*

---

### D2833 — Bull Trap : déclenchement (reversal ≥ 3 boxes après breakout 1-box)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_01) : Le Bull Trap se produit quand les prix se retournent après un breakout d'une box, et que la O-Column subséquente descend d'AU MOINS TROIS boxes. Un breakout d'une box n'est pas fort, et le retournement immédiat montre une pression vendeuse renouvelée.
**TRADEX-AI C1** : Condition de confirmation — reversal de ≥3 boxes (le 3-box reversal standard P&F) invalide le breakout one-box. Signal de sortie/retournement codable.
*Catégorie : signal*

---

### D2834 — Bull Trap : exemple avril 2010 (Triple Top → Double Bottom Breakdown)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_01) : Exemple de Bull Trap en avril 2010. D'abord, le titre forge un Triple Top Breakout (la 3e X-Column dépasse les deux précédentes d'une box). Ensuite, ce breakout échoue vite : le titre forme un 3-box reversal ; cette O-Column casse sous la O-Column précédente, forgeant un Double Bottom Breakdown qui négocie/annule pleinement le Triple Top Breakout.
**TRADEX-AI C1** : Cas concret — le Bull Trap se confirme quand le retournement produit un Double Bottom Breakdown (signal baissier opposé) qui annule le breakout. Critère d'invalidation complète.
*Catégorie : structure_marche*

---

### D2835 — Bear Trap : composition (Multiple Bottom Breakdown one-box qui échoue)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_02) : Un Multiple Bottom Breakdown inclut Triple Bottom Breakdown, Quadruple Bottom Breakdown et plus large. Triple Bottom Breakdown : deux O-Columns successives forment des lows égaux et la O-Column suivante casse en dessous. Quadruple : trois O-Columns successives forment des lows égaux. Pour qu'un Bear Trap soit possible, ce breakdown ne peut être QUE d'une box ; les breakdowns de deux boxes ou plus sous le support ne qualifient PAS.
**TRADEX-AI C1** : Symétrique du Bull Trap (D2832) — Bear Trap exige un breakdown d'EXACTEMENT une box. Condition codable (miroir baissier).
*Catégorie : structure_marche*

---

### D2836 — Bear Trap : déclenchement (rebond ≥ 3 boxes après breakdown 1-box)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_02) : Le Bear Trap se produit quand les prix se retournent après un breakdown d'une box, et que la X-Column subséquente monte d'AU MOINS TROIS boxes. Un breakdown d'une box est vulnérable au whipsaw, et le retournement immédiat montre une pression acheteuse renouvelée.
**TRADEX-AI C1** : Symétrique de D2833 — rebond de ≥3 boxes invalide le breakdown one-box. Signal de retournement haussier codable.
*Catégorie : signal*

---

### D2837 — Bear Trap : exemple août 2010 (Quadruple Bottom → Double Top Breakout)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_02) : Exemple d'un Quadruple Bottom Breakdown en août 2010 : SNA casse le support avec seulement une box (un O sous les trois lows précédents). Ce breakdown ne dure pas : le titre se retourne vite, forge un 3-box reversal ; la X-Column montante s'étend pour forger un Double Top Breakout qui annule pleinement le Quadruple Bottom Breakdown.
**TRADEX-AI C1** : Cas concret — le Bear Trap se confirme quand le rebond produit un Double Top Breakout (signal haussier opposé) annulant le breakdown. Critère d'invalidation complète (miroir D2834).
*Catégorie : structure_marche*

---

### D2838 — Bullish Catapult : Triple Top Breakout → pullback → Double Top Breakout
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_03) : Les Bull/Bear Traps peuvent échouer et évoluer en catapults (similaire à un double trap). Un Bullish Catapult se forme avec un Triple Top Breakout, un pullback DANS le pattern, puis un Double Top Breakout. Un Triple Top Breakout one-box + pullback dans le pattern qualifie comme Bull Trap. Attention : le Triple Top est une zone de congestion = zone de support. Le pullback montre l'hésitation des bulls, mais il faut un Double Bottom Breakdown pour produire un signal baissier annulant pleinement le Triple Top Breakout original.
**TRADEX-AI C1** : Un Bull Trap apparent peut se muer en continuation haussière (catapult) ; ne PAS shorter sur le seul pullback tant qu'aucun Double Bottom Breakdown n'a confirmé. Garde-fou anti-piège-du-piège.
*Catégorie : structure_marche*

---

### D2839 — Bullish Catapult : exemple octobre 2010 (zone de congestion tenue)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_03) : Exemple : Multiple Top Breakout en octobre 2010, la X-Column de breakout dépasse les quatre highs précédents d'une box. Le breakout ne dure pas : le titre se retourne, déclinant dans la zone de congestion (green box). Les lows de cette zone tiennent finalement, et le titre forge un Double Top Breakout au rebond suivant. Le Bull Trap a échoué et évolué en Bullish Catapult.
**TRADEX-AI C1** : Cas concret — la tenue des lows de la zone de congestion (support) distingue un Bull Trap échoué (→catapult haussier) d'un vrai retournement baissier. Niveau-clé = lows de la congestion.
*Catégorie : structure_marche*

---

### D2840 — Bearish Catapult : Triple Bottom Breakdown → bounce → Double Bottom Breakdown
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_04) : Symétrique : les Bear Traps peuvent évoluer en Bearish Catapults. Formation : Triple Bottom Breakdown, un rebond DANS le pattern, puis Double Bottom Breakdown. Techniquement, un Triple Bottom Breakdown one-box + rebond dans le pattern qualifie comme Bear Trap. Attention : le Triple Bottom est une zone de congestion = zone de RÉSISTANCE. Le rebond montre de la résilience, mais il faut un Double Top Breakout pour produire un signal haussier annulant le Triple Bottom Breakdown original.
**TRADEX-AI C1** : Symétrique de D2838 — un Bear Trap apparent peut se muer en continuation baissière (catapult). Ne PAS acheter sur le seul rebond tant qu'aucun Double Top Breakout n'a confirmé.
*Catégorie : structure_marche*

---

### D2841 — Bearish Catapult : exemple (Triple Bottom → Bear Trap → cassure du low)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_04) : Exemple : Triple Bottom Breakdown, cassure de support avec juste une box (un O sous les deux O-Columns précédentes). Le breakdown ne dure pas : le titre se retourne à la hausse pour forger un Bear Trap. Mais le Bear Trap ne dure pas non plus : le titre repart à la baisse et casse sous son low précédent. La combinaison Triple Bottom Breakdown + Double Bottom Breakdown forge un Bearish Catapult.
**TRADEX-AI C1** : Cas concret — une double cassure baissière (Triple Bottom puis Double Bottom Breakdown) signe un Bearish Catapult ; le Bear Trap n'était qu'une étape intermédiaire.
*Catégorie : structure_marche*

---

### D2842 — Takeaway : les traps sont un early warning d'échec de signal
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md) : Les Bull et Bear Traps sont un système d'alerte précoce pour un signal qui échoue. Cependant, les traps ne sont PAS des signaux parfaits et peuvent au contraire évoluer en catapults.
**TRADEX-AI C1** : Garde-fou — un trap est un AVERTISSEMENT, pas une certitude de retournement ; ne pas inverser la position sur le seul trap (risque de catapult).
*Catégorie : signal*

---

### D2843 — Lecture d'un Bull Trap : taille de la congestion + support
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_03) : Pour un Bull Trap, regarder la TAILLE de la zone de congestion et identifier le support. Un pullback qui TIENT au-dessus du support pourrait n'être qu'un pullback (et non un retournement).
**TRADEX-AI C1** : Feature décisionnelle — comparer la profondeur du pullback au support de congestion ; tenue du support → continuation probable (catapult), cassure → trap confirmé.
*Catégorie : structure_marche*

---

### D2844 — Lecture d'un Bear Trap : résistance de congestion
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_04) : Pour un Bear Trap, identifier la RÉSISTANCE de la zone de congestion. Un rebond dans cette zone de résistance pourrait simplement être un rebond de survente (oversold bounce).
**TRADEX-AI C1** : Symétrique de D2843 — comparer le rebond à la résistance de congestion ; échec sous résistance → continuation baissière (catapult), franchissement → trap confirmé.
*Catégorie : structure_marche*

---

### D2845 — Règle : confirmer les signaux avec d'autres aspects de l'AT
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md) : Les chartistes doivent employer d'autres aspects de l'analyse technique pour confirmer les signaux sur les charts P&F.
**TRADEX-AI C1** : Règle architecturale — traps/catapults = couche structure (C1), jamais standalone ; exiger confluence (volume, momentum, niveaux Belkhayate).
*Catégorie : signal*

---

### D2846 — Le 3-box reversal comme seuil universel des traps
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_01, image_02) : Dans les deux traps, le retournement déclencheur est un 3-box reversal (≥ 3 boxes dans le sens opposé) après un breakout/breakdown d'exactement une box. Ce seuil de 3 boxes est le critère commun aux Bull et Bear Traps.
**TRADEX-AI C1** : Paramètre commun (3-box reversal) = constante de détection des traps ; à régler de pair avec la taille de box et le reversal amount P&F.
*Catégorie : signal*

---

### D2847 — One-box breakout/breakdown = signal faible par construction
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md) : La page insiste : un breakout d'une box n'est « pas si fort » et un breakdown d'une box est « vulnérable au whipsaw ». La faiblesse intrinsèque du dépassement one-box est la cause racine des traps.
**TRADEX-AI C1** : Règle de qualité — pondérer faiblement tout breakout/breakdown one-box ; privilégier les cassures ≥2 boxes (qui ne qualifient pas comme trap, cf. D2832/D2835).
*Catégorie : signal*

---

### D2848 — Trap = renversement opposé ; catapult = continuation initiale
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_03, image_04) : Différence structurelle issue de la page : un trap aboutit au signal OPPOSÉ (Bull Trap → Double Bottom Breakdown ; Bear Trap → Double Top Breakout), tandis qu'un catapult prolonge la direction INITIALE (Bullish Catapult → nouveau Double Top Breakout haussier ; Bearish Catapult → nouveau Double Bottom Breakdown baissier).
**TRADEX-AI C1** : Arbre de décision — surveiller quel signal confirme (opposé = trap, même sens = catapult) pour trancher entre retournement et continuation.
*Catégorie : structure_marche*

---

### D2849 — Further Study : Thomas Dorsey, *Point & Figure Charting*
🟡 **CONVENTION** (Source : p_and_f_bull_and_bear_traps.md) : Pour approfondir, la page renvoie à *Point & Figure Charting* de Thomas Dorsey, qui examine les idées de base et patterns clés du P&F, consacre un chapitre à la force relative (relative strength), relie ces concepts aux indicateurs de marché et outils de rotation sectorielle, et inclut des leçons sur l'usage du P&F avec les ETF.
**TRADEX-AI C1** : Référence bibliographique ; aucune règle codable, traçabilité documentaire.
*Catégorie : structure_marche*

---

### D2850 — Synthèse : zone de congestion = pivot support (haussier) / résistance (baissier)
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_bull_and_bear_traps.md, image_03, image_04) : Élément récurrent : la zone de congestion (Triple Top / Triple Bottom) agit comme support dans un contexte haussier et comme résistance dans un contexte baissier. C'est la tenue ou la cassure de cette zone qui distingue un trap (échec définitif) d'un catapult (reprise de la tendance).
**TRADEX-AI C1** : Niveau-clé décisionnel — la zone de congestion est le pivot dont dépend l'issue (trap vs catapult). À matérialiser comme niveau S/R dynamique dans le moteur.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2831 | Nature des Bull/Bear Traps | 🔵 ÉCOLE | C1 | structure_marche |
| D2832 | Bull Trap : composition (1-box) | 🟢 | C1 | structure_marche |
| D2833 | Bull Trap : reversal ≥3 boxes | 🟢 | C1 | signal |
| D2834 | Bull Trap : exemple avril 2010 | 🟢 | C1 | structure_marche |
| D2835 | Bear Trap : composition (1-box) | 🟢 | C1 | structure_marche |
| D2836 | Bear Trap : rebond ≥3 boxes | 🟢 | C1 | signal |
| D2837 | Bear Trap : exemple août 2010 | 🟢 | C1 | structure_marche |
| D2838 | Bullish Catapult (déf.) | 🟢 | C1 | structure_marche |
| D2839 | Bullish Catapult : exemple | 🟢 | C1 | structure_marche |
| D2840 | Bearish Catapult (déf.) | 🟢 | C1 | structure_marche |
| D2841 | Bearish Catapult : exemple | 🟢 | C1 | structure_marche |
| D2842 | Traps = early warning faillible | 🟢 | C1 | signal |
| D2843 | Lecture Bull Trap (support) | 🟢 | C1 | structure_marche |
| D2844 | Lecture Bear Trap (résistance) | 🟢 | C1 | structure_marche |
| D2845 | Confirmer avec d'autres outils | 🟢 | C1 | signal |
| D2846 | 3-box reversal = seuil universel | 🟢 | C1 | signal |
| D2847 | One-box = signal faible | 🟢 | C1 | signal |
| D2848 | Trap (opposé) vs catapult (continuation) | 🟢 | C1 | structure_marche |
| D2849 | Further Study (Dorsey) | 🟡 CONVENTION | C1 | structure_marche |
| D2850 | Congestion = pivot S/R décisionnel | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** les Bull/Bear Traps et catapults Point & Figure ne sont PAS des outils Belkhayate (⚫). La méthode Belkhayate repose sur Pivots + BGC + Direction + Énergie (MFI), pas sur le P&F. Aucun lien direct revendiqué. Rapprochement très indirect (non affirmé) : la zone de congestion P&F agissant comme support/résistance (D2843/D2844/D2850) recoupe conceptuellement l'usage des Pivots Belkhayate comme niveaux clés, mais la mécanique P&F (colonnes O/X, box, one-box breakout, 3-box reversal) est étrangère à Belkhayate. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D2832 / D2835 / D2846 — la détection des traps dépend entièrement de la taille de box et du seuil 3-box reversal : à calibrer sur futures GC/HG/CL/ZW avant tout codage (un mauvais paramétrage transforme un breakout franc en faux trap).
- D2838 / D2840 / D2848 — risque de « piège du piège » (catapult) : ne JAMAIS inverser une position sur le seul trap ; attendre le signal opposé confirmant (Double Bottom/Top Breakout) avant action.
- D2842 / D2845 / D2847 — les traps sont des signaux faibles (one-box) et faillibles : exiger une confluence externe (volume, momentum, niveaux Belkhayate) ; jamais standalone.
- Tous — patterns illustrés sur actions US (échelle journalière) ; transposition aux séances futures (roll, gaps de séance) non garantie.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
