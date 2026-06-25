# Extraction StockCharts — Ichimoku Cloud Trading Strategies

**Source :** `bundles/stockcharts/ichimoku_cloud_trading_strategies.md` (HTTP 200 · ~7 000 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende) · 6/6 certifiées
**Décisions :** D2171 → D2186 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/ichimoku-cloud-trading-strategies
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

🔵 **PERTINENCE FUTURES : OUI (C1) — ÉCOLE Ichimoku (système standalone)** — stratégie de trading complète à 3 critères (biais nuage + pullback Base Line + déclencheur Conversion Line) transposable aux futures (GC/HG/CL/ZW), périodes à recalibrer. Méthode externe (école Ichimoku) → tag 🔵 ÉCOLE. Belkhayate NON CONCERNÉ (⚫). Complète l'extraction Ichimoku Cloud (D2151–D2170) côté exécution/stops.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Décision |
|-------|-------|---------|----------|
| image_01.png | Chart 1 - Ichimoku Trading Strategy | What Are the Ichimoku Cloud's Five Components? | D2172 |
| image_02.png | Chart 2 - Ichimoku Trading Strategy | Trading Strategy Based on Ichimoku Cloud | D2174 |
| image_03.png | Chart 3 - Ichimoku Trading Strategy | Trading Strategy Based on Ichimoku Cloud | D2175 |
| image_04.png | Chart 4 - Ichimoku Trading Strategy | Trading Example | D2177 |
| image_05.png | Chart 5 - Ichimoku Trading Strategy | Trading Example | D2178 |
| image_06.png | Chart 6 - Ichimoku Trading Strategy | Adjusting | D2181 |

## DÉCISIONS

### D2171 — Ichimoku = système de trading standalone
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « Even though the name implies one cloud, the Ichimoku Cloud is really a set of indicators designed as a standalone trading system. These indicators can identify support and resistance, determine trend direction, and generate trading signals. »
**TRADEX-AI C1** : Ichimoku conçu comme système autonome (S/R + tendance + signaux). Pour TRADEX, intégré comme brique de tendance/timing dans le score multi-cercles, pas comme système isolé.
*Catégorie : indicateurs_tendance*

---

### D2172 — Rappel des 5 composantes
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_01) : Conversion Line (9h+9b)/2 ; Base Line (26h+26b)/2 ; Leading Span A = (Conversion+Base)/2, tracée +26 ; Leading Span B (52h+52b)/2, tracée +26 ; Chikou Span = clôture courante tracée 26 jours en arrière (montre la pression acheteuse, S/R, retournements).
**TRADEX-AI C1** : confirmation des 5 formules (cohérent avec D2154–D2156 de la page Ichimoku Cloud). Le Chikou Span sert à juger la pression vs les prix passés.
*Catégorie : indicateurs_tendance*

---

### D2173 — Logique générale de la stratégie
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « Chartists use the actual cloud to identify the overall trend and establish a trading bias. Once a bias is established, chartists wait for a correction when prices cross the Base Line (red line). An actual signal triggers when prices cross the Conversion Line (blue line) to signal an end to the correction. »
**TRADEX-AI C1** : séquence en 3 temps — (1) biais par le nuage, (2) attendre une correction (prix franchit la Base Line), (3) signal quand le prix franchit la Conversion Line. Logique d'entrée sur pullback codable.
*Catégorie : signal*

---

### D2174 — Les 3 critères d'achat (buy signal recap)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_02) : Buy — (1) Price is above the lowest line of the cloud (bullish bias), (2) Price moves below the Base Line (pullback), (3) Price moves above the Conversion Line (upturn). « There is a pecking order to the process. »
**TRADEX-AI C1** : grille d'achat à 3 conditions ORDONNÉES (ordre obligatoire : biais → pullback → upturn). Améliore le ratio risque/rendement en entrant après repli. Directement codable comme machine à états.
*Catégorie : signal*

---

### D2175 — Les 3 critères de vente (sell signal recap)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_03) : Sell — (1) Price is below the highest line of the cloud (bearish bias), (2) Price moves above the Base Line (bounce), (3) Price moves below the Conversion Line (downturn).
**TRADEX-AI C1** : grille de vente symétrique à 3 conditions ordonnées (biais baissier → bounce → downturn). Machine à états miroir de D2174.
*Catégorie : signal*

