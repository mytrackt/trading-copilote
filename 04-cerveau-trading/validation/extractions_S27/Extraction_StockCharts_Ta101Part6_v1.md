# Extraction StockCharts — TA 101 Part 6
**Source :** `bundles/stockcharts/ta_101_part_6.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D4271 → D4290 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-6
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : scaling des charts (arithmétique vs log) + volume coloré + CandleVolume — applicable à GC/HG/CL/ZW pour le calibrage des trendlines et la lecture du volume dans l'action des prix.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Chart Scaling | Chart Scaling | D4271 |
| image_02 | Chart Scaling | Chart Scaling | D4272 |
| image_03 | Volume | Volume | D4276 |
| image_04 | CandleVolume Charts | CandleVolume Charts | D4281 |

## DÉCISIONS

### D4271 — Échelle arithmétique : espacement uniforme en valeur absolue
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md, image_01) : Une échelle arithmétique espace les prix de façon uniforme sur le côté droit du chart. L'espacement entre $10 et $20 est deux fois moins grand que l'espacement entre $20 et $40 — les distances en pixels sont proportionnelles aux différences de prix absolues.
**TRADEX-AI C1** : L'échelle arithmétique convient aux analyses court terme sur range bars NT8 pour GC/HG/CL/ZW où les mouvements sont mesurés en valeur absolue (points/ticks) — adapté aux entrées intraday.
*Catégorie : structure_marche*

### D4272 — Échelle logarithmique : espacement uniforme en pourcentage
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md, image_02) : Une échelle log espace les prix en termes de pourcentage. L'espacement entre $10 et $20 est exactement le même qu'entre $20 et $40 puisqu'ils représentent la même augmentation en pourcentage (+100%).
**TRADEX-AI C1** : L'échelle log convient aux analyses long terme sur GC (Or) où des mouvements de $100 représentent des pourcentages très différents à $1000 vs $2000 — utile pour la macro-tendance et le calibrage des niveaux Belkhayate long terme.
*Catégorie : structure_marche*

### D4273 — Trendlines sur données longues : l'échelle log est supérieure
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md, image_01 + image_02) : Sur l'échelle arithmétique, TROIS lignes de tendance différentes ont été nécessaires pour suivre l'avancée des prix. Sur l'échelle log, UNE SEULE ligne de tendance correspond à toute la tendance haussière sur la même période.
🟢 **FAIT VÉRIFIÉ** : "Log scaling should be the first scaling choice when using trend lines, especially over long timeframes."
**TRADEX-AI C1** : Pour les trendlines Belkhayate sur GC (Or) analysé sur plusieurs mois/années, utiliser l'échelle log en priorité — une seule trendline au lieu de plusieurs fragmentées = analyse plus propre.
*Catégorie : indicateurs_tendance*

### D4274 — Trendlines long terme : l'échelle log comme choix par défaut
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : Citation directe : "Log scaling should be the first scaling choice when using trend lines, especially over long timeframes." C'est une recommandation normative explicite.
🔵 **ÉCOLE** (StockCharts) : Standard professionnel en analyse technique — les charts log pour les trendlines.
**TRADEX-AI C1** : Pour le dashboard TRADEX, l'échelle log doit être l'option par défaut pour les vues multi-semaines/multi-mois de GC/HG/CL/ZW/ES/DX. L'échelle arithmétique reste disponible pour le court terme intraday.
*Catégorie : indicateurs_tendance*

### D4275 — Arithmétique vs Log : impact différent sur la même tendance
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md, image_01 + image_02) : La même tendance haussière exige 3 trendlines en arithmétique vs 1 seule en log. Cela signifie que les "cassures de trendline" peuvent être des artefacts de l'échelle choisie plutôt que de vrais signaux de retournement.
**TRADEX-AI C1** : Une cassure de trendline sur GC en échelle arithmétique doit être vérifiée sur l'échelle log avant de déclencher un signal — éviter les faux signaux de retournement dus à l'échelle.
*Catégorie : gestion_risque_entree*

### D4276 — Volume : plusieurs façons de le représenter sur un chart
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md, image_03) : StockCharts fournit plusieurs façons de représenter les données de volume. Le volume peut être représenté dans un panneau indicateur au-dessus ou en dessous de la zone de prix, ou dans la zone de prix en tant qu'overlay.
**TRADEX-AI C2** : Cohérent avec l'architecture TRADEX — ATAS présente le volume en footprint (overlay sur prix) ET en histogram séparé; les deux représentations sont complémentaires pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D4277 — Volume coloré : noir pour up days, rouge pour down days
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : Avec l'option 'Color Volume', les barres de volume sont affichées en noir pour les up days et en rouge pour les down days. "Les barres de volume colorées permettent au chartiste de voir rapidement où l'activité d'achat et de vente forte ou faible se produit."
**TRADEX-AI C2** : La logique volume coloré est la version simplifiée du delta ATAS — volume noir = acheteurs actifs, rouge = vendeurs actifs; détectable sur GC/HG/CL/ZW pour confirmer la direction du signal.
*Catégorie : volume_liquidite*

### D4278 — Volume coloré + price bar : confirmation de la conviction directionnelle
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : Volume coloré noir sur barre de prix haussière = achat actif qui confirme la direction. Volume coloré rouge sur barre baissière = vente active qui confirme la direction. Divergence (ex: volume rouge sur barre haussière) = signal d'affaiblissement.
**TRADEX-AI C2** : Pour GC/HG/CL/ZW, vérifier la cohérence couleur prix/couleur volume — divergence = réduire la conviction du signal; cohérence = augmenter la conviction. Intégrable dans le scoring C2.
*Catégorie : volume_liquidite*

### D4279 — Le volume peut être affiché en overlay ou en panneau séparé
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : Le volume peut être tracé dans un "indicator panel" au-dessus ou en dessous de la "price plot area", ou dans la price plot area en tant qu'"overlay".
🟡 **SYNTHÈSE** : En overlay, le volume est intégré directement dans le mouvement de prix — CandleVolume (D4281) pousse cette logique encore plus loin.
**TRADEX-AI C1/C2** : Le dashboard TRADEX React pour GC/HG/CL/ZW peut afficher le volume en panneau séparé (standard) ET permettre le mode CandleVolume pour l'analyse intensive de la corrélation prix/volume.
*Catégorie : volume_liquidite*

### D4280 — Volume = confirmation des mouvements de prix
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : StockCharts fournit des outils de visualisation volume précisément parce que le volume confirme les mouvements de prix — un mouvement sans volume est moins fiable qu'un mouvement avec volume fort.
🔵 **ÉCOLE** (Principe classique AT) : "Volume precedes price" — le volume fort précède et confirme les breakouts et les retournements.
**TRADEX-AI C2** : Pour GC/HG/CL/ZW, un signal TRADEX doit inclure la vérification du volume relatif — volume supérieur à la moyenne lors du signal = confirmation; volume faible = signal peu fiable.
*Catégorie : volume_liquidite*

### D4281 — CandleVolume chart : largeur du chandelier proportionnelle au volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md, image_04) : Les CandleVolume charts sont similaires aux chandeliers japonais sauf que la largeur de chaque chandelier est proportionnelle à sa valeur de volume correspondante. Ce style de chart permet de visualiser l'activité de volume "dans" les mouvements de prix plutôt qu'"en dessous". Selon le style d'analyse, les barres de volume peuvent être omises pour simplifier le chart.
**TRADEX-AI C2** : CandleVolume est conceptuellement proche des footprint bars ATAS — le volume est intégré dans la représentation du prix. Cette visualisation renforce la corrélation prix/volume pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D4282 — CandleVolume : axe temporel non uniforme
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : "L'axe temporel de ces charts n'est pas uniformément espacé car les largeurs des barres chandelier varient avec les valeurs de volume. En conséquence, l'analyse de trendline utilisant des CandleVolume charts doit toujours être confirmée avec un chandelier standard ou un chart OHLC."
**TRADEX-AI C1** : Règle critique : les trendlines tracées sur CandleVolume sont INVALIDES sans confirmation sur chart standard — ne jamais baser un signal TRADEX sur une trendline CandleVolume seule pour GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D4283 — CandleVolume confirme la corrélation barres/volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : "Le SharpChart de AAPL ci-dessus montre comment les barres de volume sont corrélées aux largeurs des chandeliers" — illustration directe de la corrélation volume/prix dans un format intégré.
🟡 **SYNTHÈSE** : Un chandelier large = forte activité = consensus du marché sur ce mouvement. Un chandelier étroit = faible activité = mouvement sans conviction.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, chandelier large (fort volume) dans le sens du signal = signal de haute qualité; chandelier étroit (faible volume) = signal peu fiable, même si la direction est correcte.
*Catégorie : volume_liquidite*

### D4284 — Échelle arithmétique : adaptée au court terme et aux mouvements en valeur absolue
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : L'échelle arithmétique est implicitement recommandée pour les analyses court terme où les mouvements sont mesurés en valeur absolue (points, ticks) plutôt qu'en pourcentage.
**TRADEX-AI C1** : Pour le Mode Manuel TRADEX sur range bars NT8 (timeframe court terme), l'échelle arithmétique est appropriée — les stops et targets se calculent en points/ticks sur GC/HG/CL/ZW, pas en %.
*Catégorie : gestion_risque_entree*

### D4285 — Même tendance, métriques différentes : l'échelle choisie change l'interprétation
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md, image_01 + image_02) : La même tendance sur les mêmes données produit 3 trendlines (arithmétique) vs 1 trendline (log). Cela implique que le nombre de "cassures" apparentes dépend de l'échelle — bruit sur arithmétique peut être signal ou non-événement sur log.
**TRADEX-AI C1** : Règle de validation multi-échelle pour TRADEX : avant de valider un signal basé sur une cassure de trendline pour GC/HG/CL/ZW, vérifier sur les deux échelles — arithmétique (micro) et log (macro). Seule une cassure visible sur les deux est un vrai signal.
*Catégorie : gestion_risque_entree*

### D4286 — Volume dans price plot area (overlay) vs panneau séparé : deux usages distincts
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : Volume en overlay = corrélation directe avec le mouvement de prix (mais encombre le chart). Volume en panneau séparé = lecture claire mais perd la corrélation spatiale avec les barres de prix spécifiques.
**TRADEX-AI C2** : Pour le dashboard TRADEX, permettre le basculement overlay/panneau selon le contexte d'analyse — overlay pour l'analyse détaillée C2, panneau séparé pour le Mode Manuel (lisibilité maximale pour la décision rapide d'Abdelkrim).
*Catégorie : configuration*

### D4287 — CandleVolume peut omettre les barres de volume pour simplification
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : "Depending on the style of analysis, volume bars could be omitted to simplify the chart" — dans le format CandleVolume, la largeur du chandelier encode déjà le volume, rendant les barres de volume redondantes.
**TRADEX-AI C2** : Option UI TRADEX : en mode CandleVolume, masquer les barres de volume séparées — la largeur des chandeliers suffit pour lire le volume; dashboard GC/HG/CL/ZW plus épuré en Mode Manuel.
*Catégorie : configuration*

### D4288 — Trendlines CandleVolume : toujours confirmer sur chart standard
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_6.md) : "Trend line analysis using CandleVolume charts should always be confirmed with a standard candlestick or OHLC chart."
**TRADEX-AI C1** : Règle de garde-fou explicite : aucune trendline tracée sur CandleVolume ne peut déclencher seule un signal TRADEX — confirmation obligatoire sur chart chandelier standard ou OHLC pour GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D4289 — Volume fort sur up day = achat actif convaincu
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : La couleur noire des barres de volume sur les up days (D4277) + la largeur proportionnelle dans CandleVolume (D4281) permettent de quantifier visuellement l'intensité de l'achat journalier.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, up day + volume > moyenne + delta ATAS positif = triple confirmation d'achat actif → signal LONG de haute qualité pour le scoring TRADEX.
*Catégorie : volume_liquidite*

### D4290 — Structure complète du chart : prix + volume + indicateurs = analyse complète
🟡 **SYNTHÈSE** (Source : ta_101_part_6.md) : La série TA 101 Part 3-6 décrit une architecture complète : données brutes → barres de prix (Part 3) → types de charts (Part 4) → lecture psychologique des chandeliers (Part 5) → scaling + volume intégré (Part 6). Ensemble, ces composants forment la base de l'AT.
**TRADEX-AI C1/C2** : Le dashboard TRADEX pour GC/HG/CL/ZW implémente exactement cette hiérarchie : barres range NT8 (données brutes), chandeliers (visualisation), volume coloré + ATAS (ordre flow), scaling adaptatif (arithmétique intraday / log macro). Architecture cohérente avec les standards StockCharts.
*Catégorie : configuration*
