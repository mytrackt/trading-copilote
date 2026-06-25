# Extraction CFTC — Variable Names Disaggregated Report
**Source :** `bundles/cftc/cot_variables_disaggregated.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9611 → D9630 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalViewable/CFTC_023168.html
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : C3 Institutionnels — dictionnaire officiel des 191 colonnes du rapport COT Disaggregated (4 catégories : Prod/Merc, Swap, Managed Money, Other Reportable) utilisables pour parser les données GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D9611 — Structure d'identification du marché (colonnes 1–7)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Les 7 premiers champs du fichier CSV Disaggregated identifient le contrat : `Market_and_Exchange_Names`, `As_of_Date_In_Form_YYMMDD`, `As_of_Date_Form_YYYY-MM-DD`, `CFTC_Contract_Market_Code`, `CFTC_Market_Code`, `CFTC_Region_Code`, `CFTC_Commodity_Code`. Ces champs permettent de filtrer les lignes relatives à GC (Or), HG (Cuivre), CL (Pétrole), ZW (Blé).
**TRADEX-AI C3** : Le parser `data_reader.py` doit filtrer sur `CFTC_Commodity_Code` pour isoler GC/HG/CL/ZW avant toute lecture de position.
*Catégorie : structure_marche*

### D9612 — Open Interest total et par sous-groupe
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Trois variantes d'Open Interest existent : `Open_Interest_All` (col. 8), `Open_Interest_Old` (col. 24), `Open_Interest_Other` (col. 40). "All" = futures + options combinés. "Old" = contrats proches de l'échéance. "Other" = contrats plus lointains.
**TRADEX-AI C3** : Utiliser `Open_Interest_All` comme dénominateur pour tous les ratios de % d'OI dans le cercle C3. `Open_Interest_Old` permet de surveiller la pression sur les contrats spot proches — pertinent pour GC/CL en période de roll.
*Catégorie : volume_liquidite*

### D9613 — Catégorie Producer/Merchant (cols 9–10, 25–26, 41–42)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Prod_Merc_Positions_Long_All` et `Prod_Merc_Positions_Short_All` représentent les positions des producteurs et marchands — entités qui utilisent les futures pour se couvrir contre les risques liés à leur activité physique (mineurs d'or, raffineurs de pétrole, meuniers pour ZW, fonderies pour HG).
**TRADEX-AI C3** : Une augmentation nette short des Prod/Merc sur GC (ex. mines vendant leur production) est un signal baissier fort côté institutionnel. Contraire = couverture d'anticipation de hausse.
*Catégorie : indicateurs_tendance*

### D9614 — Catégorie Swap Dealers (cols 11–13, 27–29, 43–45)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Swap_Positions_Long_All`, `Swap__Positions_Short_All`, `Swap__Positions_Spread_All` — les Swap Dealers sont des intermédiaires financiers qui prennent l'autre côté des swaps OTC (banques, dealers). Leur position spread indique des stratégies inter-échéances.
**TRADEX-AI C3** : Un fort accroissement short des Swap Dealers sur GC sans couverture correspondante signale souvent une distribution institutionnelle. La position spread croissante indique un arbitrage calendaire actif — contexte de range probable.
*Catégorie : structure_marche*

### D9615 — Catégorie Managed Money (cols 14–16, 30–32, 46–48)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `M_Money_Positions_Long_All`, `M_Money_Positions_Short_All`, `M_Money_Positions_Spread_All` — les Managed Money sont les fonds spéculatifs (hedge funds, CTA). Ce sont les acteurs les plus directionnels du rapport Disaggregated.
**TRADEX-AI C3** : Net position Managed Money = `M_Money_Positions_Long_All` − `M_Money_Positions_Short_All`. Un net long élevé ET croissant sur GC/CL = signal C3 haussier. Divergence avec le prix = signal de retournement potentiel (règle COT classique).
*Catégorie : indicateurs_tendance*

### D9616 — Catégorie Other Reportable (cols 17–19, 33–35, 49–51)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Other_Rept_Positions_Long_All`, `Other_Rept_Positions_Short_All`, `Other_Rept_Positions_Spread_All` — regroupe les entités déclarantes qui ne rentrent ni dans Prod/Merc, ni Swap, ni Managed Money (petits fonds, family offices, etc.).
**TRADEX-AI C3** : Signal secondaire — moins fiable seul, mais utile en confirmation si cette catégorie se rallie à la direction Managed Money.
*Catégorie : indicateurs_tendance*

### D9617 — Total Reportable et Non-Reportable (cols 20–23)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Tot_Rept_Positions_Long_All` + `Tot_Rept_Positions_Short_All` = somme des 4 catégories déclarantes. `NonRept_Positions_Long_All` + `NonRept_Positions_Short_All` = petits spéculateurs sous le seuil de déclaration.
**TRADEX-AI C3** : Positions non-déclarantes croissantes long = foule de détail haussière → souvent signal contrarian baissier à l'extrême (crowd top). À surveiller sur GC/HG.
*Catégorie : psychologie*

### D9618 — Colonnes de variation hebdomadaire (cols 56–71)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Série `Change_in_*` (ex. `Change_in_Open_Interest_All`, `Change_in_M_Money_Long_All`, etc.) — chaque champ représente la variation nette entre le rapport courant et le rapport précédent (une semaine).
**TRADEX-AI C3** : `Change_in_M_Money_Long_All` − `Change_in_M_Money_Short_All` = flux net hebdomadaire des hedge funds. Un flux net positif > seuil configurable sur plusieurs semaines consécutives = momentum institutionnel confirmé → boost score C3.
*Catégorie : indicateurs_momentum*

### D9619 — Pourcentages d'Open Interest (cols 72–119)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Série `Pct_of_OI_*` — exprime chaque position en % de l'Open Interest total. Ex. `Pct_of_OI_M_Money_Long_All` = % OI détenu en long par les Managed Money.
**TRADEX-AI C3** : Les % OI sont préférables aux valeurs absolues pour comparer GC vs HG vs CL vs ZW (tailles de marchés différentes). Seuil de signal : si `Pct_of_OI_M_Money_Long_All` > `Pct_of_OI_M_Money_Short_All` + 10 points → position nette significative confirmée.
*Catégorie : indicateurs_tendance*

### D9620 — Nombre de traders par catégorie (cols 120–161)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Série `Traders_*` — nombre d'entités distinctes déclarant des positions dans chaque catégorie. Ex. `Traders_M_Money_Long_All`, `Traders_Swap_Long_All`. Séparé par sous-groupe (All/Old/Other).
**TRADEX-AI C3** : Un faible nombre de traders Managed Money long (ex. < 5) avec une grande position long nette = concentration extrême → risque de retournement brutal si quelques entités débouclent. Signal d'alerte à intégrer dans la gestion du risque (cercle C3 × C5).
*Catégorie : gestion_risque_entree*

### D9621 — Ratios de concentration Top 4 et Top 8 traders (cols 162–185)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Conc_Gross_LE_4_TDR_Long_All`, `Conc_Gross_LE_8_TDR_Long_All`, `Conc_Net_LE_4_TDR_Long_All`, `Conc_Net_LE_8_TDR_Long_All` (et variantes Short/Old/Other) — % de l'OI détenu par les 4 et 8 plus grands traders.
**TRADEX-AI C3** : Concentration Top 4 long > 60% sur GC = marché contrôlé par très peu d'acteurs → stop hunt probable, liquidité artificielle. Ajouter cette métrique au filtre C3 pour éviter les signaux dans des marchés manipulés par une poignée de géants.
*Catégorie : gestion_risque_entree*

### D9622 — Champ FutOnly_or_Combined (col. 191)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `FutOnly_or_Combined` indique si la ligne correspond au rapport Futures Seulement ("F") ou Futures + Options Combinés ("C"). Deux lignes par marché dans le fichier CSV complet.
**TRADEX-AI C3** : Utiliser exclusivement `FutOnly_or_Combined = "F"` pour l'analyse TRADEX-AI (les options ajoutent du bruit pour les actifs CME/CBOT tradés en mode pur futures). Filtrer au niveau du parser.
*Catégorie : structure_marche*

### D9623 — Triplet All/Old/Other : interprétation opérationnelle
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md) : Le rapport Disaggregated duplique chaque position sur 3 sous-ensembles temporels : "All" (tous contrats), "Old" (premier contrat de livraison), "Other" (contrats suivants). La plupart des analyses COT courantes n'utilisent que "All".
**TRADEX-AI C3** : Règle opérationnelle : parser en priorité les colonnes `_All`. N'extraire `_Old` que si une divergence Old/Other est détectée (signal roll pressure sur CL ou GC) → indicateur avancé de changement de positionnement avant roll.
*Catégorie : timing*

