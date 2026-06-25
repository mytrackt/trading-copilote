# Extraction StockCharts — Donchian Trading Guidelines
**Source :** `bundles/stockcharts/donchian_trading_guidelines.md` (HTTP 200 · ~9 400 car.) + 5 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 5/5 certifiées
**Décisions :** D1511 → D1524 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/donchian-trading-guidelines
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Donchian Trading Guideline: narrow range → volume increase | 2. Volume confirme la direction | CERTIFIE (accord .md + HTML) |
| image_02.png | A broad market advance will likely continue when transports lead | 10. Transports mènent | CERTIFIE (accord .md + HTML) |
| image_03.png | After an initial advance, a consolidation → another advance of equal proportions | Technique 1. Consolidation = mesure | CERTIFIE (accord .md + HTML) |
| image_04.png | Major trendlines define the longer trend; minor trendlines the shorter | Technique 5. Tendances majeures/mineures | CERTIFIE (accord .md + HTML) |
| image_05.png | Volume peaks often signals the end of a long move | Technique 7. Climax de volume | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1511 — Origine : Donchian, père du trend following
🔵 **ÉCOLE (Richard Donchian)** (Source : donchian_trading_guidelines.md) : Publiées pour la première fois en 1934, beaucoup des 20 règles de trading de Richard Donchian restent pertinentes aujourd'hui. Considéré par beaucoup comme le père du trend following (suivi de tendance), Donchian a développé l'un des premiers systèmes basés sur deux moyennes mobiles différentes (avant-gardiste au début des années 1930). Les 20 règles se répartissent en deux groupes : générales et techniques.
**TRADEX-AI C1** : Cadre de **suivi de tendance** historique (école trend following). Corpus pertinent pour des actifs futures tendanciels (GC/HG/CL/ZW). À traiter comme principes, pas comme système clé-en-main.
*Catégorie : structure_marche*

---

### D1512 — Règle générale 1 : sentiment de foule excessif retarde le mouvement
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Être prudent à l'achat quand la foule est excessivement haussière, ou à la vente quand elle est excessivement baissière. Même quand la foule a raison, un sentiment excessif dans une direction peut retarder le mouvement.
**TRADEX-AI C5** : Filtre de sentiment contrarien : un extrême de sentiment ne valide pas une entrée immédiate. Transposable au cercle Sentiment (VIX, Put/Call) comme garde-fou de timing.
*Catégorie : timing*

---

### D1513 — Règle générale 2 : volume confirme la sortie de range étroit
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md, image_01) : Quand les prix évoluent dans une plage étroite avec peu de volatilité, chercher une augmentation de volume pour confirmer la direction du prochain mouvement. Une force ultérieure sur volume plus élevé est haussière ; une faiblesse ultérieure sur volume plus élevé est baissière.
**TRADEX-AI C2** : Règle de confirmation par le volume sur cassure de range — directement transposable (ATAS/volume). Sortie de range à valider par expansion de volume avant signal.
*Catégorie : signal*

---

### D1514 — Règle générale 3 : laisser courir les profits, couper les pertes (priorité absolue)
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Laisser courir les profits et couper court aux pertes. Cette règle prime sur toute autre règle (« overrides any other guideline » ; original : « irrespective of all other rules »).
**TRADEX-AI C1** : Principe de gestion de risque de plus haute priorité. À encoder comme invariant du risk_manager (asymétrie gains/pertes), supérieur aux autres règles.
*Catégorie : gestion_risque_entree*

---

### D1515 — Règles générales 4 et 5 : taille réduite en incertitude, ne pas courir après un mouvement de 3 jours
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : (4) Trader des montants plus petits en période d'incertitude ; pertes et whipsaws se réduisent en se concentrant sur des setups solides et des signaux robustes. (5) Ne pas courir après une position après un mouvement de trois jours ; attendre un retournement d'une journée (one-day reversal) pour améliorer le ratio risque/rendement.
**TRADEX-AI C1** : (4) Sizing réduit quand incertitude/staleness élevés. (5) Anti-poursuite : après 3 jours de mouvement, attendre un pullback d'1 jour pour un meilleur R/R — cohérent avec le seuil R/R ≥ 1:2 du projet.
*Catégorie : gestion_risque_entree*

---

### D1516 — Règle générale 6 : stop-loss adapté à la figure graphique
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Utiliser un stop-loss pour limiter les pertes et protéger les profits accumulés. Les stops doivent se baser sur la figure (pattern) en cours : un triangle aura une structure de stop différente d'un biseau ascendant ou d'une tête-épaules.
**TRADEX-AI C1** : Le placement du stop dépend de la structure de marché identifiée, pas d'une distance fixe. À articuler avec la logique de stop côté risk_manager.
*Catégorie : gestion_risque_entree*

