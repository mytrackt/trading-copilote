# Extraction StockCharts — High-Low Percent

**Source :** `bundles/stockcharts/high_low_percent.md` (HTTP 200 · ~6 200 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D2071 → D2090 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-indicators/high-low-percent
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

⚫🔴 **PERTINENCE LIMITÉE FUTURES** : indicateur de BREADTH (largeur de marché) actions — il mesure le pourcentage de net new highs sur les composants d'un secteur/indice (sector SPDRs : XLK, XLE, XLU…). NON applicable directement à un future individuel (GC/HG/CL/ZW), qui n'a pas de « composants ». Pertinence indirecte uniquement via ES (S&P 500) comme actif de CONFIRMATION (C5 sentiment / C7 corrélations). Belkhayate NON CONCERNÉ.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | High-Low Percent - Chart 1 | Calculating the High-Low Percent | CERTIFIE (accord .md + HTML) |
| image_02.png | High-Low Percent - Chart 2 | High-Low Line | CERTIFIE (accord .md + HTML) |
| image_03.png | High-Low Percent - Chart 3 | High-Low Percent | CERTIFIE (accord .md + HTML) |
| image_04.png | High-Low Percent - Chart 4 | SharpCharts | CERTIFIE (accord .md + HTML) |
| image_05.png | High-Low Percent - Chart 5 | SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2071 — Définition du High-Low Percent (breadth)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « The High-Low Percent is a breadth indicator that measures the percentage of net new highs. After the market close, StockCharts.com calculates this indicator for the nine sector SPDRs and several indexes. »
**TRADEX-AI C5/C7** : indicateur de largeur de marché de net new highs. Pertinence limitée futures — exploitable seulement sur ES (proxy S&P 500) en CONFIRMATION, jamais sur GC/HG/CL/ZW directement.
*Catégorie : indicateurs_tendance*

---

### D2072 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : `High-Low Percent = (52-week Highs Less 52-week Lows) / Total Issues`. Exemples littéraux : (15 − 2) / 77 = +16,88 % ; (2 − 6) / 77 = −5,19 %.
**TRADEX-AI C5** : formule déterministe et reproductible. Note pertinence limitée futures : nécessite un panier de composants (Total Issues), inexistant pour un contrat future isolé.
*Catégorie : indicateurs_tendance*

---

### D2073 — Bornes et rareté des extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_01) : « High-Low Percent fluctuates between -100% and +100% with zero as the middle line. In reality, extreme readings, greater than +70% and less than -70%, are very rare and the actual range is much smaller. »
**TRADEX-AI C5** : oscillateur borné, ligne médiane zéro ; extrêmes ±70 % rares. Pertinence limitée futures — sert au mieux de contexte sentiment via ES.
*Catégorie : indicateurs_tendance*

---

### D2074 — Lecture du signe (plus de new highs vs new lows)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : Technology SPDR à 77 titres avec 15 new highs et 2 new lows → High-Low Percent positif (+16,88 %) car plus de new highs ; second exemple 2 highs / 6 lows → négatif (−5,19 %).
**TRADEX-AI C5** : signe = biais directionnel de participation. Note futures : nécessite des composants, donc ES uniquement.
*Catégorie : indicateurs_tendance*

---

### D2075 — Instabilité des données long terme (composition changeante)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « these calculations are based on the list of stocks in the underlying index or ETF (...) which do change. This means the breadth data from two years ago is based on the then-current holdings (...) chartists should consider this when using a long-term chart. »
**TRADEX-AI C7** : mise en garde sur la non-stationnarité de l'historique breadth — ne pas backtester un signal sur historique long sans précaution. Renforce le caractère indirect/contextuel.
*Catégorie : structure_marche*

---

### D2076 — Indicateur retardé définissant le trend moyen/long terme
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « As a breadth indicator, High-Low Percent is a lagging indicator that helps define the medium- to long-term trend. It takes 52 weeks to produce a new high or a new low. »
**TRADEX-AI C5** : garde-fou — indicateur retardé, à utiliser comme contexte de fond (régime moyen/long terme), pas comme signal d'entrée précoce.
*Catégorie : structure_marche*

---

### D2077 — Asymétrie expansion new highs / new lows
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « New highs expand after an extended move in the broader market (S&P 500) (...). New highs may dry up with the first decline (...), but a surge in new lows is unlikely after just a few weeks. It takes an extended decline or major support break to trigger an expansion of new lows. »
**TRADEX-AI C5** : nuance de lecture — l'assèchement des new highs précède la surge des new lows. Concept breadth actions, pertinence indirecte ES.
*Catégorie : structure_marche*

---

### D2078 — Définition de la High-Low Line (cumul)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « The High-Low Line is a cumulative measure of each period's High-Low Percent value. The High-Low Line rises when High-Low Percent is positive and falls when High-Low Percent is negative. »
**TRADEX-AI C7** : ligne de tendance cumulative pour repérer trend/retournements. Pertinence limitée futures — transposable uniquement à ES.
*Catégorie : indicateurs_tendance*

---

### D2079 — Échelle de droite non significative
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « The values on the right-hand scale are not important because these values depend on the starting date. Chartists should simply focus on the line's movements and general direction. » Possibilité d'appliquer une moyenne mobile ou d'autres indicateurs à la High-Low Line.
**TRADEX-AI C7** : se concentrer sur la direction de la ligne, pas sur les valeurs absolues. Note d'usage pour une ligne cumulative.
*Catégorie : structure_marche*

---

### D2080 — High-Low Line + EMA 20 (exemple XLE) et lag
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_02) : Chart 2 montre la XLE High-Low Line avec une EMA 20 jours et l'Energy SPDR (XLE) en fenêtre basse. « High-Low Percent is a lagging indicator that usually turns after the trend has turned. Some signals will be timely (...), but others will lag and produce whipsaws if a trend quickly reverses. »
**TRADEX-AI C5** : croisement ligne/EMA 20 = règle, mais retardée → whipsaws en cas de retournement rapide. Garde-fou explicite. Note futures : XLE = secteur énergie actions, NON le pétrole CL (future) ; ne pas confondre.
*Catégorie : signal*

