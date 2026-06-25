# Extraction SierraChart — MACD
**Source :** `bundles/sierrachart/sierra_32_macd.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9211 → D9220 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=32
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : MACD = indicateur tendance-momentum standard utilisable comme confirmation C1 sur les actifs TRADING, avec flexibilité de type de moyenne mobile.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9211 — Définition MACD Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Le MACD (Moving Average Convergence/Divergence) est un indicateur de momentum suiveur de tendance qui montre la relation entre deux moyennes mobiles de prix. Développé par Gerald Appel. Sierra Chart permet de choisir le type de moyenne mobile utilisé dans les calculs.
**TRADEX-AI C1** : Le MACD est un indicateur tendance classique pouvant servir de filtre de tendance de fond pour les signaux Belkhayate — confirme ou infirme l'alignement directionnel sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D9212 — Trois composantes calculées : MACD, Signal, Histogramme
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Le MACD Sierra Chart calcule et affiche trois indicateurs : (1) le MACD = EMA(fast) - EMA(slow) ; (2) la Moyenne Mobile du MACD (ligne Signal) = EMA du MACD sur la période MACD MA Length ; (3) le MACD Difference (histogramme) = MACD - Signal.
**TRADEX-AI C1** : Les trois composantes servent des rôles distincts dans TRADEX-AI : MACD pour la tendance, histogramme pour la vitesse du momentum (divergences), croisement MACD/Signal pour les entrées confirmées.
*Catégorie : indicateurs_tendance*

### D9213 — Inputs paramétrables : Fast, Slow, Signal lengths
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Les inputs configurables sont : Fast Moving Average Length (nF), Slow Moving Average Length (nS), MACD Moving Average Length (nM — longueur de la ligne signal). Ces trois paramètres définissent entièrement le MACD.
**TRADEX-AI C1** : Paramétrage standard MACD : nF=12, nS=26, nM=9 (configuration Appel originale). Pour TRADEX-AI sur futures, des périodes adaptées au timeframe range bars NT8 peuvent être nécessaires — à valider en Phase C backtest.
*Catégorie : indicateurs_tendance*

### D9214 — Flexibilité du type de moyenne mobile
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Le type de moyenne mobile utilisé dans les calculs est configurable via l'input Moving Average Type. Les options disponibles incluent : EMA (Exponentielle), Linear Regression Moving Average, Simple (SMA), Weighted (WMA), Wilders, Simple Skip Zeros, Smoothed.
**TRADEX-AI C1** : La possibilité de remplacer les EMA par d'autres types de MA permet d'adapter le MACD à la méthode Belkhayate — par exemple, une Weighted MA peut donner plus de poids aux prix récents, potentiellement plus réactif sur les mouvements impulsifs de l'or (GC).
*Catégorie : indicateurs_tendance*

### D9215 — Calcul MACD basé sur EMA (formule de base)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Par défaut, MACD_t = EMA_t(X, nF) - EMA_t(X, nS). La ligne signal est MACD_t_signal = EMA_t(MACD, nM). L'histogramme = MACD_t - MACD_t_signal. Les calculs commencent à t ≥ max(nS, nF) + nM pour la ligne signal et l'histogramme.
**TRADEX-AI C1** : Le MACD ne devient fiable qu'après max(26, 12) + 9 = 35 bars minimum — pour les range bars NT8 à pas variable, vérifier que le graphique contient suffisamment de bars avant de valider un signal MACD.
*Catégorie : indicateurs_tendance*

### D9216 — Input Data : source de prix flexible
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : L'input Input Data détermine la source de prix utilisée pour le calcul. Il peut s'agir du Close, Open, High, Low, ou d'autres types de données disponibles dans Sierra Chart.
**TRADEX-AI C1** : Pour TRADEX-AI, utiliser le Close (Last/Close) par défaut sur les range bars NT8 — cohérent avec la méthode Belkhayate qui travaille sur les cours de clôture de bar pour évaluer la direction.
*Catégorie : indicateurs_tendance*

### D9217 — Divergence MACD/Prix comme signal de retournement
🔵 **ÉCOLE** (Source : sierra_32_macd.md) : La divergence entre le prix et le MACD (prix fait un nouveau plus haut mais MACD ne confirme pas, ou inversement) est un signal classique de perte de momentum et de retournement potentiel.
**TRADEX-AI C1** : Divergence MACD/Prix = signal d'alerte pour le cerveau Claude dans la grille /10. Une divergence baissière sur GC (prix monte, MACD diverge) affaiblit un signal ACHETER — à pondérer dans la décision C1 Belkhayate.
*Catégorie : configuration*

### D9218 — Croisement MACD/Signal comme signal d'entrée
🔵 **ÉCOLE** (Source : sierra_32_macd.md) : Le croisement de la ligne MACD au-dessus de la ligne Signal (histogramme passe positif) est un signal haussier ; le croisement en dessous est un signal baissier. Le croisement à zéro de la ligne MACD renforce la confirmation.
**TRADEX-AI C1** : Pour TRADEX-AI, le croisement MACD/Signal peut être utilisé comme filtre d'entrée secondaire dans C1 — ne valider un signal Belkhayate que si le MACD est dans la même direction que le signal (croisement récent ou momentum confirmé).
*Catégorie : indicateurs_tendance*

### D9219 — Spreadsheet Sierra Chart disponible (MACD.32.scss)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_32_macd.md) : Sierra Chart fournit un fichier spreadsheet de référence nommé MACD.32.scss contenant les formules complètes du MACD en format tableur. Ce fichier doit être sauvegardé dans le Data Files Folder et ouvert via File >> Open Spreadsheet.
**TRADEX-AI C1** : Le fichier MACD.32.scss constitue la référence de calcul exacte Sierra — utile pour vérifier la cohérence du MACD calculé par d'autres outils (NinjaTrader, Python) avec l'implémentation Sierra de référence.
*Catégorie : indicateurs_tendance*

### D9220 — Configuration MACD recommandée TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_32_macd.md) : Configuration de référence pour TRADEX-AI : nF=12, nS=26, nM=9 (standard Appel), type MA=EMA, Input Data=Last/Close. Le MACD sert de filtre tendance C1 secondaire — il ne remplace pas les indicateurs Belkhayate (BGC, Direction, Energie, Pivots) mais les complète pour confirmer l'alignement directionnel.
**TRADEX-AI C1** : Dans la grille /10 TRADEX-AI, le MACD contribue à C1 (Prix Belkhayate) comme confirmateur de tendance — un MACD aligné avec le signal Belkhayate renforce le score; un MACD divergent peut déclasser un signal de score ≥7 à score <7 (blocage).
*Catégorie : indicateurs_tendance*
