# Extraction StockCharts — Percent B Money Flow (%B + MFI)

**Source :** `bundles/stockcharts/percent_b_money_flow.md` (HTTP 200 · ~5 100 car.) + 5 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D3051 → D3070 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/percent-b-money-flow
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - Percent B and Money Flow | Defining the Indicators | CERTIFIÉ |
| image_02.png | Chart 2 - Percent B and Money Flow | Strategy | CERTIFIÉ |
| image_03.png | Chart 3 - Percent B and Money Flow | Trading Examples | CERTIFIÉ |
| image_04.png | Trading Examples | Trading Examples [SECTION-FALLBACK] | CERTIFIÉ |
| image_05.png | Chart 5 - Percent B and Money Flow | Tweaking | CERTIFIÉ |

## DÉCISIONS

### D3051 — Stratégie de John Bollinger : %B + Money Flow Index (MFI)
🔵 **ÉCOLE (Bollinger)** (Source : percent_b_money_flow.md) : « In his book *Bollinger on Bollinger Bands*, John Bollinger introduces a trading strategy using %B and the Money Flow Index (MFI). [...] "the real power of Bollinger Bands becomes evident when they are combined with indicators." »
**TRADEX-AI C1+C2** : stratégie combinant un indicateur de position prix (%B, dérivé des Bollinger Bands) et un indicateur de volume (MFI).
*Catégorie : configuration*

---

### D3052 — Objectif : identifier le début d'une nouvelle tendance par double seuil
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « %B and the Money Flow Index are used to identify the start of a new trend when both reach a bullish or bearish threshold. A surge in %B reflects a strong upthrust in prices, and high MFI readings indicate strong buying volume. »
**TRADEX-AI C1+C2** : logique du signal — convergence de deux seuils (%B et MFI) marque le démarrage d'une nouvelle tendance ; %B = poussée prix, MFI = volume acheteur.
*Catégorie : signal*

---

### D3053 — %B : position du prix dans les Bollinger Bands
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « Percent B (%B) reflects the location of prices within the Bollinger Bands. %B at 0.80 or higher indicates that current prices are near the upper band and in the top 20% of the Bollinger Band range. »
**TRADEX-AI C1** : %B ≥ 0.80 = prix dans les 20 % supérieurs de la bande (proximité bande haute) ⇒ poussée haussière.
*Catégorie : indicateurs_momentum*

---

### D3054 — %B ≤ 0.20 = poussée baissière (20 % inférieurs)
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « %B 0.20 or lower indicates that current prices are near the lower band and in the bottom 20% of the Bollinger Band range. This suggests that prices moved sharply lower with a downside momentum thrust. »
**TRADEX-AI C1** : %B ≤ 0.20 = prix dans les 20 % inférieurs (proximité bande basse) ⇒ poussée baissière.
*Catégorie : indicateurs_momentum*

---

### D3055 — MFI : indicateur volumique de force acheteuse/vendeuse
⚫ **Belkhayate** 🔴 (Source : percent_b_money_flow.md) : « The Money Flow Index (MFI) is a volume-based indicator that measures buying or selling strength. Raw money flow equals the change in typical price multiplied by volume. »
**TRADEX-AI C2 / ⚫ Belkhayate** : le MFI est exactement l'indicateur que la méthode Belkhayate nomme « Énergie » (cf. MEMORY : Belkhayate Énergie = MFI standard). Lien direct avec le module Énergie NON encore codé (stub). 🔴 NON VÉRIFIÉ côté implémentation TRADEX (arbitrage MFI vs proxy ATR non tranché).
*Catégorie : divergence*

---

### D3056 — MFI : prix typique = (H+L+C)/3, RSI appliqué au money flow brut
⚫ **Belkhayate** 🔴 (Source : percent_b_money_flow.md) : « Raw money flow is positive when the typical price rises for the period and negative when the usual price falls. (Typical price = (H + L + C) / 3). The RSI formula is then applied to raw money flow to create an indicator oscillating between zero and one hundred. »
**TRADEX-AI C2 / ⚫ Belkhayate** : formule de calcul du MFI (= Énergie Belkhayate) — prix typique (H+L+C)/3, formule RSI sur money flow brut, oscillateur 0–100. Référence pour coder l'Énergie si MFI standard retenu. 🔴 NON VÉRIFIÉ tant que l'arbitrage TRADEX n'est pas tranché.
*Catégorie : divergence*

