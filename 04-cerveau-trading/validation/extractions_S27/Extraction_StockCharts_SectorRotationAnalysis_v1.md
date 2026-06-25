# Extraction StockCharts — Sector Rotation Analysis
**Source :** `bundles/stockcharts/sector_rotation_analysis.md` (HTTP 200) + 4 images certifiées
**Méthode images :** double ancrage · 4/4 certifiées · 0 à vérifier
**Décisions :** D3571 → D3590 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/sector-rotation-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Cycle économique intermarché applicable à CL (Énergie), HG (Matériaux), GC (refuge), DX (macro), ES (confirmation marché), VX (sentiment).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Sector Rotation Analysis (cycle business sine wave) | The Business Cycle | D3571 |
| image_02 | Sector Rotation Model (cycle économique bleu, cycle marché orange, secteurs leaders) | Sector Rotation | D3574 |
| image_03 | Sector Rotation Analysis (PerfChart 2007 peak) | Sector Rotation | D3577 |
| image_04 | Sector Rotation Analysis (PerfChart 2003 bottom) | Sector Rotation | D3578 |
| image_05 | Staples/Discretionary Ratio (ratio XLY/XLP vs S&P 500) | Staples/Discretionary Ratio | D3582 |

## DÉCISIONS

### D3571 — Cycle économique : 6 stages intermarché (Pring)
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_01) : Le cycle économique idéalisé de Martin J. Pring comprend 6 stages : Stage 1 = contraction + bonds montent (taux baissent) ; Stage 2 = bottom économie + bottom marché actions ; Stage 3 = amélioration conditions + stocks montent + commodities tournent ; Stage 4 = expansion pleine + stocks ET commodities montent + bonds baissent (inflation) ; Stage 5 = peak croissance + peak actions + commodities encore fortes ; Stage 6 = détérioration + stocks baissent + commodities tournent à la baisse.
🔵 **ÉCOLE** : Basé sur l'*Intermarket Review* de Martin J. Pring (www.pring.com).
**TRADEX-AI C4** : GC et CL sont commodities — ils montent en Stage 3-4-5 et baissent en Stage 6 ; DX tend à baisser en Stage 4 (expansion inflationniste) — signal macro pour orienter le biais directionnel sur GC/CL.
*Catégorie : correlations*

### D3572 — Stage 2 : actions anticipent le bottom AVANT la fin de contraction
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Stocks anticipate an expansion phase by bottoming before the contraction period ends. » — les actions tournent avant l'économie.
🟡 **SYNTHÈSE** : ES (S&P 500) sert de leading indicator pour le cycle macro — un bottom ES peut précéder le bottom des commodités.
**TRADEX-AI C4/C7** : Surveiller le retournement de ES comme signal avancé avant un move haussier sur GC/CL/HG — confirmation inter-marché.
*Catégorie : correlations*

### D3573 — Stage 5 : commodités peak APRÈS les actions
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Commodities remain strong and peak after stocks. » — en Stage 5 les commodités continuent de monter après le peak actions.
🟡 **SYNTHÈSE** : Si ES commence à baisser mais que GC/CL restent forts, on est probablement en Stage 5 — continuer à trader les commodités long jusqu'au peak commodities.
**TRADEX-AI C4** : Ne pas sortir prématurément de GC/CL sur simple faiblesse de ES si commodities encore en momentum — vérifier le stage du cycle.
*Catégorie : timing*

### D3574 — Rotation sectorielle : ordre des secteurs leaders (Technology → Consumer Disc → Materials → Energy → Consumer Staples → Utilities)
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_02) : « The technology sector is the first to turn up in anticipation of a bottom in the economy. Consumer discretionary stocks are not far behind. » [...] « The top of the market cycle is marked by relative strength in materials and energy. » [...] « The tipping point for the market comes when leadership shifts from energy to consumer staples. »
**TRADEX-AI C4** : Quand Energy sector (proxy CL) cède le leadership à Consumer Staples = signal de retournement de cycle imminent → réduire exposition CL long, surveiller short.
*Catégorie : correlations*