---

### D2176 — Ordre séquentiel obligatoire des critères
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « the three criteria will not be met in just one day. (...) First, the trend is bullish as defined by the cloud. Second, the stock pulls back with a move below the Base Line. Third, the stock turns back up with a move above the Conversion Line. »
**TRADEX-AI C1** : garde-fou de séquencement — les 3 critères s'enchaînent dans le temps (jamais simultanés). Implémentation = état persistant (mémoriser le pullback avant de valider l'upturn).
*Catégorie : timing*

---

### D2177 — Whipsaws quand le prix ne tient pas le nuage
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_04) : exemple Sandisk (SNDK) — « the trading bias shifted three times (...). Signals 1 and 2 resulted in whipsaws because the SNDK did not hold the cloud. The trading bias can change often for volatile stocks because the cloud is based on lagging indicators. »
**TRADEX-AI C1** : avertissement — sur actifs volatils, biais qui change souvent → whipsaws (nuage = indicateur retardé). Risque à pondérer ; pertinent pour CL/HG (volatils).
*Catégorie : gestion_risque_entree*

---

### D2178 — Une tendance forte est requise pour tenir le biais
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_05) : « A relatively strong trend is required to sustain a trading bias. Prices remain above the lower cloud line during a strong uptrend and below the upper cloud line during a strong downtrend. (...) Signal 3 resulted in a whipsaw, but Signal 4 preceded a sharp decline. »
**TRADEX-AI C1** : condition de validité — la stratégie fonctionne en tendance forte, pas en range. Filtre de régime de marché à appliquer avant d'activer les signaux Ichimoku.
*Catégorie : gestion_risque_entree*

---

### D2179 — Exemple de retournement haussier et signaux de pullback
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « After a sharp reversal (...) the trading bias turned bullish with the upside breakout (...). The first pullback produced a buy signal (5) with a dip below the Base Line (red) and a subsequent move above the Conversion Line (blue). There were two more buy signals during the consolidation period (6 & 7). »
**TRADEX-AI C1** : illustration concrète — chaque pullback sous la Base Line suivi d'un retour au-dessus de la Conversion Line = signal d'achat répétable en consolidation haussière.
*Catégorie : signal*

---

### D2180 — Confirmer les signaux par le volume
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « Chartists can use volume to confirm signals, especially buy signals. A buy signal with expanding volume would carry more weight than a buy signal on low volume. Expanding volume shows strong interest, which increases the chances of a sustainable advance. »
**TRADEX-AI C1/C2** : confluence volume — un signal d'achat avec volume en expansion pèse davantage. Lien possible avec l'order flow ATAS (C2) comme filtre de confirmation.
*Catégorie : signal*

---

### D2181 — Stops initiaux basés sur le dernier creux/sommet
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md, image_06) : « The low just before a buy signal would be logical for an initial stop-loss after a buy signal. The high just before a sell signal would be logical for an initial stop-loss after a sell signal. »
**TRADEX-AI C1** : règle de stop initial — dernier creux avant buy / dernier sommet avant sell. Niveau de stop déterministe et codable directement à l'entrée.
*Catégorie : gestion_risque_entree*

---

### D2182 — Trailing stop pour verrouiller les profits
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « Once the trade is underway and prices move in a favorable direction, chartists should consider a trailing stop to lock in profits. The example (...) shows Novellus (NVLS) with the Parabolic SAR for trailing stops. »
**TRADEX-AI C1** : gestion en cours de trade — trailing stop (ex. Parabolic SAR) pour sécuriser les gains une fois le trade favorable.
*Catégorie : gestion_risque_entree*

---

### D2183 — Stop volatilité basé sur l'ATR (2 ATR)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « The indicator window shows the Average True Range (ATR), which can be used to set a volatility-type stop. Some traders set stops two ATRs below current prices for long positions and two ATRs above current prices on short positions. »
**TRADEX-AI C1** : règle de stop ATR — 2×ATR sous le prix (long) / au-dessus (short). Stop adaptatif à la volatilité, directement transposable aux futures (recalibrer le multiplicateur si besoin).
*Catégorie : gestion_risque_entree*

---

