# Extraction StockCharts — CandleVolume
**Source :** `bundles/stockcharts/candlevolume.md` (HTTP 200 · ~10 000 car.) + 11 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D1111 → D1124 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/candlevolume
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | CandleVolume : larges/étroits, hollow/filled | Calculating CandleVolume Charts | CERTIFIE (accord .md + HTML) |
| image_02.png | Version colorisée du CandleVolume | Calculating CandleVolume Charts | CERTIFIE (accord .md + HTML) |
| image_03.png | CandleVolume avec chandeliers et axe X normaux | Calculating CandleVolume Charts | CERTIFIE (accord .md + HTML) |
| image_04.png | CandleVolume : largeurs variables → modif axe X | Calculating CandleVolume Charts | CERTIFIE (accord .md + HTML) |
| image_05.png | Candlestick Reversal (RIG hammer) | Candlestick Reversal [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Candlestick Reversal (RIG bearish engulfing) | Candlestick Reversal [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_07.png | Candlestick Reversal (price action après) | Candlestick Reversal [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_08.png | Breakout Validation (GOOG breakout) | Breakout Validation [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | Breakout Validation (suite) | Breakout Validation [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_10.png | Réglages SharpCharts CandleVolume | CandleVolume and SharpCharts | CERTIFIE (accord .md + HTML) |
| image_11.png | CandleVolume and SharpCharts (exemple) | CandleVolume and SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1111 — Définition : CandleVolume fusionne volume et chandeliers
🔵 **ÉCOLE (StockCharts / type de graphique)** (Source : candlevolume.md) : Le CandleVolume fusionne le volume dans les chandeliers, permettant d'analyser prix et volume d'un seul regard. Proche des EquiVolume charts mais plus riche : les chandeliers (au lieu de boîtes high-low) montrent ouverture et clôture en plus du high et du low. Ils s'utilisent comme des chandeliers normaux : patterns chandeliers et patterns classiques (triangles, wedges) pour générer des signaux.
**TRADEX-AI C2** : Concept de représentation combinée prix+volume ; idée transposable en feature (largeur ∝ volume) plutôt qu'en type de graphique. Relie C1 (prix) et C2 (flux).
*Catégorie : structure_marche*

---

### D1112 — Composition d'un chandelier CandleVolume (5 composantes)
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_01) : Un chandelier CandleVolume comporte cinq composantes — open, high, low, close et volume. Comme un chandelier normal, open et close forment le corps, high et low forment les mèches haute et basse. Le volume détermine la LARGEUR du chandelier.
**TRADEX-AI C2** : Mapping déterministe : largeur = f(volume). Exploitable comme feature numérique à partir des OHLCV NT8.
*Catégorie : structure_marche*

---

### D1113 — Largeur ∝ volume, couleur corps = sens open/close
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_01) : Chandeliers larges quand le volume est élevé, étroits quand il est faible. Larges et hollow : clôture nettement au-dessus de l'ouverture avec gros volume. Larges et filled : clôture nettement sous l'ouverture avec gros volume. Étroits : volume relativement faible.
**TRADEX-AI C2** : Deux features orthogonales — direction (hollow/filled = close vs open) et intensité de flux (largeur = volume). Combinables en un score de pression.
*Catégorie : structure_marche*

---

### D1114 — Colorisation : couleur = close vs clôture précédente
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_02) : En version colorisée (Color Prices / Color Volume), un chandelier hollow signifie close > open et filled signifie close < open. Un chandelier rouge = close sous la clôture PRÉCÉDENTE ; noir = close au-dessus de la clôture précédente. Idem pour les barres de volume rouges/vertes.
**TRADEX-AI C2** : Distinction clé — hollow/filled compare à l'ouverture du jour, rouge/noir compare à la clôture de la veille (momentum inter-périodes). Deux signaux différents à ne pas confondre.
*Catégorie : signal*

---

### D1115 — Normalisation du volume sur la période de look-back
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_03) : Le volume est normalisé en pourcentage de la période de look-back. Sur un graphique daily de 4 mois, le volume de chaque jour est divisé par le volume total des 4 mois. La largeur de chaque boîte représente donc le pourcentage du volume total ; les jours à gros volume occupent plus d'espace sur l'axe X que les jours à faible volume.
**TRADEX-AI C2** : Normalisation = volume relatif au contexte (non absolu). Pertinent pour comparer la pression entre barres d'un même actif ; à recalibrer par fenêtre.
*Catégorie : structure_marche*

---

### D1116 — Axe X non uniforme (largeurs variables)
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_04) : L'axe des dates n'est généralement PAS uniforme sur les CandleVolume : certaines semaines s'étendent davantage (chandeliers larges), d'autres sont plus courtes (chandeliers étroits). L'exemple Pfizer (PFE) montre d'abord des chandeliers normaux et un axe X normal, puis un autre où l'axe X change car le volume de juin fut bien plus élevé que les mois précédents.
**TRADEX-AI C2** : Limite de lisibilité (axe temps déformé) ; pour le moteur, conserver l'axe temps réel et n'utiliser que la composante volume comme feature, sans déformer la chronologie.
*Catégorie : structure_marche*

