# Extraction AdamGrimes — Technical Analysis: Thinking in Categories
**Source :** `bundles/adamgrimes/technical_analysis_thinking_in_categories.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6771 → D6790 · **Page :** https://www.adamhgrimes.com/technical-analysis-thinking-in-categories/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Classification des trades en 4 catégories (continuation, termination, support holding, support breaking) pour adapter les setups à l'environnement de marché.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6771 — Wyckoff : 4 phases du cycle de marché
🔵 **ÉCOLE** (Source : technical_analysis_thinking_in_categories.md) : Wyckoff divise le marché en 4 phases idéalisées — accumulation, mark-up, distribution, markdown. Chaque phase conditionne le type de trade applicable.
**TRADEX-AI C1** : Identifier la phase Wyckoff courante sur GC/HG/CL/ZW avant de sélectionner un setup ; n'entrer en trend continuation qu'en phase mark-up, n'entrer en trend termination qu'en phase distribution.
*Catégorie : structure_marche*

### D6772 — Les 4 catégories universelles de trades techniques
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Tout trade technique appartient à l'une de ces 4 catégories : (1) Trend Continuation, (2) Trend Termination, (3) Support/Resistance Holding, (4) Support/Resistance Breaking/Failing. Ces 4 catégories sont exhaustives et mutuellement exclusives.
**TRADEX-AI C1** : Classifier chaque signal TRADEX dans l'une de ces 4 catégories avant soumission à Claude Brain ; le prompt doit inclure la catégorie pour orienter l'analyse Belkhayate.
*Catégorie : structure_marche*

### D6773 — Trend Continuation : edge statistique vérifiable
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Les trades de trend continuation ont un edge statistique vérifiable car alignés avec le principe fondamental de persistance de tendance. Ce sont les plays de plus haute probabilité parmi les 4 catégories.
**TRADEX-AI C1** : Dans TRADEX, privilégier les signaux de type trend continuation sur GC/HG/CL/ZW quand la BGC (Belkhayate Gravity Center) et la Direction confirment une tendance établie — ces setups ont la probabilité de succès la plus élevée.
*Catégorie : indicateurs_tendance*

### D6774 — Trend Continuation : définir le risque avant l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Pour un trade de trend continuation, le risque doit être défini avant l'entrée — identifier le point exact où la tendance est violée (invalidation). Si ce point est trop loin pour offrir un R/R attractif, ne pas entrer.
**TRADEX-AI C1/C2** : Le moteur TRADEX doit calculer le niveau d'invalidation de tendance AVANT de générer un signal BUY/SELL ; si le ratio R/R calculé est < 1:2 (seuil Belkhayate), signal bloqué automatiquement.
*Catégorie : gestion_risque_entree*

### D6775 — Trend Continuation : prises de profits aux highs précédents
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Les profits les plus fiables en trend continuation sont pris systématiquement au niveau ou juste au-delà des highs précédents. Les meilleures trades évoluent en multi-legs, mais prendre les profits aux niveaux définis est la règle de cohérence.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, les targets primaires des signaux TRADEX doivent se situer aux niveaux des pivots Belkhayate précédents (Pivot High/Low calculés par NT8).
*Catégorie : gestion_position_active*

### D6776 — Trend Termination ≠ Trend Reversal
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Un trade de trend termination réussit si la tendance s'arrête — il n'est pas nécessaire que le marché reparte dans la direction opposée en tendance. Confondre trend termination et trend reversal crée des attentes erronées et des pertes excessives.
**TRADEX-AI C1** : Dans TRADEX, un signal de type « trend termination » a comme objectif premier l'arrêt du trend, pas un nouveau trend opposé. La target est une zone de consolidation, pas un retournement complet.
*Catégorie : psychologie*

### D6777 — Trend Termination : R/R potentiel élevé mais probabilité basse
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Les trades de trend termination ne sont pas des plays à haute probabilité, mais offrent des récompenses potentielles bien supérieures au risque initial. Sur un large échantillon, l'expectancy peut être positive même si la majorité des trades sont perdants.
**TRADEX-AI C1** : Le moteur TRADEX doit appliquer un score de confiance abaissé (< 60%) aux signaux de type trend termination ; ils sont valides uniquement si le R/R calculé est ≥ 1:3 (seuil majoré vs le 1:2 standard Belkhayate).
*Catégorie : gestion_risque_entree*

### D6778 — Trend Termination : discipline de fer requise — risque de perte carrière
🔴 **NON SOURCÉ — AVERTISSEMENT** (Source : technical_analysis_thinking_in_categories.md) : Les trades countertrend (trend termination) sont la principale source de pertes catastrophiques et career-ending. Le risque de gaps overnight contre une position countertrend est réel et doit être intégré dans le position sizing.
**TRADEX-AI C1/C2** : Mode Auto INTERDIT sur les signaux de type trend termination (countertrend) — ces signaux sont affichés en mode Manuel uniquement, avec avertissement explicite dans l'UI. Position size réduit de 50% vs signal trend continuation.
*Catégorie : gestion_risque_entree*

### D6779 — Support/Resistance Holding : R/R le plus faible des 4 catégories
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Les trades de support/resistance holding ont tendance à offrir les ratios reward/risk les plus faibles des 4 catégories, car le marché est en équilibre relatif juste au-dessus du support. Ces trades opèrent souvent dans des environnements sous-optimaux.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, les signaux TRADEX basés uniquement sur un test de support/résistance sans confirmation de momentum (C2) reçoivent un score Belkhayate réduit de 1 point.
*Catégorie : structure_marche*

### D6780 — Failed Breakout : subset à haute probabilité des trades S/R Holding
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Les failed breakouts (faux-cassures) constituent un sous-ensemble spécial des trades support/resistance holding avec une probabilité de succès très élevée. Quand tout le monde est positionné dans le mauvais sens, le potentiel de mouvement dramatique est maximal.
**TRADEX-AI C1/C2** : Ajouter un détecteur de failed breakout dans le moteur TRADEX : si un niveau de résistance/support est cassé puis regagné dans la même session avec volume décroissant (C2 Order Flow), générer un signal prioritaire de type S/R Holding avec score majoré de +1.
*Catégorie : configuration*

### D6781 — Support/Resistance Breaking : la majorité des breakouts échouent
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : La plupart des breakouts échouent. C'est une réalité statistique documentée. Les zones de breakout sont des zones de haute volatilité et faible liquidité, souvent très suivies (crowded trades), ce qui augmente le risque d'exécution (slippage).
**TRADEX-AI C2** : TRADEX ne génère un signal de breakout confirmé que si le volume Order Flow (C2) valide la direction — un breakout sur volume faible ou neutre est classé ATTENDRE automatiquement.
*Catégorie : volume_liquidite*

### D6782 — Breakout : patterns précurseurs des meilleurs setups
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Les meilleurs breakouts sont précédés de patterns identifiables : higher lows qui remontent vers la résistance (pour les breakouts haussiers), montrant un déséquilibre acheteur persistant avant la cassure. Les breakouts non précédés de ces patterns sont moins fiables.
**TRADEX-AI C1** : Dans TRADEX, avant de valider un signal de breakout sur GC/HG/CL/ZW, vérifier que les 2-3 derniers pivots bas (higher lows) progressent vers le niveau de résistance — condition nécessaire pour score ≥ 7/10.
*Catégorie : configuration*

### D6783 — Breakout : acheteurs exclus reviennent en jours/semaines
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Dans les meilleurs breakouts, les traders exclus par la soudaineté de la cassure sont contraints de racheter dans les jours et semaines suivants, fournissant un vent favorable durable à la position.
**TRADEX-AI C3/C7** : Après un signal de breakout validé, le moteur TRADEX maintient le biais directionnel pendant 5 à 15 sessions consécutives sauf invalidation explicite — les signaux ATTENDRE intra-session sont ignorés si la structure breakout est intacte.
*Catégorie : timing*

### D6784 — Ne pas trader les breakouts en mode réactif non planifié
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Exécuter des trades de breakout non planifiés en mode réactif est rarement une formule de succès à long terme. Les spécialistes du breakout maintiennent une watchlist de candidats et planifient leurs entrées à l'avance.
**TRADEX-AI C1** : Le mode Auto de TRADEX ne peut déclencher un signal de breakout que si ce niveau était présent dans la watchlist TRADEX depuis au moins la session précédente — pas de breakout en mode réactif pur.
*Catégorie : psychologie*

### D6785 — Adapter les setups à l'environnement de marché
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : Certains environnements de marché favorisent certaines catégories de trades. Un trader spécialisé dans un seul setup doit reconnaître que seuls quelques environnements lui sont favorables et attendre ces conditions.
**TRADEX-AI C1** : Le moteur TRADEX filtre les signaux selon le régime de marché détecté (trending/ranging/volatile) ; chaque catégorie de signal n'est activée que dans son environnement favorable.
*Catégorie : structure_marche*

### D6786 — Ne pas trader = faire partie du job description
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis_thinking_in_categories.md) : "Ne pas trader" est une action légitime et fait partie intégrante du job description d'un trader spécialisé. Attendre les conditions favorables à son setup est une compétence, pas une faiblesse.
**TRADEX-AI C1** : Le signal ATTENDRE de TRADEX est un output de première classe, équivalent aux signaux ACHETER/VENDRE — il est affiché avec la même emphase dans l'UI et documenté dans les logs.
*Catégorie : psychologie*

### D6787 — Probabilité des trades de trend continuation plus haute que countertrend
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Les plays de trend continuation sont plus hauts en probabilité que les plays de trend termination (countertrend). La règle statistique de persistance de tendance est l'un des principes fondamentaux du comportement des prix.
**TRADEX-AI C1** : TRADEX applique un bonus de +0.5 point au score /10 pour tout signal de type trend continuation aligné avec la Direction Belkhayate — et un malus de -0.5 point pour tout signal countertrend.
*Catégorie : indicateurs_tendance*

### D6788 — Counterbalancer les setups : au moins 2 catégories complémentaires
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : La plupart des traders performent mieux avec au moins deux setups contrebalancés plutôt qu'un seul. Le trader spécialisé sur un seul setup existe et peut réussir, mais doit accepter de nombreuses périodes d'inactivité.
**TRADEX-AI C1** : TRADEX supporte les 4 catégories de trade mais les pondère différemment selon le régime détecté — l'architecture est conçue pour ne pas être mono-setup.
*Catégorie : configuration*

### D6789 — Simplifier et clarifier les setups
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : La règle de développement des setups : catégoriser → simplifier → simplifier encore. La clarté des règles d'entrée/sortie et leur classification dans les 4 catégories est une priorité absolue.
**TRADEX-AI C1** : Chaque règle de la KB Belkhayate dans KNOWLEDGE_BASE_MASTER.json doit être taguée avec l'une des 4 catégories (trend_continuation / trend_termination / sr_holding / sr_breaking) pour que Claude Brain sélectionne les règles pertinentes par catégorie de signal.
*Catégorie : configuration*

### D6790 — Overlap entre catégories : un trade peut appartenir à plusieurs
🟡 **SYNTHÈSE** (Source : technical_analysis_thinking_in_categories.md) : Il existe des overlaps entre catégories — acheter un support dans une tendance peut être simultanément un trade de trend continuation ET un trade de support holding. Le trader doit construire un système de classification cohérent qui lui correspond.
**TRADEX-AI C1** : Dans TRADEX, un signal peut recevoir deux tags de catégorie simultanément (ex : trend_continuation + sr_holding) — le score /10 est calculé sur la catégorie principale, avec un bonus de +0.3 si les deux catégories sont alignées.
*Catégorie : structure_marche*
