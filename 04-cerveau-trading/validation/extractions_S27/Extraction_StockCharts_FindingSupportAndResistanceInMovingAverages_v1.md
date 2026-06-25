# Extraction StockCharts — Finding Support and Resistance in Moving Averages
**Source :** `bundles/stockcharts/finding_support_and_resistance_in_moving_averages.md` (HTTP 200 · ~9 104 car.) + 2 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1811 → D1830 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/moving-average-trading-strategies/finding-support-and-resistance-in-moving-averages
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Moving averages to find support and resistance levels using StockCharts | The Importance of Support and Resistance | CERTIFIE (accord .md + HTML) |
| image_02.png | Moving averages as support and resistance levels using StockCharts | Example of a Long Trade | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1811 — Rôle double des moyennes mobiles 50 et 200 jours
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md) : « Moving averages—particularly the 50-day and 200-day simple moving averages (SMA)—help traders gauge the direction of a trend and serve as support and resistance. »
**TRADEX-AI C1** : les SMA 50 et 200 servent à la fois de jauge de tendance et de niveaux S/R ; à intégrer comme overlay informatif sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*
---

### D1812 — Le prix tend à rebondir sur les moyennes mobiles
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md, image_01) : « price tends to bounce off the moving averages, making them act like support or resistance levels. »
**TRADEX-AI C1** : un rapprochement du prix vers une SMA 50/200 peut générer un rebond ; zone à surveiller pour entrée.
*Catégorie : structure_marche*
---

### D1813 — Effet « concours de popularité » de crowd
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « The 50-day and 200-day SMAs are popular indicators that can create buying or selling pressure due to crowd mentality. »
**TRADEX-AI C5** : pression acheteuse/vendeuse auto-réalisatrice liée à la popularité des SMA ; facteur sentiment, non causal mécaniquement.
*Catégorie : structure_marche*
---

### D1814 — SMA comme barrières psychologiques de sentiment
🔵 **ÉCOLE** (Source : finding_support_and_resistance_in_moving_averages.md) : « Both SMAs are psychological barriers... A stock above its 50-day SMA (or 200-day SMA...) is seen as strong, while a stock below it is seen as weak. »
**TRADEX-AI C5** : position prix/SMA = proxy de force perçue (au-dessus = fort, en dessous = faible).
*Catégorie : structure_marche*
---

### D1815 — La 200 jours est un benchmark institutionnel
🔵 **ÉCOLE** (Source : finding_support_and_resistance_in_moving_averages.md) : « Large institutional investors use the 200-day SMA to benchmark investments. Their actions can move markets, creating significant price reactions. »
**TRADEX-AI C3** : la SMA 200 comme référence institutionnelle ; les réactions de prix autour d'elle peuvent refléter des flux institutionnels.
*Catégorie : structure_marche*
---

### D1816 — Mesure de force de tendance via combinaison 50/200
🔵 **ÉCOLE** (Source : finding_support_and_resistance_in_moving_averages.md) : « When the 50-day is above the 200-day and in a full-sail position, it indicates a strong uptrend... When both are flattening... a weakening trend. When the 50-day is below the 200-day in full-sail, it's a strong downtrend. »
**TRADEX-AI C1** : grille qualitative de force de tendance selon la position relative et la pente des deux SMA.
*Catégorie : indicateurs_tendance*
---

### D1817 — Étape 1 du long : identifier la tendance haussière
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « The 50-day should be above the 200-day. The stronger the upward curve of both MAs and the wider the distance between them, the better. »
**TRADEX-AI C1** : pré-condition de setup long = SMA50 > SMA200, pentes haussières, écartement large.
*Catégorie : signal*
---

### D1818 — Étape 2 du long : attendre le pullback vers la SMA 50
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « Wait for the price to pull back toward the 50-day SMA. If price breaks below the 50-day, wait for it to pull closer to the 200-day SMA. »
**TRADEX-AI C1** : déclencheur de surveillance = repli du prix vers SMA50 (ou SMA200 si cassure SMA50).
*Catégorie : timing*
---

### D1819 — Étape 3 du long : repérer le rebond avec confirmation
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « Look for a bullish price action signal at or near the 50-day SMA... look at chart patterns and other indicators (such as a Fibonacci retracement or historical support...) to confirm the likely strength of the bounce. »
**TRADEX-AI C1** : exiger un signal de price action + confirmation (Fib, support historique) avant validation du rebond.
*Catégorie : signal*
---

### D1820 — Étape 4 du long : entrer en position selon stratégie
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « You might buy a breakout of the top of the candle that had the bounce... or at the opening of the next day's trading session. Your entry point is a personal choice. »
**TRADEX-AI C1** : entrée long = cassure du haut de la bougie de rebond (variante : entrée immédiate ou ouverture du lendemain).
*Catégorie : gestion_risque_entree*
---