### D3575 — Signal top marché : passage Energy → Consumer Staples en leadership
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « This is a sign that commodity prices are starting to hurt the economy » [quand leadership passe d'Energy à Consumer Staples].
**TRADEX-AI C4** : Indicator macro pour TRADEX : surveiller force relative XLE vs XLP (ETFs US) comme signal avancé de peak cycle pour CL et HG.
*Catégorie : macro_evenements*

### D3576 — Signal bottom marché : Fed baisse taux → bénéfice Utilities + Banks
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « At this stage, the Fed starts to lower interest rates and the yield curve steepens. Falling interest rates benefit debt-laden utilities and business at banks. »
🟡 **SYNTHÈSE** : Baisses de taux Fed = contexte haussier pour GC (actif refuge sans rendement — coût d'opportunité diminue) et potentiellement baissier pour DX.
**TRADEX-AI C4** : Lors de cycles de baisse de taux Fed, biais haussier sur GC renforcé — intégrer dans la grille macro C4.
*Catégorie : macro_evenements*

### D3577 — Exemple historique 2007 peak : Energy et Materials en force relative, Consumer Discretionary en retard
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_03) : « In the summer of 2007, the Energy and Materials sectors were leading the market and showing relative strength. Also, notice that Consumer Discretionary was lagging the S&P 500. This sector action matches what is expected at a market top. »
**TRADEX-AI C4** : Validation empirique : force simultanée Energy + Materials = fin de cycle haussier — contexte de prudence pour trades CL/HG long en stage avancé.
*Catégorie : correlations*

### D3578 — Exemple historique 2003 bottom : Consumer Discretionary et Technology en force relative
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_04) : « The Consumer Discretionary and Technology sectors led the first move off the March 2003 low. These two showed relative strength that affirmed the importance of the 2003 bottom. »
**TRADEX-AI C7** : Début de bull run = Tech + Conso Disc en tête ; commodités (GC/CL/HG) arrivent plus tard en Stage 3-4 → ne pas trader commodités trop tôt dans la reprise.
*Catégorie : timing*

### D3579 — Environnement déflationniste : bonds et stocks évoluent en sens inverse
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « This would not be the case in a deflationary environment, when bonds and stocks would move in opposite directions. »
🟡 **SYNTHÈSE** : Le modèle de rotation sectorielle standard suppose un environnement inflationniste — en déflation, les corrélations inter-marchés s'inversent.
**TRADEX-AI C4** : Si CPI négatif / environnement déflationniste → invalider les corrélations standard du modèle — recalibrer C7 (corrélations live 30j).
*Catégorie : macro_evenements*

### D3580 — Ratio XLY/XLP : Consumer Discretionary vs Consumer Staples comme indicateur de santé économique
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_05) : Le ratio XLY/XLP « peaked ahead of the S&P 500 in 2007 and broke support ahead of the market. The ratio bottomed ahead of the S&P 500 in late 2008 and broke resistance as the S&P 500 surged off the March 2009 low. »
**TRADEX-AI C4** : Ratio XLY/XLP comme indicateur avancé du cycle ES — un break de support du ratio précède le peak ES et donc le peak des commodités en Stage 5.
*Catégorie : correlations*

### D3581 — Consumer Discretionary outperform en économie robuste, underperform en contraction
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « The consumer discretionary sector tends to outperform when the economy is buoyant and growing. This sector under-performs when the economy is struggling or contracting. »
**TRADEX-AI C4** : XLY en sous-performance prolongée = signal de contraction économique → biais baissier sur CL/HG (demande industrielle) et biais haussier sur GC (refuge).
*Catégorie : correlations*

### D3582 — Cycle inflationniste : Stage 3 = stocks montent + commodities tournent haussières
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Stage 3 shows a vast improvement in economic conditions [...] Stocks are rising and commodities are anticipating an expansion phase by turning up. »
⚫ **HYPOTHÈSE PROJET** : En Stage 3, GC/CL/HG devraient initier leurs tendances haussières — moment optimal pour initier des positions long sur ces commodités.
**TRADEX-AI C4** : Stage 3 identifié = condition favorable pour signaux ACHETER sur GC/HG/CL — renforcer le score signal si contexte macro Stage 3.
*Catégorie : timing*

