# Extraction StockCharts — Arthur Hill on Moving Average Crossovers
**Source :** `bundles/stockcharts/arthur_hill_on_moving_average_crossovers.md` (HTTP 200 · ~3 800 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D711 → D718 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/arthur-hill-on-moving-average-crossovers
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Applying exponential moving averages and Percentage Price Oscillator to generate buy and sell signals | Some Examples | CERTIFIE (accord .md + HTML) |
| image_02.png | Some Examples [SECTION-FALLBACK] | Some Examples | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D711 — Principe du système à deux moyennes mobiles (croisement = signal)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md) : « A trading system using two moving averages would give a buy signal when the shorter (faster) moving average crosses above the longer (slower) moving average. A sell signal would be given when the shorter moving average crosses below the longer moving average. » Usage populaire des moyennes mobiles pour bâtir des systèmes de trading simples basés sur les croisements.
**TRADEX-AI C1** : Croisement court/long = règle déterministe codable comme feature de tendance ; à traiter comme couche analytique, jamais comme déclencheur d'ordre automatique.
*Catégorie : indicateurs_tendance*

---

### D712 — Arbitrage vitesse/bruit selon la longueur des moyennes
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md) : « The speed of the systems and the number of signals generated will depend on the length of the moving averages. Shorter moving average systems will be faster, generate more signals, and be nimble for early entry. However, they will generate more false signals than systems with longer moving averages. » Compromis entre réactivité (entrée précoce) et nombre de faux signaux.
**TRADEX-AI C1** : Paramétrage des périodes = arbitrage explicite réactivité vs bruit ; à caler sur le timeframe Belkhayate retenu (15min / Range Bar).
*Catégorie : indicateurs_tendance*

---

### D713 — Exemple AAPL : croisement EMA 30/100 pour buy/sell
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md, image_01) : Sur le graphique journalier d'Apple (AAPL), un croisement d'EMA 30/100 génère les signaux d'achat et de vente. Signal d'achat quand l'EMA 30 jours passe au-dessus de l'EMA 100 jours ; signal de vente quand l'EMA 30 passe sous l'EMA 100.
**TRADEX-AI C1** : Exemple concret de paramétrage (30/100 EMA daily) ; valeur illustrative, paramètres à reparamétrer selon timeframe TRADEX.
*Catégorie : signal*

---

### D714 — Lecture du croisement via le PPO (différentiel des EMA)
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md, image_01) : Un tracé différentiel 30/100 est affiché sous le graphique de prix via le Percentage Price Oscillator (PPO) réglé sur (30,100,1). L'EMA 30 est supérieure à l'EMA 100 quand le différentiel est positif ; quand il est négatif, l'EMA 30 est inférieure à l'EMA 100.
**TRADEX-AI C1** : Le PPO sert de proxy normalisé (%) du croisement, exploitable comme feature continue plutôt que signal binaire.
*Catégorie : indicateurs_tendance*

---

### D715 — Limite intrinsèque : efficace en tendance, inefficace en range
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md) : « As with all trend-following systems, the signals work well when the stock develops a strong trend but are ineffective when the stock is in a trading range. » L'entrée de Nov 2023 fut un bon point pour un long, mais le signal de sortie par croisement de Mars 2024 aurait rendu une partie des profits.
**TRADEX-AI C1** : Garde-fou — désactiver/filtrer les signaux de croisement en range (cohérent avec la logique « pas de trade en range » Belkhayate) ; les croisements rendent une partie des gains au retournement.
*Catégorie : structure_marche*

---

### D716 — Exemple EMA 20/60 et réduction des faux signaux par bandes ±2 %
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md, image_02) : Un système EMA 20/60 génère plusieurs signaux ; le différentiel 20/60 est tracé en % via PPO (20,60,1). Utiliser zéro comme point de croisement génère trop de faux signaux. Pour les réduire, placer le signal d'achat juste au-dessus de zéro (ex. +2 %) et le signal de vente juste en dessous (-2 %) : achat en force quand l'EMA 20 est à plus de 2 % au-dessus de l'EMA 60 ; vente quand l'EMA 20 est à plus de 2 % sous l'EMA 60.
**TRADEX-AI C1** : Bande morte ±X % autour du croisement = filtre anti-whipsaw directement codable (seuil paramétrable, ici 2 %).
*Catégorie : signal*

---

### D717 — Whipsaws et nécessité de stops serrés / trailing / SAR
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md) : On trouve de bons signaux mais aussi des whipsaws ; des trades rentables sont possibles, mais certains profits peuvent ne pas suffire à justifier le risque. Si une action ne tient pas sa tendance, il faut placer des stop-loss serrés pour verrouiller les profits ; un trailing stop ou le parabolic SAR auraient pu aider à verrouiller les gains.
**TRADEX-AI C7** : Renforce la règle de gestion de sortie (trailing stop / SAR) en complément du croisement ; le signal d'entrée seul ne suffit pas sans gestion de risque.
*Catégorie : gestion_risque_entree*

---

### D718 — The Bottom Line : combiner le croisement avec d'autres outils, pas de garantie future
🟢 **FAIT VÉRIFIÉ** (Source : arthur_hill_on_moving_average_crossovers.md) : « Moving average crossover systems can be effective but should be used with other aspects of technical analysis (patterns, candlesticks, momentum, volume, and so on). While it's easy to find a system that worked well in the past, there is no guarantee it will work in the future. »
**TRADEX-AI C1** : Le croisement n'est qu'une brique de confluence (jamais signal isolé) ; mise en garde explicite contre l'overfitting du backtest, cohérente avec la prudence du projet sur les paramètres COG.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D711 | Système 2 MM = croisement court/long | 🟢 | C1 | indicateurs_tendance |
| D712 | Arbitrage vitesse vs faux signaux | 🟢 | C1 | indicateurs_tendance |
| D713 | Exemple AAPL EMA 30/100 | 🟢 | C1 | signal |
| D714 | Lecture via PPO (différentiel EMA) | 🟢 | C1 | indicateurs_tendance |
| D715 | Efficace en tendance / inefficace en range | 🟢 | C1 | structure_marche |
| D716 | EMA 20/60 + bande ±2 % anti-faux signal | 🟢 | C1 | signal |
| D717 | Whipsaws → stops serrés / trailing / SAR | 🟢 | C7 | gestion_risque_entree |
| D718 | Bottom Line : combiner + pas de garantie | 🟢 | C1 | signal |

**Liens Belkhayate :** Aucun lien direct. Les croisements de moyennes mobiles ne sont PAS un indicateur Belkhayate (⚫). Lien indirect : la mise en garde « inefficace en range » recoupe la logique « ne pas trader en range » de la méthode, mais l'attribuer à Belkhayate serait « hypothèse projet, non affirmée par la source » (⚫🔴). Sinon NON CONCERNÉ.

**À vérifier (humain) :**
- D713/D716 — paramètres 30/100 et 20/60 et bande ±2 % : exemples pédagogiques sur actions US, à NE PAS coder tels quels pour GC/HG/CL/ZW sans recalibration sur le timeframe TRADEX.
- image_02 — label par SECTION-FALLBACK (la figure source a un alt/figcaption vide dans le .md) ; certifiée par concordance .md/HTML mais sans légende descriptive propre. À confirmer visuellement.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
