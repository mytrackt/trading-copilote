# Extraction StockCharts — Moving Average Envelopes

**Source :** `bundles/stockcharts/moving_average_envelopes.md` (HTTP 200 · ~9 900 car.) + 11 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D2651 → D2664 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/moving-average-envelopes
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Are Moving Average Envelopes? | What Are Moving Average Envelopes? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Formulas | Formulas [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | Adjusting the Settings | Adjusting the Settings [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_04.png | Adjusting the Settings | Adjusting the Settings [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | Trend Identification | Trend Identification [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Trend Identification | Trend Identification [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | Overbought/Oversold | Overbought/Oversold [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | Overbought/Oversold | Overbought/Oversold [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | Chart displaying Moving Average Envelopes in SharpCharts. | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_10.png | SharpChart settings for Moving Average Envelopes. | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_11.png | Moving Averages Envelopes overlaid on a price chart in StockChartsACP. | Using with StockChartsACP | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2651 — Définition : enveloppes en pourcentage autour d'une MA
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_01) : Les Moving Average Envelopes sont des enveloppes basées sur un pourcentage, placées au-dessus et au-dessous d'une moyenne mobile. La MA de base peut être simple (SMA) ou exponentielle (EMA). Chaque enveloppe est placée au même pourcentage au-dessus ou au-dessous de la moyenne mobile, créant des bandes parallèles qui suivent l'action des prix.
**TRADEX-AI C1** : Overlay d'enveloppe à pourcentage fixe symétrique autour d'une MA (SMA ou EMA) ; implémentable comme overlay sur NT8, lecture de tendance et d'extrêmes.
*Catégorie : indicateurs_tendance*

---

### D2652 — Double usage : suivi de tendance + surachat/survente
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md) : Avec une MA comme base, les enveloppes peuvent servir d'indicateur de suivi de tendance. Au-delà du simple suivi de tendance, elles peuvent aussi identifier les niveaux de surachat et survente **lorsque la tendance est relativement plate**.
**TRADEX-AI C1** : Indicateur bivalent — suivi de tendance en marché directionnel ; surachat/survente uniquement en marché plat. Condition de régime à intégrer.
*Catégorie : indicateurs_tendance*

---

### D2653 — Formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_02) : Une SMA 20 jours avec enveloppe 2,5 % donne : `Enveloppe haute = SMA 20j + (SMA 20j × 0,025)` ; `Enveloppe basse = SMA 20j - (SMA 20j × 0,025)`. SMA = chaque point pondéré également ; EMA = plus de poids aux prix récents, moins de lag. Étapes : (1) choisir SMA ou EMA, (2) sélectionner le nombre de périodes, (3) fixer le pourcentage des enveloppes.
**TRADEX-AI C1** : Formule déterministe (MA ± MA × pourcentage). Les bandes restent à pourcentage constant au-dessus/au-dessous de la MA. Directement codable.
*Catégorie : indicateurs_tendance*

---

### D2654 — Paramétrage selon objectif et profil trader
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md) : Les paramètres dépendent des objectifs trading/investissement et des caractéristiques du titre. Les traders utiliseront plutôt des MA plus courtes (rapides) et des enveloppes relativement serrées ; les investisseurs préféreront des MA plus longues (lentes) avec des enveloppes plus larges.
**TRADEX-AI C1** : Réglage adaptatif au horizon (court terme = MA rapide + bande serrée ; long terme = MA lente + bande large) ; à calibrer par actif et par mode Belkhayate.
*Catégorie : configuration*

---

### D2655 — Volatilité : ajustement manuel des bandes
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_03) : La volatilité du titre influence les paramètres. Contrairement aux Bollinger Bands (qui utilisent l'écart-type) et aux Keltner Channels (qui utilisent l'ATR) — lesquels s'ajustent automatiquement à la volatilité — le chartiste doit tenir compte **manuellement** de la volatilité pour les enveloppes. Titres très volatils → bandes plus larges ; titres peu volatils → bandes plus étroites.
**TRADEX-AI C1** : Limite clé — pas d'auto-ajustement à la volatilité (contrairement à Bollinger/Keltner) ; nécessite un calibrage manuel ou une logique de largeur dynamique pilotée par ATR si voulu.
*Catégorie : indicateurs_tendance*

---

### D2656 — Comparaison empirique des largeurs (SPY 2,5/5/10 %)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_04) : Sur le SPY avec trois enveloppes SMA 20 : les 2,5 % (rouge) ont été touchées plusieurs fois, les 5 % (vert) seulement durant le pic de juillet, les 10 % (rose) jamais touchées — ce qui indique une bande trop large. Un trader moyen-terme pourrait utiliser les 5 %, un trader court-terme les 2,5 %. Indices et ETF requièrent des enveloppes plus serrées (moins volatils que les actions individuelles) : Alcoa, plus volatile, a franchi les 10 % de nombreuses fois avec les mêmes réglages.
**TRADEX-AI C1** : Heuristique de calibrage — une bande jamais touchée est trop large ; choix du pourcentage selon volatilité de l'actif (indices/ETF serrés, actions volatiles larges).
*Catégorie : configuration*

---

### D2657 — Interprétation : cassures = attention
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md) : Les indicateurs à canaux/bandes/enveloppes sont conçus pour englober l'essentiel de l'action des prix ; les mouvements au-dessus ou au-dessous des enveloppes méritent attention. Les tendances débutent souvent par des mouvements forts dans une direction. Une poussée au-dessus de l'enveloppe haute montre une force extraordinaire ; une chute sous l'enveloppe basse montre une faiblesse extraordinaire — pouvant signaler la fin d'une tendance et le début d'une autre.
**TRADEX-AI signal** : Cassure d'enveloppe = signal d'attention (force/faiblesse extraordinaire), candidat marqueur de changement de tendance ; jamais déclencheur direct d'ordre.
*Catégorie : signal*

---

### D2658 — Direction du canal = direction de tendance
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md) : Les enveloppes laggent l'action des prix (comme les MA). La direction de la moyenne mobile dicte la direction du canal : downtrend quand le canal descend, uptrend quand il monte, tendance plate quand il évolue latéralement.
**TRADEX-AI C1** : Lecture de tendance directe par la pente du canal (= pente de la MA) ; signal de régime exploitable par la grille /10.
*Catégorie : indicateurs_tendance*

---

### D2659 — Surachat/survente en marché plat
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md) : Parfois aucune tendance forte ne s'installe après une cassure et les prix entrent en range, marqué par une MA relativement plate. Les enveloppes servent alors à identifier surachat/survente : un mouvement au-dessus de l'enveloppe haute = surachat, un mouvement sous l'enveloppe basse = survente.
**TRADEX-AI signal** : Mode oscillateur conditionnel au régime plat (MA horizontale) ; surachat = touche bande haute, survente = touche bande basse.
*Catégorie : signal*

