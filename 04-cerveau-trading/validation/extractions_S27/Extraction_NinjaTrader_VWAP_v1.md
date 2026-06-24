# Extraction NinjaTrader — Volume-Weighted Average Price (VWAP)

**Source :** `bundles/ninjatrader/what_is_volume_weighted_average_price_vwap.md` (HTTP 200 · STATIC) + 0 image
**Méthode images :** ancrage figcaption locale (HTML statique) · 0 figure `<figure>+<figcaption>` sur la page · 0/0 certifiée · 0 à vérifier
**Décisions :** D379 → D388 · **Page :** ninjatrader.com/futures/blogs/what-is-volume-weighted-average-price-vwap/
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page PRIORITAIRE — VWAP = indicateur **order flow** (prix moyen pondéré volume), pertinent pour les cercles **C1 (prix)** et **C2 (order flow)**. SOURCE **Tier 2 broker** (NinjaTrader) : les faits factuels sont 🟢, mais l'interprétation maison/marketing (benchmark institutionnel, suite Order Flow +) est marquée 🔵 ÉCOLE. NB : c'est l'**angle NinjaTrader** du VWAP, complémentaire de la page StockCharts VWAP traitée séparément.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | la page ne contient aucune figure `<figure>+<figcaption>` (manifest : 0 certifiée / 0 à vérifier / 0 décorative) | — |

---

## DÉCISIONS

### D379 — VWAP : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Le Volume-Weighted Average Price (VWAP) est un indicateur technique utilisé pour détecter les niveaux de support et résistance, gérer les entrées/sorties, déterminer la direction du marché et mesurer la force d'une tendance.
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Prix et volume sont les pierres angulaires des données d'order flow, le prix étant le résultat final du volume acheteur/vendeur ; l'importance d'un mouvement de prix corrèle souvent avec le volume échangé pendant l'action.
**TRADEX-AI C2** : VWAP = brique « prix moyen pondéré volume » = ancrage order flow pour GC/HG/CL/ZW (support/résistance dynamique intraday).
*Catégorie : indicateurs_tendance*

---

### D380 — VWAP : formule de calcul
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Le VWAP est similaire à une moyenne mobile, mais le volume est incorporé pour « pondérer » le prix moyen sur une période donnée. En d'autres termes, le VWAP prend le **montant total en dollars transigé** et le divise par le **nombre total d'unités échangées**.
🔴 **NON VÉRIFIÉ** : La formule de base est annoncée (« The basic formula used is: ») mais **absente du texte extrait** (vraisemblablement une image non capturée). À compléter depuis une source littérale (cf. page StockCharts VWAP).
**TRADEX-AI C0** : Formule déterministe à répliquer côté export NinjaScript (besoin prix typique × volume cumulé ÷ volume cumulé) ; récupérer l'expression exacte avant codage.
*Catégorie : indicateurs_tendance*

---

### D381 — Bandes d'écart-type (standard deviation bands)
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : En plus de la ligne VWAP, des lignes d'écart-type sont souvent utilisées pour indiquer des supports/résistances potentiels et autres niveaux de prix clés. Les multiplicateurs courants pour les écarts-types VWAP sont **1, 2 et 3**.
**TRADEX-AI C1** : Exposer en config 3 bandes ±1σ/±2σ/±3σ autour du VWAP comme niveaux de réaction prix sur GC/HG/CL/ZW.
*Catégorie : configuration*

---

