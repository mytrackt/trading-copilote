# Extraction CFTC — Variables CIT Supplement (Commodity Index Trader)
**Source :** `bundles/cftc/cot_variables_cit.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9591 → D9610 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariablescitsupplement.html
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Dictionnaire complet des 54 variables du supplément CIT — référence technique pour parser les données CSV CFTC et alimenter le Cercle C3 Institutionnels de TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9591 — Structure CSV CIT : 54 champs ordonnés, champ 1 = identifiant marché
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Le fichier CSV du supplément CIT contient exactement 54 champs numérotés. Le champ 1 (Market_and_Exchange_Names) identifie le marché et la bourse. Les champs 2-3 fournissent la date du rapport en deux formats (YYMMDD et MM/DD/YYYY).
**TRADEX-AI C3** : Structure de référence pour le parseur CIT de TRADEX — filtrer sur Market_and_Exchange_Names pour extraire les 4 actifs TRADING : « GOLD » (GC-CME), « COPPER » (HG-CME), « CRUDE OIL, LIGHT SWEET » (CL-CME), « WHEAT » (ZW-CBOT). Valider la correspondance avec les codes CFTC (champs 4-7).
*Catégorie : structure_marche*

### D9592 — Champs 4-7 : codes CFTC d'identification unique par contrat et marché
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Quatre champs d'identification CFTC distincts — champ 4 : CFTC_Contract_Market_Code (code unique du contrat), champ 5 : CFTC_Market_Code, champ 6 : CFTC_Region_Code, champ 7 : CFTC_Commodity_Code. Ces codes permettent une identification non ambiguë de chaque contrat.
**TRADEX-AI C3** : Codes CFTC de référence pour TRADEX — utiliser CFTC_Contract_Market_Code comme clé primaire de jointure entre les différents fichiers COT annuels. Codes connus : GC=088691, HG=085692, CL=067651, ZW=001602 (à vérifier dans les fichiers CSV réels).
*Catégorie : structure_marche*

### D9593 — Champ 8 : Open_Interest_All = open interest total toutes catégories
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Le champ 8 (Open_Interest_All) représente l'open interest total sur le marché, toutes catégories de traders confondues. C'est la référence de base pour calculer les pourcentages de positionnement par catégorie.
**TRADEX-AI C3** : Open Interest total = dénominateur commun pour tous les ratios institutionnels TRADEX. Une hausse soudaine de l'OI sur GC ou CL sans mouvement de prix correspondant peut signaler une accumulation institutionnelle silencieuse — signal C3 à croiser avec Footprint ATAS (C2).
*Catégorie : volume_liquidite*

### D9594 — Champs 9-11 : positions Non-Commercial NoCIT (excluant les CIT)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Trois champs couvrent les positions Non-Commercial hors Commodity Index Traders — champ 9 : NComm_Positions_Long_All_NoCIT, champ 10 : NComm_Positions_Short_All_NoCIT, champ 11 : NComm_Postions_Spread_All_NoCIT. Le suffixe « NoCIT » indique l'exclusion des fonds indiciels.
**TRADEX-AI C3** : La décomposition NoCIT isole les spéculateurs purs (hedge funds, CTAs) des fonds indiciels passifs. Pour TRADEX, comparer NComm_Positions_Long_NoCIT vs NComm_Positions_Short_NoCIT donne le net spéculatif hors biais indiciel — signal directionnel plus pur sur GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

### D9595 — Champs 12-13 : positions Commercial NoCIT (producteurs et hedgers purs, hors CIT)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Champ 12 : Comm_Positions_Long_All_NoCIT, champ 13 : Comm_Positions_Short_All_NoCIT. Ces champs représentent les positions des opérateurs commerciaux (producteurs, transformateurs, utilisateurs) après exclusion des Commodity Index Traders.
**TRADEX-AI C3** : Positions Commercial NoCIT = proxy du positionnement des producteurs physiques (mines d'or pour GC, raffineurs pour CL, agriculteurs pour ZW). Un net short Commercial NoCIT extrême signale une couverture massive de production = indicateur contrarien haussier pour l'actif (règle classique Belkhayate C3).
*Catégorie : indicateurs_tendance*

### D9596 — Champs 14-15 et 16-17 : total reportable vs non-reportable (petits opérateurs)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Champs 14-15 : Tot_Rept_Positions_Long/Short_All (total des positions reportables). Champs 16-17 : NonRept_Positions_Long/Short_All (positions des petits traders non-reportables, calculées par différence avec l'open interest total).
**TRADEX-AI C3** : Le ratio NonRept/OI mesure la part des « petits spéculateurs ». Dans la méthode Belkhayate, un positionnement extrême des non-reportables dans le sens opposé aux Commerciaux renforce le signal contrarien. Signal C3 secondaire sur GC/ZW (marchés à forte participation retail).
*Catégorie : psychologie*

### D9597 — Champs 18-19 : CIT_Positions_Long/Short_All = positionnement exclusif des fonds indiciels matières premières
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Champ 18 : CIT_Positions_Long_All, champ 19 : CIT_Positions_Short_All. Ces champs isolent exclusivement les positions des Commodity Index Traders (CIT) — fonds indiciels passifs répliquant des indices matières premières (type Bloomberg Commodity Index, S&P GSCI).
**TRADEX-AI C3** : Les CIT maintiennent structurellement des positions long importantes sur GC/HG/CL/ZW. Une hausse soudaine des CIT_Positions_Long indique un afflux de capitaux indiciels passifs — biais haussier structurel mais non directionnel à court terme. Signal C3 de contexte, pas de timing.
*Catégorie : correlations*

### D9598 — Champs 20-31 : variations hebdomadaires (Change_) de toutes les catégories de positions
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Les champs 20-31 couvrent les variations hebdomadaires (Change_) de chaque catégorie de positions — Open Interest (champ 20), NonComm Long/Short/Spread NoCIT (21-23), Comm Long/Short NoCIT (24-25), Tot_Rept Long/Short (26-27), NonRept Long/Short (28-29), CIT Long/Short (30-31).
**TRADEX-AI C3** : Les champs Change_ sont les signaux d'alerte primaires pour TRADEX — une variation hebdomadaire significative de Change_NonComm_Long_NoCIT ou Change_CIT_Long sur GC/CL mérite une analyse approfondie. Seuil d'alerte à calibrer par actif (ex : variation > 2 écarts-types sur 52 semaines).
*Catégorie : indicateurs_momentum*

### D9599 — Champs 32-43 : pourcentages d'open interest (Pct_OI_) par catégorie
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Les champs 32-43 expriment chaque catégorie de positions en pourcentage de l'open interest total — champ 32 : Pct_Open_Interest_All (=100%), puis Pct_OI_ pour NonComm Long/Short/Spread NoCIT (33-35), Comm Long/Short NoCIT (36-37), Tot_Rept Long/Short NoCIT (38-39), NonRept Long/Short NoCIT (40-41), CIT Long/Short (42-43).
**TRADEX-AI C3** : Les Pct_OI sont les métriques normalisées recommandées pour TRADEX — comparables entre actifs (GC vs ZW) et dans le temps. Indicateurs de concentration institutionnelle : si Pct_OI_NonComm_Long_NoCIT > 35% sur GC, signal de surexposition spéculative à risque de retournement.
*Catégorie : gestion_risque_entree*

### D9600 — Champs 44-53 : comptage des traders par catégorie (Traders_)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Les champs 44-53 fournissent le nombre de traders par catégorie — Traders_Tot_All (44), Traders_NonComm Long/Short/Spread NoCIT (45-47), Traders_Comm Long/Short NoCIT (48-49), Traders_Tot_Rept Long/Short NoCIT (50-51), Traders_CIT Long/Short (52-53).
**TRADEX-AI C3** : Le comptage de traders complète l'analyse de position — un Traders_CIT_Long élevé avec CIT_Positions_Long modéré signale une dispersion (petits fonds indiciels) ; l'inverse signale une concentration (peu de grands fonds). La concentration CIT sur GC peut amplifier les mouvements de prix lors de rebalancement indiciel.
*Catégorie : volume_liquidite*

### D9601 — Champ 54 : Contract_Units = unité de mesure du contrat (nombre de contrats)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Le champ 54 (Contract_Units) indique l'unité de mesure utilisée pour exprimer les positions dans ce fichier CSV — typiquement le nombre de contrats à terme.
**TRADEX-AI C3** : Référence de conversion pour TRADEX — chaque contrat GC = 100 troy onces, HG = 25 000 livres, CL = 1 000 barils, ZW = 5 000 boisseaux. Multiplier les positions COT par Contract_Units pour obtenir les expositions en unités physiques et estimer l'impact marché potentiel.
*Catégorie : gestion_position_active*

### D9602 — Séparation NoCIT : les CIT sont retirés des catégories Commercial et Non-Commercial
🟡 **SYNTHÈSE** (Source : cot_variables_cit.md) : La logique du supplément CIT repose sur l'extraction des Commodity Index Traders des catégories existantes. Les positions « NoCIT » (champs 9-13) représentent les catégories Commercial et Non-Commercial après soustraction des positions CIT. L'OI total reste identique.
**TRADEX-AI C3** : Règle d'interprétation COT pour TRADEX — toujours utiliser les variantes NoCIT pour analyser les signaux directionnels de trading. Les positions CIT étant passives (réplication indicielle), elles bruitent les signaux directionnels. Utiliser CIT_Long/Short séparément comme indicateur de flux passifs structurels.
*Catégorie : gestion_risque_entree*

### D9603 — Doublon de date (champs 2-3) : format YYMMDD pour tri, MM/DD/YYYY pour affichage
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_cit.md) : Le fichier CSV fournit la date du rapport en deux formats distincts — champ 2 : As_of_Date_In_Form_YYMMDD (format numérique pour tri et jointure), champ 3 : As_of_Date_In_Form_MM/DD/YYYY (format lisible pour affichage).
**TRADEX-AI C3** : Pour le parseur TRADEX, utiliser le champ 2 (YYMMDD) comme clé temporelle de jointure entre les différents fichiers COT annuels et les séries de prix NT8. Convertir en datetime Python avec strptime('%y%m%d') pour aligner avec les timestamps des données de marché.
*Catégorie : macro_evenements*
