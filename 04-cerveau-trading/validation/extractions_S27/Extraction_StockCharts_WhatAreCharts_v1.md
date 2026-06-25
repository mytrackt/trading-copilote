# Extraction StockCharts — What Are Charts?
**Source :** `bundles/stockcharts/what_are_charts.md` (HTTP 200) + 9 images certifiées
**Méthode images :** double ancrage (figcaption label + alt) · 9/9 certifiées · 0 à vérifier
**Décisions :** D4851 → D4870 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/what-are-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Fondements lecture de charts applicables à GC/HG/CL/ZW — choix timeframe, type de chart et échelle influencent directement la qualité des signaux Belkhayate.

---

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/EVbZrTe4OM43z5wByx4v | An introductory price chart of GE | Introduction | D4851 |
| /files/yW3XB8C3j8ma2TWqJeIn | Daily chart | How to Pick a Timeframe | D4852 |
| /files/DwzXZvumXLLOnCcwX4ID | Weekly chart | How to Pick a Timeframe | D4852 |
| /files/YvFQzbe7RKOxgfQ314nu | An example of a line chart | Line Chart | D4854 |
| /files/Ite0h2EXe0VkBH5MWimm | Bar chart with high, low, and close | Bar Chart | D4855 |
| /files/HkGEavwH3b3hg9S2PODK | Bar chart displaying open, high, low, and close | Bar Chart | D4856 |
| /files/pmpKWx6wl3eU2IuuTE3v | Example of hollow and filled candlestick bars | Candlestick Chart | D4857 |
| /files/9071lQhCwXOdCZuLI7l0 | Example of a logarithmic scale price chart | Price Scaling | D4864 |
| /files/WdEPKtFvakHJzx5N8UUR | Example of an arithmetic scale price chart | Price Scaling | D4865 |

---

## DÉCISIONS

### D4851 — Définition d'un chart de prix
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Un chart de prix est une séquence de prix tracés sur un timeframe spécifique — l'axe Y représente l'échelle de prix, l'axe X représente le temps, les prix les plus récents sont à droite. Les techniciens utilisent ces charts pour analyser des instruments financiers (actions, obligations, commodités, futures, indices) et prévoir les mouvements futurs.
**TRADEX-AI C1** : Applicable à GC/HG/CL/ZW — la lecture correcte d'un chart de prix est le socle de toute analyse Belkhayate ; les futures commodités ont un axe temporel de gauche à droite identique.
*Catégorie : structure_marche*

---

