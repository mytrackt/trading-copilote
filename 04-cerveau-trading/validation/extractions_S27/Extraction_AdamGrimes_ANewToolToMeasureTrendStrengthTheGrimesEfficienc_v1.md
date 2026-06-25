# Extraction AdamGrimes — A New Tool to Measure Trend Strength: The Grimes Efficiency Ratio
**Source :** `bundles/adamgrimes/a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle (graphiques GER référencés mais non inclus) · 0/0 certifiées · 0 à vérifier
**Décisions :** D5051 → D5066 · **Page :** https://www.adamhgrimes.com/a-new-tool-to-measure-trend-strength-the-grimes-efficiency-ratio/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le GER est un indicateur quantifiable de force de tendance sur une fenêtre de 20 jours — complémentaire au COG Belkhayate pour qualifier l'état de tendance sur GC/HG/CL/ZW/ES/DX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D5051 — Définition du Grimes Efficiency Ratio (GER) : formule et calcul
🟢 **FAIT VÉRIFIÉ** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Le GER est calculé en deux étapes : (1) pour chaque barre, calculer le close comme pourcentage du range High-Low des N dernières périodes : `crng = (close - lowest(low, N)) / (highest(high, N) - lowest(low, N))` ; (2) lisser cette valeur en faisant la moyenne des N dernières valeurs de crng : `GER = average(crng, N)`. Valeur de référence N=20 (environ 1 mois de trading). GER=1.0 = close au plus haut du mois, GER=0.0 = close au plus bas du mois, GER=0.5 = milieu du range.
**TRADEX-AI C1** : Le GER avec N=20 est calculable directement depuis les données NT8 (High/Low/Close) pour GC/HG/CL/ZW. Peut compléter la Direction Belkhayate comme confirmateur de tendance.
*Catégorie : indicateurs_tendance*

### D5052 — Code EasyLanguage complet du GER fourni et utilisable
🟢 **FAIT VÉRIFIÉ** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Code exact fourni par Grimes en EasyLanguage : `inputs: lookback(20); vars: rng(0), crng(0), sumrng(0); rng = highest(h, lookback) - lowest(l, lookback); crng = iff(rng > 0,((c - lowest(l, lookback)) / rng), 0); sumrng = average(crng, lookback); plot1(sumrng);` La division par zéro est gérée par le `iff(rng > 0, ..., 0)`.
**TRADEX-AI C1** : Formule directement portable en Python pour le moteur TRADEX. Ajouter à `05-saas/engine/` comme indicateur GER calculé depuis les JSONs NT8 (GC/HG/CL/ZW).
*Catégorie : indicateurs_tendance*

### D5053 — GER brut (non lissé) est trop bruité pour être exploitable
🟢 **FAIT VÉRIFIÉ** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : La version brute (close as % of range, sans lissage) peut basculer de 1.0 à 0.0 en une seule barre. Elle est trop volatile pour extraire un signal utile. C'est le lissage sur N périodes qui rend l'indicateur exploitable.
**TRADEX-AI C1** : Règle de calcul : toujours utiliser la version lissée (étape 2 de la formule) dans le moteur TRADEX. Ne jamais utiliser la valeur crng brute comme signal direct.
*Catégorie : indicateurs_tendance*

### D5054 — GER comme filtre de tendance pour stratégies règle-basées
🔵 **ÉCOLE** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Grimes suggère d'utiliser le GER comme filtre d'entrée pour des stratégies règle-basées, mais met en garde : l'indicateur décrit bien les conditions de tendance passées, mais les régimes de marché changent rapidement. Un indicateur de momentum retardé comme le GER peut faire plus de mal que de bien utilisé seul comme filtre d'entrée.
**TRADEX-AI C1** : Le GER ne doit pas être le seul filtre de tendance dans TRADEX. L'utiliser en combinaison avec Direction Belkhayate (C1) et COT (C3) pour un signal multi-cercles.
*Catégorie : indicateurs_tendance*

### D5055 — GER pour gestion de positions actives : serrage de stop en tendance déclinante
🔵 **ÉCOLE** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Plutôt que comme filtre d'entrée, Grimes recommande d'utiliser le GER pour la gestion de positions existantes. Exemple : resserrer le trailing stop plus rapidement lorsque le GER diminue (tendance qui s'affaiblit), relâcher le stop lorsque le GER est fort (tendance confirmée).
**TRADEX-AI C1** : Application directe pour le mode Auto TRADEX : si GER(GC) décroit en cours de trade, accentuer le trailing stop. À intégrer dans `05-saas/engine/risk_manager.py`.
*Catégorie : gestion_position_active*

### D5056 — GER pour ranking relatif de marchés : identifier les plus en tendance
🔵 **ÉCOLE** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Grimes propose de classer plusieurs marchés par leur GER respectif pour sélectionner ceux à trader. Les marchés avec le GER le plus élevé (proche de 1.0) sont en tendance haussière forte, ceux avec le GER le plus bas (proche de 0.0) en tendance baissière forte.
**TRADEX-AI C7** : Calculer GER pour GC/HG/CL/ZW simultanément. Prioriser le signal sur l'actif qui montre le GER le plus extrême (>0.8 ou <0.2) — cohérent avec la matrice de corrélations C7.
*Catégorie : correlations*

### D5057 — GER milieu de range (0.4-0.6) : marchés candidats aux breakouts
🔵 **ÉCOLE** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Les marchés avec un GER modéré (milieu de range, présumé en consolidation) sont des candidats potentiels aux breakouts. Grimes suggère de les surveiller pour un screening supplémentaire plutôt que de les trader directement.
**TRADEX-AI C1** : Règle de filtrage TRADEX : GC/HG/CL/ZW avec GER entre 0.4-0.6 = potentiel breakout, à surveiller mais nécessite confirmation supplémentaire (C2 Order Flow + C3 COT) avant signal.
*Catégorie : configuration*

### D5058 — GER extrême suivi de normalisation : signal contrarian de pullback
🟡 **SYNTHÈSE** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Les marchés ayant montré un GER extrêmement élevé ou bas (momentum de tendance épuisé) qui reviennent ensuite vers des niveaux plus modérés peuvent représenter des candidats au trade de pullback. La psychologie du marché alterne entre extrêmes — le GER capture ce cycle tendance/range.
**TRADEX-AI C1** : Signal TRADEX potentiel : GER(GC) >0.9 puis retour sous 0.75 = possible setup de pullback haussier. À combiner avec niveaux pivots Belkhayate pour valider l'entrée.
*Catégorie : configuration*

### D5059 — Test statistique GER contrarian sur 50 actions : +3,74% de surperformance buy signal
🟢 **FAIT VÉRIFIÉ** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Sur un panier de 50 actions, Grimes teste le fading d'un GER extrême (une seule entrée toutes les 2 semaines). Le signal d'achat (GER en extremum bas = tendance épuisée à la baisse) produit une surperformance de +3,74% sur les 20 prochaines séances par rapport au drift de référence. Le signal de vente est statistiquement non significatif (asymétrie haussière).
**TRADEX-AI C1** : Sur GC (Or), l'asymétrie haussière à long terme (safe haven) rend le signal buy du GER contrarian pertinent. Signal de vente GC à utiliser avec plus de prudence. Seuil recommandé : GER(GC) en percentile extrême bas + confirmation COT.
*Catégorie : gestion_risque_entree*

### D5060 — Différence GER vs Kaufman Efficiency Ratio (KER) : deux approches distinctes
🟢 **FAIT VÉRIFIÉ** (Source : a_new_tool_to_measure_trend_strength_the_grimes_efficiency_r.md) : Le KER (Kaufman) mesure le déplacement de prix sur une période divisé par la somme des mouvements absolus (combien de chemin parcouru vs chemin direct). Le GER mesure la position du close dans le range High-Low total de la période (percentile de prix). Le GER n'utilise PAS les mouvements cumulés, contrairement au KER. Ces deux indicateurs capturent des aspects différents de l'efficience.
**TRADEX-AI C1** : Ne pas confondre GER et KER dans le code TRADEX. Si les deux sont implémentés, les documenter séparément avec leur formule exacte dans `settings.py`.
*Catégorie : indicateurs_tendance*
