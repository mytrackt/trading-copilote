# Extraction StockCharts — Stochastic Oscillator (Fast, Slow, and Full)
**Source :** `bundles/stockcharts/stochastic_oscillator_fast_slow_and_full.md` (HTTP 200) + 9 images certifiées
**Méthode images :** double ancrage · 9/9 certifiées · 0 à vérifier
**Décisions :** D3871 → D3890 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/stochastic-oscillator-fast-slow-and-full.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : indicateur momentum directement applicable à GC/HG/CL/ZW — niveaux suracheté/survendu, divergences, set-ups Lane, confluence avec Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Stochastics - Chart 1 | How Do You Calculate | D3872 |
| image_02 | Stochastics - Chart 2 | Three Stochastic Versions | D3874 |
| image_03 | FULL STOCHASTIC OSCILLATOR. Note how the oscillator moved above 80 and remained there. | Overbought/Oversold | D3876 |
| image_04 | Stochastics - Chart 4 | Overbought/Oversold | D3877 |
| image_05 | Stochastics - Chart 5 | Overbought/Oversold | D3878 |
| image_06 | Stochastics - Chart 6 | Bull/Bear Divergences | D3881 |
| image_07 | Stochastics - Chart 7 | Bull/Bear Divergences | D3882 |
| image_08 | Stochastics - Chart 8 | Bull/Bear Set-Ups | D3884 |
| image_09 | Stochastics - Chart 9 | Bull/Bear Set-Ups | D3885 |
| image_10 | Stochastics - Chart 10 | Using with SharpCharts | D3888 |
| image_11 | Stochastics - SharpCharts | Using with SharpCharts | D3888 |

## DÉCISIONS

### D3871 — Définition : le Stochastique mesure la vitesse et le momentum, PAS le prix ou le volume
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : Selon George C. Lane (créateur, fin des années 1950) : "the Stochastic Oscillator doesn't follow price, it doesn't follow volume or anything like that. It follows the speed or the momentum of price."
🔵 **ÉCOLE** : George C. Lane, créateur de l'oscillateur stochastique, fin des années 1950.
**TRADEX-AI C1** : Le Stochastique mesure le momentum des prix GC/HG/CL/ZW — complément naturel des indicateurs de direction Belkhayate (BGC/Direction) qui mesurent la tendance de prix.
*Catégorie : indicateurs_momentum*

### D3872 — Formule %K et %D : close relative au range High-Low sur la période
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_01 Stochastics - Chart 1) :
`%K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100`
`%D = 3-day SMA of %K`
Période par défaut : 14 périodes. Lowest Low et Highest High sur la période look-back.
**TRADEX-AI C1** : Implémenter le Stochastique 14,3 sur GC/HG/CL/ZW dans le moteur Python — %K = position du close dans le range 14 périodes × 100.
*Catégorie : indicateurs_momentum*

### D3873 — Le momentum change de direction avant le prix : divergences = signal primaire de Lane
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "As a rule, the momentum changes direction before price." — "bullish and bearish divergences in the Stochastic Oscillator can be used to foreshadow reversals. This was the first and most important signal that Lane identified."
🔵 **ÉCOLE** : George C. Lane — divergences = signal #1 par ordre d'importance.
**TRADEX-AI C1** : Les divergences Stochastique/Prix sur GC/HG/CL/ZW sont un signal d'alerte précoce d'inversion — à intégrer dans la grille de scoring /10 comme critère C1 (confirmé avant le retournement du prix).
*Catégorie : indicateurs_momentum*

