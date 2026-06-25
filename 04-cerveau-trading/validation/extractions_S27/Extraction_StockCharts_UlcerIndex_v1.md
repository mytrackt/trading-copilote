# Extraction StockCharts — Ulcer Index
**Source :** `bundles/stockcharts/ulcer_index.md` (HTTP 200) + 6 images certifiées
**Méthode images :** double ancrage · 6/6 certifiées · 0 à vérifier
**Décisions :** D4751 → D4770 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ulcer-index
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Ulcer Index mesure le risque de drawdown — directement applicable pour calibrer le sizing et les stops sur GC/HG/CL/ZW, et pour construire une métrique de performance risk-adjusted en mode Auto.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/hxfk1quCEyHyfrEQOGeR | Chart 1 — Tableau calcul Ulcer Index 14 périodes | Calculating Ulcer Index | D4752 |
| /files/CBBmqge54QYxyqTAlV1k | Spreadsheet — calcul détaillé Ulcer Index | Calculating Ulcer Index | D4752 |
| /files/ywGPfJt4utqF3dGfV18E | Chart 2 — FSPTX avec Ulcer Index 9 semaines | Comparing Funds | D4757 |
| /files/2cn06yJLKqg9nRqGO10G | Chart 3 — FSPHX avec Ulcer Index 9 semaines | Comparing Funds | D4758 |
| /files/FOrni67mP4Bewksmv2Ud | Chart 4 — Tableau UPI comparaison FSPTX vs FSPHX | Risk-Adjusted Return | D4762 |
| /files/eKsvDJ6qqQHLO1JTn6RT | Chart 5 — SPY avec Ulcer Index SharpCharts | Using with SharpCharts | D4768 |
| /files/g6LAswK2j0TfbTBIGnxH | Chart 6 — SharpCharts Ulcer Index exemple | Using with SharpCharts | D4768 |

## DÉCISIONS

### D4751 — Définition Ulcer Index : mesure du risque de drawdown
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : L'Ulcer Index (UI) est un indicateur de volatilité mesurant UNIQUEMENT le risque baissier (downside risk). Développé par Peter Martin et Byron McCann en 1987, présenté dans *The Investor's Guide to Fidelity Funds* (1989). Conçu à l'origine pour les fonds mutuels (long only), il mesure l'amplitude et la durée des drawdowns.
**TRADEX-AI C1** : Pour TRADEX en mode long-only sur GC/HG/CL/ZW, l'Ulcer Index est plus pertinent que l'écart-type standard (qui pénalise aussi les mouvements haussiers) pour mesurer le risque réel d'une position.
*Catégorie : gestion_risque_entree*

### D4752 — Formule de calcul Ulcer Index en 3 étapes
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md, images Chart 1 et Spreadsheet) : Calcul sur 14 périodes par défaut : (1) Percent-Drawdown = ((Close − Max Close sur 14 périodes) / Max Close sur 14 périodes) × 100 ; (2) Squared Average = (Somme des Percent-Drawdown² sur 14 périodes) / 14 ; (3) Ulcer Index = Racine carrée du Squared Average.
**TRADEX-AI C1** : Formule directement codable en Python/NumPy pour les actifs TRADEX. Paramètre par défaut : 14 périodes. L'UI vaut 0 si les prix clôturent toujours plus haut (absence de drawdown).
*Catégorie : gestion_risque_entree*

### D4753 — UI = 0 quand prix font des hauts successifs
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : L'Ulcer Index est exactement zéro quand les prix clôturent à des niveaux plus élevés à chaque période. Il monte dès qu'il y a un recul par rapport au récent sommet.
**TRADEX-AI C1** : Un Ulcer Index à zéro sur GC/CL indique une tendance haussière parfaitement propre sans corrections — contexte idéal pour maintenir une position longue en mode Auto TRADEX.
*Catégorie : gestion_position_active*

### D4754 — L'UI pénalise les gros drawdowns de façon disproportionnée
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Citation de Peter Martin : "The squaring effect penalizes large drawdowns proportionately more than small drawdowns." Un drawdown de 20% pèse 4 fois plus qu'un drawdown de 10% dans le calcul (carrés).
**TRADEX-AI C1** : Propriété importante pour le risk_manager.py de TRADEX — un seul grand drawdown sur GC ou CL aura beaucoup plus d'impact sur l'UI qu'une série de petites corrections, ce qui correspond au ressenti réel du risque.
*Catégorie : gestion_risque_entree*

