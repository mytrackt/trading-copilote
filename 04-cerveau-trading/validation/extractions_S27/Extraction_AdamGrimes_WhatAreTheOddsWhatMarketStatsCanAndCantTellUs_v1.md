# Extraction AdamGrimes — What Are The Odds? What Market Stats Can And Can't Tell Us
**Source :** `bundles/adamgrimes/what_are_the_odds_what_market_stats_can_and_cant_tell_us.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7411 → D7430 · **Page :** https://www.adamhgrimes.com/what-are-the-odds-what-market-stats-can-and-cant-tell-us/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Cadre rigoureux pour valider statistiquement les signaux avant de les intégrer dans la KB Belkhayate.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D7411 — Simplicité de la question statistique
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : La réponse statistique est toujours la réponse à une question très précise. Une question mal posée donne une réponse correcte à la mauvaise question, et ultimement la mauvaise réponse à la réalité.
**TRADEX-AI C1** : Avant de valider un signal Belkhayate via backtest, définir la question exacte (ex. "que se passe-t-il après alignement 3/4 actifs trading sur range bars NT8 ?") — ne pas réutiliser des stats ES sur daily pour valider un signal GC sur range bars.
*Catégorie : configuration*

### D7412 — Règle des 3 conditions maximum
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Si vous ajoutez plus de 3 conditions à une étude statistique, vous êtes en danger de data mining. Garder la question aussi simple que possible.
**TRADEX-AI C1** : La règle d'entrée TRADEX (3/4 trading + 2/3 confirmation alignés) respecte ce principe : deux conditions binaires, pas de sur-spécification. Ne pas ajouter de filtres supplémentaires sans validation statistique indépendante.
*Catégorie : gestion_risque_entree*

### D7413 — Interdiction des "coupes multiples" dans les données
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Raffiner la question jusqu'à obtenir le résultat souhaité ("multiple cuts through the data") invalide l'étude statistique — c'est du cherry-picking.
**TRADEX-AI C1** : Lorsque le moteur Python évalue un signal, les seuils (score ≥ 7.0, R/R ≥ 1:2) sont figés AVANT l'observation du marché. Ne jamais ajuster les seuils post-hoc pour qu'un signal passé soit valide.
*Catégorie : gestion_risque_entree*

### D7414 — Le snapback après extension baissière n'est pas haussier en continuité
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Étude empirique S&P 500 : après fermeture sous le canal Keltner inférieur + rebond > +2.0 sigma, le lendemain ne ferme à la hausse que 45% du temps (vs 53% aléatoire) avec un rendement moyen négatif.
**TRADEX-AI C1/C5** : Un rebond violent après une extension baissière n'est PAS un signal d'achat de continuation — c'est la mean reversion qui domine. Pour GC/CL, un snapback intraday violent après excès baissier doit être traité comme potentiellement épuisé, pas comme confirmation haussière.
*Catégorie : structure_marche*

### D7415 — L'ajout de filtres peut aggraver les résultats
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Filtrer le snapback en ne gardant que les cas dans le percentile supérieur 50% du range annuel (hors bear market 2007-2009) a dégradé les statistiques : hausse le lendemain seulement 23% du temps.
**TRADEX-AI C1** : Ajouter des filtres de confirmation supplémentaires peut réduire la qualité du signal — tester chaque filtre ajouté à la grille /10 sur données historiques avant de l'activer.
*Catégorie : configuration*

### D7416 — Le contexte macro (bull/bear market) prime sur les signaux techniques isolés
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Même face à des statistiques de court terme bearish, le contexte bull market (S&P < 6% de ses ATH) maintient un biais haussier. Le "caractère du suivant" prime sur les stats brutes.
**TRADEX-AI C4** : Le cercle C4 (Macro) doit être consulté avant de contredire un signal C1 (Prix Belkhayate) sur base de statistiques de court terme. Un marché en tendance forte (ES > EMA longue) affecte l'interprétation des signaux intraday sur GC/CL.
*Catégorie : macro_evenements*

### D7417 — La mean reversion domine les snapbacks isolés
🟢 **FAIT VÉRIFIÉ** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Acheter la clôture de n'importe quel jour haussier produit un léger résultat négatif en moyenne — la mean reversion est la force dominante sur les snapbacks non filtrés.
**TRADEX-AI C1** : Ne jamais entrer sur GC/HG/CL/ZW uniquement parce que la session précédente a été violemment haussière ou baissière — chercher confirmation direction via Belkhayate BGC + alignement cercles avant entrée.
*Catégorie : structure_marche*

### D7418 — Examiner manuellement les dates historiques similaires
🟡 **SYNTHÈSE** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Après avoir identifié un pattern statistique, examiner les 10-15 dates historiques qui remplissent les conditions et analyser le comportement des jours suivants donne une intuition qualitative complémentaire aux chiffres.
**TRADEX-AI C1** : Lors de la validation manuelle d'une règle KB candidate (zone validation/), comparer le comportement de marché sur 5-10 occurrences historiques similaires sur GC/CL avant de fusionner dans KNOWLEDGE_BASE_MASTER.json.
*Catégorie : configuration*

### D7419 — Les statistiques de trading ne sont jamais des vérités universelles
🟡 **SYNTHÈSE** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Les résultats statistiques présentent toujours une large dispersion des résultats individuels autour de la moyenne. Les moyennes cachent la gamme complète des issues possibles.
**TRADEX-AI C5** : Le score de confiance Claude (%) doit refléter la dispersion connue des résultats historiques similaires, pas seulement la moyenne. Un signal avec moyenne positive mais variance élevée mérite un score de confiance réduit.
*Catégorie : psychologie*

### D7420 — Segmenter les régimes de volatilité pour améliorer les backtests
🟡 **SYNTHÈSE** (Source : what_are_the_odds_what_market_stats_can_and_cant_tell_us.md) : Il est recommandé de segmenter les résultats selon les régimes de volatilité (low vol vs high vol) pour obtenir des statistiques plus fiables et actionnables.
**TRADEX-AI C5** : Le cercle C5 (VIX) doit conditionner l'interprétation des signaux — un même pattern Belkhayate sur GC a des probabilités de succès différentes en régime VIX < 15 vs VIX > 30. Cette segmentation est à implémenter en Phase C.
*Catégorie : indicateurs_momentum*

