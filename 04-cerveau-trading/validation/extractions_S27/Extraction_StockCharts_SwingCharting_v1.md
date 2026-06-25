# Extraction StockCharts — Swing Charting
**Source :** `bundles/stockcharts/swing_charting.md` (HTTP 200) + 3 images certifiées
**Méthode images :** double ancrage · 3/3 certifiées · 0 à vérifier
**Décisions :** D3971 → D3990 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/swing-charting
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Techniques de swing charting (filtre volatilité, ZigZag, règle 4 semaines) applicables à GC/CL/HG/ZW pour identifier les swings majeurs et filtrer le bruit intraday.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.jpg | Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com | Swing Charting Techniques | D3975 |
| image_02.jpg | Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com | Swing Charting Techniques | D3976 |
| image_03.jpg | Hewlett-Packard Co. (HPQ) Swing example chart from StockCharts.com | Swing Charting Techniques | D3977 |

## DÉCISIONS

### D3971 — Définition du Swing Charting : filtre de mouvement minimum
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Le swing charting suit un concept simple — un nouveau mouvement de prix ne génère un nouveau tracé que si la progression dépasse le niveau du swing précédent dans la même direction. Il s'agit d'un graphique montrant uniquement les mouvements de hausse et de baisse d'une taille minimale, indépendamment du temps écoulé.
**TRADEX-AI C1** : Applicable à GC/HG/CL/ZW pour filtrer le bruit et ne garder que les swings significatifs sur les range bars NT8 — base d'un filtre pre-signal.
*Catégorie : structure_marche*

### D3972 — Swing Charting = système de cassure (breakout system)
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Les swing charts fonctionnent comme un système de cassure : un nouveau plus-haut après un certain nombre de jours est un signal d'achat, un nouveau plus-bas est un signal de vente.
**TRADEX-AI C1** : Signal d'entrée directionnel pour GC/HG/CL/ZW — le franchissement du swing précédent dans la direction de la tendance constitue un déclencheur actionnable.
*Catégorie : gestion_risque_entree*

### D3973 — Auteurs ayant utilisé le swing charting : Gann, Donchian, Wilder, Keltner, Livermore
🔵 **ÉCOLE** (Source : swing_charting.md) : Gann, Merrill, Livermore, Donchian, Hochheimer, Wilder et Keltner ont tous utilisé une forme de swing charting dans leurs systèmes de trading.
**TRADEX-AI C1** : Validation historique de l'approche swing — compatible avec les filtres Belkhayate qui ignorent les micro-mouvements inférieurs à un seuil de volatilité.
*Catégorie : structure_marche*

### D3974 — Filtre volatilité dynamique pour le swing : plus la volatilité augmente, moins de jours utilisés
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : De nombreux systèmes basés sur les swings utilisent la volatilité comme base pour déterminer les paramètres du filtre de swing. Ainsi, lorsque la volatilité courante augmente, le nombre de jours utilisés pour calculer le filtre de swing diminue.
**TRADEX-AI C1** : Principe d'adaptation dynamique — lorsque VIX (C5) est élevé, réduire le nb de barres du swing filter sur GC/CL ; lorsque VIX est faible, augmenter le nb de barres.
*Catégorie : indicateurs_tendance*

### D3975 — Règle Donchian des 4 semaines : achat au-dessus des plus-hauts 4 semaines, vente en dessous des plus-bas 4 semaines
🔵 **ÉCOLE** (Source : swing_charting.md, image_01.jpg) : La règle Donchian des quatre semaines : acheter quand le prix dépasse les plus-hauts des quatre semaines complètes précédentes, mais vendre (vendre à découvert) quand le prix descend sous les plus-bas des quatre dernières semaines complètes. En 1970, Dunn et Hargitt Financial Services l'ont classée meilleur système populaire de l'époque.
**TRADEX-AI C1** : Canal Donchian 4 semaines applicable sur GC/CL comme filtre de confirmation de tendance macro — aligné sur C3 (institutionnels) qui agissent sur des horizons similaires.
*Catégorie : indicateurs_tendance*

