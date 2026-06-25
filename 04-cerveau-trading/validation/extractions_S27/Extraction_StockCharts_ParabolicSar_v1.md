# Extraction StockCharts — Parabolic SAR

**Source :** `bundles/stockcharts/parabolic_sar.md` (HTTP 200 · ~9 600 car.) + 11 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D3031 → D3050 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/parabolic-sar
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Parabolic SAR is plotted below price bars when they're rising... | What Is the Parabolic SAR? | CERTIFIÉ |
| image_02.png | Rising SAR | Rising SAR [SECTION-FALLBACK] | CERTIFIÉ |
| image_03.png | Rising SAR | Rising SAR [SECTION-FALLBACK] | CERTIFIÉ |
| image_04.png | Falling SAR | Falling SAR [SECTION-FALLBACK] | CERTIFIÉ |
| image_05.png | Falling SAR | Falling SAR [SECTION-FALLBACK] | CERTIFIÉ |
| image_06.png | Adjusting the Step Increment | Adjusting the Step Increment [SECTION-FALLBACK] | CERTIFIÉ |
| image_07.png | Adjusting the Step Increment | Adjusting the Step Increment [SECTION-FALLBACK] | CERTIFIÉ |
| image_08.png | Adjusting the Maximum Step | Adjusting the Maximum Step [SECTION-FALLBACK] | CERTIFIÉ |
| image_09.png | Adjusting the Maximum Step | Adjusting the Maximum Step [SECTION-FALLBACK] | CERTIFIÉ |
| image_10.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIÉ |
| image_11.png | Parabolic SAR applied to StockChartsACP. | Using with StockChartsACP | CERTIFIÉ |

## DÉCISIONS

### D3031 — Parabolic SAR : système prix-et-temps de Welles Wilder
🔵 **ÉCOLE (Wilder)** (Source : parabolic_sar.md) : « Developed by Welles Wilder, the Parabolic SAR is a price-and-time-based trading system. Wilder called this the "Parabolic Time/Price System." SAR stands for "stop and reverse," which is the actual indicator used in the system. »
**TRADEX-AI C1** : indicateur Wilder de type « stop and reverse » ; SAR = l'indicateur effectif du système Parabolic Time/Price.
*Catégorie : indicateurs_tendance*

---

### D3032 — SAR trace le prix et se positionne dessous (hausse) / dessus (baisse)
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md, image_01) : « SAR trails price as the trend extends over time. The indicator is plotted below prices as they're rising and above prices as they're falling. [...] the indicator stops and reverses when the price trend reverses and breaks above or below the indicator. »
**TRADEX-AI C1** : règle de lecture — SAR sous le prix = tendance haussière, SAR au-dessus = tendance baissière ; il stoppe et inverse à la rupture.
*Catégorie : indicateurs_tendance*

---

### D3033 — Origine 1978 : New Concepts in Technical Trading Systems
🔵 **ÉCOLE (Wilder)** (Source : parabolic_sar.md) : « Wilder introduced the Parabolic Time/Price System in his 1978 book *New Concepts in Technical Trading Systems*. This book also includes the Relative Strength Index (RSI), Average True Range (ATR), and the Directional Movement Concept (ADX). »
**TRADEX-AI C1** : provenance documentaire — même ouvrage fondateur que RSI, ATR et ADX (cohérence du corpus Wilder).
*Catégorie : indicateurs_tendance*

---

### D3034 — Calcul du SAP ascendant : EP = plus haut de la tendance haussière courante
🟡 **CONVENTION** (Source : parabolic_sar.md) : « Rising SAR [...] Extreme Point (EP): The highest high of the current uptrend. »
**TRADEX-AI C1** : composante de calcul — en hausse, le point extrême (EP) est le plus haut de la tendance haussière en cours.
*Catégorie : indicateurs_tendance*

---

### D3035 — Facteur d'accélération (AF) : départ 0.02, pas de 0.02, max 0.20
🟡 **CONVENTION** (Source : parabolic_sar.md) : « Acceleration Factor (AF): Starting at .02, AF increases by .02 each time the extreme point makes a new high. AF can reach a maximum of .20, no matter how long the uptrend extends. »
**TRADEX-AI C1** : paramètres standard de l'AF — 0.02 initial, incrément 0.02 à chaque nouveau plus haut, plafond 0.20.
*Catégorie : indicateurs_tendance*

---

