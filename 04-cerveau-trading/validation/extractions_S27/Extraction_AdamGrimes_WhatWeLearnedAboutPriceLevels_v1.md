# Extraction AdamGrimes — What We Learned About Price Levels
**Source :** `bundles/adamgrimes/what_we_learned_about_price_levels.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D7451 → D7470 · **Page :** https://www.adamhgrimes.com/what-we-learned-about-price-levels/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Validation empirique des niveaux de prix — les highs/lows de session précédente sur ES sont réels, les ronds EURUSD sont illusoires.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D7451 — Hypothèse de base : les niveaux de prix sont aléatoires jusqu'à preuve contraire
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Toute étude sur les niveaux de prix doit commencer avec l'hypothèse nulle que ces niveaux sont aléatoires et insignifiants. La charge de la preuve appartient à ceux qui affirment la valeur des niveaux.
**TRADEX-AI C1** : Les pivots Belkhayate et niveaux COG intégrés dans la KB doivent avoir une justification empirique ou une logique mécaniste solide — pas seulement une tradition ou un "ça a l'air de fonctionner sur le chart".
*Catégorie : configuration*

### D7452 — Les high/low de session précédente sur S&P 500 sont statistiquement significatifs
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Test sur 1 535 traders / 20 charts S&P 500 5min : pour chaque chart S&P 500, les intervalles de confiance à 95% pour identifier les "vrais" niveaux (high/low session précédente + Globex high/low) sont tous clairement au-dessus de 50%. Les traders montrent une forte préférence pour les vrais niveaux.
**TRADEX-AI C1** : Les high/low de session précédente et les high/low Globex (overnight) sur ES sont des niveaux prix réels à intégrer dans la grille de confirmation TRADEX. Pour GC/CL sur NT8, les high/low de session RTH précédente sont des niveaux de référence valides.
*Catégorie : structure_marche*

### D7453 — Les nombres ronds EURUSD ne sont PAS statistiquement significatifs
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Test sur 1 535 traders / 20 charts EURUSD 5min : 5 des 10 tests ont des intervalles de confiance qui tombent dans la bande 50% ± 10%, et 2 touchent exactement 50%. Les traders ne montrent pas de préférence claire pour les vrais niveaux de nombres ronds.
**TRADEX-AI C1** : Les nombres ronds sur les actifs TRADEX (ex. GC à 2000$, CL à 80$) ne doivent PAS être traités comme des niveaux de support/résistance primaires — utiliser uniquement les pivots Belkhayate calculés et les niveaux de structure de marché réels.
*Catégorie : structure_marche*

### D7454 — Forte préférence pour niveaux S&P (magnitude, pas seulement fréquence)
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Pour S&P 500, non seulement la fréquence de bonne réponse dépasse 50%, mais la magnitude de la préférence est également forte — un seul intervalle de confiance touche la bande ±10% autour de 50% pour ES, contre 5 sur 10 pour EURUSD.
**TRADEX-AI C1** : Le signal de respect d'un niveau high/low session précédente sur ES est un signal de confirmation fort (C2 dans la grille /10 TRADEX) — sa valeur est supérieure à celle d'un niveau de nombre rond ou d'une moyenne mobile simple.
*Catégorie : structure_marche*

### D7455 — L'échantillon de 20 charts est insuffisant pour conclusions fermes
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Les 20 charts du test constituent un échantillon relativement petit — probablement insuffisant pour des conclusions fermes. Les vrais tests devraient utiliser des centaines de charts pour éliminer l'effet du hasard dans la construction du test.
**TRADEX-AI C1** : Les règles KB basées sur des études avec N < 50 occurrences doivent être taguées ⏳ VOLATILE dans la Knowledge Base — elles guident mais ne constituent pas des règles déterministes.
*Catégorie : configuration*

### D7456 — Les bons exemples sélectionnés manuellement invalident les études
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Si les exemples de charts sont choisis soigneusement (non aléatoirement), n'importe quel résultat désiré peut être obtenu. La randomisation est indispensable pour éliminer l'influence de l'expérimentateur.
**TRADEX-AI C1** : Lors de la validation manuelle de règles KB candidates dans validation/, vérifier que les exemples de confirmation ne sont pas cherry-pickés — exiger un scan exhaustif sur une période complète (ex. 12 mois) plutôt que des exemples isolés convaincants.
*Catégorie : configuration*

### D7457 — Les lignes aléatoires semblent toujours fonctionner sur certains charts
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Des lignes purement aléatoires auront l'air très convaincantes sur certains charts — et sur presque tous les charts, elles sembleront fonctionner modérément. C'est un biais cognitif fondamental dans l'analyse technique.
**TRADEX-AI C1** : Ne jamais valider un niveau Belkhayate (pivot, COG, niveau énergie) uniquement parce qu'il "a l'air de fonctionner" sur 3-5 exemples visuels — exiger un test quantitatif sur au moins 30 occurrences avant intégration en règle VALIDE.
*Catégorie : psychologie*

### D7458 — S&P 500 high/low session précédente : surveiller activement ces niveaux
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Recommandation pratique directe : si vous tradez le S&P, connaître chaque jour le high/low session précédente ET le high/low Globex (overnight), et surveiller ces niveaux tout au long de la séance. Prendre des profits partiels dans ces niveaux est une bonne pratique.
**TRADEX-AI C1/C2** : Pour ES (actif confirmation), paramétrer NT8 pour afficher automatiquement les lignes high/low RTH précédent + high/low Globex. Ces niveaux doivent apparaître dans le contexte envoyé à Claude pour l'analyse — ils constituent des zones de take profit partiel réelles.
*Catégorie : gestion_position_active*

### D7459 — Repenser les nombres ronds en EURUSD : les supprimer aide le trading
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : Pour les traders court terme EURUSD : retirer les lignes de nombres ronds des charts et éliminer toute pensée sur le price action autour de ces niveaux ne nuira probablement pas et pourrait améliorer le trading.
**TRADEX-AI C7** : Dans les corrélations de change (6J — Yen référence), ne pas utiliser les niveaux de nombres ronds comme niveaux de référence pour les corrélations — utiliser uniquement les structures de marché (hauts/bas majeurs, zones de consolidation).
*Catégorie : correlations*

### D7460 — Résultats de niveau surprenants pour le chercheur lui-même
🟡 **SYNTHÈSE** (Source : what_we_learned_about_price_levels.md) : Adam Grimes s'attendait à écrire "nous n'avons rien trouvé d'intéressant" — les résultats l'ont surpris. La forte significance statistique pour les niveaux S&P 500 est "suffisamment suggestive pour changer son approche pédagogique".
**TRADEX-AI C1** : Cette confirmation externe par un praticien sceptique renforce la valeur des pivots de session dans la méthode Belkhayate — les niveaux Belkhayate (BGC, niveaux COG) ont une base empirique sérieuse au-delà de la tradition.
*Catégorie : structure_marche*

### D7461 — Biais cognitif de confirmation dans l'analyse des niveaux de prix
🟢 **FAIT VÉRIFIÉ** (Source : what_we_learned_about_price_levels.md) : L'exemple du chart 2/6/2018 montre que 86% des répondants ont préféré les niveaux "fake" (décalés) aux niveaux réels — démontrant que la conviction visuelle n'est pas un indicateur fiable de la validité d'un niveau.
**TRADEX-AI C1** : En mode Manuel, Abdelkrim doit être informé que sa perception visuelle d'un niveau "fort" peut être un biais cognitif — le cerveau Claude fournit une évaluation objective basée sur la KB, pas sur l'apparence visuelle du chart.
*Catégorie : psychologie*

