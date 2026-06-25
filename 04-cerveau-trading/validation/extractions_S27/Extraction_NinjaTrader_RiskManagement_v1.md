# Extraction NinjaTrader — Risk Management for Futures Trading
**Source :** `bundles/ninjatrader/risk_management.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8051 → D8070 · **Page :** https://ninjatrader.com/futures/futures-trading-basics/risk-management/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Gestion du risque en futures — capital à risque, taille de position, stops, diversification et outils ATM NinjaTrader.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D8051 — Capital à risque : définition et principe fondamental
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Le capital à risque (risk capital) est défini comme l'argent que l'on peut se permettre de perdre sans affecter son niveau de vie ni repousser l'horizon de retraite. Le trading futures ne doit être pratiqué qu'avec du risk capital.
**TRADEX-AI C1** : Ce principe est un garde-fou absolu dans TRADEX. Le risk_manager.py applique des limites de perte journalière et hebdomadaire calculées sur le capital alloué.
*Catégorie : gestion_risque_entree*

### D8052 — Risque au niveau du compte : "fixed fractional"
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : La méthode "fixed fractional" consiste à ne risquer qu'un pourcentage fixe du capital total sur chaque trade. Pour les nouveaux traders futures, commencer avec des tailles de position réduites est recommandé pour maîtriser le risque global.
**TRADEX-AI C1** : TRADEX implémente le fixed fractional via risk_manager.py — taille de position calculée en fonction du stop distance pour maintenir le risque par trade dans les limites définies.
*Catégorie : gestion_position_active*

### D8053 — Stop-loss au niveau du trade : prévenir les pertes incontrôlables
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Un stop-loss est tout ordre qui clôture une position lorsque le prix se déplace contre soi. Un safety stop doit offrir un profil risque/récompense raisonnable — limiter les pertes tout en laissant assez d'espace pour que le prix fluctue sans déclencher prématurément le stop.
**TRADEX-AI C1** : Chaque signal TRADEX inclut obligatoirement un niveau de stop structurel (au-delà du swing high/low ou zone S/D) et un R/R ≥ 1:2 avant validation.
*Catégorie : gestion_risque_entree*

### D8054 — Profit targets : définition de l'objectif de gain
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les profit targets sont calculés sur le P&L net en temps réel. Un trigger journalier ou hebdomadaire peut être configuré selon les objectifs du trader.
**TRADEX-AI C1** : Dans TRADEX, les cibles de profit sont déterminées par la zone S/D opposée (zone-to-zone) avec R/R minimum 2:1 — calculées avant l'entrée.
*Catégorie : gestion_position_active*

### D8055 — Loss limits : plafond de perte journalier/hebdomadaire
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les loss limits sont calculées sur le P&L net en temps réel. Un plafond journalier ou hebdomadaire peut être configuré selon les paramètres de risque du trader. Cette règle est un composant clé de la gestion de compte.
**TRADEX-AI C1** : TRADEX implémente `suspend_auto_mode` après perte dépassant le seuil critique — aligné avec cette règle. Le risk_manager.py surveille le P&L en continu.
*Catégorie : gestion_position_active*

### D8056 — Trailing max drawdown : suivi du drawdown en temps réel
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Le trailing max drawdown peut être calculé en fin de journée ou en temps réel pour suivre l'activité du compte vs les préférences de risque. Disponible sur NinjaTrader brokerage.
**TRADEX-AI C1** : Le circuit breaker TRADEX (circuit_breaker.py) surveille le drawdown en continu — analogue fonctionnel du trailing max drawdown. CB_NT8 se déclenche si les limites sont franchies.
*Catégorie : gestion_position_active*

### D8057 — Taille de position : levier de contrôle du risque
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Déterminer la taille de position appropriée permet d'éviter des pertes significatives et de construire l'expérience. Les Micro futures (1/10 de la taille d'un E-mini) permettent de commencer petit et de monter en taille au fur et à mesure.
**TRADEX-AI C1** : GC, HG, CL, ZW existent en version Micro — TRADEX peut intégrer les Micro en phase de validation avant de scaler vers les contrats standards.
*Catégorie : gestion_position_active*

### D8058 — Concentration : limiter le nombre de contrats et marchés simultanés
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les traders qui peinent à atteindre la consistance devraient limiter le nombre de contrats et de marchés qu'ils tradent activement pour maintenir le focus et réduire le risque global du compte.
**TRADEX-AI C1** : TRADEX gère 4 actifs tradables (GC/HG/CL/ZW) — la règle 3/4 signifie que seuls les actifs alignés sont retenus pour analyse Claude, évitant la dispersion.
*Catégorie : gestion_position_active*

### D8059 — Diversification : réduire l'exposition aux marchés corrélés
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : En diversifiant sur différents types de contrats futures non corrélés (indices, devises, matières premières), les traders peuvent réduire leur exposition globale aux marchés hautement corrélés qui se déplacent tous dans la même direction (ex : indices majeurs, obligations, devises).
**TRADEX-AI C7** : Le module correlations.py de TRADEX calcule la matrice de corrélations live 30j sur GC/HG/CL/ZW/ES/VX/MBT/6J — exactement ce principe appliqué.
*Catégorie : correlations*

### D8060 — Surveillance macro : news et rapports gouvernementaux
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les traders doivent surveiller attentivement les news, les rapports gouvernementaux et autres événements susceptibles de faire bouger le marché significativement. La gestion du risque ne s'applique pas en isolation — elle est au cœur de toute stratégie bien structurée.
**TRADEX-AI C4** : Le news gate TRADEX bloque les signaux 30 min avant NFP/FOMC/CPI. Les événements macro (C4) sont intégrés dans la grille /10 comme critères de déclenchement/blocage.
*Catégorie : macro_evenements*

### D8061 — ATM strategies : gestion automatisée des positions
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les ATM strategies (Advanced Trade Management) de NinjaTrader soumettent automatiquement stops et profit targets dans les millisecondes suivant l'entrée en position. Elles réduisent l'impact émotionnel sur les décisions de sortie.
**TRADEX-AI C1** : En Mode Auto, TRADEX envoie les ordres via NT8 ATI (port 36973) avec stops et targets prédéfinis — équivalent fonctionnel des ATM strategies.
*Catégorie : gestion_position_active*

### D8062 — ATM : cibles multiples et scaling out
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Les ATM strategies permettent d'utiliser plusieurs cibles et stops pour scaler hors d'une position (scale out). Les templates de stratégie sont personnalisables et réutilisables.
**TRADEX-AI C1** : Fonctionnalité à considérer pour TRADEX Phase C+ — le scaling out partiel à la première zone S/D cible préserve une partie des gains tout en laissant courir le reste.
*Catégorie : gestion_position_active*

### D8063 — Stratégies de stop personnalisées via ATM
🔵 **ÉCOLE** (Source : risk_management.md) : NinjaTrader permet de créer des stratégies de stop personnalisées (ex : trailing stop, stop par paliers) via le custom ATM builder — configurable sans code.
**TRADEX-AI C1** : Le trailing stop configurable est pertinent pour GC et CL où des tendances fortes peuvent se développer sur plusieurs heures.
*Catégorie : gestion_position_active*

### D8064 — Trading simulé : test avant capital réel
🟢 **FAIT VÉRIFIÉ** (Source : risk_management.md) : Le trading simulé est essentiel pour les nouveaux traders qui débutent ET pour les traders expérimentés testant de nouveaux concepts. NinjaTrader offre une simulation illimitée avec tous les comptes tradés et un essai gratuit 2 semaines.
**TRADEX-AI C1** : Mode Manuel TRADEX = simulation de décision pour Abdelkrim avant de basculer en Mode Auto — principe identique.
*Catégorie : psychologie*

### D8065 — Risque par trade : pourcentage du capital total
🟡 **SYNTHÈSE** (Source : risk_management.md) : Le concept de fixed fractional implique que le pourcentage risqué par trade est fixe, quelle que soit la conviction sur le setup. Cette discipline évite les sur-engagements émotionnels sur des trades "évidents".
**TRADEX-AI C1** : Dans TRADEX, le seuil de confiance ≥ seuil (Mode Auto) ne modifie pas la taille de position — le risk_manager.py applique le même % fixe indépendamment du score /10.
*Catégorie : gestion_risque_entree*

### D8066 — Profil risque/récompense du stop : room pour respirer
🟡 **SYNTHÈSE** (Source : risk_management.md) : Un stop trop serré crée un profil risque/récompense défavorable : le trade est arrêté avant d'avoir pu se développer. Le stop doit être assez large pour absorber la volatilité normale du marché mais pas au point de rendre le R/R négatif.
**TRADEX-AI C1** : La règle TRADEX R/R ≥ 1:2 intègre cette contrainte — le stop structurel (S/D ou swing) est évalué par rapport à la cible avant validation du signal.
*Catégorie : gestion_risque_entree*

### D8067 — Micro futures : réduction d'exposition pour l'apprentissage
🔵 **ÉCOLE** (Source : risk_management.md) : Les Micro futures (1/10 d'un E-mini) permettent aux traders de commencer petit et de scaler au fur et à mesure. Ils offrent une exposition réduite tout en conservant les mêmes conditions de marché réel.
**TRADEX-AI C1** : MES (Micro E-mini S&P) est un actif de CONFIRMATION dans TRADEX. Pour l'or (MGC), une progression Micro → standard est envisageable en Phase C.
*Catégorie : gestion_position_active*

### D8068 — Émotions et discipline : ATM comme garde-fou comportemental
🟡 **SYNTHÈSE** (Source : risk_management.md) : Les ATM strategies réduisent l'impact des émotions sur les décisions de trading en automatisant les sorties. La semi-automatisation permet de rester focalisé sur la stratégie plutôt que sur la gestion en temps réel.
**TRADEX-AI C1** : Le Mode Auto de TRADEX remplit exactement ce rôle — éliminer les biais émotionnels en automatisant l'exécution dès validation du signal Belkhayate.
*Catégorie : psychologie*

### D8069 — Stratégie de diversification : marchés non corrélés
🟡 **SYNTHÈSE** (Source : risk_management.md) : La diversification efficace requiert une faible corrélation entre les marchés. Des marchés fortement corrélés (ex : ES, NQ, YM) ne réduisent pas le risque même si on trade différents contrats — ils bougent tous dans la même direction.
**TRADEX-AI C7** : GC (or) et CL (pétrole) ont des corrélations variables avec ES — la matrice correlations.py surveille ces corrélations live pour éviter les concentrations de risque non voulues.
*Catégorie : correlations*

### D8070 — Plan de gestion du risque : intégration dans la stratégie globale
🟡 **SYNTHÈSE** (Source : risk_management.md) : La gestion du risque n'existe pas en isolation — elle est au cœur de toute stratégie de trading bien structurée. Un plan de trading sans règles de risque explicites n'est pas complet.
**TRADEX-AI C1** : La grille /10 de TRADEX intègre la gestion du risque dans chaque décision : score ≥ 7,0 + aucun critère éliminatoire + R/R ≥ 1:2 — les trois conditions sont simultanément requises.
*Catégorie : gestion_risque_entree*
