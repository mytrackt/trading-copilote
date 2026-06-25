# Extraction StockCharts — DecisionPoint Price Momentum Oscillator (PMO)
**Source :** `bundles/stockcharts/decisionpoint_price_momentum_oscillator_pmo.md` (HTTP 200 · ~9 100 car.) + 16 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 16/16 certifiées
**Décisions :** D1451 → D1470 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/decisionpoint-price-momentum-oscillator-pmo
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Calculating the PMO | Calculating the PMO [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Calculating the PMO | Calculating the PMO [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Interpretation | Interpretation [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Interpretation | Interpretation [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | Interpretation | Interpretation [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Overbought/Oversold Indicator | Overbought/Oversold Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | Overbought/Oversold Indicator | Overbought/Oversold Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | Overbought/Oversold Indicator | Overbought/Oversold Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | Momentum Indicator | Momentum Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_10.png | Momentum Indicator | Momentum Indicator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_11.png | Signal Generator | Signal Generator [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_12.png | Sideways Wiggle | Sideways Wiggle [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_13.png | Bear Kiss | Bear Kiss [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_14.png | Bull Kiss | Bull Kiss [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_15.png | Clean Signals | Clean Signals [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_16.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1451 — Nature et origine du PMO
🔵 **ÉCOLE (Swenlin)** (Source : decisionpoint_price_momentum_oscillator_pmo.md) : Développé par Carl Swenlin, le DecisionPoint Price Momentum Oscillator (PMO) est un oscillateur basé sur un calcul de Rate of Change (ROC) lissé deux fois par des moyennes mobiles exponentielles utilisant un processus de lissage personnalisé. Comme le PMO est normalisé, il peut aussi servir d'outil de force relative — les titres peuvent être classés par leur valeur PMO comme expression de force relative.
**TRADEX-AI C3** : Oscillateur de momentum normalisé candidat ; double usage (momentum + force relative inter-actifs) potentiellement utile pour ranker GC/HG/CL/ZW entre eux. À traiter comme couche analytique, jamais déclencheur d'ordre.
*Catégorie : indicateurs_momentum*

---

### D1452 — Formules de calcul du PMO
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_01) : Le PMO dérive d'un ROC à 1 période lissé par deux fonctions de lissage personnalisées, très proches d'EMA mais utilisant la période seule (et non période+1) pour le multiplicateur.
`Smoothing Multiplier = (2 / Time period)`
`Custom Smoothing = {Close - Smoothing(veille)} × Multiplier + Smoothing(veille)`
`PMO Line = lissage custom 20-périodes de (10 × lissage custom 35-périodes de (((Prix du jour / Prix de la veille) × 100) - 100))`
`PMO Signal Line = EMA 10-périodes de la PMO Line`
**TRADEX-AI C3** : Formule déterministe complète, implémentable telle quelle ; paramètres par défaut 35/20/10. Le double lissage = filtre anti-bruit fort.
*Catégorie : indicateurs_momentum*

---

### D1453 — Normalisation et usage en force relative
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_03) : Le PMO oscille autour d'une ligne zéro. Sa direction indique si la force augmente ou diminue ; la pente démontre la puissance du mouvement. Comme c'est un calcul de ratio interne (vs externe comme la force relative standard qui divise deux prix), il retourne un résultat normalisé comparable au PMO de tout autre titre/indice. Les chartistes peuvent classer une liste de titres/indices par force relative via leurs valeurs PMO ; la liste n'a pas besoin d'être homogène (indices, actions, fonds dans la même liste).
**TRADEX-AI C3** : Propriété clé de comparabilité inter-actifs ; permet un classement de force relative GC vs HG vs CL vs ZW sur la même échelle normalisée.
*Catégorie : indicateurs_momentum*

---

### D1454 — Différence PMO vs MACD
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_04) : Un indicateur très similaire au PMO est le MACD (Gerald Appel). La différence principale est la valeur absolue : le MACD repose sur des moyennes mobiles — la lecture MACD d'un titre n'a aucun rapport avec celle d'un autre — alors que le PMO est un ratio interne. Sur graphiques long-terme, l'avantage du PMO est évident car il reste assez constant, contrairement au MACD (voir hebdo/mensuel).
**TRADEX-AI C3** : Argument de choix d'indicateur ; le PMO est préférable au MACD pour comparer des actifs et pour la stabilité long-terme. Aide à arbitrer la couche momentum.
*Catégorie : indicateurs_momentum*

---

### D1455 — Indicateur de surachat/survente et plage normale
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_06) : Le PMO aide à déterminer si un indice est suracheté ou survendu. Sur le S&P 500, la plage PMO normale va d'environ +2,5 (surachat) à -2,5 (survente) ; quand le PMO approche ou franchit ces limites, cela signale souvent un retournement de prix. Quand le PMO change de direction au niveau ou au-delà des extrêmes de sa plage normale, c'est une indication assez fiable qu'un changement de direction de prix à moyen terme se produit.
**TRADEX-AI C3** : Logique surachat/survente exploitable, MAIS bornes +2,5/-2,5 spécifiques au S&P 500 — à recalibrer par actif (voir D1456).
*Catégorie : indicateurs_momentum*

---

### D1456 — Plage « signature » propre à chaque actif
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_07) : Si +2,5/-2,5 est la plage usuelle des indices actions larges, chaque indice de prix a sa propre plage « signature ». Exemple : Microsoft (MSFT) montre une plage de +5,0 à -5,0. Toujours vérifier un graphique long-terme pour établir la plage normale de l'instrument analysé.
**TRADEX-AI C3** : Impératif de calibration par actif — chaque marché (GC/HG/CL/ZW) doit avoir ses seuils de surachat/survente PMO calibrés empiriquement, pas de constante universelle.
*Catégorie : configuration*

---

### D1457 — Dépendance au timeframe
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_08) : Les indicateurs techniques sont calculés sur un nombre spécifique de périodes du timeframe traité, donc un PMO mensuel a une allure complètement différente d'un PMO journalier (même période de 7 ans illustrée).
**TRADEX-AI C3** : Le PMO doit être calibré et lu par timeframe ; cohérent avec les modes Belkhayate (15min / Range Bar / scalping) — un PMO par mode.
*Catégorie : configuration*

---

### D1458 — Usage comme indicateur de momentum
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_09) : Comme indicateur de momentum, le PMO exprime la direction et la vélocité du mouvement de prix. Sur le Gold ETF (GLD), les mouvements les plus forts (dans les deux sens) sont caractérisés par un PMO droit, raide et lisse ; les tendances plus hésitantes s'accompagnent de fréquents changements de direction du PMO. Les sommets/creux du PMO suggèrent un changement de direction du momentum — drapeaux précoces de tops/bottoms de prix, plus fiables en territoire suracheté/survendu.
**TRADEX-AI C3** : Exemple explicite sur l'Or (GLD) — pertinent pour GC. La « rectitude/lissage » du PMO comme mesure qualitative de la force de tendance.
*Catégorie : indicateurs_momentum*

---

### D1459 — Divergences PMO/prix
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_10) : Comme d'autres oscillateurs, le PMO donne des indices de changements importants de direction en formant des divergences contre l'indice de prix. Divergences négatives (lignes rouges) = avertissement de tops importants (prix fait un plus haut plus élevé, PMO un plus haut plus bas). Divergence positive (lignes vertes) = signal d'un bottom important (prix fait un plus bas plus bas, PMO un plus bas plus haut).
**TRADEX-AI C3** : Règle de divergence classique directement codable (comparaison extrêmes prix vs extrêmes PMO) ; signal d'alerte de retournement.
*Catégorie : divergence*

---

### D1460 — Générateur de signaux (croisement)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_11) : Le PMO génère un signal de croisement quand il traverse son EMA-10-périodes. Ces signaux tendent à être court-terme mais peuvent durer plusieurs semaines. Ne pas les prendre au pied de la lettre car ils peuvent générer beaucoup de whipsaw — ils alertent sur des opportunités possibles plutôt que servir de modèle mécanique. Toujours vérifier le chart (price pattern + configuration du PMO). Les signaux sont meilleurs quand le prix est étendu, près d'un support/résistance, et le PMO très suracheté/survendu.
**TRADEX-AI signal** : Croisement PMO/signal = déclencheur candidat MAIS explicitement non-mécanique ; impose confirmation contextuelle (support/résistance + extrême) — cohérent avec l'exigence projet de confluence.
*Catégorie : signal*

---

### D1461 — Croisements EMA 20/50/200 (DecisionPoint Trend)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md) : Les signaux PMO peuvent être combinés avec l'analyse de tendance DecisionPoint utilisant les croisements EMA 20/50/200, qui déterminent le biais haussier/baissier long-terme, intermédiaire et court-terme. Les signaux les plus fiables surviennent quand le PMO est près des extrêmes de sa plage normale, ou lors d'un changement de direction et croisement suivant un mouvement PMO fort, propre et droit. Beaucoup de « bruit » se génère autour de la ligne zéro et quand le PMO est plat.
**TRADEX-AI C3** : Filtre multi-timeframe via EMA 20/50/200 pour qualifier le biais ; zone zéro = bruit à éviter. Stratifie la fiabilité du signal selon la position dans la plage.
*Catégorie : indicateurs_tendance*

---

### D1462 — Configuration « Sideways Wiggle »
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_12) : Formation PMO courante illustrant pourquoi tous les croisements ne se prennent pas littéralement. Lors d'une tendance haussière régulière à faible volatilité, le PMO bouge latéralement. Le fait qu'il reste au-dessus de zéro témoigne de la force du mouvement ; cependant, de mineurs zigzags de prix font whipsawer le PMO au-dessus/en-dessous de son EMA-10, générant de nombreux signaux haussiers de croisement non profitables. Le sideways wiggle finit par se terminer et peut offrir des indices subtils de fin de tendance.
**TRADEX-AI signal** : Anti-pattern explicite (whipsaw en tendance calme) ; argument pour filtrer les croisements quand le PMO est plat au-dessus de zéro — réduit les faux signaux.
*Catégorie : configuration*

---

### D1463 — Configuration « Bear Kiss »
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_13) : Le « bear kiss » est la partie finale de trois actions de topping. On le cherche quand le PMO est relativement suracheté et le prix a fait un mouvement haussier substantiel. Séquence : (1) un faux top du PMO ; (2) un top légèrement plus haut suivi d'un croisement de vente (PMO traverse vers le bas son EMA-10) ; (3) le PMO remonte puis retombe après avoir juste « embrassé » le dessous de l'EMA-10. Aspect important : l'indice de prix a cassé une ligne de tendance haussière en conjonction avec le bear kiss.
**TRADEX-AI signal** : Pattern de retournement baissier en 3 temps + confirmation par cassure de trendline ; codable comme séquence d'états pour renforcer la confiance d'un top.
*Catégorie : configuration*

