# Extraction StockCharts — Chandelier Exit
**Source :** `bundles/stockcharts/chandelier_exit.md` (HTTP 200 · ~8 500 car.) + 9 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 9/9 certifiées
**Décisions :** D1211 → D1224 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/chandelier-exit
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Chandelier Exit? | What Is the Chandelier Exit? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Chandelier - Spreadsheet | Chandelier Exit Calculation | CERTIFIE (accord .md + HTML) |
| image_03.png | Chandelier - Chart 1 | Interpreting Chandelier Exits | CERTIFIE (accord .md + HTML) |
| image_04.png | Chandelier - Chart 2 | Interpreting Chandelier Exits | CERTIFIE (accord .md + HTML) |
| image_05.png | Chandelier - Chart 3 | Chandelier Uptrend | CERTIFIE (accord .md + HTML) |
| image_06.png | Chandelier - Chart 4 | Chandelier Downtrend | CERTIFIE (accord .md + HTML) |
| image_07.png | Using with SharpCharts | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | Chandelier - Chart 5 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_09.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1211 — Nature et origine du Chandelier Exit
🔵 **ÉCOLE (Le Beau / Elder)** (Source : chandelier_exit.md, image_01) : Développé par Charles Le Beau et présenté dans les ouvrages d'Alexander Elder, le Chandelier Exit pose un stop-loss suiveur (trailing stop-loss) basé sur l'Average True Range (ATR). L'indicateur est conçu pour maintenir le trader dans une tendance et empêcher une sortie prématurée tant que la tendance se prolonge. Typiquement, le Chandelier Exit est au-dessus des prix en downtrend et en dessous des prix en uptrend.
**TRADEX-AI C1** : Outil de **gestion de stop suiveur** directement pertinent pour le projet (gestion de risque). À traiter comme mécanisme de stop, pas comme déclencheur d'entrée.
*Catégorie : gestion_risque_entree*

---

### D1212 — Formule de calcul (long et short, 22/ATR/multiplicateur)
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_02) : La formule comporte trois parties : un plus haut/plus bas de période, l'ATR et un multiplicateur. Réglage par défaut 22 périodes sur graphique journalier (≈ 22 jours de bourse dans un mois), ce paramètre 22 servant aussi à calculer l'ATR :
```
Chandelier Exit (long)  = Plus haut sur 22 jours - ATR(22) x 3
Chandelier Exit (short) = Plus bas sur 22 jours  + ATR(22) x 3
```
**TRADEX-AI C1** : Formule déterministe de stop suiveur implémentable telle quelle ; nécessite ATR(22). Paramètres par défaut (22, 3).
*Catégorie : gestion_risque_entree*

---

### D1213 — Comportement long vs short du niveau de stop
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Le stop des positions longues est suspendu trois valeurs ATR SOUS le plus haut sur 22 périodes ; il monte et descend selon l'évolution du plus haut de période et de l'ATR. Le stop des positions courtes est placé trois valeurs ATR AU-DESSUS du plus bas sur 22 périodes.
**TRADEX-AI C1** : Stop long = trailing montant uniquement avec le high ; stop short = trailing descendant avec le low. Logique de cliquet (ratchet) à coder côté gestion de position.
*Catégorie : gestion_risque_entree*

---

### D1214 — Fondement volatilité : tampon de 3× l'ATR
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_03, image_04) : Le Chandelier Exit est un système basé sur la volatilité qui identifie les mouvements de prix démesurés. Le Beau définit la volatilité par l'ATR (développé par Welles Wilder, créateur du RSI et de l'ADX). L'ATR utilise la clôture précédente, le high et le low courants pour déterminer le « True Range » d'une période ; après lissage, les True Range quotidiens deviennent l'ATR. En plaçant le stop des longs trois ATR SOUS le plus haut, l'indicateur fournit un tampon égal à trois fois la volatilité ; un déclin assez fort pour casser ce niveau justifie une réévaluation des positions longues (inversement pour les shorts).
**TRADEX-AI C1** : Le tampon = 3 × volatilité (ATR) ; cassure du niveau = signal de réévaluation, pas vente automatique. Cohérent avec un stop adaptatif à la volatilité de chaque actif (GC/HG/CL/ZW).
*Catégorie : gestion_risque_entree*

---

### D1215 — Usage en uptrend : définir la tendance et le trailing stop
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_05) : Le Chandelier Exit peut définir la tendance et poser un stop suiveur. Exemple Eaton Corp (ETN) en breakout début novembre démarrant un uptrend prolongé : le Chandelier Exit a bien défini cet uptrend en suivant l'action des prix régulièrement à la hausse, servant à contrôler le risque sur de nouvelles positions longues.
**TRADEX-AI C1** : Confirme le rôle « contrôle du risque + définition de tendance » en uptrend ; valeur illustrative.
*Catégorie : gestion_risque_entree*

