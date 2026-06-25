# Extraction AdamGrimes — Chart of the Day: Managing the Failure Test in AAPL
**Source :** `bundles/adamgrimes/chart_of_the_day_managing_the_failure_test_in_aapl.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5491 → D5502 · **Page :** https://www.adamhgrimes.com/chart-of-the-day-managing-the-failure-test-in-aapl/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : gestion active d'un trade Failure Test — stop trailing, prises de profit partielles, confiance dans signal non populaire.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D5491 — Meilleurs trades se forment dans l'indifférence générale
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Adam Grimes affirme que "le meilleur trade technique se met en place quand personne ne regarde." Le bruit médiatique et les réseaux sociaux créent le groupthink ; le trade optimal se forme dans l'indifférence collective, pas pendant les discussions généralisées.
**TRADEX-AI C5** : Un signal TRADEX généré loin du consensus médiatique et des discussions sociales actives est statistiquement plus fiable. Ne pas filtrer un signal valide parce qu'il est "impopulaire" sur les réseaux.
*Catégorie : psychologie*

### D5492 — Groupthink social media dégrade la qualité des décisions de trading
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Les médias sociaux amplifient le groupthink. Les traders qui suivent le consensus médiatique entrent trop tard sur les rebonds évidents, ratant le vrai setup qui se forme dans le calme.
**TRADEX-AI C5** : Le moteur ne doit pas tenir compte des signaux "chauds" ou médiatiquement couverts comme filtre positif. Le sentiment populaire est un filtre négatif potentiel (C5 Sentiment).
*Catégorie : psychologie*

### D5493 — Entrée Failure Test : close du jour du signal, pas le lendemain
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : L'entrée correcte sur un Failure Test est le close du jour où le pattern se forme. Attendre le lendemain = manquer l'entrée car gap up sans retour.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, un Failure Test doit être entré au close de la bougie de signal. Tout retard expose au gap d'ouverture avec une entrée dégradée.
*Catégorie : gestion_risque_entree*

### D5494 — Stop trailing après Failure Test : tightening actif sous l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Une fois le trade lancé et en profit, le stop doit être remonté légèrement sous le point d'entrée. Le tightening actif est une composante clé de la gestion de trade, pas optionnel.
**TRADEX-AI C1** : En mode Auto, après déclenchement d'un signal Failure Test, programmer le stop trailing immédiatement après entrée exécutée. Ne pas laisser le stop initial fixe.
*Catégorie : gestion_position_active*

### D5495 — Tightening excessif du stop = erreur émotionnelle
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Trop serrer le stop est une erreur. Le tightening doit répondre à des "probabilités changeantes", pas à la peur ou aux émotions du trader. Sur-tightening = sortie prématurée.
**TRADEX-AI C1** : Le moteur doit appliquer un tightening basé sur des règles déterministes (ex : ATR, niveaux pivot) et non sur le temps écoulé ou la volatilité momentanée. Garde-fou contre le tightening émotionnel.
*Catégorie : gestion_position_active*

### D5496 — Profits partiels obligatoires à 1× le risque initial
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : La discipline de prise de profit partielle à 1× le risque initial est obligatoire dans la méthode Grimes. Ce niveau doit être calculé dès l'entrée et exécuté systématiquement.
**TRADEX-AI C1** : Sur tout signal TRADEX, calculer TP1 = entrée + 1× (entrée − stop). Exécution automatique en mode Auto. Affichage obligatoire dans le dashboard en mode Manuel.
*Catégorie : gestion_position_active*

### D5497 — Connaissance des patterns + probabilités = confiance dans l'opinion impopulaire
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : La connaissance des patterns et des probabilités associées donne au trader la confiance nécessaire pour exécuter un trade contre le consensus. Sans cette base, le trader hésite et rate l'entrée.
**TRADEX-AI C1** : La KB Belkhayate (1313+ règles) doit être suffisamment précise pour que le score /10 donne une conviction forte même sur des signaux non consensuels. Valider que la couche C1 couvre les Failure Tests.
*Catégorie : psychologie*

### D5498 — Failure Test : définition pattern (2B short / entrée long)
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Le Failure Test est un pattern où le prix casse brièvement un niveau significatif puis échoue et reverse. Version longue = faux break sous support qui remonte. Version courte (2B) = faux break au-dessus d'une résistance qui retombe.
**TRADEX-AI C1** : Pattern à intégrer dans la grille de détection pour GC/HG/CL/ZW. Applicable sur les niveaux Belkhayate (Pivots, BGC extrêmes). Le faux break doit être confirmé par clôture de bougie.
*Catégorie : configuration*

### D5499 — Le Failure Test nécessite une surveillance continue, pas d'alerte ponctuelle
🟢 **FAIT VÉRIFIÉ** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Grimes note que le setup s'est formé "hier" (veille) sans que personne ne l'observe. Ce pattern requiert une surveillance continue des niveaux clés, pas un monitoring réactif post-événement.
**TRADEX-AI C1** : La boucle Python 2s de surveillance NT8 est justifiée pour détecter les Failure Tests en temps réel. Ne pas se fier aux alertes externes ou aux discussions post-facto.
*Catégorie : structure_marche*

### D5500 — Référence livre : Art & Science of Technical Analysis pour les Failure Tests
🔵 **ÉCOLE** (Source : chart_of_the_day_managing_the_failure_test_in_aapl.md) : Adam Grimes documente de nombreux exemples de Failure Tests avec probabilités dans son livre "The Art & Science of Technical Analysis". Source primaire pour l'approfondissement du pattern.
**TRADEX-AI C1** : Source KB à intégrer si disponible. Les statistiques de réussite du Failure Test issues de ce livre renforcent la grille de scoring /10.
*Catégorie : configuration*
