# Extraction StockCharts — Renko Charts
**Source :** `bundles/stockcharts/renko_charts.md` (HTTP 200 · ~12 300 car.) + 10 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 10/10 certifiées
**Décisions :** D3431 → D3450 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/renko-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Traditional bar chart with a uniform data axis. | Construction and Characteristics of Renko Charts | CERTIFIE (accord .md + HTML) |
| image_02.png | Renko chart for the same time frame as the bar chart (irregular date axis, less choppy) | Construction and Characteristics of Renko Charts | CERTIFIE (accord .md + HTML) |
| image_03.png | Renko chart based on closing prices. | Close Versus High-Low Range | CERTIFIE (accord .md + HTML) |
| image_04.png | Renko chart based on the high-low range. | Close Versus High-Low Range | CERTIFIE (accord .md + HTML) |
| image_05.png | Fixed Value versus ATR | Fixed Value versus ATR [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | Renko chart when the ending ATR value is low. | Fixed Value versus ATR | CERTIFIE (accord .md + HTML) |
| image_07.png | Renko chart when the ending ATR value is high. | Fixed Value versus ATR | CERTIFIE (accord .md + HTML) |
| image_08.png | Trends, Support, and Resistance | Trends, Support, and Resistance [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_09.png | Renko chart for QQQ | Renko Charts In SharpCharts | CERTIFIE (accord .md + HTML) |
| image_10.png | SharpChart settings for Renko charts. | Renko Charts In SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3431 — Nature : graphique prix-pur ignorant le temps, briques de valeur fixe (origine Japon)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : « Renko charts originated in Japan. The charts ignore time and focus solely on price changes that meet a minimum requirement. » Au lieu de colonnes X/O (Point & Figure), le Renko utilise des « bricks » représentant un mouvement de prix fixe (aussi appelées blocks ou boxes), qui montent ou descendent en lignes à 45° avec une brique par colonne verticale.
**TRADEX-AI C1** : Type de graphique prix-pur (sans axe temps régulier) ; conceptuellement proche des range bars NT8 utilisées par Belkhayate (mode Rapide Range Bar 4-5t). ⚫🔴 écho possible — à ne pas assimiler directement à Belkhayate.
*Catégorie : structure_marche*

---

### D3432 — Couleurs : briques creuses (hausse) vs pleines/noires (baisse)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Les briques de mouvements haussiers sont creuses (hollow), celles de mouvements baissiers sont pleines d'une couleur solide (typiquement noir).
**TRADEX-AI C1** : Codage couleur directionnel déterministe (hausse/baisse) ; sert à lire la Direction Belkhayate de façon binaire sur un flux prix-pur. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3433 — Filtrage : briques de valeur fixe filtrent les petits mouvements
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Les Renko reposent sur des briques de valeur fixe qui filtrent les plus petits mouvements de prix. Contrairement à un chart bar/line/candlestick à axe date uniforme (un point par jour/semaine), le Renko ignore le temps et ne se concentre que sur les variations de prix.
**TRADEX-AI C1** : Filtrage du bruit de prix par seuil fixe = même principe que les range bars NT8 (Belkhayate Rapide) ; pertinent pour réduire le bruit avant scoring. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3434 — Règle de tracé : nouvelle brique seulement si le mouvement ≥ taille de brique
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Si la valeur de brique est fixée à 10 points, un mouvement de 10 points ou plus est requis pour tracer une nouvelle brique. Les mouvements < 10 points sont ignorés et le Renko reste inchangé.
**TRADEX-AI C1** : Règle déterministe de construction (seuil = box size) ; identique au paramétrage de range bars (taille en ticks) côté NT8. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3435 — Exemple S&P 500 10-pt : avance de 9 pts → aucune brique ; 10 pts → brique (1840→1850)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Sur un Renko S&P 500 10 points, une avance de 9 points (1840→1849) ne dessine pas de brique. Si le S&P avance à 1850 le lendemain, une brique est tracée (mouvement ≥ 10 pts), de 1840 à 1850, creuse/blanche. À l'inverse, un déclin de 1840 à 1830 trace une brique pleine/noire.
**TRADEX-AI C1** : Illustration chiffrée de la règle de seuil ; confirme le mécanisme box-size sans introduire de paramètre TRADEX. Valeur pédagogique. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3436 — Effet visuel : axe date irrégulier, price action moins choppy
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_01, image_02) : Sur six mois, le Renko a un axe date irrégulier et une price action moins choppy parce qu'il ignore les mouvements < 10 points ; il reste inchangé jusqu'à un mouvement d'au moins 10 points.
**TRADEX-AI C1** : Conséquence directe du filtrage : lecture de tendance plus lisse ; bénéfique pour la lisibilité Direction/BGC Belkhayate, mais l'axe temps déformé complique le calage news/macro (C4). ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3437 — Close vs High-Low : deux modes de construction (champ « field »)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_03, image_04) : Les Renko peuvent se baser sur les prix de clôture ou sur le high-low range via le réglage « field ». Clôture = un point de données par période, moins de volatilité. High-low range = deux points en jeu, plus de fluctuations donc plus de briques. Le Renko high-low fluctue plus que le close-only.
**TRADEX-AI C1** : Choix de mode (close vs high-low) = paramètre de sensibilité ; à figer pour TRADEX selon le besoin (close = plus stable, high-low = plus réactif). Recoupe le compromis sensibilité des range bars. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3438 — Box size en valeur fixe : taille de brique constante même avec nouvelles données
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Avec le réglage « box » en valeur fixe (point value), la taille de brique reste constante même quand de nouvelles données entrent. Les deux charts S&P 500 (10 pts) sont en valeur fixe.
**TRADEX-AI C1** : Mode déterministe stable (box fixe = paramètre constant) ; préférable pour la reproductibilité d'un backtest/scoring TRADEX vs le mode ATR variable. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3439 — Box size en ATR : taille de brique fluctuante (ATR 14 par défaut)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_05) : En ATR, la taille de brique fluctue. L'ATR par défaut est sur 14 périodes et varie dans le temps ; la taille de brique est basée sur l'ATR au moment de création du chart. Si l'ATR change le lendemain, la nouvelle valeur ATR sert à fixer la taille de brique.
**TRADEX-AI C1** : Mode adaptatif à la volatilité (ATR-based) ; lien direct avec l'ATR du projet (proxy Énergie discuté). Variabilité = risque de non-reproductibilité du backtest. ⚫🔴 écho possible — à arbitrer.
*Catégorie : structure_marche*

---

### D3440 — ATR Renko basé sur charts standards ; écart possible avec l'ATR affiché (arrondis)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Les valeurs ATR sont basées sur des charts standards (close-only, bar, candlestick) à un point par période et axe date uniforme. L'ATR affiché sur ces charts peut différer de l'ATR-brick d'un Renko à cause d'arrondis.
**TRADEX-AI C1** : Garde-fou : l'ATR servant à dimensionner les briques n'égale pas exactement l'ATR lu sur le chart standard ; à documenter si TRADEX dérive un box size d'un ATR. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3441 — Exemple ATR : fin 10 juin ATR=12.05 ; fin 15 avril ATR=20.55 (briques plus grosses)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_06, image_07) : Premier chart finissant le 10 juin → ATR 12.05 (valeur de chaque brique). Second finissant le 15 avril → ATR 20.55. La valeur de brique change avec l'ATR ; les briques du 15 avril valent bien plus que celles du 10 juin.
**TRADEX-AI C1** : Démonstration chiffrée de la dépendance brick-size ↔ date de fin en mode ATR ; confirme la non-reproductibilité évoquée en D3439. Valeur pédagogique. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3442 — Briques et MA : la MA se calcule sur les valeurs Renko, pas sur les jours de bourse
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_08) : Sur un Renko S&P 500 daily 10 pts avec SMA 10 périodes : la SMA 10 se base sur les 10 dernières valeurs Renko, PAS sur les 10 derniers jours de bourse. Un indicateur sur Renko se base sur les valeurs Renko et diffère de celui d'un bar chart. On peut typiquement utiliser des MA plus courtes sur Renko car les petits mouvements ont été filtrés.
**TRADEX-AI C1** : Avertissement critique : tout indicateur (MA, MFI/Énergie, etc.) calculé sur un flux Renko/range bars n'a PAS la même base temporelle qu'un indicateur daily. Impacte directement le calcul de l'« Énergie » Belkhayate si appliqué sur range bars NT8. ⚫🔴 écho fort — à trancher.
*Catégorie : indicateurs_momentum*

