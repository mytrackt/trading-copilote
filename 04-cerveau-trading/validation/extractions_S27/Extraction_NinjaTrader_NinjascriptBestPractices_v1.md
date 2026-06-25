# Extraction NinjaTrader — NinjaScript Best Practices
**Source :** `bundles/ninjatrader/ninjascript_best_practices.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7971 → D7990 · **Page :** https://ninjatrader.com/futures/blogs/ninjascript-best-practices/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : bonnes pratiques NinjaScript pour fiabiliser les scripts NT8 connectés à TRADEX-AI (collecteurs de données, ATI).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D7971 — NinjaScript est event-driven et multi-threadé
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : NinjaScript est event-driven et multi-threadé. Le code réagit constamment au marché, à la plateforme et aux actions utilisateur. Si le script n'est pas écrit en tenant compte de cela, des bugs, lenteurs et comportements imprévisibles peuvent survenir.
**TRADEX-AI C1** : Tout script NinjaScript servant de collecteur de données pour TRADEX-AI doit respecter le cycle de vie des états — aucune logique de données dans SetDefaults, tout calcul dans DataLoaded ou plus tard.
*Catégorie : configuration*

### D7972 — Lifecycle NinjaScript : 5 états clés
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Les états NinjaScript via OnStateChange() : (1) SetDefaults — propriétés par défaut, couleurs, mode calcul. (2) Configure — ajout de series de données, paramètres. (3) DataLoaded — objets dépendants des données marché (indicateurs, instruments, barres). (4) Historical — logique sur barres historiques. (5) Realtime — logique sur données temps réel.
**TRADEX-AI C1** : Le script NT8 de collecte de données pour TRADEX doit initialiser les objets NT8 (indicateurs Belkhayate, BGC, Énergie) dans DataLoaded — jamais dans SetDefaults ou Configure.
*Catégorie : configuration*

### D7973 — SetDefaults : uniquement propriétés, zéro calcul marché
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Dans SetDefaults, on définit le nom, les options overlay, la fréquence de calcul (ex: Calculate.OnPriceChange). Aucun calcul ou logique dépendant des données marché ne doit être inclus — cette partie s'exécute avant que le script connaisse quoi que ce soit du marché.
**TRADEX-AI C1** : Dans tout script NT8 connecté à TRADEX-AI, Calculate = Calculate.OnPriceChange doit être défini dans SetDefaults. Aucune référence à TickSize, Close[], ou indicateurs dans ce bloc.
*Catégorie : configuration*

### D7974 — DataLoaded : état sûr pour initialiser calculs et variables
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Si des calculs, références de données, listes ou variables personnalisées sont nécessaires, il faut attendre au minimum l'état Configure ou DataLoaded. Ces états précoces n'ont pas encore accès aux données marché — y accéder trop tôt génère des erreurs ou résultats aberrants. Exemple : myCustomValue = TickSize * 5 doit être dans DataLoaded.
**TRADEX-AI C1** : Les paramètres dérivés des données marché NT8 (TickSize, Close, BarsInProgress) utilisés par le collecteur TRADEX doivent tous être initialisés dans l'état DataLoaded.
*Catégorie : configuration*

### D7975 — Réinitialisation des variables dans DataLoaded pour éviter résidus d'optimisation
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Lors de l'optimisation de stratégies, NinjaTrader peut réutiliser le même script sur plusieurs itérations. Les valeurs résiduelles peuvent persister si elles ne sont pas réinitialisées. Compteurs et listes doivent être réinitialisés dans State.DataLoaded pour garantir un état propre à chaque exécution.
**TRADEX-AI C1** : Dans le script NT8 de collecte pour TRADEX-AI, tous les compteurs, flags et listes accumulateurs doivent être réinitialisés dans DataLoaded — jamais laisser de résidu entre deux exécutions.
*Catégorie : configuration*

### D7976 — Multiple data series : uniquement dans Configure
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Si le script travaille avec plusieurs séries de données (multi-timeframe, multi-instrument), elles doivent être ajoutées dans l'état Configure. C'est le seul état permettant de créer des séries de données supplémentaires.
**TRADEX-AI C1** : Pour un script NT8 collectant GC + HG + CL + ZW simultanément (multi-instrument), les AddDataSeries() doivent être appelés dans Configure — pas dans DataLoaded ni OnBarUpdate.
*Catégorie : configuration*

### D7977 — Éléments UI : jamais avant la fin de l'état Historical
🟢 **FAIT VÉRIFIÉ** (Source : ninjascript_best_practices.md) : Si un script interagit avec le graphique (dessiner sur l'écran, créer des panneaux personnalisés), il faut attendre la sortie de la phase de chargement historique. Tenter d'utiliser des éléments UI trop tôt peut casser les visuels ou provoquer des erreurs inattendues.
**TRADEX-AI C1** : Tout script NT8 qui écrit des objets sur le graphique (flèches, zones, textes) pour visualiser les signaux Belkhayate doit vérifier que l'état Historical est passé avant tout DrawObject().
*Catégorie : configuration*

### D7978 — NinjaScript : code propre = moins de bugs en trading live
🟡 **SYNTHÈSE** (Source : ninjascript_best_practices.md) : Le respect des bonnes pratiques NinjaScript produit : (1) code plus lisible et déboguable, (2) scripts qui chargent plus vite et tournent plus fluidement, (3) moins de bugs — plus de null references ni comportements étranges lors de l'optimisation.
**TRADEX-AI C1** : La qualité du code NinjaScript des collecteurs NT8 impacte directement la fiabilité des données JSON reçues par le moteur Python TRADEX — tout bug NT8 se propage comme donnée corrompue ou manquante.
*Catégorie : gestion_risque_entree*

### D7979 — Calculate.OnPriceChange : mode de calcul recommandé pour indicateurs temps réel
🔵 **ÉCOLE** (Source : ninjascript_best_practices.md) : Calculate.OnPriceChange est cité comme exemple de réglage dans SetDefaults pour les scripts NinjaTrader. Ce mode déclenche le recalcul à chaque changement de prix (tick).
**TRADEX-AI C1** : Le collecteur NT8 qui alimente TRADEX-AI doit utiliser Calculate.OnPriceChange pour s'assurer que les données JSON sont actualisées à chaque tick — compatible avec la surveillance Python toutes les 2 secondes.
*Catégorie : configuration*

### D7980 — Optimisation NinjaScript : réutilisation de script entre itérations
🔵 **ÉCOLE** (Source : ninjascript_best_practices.md) : Lors d'une optimisation de stratégie, NinjaTrader peut réutiliser la même instance de script sur plusieurs itérations sans la réinstancier complètement. Les variables non réinitialisées conservent leurs valeurs précédentes, ce qui peut fausser les résultats d'optimisation.
**TRADEX-AI C1** : Cette règle s'applique au backtest des stratégies Belkhayate dans NT8 — toujours réinitialiser les compteurs de signal, les états circuit-breaker internes NT8, et les drapeaux de position dans DataLoaded.
*Catégorie : configuration*
