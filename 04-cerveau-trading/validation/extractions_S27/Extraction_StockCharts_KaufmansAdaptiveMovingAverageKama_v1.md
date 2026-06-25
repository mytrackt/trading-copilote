# Extraction StockCharts — Kaufman's Adaptive Moving Average (KAMA)

**Source :** `bundles/stockcharts/kaufmans_adaptive_moving_average_kama.md` (HTTP 200 · ~12 258 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D2391 → D2410 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/kaufmans-adaptive-moving-average-kama
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | (chart KAMA d'intro) | What Is Kaufman's Adaptive Moving Average? [SECTION-FALLBACK] | CERTIFIÉ |
| image_02.png | KAMA Chart (exemple de calcul) | Calculation Example/Chart | CERTIFIÉ |
| image_03.png | KAMA Chart (price crosses) | Interpreting KAMA | CERTIFIÉ |
| image_04.png | KAMA Chart (Kroger, direction) | Interpreting KAMA | CERTIFIÉ |
| image_05.png | KAMA Chart (MMM, double KAMA) | Interpreting KAMA | CERTIFIÉ |
| image_06.png | KAMA Chart (SharpCharts) | Using with SharpCharts | CERTIFIÉ |
| image_07.png | (chart ACP) | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIÉ |

## DÉCISIONS

### D2391 — Nature et objet de KAMA
🔵 **ÉCOLE** (Source : kaufmans_adaptive_moving_average_kama.md, image_01) : Développée par Perry Kaufman, KAMA est une moyenne mobile conçue pour tenir compte du bruit/volatilité du marché. Elle suit le prix de près quand les oscillations sont petites (bruit faible) et s'ajuste/suit de plus loin quand les oscillations s'élargissent. Indicateur suiveur de tendance : identifie la tendance, time les retournements, filtre les mouvements.
**TRADEX-AI C1** : Moyenne mobile adaptative (école Kaufman) ; candidate comme filtre de tendance auto-ajusté au régime de volatilité GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D2392 — Réglages recommandés KAMA(10,2,30)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : Réglages recommandés par Kaufman : KAMA(10,2,30) — 10 = nb de périodes de l'Efficiency Ratio (ER) ; 2 = nb de périodes de l'EMA la plus rapide ; 30 = nb de périodes de l'EMA la plus lente.
**TRADEX-AI C1** : Triplet de paramètres par défaut ; valeurs de référence si KAMA est intégrée.
*Catégorie : configuration*

---

### D2393 — Étape 1 : Efficiency Ratio (ER)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : `ER = Change / Volatility`, avec `Change = ABS(Close - Close il y a 10 périodes)` et `Volatility = Sum10(ABS(Close - Prior Close))` (somme des valeurs absolues des 10 derniers changements de prix). ABS = valeur absolue.
**TRADEX-AI C1** : Formule déterministe de l'ER ; mesure le ratio mouvement net / mouvement total.
*Catégorie : indicateurs_tendance*

---

### D2394 — Interprétation statistique de l'ER (0 à 1)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : L'ER donne « l'efficience fractale » des changements de prix. Il fluctue entre 1 et 0 (extrêmes rares) : ER=1 si le prix monte ou descend 10 périodes consécutives ; ER=0 si le prix est inchangé sur les 10 périodes.
**TRADEX-AI C1** : Échelle normalisée 0–1 du caractère directionnel ; exploitable comme jauge de « trendiness ».
*Catégorie : indicateurs_tendance*

---

### D2395 — Étape 2 : Smoothing Constant (SC)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : `SC = [ER x (fastest SC - slowest SC) + slowest SC]²`, soit `SC = [ER x (2/(2+1) - 2/(30+1)) + 2/(30+1)]²`. Fastest SC = constante de lissage de l'EMA courte (2 périodes), slowest SC = celle de l'EMA lente (30 périodes) ; le « ² » final élève au carré.
**TRADEX-AI C1** : Constante de lissage adaptative dérivée de l'ER ; cœur de l'adaptativité de KAMA.
*Catégorie : configuration*

---

### D2396 — Étape 3 : formule récursive de KAMA
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : `Current KAMA = Prior KAMA + SC x (Price - Prior KAMA)`. La première valeur KAMA est une simple moyenne mobile (valeur initiale nécessaire).
**TRADEX-AI C1** : Récurrence calculatoire complète ; implémentable telle quelle si KAMA retenue.
*Catégorie : indicateurs_tendance*

---

### D2397 — Exemple de calcul (Excel + QQQ)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_02) : Une capture de tableur Excel illustre le calcul de KAMA avec le graphe QQQ correspondant ; un fichier tableur téléchargeable est fourni.
**TRADEX-AI C1** : Référence de validation du calcul ; utile pour tester une implémentation.
*Catégorie : configuration*

---

### D2398 — Interprétation : croisements prix/KAMA
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_03) : Un croisement au-dessus ou au-dessous de KAMA indique un changement de direction des prix. Comme toute MA, un simple système de croisement génère beaucoup de signaux et de whipsaws.
**TRADEX-AI C1** : Signal de croisement directionnel, mais bruité brut ; à filtrer avant usage.
*Catégorie : signal*

---

### D2399 — Filtres anti-whipsaw sur croisements
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : On réduit les whipsaws en appliquant un filtre prix ou temps : exiger que le prix tienne le croisement un nombre fixé de jours, ou que le croisement dépasse KAMA d'un pourcentage fixé.
**TRADEX-AI C1** : Règle de filtrage (persistance temporelle ou seuil %) ; garde-fou contre faux signaux.
*Catégorie : signal*

---

### D2400 — Direction de KAMA = tendance de fond
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_04) : La direction de KAMA définit la tendance globale. La tendance est baissière tant que KAMA baisse et forge des plus-bas plus bas ; haussière tant que KAMA monte et forge des plus-hauts plus hauts. Peut nécessiter d'ajuster le paramètre médian pour lisser.
**TRADEX-AI C1** : Définition de tendance par pente de KAMA (HH/LL) ; filtre directionnel.
*Catégorie : indicateurs_tendance*

