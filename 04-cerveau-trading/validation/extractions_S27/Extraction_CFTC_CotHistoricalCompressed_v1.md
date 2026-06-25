# Extraction CFTC — COT Historical Compressed (Index des fichiers historiques)
**Source :** `bundles/cftc/cot_historical_compressed.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9551 → D9570 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Index des archives COT depuis 1986 — source primaire Cercle C3 Institutionnels pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9551 — Formats COT disponibles : Futures Only vs Futures-and-Options Combined
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : La CFTC publie deux formats distincts pour chaque rapport COT — « Futures Only » (positions sur contrats à terme uniquement) et « Futures-and-Options Combined » (cumul contrats à terme + options). Ces deux formats existent pour les rapports Legacy, Disaggregated et TFF.
**TRADEX-AI C3** : Pour lire les positions institutionnelles sur GC/HG/CL/ZW, préférer le format « Futures-and-Options Combined » qui reflète l'exposition totale des grands opérateurs (options incluses).
*Catégorie : volume_liquidite*

### D9552 — Historique Disaggregated COT disponible depuis septembre 2009
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : Les fichiers complets Disaggregated COT (Futures Only et Futures-and-Options Combined) sont archivés par année depuis septembre 2009. Chaque fichier annuel contient l'ensemble des marchés reportables pour cette année.
**TRADEX-AI C3** : Backtests COT sur GC/HG/CL/ZW possibles depuis 2009 — horizon d'environ 15 ans de données institutionnelles disaggregated disponibles en téléchargement direct CFTC.
*Catégorie : structure_marche*

### D9553 — Historique TFF (Traders in Financial Futures) disponible depuis septembre 2009
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : Les fichiers complets TFF (Futures Only et Futures-and-Options Combined) sont archivés par année depuis septembre 2009, en parallèle des rapports Disaggregated.
**TRADEX-AI C3** : Le TFF fournit la décomposition Dealer/AssetManager/LeveragedFunds/Other pour les marchés financiers — pertinent pour DX et ES (actifs CONFIRMATION TRADEX). Disponible pour backtest depuis 2009.
*Catégorie : structure_marche*

### D9554 — Historique Legacy COT disponible depuis 1986 (Futures Only)
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : Les fichiers complets Legacy COT Futures Only sont archivés par année depuis 1986 — soit plus de 35 ans d'historique. Le format Futures-and-Options Combined est disponible depuis mars 1995.
**TRADEX-AI C3** : L'historique Legacy depuis 1986 permet des analyses long-terme sur GC (or) et CL (pétrole) — corrélations multi-décennales entre positions Commercial/Non-Commercial et tendances de prix (Cercle C7 corrélations).
*Catégorie : correlations*

### D9555 — Historique Commodity Index Trader (CIT) Supplement disponible depuis janvier 2006
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : Le supplément CIT est archivé par année depuis janvier 2006. Ce rapport sépare les Commodity Index Traders (CIT) des autres participants commerciaux et non-commerciaux.
**TRADEX-AI C3** : Les CIT (fonds indiciels matières premières) exercent une pression haussière structurelle sur GC/HG/CL/ZW. Leur présence dans le COT est un signal de biais institutionnel long — pertinent pour détecter des phases d'accumulation sur actifs TRADING.
*Catégorie : structure_marche*

### D9556 — Changement de format grain COT en 1998 : contrats au lieu de boisseaux
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : À partir de 1998, les données COT sur les céréales (dont ZW — blé) sont reportées en nombre de contrats et non plus en boisseaux. Les variations de positions entre le dernier rapport 1997 et le premier rapport 1998 n'ont pas été calculées.
**TRADEX-AI C3** : Rupture de série historique sur ZW (blé) en 1998 — tout backtest COT ZW croisant l'année 1997/1998 doit traiter cette discontinuité. Pour TRADEX, utiliser uniquement les données post-1998 pour ZW afin d'assurer la comparabilité.
*Catégorie : gestion_risque_entree*

### D9557 — Données COT avant septembre 1992 : fréquence bi-mensuelle uniquement
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : Avant le 30 septembre 1992, seules les données de mi-mois et de fin de mois sont disponibles (fréquence bi-mensuelle). La CFTC avertit que ces données peuvent contenir des erreurs non corrigeables en raison du délai entre la date du rapport et sa compilation.
**TRADEX-AI C3** : Données COT pré-1992 à exclure de tout backtest automatisé TRADEX en raison de la fréquence réduite et des erreurs potentielles non corrigées. Horizon minimum fiable : septembre 1992 pour Legacy, septembre 2009 pour Disaggregated/TFF.
*Catégorie : gestion_risque_entree*

### D9558 — Structure des archives : fichiers CSV compressés organisés par année et par format
🟡 **SYNTHÈSE** (Source : cot_historical_compressed.md) : L'archive CFTC est structurée en fichiers CSV annuels distincts par type de rapport (Legacy / Disaggregated / TFF / CIT) et par format (Futures Only / Futures-and-Options Combined). Chaque fichier contient tous les marchés reportables de l'année.
**TRADEX-AI C3** : Architecture de collecte COT pour TRADEX — télécharger les fichiers annuels Disaggregated (post-2009) et filtrer les codes CFTC GC=088691/HG=085692/CL=067651/ZW=001602 pour extraire les séries institutionnelles des 4 actifs TRADING.
*Catégorie : macro_evenements*

### D9559 — Point de contact CFTC pour commentaires sur les données historiques
🟢 **FAIT VÉRIFIÉ** (Source : cot_historical_compressed.md) : La CFTC désigne l'adresse [email protected] comme point de contact officiel pour les commentaires et questions sur les données COT historiques compressées.
**TRADEX-AI C3** : Canal officiel pour signaler des anomalies dans les données COT utilisées par TRADEX — à documenter dans les procédures de maintenance du Cercle C3.
*Catégorie : macro_evenements*

### D9560 — Rapports COT publiés chaque mardi : données reflétant les positions en fin de journée du mardi précédent
🟡 **SYNTHÈSE** (Source : cot_historical_compressed.md) : Les fichiers historiques compressés archivisent l'ensemble des publications hebdomadaires COT, chaque rapport reflétant les positions de fin de journée du mardi de la semaine de référence.
**TRADEX-AI C3** : Cadence de mise à jour COT = hebdomadaire (mardi) — dans TRADEX, le Cercle C3 se rafraîchit une fois par semaine après publication CFTC. Intégrer un flag « COT_stale » si données > 7 jours (staleness_monitor).
*Catégorie : timing*
