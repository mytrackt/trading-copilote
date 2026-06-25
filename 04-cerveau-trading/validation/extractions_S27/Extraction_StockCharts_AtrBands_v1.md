# Extraction StockCharts — ATR Bands
**Source :** `bundles/stockcharts/atr_bands.md` (HTTP 200 · ~2 100 car.) + 0 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 0/0 certifiées (page sans figure)
**Décisions :** D751 → D757 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/atr-bands
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée (manifest : .md=0 figures vs HTML=0 images — page purement textuelle).

## DÉCISIONS

### D751 — Nature : indicateur de volatilité bâti sur l'ATR de Wilder
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « ATR Bands are a volatility-based indicator that plots bands above and below a moving average of the underlying price. » Étendant le concept d'Average True Range (ATR) développé par J. Welles Wilder, les ATR Bands créent une représentation visuelle de la volatilité autour du prix et de sa moyenne mobile centrale.
**TRADEX-AI C1** : Indicateur de volatilité dérivé de l'ATR (bandes = MM centrale ± multiple d'ATR) ; brique analytique de mesure de volatilité, jamais déclencheur d'ordre.
*Catégorie : indicateurs_momentum*

---

### D752 — Usage 1 : évaluer la volatilité et adapter sa stratégie
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « Most traders use ATR Bands to gauge market volatility. By visually projecting volatility thresholds around a stock's prices, the bands can help you assess the current market environment, which, in turn, can help you adjust your strategies accordingly. »
**TRADEX-AI C1** : Lecture de l'environnement de volatilité courant comme contexte d'adaptation (taille, distance de stop) ; feature de régime de volatilité.
*Catégorie : structure_marche*

---

### D753 — Usage 2 : placer stop-loss à un multiple d'ATR sous l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « By placing stop-loss orders a certain multiple of the ATR below the entry price, you can give your trades enough room to fluctuate without being prematurely stopped out. »
**TRADEX-AI C7** : Stop-loss = prix d'entrée − (k × ATR), règle déterministe directement codable pour dimensionner la distance de stop selon la volatilité réelle.
*Catégorie : gestion_risque_entree*

---

### D754 — Usage 2bis : take-profit à un multiple d'ATR au-dessus de l'entrée
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « Similarly, take-profit levels can be set using a multiple of the ATR above the entry price to align profit targets with market volatility. »
**TRADEX-AI C7** : Take-profit = prix d'entrée + (m × ATR) ; couplé au stop ATR, permet de calculer un R/R volatilité-ajusté (cohérent avec le seuil R/R ≥ 1:2).
*Catégorie : gestion_risque_entree*

---

### D755 — Usage 3 : dimensionnement de position selon l'ATR
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « By assessing the ATR value, you can determine the appropriate trade size relative to the volatility of the asset. Higher volatility (indicated by a higher ATR) might suggest smaller position sizes to manage risk, while lower volatility might allow for larger positions. »
**TRADEX-AI C7** : Position sizing inverse à la volatilité (ATR↑ → taille↓) ; logique de risque constant transposable en module de sizing.
*Catégorie : gestion_risque_entree*

---

### D756 — Usage 4 : combiner ATR Bands avec d'autres indicateurs (RSI, moyennes mobiles)
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « Combining ATR Bands with the Relative Strength Index (RSI) can help you identify overbought or oversold conditions. Using ATR Bands with moving averages might give you a clearer picture of trend direction and volatility. »
**TRADEX-AI C1** : Les ATR Bands sont une couche de confluence (volatilité) à coupler à momentum/tendance, jamais un signal isolé.
*Catégorie : signal*

---

### D757 — Mise en garde : usages multiples, non exhaustifs et à personnaliser
🟢 **FAIT VÉRIFIÉ** (Source : atr_bands.md) : « These are just a few ways to use ATR Bands. You can explore numerous other methods and combinations to develop a trading approach that's more tailored to your preferences. » La source liste des idées d'usage (volatilité, stops/TP, sizing, combinaison) sans prescrire de paramètres chiffrés (multiple d'ATR, période, type de MM non spécifiés sur cette page).
**TRADEX-AI C1** : Aucun paramètre numérique fourni par la source ; toute valeur de multiple/période devra être définie ailleurs (page ATR dédiée) et validée avant codage.
*Catégorie : indicateurs_momentum*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D751 | Indicateur de volatilité basé sur l'ATR (Wilder) | 🟢 | C1 | indicateurs_momentum |
| D752 | Évaluer la volatilité / adapter la stratégie | 🟢 | C1 | structure_marche |
| D753 | Stop-loss = entrée − k×ATR | 🟢 | C7 | gestion_risque_entree |
| D754 | Take-profit = entrée + m×ATR | 🟢 | C7 | gestion_risque_entree |
| D755 | Position sizing inverse à l'ATR | 🟢 | C7 | gestion_risque_entree |
| D756 | Combiner avec RSI / moyennes mobiles | 🟢 | C1 | signal |
| D757 | Usages non exhaustifs, aucun paramètre chiffré | 🟢 | C1 | indicateurs_momentum |

**Liens Belkhayate :** Les ATR Bands ne sont PAS un indicateur Belkhayate (⚫). À noter : la mémoire projet indique que l'« Énergie » Belkhayate = MFI (Money Flow Index), et qu'un arbitrage MFI vs proxy ATR reste NON tranché (formule Énergie non codée). L'ATR pourrait servir de proxy de volatilité dans cet arbitrage — mais l'affirmer comme composant Belkhayate serait « hypothèse projet, non affirmée par la source » (⚫🔴). Cette page StockCharts ne parle PAS de Belkhayate. Usage TRADEX privilégié : stops/TP/sizing volatilité-ajustés (gestion du risque), pas l'Énergie.

**À vérifier (humain) :**
- D753/D754/D755 — la source ne donne AUCUN multiple d'ATR ni période de MM chiffrés ; les valeurs (k, m, période) restent à définir et valider (probablement sur la page ATR dédiée, hors de ce bundle).
- Lien ATR ↔ « Énergie/proxy ATR » Belkhayate : arbitrage MFI vs ATR explicitement NON tranché dans la mémoire projet — ne rien coder sans décision humaine.
- Page sans aucune image (0/0) — rien à certifier côté visuel.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
