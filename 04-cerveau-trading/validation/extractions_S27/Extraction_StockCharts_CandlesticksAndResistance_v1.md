# Extraction StockCharts — Candlesticks and Resistance

**Source :** `bundles/stockcharts/candlesticks_and_resistance.md` (HTTP 200 · ~4 100 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D1051 → D1059 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlesticks-and-resistance
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Resistance level marked by doji. | Candlesticks and Resistance | CERTIFIE |
| image_02.png | Shooting star and dark cloud cover marked the resistance level. | Candlesticks and Resistance | CERTIFIE |
| image_03.png | Shooting stars marked the resistance level. | Candlesticks and Resistance | CERTIFIE |

## DÉCISIONS

### D1051 — Rôle des chandeliers face à la résistance
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md) : « Single candlesticks and candlestick patterns can confirm or mark resistance levels. (…) In a trading range, candlesticks can help identify entry points to sell near resistance or buy near support levels. »
**TRADEX-AI C1** : Les chandeliers servent à **marquer/confirmer** une résistance et à timer des entrées vendeuses près de la résistance dans un range — fonction de structuration des zones de prix C1.
*Catégorie : structure_marche*
---

### D1052 — Liste des figures associées à la résistance
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md) : Figures listées pour identifier/confirmer une résistance : Bearish Engulfing (R), Bearish Harami (R), Dark Cloud Cover (R), Doji (Normal/Long-Legged/Dragonfly), Evening Star ou Bearish Abandoned Baby (R), Hanging Man (R), Long Black Candlestick ou Black Marubozu, Shooting Star (R), Spinning Top, Three Black Crows (R). « The bearish reversal patterns are marked with an (R). »
**TRADEX-AI C1** : Set de figures candidates pour le détecteur « résistance » C1 ; distingue retournements baissiers (R) et figures de pression/indécision (Marubozu, Doji, Spinning Top).
*Catégorie : signal*
---

### D1053 — Logique des retournements baissiers à la résistance
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlesticks_and_resistance.md) : « Bearish reversal candlesticks and patterns suggest that buying pressure was suddenly overturned and selling pressure prevailed. Such a quick reversal of fortune indicates overhead supply, suggesting a resistance level could form. »
**TRADEX-AI C1+C5** : Un retournement baissier près d'un sommet = bascule pression acheteuse→vendeuse signalant une offre en surplomb (overhead supply) → formation probable de résistance.
*Catégorie : signal*
---

### D1054 — Pression vendeuse sans retournement (Hanging Man, Long Black, Black Marubozu)
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md) : Ces figures « signify increased selling pressure rather than an actual reversal ». Hanging Man : longue ombre basse = pression vendeuse intra-séance surmontée à la clôture mais « raises a yellow flag ». Long Black / Black Marubozu : pression vendeuse soutenue open→close signalant la faiblesse acheteuse.
**TRADEX-AI C1** : Distinction clé — certaines figures signalent une **pression** (alerte/yellow flag) et non un retournement confirmé ; à pondérer plus faiblement qu'un vrai signal de retournement.
*Catégorie : signal*
---

### D1055 — Doji et Spinning Top à la résistance (neutres)
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md) : « The doji and spinning top show indecision and are generally considered neutral. (…) New buyers must be willing to pay higher prices for an advance to continue. (…) a standoff shows a lack of conviction among buyers and a possible resistance level. »
**TRADEX-AI C1+C5** : Doji/Spinning Top = neutres (indécision) ; à la résistance, ils traduisent un manque de conviction acheteuse → résistance possible. Signal faible/contextuel, pas de retournement net.
*Catégorie : signal*
---

### D1056 — Cas Veritas (VRTS) : doji marquant la résistance
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md, image_01) : Après une avance de $90 à $140, un gap up et deux doji ont marqué « a sudden stalemate between buyers and sellers; subsequently, a resistance level formed. » Un doji ultérieur près de la résistance a confirmé le manque de conviction.
**TRADEX-AI C1** : Exemple empirique — des doji groupés après une forte avance = stalemate marquant la résistance ; confirme l'usage du doji comme marqueur de zone (pas signal d'entrée seul).
*Catégorie : structure_marche*
---

### D1057 — Cas Lucent (LU) : shooting star + dark cloud cover
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md, image_02) : Dans un range $53–$42, la résistance fut d'abord établie « in late April with a shooting star and dark cloud cover. These bearish reversals were confirmed with a gap down two days later and a resistance test at $52. »
**TRADEX-AI C1+C3** : Combinaison shooting star + dark cloud cover = double signal baissier à la résistance ; la **confirmation** (gap down + retest) valide la zone → logique de confirmation multi-bougies.
*Catégorie : signal*
---

### D1058 — Cas Delta Air Lines (DAL) : shooting stars + evening star
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_resistance.md, image_03) : Résistance à $57 établie par le haut d'une shooting star ; en mai « a slew of shooting stars formed, as did the odd spinning top and long-legged doji ». Le déclin sous 56 a confirmé le caractère baissier ; un petit chandelier blanc sans suite a levé le yellow flag, puis un gap down a formé une bearish evening star.
**TRADEX-AI C1** : Accumulation de shooting stars + doji à un même niveau = résistance robuste ; l'absence de suivi (small white candle sans follow-through) est un signal d'avertissement avant retournement.
*Catégorie : signal*
---

### D1059 — Confirmation obligatoire avant décision
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlesticks_and_resistance.md) : Dans les 3 cas, le caractère baissier des figures n'est acté qu'après confirmation (« confirmed with a gap down », « The decline that broke below 56 confirmed these as bearish »).
**TRADEX-AI C1+C3** : Principe transversal — une figure baissière à la résistance ne devient un signal exploitable qu'après **confirmation directionnelle** (gap/clôture franchissant un niveau) ; garde-fou anti-faux-signal pour le scoring TRADEX-AI.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Thème | Apport pour TRADEX-AI | Cercle | Tag |
|-------|------------------------|--------|-----|
| Rôle résistance | Chandeliers marquent/confirment résistance + timing vente | C1 | 🟢 |
| Liste figures (R) | Set candidat détecteur résistance (10 figures) | C1 | 🟢 |
| Retournement baissier | Bascule achat→vente = overhead supply | C1+C5 | 🔵 |
| Pression ≠ retournement | Hanging Man/Marubozu = yellow flag, pondérer + faible | C1 | 🟢 |
| Doji/Spinning Top | Neutres, manque de conviction = résistance possible | C1+C5 | 🟢 |
| Cas VRTS/LU/DAL | Exemples empiriques de marquage de résistance | C1 | 🟢 |
| Confirmation obligatoire | Signal valide seulement après confirmation directionnelle | C1+C3 | 🔵 |

**Belkhayate :** ⚫ NON CONCERNÉ — aucun lien explicite avec la méthode Belkhayate dans la source.
**Actifs :** principe générique applicable à GC·HG·CL·ZW (lecture chandelier + niveaux S/R sur données NT8/ATAS).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Décisions BRUTES en zone validation/, non fusionnées dans KNOWLEDGE_BASE_MASTER.json.
