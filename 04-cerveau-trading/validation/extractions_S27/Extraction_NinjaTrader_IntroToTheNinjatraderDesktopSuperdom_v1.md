# Extraction NinjaTrader — Intro to the NinjaTrader Desktop SuperDOM
**Source :** `bundles/ninjatrader/intro_to_the_ninjatrader_desktop_superdom.md` (HTTP 200) + 0 images certifiées
**Méthode images :** références à Figure 1/2/3/4 dans le bundle mais images non incluses · 0/0 certifiées · 0 à vérifier
**Décisions :** D7911 → D7930 · **Page :** https://ninjatrader.com/futures/blogs/intro-to-the-ninjatrader-desktop-superdom/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le SuperDOM est l'interface d'exécution d'ordres NT8 utilisée par TRADEX-AI via ATI (port 36973) en mode Auto ; comprendre sa structure valide l'architecture d'exécution.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| Figure 1 (non incluse) | SuperDOM — points de navigation généraux | Navigation | D7911 |
| Figure 2 (non incluse) | SuperDOM — proximité de prix pour placement d'ordres | Placement ordres | D7914 |
| Figure 3 (non incluse) | SuperDOM — dialogue ATM personnalisé | ATM | D7917 |
| Figure 4 (non incluse) | SuperDOM — fonctions de personnalisation | Customisation | D7920 |

## DÉCISIONS

### D7911 — SuperDOM : structure à 3 colonnes
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le SuperDOM (Depth of Market) de NinjaTrader Desktop est organisé en 3 colonnes actives en temps réel : colonne Buy (taille bid disponible à chaque prix), colonne Price (dernier prix négocié + taille, prix moyen position ouverte, bid interne en bleu, ask interne en vert), colonne Sell (taille ask disponible à chaque prix).
**TRADEX-AI C2** : Le SuperDOM est la fenêtre de profondeur de marché que TRADEX-AI surveille via NT8 ATI ; la colonne Price expose les données de depth of market alimentant le cercle C2 (order flow).
*Catégorie : volume_liquidite*

### D7912 — SuperDOM : affichage du prix moyen de position
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le SuperDOM affiche le prix moyen de la position ouverte en brun dans la colonne Price.
**TRADEX-AI C2** : En mode Auto, TRADEX-AI peut lire le prix moyen de position depuis le SuperDOM via NT8 pour calculer le P&L flottant et décider d'un ajustement de stop.
*Catégorie : gestion_position_active*

### D7913 — SuperDOM : paramètres de saisie d'ordre obligatoires
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Avant de placer un ordre dans le SuperDOM, 4 paramètres doivent être sélectionnés : instrument/symbole, quantité de contrats, compte, durée de l'ordre (day order ou GTC — good till cancel).
**TRADEX-AI C1** : L'architecture ATI de TRADEX-AI (port 36973) doit fournir ces 4 paramètres pour chaque ordre en mode Auto ; la durée GTC est obligatoire pour les positions overnight.
*Catégorie : gestion_risque_entree*

### D7914 — SuperDOM : placement d'ordres limite et stop par clic
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Dans le SuperDOM, les ordres limite se placent avec le bouton gauche de la souris (LMB) et les ordres stop avec le bouton central (CWB). Les règles de placement par rapport au prix courant sont : Buy Stop (au-dessus du prix courant, colonne Buy, CWB) ; Buy Limit (en dessous du prix courant, colonne Buy, LMB) ; Sell Limit (au-dessus du prix courant, colonne Sell, LMB) ; Sell Stop (en dessous du prix courant, colonne Sell, CWB).
**TRADEX-AI C1** : En mode Auto via ATI, TRADEX-AI génère des ordres limite ou stop selon la direction du signal Belkhayate ; ces règles de prix relatif doivent être respectées pour éviter les fills immédiats involontaires.
*Catégorie : gestion_risque_entree*

