# Extraction SierraChart — MACD - Volume Weighted (ID 248)
**Source :** `bundles/sierrachart/sierra_248_volume_weighted_macd.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9131 → D9150 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=248
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Variante MACD pondérée par le volume — confirme les signaux de momentum en intégrant la conviction du marché (volume) dans le calcul de la tendance.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9131 — Définition du MACD Volume Weighted
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Le MACD Volume Weighted remplace les Exponential Moving Averages (EMA) standard du MACD classique par des Volume Weighted Moving Averages (VWMA). Les trois composantes (MACD line, Signal line, Difference/Histogram) sont conservées avec la même structure que le MACD standard.
**TRADEX-AI C2** : Intégration du volume dans le calcul MACD renforce la détection de momentum avec conviction institutionnelle. Pour GC et CL (forte participation institutionnelle), ce MACD pondéré volume peut confirmer les signaux C2 (Order Flow) et renforcer la grille /10.
*Catégorie : indicateurs_momentum*

### D9132 — Paramètre Fast Moving Average Length (nF)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Input configurable nF = longueur de la VWMA rapide utilisée pour calculer la composante Fast du MACD Volume Weighted. Équivalent du Fast EMA dans le MACD classique, mais pondéré par le volume.
**TRADEX-AI C2** : Valeur standard recommandée : nF = 12 (cohérence avec MACD classique 12/26/9). Sur range bars NT8, adapter selon le timeframe utilisé. À documenter dans settings.py pour reproductibilité.
*Catégorie : indicateurs_momentum*

### D9133 — Paramètre Slow Moving Average Length (nS)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Input configurable nS = longueur de la VWMA lente. nS > nF obligatoirement pour que le MACD ait une signification (différence fast − slow). Le calcul est défini pour t ≥ max{nS, nF} + nM.
**TRADEX-AI C2** : Valeur standard : nS = 26. La période de warm-up totale = max(nS, nF) + nM. Avec 12/26/9, warm-up = 35 barres avant le premier signal valide — à gérer dans le staleness_monitor.py de TRADEX-AI.
*Catégorie : indicateurs_momentum*

### D9134 — Paramètre MACD Moving Average Length (nM)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Input configurable nM = longueur de la Signal Line (Moving Average du MACD). La Signal Line est calculée comme une EMA du MACD Volume Weighted (et non une VWMA) — détail technique important.
**TRADEX-AI C2** : La Signal Line reste une EMA même dans la version Volume Weighted. Valeur standard nM = 9. Cette asymétrie (VWMA pour MACD, EMA pour Signal) est conforme à la documentation Sierra Chart et doit être respectée dans toute implémentation Python.
*Catégorie : indicateurs_momentum*

### D9135 — Signal Line calculée en EMA (non VWMA)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : La Moving Average of the Volume Weighted MACD (Signal Line) est calculée explicitement avec une Exponential Moving Average, pas une VWMA. Seule la première étape (MACD line) utilise les VWMA.
**TRADEX-AI C2** : Point technique critique : lors d'une implémentation Python de ce MACD, la Signal Line doit être une EMA du MACD VW, et non une VWMA. Erreur fréquente à éviter. La différence change le comportement du signal en cas de volume atypique.
*Catégorie : indicateurs_momentum*

### D9136 — Calcul interne du MACD VW pour période de warm-up
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Sierra Chart calcule MACD_t en interne pour nS ≤ t < max{nS, nF} + nM, mais ces valeurs ne sont PAS affichées. Seule la valeur à t = max{nS, nF} + nM − 1 est utilisée pour initialiser l'EMA de la Signal Line.
**TRADEX-AI C2** : Le warm-up est silencieux : les premières valeurs calculées servent uniquement à initialiser la Signal Line EMA. Dans TRADEX-AI, ne pas interpréter les premières valeurs affichées comme des signaux fiables — attendre au moins nM barres supplémentaires après le warm-up initial.
*Catégorie : configuration*

### D9137 — MACD Difference = MACD VW − Signal Line
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : Le MACD Difference (histogramme) = MACD Volume Weighted − Moving Average (Signal Line). Même structure que le MACD classique mais avec les VWMA pour la ligne principale.
**TRADEX-AI C2** : Histogramme positif = MACD > Signal → momentum haussier avec conviction volume. Histogramme négatif → momentum baissier. Pour GC/HG/CL/ZW, croiser ce signal avec la Direction Belkhayate (C1) pour valider l'entrée en grille /10.
*Catégorie : indicateurs_momentum*

### D9138 — Input Data : flexibilité de la source de données
🟢 **FAIT VÉRIFIÉ** (Source : sierra_248_volume_weighted_macd.md) : L'Input Data permet de choisir la source de calcul (Close, Open, High, Low, HL/2, HLC/3, OHLC/4, etc.). La VWMA est appliquée à cette donnée source.
**TRADEX-AI C2** : Utiliser Close par défaut pour cohérence avec les autres indicateurs TRADEX-AI. Sur NT8 avec range bars, le Close de chaque barre est la dernière transaction — représentatif du prix d'équilibre du bar.
*Catégorie : indicateurs_momentum*

### D9139 — Avantage VWMA vs EMA : pondération par le volume
🔵 **ÉCOLE** (Source : sierra_248_volume_weighted_macd.md) : La VWMA pondère chaque prix par son volume correspondant, contrairement à l'EMA qui pondère par l'âge. Une barre à fort volume a plus de poids dans la VWMA qu'une barre à faible volume.
**TRADEX-AI C2** : Sur les matières premières (GC, CL), les barres à fort volume correspondent souvent à des niveaux de prix importants (pivots institutionnels, résistances/supports). Le MACD VWMA capte ces niveaux mieux que le MACD EMA standard. Pertinent pour le cercle C2 (Order Flow).
*Catégorie : volume_liquidite*

### D9140 — Cohérence avec le MACD standard : même structure 3 composantes
🟡 **SYNTHÈSE** (Source : sierra_248_volume_weighted_macd.md) : Le MACD Volume Weighted conserve exactement la même architecture que le MACD standard (3 subgraphs : MACD line, Signal Line, Difference). Seule la méthode de calcul de la MA principale change (VWMA vs EMA).
**TRADEX-AI C2** : Les traders utilisant déjà le MACD standard peuvent migrer vers la version VWMA sans changer leur logique de lecture des signaux (crossovers, divergences, histogramme). Dans TRADEX-AI, les règles d'interprétation MACD existantes dans la KB sont directement applicables à cette variante.
*Catégorie : indicateurs_momentum*

### D9141 — Pertinence pour TRADEX : confirmation momentum avec volume sur GC
🟡 **SYNTHÈSE** (Source : sierra_248_volume_weighted_macd.md) : Le MACD Volume Weighted est particulièrement pertinent pour l'Or (GC) où les mouvements institutionnels à fort volume précèdent souvent les tendances durables. Le VWMA filtre les "faux" signaux MACD sur barres à faible volume.
**TRADEX-AI C2** : Sur GC, utiliser le MACD VW comme filtre C2 dans la grille /10 : MACD VW > Signal ET histogramme positif croissant = +1 point C2. Réduit les faux signaux MACD en période de faible liquidité (nuits, veilles de fériés).
*Catégorie : gestion_risque_entree*

### D9142 — Fichier spreadsheet de référence : MACD_-_Volume_Weighted.248.scss
🔵 **ÉCOLE** (Source : sierra_248_volume_weighted_macd.md) : Sierra Chart fournit le fichier `MACD_-_Volume_Weighted.248.scss` pour vérification indépendante des formules. Date de dernière modification : 24 janvier 2025.
**TRADEX-AI C2** : Document de référence pour valider toute implémentation Python du MACD VW dans le moteur TRADEX-AI. À conserver comme source de vérification lors de la Phase C (collecteurs NT8/ATAS).
*Catégorie : configuration*
