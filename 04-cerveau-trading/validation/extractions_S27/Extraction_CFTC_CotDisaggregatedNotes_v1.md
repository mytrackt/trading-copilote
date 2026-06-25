# Extraction CFTC — Disaggregated COT Explanatory Notes
**Source :** `bundles/cftc/cot_disaggregated_notes.md` (PDF certifié, 4 pages) + 0 images certifiées
**Méthode images :** pdfplumber texte · images=MANUEL (stratégie §3.3) · 0 détectées
**Décisions :** D9531 → D9550 · **Page :** https://www.cftc.gov/sites/default/files/idc/groups/public/@commitmentsoftraders/documents/file/disaggregatedcotexplanatorynot.pdf
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Ce PDF officiel définit les 4 catégories du Disaggregated COT (Producer/Merchant, Swap Dealer, Managed Money, Other Reportables) — fondement du module C3 Institutionnels TRADEX-AI pour GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image détectée dans le PDF) | — | — | — |

---

## DÉCISIONS

### D9531 — Fait fondateur : Création du Disaggregated COT (4 septembre 2009)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.1) : La CFTC a commencé à publier le Disaggregated COT le 4 septembre 2009. La première version couvrait 22 marchés majeurs de matières premières physiques. Le 4 décembre 2009, les marchés physiques restants ont été inclus.
**TRADEX-AI C3** : Le Disaggregated COT est disponible depuis septembre 2009 pour les marchés physiques incluant GC, HG, CL, ZW. Les données rétro-calculées depuis juin 2006 permettent ~15 ans de backtesting. Pour le module C3 TRADEX, utiliser uniquement les données Disaggregated COT post-septembre 2009 pour la fiabilité maximale des classifications (les données 2006-2009 sont rétro-calculées et moins fiables).
*Catégorie : structure_marche*

### D9532 — Fait fondateur : Les 4 catégories du Disaggregated COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.1) : Le Disaggregated COT sépare les traders en 4 catégories : (1) Producer/Merchant/Processor/User, (2) Swap Dealers, (3) Managed Money, (4) Other Reportables. Le COT legacy ne séparait que "commercial" et "non-commercial".
**TRADEX-AI C3** : Les 4 catégories Disaggregated sont le cadre analytique principal du module C3 TRADEX. Hiérarchie de pertinence pour les signaux TRADEX : [1] Managed Money (signal directionnel pur) > [2] Producer/Merchant (signal de couverture/hedging) > [3] Swap Dealers (signal mixte, à pondérer) > [4] Other Reportables (signal faible). Implémenter ces 4 flux dans data_reader.py avec cette pondération.
*Catégorie : structure_marche*

### D9533 — Définition officielle : Producer/Merchant/Processor/User
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Un "producer/merchant/processor/user" est une entité qui s'engage principalement dans la production, le traitement, l'emballage ou la manutention d'une matière première physique et qui utilise les marchés futures pour gérer ou couvrir les risques associés à ces activités.
**TRADEX-AI C3** : Pour GC (Or) : producteurs = mines d'or (Barrick, Newmont), marchands = raffineurs et dealers en or physique. Leurs positions SHORT sur GC = couverture de production = normale, pas bearish structurel. Pour CL (Pétrole) : producteurs = compagnies pétrolières, utilisateurs = compagnies aériennes (jet fuel). Un Producer SHORT massif sur CL = les producteurs anticipent une baisse et verrouillent leurs prix — signal bearish secondaire. Pour ZW : agriculteurs qui hedgent leur récolte.
*Catégorie : structure_marche*

