# Extraction CFTC — About the COT Reports (History & Structure)
**Source :** `bundles/cftc/cot_about_reports.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9511 → D9530 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/AbouttheCOTReports/index.htm
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Ce document décrit la structure officielle des rapports COT (historique, formats, calendrier, types) — référence fondatrice pour l'implémentation du module C3 Institutionnels dans TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| Figure 1 (mentionnée) | COT Futures Only CBT short form Dec 2006 | How to Read COT | D9514 |
| Figure 2 (mentionnée) | PRE sample COT Futures Only CBT short form Dec 2006 | How to Read COT | D9514 |

*Note : les figures sont mentionnées dans le texte mais les fichiers images ne sont pas présents dans le bundle (aucune image dans le dossier cot_about_reports/images/). Traitement = MANUEL.*

---

## DÉCISIONS

### D9511 — Fait historique : Origine des rapports COT (1924)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les ancêtres des rapports COT remontent à 1924, quand le Grain Futures Administration du USDA (prédécesseur de la CFTC) a publié son premier rapport annuel sur le hedging et la spéculation dans les marchés futures agricoles réglementés.
**TRADEX-AI C3** : Les données COT ont une profondeur historique exceptionnelle (100 ans d'évolution). Cette ancienneté valide leur pertinence comme outil d'analyse institutionnelle — les comportements de hedging Commercial sur les matières premières agricoles (ZW) et énergétiques (CL) sont structurellement stables depuis des décennies.
*Catégorie : structure_marche*

### D9512 — Fait historique : Première publication régulière COT (1962)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Depuis le 30 juin 1962, les données COT ont été publiées mensuellement pour 13 matières premières agricoles. La publication initiale était sur base de fin de mois, publiée le 11e ou 12e jour calendaire du mois suivant.
**TRADEX-AI C3** : La couverture des matières premières agricoles depuis 1962 inclut les précurseurs de ZW (Blé CBOT). La longue histoire des données COT agricoles permet de calculer des percentiles de positions Commercial/Non-Commercial sur ZW avec une base statistique solide (60+ ans). À utiliser pour définir des niveaux "extreme" de positionnement sur ZW.
*Catégorie : saisonnalite*

### D9513 — Règle structurelle : Seuil de 20 traders pour inclusion dans le COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le rapport COT couvre uniquement les marchés où 20 traders ou plus détiennent des positions égales ou supérieures aux niveaux de déclaration établis par la CFTC. Ce seuil garantit la représentativité et la confidentialité.
**TRADEX-AI C3** : GC (Or), HG (Cuivre), CL (Pétrole WTI) et ZW (Blé) sont des marchés majeurs avec des centaines de traders déclarables — le seuil de 20 est largement dépassé. Le signal COT pour ces actifs est statistiquement représentatif. Pour les marchés de référence TRADEX (MBT Bitcoin Micro, 6J Yen), vérifier si le seuil de 20 traders est atteint avant d'utiliser leurs données COT.
*Catégorie : volume_liquidite*

### D9514 — Règle de lecture : Structure du Short Report COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le "short report" COT affiche l'open interest séparé en positions déclarables (reportable) et non-déclarables (non-reportable). Pour les positions déclarables, il fournit : (1) positions commercial et non-commercial, (2) spreading, (3) variations depuis le rapport précédent, (4) pourcentages d'open interest par catégorie, (5) nombre de traders par catégorie.
**TRADEX-AI C3** : Checklist d'analyse du short report pour TRADEX sur GC/HG/CL/ZW : [1] Commercial NET = Long_Comm - Short_Comm → signal directionnel hedgers ; [2] Non-commercial NET = Long_NonComm - Short_NonComm → signal spéculatif ; [3] % Open Interest par catégorie → contexte de concentration ; [4] Variations semaine/semaine → momentum du positionnement institutionnel. Intégrer ces 4 métriques dans le score C3.
*Catégorie : indicateurs_tendance*

### D9515 — Règle de lecture : Structure du Long Report COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le "long report" COT contient tout le contenu du short report, plus : (1) ventilation par "crop year" (année de récolte) pour les marchés appropriés, (2) concentration des positions des 4 et 8 plus grands traders.
**TRADEX-AI C3** : Pour TRADEX, le long report est prioritaire pour ZW (Blé) en raison de la ventilation crop year. Pour GC, HG, CL, la concentration des 4/8 plus grands traders est un indicateur de risque de whale move — à surveiller avant une entrée en mode Auto. Règle : si concentration Top-4 > 40% OI sur un actif → réduire de 20% le score C3 pour cet actif (risque de manipulation institutionnelle).
*Catégorie : gestion_risque_entree*

### D9516 — Règle structurelle : Rapport Supplemental (Index Traders, agricoles)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le rapport Supplemental est publié en format Futures-and-Options-Combined pour les marchés agricoles sélectionnés. En plus de toutes les informations du short format, il montre les positions des "Index Traders". Publié depuis 2007.
**TRADEX-AI C3** : Pour ZW (Blé CBOT), le Supplemental COT est la seule source qui isole les positions des Index Traders (fonds indiciels passifs). Une forte présence d'Index Traders LONG sur ZW = demande structurelle passive ≠ signal directionnel actif. Le module C3 TRADEX doit filtrer les Index Traders de l'analyse signal pour ZW : signal valide = Managed Money NET + Commercial NET, sans contribution Index Trader.
*Catégorie : structure_marche*

### D9517 — Fait structurel : Format Futures-Only vs Futures-and-Options-Combined
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les rapports COT sont disponibles en deux formats : "Futures-Only" (positions futures uniquement) et "Futures-and-Options-Combined" (positions futures + options combinées). Les deux formats sont publiés chaque semaine.
**TRADEX-AI C3** : TRADEX doit utiliser le format "Futures-Only" pour l'analyse directionnelle sur GC/HG/CL/ZW — les positions futures reflètent les engagements directionnels purs. Le format "Futures-and-Options-Combined" peut masquer le biais directionnel car les options peuvent être utilisées pour des stratégies non directionnelles (couvertures gamma, straddles). Exception : pour l'analyse de sentiment extrême (pic de couvertures puts), utiliser le format combiné.
*Catégorie : indicateurs_momentum*

### D9518 — Règle temporelle : Données "as of Tuesday" (référence mardi)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Chaque rapport COT fournit une ventilation de l'open interest du mardi ("Tuesday's open interest"). Les données sont prises à la clôture du marché le mardi de chaque semaine.
**TRADEX-AI C3** : Les données COT reflètent l'état du marché au mardi de fermeture. Pour une publication vendredi 15h30 ET, le décalage est de ~3,5 jours. Pendant cette fenêtre (mardi clôture → vendredi 15h30), les positions institutionnelles ont pu évoluer. Le signal C3 a donc une fraîcheur maximale de ~3,5 jours — à documenter dans le "staleness monitor" de TRADEX comme "COT_DATA_AGE ≤ 3.5j requis, sinon STALE".
*Catégorie : timing*

### D9519 — Règle temporelle : Publication vendredi 15h30 ET (horaire officiel)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les rapports COT hebdomadaires (Futures-Only et Futures-and-Options-Combined) sont publiés chaque vendredi à 15h30 heure de l'Est (Eastern Time).
**TRADEX-AI C3** : Règle d'intégration TRADEX : scheduler de mise à jour C3 chaque vendredi à 15h35 ET (21h35 heure du Maroc en été, 20h35 en hiver). Si le download automatique échoue, basculer sur les données COT de la semaine précédente et noter "COT_STALE = True" dans le dashboard — bloquer tout signal C3 haussier basé sur COT périmé.
*Catégorie : timing*

### D9520 — Fait historique : Passage à la publication hebdomadaire (2000)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : La publication du COT est passée en fréquence hebdomadaire en 2000 (depuis la fréquence bi-hebdomadaire établie en 1992). Avant 2000 : mensuel jusqu'en 1990, mi-mois et fin de mois en 1990, bi-hebdomadaire en 1992.
**TRADEX-AI C3** : La fréquence hebdomadaire depuis 2000 est la référence pour les analyses TRADEX. Toute analyse de backtesting COT sur GC/HG/CL/ZW avant 2000 utilise des données à fréquence mensuelle ou bi-hebdomadaire — les résultats ne sont pas directement comparables aux analyses hebdomadaires modernes. Bornage recommandé : données COT utilisables pour TRADEX à partir de janvier 2000.
*Catégorie : structure_marche*

### D9521 — Fait historique : Ajout des données options COT (1995)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les données sur les positions d'options ont été ajoutées au rapport COT en 1995, créant le format "Futures-and-Options-Combined".
**TRADEX-AI C3** : L'ajout des données options en 1995 permet d'analyser la couverture optionnelle institutionnelle sur GC/HG/CL/ZW. Pour le module C5 (Sentiment TRADEX), le ratio Put/Call implicite dans les données options COT complète le VIX comme indicateur de sentiment sur les matières premières. Note : le format combiné est disponible depuis 1995 historiquement.
*Catégorie : indicateurs_momentum*

### D9522 — Fait historique : Ajout du nombre de traders et concentration (début 1970s)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Dans les années 1970, le COT a ajouté : (1) données sur le nombre de traders par catégorie, (2) ventilation par année de récolte (crop year), (3) ratios de concentration. Ces données sont disponibles depuis cette période.
**TRADEX-AI C3** : Le nombre de traders par catégorie est un indicateur de "breadth" institutionnel. Sur GC : si le nombre de Managed Money traders augmente significativement (ex. +20% sur un mois), c'est un signal d'intérêt institutionnel croissant — renforce le signal C3. Si le nombre de traders chute brutalement sur un actif, c'est un signal de désintérêt / sortie de capital institutionnel.
*Catégorie : volume_liquidite*

### D9523 — Fait structurel : Accès libre gratuit depuis 1995 (CFTC.gov)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Depuis 1995, les données COT sont disponibles gratuitement sur CFTC.gov. Avant : subscription par courrier jusqu'en 1993, puis accès électronique payant jusqu'en 1995.
**TRADEX-AI C3** : L'accès gratuit aux données COT sur CFTC.gov est un avantage concurrentiel pour TRADEX-AI — pas de coût de données pour le module C3 Institutionnels. Implémenter le téléchargement automatique depuis CFTC.gov (format CSV disponible) pour les 4 actifs TRADEX : GC (Code CFTC : 088691), HG (085692), CL (067651), ZW (001602).
*Catégorie : macro_evenements*

### D9524 — Fait structurel : Public Reporting Environment PRE (depuis 2022)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : En octobre 2022, la CFTC a mis en ligne un "Public Reporting Environment" (PRE) permettant de rechercher, filtrer, personnaliser et télécharger les données COT avec des filtres par date, groupe de matières premières, sous-groupe, nom de commodité et nom de marché.
**TRADEX-AI C3** : Le PRE CFTC est l'outil recommandé pour l'intégration automatisée dans TRADEX. Filtres à configurer dans le module C3 : Report Date (dernier vendredi), Commodity Group = Metals + Energy + Agriculture, actifs ciblés = GC/HG/CL/ZW. Le format de sortie CSV est exploitable directement par le data_reader.py de TRADEX.
*Catégorie : macro_evenements*

### D9525 — Règle d'interprétation : Sample COT (Blé CBT décembre 2006)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le document officiel "How to Read the COT Reports" utilise le contrat Blé CBT (CBT Wheat Futures) comme exemple de référence. L'exemple montre le short format du rapport du 12 décembre 2006 et son équivalent dans le PRE avec filtres : Commodity Group = Agriculture, Subgroup = Grains, Commodity = Wheat, Market = Wheat-SRW.
**TRADEX-AI C3** : Pour ZW (Blé CBOT/CBOT-SRW = ZW dans NT8), le code CFTC dans le PRE est "Wheat-SRW" (Soft Red Winter Wheat). Confirmer que ZW NT8 correspond bien au contrat CBT Wheat SRW et non au HRW (Hard Red Winter) ou Spring Wheat. Cette distinction est critique pour associer les bonnes données COT au bon contrat ZW dans TRADEX.
*Catégorie : structure_marche*

### D9526 — Règle d'enrichissement : Données option positions (format combiné)
🟡 **SYNTHÈSE** (Source : cot_about_reports.md) : Le format "Futures-and-Options-Combined" inclut les positions d'options converti en équivalent delta futures. Cela permet d'avoir une vue consolidée de l'exposition directionnelle totale des institutionnels (futures + options delta-ajustées).
**TRADEX-AI C3** : Pour une analyse C3 avancée sur GC, utiliser le format combiné pour capturer les couvertures institutionnelles via options. Un fort biais PUT des Commercials sur GC (visible dans le format combiné) = hedging contre une baisse de l'or = signal bearish renforcé. À implémenter en Phase 2 du module C3 après validation du flux Futures-Only de base.
*Catégorie : indicateurs_momentum*

### D9527 — Règle pratique : "Explanatory Notes" COT comme documentation de référence
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le document "Commitments of Traders Explanatory Notes" est référencé comme la documentation de référence pour comprendre la méthodologie détaillée du rapport COT.
**TRADEX-AI C3** : Les "Explanatory Notes" CFTC (dont les notes Disaggregated, bundle idx 454) constituent la spécification technique officielle du COT. Tout développement du module C3 TRADEX doit se conformer à ces notes — notamment pour les définitions de Producer/Merchant, Swap Dealer, Managed Money utilisées dans le Disaggregated COT.
*Catégorie : structure_marche*

### D9528 — Règle d'analyse : Variations semaine/semaine (changes from previous report)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le short report COT inclut les "changes from the previous report" (variations depuis le rapport précédent) pour chaque catégorie de traders. Ces variations sont publiées directement dans le rapport.
**TRADEX-AI C3** : Les variations hebdomadaires des positions sont le signal de momentum COT le plus actionnable pour TRADEX. Règle : si Managed Money sur GC augmente de > 10 000 contrats en une semaine, c'est un signal d'accumulation institutionnelle bullish (C3 positif fort). Variation inverse (réduction > 10 000 contrats) = distribution institutionnelle = C3 négatif. Les seuils de 10 000 contrats sont indicatifs — à calibrer sur données historiques GC.
*Catégorie : indicateurs_tendance*

### D9529 — Règle d'analyse : Pourcentages d'open interest par catégorie
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le short report COT inclut les "percents of open interest by category" — le pourcentage de l'open interest total détenu par chaque catégorie de traders (commercial, non-commercial, non-reportable).
**TRADEX-AI C3** : Les pourcentages d'open interest normalisent les données COT indépendamment de la taille absolue du marché. Utiliser les percentiles historiques de ces pourcentages (ex. : Managed Money % OI sur GC dans le top 90% = sur-extension haussière = prudence entrée LONG). La normalisation par % OI permet de comparer les niveaux actuels aux extrêmes historiques même si l'open interest total a changé.
*Catégorie : indicateurs_tendance*

### D9530 — Règle de robustesse : Données historiques disponibilité par format
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Historique disponible sur CFTC.gov : Futures-Only depuis 1986, Futures-and-Options-Combined depuis 1995, Supplemental depuis 2006. Les données Disaggregated COT sont disponibles depuis juin 2006 (premier rapport 4 septembre 2009, rétro-calculé depuis 2006).
**TRADEX-AI C3** : Pour les backtests COT TRADEX, utiliser : (1) Format Futures-Only post-2000 pour analyses hebdomadaires uniformes ; (2) Format Disaggregated post-2006 pour analyses par catégorie (Producer vs Managed Money) ; (3) Supplemental post-2007 uniquement pour ZW (Index Traders). Documenter ces bornes temporelles dans le module C3 et alerter l'utilisateur si une requête historique dépasse ces limites.
*Catégorie : gestion_risque_entree*