### D3583 — Stage 4 : obligations baissent car expansion augmente les pressions inflationnistes
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Stage 4 marks a period of full expansion. Both stocks and commodities are rising, but bonds turn lower because the expansion increases inflationary pressures. To combat this, interest rates start to move higher. »
**TRADEX-AI C4** : Hausse des taux en Stage 4 = environnement mixte pour GC (négatif taux réels) mais positif pour commodités industrielles HG/CL ; DX tend à se renforcer avec taux.
*Catégorie : macro_evenements*

### D3584 — Stage 6 : détérioration + stocks et commodities baissent tous les deux
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Stage 6 marks a deterioration in the economy [...] Stocks have already been moving lower and commodities now turn lower in anticipation of decreased demand from the deteriorating economy. »
**TRADEX-AI C4** : Stage 6 identifié = contexte favorable pour signaux VENDRE sur CL/HG (demande en baisse) ; GC peut tenir plus longtemps comme refuge.
*Catégorie : timing*

### D3585 — Modèle cycle marché (orange) précède cycle économique (bleu)
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md, image_02) : « Notice how the orange market cycle leads the business cycle. The market turns up and crosses the centerline before the economic cycle turns. »
🟡 **SYNTHÈSE** : ES (S&P 500) est un leading indicator du cycle économique global — surveiller ES pour anticiper les virages macro avant qu'ils n'apparaissent dans les données économiques.
**TRADEX-AI C4** : Intégrer le retournement de ES dans la grille C4 comme signal anticipatif du virage cycle — ES confirme avant les chiffres macro officiels.
*Catégorie : correlations*

### D3586 — Steepening yield curve après baisse taux : favorable lending + banks + commodities
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « The steepening yield curve also improves profitability at banks and encourages lending. Low interest rates and easy money eventually lead to a market bottom and the cycle repeats itself. »
🟡 **SYNTHÈSE** : Yield curve steepening = signal avancé de reprise économique → préparer les positions long sur commodités (GC/CL/HG) dans ce contexte.
**TRADEX-AI C4** : Courbe des taux qui se pentifie = condition macro favorable pour le prochain bull run sur commodités — intégrer dans analyse C4.
*Catégorie : macro_evenements*

### D3587 — Le cycle de rotation sectorielle n'est pas infaillible — modèle idéalisé
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : « Keep in mind that this is the ideal business cycle in an inflationary environment. »
**TRADEX-AI C4** : Utiliser le modèle de cycle comme cadre de probabilité, non comme règle déterministe — combiner avec les 7 Cercles TRADEX pour validation multi-sources.
*Catégorie : gestion_risque_entree*

### D3588 — Ressource complémentaire : John Murphy *Trading with Intermarket Analysis*
🔵 **ÉCOLE** (Source : sector_rotation_analysis.md) : John Murphy est cité comme référence pour l'analyse intermarché et la rotation sectorielle.
**TRADEX-AI C7** : La méthode Belkhayate s'inscrit dans la tradition de l'analyse intermarché de Murphy — cohérence avec les corrélations live C7 du système TRADEX.
*Catégorie : correlations*

### D3589 — Données historiques StockCharts pour Real Estate et Communication Services
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : StockCharts fournit des données historiques pour l'analyse des secteurs Real Estate et Communication Services.
**TRADEX-AI C4** : Données sectorielles disponibles pour enrichir l'analyse macro du cycle — pertinence secondaire pour TRADEX focalisé sur commodités.
*Catégorie : macro_evenements*

### D3590 — PerfChart live disponible pour suivi rotation sectorielle en temps réel
🟢 **FAIT VÉRIFIÉ** (Source : sector_rotation_analysis.md) : Un PerfChart live des 11 secteurs S&P SPDR ETFs est disponible sur StockCharts.
**TRADEX-AI C4** : Outil de monitoring macro disponible pour suivre la rotation sectorielle en complément de l'analyse ES/VX — usage manuel par Abdelkrim.
*Catégorie : macro_evenements*
