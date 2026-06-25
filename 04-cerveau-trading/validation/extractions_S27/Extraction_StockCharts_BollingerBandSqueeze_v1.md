# Extraction StockCharts — Bollinger Band Squeeze
**Source :** `bundles/stockcharts/bollinger_band_squeeze.md` (HTTP 200 · ~13 099 car.) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section fallback) · 7/7 certifiées
**Décisions :** D891 → D903 · **Page :** https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/bollinger-band-squeeze
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 - Bollinger Band Squeeze | How Do You Set Up the Indicators? | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 - Bollinger Band Squeeze | How the Strategy Works | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 - Bollinger Band Squeeze | How the Strategy Works | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 - Bollinger Band Squeeze | Trading Signals | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 5 - Bollinger Band Squeeze | Tweaking | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 6 - Bollinger Band Squeeze | Tweaking | CERTIFIE (accord .md + HTML) |
| image_07.png | Chart 7 - Bollinger Band Squeeze | The Head Fake | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D891 — Définition du Bollinger Band Squeeze
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md) : « A Bollinger Band Squeeze is a condition that occurs when the Bollinger Bands narrow due to decreased volatility. According to John Bollinger, periods of low volatility are often followed by periods of high volatility. Therefore, a volatility contraction or narrowing of the bands can foreshadow a significant advance or decline. »
**TRADEX-AI C1** : Détecteur de contraction de volatilité → expansion imminente ; brique « configuration » de pré-signal sur GC/HG/CL/ZW.
*Catégorie : configuration*
---

### D892 — Déclenchement par cassure de bande
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md) : « Once the squeeze play is on, a subsequent band break signals the start of a new move. A new advance starts with a squeeze and subsequent break above the upper band. A new decline starts with a squeeze and subsequent break below the lower band. »
**TRADEX-AI C1** : Cassure de la bande supérieure post-squeeze = nouveau mouvement haussier ; cassure de la bande inférieure = baissier.
*Catégorie : signal*
---

### D893 — Paramètres par défaut des Bollinger Bands
🟡 **CONVENTION** (Source : bollinger_band_squeeze.md, image_01) : « setting the Bollinger Bands at 20 periods and two standard deviations, the default settings... Bollinger Bands start with the 20-day SMA of closing prices. The upper and lower bands are then set two standard deviations above and below this moving average. »
**TRADEX-AI C1** : Réglage par défaut BB(20, 2) sur clôtures ; ajustable selon l'actif/timeframe.
*Catégorie : indicateurs_tendance*
---

### D894 — Indicateur BandWidth (distance entre bandes)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md) : « this indicator is called Bollinger BandWidth... It is simply the value of the upper band less the value of the lower band... stocks with higher prices tend to have higher BandWidth readings... If price equals 100 and BandWidth equals 5, then BandWidth would be 5% of the price. »
**TRADEX-AI C1** : BandWidth = (bande sup − bande inf) ; à normaliser en % du prix pour comparer GC/HG/CL/ZW (échelles de prix différentes).
*Catégorie : indicateurs_tendance*
---

### D895 — Procédure de la stratégie (squeeze + range 6 mois)
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md, image_02, image_03) : « First, look for securities with narrowing Bollinger Bands and low BandWidth levels. Ideally, BandWidth should be near the low end of its six-month range. Second, wait for a band break to signal the start of a new move. An upside band break is bullish, while a downside band break is bearish. »
**TRADEX-AI C1** : Setup en 2 temps : (1) BandWidth proche du bas de sa fourchette 6 mois, (2) attendre la cassure directionnelle.
*Catégorie : configuration*
---

### D896 — Le squeeze est non directionnel
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md) : « narrowing bands do not provide any directional clues. They simply infer that volatility is contracting and chartists should be prepared for a volatility expansion. » Recap : « Bollinger Bands narrow... BandWidth near the low end of its six-month range... Price breaks above the upper band or below the lower band. »
**TRADEX-AI C1** : Le squeeze seul ne donne JAMAIS de direction → critère éliminatoire pour un signal autonome ; nécessite confirmation directionnelle externe.
*Catégorie : configuration*
---

### D897 — Confirmation par support/résistance
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md, image_04) : « a break above resistance can be used to confirm a break above the upper band. Similarly, a break below support can be used to confirm a break below the lower band. Unconfirmed band breaks are subject to failure. »
**TRADEX-AI C1** : Cassure de bande à confirmer par cassure de S/R (cohérent avec pivots Belkhayate) ; cassure non confirmée = haut risque d'échec.
*Catégorie : signal*
---