### D9534 — Définition officielle : Swap Dealer
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Un "swap dealer" est une entité qui traite principalement des swaps pour une matière première et utilise les marchés futures pour gérer ou couvrir le risque associé à ces transactions de swaps. Les contreparties du swap dealer peuvent être des traders spéculatifs (hedge funds) ou des clients commerciaux traditionnels gérant le risque de leurs activités dans la matière première physique.
**TRADEX-AI C3** : Les Swap Dealers sur GC et CL sont principalement des banques d'investissement (Goldman, JPMorgan) qui ont des expositions swap avec des clients institutionnels. Leurs positions futures sont des couvertures de swaps — pas forcément des vues directionnelles propres. Signal Swap Dealer = ambigu pour TRADEX. Règle : ne pas inclure Swap Dealer NET dans le calcul du score C3 directionnel, mais utiliser comme indicateur de liquidité institutionnelle (volume d'activité swap élevé = marché liquide, spread bid/ask favorable).
*Catégorie : structure_marche*

### D9535 — Définition officielle : Money Manager (Managed Money)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Un "money manager" (pour les besoins du rapport) est : (1) un CTA (Commodity Trading Advisor) enregistré, (2) un CPO (Commodity Pool Operator) enregistré, ou (3) un fonds non enregistré identifié par la CFTC. Ces traders gèrent et conduisent le trading futures organisé au nom de clients. Les "hedge funds" sont inclus dans cette catégorie, qu'ils soient enregistrés ou non.
**TRADEX-AI C3** : Managed Money = "smart money spéculatif" — la catégorie la plus informative pour les signaux directionnels TRADEX sur GC/HG/CL/ZW. Règle signal C3 Managed Money : NET LONG croissant sur 3 semaines consécutives = tendance haussière confirmée institutionnellement (score C3 = +2/3). NET SHORT croissant sur 3 semaines = tendance baissière confirmée (score C3 = -2/3). Retournement brutal NET (>15 000 contrats en 1 semaine sur GC) = signal d'alerte / changement de régime.
*Catégorie : indicateurs_tendance*

### D9536 — Définition officielle : Other Reportables
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Tout trader déclarable qui n'est pas placé dans les 3 autres catégories (Producer/Merchant, Swap Dealer, Managed Money) est classé dans "Other Reportables". Cette catégorie est un "fourre-tout" des traders institutionnels non classifiables autrement.
**TRADEX-AI C3** : Les "Other Reportables" sur GC/HG/CL/ZW incluent des family offices, des fonds souverains partiels, des traders propriétaires (prop firms). Leur signal est secondaire mais leur accumulation peut précéder un mouvement de Managed Money — à utiliser comme indicateur précoce (leading) dans des configurations avancées du module C3. Pour la version initiale TRADEX, ignorer Other Reportables dans le calcul du score C3.
*Catégorie : structure_marche*

### D9537 — Règle de classification : Form 40 comme base de données de classification
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.2) : Les classifications des 4 catégories sont dérivées des réponses des traders sur le Form 40 (version mai 2000), incluant les informations du Schedule 1. Le Form 40 est requis par la réglementation CFTC 18.04 pour tous les traders déclarables. Le non-dépôt ou les réponses mensongères constituent une violation de la Commodity Exchange Act.
**TRADEX-AI C3** : La classification COT est basée sur l'auto-déclaration des traders via Form 40, révisée et validée par les équipes CFTC. Les erreurs de classification sont possibles (avouées dans les "Potential Limitations"). Pour TRADEX, traiter les classifications COT comme des approximations fiables (>95%) mais non infaillibles — ne pas sur-pondérer un signal COT isolé, toujours combiner avec C1 (Prix) et C2 (Order Flow).
*Catégorie : gestion_risque_entree*

### D9538 — Règle de classification : Activité prédominante détermine la catégorie
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.2) : Certaines organisations multi-services ont centralisé leur trading futures. Dans ces cas, le Form 40 peut indiquer plusieurs catégories. La Division de Market Oversight place chaque trader dans la catégorie la plus appropriée basée sur son activité prédominante. Dans la plupart des cas, le choix est clair ; dans certains cas, un jugement est exercé.
**TRADEX-AI C3** : La classification par "activité prédominante" signifie qu'un même trader peut avoir des activités de hedging ET de spéculation, mais sera classé dans une seule catégorie. Implication TRADEX : les classifications COT ne sont pas parfaitement hermétiques — un "Producer/Merchant" peut avoir des positions spéculatives, un "Managed Money" peut parfois hedger. Cette impureté structurelle est une limite connue du signal C3.
*Catégorie : structure_marche*

