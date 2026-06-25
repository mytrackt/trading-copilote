# Extraction SierraChart — Stochastic RSI
**Source :** `bundles/sierrachart/sierra_180_stochrsi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9011 → D9030 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=180
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Stochastic RSI — oscillateur momentum double-stochastique calculé sur Close Price, plus sensible que le RSI classique, utile pour détecter les zones de sur-extension sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans le bundle | — | — |

## DÉCISIONS

### D9011 — Définition Stochastic RSI : oscillateur sur le RSI
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : Le Stochastic RSI calcule et affiche le stochastique du RSI basé sur les données de prix Close (Last). Le RSI est utilisé dans le calcul. Il s'agit d'un oscillateur appliquant la formule stochastique au RSI plutôt qu'aux prix directs.
**TRADEX-AI C1** : Le StochRSI est plus sensible et réactif que le RSI classique car il applique une normalisation stochastique à un oscillateur déjà normalisé. Sur GC/HG/CL/ZW, utile pour détecter les extrêmes de momentum intraday avant retournement.
*Catégorie : indicateurs_momentum*

### D9012 — Formule StochRSI : application du stochastique au RSI
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : La formule est : StochRSI_t(n_RSI, n_HL) = (RSI_t - MinRSI_{n_HL}) / (MaxRSI_{n_HL} - MinRSI_{n_HL}). Où MinRSI et MaxRSI sont le minimum et maximum du RSI calculés sur les n_HL dernières barres (RSI HighestLowest Length).
**TRADEX-AI C1** : La normalisation [0,1] (ou [0,100]) du StochRSI facilite les comparaisons inter-actifs. Pour TRADEX-AI, utiliser les seuils 0.20/0.80 (ou 20/80) comme zones de sur-vente/sur-achat sur tous les actifs GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

### D9013 — Paramètre RSI Length (n_RSI)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : Le paramètre RSI Length (noté n_RSI) définit la période du RSI de base utilisé dans le calcul du StochRSI. C'est la période du RSI de Wilder appliqué au Close Price.
**TRADEX-AI C1** : RSI Length standard = 14 périodes (Wilder). Sur range bars NT8 pour futures matières premières, 14 est un bon point de départ. Valeurs courantes alternatives : 9 (plus réactif) ou 21 (plus stable). Fixer à 14 par défaut dans settings.py.
*Catégorie : indicateurs_momentum*

### D9014 — Paramètre RSI Average Type
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : Le paramètre Average Type détermine le type de Moving Average utilisé dans les calculs RS et RSI-bar-smoothing du StochRSI. Ce paramètre unique contrôle TOUTES les trois moyennes mobiles internes du calcul. Options : SMA, EMA, Linear Regression MA, Weighted MA, Wilders MA, SMA-Skip Zeros, Smoothed MA.
**TRADEX-AI C1** : La documentation précise explicitement que "les types des trois MA dans le calcul sont déterminés par ce seul paramètre". Utiliser Wilders MA (cohérent avec la méthode RSI originale de Wilder) pour la fidélité à la formule classique.
*Catégorie : indicateurs_momentum*

### D9015 — Paramètre RSI HighestLowest Length (n_HL)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : Le paramètre RSI HighestLowest Length (noté n_HL) définit la fenêtre sur laquelle le maximum et le minimum du RSI sont calculés pour la normalisation stochastique. Le StochRSI commence à être calculé pour t ≥ n_RSI + n_HL - 1.
**TRADEX-AI C1** : RSI HighestLowest Length standard = 14 périodes. Plus n_HL est petit, plus le StochRSI oscille rapidement entre 0 et 1 (signaux fréquents mais plus de bruit). Sur CL (pétrole, volatilité élevée), envisager n_HL=10 pour une meilleure réactivité.
*Catégorie : indicateurs_momentum*

### D9016 — Délai de calcul : n_RSI + n_HL - 1 barres minimum
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : Le StochRSI commence à être calculé uniquement à partir de l'index t ≥ n_RSI + n_HL - 1. Avec les valeurs standard (14+14-1=27), il faut 27 barres minimum avant d'obtenir une valeur StochRSI valide.
**TRADEX-AI C1** : Warmup minimum = 27 barres (paramètres standard 14,14). Plus faible que l'ADXR (40 barres) — avantage du StochRSI en termes de disponibilité rapide après démarrage. Implémenter vérification warmup dans le moteur Python.
*Catégorie : gestion_risque_entree*

### D9017 — Données source : Close (Last) Price uniquement
🟢 **FAIT VÉRIFIÉ** (Source : sierra_180_stochrsi.md) : La documentation Sierra Chart précise explicitement que le Stochastic RSI est calculé sur les données de prix "Close (Last) Price". Il n'y a pas d'option pour changer l'Input Data contrairement aux Bollinger Bands (ID=14).
**TRADEX-AI C1** : Le StochRSI Sierra Chart est basé uniquement sur le Close — cohérent avec l'utilisation standard. Pour TRADEX-AI, s'assurer que la série Close fournie par NT8 est bien le Close de la barre range (dernier prix de la barre), pas un prix typique composite.
*Catégorie : indicateurs_momentum*

### D9018 — Interprétation : zones de sur-achat et sur-vente
🔵 **ÉCOLE** (Source : sierra_180_stochrsi.md) : Le StochRSI oscille entre 0 et 1 (ou 0-100 selon l'implémentation). Les zones standard sont : > 0.80 (80) = sur-achat, < 0.20 (20) = sur-vente. Ces zones sont plus fréquemment atteintes que les équivalents RSI (70/30) car le StochRSI est normalisé sur son propre range.
**TRADEX-AI C1** : Pour TRADEX-AI : StochRSI > 0.80 = signal potentiel SHORT si aligné avec Belkhayate Direction baissière · StochRSI < 0.20 = signal potentiel LONG si aligné avec Direction haussière. Ne JAMAIS prendre un signal uniquement sur le StochRSI.
*Catégorie : gestion_risque_entree*

### D9019 — Interprétation : divergences StochRSI / prix
🔵 **ÉCOLE** (Source : sierra_180_stochrsi.md) : Les divergences entre le StochRSI et les prix constituent des signaux d'affaiblissement de tendance : prix fait un nouveau sommet mais StochRSI ne confirme pas (divergence baissière) ou prix fait un nouveau creux mais StochRSI remonte (divergence haussière).
**TRADEX-AI C1** : Intégrer la détection de divergence StochRSI/prix dans le moteur TRADEX-AI comme signal de retournement de C1 (confirmation supplémentaire). Divergence baissière sur GC + signal Belkhayate VENDRE = confluence forte.
*Catégorie : configuration*

### D9020 — Comparaison StochRSI vs RSI vs Stochastique classique
🔵 **ÉCOLE** (Source : sierra_180_stochrsi.md) : Le StochRSI combine les propriétés du RSI (mesure de momentum basée sur les variations de prix) et du Stochastique (normalisation sur range haute/basse). Il est plus sensible que le RSI seul (atteint plus souvent les extrêmes) et plus stable que le Stochastique seul (moins affecté par les spikes de prix).
**TRADEX-AI C1** : Pour TRADEX-AI, le StochRSI est préférable au RSI classique comme indicateur de momentum C1 car : (1) atteint plus facilement les zones extrêmes, (2) normalisation [0,1] facilite la comparaison inter-actifs, (3) moins de faux signaux que le Stochastique brut.
*Catégorie : indicateurs_momentum*

### D9021 — Application sur actifs TRADING TRADEX : paramètres recommandés
🟡 **SYNTHÈSE** (Source : sierra_180_stochrsi.md) : Les paramètres standard du StochRSI (RSI Length=14, HL Length=14) sont adaptés aux marchés liquides avec données continues. Pour les futures matières premières, les sessions de nuit et la volatilité spécifique à chaque actif peuvent nécessiter des ajustements.
**TRADEX-AI C1** : Paramétrage proposé par actif : GC (Or) → StochRSI(14,14) standard · HG (Cuivre) → StochRSI(14,14) standard · CL (Pétrole) → StochRSI(10,10) plus réactif · ZW (Blé, moins liquide) → StochRSI(14,21) pour réduire le bruit. À valider Phase C.
*Catégorie : configuration*

### D9022 — Lien avec méthode Belkhayate : confirmation des entrées
🟡 **SYNTHÈSE** (Source : sierra_180_stochrsi.md) : La méthode Belkhayate utilise l'Énergie (force directionnelle) et le BGC pour identifier les zones de trading. Le StochRSI apporte une mesure complémentaire du momentum à court terme. Quand l'Énergie Belkhayate est forte ET le StochRSI confirme la direction (sur-vente en contexte haussier), le signal est plus fiable.
**TRADEX-AI C1** : Dans le score TRADEX-AI /10, le StochRSI peut contribuer au Cercle C1 (Prix) : StochRSI en zone extrême opposée à la tendance Belkhayate = momentum d'entrée favorable (entry timing). Éviter les entrées quand StochRSI est dans la zone neutre (0.40-0.60).
*Catégorie : configuration*

### D9023 — Implémentation Python StochRSI
🟡 **SYNTHÈSE** (Source : sierra_180_stochrsi.md) : La formule StochRSI = (RSI_t - Min_nHL(RSI)) / (Max_nHL(RSI) - Min_nHL(RSI)) est simple à implémenter avec pandas. Étapes : (1) calculer RSI sur n_RSI périodes avec lissage Wilder, (2) calculer rolling max et min du RSI sur n_HL périodes, (3) appliquer normalisation stochastique.
**TRADEX-AI C1** : Ajouter StochRSI dans `05-saas/engine/indicators.py` (à créer Phase C). Utiliser `ta` library (Technical Analysis) ou implémentation custom pandas pour contrôle exact des paramètres. Exposer via data_reader.py avec cache 2 secondes.
*Catégorie : indicateurs_momentum*

### D9024 — Gestion du cas dénominateur zéro (Max=Min)
🟡 **SYNTHÈSE** (Source : sierra_180_stochrsi.md) : Quand Max_nHL(RSI) = Min_nHL(RSI) (le RSI n'a pas bougé sur n_HL périodes), le dénominateur est zéro et la formule est indéfinie. Ce cas survient en périodes de très faible volatilité ou au début des données.
**TRADEX-AI C1** : Dans l'implémentation Python TRADEX-AI, protéger contre la division par zéro : si (Max - Min) == 0 → retourner 0.5 (valeur neutre) et logger un warning dans le moteur. Ce cas = marché en stase = ATTENDRE automatiquement.
*Catégorie : gestion_risque_entree*

### D9025 — StochRSI dans le contexte multi-timeframe TRADEX-AI
🟡 **SYNTHÈSE** (Source : sierra_180_stochrsi.md) : Comme tout oscillateur, le StochRSI doit être interprété dans le contexte du timeframe. Un StochRSI en sur-achat sur le 5min n'a pas le même poids qu'un StochRSI en sur-achat sur le Daily — ce dernier indique une sur-extension de plus grande ampleur.
**TRADEX-AI C1** : Pour TRADEX-AI, calculer le StochRSI sur 2 timeframes : Daily (tendance de fond) et NT8 range bars (entry timing). Signal optimal : StochRSI Daily en zone neutre (tendance non épuisée) + StochRSI intraday en zone extrême favorable (entrée au retournement).
*Catégorie : configuration*
