# Extraction AdamGrimes — Common Sense Checks for Quantitative Data
**Source :** `bundles/adamgrimes/common_sense_checks_quantitative_data.md` (HTTP 200) + 1 image certifiée
**Méthode images :** ancrage figcaption locale · 1/1 certifiées · 0 à vérifier
**Décisions :** D5611 → D5630 · **Page :** https://www.adamhgrimes.com/common-sense-checks-quantitative-data/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Validation rigoureuse des données quantitatives et des résultats de backtests — méthode TLAR (That Looks About Right) pour détecter les erreurs et éviter l'overfitting.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.jpg | Norden_bombsight_crosshairs | AdamHGrimes | D5612 |

## DÉCISIONS

### D5611 — Méthode TLAR : vérification de bon sens des données brutes
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : Le test TLAR ("That Looks About Right") est une vérification de bon sens à appliquer sur les données brutes avant toute analyse : chercher les valeurs aberrantes (returns +/-20% sur actions liquides, prix négatifs, high < low, open ou close hors du range high-low, données manquantes). Ces anomalies signalent des erreurs de données, pas des opportunités.
**TRADEX-AI C1** : Avant toute analyse KB sur les données NT8/ATAS, le `data_reader.py` doit valider : prix > 0, high >= low >= 0, open/close dans [low, high], aucune donnée manquante sur les 4 actifs TRADING.
*Catégorie : indicateurs_tendance*

### D5612 — Vérification visuelle obligatoire des séries temporelles (image : Norden_bombsight_crosshairs)
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md, image_01.jpg) : La visualisation d'une série temporelle de prix est une étape obligatoire pour détecter les anomalies non visibles dans les stats descriptives (ex : 101.23, 104.21, 1021.30, 100.21 — un zéro supplémentaire difficile à voir en liste). L'image illustre la nécessité d'une visée précise et calibrée.
**TRADEX-AI C1** : Le dashboard TRADEX-AI doit afficher les séries de prix des 4 actifs TRADING en continu — la visualisation est un garde-fou contre les erreurs de données silencieuses qui compromettraient l'analyse KB.
*Catégorie : volume_liquidite*

### D5613 — TLAR appliqué aux résultats : méfiance du système "trop bon"
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : Si un signal sur le S&P 500 gagne 80% du temps avec un grand échantillon, c'est une erreur dans l'analyse — pas une découverte. Le TLAR s'applique aussi aux résultats finaux : tout résultat paraissant "trop bon pour être vrai" doit être considéré comme contenant une erreur jusqu'à preuve du contraire.
**TRADEX-AI C1** : Si le taux de succès des signaux TRADEX dépasse 70% sur un backtest, auditer immédiatement la logique de scoring avant toute validation — signe probable de look-ahead bias ou d'overfitting.
*Catégorie : gestion_risque_entree*

### D5614 — Annualisation correcte des rendements
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : Un rendement de 0.41% sur 20 jours s'annualise en 5.3% (12.6 périodes de 20 jours dans 252 jours de trading : (1 + 0.0041)^12.6 - 1). Un rendement de 0.06% sur 5 jours s'annualise en 3.07%. Ces chiffres, comparés à la performance historique des actions (~7%/an), passent le test TLAR.
**TRADEX-AI C1** : Tout calcul de performance TRADEX doit annualiser les rendements avec la formule correcte (capitalisation composée, 252 jours/an) avant de comparer aux benchmarks — évite les conclusions erronées sur des périodes courtes.
*Catégorie : gestion_position_active*

### D5615 — Signal "consécutif à la baisse" comme exemple de mean reversion
🔵 **ÉCOLE** (Source : common_sense_checks_quantitative_data.md) : L'hypothèse que des clôtures consécutives dans une direction crée un setup de mean reversion est un exemple de raisonnement quantitatif valide. La procédure : identifier l'événement signal, collecter les instances historiques, mesurer la performance post-signal sur N jours.
**TRADEX-AI C1** : Le cerveau KB peut utiliser des patterns de consécutivité (ex : 3 clôtures baissières consécutives sur GC) comme composante d'un signal de mean reversion — à valider avec la méthode backtest Grimes avant intégration.
*Catégorie : configuration*

### D5616 — Vérifier les données à deux points du processus
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : La vérification TLAR doit être effectuée à au moins deux moments : (1) sur les données brutes, (2) sur les résultats finaux. Une seule vérification est insuffisante — des erreurs peuvent s'introduire lors du traitement intermédiaire.
**TRADEX-AI C1** : Le pipeline de données TRADEX applique deux contrôles : validation à l'entrée dans `data_reader.py` et validation des résultats dans `claude_brain.py` avant émission du signal final.
*Catégorie : gestion_risque_entree*

### D5617 — Benchmarker les résultats contre les rendements connus du marché
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : La validation des résultats quantitatifs passe par la comparaison avec les rendements connus du sous-jacent. Pour les actions US, ~7%/an est le repère. Un résultat annualisé entre 3% et 7% est plausible ; au-delà de 15-20%, chercher l'erreur d'abord.
**TRADEX-AI C1** : Pour GC (Or) : la performance historique annuelle est ~7-10%/an en tendance. Tout signal TRADEX qui backtesteserait à >20%/an sur Or doit être audité avant validation — plafond de vraisemblance TLAR.
*Catégorie : gestion_risque_entree*

### D5618 — Questions à poser avant de valider un système comme tradable
🔵 **ÉCOLE** (Source : common_sense_checks_quantitative_data.md) : Avant de déclarer un système prêt à trader, il faut se poser des questions précises sur les données : quel horizon temporel ? quelle volatilité du marché sur cette période ? quel drawdown maximum ? quelle fréquence de trades ? Les statistiques présentées seules sont insuffisantes.
**TRADEX-AI C1** : La validation d'un nouveau critère de scoring KB requiert : horizon de test ≥ 2 ans, ≥ 30 trades dans le backtest, drawdown maximum documenté, comparaison avec période de stress de marché (ex : 2020, 2022).
*Catégorie : gestion_risque_entree*

### D5619 — Wrangling de données : part sous-estimée du travail quantitatif
🟢 **FAIT VÉRIFIÉ** (Source : common_sense_checks_quantitative_data.md) : La majeure partie du temps des chercheurs quantitatifs est consacrée à la validation et au nettoyage des données ("data wrangling"), non à la construction de modèles. Ignorer cette réalité conduit à bâtir des modèles sur des données corrompues.
**TRADEX-AI C1** : Le `staleness_monitor.py` et le `data_reader.py` de TRADEX implémentent ce principe — la surveillance de la fraîcheur et de l'intégrité des données est une priorité architecturale, pas une option.
*Catégorie : volume_liquidite*

### D5620 — Mean reversion post signal : cadre général
🔵 **ÉCOLE** (Source : common_sense_checks_quantitative_data.md) : L'hypothèse de mean reversion après un event signal (ex : 2 clôtures consécutives à la baisse) est un cadre de recherche valide. Sur le S&P 500, Grimes cite des rendements post-signal de 0.06% sur 5 jours et 0.41% sur 20 jours comme plausibles et passant le TLAR.
**TRADEX-AI C7** : Les corrélations et patterns de mean reversion inter-marchés (ex : GC après 3 jours de baisse DX) peuvent être intégrés comme composante C7 du score — à valider avec ≥ 30 instances historiques avant activation.
*Catégorie : correlations*
