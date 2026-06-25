# Extraction StockCharts — Relative Rotation Graphs (RRG)
**Source :** `bundles/stockcharts/relative_rotation_graphs_rrg_charts.md` (HTTP 200) + 14 images certifiées
**Méthode images :** double ancrage · 14/14 certifiées · 0 à vérifier
**Décisions :** D3391 → D3404 · **Page :** chartschool.stockcharts.com/.../chart-types/relative-rotation-graphs-rrg-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 RRG illustré sur **secteurs actions** (SPDR vs S&P 500), mais le concept RS-Ratio/RS-Momentum vs benchmark s'applique à l'analyse **inter-marché** (Cercle C7) : GC/HG/CL/ZW vs un benchmark commun.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | XLK price relative + RRG indicators | JdK RS-Ratio | D3393 |
| image_02 | XLY price relative + RRG indicators | JdK RS-Ratio | D3393 |
| image_03/04 | JdK RS-Momentum (section-fallback) | JdK RS-Momentum | D3395 |
| image_05 | RRG Construction (section-fallback) | RRG Construction | D3396 |
| image_06 | Rotation Sequence (section-fallback) | Rotation Sequence | D3398 |
| image_07 | Rotation Trails (section-fallback) | Rotation Trails | D3399 |
| image_08/09 | Interpreting RRG (section-fallback) | Interpreting RRG Charts | D3401 |
| image_10-14 | Weekly vs Daily (section-fallback) | Weekly Versus Daily | D3402 |

## DÉCISIONS

### D3391 — RRG : définition
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md) : Outil de visualisation de la force relative — analyse les tendances de force relative de plusieurs titres contre un benchmark commun ET entre eux. Quatre quadrants définissent les 4 phases d'une tendance relative ; les rotations se voient quand un titre passe d'un quadrant à l'autre.
🔵 **ÉCOLE** : « RRG® » = marque déposée de RRG Research.
**TRADEX-AI C7** : Cadre de rotation inter-marché applicable à GC/HG/CL/ZW vs benchmark.
*Catégorie : structure_marche*

### D3392 — Origine (de Kempenaer, 2004-2005)
🔵 **ÉCOLE** (Source : relative_rotation_graphs_rrg_charts.md) : Développé en 2004-2005 par Julius de Kempenaer (RRG Research) pour répondre au besoin de performance relative et de séparation leaders/laggards.
**TRADEX-AI C7** : Contexte/attribution.
*Catégorie : structure_marche*

### D3393 — JdK RS-Ratio
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_01, image_02) : RS-Ratio mesure la **tendance** de la performance relative (analyse de ratio vs benchmark). > 100 = uptrend relatif (force), < 100 = downtrend relatif (faiblesse). Plus éloigné de 100 = tendance plus forte. Indicateurs « normalisés » → comparables entre titres au même benchmark.
**TRADEX-AI C7** : RS-Ratio = mesure de force relative comparable inter-marché.
*Catégorie : indicateurs_tendance*

### D3394 — Lag du RS-Ratio
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md) : Comme tout indicateur trend-following (ex. MA), RS-Ratio a un lag : le price relative bouge avant que RS-Ratio ne croise 100.
**TRADEX-AI C3** : Tenir compte du retard ; ne pas attendre RS-Ratio seul pour anticiper.
*Catégorie : indicateurs_tendance*

### D3395 — JdK RS-Momentum
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_03, image_04) : RS-Momentum mesure le momentum (rate-of-change) de RS-Ratio. Indicateur avancé : croise 100 quand RS-Ratio forme un creux/sommet. C'est un « indicateur d'indicateur » → bruyant ; privilégier les mouvements soutenus au-dessus/dessous de 100.
**TRADEX-AI C7** : RS-Momentum = signal avancé de retournement de force relative.
*Catégorie : indicateurs_momentum*

