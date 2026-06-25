# Extraction StockCharts — High-Low Index

**Source :** `bundles/stockcharts/high_low_index.md` (HTTP 200 · ~6 600 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D2051 → D2070 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/high-low-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

⚫🔴 **PERTINENCE LIMITÉE FUTURES** : indicateur de BREADTH (largeur de marché) actions — il agrège les nouveaux plus-hauts / plus-bas 52 semaines des composants d'un indice (Nasdaq 100, S&P 100, NY Composite). NON applicable directement à un future individuel (GC/HG/CL/ZW), qui n'a pas de « composants ». Pertinence indirecte uniquement via ES (S&P 500) comme actif de CONFIRMATION (C5 sentiment / C7 corrélations). Belkhayate NON CONCERNÉ.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Spreadsheet 1 | Calculating the High-Low Index | CERTIFIE (accord .md + HTML) |
| image_02.png | High-Low Index - Chart 1 | Calculating the High-Low Index | CERTIFIE (accord .md + HTML) |
| image_03.png | High-Low Index - Chart 2 | Direction Identification | CERTIFIE (accord .md + HTML) |
| image_04.png | High-Low Index - Chart 3 | Bull-Bear Bias | CERTIFIE (accord .md + HTML) |
| image_05.png | High-Low Index - Chart 4 | SharpCharts | CERTIFIE (accord .md + HTML) |
| image_06.png | High-Low Index - SharpCharts | SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2051 — Définition du High-Low Index (breadth)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « The High-Low Index is a breadth indicator based on Record High Percent, which is based on new 52-week highs and new 52-week lows. (...) The High-Low Index is simply a 10-day SMA of the Record High Percent, which makes it a smoothed version of the Record High Percent. »
**TRADEX-AI C5/C7** : indicateur de largeur de marché lissé. Pertinence limitée futures — exploitable seulement sur ES (proxy S&P 500) en CONFIRMATION, jamais sur GC/HG/CL/ZW directement.
*Catégorie : indicateurs_tendance*

---

### D2052 — Formule Record High Percent
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_01) : `Record High Percent = {New Highs / (New Highs + New Lows)} x 100`. Fluctue entre 0 et 100. La table (Spreadsheet 1) illustre les possibilités sur un indice de 100 titres (Nasdaq 100, S&P 100).
**TRADEX-AI C5** : formule déterministe et reproductible. Note pertinence limitée futures : nécessite un panier de composants (New Highs + New Lows), inexistant pour un contrat future isolé.
*Catégorie : indicateurs_tendance*

---

### D2053 — Formule du High-Low Index (lissage 10 jours)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_01) : `High-Low Index = 10-day SMA of Record High Percent`. Le lissage SMA 10 jours réduit les oscillations brutales du Record High Percent.
**TRADEX-AI C5** : convention de paramétrage (SMA 10) servant à débruiter l'indicateur de breadth. Valeur documentaire — non transposable à un future isolé.
*Catégorie : indicateurs_tendance*

---

### D2054 — Lecture des bornes du Record High Percent
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « Readings below 50 indicate that there were more new lows than new highs. Readings above 50 indicate that there were more new highs than new lows. 0 indicates there were zero new highs (...) 100 indicates that there was at least 1 new high and no new lows (...) 50 indicates that new highs and new lows were equal. »
**TRADEX-AI C5** : ligne médiane 50 = équilibre haussiers/baissiers. Pertinence limitée futures — sert au mieux de contexte sentiment via ES.
*Catégorie : indicateurs_tendance*

---

### D2055 — Lissage illustré (Record High Percent vs High-Low Index)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_02) : Chart 1 montre le Record High Percent ($RHOEX, ligne noire) et le High-Low Index ($OEXHILO, ligne rouge). En mai-juin 2010, le Record High Percent rebondissait de 0 à 100 plusieurs fois, tandis que le High-Low Index tendait à la baisse en mai et à la hausse en juin.
**TRADEX-AI C5** : démonstration de l'intérêt du lissage pour dégager une tendance exploitable. Note futures : transposable conceptuellement à ES uniquement.
*Catégorie : structure_marche*

---

### D2056 — Interprétation force/faiblesse au seuil 50
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « a stock index is deemed strong (bullish) when the High-Low Index is above 50, which means new highs outnumber new lows. Conversely, a stock index is deemed weak (bearish) when the High-Low Index is below 50. »
**TRADEX-AI C5** : seuil 50 = biais directionnel. Pertinence limitée futures — jauge de conviction sur ES, pas déclencheur d'ordre sur actifs tradables.
*Catégorie : signal*

---

