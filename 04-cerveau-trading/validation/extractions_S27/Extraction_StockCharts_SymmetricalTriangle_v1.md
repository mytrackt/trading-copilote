# Extraction StockCharts — Symmetrical Triangle
**Source :** `bundles/stockcharts/symmetrical_triangle.md` (HTTP 200) + 2 images certifiées
**Méthode images :** double ancrage · 2/2 certifiées · 0 à vérifier
**Décisions :** D3991 → D4010 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/symmetrical-triangle
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Pattern triangle symétrique (continuation de tendance ~75%) directement applicable sur GC/CL/HG/ZW pour identifier des consolidations avant reprise de tendance ; confirmation par volume et breakout.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.png | Example of a Symmetrical Triangle pattern. | Symmetrical Triangle | D3991 |
| image_02.png | An example of a Symmetrical Triangle Pattern in the chart of Conseco, Inc. | Symmetrical Triangle | D4001 |

## DÉCISIONS

### D3991 — Triangle symétrique : définition et formation
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md, image_01.png) : Le triangle symétrique, aussi appelé coil (ressort), se forme généralement lors d'une tendance comme pattern de continuation. Il contient au minimum deux plus-hauts décroissants et deux plus-bas croissants. Lorsque ces points sont reliés, les lignes convergent en s'étendant. On peut également le considérer comme un coin se contractant, large au début et se rétrécissant dans le temps.
**TRADEX-AI C1** : Formation de consolidation à surveiller sur GC/CL/HG/ZW — indique une indécision temporaire avant reprise ; ne pas entrer avant le breakout confirmé.
*Catégorie : configuration*

### D3992 — Triangle symétrique : principalement pattern de continuation (~75% des cas)
🔵 **ÉCOLE** (Source : symmetrical_triangle.md) : Dans *Technical Analysis of Stock Trends* (1948), Edwards et Magee indiquent qu'environ 75% des triangles symétriques sont des patterns de continuation et le reste marque des retournements. Les patterns de retournement sont particulièrement difficiles à analyser et présentent souvent des faux breakouts.
**TRADEX-AI C1** : Sur GC/CL/ZW, en présence d'un triangle symétrique, appliquer un biais de continuation (probabilité 75%) — mais attendre le breakout confirmé avant d'agir.
*Catégorie : configuration*

### D3993 — Condition préalable : tendance établie d'au moins quelques mois
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Une tendance établie (d'au moins quelques mois) doit exister pour qualifier le triangle comme pattern de continuation. Le triangle symétrique marque une période de consolidation avant de continuer après le breakout.
**TRADEX-AI C1** : Ne valider un triangle symétrique comme signal de continuation sur GC/HG/CL/ZW que si la tendance sous-jacente est établie depuis plusieurs semaines minimum — aligné avec l'analyse macro C4.
*Catégorie : configuration*

### D3994 — Minimum 4 points requis (idéalement 6) pour former un triangle symétrique valide
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Il faut au minimum quatre points pour considérer une formation comme un triangle symétrique. Le deuxième plus-haut (2) doit être inférieur au premier (1), et la ligne supérieure doit s'incliner vers le bas. Le deuxième plus-bas (2) doit être supérieur au premier (1), et la ligne inférieure doit s'incliner vers le haut. Idéalement, le pattern se forme avec six points (trois de chaque côté) avant le breakout.
**TRADEX-AI C1** : Critère de validité structurelle pour GC/HG/CL/ZW — exiger au minimum 4 points de contact (2 hauts + 2 bas) avant de considérer le pattern comme valide.
*Catégorie : configuration*

### D3995 — Volume : doit diminuer pendant la formation du triangle
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Le volume doit diminuer à mesure que le triangle symétrique se développe et que la plage de trading se contracte. Cela correspond au calme avant la tempête — la consolidation se resserre avant le breakout.
**TRADEX-AI C2** : Sur GC/CL, surveiller la contraction du volume (C2 Order Flow) pendant la formation du triangle — une contraction de volume confirme le pattern ; une expansion prématurée invalide la lecture.
*Catégorie : volume_liquidite*

### D3996 — Durée typique du triangle symétrique : environ trois mois (minimum pennant si < 3 semaines)
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Le triangle symétrique peut s'étendre sur quelques semaines ou plusieurs mois. Le pattern est généralement considéré comme un pennant s'il dure moins de trois semaines. Typiquement, la durée est d'environ trois mois.
**TRADEX-AI C1** : Distinction triangle vs pennant : sur GC/HG/CL/ZW, un pattern durant moins de 3 semaines = pennant (cible plus faible) ; au-delà = triangle symétrique (cible plus large).
*Catégorie : timing*

### D3997 — Breakout idéal entre 1/2 et 3/4 du développement du pattern
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Le breakout idéal se produit entre 1/2 et 3/4 du développement du pattern ou de sa durée, mesurée de l'apex (convergence des lignes) jusqu'au début de la ligne de tendance inférieure (base). Un break avant le point 1/2 peut être prématuré, et un break trop proche de l'apex peut être non significatif.
**TRADEX-AI C1** : Zone de breakout optimal pour GC/CL : entre 50% et 75% du temps de formation du triangle — breakouts hors de cette zone nécessitent une confirmation supplémentaire.
*Catégorie : timing*

### D3998 — Direction du breakout : ne jamais anticiper, attendre la confirmation
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : La direction future du breakout ne peut être déterminée qu'après que le break s'est produit. Tenter de deviner la direction du breakout peut être dangereux. Même si un pattern de continuation est censé breaker dans la direction de la tendance à long terme, ce n'est pas toujours le cas.
**TRADEX-AI C1** : Règle de discipline absolue pour TRADEX — ne jamais anticiper la direction du breakout sur GC/HG/CL/ZW ; attendre la clôture de confirmation avant de placer un ordre.
*Catégorie : gestion_risque_entree*

### D3999 — Confirmation du breakout : clôture de barre + filtre prix (3%) ou temps (3 jours) + expansion volume
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Un break doit être sur une base de clôture pour être considéré comme valide. Certains traders appliquent un filtre prix (break de 3%) ou temps (soutenu pendant 3 jours) pour confirmer la validité. Le breakout doit se produire avec une expansion de volume, surtout pour les breakouts haussiers.
**TRADEX-AI C1/C2** : Critères de confirmation breakout sur GC/CL : clôture au-delà du triangle + expansion de volume (C2). Pour les breakouts haussiers sur GC, l'expansion de volume est obligatoire.
*Catégorie : gestion_risque_entree*

### D4000 — Retour à l'apex après breakout : support/résistance potentiel
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Après le breakout (en hausse ou en baisse), l'apex peut devenir un futur support ou résistance. Le prix revient parfois à l'apex ou à un niveau de support/résistance autour du point de breakout avant de reprendre dans la direction du breakout.
**TRADEX-AI C1** : Opportunité de second entry sur GC/HG/CL/ZW : si le prix revient à l'apex après un breakout valide, c'est une zone d'entrée à meilleur R/R — stop sous/sur l'apex selon la direction.
*Catégorie : gestion_risque_entree*

### D4001 — Mesure de la cible prix : méthode 1 — largeur maximale du triangle appliquée au point de breakout
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md, image_02.png) : Première méthode pour estimer l'étendue du mouvement après le breakout : mesurer la distance maximale du triangle symétrique et l'appliquer au point de breakout.
**TRADEX-AI C1** : Calcul de cible prix pour GC/CL : largeur maximale du triangle (base) projetée depuis le point de breakout = première cible take-profit.
*Catégorie : gestion_position_active*

