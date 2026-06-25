# Extraction StockCharts — Rate of Change (ROC)
**Source :** `bundles/stockcharts/rate_of_change_roc.md` (HTTP 200 · ~18 800 car.) + 12 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 12/12 certifiées
**Décisions :** D3351 → D3370 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/rate-of-change-roc
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Rate of Change Indicator? | What Is the Rate of Change Indicator? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | ROC - Spreadsheet 1 | Rate of Change Calculation | CERTIFIE (accord .md + HTML) |
| image_03.png | ROC - Calculation Example | Rate of Change Calculation | CERTIFIE (accord .md + HTML) |
| image_04.png | Using the ROC to identify oversold conditions | Oversold Conditions | CERTIFIE (accord .md + HTML) |
| image_05.png | Using the ROC to identify overbought conditions | Overbought Conditions | CERTIFIE (accord .md + HTML) |
| image_06.png | High volatility stock with ROC | Using ROC with High Volatility Stocks | CERTIFIE (accord .md + HTML) |
| image_07.png | Adjusting the chart to accomodate high volatility | Using ROC with High Volatility Stocks | CERTIFIE (accord .md + HTML) |
| image_08.png | Identifying the trend using ROC | Identifying Trends With Rate of Change | CERTIFIE (accord .md + HTML) |
| image_09.png | Using the ROC to identify potential divergences | Identifying Divergences with Rate of Change | CERTIFIE (accord .md + HTML) |
| image_10.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_11.png | SharpCharts Settings for the ROC (Rate of Change) Indicator | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_12.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3351 — Nature de l'indicateur ROC (momentum pur)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_01) : Le Rate of Change (ROC), aussi appelé Momentum, est un oscillateur de momentum pur qui mesure la variation en pourcentage du prix d'une période à la suivante. Le calcul compare le prix actuel au prix d'il y a « n » périodes. Le tracé forme un oscillateur fluctuant au-dessus et au-dessous de la ligne zéro selon que le rythme de variation passe du positif au négatif.
**TRADEX-AI C3** : Oscillateur de momentum candidat pour mesurer l'accélération/décélération de GC/HG/CL/ZW ; à traiter comme feature continue, pas comme déclencheur autonome.
*Catégorie : indicateurs_momentum*

---

### D3352 — Signaux génériques de ROC
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : En tant qu'oscillateur de momentum, les signaux ROC incluent : croisements de ligne centrale, divergences, et lectures de surachat/survente. Les divergences échouent à anticiper les retournements plus souvent qu'elles ne réussissent (discussion détaillée écartée par la source). Les croisements de ligne centrale, bien que sujets au whipsaw surtout à court terme, peuvent servir à identifier la tendance globale. L'identification des extrêmes de surachat/survente vient naturellement avec ROC.
**TRADEX-AI C3** : Hiérarchie de fiabilité posée par la source : surachat/survente > tendance via ligne centrale > divergences (peu fiables). À respecter dans la pondération du score /10.
*Catégorie : signal*

---

### D3353 — Formule de calcul du ROC
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_02, image_03) : Formule :
```
ROC = [(Close - Close il y a n périodes) / (Close il y a n périodes)] * 100
```
L'exemple tabulé montre le ROC 12 jours sur le Dow Industrials en mai 2010. Les cellules jaunes montrent le ROC du 28 avril au 14 mai (13 jours de trading réels, le close du 28 servant de point de départ le 29). Les cellules bleues montrent le ROC 12 jours du 7 au 25 mai.
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; attention au décalage d'indexation (« n périodes ago » = n+1 closes impliqués). Paramètre par défaut 12.
*Catégorie : indicateurs_momentum*

---

### D3354 — Interprétation de base (rise over run)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : ROC est le momentum sous sa forme la plus pure : la « hausse » (variation de prix) sur le « parcours » (temps). Les prix montent tant que ROC reste positif, baissent tant qu'il est négatif. ROC s'étend en territoire positif quand une avance accélère, et plonge davantage en négatif quand un déclin accélère.
**TRADEX-AI C3** : Lecture directe de la direction + accélération ; ROC positif/négatif = filtre binaire de tendance, l'amplitude = intensité.
*Catégorie : indicateurs_momentum*

