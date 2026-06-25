# Extraction StockCharts — Stage 5: Routines
**Source :** `bundles/stockcharts/stage_5_routines.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D3751 → D3770 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/the-traders-journal-by-gatis-roze/stage-5-routines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : routines de trading structurées — directement applicable à la discipline d'exécution quotidienne sur GC/HG/CL/ZW et à la structuration des sessions de surveillance TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
*Aucune image dans ce bundle (page index/TOC uniquement).*

## DÉCISIONS

### D3751 — Stage 5 : L'Escalier vers la Reproduction des Profits
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Le titre de l'article fondateur "Tensile Trading Stage #5 The Stairway to Reproducing Profits - Routines" affirme que les routines sont le mécanisme permettant de reproduire les profits de manière consistante.
🟢 **FAIT VÉRIFIÉ** : L'introduction du Stage 5 affirme : "Great athletes make greatness look effortless. Great traders make trading seem natural. The fact is that those who've achieved mastery make greatness look easy."
**TRADEX-AI C1** : Les routines TRADEX-AI doivent être aussi automatiques que des réflexes — démarrer le moteur Python (surveillance 2s), vérifier le staleness_monitor, confirmer la connexion NT8/ATAS — ces vérifications pré-trade deviennent invisibles avec la pratique répétée.
*Catégorie : configuration*

### D3752 — Les Premières 3 Heures de la Journée d'un Trader
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader: The First 3 Hours" référencé — Roze a "connu beaucoup de grands traders. Oui, ils existent. Certains sont devenus des gestionnaires de fonds."
🟡 **SYNTHÈSE** : Les 3 premières heures de trading (ouverture marché) sont les plus volatiles et les plus critiques — les professionnels ont des routines pré-marché précises : lecture des overnight gaps, vérification des news, positionnement du marché global avant de regarder les positions individuelles.
**TRADEX-AI C4** : Pour les futures TRADEX-AI (GC/HG/CL/ZW), la routine pré-session inclut : (1) vérifier les événements macro du jour (NFP/FOMC/CPI via News Gate), (2) lire les niveaux de clôture overnight, (3) vérifier DX/ES/VX pour l'état macro — avant d'activer le moteur de surveillance.
*Catégorie : timing*

### D3753 — Redux : La Préparation Parfaite Précède l'Exécution
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader - Redux" référencé — analogie de l'alpiniste qui "prépare méticuleusement et exécute parfaitement une ascension de montagne, capturant l'importance des deux."
🟡 **SYNTHÈSE** : La préparation (plan de trade) est aussi importante que l'exécution — un trade bien préparé s'exécute mécaniquement ; un trade non préparé déclenche l'improvisation émotionnelle.
**TRADEX-AI C1** : TRADEX-AI assure la préparation automatique (analyse 7 cercles, score /10, calcul R/R) — Abdelkrim arrive à l'exécution avec un dossier complet. Le Mode Manuel n'est pas de l'improvisation mais de la décision éclairée sur base préparée.
*Catégorie : gestion_risque_entree*

### D3754 — Partie III : 11h30 - 13h00 (Heure NYC)
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader: Part III 11:30 AM - 1:00 PM (NYC Time)" référencé — Roze "porte littéralement son bureau pendant les heures de trading". Larry Prusak : "All work is social."
🟡 **SYNTHÈSE** : La période 11h30-13h00 NYC est la "traversée du désert" du trading — liquidité réduite entre les sessions de matin et d'après-midi. Les professionnels réduisent leur activité et utilisent ce temps pour analyser les positions existantes.
**TRADEX-AI C2** : Pour GC/HG/CL/ZW (futures CME/CBOT), les horaires de liquidité optimale sont différents des actions — GC peak: 8h-12h NYC + 14h-17h NYC. Le staleness_monitor doit intégrer des seuils de freshness différents selon les plages horaires de liquidité.
*Catégorie : timing*

### D3755 — La Pause du Milieu de Journée
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader: The Midday Pause" référencé — "Inévitablement, un moment arrive pendant la journée de trading où je me demande 'pourquoi est-ce que je fais ça ?'"
🟡 **SYNTHÈSE** : La pause du milieu de journée est psychologiquement nécessaire — elle évite la fatigue décisionnelle qui conduit à de mauvais trades. Les traders professionnels planifient activement des pauses dans leur routine.
**TRADEX-AI C5** : Une règle de psychologie pour TRADEX-AI : si Abdelkrim a pris 2 pertes consécutives dans la journée, activer une pause forcée de 30-60 min avant tout nouveau signal — ce délai de réflexion est distinct de la suspension_auto de risk_manager.py (qui s'applique au mode Auto uniquement).
*Catégorie : psychologie*

### D3756 — 13h00 - 14h30 : Certaines Batailles, il Vaut Mieux Fuir
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader 1:00 - 2:30 PM (NYC Time)" référencé — "Certaines batailles, vous restez et vous combattez. D'autres, il vaut mieux s'en aller."
🟡 **SYNTHÈSE** : La capacité à reconnaître quand ne PAS trader est aussi importante que de savoir quand trader — les conditions de marché défavorables (faible liquidité, range étroit, news incertaines) justifient l'abstention active.
**TRADEX-AI C1** : Le signal ATTENDRE de TRADEX-AI est une décision active, pas un défaut — il traduit exactement "cette bataille, il vaut mieux s'en aller". Le score < 7,0 déclenche un ATTENDRE mécanique ; le Mode Manuel permet à Abdelkrim d'imposer son propre ATTENDRE si le contexte le justifie.
*Catégorie : gestion_risque_entree*

### D3757 — La Dernière Heure et Demie : L'Heure du Pouvoir
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Day in the Life of a Stock Market Trader: The Last 90 Minutes" référencé — "La dernière heure de trading est comme 'The Hour of Power'. Ça compte !"
🟡 **SYNTHÈSE** : La dernière heure de trading (closing range) concentre un volume significatif — les institutionnels ajustent leurs positions en fin de journée, créant des mouvements prévisibles. C'est souvent la meilleure période pour les entrées ou sorties.
**TRADEX-AI C2** : Pour GC (COMEX), la dernière heure (15h00-16h00 NYC) concentre les clôtures de positions institutionnelles — les signaux TRADEX-AI dans cet intervalle peuvent bénéficier d'un momentum additionnel. Le Order Flow ATAS (C2) est particulièrement pertinent dans ce créneau.
*Catégorie : timing*

### D3758 — Les Routines d'Investissement : Pilier de Tout Programme Réussi
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Investing Routines: A Pillar of Any Successful Program" référencé — analogie avec les bumper cars : "La voiture de foire partait dans une direction jusqu'à ce qu'elle heurte un mur, puis repartait dans une nouvelle direction aléatoire."
🟡 **SYNTHÈSE** : Un trader sans routines ressemble à une bumper car — réactif, chaotique, sans direction constante. Les routines créent la trajectoire directionnelle nécessaire à la reproductibilité.
**TRADEX-AI C1** : La boucle Python 2s de TRADEX-AI est la routine la plus fondamentale — elle remplace le "bump and redirect" émotionnel par une surveillance mécanique constante. Les routines humaines (vérification pré-session, revue post-session) amplifient cette mécanique.
*Catégorie : configuration*

### D3759 — Warm-Up Avant l'Exécution : Deux Approches de Traders
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "How Two Investors Warm-up Before Executing Any Trade" référencé — Roze rapporte une conversation "très personnelle" avec Harvey Baraban sur leurs routines de warm-up respectives avant de trader.
🟡 **SYNTHÈSE** : Un warm-up de trading inclut typiquement : (1) vérification de l'état d'esprit personnel, (2) lecture des conditions de marché global, (3) revue des positions ouvertes, (4) identification des niveaux clés du jour — avant toute exécution.
**TRADEX-AI C1** : Checklist warm-up TRADEX-AI : (1) vérifier connexion NT8+ATAS (staleness_monitor green), (2) lire News Gate (aucun événement macro dans les 30 min), (3) vérifier circuit breakers (tous green), (4) confirmer score /10 actuel — puis décider Mode Manuel ou Auto.
*Catégorie : configuration*

### D3760 — Productivité Personnelle et Routines
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Personal Productivity & Routines" référencé — cliché sur la discipline : "You've got to do what you have to do before you can do what you want to do."
🟡 **SYNTHÈSE** : La discipline de trading précède la liberté de trading — les tâches obligatoires (analyse, journalisation, gestion du risque) doivent précéder les prises de position. La discipline n'est pas une contrainte mais la condition préalable à la liberté.
**TRADEX-AI C1** : Dans TRADEX-AI, les "tâches obligatoires" automatisées (surveillance 2s, analyse 7 cercles, vérification news gate) PRÉCÈDENT systématiquement le signal — il est architecturalement impossible d'exécuter un ordre sans avoir passé ces filtres. La discipline est codée dans le système.
*Catégorie : configuration*

### D3761 — La Discipline du Trader : Comment Rester le Cap
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "A Trader's Discipline: How I Stay the Course" référencé — "Les investisseurs n'ont pas toujours la discipline d'agir comme une publicité Nike 'Just do it'."
🟡 **SYNTHÈSE** : La discipline en trading n'est pas une question de volonté mais de système — un bon système de trading rend la discipline facile car chaque action est définie à l'avance, éliminant les décisions en temps réel sous pression émotionnelle.
**TRADEX-AI C5** : TRADEX-AI élimine le problème de discipline pour l'analyse — les 7 cercles sont évalués mécaniquement. La discipline humaine d'Abdelkrim se concentre sur : (1) ne pas outrepasser le Mode Manuel quand le score dit ATTENDRE, (2) respecter les stops une fois en position.
*Catégorie : psychologie*

### D3762 — Le Secret du Succès
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "The Secret Of Success Is..." référencé — Roze comme étudiant en business school a eu le privilège d'observer John Elway jouer.
🟡 **SYNTHÈSE** : Le "secret du succès" tel que révélé dans ce contexte de trading est invariablement la pratique délibérée répétée — la constance des routines, pas l'inspiration ou le talent naturel, distingue les traders professionnels des amateurs.
**TRADEX-AI C1** : TRADEX-AI est construit pour la pratique délibérée : chaque session génère un README de transition documentant l'état du système — cette documentation systématique est la pratique délibérée appliquée au développement du système de trading lui-même.
*Catégorie : configuration*

### D3763 — L'Arbre de l'Argent : L'Arbre de Couleurs
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Your Money Tree: The Tree of Color" référencé — "La plupart des gens appellent ça l'Analyse Technique, mais je préfère penser à ça comme une 'Analyse Visuelle'." Image d'un arbre dont chaque branche représente un aspect de l'analyse technique.
🟡 **SYNTHÈSE** : L'"arbre de couleurs" (tree of color) est une métaphore visuelle de la structure de l'analyse technique — les indicateurs de tendance sont les branches principales ; les oscillateurs sont les branches secondaires ; les patterns de prix sont les feuilles.
⚫ **HYPOTHÈSE PROJET** : Le dashboard TRADEX-AI avec ses 7 cercles constitue un "arbre de couleurs" digital — chaque cercle est une branche, chaque indicateur est une feuille, le score /10 est la santé globale de l'arbre.
**TRADEX-AI C1** : L'interface React du dashboard TRADEX-AI doit présenter les 7 cercles comme des éléments visuels colorés (vert/orange/rouge) — permettant à Abdelkrim de "lire l'arbre" d'un coup d'œil sans parcourir des chiffres.
*Catégorie : configuration*

### D3764 — Parallèles Puissants : Top Traders et Top Commerciaux
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Powerful Parallels Yield Insights into Top Traders & Top Salespersons" référencé — "Savoir comment les meilleurs commerciaux convertissent les suspects en prospects en clients révèle des insights puissants sur les meilleurs traders."
🟡 **SYNTHÈSE** : L'analogie trader/commercial est instructive : les deux qualifient des opportunités (suspects → prospects → signaux valides), construisent un pipeline (watchlist → setups en attente), et concluent seulement sur les meilleures opportunités (best of breed).
**TRADEX-AI C1** : TRADEX-AI opère comme un "pipeline commercial" : le moteur Python surveille 9 actifs (suspects), le filtre 3/4 trading + 2/3 confirmation les qualifie en prospects, le score ≥ 7,0 les élève en signaux valides (clients). Seuls les meilleurs setups font l'objet d'un ordre.
*Catégorie : structure_marche*

### D3765 — Être au Sommet du Marché sur 12 Mois
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "How to be a Successful Investor Over All 12 Months" référencé — Mark Twain commentant le Nouvel An : "La semaine dernière..." — Roze note que la constance sur 12 mois, pas la performance des mois exceptionnels, définit un bon trader.
🟡 **SYNTHÈSE** : La saisonnalité affecte les performances sur 12 mois — certaines périodes (Q4, fin d'année fiscale) sont plus difficiles ou plus favorables selon les actifs. Maintenir la constance méthodologique sur toutes les saisons est l'objectif.
**TRADEX-AI C1** : Les 4 actifs TRADEX-AI ont des saisonnalités distinctes : GC (hausse en période d'incertitude), CL (saisonnalité demande été/hiver), ZW (saisonnalité récolte), HG (cycle économique global). Le module C7 (corrélations) doit intégrer ces patterns saisonniers.
*Catégorie : saisonnalite*

### D3766 — Rester au-Dessus du Marché
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Staying Atop the Market" référencé — "Le marché boursier est toujours un pas en avance sur vous. Plus tôt vous acceptez ce fait, mieux ce sera pour votre trading."
🟡 **SYNTHÈSE** : "Rester au-dessus du marché" signifie avoir des processus de surveillance proactifs (pas réactifs) — être informé des rotations sectorielles, des changements de régime, des shifts de sentiment AVANT qu'ils n'impactent les positions ouvertes.
**TRADEX-AI C1** : La surveillance TRADEX-AI 2s est la réponse technique à ce principe — détecter les signaux AVANT que les mouvements ne soient "évidents". Le circuit breaker et le staleness_monitor assurent que le système reste "au-dessus" même en cas de dégradation des données.
*Catégorie : configuration*

### D3767 — Comparer son Journal de Trader au Sien
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Compare Your Traders Journal to Mine" référencé — "Je vous montre le mien si vous me montrez le vôtre ! À quoi pensiez-vous ? On parle de journaux ici."
🟡 **SYNTHÈSE** : La tenue d'un journal de trading est une pratique universelle des traders professionnels — il documente les décisions, les émotions au moment du trade, les résultats — permettant une révision critique et un apprentissage accéléré.
**TRADEX-AI C1** : Les README de fin de session (00-pilotage/_context/) constituent le "journal de trader" de TRADEX-AI — chaque session documente les décisions, les signaux générés/ignorés, les ajustements. Cette documentation est la matière première de l'amélioration continue.
*Catégorie : configuration*

### D3768 — Dîner avec un Investisseur de 8 Milliards
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "Unique Insights From Dinner With An $8 Billion Investor" référencé — Roze a eu le plaisir de dîner avec un gestionnaire de fonds qui gère plus de 8 milliards et qui a un track-record remarquable.
🟡 **SYNTHÈSE** : Les insights des grands investisseurs institutionnels convergent généralement vers : discipline de processus, gestion du risque rigoureuse, horizon temporel cohérent avec la stratégie — des principes applicables à tous niveaux de capital.
**TRADEX-AI C3** : C3 (Institutionnels/COT) dans TRADEX-AI s'inspire de cette logique — suivre ce que font les "8 milliards" (positions COT des commerciaux et non-commerciaux CFTC) pour GC/HG/CL/ZW est un signal de confirmation puissant, même si Abdelkrim opère avec un capital beaucoup plus modeste.
*Catégorie : structure_marche*

### D3769 — Ne Pas Perdre de Vue la Forêt en Se Concentrant sur les Arbres
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "How Not to Lose Sight of the Forest (the Market) by Focusing on the Trees (Individual Equities)" référencé — certains traders se concentrent trop sur leurs positions individuelles et ratent la tendance macro.
🟡 **SYNTHÈSE** : La règle "voir la forêt avant les arbres" signifie : avant d'analyser un actif individuel, lire l'état du marché global (tendance macro, sentiment général, risque systémique) — l'actif individuel doit être vu dans son contexte macro.
**TRADEX-AI C4** : Le design en 3 niveaux de TRADEX-AI (Niveau 1 : 3/4 actifs trading, Niveau 2 : 2/3 confirmation, Niveau 3 : analyse Claude) applique exactement ce principe — ES/DX/VX (la forêt) filtrent avant l'analyse de GC/HG/CL/ZW (les arbres). Aucun signal actif individuel sans contexte macro validé.
*Catégorie : structure_marche*

### D3770 — Checklist Hebdomadaire : Valeur des Routines selon un VC
🟢 **FAIT VÉRIFIÉ** (Source : stage_5_routines.md) : Article "You Said It Fred: A Leading VC On The Value Of Routines, Plus An Overview Of My Weekly Checklist" référencé — une figure VC importante mentionne l'importance des routines ; Roze partage sa checklist hebdomadaire.
🟡 **SYNTHÈSE** : Une checklist hebdomadaire de trading inclut typiquement : (1) révision des trades de la semaine (gagnants/perdants), (2) mise à jour des niveaux clés (supports/résistances, pivots), (3) anticipation des événements macro de la semaine à venir, (4) ajustement des seuils de signal si nécessaire.
**TRADEX-AI C4** : Checklist hebdomadaire TRADEX-AI : (1) mettre à jour le calendrier NFP/FOMC/CPI (News Gate), (2) vérifier les nouvelles positions COT CFTC (publiées chaque vendredi, pour C3), (3) recalculer les corrélations 30j (C7), (4) auditer les logs d'erreurs circuit_breaker de la semaine.
*Catégorie : configuration*