---

### D1517 — Règle générale 7 : biais long plus large en uptrend (loi des pourcentages)
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Par la loi des pourcentages, les positions longues devraient être plus grandes que les positions courtes durant un uptrend large, en supposant que les hausses dépasseront les baisses dans une série de sommets/creux croissants. Un short de 50 à 40 rend 20 % ; un long de 40 à 50 rend 25 % : le gain en pourcentage des hausses est supérieur (version originale : déclin 50→25 = 50 %, avance 25→50 = 100 %).
**TRADEX-AI C1** : Asymétrie de sizing favorable au long en uptrend (raison mathématique). Modulateur de taille à articuler avec la direction de tendance dominante.
*Catégorie : gestion_risque_entree*

---

### D1518 — Règle générale 8 : ordres limites à l'entrée, ordres au marché à la sortie
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Utiliser des ordres limites pour initier une position ; utiliser des ordres au marché pour clôturer une position.
**TRADEX-AI C1** : Règle d'exécution directement implémentable côté NT8 ATI : entrée = limit order, sortie = market order. Pertinent pour l'exécution (mode Auto/Manuel).
*Catégorie : gestion_risque_entree*

---

### D1519 — Règle générale 9 : acheter la force relative, vendre la faiblesse relative
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md) : Acheter les titres en uptrend montrant de la force relative ; vendre les titres en downtrend montrant de la faiblesse relative. Ces deux règles restent subordonnées à toutes les autres règles.
**TRADEX-AI C7** : Sélection par force relative — transposable en lecture inter-marché/corrélations pour privilégier les actifs les plus forts (long) / faibles (short) dans la matrice 30j.
*Catégorie : structure_marche*

---

### D1520 — Règle générale 10 : confirmation par les valeurs de transport (Dow Transports)
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md, image_02) : Une hausse de marché large est plus susceptible de se poursuivre quand les valeurs de transport (Dow Transports) mènent ; elle est suspecte quand elles sont à la traîne. (Version originale : moves where rails lead.)
**TRADEX-AI C4** : Confirmation inter-marché de type Dow Theory (transports comme leader). Concept transposable en logique de confirmation, mais hors actifs TRADEX (GC/HG/CL/ZW) — référence macro.
*Catégorie : structure_marche*

---

### D1521 — Règle générale 11 : capitalisation/activité aussi importantes que les fondamentaux
🟡 **CONVENTION** (Source : donchian_trading_guidelines.md) : La capitalisation d'un titre, son niveau d'activité sur le marché et ses caractéristiques de trading sont aussi importants que ses fondamentaux. L'interprétation est difficile car le sens de « capitalisation » chez Donchian reste flou (souligné par la source elle-même).
**TRADEX-AI** : NON CONCERNÉ directement (notion actions/capitalisation, ambiguë selon la source). Valeur informative ; non transposable aux futures.
*Catégorie : structure_marche*

---

### D1522 — Règles techniques 1-2 : consolidation = mesure de mouvement et future S/R
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md, image_03) : (Tech.1) Une consolidation (range latéral) suivant une avance initiale mène souvent à une autre avance de proportion équivalente, puis un contre-mouvement vers la consolidation ; symétrique pour un déclin. (Tech.2) Une longue consolidation latérale après une avance marque une résistance future (attendre résistance/retournement baissier au retour) ; après un déclin, elle marque un support futur.
**TRADEX-AI C1** : (Tech.1) Objectif de prix par mesure (la consolidation projette un mouvement d'ampleur égale) — utilisable comme cible. (Tech.2) Les consolidations deviennent des niveaux S/R futurs.
*Catégorie : structure_marche*

---

### D1523 — Règles techniques 3-6 : trend lines, crawling, tendances majeures/mineures, triangles
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md, image_04) : (Tech.3) Chercher des opportunités d'achat quand le prix décline vers une trend line sur volume moyen/faible (vente symétrique) ; se méfier si le prix colle à la ligne ou si elle est touchée trop souvent. (Tech.4) Préparer une cassure baissière quand le prix décline vers une trend line haussière, ne rebondit pas et rampe le long ; symétrique haussier. Les contacts répétés augmentent la probabilité de cassure. (Tech.5) Les trend lines majeures définissent la tendance longue, les mineures la tendance courte : au-dessus d'une majeure (haussière), utiliser les mineures (baissières) pour les pullbacks et générer des achats sur cassure haussière. (Tech.6) Les triangles cassent généralement du côté plat : un triangle ascendant casse à la hausse, un descendant à la baisse.
**TRADEX-AI C1** : Boîte à outils trend-line : achat sur pullback vers support de tendance (volume faible), alerte cassure sur « crawling », hiérarchie tendance majeure/mineure, et biais de cassure des triangles (côté plat). Logiques transposables en règles de structure.
*Catégorie : structure_marche*