### D4002 — Mesure de la cible prix : méthode 2 — ligne de tendance parallèle
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Deuxième méthode : tracer une ligne de tendance parallèle à la ligne de tendance du pattern qui s'incline (en hausse ou en baisse) dans la direction du breakout. L'extension de cette ligne indique une cible de breakout potentielle.
**TRADEX-AI C1** : Technique du canal parallèle pour cibler les mouvements post-breakout sur GC/HG/CL/ZW — croiser les deux méthodes (largeur + canal) pour identifier une zone de confluence cible.
*Catégorie : gestion_position_active*

### D4003 — Exemple Conseco : triangle baissier sur 5 mois, breakout à la baisse avec volume
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md, image_02.png) : Conseco (CNCEQ) a formé un large triangle symétrique sur cinq mois avant de breaker à la baisse. Le breakout s'est produit avec une augmentation de volume et une accélération de la baisse de prix. Le Chaikin Money Flow a décliné en dessous de -30%.
**TRADEX-AI C2** : Indicateur Chaikin Money Flow (CMF) < -30% comme signal de pression vendeuse forte lors d'un breakout baissier — applicable sur GC/CL pour confirmer les breakouts baissiers de triangles.
*Catégorie : volume_liquidite*

### D4004 — Patterns de retournement symétriques : faux breakouts fréquents
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Les patterns de retournement sont particulièrement difficiles à analyser et présentent souvent des faux breakouts.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, lorsqu'un triangle symétrique va à contre-tendance, exiger une confirmation renforcée (filtre temps 3 jours + volume significatif) avant de traiter le breakout comme valide.
*Catégorie : gestion_risque_entree*

### D4005 — Faiblesse du rally de réaction : indicateur de l'amplitude de la baisse suivante
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : La faiblesse du rally de réaction (rebond après la première baisse post-breakout) préfigurait la violence de la baisse qui a suivi.
**TRADEX-AI C1** : Lecture qualitative du rebond post-breakout sur GC/CL — un rebond faible (ne revient pas à l'apex) = signal que la tendance baissière est forte → maintenir/renforcer la position courte.
*Catégorie : gestion_position_active*

### D4006 — Les cibles de prix du triangle sont des guidelines approximatifs, pas des objectifs précis
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : Les cibles de prix potentielles trouvées par mesure et extension de ligne de tendance parallèle sont uniquement destinées à servir de guidelines approximatifs.
**TRADEX-AI C1** : Les cibles de triangle sur GC/HG/CL/ZW sont des zones d'alerte, pas des niveaux exacts — gérer la position activement (C1 Belkhayate) plutôt que de sortir mécaniquement à la cible.
*Catégorie : gestion_position_active*

### D4007 — L'analyse technique est dynamique : surveiller les charts en continu
🟢 **FAIT VÉRIFIÉ** (Source : symmetrical_triangle.md) : L'analyse technique est dynamique, et vous devez surveiller vos graphiques en continu. Dans l'exemple SUNW, le titre a potentiellement atteint sa cible ($42) en quelques mois, mais ne montrait aucun signe de ralentissement et a continué au-dessus de $100 dans les mois suivants.
**TRADEX-AI C1** : Ne pas sortir mécaniquement à la cible théorique sur GC/CL — surveiller les conditions Belkhayate en temps réel (BGC, Direction, Énergie) pour rester en position si la tendance accélère.
*Catégorie : gestion_position_active*