---

### D3355 — Bornes asymétriques du ROC
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : ROC n'a aucune borne supérieure (le ciel est la limite pour une avance), mais a une borne inférieure : un titre ne peut décliner que de 100 % (jusqu'à zéro). Malgré ces bornes asymétriques, ROC produit des extrêmes identifiables signalant surachat et survente.
**TRADEX-AI C3** : L'asymétrie (gains illimités / pertes plafonnées à -100 %) doit être prise en compte si ROC est normalisé ; ne pas appliquer de seuils symétriques aveugles sur des actifs très volatils.
*Catégorie : indicateurs_momentum*

---

### D3356 — ROC idéal en marché latéral, oscillation en tendance
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Il existe trois mouvements de prix : haussier, baissier, latéral. Les oscillateurs comme ROC sont idéalement adaptés au mouvement latéral avec fluctuations régulières (extrêmes plus faciles à identifier). En tendance, les prix fluctuent aussi : un uptrend = série de plus hauts/plus bas croissants en zigzag, avec des pullbacks à intervalles réguliers (% ou temps) ; un downtrend = plus bas/plus hauts décroissants, avec des rebonds contre-tendance culminant sous le précédent sommet. ROC peut repérer les niveaux de % ayant précédé un retournement passé.
**TRADEX-AI C1** : ROC pertinent surtout en range — cohérent avec « pas de signal directionnel pur en tendance forte » ; à coupler avec un détecteur de régime.
*Catégorie : structure_marche*

---

### D3357 — Survente dans un uptrend (exemple INTC)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_04) : Sur Intel (INTC) en uptrend de juin 2025 à janvier 2026, ROC sert à identifier les niveaux de survente court terme comme opportunités de participer à la tendance majeure ; les signaux de surachat court terme sont ignorés car la tendance de fond est haussière. Sur la base du rebond de juillet-août 2025, -10 % est fixé comme borne de survente. Les réglages surachat/survente dépendent de la volatilité (titre plus volatil : -15 % ; moins volatil : -5 %). Une survente alerte d'un retournement potentiel mais le prix n'a pas encore tourné — un titre peut rester survendu. Une SMA 20 jours est superposée pour confirmer le retournement réel : après survente ROC mi-novembre, INTC passe au-dessus de sa SMA 20 fin novembre (confirmation) ; deuxième survente mi-décembre confirmée fin décembre.
**TRADEX-AI C3** : Règle opérationnelle clé — en tendance, n'utiliser que les extrêmes alignés avec la tendance (survente en uptrend), et confirmer par croisement de SMA 20 avant d'agir. Le seuil dépend de la volatilité de l'actif → calibrer par GC/HG/CL/ZW.
*Catégorie : signal*

---

### D3358 — Surachat dans un downtrend (exemple CRM)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_05) : Sur Salesforce (CRM) en downtrend de novembre 2021 à décembre 2022, le ROC standard 12 jours identifie les niveaux de surachat dans une tendance baissière majeure. Le plus haut de fin mars survient avec un surachat au-dessus de +10 % (hausse >10 % sur 12 jours ≈ 2,5 semaines). Surachat suivant en juin (>+10 %), bref dépassement fin juillet, puis cassure du support en trend line fin août = continuation baissière. Surachat suivant fin octobre 2022 ; le titre casse finalement le support à 138 début décembre 2022.
**TRADEX-AI C3** : Symétrique de D3357 — en downtrend, n'exploiter que les surachats (contre-tendance) comme zones de re-short. Le nombre de périodes dépend du titre et du timeframe visé.
*Catégorie : signal*

---

### D3359 — ROC sur titres très volatils (exemple ANF)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_06) : Sur Abercrombie & Fitch (ANF) en range d'octobre 2006 à février 2008, le ROC 20 jours fixe surachat à +10 % et survente à -10 %. Les niveaux identifient bien les extrêmes, mais timer le retournement réel est plus difficile à cause de la volatilité.
**TRADEX-AI C3** : Avertissement — sur actif volatil, les seuils ROC repèrent les extrêmes mais le timing reste imprécis ; nécessite un filtre de lissage (cf. D3360).
*Catégorie : signal*