---

### D1524 — Règles techniques 7-9 : climax de volume, gaps, ajout après reversal 1 jour
🟢 **FAIT VÉRIFIÉ** (Source : donchian_trading_guidelines.md, image_05) : (Tech.7) Chercher un climax de volume signalant la fin d'un long mouvement (blow-off en sommet, selling climax en creux). (Tech.8) Tous les gaps ne se comblent pas : breakaway gap (début de tendance) et continuation gap ne se comblent pas, exhaustion gap (retournement) se comble — ne pas compter sur le comblement sans identifier le type de gap. (Tech.9) Durant une avance, initier/renforcer les longs après un déclin d'1 jour (surtout sur volume plus faible) ; durant un déclin, initier/renforcer les shorts après une avance d'1 jour, surtout sur volume plus faible. **Synthèse de la page** : trois thèmes — (1) la tendance sous-jacente détermine la préférence de position, (2) le volume est central (mouvements pro-tendance sur volume haut, contre-tendance sur volume bas, mais climax = fin de mouvement), (3) ranges/consolidations marquent réversals et S/R futurs.
**TRADEX-AI C2** : (Tech.7) Climax de volume = signal d'épuisement (ATAS). (Tech.8) Typologie des gaps avant tout pari sur comblement. (Tech.9) Ajout pro-tendance après pullback contre-tendance d'1 jour sur volume faible. Thèmes-clés : tendance + volume + consolidations.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1511 | Origine Donchian (trend following) | 🔵 ÉCOLE | C1 | structure_marche |
| D1512 | Gén.1 sentiment foule excessif | 🟢 | C5 | timing |
| D1513 | Gén.2 volume confirme cassure de range | 🟢 | C2 | signal |
| D1514 | Gén.3 laisser courir/couper (priorité) | 🟢 | C1 | gestion_risque_entree |
| D1515 | Gén.4-5 taille réduite + anti-poursuite 3j | 🟢 | C1 | gestion_risque_entree |
| D1516 | Gén.6 stop adapté à la figure | 🟢 | C1 | gestion_risque_entree |
| D1517 | Gén.7 biais long en uptrend (%) | 🟢 | C1 | gestion_risque_entree |
| D1518 | Gén.8 limit entrée / market sortie | 🟢 | C1 | gestion_risque_entree |
| D1519 | Gén.9 force/faiblesse relative | 🟢 | C7 | structure_marche |
| D1520 | Gén.10 transports (Dow Transports) | 🟢 | C4 | structure_marche |
| D1521 | Gén.11 capitalisation (ambigu) | 🟡 CONVENTION | C1 | structure_marche |
| D1522 | Tech.1-2 consolidation = mesure + S/R | 🟢 | C1 | structure_marche |
| D1523 | Tech.3-6 trend lines / triangles | 🟢 | C1 | structure_marche |
| D1524 | Tech.7-9 climax volume / gaps / ajout 1j | 🟢 | C2 | signal |

**Liens Belkhayate :** Donchian n'est PAS la méthode Belkhayate (⚫). Aucun lien direct revendiqué. Pertinence projet **élevée** néanmoins : corpus de trend following + règles de volume, stop et exécution directement utiles aux actifs futures tendanciels (GC/HG/CL/ZW) et à l'exécution NT8 ATI (D1518), en complément — non substitution — des règles d'entrée Belkhayate. Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D1520 — confirmation par Dow Transports : concept hors actifs TRADEX ; à n'utiliser qu'en lecture macro, pas comme critère du score /10.
- D1521 — règle « capitalisation » ambiguë (la source le reconnaît) et propre aux actions : marquée 🟡, NON transposable aux futures telle quelle.
- D1518 — règle d'exécution (limit entrée / market sortie) à confronter aux garde-fous d'exécution NT8 ATI déjà figés avant intégration.
- D1517 — biais de sizing long/short à articuler avec les règles de risque déjà verrouillées (ne pas créer de contradiction avec le risk_manager).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