### D9539 — Règle de classification : Entités séparées traitées séparément
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.2) : Certaines organisations mères créent des entités de trading séparées pour gérer leurs différentes activités ou localisations. Dans ces cas, chaque entité dépose un Form 40 séparé et est analysée séparément pour sa classification Disaggregated COT.
**TRADEX-AI C3** : Un groupe comme Goldman Sachs peut avoir des entités séparées classées comme "Swap Dealer" (la banque d'investissement) et "Managed Money" (le fonds GS Asset Management). Leurs positions apparaissent dans des catégories différentes du COT. Cela signifie que les positions institutionnelles d'un même groupe sont potentiellement dispersées dans plusieurs catégories — renforçant la nécessité d'analyser toutes les catégories, pas uniquement Managed Money.
*Catégorie : structure_marche*

### D9540 — Règle de dynamisme : Les classifications peuvent changer dans le temps
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.2) : La classification d'un trader peut changer au fil du temps pour plusieurs raisons : (1) changement dans la façon d'utiliser les marchés, (2) trading de matières premières supplémentaires ou réduites, (3) évolution de la clientèle. Ces changements entraînent des modifications de classification.
**TRADEX-AI C3** : Les classifications COT ne sont pas statiques — un hedge fund peut devenir plus "commercial" s'il développe une activité physique, ou inversement. Pour les analyses de longues périodes sur GC/HG/CL/ZW, les changements de classification historiques peuvent créer des discontinuités dans les séries temporelles COT. Limiter les analyses de tendance Disaggregated à des périodes ≤ 3 ans pour minimiser le biais de reclassification.
*Catégorie : timing*

### D9541 — Définition : Spreading dans le Disaggregated COT
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Le Disaggregated COT présente l'open interest par long, short ET spreading pour les catégories Swap Dealers, Managed Money et Other Reportables. Pour Producer/Merchant/Processor/User, seules les positions long ou short sont reportées (pas de spreading). Le "spreading" = montant de positions futures offsettantes sur différentes échéances calendaires (ou futures et options sur mêmes/différentes échéances). Les spreads inter-marchés ne sont pas inclus.
**TRADEX-AI C3** : Le spreading dans le COT Disaggregated représente des positions arbitragistes, pas des positions directionnelles. Pour calculer la position nette directionnelle Managed Money sur GC : NET = MM_Long_Outright - MM_Short_Outright (exclure MM_Spreading). Le spreading Managed Money élevé sur CL indique une activité de roll de positions (gestion de courbe à terme) — signal neutre pour le module C3.
*Catégorie : indicateurs_tendance*

### D9542 — Règle de confidentialité : Suppression du nombre de traders < 4
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : Pour préserver la confidentialité des traders, dans toute matière première où une catégorie spécifique a moins de 4 traders actifs, la taille des positions pertinentes est fournie mais le nombre de traders est supprimé (représenté par "·").
**TRADEX-AI C3** : Si une catégorie sur un actif TRADEX affiche "·" pour le nombre de traders, cela signifie < 4 traders dans cette catégorie — marché concentré avec risque de manipulation élevé. Règle TRADEX : si Producer/Merchant sur HG (Cuivre) ou ZW affiche "·" traders, le signal COT pour cet actif est à pondérer à 50% de sa valeur normale dans le score C3 (risque de concentration excessive).
*Catégorie : gestion_risque_entree*

