# Extraction StockCharts — Gap Trading Strategies
**Source :** `bundles/stockcharts/gap_trading_strategies.md` (HTTP 200 · ~17 211 car.) + 4 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D1871 → D1890 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/gap-trading-strategies
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Cisco Systems, Inc. (CSCO) Gap example chart from StockCharts.com | What is a Gap? | CERTIFIE (accord .md + HTML) |
| image_02.png | Amazon.com, Inc. (AMZN) Gap example chart from StockCharts.com | What is a Gap? | CERTIFIE (accord .md + HTML) |
| image_03.png | EarthLink, Inc. (ELNK) Gap example chart from StockCharts.com | What is a Gap? | CERTIFIE (accord .md + HTML) |
| image_04.png | Offshore Logistics, Inc. (OLG) Gap example chart from StockCharts.com | What is a Gap? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1871 — Définition du gap trading
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « Gap trading is a strategy that exploits price differences between the closing price of one day and the opening of the next. These gaps can arise from news or financial events. »
**TRADEX-AI C1** : le gap trading exploite l'écart clôture J / ouverture J+1 ; gaps souvent issus de news/événements (lien C6 géopolitique/news).
*Catégorie : timing*
---

### D1872 — Définition du gap et limite des classifications classiques
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « A gap is a change in price levels between the close and open of two consecutive days. Although most... define... Common, Breakaway, Continuation and Exhaustion, those labels are applied after the chart pattern is established... they offer little guidance for trading. »
**TRADEX-AI C1** : les 4 types classiques (Common/Breakaway/Continuation/Exhaustion) sont rétrospectifs et peu opérationnels pour le trading temps réel.
*Catégorie : structure_marche*
---

### D1873 — Full Gap Up (définition opérationnelle)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md, image_01) : « A Full Gap Up occurs when the opening price is greater than yesterday's high price. »
**TRADEX-AI C1** : Full Gap Up = ouverture > plus haut de la veille. Condition détectable mécaniquement à l'open.
*Catégorie : structure_marche*
---

### D1874 — Full Gap Down (définition opérationnelle)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md, image_02) : « A Full Gap Down occurs when the opening price is less than yesterday's low. »
**TRADEX-AI C1** : Full Gap Down = ouverture < plus bas de la veille.
*Catégorie : structure_marche*
---

### D1875 — Partial Gap Up et Partial Gap Down (définitions)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md, image_03) : « A Partial Gap Up occurs when today's opening price is higher than yesterday's close, but not higher than yesterday's high. » + (image_04) « A Partial Gap Down occurs when the opening price is below yesterday's close, but not below yesterday's low. »
**TRADEX-AI C1** : Partial Gap Up = open entre clôture et plus haut veille ; Partial Gap Down = open entre clôture et plus bas veille.
*Catégorie : structure_marche*
---

### D1876 — Quatre types de gaps × long/short = huit stratégies
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « Each of the four gap types has a long and short trading signal, defining the eight gap trading strategies. »
**TRADEX-AI C1** : 4 types de gap × 2 sens = 8 stratégies primaires.
*Catégorie : signal*
---

### D1877 — Règle d'attente : 1 heure après l'ouverture
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « The basic tenet of gap trading is to allow one hour after the market opens for the stock price to establish its range. »
**TRADEX-AI C1** : principe de base = attendre 1 heure post-ouverture pour que le range s'établisse (revisite chart 1-min après 10:30 AM ET).
*Catégorie : timing*
---

### D1878 — Trailing stops asymétriques : 8% long / 4% short
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « Once a position is entered, you calculate and set an 8% trailing stop to exit a long position, and a 4% trailing stop to exit a short position. »
**TRADEX-AI C1** : sortie par trailing stop = 8% (long) / 4% (short) ; valeurs par défaut de la méthode.
*Catégorie : gestion_risque_entree*
---

### D1879 — Mécanique du trailing stop long (exemple)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « You buy a stock at $100. You set the exit at no more than 8% below that, or $92. If the price rises to $120, you raise the stop to $110.375... The stop keeps rising as long as the stock price rises. »
**TRADEX-AI C1** : le trailing stop long suit la hausse du prix et se déclenche au retournement.
*Catégorie : gestion_risque_entree*
---

### D1880 — Mécanique du Buy-to-Cover short (exemple)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « You short a stock at $100. You set the Buy-to-Cover at $104 so that a trend reversal of 4% would force you to exit... If the price drops to $90, you recalculate the stop at 4% above that number, or $93. »
**TRADEX-AI C1** : le Buy-to-Cover short suit la baisse du prix à 4% au-dessus du plus bas.
*Catégorie : gestion_risque_entree*
---

### D1881 — Full Gap Up: Long (déclencheur d'entrée)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « If a stock's opening price is greater than yesterday's high, revisit the 1-minute chart after 10:30 AM and set a long (buy) stop two ticks above the high achieved in the first hour of trading. »
**TRADEX-AI C1** : Full Gap Up Long = buy-stop 2 ticks au-dessus du plus haut de la 1re heure.
*Catégorie : signal*
---

