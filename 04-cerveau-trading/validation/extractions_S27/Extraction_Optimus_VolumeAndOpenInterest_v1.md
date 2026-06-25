# Extraction Optimus — Price, Volume and Open Interest

**Source :** `bundles/optimusfutures/volume_and_open_interest.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancre URL seule · 0/0 certifiées · 0 à vérifier
**Décisions :** D8811 → D8830 · **Page :** https://optimusfutures.com/blog/volume-and-open-interest/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Volume + Open Interest = filtre de confirmation de tendance pour GC/CL/HG/ZW — alimente C2 (Order Flow) et C3 (Institutionnels).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image extractible depuis le bundle texte) | — | — | — |

---

## DÉCISIONS

### D8811 — Open Interest : définition et rôle unique en futures
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : L'open interest mesure le nombre total de contrats ouverts non réglés en futures. Contrairement aux marchés actions, c'est un indicateur exclusif aux marchés à terme qui révèle si du nouvel argent entre ou sort du marché.
**TRADEX-AI C3** : Pour GC, HG, CL, ZW — surveiller l'open interest (C3 Institutionnels) comme signal d'entrée ou de sortie de capitaux, en complément du COT hebdomadaire.
*Catégorie : volume_liquidite*

### D8812 — Open Interest en hausse + prix en hausse = confirmation haussière
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Si l'OI monte alors que le prix monte, cela signale une conviction haussière forte — de nouveaux capitaux entrent pour soutenir la hausse. Le trend a des chances de continuer.
**TRADEX-AI C2** : Signal de confirmation de trend GC/CL — si prix ↑ ET OI ↑, renforce le score de confiance du signal ACHETER (C2 Order Flow validation).
*Catégorie : indicateurs_tendance*

### D8813 — Open Interest en hausse + prix en baisse = confirmation baissière
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Prix baisse ET OI monte = entrée de nouvelles positions short. Le marché est en phase baissière active, pas en simple correction.
**TRADEX-AI C2** : Pour CL, HG en downtrend — si prix ↓ ET OI ↑, renforce signal VENDRE. Distingue une vraie pression vendeuse d'un rebond technique.
*Catégorie : indicateurs_tendance*

### D8814 — Open Interest en baisse + prix en hausse = hausse non confirmée
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Prix monte mais OI baisse = les positions short se ferment (short covering), pas de nouveaux acheteurs. La hausse est fragile et peu susceptible de durer.
**TRADEX-AI C2** : Garde-fou signal ACHETER — si prix ↑ mais OI ↓, réduire confiance du signal (possible faux breakout). Applicable à GC, ZW lors de spikes de prix.
*Catégorie : gestion_risque_entree*

### D8815 — Open Interest en baisse + prix en baisse = baisse de liquidation
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Prix baisse ET OI baisse = clôture de positions long existantes. Peut signaler la fin du trend baissier et un potentiel renforcement du marché (signal haussier contra-tendance).
**TRADEX-AI C2** : Pour GC en consolidation — si prix ↓ ET OI ↓, surveiller un retournement haussier potentiel. Contexte favorable à une entrée long prudente.
*Catégorie : structure_marche*

### D8816 — Volume élevé = énergie du marché, pas direction seule
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Le volume mesure l'activité journalière des échanges. Un volume en hausse confirme un trend existant ; un volume en baisse dans un trend suggère un essoufflement et risque de retournement.
**TRADEX-AI C2** : Condition de filtre pour tous les actifs tradables — exiger un volume supérieur à la moyenne avant de valider un signal (éviter les signaux sur volume creux = illiquidité).
*Catégorie : volume_liquidite*

### D8817 — Volume et OI combinés en hausse = mouvement de marché fort
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Quand volume ET open interest augmentent simultanément, cela indique une forte participation et un mouvement de marché robuste avec de nouveaux acteurs qui entrent.
**TRADEX-AI C2+C3** : Double confirmation — si sur GC/CL volume ↑ ET OI ↑ dans la direction du signal, ajouter +0,5 point au score /10 (confluence C2 + C3).
*Catégorie : volume_liquidite*

### D8818 — Breakout confirmé par volume + OI en hausse
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Lors d'une sortie de consolidation, un breakout accompagné de volume croissant ET d'OI croissant signale le début d'un nouveau trend. Sans ces confirmations, le breakout est suspect.
**TRADEX-AI C1+C2** : Règle d'entrée — un breakout sur pivot Belkhayate (C1) n'est validé que si volume ↑ ET OI ↑ simultanément (C2). Sans cela, signal = ATTENDRE.
*Catégorie : gestion_risque_entree*

### D8819 — Volume décroissant pendant un trend = signal d'alerte de retournement
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Si le volume diminue pendant un uptrend, la conviction des acheteurs baisse. Ceci peut annoncer un retournement avant que le prix ne l'indique.
**TRADEX-AI C2** : Garde-fou position active — si volume ↓ pendant un trade en cours (GC/HG/CL/ZW), envisager de réduire la taille ou serrer le stop (gestion de position active).
*Catégorie : gestion_position_active*

### D8820 — Consolidation = volume et OI faibles sous la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Les phases de consolidation se caractérisent typiquement par un volume faible, déclinant, et inférieur à la moyenne. L'OI y est également bas.
**TRADEX-AI C1** : Filtre de contexte — si volume ET OI sont sous la moyenne sur GC/ZW, le marché est en range : réduire agressivité des signaux, attendre confirmation de breakout avec volume.
*Catégorie : structure_marche*

### D8821 — OI stabilisé après trend = fin de momentum imminente
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Une stabilisation de l'OI après une phase de trend accompagnée d'un volume décroissant précède souvent la fin du momentum et une phase de consolidation.
**TRADEX-AI C2** : Signal de sortie partielle — si sur un trade GC/CL l'OI se stabilise et le volume baisse, fermer 50% de la position et serrer le stop sur le reste.
*Catégorie : gestion_position_active*

### D8822 — Prix = direction immédiate ; volume = énergie ; OI = nouveaux capitaux
🔵 **ÉCOLE** (Source : volume_and_open_interest.md) : La trinité analytique des futures : le prix donne la direction, le volume mesure l'énergie du mouvement, l'OI révèle si de nouveaux capitaux entrent ou si des positions existantes se clôturent.
**TRADEX-AI C2** : Grille pédagogique pour l'analyse multi-facteurs — les 3 composantes alimentent le score /10 de manière complémentaire et non redondante.
*Catégorie : indicateurs_tendance*

### D8823 — La volatilité du prix comme indicateur de risque
🔵 **ÉCOLE** (Source : volume_and_open_interest.md) : La volatilité (amplitude des mouvements de prix) est un indicateur de risque. Haute volatilité = grands swings potentiels = risque accru. À évaluer avant toute entrée.
**TRADEX-AI C5** : Intégration avec VX (VIX) — si volatilité futures GC/CL est élevée ET VIX > seuil, augmenter le filtre de risque et réduire la taille de position (C5 Sentiment).
*Catégorie : gestion_risque_entree*

### D8824 — Niveaux support/résistance comme obstacles au prix (hurdles)
🔵 **ÉCOLE** (Source : volume_and_open_interest.md) : Les zones de support/résistance sont des obstacles au mouvement libre du prix. Un prix avec de l'espace libre devant lui (sans S/R proche) offre un meilleur potentiel de mouvement.
**TRADEX-AI C1** : Condition de qualité du signal — vérifier que le prix a au moins 1,5x le R/R visé d'espace avant le prochain niveau S/R majeur avant de valider le signal (R/R ≥ 1:2 requis).
*Catégorie : gestion_risque_entree*

### D8825 — Foreshadowing reversal : OI + volume baissent = perte de momentum
🟡 **SYNTHÈSE** (Source : volume_and_open_interest.md) : Quand un trend fort commence à perdre force, la baisse simultanée de volume ET d'OI sert de signal précurseur de retournement, particulièrement visible aux niveaux S/R clés.
**TRADEX-AI C2+C1** : Confluence signal — si sur ZW/HG à un niveau S/R Belkhayate (C1), OI ↓ ET volume ↓, signal de retournement potentiel avec confiance renforcée.
*Catégorie : configuration*

### D8826 — Exemple WTI : OI + volume confirment fin de trend baissier
🟢 **FAIT VÉRIFIÉ** (Source : volume_and_open_interest.md) : Sur WTI Crude Oil (CL), un déclin de l'OI couplé à un changement de volume a précédé la perte de momentum baissier. Ce pattern est documenté comme comportement cyclique : consolidation → breakout → trend → consolidation.
**TRADEX-AI C2** : Applicable à CL — surveiller OI + volume pour anticiper les fins de trend avant signal contraire. Pertinent pour sortie de position et re-entry.
*Catégorie : configuration*

### D8827 — Volume et OI ne suffisent pas à expliquer chaque breakout
🟡 **SYNTHÈSE** (Source : volume_and_open_interest.md) : Volume et OI améliorent la précision de l'analyse mais n'expliquent pas tous les breakouts. Ce sont des filtres probabilistes, non des certitudes.
**TRADEX-AI C2** : Garde épistémique — volume + OI sont des facteurs du score /10, jamais des déclencheurs autonomes. La règle 3/4 + 2/3 reste primaire.
*Catégorie : psychologie*

### D8828 — Momentum du prix : cohérence directionnelle des bougies
🔵 **ÉCOLE** (Source : volume_and_open_interest.md) : Le momentum se lit dans la cohérence des bougies : bougies larges dans une direction = momentum fort. Mouvements en va-et-vient = indécision. Un marché indécis ne génère pas de signal valide.
**TRADEX-AI C1** : Filtre de contexte Belkhayate — la Direction (C1) doit être cohérente (≥ 3 bougies dans la même direction sur le timeframe principal) avant de valider un signal.
*Catégorie : indicateurs_tendance*

### D8829 — Cheat sheet : 4 combinaisons prix/OI et leurs implications
🟡 **SYNTHÈSE** (Source : volume_and_open_interest.md) : Tableau des 4 scénarios : (1) Prix↑ OI↑ = haussier confirmé · (2) Prix↓ OI↑ = baissier confirmé · (3) Prix↑ OI↓ = hausse fragile / baissier à terme · (4) Prix↓ OI↓ = liquidation / haussier potentiel.
**TRADEX-AI C2+C3** : Matrice de décision rapide à intégrer dans le module de scoring — chaque combinaison contribue au score /10 selon la direction du signal détecté.
*Catégorie : structure_marche*

### D8830 — Analyse comparative : volume = quotidien, OI = cumulatif actif
🔵 **ÉCOLE** (Source : volume_and_open_interest.md) : Volume = contrats échangés aujourd'hui (remis à zéro chaque jour). OI = total des contrats actifs ouverts (cumulatif, ne se remet pas à zéro). Deux mesures complémentaires non substituables.
**TRADEX-AI C2** : Distinction opérationnelle pour le data_reader.py — lire volume journalier ET OI séparément depuis NT8/ATAS, ne pas les confondre dans la logique de scoring.
*Catégorie : volume_liquidite*
