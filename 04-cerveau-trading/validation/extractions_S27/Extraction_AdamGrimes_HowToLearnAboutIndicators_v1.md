# Extraction AdamGrimes — How to Learn About Indicators
**Source :** `bundles/adamgrimes/how_to_learn_about_indicators.md` (HTTP 200) + 0 images certifiées
**Méthode images :** sans image · 0/0 certifiées · 0 à vérifier
**Décisions :** D6071 → D6082 · **Page :** https://www.adamhgrimes.com/how-to-learn-about-indicators/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Protocole d'évaluation d'indicateurs — applicable pour valider tout indicateur Belkhayate (COG, Énergie, Timing) avant intégration dans la KB.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6071 — Principe fondamental : comprendre avant d'utiliser
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Enseigner un indicateur via ses "setups" (acheter quand la ligne croise, vendre quand ça entre dans cette zone) sans en comprendre le calcul est une erreur fondamentale. La majorité des "formateurs" et même des développeurs d'indicateurs ne comprennent pas réellement ce que leur outil mesure.
**TRADEX-AI C1** : Avant d'intégrer tout indicateur Belkhayate (COG, Énergie, BGC, Timing) dans `claude_brain.py`, documenter son calcul exact dans la KB. Une règle sans calcul vérifié doit être marquée `HYPOTHESE_PROJET` et non `FAIT_VERIFIE`.
*Catégorie : structure_marche*

### D6072 — Divergence : exemple de concept non compris
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : La "divergence" entre prix et indicateur est un exemple de concept enseigné sans compréhension réelle. Questions non posées : que mesure réellement la divergence ? Dépend-elle de la durée du mouvement ou de son amplitude ? Qu'est-ce qui est réellement comparé ? Sans répondre à ces questions, on ne peut pas valider l'utilité du signal.
**TRADEX-AI C1** : Pour toute règle de divergence dans la KB Belkhayate, documenter précisément quel indicateur est comparé à quoi, sur quelle période, et avec quelle magnitude minimum pour constituer un signal valide.
*Catégorie : indicateurs_momentum*

### D6073 — 3 étapes pour comprendre un indicateur
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Méthode rigoureuse en 3 étapes : (1) Comprendre le calcul exact. (2) Comprendre la réponse de l'indicateur aux changements de données. (3) Comprendre ce que cela signifie sur données marché réelles. Sans ces 3 étapes, on ne peut pas décider si et comment utiliser l'outil.
**TRADEX-AI C1** : Le protocole de validation KB TRADEX doit suivre ces 3 étapes pour chaque indicateur Belkhayate. La fiche KB d'un indicateur est incomplète si l'une des 3 étapes est absente.
*Catégorie : structure_marche*

### D6074 — Historique de l'indicateur : contexte de développement
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Comprendre l'historique d'un indicateur est utile : qui l'a inventé ? Quelles modifications ont été apportées ? Quelle puissance de calcul était disponible à l'époque ? Les contraintes de l'époque (calcul manuel, moyens limités) expliquent souvent des choix de paramètres qui ne sont plus optimaux aujourd'hui.
**TRADEX-AI C1** : Pour les indicateurs Belkhayate (COG, Énergie, Timing), documenter dans la KB leur contexte historique de développement. Les paramètres figés (période 180, ordre 3, coeffs 0.618/1.618) doivent avoir une justification documentée.
*Catégorie : indicateurs_tendance*

### D6075 — Idée-clé unique : raison d'être de l'indicateur
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Identifier l'idée unique derrière un indicateur : pourquoi est-il préférable de regarder ce calcul plutôt que le prix brut ? Cette question force à articuler l'hypothèse de marché sous-jacente. Si on ne peut pas répondre clairement, l'indicateur ne devrait pas être utilisé.
**TRADEX-AI C1** : Chaque indicateur dans la KB Belkhayate doit avoir un champ `hypothese_marche` expliquant pourquoi il apporte de l'information supplémentaire au prix brut. COG : "identifie le centre de gravité statistique des prix" — à documenter précisément.
*Catégorie : structure_marche*