### D3036 — Formule du SAR ascendant
🟡 **CONVENTION** (Source : parabolic_sar.md) : « Current SAR = Prior SAR + Prior AF(Prior EP - Prior SAR) [...] The Acceleration Factor is multiplied by the difference between the Extreme Point and the prior period's SAR. This is then added to the prior period's SAR. »
**TRADEX-AI C1** : formule déterministe SAR montant = SAR précédent + AF × (EP − SAR précédent).
*Catégorie : indicateurs_tendance*

---

### D3037 — Garde-fou SAR ascendant : jamais au-dessus des bas des 2 périodes précédentes
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « Note however that SAR can never be above the prior two periods' lows. Should SAR be above one of those lows, use the lowest of the two for SAR. »
**TRADEX-AI C1** : contrainte de bornage — en tendance haussière, SAR plafonné au plus bas des deux périodes précédentes (évite que le stop coupe le prix).
*Catégorie : gestion_risque_entree*

---

### D3038 — Calcul du SAR descendant : EP = plus bas de la tendance baissière courante
🟡 **CONVENTION** (Source : parabolic_sar.md) : « Falling SAR [...] Extreme Point (EP): The lowest low of the current downtrend. »
**TRADEX-AI C1** : composante de calcul — en baisse, le point extrême (EP) est le plus bas de la tendance baissière en cours.
*Catégorie : indicateurs_tendance*

---

### D3039 — Formule du SAR descendant + bornage par les hauts des 2 périodes
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « Current SAR = Prior SAR - Prior AF(Prior SAR - Prior EP) [...] Note that SAR can never be below the prior two periods' highs. Should SAR be below one of those highs, use the highest of the two for SAR. »
**TRADEX-AI C1** : formule SAR descendant = SAR précédent − AF × (SAR précédent − EP) ; borné au plus haut des deux périodes précédentes.
*Catégorie : gestion_risque_entree*

---

### D3040 — SAR = indicateur suiveur de tendance / trailing stop
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « SAR follows price and can be considered a trend-following indicator. Once a downtrend reverses and starts up, SAR follows prices like a trailing stop. »
**TRADEX-AI C1** : usage principal — SAR sert de stop suiveur (trailing stop) dans le sens de la tendance.
*Catégorie : gestion_risque_entree*

---

### D3041 — En hausse, SAR ne décroît jamais et protège les profits
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « The stop continuously rises as long as the uptrend remains in place. In other words, SAR never decreases in an uptrend and continuously protects profits as prices advance. The indicator acts as a guard against the propensity to lower a stop-loss. »
**TRADEX-AI C1** : discipline de gestion — en tendance haussière le stop ne fait que monter ; garde-fou contre la tentation de baisser un stop-loss.
*Catégorie : gestion_risque_entree*

---

### D3042 — Reversal : prix passe sous SAR → downtrend, SAR au-dessus, protège les shorts
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « Once price stops rising and reverses below SAR, a downtrend starts, with SAR above the price. SAR follows prices lower like a trailing stop. [...] Because SAR never rises in a downtrend, it continuously protects profits on short positions. »
**TRADEX-AI C1** : signal de retournement = prix franchit SAR ; en baisse, SAR descend et protège les profits des positions short.
*Catégorie : gestion_risque_entree*

---

### D3043 — Le Step (AF) pilote la sensibilité du SAR
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « the Step, also referred to as the Acceleration Factor (AF), is a multiplier that influences the rate-of-change in SAR. [...] The Step dictates the sensitivity of the SAR indicator. »
**TRADEX-AI C1** : le paramètre Step gouverne la réactivité de l'indicateur ; configurable par l'utilisateur (Step + Maximum Step).
*Catégorie : configuration*

---

### D3044 — Step bas = moins sensible ; Step haut = plus sensible (risque whipsaws)
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md, image_06/image_07) : « SAR sensitivity can be decreased by decreasing the Step. A lower step moves SAR further from price, making a reversal less likely. [...] The indicator will reverse too often if the step is set too high. This will produce whipsaws and fail to capture the trend. »
**TRADEX-AI C1** : arbitrage paramétrique — Step trop élevé ⇒ excès de retournements (whipsaws) ; Step bas ⇒ SAR plus éloigné du prix, retournement moins probable.
*Catégorie : configuration*

---

