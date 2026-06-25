# Extraction StockCharts — Bob Farrell's 10 Rules
**Source :** `bundles/stockcharts/bob_farrells_10_rules.md` (HTTP 200 · ~12 525 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D871 → D883 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/bob-farrells-10-rules
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section (règle) | Statut |
|-------|-------|-----------------|--------|
| image_01.png | Rule 1: Markets tend to return to the mean over time. | Règle 1 | CERTIFIE (accord .md + HTML) |
| image_02.png | Rule 2: Excess moves... opposite direction. | Règle 2 | CERTIFIE (accord .md + HTML) |
| image_03.png | Rule 3: There are no new eras; excess moves are never permanent | Règle 3 | CERTIFIE (accord .md + HTML) |
| image_04.png | Rule 4: Rapid rising or falling markets... go further | Règle 4 | CERTIFIE (accord .md + HTML) |
| image_05.png | Bob Farrell's rule 6: Fear and greed... | Règle 6 | CERTIFIE (accord .md + HTML) |
| image_06.png | Bob Farrell's rule 7: Markets are strongest when broad... | Règle 7 | CERTIFIE (accord .md + HTML) |
| image_07.png | Bob Farrel's rule 8: bear markets have three stages... | Règle 8 | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D871 — Origine et autorité de Bob Farrell
🟢 **FAIT VÉRIFIÉ** (Source : bob_farrells_10_rules.md) : « Bob Farrell is a Wall Street veteran who draws on 50 years of experience... he launched his career as a technical analyst with Merrill Lynch in 1957... He became a pioneer in sentiment studies and market psychology. His 10 rules on investing stem from personal decades of experience. »
**TRADEX-AI C5** : Cadre heuristique de psychologie/sentiment de marché, source d'autorité reconnue ; alimente C5 (sentiment) et la grille comme garde-fous qualitatifs, jamais comme signal mécanique.
*Catégorie : structure_marche*
---

### D872 — Règle 1 : retour à la moyenne
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_01) : « Markets tend to return to the mean over time. Trends that get overextended in one direction or another return to their long-term average. » Illustré sur le S&P 500 avec une EMA 52 semaines et le PPO(1,52,1) revenant à zéro.
**TRADEX-AI C1** : Principe de réversion à la moyenne — cohérent avec l'approche pivots/BGC Belkhayate ; un éloignement extrême d'une MM longue est un contexte, pas un signal d'entrée.
*Catégorie : structure_marche*
---

### D873 — Règle 2 : excès symétriques (pendule)
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_02) : « Excess moves in one direction will lead to an excess move in the opposite direction... like a pendulum. » Illustré par la bulle Nasdaq 1999 (PPO 52,1,1 > +40 %) suivie de la chute 2000-2001 (PPO < -40 %).
**TRADEX-AI C5** : Excès haussier appelle excès baissier symétrique ; cadre de gestion du risque face aux mouvements paraboliques.
*Catégorie : structure_marche*
---

### D874 — Règle 3 : pas de « nouvelle ère »
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_03) : « There are no new eras—excesses are never permanent... 'This time it is different' is perhaps the most dangerous phrase in investing. » Cité Jesse Livermore : « there is nothing new in Wall Street. »
**TRADEX-AI C5** : Garde-fou anti-FOMO / anti-bulle ; signal de prudence sur les modes spéculatifs.
*Catégorie : structure_marche*
---

### D875 — Règle 4 : marchés exponentiels et correction abrupte
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_04) : « Exponential rapidly rising or falling markets usually go further than you think, but they do not correct by going sideways... the correction tends to be sharp. » Illustré par le Shanghai Composite ($SSEC) 2005-2007 (move parabolique, surachat répété sans top).
**TRADEX-AI C1** : Un surachat en tendance forte n'est pas un top ; la correction d'un mouvement parabolique est verticale, pas latérale — implication directe sur le placement des stops.
*Catégorie : indicateurs_tendance*
---

### D876 — Règle 5 : le public achète au sommet, vend au creux
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md) : « The public buys the most at the top and the least at the bottom... The survey from the American Association of Individual Investors is often cited as a barometer for investor sentiment... excessively bullish sentiment warns of a market top, while excessively bearish sentiment warns of a market bottom. »
**TRADEX-AI C5** : Lecture contrarian du sentiment retail (proxy AAII) ; complémentaire du VIX et Put/Call ratio en C5.
*Catégorie : structure_marche*
---