### D9624 — Correspondance codes CFTC avec actifs TRADEX
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md + CFTC public) : Les champs `CFTC_Contract_Market_Code` et `CFTC_Commodity_Code` permettent l'identification exacte. Codes connus : GC (Or COMEX) = 088691 / 084691 ; HG (Cuivre COMEX) = 085692 ; CL (WTI NYMEX) = 067651 ; ZW (Blé CBOT) = 001602.
**TRADEX-AI C3** : Ces codes doivent être configurés comme constantes dans `settings.py` sous `CFTC_CODES` pour que `data_reader.py` filtre automatiquement les lignes pertinentes lors de l'ingestion du CSV hebdomadaire CFTC.
*Catégorie : structure_marche*

### D9625 — Net Position Managed Money : formule canonique
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md) : Formule net position MM = `M_Money_Positions_Long_All` − `M_Money_Positions_Short_All`. Pour exclure les spreads (positions neutres inter-échéances) : Net ajusté = Long − Short (les spreads s'annulent). La colonne `M_Money_Positions_Spread_All` n'entre pas dans le calcul directionnel.
**TRADEX-AI C3** : Implémenter cette formule dans `correlations.py` comme signal de base COT. Calculer également le z-score sur 52 semaines pour normaliser selon le contexte historique de chaque actif (GC a un OI très différent de ZW).
*Catégorie : indicateurs_tendance*

### D9626 — Comparaison Disaggregated vs Legacy : profondeur analytique
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md) : Le rapport Disaggregated (depuis 2009) décompose les Commercials Legacy en 3 sous-catégories (Prod/Merc + Swap + Other Reportable) et les Non-commercials en Managed Money + Other Reportable. Cette granularité manque dans le rapport Legacy.
**TRADEX-AI C3** : Pour GC/HG/CL/ZW, préférer systématiquement le rapport Disaggregated au Legacy. Le Legacy reste utile pour l'historique pré-2009 uniquement. Les données S27 du pipeline CFTC doivent pointer vers les fichiers Disaggregated en priorité.
*Catégorie : structure_marche*

