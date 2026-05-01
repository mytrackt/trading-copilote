---
name: skill-06-gestion-risque-entree
description: Règles de gestion du risque à l'entrée Belkhayate — stop loss, taille de position, confirmation d'entrée, et règles de capital.
trigger: Utiliser avant chaque entrée en position pour valider le niveau de risque, placer le stop loss, et calibrer la taille de la position.
source: KNOWLEDGE_BASE_MASTER.json — 301 règles extraites
---

# SKILL 06 — GESTION DU RISQUE À L'ENTRÉE (Méthode Belkhayate)

## Règles d'entrée fondamentales

- N'entrer que lorsque le marché revient casser à nouveau le niveau, pas sur la première cassure.
- Entrer un tick en dessous du point de cassure confirmé, pas au moment de la cassure initiale.
- La première cassure peut être un faux signal — attendre la re-cassure confirmée.
- Entrer avec une perte de temps et un objectif pour éliminer le stress émotionnel.
- Ne pas acheter les dips impulsifs sans attendre la confirmation du marché.
- Attendre que les gros acteurs entrent sur le marché plutôt que de trader avec les petits joueurs.
- Ne pas entrer immédiatement — attendre le meilleur moment plutôt que de se précipiter.
- Être patient et sélectif : ne pas appuyer sur le bouton juste pour entrer.

---

## Stop loss & Objectifs de profit

- Définir un stop loss de 8 ticks et un objectif de profit de 13 ticks sur les signaux standards.
- Toujours définir le stop loss avant d'entrer en position.
- Placer les ordres de stop en dessous du VWAP ou en dessous des supports clés.
- Utiliser des unités de temps courtes (5 range bars ou 1 minute) pour minimiser le coût du stop loss.
- Plus l'unité de temps est longue, plus le stop loss grandit et coûte cher.
- Ne pas chercher à gagner plus de 7-8 ticks — les algorithmes ne visent généralement que 3-4-5 ticks.
- Entrer et sortir le plus vite possible pour maximiser le ratio risque/récompense.

---

## Confirmation avant entrée

- Attendre la cassure du niveau de résistance avant d'entrer en position.
- Observer l'accélération du marché après une cassure pour confirmer l'entrée.
- Entrer en confiance lorsqu'on voit 1-2 ticks d'attaque suivis d'une multiplication du volume (doublé ou triplé).
- Attendez l'accélération sur le volume avant d'entrer — ne rentrez pas dans les zones d'accalmie.
- Attendre que le marché casse un trading range avec force.
- Attendre que le stock se consolide à un support quotidien clair avec volume au-dessous de la moyenne.
- Un stock doit confirmer au-dessus d'un niveau clé en se consolidant pour que le signal soit valide.
- Si le stock rejette un niveau clé à plusieurs reprises → la thèse n'est plus valide.

---

## Niveaux d'entrée précis

- Acheter uniquement lorsque le Gravity Center devient vert.
- N'entrez jamais entre les niveaux de pivot et les niveaux de GAN.
- Acheter l'Or quand le pivot du Dollar est cassé avec force sur timeframe court (2 minutes).
- Anticiper une position d'achat avant la cassure du pivot si deux marchés corrélés donnent des signaux d'achat confirmés.
- Entrer lorsque le marché ouvre et se dirige vers le point pivot.
- Lorsque le marché ouvre sous le pivot → probabilité supérieure de baisser.
- Lorsque le marché ouvre au-dessus du pivot → probabilité supérieure de monter.
- Ne jamais trader entre les lignes des pivots — attendre que le marché arrive à ces lignes.
- Acheter lorsque le prix est en arrière du Barycenter (zone rouge), vendre quand il est en avant (zone blanche).

---

## Capital et marges

