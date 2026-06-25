# Extraction AdamGrimes — Catching The Wave: Ideas For Finding Trend Days
**Source :** `bundles/adamgrimes/catching_the_wave_ideas_for_finding_trend_days.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5411 → D5430 · **Page :** https://www.adamhgrimes.com/catching-the-wave-ideas-for-finding-trend-days/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : identification des jours de tendance forte sur futures GC/CL/HG/ZW — critères quantitatifs + subjectifs pour filtrer les journées d'accumulation vs. tendance.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

---

## DÉCISIONS

### D5411 — Les jours de tendance (trend days) sont rares et décisifs
🟢 **FAIT VÉRIFIÉ** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : La plupart des journées de marché voient davantage de va-et-vient (back and fill) que de continuation. Les jours de tendance réelle surviennent en moyenne environ une fois par mois. Beaucoup de traders réalisent leur profit mensuel entier sur un seul bon trend day.
**TRADEX-AI C1** : Sur GC/CL/HG/ZW, le moteur doit distinguer le mode "range / accumulation" (coût d'attente faible) du mode "trend day" (forte conviction directionnelle) — les deux nécessitent des stratégies d'entrée et de gestion radicalement différentes. Un signal TRADEX en mode range est potentiellement trompeur ; le filtre de contexte journalier est obligatoire.
*Catégorie : structure_marche*

---

### D5412 — La compression de volatilité prédit les jours de tendance
🟢 **FAIT VÉRIFIÉ** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : La compression de volatilité — mesurable de plusieurs façons — est un facteur qui fait pencher la balance en faveur d'un prochain jour de tendance. Les inside days (journée dont le range est contenu dans celui de la veille) sont un indicateur de compression de volatilité basse fréquence. Plusieurs inside days consécutifs (inside day d'inside day) renforcent cet edge.
**TRADEX-AI C1** : Sur GC ou CL, repérer 2+ inside days consécutifs sur le daily avant une session TRADEX augmente la probabilité d'un trend day. Intégrer ce signal dans le filtre pré-signal du moteur Python (Niveau 1) comme critère de contexte favorable.
*Catégorie : indicateurs_tendance*

---

### D5413 — Plusieurs clôtures consécutives dans la même direction préparent un snapback
🟢 **FAIT VÉRIFIÉ** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Plusieurs jours de clôtures consécutives dans la même direction peuvent générer un snapback qui lui-même peut devenir un fort trend day dans le sens opposé.
**TRADEX-AI C1** : Sur ZW ou HG, une série de 3+ clôtures haussières sans pullback significatif peut signaler un risque de snapback baissier — à intégrer dans la grille de score TRADEX comme facteur de prudence sur les signaux LONG dans ce contexte.
*Catégorie : structure_marche*

---

### D5414 — Les trend days peuvent survenir à l'intérieur d'une consolidation plus large
🟢 **FAIT VÉRIFIÉ** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Les jours de tendance peuvent apparaître même si le marché est globalement en range sur des timeframes supérieures. Un trader intraday ne doit pas écarter un marché en consolidation pour les setups de trend day.
**TRADEX-AI C1** : Sur GC ou CL en consolidation hebdomadaire, le moteur TRADEX ne doit pas filtrer tous les signaux — un breakdown/breakout journalier à l'intérieur du range reste exploitable si les conditions de score ≥ 7,0 sont remplies.
*Catégorie : structure_marche*

---

### D5415 — Les timeframes alternent tendance / range
🔵 **ÉCOLE** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Les timeframes basses tendent à alterner entre phases de tendance et phases de range. Un trend day est ainsi relativement peu probable le lendemain d'un autre trend day.
**TRADEX-AI C1** : Après une journée de forte tendance sur GC (ex. +2% directionnel), le filtre TRADEX doit abaisser la probabilité d'un nouveau trend day le lendemain — réduire le score de contexte journalier ou exiger un score ≥ 8,0 pour valider un signal.
*Catégorie : timing*

---

### D5416 — Les tight ranges d'après-midi préparent les tendances matinales du lendemain
🔵 **ÉCOLE** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Un range étroit en fin de journée (afternoon tight range) peut préparer une tendance forte en début de séance le lendemain matin (early morning trend).
**TRADEX-AI C1** : Sur CL ou GC, si la session de l'après-midi U.S. se termine avec un range ATR < 30% de la moyenne, alerter le moteur d'un probable setup de trend au prochain open — à combiner avec l'action du marché précoce (gaps, Europe).
*Catégorie : timing*

---

### D5417 — L'action matinale (première heure) est critique pour identifier un trend day
🟢 **FAIT VÉRIFIÉ** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Un bon trend day se manifeste généralement dans la première heure de trading. Le plan de la veille nécessite souvent des ajustements dès les premières minutes. Les éléments à surveiller en début de session : gap à l'ouverture, rétraction ou tenue du gap, comportement des marchés européens en fin de session, action des obligations, devises et or, et toute nouvelle surprise.
**TRADEX-AI C4** : Le filtre macro du moteur (Niveau 2) doit vérifier à l'ouverture U.S. : (1) gap GC/CL vs. clôture précédente, (2) direction Europe (DAX/CAC clôture), (3) mouvement DX (Dollar Index). Si ces 3 éléments sont alignés directionnellement dans la même direction, scorer +1 sur la grille /10.
*Catégorie : macro_evenements*

---

### D5418 — L'évaluation d'un trend day combine outils quantitatifs et jugement subjectif
🔵 **ÉCOLE** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : La prédiction des trend days repose sur une combinaison d'outils quantifiables (compression volatilité, inside days, direction multiple clôtures) et de facteurs subjectifs (environnement macro général, réactivité récente du marché aux nouvelles, événements catalyseurs prévus, action inter-marchés).
**TRADEX-AI C4/C7** : La grille de score /10 de TRADEX doit intégrer explicitement les deux dimensions : critères déterministes automatiques (C1 à C3) + facteurs contextuels (C4 macro, C7 corrélations inter-marchés) pour reproduire ce processus d'évaluation hybride.
*Catégorie : configuration*

---

### D5419 — Les positions overnight compensent le risque par une prime d'edge
🟡 **SYNTHÈSE** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Les marchés financiers tendent à récompenser le risque overnight — une large part de l'edge dans les marchés est une compensation pour le risque de portage de position. Les daytraders qui n'ont jamais de positions overnight peuvent manquer une part substantielle de cet edge.
**TRADEX-AI C1** : En mode Manuel, TRADEX peut afficher la distinction entre signal intraday pur et signal avec potentiel de continuation overnight sur GC/ZW — permettre à Abdelkrim de juger si le contexte justifie une tenue de position au-delà de la session.
*Catégorie : gestion_risque_entree*

---

### D5420 — Trader dans tous les environnements développe la compréhension du marché
🔵 **ÉCOLE** (Source : catching_the_wave_ideas_for_finding_trend_days.md) : Même sans trend day, trader avec un risque réduit dans les autres environnements de marché fournit plus d'informations sur le caractère du marché que n'importe quel processus analytique ou outil. Le trading est une compétence qui va au-delà de la seule analyse.
**TRADEX-AI C1** : TRADEX ne doit pas bloquer tous les signaux en dehors des trend days — en mode "range", proposer des configurations réduites (taille de position divisée par 2, objectif profit ramené à 1:1.5 R/R minimum) pour maintenir la lecture du marché active.
*Catégorie : psychologie*
