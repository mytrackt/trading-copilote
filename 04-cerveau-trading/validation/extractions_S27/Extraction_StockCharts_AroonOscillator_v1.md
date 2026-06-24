# Extraction StockCharts — Aroon Oscillator
**Source :** `bundles/stockcharts/aroon_oscillator.md` (HTTP 200 · ~6 600 car.) + 6 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D671 → D682 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/aroon-oscillator
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Aroon Oscillator - Chart 1 | How To Calculate the Aroon Oscillator | CERTIFIE (accord .md + HTML) |
| image_02.png | Aroon Oscillator - Table 1 | How To Calculate the Aroon Oscillator | CERTIFIE (accord .md + HTML) |
| image_03.png | Aroon Oscillator - Chart 2 | General Trend Bias | CERTIFIE (accord .md + HTML) |
| image_04.png | Aroon Oscillator - Chart 3 | Strong Trend Bias | CERTIFIE (accord .md + HTML) |
| image_05.png | Aroon Oscillator - SharpCharts | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_06.png | Aroon Oscillator - SharpCharts | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D671 — Définition : différence Aroon-Up moins Aroon-Down
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md) : « The Aroon Oscillator is the difference between Aroon-Up and Aroon-Down. […] This indicator fluctuates between -100 and +100 with zero as the middle line. An upward trend bias is present when the oscillator is positive, while a downward trend bias exists when the oscillator is negative. »
**TRADEX-AI C1** : Indicateur de tendance borné [-100, +100], ligne médiane zéro. Biais haussier si > 0, baissier si < 0 — exploitable comme filtre directionnel sur GC·HG·CL·ZW.
*Catégorie : indicateurs_tendance*

---

### D672 — Formule de calcul (paramètre par défaut 25)
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md, image_01) : « Aroon-Up = 100 x (25 - Days Since 25-day High)/25 ; Aroon-Down = 100 x (25 - Days Since 25-day Low)/25 ; Aroon Oscillator = Aroon-Up - Aroon-Down. The SharpCharts default parameter is 25 ». Aroon-Up/Down mesurent le nombre de jours depuis un plus-haut/plus-bas sur x jours, exprimés en % entre 0 et 100.
**TRADEX-AI C1** : Formule déterministe codable telle quelle. Période par défaut 25. Aucune dépendance propriétaire — réplicable côté Python pour les actifs trading.
*Catégorie : configuration*

---

### D673 — Bornes extrêmes ±100 exigent un mouvement de prix fort
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md, image_02) : « the oscillator equals +100 when Aroon-Up equals 100 and Aroon-Down equals 0. Similarly, the Aroon Oscillator equals -100 when Aroon-Up is 0, and Aroon-Down is 100. It requires some strong upward price movement for the Aroon Oscillator to reach +100. […] strong downward price movement is required for the oscillator to reach -100. »
**TRADEX-AI C1** : Atteindre ±100 = signal de force directionnelle marquée (nouveau plus-haut ET aucun plus-bas récent, ou inverse). Utilisable comme jauge d'intensité de tendance.
*Catégorie : indicateurs_tendance*

---

### D674 — Combinaisons Up/Down produisant un même niveau d'oscillateur
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md, image_02) : « An Aroon Oscillator that equals +40 requires Aroon-Up to be at least 40, which means Aroon-Down would be 0. A positive 40 could occur from an array of Aroon-Up and Aroon-Down combinations (40-0, 44-4, 48-8, 60-20, 72-32, 80-40 or 100-60). »
**TRADEX-AI C1** : Un même niveau d'oscillateur recouvre plusieurs états Up/Down. Pour une lecture fine, conserver Aroon-Up et Aroon-Down séparément en plus de l'oscillateur dans l'état moteur.
*Catégorie : configuration*

---

### D675 — Interprétation : nouveaux plus-hauts vs nouveaux plus-bas récents
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md) : « A reading above zero means that Aroon-Up is greater than Aroon-Down, which implies that prices are making new highs more recently than new lows. Conversely, readings below zero indicate that Aroon-Down is greater than Aroon-Up. […] Time and price favor an uptrend when the indicator is positive and a downtrend when the indicator is negative. »
**TRADEX-AI C1** : Le signe de l'oscillateur traduit la récence relative des plus-hauts/plus-bas. Sert de lecture directionnelle simple, binaire, peu ambiguë.
*Catégorie : signal*

---

### D676 — Seuils ±50 pour qualifier un mouvement fort
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md) : « A positive or negative threshold can be used to define the strength of the trend. For example, a surge above +50 would reflect a strong upside move, while a plunge below -50 would indicate a strong downside move. »
**TRADEX-AI C3** : Seuils ±50 utilisables comme filtre de confirmation (force du mouvement) avant validation d'un signal directionnel. Paramétrable.
*Catégorie : signal*

---

### D677 — Sensibilité dépend de la période (25 vs 75)
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md, image_03) : « 25-day Aroon was much more sensitive than 75-day Aroon. […] 25-day Aroon crossed the zero line over eight times in eighteen months. 75-day Aroon crossed the zero line just four times. […] Short-term traders would clearly opt for a 25-day Aroon or shorter, while position traders looking for 2-4 month moves would opt for 75-day Aroon. »
**TRADEX-AI C1** : Choix de période = arbitrage sensibilité/bruit. Court terme → 25 ou moins ; position → 75. À aligner sur les timeframes Belkhayate (Standard 15min / Range Bar) lors du paramétrage moteur.
*Catégorie : configuration*

