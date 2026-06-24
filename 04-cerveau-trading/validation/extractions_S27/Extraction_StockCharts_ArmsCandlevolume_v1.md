# Extraction StockCharts — Arms CandleVolume
**Source :** `bundles/stockcharts/arms_candlevolume.md` (HTTP 200 · ~6 500 car.) + 11 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D611 → D621 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/arms-candlevolume
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Three types of EquiVolume boxes. | EquiVolume Overview | CERTIFIE |
| image_02.png | Note the wide Arms CandleVolume boxes in October compared to lower volume narrower boxes (Nov/Déc) | EquiVolume Overview | CERTIFIE |
| image_03.png | Price chart using standard candlesticks. | EquiVolume Overview | CERTIFIE |
| image_04.png | Colored standard candlestick bars — 4 variations (black-filled, black-hollow, red-filled, red-hollow) | Candlestick Overview | CERTIFIE |
| image_05.png | Standard Candlestick chart. | Arms CandleVolume | CERTIFIE |
| image_06.png | EquiVolume Chart of Intel Corp. (INTC). | Arms CandleVolume | CERTIFIE |
| image_07.png | An Arms CandleVolume chart combines EquiVolume and candlestick charts. | Arms CandleVolume | CERTIFIE |
| image_08.png | Arms CandleVolume chart shows a high volume day on October 9. | Interpretation | CERTIFIE |
| image_09.png | Gap + wide CandleVolume box Sept. 5 ; bearish engulfing high volume mid-Sept peak. | Interpretation | CERTIFIE |
| image_10.png | Arms CandleVolume in SharpCharts | Arms CandleVolume in SharpCharts | CERTIFIE |
| image_11.png | Customizing colors for CandleVolume boxes in SharpCharts. | Arms CandleVolume in SharpCharts | CERTIFIE |

## DÉCISIONS

### D611 — Définition Arms CandleVolume
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md) : « Arms CandleVolume charts merge candlesticks and EquiVolume to create a price chart that focuses on volume, the price range, and the candlestick. » Le type combine le chandelier (open/close, high-low) avec la boîte EquiVolume de Richard Arms (créateur de l'Arms Index/TRIN).
**TRADEX-AI C2** : Type de graphique fusionnant prix et volume sur l'axe horizontal — outil de lecture du couple structure-volume, alimente C2 (order flow / volume) en complément du chandelier C1.
*Catégorie : structure_marche*
---

### D612 — Construction de la boîte EquiVolume (3 composants)
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_01) : « An EquiVolume box consists of three components—price high, price low, and volume. The price high forms the upper boundary, the price low forms the lower boundary, and volume dictates the width. » La hauteur = range high-low, la largeur = volume.
**TRADEX-AI C2** : Le volume est encodé en largeur géométrique (pas en barre séparée) — permet de juger d'un coup d'œil l'importance relative d'une séance.
*Catégorie : structure_marche*
---

### D613 — Couleur de la boîte EquiVolume (close vs close précédent)
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_01) : « EquiVolume boxes are black when the close is above the prior close and red when the close is below the prior close. »
**TRADEX-AI C1** : La couleur de boîte code la direction inter-séance (close vs close veille), distincte de la dynamique intra-séance open→close du chandelier.
*Catégorie : signal*
---

### D614 — Normalisation du volume en % de la période de lookback
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md) : « volume is normalized to show it as a percentage of the lookback period. For a four-month daily chart, each day's volume would be divided by the total volume for those four months. (…) High-volume days occupy more space on the X-axis than low-volume days. »
**TRADEX-AI C2** : Largeur = part du volume total de la fenêtre → métrique relative dépendante de la période choisie ; à fixer explicitement (ex. fenêtre 30j) avant toute comparaison.
*Catégorie : structure_marche*
---

### D615 — Axe des dates non uniforme
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_02) : « The varying width means the date axis will not be uniform. Some weeks will extend longer because of high volume, while others will be shorter because of low volume. » Exemple IPG : octobre s'étire (boîtes larges) vs novembre/décembre (boîtes étroites).
**TRADEX-AI C2** : L'axe temporel est déformé par le volume — toute logique algorithmique de comptage de barres/dates doit en tenir compte (le temps « calendaire » n'est pas l'axe affiché).
*Catégorie : structure_marche*
---

### D616 — Couleur du chandelier intégré (close vs close précédent)
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_04) : « The price change from the close to the prior close determines the candlestick color. Candlesticks are black when the close is higher and red when the close is lower. »
**TRADEX-AI C1** : Convention de couleur du chandelier (noir = hausse vs veille, rouge = baisse) — alignée sur celle de la boîte EquiVolume.
*Catégorie : configuration*
---

