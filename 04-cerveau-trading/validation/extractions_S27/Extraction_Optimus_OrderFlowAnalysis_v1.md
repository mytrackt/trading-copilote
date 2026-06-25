# Extraction Optimus — Order Flow Analysis
**Source :** `bundles/optimusfutures/order_flow_analysis.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image extractible dans ce bundle (figures référencées mais non embarquées) · 0/0 certifiées · 0 à vérifier
**Décisions :** D8591 → D8610 · **Page :** https://optimusfutures.com/blog/order-flow-analysis/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : fondamentaux DOM + Cluster Charts = colonne vertébrale du cercle C2 (Order Flow) dans TRADEX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Figures DOM/Cluster référencées dans le texte, non extractibles en tant qu'images statiques | — | — |

## DÉCISIONS

### D8591 — Définition de l'Order Flow Analysis
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : L'Order Flow Analysis est une méthode d'analyse qui examine la séquence des transactions en temps réel pour déterminer comment elles influencent les prix à court terme. Elle est distincte de l'analyse technique et fondamentale classiques, et n'est possible qu'avec les outils numériques modernes.
**TRADEX-AI C2** : L'Order Flow Analysis est le fondement du cercle C2 de TRADEX. Les données ATAS (footprint, delta, big trades) sont la mise en oeuvre concrète de cette méthode sur NinjaTrader 8.
*Catégorie : structure_marche*

### D8592 — DOM : ordres limites en attente (vue forward-looking)
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Le DOM (Depth of Market) affiche les ordres limites en attente d'exécution — c'est une vue "future" des intentions d'achat/vente. Il montre où les participants veulent acheter ou vendre mais n'ont pas encore exécuté.
**TRADEX-AI C2** : Le DOM fourni par NinjaTrader 8 via le SuperDOM est la source primaire de liquidité visible pour TRADEX. Données accessibles via NT8 SuperDOM et/ou ATAS.
*Catégorie : volume_liquidite*

### D8593 — Cluster Charts : transactions déjà exécutées (vue backward-looking)
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Les Cluster Charts (aussi appelés footprint charts ou Numbers Bars) affichent les transactions déjà exécutées à chaque niveau de prix. C'est une vue "passé" qui révèle où et en quelle quantité les ordres ont été remplis.
**TRADEX-AI C2** : Le footprint ATAS est la mise en oeuvre des Cluster Charts dans TRADEX. data_reader.py doit lire les données de delta/bid-ask volume par niveau de prix depuis les exports ATAS.
*Catégorie : volume_liquidite*

### D8594 — Prix courant = meilleur Bid OU meilleur Ask
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Le prix courant (Current Price) est le dernier prix auquel un trade a eu lieu — soit au meilleur Bid (Best Bid), soit au meilleur Ask (Best Ask). Le petit triangle noir dans un DOM indique de quel côté la dernière transaction a eu lieu.
**TRADEX-AI C2** : Information micro-structure directement lisible depuis NT8 SuperDOM. Indique la pression instantanée acheteurs/vendeurs pour les actifs TRADING (GC/HG/CL/ZW).
*Catégorie : volume_liquidite*

### D8595 — Ordres marchés vs ordres limites : mécanique fondamentale
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Aucun trade ne se produit jusqu'à ce qu'un Market Order arrive. Les Limit Orders attendent passivement. Un Buy Market Order se remplit contre les Sell Limit Orders au meilleur Ask. Un Sell Market Order se remplit contre les Buy Limit Orders au meilleur Bid. Cette mécanique est universelle sur tous les marchés de futures.
**TRADEX-AI C2** : Règle fondamentale de micro-structure intégrée dans la logique d'interprétation du delta ATAS. Un delta positif = plus de Market Buy que de Market Sell sur la période.
*Catégorie : volume_liquidite*

### D8596 — Spread Bid-Ask = indicateur de liquidité
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Un spread étroit entre meilleur Bid et meilleur Ask = marché liquide. Un spread large = marché illiquide. Sur les futures standardisées (GC, ES, CL), le spread est presque toujours de 1 tick en conditions normales car de nouveaux ordres limites s'ajoutent immédiatement après chaque mouvement.
**TRADEX-AI C4** : Le staleness_monitor.py doit surveiller l'élargissement du spread comme indicateur de conditions illiquides (avant news, hors heures de trading actif). Signal de blocage si spread anormal.
*Catégorie : volume_liquidite*

### D8597 — Bid Volume vs Ask Volume dans les Cluster Charts
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Dans un Cluster Chart, chaque niveau de prix affiche : Bid Volume (contrats vendus au marché quand ce prix était le meilleur Bid) × Ask Volume (contrats achetés au marché quand ce prix était le meilleur Ask). IMPORTANT : Bid/Ask Volume ≠ Bid/Ask Size. Volume = ordres exécutés. Size = ordres en attente.
**TRADEX-AI C2** : Distinction fondamentale pour l'interprétation ATAS. Le moteur TRADEX doit utiliser les volumes exécutés (Volume), pas les ordres en attente (Size) pour calculer le delta.
*Catégorie : volume_liquidite*

### D8598 — Mouvement de prix d'un tick : absorption complète du meilleur niveau
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Pour que le prix monte d'un tick, il faut que tous les ordres limites de vente au meilleur Ask soient absorbés par des Market Buy Orders. Pour baisser d'un tick, il faut absorber tous les Buy Limit Orders au meilleur Bid. La taille de ces niveaux détermine la résistance au mouvement de prix.
**TRADEX-AI C2** : Concept directement utilisable pour identifier les zones de résistance/support microstructurelle sur GC/CL/ZW via ATAS. Un grand wall de vendeurs au Ask = résistance de court terme.
*Catégorie : structure_marche*

### D8599 — Marchés illiquides : sauts de tick et prix non-tradés
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Dans les marchés peu liquides, le meilleur Bid ou Ask suivant peut être à plusieurs ticks de distance. Le prix peut sauter plusieurs ticks laissant des niveaux de prix sans aucune transaction — zones de "fair value gap" potentielles.
**TRADEX-AI C4** : Pour ZW (Blé) et HG (Cuivre) en dehors des heures de pointe, ce phénomène est plus fréquent. Le staleness_monitor.py doit signaler les conditions illiquides pour ces actifs.
*Catégorie : volume_liquidite*

### D8600 — Retrait des ordres limites pendant les nouvelles économiques
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Lors de publications d'indicateurs économiques importants (NFP, FOMC, CPI), les traders retirent leurs ordres limites. Le book devient "thin" (mince) et le spread peut s'élargir même sur des marchés normalement très liquides pour une très courte durée.
**TRADEX-AI C4** : Confirme et valide le News Gate TRADEX : bloquer les signaux 30 min avant NFP/FOMC/CPI car la micro-structure du marché devient anormale pendant cette période.
*Catégorie : macro_evenements*

### D8601 — Spoofing : manipulation via ordres limites annulés
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Les Bid Sizes et Ask Sizes du DOM changent constamment car des traders ajoutent et annulent des ordres limites. Une partie de ces annulations est légitime ; une autre est du "spoofing" (manipulation visant à créer une illusion de demande/offre).
**TRADEX-AI C2** : Limite du DOM : les grandes quantités visibles au Bid/Ask peuvent être du spoofing. TRADEX ne doit pas baser un signal uniquement sur la taille des ordres DOM — préférer les volumes exécutés (Cluster Charts/ATAS).
*Catégorie : volume_liquidite*

### D8602 — DOM histogramme : visualisation rapide pression achat/vente
🔵 **ÉCOLE** (Source : order_flow_analysis.md) : Le mode histogramme du DOM colore les niveaux Bid et Ask proportionnellement à leur taille relative. Si le Bid (achat) est 2x plus grand que l'Ask (vente), la barre Bid est 2x plus longue. Vue instantanée de la pression nette acheteurs vs vendeurs.
**TRADEX-AI C2** : Fonctionnalité disponible dans NT8 SuperDOM et ATAS. Utile pour une lecture rapide de la pression lors de l'analyse manuelle (mode Manuel TRADEX).
*Catégorie : volume_liquidite*

### D8603 — Imbalance dans les Cluster Charts : seuil de ratio configurable
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Dans les Cluster Charts avancés, une "imbalance" est détectée quand le ratio Ask Volume / Bid Volume (diagonal) dépasse un seuil configurable (ex. 3x = 300%). Colorié en vert si Ask > Bid (pression haussière), rouge si Bid > Ask (pression baissière). Le seuil est ajustable selon l'actif.
**TRADEX-AI C2** : Règle TRADEX : utiliser un seuil d'imbalance d'au moins 300% pour filtrer le bruit. Les imbalances certifiées ATAS avec ratio >= 300% sont des signaux C2 valides. Applicable sur GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D8604 — Volume Profiles superposés aux Numbers Bars
🔵 **ÉCOLE** (Source : order_flow_analysis.md) : Les Numbers Bars (Cluster Charts) peuvent être superposés sur des Volume Profiles pour visualiser simultanément : (1) le volume distribué par niveau de prix (profile) et (2) le détail bid/ask exécuté à chaque tick (cluster). Outil d'analyse combiné.
**TRADEX-AI C2** : Dans ATAS Pro, cette combinaison est disponible nativement. La superposition Numbers Bars + Volume Profile est recommandée pour les analyses C2 sur les actifs TRADEX.
*Catégorie : volume_liquidite*

### D8605 — DOM 10 niveaux : limite de visibilité des ordres en attente
🔵 **ÉCOLE** (Source : order_flow_analysis.md) : Les exchanges futures fournissent généralement 10 niveaux Bid et 10 niveaux Ask dans le DOM standard. Des ordres plus profonds existent mais ne sont pas visibles. Cette limite de visibilité est une contrainte inhérente à l'analyse DOM.
**TRADEX-AI C2** : Limite technique à intégrer dans l'interprétation : les "iceberg orders" et ordres profonds hors des 10 niveaux ne sont pas visibles. Ne jamais conclure à l'absence d'intérêt sur la base du DOM seul.
*Catégorie : volume_liquidite*

### D8606 — Order Flow Analysis = lecture des forces de marché en temps réel
🟡 **SYNTHÈSE** (Source : order_flow_analysis.md) : L'Order Flow Analysis permet de "voir" les forces réelles d'offre et demande en temps réel, via les flux de transactions. Contrairement à l'AT classique (indicateurs lagging) ou à l'AF (données macro lentes), l'OFA est instantanée et reflète ce qui se passe maintenant dans le carnet d'ordres.
**TRADEX-AI C2** : Positionnement clair de C2 dans TRADEX : couche temps réel 2 secondes, la plus rapide des 7 cercles. Les données ATAS reflètent le flux de transactions de la seconde écoulée.
*Catégorie : structure_marche*

### D8607 — Combinaison DOM + Cluster Charts : vue complète
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Pour une analyse Order Flow complète, les deux outils sont nécessaires : (1) DOM pour voir ce qui est en attente (futur proche), (2) Cluster Charts pour analyser ce qui s'est passé (passé immédiat). L'un sans l'autre donne une image incomplète.
**TRADEX-AI C2** : Règle TRADEX : le signal C2 doit intégrer à la fois le delta cumulé (Cluster/ATAS) ET l'état du DOM (NT8 SuperDOM) avant de valider. Un signal C2 basé sur un seul outil est insuffisant.
*Catégorie : gestion_risque_entree*

### D8608 — Acheteurs et vendeurs institutionnels : impact sur le livre d'ordres
🟡 **SYNTHÈSE** (Source : order_flow_analysis.md) : Un trader institutionnel avec 1000 contrats à acheter sur ES absorbe immédiatement plusieurs niveaux d'Ask, déplaçant le prix de plusieurs ticks en quelques millisecondes. Cela crée une imbalance order flow massive momentanée, visible dans le DOM et les Cluster Charts.
**TRADEX-AI C3** : Lien direct avec C3 (Institutionnels). Un Grand Trade détecté par ATAS (Big Trades indicator) sur GC ou CL peut signaler une action institutionnelle à valider avec les données COT hebdomadaires (C3).
*Catégorie : volume_liquidite*

### D8609 — News économiques : retrait massif de liquidité du book
🟢 **FAIT VÉRIFIÉ** (Source : order_flow_analysis.md) : Lors de publications de données économiques importantes, les market makers et traders institutionnels retirent leurs ordres limites préventiquement. Le résultat est une détérioration rapide du book — gaps potentiels et slippage élevé pour les ordres marchés pendant quelques secondes/minutes.
**TRADEX-AI C4** : Double confirmation du News Gate TRADEX : (1) news gate temporel (30 min avant) + (2) surveillance de la densité du book (staleness_monitor.py) pour détecter le retrait de liquidité.
*Catégorie : macro_evenements*

### D8610 — Order Flow = supplément aux deux analyses classiques (TA + FA)
🟡 **SYNTHÈSE** (Source : order_flow_analysis.md) : L'Order Flow Analysis est complémentaire — et non substituable — à l'analyse technique (AT) et fondamentale (AF). L'AT identifie les niveaux clés et patterns ; l'AF donne le contexte macro ; l'OFA confirme la dynamique d'exécution en temps réel à ces niveaux.
**TRADEX-AI C2** : Architecture TRADEX validée : C1 (AT Belkhayate) + C4 (macro) + C2 (OFA) = les 3 couches principales. C2 confirme les signaux C1 au moment de l'exécution. Aucune des 3 ne remplace les autres.
*Catégorie : structure_marche*
