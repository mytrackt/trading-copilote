# Extraction AdamGrimes — The Two Forces
**Source :** `bundles/adamgrimes/the_two_forces.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6931 → D6950 · **Page :** https://www.adamhgrimes.com/the-two-forces/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Deux forces fondamentales (mean reversion + momentum) structurent toute action des prix — base théorique pour filtrer les signaux TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6931 — Les deux forces fondamentales du marché
🟢 **FAIT VÉRIFIÉ** (Source : the_two_forces.md) : Toute l'action des prix repose sur deux forces opposées — mean reversion (tendance des grands mouvements à être inversés) et momentum (tendance des grands mouvements à se prolonger). Ces deux forces sont généralement en équilibre ; le marché se déplace de façon quasi-aléatoire sauf lorsque l'une des deux forces domine.
**TRADEX-AI C1** : Avant tout signal, classifier l'environnement de prix comme dominé par le mean reversion ou le momentum. Si l'environnement est ambigu (équilibre), la réponse par défaut est ATTENDRE.
*Catégorie : structure_marche*

### D6932 — Patterns de mean reversion : fading des grandes barres
🔵 **ÉCOLE** (Source : the_two_forces.md) : Le mean reversion se traduit par des opportunités de fade (contre-tendance) sur : (1) grande barre individuelle isolée, (2) série de barres avec grand déplacement de prix, (3) N clôtures consécutives dans la même direction, (4) N-day high/low (breakouts de canal), (5) grands écarts par rapport à la moyenne mobile.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, une barre anormalement grande par rapport à l'ATR moyen déclenche une alerte mean reversion — le signal momentum associé doit être traité avec méfiance jusqu'à confirmation de continuation.
*Catégorie : configuration*

### D6933 — Patterns de momentum : compression de volatilité
🔵 **ÉCOLE** (Source : the_two_forces.md) : Le momentum se manifeste préférentiellement dans deux contextes : (1) après une compression de volatilité (contraction avant expansion) — entrée dans la direction de la sortie ; (2) après un grand mouvement suivi d'un pullback (retracement de mean reversion) — entrée dans la direction du grand mouvement initial.
**TRADEX-AI C1** : La compression de volatilité sur GC/HG/CL/ZW (range étroit sur N barres) est un précurseur de signal momentum. Associer à C5 (VX) et C2 (OrderFlow delta) pour confirmer la direction de la sortie.
*Catégorie : indicateurs_momentum*

### D6934 — Le concept de "large" comme filtre de validité
🟡 **SYNTHÈSE** (Source : the_two_forces.md) : Le mot "large" revient systématiquement dans les setups de mean reversion. Identifier les mouvements "outsized" (hors norme par rapport à l'environnement récent) est la compétence fondamentale. Sans ce calibrage, les signaux mean reversion sont non fiables.
**TRADEX-AI C1** : Définir pour chaque actif tradable (GC, HG, CL, ZW) un seuil ATR dynamique (ex. 1,5× ATR 14 barres) au-dessous duquel aucun setup mean reversion n'est déclenché.
*Catégorie : gestion_risque_entree*

### D6935 — Équilibre de marché = état par défaut
🟢 **FAIT VÉRIFIÉ** (Source : the_two_forces.md) : Les deux forces (mean reversion et momentum) sont habituellement en équilibre, ce qui produit un mouvement essentiellement aléatoire. Un edge existe uniquement lorsqu'on identifie des patterns montrant qu'une des deux forces va dominer sur un timeframe précis.
**TRADEX-AI C1** : TRADEX-AI ne doit émettre un signal ACHETER ou VENDRE que lorsqu'un pattern identifiable montre la domination probable d'une des deux forces. En absence de pattern clair, la décision est ATTENDRE. Ceci renforce la règle 3/4 trading + 2/3 confirmation.
*Catégorie : gestion_risque_entree*

### D6936 — Pullback comme condition d'entrée momentum
🔵 **ÉCOLE** (Source : the_two_forces.md) : Pour les setups momentum via pullback : (1) un grand mouvement directionnel survient, (2) le mean reversion s'installe (pullback), (3) on entre dans la direction du grand mouvement initial. L'entrée n'est PAS au sommet du grand mouvement mais après le pullback correctif.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, un grand mouvement directionnel suivi d'un pullback de 38–61,8% (Fibonacci) constitue une zone d'entrée momentum prioritaire. Confirmer avec C2 (delta OrderFlow positif sur la reprise) avant déclenchement.
*Catégorie : gestion_risque_entree*

### D6937 — Framework binaire mean reversion / momentum pour tout pattern
🟡 **SYNTHÈSE** (Source : the_two_forces.md) : Tout pattern technique peut être reclassifié dans l'un des deux cadres (mean reversion ou momentum). Cette recatégorisation simplifie la lecture du marché et améliore la cohérence des décisions : on sait toujours quelle force on cherche à exploiter.
**TRADEX-AI C1** : Lors de l'analyse Claude Brain, chaque signal doit être labellisé MOMENTUM ou MEAN_REVERSION. Les deux labels ne peuvent pas coexister sur le même signal au même moment. Cela force la cohérence logique du prompt.
*Catégorie : structure_marche*