---

### D2081 — Décryptage des signaux retardés (exemple XLE)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_02) : XLE remonte en juillet mais la High-Low Line ne tourne et ne casse son EMA 20 que le 1er août (retard) ; downturn de mi-novembre (lag), puis upturn de mi-décembre durant plus de six mois (bon trend capté).
**TRADEX-AI C5** : illustration concrète du décalage temporel entre prix et breadth. Confirme l'usage en contexte, pas en timing fin.
*Catégorie : structure_marche*

---

### D2082 — High-Low Percent en oscillateur autonome (exemple XLU)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_03) : Chart 3 — High-Low Percent du Utilities SPDR (XLU) fluctue entre −15 % et +72 %. « This range is large because utilities are a rather homogeneous group and XLU has less than 40 stocks. »
**TRADEX-AI C5** : l'amplitude dépend de l'homogénéité et du nombre de composants du groupe. Pertinence limitée futures — propriété spécifique aux paniers d'actions.
*Catégorie : indicateurs_tendance*

---

### D2083 — Croisements de zéro vs seuils ±5 %
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_03) : « Chartists can look for crosses above/below the zero line to establish their trading bias or use a bullish/bearish threshold. In this example, a move above 5% is deemed bullish, while a move below -5% is deemed bearish. These thresholds reduce the number of signals and whipsaws. »
**TRADEX-AI C5** : convention de filtrage par bande morte ±5 % autour de zéro pour réduire les faux signaux. Principe transposable comme garde-fou d'oscillateur.
*Catégorie : signal*

---

### D2084 — Signaux retardés persistants (rappel)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_03) : « Signals look great when a strong trend emerges, but there will also be late signals because of the lag. Keep this in mind when using High-Low Percent. »
**TRADEX-AI C5** : avertissement réitéré sur le retard — bons signaux en tendance forte, tardifs sinon. Garde-fou de prudence.
*Catégorie : structure_marche*

---

### D2085 — Path of least resistance (Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « In its simplest form, the path of least resistance is up when there are more new highs than new lows. The path is down when new lows outnumber new highs. Remember that High-Low Percent is a lagging indicator; changes (...) usually happen after the trend (...) has reversed. »
**TRADEX-AI C5/C7** : synthèse directionnelle — biais de moindre résistance via le signe de la breadth, en gardant le retard à l'esprit. Réservé à ES.
*Catégorie : signal*

---

### D2086 — Création d'une High-Low Line via type « cumulative »
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_04) : « Chartists can easily create a High-Low Line by using "cumulative" for chart type. A moving average can be added as an "overlay" and the underlying security (XLK) can be shown in a window above or below the main chart window. »
**TRADEX-AI C5** : note d'implémentation StockCharts (type cumulative + overlay MA). Non transposable tel quel à NT8/ATAS — valeur documentaire.
*Catégorie : configuration*

---

