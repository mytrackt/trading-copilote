# Extraction StockCharts — P&F Signal Reversed (Bullish/Bearish)
**Source :** `bundles/stockcharts/p_and_f_signal_reversed.md` (HTTP 200) + 8 images certifiées
**Méthode images :** double ancrage · 8/8 certifiées · 0 à vérifier
**Décisions :** D2971 → D2980 · **Page :** chartschool.stockcharts.com/.../classic-patterns/p-and-f-signal-reversed
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Bullish Signal Reversed (2 higher highs + Double Bottom Breakdown) | Bullish Signal Reversed | D2972 |
| image_02 | Bullish Signal Reversed (TROW) | Bullish Signal Reversed | D2972 |
| image_03 | Reversal (new high avant Double Bottom Breakdown) | Reversals and Continuations | D2974 |
| image_04 | Continuation Bullish Signal Reversed | Reversals and Continuations | D2975 |
| image_05 | Two Bearish Signal Reversed (ATHR) | Bearish Signal Reversed | D2976 |
| image_06 | Bearish Signal Reversed failed to hold (BIG) | Bearish Signal Reversed | D2977 |
| image_07 | Bullish continuation après plus-bas | Reversals and Continuations | D2978 |
| image_08 | Two continuation Bearish Signal Reversed (AVT) | Reversals and Continuations | D2978 |

## DÉCISIONS

### D2971 — Signal Reversed : définition
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md) : Les patterns Bullish/Bearish Signal Reversed inversent une tendance existante par un signal contraire. Bullish Signal Reversed = une série de plus-hauts est inversée par un Double Bottom Breakdown. Bearish Signal Reversed = une série de plus-bas est inversée par un Double Top Breakout. Forment des retournements OU des continuations.
**TRADEX-AI C1** : Pattern P&F déterministe (colonnes X/O) calculable sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D2972 — Bullish Signal Reversed : construction
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_01, image_02) : Démarre par une série de plus-hauts (X-Columns au-dessus du X précédent) et plus-bas montants (O-Columns au-dessus du O précédent) = uptrend (« bullish signal »). Minimum 2 plus-hauts successifs. Le signal « reversed » survient quand le dernier O-Column casse sous le bas du O-Column précédent (Double Bottom Breakdown).
**TRADEX-AI C1** : Règle de détection codable ; exiger ≥2 plus-hauts avant la cassure.
*Catégorie : signal*

### D2973 — Plus-hauts non uniformes
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_02) : Les plus-hauts n'ont pas besoin d'être uniformes ni marginalement (1-box) plus hauts ; le pattern requiert simplement une série de plus-hauts/plus-bas montants inversée par un Double Bottom Breakdown.
**TRADEX-AI C1** : Ne pas imposer d'incrément fixe entre plus-hauts dans la détection.
*Catégorie : structure_marche*

### D2974 — Reversal vs continuation
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_03) : L'aspect reversal/continuation dépend de la direction du mouvement antérieur et des niveaux de prix relatifs. Un Bullish Signal Reversed formé juste après un nouveau plus-haut = clairement un pattern de **retournement**.
**TRADEX-AI C3** : Contextualiser le signal par la position dans la tendance majeure.
*Catégorie : structure_marche*

### D2975 — Continuation = reprise de tendance
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_04) : Un Bullish Signal Reversed qui retrace une partie d'un déclin (ou rebondit dans un downtrend plus large) = pattern de **continuation** ; en termes de bar chart, ressemble à un rising wedge ou flag.
**TRADEX-AI C1** : Lier au régime de marché (continuation baissière) pour la pondération.
*Catégorie : structure_marche*

### D2976 — Bearish Signal Reversed : construction
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_05) : Démarre par série de plus-bas (O sous O précédent) et plus-hauts descendants (X n'excédant pas le X précédent) = downtrend. Minimum 2 plus-bas successifs. Le signal « reversed » survient quand le dernier X-Column casse au-dessus du haut du X précédent (Double Top Breakout).
**TRADEX-AI C1** : Miroir baissier ; même logique de détection.
*Catégorie : signal*

### D2977 — Les signaux ne tiennent pas toujours
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_06) : Exemple BIG — un Bearish Signal Reversed peut casser puis échouer à tenir, le titre repartant fortement à la baisse. Rappel que les signaux ne mènent pas toujours au résultat attendu.
**TRADEX-AI C3** : Garde anti-faux-signal — exiger confirmation/gestion du risque après le breakout.
*Catégorie : gestion_risque_entree*

### D2978 — Jugement = art + science
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md, image_07, image_08) : L'inclusion ou non de price action (ex. Triple Bottom Breakdown adjacent) relève d'un jugement — « technical analysis is part art and part science ».
**TRADEX-AI C1** : Limiter l'automatisation aux règles strictes ; le contexte reste discrétionnaire (mode Manuel).
*Catégorie : structure_marche*

### D2979 — Objectifs et risque
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md) : Objectifs via Horizontal/Vertical Count Method (articles séparés) ; ce ne sont PAS des cibles dures, juste des estimations. La box juste sous le bas du pattern marque souvent le niveau « worst-case » d'échec.
**TRADEX-AI C1** : Utiliser la box sous le pattern comme stop structurel ; objectifs = indicatifs.
*Catégorie : gestion_risque_entree*

### D2980 — Meilleur usage = continuation
🟢 **FAIT VÉRIFIÉ** (Source : p_and_f_signal_reversed.md) : Probablement mieux utilisés comme patterns de **continuation** (pullback après long X-Column / correction après long O-Column) car ils signalent une reprise de la tendance majeure. P&F daily = vue long terme ; 60/30-min = perspective medium-term.
**TRADEX-AI C3** : Prioriser les configurations de continuation alignées sur la tendance majeure GC/HG/CL/ZW.
*Catégorie : signal*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2971 → D2980 (10) |
| Images citées | 8/8 |
| Catégories | structure_marche · signal · gestion_risque_entree |
| Tags | 🟢 FAIT VÉRIFIÉ |
| Belkhayate | NON CONCERNÉ |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