### D617 — Corps plein vs creux (close vs open)
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_04) : « The price movement from open to close determines whether a candlestick is hollow or filled. The candlestick is hollow when the close is above the open and filled (solid) when the close is below the open. » 4 variations : black-filled, black-hollow, red-filled, red-hollow.
**TRADEX-AI C1** : Deux dimensions distinctes lues simultanément — couleur (inter-séance) ET remplissage (intra-séance open→close) ; mêmes shadows que la boîte pour le range.
*Catégorie : configuration*
---

### D618 — Usage : valider les patterns de retournement chandelier par le volume
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_08) : « Chartists can use Arms CandleVolume charts to find candlestick reversal patterns and analyze volume flows to complement these patterns. » Exemple COST : bullish engulfing à fort volume le 9 octobre — chandelier long ET large car volume au plus haut sur 2 mois ; « Volume validates the bullish engulfing pattern and affirms support. »
**TRADEX-AI C1+C2** : Fonction première = confirmer une figure de retournement par la largeur (volume) de la boîte ; un engulfing à boîte large pèse plus qu'à boîte étroite.
*Catégorie : signal*
---

### D619 — Largeur de boîte non finalisée avant clôture
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_09) : « the true width of Arms CandleVolume boxes is shown when the chart ends on that particular date. (…) The width of this box is not finalized until after the market close on September 5. » Exemple : gap + boîte large COST le 5 septembre.
**TRADEX-AI C2** : La largeur (donc le signal de force) n'est fiable qu'à la clôture de la séance — pas exploitable en intra-séance comme valeur définitive (garde-fou anti-signal prématuré).
*Catégorie : signal*
---

### D620 — Largeur de boîte comme validateur de support/résistance
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md) : « Wide Arms CandleVolume boxes can also be used to affirm a support level or validate resistance. A bounce off support with a wide Arms CandleVolume box is stronger than a bounce with a narrow Arms CandleVolume box. The same is true for a decline from resistance. »
**TRADEX-AI C2** : Règle de pondération — un rebond/rejet sur niveau confirmé par une boîte large (fort volume) est plus fiable qu'avec une boîte étroite ; transposable à la pondération du score d'un signal sur support/résistance.
*Catégorie : signal*
---

### D621 — Paramétrage SharpCharts (réglages volume et couleurs)
🟢 **FAIT VÉRIFIÉ** (Source : arms_candlevolume.md, image_10, image_11) : Arms CandleVolume se règle via **Chart Type** dans **Attributes**. Le volume peut être off / separate / overlay, et « can also be skipped (off) because it is reflected on the Arms CandleVolume chart ». Option **Color Volume** + **Up Color / Down Color** pour personnaliser barres de prix et volume.
**TRADEX-AI C2** : Détail outillage tiers (StockCharts) — non directement implémentable côté TRADEX-AI (plateforme = NT8/ATAS), conservé pour référence de configuration.
*Catégorie : structure_marche*
---

## SYNTHÈSE

| Thème | Apport pour TRADEX-AI | Cercle | Tag |
|-------|------------------------|--------|-----|
| Type de graphique | Fusion chandelier + volume (largeur = volume) | C2 | 🟢 |
| Construction boîte | high/low = hauteur, volume = largeur, normalisé %lookback | C2 | 🟢 |
| Codage couleur/remplissage | couleur = close vs veille ; remplissage = close vs open | C1 | 🟢 |
| Axe déformé | temps affiché ≠ temps calendaire (déformé par volume) | C2 | 🟢 |
| Validation patterns | boîte large valide engulfing / retournement | C1+C2 | 🟢 |
| Largeur ≠ finalisée intra-séance | fiable seulement à la clôture (garde-fou) | C2 | 🟢 |
| Support/résistance | rebond/rejet à boîte large > boîte étroite (pondération) | C2 | 🟢 |
| Paramétrage SharpCharts | réf. outillage tiers, non implémentable NT8/ATAS | C2 | 🟢 |

**Belkhayate :** ⚫ NON CONCERNÉ — aucun lien explicite avec la méthode Belkhayate dans la source.
**Actifs :** principe générique applicable à GC·HG·CL·ZW (lecture volume), sous réserve de disposer du volume natif NT8/ATAS et non de l'implémentation StockCharts.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Décisions BRUTES en zone validation/, non fusionnées dans KNOWLEDGE_BASE_MASTER.json.
