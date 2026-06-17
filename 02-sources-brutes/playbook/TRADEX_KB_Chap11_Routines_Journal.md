# Chapitre 11 — Routines et journal de trading

## TRADEX-AI · Cerveau de connaissances · Cours « Mentor Trader Senior »

**Statut de fiabilité — système de tags :** 🟢 FAIT · 🟡 CONVENTION · 🔵 ÉCOLE · ⏳ VOLATILE · 🔴 NON VÉRIFIÉ / RED FLAG · ⚫ PROPRIÉTAIRE / NON AUDITABLE **Règle d'or : ne jamais transformer un 🔵/🔴/⚫ en 🟢.**

---

## 11.0 Pourquoi les routines sont une infrastructure, pas une option

🟢 Une stratégie sans routine d'exécution produit des résultats variables. Les routines transforment les règles écrites (Chap. 9\) en comportements automatisés reproductibles. Elles réduisent la charge cognitive avant et pendant la session, laissant plus de capacité mentale pour l'exécution de qualité.

🟢 **Analogie documentée :** les pilotes de ligne suivent des checklists obligatoires avant chaque vol — non pas parce qu'ils ont oublié comment piloter, mais parce que les procédures standardisées réduisent les erreurs même chez les experts. La même logique s'applique au trading.

🟡 **Convention de ce chapitre :** les routines sont présentées en trois blocs temporels (pré-session, pendant la session, post-session) et complétées par la structure du journal de trading comme système de mesure.

---

## 11.1 La routine pré-session

### 11.1.1 Objectif et durée

🟢 **Objectif :** arriver à l'ouverture de session avec un plan complet, des niveaux identifiés, un état mental évalué, et aucune décision à prendre "en live" qui aurait pu être prise avant.

🟡 **Durée recommandée :** 20 à 45 minutes avant l'ouverture RTH selon la complexité des actifs suivis. À adapter selon le nombre d'actifs et la richesse du plan.

### 11.1.2 Bloc 1 — Contexte macro (5–10 minutes)

🟢 **Vérification du calendrier économique :** Consulter les annonces prévues pour la session (et la session suivante si positions overnight). Sources fiables :

- **Forex Factory** (forexfactory.com) : gratuit, filtrable par impact  
- **Econoday** (econoday.com) : plus détaillé, orienté institutionnel  
- **CME Group Economic Calendar** (cmegroup.com) : spécifique aux actifs futures

🟢 **Annonces à impact élevé pour les actifs TRADEX-AI :**

| Annonce | Actif impacté | Fréquence | Source officielle |
| :---- | :---- | :---- | :---- |
| EIA Crude Oil Inventories | CL | Hebdomadaire (mercredi \~10h30 ET) | eia.gov |
| Non-Farm Payrolls (NFP) | ES, GC, CL | Mensuel (1er vendredi du mois, 8h30 ET) | bls.gov |
| FOMC Rate Decision | ES, GC, CL | 8× par an | federalreserve.gov |
| CPI (Inflation US) | ES, GC | Mensuel | bls.gov |
| API Crude Inventory | CL | Hebdomadaire (mardi \~16h30 ET) | api.org (payant) |
| GDP US | ES, GC | Trimestriel | bea.gov |

🟢 **Règle opérationnelle :** marquer les annonces impact élevé sur le plan de trading. Pas d'entrée dans les 30 minutes précédant une annonce majeure. Possibilité de réduire la taille ou fermer les positions existantes selon la stratégie.

### 11.1.3 Bloc 2 — Analyse technique de contexte (10–15 minutes)

🟢 **Séquence d'analyse MTF (Multi-Timeframe) :**

**TF Weekly/Daily (contexte macro) :**

- Identifier la structure : HH/HL (haussier), LH/LL (baissier), ou range  
- Situer le prix par rapport au COG Daily : au-dessus/en-dessous de la ligne centrale, proche d'une bande  
- Identifier les niveaux S/R majeurs sur le Daily

**TF H4 (signal) :**

- Affiner la structure à court terme  
- Identifier la phase Wyckoff probable (A, B, C, D, E)  
- Noter les niveaux COG H4 actifs  
- Identifier le régime : ADX(14) \< 25 (range) ou \> 25 (tendance)

**TF H1/M15 (entrée) :**

- Identifier les setups potentiels pour la session  
- Calculer les RR théoriques  
- Scorer chaque setup potentiel (grille 0–10, Chap. 8\)

🟡 **Ordre immuable :** toujours du TF le plus grand vers le plus petit. Commencer par le M15 crée un biais de court terme qui masque le contexte macro.

