# Chapitre 12 — Macro et actualités

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 12.0 Pourquoi la macro est incontournable pour les futures

🟢 Les futures sont des contrats sur des actifs réels (pétrole, or, indices boursiers). Contrairement aux actions individuelles, ces actifs sont directement pilotés par des forces macroéconomiques mondiales : politique monétaire, offre/demande physique, géopolitique, flux de capitaux. Ignorer la macro en tradant des futures revient à naviguer sans connaître les courants marins.

🟢 **Principe de hiérarchie des drivers :** sur le court terme (intraday), la technique domine. Sur le moyen terme (jours à semaines), la macro domine. Quand la macro et la technique sont alignées, la probabilité de succès augmente. Quand elles s'opposent, la macro finit généralement par l'emporter.

🟡 **Limite de ce chapitre :** la macro évolue constamment (⏳). Les relations présentées sont des mécanismes structurels documentés — pas des règles permanentes. Certaines corrélations peuvent s'inverser temporairement selon le régime (risk-on / risk-off, cycle de taux, etc.).

---

## 12.1 La politique monétaire — Le driver dominant

### 12.1.1 La Fed et son impact sur les actifs TRADEX-AI

🟢 **La Réserve Fédérale américaine (Fed)** est la banque centrale la plus influente au monde pour les actifs libellés en USD. Ses décisions de politique monétaire impactent directement CL, GC et ES.

🟢 **Mécanisme de transmission — Taux directeurs :**

Fed Monte les taux →

    USD se renforce →

        Or (GC) baisse (coûte plus cher en devises étrangères)

        Pétrole (CL) baisse tendanciellement (USD fort \= pétrole cher pour acheteurs non-USD)

        Actions (ES) baissent (coût du capital augmente, valorisations comprimées)

Fed Baisse les taux →

    USD se fragilise →

        Or (GC) monte

        Pétrole (CL) monte tendanciellement

        Actions (ES) montent (liquidité abondante, valorisations expansives)

🔴 **Ces relations sont tendancielles, pas mécaniques.** Il existe de nombreuses périodes où elles ne tiennent pas (ex. : hausse des taux \+ hausse de l'or si l'inflation est perçue comme hors de contrôle). Ne pas les utiliser comme règles déterministes.

### 12.1.2 Le calendrier FOMC

🟢 **FOMC (Federal Open Market Committee) :** comité de la Fed qui décide des taux directeurs. 8 réunions par an, calendrier publié à l'avance sur **federalreserve.gov**.

🟢 **Structure d'une réunion FOMC :**

- J-1 : fin de la période de "blackout" (les membres de la Fed ne font plus de déclarations publiques)  
- J (mercredi, \~14h00 ET) : annonce de la décision de taux  
- J (mercredi, \~14h30 ET) : conférence de presse du Président de la Fed  
- Jours suivants : publications des minutes FOMC (\~3 semaines après)

🟢 **Impact sur les marchés :**

- La décision elle-même : impact immédiat mais souvent "priced in" si conforme aux attentes  
- La conférence de presse : souvent le vrai driver (ton du discours, forward guidance)  
- Les minutes : impact modéré, 3 semaines après

🟡 **Règle TRADEX-AI :** pas d'entrée nouvelle dans les 2 heures encadrant l'annonce FOMC. Réduire la taille des positions existantes ou fermer avant l'annonce si le trade est proche du stop.

### 12.1.3 Les autres banques centrales

🟢 **BCE (Banque Centrale Européenne) :** impact indirect sur CL et GC via l'EUR/USD. Un euro fort \= dollar faible \= or et pétrole tendanciellement plus élevés.

🟢 **OPEP+ :** pour le crude oil, l'OPEP+ (Organisation des Pays Exportateurs de Pétrole \+ Russie et alliés) est aussi influente que la Fed. Ses décisions de quotas de production impactent directement les prix CL.

⏳ **Calendrier OPEP+ :** réunions irrégulières, souvent trimestrielles. Annonces disponibles sur **opec.org**. Les décisions surprises (coupes de production non planifiées) provoquent des gaps importants.

---

## 12.2 Les indicateurs macroéconomiques clés

### 12.2.1 Indicateurs US — Impact sur ES, GC, CL

🟢 **Tableau des indicateurs avec sources officielles vérifiables :**

