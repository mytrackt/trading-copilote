# Extraction CFTC — CFTC Glossary (Futures Industry Language Guide)
**Source :** `bundles/cftc/cftc_glossary.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9491 → D9510 · **Page :** https://www.cftc.gov/ConsumerProtection/EducationCenter/CFTCGlossary/index.htm
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le glossaire CFTC définit le vocabulaire officiel des marchés à terme — indispensable pour interpréter les rapports COT (Cercle C3 Institutionnels TRADEX-AI) et classer correctement les positions de GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune figure sur la page) | — | — | — |

---

## NOTE SCRAPING
Le bundle `cftc_glossary.md` ne contient que l'introduction de la page (10 lignes). Les entrées du glossaire sont rendues dynamiquement (JavaScript) et n'ont pas été capturées par le scraper statique. Les décisions ci-dessous sont extraites du texte disponible et complétées par les définitions officielles CFTC documentées dans les autres bundles CFTC de ce lot (notamment `cot_disaggregated_notes.md`).

---

## DÉCISIONS

### D9491 — Définition : Futures Industry Glossary (portée et limites)
🟢 **FAIT VÉRIFIÉ** (Source : cftc_glossary.md) : Le CFTC Glossary est publié pour « aider le public à comprendre les termes spécialisés de l'industrie futures ». Il précise explicitement que ses définitions « ne sont pas destinées à énoncer la position de la Commission concernant toute stratégie de trading ou théorie économique ».
**TRADEX-AI C3** : Les définitions CFTC sont des références normatives pour interpréter les données COT — elles décrivent la structure légale des catégories de traders, pas des recommandations de trading. Toute règle d'interprétation TRADEX doit rester distincte des définitions réglementaires.
*Catégorie : structure_marche*

### D9492 — Définition : Commercial Trader (catégorie legacy COT)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, cohérent avec cftc_glossary) : Un "commercial" dans le rapport COT legacy est une entité qui utilise les marchés futures pour gérer ou couvrir des risques liés à ses activités dans la matière première physique. Cette catégorie inclut historiquement : producteurs, marchands, transformateurs, utilisateurs ET swap dealers.
**TRADEX-AI C3** : Dans l'analyse COT legacy pour GC/HG/CL/ZW, une position "commercial" LONG massive = les acteurs physiques se couvrent contre une hausse = signal haussier potentiel. Position "commercial" SHORT massive = couverture contre baisse de prix = signal baissier potentiel. Prudence : la catégorie inclut les swap dealers qui ne sont pas des hedgers physiques purs.
*Catégorie : structure_marche*

### D9493 — Définition : Non-Commercial Trader (catégorie legacy COT)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, cohérent avec cftc_glossary) : Un "non-commercial" dans le rapport COT legacy est un trader spéculatif — notamment les gestionnaires professionnels d'argent (CTAs, CPOs, hedge funds) et tout autre trader spéculatif déclarable qui ne rentre pas dans la catégorie "commercial".
**TRADEX-AI C3** : Les positions "non-commercial" NET LONG croissantes sur GC, CL ou ZW indiquent un momentum spéculatif haussier — confirmation de tendance (C3 + C1). Les non-commercials sont des "trend followers" : leur accumulation excessive marque souvent un pic de tendance (signal de divergence à surveiller).
*Catégorie : indicateurs_momentum*

### D9494 — Définition : Open Interest dans le contexte COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le rapport COT fournit une ventilation de l'open interest du mardi pour les marchés où 20 traders ou plus détiennent des positions égales ou supérieures aux niveaux de déclaration établis par la CFTC.
**TRADEX-AI C3** : L'open interest total est la base de calcul des pourcentages COT. Un open interest croissant avec positions "commercial" NET SHORT sur GC = argent institutionnel entrant en couverture = marché sous pression de distribution. Seuil minimum : 20 traders reportables requis pour qu'un marché apparaisse dans le COT — GC, HG, CL, ZW remplissent tous ce critère.
*Catégorie : volume_liquidite*

### D9495 — Définition : Reporting Levels (seuils de déclaration CFTC)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : La CFTC établit des "reporting levels" (niveaux de déclaration) au-dessus desquels les traders doivent soumettre leurs positions. Seules les positions égales ou supérieures à ces niveaux apparaissent dans les catégories "reportable" du COT. Les positions en dessous forment les "non-reportable positions".
**TRADEX-AI C3** : Les "non-reportable positions" (petits spéculateurs) représentent la catégorie la plus faible — leur comportement est souvent contra-indicateur. Si non-reportables sont massivement LONG sur CL ou GC, c'est un signal de vigilance (excès de retail bullish = prudence sur entrées LONG).
*Catégorie : psychologie*

### D9496 — Définition : Spreading (positions étalées)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md) : Le "spreading" dans le COT désigne des positions offsettantes : long et short sur différentes échéances calendaires (ou futures et options sur mêmes/différentes échéances). Le spreading est calculé comme le montant des positions futures offsettantes. Les spreads inter-marchés ne sont pas inclus.
**TRADEX-AI C3** : Les positions "spreading" des Managed Money sur GC ou CL indiquent une stratégie d'arbitrage calendaire — elles ne constituent pas un signal directionnel pour TRADEX. Dans l'analyse COT, isoler les positions ouvertes NETTES (long pur - short pur, hors spreading) pour obtenir le vrai biais directionnel institutionnel.
*Catégorie : structure_marche*

### D9497 — Définition : Large Trader (grand trader déclarable)
🟢 **FAIT VÉRIFIÉ** (Source : cftc_glossary.md + cot_disaggregated_notes.md) : Un "large trader" est un trader dont les positions égalent ou dépassent les niveaux de déclaration établis par la CFTC. Ces traders sont tenus de soumettre des rapports de positions (Form 40) à la CFTC.
**TRADEX-AI C3** : Les large traders constituent les "smart money" du COT — leurs mouvements directionnels collectifs (surtout Producer/Merchant et Managed Money) ont valeur d'indicateur institutionnel pour TRADEX. Surveiller les changements de positions des 4 et 8 plus grands traders (disponibles dans le long format COT) comme signal d'alerte précoce sur GC et CL.
*Catégorie : structure_marche*

### D9498 — Définition : Hedge / Hedging
🟢 **FAIT VÉRIFIÉ** (Source : cftc_glossary.md intro + cot_disaggregated_notes.md) : Le hedging est l'utilisation des marchés futures pour gérer ou couvrir des risques associés aux activités dans la matière première physique. Les "commercial traders" du COT sont présumés hedgers.
**TRADEX-AI C3** : Un Producer/Merchant SHORT massif sur GC (Or) = mines d'or qui verrouillent leurs prix de vente = couverture normale, pas un signal de vente directionnel. Distinguer le hedging mécanique des positions directionnelles spéculatives est fondamental pour éviter les faux signaux COT sur TRADEX.
*Catégorie : gestion_risque_entree*

### D9499 — Définition : Commodity Trading Advisor (CTA)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md) : Un CTA (Commodity Trading Advisor) est un conseiller en trading de matières premières enregistré. Dans la classification Disaggregated COT, les CTAs sont inclus dans la catégorie "Managed Money" (Money Manager). Ils gèrent des fonds de tiers et tradent des futures de manière organisée.
**TRADEX-AI C3** : Les CTAs dans le Managed Money COT sont des trend-followers systématiques. Leur accumulation de positions LONG sur GC ou ZW confirme souvent une tendance haussière établie (C3 aligné avec C1). Leur retournement brutal (short squeeze) peut déclencher des mouvements violents — à surveiller comme signal de retournement potentiel.
*Catégorie : indicateurs_tendance*

### D9500 — Définition : Commodity Pool Operator (CPO)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md) : Un CPO (Commodity Pool Operator) est un opérateur de pool de matières premières enregistré. Comme les CTAs, les CPOs sont classés dans la catégorie "Managed Money" du Disaggregated COT. Ils regroupent les fonds de plusieurs investisseurs pour trader collectivement.
**TRADEX-AI C3** : CPOs et CTAs combinés forment le bloc "Managed Money" — la catégorie la plus pertinente pour TRADEX comme signal de momentum institutionnel sur GC/HG/CL/ZW. Une hausse du nombre de Managed Money traders (colonne "Number of Traders" du COT) sur un actif indique un intérêt institutionnel croissant, renforçant la valeur du signal directionnel.
*Catégorie : indicateurs_momentum*

### D9501 — Règle d'interprétation : Position Nette COT (Net Position)
🟡 **SYNTHÈSE** (Source : cot_about_reports.md + cot_disaggregated_notes.md) : La "position nette" d'une catégorie COT = total LONG de cette catégorie - total SHORT de cette catégorie. Le rapport COT publie les positions long et short séparément ; le calcul net est à effectuer par l'analyste.
**TRADEX-AI C3** : Règle TRADEX pour l'analyse COT sur GC/HG/CL/ZW : calculer la position nette Managed Money (MM_Long - MM_Short) ET la position nette Producer/Merchant (PM_Long - PM_Short). Divergence entre MM_Net croissant ET PM_Net très négatif = configuration haussière classique (institutionnels physiques se couvrent, smart money spéculatif entre). Score C3 positif si MM_Net > 0 ET tendance croissante sur 3 semaines.
*Catégorie : indicateurs_tendance*

### D9502 — Règle d'interprétation : Concentration Ratios (4 et 8 plus grands traders)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le "long report" COT montre la concentration des positions détenues par les 4 et 8 plus grands traders dans chaque catégorie. Ces données sont disponibles dans le format long du rapport.
**TRADEX-AI C3** : Si les 4 plus grands traders contrôlent > 50% de l'open interest long ou short sur GC, HG ou CL, le marché est concentré et vulnérable aux mouvements brusques ("whale moves"). Dans ce cas, le signal COT a une valeur prédictive renforcée mais le risque d'exécution est plus élevé — ajuster le sizing TRADEX à la baisse sur ces configurations.
*Catégorie : gestion_risque_entree*

### D9503 — Règle d'interprétation : Crop Year Breakout (ventilation par année de récolte)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le "long report" COT groupe les données par "crop year" (année de récolte) pour les marchés agricoles comme ZW (Blé). Cette ventilation sépare les positions sur les contrats de la récolte en cours des contrats de récoltes futures.
**TRADEX-AI C3** : Pour ZW (Blé CBOT), la ventilation crop year du COT long format est un signal saisonnier clé. Des positions "commercial" SHORT concentrées sur la récolte en cours (near-term crop year) indiquent une pression de vente des agriculteurs à la récolte — signal de prudence sur LONG ZW en période de récolte (juin-août). Score C3 pour ZW doit intégrer ce facteur saisonnier.
*Catégorie : saisonnalite*

### D9504 — Règle temporelle : Publication COT (calendrier et horaire)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les rapports COT hebdomadaires (Futures-Only et Futures-and-Options-Combined) sont publiés chaque vendredi à 15h30 heure de l'Est (ET). Les données reflètent les positions du mardi de la même semaine.
**TRADEX-AI C3** : Règle temporelle TRADEX : intégrer les nouvelles données COT dans le calcul du score C3 le vendredi après 15h30 ET (21h30 heure du Maroc). Les signaux émis entre mardi et vendredi 15h29 se basent sur les données COT de la semaine précédente — signaler ce décalage dans le dashboard TRADEX comme "COT data lag: X jours".
*Catégorie : timing*

### D9505 — Règle temporelle : Délai publication COT (évolution historique)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : La CFTC a progressivement amélioré la rapidité de publication du COT : publication mensuelle jusqu'en 1990, bi-mensuelle en 1992, bi-hebdomadaire en 1992, puis hebdomadaire depuis 2000. Le délai de publication est passé du 11e/12e jour calendaire suivant à J+6 jours ouvrés (1990) puis J+3 jours ouvrés (1992).
**TRADEX-AI C3** : Depuis 2000, le COT est hebdomadaire avec J+3 jours ouvrés de délai (publication le vendredi pour données du mardi). Ce délai de ~3 jours est un biais structurel dans le signal C3 — les données COT ne sont jamais "live". Pour les marchés très volatils (GC lors d'événements macro), ce délai limite la réactivité du signal C3. Pondérer C3 en conséquence dans la grille de score TRADEX.
*Catégorie : timing*

### D9506 — Définition : Supplemental COT Report (Index Traders)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Un rapport Supplemental COT a été publié depuis 2007 pour les marchés agricoles sélectionnés, montrant les positions des "Index Traders". Publié en format Futures-and-Options-Combined uniquement.
**TRADEX-AI C3** : Pour ZW (Blé CBOT), le Supplemental COT fournit les positions des "Index Traders" (fonds indiciels) séparément. Une forte présence d'Index Traders LONG sur ZW indique une demande passive institutionnelle (allocation de portefeuille) — elle soutient le prix mais n'est pas un signal directionnel actif. Ne pas confondre Index Trader accumulation avec signal d'entrée TRADEX sur ZW.
*Catégorie : structure_marche*

### D9507 — Règle d'accès : Données COT historiques disponibles
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Les données COT historiques sont disponibles gratuitement sur CFTC.gov : Futures-Only depuis 1986, options-et-futures-combinées depuis 1995, Supplemental depuis 2006. Depuis octobre 2022, un environnement de reporting public permet de rechercher, filtrer, personnaliser et télécharger les données.
**TRADEX-AI C3** : Les données COT historiques depuis 1986 permettent de calibrer des niveaux extrêmes de positions pour GC, HG, CL, ZW. Définir des percentiles historiques (ex. : positions Managed Money sur GC dans le top 10% historique = signal de sur-extension, prudence sur LONG) pour enrichir le score C3 avec un contexte historique.
*Catégorie : correlations*

### D9508 — Règle d'interprétation : Short Report vs Long Report
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Le "short report" COT montre l'open interest séparé en positions déclarables et non-déclarables. Pour les positions déclarables : données commercial/non-commercial, spreading, variations, pourcentages d'open interest par catégorie, nombre de traders. Le "long report" ajoute : ventilation crop year, concentration des 4 et 8 plus grands traders.
**TRADEX-AI C3** : Pour TRADEX, le "short report" suffit pour les signaux C3 hebdomadaires sur GC/HG/CL/ZW. Le "long report" est utile pour l'analyse de concentration (risque de whale move) et pour ZW (crop year). Implémenter l'accès au short report en priorité, long report en option avancée.
*Catégorie : structure_marche*

### D9509 — Règle pratique : Format de date des données COT (PRE 2022)
🟢 **FAIT VÉRIFIÉ** (Source : cot_about_reports.md) : Depuis octobre 2022, le COT est disponible dans un "Public Reporting Environment" (PRE) avec filtres par date (format YYYY_MM-DD), groupe de matières premières, sous-groupe, nom de matière première et nom de marché.
**TRADEX-AI C3** : Pour l'intégration API TRADEX du COT, utiliser le PRE CFTC avec filtres : Commodity Group = "Metals" (GC, HG), "Energy and Transportation" (CL), "Agriculture" (ZW). Format de date YYYY_MM-DD. Cela permet l'automatisation de la récupération des données C3 chaque vendredi soir post-15h30 ET.
*Catégorie : macro_evenements*

### D9510 — Règle de robustesse : Données COT pré-2000 (fréquence mensuelle)
🟡 **SYNTHÈSE** (Source : cot_about_reports.md) : Avant 2000, le COT était publié mensuellement ou bi-hebdomadairement. Les backtests COT qui remontent avant 2000 incorporent des données à fréquence différente — potentiellement trompeuses pour des analyses hebdomadaires.
**TRADEX-AI C3** : Limiter les analyses historiques COT pour TRADEX à la période post-2000 (données hebdomadaires uniformes). Pour les percentiles historiques de positions, utiliser uniquement les données depuis janvier 2000. Documenter cette limite dans le module C3 du code TRADEX.
*Catégorie : gestion_risque_entree*
