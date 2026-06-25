# Extraction CFTC — Variable Names Legacy/Traditional Report
**Source :** `bundles/cftc/cot_variables_legacy.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D9631 → D9650 · **Page :** https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalViewable/cotvariableslegacy.html
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : C3 Institutionnels — dictionnaire officiel des 130 colonnes du rapport COT Legacy (2 catégories : Commercial / Non-Commercial) — référence historique pré-2009 et format simplifié pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D9631 — Structure d'identification du marché Legacy (cols 1–7)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Les 7 premiers champs identifient le contrat : `Market and Exchange Names`, `As of Date in Form YYMMDD`, `As of Date in Form YYYY-MM-DD`, `CFTC Contract Market Code`, `CFTC Market Code in Initials`, `CFTC Region Code`, `CFTC Commodity Code`. Structure similaire au Disaggregated mais avec des noms de colonnes contenant des espaces (pas de tirets bas).
**TRADEX-AI C3** : Attention parsing — le fichier Legacy utilise des espaces dans les noms de colonnes contrairement au Disaggregated qui utilise des tirets bas (`_`). Le parser `data_reader.py` doit gérer les deux conventions ou normaliser via `df.columns = df.columns.str.replace(' ', '_')`.
*Catégorie : structure_marche*

### D9632 — Catégorie Non-commercial (cols 9–11 et déclinaisons)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Noncommercial Positions-Long (All)`, `Noncommercial Positions-Short (All)`, `Noncommercial Positions-Spreading (All)` — les Non-commercials sont les spéculateurs purs (fonds, CTA) dans la classification Legacy. Équivalent approximatif des Managed Money du Disaggregated.
**TRADEX-AI C3** : Net Non-commercial = Long − Short. Cette métrique est la variable la plus suivie par les traders COT traditionnels. Pour pré-2009 (historique), c'est la seule disponible. Pour 2009+, préférer Managed Money (Disaggregated) qui est plus précis.
*Catégorie : indicateurs_tendance*

