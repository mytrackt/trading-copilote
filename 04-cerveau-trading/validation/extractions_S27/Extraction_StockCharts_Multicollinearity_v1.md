# Extraction StockCharts — Multicollinearity (multicolinéarité des indicateurs)
**Source :** `bundles/stockcharts/multicollinearity.md` (HTTP 200 · ~8 168 car.) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées
**Décisions :** D2731 → D2740 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/multicollinearity
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Table | Image | Label certifié | Section | Décision liée |
|-------|-------|----------------|---------|---------------|
| — | image_01.png | The RSI, CCI, and Wm%R all indicate similar scenarios. | Indicators From Different Categories | D2737 |
| — | image_02.png | Three indicators that are not collinear show different information about a stock. | Indicators From Different Categories | D2738 |

## DÉCISIONS

### D2731 — Définition de la multicolinéarité
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : « Multicollinearity is a statistical term referring to the unknowing use of the same type of information more than once. It is a common problem in technical analysis. Analysts need to be careful not to utilize technical indicators that reveal the same type of information. »
**TRADEX-AI C3** : Méthodologie de construction de la grille /10 — interdire l'empilement d'indicateurs porteurs de la même information. Critère qualité C3 (institutionnels/méthodo) pour la sélection des variables du score.
*Catégorie : configuration*
---

### D2732 — Règle cardinale de Bollinger
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : « Here is how John Bollinger puts it: "A cardinal rule for the successful use of technical analysis requires avoiding multicollinearity amid indicators. Multicollinearity is simply the multiple counting of the same information. The use of four different indicators all derived from the same series of closing prices to confirm each other is a perfect example." »
**TRADEX-AI C3** : Règle cardinale citée (Bollinger) : quatre indicateurs dérivés des mêmes clôtures ne se confirment pas, ils comptent une info une fois × 4. Garde-fou direct contre la fausse confluence dans la grille /10.
*Catégorie : configuration*
---

### D2733 — Pourquoi c'est dangereux : information redondante
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : « It is a problem because collinear variables contribute redundant information and can cause other variables to appear to be less important than they are. One of the real problems is that, oftentimes, multicollinearity is difficult to spot. »
**TRADEX-AI C3** : Risque double — (1) gonflement artificiel d'un signal redondant, (2) écrasement d'une vraie variable indépendante. Difficile à détecter → exige un contrôle explicite lors du design de la grille. Garde-fou anti-faux-score.
*Catégorie : gestion_risque_entree*
---

### D2734 — Catégorie Momentum (indicateurs collinéaires entre eux)
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : Catégorie « Momentum » listée — Rate of Change (ROC), Stochastics (%K, %D), RSI, Commodity Channel Index (CCI), Williams %R (Wm%R), StochRSI, TRIX, Ultimate Oscillator, Aroon.
**TRADEX-AI C3** : Bloc d'indicateurs momentum considérés interchangeables/redondants par StockCharts. Pour TRADEX-AI : choisir AU PLUS UN représentant momentum dans la grille (ex. un seul parmi RSI/Stoch/CCI/Wm%R).
*Catégorie : indicateurs_momentum*
---

### D2735 — Catégorie Trend (indicateurs collinéaires entre eux)
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : Catégorie « Trend » listée — Moving Averages, MACD, Average True Range (ATR), Wilder's DMI (ADX), Price Oscillator (PPO).
**TRADEX-AI C1** : Bloc tendance. Note importante : ATR figure ici dans « Trend » alors qu'il mesure la volatilité — à arbitrer pour la grille. Choisir un seul représentant de tendance dominant (MM ou MACD ou ADX), pas tous.
*Catégorie : indicateurs_tendance*
---

### D2736 — Catégorie Volume (indicateurs collinéaires entre eux)
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : Catégorie « Volume » listée — Accumulation Distribution, Chaikin Money Flow (CMF), Volume Rate of Change, Volume Oscillator (PVO), Demand Index, On Balance Volume (OBV), Money Flow Index.
**TRADEX-AI C2** : Bloc volume/order flow. Le Money Flow Index (= « Énergie » Belkhayate selon MEMORY projet) appartient à cette catégorie : ne pas le combiner avec ADL/OBV/CMF comme s'ils confirmaient indépendamment. Un seul indicateur volume par signal.
*Catégorie : indicateurs_momentum*
---

### D2737 — Test pratique : indicateurs collinéaires (RSI/CCI/Wm%R)
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md, image_01) : « The best way to quickly determine if an indicator is collinear with another one is to chart it. (…) If they rise and fall in the same areas, the odds are that they're collinear and you should just use one of them. (…) all three indicators are basically saying the same thing. (…) Pick one of the indicators for your analysis and do not use the others. » (RSI, CCI, Wm%R montent/baissent ensemble.)
**TRADEX-AI C3** : Test opérationnel de colinéarité — corrélation visuelle des montées/descentes. RSI, CCI, Wm%R = redondants (exemple littéral). Implémentable : calculer la corrélation des séries d'indicateurs et écarter les doublons avant scoring.
*Catégorie : configuration*
---

### D2738 — Contre-exemple : indicateurs non collinéaires (confirmation valide)
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md, image_02) : « Below are some examples of indicators that are not collinear. When interpreted correctly, each will give different information. The indicators can be used to confirm a trading signal. »
**TRADEX-AI C3** : La VRAIE confirmation vient d'indicateurs de catégories différentes (ex. 1 tendance + 1 momentum + 1 volume). C'est le fondement méthodologique de la confluence multi-cercles TRADEX-AI (C1+C2+...), pas l'empilement intra-catégorie.
*Catégorie : signal*
---

### D2739 — Le piège : croire confirmer en empilant des redondants
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : « If you are randomly selecting indicators to support your analysis, you will more than likely fall into the multicollinearity trap of using multiple indicators that are all saying the same thing. They are not giving you any additional information; in fact, they are restricting your overall view of the market. »
**TRADEX-AI C3** : Garde-fou explicite contre la sélection aléatoire d'indicateurs. Pour la grille /10 : chaque critère doit apporter une information orthogonale — sinon il fausse le score à la hausse. À auditer lors du design des poids.
*Catégorie : gestion_risque_entree*
---

### D2740 — Conclusion : ne pas chercher du soutien parmi des collinéaires
🟢 **FAIT VÉRIFIÉ** (Source : multicollinearity.md) : « Don't search for supporting information among collinear indicators; though they can be appealing, they are ultimately misleading. »
**TRADEX-AI C3** : Principe directeur pour la conception du moteur de score : la diversité d'information prime sur le nombre d'indicateurs. Règle d'or à inscrire dans la documentation de la grille /10 (un critère = une source d'information distincte).
*Catégorie : configuration*
---

## SYNTHÈSE
| Champ | Valeur |
|-------|--------|
| Décisions ajoutées | 10 (D2731 → D2740) |
| Images citées | 2/2 certifiées |
| Catégories | configuration, gestion_risque_entree, indicateurs_momentum, indicateurs_tendance, signal |
| Cercle dominant | C3 (méthodologie / qualité des variables de la grille /10) |
| Tags | 🟢 FAIT VÉRIFIÉ ×10 |
| Belkhayate | Lien indirect : le Money Flow Index appartient à la catégorie Volume (D2736), or l'« Énergie » Belkhayate = MFI standard selon MEMORY projet ⚫🔴 — implique de ne pas cumuler Énergie + autre indicateur volume comme confirmation indépendante. Hypothèse projet, non affirmée par la source. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE en zone validation/, NON fusionnée dans KNOWLEDGE_BASE_MASTER.json — attend OK utilisateur.