---

### D3360 — Lissage par EMA + SMA du ROC (exemple ANF suite)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_07) : Pour réduire la volatilité : ANF affiché en EMA 10 jours (noir), prix réel invisible ; EMA 30 jours superposée comme ligne de signal ; ROC 20 jours affiché avec une SMA 5 jours pour lisser. Moins de lectures surachat/survente avec la SMA 5. Signaux d'achat : ligne verte pointillée quand ROC dépasse -10 %, flèche verte quand l'EMA 10 croise au-dessus de la SMA 30. Les survente sont généralement précoces, les croisements de moyennes mobiles généralement tardifs. EMA 10 choisie car plus rapide qu'une SMA 10 ; SMA 30 car plus lente qu'une EMA 30 — accélérer la courte et ralentir la longue donne des signaux légèrement plus rapides.
**TRADEX-AI C3** : Technique anti-whipsaw transposable : lisser le ROC (SMA courte) et confirmer par croisement EMA/SMA. Paramètres 10/30 et SMA 5 à recalibrer sur le timeframe Belkhayate.
*Catégorie : indicateurs_momentum*

---

### D3361 — ROC multi-timeframe pour définir la tendance (cadre 252/126/63/21)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Bien que les oscillateurs conviennent mieux aux ranges, ils peuvent définir la direction globale. ≈252 jours de trading par an, soit 126 jours/semestre, 63 jours/trimestre, 21 jours/mois. Un retournement de tendance commence sur le timeframe le plus court et se diffuse progressivement aux autres. La tendance long terme est généralement haussière quand les ROC 252 jours ET 126 jours sont tous deux positifs (prix supérieurs à ceux d'il y a 12 et 6 mois → positions longues prises il y a 6-12 mois rentables).
**TRADEX-AI C3** : Architecture multi-horizon directement transposable au filtrage de tendance ; alignement de plusieurs ROC = confirmation de direction (analogue à la logique d'alignement multi-actifs TRADEX). Paramètres en jours, à convertir pour range bars.
*Catégorie : indicateurs_tendance*

---

### D3362 — Lecture séquentielle des 4 ROC (exemple IBM)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_08) : Sur IBM avec ROC 252/126/63/21, trois grandes tendances en trois ans : (1) hausse, ROC 252 largement positif jusqu'à sept. 2008 ; (2) baisse, indicateur négatif d'oct. 2008 à sept. 2009 ; (3) hausse depuis fin sept. 2009. Même si l'uptrend persiste, IBM s'aplatit, affectant les ROC 126 et 63. Le ROC 63 (trimestriel) flirte avec le négatif depuis février (4) ; le ROC 126 (semestriel) plonge en négatif pour la première fois depuis avril 2009 (5). Cela montre une détérioration alertant à surveiller ; une cassure sous le range de 6 mois serait baissière (6).
**TRADEX-AI C3** : Illustration que la détérioration apparaît d'abord sur les ROC courts — système d'alerte précoce de retournement à exploiter comme indicateur avancé de fin de tendance.
*Catégorie : indicateurs_tendance*

---

### D3363 — Divergences ROC : prudence (faux signaux)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_09) : Les divergences haussières/baissières entre ROC et prix existent mais peuvent être trompeuses à cause des mouvements brusques. Les avances soutenues démarrent souvent par une forte poussée initiale ; les avances suivantes étant moins fortes, une divergence baissière se forme dans le ROC. Rappel : les prix montent tant que ROC reste positif — des lectures positives plus faibles qu'avant reflètent toujours une hausse, pas une baisse.
**TRADEX-AI C3** : Garde-fou anti-faux-signal — ne PAS interpréter une divergence baissière ROC comme un signal de vente tant que ROC reste positif. Divergences = signal faible, à ne pas pondérer fortement dans le /10.
*Catégorie : signal*

---

### D3364 — Synthèse opératoire (The Bottom Line)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Le ROC mesure la vitesse de variation des prix : une poussée vers le haut reflète une forte avance, une chute reflète un déclin abrupt. ROC est le mieux utilisé pour identifier les extrêmes de surachat/survente, typiquement indiqués quand ROC croise au-dessus de 10 ou sous -10. Des ROC multi-timeframes plus longs aident à identifier la tendance globale. Les divergences peuvent être trompeuses et doivent être utilisées avec prudence. Comme tout indicateur, ROC doit s'utiliser conjointement à d'autres aspects de l'analyse technique.
**TRADEX-AI C3** : Seuils repères ±10 = surachat/survente. ROC = jamais seul, toujours en confirmation → conforme à la règle TRADEX d'alignement multi-critères avant tout signal.
*Catégorie : signal*

---

### D3365 — Paramétrage SharpCharts (défaut 12, lignes ±10)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_10, image_11) : ROC peut être placé au-dessus, en dessous ou derrière le tracé du prix. À la sélection, le paramètre est réglé sur 12 par défaut, ajustable pour augmenter/diminuer la sensibilité. On peut ajouter une moyenne mobile (ligne de signal / lissage) ou des lignes horizontales (Overlay). Dans l'exemple, des lignes rouges à +10 et -10 marquent surachat/survente.
**TRADEX-AI C1** : Confirme le défaut 12 et l'usage de lignes ±10 comme bornes de surachat/survente ; paramètre unique simple à coder.
*Catégorie : indicateurs_momentum*

---

### D3366 — Paramétrage StockChartsACP
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md, image_12) : Dans StockChartsACP, l'indicateur s'ajoute via le panneau Chart Settings (positionnable au-dessus, en dessous ou derrière le prix). Par défaut, il examine la variation de prix sur 12 périodes, paramètre ajustable.
**TRADEX-AI C1** : Redondant avec D3365 sur le défaut 12 ; valeur informative sur l'outil, pas de nouveau paramètre exploitable.
*Catégorie : indicateurs_momentum*

