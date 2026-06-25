# Extraction SierraChart — DMI & ADX & ADXR
**Source :** `bundles/sierrachart/sierra_197_dmi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9051 → D9065 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=197
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : étude combinée DMI+ADX+ADXR sur un seul panneau — mesure la force et la direction de tendance, directement applicable à la grille C1 de TRADEX-AI sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9051 — Étude combinée DMI+ADX+ADXR dans un seul Chart Region
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : La study Sierra Chart ID=197 calcule et affiche simultanément le Directional Movement Index (DMI = +DI et -DI), l'ADX, et l'ADXR dans la même région de graphique (Chart Region). Les trois indicateurs partagent les mêmes inputs Length et Mov Avg Length.
**TRADEX-AI C1** : Utilisation pratique : un seul panneau Sierra Chart suffit pour surveiller la direction (+DI/-DI) et la force (ADX/ADXR) de tendance sur GC, HG, CL, ZW.
*Catégorie : indicateurs_tendance*

### D9052 — Input Length : paramètre DX Length partagé par DMI/ADX/ADXR
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : L'input `Length` correspond au `DX Length` des studies individuelles DMI, ADX et ADXR. Il fixe la période de calcul du True Range et des Directional Movements (+DM, -DM) utilisés pour calculer +DI, -DI et DX.
**TRADEX-AI C1** : Valeur standard Wilder : Length = 14. Sur TRADEX-AI, utiliser Length=14 comme base pour GC/CL ; tester Length=10 pour HG (plus réactif sur marché cuivre industriel).
*Catégorie : indicateurs_tendance*

### D9053 — Input Mov Avg Length : paramètre DX Mov Avg Length pour ADX
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : L'input `Mov Avg Length` correspond au `DX Mov Avg Length` de la study ADX. Il détermine la longueur du lissage appliqué au DX brut pour obtenir l'ADX (Average Directional Index). La valeur standard Wilder est 14 (EMA Wilder).
**TRADEX-AI C1** : Mov Avg Length = 14 recommandé. Une valeur plus courte (ex. 10) produit un ADX plus réactif mais plus bruité — à éviter en mode Auto pour limiter les faux signaux.
*Catégorie : indicateurs_tendance*

### D9054 — Input ADXR Interval : intervalle de lissage de l'ADXR
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : L'input `ADXR Interval` est spécifique à l'ADXR (Average Directional Movement Rating). L'ADXR est la moyenne de l'ADX actuel et de l'ADX d'il y a `ADXR Interval` périodes. Il lisse davantage l'ADX pour réduire les oscillations.
**TRADEX-AI C1** : L'ADXR peut servir de signal de confirmation de la force de tendance : si ADXR > ADX = tendance qui accélère ; si ADXR < ADX = tendance qui décélère. Utile pour les filtres d'entrée C1 sur ZW/GC.
*Catégorie : indicateurs_tendance*

### D9055 — Relation Length/Mov Avg Length entre les trois studies
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : La study ID=197 garantit que Length et Mov Avg Length sont identiques pour DMI, ADX et ADXR. Cette cohérence interne est requise pour que les trois indicateurs soient comparables et affichés correctement dans le même panneau.
**TRADEX-AI C1** : Si TRADEX-AI calcule DMI et ADX séparément en Python, s'assurer d'utiliser la même valeur `n` pour les deux calculs, sinon les croisements +DI/-DI ne seront pas cohérents avec les niveaux ADX affichés.
*Catégorie : indicateurs_tendance*

### D9056 — DMI : +DI et -DI comme indicateurs directionnels
🔵 **ÉCOLE** (Source : sierra_197_dmi.md) : Le Directional Movement Index (DMI) se compose de deux lignes : +DI (Positive Directional Indicator) et -DI (Negative Directional Indicator). Le croisement de +DI au-dessus de -DI signale une tendance haussière ; le croisement inverse signale une tendance baissière.
**TRADEX-AI C1** : Règle de base pour TRADEX-AI : +DI > -DI = biais haussier C1 ; -DI > +DI = biais baissier C1. Combiné avec ADX > 25, le signal directionnel est renforcé.
*Catégorie : indicateurs_tendance*

### D9057 — ADX : mesure de la force de tendance (pas de direction)
🔵 **ÉCOLE** (Source : sierra_197_dmi.md) : L'ADX mesure la force (intensité) de la tendance indépendamment de sa direction. Un ADX croissant indique une tendance qui se renforce ; un ADX décroissant indique une tendance qui s'affaiblit ou un marché en range. L'ADX ne distingue pas hausse de baisse.
**TRADEX-AI C1** : Seuil opérationnel TRADEX-AI : ADX < 20 = marché sans tendance (ATTENDRE) ; ADX 20-25 = tendance faible ; ADX > 25 = tendance établie (signal recevable) ; ADX > 40 = tendance forte.
*Catégorie : indicateurs_tendance*

### D9058 — ADXR : version lissée de l'ADX pour confirmation
🔵 **ÉCOLE** (Source : sierra_197_dmi.md) : L'ADXR (Average Directional Movement Rating) est calculé comme la moyenne de l'ADX actuel et de l'ADX d'il y a `ADXR Interval` barres. Il offre une version plus lissée de l'ADX, moins sensible aux pics ponctuels.
**TRADEX-AI C1** : L'ADXR peut être utilisé dans la grille /10 comme confirmateur de tendance secondaire : si ADXR > 25 = confirmation de tendance pour +0,5 point dans le scoring C1.
*Catégorie : indicateurs_tendance*

### D9059 — Spreadsheets disponibles pour DMI, ADX et ADXR
🔵 **ÉCOLE** (Source : sierra_197_dmi.md) : Sierra Chart fournit trois fichiers spreadsheet distincts : `Directional_Movement_Index.24.scss`, `ADX.13.scss`, `ADXR.16.scss`. Un avertissement spécifique indique que les erreurs de pourcentage dans le spreadsheet DMI sont plus importantes que dans les autres études, car le DMI utilise un schéma d'arrondi différent.
**TRADEX-AI C1** : Implication technique : lors de la validation des calculs Python vs Sierra Chart, tolérer un écart légèrement plus grand (ex. ±0.5%) pour le DMI par rapport à ADX/ADXR, en raison de ce schéma d'arrondi différent.
*Catégorie : indicateurs_tendance*

### D9060 — Application pratique : ADX > 25 + croisement DI = signal valide
🟡 **SYNTHÈSE** (Source : sierra_197_dmi.md) : La combinaison standard DMI+ADX : signal haussier = +DI croise -DI à la hausse ET ADX > 25 ; signal baissier = -DI croise +DI à la hausse ET ADX > 25. Sans ADX > 25, les croisements DI sont souvent faux signaux en range.
**TRADEX-AI C1** : Règle de filtrage TRADEX-AI : tout croisement DMI se produisant avec ADX < 20 est rejeté comme signal C1. La condition ADX ≥ 25 est un pré-requis pour valider la direction DMI dans la grille /10.
*Catégorie : indicateurs_tendance*

### D9061 — Applicabilité sur futures GC/HG/CL/ZW
🟡 **SYNTHÈSE** (Source : sierra_197_dmi.md) : Le DMI+ADX+ADXR est indépendant de l'actif et applicable à tout instrument. Sur les futures CME/CBOT (GC, HG, CL, ZW), la période standard Length=14 barres sur range bars NT8 est compatible avec la configuration TRADEX-AI.
**TRADEX-AI C1** : Configurer Length=14 et Mov Avg Length=14 pour tous les actifs TRADEX-AI en première instance. Ajuster par actif uniquement après backtest Phase C sur range bars NT8.
*Catégorie : indicateurs_tendance*

### D9062 — Interopérabilité : ID=197 unifie trois studies individuelles (ID=24, 13, 16)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : La study ID=197 est une étude composite qui unifie les studies individuelles : Directional Movement Index (ID=24), ADX (ID=13), et ADXR (ID=16). Elle partage les mêmes inputs que ces studies séparées.
**TRADEX-AI C1** : Si Sierra Chart est utilisé comme source de données de référence, utiliser la study ID=197 pour avoir les trois métriques sur un seul panneau. En Python, implémenter les trois calculs dans un seul module `dmi_adx.py` pour cohérence.
*Catégorie : indicateurs_tendance*

### D9063 — ADXR Interval : valeur par défaut non spécifiée
⚫ **HYPOTHÈSE PROJET** (Source : sierra_197_dmi.md) : Le bundle ne précise pas la valeur par défaut de `ADXR Interval`. La valeur standard Wilder historique est 14 (identique à Length), mais Sierra Chart peut avoir une valeur différente.
**TRADEX-AI C1** : À vérifier dans Sierra Chart en ouvrant la study ID=197 et en lisant la valeur par défaut d'ADXR Interval avant d'implémenter en Python.
*Catégorie : indicateurs_tendance*

### D9064 — DMI/ADX dans la grille C1 de scoring /10
🟡 **SYNTHÈSE** (Source : sierra_197_dmi.md) : Le DMI/ADX est l'un des indicateurs de tendance les plus utilisés dans les systèmes de trading algorithmique. Sa présence dans Sierra Chart ID=197 confirme son statut d'outil standard pour mesurer la qualité de la tendance.
**TRADEX-AI C1** : Proposition d'intégration grille /10 : ADX ≥ 25 + DI aligné avec direction du signal = +1 point C1 ; ADX < 20 = -1 point ou blocage conditionnel selon configuration.
*Catégorie : indicateurs_tendance*

### D9065 — Précision calcul : schéma d'arrondi spécifique au DMI
🟢 **FAIT VÉRIFIÉ** (Source : sierra_197_dmi.md) : Sierra Chart documente explicitement que le spreadsheet DMI affiche des erreurs de pourcentage plus importantes que les autres études en raison d'un schéma d'arrondi différent (not further specified dans le bundle).
**TRADEX-AI C1** : Lors de tests de cohérence des calculs Python, définir une tolérance élargie pour les valeurs DMI : accepter un écart jusqu'à ±1% vs Sierra Chart, contre ±0.1% pour ADX/ADXR.
*Catégorie : indicateurs_tendance*