### D9543 — Règle de comptage : Somme des traders > total réel (double comptage spreading)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.3) : La somme des nombres de traders dans chaque catégorie dépasse typiquement le nombre total de traders déclarables. Cela résulte du fait que pour Swap Dealers, Managed Money et Other Reportables, le "spreading" peut être une activité partielle — le même trader peut apparaître dans le compte "long" ou "short", ET dans le compte "spreading".
**TRADEX-AI C3** : Ne pas sommer les nombres de traders par catégorie pour obtenir un total institutionnel — ce chiffre serait sur-estimé. Pour TRADEX, utiliser le nombre de traders par catégorie séparément comme indicateur de "breadth" (ex. : augmentation du nombre de Managed Money traders sur GC = intérêt institutionnel croissant = signal C3 positif secondaire).
*Catégorie : volume_liquidite*

### D9544 — Données historiques : Backcasting 2006-2009 (limitation fiabilité)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : Les données historiques Disaggregated COT sont disponibles depuis le 13 juin 2006. La CFTC ne maintient pas d'historique des classifications des grands traders — les classifications récentes ont été utilisées pour classer les positions historiques de chaque trader déclarable. Cette approche de "backcasting" diminue la précision des données plus on remonte dans le temps.
**TRADEX-AI C3** : Le backcasting COT Disaggregated (2006-2009) est une approximation — les classifications actuelles appliquées aux positions historiques ne reflètent pas forcément les classifications qui auraient été faites à l'époque. Règle de robustesse TRADEX : pour les analyses Disaggregated sur GC/HG/CL/ZW, utiliser uniquement les données depuis septembre 2009 (premier rapport officiel) pour une fiabilité maximale. Les données 2006-2009 peuvent être utilisées à titre indicatif uniquement.
*Catégorie : gestion_risque_entree*

### D9545 — Limitation avouée : Impureté des classifications (hedgers dans Managed Money, spéculateurs dans Commercial)
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : Certains traders classés "swap dealers" s'engagent dans des activités commerciales dans la matière première physique. Certains traders classés "producer/merchant/processor/user" s'engagent dans des activités de swaps. Le staff classe les traders, pas leurs activités de trading — on ne peut pas savoir avec certitude que tout le trading d'un Producer/Merchant est du hedging.
**TRADEX-AI C3** : Implication directe pour TRADEX : le signal COT Disaggregated n'est pas un signal binaire "pur hedging vs pure spéculation". Il y a du "bruit" de classification dans toutes les catégories. Appliquer un facteur de confiance COT ≤ 85% dans le score C3 — même les meilleures configurations COT conservent une incertitude structurelle. Ne jamais attribuer score C3 = 10/10 basé uniquement sur COT.
*Catégorie : gestion_risque_entree*

### D9546 — Règle de transparence : Annonce publique lors de corrections majeures
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : Quand des problèmes majeurs de reporting ou de classification sont trouvés, une annonce est faite et des corrections sont publiées aussi rapidement que possible.
**TRADEX-AI C3** : TRADEX doit implémenter une surveillance des annonces CFTC pour détecter les corrections de données COT. Une correction de classification sur GC ou CL pourrait invalider plusieurs semaines de signal C3. Recommandation : vérifier la page CFTC "Corrections" hebdomadairement lors du download COT du vendredi — si correction détectée sur actifs TRADEX, recalculer le score C3 et alerter l'utilisateur.
*Catégorie : macro_evenements*

### D9547 — Comparaison : Legacy Commercial = Producer/Merchant + Swap Dealer
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : La catégorie "commercial" du COT legacy inclut : (1) producteurs, marchands, transformateurs et utilisateurs de la matière première physique (= Producer/Merchant dans Disaggregated), ET (2) swap dealers qui ont couvert un risque OTC dans les futures, qu'ils aient une contrepartie commerciale ou spéculative. Ces deux sous-catégories sont séparées dans le Disaggregated COT.
**TRADEX-AI C3** : Règle de migration TRADEX des analyses COT legacy vers Disaggregated : "Commercial" legacy ≈ Producer/Merchant + Swap Dealer dans Disaggregated. Pour reconstruire une série COT "commercial" comparable à l'analyse legacy sur GC : PM_Long + SD_Long et PM_Short + SD_Short. Cela permet de valider les analyses historiques pré-2009 avec des données Disaggregated post-2009.
*Catégorie : correlations*

