# Extraction StockCharts — Candlesticks and Support

**Source :** `bundles/stockcharts/candlesticks_and_support.md` (HTTP 200 · ~4 300 car.) + 3 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D1071 → D1079 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/candlestick-charts/candlesticks-and-support
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | The support level was confirmed with the doji after a Marubozu and a spinning top candlestick pattern. | Introduction | CERTIFIE |
| image_02.png | A Bullish Engulfing pattern confirms the support level. | Introduction | CERTIFIE |
| image_03.png | The support level was further confirmed by a spinning top, harami, and hammer. | Introduction | CERTIFIE |

## DÉCISIONS

### D1071 — Rôle des chandeliers face au support
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md) : « Single candlesticks and candlestick patterns can confirm or mark support levels. (…) In a trading range, candlesticks can help choose entry points for buying near support and selling near resistance. »
**TRADEX-AI C1** : Les chandeliers servent à **marquer/confirmer** un support et à timer des entrées acheteuses près du support dans un range — fonction de structuration des zones de prix C1.
*Catégorie : structure_marche*
---

### D1072 — Liste des figures associées au support
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md) : Figures listées pour identifier/confirmer un support : Bullish Engulfing (R), Bullish Harami (R), Doji (Normal/Long-Legged/Dragonfly), Hammer (R), Inverted Hammer (R), Long White Candlestick ou White Marubozu, Morning Star ou Bullish Abandoned Baby (R), Piercing Pattern (R), Spinning Top, Three White Soldiers (R). « The bullish reversal patterns are marked with an (R). »
**TRADEX-AI C1** : Set de figures candidates pour le détecteur « support » C1 ; miroir haussier du set résistance — distingue retournements haussiers (R) et figures de pression/indécision (Marubozu, Doji, Spinning Top).
*Catégorie : signal*
---

### D1073 — Logique des retournements haussiers au support
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlesticks_and_support.md) : « Bullish reversal candlesticks and patterns indicate that buying pressure overcame early selling pressure for a strong finish. This bullish price action suggests enough strong demand for support to be established. »
**TRADEX-AI C1+C5** : Un retournement haussier près d'un creux = pression acheteuse l'emportant sur la pression vendeuse → demande suffisante pour établir un support.
*Catégorie : signal*
---

### D1074 — Pression acheteuse sans retournement (Inverted Hammer, Long White, White Marubozu)
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md) : Ces figures « show increased buying pressure rather than an actual price reversal ». Inverted Hammer : longue ombre haute = intérêt acheteur intra-séance qui s'estompe ; clôture sous le haut mais le fait que les acheteurs aient poussé les prix est haussier. Long White / White Marubozu : pression acheteuse soutenue open→close.
**TRADEX-AI C1** : Symétrie avec la résistance — certaines figures signalent une **pression acheteuse** (bode well for support) sans retournement net ; à pondérer plus faiblement qu'un retournement confirmé.
*Catégorie : signal*
---

### D1075 — Doji et Spinning Top au support (neutres)
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md) : « The doji and spinning top denote indecision and are generally considered neutral. (…) After a decline, the appearance of a doji or spinning top denotes a sudden letup in selling pressure. A stand-off has developed (…) and a support level may form. »
**TRADEX-AI C1+C5** : Au support, Doji/Spinning Top traduisent un essoufflement soudain de la pression vendeuse → support possible. Signal faible/contextuel, pas de retournement net.
*Catégorie : signal*
---

### D1076 — Cas Electronic Data Systems (EDS) : doji après Marubozu et spinning top
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md, image_01) : Dans un range $58–$75, à l'approche du support $58 « a long-legged doji and later a spinning top » se sont formés ; « the doji formed immediately after a Marubozu (…). This doji marked a sudden decrease in relative selling pressure and support held. » Support retesté en avril (long-legged doji).
**TRADEX-AI C1** : Exemple empirique — un doji juste après un long Marubozu noir = chute brutale de la pression vendeuse marquant la tenue du support ; séquence Marubozu→Doji comme indice de bascule.
*Catégorie : structure_marche*
---

### D1077 — Cas Broadcom (BRCM) : bullish engulfing + long white candle
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md, image_02) : Un bullish engulfing a marqué un nouveau support sous $210 ; quelques jours après « a long white candlestick formed and engulfed the previous four candlesticks ». La combinaison « reinforced the validity of support around $208 ». Support retesté (piercing pattern début octobre, large hammer fin octobre).
**TRADEX-AI C1+C3** : Combinaison bullish engulfing + long white candle = renforcement de la validité du support ; piercing pattern et hammer ultérieurs confirment la zone → empilement de signaux haussiers sur un même niveau.
*Catégorie : signal*
---

### D1078 — Cas Medtronic (MDT) : spinning top + harami + hammer
🟢 **FAIT VÉRIFIÉ** (Source : candlesticks_and_support.md, image_03) : Support ~$46 établi par un spinning top puis un harami ; après une chute en avril « a hammer was formed to confirm support at $46 ». Après une reaction rally, le titre a de nouveau trouvé support ~$46.
**TRADEX-AI C1** : Séquence spinning top → harami → hammer confirmant un même support ; le hammer agit comme confirmation finale de la zone de demande.
*Catégorie : signal*
---

### D1079 — Confirmation et empilement de figures au support
🔵 **ÉCOLE** (chandeliers japonais) (Source : candlesticks_and_support.md) : Dans les 3 cas, le support est « confirmed » / « further confirmed » par une succession de figures (doji après Marubozu ; engulfing + long white ; spinning top + harami + hammer).
**TRADEX-AI C1+C3** : Principe transversal — la fiabilité d'un support croît avec l'**empilement de figures concordantes** et les retests ; transposable à la pondération du score d'un signal d'achat sur support (plus de confirmations = score plus élevé).
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Thème | Apport pour TRADEX-AI | Cercle | Tag |
|-------|------------------------|--------|-----|
| Rôle support | Chandeliers marquent/confirment support + timing achat | C1 | 🟢 |
| Liste figures (R) | Set candidat détecteur support (10 figures, miroir résistance) | C1 | 🟢 |
| Retournement haussier | Pression achat > vente = demande établissant support | C1+C5 | 🔵 |
| Pression ≠ retournement | Inverted Hammer/White Marubozu = pression, pondérer + faible | C1 | 🟢 |
| Doji/Spinning Top | Essoufflement vendeur = support possible | C1+C5 | 🟢 |
| Cas EDS/BRCM/MDT | Exemples empiriques de marquage de support | C1 | 🟢 |
| Confirmation/empilement | Fiabilité ↑ avec figures concordantes + retests (scoring) | C1+C3 | 🔵 |

**Belkhayate :** ⚫ NON CONCERNÉ — aucun lien explicite avec la méthode Belkhayate dans la source.
**Actifs :** principe générique applicable à GC·HG·CL·ZW (lecture chandelier + niveaux S/R sur données NT8/ATAS).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Décisions BRUTES en zone validation/, non fusionnées dans KNOWLEDGE_BASE_MASTER.json.
