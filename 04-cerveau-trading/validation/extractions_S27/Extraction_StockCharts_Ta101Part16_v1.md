# Extraction StockCharts — TA 101 Part 16 (Candlestick Patterns)
**Source :** `bundles/stockcharts/ta_101_part_16.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D4151 → D4170 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-16
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Patterns chandelier (doji, formations multi-bougies) applicables sur tous les actifs TRADEX (GC/HG/CL/ZW/ES/VX/DX) pour détecter indécision et retournements de tendance à court terme.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Doji Candlestick | Doji Candlestick | D4151 |
| image_02.png | Doji Candlestick | Doji Candlestick | D4153 |
| image_03.png | Doji Candlestick | Doji Candlestick | D4155 |
| image_04.png | Doji Candlestick Formations | Doji Candlestick Formations | D4157 |
| image_05.png | Other Important Candlestick Patterns | Other Important Candlestick Patterns | D4160 |

## DÉCISIONS

### D4151 — Patterns chandelier : outil de lecture de la psychologie de marché
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md, image_01) : Une série de chandeliers développe souvent des patterns reconnaissables qui donnent au trader un aperçu de la psychologie actuelle du marché et la probabilité des mouvements de prix à court terme. Beaucoup de ces patterns de 1, 2 ou 3 chandeliers sont utilisés comme signes d'avertissement pour des retournements de tendance imminents.
**TRADEX-AI C1** : Les patterns chandelier complètent les indicateurs Belkhayate sur GC/HG/CL/ZW — un pattern de retournement à un niveau pivot Belkhayate renforce le score C1 de façon décisive.
*Catégorie : configuration*

### D4152 — Origine historique : traders japonais de riz au XVIIe siècle
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Des dizaines de patterns chandeliers ont été identifiés depuis les années 1700 avec les traders japonais de futures sur riz. Ces traders pouvaient rapidement identifier et communiquer les forces d'offre et de demande à court terme dans le marché avec ces patterns récurrents.
🔵 **ÉCOLE** : Attribution aux traders japonais de riz du XVIIe siècle — méthode ancienne et éprouvée sur commodités (asset class similaire à GC/ZW).
**TRADEX-AI C1** : Origine commodités → applicabilité directe sur GC (Or) et ZW (Blé) qui sont aussi des commodités physiques avec psychologie d'offre/demande similaire.
*Catégorie : indicateurs_tendance*

### D4153 — Doji : définition — indécision entre acheteurs et vendeurs
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md, image_02) : Le doji est un chandelier dont le prix monte et descend au-dessus et en dessous du prix d'ouverture pendant la journée, puis clôture au même prix (ou presque) qu'il a ouvert. C'est une indication que les forces acheteuses et vendeuses du marché étaient équilibrées, même si les investisseurs ont vécu une montagne russe de variations de prix pendant la journée.
**TRADEX-AI C1/C5** : Un doji sur GC/CL à un niveau de pivot Belkhayate = balance acheteurs/vendeurs = indécision → ne pas ouvrir de nouvelle position ; attendre confirmation directionnelle.
*Catégorie : indicateurs_momentum*

### D4154 — Doji : signe d'indécision précédant souvent un retournement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Les doji sont un signe d'indécision de marché qui précède souvent un retournement de tendance.
🟡 **SYNTHÈSE** : La valeur prédictive du doji est contextuelle — il est plus significatif après une tendance prolongée qu'au milieu d'une consolidation.
**TRADEX-AI C1** : Sur HG/ZW : un doji après une tendance prolongée = signal d'alerte retournement → passer en mode surveillance renforcée, réduire confiance du signal en cours.
*Catégorie : gestion_risque_entree*

### D4155 — Doji ombre inférieure longue : signal haussier
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md, image_03) : Avec les doji, une longue ombre inférieure est considérée haussière car l'intérêt acheteur a ramené le prix depuis un déclin intraday profond avant la clôture du marché.
**TRADEX-AI C1** : GC/CL : doji avec longue ombre basse sur range bars NT8 = rejet de zone de support + intérêt acheteur fort → compatible avec signal ACHETER si autres cercles s'alignent.
*Catégorie : indicateurs_tendance*

### D4156 — Doji ombre supérieure longue : signal baissier
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Les longues ombres supérieures sont baissières pour une raison similaire : l'intérêt acheteur initial cède la place aux vendeurs avant la clôture du marché.
**TRADEX-AI C1** : HG/ZW : doji avec longue ombre haute sur resistance Belkhayate = rejet de zone de résistance par les vendeurs → signal de prudence, réduire position longue ou attendre.
*Catégorie : indicateurs_tendance*

### D4157 — Formations doji multi-chandeliers : pivot dans les changements de tendance
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md, image_04) : Les formations de chandeliers avec doji sont souvent présentes dans les changements de tendance. Le doji dans ces patterns illustre comment l'indécision du marché agit souvent comme un pivot dans les changements de tendance.
🟡 **SYNTHÈSE** : Les formations à 2-3 chandeliers (morning star, evening star, harami) utilisent le doji comme élément central de pivot.
**TRADEX-AI C1** : Intégrer la détection des formations doji multi-chandeliers dans le prompt Claude API pour CL/GC — le doji pivot au sein d'une formation est plus fiable que le doji isolé.
*Catégorie : configuration*

### D4158 — Source Bulkowski : 6 patterns les plus fiables testés sur 4,7 millions de chandelles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Thomas N. Bulkowski a identifié six des patterns chandeliers les plus fiables basés sur des tests sur 4,7 millions de lignes de chandeliers.
🔵 **ÉCOLE** : Attribution à Thomas N. Bulkowski — source académique quantitative, pas une opinion.
**TRADEX-AI C1** : Prioriser les 6 patterns Bulkowski dans le scoring TRADEX — statistiquement validés sur grand échantillon, plus fiables que les patterns rares ou exotiques.
*Catégorie : indicateurs_tendance*

### D4159 — Couleur des corps dans les patterns : parfois non pertinente
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Les corps gris dans les diagrammes de patterns indiquent que la couleur du corps n'est pas pertinente pour le pattern concerné.
🟡 **SYNTHÈSE** : Certains patterns chandeliers sont définis uniquement par la structure des ombres et la position relative des corps, indépendamment de la couleur (haussier/baissier du corps).
**TRADEX-AI C1** : Dans le prompt Claude API, ne pas exclure des patterns sur la seule base de la couleur du corps — vérifier les conditions structurelles complètes du pattern.
*Catégorie : configuration*

### D4160 — 6 patterns Bulkowski les plus fiables : référence opérationnelle
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md, image_05) : Les six patterns les plus fiables selon Bulkowski sont présentés dans l'Encyclopedia of Candlestick Charts, validés sur 4,7 millions de chandelles.
🔵 **ÉCOLE** : Attribution Bulkowski — référence : *Encyclopedia of Candlestick Charts* (Thomas N. Bulkowski).
**TRADEX-AI C1** : Référence bibliographique confirmée pour enrichissement futur de la KB TRADEX avec les statistiques de réussite par pattern sur commodités (GC/HG/CL/ZW).
*Catégorie : indicateurs_tendance*

### D4161 — Greg Morris : introduction générale aux chandeliers
🔵 **ÉCOLE** (Source : ta_101_part_16.md) : Greg Morris's book *Candlestick Charting Explained* est recommandé comme bonne introduction générale au sujet.
**TRADEX-AI C1** : Source complémentaire pour enrichissement KB — niveau introductif, à prioriser après Bulkowski dans le pipeline d'extraction.
*Catégorie : indicateurs_tendance*

### D4162 — Patterns chandelier : pertinence sur 1, 2 ou 3 chandeliers
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Beaucoup de patterns chandeliers utilisés comme signes d'avertissement de retournements sont des patterns de 1, 2 ou 3 chandeliers.
🟡 **SYNTHÈSE** : Les patterns à 1 chandelier (doji, hammer, shooting star) donnent un signal rapide ; ceux à 3 chandeliers (morning/evening star) sont plus fiables mais plus lents.
**TRADEX-AI C1** : Sur range bars NT8 (timeframe court), privilégier d'abord les patterns à 2-3 chandeliers car les patterns simples peuvent générer plus de faux signaux sur haute fréquence.
*Catégorie : gestion_risque_entree*

### D4163 — Swing intraday du doji ERIE : 2,2% de volatilité haute/basse
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : Le SharpChart intraday à 10 minutes d'un doji particulier montre un swing de prix de 2,2% du haut au bas que les investisseurs ont subi pendant la journée.
⏳ **VOLATILE** : Exemple spécifique (ERIE) — valeur indicative de l'amplitude de volatilité d'un doji type en actions.
**TRADEX-AI C1** : Sur futures GC/CL, un doji journalier peut représenter des swings intraday bien supérieurs — l'amplitude de l'ombre doit être relativisée par l'ATR de l'actif.
*Catégorie : gestion_position_active*

### D4164 — Patterns chandeliers : limites à court terme uniquement
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Les patterns chandeliers donnent un aperçu de la "probabilité des mouvements de prix à court terme" — ils ne prédisent pas les tendances longues.
**TRADEX-AI C1** : Utiliser les patterns chandeliers comme confirmation d'entrée/sortie tactique sur GC/HG/CL/ZW, jamais comme signal de tendance macrostructurelle.
*Catégorie : gestion_risque_entree*

### D4165 — Doji : équilibre des forces malgré la volatilité intraday
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Un doji indique que les forces acheteuses et vendeuses étaient équilibrées — même si les prix ont beaucoup bougé intraday. L'équilibre final (clôture = ouverture) est la donnée décisive.
**TRADEX-AI C2** : Croiser le doji avec le delta ATAS C2 : si le delta net est proche de zéro à la clôture du doji, l'indécision est confirmée par l'order flow — signal d'attente renforcé.
*Catégorie : indicateurs_momentum*

### D4166 — Formations doji : rôle de pivot dans les changements de tendance
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Les formations avec doji (multi-chandeliers) illustrent comment l'indécision de marché agit souvent comme un pivot. C'est le doji lui-même qui matérialise le point de bascule psychologique.
⚫ **HYPOTHÈSE PROJET** : En méthode Belkhayate, le doji pivot à un niveau d'énergie nulle (BGC proche de zéro) constitue une confluences C1+C2 maximale.
**TRADEX-AI C1** : Doji sur niveau BGC nul + ombre directionnelle longue = entrée à haute probabilité Belkhayate sur CL/GC — scorer +0,5 point au score TRADEX /10.
*Catégorie : configuration*

### D4167 — Candlestick patterns : avertissement de retournement, pas certitude
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Les patterns chandeliers sont utilisés comme "signes d'avertissement" (warning signs) — ils indiquent une probabilité de retournement, pas une certitude.
**TRADEX-AI C1** : Dans le prompt Claude API, formuler la présence d'un pattern chandelier comme "indice C1 + N" dans le score — jamais comme condition suffisante pour signal autonome.
*Catégorie : psychologie*

### D4168 — Chandelier : héritage historique sur futures de commodités
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Les chandeliers ont été développés sur les futures de riz — donc sur une commodité physique, avec des caractéristiques de saisonnalité, d'offre/demande physique et de comportement institutionnel similaires aux actifs TRADEX.
🔵 **ÉCOLE** : Origine traders japonais XVIIe siècle sur marché des futures (riz).
**TRADEX-AI C1** : Validité des patterns chandeliers confirmée sur commodités — leur application sur GC/HG/CL/ZW est historiquement cohérente avec l'origine de la méthode.
*Catégorie : structure_marche*

### D4169 — Patterns à surveiller : horizon Part 17 (Comparison Charting)
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_16.md) : La prochaine partie (Part 17) couvre le Comparison Charting.
**TRADEX-AI C7** : Le Comparison Charting (performance relative) est directement applicable aux corrélations inter-marchés C7 de TRADEX (GC vs DX, ES vs VX, etc.).
*Catégorie : correlations*

### D4170 — Fiabilité statistique : critère discriminant pour sélection des patterns
🟡 **SYNTHÈSE** (Source : ta_101_part_16.md) : Bulkowski a testé 4,7 millions de chandelles pour identifier les patterns fiables — la validité statistique distingue les patterns opérationnels des patterns anecdotiques.
**TRADEX-AI C1** : Prioriser dans la KB TRADEX uniquement les patterns avec validation statistique (Bulkowski ou équivalent) — écarter les patterns rarissimes ou non testés empiriquement.
*Catégorie : indicateurs_tendance*