---

### D1464 — Configuration « Bull Kiss »
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_14) : Le « bull kiss » survient peu après un signal d'achat de croisement PMO, résultant d'un pullback de prix après la poussée initiale qui a généré le croisement. Bull et bear kiss sont essentiellement opposés et symétriques, mais le comportement de prix diffère : le bear kiss est normalement une non-confirmation coïncidant avec le plus haut final d'un rallye, tandis que le bull kiss coïncide normalement avec un plus bas plus élevé dans un nouveau rallye.
**TRADEX-AI signal** : Pattern de confirmation haussière (pullback après croisement d'achat) ; symétrique du bear kiss, utile comme renfort d'un signal d'achat.
*Catégorie : configuration*

---

### D1465 — Configuration « Clean Signals »
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_15) : Si les formations bull/bear kiss sont communes, il est aussi possible d'avoir des renversements/croisements PMO très propres, dépourvus des gyrations associées aux blow-offs et retests, quand le changement de tendance de prix est relativement lisse. Les actions de renversement et croisement couvrent un large éventail de configurations ; étudier les charts mène à mieux comprendre quel price action engendre quel comportement PMO.
**TRADEX-AI signal** : Reconnaissance que la fiabilité dépend de la « propreté » du croisement ; les croisements lisses sont plus fiables que ceux entourés de gyrations.
*Catégorie : configuration*