### D3874 — Trois versions : Fast (brut), Slow (lissé 3j), Full (entièrement personnalisable)
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_02 Stochastics - Chart 2) :
- Fast %K = calcul de base · Fast %D = SMA(3, Fast %K)
- Slow %K = SMA(3, Fast %K) = Fast %D · Slow %D = SMA(3, Slow %K)
- Full %K = SMA(X, Fast %K) · Full %D = SMA(X, Full %K)
Paramètres par défaut : Fast(14,3) · Slow(14,3) · Full(14,3,3).
**TRADEX-AI C1** : Utiliser le Slow Stochastique (14,3) pour TRADEX-AI sur GC/HG/CL/ZW — moins de faux signaux que le Fast, plus réactif que le Full avec période étendue.
*Catégorie : indicateurs_momentum*

### D3875 — Interprétation : > 50 = close dans la moitié haute du range ; < 50 = moitié basse
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "The Stochastic Oscillator is above 50 when the close is in the upper half of the range and below 50 when the close is in the lower half. Low readings (below 20) indicate that price is near its low for the given time period. High readings (above 80) indicate that price is near its high."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, Stochastique > 50 = force relative (fermeture haute du range) → biais haussier ; < 50 = faiblesse relative → biais baissier. Seuils opérationnels : suracheté ≥ 80, survendu ≤ 20.
*Catégorie : indicateurs_momentum*

### D3876 — Surchat/survendu : 80 et 20 sont les seuils classiques, ajustables selon l'actif
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_03 FULL STOCHASTIC OSCILLATOR. Note how the oscillator moved above 80 and remained there.) : "Traditional settings use 80 as the overbought threshold and 20 as the oversold threshold. These levels can be adjusted to suit analytical needs and security characteristics."
🟢 **FAIT VÉRIFIÉ** : "The indicator is overbought and strong when above 80. A subsequent move below 80 is needed to signal a reversal."
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, utiliser 80/20 comme seuils par défaut — la cassure de 80 vers le bas confirme un signal de vente, la remontée au-dessus de 20 confirme un signal d'achat. Un oscillateur qui reste > 80 prolongé indique une tendance forte (ne pas vendre prématurément).
*Catégorie : indicateurs_momentum*

### D3877 — En tendance haussière : ignorer les signaux surachetés, exploiter les signaux survendus
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_04 Stochastics - Chart 4) : "Trading in the direction of the bigger trend improves the odds. The Full Stochastic Oscillator moved below 20 in early September and early November. Subsequent moves back above 20 signaled an upturn in prices (green dotted line) and continuation of the bigger uptrend."
🔵 **ÉCOLE** : Tensile Trading / StockCharts methodology — trader dans la direction de la tendance principale.
**TRADEX-AI C1** : Règle TRADEX-AI : si la Direction Belkhayate est haussière sur GC/HG/CL/ZW, ignorer les signaux suracheté Stochastique (>80) et n'activer que les retours depuis survendu (<20 → retour >20) comme points d'entrée.
*Catégorie : indicateurs_momentum*

### D3878 — En tendance baissière : ignorer les survendus, exploiter les retours depuis surchat (>80 → <80)
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_05 Stochastics - Chart 5) : "With a downtrend in force, the Full Stochastic Oscillator (10,3,3) was used to identify overbought readings to foreshadow a potential reversal. Oversold readings were ignored because of the bigger downtrend."
**TRADEX-AI C1** : Règle TRADEX-AI : si la Direction Belkhayate est baissière sur GC/HG/CL/ZW, ignorer les signaux survendu Stochastique (<20) et n'activer que les retours depuis suracheté (>80 → retour <80) comme points de vente/short.
*Catégorie : indicateurs_momentum*

### D3879 — Sensibilité : période courte = plus réactif/plus faux signaux ; période longue = moins réactif/moins de signaux
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "The shorter look-back period (10 versus 14) increases the sensitivity of the oscillator for more overbought readings... A shorter look-back period will produce a choppy oscillator with many overbought and oversold readings. A longer look-back period will provide a smoother oscillator with fewer overbought and oversold readings."
**TRADEX-AI C1** : Pour TRADEX-AI sur GC/HG/CL/ZW, adapter la période Stochastique au timeframe : période 10 pour signaux intraday rapides (range bars NT8), période 14 pour swing trading, période 20 pour contexte plus long.
*Catégorie : indicateurs_momentum*

