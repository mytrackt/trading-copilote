# Extraction StockCharts — Heikin-Ashi Candlesticks
**Source :** `bundles/stockcharts/heikin_ashi_candlesticks.md` (HTTP 200 · ~13 071 car.) + 9 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 9/9 certifiées
**Décisions :** D2011 → D2030 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/heikin-ashi-candlesticks
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Spreadsheet displaying Heikin-Ashi calculations. | Calculating Heikin-Ashi | CERTIFIE |
| image_02.png | Example showing how candlesticks convert to Heikin-Ashi candlesticks. | Calculating Heikin-Ashi | CERTIFIE |
| image_03.png | HA chart : indecisive market, strong decline, strong advance. | How To Read a Heikin-Ashi Chart | CERTIFIE |
| image_04.png | Illustration of dojis and spinning tops. | Doji and Spinning Tops | CERTIFIE |
| image_05.png | Spinning top and dojis represent reversal areas (confirmation = breakout). | Doji and Spinning Tops | CERTIFIE |
| image_06.png | HA chart : breakouts from falling wedge and triangle. | Classic Chart Patterns and Heikin-Ashi | CERTIFIE |
| image_07.png | HA chart : breakout from a falling channel. | Classic Chart Patterns and Heikin-Ashi | CERTIFIE |
| image_08.png | Candlesticks and Heikin-Ashi Candlesticks (side by side). | SharpCharts | CERTIFIE |
| image_09.png | SharpChart settings for Heikin-Ashi charts. | SharpCharts | CERTIFIE |

## DÉCISIONS

### D2011 — Définition : chandelier combo issu des chandeliers japonais
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « Heikin-Ashi Candlesticks are an offshoot from Japanese candlesticks. Heikin-Ashi Candlesticks use the open-close data from the prior period and the open-high-low-close data from the current period to create a combo candlestick. The resulting candlestick filters out some noise in an effort to better capture the trend. »
**TRADEX-AI C1** : Type de chandelier lissé (combo prix courant + prior) ; filtre le bruit pour mieux capter la tendance. Mode d'affichage alternatif au chandelier classique.
*Catégorie : indicateurs_tendance*

---

### D2012 — Étymologie : « pace moyen des prix »
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « In Japanese, Heikin means "average" and Ashi means "pace"... Heikin-Ashi represents the average pace of prices. »
**TRADEX-AI C1** : 🔵 ÉCOLE japonaise. Heikin-Ashi = « pace moyen des prix » ; cadrage conceptuel : ce n'est pas le prix brut mais une moyenne.
*Catégorie : indicateurs_tendance*

---

### D2013 — Usage : tendances, points de retournement, figures classiques
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « Heikin-Ashi candlesticks are not used like regular candlesticks. You won't find dozens of bullish or bearish reversal patterns consisting of one to three candlesticks. Instead... identify trending periods, potential reversal points, and classic chart patterns. »
**TRADEX-AI C1** : Ne pas appliquer les patterns 1-3 bougies classiques ; usage = identifier périodes de tendance, retournements potentiels, figures classiques.
*Catégorie : indicateurs_tendance*

---

### D2014 — Formule HA-Close
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_01) : « HA-Close = (Open(0) + High(0) + Low(0) + Close(0)) / 4 »
**TRADEX-AI C1** : Clôture HA = moyenne O/H/L/C de la période courante. Implémentable directement sur les données NT8.
*Catégorie : indicateurs_tendance*

---

### D2015 — Formule HA-Open
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « HA-Open = (HA-Open(-1) + HA-Close(-1)) / 2 »
**TRADEX-AI C1** : Ouverture HA = moyenne (ouverture HA + clôture HA) de la période précédente. Dépendance récursive sur la bougie HA antérieure.
*Catégorie : indicateurs_tendance*

---

