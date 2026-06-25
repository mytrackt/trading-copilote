# Extraction StockCharts — Standard Deviation (Volatility)
**Source :** `bundles/stockcharts/standard_deviation_volatility.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D3851 → D3870 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/standard-deviation-volatility.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : mesure de volatilité directement applicable à GC/HG/CL/ZW — qualification des mouvements de prix significatifs, filtrage des signaux par régime de volatilité.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Standard Deviation Excel Spreadsheet | Calculating Standard Deviation | D3853 |
| image_02 | Standard Deviation Chart 1 | Calculating Standard Deviation | D3853 |
| image_03 | Standard Deviation Chart 2 | Standard Deviation Values | D3855 |
| image_04 | Standard Deviation Chart 3 | Measuring Expectations | D3857 |
| image_05 | Standard Deviation Chart 5 | Measuring Expectations | D3858 |
| image_06 | Standard Deviation Chart 6 | Using with SharpCharts | D3866 |
| image_07 | Standard Deviation SharpCharts | Using with SharpCharts | D3866 |

## DÉCISIONS

### D3851 — Définition : l'écart-type mesure la dispersion autour de la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "Standard deviation is a statistical term that measures the amount of variability or dispersion around an average. Standard deviation is also a measure of volatility."
**TRADEX-AI C1** : L'écart-type est un proxy de volatilité directement utilisable sur GC/HG/CL/ZW pour évaluer l'ampleur attendue des mouvements de prix — intégrable comme filtre de qualité de signal.
*Catégorie : indicateurs_tendance*

### D3852 — Relation dispersion/volatilité : plus la dispersion est grande, plus la volatilité est élevée
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The larger this dispersion or variability is, the higher the standard deviation. The smaller this dispersion or variability is, the lower the standard deviation."
**TRADEX-AI C5** : Sur VX (VIX), la relation entre dispersion et volatilité est directe — un écart-type élevé sur VX indique un régime de haute peur, ce qui doit moduler les seuils de confiance du signal TRADEX-AI.
*Catégorie : indicateurs_momentum*

### D3853 — Calcul en 6 étapes : population entière (STDEVP), pas un échantillon
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md, image_01 Standard Deviation Excel Spreadsheet, image_02 Standard Deviation Chart 1) : "StockCharts.com calculates the standard deviation for a population, which assumes that the periods involved represent the whole data set, not a sample from a bigger data set." Calcul en 6 étapes : moyenne → écarts → carrés → somme → division → racine carrée.
**TRADEX-AI C1** : Si TRADEX-AI implémente un calcul d'écart-type sur les prix GC/HG/CL/ZW, utiliser STDEVP (population) et non STDEV (échantillon) — cohérence avec la méthode StockCharts.
*Catégorie : indicateurs_tendance*

### D3854 — Période par défaut 10, adaptable : 21j ≈ 1 mois, 63j ≈ 1 trimestre, 250j ≈ 1 an
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The standard deviation is available as an indicator in SharpCharts with a default parameter of 10... Roughly speaking, 21 days equals one month, 63 days equals one quarter and 250 days equals one year."
**TRADEX-AI C1** : Pour TRADEX-AI, une période de 21 jours (1 mois) est recommandée pour mesurer la volatilité court terme sur GC/HG/CL/ZW — 250 jours pour le contexte macro annuel.
*Catégorie : indicateurs_tendance*

### D3855 — Les valeurs d'écart-type dépendent du prix : ne pas comparer directement deux actifs à prix différents
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md, image_03 Standard Deviation Chart 2) : "Securities with high prices, such as Google (±550), will have higher standard deviation values than securities with low prices, such as Intel (±22). These higher values are not a reflection of higher volatility, but rather a reflection of the actual price."
⏳ **VOLATILE** : Les prix de référence (Google ±550, Intel ±22) sont datés mais le principe reste valide.
**TRADEX-AI C7** : Pour comparer la volatilité entre GC (≈2000$/oz) et ZW (≈600¢/bu), diviser l'écart-type par le prix de clôture pour obtenir un % de volatilité comparable — ne jamais comparer les valeurs brutes d'écart-type entre actifs de prix différents.
*Catégorie : correlations*

### D3856 — Normalisation : diviser l'écart-type par le prix de clôture pour comparer des actifs différents
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "One would have to divide the standard deviation by the closing price to directly compare volatility for the two securities."
**TRADEX-AI C7** : Formule de normalisation = Std_Dev(n) / Close × 100. Applicable pour classer GC/HG/CL/ZW par niveau de volatilité relative et ajuster le sizing des positions.
*Catégorie : correlations*

### D3857 — Règle 68-95-99.7 : distribution normale des mouvements de prix
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md, image_04 Standard Deviation Chart 3) : "In a normal distribution, 68% of the observations fall within one standard deviation, while 95% fall within two and 99.7% fall within three. Using these guidelines, traders can estimate the significance of a price movement."
🟡 **SYNTHÈSE** : "price changes for securities are not always normally distributed" — nuance importante : la règle est une approximation.
**TRADEX-AI C1** : Un mouvement > 1 écart-type sur GC/HG/CL/ZW signale une force/faiblesse supérieure à la moyenne — utilisable comme filtre de signal : n'activer le Niveau 3 (Claude) que si le mouvement dépasse 1σ.
*Catégorie : indicateurs_tendance*

### D3858 — Écart-type 21j MSFT : 0.88 → mouvements > 0.88$ = notables (1σ), > 1.76$ (2σ), > 2.64$ (3σ)
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md, image_05 Standard Deviation Chart 5) : "The 21-day standard deviation is still quite variable as it fluctuated between .32 and .88 from mid-August until mid-December. A 250-day moving average can be applied to smooth the indicator and find an average."
⏳ **VOLATILE** : Valeurs spécifiques à MSFT et à une période historique.
**TRADEX-AI C1** : Appliquer une MA(250) à l'écart-type 21j sur GC/HG/CL/ZW pour établir un niveau de volatilité "normal" — les mouvements dépassant ce niveau moyen signalent un intérêt accru et peuvent préfigurer un changement de tendance ou un breakout.
*Catégorie : indicateurs_tendance*

### D3859 — Un mouvement > MA(250) de l'écart-type 21j indique un intérêt accru pouvant préfigurer un changement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "These above-average price movements indicate heightened interest that could foreshadow a trend change or mark a breakout."
**TRADEX-AI C1** : Sur GC, un mouvement quotidien dépassant la MA(250) de l'écart-type 21j est un signal d'alerte Niveau 1 — déclencher la vérification complète (Niveau 2 + Niveau 3 si conditions réunies).
*Catégorie : indicateurs_tendance*

### D3860 — L'écart-type ne génère pas de signal directionnel : il mesure l'amplitude, pas la direction
🟡 **SYNTHÈSE** (Source : standard_deviation_volatility.md) : "A move greater than one standard deviation would show above average strength or weakness, depending on the direction of the move." — le sens doit être déterminé par d'autres outils.
**TRADEX-AI C1** : L'écart-type est un filtre de taille de mouvement sur GC/HG/CL/ZW, PAS un indicateur directionnel — la direction reste déterminée par les indicateurs Belkhayate (BGC, Direction, Pivots).
*Catégorie : indicateurs_tendance*

### D3861 — L'écart-type utilisé dans les Bandes de Bollinger : ±2σ autour d'une moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The standard deviation is also used with other indicators, such as Bollinger Bands. These bands are set 2 standard deviations above and below a moving average. Moves that exceed the bands are deemed significant enough to warrant attention."
**TRADEX-AI C1** : Les Bandes de Bollinger (±2σ) sont une application directe de l'écart-type sur GC/HG/CL/ZW — les cassures de bandes signalent des mouvements statistiquement significatifs qui méritent une analyse Belkhayate approfondie.
*Catégorie : indicateurs_tendance*

### D3862 — L'écart-type doit être utilisé avec d'autres outils : oscillateurs momentum + patterns
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "the standard deviation should be used in conjunction with other analysis tools, such as momentum oscillators or chart patterns."
**TRADEX-AI C1** : L'écart-type seul est insuffisant — dans TRADEX-AI il doit être combiné avec les indicateurs Belkhayate (momentum C1) et l'Order Flow ATAS (C2) pour qualifier les signaux sur GC/HG/CL/ZW.
*Catégorie : configuration*

### D3863 — Utilisation dans les scans : filtrer les actifs à haute volatilité
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The Standard Deviation indicator is often used in scans to weed out securities with extremely high volatility." Formule : `Std Deviation(250) / SMA(20,Close) * 100 < 20` pour exclure la haute volatilité.
**TRADEX-AI C1** : Pour TRADEX-AI, un régime de volatilité anormalement élevée sur GC/HG/CL/ZW (ex. Std_Dev(250)/SMA(20) > seuil) doit activer la prudence — réduire le seuil de confiance minimum ou bloquer le mode Auto.
*Catégorie : gestion_risque_entree*

### D3864 — L'écart-type est calculable sur charts hebdomadaires et mensuels
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The standard deviation can also be used on weekly or monthly charts."
**TRADEX-AI C1** : L'écart-type sur timeframe hebdomadaire et mensuel donne le contexte macro de volatilité pour GC/HG/CL/ZW — utilisable pour qualifier le régime de marché avant d'activer les signaux intraday.
*Catégorie : indicateurs_tendance*

### D3865 — Les valeurs historiques d'écart-type changent si l'actif subit un grand mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "Historical standard deviation values will also be affected if a security experiences a large price change over a period of time. A security that moves from 10 to 50 will most likely have a higher standard deviation at 50 than at 10."
⏳ **VOLATILE** : Principe structurel stable mais valeurs de référence spécifiques à chaque actif et période.
**TRADEX-AI C1** : Après un grand mouvement de GC/HG/CL/ZW (ex. rallye de +20%), recalibrer les seuils d'écart-type de référence — ne pas utiliser les valeurs historiques d'avant le mouvement comme base.
*Catégorie : gestion_position_active*

### D3866 — Paramètre par défaut SharpCharts : 10 périodes, modifiable selon le style d'analyse
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md, image_06 Standard Deviation Chart 6, image_07 Standard Deviation SharpCharts) : "The standard deviation is available as an indicator in SharpCharts with a default parameter of 10. This parameter can be changed according to analysis needs."
**TRADEX-AI C1** : Pour TRADEX-AI, utiliser 21 périodes (mensuel) comme paramètre principal de l'écart-type sur GC/HG/CL/ZW — 10 périodes pour les signaux de très court terme intraday.
*Catégorie : indicateurs_tendance*

### D3867 — L'écart-type peut être placé au-dessus, en-dessous ou derrière le graphique des prix
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The indicator can be placed above, below or behind the actual price plot."
⚫ **HYPOTHÈSE PROJET** : La disposition visuelle n'est pas directement liée à la méthode Belkhayate mais relève de l'ergonomie du dashboard.
**TRADEX-AI C1** : Le dashboard TRADEX-AI devra afficher l'écart-type 21j dans un panneau séparé sous le graphique prix GC/HG/CL/ZW pour faciliter la lecture visuelle de la volatilité.
*Catégorie : configuration*

### D3868 — Des overlays peuvent être ajoutés à l'indicateur écart-type (ex. MA sur l'écart-type)
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "Indicators can be applied to the standard deviation by clicking advanced options and then adding an overlay."
**TRADEX-AI C1** : Une MA(250) appliquée à l'écart-type 21j sur GC/HG/CL/ZW donne le niveau "normal" de volatilité — les dépassements de cette MA signalent des conditions inhabituelles (voir D3858-D3859).
*Catégorie : indicateurs_tendance*

### D3869 — Scan "filtrage haute volatilité" : Std_Dev(250) / SMA(20,Close) * 100 < 20
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : Code de scan SharpCharts publié — `[Std Deviation(250) / SMA(20,Close) * 100 < 20]` pour exclure les actifs à volatilité excessive.
**TRADEX-AI C1** : Règle dérivée pour TRADEX-AI : si Std_Dev(250) / SMA(20,Close) * 100 > 20 sur GC/HG/CL/ZW, activer un flag "haute volatilité" qui réduit la taille de position recommandée et exige une confiance ≥ 8/10 pour le mode Auto.
*Catégorie : gestion_risque_entree*

### D3870 — L'écart-type comme mesure des attentes : quantifier l'importance d'un mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : standard_deviation_volatility.md) : "The current value of the standard deviation can be used to estimate the importance of a move or set expectations."
🟡 **SYNTHÈSE** : L'écart-type transforme un mouvement de prix brut en un signal statistiquement qualifié (normal vs. exceptionnel).
**TRADEX-AI C1** : Dans la grille de scoring /10 de TRADEX-AI, un mouvement de prix GC/HG/CL/ZW dépassant 2σ (95e percentile) ajoute un point de confiance — mouvement statistiquement rare = signal plus fiable.
*Catégorie : configuration*
