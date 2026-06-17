# Chapitre 13 — Pièges et erreurs fréquentes

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 13.0 Pourquoi cataloguer les erreurs

🟢 Les erreurs en trading ont un coût financier direct et immédiat. Contrairement à la plupart des domaines où une erreur coûte du temps ou de la réputation, une erreur de trading coûte du capital — et le capital perdu nécessite un gain proportionnellement plus grand pour être récupéré (asymétrie mathématique, Chap. 7).

🟢 **Principe de ce chapitre :** les erreurs sont classées par catégorie (technique, gestion du risque, psychologique, systémique) avec pour chaque erreur : le mécanisme précis, l'impact quantifiable quand possible, et la contre-mesure mécanique intégrable dans TRADEX-AI.

🟡 Ce chapitre est délibérément redondant avec certains points des chapitres précédents — la répétition structurée est une technique d'apprentissage documentée pour ancrer les comportements à éviter.

---

## 13.1 Erreurs techniques

### 13.1.1 Trader sans niveau clé identifié *a priori*

🟢 **Description :** entrer en position sans avoir identifié un niveau de support/résistance, de COG ou de structure justifiant l'entrée. Le "niveau" est trouvé après coup pour justifier le trade.

🟢 **Mécanisme :** biais de confirmation (Chap. 10). Le cerveau cherche un justificatif après que la décision émotionnelle d'entrer a déjà été prise.

🟢 **Impact :** stop arbitraire → RR incalculable → taille de position incorrecte → espérance inconnue.

🟢 **Contre-mesure TRADEX-AI :** le système ne génère pas de signal sans niveau COG actif identifié. Champ "niveau déclencheur" obligatoire dans le journal avant toute entrée.

### 13.1.2 Utiliser un indicateur sans comprendre son calcul

🟢 **Description :** appliquer un indicateur (RSI, MACD, Stochastique) comme une boîte noire en suivant ses signaux sans comprendre ce qu'il calcule et dans quelles conditions il est pertinent ou non.

🟢 **Exemple concret — RSI :** Le RSI (Relative Strength Index, Wilder 1978\) mesure la vitesse et la magnitude des mouvements de prix récents. Il est calculé sur N périodes (défaut 14\) et oscille entre 0 et 100\. Un RSI \> 70 signifie que les gains récents ont été disproportionnés par rapport aux pertes récentes — pas que le prix va obligatoirement baisser.

🔴 **Erreur fréquente :** "RSI \> 70 \= signal de vente". En tendance haussière forte, le RSI peut rester au-dessus de 70 pendant des dizaines de bougies. Utiliser le RSI comme signal de vente en tendance haussière est statistiquement contre-productif.

🟢 **Règle :** tout indicateur intégré dans TRADEX-AI doit avoir une description de son calcul documentée \+ les conditions de marché dans lesquelles il est pertinent (🟢) ou non pertinent (🔴).

### 13.1.3 Le sur-trading (overtrading)

🟢 **Description :** prendre trop de trades, souvent hors des critères de setup définis, par impatience ou par besoin de "faire quelque chose".