### D9627 — Contrainte de fréquence hebdomadaire du rapport COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : Le champ `As_of_Date_Form_YYYY-MM-DD` confirme la granularité : une ligne par marché par semaine (positions au mardi, publiées vendredi). Le rapport Disaggregated n'est pas intraday.
**TRADEX-AI C3** : Intégration dans l'architecture événementielle : le cercle C3 ne peut pas déclencher seul un signal intraday. Rôle = filtre de contexte hebdomadaire (bullish/bearish bias institutionnel), jamais déclencheur. Mise à jour du signal C3 = 1x/semaine après publication CFTC (vendredi ~15h30 ET).
*Catégorie : timing*

### D9628 — Champ CFTC_SubGroup_Code (col. 190)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `CFTC_SubGroup_Code` classe les contrats en sous-groupes thématiques (ex. métaux, énergie, grains). Utilisé pour grouper les marchés dans les publications CFTC.
**TRADEX-AI C3** : Facultatif pour le parser TRADEX-AI — la sélection se fait déjà via `CFTC_Commodity_Code`. Utile si on veut grouper GC+HG comme "métaux" pour un signal de corrélation inter-marché C3×C7.
*Catégorie : correlations*

### D9629 — Variable Contract_Units (col. 186)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_disaggregated.md) : `Contract_Units` indique l'unité de contrat (ex. "TROY OUNCES" pour GC, "POUNDS" pour HG, "BARRELS" pour CL, "BUSHELS" pour ZW).
**TRADEX-AI C3** : Stocker cette variable pour conversion des positions en valeur notionnelle si nécessaire (ex. 1 contrat GC = 100 troy oz × prix spot = valeur $). Permet d'estimer l'exposition notionnelle totale des Managed Money sur GC en dollars — indicateur d'appétit institutionnel absolu.
*Catégorie : volume_liquidite*

### D9630 — Architecture parsing recommandée pour le pipeline TRADEX
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md) : Le fichier CSV Disaggregated contient 191 colonnes. Pour TRADEX-AI, seuls ~20 champs sont utiles : identifiants (1–7), positions All des 4 catégories (8–23), variations hebdomadaires All (56–71), % OI All (72–87), nombre traders All (120–133), concentration (162–169), FutOnly_or_Combined (191).
**TRADEX-AI C3** : Définir une liste `DISAGG_COLS_USEFUL` dans `settings.py` pour ne charger que ces colonnes via `pandas.read_csv(usecols=...)` → réduction drastique de l'empreinte mémoire lors du traitement hebdomadaire des 4 actifs.
*Catégorie : structure_marche*
