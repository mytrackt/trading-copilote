# Extraction StockCharts — True Range
**Source :** `bundles/stockcharts/true_range.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D4691 → D4697 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/true-range
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : True Range est le fondement du calcul ATR, utilisé pour dimensionner les stops et mesurer la volatilité sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image dans ce bundle) | — | — | — |

## DÉCISIONS

### D4691 — Définition True Range (TR)
🟢 **FAIT VÉRIFIÉ** (Source : true_range.md) : Le True Range (TR) mesure l'étendue journalière des prix EN INCLUANT les gaps par rapport à la clôture précédente. TR = max(High−Low, High−ClosePrév, ClosePrév−Low). Introduit par J. Welles Wilder dans *New Concepts in Technical Trading Systems*.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, le TR capte les gaps de nuit (session Globex) que le simple High−Low ignore — pertinent pour calibrer les stops sur ces contrats futures à forte activité hors-séance.
*Catégorie : gestion_risque_entree*

### D4692 — Trois composantes obligatoires du calcul TR
🟢 **FAIT VÉRIFIÉ** (Source : true_range.md) : Le TR évalue trois valeurs : (1) High − Low, (2) |High − Close précédente|, (3) |Close précédente − Low|. La plus grande des trois est retenue. Cette règle est systématique et sans exception.
**TRADEX-AI C1** : Pour les futurs (GC, CL), les sessions overnight créent régulièrement des gaps ; le composant |High − Close précédente| ou |Close précédente − Low| sera donc souvent dominant — le moteur Python doit utiliser cette formule complète, pas seulement High−Low.
*Catégorie : gestion_risque_entree*

### D4693 — TR brut vs ATR lissé
🟢 **FAIT VÉRIFIÉ** (Source : true_range.md) : Le True Range brut (TR) est lissé pour produire l'Average True Range (ATR). Le TR seul est la brique élémentaire ; l'ATR est l'indicateur opérationnel dérivé.
**TRADEX-AI C1** : Dans le moteur TRADEX, l'ATR calculé sur GC/HG/CL/ZW doit utiliser ce TR complet (3 composantes) comme input — toute implémentation qui prend uniquement High−Low sous-estime la volatilité réelle.
*Catégorie : gestion_risque_entree*

### D4694 — TR et gaps de prix
🟢 **FAIT VÉRIFIÉ** (Source : true_range.md) : La raison d'être du TR par rapport au range simple (High−Low) est explicitement de prendre en compte les gaps de prix entre séances. Sans TR, un gap haussier de nuit apparaîtrait comme une journée de faible volatilité alors que la vraie étendue de mouvement est bien plus grande.
**TRADEX-AI C1** : Sur les marchés de matières premières (GC Or, CL Pétrole), les annonces macro (NFP, FOMC, données EIA) provoquent des gaps fréquents — le TR est donc indispensable pour ne pas sous-estimer la volatilité et dimensionner correctement les stops.
*Catégorie : macro_evenements*

### D4695 — Origine et référence bibliographique
🔵 **ÉCOLE** (Source : true_range.md) : Le True Range et l'ATR ont été introduits par J. Welles Wilder dans *New Concepts in Technical Trading Systems* (1978). C'est la référence académique canonique de cet indicateur.
**TRADEX-AI C1** : Référence de sourcing pour la KB — tout audit futur des règles ATR/TR dans KNOWLEDGE_BASE_MASTER.json peut citer Wilder 1978 comme source primaire.
*Catégorie : indicateurs_tendance*

### D4696 — TR comme mesure de volatilité instantanée
🟡 **SYNTHÈSE** (Source : true_range.md) : Le TR mesure la volatilité sur une seule barre (instantanée), tandis que l'ATR lisse cette mesure sur N périodes. Pour une décision d'entrée ponctuelle, le TR courant indique si le marché est actuellement volatil (fort TR) ou en compression (faible TR).
**TRADEX-AI C1** : Un TR anormalement élevé sur GC ou CL avant un signal peut justifier de réduire la taille de position ou d'élargir le stop — à intégrer dans le risk_manager.py du moteur TRADEX.
*Catégorie : gestion_position_active*

### D4697 — TR ne donne pas de signal directionnel
🟢 **FAIT VÉRIFIÉ** (Source : true_range.md) : Le True Range est une mesure de volatilité pure, sans composante directionnelle. Il indique l'amplitude du mouvement mais pas son sens (haussier ou baissier).
**TRADEX-AI C1** : Dans le scoring TRADEX (/10), le TR / ATR contribue au dimensionnement des stops (C1) mais ne peut pas alimenter un signal ACHETER ou VENDRE — il doit être combiné avec des indicateurs directionnels (BGC, Direction, TSI, etc.).
*Catégorie : configuration*
