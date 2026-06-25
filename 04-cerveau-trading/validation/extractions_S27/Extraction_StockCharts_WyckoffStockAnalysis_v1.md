# Extraction StockCharts — Wyckoff Stock Analysis
**Source :** `bundles/stockcharts/wyckoff_stock_analysis.md` (HTTP 200) + 10 images certifiées
**Méthode images :** double ancrage · 10/10 certifiées · 0 à vérifier
**Décisions :** D4951 → D4970 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-stock-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Sélection d'actifs par force relative, patterns volume/prix pour entrées — applicable à GC/HG/CL/ZW dans le contexte ES/DX.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/0MwEcoIyRjvlSWKZSaEP | Wyckoff — 4 phases (accumulation/markup/distribution/markdown) | Four Phases | D4951 |
| /files/ROEt1uLYckuwLZr5AgET | Wyckoff — Buy points accumulation | Four Phases | D4952 |
| /files/ONR2zIPqJ1CFBAL1urCR | XLK vs SPY — relative strength Tech | Sector Group Behavior | D4954 |
| /files/MWxaLuc5mQIXsy4vMqux | XLF vs SPY — relative weakness Finance | Sector Group Behavior | D4955 |
| /files/gut40zChNz0KL8xgpZpI | Edison (ED) vs S&P 500 — relative strength | Relative Performance | D4956 |
| /files/ys6XUen5esplZZzmoUlX | Nucor (NUE) vs S&P 500 — relative weakness | Relative Performance | D4957 |
| /files/auMZi4nJYPO20Sro6GhP | Boeing (BA) — high volume springboard | High Volume Springboard | D4958 |
| /files/PbJ04Rh4h9m0HougX8aw | Gannet (GCI) — 50% retracement | 50% Retracement | D4960 |
| /files/Zn9WldzPyswLj2WxrNDC | Amgen (AMGN) — high volume consolidation | High Volume Consolidation | D4961 |
| /files/xrDAcqcglDvdZMvrW2Ug | Amgen P&F — Triple Top Breakout target | Risk-Reward and Stops | D4963 |

## DÉCISIONS

### D4951 — 4 phases Wyckoff : accumulation → markup → distribution → markdown
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/0MwEcoIyRjvlSWKZSaEP) : Wyckoff identifie 4 phases cycliques : accumulation (smart money achète), markup (tendance haussière), distribution (smart money vend), markdown (tendance baissière). La phase de l'actif détermine le type de position à initier.
**TRADEX-AI C1** : Avant tout signal TRADEX sur GC/HG/CL/ZW, identifier la phase actuelle (accumulation/markup/distribution/markdown) — les longs sont préférés en accumulation/markup, les shorts en distribution/markdown.
*Catégorie : structure_marche*

### D4952 — Long positions préférées en phase markup ; 5 points d'achat valides
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/ROEt1uLYckuwLZr5AgET) : En dehors du markup, les 5 points d'achat avec bon R/R : spring (agressif, risque élevé), cassure (trend follower), throwback, correction dans le markup, re-accumulation. Les positions longues sont évitées en distribution/markdown.
**TRADEX-AI C1** : Le mode Auto TRADEX ne génère de signaux ACHETER que si la phase identifiée est markup ou accumulation tardive — en distribution/markdown, seuls les signaux VENDRE ou ATTENDRE sont émis.
*Catégorie : gestion_risque_entree*

### D4953 — Short positions préférées en phase markdown ; patterns bearish inverses
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff n'évitait pas les positions short. En markdown : pic inférieur dans distribution (agressif), cassure de support sur volume (trend follower), throwback, re-distribution, rebond oversold 50%. Les patterns bullish ont leurs équivalents bearish exacts.
**TRADEX-AI C1** : TRADEX supporte les deux directions (ACHETER/VENDRE) sur GC/HG/CL/ZW — la direction est dictée par la phase Wyckoff de l'actif, pas par un biais directionnel fixe.
*Catégorie : gestion_risque_entree*

### D4954 — Sélection d'actifs : cibler d'abord le secteur en force relative
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/ONR2zIPqJ1CFBAL1urCR) : Wyckoff analysait d'abord les secteurs pour trouver ceux en force relative (haussier quand le marché est neutre, ou baissier lentement quand le marché chute). La technologie (XLK) montrait une force relative vs SPY en septembre-octobre 2011.
**TRADEX-AI C7** : La matrice de corrélations live (C7) de TRADEX joue le rôle de sélecteur de secteur Wyckoff — l'actif TRADING le plus en force relative vs ES sur 30j est celui à privilégier pour les signaux d'achat.
*Catégorie : correlations*

### D4955 — Force relative : 3 manifestations (avance plus vite, avance en range, tient en correction)
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/gut40zChNz0KL8xgpZpI) : Un actif montre une force relative quand : 1) il avance plus vite que l'indice, 2) il avance quand l'indice est en range, 3) il tient ou avance quand l'indice corrige. Exemple : Edison (ED) forme un higher low et casse la résistance quand le S&P 500 corrige.
**TRADEX-AI C7** : Critère de force relative TRADEX pour GC/HG/CL/ZW : si l'actif tient au-dessus de son dernier pivot bas pendant une correction de ES → force relative confirmée → pondération C7 maximale dans la grille de score.
*Catégorie : correlations*

