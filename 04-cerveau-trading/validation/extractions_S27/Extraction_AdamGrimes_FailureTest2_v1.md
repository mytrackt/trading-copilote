# Extraction AdamGrimes — The Failure Test
**Source :** `bundles/adamgrimes/failure_test_2.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5731 → D5750 · **Page :** https://www.adamhgrimes.com/failure-test-2/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le Failure Test (faux breakout) est un pattern court-terme Belkhayate-compatible pour entrées contre-tendance sur niveaux clés GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image extraite dans ce bundle | — | — |

## DÉCISIONS

### D5731 — Définition du Failure Test (faux breakout)
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Le Failure Test se produit quand un marché dépasse un pivot (ou zone S/R) puis revient immédiatement en sens inverse. Synonymes : "2B" (Sperandeo), "spring" (Wyckoff, test sous support), "upthrust" (Wyckoff, test au-dessus d'une résistance).
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, tout faux breakout au-delà d'un pivot Belkhayate suivi d'une reprise immédiate constitue un signal Failure Test — à surveiller comme entrée possible.
*Catégorie : structure_marche*

### D5732 — Règle d'entrée SHORT sur Failure Test résistance
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Entrée short optimale : le prix casse au-dessus de la résistance et échoue à fermer au-dessus sur la même bougie → entrer short à la clôture de cette bougie avec stop juste au-dessus du plus haut. Alternative : la bougie suivante redescend sous la résistance → même logique de stop au-delà du nouveau plus haut.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, si le prix franchit un pivot Belkhayate haut et que la clôture revient en dessous, signal SHORT valide avec stop au-dessus du chandelier de rupture.
*Catégorie : gestion_risque_entree*

### D5733 — Règle d'entrée LONG sur Failure Test support
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Entrée long : identique mais inversée — test sous support suivi d'une clôture au-dessus → entrer long à la clôture avec stop juste en dessous du plus bas du test.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, si le prix viole un support Belkhayate (pivot bas) et clôture au-dessus, signal LONG avec stop sous le plus bas du test.
*Catégorie : gestion_risque_entree*

### D5734 — Logique de marché : le marché cherche les stops
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Les marchés sont conçus pour créer du volume d'échanges — ils cherchent naturellement les niveaux où des ordres sont concentrés (stops clustered). Un Failure Test exploite cette tendance en se positionnant contre le mouvement de chasse aux stops avec un risque clairement défini.
**TRADEX-AI C2** : Sur ATAS, surveiller l'absorption au-delà des pivots (delta négatif sur clôtures en dehors du range) pour confirmer un Failure Test — le volume sans conviction au-delà du niveau confirme le piège.
*Catégorie : structure_marche*

### D5735 — Deux contextes d'application du Failure Test
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Grimes utilise le Failure Test dans deux contextes : (1) en range, sur les tests purs de support/résistance ; (2) en tendance, comme entrée contre-tendance pour tenter de capter le retournement au sommet d'une hausse ou au bas d'une baisse.
**TRADEX-AI C1** : Pour GC/CL surtout, distinguer si le Failure Test est en range (fiabilité élevée) ou contre-tendance forte (risque accru) — ajuster la taille de position en conséquence.
*Catégorie : configuration*

### D5736 — Gestion du risque spécifique au Failure Test : taille réduite
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : En range, la liquidité peut être faible → gap contre la position possible à l'ouverture. En tendance, le "gap and go" au-delà du stop est possible et ne se renverse généralement pas. Recommandation : trader ce setup avec une taille inférieure aux autres setups habituels.
**TRADEX-AI C1** : Règle risque TRADEX — sur Failure Test, limiter l'exposition à 50% de la taille standard ; si ouverture adverse, réduire immédiatement.
*Catégorie : gestion_risque_entree*

### D5737 — Réaction adversaire à l'ouverture : agir immédiatement
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Si l'ouverture est adverse (gap contre la position), agir immédiatement car la situation tend à s'aggraver tout au long de la session. Ne pas tenir une position en Failure Test contre un gap d'ouverture en espérant un retour.
**TRADEX-AI C1** : Règle gestion position TRADEX — sur Failure Test, une ouverture gap adverse = sortie immédiate, pas d'attente de retracement.
*Catégorie : gestion_position_active*

### D5738 — Utilité défensive du Failure Test pour détenteurs de position
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Même sans intention de shorter, un investisseur qui voit son actif tenter un breakout au-dessus d'anciens plus hauts et échouer (Failure Test) peut utiliser ce signal pour prendre des bénéfices partiels et affiner sa sortie.
**TRADEX-AI C1** : En mode Manuel, si GC/HG/CL/ZW est en position longue et que le prix forme un Failure Test haut, l'afficher comme signal de prise de profit partielle — pas forcément un short.
*Catégorie : gestion_position_active*

### D5739 — Étude des patterns perdants : nécessité pédagogique
🔵 **ÉCOLE** (Source : failure_test_2.md) : Grimes insiste : étudier de nombreux exemples de patterns qui ont échoué (loser patterns). Au point B (test bas), un long entré sur Failure Test peut très bien être perdant. La conscience des deux issues possibles est indispensable.
**TRADEX-AI C1** : Dans le moteur TRADEX, un Failure Test identifié n'est PAS un signal automatique — il doit être confirmé par d'autres cercles (C2 volume, C4 macro) avant d'être élevé en signal.
*Catégorie : psychologie*

### D5740 — Applicabilité multi-timeframe du Failure Test
🟢 **FAIT VÉRIFIÉ** (Source : failure_test_2.md) : Le Failure Test fonctionne sur tous les timeframes, pour traders et investisseurs — c'est un pattern structurellement robuste indépendant de la résolution temporelle.
**TRADEX-AI C1** : Valider un Failure Test sur le timeframe principal (range bars NT8) ET confirmer sur le timeframe supérieur (daily) pour les actifs GC/HG/CL/ZW avant déclenchement.
*Catégorie : configuration*