### D2057 — Seuils extrêmes 70 / 30 (tendances fortes)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « Readings consistently above 70 usually coincide with a strong uptrend. Readings consistently below 30 usually coincide with a strong downtrend. » L'indicateur peut atteindre ses extrémités et y rester en tendance forte.
**TRADEX-AI C5** : seuils littéraux 70/30 de confirmation de tendance forte. Applicable uniquement comme jauge sur ES.
*Catégorie : signal*

---

### D2058 — Identification de direction par SMA 20 jours
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_03) : Chart 2 montre le NYSE High-Low Index ($NYHILO) et sa SMA 20 jours. « The High-Low Index turns up when it moves above the 20-day SMA and turns down when it moves below the 20-day SMA. »
**TRADEX-AI C1/C5** : croisement indicateur/SMA = règle directionnelle déterministe. Note futures : applicable seulement sur breadth ES, pas sur prix d'un future.
*Catégorie : indicateurs_tendance*

---

### D2059 — Sens des croisements (expansion/contraction des new highs)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « New highs are increasing and/or new lows are decreasing when the High-Low Index rises. New highs are decreasing and/or new lows are increasing when the High-Low Index falls. »
**TRADEX-AI C5** : interprétation des mouvements en termes de participation interne du marché. Pertinence limitée futures (concept actions).
*Catégorie : structure_marche*

---

### D2060 — Filtrage des signaux par la tendance dominante
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_03) : « Because the bigger trend was down from October 2007 to March 2009, the bearish signals worked much better than the bullish signals. » Lignes pointillées vertes = High-Low Index au-dessus de sa SMA 20 (positif) ; rouges = en dessous (négatif).
**TRADEX-AI C1** : garde-fou — privilégier les signaux alignés avec la tendance majeure (cohérent avec « pas de contre-tendance » du projet).
*Catégorie : signal*

---

### D2061 — Bull-Bear Bias par le niveau absolu (midpoint 50)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « The absolute level of the High-Low Index can also be used to ascertain strength or weakness (...) Sometimes the High-Low Index can be rather volatile, but still remain consistently above or below its midpoint (50). (...) This level provides a clear bullish or bearish bias. »
**TRADEX-AI C5** : usage du niveau absolu (au-dessus/en-dessous de 50) comme biais durable plutôt que signal de croisement. Réservé à ES.
*Catégorie : signal*

---

### D2062 — Croisements SMA = whipsaws ; préférer le niveau global
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_04) : Chart 3 (Nasdaq) — l'indice croisait sa SMA 20 de nombreuses fois (juin-août 2007, nov. 2007-fév. 2008) ; « Playing these crossovers would have resulted in numerous whipsaws. Instead, chartists can look at the overall level. »
**TRADEX-AI C5** : garde-fou anti-whipsaw — privilégier le biais de niveau au croisement en marché agité. Principe de prudence général applicable au moteur.
*Catégorie : structure_marche*

---

### D2063 — Persistance des biais (exemples 3 mois / 7 mois)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_04) : « the High-Low Index moved below 50 at the end of May and remained below 50 until late August (3 months). Once moving above 50, the High-Low Index remained above 50 until early March (7 months). Not all signals will last this long, however. »
**TRADEX-AI C5** : illustration de la durabilité variable des biais ; avertissement explicite que les durées passées ne se reproduisent pas. Pertinence limitée futures.
*Catégorie : structure_marche*

---

### D2064 — Usage du biais pour filtrer les autres signaux
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « Chartists can focus on bullish signals when the High-Low Index is above 50 and ignore bearish signals. Oversold readings, resistance breakouts or bullish moving average crosses can be used in a bullish environment. » Symétrique pour < 50.
**TRADEX-AI C5/C7** : le biais breadth sert de filtre de contexte (active/désactive les signaux des autres outils). Transposable à ES comme garde-fou de régime.
*Catégorie : configuration*

---

### D2065 — Indicateur retardé (lagging) : 52 semaines requises
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « New 52-week highs and new 52-week lows are considered lagging indicators. (...) the market will change direction before there is a significant shift in the number of new 52-week highs or (...) lows. (...) It takes at least 52 weeks to forge a new high or a new low. »
**TRADEX-AI C5** : garde-fou — indicateur retardé, à ne pas utiliser comme signal d'entrée précoce. Vaut comme contexte de fond.
*Catégorie : structure_marche*

---

### D2066 — Asymétrie d'apparition new highs / new lows
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « New highs dry up when a stock index corrects after an extended advance. Some new lows will surface during a correction, but it takes an extended decline to generate a serious increase in new lows. » Symétrique pour les new highs lors d'un rebond après baisse étendue.
**TRADEX-AI C5** : nuance de lecture — l'assèchement des new highs précède la surge des new lows. Concept breadth actions, pertinence indirecte ES.
*Catégorie : structure_marche*

---

