# Extraction StockCharts — Stage 8: Monitoring Your Investments
**Source :** `bundles/stockcharts/stage_8_monitoring_your_investments.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D3811 → D3820 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/the-traders-journal-by-gatis-roze/stage-8-monitoring-your-investments.md
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : principes de surveillance active applicables à GC/HG/CL/ZW — gestion de position ouverte et discipline de monitoring post-entrée.

## INVENTAIRE IMAGES CERTIFIÉES
*Aucune image dans ce bundle.*

## DÉCISIONS

### D3811 — Surveiller une position dès l'achat : première perte la moins chère
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "If the trend turns against you, the first loss is always the cheapest." Le monitoring commence immédiatement après l'achat.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, dès qu'un signal est exécuté en mode Auto ou Manuel, la surveillance du trend doit être continue — toute inversion de trend doit déclencher une révision immédiate de la position.
*Catégorie : gestion_position_active*

### D3812 — Principe "chaise près de la sortie" — planifier la sortie avant l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : Stage 9 (Selling) est défini comme cible avant même d'entrer. La citation "Don't wait for a gift wrapped invitation to the selling party" illustre ce principe.
🟡 **SYNTHÈSE** : Le monitoring est inséparable de l'anticipation de la sortie.
**TRADEX-AI C1** : Pour chaque signal TRADEX-AI (GC/HG/CL/ZW), le stop-loss et l'objectif de profit doivent être définis AVANT l'envoi de l'ordre via NT8 ATI — jamais en cours de position.
*Catégorie : gestion_risque_entree*

### D3813 — Les marchés se répètent : l'histoire déverrouille les insights actuels
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "History matters because markets do indeed repeat themselves." (article "How History Unlocks Deep Insights Within Today's Price and Volume Charts").
**TRADEX-AI C7** : Les corrélations historiques GC/HG/CL/ZW/ES/DX/VX doivent être intégrées dans la matrice de corrélation 30j — les patterns historiques répétitifs renforcent la confiance d'un signal.
*Catégorie : correlations*

### D3814 — Monitoring = tâche de Sisyphe : effort continu sans fin
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : Article "Monitoring Your Investments is a Sisyphean Task" — la surveillance des positions est un travail continu et incessant.
**TRADEX-AI C1** : Le moteur Python surveille NT8/ATAS toutes les 2 secondes (architecture événementielle niveau 1) — principe aligné avec cette règle de monitoring continu.
*Catégorie : gestion_position_active*

### D3815 — Principe des groupes (lois de regroupement) — les marchés se déplacent en blocs
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "Fish swim in schools. Birds fly in flocks. Humans follow grouping principles too." (article "Why Successful Investors Embrace the Laws of Grouping").
🟡 **SYNTHÈSE** : Les actifs se déplacent en corrélation sectorielle — surveiller le groupe renforce la surveillance individuelle.
**TRADEX-AI C7** : GC et HG (métaux), CL et ZW (matières premières énergie/agri) montrent des comportements de groupe — un signal sur GC doit être validé par la direction de HG (corrélation C7).
*Catégorie : correlations*

### D3816 — L'ego perturbe les décisions de monitoring
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : Article "Talk to Your EGO Before You Trade!" (Stage 9 Selling) — l'ego est un obstacle identifié dans la littérature Tensile Trading.
**TRADEX-AI C5** : Le mode Auto de TRADEX-AI élimine le biais ego en exécutant les sorties sans intervention humaine quand la confiance ≥ seuil — en mode Manuel, Abdelkrim doit être conscient de ce biais.
*Catégorie : psychologie*

### D3817 — Les positions doivent être traitées comme des enfants — surveillance parentale
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "investors should think of their equity positions as their children" (article "Yes - Successful Investors Must Be Like Loving Parents").
🟡 **SYNTHÈSE** : La surveillance active est une responsabilité de soin, pas une tâche secondaire.
**TRADEX-AI C1** : Chaque position ouverte sur GC/HG/CL/ZW dans TRADEX-AI doit avoir un statut de monitoring actif — le dashboard doit afficher l'état de chaque position en temps réel.
*Catégorie : gestion_position_active*

### D3818 — 90% des sociétés Fortune 500 ont disparu — rien n'est permanent
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "Can You Believe 90% of Fortune 500 Equities Have Vaporized?" — les tendances des actifs ne durent pas indéfiniment.
**TRADEX-AI C1** : Les tendances sur GC/HG/CL/ZW finissent par s'inverser — le système de monitoring doit détecter les signes d'essoufflement (Énergie Belkhayate, Direction) avant que la tendance ne casse complètement.
*Catégorie : gestion_position_active*

### D3819 — Pipeline de profits : processus séquentiel rigoureux d'investissement
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : Article "Your Investing Pipeline to Profits" — six étapes étudiées dans les séminaires Tensile Trading, pipeline séquentiel.
🟡 **SYNTHÈSE** : Un pipeline structuré (comme les 3 niveaux TRADEX-AI) améliore la discipline de surveillance.
**TRADEX-AI C1** : L'architecture événementielle TRADEX-AI (Niveau 1 Python → Niveau 2 Python → Niveau 3 Claude) constitue un pipeline structuré aligné avec ce principe — chaque niveau doit être franchi avant d'activer le suivant.
*Catégorie : configuration*

### D3820 — Augmenter les probabilités de profit après l'achat : surveillance proactive
🟢 **FAIT VÉRIFIÉ** (Source : stage_8_monitoring_your_investments.md) : "You Bought It...But Here's How You Increase Your Probabilities of Making Profits!" — la surveillance active post-achat améliore les probabilités de profit.
**TRADEX-AI C1** : Après exécution d'un ordre GC/HG/CL/ZW, le moteur Python continue de surveiller les indicateurs Belkhayate (BGC, Direction, Énergie, Pivots) pour optimiser le timing de sortie et maximiser le R/R ≥ 1:2.
*Catégorie : gestion_position_active*