---

### D3057 — Règle d'achat : %B > 0.80 ET MFI > 80
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « Buy when %B moves above .80 and the Money Flow Index (MFI) moves above 80. »
**TRADEX-AI C1+C2** : condition d'entrée long déterministe — %B au-dessus de 0.80 ET MFI au-dessus de 80 simultanément.
*Catégorie : signal*

---

### D3058 — Règle de vente : %B < 0.20 ET MFI < 20
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « Sell when %B moves below .20 and the Money Flow Index (MFI) moves below 20. »
**TRADEX-AI C1+C2** : condition d'entrée short déterministe — %B sous 0.20 ET MFI sous 20 simultanément. (NB seuils MFI 20/80 = seuils Énergie Belkhayate ⚫.)
*Catégorie : signal*

---

### D3059 — Bollinger recommande le Parabolic SAR pour les stops
🔵 **ÉCOLE (Bollinger)** (Source : percent_b_money_flow.md) : « Bollinger suggests using the Parabolic SAR for stops. »
**TRADEX-AI C1** : gestion de sortie associée — la stratégie %B+MFI utilise le Parabolic SAR comme mécanisme de stop (lien avec bundle parabolic_sar D3031–3050).
*Catégorie : gestion_risque_entree*

---

### D3060 — Philosophie : vendre la faiblesse, acheter la force
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « The idea behind the system is to sell weakness and buy strength. A strong up thrust shows strength and further strength is then expected. In theory, the buy signal will occur in the middle of the advance. »
**TRADEX-AI C1** : logique momentum (pas mean-reversion) — le signal d'achat est censé survenir au milieu de l'avancée, en pariant sur la continuation.
*Catégorie : signal*

---

### D3061 — Symétrie baissière : sell signal au milieu du déclin
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « A strong down thrust shows weakness and further weakness is expected. This means a sell signal will occur in the middle of the decline. »
**TRADEX-AI C1** : symétrique de D3060 — le signal de vente est censé apparaître au milieu de la baisse.
*Catégorie : signal*

---

### D3062 — Exemple Agilent : sell perdant en déc., buy gagnant modeste en janvier
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md, image_02) : « Agilent with a sell signal in mid-December and a buy signal in early January. Selling short on the mid-December sell signal would have resulted in a loss, while buying on the early January buy signal would have resulted in a modest gain. »
**TRADEX-AI C1** : cas réaliste — les signaux ne sont pas tous gagnants ; le sell de mi-décembre aurait été perdant.
*Catégorie : configuration*

---

### D3063 — Risque principal : échec de continuation de la tendance
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md, image_03) : « Hershey (HSY) [...] A sharp decline followed the mid-October buy signal and resulted in a sharp loss. Failure of the trend to continue is the biggest risk to the system. »
**TRADEX-AI C1** : risque dominant identifié — la non-continuation de la tendance après le signal (faux départ) ; documenté par perte sèche sur HSY.
*Catégorie : gestion_risque_entree*

---

### D3064 — Parabolic SAR stop déclenché puis nouveau signal (RRC)
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « Range Resources (RRC) [...] After triggering a Parabolic SAR stop for a loss, the stock produced another sell signal in mid-December. This one occurred in the middle of the decline as the stock fell further in early January. »
**TRADEX-AI C1** : illustration de la gestion par SAR — premier signal stoppé en perte, second signal mieux positionné (milieu du déclin).
*Catégorie : gestion_risque_entree*

---

### D3065 — Tweaking : risque de rebond à contre-tendance après un mouvement fort
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « there is significant risk of a countertrend bounce after a sharp move. [...] after an up thrust and buy signal, a stock is often short-term overbought and ripe for a pullback already. »
**TRADEX-AI C1** : faiblesse structurelle — après le thrust déclenchant le signal, le titre est souvent déjà suracheté court terme (risque de pullback immédiat).
*Catégorie : gestion_risque_entree*

---