---

### D1216 — Le Chandelier Exit ne déclenche pas l'entrée (combiner StochRSI)
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_05) : Avec le Chandelier Exit fournissant le stop-loss, le trader doit trouver un autre indicateur pour déclencher les signaux d'achat dans la tendance. Un oscillateur de momentum sensible peut capturer les conditions de survente court terme : l'exemple utilise le StochRSI (Stochastic Oscillator appliqué au RSI) ; des creux sous 0,20 reflètent une survente court terme, un retour au-dessus de 0,20 suggère que l'uptrend continue.
**TRADEX-AI C1** : Règle architecturale : Chandelier Exit = stop, pas entrée → coupler à un déclencheur de momentum (ex. StochRSI) côté C1. Sépare clairement gestion de sortie et timing d'entrée.
*Catégorie : gestion_risque_entree*

---

### D1217 — Usage en downtrend et ajustement du multiplicateur pour titres volatils
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_06) : Certains titres plus volatils requièrent un tampon plus grand, donc un multiplicateur plus élevé. Sur Hewlett-Packard (HPQ) en downtrend en 2012, un Chandelier Exit normal (22, 3.0, short) aurait déclenché des stops juste avant la poursuite du downtrend (HPQ repassant au-dessus de la ligne plusieurs fois). En portant le multiplicateur à 5 (ligne rouge), on autorise plus de volatilité ; HPQ a tenu ce réglage jusqu'au breakout de mi-décembre signalant le début d'un uptrend.
**TRADEX-AI C1** : Le multiplicateur ATR est un hyperparamètre de risque par actif : plus volatil → multiplicateur plus haut pour éviter les whipsaws. À calibrer pour CL (pétrole, très volatil) vs ZW/HG.
*Catégorie : gestion_risque_entree*

---

### D1218 — Timing d'entrée en downtrend via CCI
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Le Chandelier Exit est bon pour les stops mais le trader doit utiliser l'analyse graphique de base ou un oscillateur de momentum pour timer les entrées. Le Commodity Channel Index (CCI) peut identifier les conditions de surachat court terme dans un downtrend : CCI devient suracheté au-dessus de +100 ; un retour sous +100 signale que le momentum se retourne à la baisse.
**TRADEX-AI C1** : En downtrend, déclencheur short = CCI repassant sous +100 (surachat épuisé) ; complément d'entrée, le Chandelier gérant le stop. Confirme la séparation stop/entrée.
*Catégorie : timing*

---

### D1219 — Synthèse opératoire (stop suiveur + outil de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Le Chandelier Exit sert surtout à poser un stop-loss suiveur durant une tendance, aidant à rester dans la tendance plus longtemps que prévu. Même s'il est surtout utilisé pour les stops, il peut aussi servir d'outil de tendance : une cassure au-dessus du Chandelier Exit (long) signale de la force, une cassure en dessous du Chandelier Exit (short) signale de la faiblesse. Une fois une nouvelle tendance commencée, on utilise le Chandelier Exit correspondant pour aider à définir cette tendance.
**TRADEX-AI C1** : Double rôle confirmé : (1) stop suiveur prioritaire, (2) signal de force/faiblesse sur cassure. Le rôle stop reste le principal pour le projet.
*Catégorie : gestion_risque_entree*

---

### D1220 — Paramétrage SharpCharts (défaut 22,3.0 + syntaxe short)
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_07, image_08) : L'overlay Chandelier Exit est dans la section « Overlays ». Réglages par défaut (22, 3.0), conçus pour les positions longues : 22 fixe les périodes de l'ATR et la fenêtre du plus haut/bas, 3.0 fixe le multiplicateur ATR. Les titres volatils peuvent nécessiter un multiplicateur plus élevé pour réduire les whipsaws ; les titres « ternes » un multiplicateur plus bas pour plus de sensibilité. On modifie pour les shorts en ajoutant une virgule et le mot short : (22,3.0,short).
**TRADEX-AI C1** : Référence des paramètres par défaut (22, 3.0) et règle d'ajustement (volatil → multiplicateur ↑, calme → ↓). Détail UI sinon.
*Catégorie : configuration*

---

### D1221 — Disponibilité StockChartsACP
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md, image_09) : L'overlay est ajoutable depuis le panneau Chart Settings d'un graphique StockChartsACP ; il peut être superposé au tracé du prix ou sur un panneau d'indicateur. Par défaut, 22 périodes et multiplicateur ATR 3.0, ajustables ; on peut spécifier si l'indicateur est calculé pour sortir d'une position short ou long.
**TRADEX-AI C1** : Détail plateforme (ACP) ; confirme défaut (22, 3.0) et l'option long/short. Pas de paramètre nouveau pour le moteur.
*Catégorie : configuration*

