# Extraction StockCharts — TA 101 Part 3
**Source :** `bundles/stockcharts/ta_101_part_3.md` (HTTP 200) + 1 image certifiée
**Méthode images :** double ancrage · 1/1 certifiées · 0 à vérifier
**Décisions :** D4211 → D4230 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis-101/ta-101-part-3
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : fondements de la validité des signaux AT appliqués à GC/HG/CL/ZW/ES/VX/DX — liquidity gate, news gate, données ajustées.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Chart showing sections of a SharpChart | Chart Construction | D4220 |

## DÉCISIONS

### D4211 — Tick data : source primaire de toute analyse de prix
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les exchanges enregistrent le prix et le nombre de parts pour chaque transaction — c'est la donnée tick. Cette donnée est compilée sur différentes périodes pour construire des barres de prix (OHLC) avec des timeframes allant de 1 minute à 1 an.
**TRADEX-AI C1** : NT8 fournit les données OHLC compilées depuis le tick — toute barre GC/HG/CL/ZW est construite sur ce même principe; la granularité (range bars vs daily) doit correspondre au timeframe d'analyse.
*Catégorie : structure_marche*

### D4212 — Barres intraday : usage traders court terme
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les barres de prix inférieures à un jour (1 min à 1 heure) sont appelées intraday et utilisées typiquement par les day traders qui tiennent des positions de minutes à heures.
**TRADEX-AI C1** : TRADEX-AI opère sur range bars NT8 — aligné avec la logique intraday; les signaux GC/HG/CL/ZW ciblant des entrées courtes s'appuient sur des barres de même nature.
*Catégorie : timing*

### D4213 — Barre journalière : standard investisseurs moyen/long terme
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Une barre de prix journalière est construite à partir de toutes les transactions d'une journée complète de trading. Les investisseurs tenant des positions de jours à années utilisent le plus souvent les barres journalières.
⚫ **HYPOTHÈSE PROJET** : Le backtest COG Belkhayate sur daily (sessions S11) a été invalidé précisément parce que la méthode Belkhayate est calibrée pour range bars NT8, pas pour daily — ce fait source confirme l'incompatibilité conceptuelle.
**TRADEX-AI C1** : Validation range bars NT8 Phase C obligatoire avant tout signal GC/HG/CL/ZW.
*Catégorie : timing*

### D4214 — Volume : donnée tick compilée en barres de volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Le volume en nombre de parts échangées est enregistré comme donnée tick au même titre que le prix. Les données de volume tick sont additionnées pour construire des barres de volume, puis représentées graphiquement avec leurs barres de prix correspondantes.
**TRADEX-AI C2** : Le volume agrégé est la base de l'order flow ATAS (footprint, delta, big trades) pour GC/HG/CL/ZW — la donnée brute est toujours une somme de ticks.
*Catégorie : volume_liquidite*

### D4215 — Indices : non tradables, rôle confirmatoire
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les indices sont fournis par des sociétés de services financiers et les grandes bourses. Les indices NE SONT PAS des instruments financiers tradables. Ils représentent des moyennes de marché, des industries, des matières premières, des devises, des obligations et d'autres mesures.
**TRADEX-AI C3/C4** : Cohérent avec la classification TRADEX — ES, VX, DX sont utilisés en CONFIRMATION uniquement, jamais pour exécuter un ordre.
*Catégorie : structure_marche*

### D4216 — Indices de breadth : mesure du sentiment de marché
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les indices de breadth mesurent combien d'instruments évoluent à l'intérieur d'un indice de marché particulier. Les indices de breadth donnent aux analystes un aperçu du sentiment des investisseurs. Exemples : NASDAQ Advance-Decline Issues, NYSE Advance-Decline Volume.
**TRADEX-AI C5** : VX (VIX) est un indice de sentiment de même nature — mesure la "breadth" de la peur; renforce son rôle de filtre dans le cercle C5.
*Catégorie : psychologie*

### D4217 — Condition 1 de validité AT : haute liquidité obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Première hypothèse clé de l'analyse technique : la haute liquidité. La liquidité = volume. Cela signifie que les instruments ont la capacité de se trader rapidement sans affecter dramatiquement les prix. Sur un actif illiquide, le broker doit souvent modifier significativement le prix pour trouver vendeur ou acheteur.
**TRADEX-AI C2** : GC (Or), HG (Cuivre), CL (Pétrole WTI), ZW (Blé) sont tous des futures CME/CBOT à haute liquidité — condition remplie; le staleness monitor vérifie la fraîcheur des données, proxy de liquidité active.
*Catégorie : volume_liquidite*