### D4956 — Faiblesse relative : 3 manifestations (décline plus vite, décline en range, ne rebondit pas)
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/ys6XUen5esplZZzmoUlX) : Un actif montre une faiblesse relative quand : 1) il décline plus vite que l'indice, 2) il décline quand l'indice est en range, 3) il décline ou reste plat quand l'indice rebondit. Exemple : Nucor (NUE) baisse pendant le rebond ES de juillet-août.
**TRADEX-AI C7** : Critère de faiblesse relative TRADEX : si CL (Pétrole) ne rebondit pas quand ES rebondit → signal de faiblesse interne → favoriser les signaux VENDRE ou ATTENDRE sur CL même en contexte ES neutre.
*Catégorie : correlations*

### D4957 — High Volume Springboard : volume élevé sur rebond de support = signal haussier
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/auMZi4nJYPO20Sro6GhP) : Après une hausse puis consolidation avec support clair, un rebond sur fort volume depuis le support (springboard) est un signal de continuation haussière. Boeing (BA) : support ~62, résistance ~68 — fort volume sur rebond fin novembre → cassure vers 75+.
**TRADEX-AI C2** : Règle springboard TRADEX : sur GC/HG/CL/ZW, un rebond du support de consolidation avec delta ATAS positif et volume > moyenne 20 barres = signal d'entrée Long prioritaire — score C2 = 1/1.
*Catégorie : configuration*

### D4958 — Le springboard combiné à la force relative double la conviction du signal
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Boeing montrait simultanément : 1) force relative (tenait le bas d'octobre pendant la baisse du S&P 500), 2) springboard sur fort volume. La combinaison des deux renforce considérablement la conviction du signal d'achat.
**TRADEX-AI C1/C7** : Signal TRADEX de haute conviction sur GC/HG/CL/ZW = springboard volume C2 + force relative C7 + tendance C1 alignés. Ces 3 cercles alignés déclenchent le passage au niveau 3 (appel Claude API).
*Catégorie : gestion_risque_entree*

### D4959 — Retracement 50% : niveau idéal pour entrée dans une tendance haussière
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/PbJ04Rh4h9m0HougX8aw) : Wyckoff utilisait le niveau de 50% de retracement comme ligne de démarcation. Un retracement plus faible = pression vendeuse faible = force sous-jacente. Au niveau 50%, chercher un rebond sur fort volume pour signaler la continuation. Exemple Gannet (GCI) : rebond depuis 50% avec le plus fort volume en 4 semaines.
**TRADEX-AI C1** : Sur GC (Or), calculer en temps réel le niveau de 50% du dernier up-leg — un rebond depuis ce niveau avec volume expansion ATAS = entrée Long optimale Wyckoff, R/R maximisé.
*Catégorie : timing*

### D4960 — High Volume Consolidation : attention accrue, mouvement explosif imminent
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/Zn9WldzPyswLj2WxrNDC) : Quand un actif consolide avec expansion de volume, un mouvement explosif est imminent. La direction n'est pas certaine à priori — examiner le contexte global (force relative, tendance) pour déterminer le biais directionnel. Amgen : force relative + springboard volume → breakout haussier.
**TRADEX-AI C2** : Sur GC/HG/CL/ZW, une consolidation avec volume croissant (détecté par ATAS) = état d'alerte maximale. Le biais directionnel est déterminé par ES (C4), DX (C4) et la force relative C7 — le signal final attend la cassure directionnelle.
*Catégorie : volume_liquidite*

### D4961 — Patterns bearish : inverse exact des patterns bullish
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Les 3 patterns bearish sont les miroirs des bullish : 1) High volume déclin depuis la résistance de consolidation (vs springboard), 2) Rebond 50% suivi de thrust baissier sur fort volume (vs retracement 50% bullish), 3) Consolidation high volume avec cassure baissière (vs breakout haussier). Volume sur les jours de baisse > volume sur les jours de hausse = flux négatif.
**TRADEX-AI C2** : Règle delta ATAS TRADEX : delta cumulatif négatif sur la période de consolidation = biais baissier confirmé → favoriser les signaux VENDRE sur l'actif concerné.
*Catégorie : configuration*

### D4962 — Reward doit être au minimum 3x le risque (R/R ≥ 1:3 selon Wyckoff)
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff exigeait un potentiel de profit d'au moins 3 fois le risque (risquer 5$ pour gagner 15$+). Avec un ratio R/R de 1:3, être profitable 50% du temps suffit à dégager des gains nets.
**TRADEX-AI C1** : Le seuil TRADEX de R/R ≥ 1:2 (CLAUDE.md) est plus conservateur que Wyckoff (1:3). Pour les signaux haute conviction (score ≥ 8/10), cibler R/R ≥ 1:3 sur GC/HG/CL/ZW pour maximiser l'espérance mathématique.
*Catégorie : gestion_risque_entree*

