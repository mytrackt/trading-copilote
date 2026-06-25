# Extraction NinjaTrader — Mastering Risk Management in Futures Trading
**Source :** `bundles/ninjatrader/mastering_risk_management_in_futures_trading.md` (HTTP 200) + 0 images certifiées
**Méthode images :** références à Figure 1/2 dans le bundle mais images non incluses · 0/0 certifiées · 0 à vérifier
**Décisions :** D7931 → D7950 · **Page :** https://ninjatrader.com/futures/blogs/mastering-risk-management-in-futures-trading/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Règles de risk management (stop loss, fixed fractional, ATM, account-level limits) directement applicables au risk_manager.py et aux garde-fous TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| Figure 1 (non incluse) | NinjaTrader account risk settings | Account Level Stop Loss | D7931 |
| Figure 2 (non incluse) | ATM dialog — scale out d'une position | Advanced Trade Management | D7937 |

## DÉCISIONS

### D7931 — Account-level stop loss : limites journalières et hebdomadaires
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : NinjaTrader propose des paramètres de risque au niveau du compte qui liquident automatiquement les positions journalièrement ou hebdomadairement dès qu'un objectif de profit ou un stop loss est atteint. Un trailing stop de compte et un verrou de session (interdiction de nouvelles entrées jusqu'à la session suivante) sont également disponibles.
**TRADEX-AI C1** : Les account-level risk settings NT8 constituent la dernière ligne de défense de TRADEX-AI ; le risk_manager.py doit surveiller l'atteinte de ces limites et suspendre le mode Auto automatiquement dès leur approche.
*Catégorie : gestion_risque_entree*

### D7932 — Overtrading : cause principale de mauvais résultats
🔵 **ÉCOLE** (Source : mastering_risk_management_in_futures_trading.md) : L'overtrading est souvent causé par un manque de discipline lors de la chasse aux profits ou de la récupération de pertes ; il peut conduire à de mauvais résultats. Les traders expérimentés fixent des limites journalières ou hebdomadaires pour verrouiller les profits ou limiter les pertes.
**TRADEX-AI C1** : Garde-fou TRADEX-AI : le moteur Python doit compter le nombre de trades par session et bloquer les nouvelles entrées si la limite configurée est atteinte, indépendamment du signal Claude.
*Catégorie : psychologie*

### D7933 — Discipline : verrouiller les profits dès l'objectif atteint
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Une fois l'objectif de profit atteint, le verrouiller et prendre la victoire est une pratique recommandée par les traders expérimentés.
**TRADEX-AI C1** : Règle de gestion de position : en mode Auto, dès que le profit target journalier configuré est atteint, TRADEX-AI suspend automatiquement les nouvelles entrées pour la session en cours.
*Catégorie : gestion_position_active*

### D7934 — Stop loss = assurance de trading
🟡 **SYNTHÈSE** (Source : mastering_risk_management_in_futures_trading.md) : Les ordres stop loss sont l'assurance du trader ; ils protègent le compte contre les grandes pertes. Analogie : comme la ceinture de sécurité et l'assurance auto avant de conduire.
**TRADEX-AI C1** : Règle absolue TRADEX-AI : aucun ordre ne peut être envoyé en mode Auto sans un stop loss attaché ; le risk_manager.py doit vérifier la présence du stop avant toute transmission via ATI.
*Catégorie : gestion_risque_entree*

### D7935 — Stop loss : placement optimal avant de dimensionner la position
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Avant de placer un trade, le trader doit d'abord déterminer le meilleur montant de stop loss pour protéger son capital tout en laissant au marché assez de room pour fluctuer sans être stoppé trop tôt ou trop souvent. C'est seulement ensuite qu'il peut fixer la taille de position correcte pour rester dans la tolérance au risque du compte.
**TRADEX-AI C1** : Séquence obligatoire dans risk_manager.py : (1) calculer le stop loss selon la structure de marché Belkhayate, (2) calculer la taille de position en fonction du stop et du risque max autorisé par trade — jamais l'inverse.
*Catégorie : gestion_risque_entree*

### D7936 — Stop loss : ordre stop market conditionnel
🔵 **ÉCOLE** (Source : mastering_risk_management_in_futures_trading.md) : Les stop loss sont typiquement des stop market orders — ordres conditionnels basés sur un prix stop sélectionné. Pour clôturer un short (buy stop), le prix stop doit être au-dessus du prix courant. Pour clôturer un long (sell stop), le prix stop doit être en dessous du prix courant.
**TRADEX-AI C1** : Règle de validation des ordres ATI : le risk_manager.py vérifie la cohérence du prix stop (au-dessus du prix courant pour buy stop, en dessous pour sell stop) avant de transmettre l'ordre.
*Catégorie : gestion_risque_entree*

