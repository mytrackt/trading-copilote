# Extraction_StockCharts_Candlestick_Bullish_v1.md
**Source :** StockCharts ChartSchool — Candlestick Bullish Reversal Patterns  
**URL :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlestick-bullish-reversal-patterns  
**Décisions :** D78 → D88  
**Images certifiées :** 10/10 (double ancrage v3.2)  
**Date extraction :** 23/06/2026  

---

⚠️ *Outil éducatif uniquement · Jamais du conseil financier · Aucune exécution automatique d'ordre*

---

## BLOC 1 — PRINCIPES DES RETOURNEMENTS HAUSSIERS

### D78 — Retournement haussier : définition et pré-requis tendance (image_01)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §What Is a Bullish Reversal + §There Must Be an Existing Downtrend) : Un pattern de retournement haussier signale un changement potentiel d'une tendance baissière vers une tendance haussière (sentiment passant de la vente à l'achat). **Il doit exister une tendance baissière préalable à renverser** — un engulfing haussier sur de nouveaux plus hauts est un pattern de continuation, pas un retournement.

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §There Must Be… + image_01 · label certifié : A bullish engulfing pattern formed near a resistance level showing strength…) : Tendance baissière identifiable par : cours sous l'EMA 20j · chaque pic/creux inférieur au précédent · cours sous une trend line.

**TRADEX-AI C1** : Gate de contexte obligatoire — un pattern de bougie haussier n'est valide comme retournement que si le régime préalable est baissier (filtre EMA 20 / structure / ADX).

---

### D79 — Confirmation haussière

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §How Do You Confirm a Bullish Reversal) : La plupart des patterns exigent une **confirmation haussière** : gap up, longue bougie blanche, ou avancée à fort volume. Les patterns chandeliers sont court terme (efficaces ~1 à 2 semaines) → la confirmation doit venir dans les **1 à 3 jours** suivant le pattern. Sans confirmation, le pattern est neutre (au mieux un niveau de support potentiel).

**TRADEX-AI C3/gestion_risque_entree** : Ne jamais entrer sur le seul pattern — exiger une confirmation (gap/volume/bougie) sous 1–3 barres sur NQ/ES/Gold.

---

## BLOC 2 — PATTERNS HAUSSIERS À 2 BOUGIES

### D80 — Bullish Engulfing (image_02)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Bullish Engulfing + image_02 · label certifié : Bullish engulfing patterns foreshadowed two significant advances) : Deux bougies — la 1re noire, la 2de blanche. Le corps blanc doit **englober totalement** le corps de la bougie noire précédente (idéalement aussi les ombres). Plus la bougie blanche est grande et l'englobement important, plus le retournement est haussier. Confirmation supplémentaire requise.

🔵 **ÉCOLE** (Source : candlestick_bullish.md §Bullish Engulfing, note) : Similaire à l'outside reversal day, mais n'exige d'englober que l'ouverture et la clôture (pas tout le range high/low).

**TRADEX-AI C1/C3** : Pattern 2 bougies à englobement open/close — coder la détection sur clôtures.

---

### D81 — Piercing Pattern (image_03)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Piercing Pattern + image_03 · label certifié : A piercing pattern confirmed the support level after which the stock advanced) : Deux bougies à corps relativement grands — 1re noire, 2de blanche. La blanche **ouvre sous la clôture précédente** et **clôture au-dessus du milieu du corps** de la bougie noire. Une clôture sous le milieu ne serait pas considérée comme haussière.

**TRADEX-AI C3** : Seuil mesurable — clôture de la 2de bougie > 50 % du corps de la 1re. Combiner avec un niveau de support.

---

### D82 — Bullish Harami et ses 4 combinaisons (images_04/05)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Bullish Harami + image_04 · label certifié : Examples of harami candlesticks. + image_05 · label certifié : A bullish harami formed at support…) : Deux bougies — la 1re à grand corps, la 2de à petit corps **englobé** par la 1re. Quatre combinaisons : **blanc/blanc, blanc/noir, noir/blanc, noir/noir**. Plus le 2d corps est petit, plus le retournement est probable ; un doji en 2de bougie augmente les chances.