### D4963 — P&F targets : largeur du pattern × reversal × valeur boîte = objectif de prix
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md, /files/xrDAcqcglDvdZMvrW2Ug) : Wyckoff utilisait les P&F pour calculer les objectifs. Amgen : 5 colonnes × 3 boxes × 1$/box = 15$ de hausse projetée → cible 69 (54+15). StockCharts confirme cible 72 avec méthode reversal. Ces cibles sont des guidelines, pas des absolus.
**TRADEX-AI C1** : La méthode P&F de projection est applicable sur GC (valeur boîte = 5$/oz, reversal 3 boxes typique) pour calculer les cibles de sortie des trades longs/shorts — à intégrer dans le calcul automatique du R/R.
*Catégorie : gestion_risque_entree*

### D4964 — Stops : placer aux niveaux de danger obvieux, pas trop serrés
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff plaçait les stops aux niveaux de support/résistance clés dont la cassure invaliderait l'analyse initiale. Stops trop serrés = stop-out prématuré par bruit normal. Resserrer le stop une fois le mouvement engagé pour locker les profits. Stops très serrés une fois la cible P&F atteinte.
**TRADEX-AI C1** : Règle stop TRADEX : le stop initial est placé sous le support clé Wyckoff (last swing low) + buffer ATR, jamais à distance fixe. Le trailing stop se resserre progressivement une fois +1R gagné.
*Catégorie : gestion_position_active*

### D4965 — 4 étapes de sélection d'un actif selon Wyckoff
🟡 **SYNTHÈSE** (Source : wyckoff_stock_analysis.md) : Process de sélection Wyckoff : 1) Identifier le secteur en force/faiblesse relative, 2) Dans ce secteur, trouver l'actif en meilleure force/faiblesse relative, 3) Chercher les signaux via patterns prix et volume, 4) Calculer R/R pour valider la faisabilité du trade.
**TRADEX-AI C7** : Ce processus est celui de TRADEX appliqué aux matières premières : 1) Tendance ES/DX (macro), 2) Actif trading le plus en force relative parmi GC/HG/CL/ZW, 3) Signal cercles C1/C2, 4) R/R calculé. Les 4 étapes correspondent aux 3 niveaux d'architecture événementielle.
*Catégorie : gestion_risque_entree*

### D4966 — Wyckoff sur shorting : même rigueur que pour les longs
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff n'hésitait pas à shorter. Il cherchait des actifs en faiblesse relative quand le marché était en downtrend. La même logique de confirmation (volume, pattern, R/R) s'applique aux shorts qu'aux longs.
**TRADEX-AI C1** : TRADEX traite symétriquement les signaux ACHETER et VENDRE — la même grille de score /10 s'applique dans les deux sens sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

### D4967 — Throwback après breakout : deuxième chance d'entrée
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Après une cassure de résistance (uptrend) ou de support (downtrend), un throwback ramène temporairement l'actif sur l'ancien niveau (devenu respectivement support ou résistance). C'est une deuxième chance d'entrée avec un meilleur R/R.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, si le moteur manque l'entrée sur la cassure initiale (signal émis mais non exécuté), le throwback offre une entrée de rattrapage valide — intégrer cette logique dans la file d'attente des signaux TRADEX.
*Catégorie : timing*

### D4968 — Les fondamentaux sont déjà dans le prix : ignorer les earnings
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff se concentrait exclusivement sur l'action des prix. Les fondamentaux et les médias financiers sont inutiles — au moment où l'information est disponible au public, elle est déjà intégrée dans le prix par le smart money.
**TRADEX-AI C6** : Nuance pour TRADEX : les événements macro non anticipés (NFP, FOMC, CPI) créent des discontinuités — d'où le News Gate (G1 du CLAUDE.md). En dehors de ces événements, le cerveau TRADEX se concentre sur le prix et le volume.
*Catégorie : macro_evenements*

### D4969 — Force relative appliquée aux matières premières : GC vs HG comme proxy
🟡 **SYNTHÈSE** (Source : wyckoff_stock_analysis.md) : Le principe de force relative Wyckoff (comparaison d'actifs dans le même univers) s'applique aux matières premières — comparer GC vs HG pour détecter lequel montre plus de force dans un contexte bull/bear DX.
**TRADEX-AI C7** : La matrice corrélations live C7 de TRADEX implémente cette logique : le ratio GC/HG (ou GC/CL) sur 30j identifie l'actif trading le plus en force relative — celui-ci reçoit une pondération supérieure dans la grille de score.
*Catégorie : correlations*

### D4970 — Réévaluer en permanence : les objectifs P&F peuvent être invalidés avant d'être atteints
🟢 **FAIT VÉRIFIÉ** (Source : wyckoff_stock_analysis.md) : Wyckoff rappelle de réévaluer continuellement le chart et la validité du mouvement en cours. La situation technique peut changer avant que la cible soit atteinte. Ajuster le plan de trade en conséquence.
**TRADEX-AI C1** : Le moteur TRADEX réévalue les signaux actifs toutes les 2 secondes (architecture événementielle) — si la structure de marché change (support cassé, volume diverge), le signal actif est reclassé ATTENDRE, même si l'objectif n'est pas atteint.
*Catégorie : gestion_position_active*
