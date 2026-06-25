# Extraction SierraChart — ADX (ID 13)
**Source :** `bundles/sierrachart/sierra_13_adx.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8931 → D8950 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=13
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : ADX de Welles Wilder — mesure de force de tendance, filtre tendance/range essentiel pour la grille de scoring /10 Belkhayate (C1).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D8931 — ADX Sierra Chart ID 13 : définition — Average Directional Movement Index de Welles Wilder
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : L'étude ADX (ID 13) dans Sierra Chart calcule et affiche l'Average Directional Movement Index (ADX) de Welles Wilder. L'ADX est basé sur des calculs similaires à ceux utilisés dans le Directional Movement Index (DMI).
**TRADEX-AI C1** : L'ADX est l'indicateur de force de tendance de référence mondiale — il mesure l'intensité d'une tendance sans indiquer sa direction. Sur GC (Or), un ADX fort (>25) confirme une tendance directionnelle exploitable pour la méthode Belkhayate, tandis qu'un ADX faible (<20) signale un marché en range à éviter.
*Catégorie : indicateurs_tendance*

### D8932 — ADX Sierra Chart : paramètre DX Length — longueur du Directional Index
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : L'étude ID 13 dispose de l'input "DX Length" (noté n_DX dans la formule). Ce paramètre contrôle la longueur des Directional Indicators DI+ et DI-. C'est le premier paramètre configurable de l'ADX.
**TRADEX-AI C1** : Paramètre opérationnel TRADEX — DX Length = 14 (valeur originale Welles Wilder, universellement adoptée). Ne pas modifier sans validation backtest sur GC/CL. La valeur 14 correspond à 14 barres de la période choisie (14 jours en daily, 14 range bars en intraday).
*Catégorie : configuration*

### D8933 — ADX Sierra Chart : paramètre DX Mov Avg Length — longueur de la moyenne mobile de lissage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : L'étude ID 13 dispose de l'input "DX Mov Avg Length" (noté n_ADX dans la formule). L'ADX est calculé comme une Wilders Moving Average du DX sur cette longueur. La formule : ADX_t(n_DX, n_ADX) est une Wilder's MA du DX calculée pour t >= n_DX + n_ADX - 1.
**TRADEX-AI C1** : Paramètre opérationnel TRADEX — DX Mov Avg Length = 14 (valeur Welles Wilder standard). La combinaison DX Length 14 / DX Mov Avg Length 14 est la configuration canonique ADX. L'ADX nécessite n_DX + n_ADX - 1 = 27 barres minimum avant de produire des valeurs — à noter pour les charts avec peu d'historique.
*Catégorie : configuration*

### D8934 — ADX Sierra Chart : utilisation obligatoire de la Wilders Moving Average
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : La formule Sierra Chart de l'ADX utilise explicitement une "Wilders Moving Average" pour lisser le DX. La Wilder's MA est l'EMA à facteur de lissage 1/n (différente de l'EMA standard à facteur 2/(n+1)).
**TRADEX-AI C1** : Précision technique importante — le lissage Wilders (pas EMA standard) est la définition originale de l'ADX. Si TRADEX calcule l'ADX en Python, utiliser la formule Wilders (alpha = 1/n) et non l'EMA standard pour rester cohérent avec Sierra Chart et la définition de Welles Wilder.
*Catégorie : configuration*

### D8935 — ADX Sierra Chart : calcul des DI+ et DI- légèrement différent du DMI standard
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : "The ADX is based on calculations similar to those used in the Directional Movement Index. Just as in that study, the DX Length Input is denoted as n_DX. The Directional Indicators DI_t^(+)(n_DX) and DI_t^(-)(n_DX) are calculated slightly differently here, as shown below."
**TRADEX-AI C1** : Nuance technique Sierra Chart — l'ADX (ID 13) et le DMI ADX ADXR (étude distincte dans Sierra Chart) calculent DI+ et DI- de façon légèrement différente. Pour la cohérence TRADEX, utiliser un seul indicateur Sierra Chart (ADX ID 13) comme référence, ne pas mixer ADX et DMI du même chart.
*Catégorie : configuration*

### D8936 — ADX Sierra Chart : condition minimale de calcul — barres requises avant premier signal
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : L'ADX est calculé pour t >= n_DX + n_ADX - 1. Le DX est initialement égal à zéro et calculé pour t >= 0. Avec les paramètres standard (14/14), le premier ADX valide apparaît à la barre t = 27 (14 + 14 - 1 = 27).
**TRADEX-AI C1** : Règle opérationnelle TRADEX — sur les charts avec peu d'historique (ex : nouveau contrat ou chart fraîchement chargé), ignorer les premières 27 barres de l'ADX (valeurs non fiables). Dans data_reader.py, ajouter une validation "ADX valide seulement si plus de 30 barres disponibles".
*Catégorie : gestion_risque_entree*

### D8937 — ADX Sierra Chart : disponibilité spreadsheet officielle de l'ADX
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : Sierra Chart fournit une spreadsheet officielle "ADX.13.scss" contenant les formules de l'ADX. Elle doit être sauvegardée dans le Data Files Folder et ouverte via File >> Open Spreadsheet.
**TRADEX-AI C1** : Validation croisée disponible — la spreadsheet ADX.13.scss permet de vérifier les calculs Python de l'ADX dans TRADEX avant intégration en production. Procédure de validation : charger le .scss Sierra Chart, comparer colonne ADX Sierra vs calcul Python sur les mêmes données GC.
*Catégorie : configuration*

### D8938 — ADX Sierra Chart : étude distincte du DMI ADX ADXR (ID différent dans le catalogue)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : Le catalogue Sierra Chart liste séparément : "ADX" (ID 13), "ADXR" (study distincte), et "DMI ADX ADXR" (étude combinée). Ce sont 3 études distinctes avec des outputs différents.
**TRADEX-AI C1** : Pour TRADEX, utiliser uniquement ADX ID 13 (ligne ADX seule) pour la mesure de force de tendance. Si DI+/DI- directionnels sont nécessaires pour le scoring, utiliser "DMI ADX ADXR" qui inclut les trois composantes. Ne pas confondre les deux études dans l'export JSON Sierra Chart.
*Catégorie : configuration*

### D8939 — ADX Sierra Chart : seuil opérationnel — ADX 25 comme frontière tendance/range
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : La documentation Sierra Chart ne définit pas de seuil fixe d'interprétation. Les seuils opérationnels standards (ADX < 20 = range, ADX 20-25 = faible tendance, ADX > 25 = tendance confirmée, ADX > 40 = tendance forte) proviennent de la littérature Welles Wilder.
**TRADEX-AI C1** : Seuils opérationnels TRADEX validés par la méthode Belkhayate — ADX < 20 : bloquer signal Mode Auto (marché range, signaux peu fiables) · ADX 20-25 : signal Manuel uniquement · ADX > 25 : signal Auto autorisé si autres conditions remplies · ADX > 40 : attention retournement possible (tendance mature).
*Catégorie : gestion_risque_entree*

### D8940 — ADX Sierra Chart : ADX ne donne pas la direction — combinaison obligatoire avec DI+/DI-
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : L'ADX mesure uniquement la FORCE de la tendance, pas sa direction. La direction est donnée par DI+ (haussier) vs DI- (baissier). Un ADX en hausse avec DI+ > DI- indique une tendance haussière forte ; DI- > DI+ indique une tendance baissière forte.
**TRADEX-AI C1** : Règle fondamentale TRADEX — dans la grille de scoring /10, le critère "tendance C1" doit combiner ADX (force) ET comparaison DI+/DI- (direction). Score partiel si ADX > 25 mais direction DI non alignée avec le signal Belkhayate BGC. Utiliser DMI ADX ADXR pour accéder à DI+/DI-.
*Catégorie : indicateurs_tendance*

### D8941 — ADX Sierra Chart : ADXR disponible — Average Directional Movement Index Rating
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : Sierra Chart propose "ADXR" comme étude séparée dans son catalogue. L'ADXR est la moyenne de l'ADX actuel et de l'ADX d'il y a n périodes — il est plus lissé que l'ADX standard.
**TRADEX-AI C1** : L'ADXR peut être utilisé comme filtre de tendance de long terme dans TRADEX — sa nature plus lissée le rend moins sensible aux faux signaux de tendance (ex : pics ADX temporaires sur news). Pour la surveillance 2s, utiliser ADX (plus réactif) pour l'intraday et ADXR (plus stable) pour le contexte de tendance globale.
*Catégorie : indicateurs_tendance*

### D8942 — ADX Sierra Chart : documentation Last Modified — date de stabilité
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : La documentation Sierra Chart pour l'étude ADX ID 13 a été modifiée le "Sunday, 29th January, 2023".
**TRADEX-AI C1** : Documentation stable depuis janvier 2023 — plus de 3 ans sans modification. L'ADX ID 13 Sierra Chart est un indicateur mature avec une API stable. Son intégration dans TRADEX ne présente pas de risque de breaking change côté Sierra Chart.
*Catégorie : configuration*

### D8943 — ADX Sierra Chart : utilisation avec Notation Sigma (Sommation)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : "For an explanation of the Sigma (Σ) notation for summation, refer to our description here." La formule ADX utilise la notation Sigma pour la sommation dans le calcul du Wilder's MA.
**TRADEX-AI C1** : Confirmation formelle — la Wilders Moving Average dans l'ADX Sierra Chart utilise une sommation récursive (Wilder's smoothing). En Python TRADEX : ADX_t = ((ADX_{t-1} * (n-1)) + DX_t) / n, avec DX = 100 * |DI+ - DI-| / (DI+ + DI-). Cette formule récursive doit être initialisée sur n_DX + n_ADX premières barres.
*Catégorie : configuration*

### D8944 — ADX Sierra Chart : DX initialisé à zéro — comportement au démarrage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : "The Directional Index at Index t is denoted as DX_t(n_DX). This is initially equal to zero, and we compute it for t >= 0."
**TRADEX-AI C1** : Comportement de démarrage documenté — l'ADX Sierra Chart démarre avec DX = 0, ce qui produit des valeurs ADX artificiellement basses au début du chart. Règle TRADEX : valider que l'ADX a bien convergé (> 50 barres disponibles) avant d'utiliser sa valeur dans la grille de scoring.
*Catégorie : configuration*

### D8945 — ADX Sierra Chart : comportement sur marché range (ADX plat bas)
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : Un ADX qui reste bas (<20) pendant une longue période indique un marché en consolidation. Dans ces conditions, l'ADX peut rester plat sans signal clair de tendance émergente.
**TRADEX-AI C1** : Règle opérationnelle TRADEX pour Mode Auto — si ADX est resté sous 20 pendant plus de 10 barres consécutives sur GC ou CL, activer un "range mode filter" qui désactive les signaux directionnels Belkhayate et bascule vers une stratégie de rebond sur pivots plutôt que de suivi de tendance.
*Catégorie : gestion_risque_entree*

### D8946 — ADX Sierra Chart : pics ADX — signal de retournement potentiel
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : Un ADX qui monte fortement puis commence à baisser depuis un niveau élevé (>40-50) peut signaler un épuisement de tendance et un potentiel retournement — non documenté dans la page Sierra Chart mais implication de la formule Wilders.
**TRADEX-AI C1** : Garde-fou TRADEX — quand ADX dépasse 45 puis commence à décliner, réduire le score de confiance du signal Belkhayate de 10%. Un ADX en pic élevé + déclin = tendance mature possiblement proche d'un retournement. Appliquer à GC, CL, ZW.
*Catégorie : gestion_position_active*

### D8947 — ADX Sierra Chart : comparaison ADX Sierra vs calcul Python — validation obligatoire
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : La formule ADX Sierra Chart (DX Length + DX Mov Avg Length en Wilders MA) doit être reproduite identiquement en Python pour que les valeurs TRADEX correspondent à celles affichées sur le chart Sierra Chart de référence.
**TRADEX-AI C1** : Procédure de validation TRADEX Phase C — avant de déployer l'ADX Python dans le moteur, vérifier que la valeur ADX Python == valeur ADX Sierra Chart sur les mêmes barres GC (tolérance < 0.01). Utiliser la spreadsheet ADX.13.scss comme reference de vérification croisée.
*Catégorie : configuration*

### D8948 — ADX Sierra Chart : paramètres combinés DX Length 14 / DX Mov Avg Length 14 — configuration canonique Welles Wilder
🟢 **FAIT VÉRIFIÉ** (Source : sierra_13_adx.md) : Les deux paramètres configurables de l'ADX ID 13 sont : DX Length (n_DX) et DX Mov Avg Length (n_ADX). La configuration standard de l'auteur Welles Wilder (dans "New Concepts in Technical Trading Systems", 1978) est 14/14.
**TRADEX-AI C1** : Paramètres VERROUILLÉS pour TRADEX — ADX : DX Length = 14, DX Mov Avg Length = 14 (configuration Welles Wilder originale). Ces valeurs sont cohérentes avec la méthode Belkhayate qui s'appuie sur les indicateurs classiques de Wilder. Ne pas modifier sans décision documentée en CLAUDE.md.
*Catégorie : configuration*

### D8949 — ADX Sierra Chart : étude applicable sur futures CME — GC, HG, CL, ZW
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : L'ADX étant un indicateur universel basé uniquement sur High/Low/Close, il est directement applicable à tous les contrats futures CME sans adaptation.
**TRADEX-AI C1** : Applicabilité confirmée pour tous les actifs TRADEX — ADX ID 13 compatible avec GC (CME), HG (CME), CL (NYMEX), ZW (CBOT) via Sierra Chart / Rithmic. L'ADX est aussi pertinent pour les actifs de confirmation DX, ES, VX — lecture de la force de tendance macro (C4).
*Catégorie : indicateurs_tendance*

### D8950 — ADX Sierra Chart : intégration dans la grille de scoring TRADEX /10 — proposition
🟡 **SYNTHÈSE** (Source : sierra_13_adx.md) : L'ADX mesure la force de tendance. Sa valeur (< 20 / 20-25 / 25-40 / > 40) peut être directement mappée sur un critère de la grille de scoring /10 Belkhayate — le "cercle C1 — Prix" inclut la confirmation de tendance comme composante.
**TRADEX-AI C1** : Proposition d'intégration grille /10 TRADEX — Critère "Force tendance ADX" : ADX < 20 = 0 pt · ADX 20-25 = 0.5 pt · ADX 25-40 = 1 pt · ADX > 40 = 0.75 pt (décroissance pour tendance mature). Ce critère s'ajoute aux autres composantes C1 (BGC, Direction Belkhayate, Pivots) dans la grille. A valider avec Abdelkrim lors de la décision de scoring final.
*Catégorie : configuration*
