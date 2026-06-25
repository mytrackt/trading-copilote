# Extraction CFTC — TFF Explanatory Notes (Traders in Financial Futures)
**Source :** `bundles/cftc/cot_tff_notes.md` (PDF 4 pages, CERTIFIÉ pdfplumber) + 0 images certifiées
**Méthode images :** pdfplumber texte · images=MANUEL (stratégie §3.3) · 0/0 certifiées · 0 à vérifier
**Décisions :** D9571 → D9590 · **Page :** https://www.cftc.gov/sites/default/files/idc/groups/public/@commitmentsoftraders/documents/file/tfmexplanatorynotes.pdf
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Notes officielles CFTC définissant les 4 catégories TFF — Cercle C3 Institutionnels, applicable aux actifs CONFIRMATION (DX, ES) et aux corrélations inter-marché TRADEX-AI.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune — images détectées manuellement) | — | — | — |

## DÉCISIONS

### D9571 — Le rapport TFF créé en 2010 décompose les marchés financiers en 4 catégories distinctes
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Le rapport TFF (Traders in Financial Futures), annoncé le 22 juillet 2010, introduit 4 catégories de traders pour les marchés financiers à terme : Dealer/Intermediary, Asset Manager/Institutional, Leveraged Funds, Other Reportables. Il remplace la dichotomie binaire Commercial/Non-Commercial du Legacy COT pour ces marchés.
**TRADEX-AI C3** : Le TFF est le rapport COT pertinent pour DX (Dollar Index) et ES (S&P 500) — actifs CONFIRMATION TRADEX. Lire le TFF (et non le Legacy COT) pour ces marchés financiers afin d'identifier la catégorie institutionnelle dominante.
*Catégorie : structure_marche*

### D9572 — Dealer/Intermediary = côté vendeur (sell-side) : grandes banques et dealers OTC
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : La catégorie Dealer/Intermediary représente le « sell-side » des marchés financiers. Elle comprend les grandes banques (US et non-US), les dealers en valeurs mobilières, en swaps et autres dérivés. Ces acteurs gèrent des livres matchés (matched books) et couvrent leurs risques sur plusieurs marchés et clients.
**TRADEX-AI C3** : Positions Dealer/Intermediary sur ES et DX = proxy du positionnement des grandes banques mondiales. Un biais net short Dealer sur ES peut signaler une couverture de risque institutionnelle (haussière pour le marché sous-jacent par effet miroir). Signal macro C4 potentiel.
*Catégorie : macro_evenements*

### D9573 — Asset Manager/Institutional = fonds de pension, assurances, mutual funds
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : La catégorie Asset Manager/Institutional regroupe les investisseurs institutionnels : fonds de pension, dotations (endowments), compagnies d'assurance, mutual funds, et gestionnaires de portefeuille dont la clientèle est majoritairement institutionnelle.
**TRADEX-AI C3** : Les Asset Managers sont les acheteurs structurels long terme. Un positionnement net long croissant des Asset Managers sur ES = signal de biais haussier structurel pour les marchés actions — contexte favorable ou défavorable pour GC selon corrélation or/actions (Cercle C7).
*Catégorie : correlations*

### D9574 — Leveraged Funds = hedge funds, CTAs, CPOs — spéculateurs directionnels
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : La catégorie Leveraged Funds comprend les hedge funds, les Commodity Trading Advisors (CTAs) enregistrés, les Commodity Pool Operators (CPOs) enregistrés, et les fonds non enregistrés identifiés par la CFTC. Leurs stratégies incluent positions directionnelles et arbitrages intra- et inter-marchés.
**TRADEX-AI C3** : Les Leveraged Funds sont les spéculateurs les plus réactifs aux signaux techniques. Leur positionnement net sur DX et ES est un indicateur de sentiment spéculatif de court terme — pertinent pour confirmer ou infirmer un signal TRADEX au niveau du Cercle C5 Sentiment.
*Catégorie : psychologie*