### D4755 — UI mesure profondeur ET durée des drawdowns
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Peter Martin : "Ulcer Index measures the depth and duration of percentage drawdowns in price from earlier highs. The greater a drawdown in value, and the longer it takes to recover to earlier highs, the higher the UI."
**TRADEX-AI C1** : Différence clé avec l'ATR (qui ne mesure que la volatilité instantanée) : l'UI intègre le temps de récupération. Sur GC, une chute de 2% suivie d'un retour rapide pèse moins qu'une chute de 1.5% qui dure 10 jours.
*Catégorie : gestion_risque_entree*

### D4756 — Supérieur à l'écart-type pour les investisseurs long-only
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : "Many consider the Ulcer Index superior to the standard deviation and other measures of risk" pour les investisseurs long-only. L'écart-type pénalise aussi la volatilité haussière, ce qui n'est pas pertinent pour un trader qui veut profiter des hausses.
**TRADEX-AI C1** : Argument pour utiliser l'UI plutôt que l'ATR ou l'écart-type pour évaluer le risque des positions longues dans risk_manager.py — particulièrement pertinent pour GC (Or, actif de refuge à tendance longue).
*Catégorie : gestion_risque_entree*

### D4757 — Interprétation : seuil UI > 10 = rare sur données hebdomadaires
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md, image Chart 2) : Sur données hebdomadaires avec UI 9 semaines, un dépassement de UI > 10 est relativement rare (observé surtout en 2008 crise financière et 2011). La moyenne mobile 52 semaines de l'UI sert de référence long terme.
**TRADEX-AI C1** : Pour calibrer les alertes TRADEX sur GC/CL : un UI (14 périodes) > 10 sur timeframe daily signale un régime de drawdown inhabituellement sévère → considérer réduction de taille ou suspension mode Auto.
*Catégorie : gestion_position_active*

### D4758 — Comparer deux actifs via leur UI : base statistique
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md, image Chart 3) : L'UI peut être utilisé pour comparer le risque relatif de deux actifs. Dans l'exemple, FSPHX (santé) a un UI moyen de 3.24 vs FSPTX (tech) à 4.71 → le fonds santé présente moins de risque de drawdown.
**TRADEX-AI C7** : Pour TRADEX C7 (Corrélations), comparer l'UI de GC vs CL vs HG vs ZW permet de classer les actifs par niveau de risque drawdown — pertinent pour le sizing proportionnel des positions en mode Auto.
*Catégorie : gestion_risque_entree*

### D4759 — Paramètre recommandé par Martin : données hebdomadaires
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Peter Martin note explicitement que "l'Ulcer Index fonctionne bien avec des données hebdomadaires" pour comparer des fonds.
**TRADEX-AI C4** : Pour l'analyse macro (contexte long terme GC/VX), calculer l'UI sur timeframe hebdomadaire. Pour les décisions d'entrée intraday sur range bars NT8, calculer l'UI sur timeframe daily ou range bars.
*Catégorie : configuration*

### D4760 — Paramètre par défaut : 14 périodes
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Le paramètre par défaut de l'Ulcer Index est de 14 périodes. Applicable sur les données de clôture.
**TRADEX-AI C1** : Point de départ pour l'implémentation TRADEX — UI(14) sur daily pour GC/HG/CL/ZW. À ajuster si nécessaire pour les range bars NT8.
*Catégorie : configuration*

### D4761 — Ulcer Performance Index (UPI) = Martin Ratio
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Martin a introduit l'Ulcer Performance Index (UPI), aussi appelé Martin Ratio : UPI = (Rendement total − Taux sans risque) / Ulcer Index. C'est l'équivalent du Sharpe Ratio mais utilisant l'UI au lieu de l'écart-type au dénominateur.
**TRADEX-AI C1** : Le Martin Ratio est une métrique de performance risk-adjusted plus adaptée à TRADEX que le Sharpe pour évaluer les stratégies long-only sur GC/HG/CL/ZW — à implémenter dans les rapports de performance du mode Auto.
*Catégorie : gestion_risque_entree*

### D4762 — UPI > Sharpe pour long-only : cas pratique
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md, image Chart 4) : Le tableau comparatif montre que le fonds santé (FSPHX) a un UPI supérieur au fonds technologie (FSPTX) malgré un rendement attendu inférieur, en raison d'un UI nettement plus bas. Conclusion : FSPHX offre un meilleur rendement ajusté au risque baissier.
**TRADEX-AI C1** : Logique applicable à TRADEX : si deux setups sur GC et CL ont des rendements attendus similaires, choisir celui avec l'UI plus faible (moins de risque de drawdown prolongé).
*Catégorie : gestion_position_active*

