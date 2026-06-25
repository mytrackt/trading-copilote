# Extraction StockCharts — Price Relative / Relative Strength (force relative inter-marché, C7)
**Source :** `bundles/stockcharts/price_relative_relative_strength.md` (HTTP 200 · ~15 400 car.) + 7 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende) · 7/7 certifiées
**Décisions :** D3231 → D3250 · **Page :** chartschool.stockcharts.com/.../technical-indicators/price-relative-relative-strength
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Indicateur de **force relative inter-marché** (ratio A/B) → Cercle **C7** (corrélations / inter-marché du projet). À NE PAS confondre avec le RSI de Wilder.

---

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Price Relative - Spreadsheet 1 | How To Calculate | D3234 |
| image_02 | Price Relative - Chart 1 | How To Calculate | D3235 |
| image_03 | Price Relative - Chart 2 | Trend Identification | D3239 |
| image_04 | Price Relative - Chart 3 | Bullish/Bearish Divergences | D3241 |
| image_05 | Price Relative - Chart 4 | Bullish/Bearish Divergences | D3242 |
| image_06 | Price Relative - Chart 5 | Using with SharpCharts | D3248 |
| image_07 | Price Relative - SharpCharts | Using with SharpCharts | D3248 |

---

## DÉCISIONS

### D3231 — Définition : ratio comparatif de performance
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Le Price Relative (alias Relative Strength / Relative Strength Comparative) utilise un **ratio chart** pour comparer la performance d'un titre à un autre.
**TRADEX-AI C7** : mesure relative entre deux marchés ; brique directe de l'analyse inter-marché du projet.
*Catégorie : structure_marche*

### D3232 — Trois usages (benchmark, secteur, comportement défensif)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Usages : (1) performance vs benchmark (ex. S&P 500) ; (2) performance vs secteur/industrie (sur/sous-performance des pairs) ; (3) identifier les titres qui **tiennent** en déclin de marché ou montrent de la faiblesse en hausse.
**TRADEX-AI C7** : grille d'usages transposable aux relations GC/HG/CL/ZW vs DX/ES/MBT/6J.
*Catégorie : structure_marche*

### D3233 — Ratio ticker (symbole avec deux-points)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Sur StockCharts, un **ratio ticker** joint deux symboles par un deux-points (ex. « IBM:$SPX », « $INDU:$GOLD ») ; sa valeur = clôture du premier / clôture du second.
**TRADEX-AI C7** : convention de notation ; un ratio « HG:GC » (cuivre/or) est calculable de la même façon.
*Catégorie : structure_marche*

### D3234 — Formule complète (close/open/high/low du ratio)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_01) : `Price Relative = Base Security / Comparative Security`. Détail : `Close = close1/close2`, `Open = open1/close2`, `High = high1/close2`, `Low = low1/close2` (les O/H/L du ratio divisent toujours par la **clôture** du second symbole).
**TRADEX-AI C7** : formule déterministe codable ; noter que seul le close du dénominateur est utilisé pour O/H/L.
*Catégorie : indicateurs_tendance*

### D3235 — Lecture du ratio (sens des variations)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_02) : Ex. SBUX/$SPX : première valeur 0,0256 (30,66/1197,75). Le ratio **monte** si la base avance plus / décline moins que le benchmark ; **baisse** sinon. La variation quotidienne du ratio ≈ (%var base − %var benchmark). Ex. : SBUX −2,66 % vs SPX −1,62 % → ratio −1,04 %.
**TRADEX-AI C7** : interprétation directionnelle quantifiée ; la variation du ratio approxime l'écart de rendement.
*Catégorie : indicateurs_tendance*

### D3236 — Sémantique : hausse = surperformance, baisse = sous-performance
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Le Price Relative **monte** quand le titre montre de la force relative et surperforme son benchmark ; **baisse** quand il sous-performe (faiblesse relative). Important pour la sélection de titres (les gérants visent à battre le benchmark).
**TRADEX-AI C7** : règle de hiérarchisation leaders/laggards entre actifs.
*Catégorie : indicateurs_tendance*

### D3237 — Deux familles d'usage : tendance et divergences
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Deux approches : (1) **analyse de tendance** du Price Relative (trend, S/R, moyennes mobiles, autres indicateurs) ; (2) recherche de **divergences** bullish/bearish pour anticiper un retournement du prix.
**TRADEX-AI C7** : deux modes d'exploitation distincts à implémenter.
*Catégorie : signal*

### D3238 — Tendance du ratio par higher highs/lower lows
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Comme tout prix, le Price Relative **trend up** sur higher highs / higher lows et **trend down** sur lower lows / lower highs. Une MM de choix s'applique.
**TRADEX-AI C7** : l'analyse de structure standard s'applique au ratio comme à un prix.
*Catégorie : indicateurs_tendance*