---

### D3443 — Tendances : briques blanches (hausse) / noires (baisse), creux=support, pics=résistance
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Les briques blanches se forment quand le prix monte d'un certain montant, les noires quand il baisse. Les troughs peuvent marquer des supports, les peaks des résistances.
**TRADEX-AI C1** : Lecture directe support/résistance sur Renko ; recoupe l'usage des pivots/zones Belkhayate comme niveaux opératoires, mais via géométrie de briques. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3444 — Signal de retournement : reversal à deux briques (two-brick reversal)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : On peut chercher un « two-brick reversal » pour signaler un changement de tendance. Exemple : l'indice chute avec cinq briques noires (août, puis sept-oct) ressemblant à des falling flags ; un reversal survient quand deux briques blanches se forment et cassent au-dessus de la résistance court terme.
**TRADEX-AI C1** : Règle de signal déterministe (2 briques contraires = retournement) codable sur un flux Renko/range bars ; candidate comme configuration analytique, jamais ordre automatique. ⚫🔴 écho possible.
*Catégorie : signal*

---

### D3445 — Fibonacci applicable sur Renko
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : « Chartists can also apply the Fibonacci Retracements Tool to Renko charts. »
**TRADEX-AI C1** : Compatibilité Fibonacci sur Renko ; cohérent avec les retracements 33-50 % évoqués ailleurs (règles Rhodes) et l'usage Fibonacci dans la KB. Outil analytique, pas un signal autonome. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3446 — Synthèse : filtre le bruit comme Kagi/Three Line Break, repère highs/lows et S/R
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Comme leurs « cousins » japonais (Kagi, Three Line Break), les Renko filtrent le bruit en se concentrant sur les variations minimales de prix ; aucune brique sans mouvement d'un montant spécifique. Comme le Point & Figure, il est facile de repérer les highs/lows importants et les niveaux clés de support/résistance.
**TRADEX-AI C1** : Positionnement du Renko dans la famille des charts prix-pur filtrants ; conforte l'intérêt pour un flux débruité avant scoring Belkhayate. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3447 — Identification de tendance : higher highs/lows (up) vs lower lows/highs (down), à confirmer
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Avec cette information, on identifie des uptrends (higher highs / higher lows) ou downtrends (lower lows / lower highs). Comme pour toute technique, le chartiste doit employer d'autres outils techniques pour confirmer ou réfuter ses conclusions sur Renko.
**TRADEX-AI C1** : Définition structurelle de tendance (HH/HL vs LL/LH) + exigence de confirmation multi-outils ; cohérent avec la règle multi-cercles du projet (jamais un seul signal). ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3448 — Paramétrage SharpCharts : Chart Type = Renko, choix points/ATR, field close/high-low, couleurs
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md, image_10) : Créer un Renko via Attributes → Chart Type = Renko, choisir entre points ou ATR, régler les paramètres. L'ATR utilise l'Average True Range du bar chart sous-jacent pour une valeur « Automatic » de box size (peut changer si le prix change → modification significative du Renko à chaque mise à jour). Le « Renko Price Field » se règle sur close ou high-low (high-low = plus de sensibilité). Couleurs via Up Color / Down Color.
**TRADEX-AI C1** : Procédure d'outil (StockCharts) ; sans portée algorithmique directe, mais documente les deux axes de paramétrage (box source + price field + couleur) à répliquer si TRADEX implémente un Renko. ⚫🔴 écho possible.
*Catégorie : structure_marche*