### D3396 — Construction (scatter-plot)
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_05) : RS-Ratio en axe X, RS-Momentum en axe Y, croisement à 100 → 4 quadrants. Chaque point = (RS-Ratio, RS-Momentum) d'un symbole.
**TRADEX-AI C7** : Graphe 2D à reproduire pour la matrice corrélations/rotations.
*Catégorie : configuration*

### D3397 — Les 4 quadrants
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md) : **Leading** (vert, +/+ : RS-Ratio & RS-Momentum >100) · **Weakening** (jaune, +/- ) · **Lagging** (rouge, -/- ) · **Improving** (bleu, -/+ ).
**TRADEX-AI C7** : Classification d'état relatif des actifs (leader/retardataire).
*Catégorie : structure_marche*

### D3398 — Séquence de rotation (horaire)
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_06) : Rotation idéalisée **horaire** : Leading → Weakening (RS-Momentum tourne en premier) → Lagging → Improving → Leading. RS-Momentum est l'indicateur avancé qui tourne d'abord.
**TRADEX-AI C7** : Anticiper la séquence (mais elle n'est pas toujours parfaitement circulaire).
*Catégorie : signal*

### D3399 — Rotation trails (longueur/épaisseur)
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_07) : Les trails historiques (1 point/semaine) montrent la rotation. Longueur = ampleur/volatilité du mouvement ; épaisseur = distance au benchmark (plus loin = plus gros mouvement relatif).
**TRADEX-AI C7** : Métriques de force/volatilité relative à exploiter.
*Catégorie : structure_marche*

### D3400 — Réglage trail / nombre de symboles
🟡 **CONVENTION** (Source : relative_rotation_graphs_rrg_charts.md) : Raccourcir la longueur de trail quand beaucoup de symboles (dé-encombrer) ; trails longs OK pour peu de symboles.
**TRADEX-AI C7** : Paramètre d'affichage.
*Catégorie : configuration*

### D3401 — RRG n'est PAS un système de trading
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_08, image_09) : Pas de règles/signaux prédéfinis ; ouvert à interprétation. Repères : RS-Ratio > RS-Momentum en importance ; un cross de la gauche vers la droite = nouvel uptrend relatif (RS-Ratio >100), et inverse.
**TRADEX-AI C7** : Utiliser comme couche contextuelle de force relative, jamais comme déclencheur d'ordre.
*Catégorie : structure_marche*

### D3402 — Weekly vs Daily
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md, image_10, image_11, image_12, image_13, image_14) : Le timeframe affecte le RRG comme un bar chart : un secteur en lagging sur weekly peut être en leading sur daily (rotation court terme). Étudier plusieurs timeframes pour une image complète.
**TRADEX-AI C3** : Multi-temporalité — cohérence weekly (tendance) + daily (signal).
*Catégorie : timing*

### D3403 — Usage selon style
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md) : Momentum traders → croisements vers improving/weakening ; trend followers → croisements vers leading/lagging. À combiner avec d'autres outils (risque de rotation qui se retourne).
**TRADEX-AI C7** : Adapter la lecture au style ; confirmation requise.
*Catégorie : signal*

### D3404 — Pertinence TRADEX (inter-marché)
🟢 **FAIT VÉRIFIÉ** (Source : relative_rotation_graphs_rrg_charts.md) : Outil de **performance relative** vs benchmark — applicable au-delà des secteurs actions.
**TRADEX-AI C7** : Candidat pour visualiser la rotation GC/HG/CL/ZW (+ ES/DX/VX) vs un benchmark commun dans la matrice corrélations 30j. Pertinence directe futures = à valider (exemples source = actions).
*Catégorie : structure_marche*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3391 → D3404 (14) |
| Images citées | 14/14 |
| Catégories | structure_marche · indicateurs_tendance · indicateurs_momentum · signal · timing · configuration |
| Tags | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Belkhayate | NON CONCERNÉ (outil force relative C7) |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
