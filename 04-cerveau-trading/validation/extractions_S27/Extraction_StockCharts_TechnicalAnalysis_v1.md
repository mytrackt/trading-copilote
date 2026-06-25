# Extraction StockCharts — Technical Analysis (Introduction Générale)
**Source :** `bundles/stockcharts/technical_analysis.md` (HTTP 200) + 5 images certifiées
**Méthode images :** double ancrage · 5/5 certifiées · 0 à vérifier
**Décisions :** D4351 → D4370 · **Page :** https://chartschool.stockcharts.com/table-of-contents/overview/technical-analysis
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Fondements de l'AT applicables à GC/HG/CL/ZW (futures/commodités) — cadre théorique et méthode top-down pour filtrer les signaux.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01.jpg | The weekly chart of Alphabet Inc. (GOOGL) shows a long-term uptrend and downtrend | Applying Technical Analysis | D4351 |
| image_02.jpg | Daily chart of Alphabet Inc. (GOOGL) shows a short-term view of the stock's price action | Applying Technical Analysis | D4351 |
| image_03.png | Trending and trading ranges in Oracle (ORCL) example chart from StockCharts.com | Price Movements Are Not Totally Random | D4354 |
| image_04.png | Chart Analysis Basics | Chart Analysis Basics | D4357 |
| image_05.png | Boeing Co. (BA) Technical Analysis example chart from StockCharts.com | Supply, Demand, and Price Action | D4360 |

## DÉCISIONS

### D4351 — L'AT s'applique à tout actif dont le prix est gouverné par l'offre et la demande
🔵 **ÉCOLE** (Source : technical_analysis.md, image_01.jpg, image_02.jpg) : L'analyse technique peut être appliquée aux actions, indices, commodités, futures ou tout instrument tradable dont le prix est influencé par l'offre et la demande. Elle peut s'appliquer sur tout timeframe : intraday (1-min à horaire), daily, hebdomadaire, mensuel.
**TRADEX-AI C1** : Valide l'utilisation de l'AT sur GC/HG/CL/ZW (futures commodités Catégorie 1) et sur ES/DX/VX (Catégorie 2 Confirmation). L'AT Belkhayate est universellement applicable sur ces instruments.
*Catégorie : structure_marche*

### D4352 — Prérequis 1 : liquidité suffisante pour que l'AT soit fiable
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis.md) : L'AT fonctionne mieux sur les actifs fortement tradés (nombreux acheteurs/vendeurs). Les actifs peu liquides sont difficiles à trader et leurs prix sont plus faciles à manipuler. Ces forces extérieures les rendent impropres à l'AT.
**TRADEX-AI C2/C7** : GC (Or), CL (Pétrole), ES (S&P500) ont une liquidité exceptionnelle — AT très fiable. HG (Cuivre) et ZW (Blé) ont une liquidité inférieure — surveiller l'Open Interest (C3) et le volume journalier avant de traiter un signal sur ces actifs.
*Catégorie : volume_liquidite*

### D4353 — Prérequis 2 : pas de changements de prix artificiels (splits, dividendes)
🔵 **ÉCOLE** (Source : technical_analysis.md) : Les splits, dividendes et distributions créent des changements de prix artificiels qui affectent dramatiquement le graphique et rendent l'AT difficile à appliquer. Ce type d'influence peut être corrigé en ajustant les données historiques avant le changement de prix.
**TRADEX-AI C1** : Pour les futures (GC/HG/CL/ZW), les roll dates créent l'équivalent des dividendes. Les données NT8 doivent être sur un contrat "continuous adjusted" pour garantir la cohérence des indicateurs Belkhayate sur l'historique.
*Catégorie : volume_liquidite*

### D4354 — Les prix ont tendance à se comporter de manière non-aléatoire (trending)
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis.md, image_03.png) : La plupart des techniciens reconnaissent que les prix tendent (trending). Jack Schwager : "Les marchés peuvent vivre des périodes étendues de fluctuation aléatoire, entrecoupées de périodes plus courtes de comportement non-aléatoire. L'objectif du chartiste est d'identifier ces périodes (c'est-à-dire les tendances majeures)."
**TRADEX-AI C1** : Fondement théorique de TRADEX-AI : le système cherche précisément ces périodes non-aléatoires (tendances claires) sur GC/HG/CL/ZW. En absence de tendance (random / range), le système émet ATTENDRE.
*Catégorie : structure_marche*

