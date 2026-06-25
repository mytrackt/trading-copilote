# Extraction CFTC — Variable Names Traders in Financial Futures (TFF)
**Source :** `bundles/cftc/cot_variables_tff.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9651 → D9670 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariablestfm.html
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : C3 Institutionnels + C4 Macro — dictionnaire officiel des 87 colonnes du rapport COT TFF (4 catégories : Dealer/Intermediary, Asset Manager, Leveraged Money, Other Reportable) — pertinent pour ES (S&P500) et DX (Dollar Index) en tant qu'actifs de CONFIRMATION TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D9651 — Champ de date TFF : Report_Date_as_MM_DD_YYYY (col. 3)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : Le rapport TFF utilise `Report_Date_as_MM_DD_YYYY` (col. 3) à la place de `As_of_Date_Form_YYYY-MM-DD` du Disaggregated. Format américain MM/DD/YYYY au lieu de ISO 8601.
**TRADEX-AI C3/C4** : Le parser TFF doit convertir explicitement ce format avec `pd.to_datetime(df['Report_Date_as_MM_DD_YYYY'], format='%m/%d/%Y')` avant tout traitement. Risque de confusion date/mois si non géré — bug silencieux potentiel dans les séries temporelles.
*Catégorie : structure_marche*

### D9652 — Structure d'identification TFF (cols 1–7)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : Colonnes 1–7 identiques en structure au Disaggregated : `Market_and_Exchange_Names`, `As_of_Date_In_Form_YYMMDD`, `Report_Date_as_MM_DD_YYYY`, `CFTC_Contract_Market_Code`, `CFTC_Market_Code`, `CFTC_Region_Code`, `CFTC_Commodity_Code`. Même convention tirets bas.
**TRADEX-AI C3/C4** : Pour ES (S&P 500 E-mini CME) et DX (Dollar Index ICE), les codes CFTC TFF sont respectivement 13874A et 098662. Ces codes doivent être ajoutés à `settings.py` sous `CFTC_CODES_TFF` distincts des codes Disaggregated.
*Catégorie : structure_marche*

### D9653 — Catégorie Dealer/Intermediary TFF (cols 9–11)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Dealer_Positions_Long_All`, `Dealer_Positions_Short_All`, `Dealer_Positions_Spread_All` — les Dealers sont les grandes banques et courtiers de marché (Goldman Sachs, JPMorgan, etc.) qui tiennent des marchés sur les futures financiers. Équivalent des Swap Dealers du Disaggregated, mais pour les marchés financiers (indices, devises, taux).
**TRADEX-AI C4** : Sur DX (Dollar Index), les Dealers long = signe que les grandes banques anticipent une hausse du dollar → impact baissier sur GC/HG (corrélation inverse). Cette variable TFF alimente le cercle C4 Macro de TRADEX-AI pour filtrer les signaux sur métaux.
*Catégorie : correlations*

### D9654 — Catégorie Asset Manager/Institutional (cols 12–14)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Asset_Mgr_Positions_Long_All`, `Asset_Mgr_Positions_Short_All`, `Asset_Mgr_Positions_Spread_All` — les Asset Managers sont les fonds de pension, mutual funds, compagnies d'assurance. Ce sont les détenteurs de positions les plus stables et les plus longues.
**TRADEX-AI C4** : Sur ES (S&P 500), un net long élevé des Asset Managers = exposition institutionnelle structurelle au risque équité. Si ce net long diminue brusquement → "deleveraging" institutionnel probable → impact baissier sur risque global → signal C5 de prudence sur GC (refuge).
*Catégorie : macro_evenements*

