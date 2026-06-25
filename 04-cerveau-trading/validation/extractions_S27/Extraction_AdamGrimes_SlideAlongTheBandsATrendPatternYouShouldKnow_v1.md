# Extraction AdamGrimes — Slide Along The Bands A Trend Pattern You Should Know
**Source :** `bundles/adamgrimes/slide_along_the_bands_a_trend_pattern_you_should_know.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées · 0 à vérifier
**Décisions :** D6631 → D6646 · **Page :** https://www.adamhgrimes.com/slide-along-the-bands-a-trend-pattern-you-should-know/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Pattern « slide along the bands » — tendance basse volatilité qui se prolonge sans pullback, applicable à GC/CL/ZW via bandes Keltner.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6631 — Slide along the bands : définition du pattern
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : « Slide along the bands » est un pattern de tendance à basse volatilité caractérisé par : (1) contraction des ranges quotidiens, (2) absence ou quasi-absence de pullbacks contre la tendance, (3) extension bien au-delà de ce qu'on attendrait, (4) positionnement unilatéral de la majorité des participants.
**TRADEX-AI C1** : Détecter ce pattern sur GC/CL via bandes Keltner (2.25 ATR autour d'une EMA 20) : si le prix reste collé à la bande pendant ≥ 5 barres sans retracer de plus de 0.5 ATR, le moteur Python doit taguer l'actif « SLIDE_PATTERN_ACTIF ».
*Catégorie : indicateurs_tendance*

### D6632 — Gestion d'une position dans le bon sens : trailing stop simple
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : Quand on est du bon côté d'un slide pattern, la seule action correcte est de traîner un stop. On ne sait ni jusqu'où ni combien de temps la tendance ira. Chercher à sortir activement est une erreur : laisser le marché décider en touchant le stop.
**TRADEX-AI C1** : Règle de gestion active : si SLIDE_PATTERN_ACTIF = True, le signal TRADEX doit afficher « Trailing stop uniquement — ne pas chercher de sortie active » et interdire tout signal ATTENDRE intermédiaire basé sur un retournement mineur.
*Catégorie : gestion_position_active*

### D6633 — Gestion du mauvais côté d'un slide pattern
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : Être du mauvais côté d'un slide pattern est particulièrement destructeur : le marché grinde contra pendant des semaines ou des mois. Identifier ce pattern avant d'entrer permet d'éviter de se retrouver dans cette situation.
**TRADEX-AI C1** : Règle de filtrage d'entrée : si SLIDE_PATTERN_ACTIF = True dans la direction opposée au signal envisagé, le signal est automatiquement reclassé ATTENDRE quelle que soit la note /10.
*Catégorie : gestion_risque_entree*

### D6634 — Pas de pullback = pas d'entrée en cours de tendance
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : Un slide pattern ne produit pas de pullbacks utilisables pour entrer. Essayer d'entrer dans cette configuration est difficile ; il est souvent préférable de passer et d'attendre un autre trade. Quand un pullback arrive enfin, il peut se transformer en effondrement complet.
**TRADEX-AI C1** : Si SLIDE_PATTERN_ACTIF = True, le moteur Python bloque les signaux d'entrée « pullback vers EMA » et logue « SLIDE_NO_ENTRY — attendre rupture de pattern ».
*Catégorie : configuration*

### D6635 — Fin violente du slide pattern
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : Quand un slide pattern se termine, il se termine souvent violemment avec un spike contre la tendance. Les participants piégés du mauvais côté capitulent en masse. Respecter ses stops est impératif.
**TRADEX-AI C2** : Surveiller dans l'order flow (ATAS) une accélération soudaine du delta contra-tendance ≥ 2× la moyenne des 10 dernières barres comme signal d'alerte de fin de slide pattern.
*Catégorie : volume_liquidite*

### D6636 — Bandes Keltner : outil de calibrage de la structure
🟢 **FAIT VÉRIFIÉ** (Source : slide_along_the_bands_a_trend_pattern_you_should_know.md) : L'auteur utilise des canaux calibrés à ±2.25 ATR autour d'une EMA 20 périodes. Ces bandes structurent la lecture visuelle du marché et permettent de reconnaître le slide pattern. L'EMA 20 seule n'a pas de tendance statistique forte mais elle entraîne l'œil à voir correctement.
**TRADEX-AI C1** : Paramètre Keltner verrouillé pour la détection SLIDE dans TRADEX : EMA 20 barres (range bars NT8), bandes ±2.25 ATR. Ces valeurs ne doivent pas être modifiées sans backtest validé sur GC et CL.
*Catégorie : indicateurs_tendance*