### D3976 — Filtre de Merrill (Filtered Waves) : filtre en % de mouvement de prix
🔵 **ÉCOLE** (Source : swing_charting.md, image_02.jpg) : Arthur Merrill a décrit les filtered waves dans son livre *Filtered Waves* (1977). Son filtre de swing est simplement un pourcentage de mouvement de prix. Cette technique retire le prix absolu de la décision et peut fonctionner sur presque toute série temporelle — filtre d'amplitude supprimant les informations indésirables.
**TRADEX-AI C1** : Un filtre en pourcentage (ex. 1-2% sur GC) permet d'identifier uniquement les swings significatifs indépendamment du niveau absolu de prix de l'Or — pertinent sur les actifs à prix élevé comme GC (>2000 USD).
*Catégorie : indicateurs_tendance*

### D3977 — ZigZag comme implémentation standard du swing charting filtré
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md, image_03.jpg) : ZigZag est utilisé par de nombreux programmes de graphiques, dont StockCharts.com, pour ce type de représentation en ondes filtrées. Un exemple simple est d'afficher les données de prix en n'identifiant que les mouvements de 5% ou plus.
**TRADEX-AI C1** : ZigZag configurable sur GC/HG/CL/ZW dans NT8 pour identifier automatiquement les points de retournement majeurs — seuil suggéré : 1-3% selon l'actif.
*Catégorie : indicateurs_tendance*

### D3978 — Le dernier segment ZigZag est dynamique jusqu'à confirmation du retournement
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Le dernier segment ZigZag changera au fur et à mesure que le prix le plus récent évolue, jusqu'à ce que les prix se retournent du montant du filtre. Le point critique est le point de retournement (turning point) — le point auquel les prix ont atteint au moins le montant du filtre depuis leur retournement. Si un turning point est visible, les prix ont déjà bougé d'au moins le montant filtré dans la direction opposée.
**TRADEX-AI C1** : Ne jamais utiliser le dernier segment ZigZag en temps réel comme signal confirmé sur GC/CL — attendre la confirmation du turning point (mouvement ≥ filtre dans la direction opposée).
*Catégorie : gestion_risque_entree*

### D3979 — Filtre 10% vs 5% : réduction des petites vagues
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Avec un filtre de 10%, certaines petites vagues présentes avec un filtre de 5% sont supprimées.
**TRADEX-AI C1** : Calibration progressive du filtre ZigZag sur HG/ZW — commencer par 2% puis tester 5% pour trouver le niveau optimal filtrant le bruit sans éliminer les signaux Belkhayate.
*Catégorie : indicateurs_tendance*

### D3980 — Filtre 15% : seuls les macro-swings restent visibles
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Avec un filtre de 15%, la petite hausse des derniers jours visible sur les graphiques précédents disparaît, car les prix n'ont pas bougé à la hausse de 15% depuis le début du segment baissier.
**TRADEX-AI C1** : Un filtre élevé (>10%) sur GC peut servir à identifier les tendances de fond sur plusieurs mois — pertinent pour C3 (positionnement institutionnel) et calibration des swing stops.
*Catégorie : structure_marche*

### D3981 — Swing charting : outil de suivi de tendance, limitation des pertes, respect des règles définies
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Le swing charting est un outil viable pour le trading et les décisions d'investissement, car il aide à rester dans la tendance, à limiter les pertes et à suivre des règles bien définies.
**TRADEX-AI C1** : Synthèse opérationnelle — le swing charting sert de filtre de tendance (C1) pour GC/HG/CL/ZW : ne trader que dans le sens du dernier swing majeur validé.
*Catégorie : gestion_position_active*

### D3982 — Techniques multiples : trois nouveaux plus-hauts consécutifs = haussier jusqu'à trois nouveaux plus-bas
🟢 **FAIT VÉRIFIÉ** (Source : swing_charting.md) : Certains systèmes utilisent trois nouveaux plus-hauts consécutifs comme une hausse (upswing) et le maintiennent jusqu'à trois nouveaux plus-bas consécutifs.
**TRADEX-AI C1** : Règle des 3-consécutifs applicable sur GC/CL pour confirmer un changement de swing — combiné avec la direction Belkhayate (C1) pour valider un retournement de tendance.
*Catégorie : configuration*

### D3983 — Swing charting : origines et diversité des approches
🟡 **SYNTHÈSE** (Source : swing_charting.md) : Il existe une multitude de techniques de swing charting différentes, mais le concept est identique : filtrer les mouvements inférieurs à un seuil et ne tracer que les mouvements significatifs. La liste des variantes est infinie.
**TRADEX-AI C1** : L'approche Belkhayate (filtrage des micro-fluctuations) est cohérente avec les principes universels du swing charting — validation de cohérence méthodologique.
*Catégorie : structure_marche*
