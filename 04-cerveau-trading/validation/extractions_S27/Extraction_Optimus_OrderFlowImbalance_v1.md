# Extraction Optimus — Order Flow Imbalance
**Source :** `bundles/optimusfutures/order_flow_imbalance.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image extractible dans ce bundle (scénarios DOM référencés comme images mais non embarqués) · 0/0 certifiées · 0 à vérifier
**Décisions :** D8611 → D8630 · **Page :** https://optimusfutures.com/blog/order-flow-imbalance/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : détection des imbalances Order Flow = signal C2 clé pour confirmer entrées sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Scénarios DOM simulés en texte (spreadsheet hypothétique) — pas d'images extractibles | — | — |

## DÉCISIONS

### D8611 — Définition de l'Order Flow Imbalance
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : L'Order Flow Imbalance (déséquilibre de flux d'ordres) survient quand il existe une différence substantielle entre le nombre d'ordres acheteurs et vendeurs pour un actif. Un côté domine l'autre de façon significative. C'est le moteur fondamental des mouvements de prix à court terme.
**TRADEX-AI C2** : L'imbalance est le signal C2 primaire dans TRADEX. Quand buy orders >> sell orders sur GC/HG/CL/ZW, c'est un signal de pression haussière quantifiable via ATAS footprint.
*Catégorie : volume_liquidite*

### D8612 — Imbalance DOM : structure Bid-Ask 3 colonnes
🔵 **ÉCOLE** (Source : order_flow_imbalance.md) : Un DOM affiche 3 colonnes : (gauche) Bid — ordres limite d'achat en vert avec leur quantité par niveau de prix ; (milieu) les prix ; (droite) Ask — ordres limite de vente en rouge. 10 niveaux Bid et 10 niveaux Ask visibles. Le prix surligné en bleu = dernier prix exécuté.
**TRADEX-AI C2** : Structure DOM standard NT8 / ATAS. Les quantités Bid et Ask dans cette grille alimentent le calcul de pression nette pour le score C2 du moteur TRADEX.
*Catégorie : volume_liquidite*

### D8613 — Market Orders = seuls créateurs d'imbalance et de mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Les ordres limites (Bid/Ask) seuls ne créent pas de mouvement de prix — ils sont statiques. C'est l'arrivée d'un Market Order qui absorbe les ordres limites et crée l'imbalance qui déplace le prix. Sans Market Order, aucun trade ne se produit.
**TRADEX-AI C2** : Règle clé : surveiller l'arrivée de Market Orders agressifs (Big Trades ATAS) et non la taille des ordres limites passifs. Un "wall" de Bid ne garantit pas le support — il peut être contourné par des ventes massives au marché.
*Catégorie : volume_liquidite*

### D8614 — Imbalance haussière : Buy Market Orders > Sell Limit Orders disponibles
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Scénario haussier concret : 1000 Market Buy Orders vs 290 ordres limites de vente au meilleur Ask → les 290 se font absorber instantanément, les 710 restants montent au niveau d'Ask suivant (843 contrats disponibles) → le prix monte d'un tick. Mécanisme en cascade.
**TRADEX-AI C2** : Ce scénario est le cas typique de signal C2 haussier sur GC/CL. ATAS detects la séquence d'absorption en temps réel via le delta cumulé et les imbalances footprint.
*Catégorie : volume_liquidite*

### D8615 — Imbalance baissière : cascade de liquidation sur 8 niveaux de prix
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Scénario baissier : 7000 Market Sell Orders arrivent alors que le meilleur Bid est à 203 contrats. Les 7000 ventes absorbent 8 niveaux de prix de Bids successifs, faisant chuter le prix de 2168.00 à 2166.25 (6 ticks de baisse). Plus l'imbalance est grande, plus la chute est rapide et profonde.
**TRADEX-AI C2** : Ce scénario (catalysé par un rapport économique négatif) est couvert par le News Gate TRADEX (C4). Pendant NFP/FOMC : book thin + imbalances potentielles massives = blocage automatique des signaux.
*Catégorie : macro_evenements*

### D8616 — Anticiper la direction via l'imbalance : Buy > Sell = momentum haussier
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Une imbalance significative où les ordres acheteurs dépassent largement les vendeurs indique souvent un mouvement de prix imminent dans la direction de l'imbalance. Une forte imbalance Buy-side = signal de momentum haussier. Une forte imbalance Sell-side = momentum baissier.
**TRADEX-AI C2** : Règle de signal C2 dans TRADEX : imbalance buy-side significative sur GC/HG/CL/ZW, confirmée par C1 (direction Belkhayate) = signal valide. Une seule imbalance isolée sans confirmation C1 est insuffisante.
*Catégorie : gestion_risque_entree*

### D8617 — Scalping sur imbalances de court terme
🟡 **SYNTHÈSE** (Source : order_flow_imbalance.md) : Les scalpers peuvent exploiter les petites imbalances temporaires en achetant au Bid et vendant à l'Ask dans des marchés très liquides et volatils. Cela nécessite une exécution très rapide et une compréhension fine du spread. Pas approprié pour tous les traders.
**TRADEX-AI C2** : TRADEX n'est pas conçu pour le scalping pur (latence Python + Claude trop élevée). Le mode Auto vise des mouvements de plus grande amplitude. Le scalping sur imbalances reste une approche manuelle pour Abdelkrim en mode Manuel.
*Catégorie : configuration*

### D8618 — Statistical Arbitrage sur imbalances
🟡 **SYNTHÈSE** (Source : order_flow_imbalance.md) : Des modèles sophistiqués peuvent identifier des relations statistiques entre les imbalances d'order flow et les mouvements de prix futurs. Les patterns historiques d'imbalance peuvent être utilisés pour estimer la probabilité d'un mouvement directionnel.
**TRADEX-AI C7** : Le module correlations.py pourrait à terme intégrer des statistiques d'imbalance historiques pour pondérer les signaux C2. Ticket d'enrichissement potentiel KB pour une session future.
*Catégorie : correlations*

### D8619 — Footprint charts : outil principal pour visualiser les imbalances
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Le footprint chart (Cluster Chart) permet de lire les imbalances order flow en analysant les volumes exécutés. Sur chaque footprint : Bid exécutés (gauche) × Ask exécutés (droite), appariés diagonalement. Un ratio proche de 100% = équilibre. Un ratio très éloigné = imbalance.
**TRADEX-AI C2** : ATAS footprint (Numbers Bars) est l'outil C2 primaire de TRADEX pour cette lecture. data_reader.py doit extraire les colonnes Bid Volume et Ask Volume par niveau de prix.
*Catégorie : volume_liquidite*

### D8620 — Lecture diagonale du footprint pour détecter l'imbalance
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Dans un footprint, on apparie diagonalement le Bid exécuté d'un niveau avec le Ask exécuté du niveau adjacent (un tick au-dessus). Si Ask >> Bid (ex. 194 vs 31 = 625%), l'imbalance est surlignée en rouge (pression baissière). Si Bid >> Ask (ex. 444%), surlignée en vert (pression haussière).
**TRADEX-AI C2** : Règle d'implémentation pour TRADEX : le ratio diagonal imbalance ATAS doit être >= 300% pour constituer un signal C2 valide. En dessous, considérer le marché équilibré.
*Catégorie : volume_liquidite*

### D8621 — Seuil d'imbalance significatif : configurable selon l'actif
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Le niveau d'imbalance "significatif" est subjectif et dépend des tendances historiques de l'actif concerné. Un seuil de 300% est un exemple courant — seules les imbalances >= 300% sont surlignées. Ce paramètre doit être calibré par actif.
**TRADEX-AI C2** : Action TRADEX : calibrer le seuil d'imbalance ATAS séparément pour GC, HG, CL, ZW. La volatilité naturelle de chaque actif impose des seuils différents (ex. CL plus volatile que ZW).
*Catégorie : configuration*

### D8622 — Imbalance vente massive → cascade de baisse observable sur footprint
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Sur un footprint chart, une succession de niveaux avec forte imbalance vente (rouge) peut représenter une cascade de liquidation. Les pourcentages d'imbalance sur chaque niveau permettent de quantifier l'intensité de la pression vendeuse et anticiper la profondeur potentielle du mouvement.
**TRADEX-AI C2** : Dans TRADEX, une cascade d'imbalances rouges successives sur 3+ niveaux de prix = signal baissier C2 fort. Si C1 est aussi baissier (Belkhayate direction) → score += signal valide.
*Catégorie : volume_liquidite*

### D8623 — Imbalance = indicateur de pression directionnelle (pas de certitude)
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : L'imbalance d'order flow donne une indication de la pression directionnelle actuelle — bullish ou bearish. Mais elle ne garantit pas la direction. Les market orders à venir restent inconnus. L'imbalance actuelle informe le biais directionnel, pas le résultat.
**TRADEX-AI C2** : Intégration dans la grille de score TRADEX : le signal C2 (imbalance) est un facteur parmi 7. Il augmente la probabilité (score +) mais ne décide pas seul. Seuil global 7/10 requis avec aucun critère éliminatoire.
*Catégorie : gestion_risque_entree*

### D8624 — DOM comme "order book" : simulation de scénarios pour comprendre l'impact
🔵 **ÉCOLE** (Source : order_flow_imbalance.md) : Pour comprendre l'impact d'un gros ordre, il est utile de transposer le DOM dans un tableau et simuler l'absorption niveau par niveau. Exercice pédagogique qui développe l'intuition sur la profondeur du marché et la résistance des niveaux de prix.
**TRADEX-AI C2** : Exercice de formation recommandé pour Abdelkrim en mode Manuel : simuler des scénarios DOM sur ES/GC pour développer l'intuition avant de trader avec TRADEX en mode Auto.
*Catégorie : psychologie*

### D8625 — Spread Bid-Ask étroit = liquidité = 1 tick sur marchés liquides
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Sur un DOM ES (E-Mini S&P 500), le spread entre meilleur Ask et meilleur Bid est typiquement de 0.25 point = 1 tick. Ce spread étroit confirme la haute liquidité du marché. Un spread de plus d'1 tick sur ES signale une condition anormale.
**TRADEX-AI C4** : Pour les actifs TRADEX : GC spread normal = 10 cents (1 tick), CL = $0.01 (1 tick), ZW = 0.25 cents (1 tick). Le staleness_monitor.py doit détecter les spreads anormaux comme indicateur de liquidité dégradée.
*Catégorie : volume_liquidite*

### D8626 — Rôle de "liquidity provider" pour traders institutionnels
🟡 **SYNTHÈSE** (Source : order_flow_imbalance.md) : Un trader avec capital important peut se positionner comme "liquidity provider" lors d'une imbalance en prenant le côté opposé et profitant du spread. Cette approche n'est réaliste que pour les institutionnels ou gros traders retail. Pour les traders individuels, c'est hors portée.
**TRADEX-AI C3** : Lien C3 : les institutionnels qui fournissent de la liquidité lors des imbalances sont visibles dans les données COT hebdomadaires (Commercial positions). Une réduction soudaine de leur exposition = signal C3 à surveiller.
*Catégorie : volume_liquidite*

### D8627 — Lecture des imbalances : information passée uniquement
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : L'analyse de l'imbalance à partir des order book data travaille toujours avec de l'information passée — on ne peut voir que les ordres limites déjà placés, pas les market orders qui vont arriver. C'est une limitation fondamentale : on lit le passé et le présent, pas l'avenir.
**TRADEX-AI C2** : Limite fondamentale intégrée dans l'architecture TRADEX : le signal C2 est probabiliste et non prédictif. Il pondère le score global mais ne peut pas anticiper un retournement brutal provoqué par des market orders inattendus.
*Catégorie : gestion_risque_entree*

### D8628 — Footprint vs DOM : complémentarité pour la lecture complète de l'imbalance
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_imbalance.md) : Le DOM montre les ordres en attente (future liquidity), le footprint montre les ordres exécutés (historical pressure). Utiliser les deux ensemble donne la vision la plus complète : où se trouve la liquidité future ET quelle était la pression récente.
**TRADEX-AI C2** : Règle d'architecture TRADEX : data_reader.py doit intégrer les deux flux ATAS : (1) DOM data (liquidité disponible) + (2) Footprint/Numbers Bars data (volume exécuté par niveau). Signal C2 = croisement des deux.
*Catégorie : volume_liquidite*

### D8629 — Imbalance comme filtre de momentum (achat dans tendance)
🟡 **SYNTHÈSE** (Source : order_flow_imbalance.md) : Une forte imbalance Buy-side peut indiquer un momentum haussier et inciter les traders à acheter en anticipation de la poursuite du mouvement. De même, une Sell imbalance indique un momentum baissier. Ces imbalances peuvent être utilisées pour filtrer les entrées dans le sens de la tendance.
**TRADEX-AI C2** : Application TRADEX : C2 (imbalance Buy) + C1 (direction Belkhayate haussière) = score += +1 sur la grille /10. La convergence des deux cercles renforce la confiance du signal.
*Catégorie : gestion_risque_entree*

### D8630 — Conditions illiquides et imbalances : interprétation différente
🟡 **SYNTHÈSE** (Source : order_flow_imbalance.md) : En marché illiquide (hors heures, pre-market, pendant news), les imbalances sont artificiellement amplifiées — même un petit ordre marché peut créer une grande imbalance apparente. Ces imbalances en conditions illiquides ne doivent pas être interprétées comme des signaux fiables.
**TRADEX-AI C2** : Garde-fou TRADEX : le staleness_monitor.py doit qualifier la liquidité avant de transmettre les données ATAS au claude_brain.py. En condition illiquide → C2 marqué comme "non fiable" → score C2 = 0 (neutralisé).
*Catégorie : gestion_risque_entree*
