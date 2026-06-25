# Extraction Optimus — TPO Charts Explained for Beginners: Market Profile Guide
**Source :** `bundles/optimusfutures/tpo_charts_explained_for_beginners_market_profile_guide.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D8751 → D8770 · **Page :** https://optimusfutures.com/blog/tpo-charts-explained-for-beginners-market-profile-guide/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Les TPO charts révèlent la structure institutionnelle (POC, Value Area, Initial Balance) invisible sur les chandeliers standards — source de confirmation C2/C3.

## INVENTAIRE IMAGES CERTIFIÉES
*(aucune figure certifiée dans ce bundle)*

## DÉCISIONS

### D8751 — Les TPO charts montrent le temps passé à chaque prix (time-at-price)
🔵 **ÉCOLE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Un graphique TPO (Time Price Opportunity) représente chaque période de temps par une lettre placée à chaque niveau de prix atteint durant cette période. Contrairement aux chandeliers qui montrent uniquement OHLCV, le TPO révèle combien de temps (de périodes) le prix a stationné à chaque niveau.
**TRADEX-AI C2** : La lecture TPO est complémentaire à ATAS : elle identifie les zones de valeur institutionnelle (là où le temps s'accumule) que le Footprint seul ne met pas en évidence. À utiliser comme filtre de niveaux S/R dynamiques.
*Catégorie : structure_marche*

### D8752 — TPO vs Volume Profile : deux dimensions complémentaires
🔵 **ÉCOLE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Le TPO mesure le temps passé à chaque prix (fréquence temporelle). Le Volume Profile mesure le volume échangé à chaque prix (fréquence volumétrique). Les deux ne coïncident pas toujours : un niveau peut concentrer beaucoup de temps mais peu de volume (ou l'inverse). La confluence des deux est un signal fort.
**TRADEX-AI C2** : Règle de confluence : un niveau S/R est de haute qualité uniquement si POC TPO ET POC Volume Profile sont proches (< 2 ticks d'écart). Cela renforce la conviction pour une entrée ou une sortie.
*Catégorie : structure_marche*

### D8753 — Les 3 piliers du Market Profile : POC, Value Area, Profile Shape
🔵 **ÉCOLE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : (1) POC (Point of Control) = prix avec le plus de TPOs (temps d'acceptation maximal). (2) Value Area = zone contenant 70% des échanges TPO (une déviation standard autour du POC). (3) Profile Shape = forme globale du profil (D-shape = acceptation / P-shape = squeeze haussier / b-shape = squeeze baissier / elongated = trending).
**TRADEX-AI C2** : Ces 3 piliers sont les niveaux clés à calculer quotidiennement pour GC, HG, CL, ZW. Le POC du jour précédent est un niveau de référence pour le signal du lendemain (C2 → niveau d'intérêt).
*Catégorie : structure_marche*

### D8754 — POC (Point of Control) : niveau de plus forte acceptation temporelle
🟢 **FAIT VÉRIFIÉ** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Le POC est le niveau de prix où le marché a passé le plus de temps. Il représente le prix de "fair value" perçu par les participants. Les prix ont tendance à revenir vers le POC après s'en être écartés (mean reversion).
**TRADEX-AI C2** : Le POC de la session précédente est un aimant de prix (magnet level). Un trade contre le POC nécessite confirmation order flow fort ; un trade en direction du POC a une probabilité de réussite statistiquement plus élevée.
*Catégorie : structure_marche*

### D8755 — Value Area : zone de 70% des échanges temporels
🟢 **FAIT VÉRIFIÉ** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : La Value Area (VA) englobe les niveaux de prix qui représentent 70% de l'activité TPO. Les bornes sont : Value Area High (VAH) et Value Area Low (VAL). Un retour dans la VA après en être sorti est statistiquement probable (règle 80% : si le marché ouvre hors VA et re-entre dans la VA, il y a 80% de chances qu'il traverse jusqu'à l'autre borne de la VA).
**TRADEX-AI C2** : VAH et VAL du jour précédent sont des niveaux de support/résistance dynamiques de première importance pour GC, HG, CL, ZW. À calculer chaque soir et injecter dans le contexte signal Claude.
*Catégorie : structure_marche*

### D8756 — Initial Balance (IB) : anticipation trend day vs balance day
🟢 **FAIT VÉRIFIÉ** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : L'Initial Balance est formé par les deux premières heures de trading (souvent 9h30-11h30 ET pour les futurs américains). Un IB étroit suggère une journée de tendance probable (le marché cherchera à s'étendre). Un IB large suggère une journée de range/balance (le marché reste dans l'IB).
**TRADEX-AI C4** : Intégrer la lecture de l'IB dans le filtre macro du matin (C4). Si l'IB est étroit à l'ouverture, le moteur peut autoriser des signaux de tendance ; si l'IB est large, les signaux de range-bound sont préférés.
*Catégorie : timing*

### D8757 — Profile Shape D (D-shape) = journée d'acceptation/équilibre
🔵 **ÉCOLE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Un profil en forme de D (symétrique, centré sur le POC) indique que le marché a trouvé un consensus de prix. Acheteurs et vendeurs sont en équilibre. Ce contexte favorise le mean reversion et les trades de range.
**TRADEX-AI C2** : Profil D identifié → favoriser les trades de retour vers le POC, éviter les trades de cassure sans confirmation order flow majeure. Réduire la taille de position (marché sans direction).
*Catégorie : configuration*

### D8758 — Divergence structurelle TPO/Volume Profile = signal fort
🟡 **SYNTHÈSE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Lorsque le POC TPO et le POC Volume Profile sont à des niveaux différents, il existe une divergence structurelle. Le niveau le plus défendu (acheteurs/vendeurs actifs) est généralement celui du Volume Profile POC. La divergence signale une possible tension entre perception temporelle et engagement volumétrique.
**TRADEX-AI C2** : Une divergence TPO/Volume Profile sur un actif tradable (GC/HG/CL/ZW) est un signal d'alerte : éviter les trades directionnels sans resolution de la divergence, ou les utiliser comme zones de risque à surveiller.
*Catégorie : structure_marche*

### D8759 — Overlayer TPO avec Volume Profile pour confluence
🔵 **ÉCOLE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : L'article recommande explicitement de superposer le Volume Profile au TPO dans Optimus Flow (Quantower) pour identifier les zones de confluence : un niveau où les deux méthodes concordent (POC TPO ≈ POC VP, VAH/VAL coïncident) est un niveau de haute conviction.
**TRADEX-AI C2** : Dans TRADEX, les niveaux de confirmation C2 de plus haute valeur sont ceux où TPO et Volume Profile convergent. Ces niveaux ont le plus fort pouvoir d'attraction du prix et doivent être utilisés en priorité pour les stops et les cibles.
*Catégorie : gestion_risque_entree*

### D8760 — Les TPO charts révèlent ce que les chandeliers cachent
🟡 **SYNTHÈSE** (Source : tpo_charts_explained_for_beginners_market_profile_guide.md) : Les chandeliers montrent le résultat (OHLC) mais pas le processus d'acceptation du prix. Deux chandeliers identiques (même OHLC) peuvent avoir des structures TPO très différentes, l'un montrant une acceptation forte au centre (D-shape), l'autre montrant un marché en exploration (elongated). Le TPO révèle la qualité du mouvement.
**TRADEX-AI C2** : Pour les actifs GC, HG, CL, ZW, analyser le TPO journalier en complément des chandeliers NT8 permet d'évaluer si les niveaux de prix sont acceptés ou simplement traversés — information critique pour valider les niveaux Belkhayate (BGC, Pivots).
*Catégorie : structure_marche*
