# Extraction Optimus — How To Trade Fair Value Gaps
**Source :** `bundles/optimusfutures/how_to_trade_fair_value_gaps.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image scrappée · 0/0 certifiées · 0 à vérifier
**Décisions :** D8531 → D8550 · **Page :** https://optimusfutures.com/blog/how-to-trade-fair-value-gaps/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Les Fair Value Gaps (FVG) définissent des zones de déséquilibre prix exploitables sur GC/CL/HG/ZW — alimente C1 Prix et C2 Order Flow.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image scrappée — bundle texte uniquement) | — | — | — |

## DÉCISIONS

### D8531 — Définition FVG : gap causé par déséquilibre acheteurs/vendeurs
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Un Fair Value Gap (FVG) est un gap de prix créé quand les forces acheteuses et vendeuses sont fortement déséquilibrées. Causes typiques : event macro majeur, publication de données économiques, gros trades institutionnels.
**TRADEX-AI C1** : Le FVG est une structure de prix (C1) directement lisible sur NT8. Sur GC (or), les FVGs apparaissent souvent après les publications NFP/FOMC/CPI — coïncide avec le News Gate de TRADEX.
*Catégorie : structure_marche*

### D8532 — Identification FVG : large bougie dont les mèches voisines ne couvrent pas entièrement l'espace
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Un FVG se repère sur le chart par une grande bougie dont les mèches haute et basse des bougies adjacentes ne couvrent pas complètement la bougie centrale. L'espace entre les mèches adjacentes = le FVG.
**TRADEX-AI C1** : Règle d'identification objective applicable en lecture automatique du flux NT8. À implémenter comme pattern dans la couche structure_marche du moteur Claude.
*Catégorie : structure_marche*

### D8533 — Distinction FVG vs petit gap : seul un fort déséquilibre crée un FVG
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Tous les gaps ne sont pas des FVGs. Un gap entre deux petites bougies n'est pas un FVG car le déséquilibre acheteurs/vendeurs n'est pas suffisant. Seuls les grands gaps spanning plusieurs bougies qualifient.
**TRADEX-AI C1** : Règle de filtrage pour éviter les faux positifs. Le moteur Python de TRADEX doit appliquer un seuil de taille minimale (en ticks/points) pour labelliser un gap comme FVG sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D8534 — FVG présent sur tous les timeframes, plus fréquent sur daily/weekly
🟡 **SYNTHÈSE** (Source : how_to_trade_fair_value_gaps.md) : Les FVGs se trouvent sur tous les timeframes, mais sont les plus communs et significatifs sur les charts daily et weekly. Sur des timeframes courts, ils sont plus nombreux mais moins fiables.
**TRADEX-AI C1** : En TRADEX (range bars NT8), les FVGs sur daily/weekly sont des niveaux de support/résistance structurels à intégrer dans les pivots Belkhayate. Poids supérieur aux FVGs intraday.
*Catégorie : timing*

### D8535 — FVGs peuvent être comblés ou ne jamais se combler
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Un FVG peut être comblé (le prix revient couvrir la zone) ou rester ouvert si le marché continue dans la direction initiale sans retracement. Les deux scénarios existent et aucun n'est universel.
**TRADEX-AI C1** : Règle de gestion du risque : un signal FVG n'est valide que si le prix commence à retracer vers la zone. Attendre la confirmation du retracement avant d'entrer — cohérent avec la règle "wait for confirmation" de la méthode Belkhayate.
*Catégorie : gestion_risque_entree*

### D8536 — Stratégie "Buy the Gap" : entrée au niveau du FVG, sortie au retour au gap
🟡 **SYNTHÈSE** (Source : how_to_trade_fair_value_gaps.md) : La stratégie la plus commune : acheter au niveau du FVG (prix qui revient dans la zone), cibler un retour complet au gap. Exemple cité : sur ES (1h chart), approche mesurée 2:1 R/R pour les traders court terme, ou objectif au précédent high pour les traders long terme.
**TRADEX-AI C1** : Sur GC, utiliser le FVG comme zone d'entrée potentielle avec objectif mesuré (2:1 R/R minimum — cohérent avec la règle TRADEX R/R ≥ 1:2). Le stop est placé sous/sur la zone FVG.
*Catégorie : gestion_risque_entree*

### D8537 — FVG comme zone de support/résistance future
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Un FVG comblé peut agir comme support (si gap haussier) ou résistance (si gap baissier) lors de prochaines approches du prix. Example : gap-up, retrace vers zone → zone devient support pour re-entrée haussière.
**TRADEX-AI C1** : Les zones FVG sont à ajouter dans la grille des niveaux S/R Belkhayate (avec pivots). Un FVG ancien sur GC daily peut être un niveau de référence pour la gestion de position (C1).
*Catégorie : structure_marche*

### D8538 — Stratégie "Short the Gap" : miroir baissier du Buy the Gap
🔵 **ÉCOLE** (Source : how_to_trade_fair_value_gaps.md) : Le FVG baissier peut être tradé en short : vendre au niveau du FVG quand le prix retrace dans la zone après un gap-down, couvrir le short quand le prix revient dans le gap. Moins fréquent mais applicable.
**TRADEX-AI C1** : Sur CL (pétrole), les FVGs baissiers sont fréquents après des events géopolitiques (C6). La logique short FVG est applicable en mode VENDRE avec les mêmes règles R/R ≥ 1:2.
*Catégorie : configuration*

### D8539 — Confirmation obligatoire avant entrée sur FVG
🟢 **FAIT VÉRIFIÉ** (Source : how_to_trade_fair_value_gaps.md) : Avant d'entrer sur un FVG, attendre une confirmation que le prix va réellement retracer vers la zone. Un signal de reversal (bougie de renversement haussière ou baissière) au niveau du gap est le déclencheur recommandé.
**TRADEX-AI C1** : Règle de confirmation TRADEX : le FVG seul (C1) ne suffit pas à déclencher un signal. Il doit être confirmé par Order Flow (C2 : delta renversement) et/ou momentum (indicateur Belkhayate). Cohérent avec la règle 3/4 + 2/3.
*Catégorie : gestion_risque_entree*

### D8540 — Combinaison d'indicateurs pour réduire les faux signaux FVG
🟡 **SYNTHÈSE** (Source : how_to_trade_fair_value_gaps.md) : Utiliser plusieurs indicateurs en combinaison avec les FVGs réduit les faux signaux. Un seul indicateur n'est pas suffisant. L'utilisation de stop-loss est obligatoire. La patience est requise : attendre le bon setup.
**TRADEX-AI C1** : Principe multi-cercles de TRADEX : FVG (C1) + Delta/Volume (C2) + contexte macro (C4) + VIX (C5). L'approche multi-cercles de TRADEX est conceptuellement alignée avec ce principe de confirmation multiple.
*Catégorie : psychologie*