- Un contrat de blé nécessite 1000 dollars de marge.
- Respecter la règle PDT : maximum 3 jours de trading par période de 5 jours avec moins de 25 000$ en compte marge.
- Ne pas trader si on a perdu de l'argent la veille — le jugement est affecté.
- Trader en papier au minimum 2 à 4 semaines avant de trader en live pour pratiquer les stratégies.

---

## Filtres d'entrée par setup

### Swing trading (multi-jours)
- Scanner les gappers en pré-marché avec volume élevé pour identifier les opportunités.
- Attendre que le marché se consolide après un gap important avant d'entrer.
- Entrer lorsque le prix revient tester un niveau technique après un breakout intraday.
- Utiliser la première journée pour prendre un profit intraday, puis garder la position pour plusieurs jours.
- Entrer au-dessus du 200 SMA et de la 8 EMA lorsqu'ils se croisent en synchronisation avec un breakout long terme.
- Attendre que le stock recrute sur le 8 SMA après une vente drastique en dessous du 200 SMA.
- Entrer sur un breakout de wedge lorsque 1-2 chandelles cassent au-dessus du breakout quotidien après retest de plusieurs jours.

### Scalping Gravity Center
- Vendre quand le prix est exactement au Gravity Center avec un signal de faiblesse (weak candles).
- Entrer au marché au hasard initialement pour s'entraîner à gérer les entrées et sorties.
- Décider manuellement de l'entrée en cliquant achat ou vente.
- Ne pas chercher le moment parfait d'entrée : l'important est la gestion de sortie.

### Short selling
- Ne exécuter un short que si le stock casse et détruit le VWAP.
- Sur la carte de 5 minutes : ne short que si le candle ferme sous le VWAP.
- Chercher les hauts de pré-marché comme niveau d'entrée potentiel pour des stratégies courtes.
- Utiliser le prix d'ouverture à 10h comme niveau de stop loss dans une stratégie de short sur hauts pré-marché.

---

## Règles de validation croisée à l'entrée

- Vérifier que l'instrument a assez d'espace à parcourir avant d'entrer (potentiel de mouvement).
- L'instrument doit rester au-dessus des hauts pré-marché après 10h00.
- Confirmer avec le VWAP : l'achat doit se recapturer sur VWAP après avoir touché un support.
- Utiliser le VWAP comme zone d'entrée et comme référence pour le risque.
- Identifier les zones de soutien et résistance quotidiennes avant d'entrer au marché.
- Utiliser les niveaux clés quotidiens comme stop loss et zones de profit.
- Identifiez les résistances sur le volume (POC) et sur le prix pour confirmer les niveaux importants.

---

## Entrées avancées (structure ABCD)

- Ne jamais acheter dans le segment AB d'une impulsion — attendre le segment CD pour les meilleures entrées.
- Tracer les niveaux de retracement à 50% de l'impulsion AB pour identifier les zones de correction.
- Chercher une bougie avec une longue queue (ombre) au retracement de 50% comme signal d'entrée fiable.
- Identifier la structure ABCD et attendre l'étirement vers D pour maximiser les gains.
- Chercher l'appât (faux signal) qui précède l'accélération du marché.
- Tracer une ligne de cassure après identification de l'appât pour déclencher l'entrée.
- La cassure de la ligne d'appât génère une accélération violente du marché.

---

## Règles d'évitement à l'entrée

- Ne pas entrer sur la première cassure par impatience, même si beaucoup de traders le font.
- Éviter d'acheter le Nasdaq ou le Dow à l'ouverture — attendre que le marché montre ses cartes.
- Ne pas entrer si le marché est dans un trading range (75% du temps).
- Éviter de trader contre la tendance ou en phase de consolidation.
- Ne pas acheter les dips impulsifs sans attendre la confirmation du marché.
- Éviter les premiers jours rouges chaotiques : attendre le jour 2 quand le nouveau marché éclipse l'ancien.
- Ne pas entrer en position lors d'un retrait avec mèche lorsque le marché pénètre un espace jamais atteint.
