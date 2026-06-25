# Extraction StockCharts — Correlation Coefficient
**Source :** `bundles/stockcharts/correlation_coefficient.md` (HTTP 200 · ~8 600 car.) + 9 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 9/9 certifiées
**Décisions :** D1391 → D1410 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/correlation-coefficient
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section |
|-------|-------|---------|
| image_01.png | Correlation Coefficient - Excel Example | How Correlation Coefficient Is Calculated |
| image_02.png | Correlation Coefficient - Intel | How Correlation Coefficient Is Calculated |
| image_03.png | Correlation Coefficient - Oil and Oil Stocks | Interpreting Correlation Coefficient |
| image_04.png | Correlation Coefficient - Gold and Dollar | Interpreting Correlation Coefficient |
| image_05.png | Correlation Coefficient - Sectors | Diversification: Investing in Non-correlated Securities |
| image_06.png | Correlation Coefficient - Other Assets | Diversification: Investing in Non-correlated Securities |
| image_07.png | Correlation Coefficient - Intel SharpCharts | Using With SharpCharts |
| image_08.png | Correlation Coefficient - SharpCharts | Using With SharpCharts |
| image_09.jpg | Using With StockChartsACP | Using With StockChartsACP [SECTION-FALLBACK] |

## DÉCISIONS

### D1391 — Définition du Correlation Coefficient
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « The Correlation Coefficient is a statistical measure that reflects the correlation between two securities... The Correlation Coefficient is positive when both securities move in the same direction (up or down) and negative when the two securities move in opposite directions. »
**TRADEX-AI C7** : Mesure statistique du lien directionnel entre deux actifs. Brique fondatrice de la matrice de corrélations live 30j (cercle C7 : GC/HG/CL/ZW/ES/VX/MBT/6J).
*Catégorie : structure_marche*
---

### D1392 — Usages : intermarché, secteur-titre, secteur-marché
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « Determining the relationship between two securities is useful for analyzing intermarket relationships, sector-stock relationships and sector-market relationships. This indicator can also help investors diversify by identifying securities with a low or negative correlation to the stock market. »
**TRADEX-AI C7** : Outil dédié à l'analyse intermarché — exactement le rôle de C7 dans TRADEX (corrélations entre actifs trading et références MBT/6J). Sert aussi à identifier des actifs décorrélés (diversification).
*Catégorie : structure_marche*
---

### D1393 — Méthode de calcul (exemple INTC vs QQQ)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_01) : « In this example, we will use Intel (INTC) and the Nasdaq 100 ETF (QQQ)... Using the bottom row, you can now compute the Variance, Covariance, and Correlation Coefficient. »
**TRADEX-AI C7** : Calcul = variance + covariance des deux séries de prix sur N périodes (codable niveau 1, 0$). Méthode statistique classique applicable aux paires d'actifs TRADEX.
*Catégorie : structure_marche*
---

### D1394 — Exemple de forte corrélation positive (+0,95)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_02) : « Intel showed a strong positive correlation (+0.95) with the Nasdaq 100 ETF over the 20-day period. »
**TRADEX-AI C7** : Illustration — un titre tech vs son indice ≈ +0,95 sur 20 jours. Ordre de grandeur de référence pour une corrélation forte.
*Catégorie : structure_marche*
---

### D1395 — Bornes de l'indicateur (-1 à +1)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « The correlation coefficient oscillates between -1 and +1. It is not a momentum oscillator, however. Instead, it moves from periods of positive correlation to periods of negative correlation. »
**TRADEX-AI C7** : Borné [-1, +1]. N'est PAS un oscillateur de momentum (ne pas l'interpréter comme surachat/survente). Mesure un régime de corrélation variable dans le temps.
*Catégorie : structure_marche*
---

### D1396 — Seuil de corrélation positive forte (> +0,50)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_03) : « +1 is considered perfect positive correlation, which is rare. Anything between 0 and +1 indicates that two securities move in the same direction... In general, anything above .50 shows a strong positive correlation. »
**TRADEX-AI C7** : Seuil opérationnel — corrélation > +0,50 = forte corrélation positive. Seuil exploitable pour pondérer les confirmations inter-actifs dans la grille /10.
*Catégorie : structure_marche*
---