---

### D1117 — Validation des retournements chandeliers par le volume
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_05, image_06, image_07) : Le CandleVolume valide les patterns de retournement chandelier : un retournement sur volume élevé pèse plus qu'un retournement sur faible volume. Exemples Transocean (RIG) : un *wide hammer* (hammer large) mi-avril, puis un *wide bearish engulfing* (engulfing baissier large) mi-mai, suivis de la price action correspondante.
**TRADEX-AI C2** : Règle de pondération — un pattern de retournement (hammer, engulfing) gagne en poids si la barre est « large » (gros volume). Pondérer le score de retournement par le volume relatif.
*Catégorie : signal*

---

### D1118 — Volume comme « carburant » du breakout
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md) : Le volume est important pour valider les cassures de support/résistance. Le volume est le « carburant » : un breakout haussier sur volume élevé est plus haussier qu'un breakout sur faible volume.
**TRADEX-AI C2** : Filtre de validation de breakout — exiger un volume élevé (barre large) pour valider une cassure. Transposable en condition objective (volume > seuil relatif).
*Catégorie : configuration*

---

### D1119 — Breakout haussier large = forte demande durable
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_08, image_09) : Un breakout haussier sur volume élevé montre une forte demande, moins susceptible de s'estomper. Exemple Google (GOOG) cassant au-dessus de la résistance avec un *wide hollow candlestick* (large et hollow = volume élevé / forte demande sur la cassure). L'auteur prévient toutefois que tous les setups ne paient pas aussi bien.
**TRADEX-AI C2** : La « large hollow candle » sur résistance = signature de breakout fiable. Avertissement intégré : pas de garantie → conserver gestion du risque et R/R.
*Catégorie : configuration*

---

### D1120 — Bilan : valider patterns, supports et résistances
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md) : Le CandleVolume combine prix et volume pour une analyse visuelle simple. Partageant les caractéristiques des chandeliers normaux, il sert à valider les patterns chandeliers, à affirmer un test de support ou valider un niveau de résistance. Un rebond sur support avec un chandelier large est plus fort qu'avec un chandelier étroit ; idem pour un déclin depuis une résistance. Presque tout ce qui se fait sur chandeliers normaux s'applique au CandleVolume.
**TRADEX-AI C2** : Principe synthétique — la largeur (volume) module la force d'un rebond/rejet sur niveau. Combinable avec les Pivots/niveaux comme pondération de la réaction.
*Catégorie : signal*

---