### D4218 — Piège des actifs illiquides : manipulation de prix possible
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les actions à faible liquidité (souvent inférieures à 1 cent) peuvent voir leur prix manipulé par quelqu'un disposant de ressources importantes. Les principes sur lesquels l'analyse technique est fondée supposent que seules les forces normales du marché font bouger les prix.
⚫ **HYPOTHÈSE PROJET** : Ce risque est absent sur GC/HG/CL/ZW (futures CME à haute liquidité) — confirme que les actifs TRADEX sont correctement sélectionnés.
**TRADEX-AI C2** : Aucun actif TRADEX n'entre dans la catégorie illiquide — la condition de validité AT est structurellement remplie.
*Catégorie : volume_liquidite*

### D4219 — Condition 2 de validité AT : pas de changements de prix artificiels
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Deuxième hypothèse clé : les prix ne peuvent pas être modifiés par des forces autres que la peur et la cupidité qui animent le marché. Les splits, dividendes et distributions constituent des exemples de changements "artificiels" qui faussent les charts et tous les indicateurs techniques (signal baissier fictif sur split 2-for-1 avec gap -50%).
🟡 **SYNTHÈSE** : Pour les futures GC/HG/CL/ZW, cette problématique se manifeste via les rollovers de contrats (price gap artificiel entre contrats expirant et nouveau front month) — les données NT8 doivent utiliser des séries continues ajustées.
**TRADEX-AI C1** : Vérifier que NT8 utilise des séries continues adjusted (back-adjusted) pour GC/HG/CL/ZW afin d'éliminer les gaps de rollover artificiels dans l'analyse Belkhayate.
*Catégorie : gestion_risque_entree*

### D4220 — Condition 3 de validité AT : pas de news extrêmes
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md, image_01) : Troisième hypothèse clé : l'analyse technique ne peut pas prédire des événements extrêmes comme le décès inattendu d'un PDG ou la tragédie du 11 septembre. Quand une "news extrême" survient, les techniciens doivent attendre patiemment que le chart se stabilise et commence à refléter le "nouveau normal".
**TRADEX-AI C6** : Justification directe du News Gate TRADEX (blocage 30 min avant NFP/FOMC/CPI) — les événements macro extrêmes cassent les fondements de l'AT; ce garde-fou est théoriquement validé par StockCharts.
*Catégorie : macro_evenements*

### D4221 — News extrêmes : les signaux AT sont invalides pendant la période de perturbation
🟡 **SYNTHÈSE** (Source : ta_101_part_3.md) : StockCharts précise que ce n'est pas que les charts deviennent inutiles, mais que les "fondements philosophiques des signaux et des patterns AT traditionnels disparaissent" pendant les événements extrêmes. Les prédictions standard ne peuvent pas être utilisées avec précision dans ces circonstances.
**TRADEX-AI C6** : Le News Gate TRADEX doit être étendu au-delà du seul blocage 30min pré-event — inclure une période post-event d'attente jusqu'à "stabilisation" (critère à définir par volatilité ou return-to-mean).
*Catégorie : macro_evenements*

### D4222 — Structure d'un chart : zones prix, volume et indicateurs
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md, image_01) : Un SharpChart comprend : une zone Price Plot Area (prix + overlays), une zone Indicator Panel (indicateurs non exprimés en prix), des axes date/temps. Les overlays sont des indicateurs techniques normalement exprimés en termes de prix. Les indicateurs non-prix sont tracés dans des panneaux séparés.
**TRADEX-AI C1** : Architecture standard — Belkhayate BGC/Direction/Energie/Pivots = overlays sur price plot; momentum/volume = indicator panels séparés dans le dashboard TRADEX.
*Catégorie : structure_marche*

### D4223 — Indicateur technique : définition formelle
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Un indicateur technique est une expression mathématique du prix et/ou du volume qui peut fournir un aperçu des mouvements de prix futurs.
🔵 **ÉCOLE** (StockCharts) : Cette définition englobe tous les outils Belkhayate (COG, Direction, Energie, Pivots) qui sont des transformations mathématiques du prix/volume.
**TRADEX-AI C1** : Les 7 cercles d'intelligence TRADEX sont tous des "indicateurs techniques" au sens StockCharts — leur validité présuppose les 3 conditions (liquidité, prix non-artificiels, pas de news extrêmes).
*Catégorie : indicateurs_tendance*