### D3880 — Confirmation en 3 étapes d'une divergence haussière : signal line cross + retour >20 + passage >50 + breakout
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "There are three steps to confirming this higher low. The first is a signal line cross and/or move back above 20. The second is a move above 50... The third is a resistance breakout on the price chart."
**TRADEX-AI C1** : Divergence haussière Stochastique sur GC/HG/CL/ZW = signal valide seulement si les 3 étapes sont confirmées : (1) %K croise %D vers le haut ET/OU >20, (2) Stochastique passe >50, (3) cassure de résistance prix. La convergence des 3 éléments renforce la confiance dans la grille /10.
*Catégorie : indicateurs_momentum*

### D3881 — Divergence haussière : nouveau plus bas prix + plus bas Stochastique plus haut = moins de momentum baissier
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_06 Stochastics - Chart 6) : "A bullish divergence forms when price records a lower low, but the Stochastic Oscillator forms a higher low. This shows less downside momentum that could foreshadow a bullish reversal."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, une divergence haussière Stochastique est un signal C1 fort à combiner avec les niveaux de Pivots Belkhayate (support) pour valider un retournement potentiel.
*Catégorie : indicateurs_momentum*

### D3882 — Divergence baissière : nouveau plus haut prix + plus haut Stochastique plus bas = moins de momentum haussier
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_07 Stochastics - Chart 7) : "A bearish divergence forms when price records a higher high, but the Stochastic Oscillator forms a lower high. This shows less upside momentum that could foreshadow a bearish reversal."
🟢 **FAIT VÉRIFIÉ** : Confirmation baissière = cassure support OU Stochastique < 50 (centeline).
**TRADEX-AI C1** : Sur GC (Or en tendance haussière prolongée), surveiller les divergences baissières Stochastique/Prix — un break sous 50 du Stochastique + cassure support Belkhayate = signal de sortie/vente prioritaire.
*Catégorie : indicateurs_momentum*

### D3883 — Le niveau 50 est la ligne centrale : au-dessus = force (tasse à moitié pleine) ; en-dessous = faiblesse
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "Think of it as the 50-yard line in football. The offense has a higher chance of scoring when it crosses the 50-yard line." Un cross au-dessus de 50 = prix dans la moitié haute du range (force) ; en-dessous = faiblesse.
**TRADEX-AI C1** : Le passage de 50 par le Stochastique sur GC/HG/CL/ZW est un signal de confirmation de tendance — intégrer dans la grille /10 comme indicateur de momentum neutre vs. directionnel.
*Catégorie : indicateurs_momentum*

### D3884 — Bull Set-Up (Lane) : plus bas prix + plus haut Stochastique = renforcement du momentum haussier → bas tradable à venir
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_08 Stochastics - Chart 8) : "A bull set-up is basically the inverse of a bullish divergence. The underlying security forms a lower high, but the Stochastic Oscillator forms a higher high... The next decline is then expected to result in a tradable bottom."
🔵 **ÉCOLE** : George Lane — "set-ups" distincts des divergences classiques.
**TRADEX-AI C1** : Un Bull Set-Up sur GC/HG/CL/ZW préfigure un point d'entrée dans la prochaine correction — surveiller le retour du Stochastique sous 20 puis la remontée comme point d'entrée idéal.
*Catégorie : indicateurs_momentum*

### D3885 — Bear Set-Up (Lane) : plus haut prix + plus bas Stochastique = renforcement du momentum baissier → sommet tradable à venir
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_09 Stochastics - Chart 9) : "A bear set-up occurs when the security forms a higher low, but the Stochastic Oscillator forms a lower low. Even though the stock held above its prior low, the lower low in the Stochastic Oscillator shows increasing downside momentum. The next advance is expected to result in an important peak."
🔵 **ÉCOLE** : George Lane — Bear Set-Up.
**TRADEX-AI C1** : Un Bear Set-Up Stochastique sur GC/HG/CL/ZW avertit que le prochain rebond sera limité et représentera une opportunité de vente — le Stochastique ne montant pas au-delà de 80 après le bear set-up confirme la faiblesse.
*Catégorie : indicateurs_momentum*