### D3239 — Filtre SMA 150 jours sur le ratio
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_03) : Downtrend long terme possible quand le Price Relative est **sous sa SMA 150 jours** ; uptrend long terme quand il est **au-dessus**. Ex. HPQ:$SPX (SMA 15j sur prix et ratio) : cassure de résistance mi-juin = départ d'uptrend ; cassure sous la SMA 150 = départ de sous-performance.
**TRADEX-AI C7** : seuil SMA 150 sur le ratio = filtre directionnel de force relative codable. *(Note interne : le texte mentionne SMA 15j appliquée dans l'exemple et SMA 150j comme seuil long terme — paramètres distincts à respecter.)*
*Catégorie : configuration*

### D3240 — Divergence bullish = force pendant un déclin
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Une **divergence bullish** du Price Relative signale de la force relative pendant un déclin de prix. Les titres qui tiennent le mieux en déclin sont souvent les leaders au rebond du marché.
**TRADEX-AI C7** : signal anticipé de leadership ; détecter prix↓ + ratio↑.
*Catégorie : signal*

### D3241 — Exemple divergence bullish (DD:$SPX)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_04) : Dupont (DD) déclinait de fin avril à début juillet mais le Price Relative montait (force relative) ; DD est devenu leader au retournement de juillet. Prix et ratio ont cassé la résistance fin juillet (lignes bleues).
**TRADEX-AI C7** : pattern concret prix↓ / ratio↑ → leadership ultérieur ; cassure conjointe = confirmation.
*Catégorie : signal*

### D3242 — Divergence bearish = faiblesse pendant une hausse
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_05) : Une **divergence bearish** signale une faiblesse relative pendant une avance de prix ; ces titres mènent souvent à la baisse au retournement. Ex. Mastercard (MA:$SPX) : nouveau reaction high du prix fin avril non confirmé (ratio en lower high marqué) → forte baisse en mai.
**TRADEX-AI C7** : détecter prix↑ + ratio plat/↓ comme avertissement baissier.
*Catégorie : signal*

### D3243 — Application au broad market (rotation sectorielle)
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Le Price Relative s'applique aussi au marché large : 9 secteurs (sector SPDRs). Maintenir des Price Relatives par secteur identifie leaders et laggards.
**TRADEX-AI C7** : cadre de rotation transposable à un panier d'actifs (matières premières vs macro).
*Catégorie : structure_marche*

### D3244 — Mode offensif vs défensif du marché
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Le marché est en **mode offensif** quand technologie et consommation discrétionnaire mènent ; en **mode défensif** quand consommation de base, santé et services aux collectivités mènent.
**TRADEX-AI C7** : lecture de régime risk-on/risk-off par leadership sectoriel — utile pour le contexte macro (C4/C7) du projet.
*Catégorie : structure_marche*

### D3245 — Workflow secteurs → titres + confirmation
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Une fois les secteurs leaders identifiés, chercher les titres leaders dedans ; éviter les secteurs en faiblesse relative. **Confirmer** le Price Relative avec d'autres outils (oscillateurs de momentum, chart patterns).
**TRADEX-AI C7** : workflow top-down + obligation de confirmation (cohérent avec « 3/4 + 2/3 alignés »).
*Catégorie : gestion_risque_entree*

### D3246 — Ratio symbol : sémantique des valeurs
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Le ratio ticker représente la close du premier symbole divisée par la close du second (rappel FAQ).
**TRADEX-AI C7** : redéfinition compacte du ratio ; confirme D3233.
*Catégorie : structure_marche*

### D3247 — Pseudo-symboles $SECTOR / $INDUSTRY
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : Dans un ratio symbol, les pseudo-symboles **$SECTOR** et **$INDUSTRY** sont automatiquement remplacés par l'ETF/index de secteur/industrie approprié (ex. « IBM:$SECTOR » ≡ « IBM:XLK »).
**TRADEX-AI C7** : fonctionnalité propre à StockCharts ; tag 🟡 (convention plateforme), non transposable telle quelle hors SharpCharts.
*Catégorie : configuration*

### D3248 — Placement du tracé (behind price) + construction SharpCharts
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md, image_06, image_07) : Le Price Relative se construit via l'indicateur « Price » + un ratio ticker (base + « : » + comparatif). Plaçable au-dessus, en dessous ou **derrière** le prix ; « behind price » facilite la comparaison des deux lignes. Ex. : divergence bullish en août, bearish en décembre.
**TRADEX-AI C7** : détail d'affichage SharpCharts ; tag 🟡 (convention plateforme). La logique (ratio + divergences) reste 🟢 transposable.
*Catégorie : configuration*

### D3249 — FAQ : noms alternatifs et portée
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : FAQ confirme : aussi appelé **Relative Strength Indicator / Relative Strength Comparative** ; utilisable au-delà des titres individuels (analyse de marché large, leaders/laggards sectoriels) ; usage courant = titre vs benchmark (S&P 500) ou vs secteur/industrie.
**TRADEX-AI C7** : consolide la nomenclature ; lever l'ambiguïté avec le RSI de Wilder (tag 🟡 sur le nom « Relative Strength »).
*Catégorie : structure_marche*

### D3250 — Références : Murphy (inter-marché) et Pring
🟢 **FAIT VÉRIFIÉ** (Source : price_relative_relative_strength.md) : John Murphy (*Technical Analysis of the Financial Markets*) traite la force relative dans le chapitre **inter-marché** (force relative sectorielle et sur titres). Martin Pring (*Technical Analysis Explained*) consacre un chapitre à la force relative et à sa combinaison avec d'autres indicateurs.
**TRADEX-AI C7** : ancrage bibliographique inter-marché (Murphy) ; tag 🔵 ÉCOLE. Renforce le rattachement au Cercle C7.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D3231 → D3250 (20) |
| Faits vérifiés 🟢 | 20 |
| Tags secondaires | 🔵 ÉCOLE (D3250 Murphy/Pring) · 🟡 CONVENTION (D3247, D3248 SharpCharts ; D3249 nom « Relative Strength » ≠ RSI Wilder) |
| Cercle dominant | C7 (corrélations / inter-marché) |
| Images | 7/7 certifiées |
| Actifs cibles | GC · HG · CL · ZW (ratios inter-marché, ex. HG:GC, GC:DX) |
| Belkhayate | NON CONCERNÉ (indicateur inter-marché classique, aucun lien propriétaire) |
| Cas à vérifier | D3239 — distinguer SMA 15j (exemple) vs SMA 150j (seuil long terme) lors du codage ; lever l'ambiguïté nom « Relative Strength » vs RSI Wilder (D3249) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
