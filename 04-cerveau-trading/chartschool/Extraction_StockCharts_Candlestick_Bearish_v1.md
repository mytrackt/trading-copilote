# Extraction_StockCharts_Candlestick_Bearish_v1.md
**Source :** StockCharts ChartSchool — Candlestick Bearish Reversal Patterns  
**URL :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlestick-bearish-reversal-patterns  
**Décisions :** D89 → D98  
**Images certifiées :** 11/11 (double ancrage v3.2)  
**Date extraction :** 23/06/2026  

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — PRINCIPES DES RETOURNEMENTS BAISSIERS

### D89 — Retournement baissier : définition, pré-requis tendance et confirmation (image_01)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §What Is a Bearish Reversal + §There Must Be an Existing Uptrend + §How Do You Confirm + image_01 · label certifié : A long black candlestick following the dark cloud cover confirmed the bearish reversal) : Un pattern de retournement baissier signale un changement potentiel d'une tendance haussière vers une tendance baissière. **Il doit exister une tendance haussière préalable** (court terme suffit) — un pattern baissier dans une tendance baissière est un pattern de continuation.

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §How Do You Confirm) : Confirmation baissière = suivi à la baisse (gap down, longue bougie noire, ou repli à fort volume), à venir dans les **1 à 3 jours**. Sans confirmation, le pattern est neutre (niveau de résistance potentiel au mieux). Tendance haussière identifiable : cours > EMA 20j · pics/creux croissants · cours > trend line.

**TRADEX-AI C1/C3** : Gate symétrique du haussier — pattern baissier valide seulement si régime préalable haussier (C1) + confirmation sous 1–3 barres avant entrée SHORT.

---

## BLOC 2 — PATTERNS BAISSIERS À 2-3 BOUGIES

### D90 — Bearish Abandoned Baby (image_02)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Bearish Abandoned Baby + image_02 · label certifié : The abandoned baby marked a sharp trend reversal) : Trois bougies — (1) longue blanche, (2) **doji qui gappe au-dessus du plus haut** précédent, (3) longue noire qui **gappe sous le plus bas** du doji. Différence avec l'evening doji star : les gaps de part et d'autre du doji. Aucune confirmation supplémentaire requise.

**TRADEX-AI C3** : Pattern fort à double gap autour d'un doji. ⚠️ Gaps rares sur futures 24h → pattern peu fréquent en intraday continu (NQ/ES/Gold).

---

### D91 — Bearish Engulfing (image_03)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Bearish Engulfing + image_03 · label certifié : A bearish engulfing pattern confirmed the trend reversal and a break of a support level) : Deux bougies — 1re blanche, 2de noire. Le corps noir doit **englober totalement** le corps blanc précédent (idéalement aussi les ombres). Plus la bougie noire est grande, plus le retournement est baissier. Confirmation requise.

🔵 **ÉCOLE** (Source : candlestick_bearish.md note) : Similaire à l'outside reversal day, mais n'exige d'englober que l'open/close (pas tout le range).

**TRADEX-AI C1/C3** : Miroir exact du bullish engulfing (D80) — détection sur englobement open/close.

---

### D92 — Bearish Harami et ses 4 combinaisons (images_04/05/06)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Bearish Harami + image_04 · label certifié : Examples of bearish harami patterns. + image_05 · label certifié : A bearish harami pattern with a long black candlestick and small black candlestick… + image_06 · label certifié : A bearish harami with a long white candlestick and a small black candlestick…) : Deux bougies — 1re à grand corps, 2de à petit corps **englobé**. Quatre combinaisons : **blanc/blanc, blanc/noir, noir/blanc, noir/noir**. Plus le 2d corps est petit, plus le retournement est probable ; un doji augmente les chances. Les harami sont baissiers après une avancée, haussiers après un déclin (nature = contexte tendance).

🔵 **ÉCOLE** (Source : candlestick_bearish.md, Nison *Beyond Candlesticks*) : Les harami les plus baissiers sont noir/blanc ou noir/noir (1re bougie noire = hausse soudaine de la pression vendeuse).

**TRADEX-AI C1/C3** : Même structure que le harami haussier (D82) — désambiguïsation par le contexte de tendance.

