# Extraction NinjaTrader — How To Trade With Volume Profile Part 1
**Source :** `bundles/ninjatrader/how_to_trade_with_volume_profile_part_1.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7811 → D7830 · **Page :** https://ninjatrader.com/futures/blogs/how-to-trade-with-volume-profile-part-1/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Volume profile comme cadre décisionnel pour qualifier la structure de marché (balance/imbalance) et définir les niveaux de référence POC/VAH/VAL/HVN/LVN — applicable à tous les actifs TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7811 — Définition du volume profile : activité par niveau de prix, pas par temps
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Le volume profile est une carte visuelle du volume d'activité par niveau de prix (histogram horizontal) — distinct du volume traditionnel qui mesure l'activité par période de temps (par bougie). Il montre où les traders ont été les plus actifs, révélant l'acceptation et le rejet de prix.
**TRADEX-AI C2** : Le volume profile est une source C2 prioritaire dans TRADEX — lire les JSON NT8/ATAS incluant les données VP (POC, VAH, VAL, HVN, LVN) comme inputs du moteur Python niveau 1.
*Catégorie : volume_liquidite*

### D7812 — Point of Control (POC) : niveau d'accord maximal
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Le POC est le niveau de prix où le plus grand volume a été échangé pendant une session. Il représente l'accord maximal, la participation maximale, et agit comme un aimant pour le prix. En conditions de marché équilibré, le prix revisite souvent le POC ; en tendance, il réagit fortement quand il s'en éloigne.
**TRADEX-AI C1/C2** : Le POC est un niveau de référence clé pour GC/CL/HG/ZW. Dans Belkhayate, l'accord maximal du marché au POC croise le concept de zone d'équilibre/BGC. Intégrer le POC comme niveau de confluence dans la grille de scoring /10.
*Catégorie : volume_liquidite*

### D7813 — Value Area (VAH/VAL) : ~70% du volume échangé
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : La value area représente environ 70% du volume échangé d'une session. VAH (Value Area High) = plafond de valeur, VAL (Value Area Low) = plancher de valeur. À l'intérieur : marché en accord. À l'extérieur : expansion dans une nouvelle valeur ou rejet vers l'équilibre.
**TRADEX-AI C2** : VAH et VAL sont des niveaux de support/résistance dynamiques clés. Un prix qui sort de la value area doit être analysé : si le delta confirme, c'est expansion ; si le delta diverge, c'est rejet probable. Intégrer dans les calculs de niveaux du moteur.
*Catégorie : volume_liquidite*

### D7814 — High-Volume Nodes (HVN) : zones de support/résistance et consolidation
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Les HVN sont des zones épaisses du profil où de forts volumes ont été échangés. Ils agissent typiquement comme support/résistance et zones de consolidation. Quand le prix revient sur ces zones, il ralentit souvent, tourne, ou construit une nouvelle structure.
**TRADEX-AI C2** : Sur GC/CL/HG/ZW — les HVN sont des zones de friction naturelle. En approche d'un HVN, réduire la taille de position ou attendre confirmation d'absorption avant d'entrer. Signal de prudence pour le moteur Python.
*Catégorie : volume_liquidite*

### D7815 — Low-Volume Nodes (LVN) : zones de déséquilibre et rupture rapide
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Les LVN sont des zones fines où le prix s'est déplacé rapidement avec une participation minimale. Quand le prix entre à nouveau dans ces zones, il se déplace souvent rapidement — soit en tranchant avec momentum, soit en rejetant brusquement la zone. Les LVN marquent des inefficacités.
**TRADEX-AI C2** : Un LVN entre le prix actuel et un objectif de cible = mouvement rapide probable. Un LVN entre l'entrée et le stop = risque d'accélération adverse. Intégrer dans les calculs de risk management.
*Catégorie : volume_liquidite*

### D7816 — Marché équilibré : profil en cloche, rotation autour de la valeur
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : En marché équilibré, le volume profile forme souvent une cloche symétrique avec un POC central, rotation autour de la valeur, tests répétés de VAH/VAL, et peu de follow-through au-delà des extrêmes. Les acheteurs et vendeurs sont en accord relatif. Ces jours récompensent patience et précision avec comportement mean-revertant vers le POC.
**TRADEX-AI C1** : Contexte de marché équilibré = configuration de range. Le moteur Python doit qualifier le contexte (balance vs imbalance) avant de générer un signal. En balance, les setups de retour vers le POC sont prioritaires.
*Catégorie : structure_marche*

### D7817 — Marché déséquilibré : profil allongé, valeur migrante, jour de tendance
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : En marché déséquilibré, le profil est allongé ou asymétrique, la valeur migre plus haut ou plus bas, les mouvements sont fortement directionnels, le POC migre pendant la session, et des impressions simples (single prints) se forment. Ce sont des jours de tendance : fader les extrêmes est dangereux, les cassures et pullbacks fonctionnent mieux, et la migration de valeur confirme le biais directionnel.
**TRADEX-AI C1** : Contexte déséquilibré = jour de tendance. En mode Auto, les signaux dans le sens de la migration de valeur ont une pondération supérieure. La grille de scoring /10 doit distinguer balance vs imbalance pour pondérer correctement les signaux.
*Catégorie : structure_marche*

### D7818 — Stratégie POC Reversion : retour vers le POC en marché équilibré
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Quand le prix s'étend depuis le POC et ralentit, en marché équilibré sans catalyseur directionnel fort, avec prix étendu au-delà de la valeur et montrant des signes d'épuisement de momentum — le POC agit comme un aimant qui attire le prix vers la zone du plus fort accord précédent. La stratégie de reversion est construite sur ce principe.
**TRADEX-AI C1/C2** : Pour GC/CL/HG/ZW en mode de marché équilibré — le retour vers le POC est un signal de cible valide. À intégrer dans le prompt KB quand le contexte est "balance day" confirmé par les données VP.
*Catégorie : configuration*

### D7819 — Stratégie Value Area Rotation : trader le range VAH-VAL
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Si le prix reste dans la value area (entre VAH et VAL), certains traders voient le marché comme rotationnel. Approche : VAL comme référence basse, VAH comme référence haute, surveiller la rotation vers le POC ou le côté opposé du range. Idée fondamentale : la valeur est établie, le marché est confortable dans ce range tant que le prix trouve de l'acceptation dans la value area.
**TRADEX-AI C1** : En marché équilibré, la rotation VAH↔VAL est un cadre de range trading applicable à GC/CL/HG/ZW. Les niveaux VAH et VAL sont des niveaux de référence à intégrer dans le dashboard et le scoring de signal.
*Catégorie : configuration*

### D7820 — Stratégie LVN Breakout : momentum sur rupture de zone de déséquilibre
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Les LVN agissent comme des poches d'air — zones où le prix s'est déplacé vite avec faible participation. Si le prix casse à travers un LVN avec momentum, chercher continuation dans la direction de la cassure, attendre expansion de volume forte, confirmer l'acceptation au-delà du LVN. Si le momentum s'estompe et que le prix retombe en valeur précédente, la thèse de cassure est invalidée.
**TRADEX-AI C2** : Un LVN cassé avec confirmation de volume = signal de continuation. Un LVN rejeté = retour en valeur probable. Cette logique doit être intégrée dans l'interprétation des données VP par le moteur.
*Catégorie : configuration*

### D7821 — Stratégie Trend Day Value Migration : suivre la valeur migrante
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Lors des forts jours de tendance, le POC et les value areas se déplacent régulièrement dans la direction de la tendance. En uptrend avec valeur migrante : chercher pullbacks vers la valeur précédente, utiliser le POC montant comme support, cibler la continuation haussière. En downtrend inverse : fading des rallies vers valeur précédente, POC descendant comme résistance. La valeur qui s'empile dans une direction signale une participation soutenue.
**TRADEX-AI C1** : Migration de valeur = confirmation du biais directionnel. Le moteur Python doit détecter si le POC migre dans la direction du signal généré — confirmation renforçante pour la grille de scoring /10.
*Catégorie : indicateurs_tendance*

### D7822 — Placement des stops : au-delà de la structure, pas là où ça "semble" sûr
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Placer le stop où l'idée de trade est objectivement invalidée, pas où ça semble émotionnellement safe. Les approches communes : au-delà de VAH/VAL, en dehors de la structure, au-delà des zones de rejet. Si le prix rentre en valeur après une tentative de cassure, le postulat a changé.
**TRADEX-AI C1** : Règle de stop structurel confirmée pour TRADEX : le stop est placé au-delà du niveau qui invalide objectivement le signal (VAH/VAL pour un trade sur value area, LVN pour un breakout). Cohérent avec la gestion de risk_manager.py.
*Catégorie : gestion_risque_entree*

### D7823 — Dimensionnement position : tick value × distance stop = risque dollar
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Calculer systématiquement : valeur du tick × distance du stop × nombre de contrats = risque dollar. Garder le risque cohérent entre les trades. La gestion du risque en futures fait partie intégrante d'une stratégie solide.
**TRADEX-AI C1** : Formule à implémenter dans risk_manager.py pour chaque actif : GC = 10$/tick, CL = 10$/tick, HG = 2,50$/tick, ZW = 12,50$/tick. Le moteur calcule la taille de position automatiquement selon le risque dollar défini par l'utilisateur.
*Catégorie : gestion_risque_entree*

### D7824 — Éviter le surtrading : n'opérer que sur setups haute qualité confirmés
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Le volume profile donne de la clarté, mais pas des opportunités constantes. Trader seulement : les setups haute qualité, la structure claire, le déséquilibre confirmé. Ignorer le bruit et trader avec intention.
**TRADEX-AI C1** : Le moteur TRADEX niveau 1 (filtre Python) doit rejeter les signaux ambigus — pas de signal si score < 7.0/10, pas de signal si critère éliminatoire présent. Cohérent avec la règle 3/4 trading + 2/3 confirmation alignés.
*Catégorie : psychologie*

### D7825 — Volume profile = participation révélée, pas prédiction de prix
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Le volume profile ne prédit pas le prix — il révèle la participation. Et la participation drive le mouvement. La simplicité, la cohérence et l'amélioration session après session sont les clés — pas la complexité.
**TRADEX-AI C2** : Principe fondamental pour le prompt KB : le VP est un indicateur de participation passée/présente, pas prédictif. Claude doit l'utiliser comme contexte de structure plutôt que comme signal directif.
*Catégorie : psychologie*

### D7826 — Lecture de structure avant tout : marché équilibré ou déséquilibré ?
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Avant de trader, observer. Le volume profile aide à identifier rapidement si le marché est équilibré (profil en cloche, rotation) ou déséquilibré/en tendance (profil allongé, valeur migrante). Laisser le VP définir l'environnement avant de définir le trade.
**TRADEX-AI C2** : Le moteur Python niveau 1 doit en premier lieu qualifier le contexte de marché (balance/imbalance) avant toute analyse de signal. Ce contexte détermine quelle stratégie VP est applicable (reversion vs trending).
*Catégorie : structure_marche*

### D7827 — Configuration NinjaTrader Order Flow+ Volume Profile
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Dans NT8, ajouter Order Flow Volume Profile sur le chart, sélectionner session ou profil composite, puis ajuster : pourcentage de la value area, sessions du profil, configurations d'overlay. Cette flexibilité permet de personnaliser selon l'approche (rotations intraday vs shifts structurels plus larges).
**TRADEX-AI C2** : Le guide d'installation TRADEX doit documenter la configuration VP NT8 recommandée pour GC/CL/HG/ZW : VP session précédente en overlay, value area à 70%, affichage POC/VAH/VAL/HVN/LVN. Ces niveaux sont exportés dans les JSON NT8.
*Catégorie : volume_liquidite*

### D7828 — POC comme aimant en marché équilibré, résistance/support en tendance
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Le POC représente l'accord maximal du marché. En marché équilibré, le prix revisite souvent le POC car les conditions de balance le ramènent vers la zone de plus forte participation. En marché de tendance, il réagit fortement quand il s'en éloigne — le POC peut agir comme support/résistance selon le contexte.
**TRADEX-AI C1** : Double rôle du POC selon le contexte : aimant (balance) ou niveau de structure (tendance). Le cerveau KB doit prendre en compte le contexte de marché pour interpréter le POC correctement dans ses analyses.
*Catégorie : structure_marche*

### D7829 — Outside value = expansion dans nouvelle valeur OU rejet vers l'équilibre
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_with_volume_profile_part_1.md) : Quand le prix sort de VAH ou VAL, deux scénarios : (1) expansion vers une nouvelle valeur (confirmation delta + volume) = tendance ; (2) rejet vers l'équilibre (delta divergence + absorption) = retour dans la value area. Ces deux scenarios ont des trades opposés.
**TRADEX-AI C1/C2** : Décision binaire critique en dehors de la value area : expansion ou rejet. Le moteur doit utiliser le delta comme arbitre — delta confirme = expansion, delta diverge = rejet. Intégrer dans la logique de qualification de signal au niveau 2.
*Catégorie : structure_marche*

### D7830 — Discipline et cohérence : aucune stratégie ne fonctionne sans contrôle du risque
🔵 **ÉCOLE** (Source : how_to_trade_with_volume_profile_part_1.md) : Une structure parfaite, des niveaux correctement marqués et une lecture de participation impeccable n'ont pas de valeur sans contrôle du risque. Une décision émotionnelle peut tout défaire. La cohérence en trading ne vient pas des seules entrées — elle vient de la gestion du downside avec intention.
**TRADEX-AI C5** : Le mode Manuel TRADEX doit afficher en permanence le disclaimer légal ET rappeler la règle de risque dollar avant chaque signal. Le mode Auto reste verrouillé par défaut — cohérent avec RULE 0 sécurités obligatoires.
*Catégorie : gestion_risque_entree*