🔵 **ÉCOLE** (Source : candlestick_bullish.md §Bullish Harami, Nison *Beyond Candlesticks*) : Les harami les plus haussiers sont blanc/noir ou blanc/blanc (1re bougie blanche = résurgence d'achat ; petite bougie = consolidation). Les harami partagent la même forme en haussier ou baissier — leur nature dépend de la tendance préalable.

**TRADEX-AI C1/C3** : Harami = pattern d'indécision/consolidation post-tendance — nature (haussier/baissier) déterminée par le contexte de tendance (C1).

---

## BLOC 3 — PATTERNS HAUSSIERS À 1 ET 3 BOUGIES

### D83 — Hammer (image_06)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Hammer + image_06 · label certifié : The hammer confirmed the support level after which the stock advanced sharply) : Une bougie (blanche ou noire) à petit corps, **longue ombre basse** et ombre haute petite/inexistante. L'ombre basse doit faire **au moins 2× la longueur du corps** ; le range high/low doit être grand par rapport aux 10-20 derniers jours. Confirmation requise.

**TRADEX-AI C3** : Détection — ratio ombre basse / corps ≥ 2 ET range élevé vs N dernières barres. Confirmer avant entrée.

---

### D84 — Morning Star / Morning Doji Star (image_07)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Morning Star + image_07 · label certifié : A morning doji star was followed by a strong three-day advance…) : Trois bougies — (1) longue noire, (2) petite bougie (blanche/noire) qui **gappe sous** la clôture précédente (doji = morning doji star), (3) longue blanche de confirmation. Si la 2de est un doji, les chances de retournement augmentent. Les versions doji star sont des retournements forts ne nécessitant pas de confirmation supplémentaire au-delà de la 3e bougie blanche.

**TRADEX-AI C1/C3** : Pattern 3 bougies de retournement — la 3e bougie blanche fait office de confirmation intégrée.

---

### D85 — Bullish Abandoned Baby (image_08)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Bullish Abandoned Baby + image_08 · label certifié : The bullish abandoned baby was the reversal pattern that indicated the trend reversal) : Trois bougies — (1) longue noire, (2) **doji qui gappe sous le plus bas** de la précédente, (3) longue blanche qui **gappe au-dessus du plus haut** du doji. Différence avec le morning doji star : les **gaps de part et d'autre du doji**. Aucune confirmation supplémentaire requise.

**TRADEX-AI C3** : Pattern rare et fort — détection par double gap autour d'un doji. ⚠️ Les gaps sont rares sur futures 24h (NQ/ES/Gold) — pattern peu fréquent en intraday continu.

---

## BLOC 4 — OUTILS COMPLÉMENTAIRES

### D86 — Confirmation par le support (image_09)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Support + image_09 · label certifié : Bullish reversal pattern at a Fibonacci retracement level marks a support level) : Pour augmenter la robustesse, chercher les retournements haussiers **aux niveaux de support** (moyennes mobiles, reaction lows précédents, trend lines, retracements Fibonacci).

**TRADEX-AI C1** : Pondérer le score d'un pattern haussier par sa proximité à un support identifié (confluence).

---

### D87 — Confirmation par le momentum

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Momentum) : Utiliser des oscillateurs pour confirmer l'amélioration du momentum : **divergences positives** sur MACD, PPO, Stochastique, RSI, StochRSI, Williams %R augmentent la robustesse du retournement haussier.

**TRADEX-AI C3** : Lien direct avec la KB existante — divergence positive RSI (D18–D39) / MACD (D40–D61) en confluence avec un pattern haussier renforce le signal.

---

### D88 — Confirmation par le money flow + signal combiné (image_10)

🟢 **FAIT VÉRIFIÉ** (Source : candlestick_bullish.md §Money Flow + image_10 · label certifié : A bullish engulfing pattern, a positive divergence in the stochastic oscillator, and an improving CMF confirmed the strong advance…) : Les indicateurs basés volume (OBV, Chaikin Money Flow, Accumulation/Distribution Line) aident à identifier la pression acheteuse/vendeuse. **Signal ultime** = pattern haussier PRÈS d'un support AVEC divergences positives ET signes de pression acheteuse.

**TRADEX-AI C2/C3** : Confluence triple (support + momentum + flux volume) = signal haussier de plus haute qualité. Cohérent avec la grille de score /10 (plusieurs cercles alignés).

---

## RÉSUMÉ COMPTEUR

```
Première décision session : D78
Dernière décision session  : D88
Prochaine décision         : D89
Total décisions            : 11
Total KB cumulé            : D1 → D88
```

---

*Extraction_StockCharts_Candlestick_Bullish_v1.md · TRADEX-AI · 23/06/2026*  
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