### D7915 — SuperDOM : risque de fill immédiat si mauvais côté
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Si un ordre est placé au mauvais niveau de prix ou du mauvais côté du carnet, il peut être exécuté immédiatement (fill immédiat non souhaité).
**TRADEX-AI C1** : Garde-fou TRADEX-AI : avant transmission d'un ordre via ATI, vérifier que le prix de l'ordre est du bon côté du spread courant selon le type d'ordre (limit/stop) ; un circuit breaker doit intercepter les ordres incohérents.
*Catégorie : gestion_risque_entree*

### D7916 — SuperDOM : annulation et modification d'ordres
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Pour annuler un ordre dans le SuperDOM : cliquer sur le X dans la barre d'ordre. Pour déplacer un ordre (cancel and replace) : cliquer une fois sur la barre d'ordre pour la sélectionner, puis cliquer sur un nouveau prix.
**TRADEX-AI C1** : L'interface ATI de TRADEX-AI doit implémenter les fonctions cancel et cancel/replace pour modifier les stops et targets en mode Auto si les conditions de marché changent.
*Catégorie : gestion_position_active*

### D7917 — ATM Strategies : gestion automatisée de position
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le SuperDOM supporte les ATM (Advanced Trade Management) strategies qui génèrent automatiquement des brackets OCO (one-cancels-the-other), trailing stops et ordres personnalisés lors de l'entrée en position.
**TRADEX-AI C1** : En mode Auto, TRADEX-AI utilise les ATM strategies NT8 pour attacher automatiquement stop loss et profit target à chaque ordre d'entrée ; cette architecture est verrouillée dans les décisions de conception.
*Catégorie : gestion_position_active*

### D7918 — ATM : objectif de better risk management
🔵 **ÉCOLE** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Les ATM strategies sont conçues pour aider à mieux gérer le risque et apporter plus de flexibilité lors du placement d'ordres complexes.
**TRADEX-AI C1** : L'utilisation obligatoire des ATM strategies en mode Auto est une sécurité fondamentale de TRADEX-AI : aucun ordre en mode Auto ne doit être envoyé sans bracket ATM stop loss/target attaché.
*Catégorie : gestion_risque_entree*

### D7919 — SuperDOM : customisation des colonnes de données
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le SuperDOM est hautement personnalisable : il est possible d'ajouter des colonnes de données supplémentaires comme P&L de position, profil de volume au prix (Volume at Price Profile), et une colonne de notes.
**TRADEX-AI C2** : Le Volume at Price Profile dans le SuperDOM est une source complémentaire de données C2 (order flow) pour TRADEX-AI ; il indique les niveaux de liquidité concentrée.
*Catégorie : volume_liquidite*

### D7920 — SuperDOM : fonctionnalités avancées de customisation
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Personnalisations avancées disponibles : quick-click buttons pour saisie d'ordre plus rapide et flexible, affichage des valeurs d'indicateurs (daily high/low markers), indicateur VWAP.
**TRADEX-AI C2** : Le VWAP affiché dans le SuperDOM est un proxy institutionnel de C2 ; dans TRADEX-AI, il sert de niveau de référence pour évaluer si le prix est au-dessus ou en dessous de la valeur institutionnelle intraday.
*Catégorie : volume_liquidite*

### D7921 — VWAP dans le SuperDOM
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le VWAP (Volume Weighted Average Price) peut être affiché comme indicateur dans le SuperDOM.
**TRADEX-AI C2** : Le VWAP est un indicateur clé du cercle C2 de TRADEX-AI ; prix au-dessus du VWAP = biais institutionnel haussier intraday ; en dessous = biais baissier. Cet indicateur renforce ou affaiblit le score C2.
*Catégorie : volume_liquidite*

### D7922 — SuperDOM : vue en une fenêtre de la profondeur de marché
🔵 **ÉCOLE** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Un des avantages clés du SuperDOM est sa vue en une seule fenêtre de la profondeur de marché en temps réel, en contexte avec les ordres et positions actifs.
**TRADEX-AI C2** : La lecture de la profondeur de marché (DOM) en temps réel via NT8 est la source principale du cercle C2 (order flow) de TRADEX-AI ; la structure bid/ask visible dans le SuperDOM est captée par le data_reader.py.
*Catégorie : volume_liquidite*

