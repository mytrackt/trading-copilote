# Extraction SierraChart — TPO Value Area Lines
**Source :** `bundles/sierrachart/sierra_158_tpo_value_area_lines.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8971 → D8990 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=158
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : TPO Value Area Lines (VAH/VAL/POC) — niveaux Market Profile critiques pour définir zones d'acceptation/rejet des prix, utilisables comme support/résistance dynamiques pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D8971 — Définition TPO Value Area Lines : VAH / VAL / POC
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Le study TPO Value Area Lines affiche trois niveaux par période : Value Area High (VAH), Value Area Low (VAL), et Point of Control (POC). Ces niveaux sont calculés à partir des blocs TPO (Time Price Opportunity) pour chaque période de temps définie.
**TRADEX-AI C2** : VAH/VAL/POC sont des niveaux clés de Market Profile — sur GC (Or), le POC représente le prix "fair value" institutionnel de la séance. Un rejet du POC avec delta négatif (ATAS) = signal SHORT.
*Catégorie : structure_marche*

### D8972 — Définition TPO : bloc temporel à un prix
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Un TPO représente le trading à un prix ou plage de prix particulier pour une période de temps continue spécifique. La plage de prix est définie par le paramètre "Price Increment In Ticks". La durée de chaque TPO est définie par "TPO Letter Time Length in Minutes".
**TRADEX-AI C2** : La granularité du TPO (durée et taille tick) détermine la précision des niveaux VAH/VAL/POC — sur futures (GC taille tick 0.10$), utiliser Price Increment In Ticks=1 pour une précision maximale.
*Catégorie : structure_marche*

### D8973 — Restriction : usage sur graphique standard uniquement
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Le study TPO Value Area Lines NE PEUT PAS être utilisé sur un TPO Profile Chart — les calculs seraient inexacts. Il est conçu exclusivement pour les graphiques standard (barres ou bougies).
**TRADEX-AI C2** : Dans TRADEX-AI, les niveaux TPO VAH/VAL/POC doivent être lus depuis un graphique standard Sierra Chart (ou l'équivalent ATAS), PAS depuis un TPO Profile Chart dédié.
*Catégorie : structure_marche*

### D8974 — Paramètre TPO Value Area % (défaut 70%)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Le paramètre "TPO Value Area %" spécifie le pourcentage autour du Point of Control que la Value Area couvre. La valeur par défaut est 70%. Cette valeur correspond à la convention Market Profile standard de Steidlmayer.
**TRADEX-AI C2** : Fixer à 70% (valeur standard institutionnelle). La Value Area à 70% représente la zone où ~70% du volume/temps a été tradé — zone de "fair value". Breakout hors VA = signal directionnel.
*Catégorie : structure_marche*

### D8975 — Paramètre Time Period Type et Time Period Length
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : La période de calcul des Value Area Lines est définie par la combinaison de "Time Period Type" (Minutes, Hours, Days, Weeks, Months, Years) et "Time Period Length" (quantité). Exemple : Type=Days, Length=1 = calcul journalier.
**TRADEX-AI C2** : Pour TRADEX-AI, utiliser Time Period Type=Days, Length=1 pour les niveaux journaliers (VAH/VAL/POC de la séance précédente). Ces niveaux sont des références institutionnelles majeures pour GC/CL.
*Catégorie : structure_marche*

### D8976 — Paramètre TPO Letter Time Length in Minutes (défaut 30min)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Ce paramètre définit la durée de chaque bloc TPO utilisé pour calculer les Value Area Lines. La valeur par défaut est 30 minutes. La période de la barre du graphique doit diviser de façon entière cette valeur et être ≤ à cette valeur.
**TRADEX-AI C2** : Sur graphique intraday NT8 (ex : barres 5min), TPO Letter Time Length=30min est valide (30÷5=6 entier). Pour des barres range, adapter selon la durée moyenne par barre estimée.
*Catégorie : structure_marche*

### D8977 — Paramètre Draw Developing Value Area Lines
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Quand ce paramètre est "Yes", les niveaux VAH/VAL/POC à chaque barre représentent la Value Area depuis le début de la période jusqu'à cette barre (développement en temps réel). Quand "No", les niveaux sont fixes pour toute la période.
**TRADEX-AI C2** : Pour TRADEX-AI en mode temps réel : Draw Developing = Yes pour suivre l'évolution intraday de la VA. Pour référencer la session précédente : Reference n Periods Back = 1 avec Draw Developing = No.
*Catégorie : structure_marche*

### D8978 — Paramètre Reference n Periods Back
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Ce paramètre (actif uniquement si Draw Developing = No) définit combien de périodes en arrière les Value Area Lines font référence. 0 = période courante, 1 = période précédente, 2 = deux périodes en arrière.
**TRADEX-AI C2** : Réglage recommandé pour TRADEX-AI : Reference n Periods Back = 1 → afficher les niveaux de la SESSION PRÉCÉDENTE comme support/résistance de référence. Niveaux les plus pertinents pour les institutionnels.
*Catégorie : structure_marche*

### D8979 — Paramètre Price Increment In Ticks
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Ce paramètre définit le regroupement des prix pour les calculs TPO. La valeur 1 représente le tick size du symbole. Valeur plus haute = granularité plus large. Exemple pour un actif à tick=0.25 avec Price Increment=4 : niveaux groupés par 1.0 point.
**TRADEX-AI C2** : Pour GC (Or, tick=0.10$) : Price Increment In Ticks=1 = résolution 0.10$. Pour CL (pétrole, tick=0.01$) : envisager Price Increment=5 (=0.05$) pour réduire le bruit et obtenir des niveaux plus "institutionnels".
*Catégorie : structure_marche*

### D8980 — Importance du paramètre Tick Size dans Chart Settings
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : La documentation Sierra Chart précise qu'il est ESSENTIEL que le "Tick Size" dans Chart >> Chart Settings soit correctement configuré pour que les calculs TPO soient exacts. Une erreur de tick size produira des niveaux VAH/VAL/POC incorrects.
**TRADEX-AI C2** : Vérification impérative lors de la Phase C : confirmer le tick size exact de chaque actif (GC=0.10$, HG=0.0005$, CL=0.01$, ZW=0.25¢) dans les paramètres Sierra Chart ou NT8.
*Catégorie : gestion_risque_entree*

### D8981 — Paramètre Automatically Correct Invalid Time Period
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Quand ce paramètre est "Yes", si la période du graphique passe en Daily ou supérieur, le Time Period Type est automatiquement remplacé par Months/1. Quand "No", pas de correction automatique.
**TRADEX-AI C1** : Mettre ce paramètre à "No" dans TRADEX-AI pour conserver un contrôle explicite des périodes. Les changements automatiques cachés de paramètres sont un risque de cohérence dans un système de trading automatisé.
*Catégorie : gestion_risque_entree*

### D8982 — Calcul Value Area : méthode Count 2 Levels at a Time
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Quand le paramètre "Count 2 Levels at a Time for Value Area" est "Yes", le calcul de la Value Area utilise un niveau sur deux (tous les deux niveaux) plutôt que chaque niveau consécutif. Ce comportement correspond à la méthode CME Group originale de calcul Market Profile.
**TRADEX-AI C2** : Pour une cohérence avec les niveaux CME institutionnels sur GC (Or CME) et CL (pétrole CME), activer Count 2 Levels = Yes pour aligner les VAH/VAL/POC avec les références institutionnelles.
*Catégorie : structure_marche*

### D8983 — Session Day vs Evening Session
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Deux paramètres gèrent la session de nuit : "New Period At Day Session Start" (crée des niveaux séparés pour session de nuit et session de jour) et "Base on Day Session Only" (ignore complètement la session de nuit dans les calculs).
**TRADEX-AI C2** : Pour GC (Or CME, session électronique 23h/jour) : utiliser Base on Day Session Only = No pour capturer l'activité asiatique. Pour ES (S&P500, confirmation) : séparation Day/Evening peut révéler le contexte overnight.
*Catégorie : structure_marche*

### D8984 — Calcul basé sur nombre de barres spécifique
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Pour baser les Value Area Lines sur N barres spécifiques : multiplier N barres × timeframe par barre. Exemple : 12 barres × 5min = 60 minutes → Time Period Type=Minutes, Length=60.
**TRADEX-AI C2** : Sur NT8 avec range bars (durée variable par barre), cette méthode n'est pas directement applicable. Préférer Time Period Type=Days ou Hours pour une référence temporelle stable indépendante du nombre de barres.
*Catégorie : structure_marche*

### D8985 — Interprétation opérationnelle : POC comme niveau d'équilibre
🔵 **ÉCOLE** (Source : sierra_158_tpo_value_area_lines.md) : Le Point of Control (POC) représente le niveau de prix où le plus de temps (ou TPO) a été tradé pendant la période. Il constitue le niveau de "fair value" ou d'équilibre de la session — les prix ont tendance à y revenir en l'absence de catalyseur directionnel.
**TRADEX-AI C2** : TRADEX-AI doit intégrer le POC comme niveau clé de C2 (structure de marché) : prix au-dessus POC = contexte haussier, en dessous = contexte baissier. Pondération dans le score /10 selon la distance au POC.
*Catégorie : structure_marche*

### D8986 — Interprétation opérationnelle : breakout de la Value Area
🔵 **ÉCOLE** (Source : sierra_158_tpo_value_area_lines.md) : Un breakout au-dessus de la VAH ou en dessous de la VAL signifie que le prix sort de la zone d'acceptation. Si le prix reste hors de la Value Area (règle des 80% : si 2 TPO consécutifs restent hors VA), la tendance est validée.
**TRADEX-AI C2** : Intégrer la règle "2 closes consécutifs hors VA" comme critère de confirmation de tendance dans le moteur de signal TRADEX-AI. Breakout VAH + Belkhayate Direction haussière = signal fort C1+C2 alignés.
*Catégorie : configuration*

### D8987 — Paramètre One Period Only at End of Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Quand ce paramètre est "Yes", un seul ensemble de lignes VAH/VAL/POC est affiché pour la période spécifiée à la fin du graphique. Les weekend days ne sont pas pris en compte pour ce mode.
**TRADEX-AI C2** : Mode utile pour l'affichage dashboard TRADEX-AI : afficher uniquement les niveaux VA de la séance en cours (One Period Only = Yes) comme overlay sur le graphique temps réel, sans surcharger l'écran de lignes historiques.
*Catégorie : structure_marche*

### D8988 — Corrélation TPO VA Lines avec méthode Belkhayate
🟡 **SYNTHÈSE** (Source : sierra_158_tpo_value_area_lines.md) : Les niveaux TPO (VAH/VAL/POC) et les pivots Belkhayate (points de pivot hebdomadaires/mensuels) sont deux systèmes de niveaux de référence complémentaires. La méthode Belkhayate identifie les pivots mathématiques ; le Market Profile identifie les zones d'acceptation/rejet basées sur le temps passé aux prix.
**TRADEX-AI C1+C2** : Quand un pivot Belkhayate coïncide avec un niveau TPO (VAH/POC/VAL), la confluence crée un niveau de haute conviction. Dans le score /10, attribuer un bonus de confluence C1+C2 à ces zones.
*Catégorie : configuration*

### D8989 — Contrainte technique : chart bars doit diviser TPO Letter Time Length
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : La période de chaque barre du graphique doit diviser de façon entière le "TPO Letter Time Length in Minutes" ET être inférieure ou égale à cette valeur. Sinon, les calculs de Value Area sont incorrects (voir documentation "Incorrect Value Area or Point of Control Values").
**TRADEX-AI C2** : Contrainte technique critique pour l'intégration TRADEX-AI : vérifier la compatibilité timeframe barre / TPO time length avant déploiement Phase C. Documenter dans settings.py les combinaisons validées par actif.
*Catégorie : gestion_risque_entree*

### D8990 — Paramètre 30-Minute SubPeriod Handling (Start Time non multiple de 30)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_158_tpo_value_area_lines.md) : Trois options pour gérer les sous-périodes irrégulières quand le Start Time de la session n'est pas un multiple de 30 minutes : Standard (pas de gestion spéciale), Merge Odd SubPeriod with Next (fusion), Start New Subperiods at Even 30 Minute Time Blocks (sous-période courte initiale).
**TRADEX-AI C2** : Pour les futures US (ouverture à des heures non standards comme 17:00 CT = heure impaire), choisir "Start New Subperiods at Even 30 Minute Time Blocks" pour aligner les blocs TPO sur les heures rondes institutionnelles.
*Catégorie : structure_marche*