---

### D1466 — Synthèse des usages (Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md) : Le PMO peut être utilisé à la fois comme mesure de force relative, de momentum et de conditions de surachat/survente. Il peut aussi servir à déterminer les renversements de prix via les croisements haussiers/baissiers.
**TRADEX-AI C3** : Triple rôle confirmé (force relative + momentum + surachat/survente) ; positionne le PMO comme feature multi-usage de la couche momentum.
*Catégorie : indicateurs_momentum*

---

### D1467 — Paramètres SharpCharts par défaut
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_16) : Le DecisionPoint PMO est disponible dans SharpCharts. Réglages par défaut : EMA 35-périodes et 20-périodes avec une ligne de signal EMA 10-périodes. Les utilisateurs peuvent opter pour un timeframe plus court/long pour augmenter/diminuer la sensibilité. L'indicateur peut être placé au-dessus, en dessous ou derrière le tracé de prix.
**TRADEX-AI configuration** : Paramètres par défaut 35/20/10 confirmés ; sensibilité réglable via la longueur des périodes — point de départ d'implémentation.
*Catégorie : configuration*

---

### D1468 — Scan « PMO rising not yet crossed » (haussier)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md) : Scan haussier : base de titres ≥ 10 $ et ≥ 100 000 de volume quotidien sur 60 jours. Le PMO doit avoir monté les 3 derniers jours mais pas encore croisé sa ligne de signal ; de plus EMA20 > EMA50 > EMA200 (marché haussier intermédiaire/long-terme). Critères PMO(35,20,10) croissants sur 3 jours et PMO Line < PMO Signal.
**TRADEX-AI signal** : Logique de scan codable (PMO ascendant pré-croisement + alignement EMA haussier) ; détecteur d'anticipation de croisement d'achat. Filtres prix/volume à adapter aux futures.
*Catégorie : signal*