### 11.1.4 Bloc 3 — Calcul des niveaux clés (5 minutes)

🟢 **Niveaux à calculer et noter avant la session :**

COG Ligne centrale (H4)    : \_\_\_\_\_\_\_

COG Bande haute (H4)       : \_\_\_\_\_\_\_

COG Bande basse (H4)       : \_\_\_\_\_\_\_

POC session précédente     : \_\_\_\_\_\_\_

VAH session précédente     : \_\_\_\_\_\_\_

VAL session précédente     : \_\_\_\_\_\_\_

Plus haut Daily            : \_\_\_\_\_\_\_

Plus bas Daily             : \_\_\_\_\_\_\_

Niveaux S/R structurels    : \_\_\_\_\_\_\_, \_\_\_\_\_\_\_, \_\_\_\_\_\_\_

🟡 Ces niveaux sont fixes pour la session — ils ne se recalculent pas en cours de session sauf si le TF supérieur produit un mouvement exceptionnel.

### 11.1.5 Bloc 4 — État mental et règles du jour (3–5 minutes)

🟢 **Checklist pré-session (issue Chap. 10\) :**

- État émotionnel coté (1–5) : trading interdit si ≥ 4  
- DD de la veille et de la semaine notés  
- Rappel des circuit-breakers actifs  
- Rappel du risque par trade calculé (1 % du capital actuel)  
- Rappel de la limite de trades par session (souvent 3 max)

---

## 11.2 La routine pendant la session

### 11.2.1 Protocole d'exécution d'un trade

🟢 **Séquence obligatoire — dans cet ordre :**

ÉTAPE 1 — Vérification setup (checklist binaire)

  → Les 5 composantes sont-elles présentes ? (Chap. 8 §8.1.1)

  → Score 0–10 calculé → ≥ 7 pour entrer

ÉTAPE 2 — Calcul de la taille de position

  → Capital × 1 % / (stop\_ticks × valeur\_tick)

  → Arrondi à l'inférieur

ÉTAPE 3 — Vérification circuit-breaker

  → DD journalier actuel \< 2R ?

  → Pas d'annonce dans les 30 min ?

ÉTAPE 4 — Saisie des ordres

  → Ordre d'entrée

  → Stop-loss (saisi immédiatement, jamais mental)

  → Cible 1 (50 % de la position)

  → Cible 2 (50 % restant avec trailing)

ÉTAPE 5 — Non-intervention

  → Après saisie des ordres, NE PAS modifier le stop

  → NE PAS fermer manuellement avant la cible sauf invalidation technique

🟢 La séquence est non négociable. Sauter une étape \= trade hors protocole \= journaliser comme violation.

### 11.2.2 Gestion de l'attente inter-trades

🟡 **Le temps entre les trades est une composante de la routine.**

Pendant les périodes sans setup valide :

- Ne pas regarder le P\&L d'une position ouverte en continu  
- Faire autre chose (lecture, analyse macro, revue de trades passés)  
- Ne pas "chercher" un trade qui n'existe pas

🟢 **Règle des 3 trades maximum par session :** convention pratique pour les traders intraday. Au-delà de 3 trades en une session, la fatigue décisionnelle augmente et la qualité des entrées se dégrade. 🔴 Ce seuil est une convention — il n'existe pas d'étude publiée validant exactement "3". L'important est de définir un seuil et de le respecter.

### 11.2.3 Gestion des positions ouvertes

🟢 **Règle du non-suivi :** une position avec un stop et une cible saisis dans la plateforme n'a pas besoin d'être surveillée tick par tick. Le système gère la sortie mécaniquement.

🟡 **Check permis toutes les N minutes :** vérifier si le contexte a changé (annonce non prévue, mouvement exceptionnel sur un autre marché) justifiant une sortie manuelle. Fréquence recommandée : toutes les 30 minutes au minimum — pas en continu.

🟢 **Seule raison valide de modifier un stop manuellement :** déplacement du stop vers le break-even ou en trailing (jamais élargissement du stop pour "sauver" le trade).

---

## 11.3 La routine post-session

### 11.3.1 Clôture de session (15–20 minutes)

🟢 **Séquence de clôture :**

1\. Fermer toutes les positions si règle "pas d'overnight" s'applique

2\. Exporter le relevé de trades de la plateforme (PDF ou CSV)

3\. Remplir le journal de trading pour chaque trade du jour

4\. Calculer les métriques du jour : R total, DD journalier, taux de respect des règles

