# Extraction SierraChart — Average True Range
**Source :** `bundles/sierrachart/sierra_19_atr.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9071 → D9085 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=19
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : l'ATR est l'outil de mesure de volatilité de référence pour calibrer les stops, les seuils de signal et l'énergie Belkhayate sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9071 — ATR : Moving Average of True Range
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : La study Sierra Chart ID=19 calcule et affiche une Moyenne Mobile du True Range. Le True Range (TR) est la mesure de la plage de prix la plus large entre : High-Low, |High-Close précédent|, |Low-Close précédent|. L'ATR est une moyenne mobile de ces valeurs sur n barres.
**TRADEX-AI C1** : L'ATR est l'indicateur de volatilité de base pour TRADEX-AI. Il sert à calibrer les niveaux de stop-loss dynamiques, les seuils d'entrée, et à mesurer l'activité du marché sur GC, HG, CL, ZW.
*Catégorie : gestion_risque_entree*

### D9072 — Input Moving Average Length : période de calcul de l'ATR
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : L'input `Moving Average Length` (noté n dans la formule) détermine sur combien de barres la moyenne mobile du True Range est calculée. La valeur standard Wilder est 14 barres.
**TRADEX-AI C1** : Paramètre clé TRADEX-AI. ATR(14) est la valeur de référence. Sur les range bars NT8 utilisées dans TRADEX-AI, ajuster si nécessaire pour obtenir une mesure de volatilité représentative de 1-2 séances de trading.
*Catégorie : gestion_risque_entree*

### D9073 — Input Moving Average Type : 7 types de lissage disponibles
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : L'input `Moving Average Type` permet de choisir entre 7 types de lissage : Simple Moving Average (SMA), Exponential Moving Average (EMA), Linear Regression Moving Average, Weighted Moving Average, Wilders Moving Average, Simple Moving Average - Skip Zeros, Smoothed Moving Average. La formule de base documentée utilise la SMA.
**TRADEX-AI C1** : Pour TRADEX-AI, utiliser `Wilders Moving Average` (type = Wilder) pour rester cohérent avec la méthode originale de Wilder (ATR = EMA Wilder avec alpha=1/n). Éviter la SMA pure car elle traite toutes les barres avec le même poids.
*Catégorie : gestion_risque_entree*

### D9074 — Wilders Moving Average : type recommandé pour ATR original
🔵 **ÉCOLE** (Source : sierra_19_atr.md) : Wilder's Moving Average (aussi appelé Smoothed Moving Average) utilise un lissage exponentiel avec alpha=1/n, ce qui donne plus de poids aux données récentes tout en conservant un historique long. C'est le type utilisé dans la formulation originale de J. Welles Wilder pour l'ATR.
**TRADEX-AI C1** : Dans le module Python de TRADEX-AI, implémenter l'ATR avec lissage Wilder : `ATR_t = ATR_{t-1} × (n-1)/n + TR_t × 1/n` pour être cohérent avec les calculs Sierra Chart en mode Wilder.
*Catégorie : gestion_risque_entree*

### D9075 — Utilisation recommandée : Daily Chart pour ATR journalier
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : Sierra Chart précise que l'ATR peut être utilisé sur n'importe quel timeframe. Cependant, pour obtenir une moyenne du True Range journalier, il est nécessaire d'utiliser un Historical Daily Chart avec une période de 1 jour par barre.
**TRADEX-AI C1** : Pour les actifs GC/HG/CL/ZW, calculer un ATR journalier de référence sur chart Daily pour dimensionner les stops en valeur absolue (ex. stop = 1.5×ATR_daily). L'ATR intraday sur range bars NT8 sert pour les niveaux fins.
*Catégorie : gestion_risque_entree*

### D9076 — Overlay ATR sur chart intraday via Study/Price Overlay
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : Sierra Chart permet de superposer l'ATR calculé sur un Historical Daily Chart vers un chart intraday grâce à la study `Study/Price Overlay`. La procédure : ajouter ATR sur chart Daily → utiliser Study/Price Overlay sur chart intraday pour afficher la valeur ATR journalière.
**TRADEX-AI C1** : Technique avancée Sierra Chart applicable pour afficher l'ATR(14) journalier de GC sur le chart intraday range bars NT8, permettant de visualiser le contexte de volatilité quotidien lors de l'analyse des signaux TRADEX-AI.
*Catégorie : gestion_risque_entree*

### D9077 — ATR : outil de mesure de volatilité (pas directionnel)
🔵 **ÉCOLE** (Source : sierra_19_atr.md) : L'ATR mesure l'amplitude de mouvement du prix (volatilité) sans indiquer de direction. Un ATR élevé indique une forte volatilité ; un ATR faible indique une faible volatilité. L'ATR ne monte pas uniquement en marché baissier — il monte aussi en marché haussier fortement tendanciel.
**TRADEX-AI C1** : Dans la grille /10 de TRADEX-AI, l'ATR peut contribuer à C1 comme filtre de volatilité : ATR trop faible (marché endormi) = signal moins fiable ; ATR dans zone normale = conditions favorables ; ATR extrêmement élevé = marché explosif, risque accru.
*Catégorie : gestion_risque_entree*

### D9078 — ATR comme proxy d'Énergie Belkhayate (stub non codé)
⚫ **HYPOTHÈSE PROJET** (Source : sierra_19_atr.md + CLAUDE.md) : L'Énergie Belkhayate n'est pas encore codée dans TRADEX-AI (stub confirmé dans CLAUDE.md). L'ATR est mentionné comme "proxy ATR" possible pour l'Énergie. Sierra Chart ID=19 fournit une implémentation native fiable.
**TRADEX-AI C1** : En attendant la résolution du conflit MFI vs proxy ATR pour l'Énergie Belkhayate (ticket ouvert), utiliser l'ATR(14) Wilder comme mesure intermédiaire d'énergie marché dans le scoring C1 de TRADEX-AI.
*Catégorie : indicateurs_momentum*

### D9079 — Formule ATR : base SMA (remplaçable par 6 autres types)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : La formule documentée utilise une SMA comme base : `ATR_t(n) = SMA(TR, n)`. Mais Sierra Chart précise explicitement que la SMA peut être remplacée par : EMA, Linear Regression MA, Weighted MA, Wilders MA, SMA-Skip Zeros, Smoothed MA selon l'input `Moving Average Type`.
**TRADEX-AI C1** : Ce choix impacte directement les calculs Python. S'assurer que le type de moyenne utilisé dans Python correspond exactement au type configuré dans Sierra Chart pour éviter des divergences dans les signaux de confirmation.
*Catégorie : gestion_risque_entree*

### D9080 — ATR sur range bars NT8 vs ATR sur time bars
🟡 **SYNTHÈSE** (Source : sierra_19_atr.md) : Sierra Chart confirme que l'ATR fonctionne sur "any chart bar timeframe". Sur les range bars (barres de range fixe), chaque barre a par définition le même high-low range, donc le True Range se réduit à max(range, |High-Close_prev|, |Low-Close_prev|). L'ATR sur range bars est différent de l'ATR sur time bars.
**TRADEX-AI C1** : Sur les range bars NT8 utilisées dans TRADEX-AI, l'ATR(14) mesure principalement les gaps overnight et les expansions de volatilité, pas l'amplitude intrabar (fixe par construction). À documenter dans les notes de configuration TRADEX-AI Phase C.
*Catégorie : gestion_risque_entree*

### D9081 — ATR pour dimensionner stop-loss dynamique
🟡 **SYNTHÈSE** (Source : sierra_19_atr.md) : L'utilisation principale de l'ATR dans les systèmes de trading est le dimensionnement des stops dynamiques (ex. stop = prix_entrée ± k×ATR). Cette utilisation est implicite dans la documentation Sierra Chart qui positionne l'ATR comme mesure de volatilité de référence.
**TRADEX-AI C1** : Règle de gestion de risque TRADEX-AI : stop_loss_distance = 1.5 × ATR(14) comme valeur initiale. À affiner par actif (GC peut nécessiter k=2.0 en raison de sa volatilité spécifique ; ZW k=1.2 en régime calme).
*Catégorie : gestion_risque_entree*

### D9082 — Historical Daily Chart : procédure d'ouverture
🔵 **ÉCOLE** (Source : sierra_19_atr.md) : Pour obtenir l'ATR journalier dans Sierra Chart : `File >> Find Symbol >> [sélectionner symbole] >> Open Historical Chart`. La barre de temps est automatiquement à 1 jour. Ensuite, ajouter la study ATR (ID=19) sur ce chart.
**TRADEX-AI C1** : Procédure Sierra Chart documentée pour la Phase C de TRADEX-AI lors de la configuration des collecteurs de données journalières GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D9083 — ATR comme filtre de staleness et qualité de données
🟡 **SYNTHÈSE** (Source : sierra_19_atr.md) : Un ATR proche de zéro ou anormalement bas sur plusieurs barres consécutives peut indiquer des données stales (non mises à jour) ou un marché fermé (nuit, weekend, jour férié). Ce pattern est distinct d'un ATR faible normal.
**TRADEX-AI C1** : Utiliser l'ATR comme signal complémentaire dans le `staleness_monitor.py` : si ATR < seuil_minimum_attendu pour l'actif × 0.1, déclencher une alerte de qualité données avant de générer un signal.
*Catégorie : gestion_risque_entree*

### D9084 — Spreadsheet disponible : Average_True_Range.19.scss
🔵 **ÉCOLE** (Source : sierra_19_atr.md) : Sierra Chart fournit un fichier spreadsheet `Average_True_Range.19.scss` pour auditer les formules ATR. Ce fichier est enregistré dans le Data Files Folder de Sierra Chart.
**TRADEX-AI C1** : Référence de validation : si la valeur ATR calculée par TRADEX-AI diverge de Sierra Chart de plus de 0.1%, vérifier la formule Python contre ce spreadsheet (notamment le type de moyenne utilisé).
*Catégorie : gestion_risque_entree*

### D9085 — ATR : date de dernière modification Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_19_atr.md) : La page Sierra Chart ATR (ID=19) a été modifiée pour la dernière fois le lundi 17 février 2025, indiquant une documentation à jour et maintenue activement.
**TRADEX-AI C1** : La documentation Sierra Chart ATR est récente (2025). Les formules et inputs documentés sont valides pour la version courante de Sierra Chart utilisée dans TRADEX-AI Phase C.
*Catégorie : gestion_risque_entree*