### D877 — Règle 6 : peur et avidité > résolution long terme
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_05) : « Fear and greed are stronger than long-term resolve... Plan your trade and trade your plan... When the emotions are running high, take a breather, step back, and analyze the situation from a greater distance. »
**TRADEX-AI C5** : Discipline émotionnelle ; justifie les garde-fous (suspension Auto après perte, rate limiting) du système.
*Catégorie : gestion_risque_entree*
---

### D878 — Règle 7 : force des marchés = largeur (breadth)
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_06) : « Markets are strongest when they are broad and weakest when they narrow to a handful of blue-chip names... Small- and mid-caps (troops) must also be on board to give the rally credibility. »
**TRADEX-AI C7** : La largeur de marché valide une tendance ; pour TRADEX-AI, transposable en confirmation inter-marché (ES large vs leadership étroit) en C7.
*Catégorie : structure_marche*
---

### D879 — Règle 8 : trois phases du bear market
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md, image_07) : « Bear markets have three stages—sharp down, reflexive rebound, and a drawn-out fundamental downtrend... Dow Theory suggests that bear markets consist of three down legs with reflexive rebounds in between. »
**TRADEX-AI C1** : Carte de la structure d'un marché baissier (chute brutale → rebond technique → déclin de fond) ; évite de confondre rebond réflexe et retournement.
*Catégorie : structure_marche*
---

### D880 — Règle 9 : consensus = signal contrarian
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md) : « When all the experts and forecasts agree – something else is going to happen... Excessive bullish sentiment from newsletter writers and analysts should be viewed as a warning sign... consider buying when stocks are unloved, and the news is all bad. »
**TRADEX-AI C5** : Indicateur contrarian sur le consensus analystes/médias ; alimente C5 et C6 (news) comme alerte, pas comme déclencheur.
*Catégorie : structure_marche*
---

### D881 — Règle 10 : bull markets plus « agréables »
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md) : « Bull markets are more fun than bear markets. Wall Street and Main Street are more in tune with bull markets than bear markets. »
**TRADEX-AI C5** : Biais d'attention/participation favorable aux hausses ; rappel d'équité de traitement haussier/baissier dans l'analyse.
*Catégorie : structure_marche*
---

### D882 — Statut des règles : heuristiques, pas absolues
🟡 **CONVENTION** (Source : bob_farrells_10_rules.md) : « Bob Farrell's 10 rules are not intended to be considered hard and fast or set in stone. There are exceptions to every rule. »
**TRADEX-AI C5** : Les 10 règles sont un cadre de jugement, jamais des critères éliminatoires de la grille /10 ; usage en pondération qualitative.
*Catégorie : gestion_risque_entree*
---

### D883 — Conscience émotionnelle aux extrêmes
🔵 **ÉCOLE** (Source : bob_farrells_10_rules.md) : « Being aware of sentiment can prevent traders from selling near the bottom and buying near the top... individual investors and traders... often feel most confident at the top of a market... most pessimistic or cautious at market bottoms. Awareness... is the first step towards conquering their adverse effects. »
**TRADEX-AI C5** : Synthèse psychologique transverse (confiance max au top / pessimisme max au creux) ; argument pour le mode Manuel (Abdelkrim décide) avec garde-fous anti-biais.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Plage | Décisions | Images | Tags dominants | Cercle |
|-------|-----------|--------|----------------|--------|
| D871→D883 | 13 | 7/7 certifiées | 🔵 ÉCOLE (10) · 🟡 (2) · 🟢 (1) | C5 (dominant) / C1 / C7 |

Corpus de sagesse de marché (psychologie + sentiment), majoritairement 🔵 ÉCOLE. Aucune formule ni seuil mécanique : ces 10 règles alimentent C5 (sentiment) et le jugement qualitatif de la grille, jamais comme critère éliminatoire ou déclencheur automatique. Règles à fort écho TRADEX-AI : R1 (réversion moyenne ↔ pivots/BGC), R4 (surachat ≠ top en tendance forte ↔ stops), R6/R10/synthèse (discipline émotionnelle ↔ mode Manuel + suspension Auto). Aucun lien Belkhayate explicite. Aucun cas ambigu, aucune image à vérifier.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
