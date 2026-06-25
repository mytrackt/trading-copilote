# Extraction AdamGrimes — Seasonality: Ask the Right Question
**Source :** `bundles/adamgrimes/seasonality_ask_right_question.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6571 → D6583 · **Page :** https://www.adamhgrimes.com/seasonality-ask-right-question/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : La saisonnalité non testée statistiquement est du bruit — les patterns saisonniers sur GC/CL/ZW doivent être validés vs simulation aléatoire avant intégration dans la KB.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6571 — La question clé pour toute stat de marché : "cette pattern affectera-t-elle le futur ?"
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_ask_right_question.md) : Devant n'importe quelle statistique de marché, la seule question valide est : "quelle est la probabilité que cela affecte le futur ?" Toutes les autres questions (corrélation, fréquence, amplitude) sont des variations de cette question centrale.
**TRADEX-AI C7** : Lors de l'intégration d'une règle saisonnière dans la KB (GC en Q4, CL en été, ZW à la récolte), documenter systématiquement la preuve que le pattern a un pouvoir prédictif réel — pas juste une fréquence historique brute.
*Catégorie : saisonnalite*

### D6572 — Les patterns peuvent exister pour 2 raisons : réalité ou variation aléatoire
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_ask_right_question.md) : Un pattern observé dans les données peut avoir deux origines exclusives : (1) il reflète quelque chose de réel dans les données, ou (2) il est apparu par variation aléatoire. La distinction est impossible sans test statistique.
**TRADEX-AI C7** : Avant d'ajouter une règle saisonnière à la KB KNOWLEDGE_BASE_MASTER.json, valider avec un test de permutation ou simulation Monte Carlo : le pattern observé est-il plus fréquent que dans des données aléatoires de même distribution ?
*Catégorie : saisonnalite*

### D6573 — Méthode de simulation : comparer patterns réels à données aléatoires de même distribution
🔵 **ÉCOLE** (Source : seasonality_ask_right_question.md) : La meilleure façon de valider un pattern saisonnier est de créer des simulations aléatoires avec les mêmes hypothèses de distribution (même rendement moyen, même volatilité) et de comparer. Si les simulations aléatoires produisent régulièrement des patterns aussi "forts" que le réel, le pattern n'est pas informatif.
**TRADEX-AI C7** : Pour GC (Or) et ZW (Blé) qui ont des saisonnalités connues, créer un backtest de validation : les semaines/mois "forts" historiques sont-ils plus forts que les semaines dans 1000 simulations aléatoires ? Intégrer seulement si p < 0.05.
*Catégorie : saisonnalite*

### D6574 — Données aléatoires produisent régulièrement des semaines "up 8-9/10 ans"
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_ask_right_question.md) : Dans les simulations aléatoires de Grimes sur le S&P 500, certaines semaines apparaissent "up 9 fois sur 10 ans" ou "up all 10 years" — purement par hasard. Ces patterns ne prédisent rien sur le futur.
**TRADEX-AI C7** : Avertissement pour les règles saisonnières déjà en KB (GC/ZW) : une fréquence historique de 8/10 ou 9/10 n'est pas statistiquement significative sur 10 ans. Marquer ces règles AMBIGU dans A_VERIFIER_HUMAIN.md si non validées par simulation.
*Catégorie : saisonnalite*

### D6575 — Aucune preuve statistique sérieuse ne supporte des influences saisonnières non-aléatoires
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_ask_right_question.md) : Grimes conclut qu'il n'existe pas de "bon travail statistique qui supporte des influences saisonnières non-aléatoires" dans les marchés. Compter naïvement les semaines positives produit des stats qui semblent fortes mais sont du bruit.
**TRADEX-AI C7** : Décision KB : les règles saisonnières génériques (ex: "Or monte en Q1") doivent être taguées ⏳ VOLATILE dans la KB jusqu'à validation par simulation. Ne pas leur attribuer un poids élevé dans la grille /10.
*Catégorie : saisonnalite*

### D6576 — Incorporer de mauvaise information dans l'analyse est une des pires erreurs
🟢 **FAIT VÉRIFIÉ** (Source : seasonality_ask_right_question.md) : Grimes identifie explicitement l'incorporation de mauvaises informations dans l'analyse comme "une des pires choses que l'on puisse faire". Des stats sans pouvoir prédictif ajoutent du bruit et dégradent la qualité des décisions.
**TRADEX-AI C1** : Règle KB qualité : tout fait ajouté à KNOWLEDGE_BASE_MASTER.json qui ne satisfait pas au moins une validation (source primaire OU backtest OU simulation) doit être tagué 🔴 NON SOURCÉ, jamais utilisé dans un signal Claude API.
*Catégorie : structure_marche*

### D6577 — Test de saisonnalité : méthode binaire (up=1 / down=0) sur N années
🔵 **ÉCOLE** (Source : seasonality_ask_right_question.md) : Protocole de test saisonnier : (1) noter chaque période 1 si positive, 0 si négative, (2) compter le nombre de 1 par période sur N années, (3) comparer la distribution observée à des simulations aléatoires. Simple à implémenter en Python/Excel.
**TRADEX-AI C7** : Ce protocole peut être implémenté en Python sur les données NT8 historiques pour GC, HG, CL, ZW. Résultat : liste des semaines/mois avec edge statistiquement validé (p < 0.05) vs liste des patterns rejetés.
*Catégorie : saisonnalite*

### D6578 — "On ne peut pas argumenter contre les maths" est un argument fallacieux
🟡 **SYNTHÈSE** (Source : seasonality_ask_right_question.md) : L'argument "vous ne pouvez pas argumenter contre les mathématiques" est fallacieux en trading. Le débat n'est pas sur les maths mais sur les conclusions et implications tirées des maths. Les conclusions sont toujours ouvertes à l'interprétation et à la critique.
**TRADEX-AI C1** : Le cerveau Claude API ne doit jamais accepter une règle de trading comme "prouvée" uniquement parce qu'elle est présentée avec des statistiques historiques. Exiger la distinction entre corrélation historique et pouvoir prédictif futur.
*Catégorie : structure_marche*