### D9655 — Catégorie Leveraged Money TFF (cols 15–17)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Lev_Money_Positions_Long_All`, `Lev_Money_Positions_Short_All`, `Lev_Money_Positions_Spread_All` — les Leveraged Money sont les hedge funds et CTA opérant sur les marchés financiers (indices, devises). Équivalent des Managed Money du Disaggregated, mais sur les futures financiers.
**TRADEX-AI C4** : Leveraged Money net short sur ES = hedge funds positionnés à la baisse sur les actions → contexte "risk-off" → signal favorable à GC (valeur refuge). Cette connexion ES-TFF → GC constitue une règle C4×C3 dans la grille /10 de TRADEX-AI.
*Catégorie : correlations*

### D9656 — Catégorie Other Reportable TFF (cols 18–20)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Other_Rept_Positions_Long_All`, `Other_Rept_Positions_Short_All`, `Other_Rept_Positions_Spread_All` — entités déclarantes ne rentrant dans aucune des 3 catégories principales (petits fonds, family offices sur futures financiers).
**TRADEX-AI C4** : Signal tertiaire dans le TFF — moins d'importance que Lev_Money ou Asset_Mgr. Utile uniquement en confirmation si cette catégorie se rallie massivement à une direction sur DX ou ES.
*Catégorie : indicateurs_tendance*

### D9657 — Total Reportable et Non-Reportable TFF (cols 21–24)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Tot_Rept_Positions_Long_All`, `Tot_Rept_Positions_Short_All`, `NonRept_Positions_Long_All`, `NonRept_Positions_Short_All` — même structure que Disaggregated et Legacy. Les Non-Reportable TFF sont les petits traders sur futures financiers.
**TRADEX-AI C4** : Non-Reportable net long extrême sur ES = retail haussier sur actions → signal contrarian modéré (potentiel top marché). Combiné avec VIX élevé (C5) → signal de prudence amplifiée pour TRADEX-AI sur tous les actifs.
*Catégorie : psychologie*

### D9658 — Variations hebdomadaires TFF (cols 25–41)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Change_in_Open_Interest_All`, `Change_in_Dealer_Long/Short/Spread_All`, `Change_in_Asset_Mgr_Long/Short/Spread_All`, `Change_in_Lev_Money_Long/Short/Spread_All`, `Change_in_Other_Rept_Long/Short/Spread_All`, `Change_in_Tot_Rept_Long/Short_All`, `Change_in_NonRept_Long/Short_All`.
**TRADEX-AI C4** : Flux Leveraged Money hebdomadaire sur DX = `Change_in_Lev_Money_Long_All` − `Change_in_Lev_Money_Short_All`. Flux positif croissant sur DX pendant 2–3 semaines = momentum haussier dollar institutionnel → contexte défavorable pour GC/HG à intégrer dans filtre C4.
*Catégorie : indicateurs_momentum*

### D9659 — Pourcentages d'OI TFF (cols 42–58)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Pct_of_Open_Interest_All` puis `Pct_of_OI_Dealer/Asset_Mgr/Lev_Money/Other_Rept/Tot_Rept/NonRept_Long/Short/Spread_All`. Seule la variante "All" existe dans TFF (pas de Old/Other contrairement à Disaggregated).
**TRADEX-AI C4** : Différence structurelle majeure avec Disaggregated : le TFF ne décompose pas en All/Old/Other. Une seule série temporelle par variable. Plus simple à parser — un seul jeu de colonnes à charger. Le `%_of_OI_Lev_Money_Long_All` sur ES est l'indicateur clé du cycle de levier des hedge funds.
*Catégorie : structure_marche*

### D9660 — Nombre de traders TFF (cols 59–73)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Traders_Tot_All`, `Traders_Dealer_Long/Short/Spread_All`, `Traders_Asset_Mgr_Long/Short/Spread_All`, `Traders_Lev_Money_Long/Short/Spread_All`, `Traders_Other_Rept_Long/Short/Spread_All`, `Traders_Tot_Rept_Long/Short_All`.
**TRADEX-AI C4** : Nombre de Leveraged Money long sur ES très faible (< 10) avec position nette massive = concentration extrême de hedge funds haussiers sur actions → risque de "unwind" brutal si sentiment change. Signal de fragilité systémique à intégrer dans le circuit breaker C5.
*Catégorie : gestion_risque_entree*