| Indicateur | Fréquence | Source officielle | Actifs impactés | Impact typique |
| :---- | :---- | :---- | :---- | :---- |
| Non-Farm Payrolls (NFP) | Mensuel (1er vendredi) | bls.gov | ES, GC, CL | Fort |
| CPI (Inflation) | Mensuel | bls.gov | ES, GC | Fort |
| PCE (inflation core Fed) | Mensuel | bea.gov | ES, GC | Fort |
| GDP (PIB US) | Trimestriel (3 révisions) | bea.gov | ES, GC, CL | Fort |
| ISM Manufacturing PMI | Mensuel (1er jour ouvré) | ismworld.org | ES, CL | Moyen |
| ISM Services PMI | Mensuel (3e jour ouvré) | ismworld.org | ES | Moyen |
| Retail Sales | Mensuel | census.gov | ES | Moyen |
| Initial Jobless Claims | Hebdomadaire (jeudi) | dol.gov | ES | Faible-Moyen |
| JOLTS (offres d'emploi) | Mensuel | bls.gov | ES | Moyen |
| Consumer Confidence (CB) | Mensuel | conference-board.org | ES | Faible |

🔴 **"Impact typique" est une convention journalistique**, pas une mesure statistique rigoureuse. L'impact réel dépend de l'écart entre le chiffre publié et les attentes du consensus (le "surprise factor").

### 12.2.2 Le modèle surprise (Citigroup Economic Surprise Index)

🟢 **Principe :** ce qui importe en trading n'est pas la valeur absolue d'un indicateur — c'est son écart par rapport aux attentes du consensus.

Surprise \= Valeur publiée − Consensus des économistes

Surprise positive (valeur \> consensus) → généralement haussier pour l'actif associé

Surprise négative (valeur \< consensus) → généralement baissier

🟢 **Citigroup Economic Surprise Index (CESI) :** indicateur qui agrège les surprises économiques sur une période glissante. Disponible sur Bloomberg (payant) et certains agrégateurs gratuits. Indique si les données économiques surprennent globalement à la hausse ou à la baisse.

🔴 Les marchés "achètent la rumeur, vendent la nouvelle" — une surprise positive sur un indicateur peut générer une baisse si le marché avait déjà intégré une surprise encore plus positive. Ce phénomène est réel mais difficile à anticiper mécaniquement.

### 12.2.3 Indicateurs spécifiques au Crude Oil (CL)

🟢 **EIA Weekly Petroleum Status Report :**

- **Qui :** Energy Information Administration (gouvernement US)  
- **Quand :** chaque mercredi \~10h30 ET  
- **Contenu :** variation des stocks de pétrole brut, stocks d'essence, stocks de distillats  
- **Source :** eia.gov/petroleum/supply/weekly/  
- **Impact :** fort sur CL — les variations de stocks supérieures au consensus provoquent des mouvements de 0,5–2 % sur CL en quelques minutes

🟢 **API Weekly Statistical Bulletin :**

- **Qui :** American Petroleum Institute (association privée)  
- **Quand :** chaque mardi \~16h30 ET (J-1 avant l'EIA)  
- **Contenu :** même données que l'EIA mais estimations privées  
- **Statut :** 🟡 les chiffres API préfigurent souvent (pas toujours) la direction de l'EIA  
- **Accès :** données complètes réservées aux membres payants. Certains agrégateurs publient les chiffres en accès libre.

🟢 **Baker Hughes Rig Count :**

- **Qui :** Baker Hughes (fournisseur de services pétroliers)  
- **Quand :** chaque vendredi \~13h00 ET  
- **Contenu :** nombre de plateformes pétrolières actives aux USA  
- **Source :** bakerhughes.com/company/news/oil-field-services-news  
- **Impact :** indicateur avancé de la production future. Augmentation du rig count → production future plus élevée → pression baissière sur CL (tendanciellement).

🟢 **Réunions OPEP+ :**

- Décisions de production quotas  
- Annonces disponibles sur opec.org  
- Impact : potentiellement très fort (gaps de 2–5 % sur CL possibles)

### 12.2.4 Indicateurs spécifiques à l'Or (GC)

🟢 **Drivers fondamentaux de l'or :**

| Driver | Mécanisme | Corrélation | Statut |
| :---- | :---- | :---- | :---- |
| Taux réels US (TIPS yield) | Or ne verse pas de coupon → coût d'opportunité | Négative forte | 🟢 Structurelle |
| DXY (Dollar Index) | Or coté en USD | Négative | 🟢 Structurelle |
| Inflation (CPI/PCE) | Or \= hedge inflation | Positive tendancielle | 🟡 Variable selon régime |
| Risque géopolitique | Valeur refuge | Positive en stress | ⏳ Épisodique |
| Demande physique (Chine, Inde) | Acheteurs nets saisonniers | Positive saisonnière | 🟡 Tendance multi-annuelle |
| Achats banques centrales | Demande institutionnelle | Positive | ⏳ Politique variable |

🟢 **TIPS Yield (Treasury Inflation-Protected Securities) :** le rendement réel des obligations indexées sur l'inflation américaine est le driver fondamental le plus documenté de l'or. Disponible sur **fred.stlouisfed.org** (FRED, base de données de la Fed de St. Louis — accès gratuit).

🔴 **"L'or est toujours un safe haven" est un mythe partiel.** En 2008, l'or a chuté en même temps que les actions pendant la phase de liquidation initiale (besoin de cash) avant de monter ensuite. En 2022, l'or a sous-performé malgré l'inflation élevée car les taux réels montaient. Le contexte macro prime toujours sur le label "valeur refuge".

---

## 12.3 Le cycle Risk-On / Risk-Off

### 12.3.1 Définition et mécanisme

🟢 **Risk-On :** les investisseurs ont de l'appétit pour le risque. Ils achètent des actifs risqués (actions, pétrole, monnaies émergentes) et vendent les actifs refuge.

🟢 **Risk-Off :** les investisseurs fuient le risque. Ils vendent les actifs risqués et achètent les actifs refuge (or, JPY, CHF, obligations US, USD).

🟢 **Actifs TRADEX-AI dans le cycle :**

| Actif | Risk-On | Risk-Off |
| :---- | :---- | :---- |
| ES (S\&P 500\) | Hausse | Baisse |
| CL (Crude Oil) | Hausse tendancielle | Baisse tendancielle |
| GC (Gold) | Neutre / légère baisse | Hausse |
| USD (DXY) | Baisse (souvent) | Hausse (valeur refuge) |
| VIX | Baisse | Hausse |

🔴 Ces associations sont tendancielles sur le moyen terme, pas mécaniques sur le court terme. CL peut monter en risk-off si la cause est géopolitique (guerre affectant l'offre de pétrole). GC peut baisser en risk-off si la liquidation force les ventes (2008, mars 2020 initial).

### 12.3.2 Indicateurs du sentiment Risk-On / Risk-Off

🟢 **VIX (CBOE Volatility Index) :**

- Mesure la volatilité implicite des options sur le S\&P 500  
- VIX \< 15 : faible peur, risk-on  
- VIX 15–25 : incertitude modérée  
- VIX \> 25 : risk-off, stress de marché  
- VIX \> 40 : panique / crise  
- Source : cboe.com

🟢 **Spread High Yield (HY spread) :** différentiel de rendement entre obligations d'entreprises à haut rendement et obligations d'État. Un spread croissant signale une fuite vers la qualité (risk-off). Disponible sur FRED : fred.stlouisfed.org (série BAMLH0A0HYM2).

🟡 **Copper/Gold ratio :** le cuivre est un baromètre de l'activité industrielle mondiale (risk-on si hausse). L'or est un refuge (risk-off si hausse). Le ratio cuivre/or augmente en risk-on, diminue en risk-off. Corrélation documentée avec les taux d'intérêt.

---

## 12.4 La géopolitique et les marchés de matières premières

### 12.4.1 Géopolitique et Crude Oil

🟢 **Le pétrole est l'actif le plus sensible à la géopolitique** parmi les actifs TRADEX-AI. Les raisons structurelles :

- Production concentrée géographiquement (Moyen-Orient, Russie, USA)  
- Transport via routes maritimes stratégiques (détroit d'Ormuz, Bosphore, Canal de Suez)  
- Arme économique potentielle (embargos, sanctions)

🟢 **Types d'événements géopolitiques et impact sur CL :**

| Événement | Impact typique sur CL | Durée typique | Statut |
| :---- | :---- | :---- | :---- |
| Conflit armé dans région productrice | Fort haussier | Semaines à mois | ⏳ Contextuel |
| Sanctions sur pays producteur | Haussier | Mois à années | ⏳ |
| Fermeture détroit d'Ormuz (menace) | Fort haussier | Jours à semaines | ⏳ |
| Accord de paix / levée de sanctions | Baissier | Variable | ⏳ |
| Décision OPEP+ production cut surprise | Fort haussier | Semaines | ⏳ |
| Décision OPEP+ production increase surprise | Fort baissier | Semaines | ⏳ |

🔴 **La durée et l'amplitude de l'impact géopolitique sont imprévisibles.** Les marchés "price in" rapidement le choc initial, puis la volatilité diminue à moins que la situation évolue. Pas de règle quantitative fiable.

### 12.4.2 Géopolitique et Or

🟢 **L'or bénéficie des crises géopolitiques** comme valeur refuge. Cet effet est réel mais temporaire dans la plupart des cas — l'or revient vers ses drivers fondamentaux (taux réels, DXY) une fois la prime de risque dissipée.

🟡 **Exception historique notable :** les guerres prolongées avec impact sur l'offre mondiale de matières premières (ex. : 2022, invasion Ukraine → impact persistant sur énergie \+ or) maintiennent une prime géopolitique durable.

---

## 12.5 La saisonnalité des marchés

### 12.5.1 Saisonnalité du Crude Oil

🟢 **Drivers saisonniers documentés sur CL :**

| Période | Phénomène | Impact typique |
| :---- | :---- | :---- |
| Janvier–Mars | Fin de la saison de chauffage (heating oil) | Tendance baissière demande |
| Avril–Juin | "Driving season" aux USA commence | Tendance haussière demande essence |
| Juillet–Août | Pic de la driving season | Demande élevée |
| Septembre–Octobre | Refinery maintenance season | Volatilité stockage |
| Novembre–Décembre | Début saison chauffage | Reprise demande distillats |

🟡 Ces patterns saisonniers sont des tendances historiques moyennes, pas des certitudes annuelles. Une surabondance d'offre ou une récession peut effacer les effets saisonniers. À utiliser comme contexte, jamais comme signal seul.

### 12.5.2 Saisonnalité de l'Or

🟡 **Patterns saisonniers historiques documentés sur GC :**

| Période | Phénomène | Impact typique |
| :---- | :---- | :---- |
| Janvier–Février | Demande bijouterie Chine (Nouvel An Chinois) | Haussier tendanciel |
| Août–Octobre | Saison des mariages en Inde (achat bijoux) | Haussier tendanciel |
| Novembre–Décembre | Achats de fin d'année, hedging institutionnel | Variable |

🔴 La saisonnalité de l'or est moins robuste que celle du pétrole car les drivers fondamentaux (taux réels, DXY) dominent largement les effets saisonniers. À utiliser uniquement comme contexte secondaire.

### 12.5.3 Saisonnalité des indices (ES)

🟡 **"Sell in May and Go Away" :** convention boursière ancienne, tendance historique à la sous-performance des actions entre mai et octobre. 🔴 Cette convention est très faible statistiquement sur les données récentes et ne constitue pas une stratégie à part entière.

🟡 **Effet janvier :** tendance historique à la hausse des actions en janvier (rééquilibrages, nouveaux objectifs annuels). 🔴 Même remarque — tendance affaiblie sur les 20 dernières années.

🟢 **Saisonnalité des volumes :** volume naturellement bas en août (vacances estivales dans les marchés occidentaux) et entre Noël et Nouvel An. Période à éviter pour les stratégies dépendant de la liquidité.

---

## 12.6 Les sources d'information — Hiérarchie et fiabilité

### 12.6.1 Sources primaires (données brutes officielles)

🟢 **Ces sources publient les données originales. Elles ne les interprètent pas.**

| Source | Contenu | URL |
| :---- | :---- | :---- |
| Federal Reserve (Fed) | Taux, discours, minutes FOMC | federalreserve.gov |
| Bureau of Labor Statistics | NFP, CPI, PPI, JOLTS | bls.gov |
| Bureau of Economic Analysis | GDP, PCE, revenus | bea.gov |
| Energy Information Administration | Stocks pétrole, production, demande | eia.gov |
| CME Group | Données futures, positions COT | cmegroup.com |
| CFTC (Commitments of Traders) | Positions des grands acteurs | cftc.gov |
| OPEC | Production, quotas | opec.org |
| FRED (Fed St. Louis) | Base de données macro gratuite | fred.stlouisfed.org |
| World Gold Council | Demande/offre or | gold.org |

### 12.6.2 Sources secondaires (agrégation et calendrier)

🟡 **Ces sources compilent et présentent les données primaires. Utiles pour le calendrier économique.**

| Source | Utilité | Coût |
| :---- | :---- | :---- |
| Forex Factory (forexfactory.com) | Calendrier économique, filtre par impact | Gratuit |
| Econoday (econoday.com) | Calendrier détaillé, consensus | Gratuit (basique) |
| Investing.com | Calendrier, données temps réel | Gratuit (basique) |
| Bloomberg Terminal | Données professionnelles complètes | Payant (\~$24k/an) |
| Reuters Eikon | Alternative Bloomberg | Payant |

🔴 **Investing.com et sources similaires :** données généralement fiables pour le calendrier et les prix, mais les analyses et "signaux" publiés sont de qualité variable. Ne jamais utiliser les recommandations de ces sites comme signal de trading.

### 12.6.3 Le rapport COT (Commitments of Traders)

🟢 **Définition :** rapport hebdomadaire publié par la CFTC (Commodity Futures Trading Commission) chaque vendredi pour les données du mardi précédent. Présente les positions nettes longues/courtes par catégorie de participants.

🟢 **Catégories de participants :**

- **Commercial Hedgers :** producteurs/consommateurs physiques (ex. : compagnies pétrolières). Ils hedgent leur production → positions souvent contra-tendance au mouvement de prix.  
- **Non-Commercial (Large Speculators) :** fonds spéculatifs, CTA. Ils suivent la tendance. Leurs positions nettes sont un indicateur de sentiment.  
- **Non-Reportable (Small Speculators) :** traders retail. Souvent contrariants en excès extrêmes.

🟡 **Utilisation du COT en trading :**

- Positions nettes Large Speculators à un extrême historique → signal contrarian potentiel  
- Divergence entre prix et positions (prix monte, positions nettes baissent) → alerte de retournement  
- 🔴 Le COT est un indicateur **hebdomadaire avec 3 jours de décalage** — pas un outil intraday. Utile pour le biais directionnel macro uniquement.

🟢 **Source :** cftc.gov/MarketReports/CommitmentsofTraders — données gratuites et téléchargeables.

---

## 12.7 Intégration macro dans TRADEX-AI

### 12.7.1 Filtre macro — Architecture

🔵 **Proposition d'architecture (à développer) :**

MODULE MACRO TRADEX-AI

INPUT QUOTIDIEN (automatisable via API) :

  \- Calendrier économique du jour (Forex Factory API ou Econoday)

  \- VIX niveau actuel

  \- DXY niveau et direction H4

  \- COT dernières données (hebdomadaire)

RÈGLES DE FILTRE :

1\. BLOCAGE ANNONCES :

   SI annonce\_impact\_élevé dans les 30 min suivantes :

     → Bloquer toute nouvelle entrée

     → Alerte : "Annonce \[nom\] dans \[X\] minutes"

2\. FILTRE RISK-ON/RISK-OFF :

   SI VIX \> 30 :

     → Mode risk-off actif

     → Pour CL : réduire taille de 50 % (volatilité excessive)

     → Pour GC : signal macro haussier (contexte favorable longs)

     → Pour ES : contexte défavorable tendance haussière

3\. BIAIS DIRECTIONNEL MACRO (hebdomadaire, manuel) :

   Basé sur COT \+ tendance DXY \+ régime taux :

     → Biais\_CL \= \[haussier | baissier | neutre\]

     → Biais\_GC \= \[haussier | baissier | neutre\]

     → Biais\_ES \= \[haussier | baissier | neutre\]

   Ce biais filtre les setups contraires (ex. : pas de short CL si biais macro haussier)

OUTPUT :

  → Statut macro par actif : \[FAVORABLE | NEUTRE | DÉFAVORABLE | BLOQUÉ\]

  → Ces statuts s'ajoutent à la grille de scoring setup (Chap. 8\)

🔵 Ce module est une proposition de design. Les APIs de calendrier économique (Forex Factory, Econoday) ont des conditions d'utilisation à vérifier avant intégration.

### 12.7.2 Pondération macro dans le scoring TRADEX-AI

🔵 **Proposition d'ajustement du score (Chap. 8 grille 0–10) :**

| Condition macro | Ajustement score |
| :---- | :---- |
| Statut macro FAVORABLE (biais aligné \+ pas d'annonce) | \+1 point |
| Statut macro NEUTRE | 0 point |
| Statut macro DÉFAVORABLE (biais contra-tendance) | −1 point |
| Statut macro BLOQUÉ (annonce imminente) | Trade interdit (override) |
| VIX \> 30 (volatilité extrême) | Taille réduite de 50 % |

🔵 Ces ajustements sont des hypothèses à valider en backtest. Un backtest incluant le filtre macro vs. sans filtre macro permettra de quantifier l'apport réel.

---

## 12.8 Erreurs fréquentes dans l'utilisation de la macro

### 12.8.1 Sur-pondérer la macro en intraday

🟢 En intraday scalping, les mouvements de 5–30 minutes sont principalement techniques (order flow, niveaux de prix, patterns). La macro impacte les biais directionnels de fond — pas les micro-mouvements. Utiliser la macro pour justifier chaque trade intraday est une erreur de granularité.

### 12.8.2 Trader les annonces économiques

🔴 **Trader directement sur les annonces économiques (NFP, FOMC) est extrêmement risqué :**

- Le spread s'élargit massivement dans les secondes précédant l'annonce  
- Le slippage peut être de 5–20 ticks sur CL lors d'une annonce EIA  
- La direction initiale peut s'inverser en quelques secondes ("fakeout")  
- Les brokers peuvent rejeter les ordres ou les exécuter avec un slippage excessif

🟡 **Exception possible :** trader le "retour au calme" 5–10 minutes après une annonce, une fois la volatilité initiale absorbée et une direction technique claire établie. Ce n'est pas trader l'annonce — c'est trader la structure post-annonce.

### 12.8.3 Confondre corrélation et causalité

🔴 **Exemple :** "quand le DXY monte, l'or baisse". Cette corrélation est documentée et structurelle. Mais DXY et or sont tous deux influencés par les taux réels US — c'est la variable causale commune. En période de taux stables, la corrélation DXY/or peut s'affaiblir. Ne jamais utiliser une corrélation comme règle absolue.

### 12.8.4 Information overload

🟢 Suivre trop de sources macro crée une paralysie analytique. Pour un trader TRADEX-AI focalisé sur CL, GC et ES, les sources essentielles sont :

- EIA (hebdomadaire) pour CL  
- FOMC et CPI pour GC et ES  
- COT (hebdomadaire) pour le biais des grands spéculateurs  
- VIX en continu pour le régime risk-on/risk-off

Tout le reste est du bruit pour un usage intraday.

---

## 12.9 Synthèse du Chapitre 12

| Driver | Actif principal | Fréquence | Source | Intégration TRADEX-AI |
| :---- | :---- | :---- | :---- | :---- |
| FOMC / taux Fed | ES, GC, CL | 8× /an | federalreserve.gov | Blocage ±2h \+ biais macro |
| EIA Crude Inventories | CL | Hebdo (mer.) | eia.gov | Blocage ±30min |
| NFP | ES, GC, CL | Mensuel | bls.gov | Blocage ±30min |
| CPI / PCE | ES, GC | Mensuel | bls.gov / bea.gov | Blocage ±30min |
| VIX | ES, CL, GC | Continu | cboe.com | Filtre taille si \> 30 |
| COT | CL, GC, ES | Hebdo (vendredi) | cftc.gov | Biais directionnel macro |
| OPEP+ | CL | Irrégulier | opec.org | Alerte manuelle |
| Géopolitique | CL, GC | Événementiel | Monitoring actif | Alerte manuelle |
| Saisonnalité | CL, GC | Annuel | Historique | Contexte secondaire |

🟡 **Règle TRADEX macro :** la macro définit le contexte et filtre les trades contraires au biais fondamental. Elle ne génère pas de signal d'entrée. L'entrée reste toujours technique (setup, niveau COG, price action). La macro est un filtre, jamais un déclencheur.

---

## 12.10 Checklist macro quotidienne

- [ ] Calendrier économique du jour consulté (Forex Factory ou Econoday)  
- [ ] Annonces à impact élevé marquées sur le plan de trading  
- [ ] VIX niveau noté → mode risk-on ou risk-off ?  
- [ ] DXY direction H4 notée → impact sur GC et CL ?  
- [ ] Biais macro hebdomadaire (COT) consulté pour les actifs tradés  
- [ ] Aucune annonce majeure dans la prochaine heure → trading possible  
- [ ] Statut macro par actif défini : FAVORABLE / NEUTRE / DÉFAVORABLE / BLOQUÉ

---

*Chapitre 12 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-18* *Tout le contenu de ce chapitre est éducatif. Les sources citées (eia.gov, bls.gov, federalreserve.gov, cftc.gov, fred.stlouisfed.org) sont des sources gouvernementales américaines en accès public. Rien ici n'est du conseil financier. Les corrélations présentées sont des tendances historiques documentées — non des règles permanentes.*  