### D7937 — Stop loss actif : obligatoire pour toute position ouverte
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Quelle que soit la durée prévue d'une position (quelques minutes ou quelques jours), avoir un ordre stop loss actif en marché pour chaque position ouverte est toujours une bonne pratique. Les événements de news et autres conditions peuvent retourner une position instantanément avec des effets dévastateurs.
**TRADEX-AI C1** : Garde-fou critique : le staleness_monitor.py de TRADEX-AI vérifie en permanence que chaque position ouverte dispose d'un stop loss actif dans NT8 ; absence de stop = alerte immédiate + suspension du mode Auto.
*Catégorie : gestion_risque_entree*

### D7938 — Stop loss GTC pour positions overnight
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Pour les positions conservées overnight, la durée de l'ordre stop loss doit obligatoirement être définie sur GTC (good till cancel).
**TRADEX-AI C1** : Règle de paramétrage ATI : pour tout signal ayant une durée prévue > 1 session, TRADEX-AI configure automatiquement le stop loss en GTC. Pour les trades intraday : durée DAY.
*Catégorie : gestion_risque_entree*

### D7939 — ATM strategies : bracket OCO entry/exit
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : À l'entrée d'une nouvelle position, des ordres additionnels peuvent être attachés pour capturer le profit et limiter les pertes : bracket simple (stop loss + profit target), trailing stop, ou sortie en plusieurs niveaux (scale out). L'ATM OCO annule automatiquement l'ordre restant si l'un des deux est rempli.
**TRADEX-AI C1** : L'architecture ATM OCO est le mode d'exécution standard de TRADEX-AI en mode Auto ; dès le fill de l'entrée, le bracket stop/target est actif, éliminant tout risque de position sans protection.
*Catégorie : gestion_position_active*

### D7940 — Exemple OCO : Micro E-mini S&P 500 3 contrats
🔵 **ÉCOLE** (Source : mastering_risk_management_in_futures_trading.md) : Exemple : achat de 3 contrats MES avec ATM bracket. Si le profit target est touché en premier, le stop loss est automatiquement annulé. Si le stop loss est touché en premier, le profit target est aussi annulé. Stop et target peuvent être à des niveaux différents.
**TRADEX-AI C1** : Ce comportement OCO est le standard NT8 utilisé par TRADEX-AI ; il garantit qu'une position ne peut pas être à la fois exposée à un stop loss et à un target résiduel non géré.
*Catégorie : gestion_position_active*

### D7941 — Fixed Fractional : formule de dimensionnement de position
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Fixed fractional = formule mathématique permettant de calculer la taille de position appropriée en fonction de l'équité du compte, de la tolérance au risque et du stop loss maximum sur un trade. Principe : le risque par trade est un pourcentage constant de l'équité du compte.
**TRADEX-AI C1** : La méthode fixed fractional doit être implémentée dans risk_manager.py de TRADEX-AI ; entrée : équité compte NT8 + stop loss calculé + pourcentage risque configuré → sortie : nombre de contrats.
*Catégorie : gestion_risque_entree*

### D7942 — Fixed Fractional : exemple avec 3% de risque
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Avec une tolérance au risque de 3%, il faudrait 23 trades perdants consécutifs pour perdre la moitié de l'équité de départ. Plus la tolérance au risque par trade est faible, plus la capacité à résister à un drawdown significatif est grande.
**TRADEX-AI C1** : Paramètre de configuration TRADEX-AI : le pourcentage de risque par trade (recommandé ≤ 3%) est configurable dans settings.py ; la valeur par défaut doit être prudente (1-2%) pour les premières phases live.
*Catégorie : gestion_risque_entree*

### D7943 — Fixed Fractional : exemple chiffré MES 10 000$
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Exemple : compte 10 000$, risque max 3% = 300$ par trade. Sur MES (point value 5$) : 1 contrat → stop max 60 points (300$/5$) ; 2 contrats → stop max 30 points (150$/5$) ; 3 contrats → stop max 20 points (100$/5$).
**TRADEX-AI C1** : Ce calcul est implémentable directement dans risk_manager.py : taille_stop_points = (equite * risque_pct) / (nb_contrats * point_value). À adapter pour GC (point value 100$/point), CL (1000$/point), HG (250$/0.01$), ZW (50$/cent).
*Catégorie : gestion_risque_entree*