### D1397 — Corrélation pétrole / actions pétrolières (exemple)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_03) : « Oil stocks and oil are positively correlated most of the time. The example below shows the Energy SPDR (XLE) with Spot Light Crude ($WTIC)... the 20-day Correlation Coefficient remains largely positive with regular forays above +.75. »
**TRADEX-AI C7** : Pétrole WTI (CL, actif tradé TRADEX) corrélé positivement la plupart du temps aux actions énergie (>+0,75 fréquent). Référence intermarché directe pour CL.
*Catégorie : structure_marche*
---

### D1398 — Seuil de corrélation négative forte (< -0,50)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « -1 is considered perfect negative correlation, which is rare. Anything between 0 and -1 indicates that two securities move in opposite directions... In general, anything below -.50 shows a strong negative correlation. »
**TRADEX-AI C7** : Seuil opérationnel — corrélation < -0,50 = forte corrélation négative. Symétrique du +0,50. Utile pour détecter les actifs antagonistes (hedge / confirmation inverse).
*Catégorie : structure_marche*
---

### D1399 — Corrélation négative Or / Dollar (exemple)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_04) : « Gold and the Dollar are the first two securities that come to mind for a negative correlation. The chart below shows Spot Gold ($GOLD) with the US Dollar Index ($USD)... it is negative the majority of the time. »
**TRADEX-AI C7** : Or (GC, actif tradé) ↔ Dollar Index (DX, actif confirmation) = corrélation négative la majorité du temps. Lien direct avec C4 (macro/DX) et C7. Confirme le rôle du DXY comme proxy inverse pour GC.
*Catégorie : structure_marche*
---

### D1400 — La corrélation varie dans le temps
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_04) : « The degree of positive correlation is likely to vary over time. » et « Although the Correlation Coefficient spends a fair amount of time in positive territory, it is negative the majority of the time. » (Or/Dollar)
**TRADEX-AI C7** : Garde-fou — une corrélation n'est jamais figée ; Or/Dollar passe parfois en positif. Justifie la matrice de corrélation LIVE 30j (recalculée en continu) plutôt qu'une table statique.
*Catégorie : structure_marche*
---

### D1401 — Diversification via actifs décorrélés (secteurs S&P)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_05) : « the nine S&P sectors are mostly positively correlated with the S&P 500. However, some are more positively correlated than others... Technology ETF (XLK) and Consumer Discretionary SPDR (XLY) have a strong positive correlation with the S&P 500. »
**TRADEX-AI C7** : Tous les secteurs ne se valent pas en corrélation au marché. Principe transposable : distinguer les actifs trading qui suivent le marché (ES) de ceux plus indépendants.
*Catégorie : structure_marche*
---

### D1402 — Secteurs défensifs moins corrélés (Staples, Utilities)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_05) : « the correlation coefficient for the Consumer Staples sector dipped below 0.50 a few times and the correlation coefficient for the Utilities sector even dipped below zero twice... Consumer Staples and Utilities are less correlated to the S&P 500. » (exemples sur 50 jours)
**TRADEX-AI C7** : Les secteurs défensifs sont structurellement moins corrélés au marché → exemple de décorrélation utile. Période 50 jours citée pour cette analyse.
*Catégorie : structure_marche*
---

### D1403 — Sortir des actions pour vraie diversification (bonds, or, devises)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_06) : « To truly diversify from stocks, it is often necessary to look outside of the stock market... The 20+ year Bond ETF (TLT)... is negatively correlated with stocks most of the time. »
**TRADEX-AI C7** : Les obligations longues (TLT) sont négativement corrélées aux actions la plupart du temps. Logique transposable aux actifs TRADEX hors-actions (GC, CL, ZW) comme diversificateurs vs ES.
*Catégorie : structure_marche*
---

### D1404 — Or mixte, Yen mixte, Dollar négatif vs actions
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_06) : « Gold (red) moves between periods of positive and negative correlation. On the whole, it has been more positively correlated than negative. The Yen Trust (green) appears to split its time between periods of positive and negative correlation... the US Dollar Fund (UUP) shows a propensity to be negatively correlated with the stock market. » (50 jours)
**TRADEX-AI C7** : Référence intermarché directe TRADEX — Or (GC) corrélation mixte vs actions ; Yen (6J, référence) alterne positif/négatif ; Dollar (DX) tend négatif vs actions. Données pour calibrer la matrice C7 (GC/6J/DX vs ES).
*Catégorie : structure_marche*
---

