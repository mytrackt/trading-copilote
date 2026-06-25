# Extraction StockCharts — Raff Regression Channel
**Source :** `bundles/stockcharts/raff_regression_channel.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D3311 → D3320 · **Page :** chartschool.stockcharts.com/.../chart-annotation-tools/raff-regression-channel
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Raff Regression Channel en uptrend (QQQ) | How To Calculate | D3312 |
| image_02 | Raff Regression Channel en downtrend (QQQ) | How To Calculate | D3313 |
| image_03 | Cassure sous le canal = retournement (URBN) | Drawing and Signals | D3315 |
| image_04 | Cassure au-dessus = retournement (NVDA) | Drawing and Signals | D3315 |
| image_05 | Réglages SharpCharts (section-fallback) | Using with SharpCharts | D3319 |

## DÉCISIONS

### D3311 — Raff Regression Channel : définition
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md) : Régression linéaire (Gilbert Raff) avec deux trend lines parallèles équidistantes au-dessus/dessous. Tendance haussière tant que les prix montent dans le canal ; elle s'inverse quand le prix casse sous l'extension. Inverse pour la baisse.
🔵 **ÉCOLE** : Outil de Gilbert Raff.
**TRADEX-AI C1** : Canal de tendance projetable sur GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D3312 — Ligne médiane = régression sur clôtures
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md, image_01) : La ligne médiane est la régression linéaire (least-squares, ligne de meilleur ajustement) basée sur les **prix de clôture**, du bas de clôture au haut de clôture.
**TRADEX-AI C1** : Calcul sur clôtures (least-squares) ; déterministe.
*Catégorie : indicateurs_tendance*

### D3313 — Largeur = high/low le plus éloigné
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md, image_02) : La largeur est fixée par le high ou low **le plus éloigné** de la régression ; la ligne opposée est placée à la même distance. (Note : clôtures pour la médiane, mais highs/lows intraday pour fixer les trend lines.)
**TRADEX-AI C1** : Règle de largeur à coder précisément (extrême le plus éloigné).
*Catégorie : configuration*

### D3314 — Tracé : extension de tendance
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md) : Un uptrend s'étend du plus bas de clôture au plus haut de clôture ; un downtrend du plus haut au plus bas. Les extensions de lignes identifient support/résistance/points de retournement.
**TRADEX-AI C1** : Extensions = niveaux S/R projetés.
*Catégorie : structure_marche*

### D3315 — Signal de retournement par cassure d'extension
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md, image_03, image_04) : Une cassure sous l'extension du canal inverse l'uptrend (URBN) ; une cassure au-dessus inverse le downtrend (NVDA).
**TRADEX-AI C3** : Cassure d'extension = signal de retournement à confirmer.
*Catégorie : signal*

### D3316 — Limite : spikes → canaux trop larges
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md) : Les spike highs/lows produisent des canaux très larges qui peuvent ne pas capturer le vrai range. Un départ de tendance en forte impulsion crée un canal large avec peu de réactions touchant les bornes.
**TRADEX-AI C3** : Garde — défier le canal si la tendance démarre par une impulsion brutale (largeur trompeuse).
*Catégorie : gestion_risque_entree*

### D3317 — Usage : identification de tendance
🟢 **FAIT VÉRIFIÉ** (Source : raff_regression_channel.md) : Bien adapté à l'**identification de tendance** ; peut aussi être tracé tôt et étendu pour prévoir des niveaux S/R futurs et des zones de surachat/survente (moves hors extensions).
**TRADEX-AI C1** : Double usage tendance + projection S/R.
*Catégorie : indicateurs_tendance*

### D3318 — Confirmation par d'autres outils
🟡 **CONVENTION** (Source : raff_regression_channel.md) : Comme tout outil, à combiner avec d'autres techniques (les exemples sont sur actions/indices US, non sur futures).
**TRADEX-AI C3** : Jamais en isolation ; recalibrer hors contexte actions.
*Catégorie : gestion_risque_entree*

### D3319 — Implémentation SharpCharts (ChartNotes)
🔵 **ÉCOLE** (Source : raff_regression_channel.md, image_05) : Ajout via ChartNotes (Annotate → Raff Regression, 5e bouton) en identifiant un high et un low.
**TRADEX-AI C0** : Référence outillage tiers ; à recréer côté NT8.
*Catégorie : configuration*

### D3320 — Formule non détaillée
🔴 **NON VÉRIFIÉ** (Source : raff_regression_channel.md) : L'article indique que « la formule dépasse le cadre de l'article » → la formule complète de régression n'est pas littéralement fournie ici (concept de least-squares seulement).
**TRADEX-AI C0** : Compléter la formule de régression linéaire depuis une source dédiée avant codage.
*Catégorie : configuration*

## SYNTHÈSE
| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D3311 → D3320 (10) |
| Images citées | 5/5 |
| Catégories | indicateurs_tendance · structure_marche · signal · gestion_risque_entree · configuration |
| Tags | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION · 🔴 NON VÉRIFIÉ |
| Belkhayate | NON CONCERNÉ (canal régression ≠ COG, malgré thème « régression » — non affirmé) |

> ⚠️ Outil éducatif · validation/ — aucune fusion master sans OK.
