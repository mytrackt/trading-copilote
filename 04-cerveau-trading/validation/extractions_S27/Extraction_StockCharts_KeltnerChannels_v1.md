# Extraction StockCharts — Keltner Channels

**Source :** `bundles/stockcharts/keltner_channels.md` (HTTP 200 · ~19 041 car.) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 10/10 certifiées
**Décisions :** D2411 → D2430 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/keltner-channels
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Légende | Section | Statut |
|-------|---------|---------|--------|
| image_01.png | (chart d'intro) | What Are Keltner Channels? [SECTION-FALLBACK] | CERTIFIÉ |
| image_02.png | Keltner Channels - Calculation Example | Keltner Channels Calculation | CERTIFIÉ |
| image_03.png | Keltner Channels - Uptrend Example | Identifying the Start of an Uptrend | CERTIFIÉ |
| image_04.png | Keltner Channels - Downtrend Example | Identifying the Start of a Downtrend | CERTIFIÉ |
| image_05.png | Keltner Channels - Breakout from a Trading Range | Identifying Breakouts from a Trading Range | CERTIFIÉ |
| image_06.png | Keltner Channels - Trading Range Example | Identifying Breakouts from a Trading Range | CERTIFIÉ |
| image_07.png | Keltner Channels vs Bollinger Bands | Keltner Channels vs Bollinger Bands | CERTIFIÉ |
| image_08.png | (chart SharpCharts) | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIÉ |
| image_09.png | SharpCharts settings for the Keltner Channels overlay | Using with SharpCharts | CERTIFIÉ |
| image_10.png | (chart ACP) | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIÉ |

## DÉCISIONS

### D2411 — Définition : enveloppes de volatilité basées ATR
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_01) : Les Keltner Channels sont des enveloppes basées sur la volatilité placées au-dessus et au-dessous d'une EMA. Similaires aux Bollinger Bands, mais utilisent l'ATR (et non l'écart-type) pour fixer la distance des canaux. Typiquement 2 ATR au-dessus/dessous de l'EMA 20 jours.
**TRADEX-AI C1** : Canal de volatilité ATR autour d'une EMA ; proche des Bollinger mais lissé par ATR. Candidat overlay de tendance/extrêmes pour GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

---

### D2412 — Rôle : indicateur suiveur de tendance
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : « Keltner Channels are a trend following indicator used to identify reversals with channel breakouts and channel direction. » L'EMA dicte la direction, l'ATR fixe la largeur du canal. Les canaux servent aussi à repérer surachat/survente quand la tendance est plate.
**TRADEX-AI C1** : Double usage : suiveur de tendance (cassures/direction) + bornes surachat/survente en range. Aligné avec une grille déterministe.
*Catégorie : indicateurs_tendance*

---

### D2413 — Origine : Chester Keltner (1960) et version Raschke
🔵 **ÉCOLE** (Source : keltner_channels.md) : Dans son livre de 1960 *How to Make Money in Commodities*, Chester Keltner introduit la « Ten-Day Moving Average Trading Rule » (version originale) : SMA 10 jours du typical price {(H+L+C)/3} comme centerline, ± SMA 10 jours du range haut-bas pour les canaux. Linda Bradford Raschke introduit dans les années 1980 la version moderne à base d'ATR. StockCharts utilise cette version moderne.
**TRADEX-AI C1** : Lignée d'école (Keltner→Raschke) ; la version ATR moderne est la référence implémentée.
*Catégorie : indicateurs_tendance*

---

### D2414 — Formule par défaut (EMA 20 ± 2×ATR(10))
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : `Middle Line = EMA 20 jours` ; `Upper = EMA 20 + (2 x ATR(10))` ; `Lower = EMA 20 - (2 x ATR(10))`. Trois étapes : choisir la longueur de l'EMA, les périodes de l'ATR, le multiplicateur de l'ATR.
**TRADEX-AI C1** : Formule déterministe complète ; implémentable telle quelle.
*Catégorie : configuration*

---

### D2415 — Effet des paramètres (EMA, ATR, multiplicateur)
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_02) : Une EMA plus longue = plus de lag, plus courte = moins de lag. ATR court (ex. 10) = lecture plus volatile ; ATR long (ex. 100) = lissé/plus constant. Le multiplicateur a le plus d'effet sur la largeur : passer de 2 à 1 réduit la largeur de moitié ; de 2 à 3 augmente de 50 %.
**TRADEX-AI C1** : Sensibilités paramétriques ; guide le réglage de la largeur de canal par régime de volatilité.
*Catégorie : configuration*

---

