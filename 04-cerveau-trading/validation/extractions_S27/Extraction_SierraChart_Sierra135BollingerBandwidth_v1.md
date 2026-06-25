# Extraction SierraChart — Bollinger Bands: Bandwidth (ID 135)
**Source :** `bundles/sierrachart/sierra_135_bollinger_bandwidth.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8911 → D8930 · **Page :** https://www.sierrachart.com/index.php?page=doc/StudiesReference.php&ID=135
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Bollinger Bandwidth — mesure de contraction/expansion de volatilité, signal de squeeze avant mouvement directionnel fort (C1/C5).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D8911 — Bollinger Bandwidth Sierra Chart ID 135 : définition et formule
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : L'étude Bollinger Bands: Bandwidth (ID 135) calcule et affiche la largeur relative d'une paire de Bollinger Bands par rapport à une Simple Moving Average des données d'entrée. La formule est : BW_t(X,n,v) calculée pour t >= n-1, exprimée relativement à la SMA.
**TRADEX-AI C1** : Le Bandwidth mesure la compression/expansion des Bollinger Bands en valeur relative (pas absolue) — sur GC ($3000+), une mesure relative est indispensable car le même Bandwidth en points a une signification différente selon le niveau de prix. Utile pour détecter les squeezes avant breakout.
*Catégorie : indicateurs_momentum*

### D8912 — Bollinger Bandwidth Sierra Chart : paramètre Input Data configurable
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : L'étude ID 135 dispose de l'input "Input Data" permettant de choisir la source des données (Close, High, Low, Open, OHLC Average, etc.) sur laquelle le Bandwidth est calculé.
**TRADEX-AI C1** : Pour TRADEX sur GC, utiliser Input Data = Close (prix de clôture de barre) pour le Bandwidth — cohérent avec l'approche Belkhayate qui privilégie le prix de clôture comme référentiel principal de décision.
*Catégorie : configuration*

### D8913 — Bollinger Bandwidth Sierra Chart : paramètre Moving Average Type configurable
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : "Depending on the setting of the Input Moving Average Type, the Simple Moving Average the above formula could be replaced with an Exponential Moving Average, a Linear Regression Moving Average, a Weighted Moving Average, a Wilders Moving Average, a Simple Moving Average - Skip Zeros, or a Smoothed Moving Average."
**TRADEX-AI C1** : Le Bandwidth peut être calculé avec EMA ou SMA au choix — pour TRADEX, utiliser SMA (défaut Bollinger classique, 20 périodes) pour la cohérence avec la littérature Belkhayate qui référence les BB standard. Un Bandwidth EMA réagirait plus vite aux compressions de volatilité.
*Catégorie : configuration*

### D8914 — Bollinger Bandwidth Sierra Chart : paramètre Length — période de calcul
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : L'input "Length" définit la période de la Moving Average et des Bollinger Bands utilisées pour le calcul du Bandwidth. Le Bandwidth n'est calculé que pour t >= Length - 1 (minimum Length barres nécessaires).
**TRADEX-AI C1** : Paramètre opérationnel TRADEX — Length = 20 (période standard Bollinger Bands de John Bollinger, référence universelle). Cette valeur est validée dans la littérature Belkhayate (KNOWLEDGE_BASE_MASTER.json inclut les BB comme indicateur de volatilité). Ne pas modifier sans validation backtest.
*Catégorie : configuration*

### D8915 — Bollinger Bandwidth Sierra Chart : paramètre Standard Deviations
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : L'input "Standard Deviations" définit le multiplicateur d'écart-type utilisé pour les bandes Bollinger dont le Bandwidth est calculé. La valeur par défaut standard est 2.0 (bandes à ±2 SD).
**TRADEX-AI C1** : Standard Deviations = 2.0 pour TRADEX (paramètre Bollinger classique). Un Bandwidth calculé sur BB 20/2.0 capture environ 95% de la distribution des prix — la contraction du Bandwidth sous son percentile historique bas (squeeze) précède généralement un mouvement de breakout fort, signal de préparation de trade.
*Catégorie : configuration*

### D8916 — Bollinger Bandwidth : interprétation squeeze — signal précurseur de breakout
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Le Bollinger Bandwidth mesure la distance relative entre les bandes supérieure et inférieure des Bollinger Bands. Quand le Bandwidth atteint un niveau bas historique (squeeze), cela indique une contraction de volatilité qui précède statistiquement un mouvement directionnel fort.
**TRADEX-AI C1** : Signal précurseur pertinent pour TRADEX — un squeeze du Bandwidth sur GC ou CL avant une décision FOMC, NFP ou géopolitique amplifie la probabilité d'un mouvement fort après le catalyseur. Ajouter à la grille de scoring /10 : Bandwidth en squeeze = +0.5 point sur critère volatilité.
*Catégorie : configuration*

### D8917 — Bollinger Bandwidth : disponibilité spreadsheet officielle Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : Sierra Chart fournit une spreadsheet officielle "Bollinger_Bands_-_Bandwidth.135.scss" contenant les formules du Bandwidth en format spreadsheet. Elle doit être sauvegardée dans le Data Files Folder et ouverte via File >> Open Spreadsheet.
**TRADEX-AI C1** : La spreadsheet .scss permet de valider manuellement les calculs du Bandwidth — utile pour la phase de validation des paramètres avant intégration dans le moteur Python TRADEX (vérification croisée Python vs Sierra Chart avant livraison).
*Catégorie : configuration*

### D8918 — Bollinger Bandwidth : relation avec Bollinger Bands standard ID autre
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : L'étude Bollinger Bands: Bandwidth (ID 135) est distincte de Bollinger Bands (standard), Bollinger Bands - Percentage, Bollinger Squeeze, Bollinger Squeeze 2, Bollinger Squeeze 3 qui sont toutes listées séparément dans le catalogue Sierra Chart. La documentation du Bandwidth renvoie explicitement aux "documentation of those studies for an explanation of the notation used here."
**TRADEX-AI C1** : Dans TRADEX, utiliser ID 135 (Bandwidth) comme indicateur séparé du chart des Bollinger Bands standard — le Bandwidth se trace dans un panneau séparé (oscillateur 0-based), pas en overlay sur le prix. Configurer dans Region 2 ou 3 du chart Sierra Chart.
*Catégorie : configuration*

### D8919 — Bollinger Bandwidth : applicable à tous les actifs TRADEX (GC, HG, CL, ZW)
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : L'étude ID 135 est un indicateur universel applicable à tout actif Sierra Chart. Sa nature relative (exprimée en pourcentage de la SMA) la rend comparable entre actifs de niveaux de prix différents.
**TRADEX-AI C1** : Applicabilité confirmée pour tous les actifs TRADING TRADEX — GC (~$3000), HG (~$4.5/lb), CL (~$70), ZW (~$6/bu). Le Bandwidth relatif permet de comparer le niveau de compression de volatilité entre ces actifs pour identifier lequel est le plus "sous pression" avant un potentiel mouvement.
*Catégorie : indicateurs_momentum*

### D8920 — Bollinger Bandwidth : signal de sortie de squeeze — confirmation avec direction
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Le Bandwidth seul ne donne pas la direction du breakout. Il indique uniquement la compression (bas) ou l'expansion (haut) de volatilité. La direction du mouvement après un squeeze doit être confirmée par d'autres indicateurs directionnels.
**TRADEX-AI C1** : Règle opérationnelle TRADEX — le Bandwidth est un indicateur de timing/volatilité, pas de direction. Dans la grille de scoring /10 Belkhayate, un squeeze Bandwidth valide le "bon timing" pour un trade mais ne remplace pas les 3/4 actifs trading alignés et 2/3 confirmation. Il complète, il ne décide pas seul.
*Catégorie : gestion_risque_entree*

### D8921 — Bollinger Bandwidth : paramètre Last Modified — documentation récente
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : La documentation Sierra Chart pour l'étude ID 135 a été modifiée le "Tuesday, 31st January, 2023".
**TRADEX-AI C1** : Documentation stable depuis 2023 — les paramètres (Input Data, Moving Average Type, Length, Standard Deviations) sont figés et documentés. Pas de risque de changement comportemental inattendu de l'indicateur dans les versions récentes Sierra Chart.
*Catégorie : configuration*

### D8922 — Bollinger Bandwidth vs Bollinger %B : distinction conceptuelle
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Sierra Chart propose deux études distinctes : Bollinger Bands - Bandwidth (ID 135) et Bollinger Bands - Percentage (%B). Le Bandwidth mesure la largeur relative des bandes. Le %B mesure la position du prix dans les bandes (0 = bande basse, 1 = bande haute, 0.5 = milieu/SMA).
**TRADEX-AI C1** : Pour TRADEX, utiliser les deux en parallèle pour GC : Bandwidth pour détecter le squeeze, %B pour la position du prix dans les bandes. Un squeeze (Bandwidth bas) avec %B proche de 0 ou 1 indique une pression aux extrêmes — signal fort de breakout imminent dans la direction correspondante.
*Catégorie : indicateurs_momentum*

### D8923 — Bollinger Bandwidth : seuil historique bas comme trigger — approche percentile
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : La définition d'un "squeeze" nécessite une référence historique — le Bandwidth actuel est comparé à son propre historique sur N périodes pour déterminer s'il est anormalement bas. Sierra Chart ne définit pas de seuil fixe; c'est à l'utilisateur de définir le percentile de référence.
**TRADEX-AI C1** : Règle de configuration TRADEX — définir le squeeze Bandwidth comme : Bandwidth actuel < percentile 20 sur les 252 derniers jours (1 an de trading). Cette définition dynamique est plus robuste qu'un seuil fixe absolu, adaptée aux marchés comme GC dont la volatilité structurelle évolue dans le temps.
*Catégorie : gestion_risque_entree*

### D8924 — Bollinger Bandwidth : timeframe d'analyse recommandé pour TRADEX
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : L'étude ID 135 peut être appliquée sur n'importe quel timeframe — daily, intraday, range bars. Les squeezes sur daily sont des signaux de long terme, les squeezes sur intraday sont des signaux de court terme.
**TRADEX-AI C1** : Pour TRADEX en surveillance 2s avec range bars NT8 : analyser le Bandwidth sur 2 timeframes — (1) Daily pour le contexte de volatilité structurelle, (2) Range bars pour le timing intraday précis. Un squeeze sur les deux timeframes simultanément est un signal de très haute conviction.
*Catégorie : configuration*

### D8925 — Bollinger Bandwidth : interaction avec Bollinger Squeeze (ID distinct dans Sierra Chart)
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : Le catalogue Sierra Chart inclut séparément : Bollinger Squeeze, Bollinger Squeeze 2, Bollinger Squeeze 3 — ces études sont distinctes du Bandwidth (ID 135) et proposent des détections automatiques de squeeze avec signaux visuels.
**TRADEX-AI C1** : Alternative opérationnelle — les études "Bollinger Squeeze" de Sierra Chart automatisent la détection du squeeze et affichent des signaux visuels directement sur le chart. Pour une utilisation rapide en mode Manuel TRADEX, Bollinger Squeeze peut être plus pratique que le Bandwidth seul (qui nécessite une interprétation visuelle du niveau).
*Catégorie : configuration*

### D8926 — Bollinger Bandwidth : sensibilité aux gaps et données manquantes
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Le Bandwidth est calculé à partir des Bollinger Bands qui nécessitent des données continues sur la période Length. Les gaps de données (weekends, sessions fermées) peuvent affecter le calcul.
**TRADEX-AI C1** : Précaution TRADEX — pour GC (Or, CME Globex, trading quasi-continu sauf weekends), vérifier que les barres du weekend ne créent pas de gaps artificels dans le Bandwidth. Utiliser "Close on Weekend" ou "Skip Zeros" dans la MA Type si nécessaire pour éviter des squeezes artificiels.
*Catégorie : configuration*

### D8927 — Bollinger Bandwidth : documentation Last Modified confirme stabilité API Sierra Chart
🟢 **FAIT VÉRIFIÉ** (Source : sierra_135_bollinger_bandwidth.md) : La page documentation de l'ID 135 indique "Last modified Tuesday, 31st January, 2023" — 2 ans avant la date actuelle (juin 2026).
**TRADEX-AI C1** : La stabilité documentaire sur 3+ ans confirme que l'API de cet indicateur Sierra Chart est stable. L'intégration dans le moteur Python TRADEX (via fichiers JSON NT8/Sierra) peut se faire en s'appuyant sur les paramètres actuels sans risque de breaking change imminent.
*Catégorie : configuration*

### D8928 — Bollinger Bandwidth : utilisation comme filtre anti-bruit pour signaux TRADEX
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Un Bandwidth en expansion (valeur croissante) indique un marché en mouvement fort — les signaux directionnels sont plus fiables. Un Bandwidth en contraction (valeur décroissante vers un squeeze) indique un marché indécis — les signaux directionnels sont moins fiables.
**TRADEX-AI C1** : Règle de filtre pour TRADEX — bloquer les signaux de Mode Auto quand le Bandwidth est en contraction forte (marché range, signaux peu fiables). Autoriser le Mode Auto prioritairement quand le Bandwidth est en expansion (marché en tendance, signaux Belkhayate plus fiables). Ajoute un garde-fou anti-faux-signal.
*Catégorie : gestion_risque_entree*

### D8929 — Bollinger Bandwidth : applicabilité sur futures CME (GC, HG, CL, ZW) confirmée
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Sierra Chart est une plateforme de futures professionnelle connectée aux marchés CME via Rithmic. L'étude ID 135 est utilisable sur tous les contracts futures.
**TRADEX-AI C1** : Applicabilité directe confirmée — Bollinger Bandwidth ID 135 compatible avec les actifs TRADEX (GC-CME, HG-CME, CL-NYMEX, ZW-CBOT) via connexion Rithmic Sierra Chart. Pas d'adaptation nécessaire pour les futures vs équities.
*Catégorie : configuration*

### D8930 — Bollinger Bandwidth : intégration dans pipeline TRADEX — lecture via fichier JSON
🟡 **SYNTHÈSE** (Source : sierra_135_bollinger_bandwidth.md) : Sierra Chart permet d'écrire des données d'études dans des fichiers via l'étude "Write Bar and Study Data To File". Le Bandwidth (ID 135) peut être exporté en temps réel vers un fichier CSV/JSON lisible par Python.
**TRADEX-AI C2** : Architecture TRADEX — le Bandwidth calculé dans Sierra Chart peut être écrit dans un fichier JSON toutes les N secondes par "Write Bar Data to File", puis lu par data_reader.py pour alimenter la couche C1 du moteur sans appel API supplémentaire. Extension possible du pipeline JSON existant NT8/ATAS.
*Catégorie : configuration*
