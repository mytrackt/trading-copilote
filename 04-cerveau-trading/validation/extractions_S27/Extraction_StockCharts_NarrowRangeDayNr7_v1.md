# Extraction StockCharts — Narrow Range Day NR7
**Source :** `bundles/stockcharts/narrow_range_day_nr7.md` (HTTP 200 · ~11 000 car.) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées
**Décisions :** D2751 → D2763 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/narrow-range-day-nr7
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Table | Image | Label certifié | Section | Décision liée |
|-------|-------|----------------|---------|---------------|
| — | image_01.png | Chart 1 - Narrow Range Days | Strategy | D2753 |
| — | image_02.png | Chart 2 - Narrow Range Days | Strategy | D2753 |
| — | image_03.png | Chart 3 - Narrow Range Days | Trading Example | D2756 |
| — | image_04.png | Chart 4 - Narrow Range Days | SharpCharts Alternatives | D2758 |
| — | image_05.png | Chart 5 - Narrow Range Days | Tweaking | D2760 |

## DÉCISIONS

### D2751 — Origine et principe (Toby Crabel, contraction → expansion)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « Narrow range patterns come from Toby Crabel's book, Day Trading with Short Term Price Patterns & Opening Range Breakout (1990). (…) the NR4 and NR7 patterns are quite popular with short-term traders. The philosophy behind the pattern is similar to the Bollinger Band Squeeze, that is, a volatility expansion often follows a volatility contraction. Narrow range days mark price contractions that often precede price expansions. »
**TRADEX-AI C1** : Modèle de breakout de volatilité (Crabel) — la contraction du range précède l'expansion. Logique identique au Bollinger Squeeze. Cabler comme détecteur de compression précédant un mouvement sur GC/HG/CL/ZW (Crabel tradait des futures).
*Catégorie : structure_marche*
---

### D2752 — Définition NR4 / NR7 (range absolu)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « This strategy starts with the day's range, which is simply the difference between the high and the low. Crabel used the absolute range, as opposed to the percentage range. (…) An NR4 pattern would be the narrowest range in four days, while an NR7 would be the narrowest range in seven days. »
**TRADEX-AI C1** : NR7 = barre dont le range (High-Low absolu) est le plus étroit des 7 dernières barres. Définition déterministe, codable directement depuis NT8. NR4 = variante sur 4 barres. Transposable du « day » au « range bar » selon le mode Belkhayate.
*Catégorie : structure_marche*
---

### D2753 — Déclenchement par opening range breakout
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md, image_01, image_02) : « It is a very short-term pattern designed to initiate a trade based on an "opening range breakout" (ORB) (…) based on the price range in the first five minutes of trading (…). Instead, chartists can look for an upside breakout when prices move above the high of the narrow range day and a downside breakdown when prices move below the low of the narrow range day. »
**TRADEX-AI C1** : Déclencheur = cassure du haut (long) ou du bas (short) de la barre NR7. L'ORB 5 min de Crabel est jugé trop court par l'article → règle retenue = breakout du high/low de la barre étroite. Niveaux d'entrée objectifs et codables.
*Catégorie : signal*
---

### D2754 — Invalidation immédiate (le trade doit fonctionner tout de suite)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « Because this is a short-term setup, it is important that the trade starts working right away. Failure to continue in the direction of the signal is the first warning. After a buy signal, a move below the low of the narrow range day would be negative. Conversely, a move above the high of the narrow range day would negate a sell signal. »
**TRADEX-AI C1** : Invalidation nette — un long est annulé si le prix repasse sous le low NR7 ; un short si le prix repasse au-dessus du high NR7. Logique de stop structurel immédiat, exploitable par le risk_manager (sortie rapide si pas de suivi).
*Catégorie : gestion_risque_entree*
---

### D2755 — Cibles de profit et stops (Parabolic SAR / ATR)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « Crabel took profits quite quickly, usually at the close of the first trading day or on the first profitable close. (…) profits can be taken near the next resistance level or a percentage target. For stops, chartists can use the Parabolic SAR to trail stops or base their stops on the Average True Range (ATR). For example, the stop-loss on a long position could be set two Average True Range values below current prices and trailed higher. »
**TRADEX-AI C1** : Gestion de sortie — prise de profit rapide (1ère clôture profitable ou résistance suivante), stop trailing via SAR ou « 2× ATR » sous le prix. Paramètre stop = 2 ATR, codable. Cohérent avec un risk_manager basé volatilité.
*Catégorie : gestion_risque_entree*
---

### D2756 — Récapitulatif des signaux Bull / Bear
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md, image_03) : « Bull Signal Recap: 1. Identify NR4 or NR7 day. 2. Buy on move above high of narrow range day high. Bear Signal Recap: 1. Identify NR4 or NR7 day. 2. Sell on move below low of narrow range day low. » Exemple Morgan Stanley : 12 signaux en <3 mois, NR7 parfois back-to-back affirmant le signal précédent.
**TRADEX-AI C1** : Règle binaire claire (identifier NR7 → acheter au-dessus du high / vendre sous le low). Note de fréquence : nombreux signaux sur courte période → besoin de filtres (cf. D2761). NR7 consécutifs ne créent pas de signaux contradictoires.
*Catégorie : signal*
---