### D3886 — Le Stochastique fonctionne en range ET en tendance zigzag : applicable aux deux régimes
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "While momentum oscillators are best suited for trading ranges, they can also be used with securities that trend, provided the trend takes on a zigzag format. Pullbacks are part of uptrends that zigzag higher."
**TRADEX-AI C1** : GC/HG/CL/ZW alternent entre phases de range et de tendance zigzag — le Stochastique est applicable dans les deux régimes, ce qui en fait un outil polyvalent pour TRADEX-AI indépendamment de la phase de marché.
*Catégorie : indicateurs_momentum*

### D3887 — Utiliser le Stochastique près des supports/résistances : rebond depuis support survendu, rejet depuis résistance suracheté
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "Should a security trade near support with an oversold Stochastic Oscillator, look for a break above 20 to signal an upturn and successful support test. Conversely, should a security trade near resistance with an overbought Stochastic Oscillator, look for a break below 80 to signal a downturn and resistance failure."
**TRADEX-AI C1** : Règle de confluence TRADEX-AI : Stochastique survendu (<20) + prix sur Pivot Belkhayate support = signal d'entrée long haute probabilité sur GC/HG/CL/ZW. Inverse pour short. La confluence Pivot + Stochastique ajoute +1 point dans la grille /10.
*Catégorie : gestion_risque_entree*

### D3888 — Paramètres par défaut SharpCharts : Fast(14,3) · Slow(14,3) · Full(14,3,3)
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md, image_10 Stochastics - Chart 10, image_11 Stochastics - SharpCharts) : "The default settings are as follows: Fast Stochastic Oscillator (14,3), Slow Stochastic Oscillator (14,3) and Full Stochastic Oscillator (14,3,3)."
**TRADEX-AI C1** : Paramètre de référence TRADEX-AI = Slow Stochastique (14,3) — compatible avec les standards de l'industrie, réducteur de bruit par rapport au Fast.
*Catégorie : indicateurs_momentum*

### D3889 — Scan "retournement haussier depuis survendu" : Close > SMA(200) + Stoch(%K,14,3) : hier <20, aujourd'hui >20
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : Code de scan StockCharts publié — `[Daily Close > Daily SMA(200,Daily Close)] AND [Yesterday's Daily Slow Stoch %K(14,3) < 20] AND [Daily Slow Stoch %K(14,3) > 20]` — filtre les retournements haussiers dans une tendance long terme positive.
**TRADEX-AI C1** : Règle dérivée TRADEX-AI pour GC/HG/CL/ZW : activer un signal LONG uniquement si Close > SMA(200) ET Stoch %K était <20 hier ET >20 aujourd'hui — filtre qui améliore la qualité des entrées dans la direction de la tendance longue.
*Catégorie : gestion_risque_entree*

### D3890 — Le Stochastique doit être utilisé avec volume, supports/résistances et breakouts pour confirmation
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_oscillator_fast_slow_and_full.md) : "Like all technical indicators, it is important to use the Stochastic Oscillator in conjunction with other technical analysis tools. Volume, support/resistance and breakouts can be used to confirm or refute signals produced by the Stochastic Oscillator."
**TRADEX-AI C2** : Sur TRADEX-AI, les signaux Stochastique sur GC/HG/CL/ZW doivent être confirmés par l'Order Flow ATAS (C2 : Delta, Big Trades) et les niveaux Pivots Belkhayate (C1) — un signal Stochastique non confirmé par le volume/order flow est insuffisant pour déclencher un ordre.
*Catégorie : configuration*
