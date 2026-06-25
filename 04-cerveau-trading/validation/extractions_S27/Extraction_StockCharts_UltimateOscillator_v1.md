# Extraction StockCharts — Ultimate Oscillator
**Source :** `bundles/stockcharts/ultimate_oscillator.md` (HTTP 200) + 7 images certifiées
**Méthode images :** double ancrage · 7/7 certifiées · 0 à vérifier
**Décisions :** D4771 → D4790 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/ultimate-oscillator

**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : oscillateur momentum multi-timeframe utile pour GC/CL/HG/ZW pour filtrer signaux Belkhayate en zones extrêmes (sur/sous-achat).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/JnWlQKFl1xl5wbEWHsvZ | Ultimate Oscillator – Chart 1 (formule/calcul) | Calculation | D4771 |
| /files/fyyUQLEEdzpzCJc0yCDx | Ultimate Oscillator – Chart 2 (bullish divergence BBY) | Buy Signal | D4774 |
| /files/Y24cCFU02pqJ3hl3RPDR | Ultimate Oscillator – Chart 3 (bullish divergence AEO) | Buy Signal | D4775 |
| /files/AdBBKquUjANcyr2nGKAW | Ultimate Oscillator – Chart 4 (bearish divergence CAT) | Sell Signal | D4776 |
| /files/NJOiaZM7e4rie8BzlFv6 | Ultimate Oscillator – Chart 5 (bearish divergence SBUX) | Sell Signal | D4777 |
| /files/29T5jvaXlFKFPwi1cxtU | Ultimate Oscillator – Chart 6 (ajustement timeframes Boeing) | Timeframes | D4779 |
| /files/368Tc2NZSKGoOroYYAbv | Ultimate Oscillator – Chart 7 (SharpCharts setup) | SharpCharts | D4780 |

---

## DÉCISIONS

### D4771 — Formule de calcul de l'Ultimate Oscillator (UO)
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/JnWlQKFl1xl5wbEWHsvZ) : L'UO est calculé selon : BP = Close − Min(Low, Prior Close) ; TR = Max(High, Prior Close) − Min(Low, Prior Close) ; Average7 = Sum7(BP)/Sum7(TR), Average14 = Sum14(BP)/Sum14(TR), Average28 = Sum28(BP)/Sum28(TR) ; UO = 100 × (4×Avg7 + 2×Avg14 + Avg28) / 7. Développé par Larry Williams en 1976, publié dans Stocks & Commodities Magazine en 1985.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, appliquer UO(7,14,28) pour mesurer le momentum Buying Pressure sur trois horizons simultanément ; l'horizon court (7) reçoit un poids double par rapport au medium (14) et quadruple par rapport au long (28).
*Catégorie : indicateurs_momentum*

### D4772 — Objectif multi-timeframe : réduire les fausses divergences
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md) : L'intégration de trois timeframes (le second est le double du premier, le troisième le double du second) vise explicitement à réduire les fausses divergences que produisent les oscillateurs mono-timeframe, qui surgissent en début d'avance puis forment une divergence baissière trompeuse.
**TRADEX-AI C1** : Pour GC/CL, préférer l'UO au RSI simple quand une tendance forte est en cours ; les divergences UO sont plus fiables que celles d'un oscillateur 14 périodes unique.
*Catégorie : indicateurs_momentum*

### D4773 — Interprétation : ligne centrale 50 comme seuil haussier/baissier
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md) : La ligne 50 est le seuil bull/bear de l'UO. Au-dessus de 50 : biais haussier (la tasse est à moitié pleine). En dessous de 50 : biais baissier. Fonctionne mieux avec des paramètres longs (ex. 20,40,80) et des tendances longues.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, utiliser UO > 50 comme filtre de biais directionnel avant de valider un signal d'entrée long ; UO < 50 = biais court à ne pas contre-trader.
*Catégorie : indicateurs_tendance*

### D4774 — Signal d'achat : divergence haussière en 3 étapes
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/fyyUQLEEdzpzCJc0yCDx) : Un signal d'achat valide requiert exactement : (1) Divergence haussière — UO forme un creux plus haut alors que le prix forme un creux plus bas ; (2) Le creux bas de la divergence doit être inférieur à 30 (condition de survente) ; (3) L'UO doit remonter au-dessus du sommet intermédiaire de la divergence pour confirmer.
**TRADEX-AI C1** : Pour GC/CL, appliquer ce filtre 3 conditions avant tout signal long généré par Belkhayate ; si UO < 30 + divergence haussière + confirmation break → renforcement du signal.
*Catégorie : gestion_risque_entree*

### D4775 — Alternative de déclenchement : franchissement du niveau 50
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/Y24cCFU02pqJ3hl3RPDR) : Pour les divergences haussières, le franchissement de la ligne 50 peut être utilisé comme déclencheur alternatif à la cassure du sommet de divergence, car l'analyse technique requiert de la flexibilité. Cela permet d'entrer plus tôt dans le mouvement.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, accepter UO cross au-dessus 50 comme signal d'entrée alternatif lorsqu'une divergence haussière est établie et que le prix a cassé une résistance à court terme.
*Catégorie : gestion_risque_entree*

### D4776 — Signal de vente : divergence baissière en 3 étapes
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/AdBBKquUjANcyr2nGKAW) : Un signal de vente valide requiert exactement : (1) Divergence baissière — UO forme un sommet plus bas alors que le prix forme un sommet plus haut ; (2) Le sommet haut de la divergence doit être supérieur à 70 (condition de surachat) ; (3) L'UO doit descendre en dessous du creux intermédiaire de la divergence pour confirmer.
**TRADEX-AI C1** : Pour GC/CL, ce filtre 3 conditions renforce un signal court Belkhayate : UO > 70 + divergence baissière + confirmation break = signal de vente haute qualité.
*Catégorie : gestion_risque_entree*

