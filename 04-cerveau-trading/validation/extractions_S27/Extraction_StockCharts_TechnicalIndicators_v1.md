# Extraction StockCharts — Technical Indicators
**Source :** `bundles/stockcharts/technical_indicators.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle (page index) · 0/0 certifiées · 0 à vérifier
**Décisions :** D4391 → D4410 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Catalogue complet d'indicateurs techniques — identifier lesquels sont pertinents pour les Cercles C1/C2/C5 sur GC/HG/CL/ZW/ES/VX/DX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D4391 — Indicateurs prix+volume : ADL, CMF, OBV, Force Index
🔵 **ÉCOLE** (Source : technical_indicators.md) : Quatre indicateurs combinent prix et volume pour mesurer les flux monétaires : Accumulation/Distribution Line (ADL), Chaikin Money Flow (CMF), On Balance Volume (OBV), Force Index. ADL et CMF : money flow dans ou hors d'un actif. OBV : cumul volume directionnel. Force Index : oscillateur prix × volume.
**TRADEX-AI C2** : Ces 4 indicateurs alimentent directement le Cercle C2 (Order Flow) — OBV et CMF sont particulièrement pertinents pour détecter la distribution institutionnelle sur GC/HG/CL avant un retournement.
*Catégorie : volume_liquidite*

### D4392 — Indicateurs de tendance : ADX, Aroon, Aroon Oscillator
🔵 **ÉCOLE** (Source : technical_indicators.md) : ADX (Average Directional Index) indique si un actif est en tendance ou en oscillation. Aroon Up/Down mesure le temps depuis le dernier plus haut / plus bas sur la période. Aroon Oscillator = différence Aroon Up − Aroon Down.
**TRADEX-AI C1** : ADX est un filtre de tendance crucial pour TRADEX — en l'absence de tendance (ADX < 25), les signaux prix Belkhayate doivent être pondérés à la baisse sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D4393 — Indicateurs de volatilité : ATR, ATRP, ATR Bands, ATR Trailing Stops
🔵 **ÉCOLE** (Source : technical_indicators.md) : Average True Range (ATR) mesure la volatilité brute. ATRP = ATR exprimé en pourcentage pour comparaison entre actifs. ATR Bands = bandes dynamiques autour d'une MA. ATR Trailing Stops = stops dynamiques basés sur la volatilité réelle.
**TRADEX-AI C1/C5** : ATR est le proxy de volatilité utilisé dans TRADEX-AI pour l'Énergie Belkhayate (stub actuel). ATR Trailing Stops fournit une méthodologie concrète pour les stops dynamiques sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D4394 — MACD et variantes : MACD, MACD-Histogram, MACD-V, MACD-V Histogram
🔵 **ÉCOLE** (Source : technical_indicators.md) : MACD = différence entre deux EMAs (momentum oscillateur). MACD-Histogram = différence MACD − signal line. MACD-V = MACD normalisé par la volatilité pour comparaison cross-actifs. MACD-V Histogram = indique si tendance est positive ou négative en termes absolus.
**TRADEX-AI C1** : Le MACD reste un indicateur de momentum standard applicable sur GC/HG/CL/ZW ; MACD-V est particulièrement utile pour comparer le momentum entre GC et HG dans le cadre des corrélations inter-marchés C7.
*Catégorie : indicateurs_momentum*

### D4395 — RSI et variantes : RSI, StochRSI, CMB Composite Index
🔵 **ÉCOLE** (Source : technical_indicators.md) : RSI (Relative Strength Index) mesure la force directionnelle du mouvement. StochRSI = Stochastique appliqué au RSI pour amplifier les variations. CMB Composite Index = oscillateur momentum non borné tentant d'améliorer les limites du RSI classique.
**TRADEX-AI C1** : RSI est un indicateur de confirmation momentum standard pour les signaux Belkhayate — une divergence RSI/prix sur GC ou CL signale un affaiblissement de tendance à intégrer dans le score /10.
*Catégorie : indicateurs_momentum*

### D4396 — Stochastique : Stochastic Oscillator (Fast, Slow, Full)
🔵 **ÉCOLE** (Source : technical_indicators.md) : Le Stochastic Oscillator mesure la position du prix par rapport à son range récent. Fast Stochastic : %K brut + %D (SMA 3). Slow Stochastic : %K lissé (=Fast %D) + nouveau %D. Full Stochastic : paramétrage flexible des deux composantes.
**TRADEX-AI C1** : Le Stochastic est un indicateur de momentum classique applicable à tous les actifs TRADEX (GC/HG/CL/ZW) ; les conditions de surachat/survente complètent la lecture de l'Énergie Belkhayate.
*Catégorie : indicateurs_momentum*

### D4397 — Indicateurs de corrélation : Correlation Coefficient, Price Relative / RS, RRG RS
🔵 **ÉCOLE** (Source : technical_indicators.md) : Correlation Coefficient = degré de corrélation entre deux actifs sur une période donnée. Price Relative / Relative Strength = ratio de performance entre deux actifs. RRG Relative Strength = RS-Ratio (performance relative) + RS-Momentum (momentum de la performance relative).
**TRADEX-AI C7** : Ces indicateurs sont directement applicables à la matrice de corrélations live 30j du Cercle C7 — le Correlation Coefficient permet de mesurer GC/DX, CL/DX, HG/ES et alerter sur les changements de corrélation.
*Catégorie : correlations*

### D4398 — Indicateurs de sentiment/volatilité marché : Standard Deviation, Ulcer Index, TTM Squeeze
🔵 **ÉCOLE** (Source : technical_indicators.md) : Standard Deviation mesure la volatilité statistique. Ulcer Index mesure le risque et la drawdown. TTM Squeeze identifie les périodes de consolidation (compression Bollinger dans Keltner) et la direction du mouvement résultant.
**TRADEX-AI C5** : L'Ulcer Index et le TTM Squeeze sont pertinents pour le Cercle C5 (Sentiment) — un TTM Squeeze en compression sur ES ou VX peut précéder un mouvement directionnel fort sur GC/HG.
*Catégorie : indicateurs_momentum*

### D4399 — Indicateurs de momentum avancés : Coppock Curve, PMO, KST, Pring's Special K
🔵 **ÉCOLE** (Source : technical_indicators.md) : Coppock Curve = ROC + WMA, conçu pour signaler les retournements haussiers cycliques de long terme. PMO (Price Momentum Oscillator) = ROC à double lissage. KST = ROC lissé sur 4 timeframes. Special K = combine vélocité court/moyen/long terme.
**TRADEX-AI C1** : Ces indicateurs de momentum multi-timeframe sont alignés avec la philosophie Belkhayate de confluence temporelle — Coppock Curve sur données hebdomadaires GC peut signaler des retournements majeurs à intégrer dans le contexte macro.
*Catégorie : indicateurs_momentum*

### D4400 — Money Flow Index (MFI) et Ease of Movement (EMV)
🔵 **ÉCOLE** (Source : technical_indicators.md) : Money Flow Index (MFI) = version pondérée par le volume du RSI — mesure shifts entre pression achat et vente. Ease of Movement (EMV) = compare volume et amplitude prix pour identifier les mouvements significatifs.
**TRADEX-AI C2** : MFI est un indicateur clé pour le Cercle C2 (Order Flow) — un MFI > 80 sur GC avec volume élevé signale une pression d'achat institutionnelle ; EMV faible malgré un grand mouvement prix révèle un manque de conviction à filtrer.
*Catégorie : volume_liquidite*

### D4401 — Indicateurs de distance et de rang : SCTR, Distance From/To Highs/Lows, Distance From MA
🔵 **ÉCOLE** (Source : technical_indicators.md) : SCTR (StockCharts Technical Rank) = rang relatif de force technique d'un actif. Distance From Highs/Lows/MA = mesure en % l'éloignement par rapport aux niveaux clés. Distance To Highs/Lows = pourcentage restant à parcourir pour atteindre un plus haut/bas.
**TRADEX-AI C7** : Ces indicateurs de distance permettent de comparer la force relative de GC, HG, CL, ZW au sein du Cercle C7 — un actif trading à grande distance de sa MA 200 présente un risque de retournement à pondérer dans le score.
*Catégorie : indicateurs_tendance*