### D3066 — Amélioration 1 : confirmer avec MACD dans le sens de la tendance émergente
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « Chartists should consider using MACD or another momentum oscillator to generate signals in the direction of the emerging trend. After a buy signal, chartists could wait for a pullback and act when MACD crosses above its signal line. »
**TRADEX-AI C3** : filtre additionnel — attendre un pullback puis un croisement MACD au-dessus de sa ligne de signal (long) / en dessous (short) avant d'agir.
*Catégorie : indicateurs_momentum*

---

### D3067 — Amélioration 2 : exiger l'absence de tendance préalable via ADX bas
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « ensure the absence of an existing trend before a signal is triggered. Low Average Directional Index (ADX) readings indicate the absence of a trend or the presence of a weak trend. Buy and sell signals after low ADX readings would indeed suggest that a new trend is emerging. »
**TRADEX-AI C1** : filtre additionnel — un ADX bas avant le signal confirme qu'une *nouvelle* tendance émerge (et non une tendance déjà établie).
*Catégorie : indicateurs_tendance*

---

### D3068 — Exemple PNC : ADX<15, %B<0.20 & MFI<20, puis MACD baissier confirme
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md, image_05) : « PNC Financial Services (PNC). First, [...] ADX moved below 15 [...]. Second, %B plunged below .20 and the Money Flow Index (MFI) fell below 20 [...]. The stock bounced after this signal and MACD turned down in July to trigger a sell signal. Waiting for the MACD signal significantly improved the risk-reward ratio. »
**TRADEX-AI C1+C2+C3** : chaîne complète optimisée — ADX<15 (pas de tendance) → %B<0.20 & MFI<20 (signal) → attente rebond → MACD baissier (confirmation), améliore le ratio risque/rendement.
*Catégorie : signal*

---

### D3069 — Setup haussier symétrique (PNC) : ADX<15, %B>0.80 & MFI>80, MACD haussier
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « The buy signal setup started with ADX moving back below 15 [...]. This was followed by a buy signal as %B surged above .80 and the Money Flow Index exceeded 80. After a pullback in November, MACD triggered a buy signal by moving above its signal line in early December. »
**TRADEX-AI C1+C2+C3** : version haussière de la chaîne — ADX<15 → %B>0.80 & MFI>80 → pullback → MACD croise au-dessus de sa ligne de signal.
*Catégorie : signal*

---

### D3070 — Conclusion : signaler le début d'une tendance sans garantie de continuation
🟢 **FAIT VÉRIFIÉ** (Source : percent_b_money_flow.md) : « %B and MFI combine momentum thrusts and money flow surges to signal the start of a new trend. There is, however, no guarantee that the new trend will extend after the signal. [...] Bollinger invites readers to explore variations and use what he termed "rational analysis" with this strategy. »
**TRADEX-AI C1+C2** : avertissement final — la combinaison %B+MFI signale un *début* de tendance sans garantie de prolongation ; Bollinger encourage l'« analyse rationnelle » et les variantes.
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3051 → D3070 (20) |
| Images certifiées | 5/5 |
| Tags | 🟢 FAIT VÉRIFIÉ (majorité) · 🔵 ÉCOLE Bollinger (D3051, D3059) · ⚫ Belkhayate + 🔴 (D3055, D3056 — MFI=Énergie) |
| Cercle | C1 (Prix/%B) + C2 (Order Flow/MFI volume) ; C3 via MACD (D3066, D3068, D3069) |
| Catégories | configuration, signal, indicateurs_momentum, indicateurs_tendance, divergence, gestion_risque_entree |
| Lien Belkhayate | DIRECT — MFI = « Énergie » Belkhayate, seuils 20/80 (D3055–D3056 ⚫🔴 ; seuils repris D3058) ; pertinent pour le module Énergie NON codé (stub) |
| Stops | Stratégie utilise Parabolic SAR pour les stops (D3059) — pont vers bundle parabolic_sar |
| Actifs | GC·HG·CL·ZW |
| Cas à vérifier | D3055 + D3056 marqués 🔴 : le rattachement MFI→Énergie Belkhayate est documenté (MEMORY) mais l'implémentation TRADEX (MFI standard vs proxy ATR) reste NON TRANCHÉE — à confirmer humain avant fusion |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. NB : MFI = Énergie Belkhayate (Money Flow Index standard, seuils 20/80). L'arbitrage codage Énergie (MFI vs proxy ATR) n'est pas tranché → D3055/D3056 conservés en 🔴 NON VÉRIFIÉ.