### D898 — Exemple SBUX : double signal en deux mois
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md, image_04) : Starbucks (SBUX) — « SBUX broke the lower band twice, but did not break support... a falling wedge-type pattern... a bullish continuation pattern. SBUX subsequently broke above the upper band, then broke resistance for confirmation. » Plus tard, un bull flag échoue : « SBUX broke the lower band and support, which led to a sharp decline. »
**TRADEX-AI C1** : Cas illustrant que la cassure de bande SANS cassure de S/R associée est un faux signal ; le contexte chartiste (wedge/flag) prime.
*Catégorie : configuration*
---

### D899 — Tweaking : indicateurs volume pendant la consolidation
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md) : « Momentum oscillators and moving averages are of little value during a consolidation... chartists should consider using volume-based indicators, such as the Accumulation Distribution Line, Chaikin Money Flow, the Money Flow Index (MFI) or On Balance Volume (OBV). Signs of accumulation increase the chances of an upside breakout, while signs of distribution increase the chances of a downside break. »
**TRADEX-AI C2** : Pendant le squeeze, privilégier les indicateurs de volume (ADL, CMF, MFI, OBV) plutôt que momentum/MM ; lien direct avec l'Énergie Belkhayate = MFI (mémoire projet) et l'order flow ATAS (C2).
*Catégorie : indicateurs_momentum*
---

### D900 — Exemple LOW : CMF anticipe une cassure baissière
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md, image_05) : Lowes (LOW), avril 2011 — « The bands moved to their narrowest range in months... Chaikin Money Flow weakening in March and turning negative in April... Negative readings in Chaikin Money Flow reflect distribution or selling pressure that can be used to anticipate or confirm a support break. »
**TRADEX-AI C2** : CMF négatif pendant le squeeze = distribution → biais cassure baissière ; preuve qu'un indicateur de pression anticipe la direction.
*Catégorie : divergence*
---

### D901 — Exemple INTU : OBV + piercing pattern avant cassure haussière
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md, image_06) : Intuit (INTU) — « On Balance Volume (OBV) continued to move higher, which showed accumulation during the September trading range... a piercing pattern formed, which is a bullish candlestick reversal pattern. This pattern reinforced support and the follow-through foreshadowed the upside breakout. »
**TRADEX-AI C2** : OBV haussier (accumulation) + chandelier piercing = faisceau de confirmation pré-cassure haussière (combine C2 et lecture chandeliers).
*Catégorie : signal*
---

### D902 — Le « Head Fake » (faux signal de cassure)
🔵 **ÉCOLE** (Source : bollinger_band_squeeze.md, image_07) : « John Bollinger advises chartists to beware of the "head fake."... A bullish head fake starts when Bollinger Bands contract and prices break above the upper band... prices quickly move back below the upper band and proceed to break the lower band. A bearish head fake starts when... prices break below the lower band... then proceed to break the upper band. »
**TRADEX-AI C1** : Piège du faux break (bull/bear trap) post-squeeze → renforce l'obligation de confirmation S/R (D897) avant toute exécution, a fortiori en mode AUTO.
*Catégorie : signal*
---

### D903 — Synthèse stratégie + scan + amélioration du R/R
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_band_squeeze.md) : « In its purest form, this strategy is neutral and the ensuing break can be up or down. Chartists... must employ other aspects of technical analysis to formulate a trading bias to act before the break or confirm the break. Acting before the break will improve the risk-reward ratio. » Scan : `[[Upper BB(20,2) - Lower BB(20,2)] / Close ] < .04` (BandWidth < 4 % du prix considéré comme étroit).
**TRADEX-AI C1** : Seuil opérationnel « squeeze » = BandWidth < 4 % du prix ; anticiper la cassure (vs attendre) améliore le R/R — pertinent pour viser le critère R/R ≥ 1:2 de la grille.
*Catégorie : gestion_risque_entree*
---

## SYNTHÈSE

| Plage | Décisions | Images | Tags dominants | Cercle |
|-------|-----------|--------|----------------|--------|
| D891→D903 | 13 | 7/7 certifiées | 🔵 ÉCOLE (6) · 🟢 (6) · 🟡 (1) | C1 (dominant) / C2 |

Stratégie de volatilité non directionnelle : squeeze (BandWidth < 4 % du prix, bas de fourchette 6 mois) → cassure de bande confirmée par S/R. Points durs codables : formule BandWidth, seuil 4 %, scan. Garde-fous critiques : le squeeze NE donne PAS de direction (D896) et le « head fake » impose une confirmation (D897/D902) — alignés avec les pivots Belkhayate et l'interdiction de signal isolé en AUTO. Lien Belkhayate notable : D899 recommande les indicateurs de volume dont le MFI = Énergie Belkhayate (mémoire projet). Aucun cas ambigu, aucune image à vérifier.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