### D4852 — Choix du timeframe selon le style de trading
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Les traders se concentrent sur des charts journaliers et intraday (moins de 5 mois visibles sur 100 barres) pour les mouvements court-terme — plus de détail mais plus de bruit. Les investisseurs utilisent des charts hebdomadaires et mensuels (jusqu'à 2 ans sur 100 barres) pour les tendances long-terme. Il y a environ 20 jours de trading par mois et 252 jours de trading par an.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW en mode intraday, privilégier les range bars NT8 (comme décidé en phase C) ; la compression weekly sert à contextualiser la tendance macro avant d'affiner en intraday.
*Catégorie : timing*

---

### D4853 — Chart journalier vs hebdomadaire : compression des données
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : 100 points sur un chart journalier = environ 5 mois. 100 points sur un chart hebdomadaire = environ 2 ans. Les charts long-terme avec données compressées montrent des mouvements moins extrêmes et moins de bruit.
**TRADEX-AI C1** : Dans TRADEX-AI, le contexte macro (tendance 2 ans) peut être établi via chart hebdomadaire GC/ES avant de valider un signal intraday — cohérent avec l'approche multi-timeframe Belkhayate.
*Catégorie : timing*

---

### D4854 — Chart en ligne : avantages et limites
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Le chart en ligne utilise uniquement le cours de clôture — il ignore les fluctuations intraday. Utile quand seules les données de clôture sont disponibles (indices, données intraday limitées). Moins encombré mais sans plage haut-bas.
**TRADEX-AI C1** : Pour DX (Dollar Index via Alpha Vantage proxy), si seul le close est disponible, le chart en ligne reste acceptable pour confirmer la tendance macro — non applicable aux futures NT8 qui fournissent OHLC complet.
*Catégorie : structure_marche*

---

### D4855 — Bar chart OHLC : lecture des données
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Le bar chart représente haut/bas par la barre verticale, le close par un trait horizontal à droite, l'open par un trait horizontal à gauche. Efficace pour afficher un grand volume de données. Idéal pour analyser le close relatif au haut et au bas. Les bars sont fines → plus de barres affichables.
**TRADEX-AI C1** : NT8 exporte les données JSON en format OHLCV ; la lecture haut/bas/clôture est identique que sur bar chart — pertinent pour valider les niveaux Belkhayate (BGC, Direction, pivots).
*Catégorie : structure_marche*

---

### D4856 — Candlestick chart : relationship open/close
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Le candlestick requiert Open/High/Low/Close. Chandelle creuse (close > open) = pression acheteuse. Chandelle pleine (close < open) = pression vendeuse. Le corps = zone entre open et close. Les mèches = haut et bas. Origines japonaises (300 ans). Un chart weekly utilise l'open du lundi, la plage high-low de la semaine, le close du vendredi.
**TRADEX-AI C1** : Les signaux de structure Belkhayate (BGC, bougies de retournement) s'appuient sur la relation open/close — la lecture candlestick est donc le format de référence pour GC/HG/CL/ZW en analyse visuelle.
*Catégorie : structure_marche*

---

### D4857 — Candlestick : code couleur close vs close précédent
🔵 **ÉCOLE** (Source : what_are_charts.md) : Certains charts candlestick utilisent la couleur en fonction du close vs close précédent (vert si close > close précédent, rouge si inférieur) plutôt que close vs open de la même bougie. Ces deux conventions coexistent.
**TRADEX-AI C1** : Dans TRADEX-AI, la convention Belkhayate standard est close vs open (chandelle creuse/pleine) — ne pas confondre avec close vs close précédent lors de la lecture des signaux NT8.
*Catégorie : structure_marche*

---

### D4858 — Point & Figure chart : price only, no time
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Le chart Point & Figure est basé uniquement sur les mouvements de prix significatifs — il ignore le temps. Seuls les mouvements dépassant des seuils définis sont enregistrés. Facilite l'identification des supports/résistances, des breakouts haussiers et breakdowns baissiers.
**TRADEX-AI C1** : Non utilisé directement dans TRADEX-AI (architecture NT8 range bars), mais les niveaux de support/résistance P&F peuvent servir de référence secondaire pour confirmer les pivots Belkhayate sur GC.
*Catégorie : structure_marche*

---

### D4859 — Cohérence méthodologique : choisir et s'y tenir
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Aucune méthode de chart n'est supérieure aux autres — les données sous-jacentes sont les mêmes. La clé est la cohérence : choisir une méthode et la maîtriser. Changer de méthode en cours d'analyse nuit à la concentration. **"It is the analysis of the price action that separates successful technicians from not-so-successful technicians."** Les 3 clés : Dédicace, Focus, Consistance.
**TRADEX-AI C1** : Règle alignée avec la philosophie Belkhayate de TRADEX-AI — la méthode est verrouillée, on ne la rouvre pas. La consistance dans l'application des règles est un garde-fou implicite.
*Catégorie : psychologie*

---

### D4860 — Échelle arithmétique vs logarithmique : définitions
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : Échelle arithmétique = 10 points = même distance verticale quel que soit le niveau de prix (distance absolue constante). Échelle logarithmique = mouvements en pourcentage → une avance de 10 à 20 (+100%) occupe la même distance qu'une avance de 40 à 80 (+100%).
**TRADEX-AI C1** : Pour l'analyse de GC sur longue période (ex. bull run oro), l'échelle log met en perspective les grands mouvements ; pour le trading court terme intraday GC, l'arithmétique est adaptée.
*Catégorie : structure_marche*

---

### D4861 — Quand utiliser l'échelle arithmétique
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : L'échelle arithmétique est utile quand : (1) le range de prix est confiné dans une plage serrée, (2) les charts court-terme et le trading — les mouvements de prix sont montrés en termes absolus, dollar pour dollar.
**TRADEX-AI C1** : Pour le trading intraday GC/HG/CL/ZW (range bars NT8), l'échelle arithmétique est le choix correct — les signaux Belkhayate fonctionnent sur les mouvements absolus de ticks/points.
*Catégorie : timing*

---

### D4862 — Quand utiliser l'échelle logarithmique
🟢 **FAIT VÉRIFIÉ** (Source : what_are_charts.md) : L'échelle log est utile quand : (1) le prix a beaucoup bougé sur une courte ou longue période, (2) pour l'analyse des lignes de tendance (meilleur ajustement aux creux), (3) pour jauger les mouvements en % sur longue période — les grands mouvements sont mis en perspective.
**TRADEX-AI C1** : Pour l'analyse de contexte macro (tendance long terme de GC, CL) avant un signal intraday, l'échelle log donne une meilleure perspective — aligné avec l'approche multi-timeframe de TRADEX-AI.
*Catégorie : timing*

---

### D4863 — Traders vs investisseurs : usage des timeframes
🟡 **SYNTHÈSE** (Source : what_are_charts.md) : Traders → charts intraday + journaliers → court terme → plus de bruit. Investisseurs → charts hebdomadaires + mensuels → 1 à 4 ans → moins de bruit. Utilisation combinée : charts long terme pour la vue d'ensemble, charts courts terme pour zoomer sur quelques mois.
**TRADEX-AI C4** : Dans TRADEX-AI, la macro (C4) utilise des données hebdomadaires/mensuelles pour DX/ES/VX, tandis que les signaux d'exécution utilisent les range bars NT8 intraday — cette hiérarchie est conforme aux meilleures pratiques de lecture des charts.
*Catégorie : timing*