---

### D93 — Dark Cloud Cover (image_07)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Dark Cloud Cover + image_07 · label certifié : A dark cloud cover confirmed the trend reversal) : Deux bougies à grands corps — 1re blanche, 2de noire. La noire **ouvre au-dessus de la clôture précédente** et **clôture sous le milieu du corps** de la bougie blanche. Une clôture au-dessus du milieu ne serait pas baissière. Confirmation requise.

**TRADEX-AI C3** : Miroir baissier du piercing pattern (D81) — seuil : clôture 2de bougie < 50 % du corps de la 1re.

---

### D94 — Evening Star / Evening Doji Star (image_08)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Evening Star + image_08 · label certifié : An evening star candlestick pattern marked a trend reversal) : Trois bougies — (1) longue blanche, (2) petite bougie qui **gappe au-dessus** de la clôture précédente (doji = evening doji star ; spinning top possible), (3) longue noire de confirmation. Un doji en 2de bougie augmente les chances de retournement.

**TRADEX-AI C1/C3** : Miroir baissier du morning star (D84) — la 3e bougie noire = confirmation intégrée.

---

### D95 — Shooting Star (image_09)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Shooting Star + image_09 · label certifié : A shooting star candlestick pattern marks a bearish trend reversal) : Une bougie à petit corps, **longue ombre haute** (≥ 2× le corps), ombre basse petite/inexistante, range high/low grand vs 10-20 derniers jours. En position « star », elle doit gapper depuis la bougie précédente.

🔵 **ÉCOLE** (Source : candlestick_bearish.md §Shooting Star) : Greg Morris (*Candlestick Charting Explained*) exige un gap up ; Steve Nison (*Beyond Candlesticks*) accepte une formation sous la clôture précédente. Le gap up renforce la robustesse mais n'est pas indispensable.

**TRADEX-AI C3** : Miroir baissier du hammer (D83) — ratio ombre haute / corps ≥ 2. Le gap est optionnel (utile sur futures où les gaps sont rares).

---

## BLOC 3 — OUTILS COMPLÉMENTAIRES

### D96 — Confirmation par la résistance (image_10)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Resistance + image_10 · label certifié : After hitting a resistance level, the bearish engulfing pattern confirmed the trend reversal) : Augmenter la robustesse en cherchant les retournements baissiers **aux niveaux de résistance**. Exemple Nike (NKE) : engulfing baissier à la résistance ~53 $, confirmé par déclin + gap down + cassure de trend line.

**TRADEX-AI C1** : Pondérer le score d'un pattern baissier par sa proximité à une résistance identifiée (confluence) — symétrique de D86.

---

### D97 — Confirmation par le momentum

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Momentum) : Confirmer l'affaiblissement du momentum via **divergences négatives** sur MACD, PPO, Stochastique, RSI, StochRSI, Williams %R. Les croisements baissiers de MA sur PPO/MACD et les croisements de trigger line du Slow Stochastic apportent confirmation.

**TRADEX-AI C3** : Lien KB — divergence négative RSI (D18–D39) / MACD (D40–D61) + croisement signal baissier MACD (D60) en confluence avec un pattern baissier renforce le SHORT.

---

### D98 — Confirmation par le money flow + signal combiné (image_11)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bearish.md §Money Flows + image_11 · label certifié : After trading at a resistance level, the dark cloud cover pattern marked a trend reversal. This was further confirmed by a negative divergence in the MACD and weak money flow…) : Indicateurs volume (OBV, CMF, A/D Line) pour repérer divergences négatives / pression vendeuse excessive. **Signal ultime** = pattern baissier PRÈS d'une résistance AVEC momentum faiblissant ET pression vendeuse — rare mais à potentiel supérieur à la moyenne.

**TRADEX-AI C2/C3** : Confluence triple (résistance + momentum + flux volume) = signal baissier de plus haute qualité. Symétrique de D88, cohérent avec la grille /10.

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D89
Dernière décision session  : D98
Prochaine décision         : D99
Total décisions            : 10
Total KB cumulé            : D1 → D98
```

---

*Extraction_StockCharts_Candlestick_Bearish_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