---

### D2401 — Lissage via paramètre médian, exemple KAMA(10,5,30)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_04) : Augmenter le paramètre médian (EMA la plus rapide) lisse KAMA. L'exemple Kroger montre KAMA(10,5,30) avec un uptrend raide déc.–mars puis un uptrend moins raide mai–août.
**TRADEX-AI C1** : Réglage KAMA(10,5,30) comme version lissée pour analyse de tendance long terme.
*Catégorie : configuration*

---

### D2402 — Combinaison double KAMA (filtre + signal)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_05) : On peut combiner une KAMA long terme (définit la grande tendance) et une KAMA court terme (signaux). Ex : KAMA(10,5,30) comme filtre de tendance, jugée haussière quand elle monte ; puis chercher des croisements haussiers quand le prix passe au-dessus de KAMA(10,2,30). Exemple MMM : crosses haussiers déc./jan./fév., KAMA long terme tourne en baisse en avril, crosses baissiers mai/juin/juil.
**TRADEX-AI C1** : Architecture à deux KAMA (régime + déclencheur) ; modèle de filtre directionnel + entrée.
*Catégorie : signal*

---

### D2403 — KAMA disponible sur SharpCharts et ACP
🟡 **CONVENTION** (Source : kaufmans_adaptive_moving_average_kama.md) : L'overlay KAMA peut être ajouté à SharpCharts et ACP Charts.
**TRADEX-AI C1** : Disponibilité outil StockCharts ; informationnel, non porté NT8.
*Catégorie : configuration*

---

### D2404 — Sensibilité via le 1er paramètre (ER)
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md, image_06) : Le 1er paramètre concerne l'Efficiency Ratio ; il est conseillé de ne PAS l'augmenter. Pour augmenter la sensibilité, le diminuer. Pour lisser KAMA (tendance long terme), augmenter le paramètre médian par incréments. Même avec une différence de 3, KAMA(10,5,30) est nettement plus lisse que KAMA(10,2,30).
**TRADEX-AI C1** : Règle de tuning : ER ↓ = plus sensible ; médian ↑ = plus lisse. Guide le réglage par actif.
*Catégorie : configuration*