🟢 **Impact quantifiable :** chaque trade hors critères a une espérance nulle ou négative (par définition — s'il avait une espérance positive, il serait dans les critères). Chaque trade génère des frais (commission \+ spread \+ slippage). 10 trades hors critères sur CL \= \~$250–$540 de frais perdus sans edge.

🟢 **Contre-mesure :** limite de 3 trades par session. Journal avec champ "score setup" obligatoire — si score \< 7, trade non autorisé. Le journal rend la violation visible et comptable.

### 13.1.4 Confondre corrélation et signal

🟢 **Description :** observer qu'une configuration s'est produite avant un mouvement favorable par le passé et en faire une règle sans backtest rigoureux.

🟢 **Exemple :** "à chaque fois que le COG croise la bande externe un mardi, le prix revient dans les 24h". Observation rétrospective sur 3 exemples sélectionnés — aucune valeur statistique.

🔴 **Minimum pour valider une observation :** 30 occurrences en out-of-sample avec les mêmes critères de définition. En dessous : hypothèse, pas règle.

### 13.1.5 Ignorer le volume

🟢 **Description :** analyser uniquement le prix (OHLC) sans regarder le volume associé. Le volume est la mesure de la conviction derrière un mouvement de prix.

🟢 **Exemples d'erreurs par omission du volume :**

- Cassure de résistance avec volume faible → fausse cassure probable (manque de conviction)  
- Pin bar de rejet avec volume faible → rejet peut être dû à l'absence d'acheteurs, pas à une vraie résistance  
- Rally avec volume décroissant → tendance qui s'essouffle, pas une tendance saine

🟡 **Règle TRADEX-AI :** tout signal de bougie est confirmé par le volume (critère binaire dans la grille de scoring Chap. 8). Un signal sans confirmation volume vaut 0 sur ce critère.

---

## 13.2 Erreurs de gestion du risque

### 13.2.1 Le stop mental

🟢 **Description :** décider mentalement d'un niveau de stop sans le saisir dans la plateforme, avec l'intention de sortir manuellement si le niveau est atteint.

🟢 **Pourquoi ça échoue systématiquement :** quand le prix approche du niveau mental, le biais d'aversion à la perte s'active. Le trader déplace mentalement le stop ("juste un peu plus loin") ou ne sort pas. Résultat : pertes systématiquement plus grandes que prévu.

🟢 **Impact quantifiable :** une perte de 1R acceptée mentalement qui devient 2R ou 3R en réalité multiplie le DD par 2–3. Sur une série de 10 trades perdants, la différence entre stops respectés et stops non respectés peut représenter 10–20R de DD supplémentaire.

🟢 **Contre-mesure absolue :** stop saisi dans la plateforme immédiatement après l'entrée. Champ "stop saisi immédiatement (oui/non)" dans le journal — toute réponse "non" est une violation critique.

### 13.2.2 Déplacer le stop dans la mauvaise direction

🟢 **Description :** élargir le stop (le déplacer plus loin de l'entrée) parce que le prix s'approche du niveau de stop et que le trader ne veut pas être stoppé.

🟢 **Mécanisme :** aversion à la perte \+ espoir que le marché va "revenir". En réalité, si le stop initial était correctement placé sur un niveau structural valide, son dépassement par le prix signifie que la thèse du trade est invalidée.

🔴 **Il n'existe aucune justification valide pour élargir un stop** après l'entrée en position (sauf correction d'une erreur de saisie initiale documentée).

🟢 **Seul mouvement de stop autorisé :** déplacer le stop vers le break-even ou en trailing (vers le trade) — jamais en s'éloignant.

### 13.2.3 Taille de position non calculée

🟢 **Description :** décider de la taille de position "au feeling" ou en fonction du montant que l'on "a envie de gagner" plutôt qu'en fonction du risque acceptable.

🟢 **Impact :** incohérence complète du risque entre les trades. Un trade "conviction forte" à 3 contrats \+ un trade "conviction faible" à 1 contrat crée une variance de résultats indépendante de l'edge.

🟢 **Contre-mesure :** formule de position sizing obligatoire avant chaque trade (Chap. 7\) :

Contrats \= floor( (Capital × 1%) / (stop\_ticks × valeur\_tick) )

Ce calcul doit être fait avant d'analyser le setup — pas après.

### 13.2.4 Moyenner à la baisse (averaging down)

🟢 **Description :** ajouter des contrats à une position perdante pour "réduire le prix de revient moyen". Chaque ajout augmente l'exposition sur un trade qui se comporte contre la thèse initiale.

🟢 **Mécanisme :** le trader croit que le prix "doit" revenir. Il augmente la mise. Si la tendance continue, les pertes s'accumulent exponentiellement.

🟢 **Impact mathématique :**

- Position initiale : 1 contrat CL, stop à −30 ticks → −300 $  
- Ajout à −40 ticks : 2 contrats, stop à −60 ticks → −(2×200$) \= −400 $  
- Ajout à −60 ticks : 3 contrats → exposition totale 6 contrats si continue de baisser

🔴 **Distinction critique :** moyenner à la baisse ≠ pyramidage sain (Chap. 7). Le pyramidage sain ajoute des contrats à une position **gagnante** selon des règles préétablies. Moyenner à la baisse ajoute des contrats à une position **perdante** de façon émotionnelle.

🟢 **Règle absolue :** aucun ajout de contrats à une position perdante. Si le stop est atteint, sortir. Reconstruire une nouvelle position si le setup se présente à nouveau.

### 13.2.5 Ignorer les frais de transaction

🟢 **Description :** calculer l'edge et les RR sans intégrer les frais réels (commission \+ spread \+ slippage).

🟢 **Impact quantifié sur CL avec frais moyens \~$40 round-turn :**

| RR théorique | R \= 200$ | Gain brut | Gain net | RR réalisé net |
| :---- | :---- | :---- | :---- | :---- |
| 2:1 | Stop \= 200$ | \+400$ | \+360$ | 1,80:1 |
| 1,5:1 | Stop \= 200$ | \+300$ | \+260$ | 1,30:1 |
| 1:1 | Stop \= 200$ | \+200$ | \+160$ | 0,80:1 |

🟢 Un RR théorique de 1:1 devient négatif après frais. **Minimum absolu avec ces frais : RR théorique ≥ 1,5:1 pour être rentable après frais.** Recommandation TRADEX-AI : RR ≥ 2:1 comme plancher.

---

## 13.3 Erreurs psychologiques (synthèse opérationnelle)

### 13.3.1 Augmenter la taille après une série de gains

🟢 **Description :** après 3–5 trades gagnants consécutifs, augmenter spontanément la taille de position au-delà des règles définies.

🟢 **Mécanisme :** excès de confiance \+ biais de récence (Chap. 10).

🟢 **Impact :** le trade suivant (qui peut être une perte normale dans la distribution) frappe avec une taille démesurée, effaçant une partie significative des gains récents.

🟢 **Règle :** la taille de position se calcule mécaniquement. Elle ne varie qu'avec le capital réel (via la formule). Toute variation "manuelle" au-delà de la formule est une violation.

### 13.3.2 Modifier les règles après une perte individuelle

🟢 **Description :** après un trade perdant (même dans les règles), modifier le setup ou les critères d'entrée pour que "ce trade n'aurait pas été pris".

🟢 **Pourquoi c'est destructeur :** les pertes dans les règles sont une composante normale de toute stratégie avec edge. Les modifier pour éviter les pertes individuelles détruit l'edge sur l'ensemble de la distribution. C'est de l'over-fitting en temps réel.

🟢 **Règle :** les règles ne se modifient que lors de la review mensuelle, sur la base d'au moins 30 trades, et uniquement si les métriques sortent des limites définies en backtest.

### 13.3.3 Ne pas journaliser les trades gagnants

🟡 **Description :** journaliser uniquement les trades perdants (pour comprendre ce qui s'est mal passé) et ignorer les trades gagnants.

🟡 **Conséquence :** perte de données sur les trades gagnants — impossible de savoir si les gains proviennent de l'edge ou de la chance, si les cibles sont bien calibrées, si le RR réalisé correspond au théorique.

🟢 **Règle :** journaliser 100 % des trades, gains et pertes, avec le même niveau de détail.

### 13.3.4 Comparer son P\&L journalier aux autres traders

🔴 **Description :** utiliser les résultats affichés d'autres traders (réseaux sociaux, forums) comme référence de performance.

🔴 **Biais de publication :** les traders publient massivement leurs gains et rarement leurs pertes. Les comptes montrés sont sélectionnés pour leur performance exceptionnelle. Ce n'est pas un échantillon représentatif.

🟢 **Seule comparaison valide :** ses propres métriques réelles vs. ses métriques de backtest. Tout le reste est du bruit.

---

## 13.4 Erreurs systémiques (liées au système et à l'environnement)

### 13.4.1 Choisir un broker inadapté

🟢 **Description :** trader des futures avec un broker dont les spreads, les conditions de marge ou la technologie d'exécution sont inadaptés à la stratégie.

🟢 **Points à vérifier avant de choisir un broker futures :**

| Critère | Importance | Ce qu'il faut vérifier |
| :---- | :---- | :---- |
| Réglementation | Critique | NFA (USA), FCA (UK), ASIC (AUS) — vérifier le numéro d'enregistrement |
| Commission round-turn | Élevée | \< $5 pour CL, \< $4 pour ES (⏳ vérifier tarifs actuels) |
| Plateforme supportée | Élevée | Compatibilité NinjaTrader 8 (Rithmic, CQG, Continuum) |
| Marge intraday | Élevée | Marge intraday réduite disponible pour scalping (souvent 25–50% de la marge initiale) |
| Slippage moyen | Élevée | Tester sur compte simulation avant live |
| Ségrégation des fonds | Critique | Fonds clients séparés des fonds propres du broker |
| Service client | Moyenne | Disponible pendant les heures de trading |

🔴 **Brokers non régulés :** aucun recours en cas de faillite ou de fraude. Ne jamais déposer de fonds chez un broker non enregistré auprès d'un régulateur reconnu.

### 13.4.2 Utiliser des données de marché de mauvaise qualité

🟢 **Description :** backtester ou trader avec des données historiques incomplètes, incorrectes ou sans ajustement pour les rollovers.

🟢 **Problèmes courants avec les données futures :**

- **Gaps de rollover non ajustés :** à chaque expiration, le prix "saute" d'un contrat à l'autre. Sans ajustement, les indicateurs calculés sur les données brutes sont incorrects au niveau des rollovers.  
- **Données continues ajustées (back-adjusted) :** méthode standard pour les backtests — les prix passés sont ajustés rétroactivement pour éliminer les sauts de rollover. Attention : les niveaux de prix absolus passés ne correspondent plus aux prix réels historiques — uniquement les mouvements relatifs sont fiables.  
- **Données tick vs. données OHLC :** pour backtester un stop intrabar (stop déclenché pendant une bougie, pas à la clôture), des données tick ou 1 minute sont nécessaires. Les données OHLC journalières ne permettent pas de simuler les stops intraday.

🟢 **Sources de données pour backtests NinjaTrader 8 :**

- **Kinetick** (kinetick.com) : service de données NinjaTrader, gratuit EOD, payant temps réel  
- **CQG** : données professionnelles, compatible NinjaTrader  
- **Rithmic** : données tick-by-tick, compatible NinjaTrader

### 13.4.3 Internet et infrastructure technique défaillants

🟢 **Description :** les problèmes de connexion internet pendant une session de trading peuvent empêcher l'exécution des ordres de sortie — notamment les stops.

🟢 **Risque concret :** une position ouverte sans connexion \= stop non géré \= perte potentiellement illimitée si le marché bouge fortement.

🟡 **Mesures préventives :**

- Connexion filaire (ethernet) plutôt que WiFi pour le trading  
- Connexion de secours (partage de connexion mobile) configurée à l'avance  
- Ordres stop saisis dans la plateforme dès l'entrée (ils s'exécutent côté broker même si la connexion est perdue)  
- Connaître le numéro de téléphone du broker pour clôturer manuellement en urgence

### 13.4.4 Trader sans plan de contingence

🟢 **Description :** ne pas avoir prévu les scénarios exceptionnels : panne plateforme, coupure internet, événement de marché extrême (flash crash, annonce surprise).

🟡 **Plan de contingence minimum :**

| Scénario | Action préventive | Action d'urgence |
| :---- | :---- | :---- |
| Panne plateforme | Stops saisis dans la plateforme | Appel broker pour clôture manuelle |
| Coupure internet | Connexion de secours configurée | Appel broker |
| Flash crash | Stop saisi (protection partielle) | Pas d'action pendant le flash — attendre stabilisation |
| Annonce surprise OPEP/Fed | Positions réduites avant annonces majeures | Clôture manuelle si exposition excessive |
| Appel de marge | Monitoring capital en continu | Clôture partielle avant d'atteindre la marge maintenance |

---

## 13.5 Erreurs spécifiques aux débutants sur futures

### 13.5.1 Sous-capitalisation

🟢 **Description :** commencer à trader des futures avec un capital insuffisant par rapport à la marge requise et au risque par trade.

🟢 **Capital minimum pratique pour CL avec règles TRADEX-AI (1 % risque, stop 30 ticks) :**

R \= Capital × 1%

Stop CL \= 30 ticks × $10 \= $300

→ Capital minimum \= $300 / 1% \= $30,000

🟢 **Capital minimum pratique pour ES (E-mini S\&P, 1 tick \= $12,50) :**

Stop ES typique \= 8 ticks × $12,50 \= $100

→ Capital minimum \= $100 / 1% \= $10,000

🔴 Ces calculs sont des minimums — pas des recommandations de démarrage. Un capital sous-dimensionné ne laisse aucune marge pour les séries de pertes normales.

🟡 **Recommandation pratique :** démarrer avec un capital permettant de supporter 20 pertes consécutives à 1 % sans atteindre la marge de maintenance. Soit \~$30,000–$50,000 pour CL.

### 13.5.2 Ne pas distinguer simulation et live

🟢 **Description :** penser que les résultats en simulation (paper trading) seront identiques en live.

🟢 **Différences réelles entre simulation et live :**

- **Slippage :** en simulation, les ordres sont exécutés au prix théorique. En live, l'exécution dépend de la liquidité disponible à ce moment.  
- **Psychologie :** en simulation, l'absence de conséquence financière réelle élimine le stress et le biais émotionnel — ce qui fausse les résultats dans les deux sens (trop calme ou trop laxiste).  
- **Données :** certaines plateformes utilisent des données légèrement décalées en simulation.

🟡 **Transition recommandée :** paper trading 30+ trades → micro-trading (taille minimale \= 1 contrat) avec capital réel réduit → taille normale progressive.

### 13.5.3 Ignorer le rollover des contrats

🟢 **Description :** continuer à trader le contrat expirant après la date de rollover, alors que la liquidité s'est reportée sur le contrat suivant.

🟢 **Impact concret :** spread plus large, moins de liquidité, risque de livraison physique pour les contrats non-cash settled (CL est physiquement livrable — ne pas détenir un contrat CL jusqu'à expiration).

🟢 **Règle :** surveiller le volume relatif entre le contrat actif et le contrat suivant. Rouler quand le volume du contrat suivant dépasse celui du contrat actif (généralement J−4 avant expiration pour CL).

### 13.5.4 Croire qu'un système rentable en backtest sera rentable en live

🔴 **Description :** penser qu'un backtest avec Profit Factor 2,5 garantit une performance live équivalente.

🟢 **Raisons documentées de la dégradation backtest → live :**

1. **Over-fitting :** les paramètres optimaux du passé ne sont pas ceux du futur  
2. **Market impact :** en live, vos ordres déplacent le marché (minimal sur les futures liquides, mais réel)  
3. **Slippage :** non modélisé correctement dans la plupart des backtests  
4. **Changements de régime :** les marchés évoluent — un edge valable en 2020–2022 peut être diminué en 2024–2026  
5. **Facteur psychologique :** l'exécution en live est moins rigoureuse qu'en backtest

🟢 **Règle TRADEX-AI :** un Profit Factor backtest de 2,0 doit être anticipé à \~1,3–1,5 en live (dégradation de 25–35 % comme hypothèse conservatrice). Si le Profit Factor live tombe en dessous de 1,0 sur 50+ trades : review complète de la stratégie.

---

## 13.6 Erreurs liées à l'information et aux formations

### 13.6.1 Les "taux de réussite" annoncés dans les formations

🔴 **Description :** formations trading qui annoncent des taux de réussite précis ("cette stratégie a 73 % de taux de gain") sans fournir la méthodologie de calcul, la période testée, l'actif et le TF.

🔴 **Pourquoi ces chiffres sont non vérifiables :**

- Pas de définition précise des critères d'entrée/sortie  
- Pas d'indication sur la période de backtest  
- Pas de séparation in-sample / out-of-sample  
- Sélection possible des exemples favorables (biais de confirmation)

🟢 **Règle TRADEX-AI :** tout chiffre de performance cité dans le cerveau de connaissances doit être accompagné de sa source, sa méthodologie et son tag de fiabilité. Aucun taux de réussite sans méthodologie vérifiable n'est intégré.

### 13.6.2 Les signaux payants et les "calls" de trading

🔴 **Description :** suivre des signaux de trading payants (alertes d'entrée/sortie vendues par abonnement) sans comprendre la stratégie sous-jacente.

🔴 **Problèmes structurels :**

- Pas de transparence sur l'historique complet des signaux (gains ET pertes)  
- Slippage différent selon le moment où chaque abonné exécute  
- Aucun apprentissage : suivre des signaux ne développe pas la compétence  
- Réglementation : en France, les signaux de trading nécessitent une autorisation AMF. Au Maroc, la réglementation est à vérifier auprès de l'AMMC (Autorité Marocaine du Marché des Capitaux).

🟢 **Position TRADEX-AI :** TRADEX-AI produit des scores et des alertes de contexte — pas des signaux exécutables "blindly". La décision finale appartient toujours au trader.

### 13.6.3 L'accumulation de formations sans exécution

🟡 **Description :** Chapitre 10 §10.6.1. La répétition ici est intentionnelle — c'est une des erreurs les plus coûteuses en temps.

🟢 **Critère de suffisance :** les chapitres 1 à 12 de ce cours constituent une base théorique complète pour commencer le paper trading. L'apprentissage supplémentaire a un rendement décroissant au-delà de ce seuil. La compétence se développe par l'exécution.

---

## 13.7 Catalogue des erreurs — Référence rapide TRADEX-AI

🟢 **Tableau de référence pour intégration dans le système de scoring :**

| Catégorie | Erreur | Impact | Contre-mesure TRADEX-AI |
| :---- | :---- | :---- | :---- |
| Technique | Trade sans niveau clé | RR incalculable | Champ "niveau" obligatoire |
| Technique | Indicateur sans contexte | Faux signaux | Tag de condition d'usage |
| Technique | Sur-trading | Frais \+ edge dilué | Max 3 trades/session |
| Technique | Ignorer le volume | Faux signaux | Critère volume dans scoring |
| Risque | Stop mental | Pertes \> R prévu | Stop saisi obligatoire |
| Risque | Élargir le stop | Perte \> 1R | Mouvement stop interdit (hors trailing) |
| Risque | Taille non calculée | Variance excessive | Formule obligatoire avant trade |
| Risque | Averaging down | Pertes exponentielles | Aucun ajout sur position perdante |
| Risque | Frais ignorés | RR réel \< RR théorique | RR minimum 2:1 après frais |
| Psychologie | Taille augmentée post-gain | Perte amplifiée | Taille calculée \= taille fixe |
| Psychologie | Règles modifiées post-perte | Over-fitting | Review mensuelle uniquement |
| Systémique | Broker non régulé | Risque de perte totale | Vérifier régulation avant dépôt |
| Systémique | Données sans rollover ajusté | Backtest incorrect | Données continue back-adjusted |
| Systémique | Pas de plan contingence | Perte incontrôlée | Protocole urgence documenté |
| Débutant | Sous-capitalisation | DD fatal sur série normale | Capital min calculé avant start |
| Débutant | Ignorer rollover | Livraison physique | Alerte rollover J−4 |
| Information | Taux de réussite non vérifiés | Fausse confiance | Tag 🔴 systématique |

---

## 13.8 Auto-diagnostic — Identifier ses erreurs récurrentes

### 13.8.1 Processus d'identification

🟢 **Méthode :**

1. Sur les 30 derniers trades journalisés, identifier les trades hors règles  
2. Classer ces trades hors règles par catégorie (technique / risque / psychologie / systémique)  
3. Identifier la catégorie dominante → c'est là que l'effort de correction doit porter  
4. Définir une règle mécanique unique pour réduire cette erreur  
5. Mesurer l'évolution sur les 30 trades suivants

🟢 **Principe de correction séquentielle :** corriger une seule erreur à la fois. Tenter de corriger toutes les erreurs simultanément disperse l'attention et produit des résultats médiocres sur tous les fronts.

### 13.8.2 Métriques de diagnostic dans le journal TRADEX-AI

🔵 **Requêtes à implémenter dans le module journal :**

Taux de violation par catégorie :

  violations\_technique / total\_trades × 100

  violations\_risque / total\_trades × 100

  violations\_psychologie / total\_trades × 100

Performance des trades hors règles vs. dans les règles :

  RR\_moyen\_hors\_règles vs. RR\_moyen\_dans\_règles

  (attendu : RR hors règles \< RR dans règles)

Évolution du taux de violation sur 10 semaines :

  Courbe de progression de la discipline d'exécution

---

## 13.9 Synthèse du Chapitre 13

🟢 Les erreurs en trading ne sont pas aléatoires — elles suivent des patterns prévisibles et documentés. Les cataloguer, les mesurer et les réduire méthodiquement est en soi une source d'amélioration de la performance, indépendamment de l'affinement de la stratégie.

🟢 **Hiérarchie de correction recommandée pour TRADEX-AI :**

1. **Priorité 1 — Erreurs fatales** (une seule peut ruiner un compte) :  
     
   - Stop mental  
   - Averaging down  
   - Broker non régulé  
   - Sous-capitalisation

   

2. **Priorité 2 — Erreurs à fort impact** (dégradent significativement l'edge) :  
     
   - Taille non calculée  
   - Élargissement du stop  
   - Trade sans niveau clé  
   - Modification des règles post-perte

   

3. **Priorité 3 — Erreurs à impact modéré** (réduisent la performance sur le long terme) :  
     
   - Sur-trading  
   - Volume ignoré  
   - Frais non intégrés  
   - Rollover ignoré

🟡 **Règle TRADEX des erreurs :** une erreur identifiée et mesurée est déjà à moitié corrigée. Une erreur non journalisée se répète indéfiniment.

---

## 13.10 Checklist anti-erreurs — Avant chaque session

- [ ] Niveau déclencheur identifié *a priori* pour chaque setup potentiel  
- [ ] Taille de position calculée mécaniquement (formule, pas feeling)  
- [ ] Stop saisi dans la plateforme dès l'entrée — protocole non négociable  
- [ ] RR théorique ≥ 2:1 calculé après frais estimés  
- [ ] Volume : critère confirmateur vérifié dans la grille de scoring  
- [ ] Calendrier économique consulté (aucune annonce dans les 30 min)  
- [ ] Capital et marge vérifiés (pas de risque d'appel de marge)  
- [ ] Connexion internet stable \+ backup configuré  
- [ ] Limite de 3 trades/session active

---

*Chapitre 13 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-18* *Tout le contenu de ce chapitre est éducatif. Rien ici n'est du conseil financier. Les seuils quantitatifs présentés (capital minimum, frais, RR) sont des estimations illustratives — vérifier les conditions réelles auprès de votre broker avant tout engagement de capital.*  