### D9575 — Other Reportables = trésoreries d'entreprises, banques centrales, banques régionales
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : La catégorie Other Reportables regroupe les traders reportables non classifiables dans les trois premières catégories. Elle inclut les trésoreries d'entreprises, les banques centrales, les petites banques, les initiateurs de prêts hypothécaires, les credit unions — principalement des hedgers de risque de change, actions ou taux.
**TRADEX-AI C3** : La présence de banques centrales dans Other Reportables sur DX est significative — un positionnement net important dans cette catégorie peut refléter des interventions de politique monétaire ou de gestion de réserves. Signal macro C4 à surveiller conjointement avec les décisions Fed/FOMC.
*Catégorie : macro_evenements*

### D9576 — Le TFF n'est pas une désagrégation du COT Legacy : un trader TFF peut être Commercial ou Non-Commercial
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Contrairement au rapport Disaggregated (qui décompose les catégories Legacy), le TFF n'est PAS une désagrégation du COT Legacy pour les marchés financiers. Un trader classé dans une des 4 catégories TFF peut provenir indifféremment de la catégorie « commercial » ou « non-commercial » du Legacy COT.
**TRADEX-AI C3** : Ne pas additionner les totaux TFF et Legacy COT pour un même marché — double comptage. Pour DX et ES, utiliser exclusivement le TFF. Pour GC/HG/CL/ZW, utiliser le Disaggregated COT (marchés physiques, non couverts par le TFF).
*Catégorie : gestion_risque_entree*

### D9577 — Seuil de publication TFF : au moins 20 traders au-dessus des niveaux de reporting CFTC
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Le rapport TFF, comme le COT, est publié pour les marchés où 20 traders ou plus détiennent des positions égales ou supérieures aux niveaux de reporting établis par la CFTC. La publication couvre les formats futures-only et futures-and-options-combined.
**TRADEX-AI C3** : Critère de liquidité institutionnelle — les marchés TRADEX (GC/HG/CL/ZW/DX/ES) dépassent tous largement le seuil de 20 traders reportables, garantissant la disponibilité des données COT/TFF chaque semaine.
*Catégorie : volume_liquidite*

### D9578 — Le « spreading » TFF = positions long et short offsetting dans des mois calendaires différents
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Le TFF calcule le « spreading » comme le montant de positions long et short offsetting dans des mois calendaires différents (ou futures + options dans le même ou différents mois calendaires). Le résidu net est reporté en colonne long ou short. Les spreads inter-marchés ne sont pas pris en compte.
**TRADEX-AI C3** : Une hausse du spreading dans la catégorie Leveraged Funds sur DX ou ES signale une activité accrue de spread trading (roll, arbitrage calendaire) — indicateur d'incertitude directionnelle chez les spéculateurs, contexte de marché potentiellement en transition.
*Catégorie : indicateurs_momentum*

### D9579 — Comptage des traders TFF : la somme par catégorie dépasse le total reportable (double comptage partiel)
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : La somme des comptages de traders par catégorie (long + short + spreading) dépasse habituellement le nombre total de traders reportables, car un même trader actif en spreading peut également apparaître dans les colonnes long ou short outright.
**TRADEX-AI C3** : Ne pas interpréter le nombre total de traders TFF comme une somme arithmétique des catégories — risque de surestimation de la concentration. Utiliser la taille des positions (open interest) plutôt que le comptage de traders pour évaluer le poids institutionnel.
*Catégorie : gestion_risque_entree*

### D9580 — Confidentialité : trader count masqué (point « · ») si moins de 4 traders actifs dans une catégorie
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Pour tout marché où une catégorie TFF spécifique compte moins de 4 traders actifs, le comptage de traders n'est pas publié (remplacé par « · ») afin de préserver la confidentialité. La taille des positions reste publiée.
**TRADEX-AI C3** : Sur des actifs moins liquides (HG cuivre, ZW blé), certaines catégories TFF peuvent afficher « · » pour le nombre de traders — ne pas interpréter l'absence de comptage comme une absence de positionnement. Utiliser la taille de position (champ séparé) comme indicateur.
*Catégorie : volume_liquidite*