---

### D2660 — Identification de tendance + pullbacks (exemple DOW)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_05, image_06) : Sur Dow Chemical avec enveloppes (20,10), DOW a surgi au-dessus de l'enveloppe haute mi-juillet jusqu'à début août (force extraordinaire), les enveloppes se retournant à la hausse pour suivre l'avance. Après une hausse de 14 à 23, le titre était suracheté mais ce mouvement marqua le début d'une tendance étendue. En tendance haussière, attendre un pullback jouable (falling flags/wedges) ; le CCI sert à repérer les survente (sous -100) pour améliorer le profil risque/rendement, le momentum redevenant haussier quand le CCI repasse positif.
**TRADEX-AI gestion_risque_entree** : Schéma opérationnel — cassure haute = établissement de tendance ; puis attendre pullback (flag/wedge) confirmé par oscillateur (CCI < -100 puis retour positif) pour entrée à meilleur R/R.
*Catégorie : gestion_risque_entree*

---

### D2661 — Logique inverse en downtrend (exemple IGT + Stochastic)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_07, image_08) : La logique inverse s'applique en downtrend : un fort mouvement sous l'enveloppe basse signale une faiblesse extraordinaire annonçant un downtrend étendu (IGT cassant sous l'enveloppe 10 % fin octobre 2009). Le titre étant survendu, il est prudent d'attendre un rebond. Le Stochastic Oscillator identifie les rebonds suracheté (au-dessus de 80) ; chercher ensuite un signal chartiste ou un retour sous 80. Avertissement : l'un des signaux a produit un whipsaw (perte) — la confirmation (cassure de support / trend line) reste nécessaire.
**TRADEX-AI gestion_risque_entree** : Schéma short symétrique — cassure basse = downtrend ; attendre rebond suracheté (Stochastic > 80 puis retour sous 80) + confirmation cassure. Risque de whipsaw explicite → exiger confirmation.
*Catégorie : gestion_risque_entree*

