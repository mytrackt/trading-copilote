# Extraction StockCharts — High Low Bands
**Source :** `bundles/stockcharts/high_low_bands.md` (HTTP 200 · ~4 154 car.) + 1 image certifiée
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 1/1 certifiée
**Décisions :** D2031 → D2039 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/high-low-bands
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | The High Low Bands indicator can identify trend direction, overbought/oversold, support/resistance, volatile conditions. | How Do You Interpret High Low Bands? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2031 — Définition : enveloppe à 3 lignes (haute / médiane / basse)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « The High Low Bands (HLB) indicator helps traders identify and analyze price trends and volatility. It's made up of three lines: an upper band, a middle band, and a lower band. »
**TRADEX-AI C1** : Indicateur d'enveloppe à 3 lignes (bande haute, médiane, basse) servant à lire tendance et volatilité.
*Catégorie : indicateurs_tendance*

---

### D2032 — Base de calcul : moyenne mobile triangulaire (TMA)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « HLB is based on the triangular moving average—a "smoothed" moving average using a particular calculation that gives greater weight to the most recent price data. »
**TRADEX-AI C1** : La médiane = moyenne mobile triangulaire (lissée, poids accru aux données récentes). Implémentable comme overlay sur NT8.
*Catégorie : indicateurs_tendance*

---

### D2033 — Construction : bandes décalées d'un pourcentage paramétrable
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « Three lines are derived from this triangular moving average—one above and one below the original average... The distance between the upper and lower bands from the middle band is adjusted by a specific percentage according to your preference. The StockChartsACP's default HLB percentage is set to 5. »
**TRADEX-AI C1** : Bandes haute/basse = TMA ± X % (défaut 5 % StockChartsACP). Paramètre à figer pour TRADEX-AI lors de l'implémentation.
*Catégorie : configuration*

---

### D2034 — Interprétation : direction de tendance via les touches de bandes
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md, image_01) : « If the price consistently touches or exceeds the upper band, the indicator suggests a strong uptrend. Conversely, if the price persistently touches or falls below the lower band, it indicates a strong downtrend. »
**TRADEX-AI C1** : Prix collant/dépassant la bande haute = uptrend fort ; collant/sous la bande basse = downtrend fort. Entrée tendancielle dans le score /10.
*Catégorie : indicateurs_tendance*

---

### D2035 — Surachat / survente près des bandes
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « Prices near the upper band might indicate an overbought condition. Prices near the lower band might indicate an oversold condition. »
**TRADEX-AI C1** : Prix proche bande haute = surachat possible ; proche bande basse = survente possible. Signal à confirmer (cf. D2036).
*Catégorie : signal*

---

### D2036 — Confirmer surachat/survente avec d'autres indicateurs (RSI, Stochastique)
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « It's best to check these readings with other indicators that interpret potential overbought/oversold readings (such as the Relative Strength Index or the Stochastic Oscillator). »
**TRADEX-AI C2** : Garde-fou : ne pas trader le surachat/survente HLB seul ; croiser avec RSI ou Stochastique. Renforce la règle multi-confirmation.
*Catégorie : signal*

---

### D2037 — Bandes comme support/résistance dynamiques + médiane = mean reversion
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « The upper and lower bands can sometimes serve as dynamic support and resistance levels, with the middle band serving as a mean reversion level toward which prices may gravitate. »
**TRADEX-AI C1** : Bandes haute/basse = S/R dynamiques ; bande médiane = niveau de retour à la moyenne (cible de mean reversion).
*Catégorie : structure_marche*

---

### D2038 — Volatilité : référence visuelle, PAS adaptative comme Bollinger
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md) : « Although the bands don't dynamically adjust to volatility like Bollinger Bands, High Low Bands can still be a visual reference to gauge price volatility. »
**TRADEX-AI C1** : 🔵 ÉCOLE indicateurs. Distinction-clé : contrairement aux Bollinger Bands, les HLB ne s'ajustent PAS dynamiquement à la volatilité (largeur fixée par %). Référence visuelle seulement.
*Catégorie : indicateurs_tendance*

---

### D2039 — Quatre usages combinés de l'indicateur
🟢 **FAIT VÉRIFIÉ** (Source : high_low_bands.md, image_01) : « The High Low Bands indicator can identify trend direction, overbought/oversold conditions, support and resistance levels, and volatile trading conditions. »
**TRADEX-AI C1** : Synthèse des 4 usages : (1) direction de tendance, (2) surachat/survente, (3) support/résistance, (4) conditions de volatilité. Profil fonctionnel de l'overlay.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Décisions | D2031 → D2039 (9 décisions — page courte ~4 154 car., AUCUN padding) |
| Plage allouée | D2031–D2050 (D2040–D2050 NON utilisées, contenu source épuisé) |
| Cercles couverts | C1 (enveloppe / structure prix) |
| Catégories | indicateurs_tendance, configuration, signal, structure_marche |
| Images certifiées | 1/1 |
| Lien Belkhayate | NON CONCERNÉ (enveloppe générique TMA ; à ne pas confondre avec les pivots/BGC Belkhayate) |
| Cas à vérifier | D2038 = 🔵 distinction Bollinger (largeur non adaptative) à retenir avant tout usage volatilité. Paramètre % défaut = 5 (D2033) à figer côté TRADEX-AI. |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Statut BRUT, attend OK utilisateur avant fusion KB.
