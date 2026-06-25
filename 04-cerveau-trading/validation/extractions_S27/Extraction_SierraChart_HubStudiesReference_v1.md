# Extraction SierraChart — Technical Studies Reference (Hub)
**Source :** `bundles/sierrachart/hub_studies_reference.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8871 → D8890 · **Page :** https://www.sierrachart.com/index.php?page=doc/TechnicalStudiesReference.php
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Inventaire complet des indicateurs Sierra Chart disponibles pour la plateforme — référence de sélection pour C1 à C7.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D8871 — Catalogue indicateurs Sierra Chart : couverture technique complète
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose plus de 200 études techniques documentées, allant des indicateurs de tendance classiques (ADX, MACD, Bollinger Bands, Moving Averages multiples) aux outils d'order flow avancés (Cumulative Delta Bars, Numbers Bars, Bid Ask Volume Ratio).
**TRADEX-AI C1** : L'ensemble des indicateurs de prix Belkhayate (BGC, Pivots, COG) peuvent être croisés avec les études Sierra Chart disponibles nativement — validation de la disponibilité de la couche C1.
*Catégorie : indicateurs_tendance*

### D8872 — Disponibilité natifs : VWAP, Bollinger Bands Bandwidth, ADX dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Les études VWAP with Standard Deviation Lines (ID 108), Bollinger Bands - Bandwidth (ID 135) et ADX (ID 13) figurent explicitement dans le catalogue officiel Sierra Chart Technical Studies Reference.
**TRADEX-AI C1** : Ces trois indicateurs sont directement utilisables dans Sierra Chart sans développement custom — leur configuration peut alimenter les données C1 et C2 du moteur TRADEX.
*Catégorie : indicateurs_tendance*

### D8873 — Indicateurs Order Flow natifs Sierra Chart : Cumulative Delta, Numbers Bars, Bid/Ask
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut nativement : Cumulative Delta Bars (Volume, Trades, Up/Down Tick Volume), Numbers Bars, Numbers Bars Calculated Values, Bid Ask Volume Ratio, Ask Bid Volume Difference Bars, Up Down Volume Difference Bars, Volume By Price, TPO and Volume Profile Chart.
**TRADEX-AI C2** : Ces études couvrent l'ensemble de la couche C2 (Order Flow) — delta cumulatif, volume à prix, profil TPO disponibles nativement sans addon externe dans Sierra Chart.
*Catégorie : volume_liquidite*

### D8874 — Indicateurs Momentum disponibles : RSI variants, Stochastic, CCI, MACD, ROC
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Le catalogue inclut RSI (standard, Connors RSI, RSI-W, RSI-TS, Stochastic RSI), Stochastic Fast/Slow/Premier, CCI, MACD variants (standard, Volume Weighted, Bollinger, Leader, Turbo), Rate of Change (Points et Percentage), Momentum, True Strength Index.
**TRADEX-AI C1** : Sélection de momentum confirmée — RSI 14 périodes et Stochastic %K/%D sont les proxies momentum les plus standards pour la grille de scoring /10 Belkhayate.
*Catégorie : indicateurs_momentum*

### D8875 — Indicateurs de volatilité et de structure de marché disponibles
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose : Average True Range (ATR), ATR Normalized, Historical Volatility, HL Volatility, Keltner Channel, Donchian Channel, Standard Deviation Bands, Starc Bands, Chaikin Volatility, ainsi que Swing High and Low, Market Structure MSL MSH, Zig Zag.
**TRADEX-AI C1** : ATR est disponible nativement — proxy de l'Énergie Belkhayate (stub actuel) peut utiliser ATR en attendant validation définitive Energy vs MFI. Swing High/Low et Market Structure MSL/MSH pertinents pour la détection de structure (C1).
*Catégorie : structure_marche*

### D8876 — Outils de corrélation inter-marchés natifs Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose nativement : Correlation Coefficient, Spread (3 Chart, 4 Chart, Butterfly), Ratio (Bar, Single Line), Difference (Bar, Single Line), Add Additional Symbol, Combination Symbol Chart, Overlay Non-sync — permettant des calculs multi-symboles sur un même chart.
**TRADEX-AI C7** : La matrice de corrélations live 30j (GC/HG/CL/ZW/ES/VX/MBT/6J) peut être construite directement dans Sierra Chart via Correlation Coefficient multi-chart sans développement externe.
*Catégorie : correlations*

### D8877 — Indicateurs Ichimoku complets dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut Tenkan Sen, Kijun Sen, Senkou Span A, Senkou Span B, Chikou Span — l'ensemble des composantes Ichimoku est disponible nativement.
**TRADEX-AI C1** : Le cloud Ichimoku peut servir de confirmation de tendance (C1) pour GC, CL, ZW — alignement Tenkan/Kijun pertinent pour confirmer la direction Belkhayate BGC.
*Catégorie : indicateurs_tendance*

### D8878 — Outil Synthetic VIX natif Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose une étude Synthetic VIX dans son catalogue officiel.
**TRADEX-AI C5** : Pour les actifs futures (GC, CL) sans accès direct au VIX, un VIX synthétique calculé sur le chart Sierra Chart peut servir de proxy pour la couche C5 (Sentiment) quand la donnée VX n'est pas disponible en temps réel.
*Catégorie : indicateurs_momentum*

### D8879 — Indicateurs Open Interest et COT natifs Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Le catalogue inclut : Open Interest, On Balance Open Interest (standard et Short Term), Price Open Interest Volume — permettant l'analyse OI directement dans Sierra Chart.
**TRADEX-AI C3** : Open Interest natif Sierra Chart complète la couche C3 (Institutionnels/COT) — l'OI sur GC, CL, ZW peut être overlayé sur le chart de prix sans source externe.
*Catégorie : volume_liquidite*

### D8880 — Paramètre par défaut Sierra Chart : valeurs non optimisées explicitement déclarées
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : La documentation Sierra Chart déclare explicitement : "The default study Input values are not necessarily the recommended or optimized values to use."
**TRADEX-AI C1** : Règle opérationnelle critique — pour tous les indicateurs Sierra Chart intégrés dans TRADEX, les paramètres par défaut doivent être remplacés par les valeurs validées Belkhayate (ex : COG 180/3, ADX 14, BB 20/2). Ne jamais utiliser les defaults Sierra Chart sans validation.
*Catégorie : configuration*

### D8881 — Multiple Chart Studies : calculs multi-symboles pour spreads et corrélations
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Les Multiple Chart Studies Sierra Chart permettent d'appliquer Ratio, Difference, Spread sur 2 à 4 charts simultanément. Le multiplicateur Chart 1/2/3 est configurable. Le chart "Chart N Number" est sélectionnable via Input. L'option "Display as Main Price Graph" permet de rendre un spread le prix principal.
**TRADEX-AI C7** : Pour calculer le spread GC/DX ou GC/ES en temps réel dans Sierra Chart, utiliser les Multiple Chart Studies avec Ratio (Bar) — chart GC = chart 1, chart DX = chart 2. Pertinent pour C7 corrélations live.
*Catégorie : correlations*

### D8882 — Paramètre synchronisation Multiple Chart Studies : Days To Load figé automatiquement
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Pour les Multiple Chart Studies, "The Days To Load and Time Period per Bar settings for a chart, that is referenced by one of these studies, cannot be changed. They are set to the same settings as the chart that is referencing it."
**TRADEX-AI C7** : Contrainte technique importante — dans la matrice corrélations TRADEX, tous les actifs (GC, HG, CL, ZW, ES, VX) doivent être configurés sur la même période (Days To Load) que le chart maître pour éviter des erreurs de synchronisation silencieuses.
*Catégorie : configuration*

### D8883 — Disponibilité indicateurs Gann dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose Gann HiLo Activator, Gann Swing Oscillator, Gann Trend Oscillator — indicateurs Gann disponibles nativement.
**TRADEX-AI C1** : Les oscillateurs Gann Swing/Trend peuvent servir de confirmation supplémentaire de la tendance Belkhayate pour GC et CL, connus pour leur sensibilité aux cycles de prix des matières premières.
*Catégorie : indicateurs_tendance*

### D8884 — Indicateurs de volume avancés : Klinger, MFI, Volume Zone Oscillator
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut : Klinger Volume Oscillator, Money Flow Index (MFI), Volume Zone Oscillator, Chaikin Money Flow, Accumulation Distribution (Williams), Force Index.
**TRADEX-AI C2** : MFI est explicitement mentionné dans CLAUDE.md comme indicateur en conflit avec le proxy ATR pour l'Énergie Belkhayate (ticket non tranché). Sierra Chart propose MFI nativement (ID disponible) — validation technique possible sans développement custom.
*Catégorie : volume_liquidite*

### D8885 — Centre de gravité (COG) natif Sierra Chart : confirmation disponibilité
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut nativement : Center Of Gravity Oscillator, Stochastic Center Of Gravity Oscillator, Fisher Center Of Gravity Oscillator, Adaptive Center of Gravity Oscillator.
**TRADEX-AI C1** : Confirmation que le COG (Centre de Gravité Belkhayate, paramètres figés 180/3/0.618/1.618) est disponible dans Sierra Chart via Center Of Gravity Oscillator — à vérifier que cet indicateur correspond bien à l'implémentation Belkhayate (formule non divulguée selon CLAUDE.md).
*Catégorie : indicateurs_tendance*

### D8886 — Disponibilité Parabolic SAR (Parabolic) dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut l'indicateur Parabolic dans son catalogue, correspondant au Parabolic SAR de Welles Wilder.
**TRADEX-AI C1** : Le Parabolic SAR peut servir de trailing stop et de confirmation de retournement de tendance pour GC et CL — applicable dans la grille de scoring C1 Belkhayate comme signal de sortie.
*Catégorie : gestion_position_active*

### D8887 — Indicateurs de range et de structure : ADR, Narrow Range Bar, Wide Range Bar
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut Average Daily Range (ADR), Narrow Range Bar, Wide Range Bar, Bar Time Duration, True Range.
**TRADEX-AI C1** : ADR pertinent pour calibrer les niveaux de Take Profit sur GC (Or) — un TP placé à 0.5 ADR ou 1 ADR est une règle opérationnelle classique. Sierra Chart calcule l'ADR nativement.
*Catégorie : gestion_risque_entree*

### D8888 — Indicateurs de pivots dans Sierra Chart : Pivot Points Daily et Variable Period
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart propose Pivot Points - Daily et Pivot Points - Variable Period, Pivot Range - Variable Period.
**TRADEX-AI C1** : Les Pivots Belkhayate (C1 — Pivots) peuvent être recoupés avec les Pivot Points classiques Daily de Sierra Chart pour confirmation — les deux systèmes de pivots coexistent dans le même chart Sierra Chart.
*Catégorie : structure_marche*

### D8889 — Disponibilité Supertrend et Keltner Channel dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut SuperTrend, Super Trend Stop, Keltner Channel comme indicateurs natifs.
**TRADEX-AI C1** : SuperTrend (basé sur ATR) peut compléter la détection de tendance Belkhayate BGC sur GC, CL — utilisable comme filtre de tendance secondaire pour réduire les faux signaux.
*Catégorie : indicateurs_tendance*

### D8890 — Disponibilité Wave Trend Oscillator et Fisher Transform dans Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : hub_studies_reference.md) : Sierra Chart inclut Wave Trend Oscillator, Fisher Transform, Inverse Fisher Transform, Fisher Function, Fisher Cyber Cycle, Fisher Relative Vigor Index 3.
**TRADEX-AI C1** : Le Fisher Transform normalise le prix selon une distribution Gaussienne — pertinent pour identifier les retournements extrêmes sur GC (Or) et CL (Pétrole), complémentaire de la méthode Belkhayate pour détecter les zones de surachat/survente.
*Catégorie : indicateurs_momentum*
