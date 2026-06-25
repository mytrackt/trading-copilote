# Extraction SierraChart — RSI (Relative Strength Index)
**Source :** `bundles/sierrachart/sierra_38_rsi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9291 → D9310 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=38
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : RSI Welles Wilder avec MA intégrée — indicateur momentum C1/C5 applicable sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9291 — Formule RSI Welles Wilder (calcul par SMA)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Le RSI Sierra Chart implémente la méthode Welles Wilder originale. RSI_t(X, n_RSI) est calculé à partir des moyennes mobiles des hausses (U_t) et des baisses (D_t) de l'Input Data. La formule utilise par défaut une Simple Moving Average pour les deux composantes, mais peut être substituée par d'autres types (voir D9295). Le RSI est défini pour t >= n_RSI + n (période de chauffe requise).
**TRADEX-AI C1** : Le RSI standard Wilder est un des indicateurs momentum de référence Belkhayate. Paramètre n_RSI = 14 (standard) recommandé pour initialisation dans settings.py — applicable sur barres range NT8 GC/CL.
*Catégorie : indicateurs_momentum*

### D9292 — Moving Average du RSI (lissage secondaire)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Sierra Chart calcule en plus une Moving Average du RSI avec une longueur RSI Moving Average Length n distincte du RSI Length n_RSI. Cette MA lissée (RSI_bar) est calculée pour t >= n_RSI + n. Les deux courbes sont affichées simultanément avec deux lignes horizontales configurables (Line1 Value, Line2 Value).
**TRADEX-AI C1** : Le signal croisement RSI / MA-RSI constitue un filtre de momentum secondaire. Dans TRADEX-AI, le croisement RSI > MA-RSI peut renforcer un signal haussier sur GC/HG — à intégrer comme condition additionnelle dans claude_brain.py (cercle C1).
*Catégorie : indicateurs_momentum*

### D9293 — Inputs configurables : RSI Length et RSI MA Length
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Paramètres clés : (1) RSI Length n_RSI — longueur de calcul du RSI. (2) RSI Moving Average Length n — longueur de la MA appliquée au RSI. (3) Input Data — source de données (Close par défaut). Ces trois paramètres sont indépendants et configurables séparément.
**TRADEX-AI C1** : Dans settings.py TRADEX-AI, prévoir RSI_LENGTH = 14 (standard Wilder) et RSI_MA_LENGTH = 9 (signal line courte). Valeurs ajustables par actif : GC peut nécessiter RSI_LENGTH = 21 sur barres range pour réduire le bruit.
*Catégorie : indicateurs_momentum*

### D9294 — Lignes horizontales de référence (Line1 et Line2)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Le RSI Sierra Chart affiche deux lignes horizontales configurables via Line1 Value et Line2 Value. Valeurs standards : 70 (suracheté) et 30 (survendu). Ces seuils sont des inputs directs modifiables par l'utilisateur.
**TRADEX-AI C1/C5** : Les zones 70/30 sont les niveaux de référence Belkhayate pour le momentum RSI. Dans TRADEX-AI : RSI > 70 → pression vendeuse à surveiller sur GC/CL ; RSI < 30 → signal acheteur potentiel. Intégrer comme conditions dans le prompt claude_brain.py (grille /10, cercle C1 et C5).
*Catégorie : indicateurs_momentum*

### D9295 — Types de moyennes mobiles supportés (Average Type)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : L'Input Average Type contrôle le type de MA utilisé DANS le calcul du RSI ET pour la MA du RSI simultanément. Types disponibles : Simple Moving Average (SMA), Exponential Moving Average (EMA), Linear Regression Moving Average, Weighted Moving Average, Wilders Moving Average, Simple Moving Average Skip Zeros, Smoothed Moving Average. Un seul paramètre détermine les trois MA internes.
**TRADEX-AI C1** : Pour TRADEX-AI, conserver Wilders Moving Average (type natif Welles Wilder) pour maximiser la fidélité à la méthode originale. L'EMA peut être utilisée comme variante plus réactive sur CL (pétrole, volatilité élevée).
*Catégorie : indicateurs_momentum*

### D9296 — Mode RSI - 50 (centrage sur zéro)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Si l'Input Use RSI - 50 est activé (Yes), la valeur 50 est soustraite du RSI, de la MA du RSI, de Line1 Value et de Line2 Value. Le RSI oscille alors autour de 0 au lieu de 50. Ce mode modifie l'affichage des quatre sous-graphiques simultanément.
**TRADEX-AI C1** : Mode RSI-50 non recommandé pour TRADEX-AI — la méthode Belkhayate utilise les niveaux 30/50/70 en référence absolue. Maintenir Use RSI - 50 = No dans la configuration standard. Documenter dans settings.py comme constante immuable.
*Catégorie : indicateurs_momentum*

### D9297 — Période de chauffe requise (warm-up)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Le RSI est calculé pour t >= n_RSI + n (période minimale = RSI Length + MA Length barres). Pour les calculs internes de l'EMA/Wilder, Sierra Chart utilise des valeurs intermédiaires non retournées en output pour t entre n_RSI-1 et n_RSI+n. Ces valeurs de chauffe sont calculées en interne mais non exposées.
**TRADEX-AI C1** : Avec RSI_LENGTH=14 et RSI_MA_LENGTH=9, la période de chauffe = 23 barres minimum. Dans staleness_monitor.py, valider qu'au moins 25 barres sont disponibles avant de calculer le RSI. En dessous de ce seuil → signal RSI = INDISPONIBLE (pas de signal émis).
*Catégorie : indicateurs_momentum*

### D9298 — Disponibilité spreadsheet (.scss)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_38_rsi.md) : Un fichier spreadsheet Sierra Chart est disponible : RSI.38.scss. Il contient les formules complètes du RSI en format tableur Sierra Chart, importable via File >> Open Spreadsheet.
**TRADEX-AI C1** : Le fichier .scss permet une vérification indépendante des formules RSI hors plateforme. Utile pour valider les calculs Python dans engine/correlations.py avant intégration en production.
*Catégorie : indicateurs_momentum*