### D382 — Comportement de la ligne VWAP (couleur + réaction prix)
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Sur un graphique 15 minutes (exemple Micro E-mini Dow, 1 journée), la ligne VWAP alterne entre **vert et rouge** selon que le prix est au-dessus ou en-dessous du VWAP. Le prix tend à **réagir** au contact de la ligne VWAP.
🔵 **ÉCOLE** : L'exemple utilise le Micro E-mini Dow (actif NinjaTrader), hors univers TRADEX-AI — transposable mais non testé sur nos actifs.
**TRADEX-AI C1/C2** : Coder l'état au-dessus/en-dessous du VWAP (biais directionnel) et surveiller les contacts prix↔VWAP comme zones de réaction sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D383 — VWAP vs moyenne mobile : prix « vrai » pondéré volume
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Comparé à une moyenne mobile traditionnelle, le VWAP identifie un prix moyen « vrai » en intégrant le volume de transactions à chaque niveau de prix.
**TRADEX-AI C2** : Préférer le VWAP à la moyenne mobile nue quand l'ancrage doit refléter le volume réellement transigé (order flow GC/HG/CL/ZW) ; les traiter comme complémentaires, pas redondants.
*Catégorie : indicateurs_tendance*

---

### D384 — Les usages du VWAP en intraday (5 cas)
🔵 **ÉCOLE** (Source : what_is_volume_weighted_average_price_vwap.md) : Les day traders utilisent le VWAP pour — (1) identifier supports/résistances ; (2) suivre les retournements de prix ; (3) confirmer ou infirmer les tendances ; (4) déterminer la force d'un marché ; (5) affiner les entrées et sorties.
**TRADEX-AI C3** : Cadre de lecture du VWAP à cinq usages ; les traiter comme confirmations, jamais comme entrées isolées (cf. D387).
*Catégorie : structure_marche*

---

### D385 — Perspective institutionnelle : benchmark d'exécution
🔵 **ÉCOLE** (Source : what_is_volume_weighted_average_price_vwap.md) : Le VWAP donne une idée de l'endroit où les institutionnels initient et liquident des positions. Il est couramment utilisé par hedge funds et fonds de pension pour construire/clôturer des positions. Considéré comme un **benchmark de remplissage d'ordre**, les traders institutionnels VWAP cherchent à **acheter sous la ligne VWAP et vendre au-dessus**.
**TRADEX-AI C2/C3** : Lire la position du prix vs VWAP comme proxy de pression institutionnelle (achat sous / vente au-dessus) sur GC/HG/CL/ZW — confirmation, non déclencheur.
*Catégorie : structure_marche*

---

### D386 — Limite : faux signaux, ne jamais utiliser seul
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Comme tout indicateur, le VWAP peut produire de **faux signaux** et doit être utilisé en combinaison avec d'autres outils d'analyse pour confirmer une thèse de trade. La gestion du risque doit rester primordiale.
**TRADEX-AI C3** : Guard permanent — un signal VWAP sur GC/HG/CL/ZW exige confirmation multi-outil (price action, structure, volume) ; ne pas baser la décision sur le seul franchissement du VWAP.
*Catégorie : gestion_risque_entree*

---

### D387 — Timeframes étendus (daily / weekly / monthly)
🟢 **FAIT VÉRIFIÉ** (Source : what_is_volume_weighted_average_price_vwap.md) : Dans la suite Order Flow + de NinjaTrader, le VWAP propose des bandes d'écart-type personnalisables et peut être utilisé sur des cadres **journalier, hebdomadaire et mensuel**.
🔵 **ÉCOLE** : Mention liée à un produit payant (Order Flow + suite) — angle commercial broker Tier 2.
**TRADEX-AI C1** : Paramètre de période d'ancrage VWAP (session/jour/semaine/mois) à exposer en config selon le mode (intraday vs swing) sur GC/HG/CL/ZW.
*Catégorie : configuration*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D379 → D387 (9) |
| Images certifiées citées | 0/0 (aucune figure sur la page) |
| Catégories utilisées | indicateurs_tendance · configuration · signal · structure_marche · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🔴 NON VÉRIFIÉ |
| Belkhayate | **NON directement** — VWAP = order flow C1/C2 ; complémentaire de la page StockCharts VWAP (angle NinjaTrader) |
| À vérifier | D380 : la formule de base est annoncée mais absente du texte (probable image non capturée) → compléter via source littérale |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
