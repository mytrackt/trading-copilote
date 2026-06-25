# Extraction StockCharts — Candlesticks and Traditional Chart Analysis
**Source :** `bundles/stockcharts/candlesticks_and_traditional_chart_analysis.md` (HTTP 200 · ~9 500 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D1091 → D1102 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlesticks-and-traditional-chart-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Confirming candlestick bullish confirmation signals with moving averages | Candlesticks and Moving Averages | CERTIFIE (accord .md + HTML) |
| image_02.png | Bearish candlestick patterns are confirmed by a downside breakout | Candlesticks and Breakouts | CERTIFIE (accord .md + HTML) |
| image_03.png | In an OHLC bar chart, harder to evaluate breakout direction | Candlesticks and Breakouts | CERTIFIE (accord .md + HTML) |
| image_04.png | Combining candlesticks and head and shoulders pattern | Candlesticks and the Head & Shoulders Pattern | CERTIFIE (accord .md + HTML) |
| image_05.png | Candlestick chart with volume | Candlesticks and Volume | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1091 — Rôle des chandeliers : confirmer d'autres outils d'analyse technique
🔵 **ÉCOLE (analyse technique classique)** (Source : candlesticks_and_traditional_chart_analysis.md) : Les chandeliers japonais ont une valeur propre comme système de graphique, mais leur force tient surtout à leur capacité à confirmer les signaux générés par d'autres outils (moyennes mobiles, breakouts, head & shoulders, volume). Ces relations mutuellement bénéfiques renforcent la confiance de l'investisseur lors de l'analyse.
**TRADEX-AI C1** : Posture architecturale — les patterns chandeliers sont une couche de confirmation, jamais un déclencheur isolé. Cohérent avec la règle 3/4 + 2/3 du projet (multi-signaux alignés).
*Catégorie : signal*

---

### D1092 — Chandeliers + moyenne mobile : confirmation de support
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_01) : Sur le graphique d'exemple, deux zones montrent un *spinning top* puis un *doji*, suivis d'un long chandelier blanc (hollow). Ces patterns ajoutent une confirmation haussière de la moyenne mobile 200 jours servant de support (vers le 10 octobre et le 5 février). Les mêmes patterns confirment aussi le niveau 30 du RSI comme condition de survente.
**TRADEX-AI C1** : Pattern de retournement (spinning top/doji + bougie de confirmation) au contact d'un support dynamique = configuration multi-confirmation. La MM200 jouant le rôle de support recoupe l'idée des Pivots Belkhayate comme niveaux de réaction.
*Catégorie : configuration*

---

### D1093 — Spinning top et doji = indécision
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_02) : Le *spinning top* et le *doji* traduisent l'indécision du marché. Dans l'exemple du triangle, la ligne supérieure est touchée deux fois par des *spinning tops*, signalant cette indécision avant la cassure.
**TRADEX-AI C1** : Feature « indécision » (petit corps, mèches symétriques) détectable à partir des OHLC NT8 ; signal d'attente / réduction de conviction, pas d'entrée.
*Catégorie : signal*

---

### D1094 — Chandeliers + breakout de pattern classique (validation directionnelle)
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_02) : Quand un pattern chandelier haussier ou baissier apparaît au voisinage d'un breakout traditionnel (zones de congestion), il ajoute de la validité à la direction de ce breakout. L'exemple aboutit à une cassure par le bas.
**TRADEX-AI C1** : Règle de confirmation de breakout : exiger un pattern chandelier cohérent avec la direction de cassure avant validation. Transposable en filtre de cohérence directionnelle.
*Catégorie : configuration*

---

### D1095 — Bearish harami avant cassure baissière du triangle ascendant
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_02) : Juste avant la cassure par le bas du triangle, apparaît un *bearish harami*, suivi d'un autre jour baissier servant de confirmation. Puis le prix gappe sous le triangle ascendant avec un long chandelier plein (filled). L'ensemble dresse un tableau globalement baissier.
**TRADEX-AI C1** : Séquence harami + bougie de confirmation + gap = chaîne de signaux baissiers détectable. Le *bearish harami* sert d'alerte précoce avant la cassure structurelle.
*Catégorie : signal*

---

### D1096 — Un pattern classique haussier peut être invalidé par la lecture chandelier
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md) : Le triangle ascendant est traditionnellement reconnu comme un pattern haussier. Pourtant, dans cet exemple, le comportement baissier émergent a été identifié grâce à l'analyse des chandeliers, qui a primé sur la lecture classique.
**TRADEX-AI C1** : Garde-fou — ne pas appliquer mécaniquement le biais directionnel théorique d'un pattern de prix ; la micro-structure chandelier peut le contredire. Gérer les signaux conflictuels explicitement.
*Catégorie : structure_marche*

---

### D1097 — Avantage chandeliers sur le bar chart OHLC pour anticiper la cassure
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_03) : Le bar chart OHLC repose sur les mêmes données mais porte moins d'information utile. Le triangle ascendant y est facilement reconnaissable, mais sans analyse chandelier (haramis, etc.), il est plus difficile d'évaluer la direction probable de la cassure AVANT qu'elle se produise.
**TRADEX-AI C1** : Justifie le choix d'un flux OHLC complet exploité en logique chandelier plutôt qu'en simple bar chart ; valeur prédictive supérieure de la micro-structure.
*Catégorie : structure_marche*

---

