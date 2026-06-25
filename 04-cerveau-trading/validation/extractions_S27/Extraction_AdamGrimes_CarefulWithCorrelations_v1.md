# Extraction AdamGrimes — Careful With Correlations
**Source :** `bundles/adamgrimes/careful_with_correlations.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D5391 → D5397 · **Page :** https://www.adamhgrimes.com/careful-with-correlations/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : La corrélation ne peut pas être lue visuellement sur un chart — la matrice de corrélations C7 de TRADEX-AI doit être calculée mathématiquement, jamais inférée visuellement.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D5391 — La corrélation ne se lit PAS sur un chart
🟢 **FAIT VÉRIFIÉ** (Source : careful_with_correlations.md) : Deux séries temporelles qui semblent visuellement très similaires (elles montent toutes les deux) peuvent avoir une corrélation de -1.0. Exemple démontré par Grimes : série ABC (+1.5%/-0.5% alternant) et série XYZ (même pattern décalé d'1 jour) — les deux montent sur le long terme mais ont une corrélation exactement de -1.0 car elles bougent toujours en directions opposées jour par jour.
**TRADEX-AI C7** : La matrice de corrélations live 30 jours de TRADEX-AI (correlations.py) DOIT calculer la corrélation des RENDEMENTS JOURNALIERS (delta de prix), jamais la corrélation des niveaux de prix. Utiliser df.pct_change() avant df.corr(). Une corrélation calculée sur les niveaux de prix est mathématiquement incorrecte et peut produire des résultats inverses à la réalité.
*Catégorie : correlations*

### D5392 — La corrélation mesure la co-direction journalière, pas la co-tendance
🟢 **FAIT VÉRIFIÉ** (Source : careful_with_correlations.md) : La corrélation est la mesure dans quelle mesure deux séries se déplacent dans la MÊME DIRECTION au MÊME MOMENT, pas la mesure dans laquelle elles partagent la même tendance de long terme. Deux actifs peuvent monter ensemble sur 6 mois (corrélation des niveaux proche de 1.0) mais avoir des mouvements journaliers totalement décorrélés ou inversement corrélés.
**TRADEX-AI C7** : Règle KB pour le cercle C7 (Corrélations) : toujours préciser l'horizon temporel de la corrélation. Une corrélation de 0.8 entre GC et HG sur 30 jours glissants ne signifie pas qu'ils montent ensemble chaque jour — elle signifie que leurs rendements journaliers sont co-directionnels dans 90% des cas. Cette nuance est critique pour l'interprétation des signaux inter-marchés.
*Catégorie : correlations*

### D5393 — Le décalage temporel (offset) peut inverser la corrélation
🟢 **FAIT VÉRIFIÉ** (Source : careful_with_correlations.md) : Un décalage d'une seule période peut transformer une corrélation de +1.0 en -1.0 si les séries alternent. Ce principe s'applique aux marchés réels : deux actifs peuvent montrer une corrélation positive avec un décalage de 0 jours et une corrélation négative avec un décalage de 1 jour (lead-lag relationship).
**TRADEX-AI C7** : La matrice de corrélations TRADEX-AI doit calculer non seulement la corrélation simultanée (lag=0) mais aussi les corrélations avec décalage lag=1 et lag=-1 entre les actifs de CONFIRMATION (DX, ES, VX) et les actifs TRADING (GC, HG, CL, ZW). Un lead-lag confirmé est plus valuable qu'une corrélation instantanée.
*Catégorie : correlations*

### D5394 — La précision conceptuelle est obligatoire en trading
🔵 **ÉCOLE** (Source : careful_with_correlations.md) : Grimes établit comme thème récurrent : "soyez précis". Utiliser des concepts de manière approximative en assumant que "proche c'est assez bien" conduit à des erreurs systématiques. La corrélation est l'exemple type : la compréhension simpliste ("ils bougent ensemble") est souvent fausse dans les cas pratiques importants.
**TRADEX-AI C1** : La KB TRADEX-AI doit définir précisément chaque concept utilisé dans la grille /10. "Corrélation positive entre GC et HG" doit être défini comme : corrélation de Pearson sur rendements log journaliers sur fenêtre de 30 jours glissants, calculée dans correlations.py. Les définitions vagues sont des sources d'erreurs de signal.
*Catégorie : correlations*

### D5395 — L'erreur de corrélation visuelle est quasi universelle
🟢 **FAIT VÉRIFIÉ** (Source : careful_with_correlations.md) : Grimes a publié sur Twitter un chart avec corrélation -1.0 qui "semblait" avoir corrélation +1.0, et a reçu une "déluges" de réponses corrigeant ce qu'ils pensaient être son erreur — aucun d'eux ne l'a cru. Cela démontre que l'erreur de lire la corrélation visuellement est quasi universelle, même chez des traders expérimentés.
**TRADEX-AI C7** : Les alertes de corrélation affichées dans le dashboard TRADEX-AI doivent toujours montrer la valeur numérique calculée, jamais une évaluation visuelle. Afficher "GC/HG corrélation : +0.73 (30J)" et non "GC et HG se déplacent ensemble". Les traders (Abdelkrim inclus) ont une tendance naturelle à surévaluer la corrélation visuelle.
*Catégorie : correlations*

### D5396 — Les études de corrélation "par zones visuelles" sont non fiables
🟢 **FAIT VÉRIFIÉ** (Source : careful_with_correlations.md) : Dans la littérature trading, de nombreux auteurs identifient des zones de "corrélation augmentée" en pointant des sections de chart où les lignes bougent dans la même direction. Grimes note : "peut-être ; peut-être pas" — on ne peut pas conclure d'une zone visuelle de co-mouvement que la corrélation était élevée dans cette zone.
**TRADEX-AI C7** : Règle d'audit KB : toute règle dans KNOWLEDGE_BASE_MASTER.json mentionnant une corrélation entre actifs DOIT citer une valeur numérique calculée ou être étiquetée ⚠️ CORRELATION_NON_VERIFIEE. Les règles de type "GC et DX bougent typiquement en sens inverse" sans valeur de corrélation calculée sont des règles de niveau 2 (observation qualitative), pas des règles de niveau 1 (fait vérifié).
*Catégorie : correlations*

### D5397 — Corrélation entre niveau de prix et rendements : deux mesures différentes
🟡 **SYNTHÈSE** (Source : careful_with_correlations.md) : L'article illustre implicitement que calculer la corrélation sur les niveaux de prix (series ABC et XYZ qui montent toutes les deux) versus sur les rendements journaliers (delta) donne des résultats radicalement différents. Les deux actifs ont des niveaux corrélés positivement mais des rendements corrélés négativement (-1.0). C'est la source principale d'erreur dans les études de corrélation inter-marchés.
**TRADEX-AI C7** : Standard technique obligatoire dans correlations.py : la matrice de corrélations TRADEX-AI utilise exclusivement les rendements log (numpy.log(price/price.shift(1))) sur fenêtre de 30 jours. Toute corrélation calculée sur les niveaux de prix bruts est à rejeter. Documenter ce standard dans le header du fichier correlations.py.
*Catégorie : correlations*