### D1882 — Full Gap Up: Short (déclencheur d'entrée)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « If the stock gaps up, but there is insufficient buying pressure to sustain the rise... set a short stop equal to two ticks below the low achieved in the first hour of trading. »
**TRADEX-AI C1** : Full Gap Up Short = short-stop 2 ticks sous le plus bas de la 1re heure (pression acheteuse insuffisante).
*Catégorie : signal*
---

### D1883 — Full Gap Down: Long et notion de « Dead Cat Bounce »
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « A stock whose price opens in a full gap down, then begins to climb immediately, is known as a "Dead Cat Bounce." If a stock's opening price is less than yesterday's low, set a long stop equal to two ticks more than yesterday's low. »
**TRADEX-AI C1** : Full Gap Down Long = buy-stop 2 ticks au-dessus du plus bas de la veille ; remontée immédiate = "Dead Cat Bounce" (prudence).
*Catégorie : signal*
---

### D1884 — Full Gap Down: Short (déclencheur d'entrée)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « If a stock's opening price is less than yesterday's low, revisit the 1-minute chart after 10:30 AM and set a short stop equal to two ticks below the low achieved in the first hour of trading. »
**TRADEX-AI C1** : Full Gap Down Short = short-stop 2 ticks sous le plus bas de la 1re heure.
*Catégorie : signal*
---

### D1885 — Full vs Partial : risque, gain et trailing stop resserré
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « Full gapping stocks generally trend farther in one direction than stocks which only partially gap... Entering a trade for a partially gapping stock generally calls for either greater attention or closer trailing stops of 5-6%. »
**TRADEX-AI C1** : full gaps tendent davantage (plus de potentiel) ; partial gaps → attention accrue, trailing stop 5-6%.
*Catégorie : gestion_risque_entree*
---

### D1886 — Stratégies Partial Gap (Up/Down, Long/Short)
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « The process for a long entry is the same as for Full Gaps... sets a long (buy) stop two ticks above the high achieved in the first hour... the short trade process... sets a short stop two ticks below the low achieved in the first hour. »
**TRADEX-AI C1** : Partial Gap = mêmes déclencheurs que Full (buy-stop 2 ticks > plus haut 1re heure / short-stop 2 ticks < plus bas 1re heure).
*Catégorie : signal*
---

### D1887 — Sécurité partial gap : attendre cassure du plus haut/bas précédent si volume insuffisant
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « If the volume requirement is not met, the safest way to play a partial gap is to wait until the price breaks the previous high (on a long trade) or low (on a short trade). »
**TRADEX-AI C2** : garde-fou volume — si volume insuffisant sur un partial gap, attendre cassure du plus haut (long) / plus bas (short) avant d'entrer.
*Catégorie : gestion_risque_entree*
---

### D1888 — End-of-Day : le volume confirme la continuation du gap
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « Increases in volume for stocks gapping up or down is a strong indication of continued movement in the same direction of the gap. A gapping stock that crosses above resistance levels provides reliable entry signals... a gap down fails support levels. »
**TRADEX-AI C2** : hausse de volume sur un gap = forte indication de continuation ; cassure de résistance (long) ou rupture de support (short) = signal fiable.
*Catégorie : signal*
---

### D1889 — Modified Trading Method : entrée anticipée + double volume
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « instead of waiting until the price breaks above the high... you enter the trade in the middle of the rebound... the stock should be trading on at least twice the average volume for the last five days... set a long stop equal to the average of the open price and the high price achieved in the first hour. »
**TRADEX-AI C2** : méthode modifiée (avancée) = entrée à mi-rebond (moyenne open/extrême 1re heure), exige volume ≥ 2× moyenne 5 jours et exécution rapide ; stops mentaux.
*Catégorie : gestion_risque_entree*
---

### D1890 — Bonnes pratiques : systèmes définis, paper trading, volume minimal
🟢 **FAIT VÉRIFIÉ** (Source : gap_trading_strategies.md) : « gap trading strategies are rigorously defined trading systems that use specific criteria to enter and exit trades. Trailing stops are defined to limit loss... Paper trading is the simplest method for... your ability to trade gaps... play only those with an average volume above 500,000 shares a day until the gap trading technique is mastered. »
**TRADEX-AI C1** : règles strictes d'entrée/sortie + trailing stops + paper trading ; filtre volume moyen > 500 000 actions/jour avant maîtrise. Aligné garde-fous projet (discipline, gestion du risque).
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Plage | Décisions | Images | Cercles | Catégories dominantes |
|-------|-----------|--------|---------|-----------------------|
| D1871→D1890 | 20 | 4/4 certifiées | C1 (timing/structure gaps), C2 (volume), lien C6 (news) | timing, structure_marche, signal, gestion_risque_entree |

Tags : 🟢 20 · 🔵 0 · 🟡 0 · ⏳ 0 · 🔴 0 · ⚫ 0. Stratégies de gaps = timing d'ouverture ; gaps souvent issus de news (lien C6). Volume central pour confirmation (C2 ATAS). Réserve d'adaptation : règles écrites pour actions (ticks 1/8–1/4 pt, horaires NYSE 10:30 AM ET, seuil 500 k actions) — à transposer aux futures GC·HG·CL·ZW (sessions, tailles de tick, sources de gap overnight différentes). Lien Belkhayate : NON CONCERNÉ. Actifs visés : GC·HG·CL·ZW.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