### D2067 — Spécificité à l'indice sous-jacent
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « the High-Low Index is a breadth indicator specific to an underlying index. The Nasdaq 100 High-Low Index applies to stocks in the Nasdaq 100, the NYSE High-Low Index applies to stocks in the NY Composite and so on. »
**TRADEX-AI C7** : chaque High-Low Index ne vaut que pour son indice. Renforce la non-applicabilité aux futures isolés — au mieux $SPXHILO comme proxy pour ES.
*Catégorie : structure_marche*

---

### D2068 — Jamais en stand-alone
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md) : « Like all indicators, the High-Low Index is not meant to be used as a stand-alone indicator. It should be used in conjunction with other aspects of technical analysis. »
**TRADEX-AI C5** : garde-fou de confluence — brique de contexte, jamais signal isolé. Cohérent avec la logique de score multi-cercles du projet.
*Catégorie : signal*

---

### D2069 — Disponibilité SharpCharts (8 indices) et tracé
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_05) : « SharpCharts users can plot the High-Low Index for eight indices, including the S&P 500, TSX Composite and Dow. » Tracé possible en fenêtre indicateur, fenêtre principale, ou derrière le prix ; ajout d'une moyenne mobile via Advanced Options / Overlay.
**TRADEX-AI C5** : note d'implémentation propre à StockCharts ($SPX disponible = pertinent pour ES). Non transposable tel quel à NT8/ATAS — valeur documentaire.
*Catégorie : configuration*

---

### D2070 — Procédure de plotting et liste de symboles
🟢 **FAIT VÉRIFIÉ** (Source : high_low_index.md, image_06) : procédure littérale — saisir le symbole de l'indice, aller dans « Indicators » → « Price », entrer le symbole du Record High Percent en « Parameters », choisir « Above/Below/Behind » pour la position. Une liste à jour de symboles High-Low Index est accessible via la recherche StockCharts.
**TRADEX-AI C5** : détail opérationnel plateforme StockCharts. Valeur documentaire uniquement.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2051 | Définition High-Low Index (breadth) | 🟢 | C5/C7 | indicateurs_tendance |
| D2052 | Formule Record High Percent | 🟢 | C5 | indicateurs_tendance |
| D2053 | Formule High-Low Index (SMA 10) | 🟢 | C5 | indicateurs_tendance |
| D2054 | Bornes Record High Percent | 🟢 | C5 | indicateurs_tendance |
| D2055 | Lissage illustré (Chart 1) | 🟢 | C5 | structure_marche |
| D2056 | Force/faiblesse au seuil 50 | 🟢 | C5 | signal |
| D2057 | Seuils extrêmes 70/30 | 🟢 | C5 | signal |
| D2058 | Direction par SMA 20 jours | 🟢 | C1/C5 | indicateurs_tendance |
| D2059 | Sens des croisements | 🟢 | C5 | structure_marche |
| D2060 | Filtrage par tendance dominante | 🟢 | C1 | signal |
| D2061 | Bull-Bear Bias (niveau absolu) | 🟢 | C5 | signal |
| D2062 | Croisements = whipsaws | 🟢 | C5 | structure_marche |
| D2063 | Persistance des biais (3/7 mois) | 🟢 | C5 | structure_marche |
| D2064 | Biais filtre les autres signaux | 🟢 | C5/C7 | configuration |
| D2065 | Indicateur retardé (52 sem.) | 🟢 | C5 | structure_marche |
| D2066 | Asymétrie new highs/new lows | 🟢 | C5 | structure_marche |
| D2067 | Spécificité à l'indice sous-jacent | 🟢 | C7 | structure_marche |
| D2068 | Jamais en stand-alone | 🟢 | C5 | signal |
| D2069 | SharpCharts 8 indices + tracé | 🟢 | C5 | configuration |
| D2070 | Procédure plotting + symboles | 🟢 | C5 | configuration |

| Élément | Valeur |
|---------|--------|
| Décisions | D2051 → D2070 (20) |
| Images certifiées | 6/6 |
| Cercles | C5 (sentiment/participation) · C7 (corrélations/structure) · C1 (tendance, marginal) |
| Catégories | indicateurs_tendance · signal · structure_marche · configuration |
| Actif applicable | ES uniquement (CONFIRMATION) — JAMAIS GC/HG/CL/ZW directement |
| Belkhayate | NON CONCERNÉ |
| Pertinence futures | LIMITÉE — breadth actions, transposable seulement à ES ($SPXHILO) en contexte macro/sentiment |
| Cas « à vérifier » | Aucun (6/6 images certifiées, tous faits littéraux 🟢) ; seuils 50/70/30 et SMA 10/20 = exemples actions, à NE PAS coder tels quels pour les futures |

**Liens Belkhayate :** Aucun lien direct — le High-Low Index n'est PAS un indicateur Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Indicateur de largeur de marché actions : valeur indirecte pour TRADEX-AI, jamais déclencheur d'ordre sur les actifs tradables.