### D1098 — Limite des chandeliers : pas d'objectif de prix
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md) : Une limite de l'usage isolé des patterns chandeliers est qu'ils ne fournissent pas d'objectif de prix potentiel. Cela peut être obtenu en combinant les chandeliers avec d'autres techniques d'analyse technique.
**TRADEX-AI C1** : Conséquence design — les chandeliers donnent timing/direction mais pas de target ; la cible vient d'un pattern structurel (cf. head & shoulders, D1099) ou du R/R (≥ 1:2 projet).
*Catégorie : gestion_risque_entree*

---

### D1099 — Head & Shoulders : objectif de prix via projection neckline
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_04) : Dans le pattern *head & shoulders* avec cassure baissière, un *bearish harami* puis deux longues bougies baissières se forment durant l'épaule droite et confirment la cassure. Sans identification du H&S, le *bearish harami* ne donnerait aucune indication d'objectif. Le calcul traditionnel d'objectif H&S : prendre la distance du sommet de la tête à la neckline et la soustraire du point de cassure de la neckline.
**TRADEX-AI C1** : Formule d'objectif déterministe (hauteur tête→neckline projetée). Combinable au timing chandelier pour produire entrée + cible chiffrée ; utile au calcul R/R.
*Catégorie : gestion_risque_entree*

---

### D1100 — Complémentarité des analyses et gestion des signaux conflictuels
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md) : Combiner les deux types d'analyse donne une image plus claire que l'un ou l'autre isolément ; l'analyse technique n'est pas une science exacte et il faut chercher des signaux confirmants. Autre avantage : les chandeliers peuvent fournir des signaux CONFLICTUELS avec l'analyse classique — c'est l'occasion de décider si le poids des preuves justifie le trade ou s'il vaut mieux passer.
**TRADEX-AI C1** : Logique « weight of evidence » → quantifier l'accord/désaccord entre couches ; un conflit doit pouvoir abaisser le score ou imposer ATTENDRE. Aligné avec la grille déterministe /10.
*Catégorie : signal*

---

### D1101 — Volume comme confirmation des patterns chandeliers
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md, image_05) : Sur le même graphique XOM avec volume ajouté : le volume augmente et passe au-dessus de sa MM200 pendant la formation du *bearish harami*, explose au breakout du triangle ascendant, puis décline lentement durant la correction haussière post-cassure. Quand le prix retourne à la baisse, le volume remonte. Après une seconde brève correction, un *doji* se forme sur un volume énorme (flèches vertes) et le sell-off se poursuit.
**TRADEX-AI C2** : Le volume valide/invalide le pattern chandelier (harami sur volume croissant, doji sur volume extrême). Recoupe l'order flow ATAS — pattern + pic de volume = confirmation renforcée.
*Catégorie : divergence*

---

### D1102 — Synthèse : les chandeliers comme preuve additionnelle, jamais isolés
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_traditional_chart_analysis.md) : Les patterns chandeliers aident à identifier des changements potentiels de direction ; utilisés avec l'analyse technique traditionnelle, ils ajoutent une confirmation. Plus on accumule d'informations convergentes, plus la conviction est forte. Les techniques d'AT fonctionnent mieux combinées à des techniques confirmantes ; plus de preuves → décisions mieux informées et meilleure capacité à reconnaître qu'on a tort et à sortir d'une position perdante.
**TRADEX-AI C1** : Principe directeur réutilisable — empilement de preuves convergentes (confluence) ; intègre aussi la sortie de position perdante (gestion du risque) quand les preuves se retournent.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1091 | Chandeliers = confirmateurs d'autres outils | 🔵 ÉCOLE | C1 | signal |
| D1092 | Chandeliers + MM200 = confirmation support | 🟢 | C1 | configuration |
| D1093 | Spinning top / doji = indécision | 🟢 | C1 | signal |
| D1094 | Chandeliers + breakout = validation direction | 🟢 | C1 | configuration |
| D1095 | Bearish harami avant cassure triangle | 🟢 | C1 | signal |
| D1096 | Lecture chandelier peut invalider pattern classique | 🟢 | C1 | structure_marche |
| D1097 | Avantage chandelier vs bar chart OHLC | 🟢 | C1 | structure_marche |
| D1098 | Limite : pas d'objectif de prix | 🟢 | C1 | gestion_risque_entree |
| D1099 | Objectif H&S (projection neckline) | 🟢 | C1 | gestion_risque_entree |
| D1100 | Complémentarité / signaux conflictuels | 🟢 | C1 | signal |
| D1101 | Volume confirme les patterns chandeliers | 🟢 | C2 | divergence |
| D1102 | Synthèse — preuve additionnelle, jamais isolée | 🟢 | C1 | signal |

**Liens Belkhayate :** les chandeliers japonais et les patterns classiques (triangle, H&S) ne sont PAS des éléments propres à la méthode Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé par Belkhayate) : l'usage d'un support/MM comme niveau de réaction (D1092) recoupe l'esprit des Pivots Belkhayate, et la logique « déclencheur chandelier sur niveau » recoupe l'étape 4 (Énergie/Déclencheur) de la méthode opérationnelle d'Abdelkrim. Ne rien inventer au-delà.

**À vérifier (humain) :**
- D1099 — la formule d'objectif H&S est exploitable mais dépend du tracé manuel de la neckline (subjectif) ; à encadrer avant tout codage automatique.
- D1101 — la confirmation par volume suppose un flux volume fiable (NT8/ATAS) ; le « volume énorme » du doji est qualitatif, à seuiller objectivement par actif (GC/HG/CL/ZW).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