### D1405 — Interprétation directionnelle conjointe
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « Over a given time period, the two securities move together when the Correlation Coefficient is positive. Conversely, the two securities move in opposite directions when the Correlation Coefficient is negative. »
**TRADEX-AI C7** : Règle de lecture de base pour confirmer/infirmer un signal : si deux actifs trading très corrélés divergent, c'est une anomalie à surveiller (cohérence intermarché).
*Catégorie : structure_marche*
---

### D1406 — Choix de la période selon l'horizon
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « The examples above show 20-day and 50-day Correlation Coefficients. Longer-term investors may use 150 or even 250 days (one year) for smoother lines that reflect longer-term relationships. »
**TRADEX-AI C7** : Période courte (20j) = relation réactive ; longue (150-250j) = relation de fond plus lissée. La matrice TRADEX 30j se situe dans le segment réactif/court terme.
*Catégorie : configuration*
---

### D1407 — Paramétrage SharpCharts (symbole + période)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_07) : « Select Correlation as an indicator... Enter the symbol for the other security and the timeframe in the parameters box ($SPX,10). The two are separated by a comma. »
**TRADEX-AI C7** : Paramétrage = (symbole comparé, période). Confirme qu'il faut un actif de base + un actif de référence + une fenêtre. Structure d'entrée pour le moteur de corrélation Python.
*Catégorie : configuration*
---

### D1408 — Symbole de base = benchmark dans ACP
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md, image_09) : « The Benchmark Symbol will be the symbol you entered. Enter the symbol for comparison in the Symbol box, select the number of periods for the indicator. »
**TRADEX-AI C7** : Notion de benchmark (actif de référence) vs symbole comparé. Pour TRADEX : benchmark = actif tradé (ex. GC), comparé = référence (ex. DX/6J/ES).
*Catégorie : configuration*
---

### D1409 — Scan de diversification (corrélation négative vs S&P)
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : Scan « Portfolio Diversification » : `[group is ETFNOUI] AND [Correlation(200,$SPX) < 0] RANK BY [Correlation(200,$SPX)]` — « ETFs that have a negative correlation with $SPX over the last 200 trading days. »
**TRADEX-AI C7** : Méthode pour repérer systématiquement des actifs inversement corrélés au marché (corrélation 200j < 0, classés). Transposable au screening de hedges/confirmations inverses TRADEX.
*Catégorie : structure_marche*
---

### D1410 — Synthèse opérationnelle de la corrélation
🟢 **FAIT VÉRIFIÉ** (Source : correlation_coefficient.md) : « The correlation coefficient tells us the relationship between two securities... the two securities move together when the Correlation Coefficient is positive. Conversely, the two securities move in opposite directions when the Correlation Coefficient is negative. »
**TRADEX-AI C7** : Synthèse — outil cœur du cercle C7. Seuils retenus : |r| > 0,50 = corrélation forte ; signe = sens ; période = horizon. Brique directement câblable dans `engine/correlations.py` (matrice live 30j).
*Catégorie : structure_marche*
---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D1391 → D1410 (20 décisions) |
| Images certifiées | 9/9 |
| Cercle dominant | C7 (corrélations / intermarché) · liens C4 macro (Or/Dollar D1399, D1404) |
| Tags | 🟢 littéral ×20 |
| Catégories | structure_marche (×17), configuration (×3) |
| Actifs concernés | GC (vs DX, Or/Dollar) · CL (vs XLE/WTIC) · 6J · DX · ES — cœur de la matrice C7 |
| Belkhayate | NON CONCERNÉ (aucun lien explicite source) |
| Seuils clés | r > +0,50 = forte corrélation positive · r < -0,50 = forte corrélation négative · borné [-1,+1] · périodes 20/50/200j |
| À vérifier | Aucun cas — 9/9 images certifiées, texte complet |

> ⚠️ Extraction BRUT, zone validation/. Outil éducatif uniquement · jamais conseil financier · aucune exécution automatique d'ordre. Attend OK utilisateur avant fusion KB.