### D2087 — Affichage en histogramme (zéro + fluctuations)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md, image_05) : « High-Low Percent can be shown on its own as a "histogram" (...). This makes it easy to see the zero line and analyze the fluctuations. Chartists can add horizontal lines using the "overlays" section. »
**TRADEX-AI C5** : note de visualisation StockCharts (histogramme + lignes horizontales de seuil). Valeur documentaire uniquement.
*Catégorie : configuration*

---

### D2088 — Liste de symboles High-Low Percent
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : une liste à jour de symboles pour tous les indicateurs High-Low Percent est accessible via la recherche StockCharts ; l'icône « Mentions » donne les détails et mentions récentes.
**TRADEX-AI C5** : ressource d'accès aux symboles plateforme. Valeur documentaire ($SPXHLP pertinent pour ES).
*Catégorie : configuration*

---

### D2089 — Complémentarité avec l'analyse du sous-jacent
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « These indicators can then complement the analysis of the underlying security. For example, the High-Low Line based on High-Low Percent for the Technology SPDR (XLK) would complement the analysis of XLK. »
**TRADEX-AI C7** : la breadth complète (jamais ne remplace) l'analyse du sous-jacent. Cohérent avec la logique de confluence multi-cercles. Réservé à ES côté futures.
*Catégorie : structure_marche*

---

### D2090 — Jamais en stand-alone / outil de définition de trend
🟢 **FAIT VÉRIFIÉ** (Source : high_low_percent.md) : « High-Low Percent is a breadth indicator that chartists can use to define the path of least resistance or to identify trend changes. » Usage en complément d'autres outils (impliqué par la complémentarité D2089 et le caractère lagging).
**TRADEX-AI C5** : garde-fou de confluence — brique de contexte de trend, jamais signal isolé.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2071 | Définition High-Low Percent (breadth) | 🟢 | C5/C7 | indicateurs_tendance |
| D2072 | Formule de calcul | 🟢 | C5 | indicateurs_tendance |
| D2073 | Bornes ±100 %, extrêmes ±70 % rares | 🟢 | C5 | indicateurs_tendance |
| D2074 | Lecture du signe | 🟢 | C5 | indicateurs_tendance |
| D2075 | Instabilité données long terme | 🟢 | C7 | structure_marche |
| D2076 | Lagging → trend moyen/long terme | 🟢 | C5 | structure_marche |
| D2077 | Asymétrie new highs/new lows | 🟢 | C5 | structure_marche |
| D2078 | Définition High-Low Line (cumul) | 🟢 | C7 | indicateurs_tendance |
| D2079 | Échelle de droite non significative | 🟢 | C7 | structure_marche |
| D2080 | High-Low Line + EMA 20 (lag/whipsaws) | 🟢 | C5 | signal |
| D2081 | Signaux retardés (exemple XLE) | 🟢 | C5 | structure_marche |
| D2082 | Oscillateur autonome (XLU) | 🟢 | C5 | indicateurs_tendance |
| D2083 | Seuils ±5 % vs croisement zéro | 🟢 | C5 | signal |
| D2084 | Signaux retardés persistants | 🟢 | C5 | structure_marche |
| D2085 | Path of least resistance | 🟢 | C5/C7 | signal |
| D2086 | Création High-Low Line (cumulative) | 🟢 | C5 | configuration |
| D2087 | Affichage histogramme | 🟢 | C5 | configuration |
| D2088 | Liste de symboles | 🟢 | C5 | configuration |
| D2089 | Complémentarité sous-jacent | 🟢 | C7 | structure_marche |
| D2090 | Jamais en stand-alone | 🟢 | C5 | signal |

| Élément | Valeur |
|---------|--------|
| Décisions | D2071 → D2090 (20) |
| Images certifiées | 5/5 |
| Cercles | C5 (sentiment/participation) · C7 (corrélations/structure) |
| Catégories | indicateurs_tendance · signal · structure_marche · configuration |
| Actif applicable | ES uniquement (CONFIRMATION) — JAMAIS GC/HG/CL/ZW directement |
| Belkhayate | NON CONCERNÉ |
| Pertinence futures | LIMITÉE — breadth actions, transposable seulement à ES ($SPXHLP) en contexte macro/sentiment |
| Cas « à vérifier » | Aucun (5/5 images certifiées, tous faits littéraux 🟢) ; PIÈGE : XLE/XLU = SPDR sectoriels actions, NE PAS confondre XLE avec le future pétrole CL ; seuils ±5 %/±70 % = exemples actions, non transposables aux futures |

**Liens Belkhayate :** Aucun lien direct — le High-Low Percent n'est PAS un indicateur Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Indicateur de largeur de marché actions : valeur indirecte pour TRADEX-AI, jamais déclencheur d'ordre sur les actifs tradables.