### D7923 — SuperDOM : précision de saisie évitant les erreurs de prix
🔵 **ÉCOLE** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : L'interface point-and-click du SuperDOM est rapide et précise et aide à éviter de coûteuses erreurs de saisie de prix.
**TRADEX-AI C1** : En mode Manuel, Abdelkrim utilise le SuperDOM pour confirmer et saisir les ordres suggérés par TRADEX-AI ; la précision point-and-click réduit le risque d'erreur de saisie.
*Catégorie : psychologie*

### D7924 — SuperDOM : application automatique de règles de gestion des risques
🔵 **ÉCOLE** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Avec le SuperDOM, les traders peuvent appliquer automatiquement des stratégies de gestion des risques ou d'autres règles complexes lors du placement des ordres.
**TRADEX-AI C1** : L'architecture TRADEX-AI exploite cette capacité : en mode Auto, les règles de risk management Belkhayate (taille position, stop, target) sont encodées dans les ATM strategies et appliquées automatiquement à chaque ordre.
*Catégorie : gestion_risque_entree*

### D7925 — SuperDOM : interface point-and-click
🔵 **ÉCOLE** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Le SuperDOM est décrit comme "price ladder" ou "trading ladder" ; son interface point-and-click est l'une des plus populaires parmi les traders actifs.
**TRADEX-AI C1** : En mode Manuel, le SuperDOM est l'outil de saisie recommandé pour Abdelkrim ; TRADEX-AI affiche le signal et les niveaux (entrée, stop, target), Abdelkrim clique dans le SuperDOM pour exécuter.
*Catégorie : psychologie*

### D7926 — ATM : trailing stop et breakeven automatiques
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Les ATM strategies supportent les trailing stops automatiques et le déplacement au breakeven.
**TRADEX-AI C1** : TRADEX-AI peut configurer un trailing stop ATM pour sécuriser les gains en mode Auto ; le déplacement au breakeven est une règle de gestion de position active (garde-fou G15 ou équivalent).
*Catégorie : gestion_position_active*

### D7927 — ATM : sortie en plusieurs niveaux (scale out)
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Les ATM strategies permettent de scaler out d'une position à différents niveaux de prix (plusieurs niveaux de profit target et de stop loss).
**TRADEX-AI C1** : Le scale out à différents niveaux de prix est une technique compatible avec la méthode Belkhayate ; TRADEX-AI peut encoder plusieurs niveaux de sortie dans l'ATM strategy pour optimiser le R/R global.
*Catégorie : gestion_position_active*

### D7928 — ATM : applicable à toute quantité de contrats
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : Les ATM strategies sont versatiles et peuvent être modifiées pour s'adapter à des trades de n'importe quelle quantité, avec autant de niveaux de stop et de target que requis.
**TRADEX-AI C1** : La flexibilité des ATM strategies NT8 valide leur usage pour toute taille de position calculée par le risk_manager.py de TRADEX-AI, qu'il s'agisse de 1 ou plusieurs contrats.
*Catégorie : gestion_position_active*

### D7929 — SuperDOM : affichage du dernier prix négocié avec taille
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : La colonne Price du SuperDOM affiche le dernier prix négocié en jaune avec la taille du trade (last traded price + size).
**TRADEX-AI C2** : Le last traded price + size visible dans le SuperDOM est une donnée d'order flow de base pour le cercle C2 ; combiné au delta ATAS, il confirme la pression directionnelle.
*Catégorie : volume_liquidite*

### D7930 — Stratégies ATM préconfigurées et personnalisables
🟢 **FAIT VÉRIFIÉ** (Source : intro_to_the_ninjatrader_desktop_superdom.md) : NT8 fournit plusieurs ATM strategies préconfigurées pouvant être personnalisées pour n'importe quel scénario de trading.
**TRADEX-AI C1** : TRADEX-AI utilise des ATM strategies personnalisées par actif (GC, HG, CL, ZW) tenant compte de la volatilité propre à chaque marché pour dimensionner les stops et targets conformément à la méthode Belkhayate.
*Catégorie : gestion_position_active*