5\. Si DD journalier \> 0 : identifier la cause (setup hors critères ? exécution ? marché ?)

6\. Préparer les notes pour la session du lendemain (niveaux proches, annonces)

7\. Fermer la plateforme

### 11.3.2 La review hebdomadaire (30–45 minutes)

🟡 **Fréquence :** une fois par semaine, idéalement le week-end quand les marchés sont fermés.

🟢 **Objectifs :**

1. Calculer les métriques de la semaine (espérance, Profit Factor, taux de respect des règles)  
2. Revoir chaque trade perdant : était-ce une perte dans les règles ou une violation ?  
3. Identifier les patterns récurrents : biais actifs, horaires à problème, type de marché défavorable  
4. Comparer les métriques semaine vs. backtest de référence

🟡 **Format recommandé :**

SEMAINE DU \_\_\_ AU \_\_\_

STATISTIQUES :

Nombre de trades    : \_\_\_

Trades dans règles  : \_\_\_ / \_\_\_ (\_\_\_%)

R total             : \_\_\_

Profit Factor       : \_\_\_

DD max semaine      : \_\_\_

OBSERVATIONS :

Trade le moins bien exécuté : \_\_\_

Biais détecté              : \_\_\_

Action corrective          : \_\_\_

DÉCISION POUR LA SEMAINE SUIVANTE :

Changement de comportement (pas de règle) : \_\_\_

🔴 **Ce qui ne doit PAS être dans la review hebdomadaire :** modifier les règles de la stratégie. Les règles se modifient uniquement lors de la review mensuelle, sur base statistique, pas sur 5 trades.

### 11.3.3 La review mensuelle (1–2 heures)

🟢 **Objectifs :**

1. Calculer les métriques du mois (minimum 20–30 trades)  
2. Comparer à la même période du backtest si disponible  
3. Évaluer si les métriques sont dans les limites de la stratégie (Profit Factor, DD max)  
4. Décider si un ajustement de règle est justifié statistiquement

🟢 **Critère de modification des règles :**

- Profit Factor mensuel \< 1,0 sur 2 mois consécutifs → review approfondie de la stratégie  
- Taux de respect des règles \< 80 % → problème de discipline, pas de stratégie → ne pas modifier les règles

🟡 **Distinction importante :** un mois difficile peut être dû à (a) un régime de marché défavorable pour la stratégie, (b) une mauvaise exécution, (c) une stratégie réellement défaillante. Ces trois causes ont des solutions différentes. Modifier les règles pour (a) ou (b) est une erreur.

---

## 11.4 Le journal de trading — Architecture complète

### 11.4.1 Structure du journal

🟢 Un journal de trading complet contient trois couches :

COUCHE 1 — DONNÉES BRUTES (par trade)

  → Informations factuelles : date, actif, direction, prix, stops, cibles, résultat

COUCHE 2 — ANALYSE D'EXÉCUTION (par trade)

  → Score setup, respect des règles, état émotionnel, qualité d'exécution

COUCHE 3 — MÉTRIQUES AGRÉGÉES (hebdomadaire / mensuel)

  → Statistiques de performance : espérance, Profit Factor, DD, taux de respect

### 11.4.2 Template complet — Couche 1 (données brutes)

🟢 **Champs obligatoires par trade :**

| Champ | Type | Exemple |
| :---- | :---- | :---- |
| ID trade | Numérique séquentiel | T-2026-047 |
| Date/heure entrée | DateTime | 2026-06-18 10:23 ET |
| Actif | Texte | CL (Crude Oil Jul 26\) |
| Direction | Long / Short | Long |
| TF d'analyse | Texte | H4/H1 |
| Prix d'entrée | Décimal | 79.42 |
| Stop initial | Décimal | 79.08 |
| Distance stop (ticks) | Entier | 34 |
| Cible 1 | Décimal | 80.10 |
| Cible 2 | Décimal | 80.76 |
| RR théorique | Décimal | 2.0 / 3.9 |
| Taille (contrats) | Entier | 1 |
| Risque $ | Décimal | 340 |
| Prix sortie | Décimal | 80.10 (cible 1\) |
| Résultat $ | Décimal | \+680 |
| Résultat R | Décimal | \+2.0 |
| Heure sortie | DateTime | 2026-06-18 13:47 ET |
| Raison sortie | Texte | Cible 1 atteinte |

### 11.4.3 Template complet — Couche 2 (analyse d'exécution)

🟢 **Champs d'analyse par trade :**

