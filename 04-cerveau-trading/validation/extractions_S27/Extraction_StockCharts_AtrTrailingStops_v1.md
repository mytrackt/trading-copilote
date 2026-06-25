# Extraction StockCharts — ATR Trailing Stops
**Source :** `bundles/stockcharts/atr_trailing_stops.md` (HTTP 200 · ~4 700 car.) + 0 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 0/0 certifiées
**Décisions :** D771 → D778 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-trailing-stops
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (manifest : .md=0 figures vs HTML=0 images — alignement impossible, à vérifier manuellement).

## DÉCISIONS

### D771 — Nature de l'indicateur ATR Trailing Stops
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : L'ATR Trailing Stop est un indicateur basé sur la volatilité qui fixe des niveaux de stop-loss dynamiques pour les sorties (ou entrées) de marché. Il utilise l'Average True Range (ATR), une mesure de la volatilité du marché, pour déterminer où placer les stops suiveurs. Il aide à gérer le risque (ou identifier des points d'entrée) en ajustant dynamiquement les niveaux de stop aux conditions de marché changeantes.
**TRADEX-AI C1** : Mécanisme de stop dynamique adossé à la volatilité ; candidat direct pour la gestion de risque (placement de stops) sur GC/HG/CL/ZW, jamais comme déclencheur autonome d'ordre.
*Catégorie : gestion_risque_entree*

---

### D772 — Étape 1 du calcul : ATR (période 21 par défaut sur ACP)
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : Le calcul commence par l'ATR, qui est une moyenne mobile des True Ranges sur une période donnée. Sur la plateforme StockChartsACP, l'ATR est réglé à **21 jours** par défaut.
**TRADEX-AI C1** : Paramètre ATR(21) à reparamétrer selon le timeframe Belkhayate (15min / Range Bar) ; valeur par défaut propre à la plateforme ACP, non universelle.
*Catégorie : gestion_risque_entree*

---

### D773 — Étape 2 : choix du multiplicateur (défaut 3)
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : Un multiplicateur ajuste la distance du stop suiveur par rapport au prix. Le choix (2x, 3x, ou plus) dépend de la volatilité anticipée et de l'agressivité de la gestion de risque. Sur StockChartsACP, le multiplicateur est réglé par défaut à **3**.
**TRADEX-AI C1** : Paramètre multiplicateur k (défaut 3) à calibrer ; distance stop = k × ATR. Variable de sensibilité du risque, à figer par backtest sur les actifs tradables.
*Catégorie : gestion_risque_entree*

---

### D774 — Étape 3 : formules du stop suiveur (long / short)
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : Calcul du stop suiveur :
* **Position longue.** Soustraire le produit (ATR × multiplicateur) du plus haut prix → niveau de stop-loss pour un long.
* **Position courte.** Ajouter le produit (ATR × multiplicateur) au plus bas prix → niveau de stop-loss pour un short.
`Stop long = Plus haut − (ATR × multiplicateur)`
`Stop short = Plus bas + (ATR × multiplicateur)`
**TRADEX-AI C1** : Formules déterministes implémentables telles quelles ; fournissent un niveau de stop chiffré exploitable en gestion de position.
*Catégorie : gestion_risque_entree*

---

### D775 — Étape 4 : mise à jour unidirectionnelle du stop
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : Le stop suiveur n'est ajusté que dans le sens de la tendance. Pour un long, le niveau de stop **augmente** si le prix fait de nouveaux plus hauts. Pour un short, le niveau de stop **diminue** si le prix fait de nouveaux plus bas. (Le stop ne recule jamais contre la tendance.)
**TRADEX-AI C1** : Règle de cliquet (ratchet) codable : `stop_long = max(stop_long_prec, nouveau_calcul)` ; `stop_short = min(...)`. Garantit que le stop ne se desserre jamais.
*Catégorie : gestion_risque_entree*

---

### D776 — Interprétation : identification de tendance
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : L'ATR Trailing Stops sert d'outil d'identification de tendance. Si la ligne est **sous** le prix → marché en uptrend. Si la ligne est **au-dessus** du prix → marché en downtrend.
**TRADEX-AI C1** : Lecture binaire de tendance (position prix vs ligne) utilisable comme filtre de cohérence avec la Direction Belkhayate ; rôle de confirmation, pas de déclencheur.
*Catégorie : indicateurs_tendance*

---

### D777 — Points de sortie (usage principal)
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : L'usage le plus courant est de fixer des stops de sortie. Pour un long, on sort quand le prix passe **sous** la ligne ATR. Pour un short, le signal de sortie est quand le prix passe **au-dessus** de la ligne ATR. Cela protège les profits en laissant courir les positions en conditions favorables et en les clôturant lors d'un retournement.
**TRADEX-AI C1** : Logique de sortie sur croisement prix/ligne ATR ; cœur de la gestion de risque de sortie, transposable en règle de clôture protectrice.
*Catégorie : gestion_risque_entree*

---

### D778 — Points d'entrée (usage secondaire, trend-following)
🟢 **FAIT VÉRIFIÉ** (Source : atr_trailing_stops.md) : Bien que principalement utilisé pour les sorties, l'ATR Trailing Stops peut servir de signal d'entrée en stratégie suiveuse de tendance : entrer en long quand le prix passe **au-dessus** du stop suiveur, et en short quand le prix passe **en dessous**.
**TRADEX-AI C1** : Usage entrée mentionné mais secondaire ; à traiter comme couche analytique de confirmation, jamais comme déclencheur autonome (mode Auto bloqué par défaut).
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D771 | Nature ATR Trailing Stops | 🟢 | C1 | gestion_risque_entree |
| D772 | Étape 1 : ATR(21) défaut ACP | 🟢 | C1 | gestion_risque_entree |
| D773 | Étape 2 : multiplicateur (défaut 3) | 🟢 | C1 | gestion_risque_entree |
| D774 | Étape 3 : formules stop long/short | 🟢 | C1 | gestion_risque_entree |
| D775 | Étape 4 : mise à jour unidirectionnelle | 🟢 | C1 | gestion_risque_entree |
| D776 | Identification de tendance | 🟢 | C1 | indicateurs_tendance |
| D777 | Points de sortie (usage principal) | 🟢 | C1 | gestion_risque_entree |
| D778 | Points d'entrée (trend-following) | 🟢 | C1 | signal |

**Liens Belkhayate :** ⚫🔴 L'ATR Trailing Stops n'est PAS un indicateur Belkhayate. Lien indirect : c'est un mécanisme de stop dynamique basé sur la volatilité (ATR/True Range, Wilder), exploitable pour la gestion de risque/placement de stops dans TRADEX-AI, sans aucune assise dans la méthode Belkhayate elle-même. Ne rien inventer sur un lien méthodologique.

**À vérifier (humain) :**
- Manifest images : 0 figure .md vs 0 image HTML, alignement « impossible » → aucune image extraite ; rien à valider côté visuel, mais noté pour traçabilité.
- D772/D773 — les paramètres 21 et 3 sont les **défauts StockChartsACP**, non des constantes universelles ; à recalibrer par backtest sur GC/HG/CL/ZW avant tout codage en dur.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