### D4763 — UI pas un indicateur de signal : outil de mesure de risque
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : "Keep in mind that the Ulcer Index is not an indicator per se. It is just a measure of downside risk that can be used to compute risk-adjusted returns." L'UI ne génère pas de signaux d'achat/vente directement.
**TRADEX-AI C1** : Clarification importante pour l'architecture TRADEX : l'UI ne contribue PAS au scoring de signal /10, mais alimente le risk_manager.py pour décider du sizing et de l'activation/suspension du mode Auto.
*Catégorie : gestion_risque_entree*

### D4764 — UI monte quand prix baissent sous leur récent sommet
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : "The index rises when prices move lower and extend from their recent high." L'UI est dynamique — il augmente au fur et à mesure que le drawdown s'approfondit et que le temps passe sans récupération.
**TRADEX-AI C1** : Critère de surveillance temps réel pour TRADEX mode Auto : si UI d'une position ouverte sur GC/CL dépasse un seuil (ex : UI > 7), déclencher une alerte ou réduire le stop.
*Catégorie : gestion_position_active*

### D4765 — Lissage de l'UI avec moyenne mobile pour tendance long terme
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : L'exemple StockCharts montre un UI 9-semaines lissé par une SMA52 pour distinguer la valeur courante de la moyenne long terme. Quand l'UI courant dépasse significativement sa moyenne → régime de risque élevé.
**TRADEX-AI C1** : Pour le dashboard TRADEX, afficher l'UI(14) et sa SMA(50) pour chaque actif TRADING — le dépassement UI > SMA50 est un signal d'alerte précoce de stress de marché.
*Catégorie : gestion_position_active*

### D4766 — UI adapté aux investisseurs long-only, pas aux traders short
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : "The Ulcer Index measures risk by focusing on drawdowns represented by price declines. This means it is best suited for long-only investors or traders." Pour un trader short, les hausses de prix sont le risque réel et l'UI ne le capture pas.
**TRADEX-AI C1** : Pour les positions VENTE sur GC/HG/CL/ZW en mode Auto TRADEX, l'UI classique n'est pas l'outil adapté — utiliser ATR ou un UI inversé (drawdown depuis le bas) pour mesurer le risque d'une position courte.
*Catégorie : gestion_risque_entree*

### D4767 — Scan pour filtrer les actifs à haute volatilité (UI < 10)
🔵 **ÉCOLE** (Source : ulcer_index.md) : Exemple de scan : `ULCER(14) < 10` combiné avec `EMA(50) > EMA(200)` pour filtrer les actions en uptrend ayant un UI acceptable. Utilisation de l'UI comme filtre de qualité risque.
**TRADEX-AI C1** : Applicable dans TRADEX : si UI(14) > seuil calibré pour GC/CL → exclure l'actif du panier de signals ce jour. Implémentable dans le Niveau 2 de filtrage Python (avant appel Claude API).
*Catégorie : gestion_risque_entree*

### D4768 — Placement visuel dans SharpCharts : derrière ou sous le prix
🔵 **ÉCOLE** (Source : ulcer_index.md, images Chart 5 et Chart 6) : L'UI peut être placé derrière le graphique de prix pour accentuer les mouvements relatifs, ou dans une fenêtre séparée. Des lignes horizontales de seuil de risque peuvent être ajoutées.
**TRADEX-AI C1** : Dans le dashboard React TRADEX, afficher l'UI dans un panneau séparé sous chaque graphique de prix des actifs TRADING, avec une ligne horizontale de seuil d'alerte personnalisable par Abdelkrim.
*Catégorie : configuration*

### D4769 — UI et taux sans risque pour le Martin Ratio
🟢 **FAIT VÉRIFIÉ** (Source : ulcer_index.md) : Dans le calcul UPI, le taux sans risque utilisé dans l'exemple est le rendement du T-Bond 10 ans ($TNX). La formule : UPI = (Rendement attendu − Taux sans risque) / UI moyen.
**TRADEX-AI C4** : Pour les backtests TRADEX, utiliser le T-Bond 10 ans comme référence sans risque dans le calcul UPI — cohérent avec la pratique standard des gestionnaires et avec la surveillance macro C4 (taux Fed).
*Catégorie : gestion_risque_entree*

### D4770 — Objectif : trouver les actifs au plus haut UPI (rendement ajusté le plus élevé)
🟡 **SYNTHÈSE** (Source : ulcer_index.md) : L'objectif de l'Ulcer Performance Index est d'identifier les actifs ou stratégies avec le plus haut ratio rendement/risque-baissier. Plus l'UPI est élevé, meilleure est la performance nette du risque de drawdown supporté.
**TRADEX-AI C1** : En mode Auto TRADEX, prioriser les signaux sur l'actif TRADING ayant le meilleur UPI historique (calculé en rolling sur 30 jours) parmi GC/HG/CL/ZW — intégrer dans le module correlations.py comme critère de sélection d'actif.
*Catégorie : gestion_position_active*