---

### D2662 — Équivalence avec le PPO (surachat/survente)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_07) : Les enveloppes sont très similaires au Percent Price Oscillator (PPO). Les enveloppes indiquent quand un titre est à un certain pourcentage au-dessus/au-dessous d'une MA ; le PPO montre la différence en pourcentage entre une EMA courte et une EMA longue. Exemple : le PPO (1,20) donne exactement les mêmes signaux que les enveloppes EMA 20 — les prix passent au-dessus de l'enveloppe 2,5 % quand le PPO passe au-dessus de 2,5 %, et sous l'enveloppe -2,5 % quand le PPO passe sous -2,5 %.
**TRADEX-AI C1** : Équivalence formelle enveloppes ↔ PPO (1,n) ; surachat/survente lisibles indifféremment sur l'un ou l'autre.
*Catégorie : indicateurs_tendance*

---

### D2663 — Surachat/survente persistants en forte tendance (exemple Nokia)
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_08) : Mesurer surachat/survente est délicat : un titre peut rester suracheté longtemps en fort uptrend (et inversement). En fort uptrend, les prix dépassent souvent l'enveloppe haute et continuent au-dessus (l'enveloppe haute s'élève alors). Des lectures de surachat peuvent en fait être un **signe de force**. Pour cette raison, **surachat/survente sont mieux utilisés quand la tendance s'aplatit** (cas Nokia : enveloppes 50,10 ; surachat persistant en forte tendance, signaux fiables seulement en phase choppy juin-avril). Surachat à confirmer par résistance chartiste / figures baissières ; survente par support / figures haussières.
**TRADEX-AI signal** : Garde-fou critique — ne pas trader le surachat/survente en tendance forte (peut signaler la force) ; n'utiliser qu'en régime plat, et confirmer par support/résistance et figures.
*Catégorie : signal*

---

### D2664 — Paramètres par défaut SharpCharts / ACP
🟢 **FAIT VÉRIFIÉ** (Source : moving_average_envelopes.md, image_09, image_10, image_11) : Sur SharpCharts, les enveloppes sont un price overlay au-dessus du tracé de prix. Réglage par défaut (20, 2,5) : premier nombre (20) = périodes de la MA, second (2,5) = décalage en pourcentage. « SMA Envelopes » = base SMA, « EMA Envelopes » = base EMA. Sur StockChartsACP, ajout depuis le panneau Chart Settings (« EMA Envelopes » / « SMA Envelopes »), superposables au prix ou à un panneau d'indicateur.
**TRADEX-AI C1** : Paramètres de référence (20 périodes, 2,5 %) et nomenclature SMA/EMA Envelopes ; base de défauts pour l'implémentation NT8.
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions produites | D2651 → D2664 (14 décisions) |
| Images certifiées | 11/11 |
| Catégories couvertes | indicateurs_tendance · configuration · signal · gestion_risque_entree |
| Cercle dominant | C1 (overlay de prix / suivi de tendance) |
| Lien Belkhayate | NON CONCERNÉ (overlay MA classique StockCharts ChartSchool, hors méthode Belkhayate) |
| Cas à vérifier | Aucun — toutes décisions 🟢 littérales sourcées. Points d'attention : (a) pas d'auto-ajustement à la volatilité (D2655) ; (b) surachat/survente uniquement en tendance plate (D2663) ; (c) risque de whipsaw → confirmation requise (D2661) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Actifs concernés : GC · HG · CL · ZW uniquement. Overlay d'analyse technique classique (StockCharts ChartSchool), aucun rapport affirmé avec la méthode Belkhayate.