### D2416 — Triple canal 1/2/3 ATR (méthode Lovvorn)
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_02) : Exemple de 3 canaux à 1, 2 et 3 ATR (technique de Kerry Lovvorn de SpikeTrade.com) : défaut rouge (2 ATR), bleu large (3 ATR), vert étroit (1 ATR), partageant la même EMA 20. Fenêtres ATR 10/50/100 : ATR 10 plus volatil/large, ATR 100 plus lisse.
**TRADEX-AI C1** : Approche multi-bandes (1/2/3 ATR) ; échelonnement de zones d'extrême exploitable.
*Catégorie : configuration*

---

### D2417 — Principe d'interprétation : moves hors canal = rares
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : Les indicateurs à canaux/bandes encadrent l'essentiel de l'action de prix ; les mouvements au-dessus/au-dessous des lignes méritent attention car relativement rares. Un surge au-dessus du canal haut = force extraordinaire ; un plongeon sous le canal bas = faiblesse extraordinaire. Ces mouvements forts peuvent signaler la fin d'une tendance et le début d'une autre.
**TRADEX-AI C1** : Sémantique des cassures de canal (force/faiblesse extrêmes) ; déclencheurs candidats de retournement.
*Catégorie : signal*

---

### D2418 — Direction du canal = tendance ; lag
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : Fondés sur une EMA, les Keltner Channels retardent le prix. La direction de l'EMA dicte celle du canal : downtrend si le canal descend, uptrend s'il monte, plat s'il va de côté.
**TRADEX-AI C1** : Lecture directionnelle simple via pente du canal ; filtre de tendance, avec lag à compenser.
*Catégorie : indicateurs_tendance*

---

### D2419 — Cassures de canal = début de tendance ; range
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : Un retournement à la hausse du canal + cassure au-dessus de la ligne haute peut signaler le début d'un uptrend ; un retournement à la baisse + cassure sous la ligne basse, un downtrend. Parfois aucune tendance ne s'installe et le prix oscille entre les lignes (range, MA plate) ; les bornes servent alors à repérer surachat/survente.
**TRADEX-AI C1** : Règle d'entrée par cassure de canal + détection de régime range ; cœur logique du signal.
*Catégorie : signal*

---

### D2420 — Setup uptrend (ADM) + entrée sur pullback
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_03) : ADM démarre un uptrend quand les canaux tournent à la hausse et le titre surge au-dessus de la ligne haute ; le prix tient au-dessus du canal bas sur les replis. Il est souvent prudent d'attendre un pullback / meilleur point d'entrée pour améliorer le ratio reward/risk ; un oscillateur de momentum (ex. StochRSI <0.20 = survente) aide à définir l'entrée.
**TRADEX-AI C1** : Pattern d'entrée long : cassure haute confirmant l'uptrend, puis entrée sur repli (R/R amélioré) avec momentum oversold. Cohérent avec exigence R/R ≥ 1:2.
*Catégorie : configuration*

---

### D2421 — Setup downtrend (NVDA) + CCI overbought
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_04) : NVDA démarre un downtrend par un déclin marqué sous la ligne basse ; ensuite résistance près de l'EMA 20 (ligne médiane). Un CCI 10 périodes sert d'oscillateur : >100 = surachat, retour sous 100 = reprise du downtrend. Des signaux qui échouent ont indiqué un possible changement de tendance, confirmé par cassure au-dessus du canal haut.
**TRADEX-AI C1** : Pattern d'entrée short symétrique + usage de la ligne médiane comme résistance ; échecs de signaux = alerte de retournement.
*Catégorie : configuration*

---

### D2422 — Range : identifier via MA plate + ADX
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_05) : Un range/environnement plat s'identifie via une MA plate et l'Average Directional Index (ADX). Exemple IBM : oscille entre support 120–122 et résistance 130–132 (fév.→sept.), EMA 20 aplatie avr.→sept. ADX bas/en baisse = tendance faible (ADX <40 tout le temps, <30 la plupart du temps).
**TRADEX-AI C1** : Critère de détection de régime range (MA plate + ADX faible) ; gate conditionnant la stratégie surachat/survente.
*Catégorie : structure_marche*

---

### D2423 — Range : trade les bornes + confluence S/R
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_05, image_06) : En range, on utilise les Keltner pour anticiper les reversals ; les lignes de canal coïncident souvent avec support/résistance graphiques. IBM passe sous le canal bas 3 fois (points d'entrée à faible risque) sans atteindre le canal haut mais s'en approche en zone de résistance. Le graphe Disney montre une situation similaire.
**TRADEX-AI C1** : Règle de mean-reversion en range : entrées aux bornes inférieures, confluence avec S/R ; entrées « low-risk ».
*Catégorie : configuration*

---

### D2424 — Keltner vs Bollinger : différence 1 (lissage ATR vs écart-type)
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_07) : Première différence : les Keltner sont plus lisses que les Bollinger car la largeur Bollinger se base sur l'écart-type (plus volatil que l'ATR). Cette largeur plus constante rend les Keltner bien adaptés au suivi/identification de tendance.
**TRADEX-AI C1** : Argument de choix : Keltner = canal plus stable pour la tendance ; complément/alternative aux Bollinger (cf. extraction Bollinger D143–D147).
*Catégorie : indicateurs_tendance*