### D2016 — Formules HA-High et HA-Low
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « HA-High = Maximum of the High(0), HA-Open(0) or HA-Close(0)... HA-Low = Minimum of the Low(0), HA-Open(0) or HA-Close(0) »
**TRADEX-AI C1** : Haut HA = max(High, HA-Open, HA-Close) ; Bas HA = min(Low, HA-Open, HA-Close). Complète le jeu de 4 formules implémentables.
*Catégorie : indicateurs_tendance*

---

### D2017 — Initialisation : dilemme « poule/œuf » et dissipation
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_02) : « there's a chicken and egg dilemma... The first Heikin-Ashi close equals (O+H+L+C)/4. The first Heikin-Ashi open equals (O+C)/2... the effects will dissipate over time (usually seven to 10 periods). »
**TRADEX-AI C1** : Garde-fou implémentation : la 1re bougie HA est artificielle ; effet de bord dissipé après ~7-10 périodes. Démarrer le calcul avant la fenêtre affichée.
*Catégorie : indicateurs_tendance*

---

### D2018 — StockCharts démarre le calcul avant la 1re date affichée
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « StockCharts.com starts its Heikin-Ashi calculations before the first price date, which is visible on each chart. Therefore, the effects of this first calculation will have already dissipated. »
**TRADEX-AI C1** : 🟡 CONVENTION StockCharts (warm-up hors fenêtre). Pour TRADEX-AI : prévoir un buffer de données antérieures avant la zone analysée.
*Catégorie : configuration*

---

### D2019 — Lecture : creux/pleins selon HA-close vs HA-open
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « A Heikin-Ashi candlestick is hollow when the HA-close is above the HA-open; conversely... filled when the HA-close is below the HA-open. »
**TRADEX-AI C1** : Bougie creuse = HA-close > HA-open (haussier) ; bougie pleine = HA-close < HA-open (baissier).
*Catégorie : indicateurs_tendance*

---

### D2020 — Longue bougie creuse = forte pression acheteuse, absence d'ombre basse
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « A long hollow Heikin-Ashi candlestick shows strong buying pressure over two days. The absence of a lower shadow also reflects strength. »
**TRADEX-AI C1** : Longue bougie creuse sans ombre basse = pression acheteuse forte sur 2 jours. Signal de force haussière.
*Catégorie : signal*

---

### D2021 — Longue bougie pleine = forte pression vendeuse, absence d'ombre haute
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « A long, filled Heikin-Ashi candlestick shows strong selling pressure over two days. The absence of an upper shadow also reflects selling pressure. »
**TRADEX-AI C1** : Longue bougie pleine sans ombre haute = pression vendeuse forte sur 2 jours. Signal de force baissière.
*Catégorie : signal*

---

### D2022 — Petites bougies / longues ombres = indécision
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_03) : « Small Heikin-Ashi candlesticks or those with long upper and lower shadows show indecision over the last two days. This often occurs when one candlestick is filled, and the other is hollow. »
**TRADEX-AI C1** : Petites bougies HA ou longues ombres haut+bas = indécision (souvent une pleine + une creuse). Zone de prudence avant signal.
*Catégorie : signal*

---

### D2023 — Tendances marquées par absence d'ombre directionnelle
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « strong decline marked by a series of Heikin-Ashi candlesticks without upper shadows... strong advance marked by a series of Heikin-Ashi candlesticks without lower shadows. »
**TRADEX-AI C1** : Série de bougies sans ombre haute = déclin fort ; série sans ombre basse = avance forte. Détection de tendance forte exploitable dans la grille /10.
*Catégorie : indicateurs_tendance*

---

### D2024 — Doji / spinning top HA = indécision, pas signal immédiat
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_04) : « Heikin-Ashi doji and spinning tops can be used to foreshadow reversals... a doji or spinning top in a downtrend should not immediately be considered bullish. It shows indecision within the downtrend. »
**TRADEX-AI C1** : 🔵 ÉCOLE chandeliers. Doji/spinning top HA = indécision, jamais signal de retournement immédiat. Garde-fou anti-faux signal.
*Catégorie : signal*

---

