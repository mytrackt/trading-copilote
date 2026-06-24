# Extraction StockCharts — Intermarket Analysis (analyse inter-marché)
**Source :** `bundles/stockcharts/intermarket_analysis.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 7/7 certifiées · 0 à vérifier
**Décisions :** D299 → D309 · **Page :** chartschool.stockcharts.com/.../market-analysis/intermarket-analysis
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** — l'inter-marché (John Murphy, *Trading with Intermarket Analysis*) alimente directement le **Cercle C7 (matrice corrélations live 30j GC/HG/CL/ZW/ES/VX/MBT/6J)** et le **Cercle C4 (macro)**. Les relations dollar↔commodities, taux↔actions, métaux industriels↔actions structurent la lecture corrélée des actifs. Les faits sont 🟢 quand littéraux ; le rattachement aux actifs TRADEX-AI et tout lien Belkhayate sont signalés (🟡 / ⚫🔴).

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Intermarket Analysis (figcaption + HTML) | What is Intermarket Analysis? | D299 |
| image_02 | Intermarket Analysis (figcaption + HTML) | Deflationary Relationships | D302 |
| image_03 | Intermarket Analysis (figcaption + HTML) | Deflationary Relationships | D302 |
| image_04 | Intermarket Analysis (figcaption + HTML) | Deflationary Relationships | D302 |
| image_05 | Intermarket Analysis (figcaption + HTML) | Dollar and Commodities | D304 |
| image_06 | Intermarket Analysis (figcaption + HTML) | Industrial Metals and Bonds | D306 |
| image_07 | Intermarket Analysis (figcaption + HTML) | Industrial Metals and Bonds | D307 |

> Note traçabilité : le bundle `.md` contient une 8ᵉ balise figure (PerfChart `data-size="line"`, section *PerfChart*) — image inline NON listée au manifest, donc NON certifiée et non citée comme 🟢.

---

## DÉCISIONS

### D299 — Définition : 4 classes d'actifs corrélées
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md, image_01) : L'analyse inter-marché est une branche de l'analyse technique qui examine les **corrélations entre quatre classes d'actifs** : actions, obligations, matières premières et devises. D'après John Murphy (*Trading with Intermarket Analysis*), ces relations aident à identifier le **stade du cycle économique** et à améliorer les prévisions. Il existe des relations claires entre actions↔obligations, obligations↔commodities, et commodities↔Dollar.
**TRADEX-AI C7** : Fonde la matrice corrélations live 30j — modéliser explicitement les couples actions(ES)↔obligations, commodities(GC/HG/CL/ZW)↔obligations, commodities↔Dollar(DX). Sert de cadre théorique au cercle C7.
*Catégorie : structure_marche*

---

### D300 — Le sens des corrélations dépend du régime inflation/déflation
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : Les relations inter-marché **dépendent des forces d'inflation ou de déflation**. Un « environnement inflationniste » ne signifie pas inflation galopante : seulement que les forces inflationnistes dominent les forces déflationnistes (et inversement). Le monde fut inflationniste des années 1970 à la fin des années 1990.
**TRADEX-AI C4/C7** : Avant d'appliquer un signe de corrélation, le moteur doit **détecter le régime macro** (inflation vs déflation) ; le même couple d'actifs peut changer de signe selon le régime. Garde anti-corrélation-figée pour la matrice 30j.
*Catégorie : structure_marche*

---

### D301 — Relations en environnement INFLATIONNISTE
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : En environnement inflationniste — relation **positive** obligations↔actions ; les obligations **changent de direction avant** les actions (typiquement) ; relation **inverse** obligations↔commodities ; relation **inverse** US Dollar↔commodities. Les actions réagissent positivement à la baisse des taux (hausse du prix des obligations).
🔵 **ÉCOLE** (Source : intermarket_analysis.md) : Les obligations comme **indicateur avancé** des actions est une lecture de l'école Murphy.
**TRADEX-AI C4/C7** : En régime inflationniste, traiter DX↔(GC/HG/CL/ZW) comme **inverse** (Dollar fort = pression baissière commodities) ; surveiller les obligations comme proxy avancé d'ES.
*Catégorie : structure_marche*

---

### D302 — Relations en environnement DÉFLATIONNISTE (bascule ~1998)
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md, image_02, image_03, image_04) : Murphy situe le passage inflation→déflation **autour de 1998** (crise des devises asiatiques 1997, bulle Nasdaq 2000, immobilier 2006, crise financière 2007). En environnement déflationniste : relation **inverse** obligations↔actions ; **inverse** commodities↔obligations ; **positive** actions↔commodities ; **inverse** US Dollar↔commodities. Les actions ont alors une relation **positive avec les taux** (actions et taux montent ensemble).
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : Les deux PerfCharts (image_03, image_04) paraissent opposés mais illustrent **tous deux** un environnement déflationniste, car actions et obligations y sont inversement corrélées dans les deux cas.
**TRADEX-AI C4/C7** : Le seul invariant inter-régime est **Dollar↔commodities = inverse**. Le couple actions↔commodities **bascule** positif en déflation : nœud critique pour la matrice ES↔(HG/CL) selon le régime détecté.
*Catégorie : structure_marche*

---

### D303 — Invariant clé : Dollar ↔ commodities = inverse (les deux régimes)
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : La relation **inverse US Dollar↔commodities** est présente dans la liste inflationniste ET déflationniste — c'est la relation la plus stable de l'article.
🟡 **CONVENTION** : Retenir cette inversion comme **a priori de signe** pour le couple DX↔commodities dans la matrice C7, à confirmer par la corrélation mesurée 30j.
**TRADEX-AI C7** : DX = proxy Dollar (DXY Alpha Vantage) ; armer le signe attendu **négatif** sur DX↔GC, DX↔HG, DX↔CL, DX↔ZW ; alerter si la corrélation live 30j contredit l'a priori (régime atypique / drawdown de relation, cf. D309).
*Catégorie : structure_marche*

---

### D304 — Le Dollar, « wild card » : faible Dollar non baissier pour actions sauf si commodities flambent
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md, image_05) : Le Dollar est un peu un **joker**. Pour les actions, un Dollar faible **n'est pas baissier** sauf s'il s'accompagne d'une **forte avancée des commodities** (laquelle serait baissière pour les obligations). Un Dollar faible agit comme stimulus économique (exports US plus compétitives) et bénéficie aux grandes multinationales. Un Dollar **fort** pèse sur les commodities (oil et autres cotés en Dollars) ; baisse des commodities = positive pour obligations (moins d'inflation) et pour actions (coût matières premières réduit).
**TRADEX-AI C4/C7** : Ne pas dériver mécaniquement un signal ES d'un mouvement de DX seul — conditionner par l'état des commodities (GC/HG/CL/ZW). Dollar fort → biais baissier commodities + biais positif coûts/actions.
*Catégorie : structure_marche*

---

### D305 — Oil et chocs d'offre : sens du signal dépend de la cause de la hausse
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : Toutes les commodities ne se valent pas. L'**oil** est sujet aux **chocs d'offre** (troubles dans pays producteurs → flambée). Une hausse de prix due à un **choc d'offre** est **négative pour les actions** ; une hausse due à une **hausse de la demande** peut être **positive pour les actions**. Idem pour les métaux industriels, moins exposés aux chocs d'offre.
**TRADEX-AI C4/C6** : Pour CL (pétrole), **désambiguïser la cause** d'une hausse (offre vs demande) avant d'en tirer un biais ES — relie au cercle C6 (géopolitique / news gate). Une hausse CL sur choc d'offre ≠ signal haussier risk-on.
*Catégorie : structure_marche*

---

### D306 — Métaux industriels = proxy de santé économique, corrélés aux actions
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md, image_06) : Les métaux industriels, moins exposés aux chocs d'offre, servent d'**indice de l'économie et du marché actions** : prix en hausse = demande croissante / économie saine ; prix en baisse = demande faible / économie faible. Le graphique montre une **relation positive claire entre métaux industriels et le S&P 500**.
**TRADEX-AI C7** : **HG (Cuivre)** = capteur avancé de santé économique → armer une corrélation **positive attendue HG↔ES** dans la matrice 30j ; une divergence HG/ES = signal de stress à remonter au scoring.
*Catégorie : indicateurs_tendance*

---

### D307 — Ratio Métaux industriels / Obligations = jauge force économique vs déflation
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md, image_07) : Métaux et obligations montent pour des raisons opposées — les métaux montent quand l'économie croît et/ou que l'inflation se construit ; les obligations montent quand l'économie est faible et/ou que la déflation domine. Le **ratio métaux/obligations monte** en force économique + inflation, et **baisse** en faiblesse économique + déflation.
🟡 **CONVENTION** : Utiliser ce ratio comme **indicateur de régime** dérivé (force éco / inflation vs déflation).
**TRADEX-AI C4** : Calculer un ratio HG/obligations (proxy) comme jauge de régime macro alimentant la détection inflation/déflation (cf. D300) ; entrée du contexte C4, pas un signal d'entrée isolé.
*Catégorie : indicateurs_tendance*

---

### D308 — Horizon : inter-marché = analyse moyen/long terme, jamais un signal seul
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : L'analyse inter-marché est un outil de **long ou moyen terme**. Les relations fonctionnent sur de **longues périodes** mais subissent des **drawdowns** (périodes où elles ne marchent plus). Un seul indicateur ou une seule relation **ne doit pas servir** à juger l'ensemble du marché ; à combiner avec d'autres techniques. Le ratio métaux/obligations peut faire partie d'un **panier d'indicateurs** de force/faiblesse du marché.
**TRADEX-AI C7** : Garde permanente — la matrice corrélations C7 informe le **contexte** (biais directionnel multi-actifs), pas le déclenchement intrabar. Décision finale = grille déterministe /10 (≥7,0 + R/R ≥1:2), jamais une corrélation seule.
*Catégorie : gestion_risque_entree*

---

### D309 — Robustesse : les corrélations cassent lors des grands chocs
🟢 **FAIT VÉRIFIÉ** (Source : intermarket_analysis.md) : De **grands événements** (ex. crise financière US 2008) peuvent **dérégler certaines relations pendant quelques mois**.
🟡 **CONVENTION** : Traiter toute corrélation 30j comme **non garantie** ; prévoir un état « relation rompue » désactivant l'a priori de signe.
**TRADEX-AI C7** : La matrice 30j doit **détecter les ruptures** (corrélation mesurée contredisant l'a priori, cf. D303) et **dégrader la confiance** plutôt que forcer le signe attendu. Relie au staleness/circuit-breaker : régime atypique = prudence, pas d'inférence corrélée.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D299 → D309 (11) |
| Images certifiées citées | 7/7 |
| Catégories utilisées | structure_marche · indicateurs_tendance · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Cercles visés | C7 (corrélations live 30j) · C4 (macro) · liens C6 (oil/news) |
| Belkhayate | **NON CONCERNÉ** — aucune affirmation de la source ne touche la méthode Belkhayate ; aucun lien forcé (pas de ⚫🔴 nécessaire) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