### D9661 — Ratios de concentration TFF (cols 74–81)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `Conc_Gross_LE_4_TDR_Long/Short_All`, `Conc_Gross_LE_8_TDR_Long/Short_All`, `Conc_Net_LE_4_TDR_Long/Short_All`, `Conc_Net_LE_8_TDR_Long/Short_All` — seule la variante "All" dans TFF (pas de Old/Other).
**TRADEX-AI C4** : Concentration Top 4 net long sur DX > 50% = dollar contrôlé par 4 acteurs majeurs → marché directeur potentiellement manipulé. Si ce contexte est combiné avec GC à un niveau clé Belkhayate → signal d'invalidation possible (C4 override C1).
*Catégorie : gestion_risque_entree*

### D9662 — Champ FutOnly_or_Combined TFF (col. 87)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_tff.md) : `FutOnly_or_Combined` présent dans TFF — même signification que dans Disaggregated : "F" = Futures Only, "C" = Futures + Options Combined.
**TRADEX-AI C4** : Même règle que Disaggregated — utiliser `"F"` uniquement pour ES et DX dans TRADEX-AI. Le filtre doit être appliqué au niveau du parser TFF.
*Catégorie : structure_marche*

### D9663 — Pertinence TFF pour ES (S&P 500 E-mini)
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : ES est l'actif de CONFIRMATION TRADEX-AI (cercle C2/C4). Le rapport TFF est le format COT adapté aux futures financiers. Pour ES, les 4 catégories TFF donnent une image précise du positionnement institutionnel sur les actions américaines.
**TRADEX-AI C4** : Signal composite ES-TFF pour TRADEX-AI : si (Asset_Mgr net long ES diminue) AND (Lev_Money net short ES augmente) AND (VX > 20) → contexte "risk-off" → boost signal GC long si Belkhayate C1 est aligné. Cette règle croise C3, C4, C5 dans la grille /10.
*Catégorie : macro_evenements*

### D9664 — Pertinence TFF pour DX (Dollar Index)
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : DX est l'actif de CONFIRMATION TRADEX-AI (cercle C4 Macro). Le rapport TFF contient les positions institutionnelles sur le Dollar Index via les futures ICE. Corrélation historique inverse DX/GC : DX hausse → GC baisse (et inversement).
**TRADEX-AI C4** : Signal DX-TFF pour filtre C4 : `Lev_Money_net_DX = Lev_Money_Long_DX - Lev_Money_Short_DX`. Si ce net est positif ET croissant → pression baissière sur GC/HG. À intégrer comme facteur de pondération négatif dans le score /10 du cercle C4 lors d'un signal GC long.
*Catégorie : correlations*

### D9665 — TFF : absence des variantes Old/Other
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : Contrairement au Disaggregated (191 colonnes avec All/Old/Other) et au Legacy (130 colonnes avec All/Old/Other), le TFF n'a que 87 colonnes sans la décomposition Old/Other. Une seule série temporelle "All" par variable.
**TRADEX-AI C4** : Avantage du TFF pour le pipeline : structure plus simple, moins de colonnes, pas de gestion Old/Other. Le parser TFF sera la version la plus légère. Inconvénient : pas d'analyse roll pressure sur ES/DX (ces marchés ont peu de roll spread significatif de toute façon).
*Catégorie : structure_marche*

### D9666 — Formule net Leveraged Money TFF
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : Net Leveraged Money = `Lev_Money_Positions_Long_All` − `Lev_Money_Positions_Short_All`. Les Spreads (`Lev_Money_Positions_Spread_All`) s'excluent du calcul directionnel. Z-score sur 52 semaines recommandé comme pour Managed Money Disaggregated.
**TRADEX-AI C4** : Implémenter dans `correlations.py` : `cot_tff_lev_net = lev_long - lev_short` pour ES et DX séparément. Ces deux z-scores alimentent respectivement le signal "risk appetite" (ES) et le signal "dollar direction" (DX) dans la grille /10 de TRADEX-AI.
*Catégorie : indicateurs_tendance*