### D4224 — Données intraday : spécifiques aux day traders
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les barres intraday (1 minute à 1 heure) sont typiquement utilisées en analyse technique par les day traders qui tiennent des positions de minutes à heures.
🟡 **SYNTHÈSE** : TRADEX-AI vise des entrées de type "day/swing" sur futures — les range bars NT8 (équivalent fonctionnel aux barres intraday) sont le timeframe approprié à la méthode Belkhayate.
**TRADEX-AI C1** : Confirmation du choix range bars NT8 plutôt que daily pour GC/HG/CL/ZW — cohérent avec le profil day/swing trader.
*Catégorie : timing*

### D4225 — L'AT a des limites : elle ne peut pas tout prédire
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : L'AT ne peut pas prédire des événements extrêmes. Ce n'est pas que les charts deviennent inutiles dans ces cas, mais que les fondements philosophiques des signaux disparaissent.
**TRADEX-AI C6** : Positionnement éducatif obligatoire dans le disclaimer TRADEX — "Signal basé sur AT, ne prédit pas les événements extrêmes" doit être visible en permanence dans l'interface.
*Catégorie : psychologie*

### D4226 — Volume tick = additionné pour construire barres de volume
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les données tick de volume sont additionnées ensemble pour construire des barres de volume, puis représentées graphiquement avec leurs barres de prix correspondantes pour l'analyse technique.
🟡 **SYNTHÈSE** : Le volume agrégé par barre est la même information que "volume par barre range" dans NT8 — ATAS y ajoute la dimension directionnelle (delta = volume achat - volume vente).
**TRADEX-AI C2** : Le volume simple (barres NT8) est la base; ATAS ajoute la directionnalité pour le C2 order flow — les deux niveaux sont nécessaires pour GC/HG/CL/ZW.
*Catégorie : volume_liquidite*

### D4227 — Breadth : insight sur le sentiment investisseur
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les indices de breadth (ex: Advance-Decline) donnent aux analystes un aperçu du sentiment des investisseurs en mesurant combien d'instruments évoluent à l'intérieur d'un indice.
🟡 **SYNTHÈSE** : Le Put/Call ratio et le Fear&Greed index (C5 TRADEX) remplissent la même fonction de "breadth sentiment" pour les matières premières que les indices Advance-Decline pour les actions.
**TRADEX-AI C5** : Valide l'usage de métriques breadth-like (Put/Call, Fear&Greed) dans le cercle C5 pour filtrer les signaux GC/HG/CL/ZW.
*Catégorie : psychologie*

### D4228 — Les 3 conditions de validité AT : conditions cumulatives
🟡 **SYNTHÈSE** (Source : ta_101_part_3.md) : Les trois hypothèses clés (haute liquidité, pas de prix artificiels, pas de news extrêmes) sont présentées comme des prérequis cumulatifs. Si l'une est violée, "les fondements philosophiques des signaux et patterns AT traditionnels disparaissent".
**TRADEX-AI C1/C6** : Les 3 garde-fous TRADEX (staleness monitor = liquidité, données continues ajustées = pas de prix artificiels, news gate = pas de news extrêmes) correspondent exactement aux 3 conditions StockCharts — architecture TRADEX théoriquement solide.
*Catégorie : gestion_risque_entree*

### D4229 — Indices de commodités dans les indices financiers
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md) : Les indices représentent "des matières premières, des devises, des obligations et de nombreuses autres mesures de l'activité de marché" — pas seulement les actions.
**TRADEX-AI C4** : DX (Dollar Index) et les indices de commodités (ex: CRB) relèvent de cette catégorie — leur analyse technique suit les mêmes principes, validant leur usage en confirmation pour GC/HG/CL/ZW.
*Catégorie : correlations*

### D4230 — Structure chart : axes temporels multiples possibles
🟢 **FAIT VÉRIFIÉ** (Source : ta_101_part_3.md, image_01) : Des axes date/temps additionnels peuvent être ajoutés entre les panneaux d'indicateurs si nécessaire. Le dashboard peut afficher plusieurs panneaux d'indicateurs au-dessus et en dessous de la zone de prix.
**TRADEX-AI C1** : Le dashboard TRADEX (React + maquettes f1-f8) doit permettre l'affichage multi-panel — aligné avec la structure SharpChart décrite; chaque cercle d'intelligence (C1-C7) peut occuper un panneau distinct.
*Catégorie : structure_marche*