---

### D3367 — Scan « Oversold Rate of Change »
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Scan repérant les actions avec ROC 126 jours positif ET ROC 21 jours survendu (< -8 %) ; signal haussier déclenché quand le titre clôture au-dessus de sa SMA 20 :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily ROC(126,Daily Close) > 0]
AND [Daily ROC(21,Daily Close) < -8]
AND [Yesterday's Daily Close < Yesterday's Daily SMA(20,Daily Close)]
AND [Daily Close > Daily SMA(20,Daily Close)]
```
**TRADEX-AI C3** : Logique « tendance LT haussière (ROC 126 > 0) + survente CT (ROC 21 < -8) + confirmation croisement SMA 20 » directement transposable en condition Python. Syntaxe de scan propre à StockCharts (non réutilisable telle quelle), seule la logique compte.
*Catégorie : signal*

---

### D3368 — Scan « Overbought Rate of Change »
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Scan symétrique : ROC 126 jours négatif ET ROC 21 jours suracheté (> 8 %) ; signal baissier quand le titre clôture sous sa SMA 20 :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily ROC(126,Daily Close) < 0]
AND [Daily ROC(21,Daily Close) > 8]
AND [Yesterday's Daily Close > Yesterday's Daily SMA(20,Daily Close)]
AND [Daily Close < Daily SMA(20,Daily Close)]
```
**TRADEX-AI C3** : Logique « tendance LT baissière + surachat CT + confirmation croisement SMA 20 » transposable pour les signaux short. Seule la logique est réutilisable (syntaxe StockCharts spécifique).
*Catégorie : signal*

---

### D3369 — Combinaison ROC 126 + ROC 21 (alignement multi-horizon)
🟢 **FAIT VÉRIFIÉ** (Source : rate_of_change_roc.md) : Les deux scans (D3367/D3368) reposent sur un principe commun explicite : utiliser un ROC long (126 j) pour qualifier la tendance de fond et un ROC court (21 j) pour repérer l'extrême contre lequel entrer, la confirmation venant d'un croisement de SMA 20.
**TRADEX-AI C3** : Pattern « tendance longue + extrême court + déclencheur de confirmation » = structure exactement isomorphe à l'architecture événementielle TRADEX (Niveau 1 filtre, Niveau 3 déclenche). Modèle de référence pour assembler un signal ROC dans le score /10.
*Catégorie : signal*