### D9581 — Historique TFF rétroactif disponible depuis juin 2006 avec limitations de backcasting
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : L'historique TFF est disponible depuis le 13 juin 2006. La CFTC précise que la classification rétroactive (backcasting) utilise les classifications actuelles des traders pour reclasser leurs positions historiques — cette approche diminue la précision à mesure que l'on remonte dans le temps, car les classifications évoluent.
**TRADEX-AI C3** : Historique TFF utilisable pour DX/ES depuis 2006 — mais avec précaution croissante avant 2010 (date de création officielle du rapport). Pour backtests TRADEX, privilégier la période post-2010 pour les données TFF, post-2009 pour les données Disaggregated.
*Catégorie : gestion_risque_entree*

### D9582 — Classification des traders par activité prédominante : jugement de la DMO CFTC
🟡 **SYNTHÈSE** (Source : cot_tff_notes.md) : La CFTC Division of Market Oversight (DMO) classe chaque trader dans la catégorie TFF correspondant à son activité prédominante, en s'appuyant sur le formulaire Form 40 (déclaration obligatoire des grands traders) et d'autres informations disponibles. La DMO classe les traders, pas leurs activités spécifiques.
**TRADEX-AI C3** : La classification TFF repose sur un jugement humain CFTC, pas sur des critères algorithmiques stricts — une même entité peut être reclassée au fil du temps. Conséquence pour TRADEX : ne pas utiliser les données TFF comme signal mécanique absolu, mais comme indicateur de biais institutionnel à pondérer avec d'autres signaux.
*Catégorie : psychologie*

### D9583 — Organisations multi-fonctionnelles : trading centralisé = une seule classification, entités séparées = classifications distinctes
🟢 **FAIT VÉRIFIÉ** (Source : cot_tff_notes.md) : Quand une organisation multi-services centralise son trading futures, son Form 40 peut refléter plusieurs catégories d'activité, mais la CFTC attribue une seule classification prédominante. Si l'organisation crée des entités de trading distinctes, chaque entité est analysée séparément et peut recevoir une classification différente.
**TRADEX-AI C3** : Implication pratique : un grand groupe bancaire peut avoir des filiales classées simultanément en Dealer et en Asset Manager — la consolidation des positions au niveau groupe n'est pas visible dans le TFF. Garder ce biais en tête lors de l'interprétation des ratios institutionnels.
*Catégorie : structure_marche*

### D9584 — Comparaison des rapports : Legacy (2 catégories) → Disaggregated (4 catégories physiques) → TFF (4 catégories financières)
🟡 **SYNTHÈSE** (Source : cot_tff_notes.md) : Hiérarchie des rapports COT — (1) Legacy COT : Commercial vs Non-Commercial (2 catégories) — (2) Disaggregated COT pour marchés physiques : Producer/PMPU + SwapDealer vs ManagedMoney + OtherReportables (4 catégories) — (3) TFF pour marchés financiers : Dealer + AssetManager + LeveragedFunds + OtherReportables (4 catégories). Le Disaggregated est re-agrégeable vers Legacy ; le TFF ne l'est pas.
**TRADEX-AI C3** : Matrice de sélection rapport TRADEX — GC/HG/CL/ZW → utiliser Disaggregated COT (marchés physiques) · DX/ES → utiliser TFF (marchés financiers) · VX → vérifier disponibilité COT spécifique. Ne jamais mélanger Legacy et Disaggregated pour un même calcul.
*Catégorie : structure_marche*

### D9585 — Mise à jour du Form 40 CFTC en cours : évolution probable des catégories TFF
⏳ **VOLATILE** (Source : cot_tff_notes.md) : La CFTC indique (dans les notes originales) travailler à une mise à niveau du formulaire Form 40 d'identification des grands traders. Cette amélioration pourrait nécessiter une modification du rapport TFF et d'autres rapports COT pour exploiter les nouvelles informations.
**TRADEX-AI C3** : Signal de vigilance — les catégories TFF peuvent évoluer si la CFTC modifie sa taxonomie. Surveiller les annonces CFTC sur les changements de classification avant chaque mise à jour majeure du module C3 de TRADEX.
*Catégorie : macro_evenements*
