# Extraction SierraChart — Relative Momentum Index (ID 255)
**Source :** `bundles/sierrachart/sierra_255_rmi.md` (HTTP 200) + 0 images certifiées
**Méthode images :** ancrage figcaption · 0/0 certifiées · 0 à vérifier
**Décisions :** D9151 → D9170 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=255
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Variante RSI qui mesure le momentum sur n périodes (RMI Length) au lieu de 1 période — réduit le bruit et améliore la détection des zones de surachat/survente sur les matières premières.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D9151 — Définition du Relative Momentum Index (RMI)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Le RMI est une variante du RSI qui calcule les changements haussiers (U) et baissiers (D) sur n périodes au lieu d'une seule période comme le RSI standard. Les formules U_t(X, n) et D_t(X, n) mesurent la variation sur n barres en arrière, lissant ainsi le signal de momentum.
**TRADEX-AI C1** : Le RMI réduit le bruit du RSI standard sur les marchés de matières premières volatils (GC, CL). En mesurant le momentum sur plusieurs barres, il filtre les micro-mouvements et se concentre sur la tendance de fond — pertinent pour le cercle C1 Belkhayate.
*Catégorie : indicateurs_momentum*

### D9152 — Paramètre RMI Length (n)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable n = nombre de périodes en arrière pour calculer la variation U (hausse) et D (baisse). Pour 0 ≤ t < n, les formules de warm-up s'appliquent. Pour t ≥ n, la variation complète sur n périodes est calculée.
**TRADEX-AI C1** : n contrôle la "mémoire" du RMI. n=3 (court) → sensible, adapté aux range bars NT8. n=14 (moyen) → équilibre signal/bruit, standard. Sur GC avec range bars, tester n=3 à n=5 pour capter les pivots intraday de la méthode Belkhayate.
*Catégorie : indicateurs_momentum*

### D9153 — Paramètre RMI Moving Average Length (nMA)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable nMA = longueur de la moyenne mobile appliquée aux séries U et D avant le calcul du ratio RMI. Le RMI est calculé à partir de t = max{n, nMA} − 1 (initialisation à 0) puis pour t ≥ max{n, nMA}.
**TRADEX-AI C1** : nMA agit comme un lisseur sur les changements de momentum. nMA plus élevé → signal plus lisse, moins de faux croisements des niveaux overbought/oversold. Recommandation : nMA = 14 pour cohérence avec les ATR et autres paramètres TRADEX-AI.
*Catégorie : indicateurs_momentum*

### D9154 — Paramètre RMI Moving Average Type
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable permettant de choisir le type de moyenne mobile pour les séries U et D : SMA (défaut), EMA, Linear Regression MA, Weighted MA, Wilders MA, SMA Skip Zeros, ou Smoothed MA.
**TRADEX-AI C1** : Le choix du type de MA change significativement le comportement du RMI. Wilders MA (utilisée dans le RSI standard) produit un RMI le plus proche du RSI classique. EMA produit un signal plus réactif. Pour TRADEX-AI, standardiser sur Wilders MA pour cohérence avec le RSI Belkhayate si utilisé en parallèle.
*Catégorie : indicateurs_momentum*

### D9155 — Paramètre Overbought Value
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable pour le niveau de surachat (horizontal line). Affiché comme ligne horizontale sur le graphique du RMI.
**TRADEX-AI C1** : Valeur standard RSI/RMI = 70. Sur matières premières en forte tendance (GC bull market), le niveau peut être relevé à 75-80 pour éviter les sorties prématurées. À paramétrer dans settings.py comme constante RMI_OVERBOUGHT par actif (GC, HG, CL, ZW).
*Catégorie : indicateurs_momentum*

### D9156 — Paramètre Oversold Value
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable pour le niveau de survente (horizontal line). Affiché comme ligne horizontale sur le graphique du RMI.
**TRADEX-AI C1** : Valeur standard = 30. En bear market sur CL (Pétrole), le niveau peut être abaissé à 20-25. Dans la grille /10 TRADEX-AI, RMI < oversold_value peut être une condition C1 pour signal ACHAT (si autres cercles confirment).
*Catégorie : indicateurs_momentum*

### D9157 — Paramètre Midline Value
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Input configurable pour la ligne médiane du RMI. Affiché comme troisième ligne horizontale de référence.
**TRADEX-AI C1** : Valeur standard = 50. La ligne médiane sépare momentum haussier (RMI > 50) de momentum baissier (RMI < 50). Dans TRADEX-AI, un croisement de la midline peut être utilisé comme condition de direction C1 pour confirmer ou infirmer un signal Belkhayate.
*Catégorie : indicateurs_momentum*

