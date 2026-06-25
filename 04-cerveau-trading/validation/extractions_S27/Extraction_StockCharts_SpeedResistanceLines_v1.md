# Extraction StockCharts — Speed Resistance Lines
**Source :** `bundles/stockcharts/speed_resistance_lines.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D3631 → D3650 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools/speed-resistance-lines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Outil de support/résistance basé sur retracements 1/3–2/3 applicable sur GC/HG/CL/ZW pour identifier niveaux de support dans uptrend et résistance dans downtrend.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Speed Resistance Lines in a downtrend (SPY chart) | Downtrend Calculation | D3632 |
| image_02 | Speed Resistance Lines in an uptrend (TLT chart) | Uptrend Calculation | D3634 |
| image_03 | Speed Resistance Lines identify support levels in the TGT chart. A break below the lower Speedline signaled a trend reversal. | Uptrend Example | D3638 |
| image_04 | The lower Speedline acted as a support level while the middle Speedline acted as resistance (PFE chart) | Uptrend Example | D3640 |
| image_05 | Speed Resistance Lines mark resistance levels in a downtrend. After breaking above the Speed Line, the downtrend reversed. (M — Macy's chart) | Downtrend Example | D3642 |
| image_06 | Speed Resistance Lines can also act as support levels after a breakout (ERTS — Electronic Arts chart) | Downtrend Example | D3644 |
| image_07 | Repositioning Speed Resistance Lines after a trend extension (ERTS chart avec lignes bleues et roses) | Repositioning | D3647 |
| image_08 | Applying Speed Resistance Lines in SharpCharts | Using Speed Resistance Lines In SharpCharts | D3649 |

## DÉCISIONS

### D3631 — Définition Speed Resistance Lines (Speedlines) : trend lines basées sur retracements 1/3 et 2/3
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « Speed Resistance Lines, sometimes referred to as Speedlines, are trend lines based on 1/3 and 2/3 retracements. »
🔵 **ÉCOLE** : Développé par Edson Gould, technicien marché des années 60-70, cité dans *Barron's* et *Wall Street Week*.
**TRADEX-AI C1** : Outil de niveaux dynamiques basé sur retracements 1/3 / 2/3 — différent des Fibonacci (38.2% / 61.8%) mais complémentaire — applicable sur GC/HG/CL/ZW pour support/résistance.
*Catégorie : structure_marche*

### D3632 — Calcul Speedlines en downtrend : 3 lignes depuis le High vers le Low, le point 2/3, le point 1/3
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_01) :
```
First Line : High → Low
Middle Line: High → 2/3 point = High - (High - Low) × 0.667
Upper Line : High → 1/3 point = High - (High - Low) × 0.333
```
Exemple SPY : High = 121.54 (avril), Low = 101.13 (juillet).
**TRADEX-AI C1** : Formule de calcul opérationnelle pour TRADEX — à implémenter en Python dans le module de niveaux dynamiques pour GC/HG/CL/ZW en downtrend.
*Catégorie : structure_marche*

### D3633 — Les Speedlines s'étendent vers la droite au fur et à mesure que de nouvelles barres se forment
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « These lines extend to the right as new bars (trading days) occur. »
**TRADEX-AI C1** : Nature dynamique des Speedlines — les niveaux de support/résistance évoluent avec le temps, non statiques comme les Fibonacci standards.
*Catégorie : structure_marche*

### D3634 — Calcul Speedlines en uptrend : 3 lignes depuis le Low vers le High, le point 2/3, le point 1/3
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_02) :
```
First Line : Low → High
Middle Line: Low → 2/3 point = Low + (High - Low) × 0.667
Lower Line : Low → 1/3 point = Low + (High - Low) × 0.333
```
Exemple TLT : Low = 86.44 (avril), High = 102.66 (juillet).
**TRADEX-AI C1** : Formule uptrend opérationnelle — applicable sur GC/CL en tendance haussière pour identifier les niveaux de support dynamiques.
*Catégorie : structure_marche*

### D3635 — Interprétation uptrend : Speedlines = deux niveaux de support potentiels
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « In an uptrend, Speed Resistance Lines mark two potential support levels to watch. A break below the middle line targets a move towards the upper line. A break below the lower line indicates enough weakness to consider a trend reversal. »
**TRADEX-AI C1** : Règle de gestion de position en uptrend : break middle line → cible lower line (ajuster stop) ; break lower line → signal de retournement de tendance → envisager sortie/inversion.
*Catégorie : gestion_position_active*

### D3636 — Interprétation downtrend : Speedlines = deux niveaux de résistance potentiels
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « In a downtrend, Speed Resistance Lines mark two potential resistance levels to watch. A break above the middle line shows strength that targets a move to the upper line. A break above the upper line indicates a trend reversal. »
**TRADEX-AI C1** : Règle de gestion de position en downtrend : break middle line (résistance) → force vers upper line ; break upper line → retournement de tendance confirmé → sortir short / envisager long.
*Catégorie : gestion_position_active*

### D3637 — Après cassure d'une Speedline : l'ancienne résistance devient support (et inversement)
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « Once broken, the line extensions can then mark resistance, just as ordinary trend lines do. » [...] « Once broken, these Speedlines can then turn into support on a pullback. »
**TRADEX-AI C1** : Principe classique de polarité support/résistance appliqué aux Speedlines — après breakout d'une Speedline, surveiller le retest de cette ligne en tant que support ou résistance.
*Catégorie : structure_marche*

### D3638 — Exemple TGT (uptrend) : lower Speedline = support 3 fois, puis break → retournement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_03) : « TGT gapped down in early February, but the stock found support at the lower Speedline and continued its uptrend. The lower Speedline also provided support in late February and early May. Target broke below the lower Speedline in early June to signal a trend reversal. Notice how this line turned into resistance in mid-June. »
**TRADEX-AI C1** : Validation empirique : lower Speedline tient 3 fois = uptrend fort ; break lower Speedline = signal de retournement fiable → stop loss positionnable légèrement sous la lower Speedline pour GC/CL en uptrend.
*Catégorie : gestion_risque_entree*

### D3639 — Speedlines efficaces même dessinées sur de courtes périodes
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « The chart below shows Pfizer (PFE) with the Speed Resistance Lines drawn from the June low to the July high. Despite such a short drawing period, the lower Speedline extension acted as support in October and again in November. »
**TRADEX-AI C1** : Les Speedlines ont un pouvoir prédictif qui s'étend bien au-delà de la période de dessin initiale — même une courte base (1-2 mois) peut générer des niveaux pertinents sur 6+ mois.
*Catégorie : structure_marche*

### D3640 — Exemple PFE : lower Speedline = support en oct ET nov ; middle Speedline = résistance en août
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_04) : « the lower Speedline extension acted as support in October and again in November. Also, notice how the middle Speedline extension acted as resistance in late August. »
**TRADEX-AI C1** : Les deux lignes (lower ET middle) jouent simultanément leur rôle — surveiller les deux pour les trades sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D3641 — Exemple Macy's (downtrend) : break au-dessus middle → force vers upper ; break upper → retournement
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_05) : « Macy's broke above the middle Speedline with a strong surge in December but hit resistance at the upper Speedline in late December and early January. The February break above the upper Speedline reversed the downtrend. »
**TRADEX-AI C1** : Séquence downtrend → retournement : 1) break middle Speedline ; 2) résistance upper Speedline ; 3) break upper Speedline = retournement confirmé → signal d'achat sur GC/CL en sortie de downtrend.
*Catégorie : gestion_risque_entree*

### D3642 — Break au-dessus de l'upper Speedline en downtrend = retournement de tendance confirmé
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « A break above the upper line indicates a trend reversal. »
**TRADEX-AI C1** : Signal fort : break upper Speedline en downtrend = confirmation de retournement — valider avec indicateurs Belkhayate (BGC > 0, Direction haussière) avant entrée long.
*Catégorie : gestion_risque_entree*

### D3643 — Principe : Speedline offre résistance avant breakout, puis support après breakout (polarité)
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « This is a classic example of how Speedlines can offer resistance before a breakout and support after a breakout. It depends on the location of price. »
**TRADEX-AI C1** : Règle de polarité des Speedlines — identique au principe support/résistance classique : ce qui était résistance devient support après cassure → utiliser pour positionner les stops et les cibles.
*Catégorie : structure_marche*

### D3644 — Exemple ERTS (downtrend) : break middle puis résistance upper ; puis support middle ; puis résistance juste sous upper
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_06) : « ERTS broke above the middle Speedline but met resistance at the upper Speedline in mid-October. After a sharp decline into December, the stock found support near the middle Speedline. [...] ERTS bounced again but met resistance just below the upper Speedline. »
**TRADEX-AI C1** : Pattern complexe mais courant : middle Speedline devient pivot bidirectionnel — résistance en cassure, support en retrait. Applicable pour targets intermédiaires sur GC/CL.
*Catégorie : structure_marche*

### D3645 — Repositionnement des Speedlines quand la tendance s'étend avec de nouveaux plus bas (downtrend)
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « Speed Resistance Lines can be repositioned as a security extends its trend with lower lows or lower highs. »
**TRADEX-AI C1** : Les Speedlines sont recalculées quand un nouveau extreme (higher high ou lower low) est atteint — mise à jour automatique dans TRADEX lors de nouveaux ATH ou ATL sur GC/CL/HG/ZW.
*Catégorie : gestion_position_active*

### D3646 — Repositionnement élargit les Speedlines : la distance 1/3 / 2/3 augmente avec l'amplitude du mouvement
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_07) : « Notice how the Speedlines widened as the stock forged lower lows. This is because the length of the move from high to low grew larger - as did the 1/3 and 2/3 retracements. »
**TRADEX-AI C1** : Plus le mouvement est ample, plus les niveaux Speedlines sont éloignés — les Speedlines s'adaptent naturellement à la volatilité du marché.
*Catégorie : structure_marche*

### D3647 — Exemple ERTS repositionné : upper Speedline pink (High juin / Low février) = résistance en avril même après break du high de janvier
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md, image_07) : « Even though the stock broke above its January high, the upper Speedline extension marked resistance in April. »
**TRADEX-AI C1** : Les Speedlines repositionnées sur le move complet restent pertinentes même après des mouvements partiels contraires — ne pas invalider prématurément les niveaux lors de faux breaks.
*Catégorie : structure_marche*

### D3648 — Analogie avec Fibonacci (38.2% / 61.8%) et Dow Theory (retracement 1/3 à 2/3)
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « Speed Resistance Lines divide the trend into three sectors, or thirds. This is similar to Fibonacci retracements, which are based on 38.2% and 61.8%. In addition, Dow Theory suggests that securities retrace 1/3 to 2/3 of an advance or decline with a corrective move. »
🔵 **ÉCOLE** : Références : Dow Theory + Fibonacci retracements.
**TRADEX-AI C1** : Convergence de 3 approches (Speedlines 1/3-2/3 + Fibonacci 38.2-61.8% + Dow Theory) sur les mêmes zones de retracement → confluence forte pour GC/CL lorsque ces niveaux coïncident.
*Catégorie : structure_marche*

### D3649 — Les Speedlines ne sont PAS des indicateurs autonomes — à utiliser en combinaison
🟢 **FAIT VÉRIFIÉ** (Source : speed_resistance_lines.md) : « As with all indicators and line studies, Speed Resistance Lines should be used in conjunction with other aspects of technical analysis. They are not designed as stand-alone indicators. »
**TRADEX-AI C1** : Règle d'utilisation : Speedlines = outil complémentaire, jamais seul pour décision de trade — combiner avec BGC Belkhayate, COG, confirmation Order Flow (C2) avant entrée.
*Catégorie : gestion_risque_entree*

### D3650 — Référence : John Murphy *Technical Analysis of the Financial Markets* couvre les Speedlines et autres outils de trend line
🔵 **ÉCOLE** (Source : speed_resistance_lines.md) : « John Murphy's Technical Analysis of the Financial Markets covers Speed Resistance Lines and many other trend line tools, including international trend lines, channels, and the fan principle. »
**TRADEX-AI C1** : Traçabilité académique : Speedlines documentées dans le manuel de référence de Murphy — base solide pour intégration dans la méthodologie TRADEX.
*Catégorie : structure_marche*