### D4777 — Divergence baissière non confirmée : attendre la cassure
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/NJOiaZM7e4rie8BzlFv6) : Une divergence baissière reste non confirmée tant que l'UO n'a pas cassé sous son creux de divergence. L'exemple SBUX montre qu'une première divergence en mi-mai n'a jamais déclenché (pas de cassure) alors qu'une seconde divergence plus grande a finalement confirmé fin juin.
**TRADEX-AI C1** : Ne jamais entrer en vente sur divergence baissière seule ; attendre la cassure du creux de divergence sur GC/HG avant d'exécuter. Signal non confirmé = ATTENDRE.
*Catégorie : gestion_risque_entree*

### D4778 — Niveaux extrêmes : 30 (survente) et 70 (surachat)
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md) : Les niveaux clés de l'UO sont 30 (zone de survente, condition requise pour le signal d'achat) et 70 (zone de surachat, condition requise pour le signal de vente). Ces niveaux garantissent que les divergences surviennent à des extrémités relatives de prix.
**TRADEX-AI C5** : Sur GC/CL, UO < 30 signale une zone de survente à surveiller pour renversement haussier ; UO > 70 signale une zone de surachat à surveiller pour renversement baissier — complémentaire au VIX pour le sentiment.
*Catégorie : indicateurs_momentum*

### D4779 — Ajustement de sensibilité selon la volatilité de l'actif
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md, /files/29T5jvaXlFKFPwi1cxtU) : Pour les actifs peu volatils qui ne génèrent pas de lectures extrêmes avec (7,14,28), raccourcir les paramètres (ex. 4,8,16) augmente la sensibilité. Pour les actifs très volatils, allonger les paramètres réduit les signaux parasites.
**TRADEX-AI C1** : Sur ZW (blé, plus volatil), tester UO(4,8,16) pour obtenir des lectures extrêmes exploitables. Sur GC (or, moins volatil en relatif), envisager UO(10,20,40) pour réduire le bruit.
*Catégorie : configuration*

### D4780 — Ne pas utiliser l'UO seul : complémentarité obligatoire
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md) : L'UO ne doit pas être utilisé seul. Il doit être confirmé par d'autres indicateurs, patterns chartistes et outils d'analyse. Les paramètres longs (20,40,80) fonctionnent mieux pour les biais directionnels à long terme.
**TRADEX-AI C1** : Dans TRADEX-AI, l'UO est un indicateur de confirmation du Cercle C1 (Prix/Belkhayate) ; il ne génère jamais de signal standalone — toujours combiné avec BGC/Direction/Énergie Belkhayate.
*Catégorie : configuration*

### D4781 — Formule de pondération asymétrique : court-terme privilégié
🔵 **ÉCOLE** (Source : ultimate_oscillator.md) : La pondération (×4 pour 7 périodes, ×2 pour 14 périodes, ×1 pour 28 périodes) donne un poids total de 7 (4+2+1). Le timeframe court reçoit 57% du poids total, le moyen 29%, le long 14%. Cette asymétrie reflète que le momentum récent est plus pertinent que l'historique.
**TRADEX-AI C1** : Comprendre que l'UO réagit principalement au momentum court terme (7 périodes) ; une lecture élevée signifie surtout une pression acheteuse récente forte, non nécessairement une tendance établie.
*Catégorie : indicateurs_momentum*

### D4782 — Achat Pressure (BP) : mesure de la pression acheteuse réelle
🔵 **ÉCOLE** (Source : ultimate_oscillator.md) : BP = Close − Min(Low, Prior Close). Cette formule intègre le clôture précédente pour tenir compte des gaps potentiels entre périodes. Elle mesure la pression acheteuse réelle en termes de l'amplitude du mouvement haussier par rapport au point bas le plus bas.
**TRADEX-AI C2** : Sur GC/CL/HG, le BP de l'UO est conceptuellement proche du Delta de l'order flow ATAS (pression acheteuse) — une convergence BP(UO) élevé + Delta ATAS positif renforce fortement un signal long.
*Catégorie : indicateurs_momentum*

### D4783 — Applicable sur tous les timeframes (intraday à mensuel)
🟢 **FAIT VÉRIFIÉ** (Source : ultimate_oscillator.md) : L'UO est utilisable sur graphiques intraday, journaliers, hebdomadaires ou mensuels. Le choix des paramètres doit être adapté selon le timeframe pour maintenir la génération de lectures extrêmes exploitables.
**TRADEX-AI C1** : L'UO sur range bars NT8 (timeframe TRADEX) est applicable ; adapter les paramètres — commencer avec (7,14,28) et ajuster selon la fréquence des extrêmes observés sur GC/CL.
*Catégorie : configuration*

### D4784 — Scan haussier : UO cross above 50 avec paramètres longs
🟡 **SYNTHÈSE** (Source : ultimate_oscillator.md) : Le scan haussier standard utilise UO(20,40,80) croisant au-dessus de 50, avec filtre volume (SMA20 > 40,000) et prix minimum (SMA60 > 20). Ce cross centreline indique un basculement du biais de baissier vers haussier sur horizon long.
**TRADEX-AI C1** : Adapter ce scan pour GC : UO(20,40,80) cross above 50 sur daily = signal de contexte macro haussier, à intégrer dans le Cercle C1 comme confirmation directionnelle long-terme avant un signal d'entrée intraday.
*Catégorie : indicateurs_tendance*

