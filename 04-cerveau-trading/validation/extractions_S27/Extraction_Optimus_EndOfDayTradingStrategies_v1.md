# Extraction Optimus — End-Of-Day Trading Strategies
**Source :** `bundles/optimusfutures/end_of_day_trading_strategies.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D8411 → D8425 · **Page :** https://optimusfutures.com/blog/end-of-day-trading-strategies/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : gestion du timing d'entrée EOD et règles de stop-loss sur les actifs tradables GC/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D8411 — Définition du trading End-Of-Day (EOD)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Le trading EOD consiste à analyser l'activité de la session précédente à la clôture du marché et à initier une position à l'ouverture suivante (ou en overnight pour les marchés 24h) — une seule décision de trade par session.
**TRADEX-AI C1** : Pour les actifs 24h comme GC, HG, CL, ZW, le signal EOD peut être émis après la clôture officielle CME et exécuté à l'ouverture électronique suivante; le moteur doit estampiller l'heure de génération du signal par rapport à la session de référence.
*Catégorie : timing*

### D8412 — Une seule entrée par session (principe de simplicité EOD)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Larry Williams, lors du World Cup Championship 1987 (10 000 $ → 1 100 000 $, +11 300%), ne plaçait qu'un seul ordre par jour à l'ouverture, basé sur les données EOD de la veille — sans scalping ni micro-trend.
**TRADEX-AI C1** : Le mode Manuel de TRADEX-AI est compatible EOD : un signal unique par session sur chaque actif tradable (GC/HG/CL/ZW) évite la sur-sollicitation du moteur et réduit le coût Claude API (niveau 3 déclenché une seule fois par session si les conditions de la grille /10 sont remplies).
*Catégorie : timing*

### D8413 — Structure logique d'un setup EOD : « If X then long/short, close EOD »
🟡 **SYNTHÈSE** (Source : end_of_day_trading_strategies.md) : Un setup EOD se formalise ainsi : « Si condition X est vraie à la clôture, alors entrer long/short à l'ouverture suivante et fermer la position à la clôture du jour suivant. » Exemples : (a) tendance baissière → short, stop au plus haut du jour, fermer EOD ; (b) 3 clôtures consécutives en hausse → short le lendemain ; (c) prix au-dessus de la MM50 ET session en dessous du plus bas de la veille → long.
**TRADEX-AI C1** : La grille de signal /10 de TRADEX-AI implémente implicitement cette logique ; l'horodatage « fermer EOD » doit figurer dans les métadonnées du signal transmis au mode Manuel pour qu'Abdelkrim sache quand sortir.
*Catégorie : configuration*

### D8414 — Stop-loss positionné au-dessus du plus haut de la session (short EOD)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Pour un short EOD sur tendance baissière, le stop-loss est placé au-dessus du plus haut de la session du jour de signal.
**TRADEX-AI C1** : Cette règle s'applique directement aux trades courts sur GC, CL, ZW en mode EOD; le risk_manager.py doit calculer le stop en fonction du High de la session de référence transmis par NT8 dans le JSON de données.
*Catégorie : gestion_risque_entree*

### D8415 — Avantage EOD 1 : réduction des frais de transaction
🔵 **ÉCOLE** (Source : end_of_day_trading_strategies.md) : Le trading EOD évite la « mort des mille stops » — cumul de frais de commission, de slippage et de stops successifs qui peuvent dépasser les profits journaliers sur les stratégies à haute fréquence.
**TRADEX-AI C4** : Pertinent pour la configuration du calcul de R/R : le seuil R/R ≥ 1:2 de TRADEX-AI est plus facilement atteint en EOD car le profit par trade est plus large (un seul trade contre plusieurs micro-trades).
*Catégorie : gestion_risque_entree*

### D8416 — Avantage EOD 2 : capture des mouvements mono-directionnels intraday
🔵 **ÉCOLE** (Source : end_of_day_trading_strategies.md) : Le trading à haute fréquence intraday empêche souvent de capturer un grand mouvement mono-directionnel sur la journée entière. Le trading EOD est conçu pour capturer ce mouvement en maintenant une seule position sur toute la session.
**TRADEX-AI C1** : En mode Auto, TRADEX-AI ne doit pas sortir prématurément d'une position EOD valide (score ≥ 7,0) sous prétexte de micro-fluctuations — la sortie doit être liée à la clôture de session ou à l'atteinte du stop/target.
*Catégorie : gestion_position_active*

### D8417 — Risque EOD 1 : développements overnight adverses (marchés 24h)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Sur les marchés 24h (futures GC, CL, etc.), une position EOD est exposée aux développements overnight — un mouvement adverse peut déclencher le stop pendant la nuit avant de se corriger.
**TRADEX-AI C4** : Le staleness_monitor.py doit surveiller les données NT8 en continu sur la nuit pour les positions ouvertes en mode Auto; si les données NT8 deviennent stales (timeout > seuil), le circuit breaker doit forcer la sortie ou bloquer toute nouvelle entrée.
*Catégorie : gestion_risque_entree*

### D8418 — Risque EOD 2 : gap de week-end (position maintenue vendredi soir)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Maintenir une position dans un instrument jusqu'au week-end expose au risque de gap à l'ouverture lundi — pouvant mettre le compte en débit si le gap est très large.
**TRADEX-AI C4** : Règle de protection TRADEX-AI : le mode Auto ne doit PAS initier de nouvelles positions EOD le vendredi après un seuil horaire (ex. 15h00 ET pour les futures US) et doit intégrer ce verrou dans risk_manager.py en tant que garde-fou G-EOD-01.
*Catégorie : gestion_risque_entree*

### D8419 — Risque EOD 3 : discours Fed et publications post-marché (earnings, FOMC)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Les discours des membres de la Fed post-marché ou les publications de résultats d'entreprises après la clôture peuvent provoquer des mouvements adverses sur les futures d'indices et les matières premières pendant la nuit.
**TRADEX-AI C4** : Le News Gate existant (bloc 30 min avant NFP/FOMC/CPI) doit être étendu pour couvrir les discours Fed post-séance ; les publications majeures nocturnes doivent être ajoutées au calendrier macro du moteur (cercle C4).
*Catégorie : macro_evenements*

### D8420 — Risque EOD 4 : manquer les développements overnight favorables (indices US)
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Si on attend l'ouverture officielle du marché US pour entrer (et non l'ouverture électronique 24h), le mouvement anticipé peut déjà s'être produit overnight — manquant l'essentiel du trade.
**TRADEX-AI C1** : Pour ES (indice de confirmation), TRADEX-AI doit consommer les données pre-market NT8 (session overnight) pour contextualiser la force ou faiblesse pré-ouverture et l'intégrer dans le calcul du score /10.
*Catégorie : timing*

### D8421 — Données EOD : condition de non-entrée après journée explosive
🟡 **SYNTHÈSE** (Source : end_of_day_trading_strategies.md) : Si la journée précédente a connu un mouvement explosif dans le sens du signal (blowout day), il ne faut PAS initier de position le lendemain dans ce sens — le mouvement est probablement épuisé.
**TRADEX-AI C1** : Cette règle de filtre anti-épuisement est un critère éliminatoire potentiel pour la grille /10 ; le moteur doit calculer l'amplitude de la dernière session (High-Low) et comparer à l'ATR N périodes pour détecter un blowout day.
*Catégorie : configuration*

### D8422 — Gestion EOD basée sur la moyenne mobile 50 jours (filtre de tendance)
🟡 **SYNTHÈSE** (Source : end_of_day_trading_strategies.md) : Stratégie EOD : si l'instrument trade au-dessus de sa MM50, entrer long chaque fois que la session du jour ferme en dessous du plus bas de la session précédente — stop à distance fractionnelle sous le plus bas de la session signal.
**TRADEX-AI C1** : La MM50 peut servir de filtre de tendance macrostructurel (C1) pour GC, CL, ZW ; une session clôturant sous le Low J-1 dans un contexte haussier (prix > MM50) constitue un signal de pullback achatable compatible Belkhayate.
*Catégorie : indicateurs_tendance*

### D8423 — EOD adapté au swing trading ET au day trading
🔵 **ÉCOLE** (Source : end_of_day_trading_strategies.md) : Les stratégies EOD peuvent être utilisées indifféremment pour le day trading (fermeture de position le jour même à la clôture) et le swing trading (maintien de la position plusieurs jours).
**TRADEX-AI C1** : L'interface TRADEX-AI doit distinguer deux modes de sortie EOD : « Close today » (day trade EOD) et « Hold overnight » (swing EOD) — Abdelkrim choisit en mode Manuel; le mode Auto utilise « Close today » par défaut (risque limité).
*Catégorie : timing*

### D8424 — Importance de la gestion du capital dans les stratégies EOD
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : La réussite de Larry Williams en 1987 était davantage attribuable à sa gestion du capital (stratégie « Optimal F » de Ralph Vince) qu'à ses setups de trading eux-mêmes — le setup était décrit comme « dumb » (basique).
**TRADEX-AI C1** : Confirmation que la qualité du signal (méthode Belkhayate) doit être couplée obligatoirement à une gestion de position rigoureuse dans risk_manager.py; le seuil de confiance ≥ seuil pour le mode Auto doit inclure un paramètre de taille de position, pas seulement une direction.
*Catégorie : gestion_risque_entree*

### D8425 — Backtest obligatoire avant implémentation d'une stratégie EOD
🟢 **FAIT VÉRIFIÉ** (Source : end_of_day_trading_strategies.md) : Il n'existe pas de recette universelle EOD — chaque stratégie doit être backtestée avec des calculs rigoureux pour valider son edge avant d'être tradée avec du capital réel.
**TRADEX-AI C1** : Toute règle Belkhayate issue de la KB et intégrée dans le prompt Claude doit avoir été validée sur données historiques NT8 (phase C du backtest range bars) avant d'être déployée en mode Auto.
*Catégorie : configuration*