### D6076 — Chevauchement entre indicateurs : attention aux redondances
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Avant d'utiliser un indicateur, évaluer son degré de chevauchement avec les indicateurs déjà utilisés. Des indicateurs hautement corrélés donnent une fausse impression de confirmation alors qu'ils mesurent la même chose.
**TRADEX-AI C1** : Dans la grille de scoring /10, vérifier que les 7 cercles mesurent bien des dimensions indépendantes. Si C1 (COG) et C2 (Order Flow) sont fortement corrélés sur GC, le score composite est biaisé vers le haut artificiellement.
*Catégorie : correlations*

### D6077 — Calcul depuis zéro : règle d'or de compréhension
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : La seule façon de vraiment comprendre un indicateur est de le coder soi-même dans Excel ou Python, en étant capable d'expliquer chaque étape à un enfant de 12 ans. Si on ne peut pas le faire, on ne comprend pas vraiment l'indicateur. Attention aux langages propriétaires (EasyLanguage, NinjaScript) qui peuvent masquer des calculs.
**TRADEX-AI C1** : Les indicateurs Belkhayate codés dans `05-saas/engine/` doivent avoir une implémentation Python pure (pas uniquement NinjaScript), permettant leur validation indépendante. Les stubs actuels (Énergie) violent cette règle.
*Catégorie : structure_marche*

### D6078 — Données synthétiques contrôlées : test de réponse
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Tester un indicateur avec des données synthétiques contrôlées : marché plat → trending → plat ; spike isolé ; "staircase" ; oscillation sinusoïdale ; trend linéaire vs exponentiel. Cela révèle les comportements réels de l'indicateur que les données de marché bruitées masquent.
**TRADEX-AI C1** : Le backtest hostile COG (commit e45a0fe) a validé cette approche. Étendre la méthodologie aux indicateurs Énergie et Timing Belkhayate lorsqu'ils seront codés. Utiliser des séries synthétiques avant les données GC/HG réelles.
*Catégorie : configuration*

### D6079 — Phase d'observation : accumulation avant hypothèse
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Après le calcul et les tests synthétiques, observer l'indicateur sur beaucoup de données marché réelles avant de formuler des hypothèses. L'objectif est de voir comment l'indicateur répond aux inflexions de prix — phase de collecte d'information, pas de validation.
**TRADEX-AI C1** : Les 164 vidéos Belkhayate en attente de transcription Gemini sont des sources d'observation qualitative. Après transcription, les règles extraites constituent des hypothèses à tester, pas des faits vérifiés.
*Catégorie : structure_marche*

### D6080 — Backtesting : tester ce qu'on observe
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : Après l'observation, concevoir des tests pour valider ce qu'on pense voir : backtests manuels ou codés. Cette étape est distincte de l'observation — ne pas mélanger les deux phases (biais de confirmation).
**TRADEX-AI C1** : Le protocole de validation KB doit séparer "observations issues de l'analyse visuelle" (marqueur SYNTHESE) et "règles validées par backtest" (marqueur FAIT_VERIFIE). Le backtest hostile COG (daily invalide) est un exemple de validation rigoureuse.
*Catégorie : configuration*

### D6081 — Décision finale d'utilisation : oui ou non basé sur preuves
🔵 **ÉCOLE** (Source : how_to_learn_about_indicators.md) : La conclusion du processus est une décision binaire : cet indicateur a-t-il une place dans mon trading, oui ou non ? Cette décision doit être basée sur la compréhension et les tests — pas sur la tradition, la popularité ou la confiance en l'auteur.
**TRADEX-AI C1** : Le statut `ATTENTE_VALIDATION` dans la KB (ex : Énergie Belkhayate) est la représentation correcte de cet état intermédiaire. Ne pas passer à `VALIDE` avant d'avoir terminé les étapes 1→8 du protocole Grimes.
*Catégorie : gestion_risque_entree*

### D6082 — Scepticisme par défaut : développeurs non profitables
🟡 **SYNTHÈSE** (Source : how_to_learn_about_indicators.md) : Plusieurs développeurs d'indicateurs techniques célèbres ont admis en interview ne pas avoir tradé profitablement. Leurs livres représentaient leur seul revenu lié à ces outils. Cela justifie une posture de scepticisme par défaut envers tout indicateur, même populaire.
**TRADEX-AI C1** : La méthode Belkhayate elle-même doit être soumise à ce scepticisme rigoureux. Les règles extraites des vidéos sont des hypothèses jusqu'à validation quantitative. Le marqueur `HYPOTHESE_PROJET` dans la KB reflète cette posture.
*Catégorie : psychologie*