| Champ | Type | Exemple |
| :---- | :---- | :---- |
| Setup utilisé | Texte | COG Bande basse \+ pin bar |
| Score setup (0–10) | Entier | 8 |
| Régime de marché | Range / Tendance / Indéfini | Range |
| Phase Wyckoff identifiée | Texte | Phase C (Spring) |
| Confluence COG | Oui / Non | Oui (bande −2σ) |
| Volume confirmatoire | Oui / Non | Oui (Stopping Volume) |
| Calendrier éco vérifié | Oui / Non | Oui (aucune annonce) |
| État émotionnel pré-trade | 1–5 | 2 |
| Respect des règles d'entrée | Oui / Non | Oui |
| Stop saisi immédiatement | Oui / Non | Oui |
| Modification du stop | Oui / Non \+ raison | Non |
| Respect de la cible | Oui / Non | Oui (cible 1 respectée) |
| RR réalisé | Décimal | 2.0 |
| Écart RR réalisé / théorique | % | 0 % |
| Note qualitative | Texte | "Bonne exécution. Pin bar propre sur bande −2σ, volume stopping. Sorti proprement à cible 1." |

### 11.4.4 Template complet — Couche 3 (métriques agrégées)

🟢 **Métriques calculées automatiquement (hebdomadaire / mensuel) :**

PÉRIODE : du \_\_\_ au \_\_\_

VOLUME :

  Nombre total de trades      : \_\_\_

  Longs                       : \_\_\_  (\_\_\_%)

  Shorts                      : \_\_\_  (\_\_\_%)

  Trades dans les règles      : \_\_\_  (\_\_\_%)

PERFORMANCE :

  R total net                 : \_\_\_

  Taux de gain                : \_\_\_  %

  RR moyen théorique          : \_\_\_

  RR moyen réalisé            : \_\_\_

  Ratio réalisé/théorique     : \_\_\_  (cible : \> 0,85)

  Profit Factor               : \_\_\_  (cible : \> 1,3)

  Espérance (R/trade)         : \_\_\_

RISQUE :

  DD maximum période          : \_\_\_  R  (\_\_\_  %)

  Pire série de pertes        : \_\_\_  consécutives

  Meilleure série de gains    : \_\_\_  consécutifs

DISCIPLINE :

  Score moyen des setups      : \_\_\_  / 10

  Taux de respect des règles  : \_\_\_  %

  Nombre de violations        : \_\_\_

  Types de violations         : \_\_\_

COMPARAISON BACKTEST :

  Profit Factor backtest réf  : \_\_\_

  Écart                       : \_\_\_  % (acceptable si \< 30 %)

  DD max backtest réf         : \_\_\_

  Écart                       : \_\_\_  % (alerte si \> 50 %)

---

## 11.5 Outils pour tenir le journal

### 11.5.1 Options disponibles

🟢 **Tableur (Excel / Google Sheets) :** Avantage : flexible, personnalisable, formules automatiques. Inconvénient : saisie manuelle, risque d'erreur.

🟡 **Logiciels spécialisés :**

- **TraderVue** (tradervue.com) : importation automatique depuis la plupart des brokers NinjaTrader. Calcule automatiquement les métriques. Version gratuite limitée.  
- **Edgewonk** (edgewonk.com) : logiciel payant (\~169 $ one-time). Orienté analyse comportementale \+ performance.  
- **TradesViz** (tradesviz.com) : alternative, interface moderne.

🔴 **Ces prix et disponibilités sont sujets à changement (⏳).** Vérifier les tarifs actuels avant achat.

🟡 **Journal papier :** non recommandé pour les métriques (calculs manuels fastidieux) mais utile pour les notes qualitatives et émotionnelles — le fait d'écrire à la main favorise la réflexion.

### 11.5.2 Intégration avec TRADEX-AI

🔵 **Architecture proposée :**

NinjaTrader 8 (exécution)

    ↓ Export CSV automatique post-session

TRADEX-AI Journal Module

    ↓ Parsing et calcul des métriques

Dashboard de performance (Couche 3\)

    ↓ Alertes si métriques hors seuils

Review hebdo/mensuelle assistée par IA

🔵 Le module journal TRADEX-AI est une composante à développer. L'export CSV depuis NinjaTrader 8 est standard et documenté dans la plateforme.

---

## 11.6 La routine de développement — S'améliorer structurellement

### 11.6.1 La courbe d'apprentissage en trading