### D9633 — Catégorie Commercial (cols 12–13 et déclinaisons)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Commercial Positions-Long (All)` et `Commercial Positions-Short (All)` — les Commercials regroupent producteurs, marchands ET swap dealers (tout ce qui est couverture). Dans Legacy, pas de séparation entre hedgers "physiques" et intermédiaires financiers.
**TRADEX-AI C3** : Limite clé du rapport Legacy : la catégorie Commercial fusionne des acteurs très différents (mineur d'or + banque swap dealer). C'est pourquoi le Disaggregated est préférable pour l'analyse précise. Le net Commercial Legacy ne permet pas de distinguer couverture physique de couverture financière.
*Catégorie : structure_marche*

### D9634 — Total Reportable et Non-Reportable Legacy (cols 14–17)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Total Reportable Positions-Long (All)` + `Total Reportable Positions-Short (All)` = somme Commercial + Non-commercial. `Nonreportable Positions-Long (All)` + `Nonreportable Positions-Short (All)` = petits traders sous le seuil de déclaration.
**TRADEX-AI C3** : Identique au Disaggregated — les Non-Reportable représentent le "retail". Positionnement extrême Net Non-Reportable = signal contrarian (sentiment foule). Valide pour les données Legacy historiques GC/CL/ZW remontant aux années 1990-2000.
*Catégorie : psychologie*

### D9635 — Triplet All/Old/Other dans Legacy (cols 8–37)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Même structure 3 sous-ensembles que Disaggregated : `Open Interest (All/Old/Other)`, positions `(All)` cols 8–17, `(Old)` cols 18–27, `(Other)` cols 28–37. "Old" = contrats proches échéance, "Other" = contrats plus lointains.
**TRADEX-AI C3** : Même règle opérationnelle que Disaggregated : utiliser `(All)` par défaut. L'analyse Old/Other pour le roll spread uniquement (CL, GC en période de roll actif).
*Catégorie : timing*

### D9636 — Variations hebdomadaires Legacy (cols 38–47)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Change in Open Interest (All)`, `Change in Noncommercial-Long (All)`, `Change in Noncommercial-Short (All)`, `Change in Noncommercial-Spreading (All)`, `Change in Commercial-Long (All)`, `Change in Commercial-Short (All)`, `Change in Total Reportable-Long (All)`, `Change in Total Reportable-Short (All)`, `Change in Nonreportable-Long (All)`, `Change in Nonreportable-Short (All)`.
**TRADEX-AI C3** : Flux net Non-commercial hebdomadaire = `Change in Noncommercial-Long` − `Change in Noncommercial-Short`. Deux semaines consécutives de flux net positif croissant = momentum institutionnel confirmé en Legacy. Utilisé pour l'historique pré-2009.
*Catégorie : indicateurs_momentum*

### D9637 — Pourcentages d'OI Legacy (cols 48–77)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Série `% OF OI-*` couvrant All/Old/Other pour chaque catégorie. Ex. `% OF OI-Noncommercial-Long (All)`, `% OF OI-Commercial-Short (All)`, `% OF OI-Nonreportable-Long (All)`.
**TRADEX-AI C3** : Même logique que Disaggregated — utiliser les % OI pour comparer entre actifs de taille différente. Pour une analyse historique longue durée GC (remonte aux années 1980), les % OI Legacy sont les seuls disponibles. Utile pour calibrer les seuils "extrêmes" d'un point de vue historique.
*Catégorie : indicateurs_tendance*

### D9638 — Nombre de traders Legacy (cols 78–101)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Série `Traders-*` : `Traders-Total (All)`, `Traders-Noncommercial-Long/Short/Spreading (All)`, `Traders-Commercial-Long/Short (All)`, `Traders-Total Reportable-Long/Short (All)`. Même structure All/Old/Other.
**TRADEX-AI C3** : Un faible nombre de Non-commercials long avec position très élevée = concentration spéculative → risque retournement. Indicateur de "crowded trade" à surveiller sur GC en particulier lors des rallyes prolongés.
*Catégorie : gestion_risque_entree*

### D9639 — Ratios de concentration Legacy (cols 102–125)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Même structure que Disaggregated : `Concentration-Gross LT = 4 TDR-Long/Short (All)`, `Concentration-Gross LT ="8" TDR-Long/Short (All)`, `Concentration-Net LT ="4" TDR-Long/Short (All)`, `Concentration-Net LT ="8" TDR-Long/Short (All)` + variantes Old/Other (cols 110–125).
**TRADEX-AI C3** : Concentration-Net Top 4 long > 40% sur GC = marché très concentré côté spéculatif. Ce seuil (40% net, vs 60% gross) est plus conservateur et plus fiable pour détecter une concentration dangereuse. Définir ces seuils dans `settings.py` comme constantes CFTC_CONC_ALERT.
*Catégorie : gestion_risque_entree*

### D9640 — Champ Contract Units Legacy (col. 126)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Contract Units` — même fonction que dans Disaggregated, indique l'unité du contrat. Présent dans les deux formats.
**TRADEX-AI C3** : Identique à D9629 Disaggregated. Confirme la cohérence entre les deux formats. Parser unifié possible avec normalisation des noms de colonnes.
*Catégorie : volume_liquidite*

### D9641 — Champs code marché en citations (cols 127–129)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `CFTC Contract Market Code (Quotes)`, `CFTC Market Code in Initials (Quotes)`, `CFTC Commodity Code (Quotes)` — versions entre guillemets des champs d'identification, utiles pour le matching string dans les parsers CSV.
**TRADEX-AI C3** : Ces variantes "Quotes" permettent un filtre robuste par string même si les codes numériques posent problème (ex. parsing de "GOLD" plutôt que "088691"). Le parser peut utiliser `CFTC Commodity Code (Quotes)` comme fallback de sécurité.
*Catégorie : structure_marche*

### D9642 — Différence structurelle clé Legacy vs Disaggregated
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Le rapport Legacy contient 130 colonnes vs 191 pour le Disaggregated. La différence principale : Legacy n'a pas de séparation Swap Dealers / Prod-Merc dans les Commercials, et pas de distinction Managed Money / Other Reportable dans les Non-commercials. Résultat : 61 colonnes de moins, analyse moins précise.
**TRADEX-AI C3** : Décision architecturale : le pipeline TRADEX-AI doit maintenir deux parsers distincts (`parse_cot_legacy()` et `parse_cot_disagg()`) ou un parser unifié avec mapping conditionnel basé sur `FutOnly_or_Combined` et le nombre de colonnes détecté.
*Catégorie : structure_marche*

### D9643 — Couverture temporelle du rapport Legacy
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Le rapport COT Legacy existe depuis 1986 pour certains actifs (GC, CL) et depuis les années 1960–1970 pour les grains (ZW). Le rapport Disaggregated ne commence qu'en septembre 2009. Pour toute analyse historique longue (10+ ans), seul le Legacy permet de remonter aux cycles précédents.
**TRADEX-AI C3** : Valeur stratégique du Legacy : calibration des seuils extrêmes (ex. maximum historique net Non-commercial GC). Ces extremes servent de bornes pour le z-score calculé dans `correlations.py`. Un backfill Legacy + Disaggregated donne une série continue optimale.
*Catégorie : timing*

### D9644 — Règle d'interprétation : Commercials comme smart money en Legacy
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Dans la théorie COT traditionnelle (Briese, Williams), les Commercials Legacy sont considérés comme le "smart money" car ce sont des acteurs industriels qui connaissent leur marché physique. Position nette Commercial record-high long = signal haussier fort selon cette théorie.
**TRADEX-AI C3** : Cette règle est une synthèse issue de la littérature COT, applicable aux données Legacy uniquement. Sur le Disaggregated, le "smart money industriel" est isolé dans Prod/Merc — plus pur analytiquement. Intégrer les deux logiques dans la KB : Commercial Legacy net long = signal C3 de base · Prod/Merc Disagg net long = signal C3 premium.
*Catégorie : indicateurs_tendance*

### D9645 — Formule net Non-commercial Legacy normalisée
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Formule standard = (`Noncommercial Positions-Long (All)` − `Noncommercial Positions-Short (All)`) / `Open Interest (All)` × 100 = % net Non-commercial. Ce ratio normalise la position nette par rapport à la taille du marché.
**TRADEX-AI C3** : Implémenter `cot_pct_net_noncomm = (nc_long - nc_short) / oi_all * 100`. Seuils orientatifs basés sur historique : < −15% = extrême short (potentiel retournement haussier) ; > +25% = extrême long (potentiel retournement baissier) pour GC. Ces seuils doivent être calibrés par actif dans `settings.py`.
*Catégorie : indicateurs_tendance*

### D9646 — Spreading Non-commercial : rôle dans le calcul net
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : `Noncommercial Positions-Spreading (All)` — positions simultanément long ET short sur des échéances différentes (calendar spread). Ces positions sont neutres directionnellement.
**TRADEX-AI C3** : Les Spreading ne doivent PAS entrer dans le calcul de la position nette directionnelle. Formule correcte : Net = Long − Short (exclure Spreading). Une hausse du Spreading sans hausse directionnelle = transition de marché tendanciel vers range — signal d'attente pour TRADEX-AI.
*Catégorie : indicateurs_tendance*

### D9647 — Comparaison Non-Reportable Legacy vs Non-Reportable Disaggregated
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Les Non-Reportable (`Nonreportable Positions-Long/Short`) sont identiques conceptuellement dans Legacy et Disaggregated : petits traders sous le seuil CFTC de déclaration (ex. < 200 contrats pour GC). La valeur absolue est la même dans les deux rapports.
**TRADEX-AI C3** : Pour le signal contrarian "retail sentiment", les deux rapports donnent le même résultat. Pas de doublon — une seule lecture suffira dans le pipeline (utiliser Disaggregated qui est déjà chargé).
*Catégorie : psychologie*

### D9648 — Champ col. 130 (fin de liste Legacy)
🟢 **FAIT VÉRIFIÉ** (Source : cot_variables_legacy.md) : Le bundle Legacy se termine à la colonne 130 sans label explicite (champ vide ou non documenté dans le source HTML). Le fichier CSV peut contenir une 130e colonne selon les versions.
**TRADEX-AI C3** : Le parser doit gérer cette colonne vide/non documentée sans erreur. Utiliser `error_bad_lines=False` ou `on_bad_lines='skip'` dans `pandas.read_csv()` pour éviter les plantages si cette colonne est présente ou absente selon les années.
*Catégorie : structure_marche*

### D9649 — Rapport Legacy comme baseline de validation croisée
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Les totaux Legacy (Total Reportable + Non-Reportable = Open Interest) constituent une contrainte comptable vérifiable. Si `Tot_Rept_Long + NonRept_Long ≠ Open_Interest`, les données sont corrompues.
**TRADEX-AI C3** : Implémenter dans `data_reader.py` une validation d'intégrité : `assert abs((tot_rept_long + nonrept_long) - oi_all) < 1` après chaque chargement du fichier COT. Si la contrainte échoue → alerter + bloquer le signal C3 ce jour-là (staleness_monitor pattern).
*Catégorie : gestion_risque_entree*

### D9650 — Recommandation d'usage Legacy pour TRADEX-AI
🟡 **SYNTHÈSE** (Source : cot_variables_legacy.md) : Synthèse d'usage pour le pipeline : (1) Priorité = Disaggregated pour données 2009+. (2) Legacy = complément historique pour calibration seuils et backtesting long terme. (3) Ne jamais mixer Legacy et Disaggregated dans un même calcul de z-score sans normalisation préalable (biais structurel lié à l'agrégation des catégories).
**TRADEX-AI C3** : Documenter cette règle dans `settings.py` via un commentaire `# COT_DATA_POLICY` et dans `KB_INDEX.md` comme contrainte d'ingestion. Le cerveau Claude doit savoir quel format il analyse quand il interprète les données C3.
*Catégorie : structure_marche*
