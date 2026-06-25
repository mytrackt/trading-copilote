# Extraction SierraChart — Price Momentum Oscillator
**Source :** `bundles/sierrachart/sierra_435_pmo.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9351 → D9360 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=435
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : PMO = oscillateur momentum double-lissage utilisable comme filtre tendance sur GC/HG/CL/ZW pour confirmer direction avant signal.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9351 — Définition PMO : oscillateur momentum à double lissage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : Le Price Momentum Oscillator (PMO) calcule d'abord un Rate of Change (ROC), puis applique une Custom Smoothing Function (CSF) deux fois successivement : une première fois sur le ROC (longueur n1), une deuxième fois sur le résultat (longueur n2). Le résultat final est la PMO Line.
**TRADEX-AI C1** : Le PMO est un indicateur momentum basé sur le prix pur — applicable sur GC, HG, CL, ZW pour mesurer la force directionnelle de la bougie en cours.
*Catégorie : indicateurs_momentum*

### D9352 — Paramètre PMO Line Length 1 (n1) : premier lissage du ROC
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : L'input `PMO Line Length 1` (noté n1) contrôle la longueur du premier passage de la Custom Smoothing Function appliqué au ROC. C'est le paramètre qui détermine la réactivité initiale de l'oscillateur.
**TRADEX-AI C1** : Sur range bars NT8, n1 doit être calibré selon la granularité du range choisi — une valeur faible rend le PMO plus réactif mais plus bruité, une valeur élevée le lisse davantage. À tester lors de la Phase C de validation.
*Catégorie : indicateurs_momentum*

### D9353 — Paramètre PMO Line Length 2 (n2) : deuxième lissage
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : L'input `PMO Line Length 2` (noté n2) contrôle la longueur du second passage de la Custom Smoothing Function appliqué sur le ROC déjà lissé. Ce double lissage réduit le bruit par rapport à un ROC simple.
**TRADEX-AI C1** : Le double lissage rend le PMO plus stable qu'un ROC brut, ce qui est avantageux pour éviter de faux signaux sur des marchés volatils comme CL (pétrole) ou GC (or).
*Catégorie : indicateurs_momentum*

### D9354 — Paramètre Signal Line : moyenne mobile sur la PMO Line
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : L'input `PMO Signal Line Length` (noté n_Sig) contrôle la longueur de la Signal Line, calculée par défaut comme une Exponential Moving Average (EMA) de la PMO Line. Le croisement PMO/Signal est l'événement principal d'usage.
**TRADEX-AI C1** : Le croisement PMO Line > Signal Line = momentum haussier naissant. Le croisement PMO Line < Signal Line = momentum baissier naissant. Ce signal de croisement peut servir de confirmation de direction (Cercle C1) avant d'envoyer un signal au moteur Claude.
*Catégorie : indicateurs_momentum*

### D9355 — Paramètre Signal Line MA Type : 7 types possibles
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : Le type de moyenne mobile de la Signal Line est configurable via l'input `PMO Signal Line Moving Average Type`. Les 7 types disponibles sont : EMA (défaut), Linear Regression MA, Simple MA, Weighted MA, Wilders MA, Simple MA Skip Zeros, Smoothed MA.
**TRADEX-AI C1** : La Wilders MA ou la Smoothed MA peuvent être préférées pour la Signal Line sur les marchés à forte volatilité (CL) car elles réagissent moins aux pics isolés que l'EMA.
*Catégorie : indicateurs_momentum*

### D9356 — Input Data : champ d'application de l'oscillateur
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : L'input `Input Data` détermine sur quelle donnée de prix le PMO est calculé (Close par défaut, mais configurable sur Open, High, Low, Volume, etc.).
**TRADEX-AI C1** : Pour TRADEX-AI, l'application sur le Close (prix de clôture de chaque range bar) est cohérente avec la méthode Belkhayate qui travaille sur les prix de clôture pour évaluer la force directionnelle.
*Catégorie : indicateurs_momentum*

### D9357 — Formule CSF : lissage propriétaire non-EMA standard
🟡 **SYNTHÈSE** (Source : sierra_435_pmo.md) : La Custom Smoothing Function (CSF) utilisée dans le PMO n'est pas une EMA standard. Elle applique un facteur de pondération de 1/100 * (2/n) selon la documentation Sierra Chart — cela la rend plus lisse qu'une EMA pure pour un même paramètre n.
**TRADEX-AI C1** : La CSF rend le PMO moins susceptible de donner de faux signaux de croisement que des oscillateurs basés sur EMA standard. Avantage pour le filtre signal TRADEX-AI (moins de faux positifs au Niveau 1).
*Catégorie : indicateurs_momentum*

### D9358 — Signal de divergence PMO/prix
🟡 **SYNTHÈSE** (Source : sierra_435_pmo.md) : Bien que non mentionné explicitement dans la page Sierra Chart, un PMO en hausse alors que le prix est en baisse constitue une divergence haussière classique — usage académique standard des oscillateurs momentum.
**TRADEX-AI C1** : Les divergences PMO/prix sur GC (or) constituent un signal d'alerte C1 exploitable — si le prix fait un nouveau bas mais que le PMO ne confirme pas, cela renforce une analyse de retournement Belkhayate.
*Catégorie : indicateurs_momentum*

### D9359 — Absence de niveau de surachat/survente natif
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : Contrairement au RSI ou au Stochastique, la page Sierra Chart ne définit aucun niveau fixe de surachat/survente pour le PMO. L'oscillateur n'a pas de borne 0-100 — il peut prendre n'importe quelle valeur positive ou négative.
**TRADEX-AI C1** : Le PMO ne fournit pas de signal d'entrée autonome par niveau — il doit être utilisé en combinaison avec d'autres indicateurs (ex. croisement de la Signal Line ou position par rapport à zéro). À intégrer uniquement comme confirmation dans la grille /10 de TRADEX-AI.
*Catégorie : indicateurs_momentum*

### D9360 — Spreadsheet disponible pour validation indépendante
🟢 **FAIT VÉRIFIÉ** (Source : sierra_435_pmo.md) : Sierra Chart fournit un fichier spreadsheet `Price_Momentum_Oscillator.435.scss` permettant de recalculer manuellement toutes les valeurs du PMO. Dernière modification : 24 janvier 2025.
**TRADEX-AI C1** : Ce fichier spreadsheet peut être utilisé pour valider les valeurs calculées par tout indicateur externe (ex. TradingView PMO) avant de les intégrer dans les données NT8 envoyées au moteur TRADEX-AI. Source de validation indépendante fiable.
*Catégorie : indicateurs_momentum*