### D7944 — Point values des actifs futures : impact sur le stop
🔵 **ÉCOLE** (Source : mastering_risk_management_in_futures_trading.md) : Le point value d'un actif futures détermine la perte ou le gain en dollars par mouvement d'un point. Exemple MES : 5$/point. Ce paramètre est essentiel pour le calcul de la taille de position en fixed fractional.
**TRADEX-AI C1** : Point values à configurer dans settings.py pour TRADEX-AI : GC (Or) = 100$/point ; HG (Cuivre) = 250$/0.01 cent = 25$/tick ; CL (Pétrole) = 1000$/point ; ZW (Blé) = 50$/cent.
*Catégorie : gestion_risque_entree*

### D7945 — Risque de compte vs risque de trade
🟡 **SYNTHÈSE** (Source : mastering_risk_management_in_futures_trading.md) : Toute approche solide de risk management considère deux niveaux de risque : le risque de trade (montant maximum perdu sur un seul trade) et le risque de compte (pourcentage maximum du compte risqué sur un seul trade). Ces deux niveaux sont équilibrés via le fixed fractional.
**TRADEX-AI C1** : Le risk_manager.py de TRADEX-AI maintient ces deux niveaux de contrôle : risque trade (stop calculé * taille) ET risque compte (% équité) ; le plus contraignant des deux s'applique.
*Catégorie : gestion_risque_entree*

### D7946 — Micro contrats : flexibilité pour comptes limités
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : L'utilisation de micro contrats donne plus de flexibilité dans le dimensionnement de position et les montants de stop loss pour les traders ayant des fonds de démarrage limités.
**TRADEX-AI C1** : TRADEX-AI peut trader les micro contrats (MGC pour l'or, MCL pour le pétrole, etc.) en mode de démarrage ou de test ; le risk_manager.py doit gérer les deux formats (standard et micro).
*Catégorie : gestion_risque_entree*

### D7947 — Effet de levier en futures : petits mouvements = grands impacts
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : En raison du levier important disponible en futures, même de petits mouvements de prix peuvent entraîner des profits ou des pertes significatifs. Être conscient du risque potentiel est seulement le début.
**TRADEX-AI C1** : Le levier futures est le principal danger du mode Auto de TRADEX-AI ; la combinaison fixed fractional + ATM stop loss + account-level limits constitue la triple protection obligatoire.
*Catégorie : gestion_risque_entree*

### D7948 — Protection du capital comme objectif prioritaire
🟢 **FAIT VÉRIFIÉ** (Source : mastering_risk_management_in_futures_trading.md) : Protéger le capital disponible pour trader est primordial — on ne peut pas trader si on a liquidé son compte. L'objectif du risk management est de protéger le capital pour continuer le parcours de trading.
**TRADEX-AI C1** : Principe fondateur du risk_manager.py TRADEX-AI : la préservation du capital prime sur la maximisation des profits ; en cas de doute sur un signal, le mode ATTENDRE est la décision par défaut.
*Catégorie : psychologie*

### D7949 — Approche disciplinée et cohérente du risk management
🟡 **SYNTHÈSE** (Source : mastering_risk_management_in_futures_trading.md) : Mettre en place un plan de risk management cohérent sur chaque trade est le meilleur moyen de réduire le stress et la perte de confiance pouvant résulter d'une ou plusieurs pertes catastrophiques.
**TRADEX-AI C1** : La cohérence du risk management automatisé de TRADEX-AI (même règles sur chaque trade) est un avantage majeur du mode Auto par rapport au trading manuel qui peut être affecté par les émotions.
*Catégorie : psychologie*

### D7950 — Simulation : environnement d'apprentissage du risk management
🔵 **ÉCOLE** (Source : mastering_risk_management_in_futures_trading.md) : Le trading en environnement simulé est l'une des meilleures façons de maîtriser le risk management, calibrer les niveaux de stop loss et pratiquer le placement d'ordres sans risquer de capitaux réels.
**TRADEX-AI C1** : TRADEX-AI dispose d'un mode simulation NT8 (Sim account) pour tester les règles de risk management avant passage en mode live ; le circuit_breaker.py doit distinguer les ordres simulation des ordres live.
*Catégorie : gestion_risque_entree*
