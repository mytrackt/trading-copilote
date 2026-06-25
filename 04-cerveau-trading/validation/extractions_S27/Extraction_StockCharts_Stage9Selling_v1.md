# Extraction StockCharts — Stage 9: Selling
**Source :** `bundles/stockcharts/stage_9_selling.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D3831 → D3845 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/the-traders-journal-by-gatis-roze/stage-9-selling.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : discipline de sortie directement applicable à la gestion des positions GC/HG/CL/ZW — psychologie de la vente, règles de sortie, gestion des pertes.

## INVENTAIRE IMAGES CERTIFIÉES
*Aucune image dans ce bundle.*

## DÉCISIONS

### D3831 — Choisir une chaise près de la sortie avant d'acheter
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "pick a chair close to the exit before you buy an equity and then sit down."
**TRADEX-AI C1** : Règle de sortie (stop-loss + target) obligatoire AVANT envoi de l'ordre NT8 ATI — le risk_manager.py doit refuser tout ordre sans stop défini.
*Catégorie : gestion_risque_entree*

### D3832 — "Margin Call" : ne pas paniquer si on est le premier à sortir
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : Citation du film MARGIN CALL — "it's not panic selling if you are first out the door." La sortie rapide est une stratégie, pas une panique.
**TRADEX-AI C1** : En mode Auto, TRADEX-AI doit exécuter les ordres de sortie dès que les conditions sont remplies — ne pas hésiter à sortir tôt sur GC/HG/CL/ZW quand le signal se dégrade.
*Catégorie : gestion_position_active*

### D3833 — Parler à son ego avant de trader
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : Article "Talk to Your EGO Before You Trade!" — "Most individual investors seem to feel it isn't cool to talk about exits before even buying an equity."
**TRADEX-AI C5** : Le biais ego (refus de planifier la sortie) est un facteur de risque psychologique — en mode Manuel, Abdelkrim doit planifier sa sortie avant de valider le signal TRADEX-AI.
*Catégorie : psychologie*

### D3834 — La vente est une lutte intérieure : dompter deux animaux sauvages
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "selling is an inner struggle that deals with an investor's ability to tame two wild..." (The Art of Selling Well: Part I) — les deux forces implicites sont la cupidité et la peur.
**TRADEX-AI C5** : Le mode Auto de TRADEX-AI neutralise ce conflit intérieur sur GC/HG/CL/ZW — la sortie est automatique quand les conditions sont réunies, sans intervention émotionnelle.
*Catégorie : psychologie*

### D3835 — Art de vendre Part II : les règles de Part I sont la fondation
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "Those rules provide the foundation for what..." (The Art of Selling Well: Part II) — les règles de vente sont fondatrices et s'enchaînent.
🟡 **SYNTHÈSE** : Une méthodologie de sortie structurée (multi-étapes) est supérieure à une décision ponctuelle.
**TRADEX-AI C1** : Le système de sortie TRADEX-AI doit être hiérarchisé : d'abord stop-loss technique, puis objectif de profit basé sur R/R ≥ 1:2, puis signal de retournement Belkhayate.
*Catégorie : gestion_position_active*

### D3836 — Gérer les pertes : accepter et corriger
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "Financial investment losses are the markets' way of telling you to make adjustments and to correct your present..." (How I Deal With Investment Losses).
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "I'm the only person I know that's lost a quarter of a billion dollars in one year... It's very character building." — les pertes sont inévitables et formatives.
**TRADEX-AI C5** : Le suspend_auto_mode (15-60 min après perte) est aligné avec ce principe — permettre une pause de correction avant de reprendre les signaux automatiques.
*Catégorie : psychologie*

### D3837 — Les investisseurs perdent parfois : vous n'êtes pas seul
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "We investors are imperfect creatures living in a complex world. We are destined to stumble and fall." (We Investors Lose At Times: You Are Not Alone).
**TRADEX-AI C5** : Le risk_manager.py de TRADEX-AI intègre ce principe via la suspension auto après perte — le système reconnaît que les pertes font partie du processus de trading, elles ne désactivent pas le système définitivement.
*Catégorie : psychologie*

### D3838 — L'effet de dotation : surestimer ce qu'on possède déjà
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : Article "The Endowment Effect" — les investisseurs ont tendance à surestimer la valeur de ce qu'ils détiennent déjà (biais cognitif nommé).
**TRADEX-AI C5** : L'effet de dotation peut retarder la sortie d'une position perdante sur GC/HG/CL/ZW — le mode Auto contourne ce biais en exécutant les stops sans intervention humaine.
*Catégorie : psychologie*

### D3839 — Méthode mnémotechnique pour les sorties
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : Article "Memory Tricks for Investors" (juillet, coaching) — des outils mnémotechniques aident à respecter les règles de sortie sous pression.
**TRADEX-AI C5** : Le dashboard TRADEX-AI doit afficher un rappel visuel des règles de sortie prédéfinies pour chaque position ouverte — aide à la décision en mode Manuel.
*Catégorie : psychologie*

### D3840 — Bob Farrell 10 règles : ne pas s'endormir sur des nouveaux sommets
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "As markets make new highs, investors often befriend a dangerous new companion. He's the greedy little devil..." (Bob Farrell: 10 Timely Reminders from a Wall Street Legend).
🔵 **ÉCOLE** : Bob Farrell, analyste légendaire de Wall Street.
**TRADEX-AI C5** : Sur GC (Or), les nouveaux sommets historiques attirent la cupidité — TRADEX-AI doit maintenir un niveau VIX + sentiment check même quand GC fait de nouveaux highs.
*Catégorie : psychologie*

### D3841 — Méthodologie de vente : 1+1=3 (combinaison de signaux)
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "Selling Methodology: 1 + 1 = 3" — enseigne Stage 9 depuis plus de 15 ans : la combinaison de signaux de sortie est plus puissante que chaque signal isolé.
🟡 **SYNTHÈSE** : La convergence de plusieurs signaux de sortie améliore la fiabilité de la décision.
**TRADEX-AI C1** : La règle TRADEX-AI "3/4 actifs tradables + 2/3 confirmations alignés" applique ce principe de convergence à l'entrée — la même logique doit s'appliquer à la sortie (convergence de stop technique + signal Belkhayate + dégradation momentum).
*Catégorie : configuration*

### D3842 — Six règles essentielles pour appuyer sur la gâchette (sortie)
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : Article "Pulling the Trigger: Six Essential Rules" — "these are internet days and news circles the globe at the speed of light."
🟡 **SYNTHÈSE** : Exécuter une sortie nécessite des règles prédéfinies face à un flux d'informations rapide.
**TRADEX-AI C6** : Le News Gate de TRADEX-AI (blocage 30min avant NFP/FOMC/CPI) est directement lié à ce principe — les nouvelles accélèrent la volatilité et doivent être anticipées dans les règles de sortie.
*Catégorie : gestion_risque_entree*

### D3843 — Brosser ses disciplines de vente : ne pas fermer la grange après la fuite du cheval
🟢 **FAIT VÉRIFIÉ** (Source : stage_9_selling.md) : "shutting the barn door after the horse has bolted means one is late to action" (Now Is the Time to Brush Up on Your Selling Disciplines).
**TRADEX-AI C1** : La surveillance continue (staleness_monitor + circuit_breaker) de TRADEX-AI est conçue pour détecter les inversions AVANT que le mouvement ne soit trop avancé — principe directement aligné.
*Catégorie : gestion_position_active*

### D3844 — Méthode de vente : l'intérieur avant l'extérieur
🟡 **SYNTHÈSE** (Source : stage_9_selling.md) : L'ensemble des articles Stage 9 convergent sur un principe : maîtriser le processus interne (psychologie, règles) avant d'exécuter la décision externe (ordre de vente).
**TRADEX-AI C5** : En mode Manuel, Abdelkrim doit valider son état psychologique (pas de peur, pas de cupidité) avant de confirmer ou refuser un signal TRADEX-AI — le dashboard peut afficher un checklist pré-décision.
*Catégorie : psychologie*

### D3845 — Stage 9 est le complément obligatoire de Stage 8 : entrée et sortie forment un système
🟡 **SYNTHÈSE** (Source : stage_9_selling.md + stage_8_monitoring_your_investments.md) : Les Stages 8 (monitoring) et 9 (selling) de Tensile Trading forment un système complet — surveiller sans plan de sortie est inutile.
**TRADEX-AI C1** : TRADEX-AI doit gérer le cycle complet position : entrée (signal) → surveillance (staleness_monitor, staleness_data) → sortie (stop ou target atteint) — aucun de ces trois éléments ne fonctionne seul.
*Catégorie : configuration*