### D4355 — Prérequis 3 : l'AT ne prédit pas les événements extrêmes (news, géopolitique)
🟢 **FAIT VÉRIFIÉ** (Source : technical_analysis.md) : L'AT ne peut pas prédire les événements extrêmes (changements de management, changements réglementaires, événements géopolitiques). Quand ces "extreme news" influencent le prix, le technicien doit attendre que le graphique se stabilise et reflète le "new normal".
**TRADEX-AI C6** : Justification directe du News Gate TRADEX-AI : bloquer les signaux 30 min avant/après NFP/FOMC/CPI et lors d'événements géopolitiques majeurs (C6). L'AT est invalide pendant et juste après ces chocs. Attendre la stabilisation.
*Catégorie : macro_evenements*

### D4356 — Le prix actualise toute l'information disponible (Dow Theory)
🔵 **ÉCOLE** (Source : technical_analysis.md) : Premier théorème Dow : le prix actualise tout (discounts everything). Le prix actuel reflète toutes les informations disponibles. Il représente la valeur équitable résultant de la somme des connaissances de tous les participants (investisseurs, analystes, gestionnaires, techniciens...).
**TRADEX-AI C1** : Fondement philosophique : TRADEX-AI analyse le prix NT8 directement, sans chercher à connaître les causes fondamentales. Le prix GC/HG/CL/ZW est la donnée primaire ; les 7 cercles d'intelligence contextualisent mais ne remplacent pas le signal prix.
*Catégorie : structure_marche*

### D4357 — Approche top-down : marché → secteur → actif individuel
🟡 **SYNTHÈSE** (Source : technical_analysis.md, image_04.png) : Les techniciens appliquent souvent une approche top-down : (1) analyse du marché global (S&P500, Dow, NASDAQ), (2) analyse des secteurs pour identifier les groupes forts/faibles, (3) analyse des actions individuelles dans les secteurs sélectionnés. Cette approche améliore la probabilité de succès.
**TRADEX-AI C1/C4** : TRADEX-AI implémente cette approche : (1) filtre ES/DX/VX (Catégorie 2 confirmation macro), (2) puis signal sur actifs Catégorie 1 (GC/HG/CL/ZW) alignés avec le contexte macro. La règle 3/4 + 2/3 est une formalisation de l'approche top-down.
*Catégorie : indicateurs_tendance*

### D4358 — Le marché est un indicateur avancé de l'économie (6-9 mois)
🔵 **ÉCOLE** (Source : technical_analysis.md) : Le marché est considéré comme un indicateur avancé et précède généralement l'économie de 6 à 9 mois. Focaliser sur le mouvement des prix revient à se focaliser sur le futur. Les changements sont souvent subtils — les indices s'accumulent avant les grandes évolutions.
**TRADEX-AI C4** : Sur GC/HG/CL/ZW, les signaux TRADEX capturent les mouvements avant que les fondamentaux économiques ne les expliquent. Les périodes d'accumulation (C3 COT institutionnels) précèdent les grandes tendances — à surveiller via C3.
*Catégorie : macro_evenements*

### D4359 — L'AT synthétise : force, maturité, R/R et points d'entrée
🟡 **SYNTHÈSE** (Source : technical_analysis.md, image_04.png) : La synthèse finale de l'AT vise à déterminer : (1) la force de la tendance actuelle, (2) la maturité ou le stade de la tendance, (3) le ratio reward-to-risk d'une nouvelle position, (4) les niveaux d'entrée potentiels.
**TRADEX-AI C1** : Correspond exactement aux critères de la grille /10 TRADEX-AI : score de force tendance (C1) + stade tendance (C1) + R/R ≥ 1:2 obligatoire (Décision D2 verrouillée) + niveau d'entrée optimal (C1 + C2). Validation directe de la structure de décision.
*Catégorie : gestion_risque_entree*

### D4360 — Biais de l'analyste : vigilance sur les biais haussiers/baissiers personnels
🟡 **SYNTHÈSE** (Source : technical_analysis.md, image_05.png) : Comme l'analyse fondamentale, l'AT est subjective et les biais personnels peuvent se refléter dans l'analyse. Un analyste "perma-bull" aura une inclinaison haussière ; un "perma-bear" une inclinaison baissière. Être conscient de ces biais est essentiel.
**TRADEX-AI C1** : Justification du système de scoring déterministe /10 de TRADEX-AI : une grille objective élimine le biais personnel d'Abdelkrim. Le score /10 est calculé par algorithme sur règles Belkhayate, non par interprétation subjective du graphique.
*Catégorie : psychologie*
