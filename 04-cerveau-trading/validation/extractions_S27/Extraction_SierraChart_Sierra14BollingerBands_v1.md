# Extraction SierraChart — Bollinger Bands
**Source :** `bundles/sierrachart/sierra_14_bollinger_bands.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8951 → D8970 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=14
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Bollinger Bands (SMA ± k·σ) — indicateur de volatilité configurable utilisable sur GC/HG/CL/ZW pour détecter compression/expansion et filtrer entrées.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D8951 — Formule Bollinger Bands : Top Band
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : La bande supérieure est calculée comme TB = SMA(n) + v·σ(n), où n = Length (période) et v = Standard Deviations (multiplicateur d'écart-type).
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, le franchissement de la bande supérieure indique une extension de volatilité haussière — à croiser avec Énergie Belkhayate avant entrée long.
*Catégorie : indicateurs_tendance*

### D8952 — Formule Bollinger Bands : Middle Band
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : La bande médiane est la simple Moving Average : MB = SMA(n). Elle constitue le niveau de référence dynamique de l'indicateur.
**TRADEX-AI C1** : Le retour vers la bande médiane (mean reversion) est un signal de neutralisation de la pression directionnelle — utile comme cible TP partielle en mode Manuel.
*Catégorie : indicateurs_tendance*

### D8953 — Formule Bollinger Bands : Bottom Band
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : La bande inférieure est BB = SMA(n) - v·σ(n). La symétrie avec la bande supérieure assure que le prix évolue à l'intérieur des bandes ~95% du temps pour v=2 (loi normale).
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, le test de la bande inférieure avec rebond est un signal potentiel de retournement haussier — nécessite confirmation C2 (delta) avant entrée.
*Catégorie : indicateurs_tendance*

### D8954 — Paramètre Length (période)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : Le paramètre Length définit la période n du SMA et de l'écart-type. La valeur standard communément utilisée est 20 périodes. Toute modification de Length change simultanément la sensibilité de la bande médiane et la largeur des bandes.
**TRADEX-AI C1** : Sur range bars NT8 pour GC (Or), Length=20 est le point de départ recommandé — à calibrer lors de la Phase C avec données réelles.
*Catégorie : indicateurs_tendance*

### D8955 — Paramètre Standard Deviations (multiplicateur)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : Le paramètre Standard Deviations (v) est le multiplicateur appliqué à l'écart-type pour définir la largeur des bandes. La valeur par défaut est typiquement 2.0.
**TRADEX-AI C1** : v=2.0 couvre ~95% de la distribution normale. Pour les marchés des matières premières (GC/CL) à forte volatilité, un v=2.5 peut être nécessaire pour réduire les faux signaux.
*Catégorie : indicateurs_tendance*

### D8956 — Paramètre Moving Average Type
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : Le paramètre Moving Average Type permet de substituer le SMA par : Exponential Moving Average (EMA), Linear Regression MA, Weighted MA, Wilders MA, SMA-Skip Zeros, ou Smoothed MA. La formule de base utilise le SMA.
**TRADEX-AI C1** : L'utilisation d'une EMA à la place du SMA rend les bandes plus réactives aux mouvements récents — pertinent sur CL (pétrole) à forte dynamique intraday.
*Catégorie : indicateurs_tendance*

### D8957 — Paramètre Input Data
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : Le paramètre Input Data détermine quelle série de prix est utilisée pour les calculs (Close, High, Low, HL2, HLC3, OHLC4, etc.). La valeur par défaut standard est le Close (Last Price).
**TRADEX-AI C1** : Utiliser Close pour la cohérence avec les autres indicateurs TRADEX-AI. Sur footprint (ATAS), envisager HL2 pour capturer l'amplitude de la barre.
*Catégorie : indicateurs_tendance*

### D8958 — Interprétation : Compression des bandes (Squeeze)
🔵 **ÉCOLE** (Source : sierra_14_bollinger_bands.md) : Quand les bandes se resserrent (faible écart-type = faible volatilité), cela signifie une phase de compression précédant souvent un mouvement directionnel fort. Ce phénomène est connu sous le nom de "Bollinger Squeeze".
**TRADEX-AI C1** : Un squeeze sur GC ou CL, combiné avec un signal Belkhayate Direction, est une configuration haute probabilité d'entrée — à valider avec score ≥ 7.0/10.
*Catégorie : configuration*

### D8959 — Interprétation : Expansion des bandes (Breakout)
🔵 **ÉCOLE** (Source : sierra_14_bollinger_bands.md) : Quand le prix casse une bande (close au-delà de la bande supérieure ou inférieure) après une période de compression, c'est une indication d'un mouvement directionnel fort. Le breakout valide la direction.
**TRADEX-AI C1** : Un close au-dessus de la bande supérieure sur ZW (blé) après squeeze constitue un signal de tendance — TRADEX-AI doit croiser avec C3 (COT institutionnels) avant entrée.
*Catégorie : configuration*

### D8960 — Interprétation : Walking the Bands
🔵 **ÉCOLE** (Source : sierra_14_bollinger_bands.md) : En tendance forte, le prix peut "marcher" le long d'une bande (rester proche de la bande supérieure en tendance haussière ou inférieure en tendance baissière) pendant plusieurs barres consécutives. Ce comportement ne constitue PAS un signal de retournement.
**TRADEX-AI C1** : En mode Auto, TRADEX-AI ne doit PAS générer de signal SHORT uniquement parce que le prix touche la bande supérieure — nécessite confirmation de retournement par C2 (order flow divergence).
*Catégorie : gestion_risque_entree*

### D8961 — Calcul : Écart-type basé sur la même période que le SMA
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : L'écart-type σ est calculé sur la même fenêtre n que le SMA. La formule σ_t(X,n) est la déviation standard de la série X sur les n dernières valeurs. Il n'y a pas de paramètre séparé pour la période de l'écart-type.
**TRADEX-AI C1** : Paramètre unique Length contrôle simultanément MA et σ — garder cette cohérence dans l'implémentation Sierra Chart pour TRADEX-AI afin d'éviter les décalages de signaux.
*Catégorie : indicateurs_tendance*

### D8962 — Disponibilité : Format Spreadsheet Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_14_bollinger_bands.md) : Sierra Chart fournit les formules Bollinger Bands dans un fichier spreadsheet `Bollinger_Bands.14.scss` accessible depuis File >> Open Spreadsheet. Ce fichier contient l'implémentation complète exportable.
**TRADEX-AI C1** : Pour validation des calculs TRADEX-AI contre la référence Sierra Chart, utiliser ce fichier .scss comme source de vérité lors de la Phase C (collecteurs NT8/ATAS).
*Catégorie : indicateurs_tendance*

### D8963 — Lien avec la méthode Belkhayate : Bollinger comme filtre volatilité
🟡 **SYNTHÈSE** (Source : sierra_14_bollinger_bands.md) : Les Bollinger Bands mesurent la volatilité relative du marché. La méthode Belkhayate utilise l'Énergie comme proxy de volatilité directionnelle. Les deux approches sont complémentaires : Bollinger mesure la dispersion statistique des prix, Belkhayate mesure la force directionnelle.
**TRADEX-AI C1** : Dans TRADEX-AI, Bollinger Bands peuvent servir de filtre de second niveau : bloquer les entrées si les bandes sont trop larges (marché déjà en extension) ou trop serrées (liquidité insuffisante).
*Catégorie : gestion_risque_entree*

### D8964 — Applicabilité sur actifs TRADEX (GC/HG/CL/ZW)
🟡 **SYNTHÈSE** (Source : sierra_14_bollinger_bands.md) : Les Bollinger Bands s'appliquent à tout actif avec des données OHLCV. Pour les futures matières premières (GC, HG, CL, ZW), la configuration Length=20 et v=2.0 constitue une base standard, mais les caractéristiques de volatilité propres à chaque actif nécessitent une calibration spécifique.
**TRADEX-AI C1** : Prévoir 4 configurations distinctes dans settings.py pour GC/HG/CL/ZW avec des valeurs Length et v calibrées sur les données historiques NT8 range bars lors de la Phase C.
*Catégorie : configuration*

### D8965 — Interprétation : Mean Reversion vs Trend Following
🔵 **ÉCOLE** (Source : sierra_14_bollinger_bands.md) : Les Bollinger Bands peuvent être utilisés en stratégie de mean reversion (achat/vente sur les bandes dans un marché en range) ou en suivi de tendance (breakout des bandes en marché tendanciel). Ces deux approches sont contradictoires et nécessitent un filtre de contexte de marché.
**TRADEX-AI C1** : TRADEX-AI utilise le BGC (Belkhayate Gravity Center) comme filtre de contexte — si le prix est au-dessus du BGC, privilégier les signaux dans le sens de la tendance plutôt que le mean reversion.
*Catégorie : gestion_risque_entree*