---

### D2425 — Keltner vs Bollinger : différence 2 (EMA vs SMA)
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md, image_07) : Deuxième différence : les Keltner utilisent une EMA (plus sensible) tandis que les Bollinger utilisent une SMA. Le graphe comparatif montre Keltner (bleu) plus lisses que Bollinger (rose), et l'écart-type couvrant une plage plus large que l'ATR.
**TRADEX-AI C1** : Distinction technique EMA vs SMA ; impacte réactivité de la ligne médiane.
*Catégorie : indicateurs_tendance*

---

### D2426 — Bottom line : identifier la tendance d'abord
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : « Keltner Channels are a trend following indicator designed to identify the underlying trend. » La tendance (up/down/plat) établit une préférence : trades haussiers favorisés en uptrend, baissiers en downtrend. Un trend plat exige une approche plus agile (pics au canal haut, creux au canal bas). À utiliser avec d'autres indicateurs ; les oscillateurs de momentum complètent bien.
**TRADEX-AI C1** : Principe directeur : préférence de trade alignée sur la tendance + confirmation multi-indicateurs. Aligné avec la logique multi-cercles TRADEX.
*Catégorie : signal*

---

### D2427 — Réglages SharpCharts (20, 2.0, 10)
🟡 **CONVENTION** (Source : keltner_channels.md, image_08, image_09) : Sur SharpCharts, overlay de prix avec défaut (20,2.0,10) : 20 = périodes de l'EMA ; 2.0 = multiplicateur ATR ; 10 = périodes de l'ATR. Place les canaux à 2 ATR au-dessus/dessous de l'EMA 20. Paramètres ajustables.
**TRADEX-AI C1** : Paramétrage outil StockCharts ; confirme les défauts de D2414. Informationnel.
*Catégorie : configuration*

---

### D2428 — Réglages StockChartsACP (défauts)
🟡 **CONVENTION** (Source : keltner_channels.md, image_10) : Sur StockChartsACP, par défaut : EMA 20 périodes, 10 périodes pour l'ATR, multiplicateur ATR 2.0. Paramètres ajustables.
**TRADEX-AI C1** : Cohérence des défauts entre plateformes StockCharts ; informationnel.
*Catégorie : configuration*

---

### D2429 — Scans : surachat/survente après cassure de canal
🟢 **FAIT VÉRIFIÉ** (Source : keltner_channels.md) : Scan haussier (oversold après breakout up) : `High il y a 20 jours > Upper Kelt Chan(20,2.0,10) il y a 20 jours` ET `CCI(10) < -100`. Scan baissier (overbought après breakout down) : `Low il y a 20 jours < Lower Kelt Chan(20,2.0,10) il y a 20 jours` ET `CCI(10) > 100`. (Univers : SMA 20 volume > 40 000.)
**TRADEX-AI C1** : Critères composites cassure de canal + CCI extrême ; transposables en règles de signal (entrée sur repli après cassure).
*Catégorie : signal*

---

### D2430 — Lectures recommandées + lien Belkhayate
🔵 **ÉCOLE / ⚫🔴 Belkhayate** (Source : keltner_channels.md) : Livres recommandés : *Trend Trading for a Living* (Thomas Carr) et *Trend Following* (Michael Covel). Aucune mention de Belkhayate ni de l'Énergie/MFI : aucun lien direct Keltner ↔ méthode Belkhayate attesté par la source. NB : Keltner est un canal ATR, structurellement proche des Bollinger, mais leur usage par Belkhayate n'est pas documenté ici.
**TRADEX-AI C1/⚫** : Références d'école trend-following ; ne PAS rattacher les Keltner à un élément Belkhayate sans validation humaine.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2411 → D2430 (20) |
| Images | 10/10 certifiées |
| Tags dominants | 🟢 littéral (15) · 🔵 ÉCOLE Keltner/Raschke (2) · 🟡 convention (2) · ⚫🔴 Belkhayate non vérifié (1, dans D2430) |
| Cercle | C1 (canal de volatilité ATR autour d'une EMA, proche Bollinger) |
| Belkhayate | ⚫🔴 D2430 : aucun lien attesté, ne rien inférer |
| Actifs | Exemples actions US (ADM, NVDA, IBM, Disney) ; livre Keltner orig. « in Commodities » mais aucun GC/HG/CL/ZW chiffré |
| Cas à vérifier | D2430 (lien Belkhayate à trancher humainement). Décision archi : Keltner vs Bollinger comme canal de volatilité de référence sur range bars NT8 (Keltner = plus lisse). |

> ⚠️ Extraction BRUT, zone validation/, NON fusionnée. Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