🟡 **Modèle en 4 phases (Maslow's Competence Model — adapté au trading) :**

1. **Incompétence inconsciente** : ne sait pas ce qu'il ne sait pas. Phase dangereuse — excès de confiance initial.  
2. **Incompétence consciente** : réalise l'étendue de ce qu'il ne maîtrise pas. Phase de formation intensive.  
3. **Compétence consciente** : applique les règles correctement avec effort et concentration.  
4. **Compétence inconsciente** : les bonnes pratiques deviennent automatiques.

🟡 La transition de la phase 3 à la phase 4 requiert de la répétition délibérée — environ 100–500 trades dans les règles selon les individus. Ces chiffres sont des estimations de praticiens, pas des données empiriques publiées.

### 11.6.2 La pratique délibérée

🟢 **Concept (Anders Ericsson, "Peak", 2016\) :** la compétence se développe par la pratique délibérée — répétition ciblée avec feedback immédiat sur des composantes spécifiques, pas par la simple accumulation d'expérience.

🟢 **Application au trading :**

- Identifier la compétence spécifique à développer (ex. : "ma sortie prématurée des trades")  
- Se concentrer sur cette compétence sur 20–30 trades  
- Mesurer le progrès sur cette composante spécifique  
- Ne passer à la composante suivante qu'une fois la première maîtrisée

🟡 **Séquence recommandée pour TRADEX-AI :**

1. D'abord : maîtriser l'identification du régime de marché (filtre ADX \+ structure)  
2. Ensuite : maîtriser l'identification des niveaux COG actifs  
3. Ensuite : maîtriser l'exécution du setup principal (COG bande externe \+ rejet)  
4. Ensuite : maîtriser la gestion du trade (scale-out, trailing)  
5. Enfin : optimiser l'ensemble du processus

### 11.6.3 Le replay de marché

🟢 **Définition :** utiliser les données historiques pour simuler une session en temps réel, bougie par bougie, sans connaître la suite. Permet de pratiquer l'identification des setups et l'exécution des règles dans des conditions proches du réel, sans risque financier.

🟢 **NinjaTrader 8 Market Replay :** fonctionnalité native de NinjaTrader 8 permettant de rejouer des sessions historiques avec les données tick-by-tick. Compatible avec les données Rithmic / CQG.

🟡 **Utilisation recommandée :** 2–3 sessions de replay par semaine pendant la phase d'apprentissage. Appliquer exactement les mêmes règles qu'en live. Journaliser les trades de replay de la même façon que les trades réels.

---

## 11.7 Synthèse du Chapitre 11

| Composante | Durée | Fréquence | Objectif |
| :---- | :---- | :---- | :---- |
| Routine pré-session | 20–45 min | Quotidienne | Plan complet avant ouverture |
| Analyse MTF | 10–15 min | Dans pré-session | Contexte \+ niveaux |
| Exécution trade | \< 2 min | Par trade | Protocole 5 étapes |
| Journal Couche 1 | 3–5 min | Par trade | Données brutes |
| Journal Couche 2 | 5–10 min | Par trade | Analyse d'exécution |
| Clôture session | 15–20 min | Quotidienne | Bilan \+ prépa lendemain |
| Review hebdomadaire | 30–45 min | Hebdomadaire | Métriques \+ patterns |
| Review mensuelle | 1–2 h | Mensuelle | Décision stratégique |
| Pratique délibérée | Variable | Selon besoin | Composante ciblée |
| Replay marché | 1–2 h | 2–3× semaine | Pratique sans risque |

🟡 **Règle TRADEX des routines :** une routine incomplète est meilleure qu'une absence de routine. Commencer par le minimum viable (plan quotidien \+ journal Couche 1\) et ajouter les couches progressivement.

---

## 11.8 Checklist des routines — Validation hebdomadaire

- [ ] Routine pré-session suivie tous les jours de trading de la semaine  
- [ ] Journal Couche 1 rempli pour chaque trade  
- [ ] Journal Couche 2 rempli pour chaque trade  
- [ ] Circuit-breakers respectés (aucun trade après DD ≥ 2R)  
- [ ] Review hebdomadaire réalisée (métriques calculées)  
- [ ] Violations de règles identifiées et notées  
- [ ] Aucune modification de règle cette semaine (réservé à la review mensuelle)

---

*Chapitre 11 — TRADEX-AI KB · Format : technique enrichi \+ tags anti-hallucination · Version 1.0 · 2026-06-18* *Tout le contenu de ce chapitre est éducatif. Rien ici n'est du conseil financier. Les outils mentionnés (TraderVue, Edgewonk, NinjaTrader) sont cités à titre indicatif — vérifier disponibilité et tarifs actuels avant utilisation.*  