### D1821 — Étape 5 du long : placement du stop loss
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « place your stop a few points below the 50-day or the 200-day... consider levels below the 200-day as your "uncle point" especially if there's strong historical support or a strong Fib retracement below the 200-day SMA. »
**TRADEX-AI C1** : stop quelques points sous SMA50/SMA200 ; "uncle point" sous SMA200 si support historique/Fib proche.
*Catégorie : gestion_risque_entree*
---

### D1822 — Étape 6 du long : cible de profit (R/R 2:1)
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « You may aim for a 2:1 reward-to-risk ratio, a measured move, or a higher resistance level. »
**TRADEX-AI C1** : cible = R/R 2:1, mouvement mesuré, ou prochaine résistance. Compatible règle projet R/R ≥ 1:2.
*Catégorie : gestion_risque_entree*
---

### D1823 — Exemple MSFT : rebonds doubles sur SMA 50 = réversion haussière
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md, image_02) : « When prices bounced off the 50-day SMA twice, this indicated that a potential bullish reversal was underway. Trading a breakout of the swing high might have made for a good "long" entry point. »
**TRADEX-AI C1** : double rebond sur SMA50 + cassure du swing high = pattern d'entrée long illustré.
*Catégorie : signal*
---

### D1824 — Anticipation du Golden Cross comme contexte support
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md) : « We also anticipated a Golden Cross event, which would have supported the technical bullish context. »
**TRADEX-AI C1** : croisement haussier SMA50/SMA200 (Golden Cross) renforce le contexte technique haussier.
*Catégorie : indicateurs_tendance*
---

### D1825 — La SMA 50 agit comme support tant que les achats reviennent
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md) : « the market considered the 50-day simple moving average (SMA) as a support level, as buying occurred every time the price declined towards the line, causing MSFT to bounce off the 50-day SMA. »
**TRADEX-AI C1** : SMA50 reste un support actif tant que la demande réapparaît à son contact.
*Catégorie : structure_marche*
---

### D1826 — Cassure du swing low + clôture sous SMA 50 = fin de tendance court/moyen terme
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md) : « MSFT prices broke below the highest swing low. In addition to closing below the 50-day SMA, this signaled an end to the short- to intermediate-term uptrend. »
**TRADEX-AI C1** : signal de fin de tendance = cassure du plus haut swing low ET clôture sous SMA50.
*Catégorie : signal*
---

### D1827 — La SMA 200 décide de la tendance long terme
🟢 **FAIT VÉRIFIÉ** (Source : finding_support_and_resistance_in_moving_averages.md) : « if the price closes below the 200-day SMA, it could end the longer-term uptrend, leading to a sideways market, a reversal, or a resumption of the uptrend if the fundamental context supports it. »
**TRADEX-AI C1** : clôture sous SMA200 = risque de fin de tendance long terme (range, reversal, ou reprise selon fondamentaux).
*Catégorie : signal*
---

### D1828 — Symétrie des règles côté short
🟡 **CONVENTION** (Source : finding_support_and_resistance_in_moving_averages.md) : « These rules also apply to going "short" the market. It's the same rules as above but in reverse. »
**TRADEX-AI C1** : les règles de rebond s'appliquent en miroir pour les positions short (SMA comme résistance).
*Catégorie : signal*
---

### D1829 — Les SMA comme jauges de direction et barrières psychologiques (synthèse)
🔵 **ÉCOLE** (Source : finding_support_and_resistance_in_moving_averages.md) : « Acting as both gauges of trend direction and psychological barriers, these SMAs wield significant influence over market sentiment and action. »
**TRADEX-AI C5** : double fonction confirmée — direction (C1) et sentiment/barrière psychologique (C5).
*Catégorie : indicateurs_tendance*
---

### D1830 — Combiner SMA avec autres outils + gestion du risque (caveat)
🔵 **ÉCOLE** (Source : finding_support_and_resistance_in_moving_averages.md) : « you should combine this knowledge with other tools and indicators and always keep risk management in mind. »
**TRADEX-AI C1** : ne jamais trader la SMA seule ; combiner indicateurs + gestion du risque. Aligné garde-fous projet.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Plage | Décisions | Images | Cercles | Catégories dominantes |
|-------|-----------|--------|---------|-----------------------|
| D1811→D1830 | 20 | 2/2 certifiées | C1 (majoritaire), C3, C5 | indicateurs_tendance, structure_marche, signal, timing, gestion_risque_entree |

Tags : 🟢 8 · 🔵 5 · 🟡 7 · ⏳ 0 · 🔴 0 · ⚫ 0. Lien Belkhayate : NON CONCERNÉ (méthode SMA classique, pas l'analyse pivots/BGC/MFI Belkhayate). Actifs visés : GC·HG·CL·ZW (overlay SMA50/200).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT — attend OK utilisateur avant fusion KB.