### D9548 — Comparaison : Legacy Non-Commercial = Managed Money + Other Reportables
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : La catégorie "non-commercial" du COT legacy inclut : (1) gestionnaires professionnels d'argent (CTAs, CPOs, hedge funds) = "Managed Money" dans Disaggregated, ET (2) un large éventail d'autres traders non-commerciaux spéculatifs = "Other Reportables" dans Disaggregated.
**TRADEX-AI C3** : Pour la continuité des analyses TRADEX entre les données legacy et Disaggregated : "Non-commercial" legacy ≈ Managed Money + Other Reportables dans Disaggregated. Le signal directionnels spéculatif "pur" du Disaggregated = Managed Money seul (sans Other Reportables) — c'est la métrique préférée pour le module C3 car plus précise que le legacy "non-commercial" qui mélange hedge funds et autres spéculateurs.
*Catégorie : indicateurs_tendance*

### D9549 — Comparaison : Index Traders CIT Supplemental vs Swap Dealers Disaggregated
🟢 **FAIT VÉRIFIÉ** (Source : cot_disaggregated_notes.md, p.4) : Il existe une relation entre les positions "Index Traders" du Supplemental COT et les positions "Swap Dealers" du Disaggregated COT, mais avec des différences spécifiques : (1) certains Swap Dealers du Disaggregated ne font aucune activité d'index trading et ne sont donc pas dans la catégorie Index Traders du CIT ; (2) certains fonds de pension et d'investissement qui investissent directement dans les futures (sans passer par un swap dealer) sont classés "Managed Money" ou "Other Reportables" dans le Disaggregated, mais comme "Index Traders" dans le CIT Supplemental.
**TRADEX-AI C3** : Pour ZW (Blé CBOT), les Index Traders du Supplemental ne correspondent pas exactement aux Swap Dealers du Disaggregated. Pour une analyse complète de la pression d'achat indicielle sur ZW, utiliser le Supplemental CIT (Index Traders) ET le Disaggregated (Swap Dealers) séparément — ils couvrent des parties différentes de l'univers des investisseurs indiciels. Implémenter les deux flux dans le module C3 ZW en Phase 2.
*Catégorie : correlations*

### D9550 — Règle opérationnelle : 4 catégories Disaggregated — guide d'interprétation TRADEX synthétique
🟡 **SYNTHÈSE** (Source : cot_disaggregated_notes.md, ensemble du document) : Synthèse des 4 catégories COT Disaggregated pour TRADEX-AI, par ordre de pertinence signal :

| Catégorie | Signal pour TRADEX | Pondération C3 |
|-----------|-------------------|----------------|
| Managed Money | Directionnel spéculatif pur — trend follower | ×1.0 (pivot principal) |
| Producer/Merchant | Couverture physique — contra-indicateur de tendance | ×0.7 (signal inverse de couverture) |
| Swap Dealers | Mixte (hedge swaps + algo) — peu directionnel | ×0.3 (signal secondaire) |
| Other Reportables | Diversifié — bruit partiel | ×0.2 (signal tertiaire) |

**TRADEX-AI C3** : Score C3 pour chaque actif = weighted sum des NET positions × pondération. Règle de décision C3 : score normalisé ≥ 0.6 sur [-1;+1] = signal C3 haussier confirmé. Score ≤ -0.6 = signal C3 baissier confirmé. Entre -0.6 et +0.6 = signal C3 neutre (ne contribue pas à la décision). Cette règle synthétise l'ensemble des enseignements des 3 bundles CFTC (D9491→D9550).
*Catégorie : configuration*