---

### D1469 — Scan « PMO falling not yet crossed » (baissier)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md) : Scan baissier symétrique : PMO en déclin les 3 derniers jours mais pas encore croisé sous sa ligne de signal ; EMA20 < EMA50 < EMA200 (marché baissier intermédiaire/long-terme). Critères PMO(35,20,10) décroissants sur 3 jours et PMO Line > PMO Signal.
**TRADEX-AI signal** : Miroir baissier du scan précédent ; détecteur d'anticipation de croisement de vente avec alignement EMA baissier.
*Catégorie : signal*

---

### D1470 — Calcul illustré sur Amazon (table)
🟢 **FAIT VÉRIFIÉ** (Source : decisionpoint_price_momentum_oscillator_pmo.md, image_02) : Une table de calcul du PMO est fournie pour Amazon, avec un tableur Excel téléchargeable reproduisant ces calculs (double lissage custom du ROC à 1 période).
**TRADEX-AI indicateurs_momentum** : Référence de validation numérique (table + tableur) permettant de vérifier une implémentation du PMO contre des valeurs de référence avant codage.
*Catégorie : indicateurs_momentum*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D1451 → D1470 (20 décisions) |
| Images certifiées | 16/16 |
| Catégories couvertes | indicateurs_momentum · indicateurs_tendance · divergence · signal · configuration |
| Cercle dominant | C3 (momentum / force relative) |
| Lien Belkhayate | NON CONCERNÉ (indicateur Swenlin/DecisionPoint, hors méthode Belkhayate) |
| Cas à vérifier | Aucun blocage — noter que les bornes surachat/survente (+2,5/-2,5) sont spécifiques aux indices et DOIVENT être recalibrées par actif (D1456) et par timeframe (D1457) avant tout usage sur GC/HG/CL/ZW |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement (exemple source GLD = proxy Or pertinent pour GC). Indicateur issu de Carl Swenlin / DecisionPoint, aucun rapport affirmé avec la méthode Belkhayate.
