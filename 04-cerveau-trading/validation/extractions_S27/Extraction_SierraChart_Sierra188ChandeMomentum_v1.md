# Extraction SierraChart — Chande Momentum Oscillator
**Source :** `bundles/sierrachart/sierra_188_chande_momentum.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9031 → D9040 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=188
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : indicateur momentum oscillant [-100,+100] utilisable pour confirmer l'élan directionnel sur GC/CL/HG/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9031 — Chande Momentum Oscillator : définition et rôle
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : Le CMO (Chande Momentum Oscillator) calcule et affiche un oscillateur de momentum basé sur la somme des hausses nettes moins la somme des baisses nettes, divisée par leur total, sur une fenêtre glissante de longueur `CMO Length`. Le résultat est un oscillateur borné compris entre -100 et +100.
**TRADEX-AI C1** : Cet oscillateur peut être ajouté dans Sierra Chart sur les actifs GC, HG, CL, ZW pour mesurer l'intensité directionnelle du momentum prix sur la période configurée.
*Catégorie : indicateurs_momentum*

### D9032 — Input Data : choix de la donnée source
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : L'input `Input Data` détermine quelle valeur OHLCV est utilisée comme source de calcul (Close, Open, High, Low, HL/2, HLC/3, etc.). Il s'agit d'un paramètre configurable dans Sierra Chart.
**TRADEX-AI C1** : Pour TRADEX-AI, l'input standard est `Close`. Modifier vers `HL/2` peut lisser l'oscillateur sur les actifs volatils comme CL ou GC.
*Catégorie : indicateurs_momentum*

### D9033 — CMO Length : paramètre de fenêtre de calcul
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : L'input `CMO Length` fixe le nombre de barres sur lesquelles sont accumulées les hausses et baisses nettes. Le CMO est calculé à partir de l'index `t ≥ n_CMO`. Plus la longueur est courte, plus l'oscillateur est sensible aux mouvements récents ; plus elle est longue, plus il est lissé.
**TRADEX-AI C1** : Paramètre directement réglable dans TRADEX-AI. Une longueur courte (9-14) convient pour détecter des retournements rapides sur GC/CL ; une longueur longue (20-30) filtre le bruit sur ZW/HG.
*Catégorie : indicateurs_momentum*

### D9034 — Lignes horizontales configurables (Line 1, Line 2, Line 3)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : La study affiche trois lignes horizontales dont les niveaux sont entièrement définis par les inputs `Line 1`, `Line 2`, `Line 3`. Ces lignes servent à délimiter des zones de surachat/survente ou des seuils de signal personnalisés.
**TRADEX-AI C1** : Configurer Line 1 = +50, Line 2 = 0, Line 3 = -50 pour identifier les zones de momentum fort (au-dessus de +50 = tendance haussière forte, en dessous de -50 = tendance baissière forte, autour de 0 = neutralité).
*Catégorie : indicateurs_momentum*

### D9035 — Formule CMO : Up Change et Down Change
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : Le CMO est calculé via deux composantes : U(X) = hausse nette à l'index t (= X_t - X_{t-1} si positif, sinon 0) et D(X) = baisse nette (= X_{t-1} - X_t si négatif, sinon 0). La valeur finale est `CMO = 100 × (ΣU - ΣD) / (ΣU + ΣD)` sur la fenêtre de longueur n_CMO.
**TRADEX-AI C1** : Contrairement au RSI qui normalise par séparation hausses/baisses indépendantes, le CMO utilise leur rapport combiné — il est donc plus sensible aux retournements abrupts, utile pour GC (Or) en régime de tendance forte.
*Catégorie : indicateurs_momentum*

### D9036 — CMO vs RSI : différence comportementale
🟡 **SYNTHÈSE** (Source : sierra_188_chande_momentum.md) : Le CMO est calculé différemment du RSI de Wilder : le RSI lisse séparément les gains et pertes avec une EMA Wilder, alors que le CMO utilise des sommes mobiles simples (Moving Summation) sur la même fenêtre. Le CMO est donc plus volatil et réactif que le RSI pour une même longueur.
**TRADEX-AI C1** : Sur TRADEX-AI, le CMO peut compléter le RSI pour la confirmation C1 : si CMO et RSI pointent dans la même direction, le signal de momentum est renforcé sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

### D9037 — Disponibilité formule spreadsheet Sierra Chart
🔵 **ÉCOLE** (Source : sierra_188_chande_momentum.md) : Sierra Chart fournit un fichier spreadsheet `Chande_Momentum_Oscillator.188.scss` contenant les formules détaillées, accessible via `File >> Open Spreadsheet` dans l'interface Sierra Chart.
**TRADEX-AI C1** : Non directement applicable à TRADEX-AI (fichier Sierra Chart natif), mais utile pour auditer la formule si un écart est constaté entre le CMO calculé en Python et celui affiché dans Sierra Chart.
*Catégorie : indicateurs_momentum*

### D9038 — Pertinence CMO pour confirmation de signal TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_188_chande_momentum.md) : Le CMO oscillant entre -100 et +100 avec des seuils configurables (Line 1/2/3) est adapté à une utilisation dans la grille de scoring /10 de TRADEX-AI comme indicateur de momentum confirmatoire.
**TRADEX-AI C1** : Règle d'usage proposée : CMO > +30 = point pour signal haussier en C1 ; CMO < -30 = point pour signal baissier ; CMO entre -30 et +30 = neutre, pas de point momentum.
*Catégorie : indicateurs_momentum*

### D9039 — Calcul valide à partir de t ≥ n_CMO
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : Le CMO n'est valide et calculable qu'à partir de l'index `t ≥ n_CMO` (nombre de barres suffisant pour remplir la fenêtre de calcul). Les premières barres n'ont pas de valeur CMO.
**TRADEX-AI C1** : Lors de l'initialisation du moteur Python, vérifier que le nombre de barres disponibles dans le JSON NT8 est supérieur à `CMO_LENGTH` avant de calculer l'oscillateur, sinon retourner `None` pour éviter un signal incorrect.
*Catégorie : indicateurs_momentum*

### D9040 — Moving Summation comme base de calcul (pas d'EMA)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_188_chande_momentum.md) : Les sommes cumulées ΣU et ΣD sont calculées par Moving Summation (somme simple sur la fenêtre glissante), pas par lissage exponentiel. C'est la distinction fondamentale du CMO par rapport aux oscillateurs basés sur EMA.
**TRADEX-AI C1** : En Python, implémenter via `sum(up_changes[-n:])` et `sum(down_changes[-n:])` sur les dernières n barres, où n = CMO_LENGTH.
*Catégorie : indicateurs_momentum*
