# Extraction Optimus — How To Read Stock Market Futures
**Source :** `bundles/optimusfutures/how_to_read_stock_market_futures.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image scrappée · 0/0 certifiées · 0 à vérifier
**Décisions :** D8491 → D8510 · **Page :** https://optimusfutures.com/blog/how-to-read-stock-market-futures/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Lecture des 3 futures d'indice (ES/NQ/YM) comme proxy de sentiment macro avant l'ouverture — alimente C4 Macro et C7 Corrélations.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image scrappée) | — | — | — |

## DÉCISIONS

### D8491 — Futures d'indice : sources de sentiment pré-ouverture
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Les futures d'indice (ES, NQ, YM) tradent quasi-24h/5j et reflètent la réaction des marchés mondiaux aux news overnight avant que le cash market n'ouvre à 9h30 ET.
**TRADEX-AI C4** : Surveiller ES/NQ/YM pré-marché enrichit le contexte macro (C4) et signale le biais directionnel avant toute analyse Belkhayate.
*Catégorie : macro_evenements*

### D8492 — Triple lecture ES+NQ+YM pour diagnostiquer la breadth
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Lire les 3 contrats ensemble donne une image complète. Si ES+NQ+YM montent tous → force large marché (breadth large). Si NQ fort + YM plat → tech leadership. Si ES stable + NQ faible → rotation hors de la croissance.
**TRADEX-AI C7** : Ce diagnostic breadth est une lecture de corrélations inter-contrats (C7) applicable avant chaque session de trading sur GC/CL/HG/ZW.
*Catégorie : correlations*

### D8493 — ES = baromètre primaire de la direction marché
🔵 **ÉCOLE** (Source : how_to_read_stock_market_futures.md) : Le contrat ES (E-mini S&P 500) est le baromètre standard car il couvre 500 entreprises sur tous secteurs ; c'est lui qu'on lit en premier pour le biais risk-on / risk-off.
**TRADEX-AI C4** : Dans TRADEX, ES est l'actif de confirmation primaire (catégorie CONFIRMATION). Sa direction pré-marché oriente le filtre macro avant de calculer le score /10.
*Catégorie : structure_marche*

### D8494 — Alignement des 3 contrats = signal de conviction plus fort
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Quand les 3 contrats bougent dans le même sens, la conviction est plus forte. Une divergence (un monte, l'autre stagne ou recule) signale une nuance : rotation, hésitation ou message sectoriel.
**TRADEX-AI C7** : Règle de corrélation directe : si ES/NQ/YM tous alignés → poids macro fort dans le score global. Si divergence → réduire le poids de la confirmation C4 dans le signal.
*Catégorie : correlations*

### D8495 — Catalyseurs overnight à vérifier avant d'interpréter le move
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Avant d'interpréter un move pré-ouverture, vérifier les catalyseurs : données économiques, earnings, discours Fed, mouvements des marchés asiatiques/européens. Un fort move overnight peut se retourner après une publication 8h30 ET.
**TRADEX-AI C4** : Correspond à la sécurité News Gate de TRADEX. Un fort move overnight sur ES doit être mis en contexte avec le calendrier macro (NFP/FOMC/CPI) avant validation du signal.
*Catégorie : macro_evenements*

### D8496 — Fair Value : l'open implicite n'est pas le raw futures price
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : L'open implicite est déterminé par l'écart entre le prix futures et la Fair Value (prix spot + coût de portage – dividendes). Si les futures montent de +10 pts mais que la FV en implique +15 pts, le marché peut ouvrir plus faiblement que le titre green ne le suggère. C'est pourquoi on voit parfois "futures verts, ouverture rouge".
**TRADEX-AI C4** : Concept de Fair Value du cash market (différent du FVG chart). Pour les matières premières (GC/CL), un mécanisme analogue existe entre futures et spot ; à documenter dans le contexte GC backwardation/contango.
*Catégorie : indicateurs_tendance*

### D8497 — Routine pré-marché en 5 étapes
🔵 **ÉCOLE** (Source : how_to_read_stock_market_futures.md) : Routine standardisée : (1) direction ES, (2) comparer NQ vs YM, (3) chercher alignement ou divergence, (4) vérifier les catalyseurs overnight, (5) évaluer l'open implicite. Ne pas s'arrêter au seul chiffre de headline.
**TRADEX-AI C4** : Cette routine peut être intégrée dans le module de contexte macro de TRADEX — exécutée automatiquement par le Python Engine avant l'appel Claude API (Niveau 2 du pipeline).
*Catégorie : configuration*

### D8498 — Move violent pré-marché = réfléchir au sizing
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Un large move overnight (ex. ES -1% à -2%) signale une volatilité élevée à l'ouverture. Les traders expérimentés ajustent le sizing de position ou le timing d'entrée en conséquence. L'accord ou le désaccord des traders US dès la cloche peut déclencher une forte réaction.
**TRADEX-AI C5** : Corrèle avec la logique VIX de TRADEX. Une forte chute overnight ES (move >1%) doit activer un filtre de volatilité similaire au seuil VIX critique.
*Catégorie : gestion_risque_entree*

### D8499 — Futures pré-marché = contexte, pas prédiction
🟢 **FAIT VÉRIFIÉ** (Source : how_to_read_stock_market_futures.md) : Les futures pré-ouverture sont une indication de sentiment, pas une prédiction fiable. Le marché peut s'inverser dès l'ouverture quand la liquidité US entre en jeu. Les traiter comme "contexte" et non comme un signal de trading en soi.
**TRADEX-AI C4** : Règle de garde-fou : le biais macro ES pré-marché est une entrée du score /10 mais ne suffit jamais à déclencher un ordre seul. Nécessite validation multi-cercles.
*Catégorie : psychologie*

### D8500 — Divergence NQ/YM : signal de rotation sectorielle
🟡 **SYNTHÈSE** (Source : how_to_read_stock_market_futures.md) : Dow fort + Nasdaq faible = rotation vers les valeurs industrielles/blue chip. Nasdaq fort + Dow faible = leadership technologique. Cette rotation peut affecter les actifs de matières premières (GC, CL) via les flux de capitaux.
**TRADEX-AI C7** : En TRADEX, si YM surperforme NQ, surveiller si les flux se dirigent vers les actifs réels (GC/CL haussiers). À intégrer dans la matrice de corrélations C7.
*Catégorie : correlations*