### D2757 — Neutralité directionnelle du NR7
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « The NR7 day is based on the premise that range contractions are followed by range expansions. In this regard, the indicator is neutral when it comes to future price direction. As with Bollinger Bands, chartists must employ other tools for a directional bias. »
**TRADEX-AI C1** : Garde-fou clé — le NR7 prédit l'expansion de volatilité, PAS la direction. Doit obligatoirement être couplé à un filtre directionnel (tendance). Empêche de trader le breakout à l'aveugle. Aligné avec la règle « jamais un seul critère ».
*Catégorie : structure_marche*
---

### D2758 — Proxy SharpCharts via ATR 1-période (NATR7)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md, image_04) : « SharpCharts does not offer an indicator that shows the day's range or identifies NR4 and NR7 days. (…) chartists can use a 1-period Average True Range (ATR) to imitate or estimate the "range" and visually identify "NATR7" readings, which means ATR is its narrowest in seven days. While this NATR7 will not produce the exact same signals, many will overlap. »
**TRADEX-AI C1** : Proxy implémentable — ATR(1) à son plus bas sur 7 barres ≈ NR7. Approximation (overlap partiel, pas identique). Pour TRADEX-AI, calculer directement le range High-Low (exact) plutôt que le proxy ATR, puisque NT8 fournit les barres.
*Catégorie : configuration*
---

### D2759 — Risque élevé de whipsaw (range étroit par nature)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « Because NR7 days are relatively commonplace and the range is small by definition, the chances of whipsaw are above average. A break above the NR7 high can fail and be followed by a break below the NR7 high. Keep the bigger picture in mind and be wary of sell signals within a bullish pattern, such as a falling flag or at a support test. »
**TRADEX-AI C1** : Garde-fou whipsaw — le faible range rend les fausses cassures fréquentes. Se méfier des signaux contraires au contexte (ex. vente dans un drapeau haussier / sur test de support). Pondération prudente dans la grille /10, jamais éliminatoire seul.
*Catégorie : gestion_risque_entree*
---

### D2760 — Qualification par filtres tendance + surachat/survente
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md, image_05) : « it is often a good idea to add a trend indicator and an overbought/oversold indicator. (…) A bullish signal occurs when Aroon Up is above Aroon Down (uptrend), the 5-day low for CCI is below -100 (oversold) and the range moves to a seven day low (turning point). Bearish signals occur when Aroon Down is above Aroon Up (downtrend), the 5-day high for CCI is above +100 (overbought) and the range moves to a seven day low. »
**TRADEX-AI C1** : Configuration qualifiée = NR7 + filtre tendance (Aroon) + filtre OB/OS (CCI ±100). Triple condition alignée = renfort de score. Attention multicollinéarité : Aroon et CCI sont de catégories différentes (tendance vs momentum) → confirmation valide.
*Catégorie : configuration*
---

### D2761 — Fréquence des NR7 et ajustement du nombre de périodes
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « Most chartists will want to qualify NR7 signals, as they are quite frequent. A typical stock will produce dozens of NR7 days in a twelve-month period (…). A decrease from NR7 to NR4 would increase the number of stocks fitting the criteria, while an increase from NR7 to NR20 would decrease the number of candidates. »
**TRADEX-AI C1** : Paramètre N de la fenêtre (NR4/NR7/NR20) = curseur de sélectivité. Plus N est grand, plus le signal est rare et significatif. À calibrer selon le nombre de signaux souhaité par actif/timeframe.
*Catégorie : configuration*
---

### D2762 — Scan NR7 haussier en tendance après pullback (seuils)
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : Scan haussier — « [Range < 1 day ago Min (6, Range)] and [today's high < yesterday's high] and [today's low > yesterday's low] and [Min (5, CCI(10)) < -100] and [Aroon Up (63) > Aroon Down(63)] » (+ filtres liquidité : sma(20,volume)>100000, sma(60,close)>20). Scan baissier = CCI(10) max(5) > 100 et Aroon Up(63) < Aroon Down(63).
**TRADEX-AI C1** : Code de scan littéral transposable. Le NR7 y est exprimé par « Range plus étroit que le min des 6 barres précédentes » + barre inside (high < veille, low > veille). CCI(10) seuils ±100, Aroon(63) pour la tendance. Réutilisable comme règle déterministe NT8.
*Catégorie : signal*
---

### D2763 — Cadrage final : point de départ, pas système complet
🟢 **FAIT VÉRIFIÉ** (Source : narrow_range_day_nr7.md) : « This article is designed as a starting point for trading system development. Use these ideas to augment your trading style, risk-reward preferences and personal judgments. »
**TRADEX-AI C1** : Cadrage projet — le NR7 est une brique de détection de compression à intégrer, pas un système autonome. À combiner avec direction (C1 Belkhayate), filtres et risk management avant tout signal exécutable.
*Catégorie : structure_marche*
---

## SYNTHÈSE
| Champ | Valeur |
|-------|--------|
| Décisions ajoutées | 13 (D2751 → D2763) |
| Images citées | 5/5 certifiées |
| Catégories | structure_marche, signal, gestion_risque_entree, configuration |
| Cercle dominant | C1 (prix / structure / volatilité) |
| Tags | 🟢 FAIT VÉRIFIÉ ×13 |
| Belkhayate | Aucun lien affirmé par la source. Rapprochement possible : le NR7 (compression → expansion) peut alimenter le timing des modes Range Bar / Scalping Belkhayate ⚫🔴 hypothèse projet, non affirmée par la source. NR7 neutre en direction → toujours subordonné à la lecture de direction Belkhayate (C1). |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, NON fusionnée dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur.