---

### D678 — Indicateur retardé (lag), suiveur de tendance, pas un timer de tops/bottoms
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md, image_03) : « the Aroon Oscillator is not immune to lag as the oscillator turns positive or negative after prices have already moved. The longer the parameter setting, the more the lag. Do not expect to pick bottoms or tops with positive or negative crossovers. As more of a trend following indicator, the Aroon Oscillator identifies moves that may be strong enough to signal the start of a sustained trend, though not all trends extend. »
**TRADEX-AI C1** : À traiter comme indicateur de suivi de tendance retardé, jamais comme déclencheur de retournement. Ne pas l'utiliser pour viser des extrêmes de prix.
*Catégorie : indicateurs_tendance*

---

### D679 — Biais de tendance fort : seuils ±90 (école Chande)
🔵 **ÉCOLE (Chande)** (Source : aroon_oscillator.md, image_04) : « the bullish threshold could be set at +90 and the bearish threshold at -90. A +90 would indicate that Aroon-Up is between 90 and 100, while Aroon-Down is between 0 and 10. […] A move above +90 is considered bullish until negated with a move below -90. This level is deep enough to absorb most pullbacks within an uptrend. […] a move below -90 is deemed strong enough to signal the start of an extended decline. »
**TRADEX-AI C3** : Régime ±90 = état "grande tendance" persistant (absorbe les pullbacks). Utilisable comme filtre macro-directionnel : ne prendre que les signaux dans le sens du régime.
*Catégorie : signal*

---

### D680 — Trader dans le sens de la grande tendance (filtre directionnel ±90)
🔵 **ÉCOLE (Chande)** (Source : aroon_oscillator.md, image_04) : « These 90/90 signals can be used to establish the big trend and then trade in the direction of that trend. […] chartists can focus exclusively on bullish signals when the big trend is up (Aroon > +90). Conversely, chartists can focus exclusively on bearish signals when the big trend is down (Aroon < -90). Chartists can even tweak the bullish and bearish thresholds, though they are advised not to over-fit. »
**TRADEX-AI C3** : Logique de filtre régime : Aroon Osc > +90 → n'autoriser que longs ; < -90 → n'autoriser que shorts. Avertissement explicite contre le sur-ajustement des seuils.
*Catégorie : signal*

---

### D681 — Limite : pas conçu pour les divergences ; combiner avec d'autres outils
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md) : « It is tempting to look for bullish and bearish divergences, but the indicator was not designed for traditional oscillator signals. As with all technical indicators, the Aroon Oscillator should be used in conjunction with other aspects of technical analysis, such as chart pattern analysis or momentum indicators. »
**TRADEX-AI C3** : Ne pas implémenter de détection de divergence sur l'Aroon Oscillator. À utiliser uniquement combiné (patterns, momentum) — cohérent avec la grille multi-cercles TRADEX.
*Catégorie : signal*

---

### D682 — Scans : croisements de la ligne zéro avec volume confirmé
🟢 **FAIT VÉRIFIÉ** (Source : aroon_oscillator.md) : Scan haussier « [Daily Aroon Osc(25) crosses 0] AND [Daily Volume > Daily SMA(50,Daily Volume)] » ; scan baissier « [0 crosses Daily Aroon Osc(25)] AND [Daily Volume > Daily SMA(50,Daily Volume)] ». Filtres : type stock, US, SMA(20) volume > 100000, SMA(60) close > 20.
**TRADEX-AI C3** : Le croisement zéro de l'Aroon Osc(25) confirmé par un volume > SMA(50) volume constitue un signal d'entrée/sortie testable. La confirmation par volume rejoint le cercle order-flow (C2). Seuils de scan = univers actions US, à adapter aux futures GC·HG·CL·ZW.
*Catégorie : signal*

---

## SYNTHÈSE

| # | Décision | Tag | Cercle | Catégorie |
|---|----------|-----|--------|-----------|
| D671 | Définition Up-Down, bornes ±100, ligne zéro | 🟢 | C1 | indicateurs_tendance |
| D672 | Formule calcul, période défaut 25 | 🟢 | C1 | configuration |
| D673 | Extrêmes ±100 = mouvement fort | 🟢 | C1 | indicateurs_tendance |
| D674 | Combinaisons Up/Down d'un même niveau | 🟢 | C1 | configuration |
| D675 | Interprétation plus-hauts/plus-bas récents | 🟢 | C1 | signal |
| D676 | Seuils ±50 force du mouvement | 🟢 | C3 | signal |
| D677 | Sensibilité 25 vs 75 | 🟢 | C1 | configuration |
| D678 | Lag, suiveur de tendance, pas de tops/bottoms | 🟢 | C1 | indicateurs_tendance |
| D679 | Régime fort ±90 | 🔵 ÉCOLE (Chande) | C3 | signal |
| D680 | Filtre directionnel ±90 grande tendance | 🔵 ÉCOLE (Chande) | C3 | signal |
| D681 | Pas de divergence, combiner avec autres outils | 🟢 | C3 | signal |
| D682 | Scans croisement zéro + volume | 🟢 | C3 | signal |

**Total : 12 décisions (D671→D682) · 10 🟢 littéral · 2 🔵 ÉCOLE (Chande) · 6/6 images certifiées · Belkhayate NON CONCERNÉ (indicateur tiers).**

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, non fusionnée dans KNOWLEDGE_BASE_MASTER.json.