---

### D3449 — Garde-fou « AT LIMIT » : box size trop petit → agrandi automatiquement, message affiché
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Si « AT LIMIT » apparaît en haut d'un chart, le box size spécifié donnerait un chart trop grand à afficher ; StockCharts augmente alors le box size au plus petit affichable et ajoute le message « AT LIMIT ». FAQ : avec un box size ATR, la taille est calculée automatiquement et peut changer en cours de journée, faisant évoluer le chart.
**TRADEX-AI C1** : Garde-fou de rendu propre à l'outil + rappel que le mode ATR fait muter le chart en intra-journée (cohérent D3439/D3441) ; à retenir pour la stabilité du flux de décision TRADEX. ⚫🔴 écho possible.
*Catégorie : gestion_risque_entree*

---

### D3450 — Source de référence : Nison, « Beyond Candlesticks » (chapitre Renko)
🟢 **FAIT VÉRIFIÉ** (Source : renko_charts.md) : Le livre « Beyond Candlesticks » de Steve Nison consacre un chapitre entier aux Renko ; il couvre aussi Three Line Break, Kagi, et l'usage des moyennes mobiles par les traders japonais.
**TRADEX-AI C1** : Référence bibliographique (Nison) ; sans règle de trading propre, fournit une piste de source d'enrichissement future. 🟡 CONVENTION / méta. ⚫ NON CONCERNÉ (Belkhayate).
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3431 | Nature : prix-pur, briques fixes, origine Japon | 🟢 ⚫🔴 | C1 | structure_marche |
| D3432 | Couleurs : creuses (hausse) / pleines (baisse) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3433 | Filtrage des petits mouvements par seuil fixe | 🟢 ⚫🔴 | C1 | structure_marche |
| D3434 | Règle tracé : brique si mouvement ≥ box size | 🟢 ⚫🔴 | C1 | structure_marche |
| D3435 | Exemple S&P 500 10 pts (9 pts rien / 10 pts brique) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3436 | Axe date irrégulier, price action moins choppy | 🟢 ⚫🔴 | C1 | structure_marche |
| D3437 | Close vs High-Low (sensibilité) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3438 | Box fixe : taille constante (reproductible) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3439 | Box ATR : taille fluctuante (ATR 14) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3440 | ATR Renko ≠ ATR chart standard (arrondis) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3441 | Exemple ATR 12.05 vs 20.55 selon date de fin | 🟢 ⚫🔴 | C1 | structure_marche |
| D3442 | MA/indicateurs sur valeurs Renko, pas sur jours | 🟢 ⚫🔴 | C1 | indicateurs_momentum |
| D3443 | Briques blanches/noires, creux=support pics=résistance | 🟢 ⚫🔴 | C1 | structure_marche |
| D3444 | Two-brick reversal = signal de retournement | 🟢 ⚫🔴 | C1 | signal |
| D3445 | Fibonacci applicable sur Renko | 🟢 ⚫🔴 | C1 | structure_marche |
| D3446 | Famille prix-pur filtrante (Kagi/3LB/P&F) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3447 | Tendance HH/HL vs LL/LH, confirmer multi-outils | 🟢 ⚫🔴 | C1 | structure_marche |
| D3448 | Paramétrage SharpCharts (points/ATR, field, couleurs) | 🟢 ⚫🔴 | C1 | structure_marche |
| D3449 | Garde-fou « AT LIMIT » + mutation intra ATR | 🟢 ⚫🔴 | C1 | gestion_risque_entree |
| D3450 | Référence Nison « Beyond Candlesticks » (🟡⚫) | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** Le Renko est un type de graphique prix-pur StockCharts. Il n'est PAS un élément de la méthode Belkhayate au sens strict (⚫), MAIS il présente un **écho fort et explicite avec les range bars NT8** utilisées par Abdelkrim (mode Rapide Range Bar 4-5t, mémoire projet) : même principe de filtrage du temps et du bruit par un seuil de prix fixe en ticks (⚫🔴 — écho possible/probable, à confirmer côté NT8). Point d'attention majeur : D3442 (indicateurs calculés sur valeurs Renko/range bars ≠ valeurs daily) impacte directement le calcul de l'« Énergie » Belkhayate = MFI standard si appliqué sur range bars — cohérent avec l'arbitrage Énergie non tranché du projet.

**À vérifier (humain) :**
- Écho Renko ↔ range bars NT8 : confirmer que le box size Renko correspond bien à la taille de range bar (4-5 ticks) employée par Belkhayate, ou si ce sont deux constructions distinctes (range bar NT8 ≠ Renko brick exactement).
- D3439/D3441/D3449 : trancher box FIXE (reproductible, recommandé pour backtest/scoring) vs box ATR (adaptatif mais non reproductible intra-journée) pour TRADEX.
- D3442 (crucial) : décider sur quelle base temporelle l'Énergie/MFI et les MA sont calculés si TRADEX opère sur range bars/Renko — recoupe l'arbitrage Énergie en suspens.
- D3437 : choisir close vs high-low pour le flux TRADEX (stabilité vs réactivité).
- Tous les exemples chiffrés (S&P 500 10 pts, ATR 12.05/20.55) = illustratifs daily, non transposables en paramètres GC/HG/CL/ZW.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