### D9158 — Période de warm-up : max{n, nMA} barres
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : Le RMI est initialisé à zéro à t = max{n, nMA} − 1. Avant cette date, aucune valeur significative n'est disponible. Le calcul complet commence à t = max{n, nMA}.
**TRADEX-AI C1** : Avec n=14, nMA=14, warm-up = 14 barres avant le premier RMI fiable. À intégrer dans staleness_monitor.py : ignorer les N premières valeurs après reconnexion NT8 pour éviter des signaux RMI erronés à la mise en route du moteur.
*Catégorie : configuration*

### D9159 — Formule U_t et D_t : variation sur n périodes (non 1 période)
🔵 **ÉCOLE** (Source : sierra_255_rmi.md) : U_t(X, n) = max(X_t − X_{t−n}, 0) ; D_t(X, n) = max(X_{t−n} − X_t, 0). Contrairement au RSI où n=1 (variation barre à barre), le RMI utilise la variation sur n barres — c'est la différence fondamentale.
**TRADEX-AI C1** : Cette formule capture le momentum à plus longue portée. Pour range bars NT8, n=3 correspond à une variation sur 3 barres (momentum court terme). n=14 = momentum moyen terme. La combinaison RMI(3) + RMI(14) peut créer un système de confirmation croisée double.
*Catégorie : indicateurs_momentum*

### D9160 — Calcul du RMI via SMA des changements U et D
🟢 **FAIT VÉRIFIÉ** (Source : sierra_255_rmi.md) : RMI_t = 100 × SMA(U, nMA) / (SMA(U, nMA) + SMA(D, nMA)). Même structure de ratio que le RSI classique (RS = UpAvg / DownAvg), mais avec les SMA (ou autre type MA configuré) de U et D sur nMA périodes.
**TRADEX-AI C1** : La formule garantit que RMI ∈ [0, 100], avec 50 comme équilibre parfait. Valeur > 70 = momentum haussier fort ; < 30 = momentum baissier fort. Compatible directement avec les seuils RSI utilisés dans la méthode Belkhayate sans recalibrage.
*Catégorie : indicateurs_momentum*

### D9161 — RMI vs RSI : avantage sur les marchés à tendance
🟡 **SYNTHÈSE** (Source : sierra_255_rmi.md) : Le RMI mesure le momentum sur n périodes au lieu de 1, ce qui le rend moins sensible aux retournements d'une seule barre. Sur les marchés en tendance forte (GC bull run), le RSI standard peut rester en zone surachat longtemps et induire des fausses sorties ; le RMI avec n>1 reste plus stable.
**TRADEX-AI C1** : Sur GC (Or) en tendance haussière longue, préférer RMI(n=5, nMA=14) au RSI(14) standard pour éviter les signaux de survente prématurés. Le RMI reste en zone neutre (40-70) pendant les pullbacks normaux, contrairement au RSI qui peut plonger sous 30 lors d'une simple correction.
*Catégorie : gestion_risque_entree*

### D9162 — Fichier spreadsheet de référence : Relative_Momenum_Index.255.scss
🔵 **ÉCOLE** (Source : sierra_255_rmi.md) : Sierra Chart fournit `Relative_Momenum_Index.255.scss` (noter la faute de frappe dans le nom : "Momenum" sans 't'). Date de dernière modification : 24 janvier 2025.
**TRADEX-AI C1** : Fichier de validation pour implémentation Python. La faute de frappe dans le nom du fichier est dans la documentation officielle Sierra Chart — à respecter tel quel si on référence ce fichier dans du code TRADEX-AI.
*Catégorie : configuration*

### D9163 — Application RMI pour ZW (Blé) : détection surachat/survente saisonnier
🟡 **SYNTHÈSE** (Source : sierra_255_rmi.md) : Le Blé (ZW) présente des cycles saisonniers marqués avec des zones de surachat en période de stress géopolitique ou climatique. Le RMI avec n>1 peut mieux capturer ces momentum saisonniers que le RSI.
**TRADEX-AI C1** : Pour ZW, RMI(n=5, nMA=14) avec overbought=75, oversold=25 peut filtrer les signaux en périodes de forte saisonnalité. À croiser avec les données macro C4 (saison récoltes, USDA reports) pour validation du signal dans la grille /10.
*Catégorie : saisonnalite*