---

### D1222 — Scan « Prix croise AU-DESSUS du Chandelier Exit (long) »
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Scan repérant les actifs où le prix a croisé au-dessus du Chandelier Exit (long) avec volume quotidien au-dessus de sa MM 50 jours (croisement haussier avec volume en expansion) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily Close crosses Chandlr(22,3.0,long)]
AND [Daily Volume > Daily SMA(50,Daily Volume)]
```
**TRADEX-AI C1** : Logique « clôture franchit le Chandelier long + volume > MM50 » = signal de force, transposable en condition Python (le Chandelier servant ensuite de stop). Syntaxe de scan propre à StockCharts (non réutilisable telle quelle).
*Catégorie : signal*

---

### D1223 — Scan « Prix croise EN DESSOUS du Chandelier Exit (short) »
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Scan symétrique repérant le croisement baissier sous le Chandelier Exit (short) avec volume en expansion :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Chandlr(22,3.0,short) crosses Daily Close]
AND [Daily Volume > Daily SMA(50,Daily Volume)]
```
**TRADEX-AI C1** : Pendant baissier de D1222 ; logique « Chandelier short passe au-dessus de la clôture + volume > MM50 » = signal de faiblesse. Logique transposable, syntaxe non réutilisable.
*Catégorie : signal*

---

### D1224 — Scanning et alertes (mécanique StockCharts)
🟢 **FAIT VÉRIFIÉ** (Source : chandelier_exit.md) : Les membres StockCharts peuvent screener les actifs sur les valeurs du Chandelier Exit et configurer des alertes déclenchées sur un signal Chandelier (les alertes utilisent la même syntaxe que les scans). Les scans se collent dans la Scan Criteria box de l'Advanced Scan Workbench, les alertes dans la Technical Alert Workbench.
**TRADEX-AI C1** : Détail outil (workflow scan/alerte StockCharts) ; valeur informative — la mécanique d'alerte sur franchissement du stop est transposable au dashboard TRADEX.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1211 | Nature et origine Chandelier Exit | 🔵 ÉCOLE | C1 | gestion_risque_entree |
| D1212 | Formule long/short (22/ATR/×3) | 🟢 | C1 | gestion_risque_entree |
| D1213 | Comportement trailing long vs short | 🟢 | C1 | gestion_risque_entree |
| D1214 | Tampon 3× ATR (volatilité) | 🟢 | C1 | gestion_risque_entree |
| D1215 | Usage uptrend (trailing stop) | 🟢 | C1 | gestion_risque_entree |
| D1216 | Pas d'entrée → coupler StochRSI | 🟢 | C1 | gestion_risque_entree |
| D1217 | Downtrend / multiplicateur titres volatils | 🟢 | C1 | gestion_risque_entree |
| D1218 | Entrée downtrend via CCI | 🟢 | C1 | timing |
| D1219 | Synthèse (stop + outil tendance) | 🟢 | C1 | gestion_risque_entree |
| D1220 | Paramétrage SharpCharts (22,3.0) | 🟢 | C1 | configuration |
| D1221 | Disponibilité StockChartsACP | 🟢 | C1 | configuration |
| D1222 | Scan prix > Chandelier (long) | 🟢 | C1 | signal |
| D1223 | Scan prix < Chandelier (short) | 🟢 | C1 | signal |
| D1224 | Scanning et alertes | 🟢 | C1 | configuration |

**Liens Belkhayate :** le Chandelier Exit n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué. **Pertinence projet élevée néanmoins** : c'est un mécanisme de stop suiveur basé ATR, directement utilisable pour la gestion de risque/sortie de TRADEX-AI (catégorie gestion_risque_entree), en complément des règles d'entrée Belkhayate sans s'y substituer. Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D1212 / D1217 / D1220 — les paramètres (22, 3.0) sont conçus pour des barres journalières actions ; sur futures GC/HG/CL/ZW en Range Bars ou 15 min, la fenêtre 22 et le multiplicateur 3 doivent être recalibrés par actif (CL très volatil → multiplicateur plus haut, cf. exemple HPQ ×5).
- D1222 / D1223 — la syntaxe `Chandlr(22,3.0,long/short)` est propre à StockCharts ; seule la logique de croisement clôture/Chandelier + filtre volume est transposable.
- Cohérence projet : valider que ce stop ATR ne contredit pas une règle de stop déjà figée côté Belkhayate / GARDE_FOUS avant intégration au risk_manager.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