### D2025 — Confirmation obligatoire par cassure d'un niveau
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_05) : « You need a confirmation of a directional change (trend reversal). For example, when you spot a doji or spinning top in a downtrend, set a resistance level to base a trend reversal. »
**TRADEX-AI C1** : Le retournement n'est validé que par cassure d'un niveau (résistance fixée après doji en downtrend / support après doji en uptrend). Condition d'entrée niveau 2/3 du moteur.
*Catégorie : gestion_risque_entree*

---

### D2026 — Les signaux échouent : exemple CAT (breakout failed)
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « CAT broke this resistance level a few days later, but the breakout failed—a reminder that not all signals are perfect... A spinning top formed during this downtrend (4), but there was no upside follow-through or reversal. »
**TRADEX-AI C1** : 🔴 garde-fou réalisme : même confirmés, certains breakouts échouent (cas CAT). Ne pas surpondérer un signal HA isolé ; rester en mode Manuel.
*Catégorie : gestion_risque_entree*

---

### D2027 — HA tend mieux : séries de bougies de même type
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_06) : « In contrast to normal candlesticks, Heikin-Ashi Candlesticks are more likely to trend with strings of consecutive filled candlesticks and hollow (white) candlesticks. »
**TRADEX-AI C1** : HA produit des séquences plus « propres » (suites de pleines / suites de creuses), facilitant la lecture de tendance vs chandeliers bruts.
*Catégorie : indicateurs_tendance*

---

### D2028 — Figures classiques applicables sur HA (wedge, triangle, channel)
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_07) : « Classic chart patterns and trend lines can also be used on Heikin-Ashi charts... formed a falling wedge... a triangle consolidation... a falling channel formed as the stock retraced around 61.80% of the prior decline. »
**TRADEX-AI C1** : Wedges, triangles, channels et retracements (ex. 61,8 %) restent valides sur HA. Compatible avec l'analyse de figures de TRADEX-AI.
*Catégorie : structure_marche*

---

### D2029 — Versatilité : tous outils d'AT applicables sur HA
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md) : « all aspects of classical technical analysis can be applied to these charts. Chartists can use Heikin-Ashi Candlesticks to identify support and resistance, draw trend lines or measure retracements. Volume indicators and momentum oscillators also work well. »
**TRADEX-AI C1** : Support/résistance, trendlines, retracements, indicateurs de volume et oscillateurs de momentum fonctionnent sur HA. Couche d'affichage compatible multi-indicateurs.
*Catégorie : indicateurs_tendance*

---

### D2030 — Convention couleurs SharpCharts (creux/plein + rouge/noir)
🟢 **FAIT VÉRIFIÉ** (Source : heikin_ashi_candlesticks.md, image_08, image_09) : « a red-filled candlestick means the close was below the open (filled) and the close was lower than the prior close (red). A black hollow candlestick means the close was above the open (hollow), and the close was higher than the prior close (black). »
**TRADEX-AI C1** : 🟡 CONVENTION StockCharts/SharpCharts (double codage : creux/plein = open vs close ; rouge/noir = vs clôture précédente). À normaliser côté UI TRADEX-AI.
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2011 → D2030 (20 décisions) |
| Cercles couverts | C1 (structure prix / type de chandelier) |
| Catégories | indicateurs_tendance, signal, gestion_risque_entree, structure_marche, configuration |
| Images certifiées | 9/9 |
| Formules implémentables | HA-Close, HA-Open, HA-High, HA-Low (D2014-D2016) + init (D2017) |
| Lien Belkhayate | NON CONCERNÉ (type de chandelier générique ; pourrait servir d'affichage lissé mais aucune référence Belkhayate) |
| Cas à vérifier | D2026 = 🔴 réalisme (signaux peuvent échouer) → renforce le mode Manuel. D2018/D2030 = 🟡 conventions StockCharts (warm-up, couleurs). D2012/D2024 = 🔵 école japonaise. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, attend OK utilisateur avant fusion KB.