### D1121 — Paramétrage SharpCharts : Chart Type, gestion du volume
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_10) : Dans SharpCharts, CandleVolume se trouve sous **Chart Type** dans les Attributs. Un réglage de volume permet volume off / separate / overlay ; il peut être désactivé car déjà reflété dans le CandleVolume.
**TRADEX-AI C2** : Détail outil StockCharts (UI) ; pas de paramètre nouveau pour le moteur. Note : le volume est intrinsèque au type, donc redondant en overlay.
*Catégorie : configuration*

---

### D1122 — Colorisation des barres (Color Volume / Up-Down Color)
🟢 **FAIT VÉRIFIÉ** (Source : candlevolume.md, image_11) : La case **Color Volume** affiche les jours hausse/baisse du volume en couleurs différentes ; les couleurs des barres de prix et de volume se choisissent via **Up Color** / **Down Color**, ou Auto pour les couleurs par défaut.
**TRADEX-AI C2** : Détail purement visuel (UI StockCharts) ; sans impact moteur. Documenté pour traçabilité.
*Catégorie : configuration*

---

### D1123 — Lien EquiVolume (référence comparative)
🔵 **ÉCOLE (StockCharts)** (Source : candlevolume.md) : Le CandleVolume est similaire aux EquiVolume charts mais offre plus d'information car il utilise des chandeliers (open/close visibles) au lieu de boîtes high-low.
**TRADEX-AI C2** : Référence vers un type voisin (EquiVolume) ; utile pour le sourcing futur mais pas de règle opérationnelle ici.
*Catégorie : structure_marche*

---

### D1124 — Bibliographie : Morris et Nison (Further Study)
🟡 **CONVENTION (bibliographie)** (Source : candlevolume.md) : La section Further Study renvoie à deux ouvrages de référence sur les chandeliers : *Candlestick Charting Explained* (Gregory Morris) et *Japanese Candlestick Charting Techniques* (Steve Nison).
**TRADEX-AI C1** : Sources de référence pour enrichissement futur de la KB sur les patterns chandeliers (sourcing, pas une règle).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1111 | Définition CandleVolume | 🔵 ÉCOLE | C2 | structure_marche |
| D1112 | 5 composantes (OHLCV), largeur = volume | 🟢 | C2 | structure_marche |
| D1113 | Largeur ∝ volume, hollow/filled | 🟢 | C2 | structure_marche |
| D1114 | Colorisation = close vs clôture veille | 🟢 | C2 | signal |
| D1115 | Normalisation volume sur look-back | 🟢 | C2 | structure_marche |
| D1116 | Axe X non uniforme | 🟢 | C2 | structure_marche |
| D1117 | Validation retournements par volume | 🟢 | C2 | signal |
| D1118 | Volume = carburant du breakout | 🟢 | C2 | configuration |
| D1119 | Breakout large hollow = demande durable | 🟢 | C2 | configuration |
| D1120 | Bilan — valider patterns/support/résistance | 🟢 | C2 | signal |
| D1121 | Paramétrage SharpCharts | 🟢 | C2 | configuration |
| D1122 | Colorisation barres (UI) | 🟢 | C2 | configuration |
| D1123 | Lien EquiVolume | 🔵 ÉCOLE | C2 | structure_marche |
| D1124 | Bibliographie Morris / Nison | 🟡 CONVENTION | C1 | structure_marche |

**Liens Belkhayate :** le CandleVolume n'est PAS un outil de la méthode Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé par Belkhayate) : la pondération d'un rebond/rejet sur niveau par le volume (D1120) recoupe l'esprit de l'étape Énergie/Déclencheur ; mais la méthode Belkhayate utilise le MFI standard (mémoire projet), pas le CandleVolume. Ne rien inventer.

**À vérifier (humain) :**
- D1115 — la « normalisation sur look-back » est propre au rendu graphique ; pour le moteur, choisir explicitement la fenêtre de normalisation du volume relatif par actif (GC/HG/CL/ZW).
- D1117 / D1119 — la notion de barre « large » (gros volume) doit être seuillée objectivement (ex. volume > X× médiane) avant codage ; la source reste qualitative.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
