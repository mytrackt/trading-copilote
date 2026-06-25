# Extraction NinjaTrader — How To Use The SuperDOM Price Ladder For Order Entry
**Source :** `bundles/ninjatrader/how_to_use_the_superdom_price_ladder_for_order_entry.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7851 → D7860 · **Page :** https://ninjatrader.com/futures/blogs/how-to-use-the-superdom-price-ladder-for-order-entry/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : SuperDOM NT8 = interface de saisie d'ordres + Level II (depth of market) pour le mode Manuel ; complément visuel au moteur de signaux TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D7851 — Définition SuperDOM : price ladder interactif avec market depth (Level II)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Le SuperDOM (DOM = Depth of Market, aussi appelé Level II ou order book) est une interface de price ladder qui affiche la profondeur de marché en temps réel. Il permet de soumettre et modifier des ordres, gérer des positions et des stratégies de sortie/stop discrétionnaires, tout en surveillant les données d'order book (bids et offers en attente).
**TRADEX-AI C2** : Le SuperDOM est la source de données Level II pour le moteur TRADEX. La profondeur de marché visible dans le SuperDOM (bids/offers, volumes à chaque niveau) complète les données footprint et delta cumulatif pour l'analyse C2 order flow.
*Catégorie : volume_liquidite*

### D7852 — SuperDOM : interface unifiée pour ordres + positions + stratégies d'exit
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Le SuperDOM fournit une fonctionnalité complète pour : (1) soumettre et modifier des ordres, (2) surveiller les données d'order book (bids et offers), (3) gérer des positions et stratégies discrétionnaires de sortie et stop. Tout dans une interface hautement visuelle.
**TRADEX-AI C1** : Pour le mode Manuel TRADEX — Abdelkrim utilisera le SuperDOM NT8 pour exécuter les signaux affichés par le dashboard TRADEX. Le guide utilisateur doit documenter le workflow : signal TRADEX → validation Abdelkrim → entrée via SuperDOM.
*Catégorie : gestion_position_active*

### D7853 — Order placement souris : stop limit (middle click), stop market (CTRL+middle), MIT (CTRL+left)
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Dans le SuperDOM, les ordres se placent via raccourcis souris sur le price ladder : Stop Limit Order = middle click sur le prix désiré (au-dessus du marché pour buy, en-dessous pour sell) + saisie de l'offset + validation. Stop Market Order = CTRL + middle click. MIT (Market If Touched) = CTRL + left click dans la cellule adjacente au prix (en-dessous du marché pour buy, au-dessus pour sell).
**TRADEX-AI C1** : Ces raccourcis sont fondamentaux pour la rapidité d'exécution en mode Manuel. Le guide utilisateur TRADEX doit inclure un récapitulatif de ces raccourcis pour permettre à Abdelkrim d'exécuter rapidement après réception du signal.
*Catégorie : gestion_risque_entree*

### D7854 — Méthode click-then-click : modification d'ordres précise à la volée
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : La méthode "click-then-click" permet d'ajuster les ordres avec précision : un premier clic sélectionne l'ordre actif dans le SuperDOM, puis on déplace la souris au nouveau niveau de prix et on reclique pour repositionner l'ordre.
**TRADEX-AI C1** : Cette méthode est utile pour ajuster rapidement les stops/targets en mode Manuel si les conditions de marché évoluent après l'entrée. À documenter dans le guide utilisateur TRADEX comme technique de modification rapide post-entrée.
*Catégorie : gestion_position_active*

### D7855 — Annulation d'ordres : par ordre individuel ou annulation globale buy/sell
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Annulation d'ordre individuel : cliquer le X à gauche de l'ordre (côté buy) ou à droite (côté sell). Annulation de tous les ordres actifs d'un côté : cliquer le X adjacent aux boutons quick "Market" en bas du price ladder.
**TRADEX-AI C1** : Fonctionnalité d'urgence critique pour le mode Manuel. En cas d'annulation rapide nécessaire (news gate déclenché, circuit breaker), Abdelkrim peut annuler tous les ordres pendants en un clic. À documenter dans le guide utilisateur avec un avertissement prioritaire.
*Catégorie : gestion_risque_entree*

### D7856 — Surveillance de l'order book : bids et offers en temps réel autour du dernier prix
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Le SuperDOM permet de surveiller les données d'order book — changements dans les bids et offers autour du dernier prix échangé — en temps réel. Cette visibilité sur la profondeur de marché complète l'analyse technique classique.
**TRADEX-AI C2** : La profondeur de marché visible dans le SuperDOM (density des bids/offers à chaque niveau) est une donnée C2 complémentaire. Des clusters de bids/offers sur des niveaux clés confirment les zones de liquidité identifiées par l'analyse VP + delta.
*Catégorie : volume_liquidite*

### D7857 — SuperDOM : interface conçue pour tous niveaux, du novice à l'expert
🔵 **ÉCOLE** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Le SuperDOM fait partie de la suite NT8 conçue pour être utilisée par tous les niveaux de traders. Les workspaces, charts, templates, watch lists et autres éléments sont personnalisables selon le style et l'approche de trading.
**TRADEX-AI C1** : Pour TRADEX en mode Manuel — configurer un workspace NT8 dédié avec SuperDOM + footprint + VP + cumul delta dans une disposition fixe. Ce workspace doit être documenté et sauvegardé comme template dans le guide utilisateur pour Abdelkrim.
*Catégorie : configuration*

### D7858 — F1 comme raccourci vers le Help Guide NT8 contextuel
🔵 **ÉCOLE** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : La touche F1 dans NT8 ouvre le Help Guide correspondant à la dernière fenêtre utilisée dans la plateforme — aide contextuelle intégrée.
**TRADEX-AI C1** : Raccourci de support rapide pour Abdelkrim. Documenter dans le guide utilisateur TRADEX : F1 sur le SuperDOM ouvre l'aide SuperDOM, F1 sur le chart ouvre l'aide chart. Permet une autonomie de dépannage sans quitter la plateforme.
*Catégorie : configuration*

### D7859 — Market orders via quick buttons en bas du SuperDOM
🟢 **FAIT VÉRIFIÉ** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Les ordres marché dans le SuperDOM peuvent être passés via les quick buttons situés en bas de l'affichage — en plus des méthodes de clic direct sur le price ladder.
**TRADEX-AI C1** : Les quick buttons Market sont les boutons d'exécution rapide pour le mode Manuel TRADEX. Quand le signal TRADEX est validé par Abdelkrim, l'exécution se fait par ces boutons ou via click sur le price ladder selon la précision de prix souhaitée.
*Catégorie : gestion_risque_entree*

### D7860 — SuperDOM comme outil complémentaire au moteur de signaux TRADEX
🟡 **SYNTHÈSE** (Source : how_to_use_the_superdom_price_ladder_for_order_entry.md) : Le SuperDOM NT8 est une interface d'exécution et de surveillance de l'order book qui fonctionne en complément des outils analytiques (footprint, VP, cumul delta). En mode Manuel, il est le point de jonction entre l'analyse générée par TRADEX-AI et l'exécution humaine par l'utilisateur.
**TRADEX-AI C1/C2** : Synthèse architecturale TRADEX — le workflow mode Manuel est : (1) Python détecte opportunité → (2) Claude génère signal → (3) Dashboard affiche signal à Abdelkrim → (4) Abdelkrim valide sur SuperDOM NT8 → (5) ATM strategy prend le relais pour la gestion. Le SuperDOM est le maillon humain de la chaîne.
*Catégorie : configuration*