---

### D3370 — Lectures recommandées
🔵 **ÉCOLE (Murphy / Pring)** (Source : rate_of_change_roc.md) : *Technical Analysis of the Financial Markets* (John Murphy) consacre un chapitre aux oscillateurs de momentum (pros/cons et exemples spécifiques au ROC). *Technical Analysis Explained* (Martin Pring) couvre les bases des indicateurs de momentum (divergences, croisements, autres signaux), avec deux chapitres dédiés à des indicateurs de momentum spécifiques.
**TRADEX-AI C3** : Références bibliographiques pour approfondir le momentum ; aucune règle exploitable directement, valeur documentaire.
*Catégorie : indicateurs_momentum*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3351 | Nature du ROC (momentum pur) | 🟢 | C3 | indicateurs_momentum |
| D3352 | Signaux génériques ROC | 🟢 | C3 | signal |
| D3353 | Formule de calcul ROC | 🟢 | C1 | indicateurs_momentum |
| D3354 | Interprétation rise/run | 🟢 | C3 | indicateurs_momentum |
| D3355 | Bornes asymétriques | 🟢 | C3 | indicateurs_momentum |
| D3356 | ROC idéal en range | 🟢 | C1 | structure_marche |
| D3357 | Survente en uptrend (INTC) | 🟢 | C3 | signal |
| D3358 | Surachat en downtrend (CRM) | 🟢 | C3 | signal |
| D3359 | ROC sur titres volatils (ANF) | 🟢 | C3 | signal |
| D3360 | Lissage EMA+SMA du ROC | 🟢 | C3 | indicateurs_momentum |
| D3361 | Multi-timeframe 252/126/63/21 | 🟢 | C3 | indicateurs_tendance |
| D3362 | Lecture séquentielle 4 ROC (IBM) | 🟢 | C3 | indicateurs_tendance |
| D3363 | Divergences ROC (prudence) | 🟢 | C3 | signal |
| D3364 | Synthèse opératoire (±10) | 🟢 | C3 | signal |
| D3365 | Paramétrage SharpCharts | 🟢 | C1 | indicateurs_momentum |
| D3366 | Paramétrage StockChartsACP | 🟢 | C1 | indicateurs_momentum |
| D3367 | Scan Oversold ROC | 🟢 | C3 | signal |
| D3368 | Scan Overbought ROC | 🟢 | C3 | signal |
| D3369 | Combinaison ROC 126+21 | 🟢 | C3 | signal |
| D3370 | Lectures recommandées | 🔵 ÉCOLE | C3 | indicateurs_momentum |

**Liens Belkhayate :** ROC n'est PAS un indicateur Belkhayate (⚫). Lien indirect : ROC est un oscillateur de momentum standard (famille proche du MFI = « Énergie » Belkhayate, mais distinct — le MFI intègre le volume, pas le ROC). Le ROC peut servir de feature de momentum complémentaire (C3) en confirmation de la « Direction » Belkhayate, jamais en substitution de l'Énergie/MFI. ⚫🔴 si proposé comme proxy d'Énergie : NON, car formule différente.

**À vérifier (humain) :**
- D3357 — exemple INTC daté « juin 2025 à janvier 2026 » : cohérence temporelle douteuse (futur par rapport à la rédaction historique de la page) ; probablement données mises à jour par StockCharts. Sans impact sur la logique, mais ne pas réutiliser les dates comme fait historique.
- D3358 — la source écrit « This means **Microsoft** was up over 10% » alors que l'exemple porte sur **Salesforce (CRM)** : erreur de copier-coller dans la source. Lire « CRM », pas Microsoft.
- D3367 / D3368 — syntaxe de scan propre à StockCharts ; seule la logique (ROC long + ROC court + croisement SMA 20) est transposable, pas le code.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