### D9667 — Dealer/Intermediary TFF vs Swap Dealers Disaggregated
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : Les Dealer/Intermediary TFF et les Swap Dealers Disaggregated jouent des rôles analogues mais sur des marchés différents : Dealers TFF sur futures financiers (ES, DX, obligations) ; Swap Dealers Disagg sur commodités (GC, HG, CL, ZW). Conceptuellement équivalents : intermédiaires financiers prenant l'autre côté des swaps.
**TRADEX-AI C3/C4** : Cette dualité permet une lecture croisée C3×C4 : si Swap Dealers Disagg augmentent leur short sur GC EN MÊME TEMPS que les Dealers TFF augmentent leur long sur DX → signal baissier doublement confirmé sur l'or (pression institutionnelle directe + pression macro dollar).
*Catégorie : correlations*

### D9668 — Contrainte comptable TFF et validation intégrité
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : Même contrainte comptable que Legacy : `Tot_Rept_Long + NonRept_Long = Open_Interest_All`. Également : somme des positions Long de toutes catégories reportables ≈ `Tot_Rept_Positions_Long_All`.
**TRADEX-AI C4** : Implémenter la même validation d'intégrité que pour Legacy (D9649) dans le parser TFF. Si `(dealer_long + asset_mgr_long + lev_money_long + other_rept_long) ≠ tot_rept_long` → données corrompues → bloquer signal C4 pour la semaine.
*Catégorie : gestion_risque_entree*

### D9669 — Synthèse des 3 formats COT pour TRADEX-AI
🟡 **SYNTHÈSE** (Source : cot_variables_disaggregated.md + cot_variables_legacy.md + cot_variables_tff.md) : Trois formats COT CFTC complémentaires pour TRADEX-AI : (1) Disaggregated = GC/HG/CL/ZW avec 4 sous-catégories précises — PRIORITÉ pour signaux C3. (2) Legacy = historique pré-2009 GC/HG/CL/ZW — utilisé pour calibration seuils. (3) TFF = ES/DX avec 4 sous-catégories financières — PRIORITÉ pour signaux C4.
**TRADEX-AI C3+C4** : Architecture recommandée `data_reader.py` : trois fonctions `load_cot_disagg(actifs=[GC,HG,CL,ZW])`, `load_cot_legacy(actifs=[GC,HG,CL,ZW], until=2009)`, `load_cot_tff(actifs=[ES,DX])` → alimentation séparée des cercles C3 (commodités) et C4 (macro financier) dans la grille /10.
*Catégorie : structure_marche*

### D9670 — Correspondance TFF avec actifs TRADEX de CONFIRMATION
🟡 **SYNTHÈSE** (Source : cot_variables_tff.md) : Le rapport TFF couvre les futures financiers. Pour TRADEX-AI, deux actifs de CONFIRMATION sont présents dans TFF : ES (S&P 500 E-mini, code CFTC 13874A) et DX (Dollar Index ICE, code CFTC 098662). VX (VIX) n'est pas disponible dans le rapport TFF standard — utiliser les données de marché directes pour VX.
**TRADEX-AI C4** : Confirmer que MBT (Bitcoin Micro) et 6J (Yen) ne sont PAS dans le rapport TFF standard. Ces actifs de RÉFÉRENCE n'ont pas de signal COT dans le pipeline TRADEX-AI — cohérent avec la règle "RÉFÉRENCE = corrélations uniquement, pas d'ordres". Le rapport TFF alimente exclusivement ES et DX dans le cercle C4.
*Catégorie : structure_marche*