---

### D2405 — Défauts ACP (2, 30, 10)
🟡 **CONVENTION** (Source : kaufmans_adaptive_moving_average_kama.md, image_07) : Par défaut sur StockChartsACP, l'overlay utilise des EMA 2 et 30 périodes plus 10 périodes pour l'Efficiency Ratio. Paramètres ajustables.
**TRADEX-AI C1** : Valeurs par défaut confirmées (cohérentes avec KAMA(10,2,30)).
*Catégorie : configuration*

---

### D2406 — Scan : uptrend + prix croise au-dessus de KAMA
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : Scan de signal d'achat : univers volume moyen ≥100 000 et close moyen >10 ; `KAMA(10,5,30) > SMA(50,KAMA(10,5,30))` (uptrend long terme) ET `Daily Close crosses KAMA(10,2,30)` (signal d'achat).
**TRADEX-AI C1** : Critère composite d'entrée long (filtre LT + croisement CT) ; transposable comme règle de signal.
*Catégorie : signal*

---

### D2407 — Scan : downtrend + prix croise au-dessous de KAMA
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : Scan de signal de vente : même univers ; `KAMA(10,5,30) < SMA(50,KAMA(10,5,30))` (downtrend long terme) ET `KAMA(10,2,30) crosses Daily Close` (signal de vente).
**TRADEX-AI C1** : Critère composite d'entrée short symétrique ; transposable comme règle de signal.
*Catégorie : signal*

---

### D2408 — KAMA comme filtre du bruit de volatilité
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : KAMA suit de près quand le bruit est faible et de plus loin quand la volatilité s'élargit — donc auto-ajustement de la réactivité selon la volatilité (reformule D2391 côté usage).
**TRADEX-AI C1** : Comportement clé : réactivité variable selon volatilité, atout en régime cuivre/pétrole volatil.
*Catégorie : indicateurs_tendance*

---

### D2409 — Lag inhérent et nature suiveuse
🟢 **FAIT VÉRIFIÉ** (Source : kaufmans_adaptive_moving_average_kama.md) : KAMA s'utilise « comme tout indicateur suiveur de tendance, telle une moyenne mobile » (crosses, changements de direction, signaux filtrés). En tant que MA, elle reste un indicateur retardé sur le prix.
**TRADEX-AI C1** : Rappel de limite : signal retardé ; à confirmer par order flow / autres cercles avant exécution.
*Catégorie : indicateurs_tendance*

---

### D2410 — Lien Belkhayate (Énergie / moyennes)
⚫🔴 **NON VÉRIFIÉ — Belkhayate** (Source : aucune dans kaufmans_adaptive_moving_average_kama.md) : Le document ne mentionne ni Belkhayate ni l'Énergie (MFI). Aucun lien direct entre KAMA et la méthode Belkhayate n'est attesté par la source. Toute assimilation KAMA ↔ moyennes/Énergie Belkhayate serait une inférence non sourcée.
**TRADEX-AI C1/⚫** : Ne PAS rattacher KAMA à un élément Belkhayate sans validation humaine ; statut bloquant tant que non tranché.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2391 → D2410 (20) |
| Images | 7/7 certifiées |
| Tags dominants | 🟢 littéral (14) · 🔵 ÉCOLE Kaufman (1) · 🟡 convention (3) · ⚫🔴 Belkhayate non vérifié (1) |
| Cercle | C1 (moyenne mobile adaptative) |
| Belkhayate | ⚫🔴 D2410 : aucun lien attesté, ne rien inférer |
| Actifs | Exemples actions US (QQQ, Kroger, MMM) ; aucun GC/HG/CL/ZW direct |
| Cas à vérifier | D2410 (lien Belkhayate à trancher humainement). Décision d'archi : intégrer KAMA comme filtre de tendance adaptatif vs garder MA simples — à valider sur range bars NT8. |

> ⚠️ Extraction BRUT, zone validation/, NON fusionnée. Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
