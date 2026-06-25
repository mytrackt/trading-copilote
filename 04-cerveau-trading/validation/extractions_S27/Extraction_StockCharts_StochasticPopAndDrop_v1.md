# Extraction StockCharts — Stochastic Pop and Drop
**Source :** `bundles/stockcharts/stochastic_pop_and_drop.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D3891 → D3910 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/stochastic-pop-and-drop
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : stratégie momentum multi-filtre applicable à GC/HG/CL/ZW pour détecter breakouts de continuation dans la tendance dominante avec confirmation volume.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Chart 1 - Stochastic Pop | Trading Bias | D3891 |
| image_02 | Chart 2 - Stochastic Pop | Waiting for a Range | D3893 |
| image_03 | Chart 3 - Stochastic Pop | Buy Signal | D3895 |
| image_04 | Chart 4 - Stochastic Pop | Stops and Targets | D3897 |
| image_05 | Chart 5 - Stochastic Pop | Sell Signal | D3901 |

## DÉCISIONS

### D3891 — Origine et auteurs de la stratégie Stochastic Pop and Drop
🔵 **ÉCOLE** (Source : stochastic_pop_and_drop.md) : La stratégie Stochastic Pop a été développée par Jake Bernstein et modifiée par David Steckler, qui a publié un article dans *Stocks & Commodities Magazine* en août 2000. Steckler a ajouté des filtres ADX et un stochastique hebdomadaire à la version originale de Bernstein.
**TRADEX-AI C1** : Stratégie de continuation de tendance basée sur le momentum — pertinente pour filtrer les entrées sur GC/HG/CL/ZW après consolidation.
*Catégorie : indicateurs_momentum*

### D3892 — Biais directionnel défini par le stochastique long terme
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Steckler utilise le stochastique hebdomadaire 14 périodes : biais haussier si au-dessus de 50 et montant. La version adaptée de l'article utilise un stochastique quotidien 70 périodes (= 5 × 14 jours) pour tout afficher sur un seul graphique. Biais haussier si stochastique 70 périodes > 50.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un stochastique lent 70 périodes > 50 définit un contexte favorable aux longs — à intégrer comme filtre de biais dans le score /10.
*Catégorie : indicateurs_momentum*

### D3893 — ADX comme filtre de consolidation avant le signal
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_02) : L'ADX 14 périodes en dessous de 20 signale une tendance faible et une possible consolidation. Steckler préfère ADX < 15 mais accepte ADX < 20. Un ADX haut et montant = tendance forte ; un ADX bas et tombant = tendance qui s'affaiblit.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, ADX < 20 identifie les phases de range avant breakout — peut signaler le bon moment d'attente avant une entrée momentum.
*Catégorie : indicateurs_tendance*

### D3894 — Conditions complètes du signal d'achat (Stochastic Pop)
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Le signal d'achat nécessite la réunion de 3 conditions : (1) stochastique 70 jours > 50 (biais haussier), (2) ADX 14 jours < 20 (consolidation en cours), (3) stochastique 14 jours qui franchit 80 à la hausse + déclin sur volume supérieur à la moyenne ou breakout de consolidation.
**TRADEX-AI C1** : Triple condition filtrant les faux signaux — applicable à GC/CL comme signal de momentum confirmé par le volume en mode Manuel.
*Catégorie : gestion_risque_entree*

### D3895 — Volume de confirmation : comparaison au SMA 250 jours
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_03) : Pour l'évaluation du volume, comparer le volume actuel à la moyenne mobile simple sur 250 jours du volume (= moyenne sur 1 an). Un volume au-dessus de cette moyenne annuelle est considéré comme fort. Un fort volume avant le breakout peut être un précurseur du breakout lui-même.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, volume > SMA 250 volume = confirmation institutionnelle — à croiser avec l'order flow ATAS pour valider les entrées.
*Catégorie : volume_liquidite*

### D3896 — Le signal Pop peut précéder le breakout de prix
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_03) : Le signal Stochastic Pop peut survenir avant le breakout effectif du prix. Un volume fort sur le rebond depuis le support peut précéder le breakout. Les traders agissant sur le Pop bénéficient d'un meilleur ratio risque/rendement que ceux attendant le breakout confirmé.
**TRADEX-AI C1** : Pour GC/CL, agir sur le Pop dès le volume fort (avant le breakout) améliore le R/R — applicable en mode Manuel quand les 3 conditions sont réunies.
*Catégorie : gestion_risque_entree*

### D3897 — Stop-loss basé sur le creux précédant le Pop
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_04) : Le stop-loss peut être placé juste en dessous du plus bas de la consolidation ou juste en dessous du creux/bas de réaction précédant le Pop. Planifier le trade (stop + objectif) avant de prendre la position : "Plan your trade and trade your plan."
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, stop juste sous le creux du Pop — structure simple de gestion du risque à intégrer dans le calcul R/R ≥ 1:2 obligatoire TRADEX.
*Catégorie : gestion_risque_entree*

### D3898 — Stop suiveur avec Parabolic SAR et signal de sortie Stochastique
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_04) : Un stop-loss suiveur peut être mis en place pour verrouiller les profits si le prix continue à monter. Le Parabolic SAR peut servir de stop suiveur. Un passage du stochastique 14 jours sous 50 signale un ralentissement ou une dégradation du momentum court terme — peut servir à prendre les profits ou resserrer le stop.
**TRADEX-AI C1** : Sur positions GC/CL longues, Parabolic SAR ou passage Stoch < 50 = signal de sortie partielle ou resserrement du stop.
*Catégorie : gestion_position_active*

### D3899 — Conditions complètes du signal de vente (Stochastic Drop)
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Le signal de vente (Stochastic Drop) est le miroir du Pop. Conditions : (1) stochastique 70 jours < 50, (2) ADX 14 jours < 20, (3) stochastique 14 jours plonge sous 20, (4) actif décline sur volume fort et/ou rupture du support de consolidation.
**TRADEX-AI C1** : Applicable à GC/HG/CL/ZW en mode court (hypothétique) — surtout utile pour identifier les zones de risque de retournement baissier en mode Manuel.
*Catégorie : gestion_risque_entree*

### D3900 — Pour les signaux baissiers, la confirmation volume est moins critique
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md, image_05) : Pour les signaux baissiers (Stochastic Drop), la confirmation par le volume n'est pas aussi importante que pour les signaux haussiers. Dans l'exemple HR Block (HRB), le signal Stochastic Drop a précédé un fort déclin même sans expansion du volume ni rupture du support.
**TRADEX-AI C1** : Sur GC/CL, un Drop stochastique (Stoch 14j < 20 + biais < 50) sans volume fort reste un signal d'alerte valide — à surveiller en mode Manuel.
*Catégorie : indicateurs_momentum*

### D3901 — Réglage fin ADX : ADX < 15 améliore la détection des consolidations
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Exiger ADX < 15 (au lieu de 20) améliore les chances de capturer une réelle consolidation sur le graphique des prix. Pour les titres à faible volatilité (ex : utilities), l'ADX peut naturellement rester bas et nécessiter un seuil < 10 pour identifier les consolidations.
🟡 **SYNTHÈSE** : La volatilité propre à chaque marché détermine le seuil ADX optimal — sur les futures de matières premières comme GC/CL (forte volatilité), ADX < 20 est probablement plus adapté que ADX < 15.
**TRADEX-AI C1** : Calibrer le seuil ADX selon la volatilité de GC, HG, CL, ZW — commencer avec ADX < 20, affiner vers 15 si trop de faux signaux.
*Catégorie : indicateurs_tendance*

### D3902 — Qualité du Pop : amplitude du mouvement stochastique
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Un surge stochastique de 35 à 85 (amplitude 50 points) est plus puissant qu'un surge de 65 à 85 (amplitude 20 points). Il faut éviter les signaux survenant après de courts replis du stochastique — ces signaux sont moins fiables.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un Pop depuis une zone < 40 vers > 80 est plus fiable qu'un Pop depuis > 60 — pondérer la qualité du signal dans le score /10.
*Catégorie : indicateurs_momentum*

### D3903 — Confirmer le Pop avec des patterns de prix
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Les signaux Pop/Drop sont conçus pour capturer un mouvement de continuation dans la tendance principale. Pour confirmer un Pop haussier : chercher un bull flag ou une sortie de falling wedge. Pour confirmer un Drop baissier : chercher un bear flag ou une rupture de rising wedge.
**TRADEX-AI C1** : Sur GC/CL, croiser le signal Stochastic Pop avec un bull flag ou wedge breakout pour maximiser la probabilité de réussite — confirmation multi-signal.
*Catégorie : configuration*

### D3904 — Critères du scan SharpCharts pour le Stochastic Pop haussier
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Scan bullish Pop : Stoch %K lent (70,3) > 50 ET ADX(14) < 20 ET Stoch %K lent (14,3) croise au-dessus de 80, avec volume SMA(20) > 40 000 et close SMA(60) > 20.
**TRADEX-AI C1** : Logique de scan transposable sur données NT8 pour GC/HG/CL/ZW — filtre déterministe à implémenter en Python pour le moteur niveau 1.
*Catégorie : configuration*

### D3905 — Critères du scan SharpCharts pour le Stochastic Drop baissier
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Scan bearish Drop : Stoch %K lent (70,3) < 50 ET ADX(14) < 20 ET Stoch %K lent (14,3) croise en-dessous de 20, avec volume SMA(20) > 40 000 et close SMA(60) > 20.
**TRADEX-AI C1** : Logique de scan transposable sur données NT8 pour GC/HG/CL/ZW — filtre déterministe complémentaire pour identifier les zones de risque.
*Catégorie : configuration*

### D3906 — Vérification ratio risque/rendement avant toute entrée
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : Avant de prendre une position, consulter le graphique de prix pour évaluer le ratio risque/rendement et s'assurer qu'il est acceptable. Cette évaluation doit précéder toute prise de position.
**TRADEX-AI C1** : Règle alignée avec TRADEX : R/R ≥ 1:2 obligatoire avant tout signal — à vérifier systématiquement en mode Manuel et Auto.
*Catégorie : gestion_risque_entree*

### D3907 — Stratégie conçue comme point de départ, non système complet
🟢 **FAIT VÉRIFIÉ** (Source : stochastic_pop_and_drop.md) : La stratégie Stochastic Pop and Drop est "conçue comme un point de départ pour le développement d'un système de trading". Elle doit être augmentée avec le style de trading, les préférences R/R et le jugement personnel du trader.
⚫ **HYPOTHÈSE PROJET** : Dans TRADEX-AI, cette stratégie sert de couche momentum complémentaire à la méthode Belkhayate — non substituable aux cercles C1-C7.
**TRADEX-AI C1** : Intégrer comme indicateur secondaire de momentum dans le score /10 TRADEX, jamais comme signal primaire indépendant.
*Catégorie : psychologie*