### D3045 — Le Maximum Step ajuste aussi la sensibilité (poids moindre que le Step)
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md, image_08/image_09) : « The sensitivity of the indicator can also be adjusted using the Maximum Step. While the Maximum Step can influence sensitivity, the Step carries more weight [...] increasing the Step ensures that the Maximum Step will be hit quicker. »
**TRADEX-AI C1** : second levier de réglage ; un Maximum Step plus bas réduit la sensibilité et produit moins de retournements.
*Catégorie : configuration*

---

### D3046 — SAR plus efficace sur titres en tendance (~30 % du temps selon Wilder)
🔵 **ÉCOLE (Wilder)** (Source : parabolic_sar.md) : « According to Wilder's estimates, the Parabolic SAR works best with trending securities, which occur roughly 30% of the time. This means the indicator will be prone to whipsaws over 50% of the time or when a security is not trending. »
**TRADEX-AI C1** : limite d'usage — SAR performant uniquement en marché tendanciel ; sujet aux whipsaws >50 % du temps hors tendance.
*Catégorie : indicateurs_tendance*

---

### D3047 — Qualité du signal dépend des réglages et du titre (pas de réglage universel)
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « the signal quality depends on the settings and characteristics of the underlying security. [...] There is no golden rule or one-size-fits-all setting. Each security should be evaluated based on its characteristics. »
**TRADEX-AI C1** : avertissement — pas de paramétrage universel ; calibrer le SAR par actif (donc par GC/HG/CL/ZW séparément).
*Catégorie : configuration*

---

### D3048 — Combiner SAR avec l'ADX pour jauger la force de tendance
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « Parabolic SAR should also be used with other indicators and technical analysis techniques. For example, Wilder's Average Directional Index can estimate the trend's strength before considering signals. »
**TRADEX-AI C7** : recommandation de croisement — utiliser l'ADX (force de tendance) en amont avant de considérer les signaux SAR.
*Catégorie : indicateurs_tendance*

---

### D3049 — Paramètres SharpCharts par défaut : 0.02 (Starting Step) / 0.20 (Maximum Step)
🟡 **CONVENTION** (Source : parabolic_sar.md, image_10) : « The default parameters are 0.02 for the Starting Step and 0.20 for the Maximum Step. If you want the increment amount to be different than the starting step value, then you can add an optional third parameter to set the increment amount. »
**TRADEX-AI C1** : réglages par défaut de référence (0.02 / 0.20) ; un 3e paramètre optionnel dissocie l'incrément du Starting Step.
*Catégorie : configuration*

---

### D3050 — Scans : cassure au-dessus d'un SAR baissier / sous un SAR haussier
🟢 **FAIT VÉRIFIÉ** (Source : parabolic_sar.md) : « Break Above Falling SAR [...] filters for stocks that have a bullish SAR reversal (Parabolic SAR (.01,.20)). » / « Break Below Rising SAR [...] a bearish SAR reversal. » avec conditions « [Yesterday's High < Yesterday's Parabolic SAR(0.01,0.2)] AND [High > Parabolic SAR(0.01,0.2)] » (haussier) et inverse (baissier).
**TRADEX-AI C1** : critères déterministes de signal — reversal haussier = High franchit au-dessus d'un SAR précédemment baissier ; reversal baissier = Low franchit en dessous d'un SAR précédemment haussier (paramètres 0.01,0.20).
*Catégorie : signal*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D3031 → D3050 (20) |
| Images certifiées | 11/11 |
| Tags | 🟢 FAIT VÉRIFIÉ (majorité) · 🔵 ÉCOLE Wilder (D3031, D3033, D3046) · 🟡 CONVENTION (D3034–D3036, D3038, D3049) |
| Cercle | C1 (Prix/tendance/stop) ; D3048 → C7 (croisement ADX) |
| Catégories | indicateurs_tendance, gestion_risque_entree, configuration, signal |
| Point clé | SAR = trailing stop Wilder (gestion_risque_entree) : D3037, D3039, D3040–D3042 ⇒ niveaux de stop déterministes |
| Belkhayate | NON CONCERNÉ (pas de lien MFI/Énergie) |
| Actifs | GC·HG·CL·ZW — calibrer Step par actif (D3047) |
| Cas à vérifier | Aucun — 0 image à vérifier ; tags 🔵/🟡 signalent attributions d'école/convention à confirmer en fusion, pas de fait litigieux |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. NB gestion de risque : SAR fournit un stop suiveur déterministe (formules D3036/D3039 + bornage D3037/D3039) — pertinent pour le module gestion_risque_entree de TRADEX-AI.