### D2184 — Rôle de chaque composante dans le système
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « The cloud sets the overall tone and provides a longer perspective on the price trend. The Conversion Line (blue) is a relatively short-term indicator that catches turns early. Catching the turn early will improve the risk-reward ratio for trades. »
**TRADEX-AI C1** : répartition des rôles — nuage = tendance de fond ; Conversion Line = timing précoce des retournements (améliore le R/R). Cohérent avec l'objectif R/R ≥ 1:2 de TRADEX.
*Catégorie : signal*

---

### D2185 — La stratégie n'est qu'un point de départ (garde-fou)
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : « Remember that this article is designed as a starting point for developing a trading system. Use these ideas to augment your trading style, risk-reward preferences, and personal judgments. »
**TRADEX-AI C1** : garde-fou — système à adapter, jamais appliqué en boîte noire. Cohérent avec le mode Manuel (Abdelkrim décide) et l'interdiction du mode Auto par défaut.
*Catégorie : configuration*

---

### D2186 — Scans Ichimoku Buy/Sell Signal
🔵 **ÉCOLE Ichimoku** (Source : ichimoku_cloud_trading_strategies.md) : Buy scan — `close > span b(9,26,52)` ET `span a > span b` ET `close crosses base line(9,26,52)`. Sell scan — `close < span a(9,26,52)` ET `span a < span b` ET `base line(9,26,52) crosses close`. Filtres : sma(20,volume) > 100000, sma(60,close) > 20.
**TRADEX-AI C1** : screening déterministe — biais (Close/Span B + Span A/B) + déclencheur (croisement Close/Base Line). Périodes/filtres = exemples actions US daily, NE PAS coder tels quels ; recalibrer sur les futures.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2171 | Système standalone | 🔵 | C1 | indicateurs_tendance |
| D2172 | Rappel 5 composantes | 🔵 | C1 | indicateurs_tendance |
| D2173 | Logique générale 3 temps | 🔵 | C1 | signal |
| D2174 | 3 critères d'achat | 🔵 | C1 | signal |
| D2175 | 3 critères de vente | 🔵 | C1 | signal |
| D2176 | Ordre séquentiel obligatoire | 🔵 | C1 | timing |
| D2177 | Whipsaws si nuage non tenu | 🔵 | C1 | gestion_risque_entree |
| D2178 | Tendance forte requise | 🔵 | C1 | gestion_risque_entree |
| D2179 | Pullbacks répétés = signaux | 🔵 | C1 | signal |
| D2180 | Confirmer par le volume | 🔵 | C1/C2 | signal |
| D2181 | Stop initial creux/sommet | 🔵 | C1 | gestion_risque_entree |
| D2182 | Trailing stop (SAR) | 🔵 | C1 | gestion_risque_entree |
| D2183 | Stop volatilité 2×ATR | 🔵 | C1 | gestion_risque_entree |
| D2184 | Rôles nuage vs Conversion Line | 🔵 | C1 | signal |
| D2185 | Point de départ, à adapter | 🔵 | C1 | configuration |
| D2186 | Scans Buy/Sell Signal | 🔵 | C1 | signal |

| Élément | Valeur |
|---------|--------|
| Décisions | D2171 → D2186 (16) |
| Images certifiées | 6/6 |
| Cercles | C1 (tendance/signal/risque, dominant) + C2 (volume, D2180) |
| Catégories | indicateurs_tendance · signal · timing · gestion_risque_entree · configuration |
| Actif applicable | GC/HG/CL/ZW (TRADING) + ES — stratégie transposable, périodes 9/26/52 à recalibrer |
| Belkhayate | NON CONCERNÉ (Ichimoku = école externe ⚫) |
| Pertinence futures | OUI (C1) — école Ichimoku, stratégie complète entrée + stops |
| Cas « à vérifier » | (1) Tag 🔵 ÉCOLE (Ichimoku). (2) Critères ORDONNÉS (D2176) : implémenter comme machine à états avec mémoire du pullback, jamais en test simultané. (3) Périodes 9/26/52 + scans (D2186) = défauts/exemples actions US, NE PAS coder tels quels. (4) Stop 2×ATR (D2183) : multiplicateur à valider sur les futures. (5) Filtre régime (D2178) : n'activer qu'en tendance forte — risque de whipsaw sur CL/HG volatils (D2177). |

**Liens Belkhayate :** Aucun lien direct — la stratégie Ichimoku n'appartient PAS à la méthode Belkhayate (⚫). Sinon NON CONCERNÉ.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
