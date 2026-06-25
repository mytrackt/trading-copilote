# Extraction AdamGrimes — Market Stats
**Source :** `bundles/adamgrimes/market_stats.md` (HTTP 200) + 0 images certifiées
**Méthode images :** sans image · 0/0 certifiées · 0 à vérifier
**Décisions :** D6271 → D6290 · **Page :** https://www.adamhgrimes.com/market-stats/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Principes de lecture quotidienne des statistiques de marché — breadth, secteurs actifs, identification du régime intraday pour calibrer la session de trading.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6271 — Le day trader doit savoir "ce qui bouge, où, et comment" chaque session
🔵 **ÉCOLE** (Source : market_stats.md) : Pour un day trader, connaître en temps réel les secteurs actifs, les instruments en mouvement, et la nature du mouvement (breadth large vs concentration sur quelques titres) est une information de premier ordre. Ce n'est pas pour "courir après ce qui est chaud" mais pour comprendre le régime de marché du jour.
**TRADEX-AI C1** : TRADEX doit intégrer une lecture de "régime intraday" avant chaque session : quels actifs GC/HG/CL/ZW bougent davantage que la normale ? Quel est le niveau de corrélation entre eux ce jour ? Ces informations alimentent le Cercle C7 (corrélations) et C1 (prix).
*Catégorie : structure_marche*

### D6272 — Le swing trader intermédiaire bénéficie d'une vue "microscopique" de la journée
🔵 **ÉCOLE** (Source : market_stats.md) : Même pour un trader de positionnement intermédiaire (pas un scalper), observer les statistiques quotidiennes détaillées donne une vue précieuse sur ce qui anime le marché. L'objectif n'est pas la réactivité mais la compréhension du contexte dans lequel les setups se forment.
**TRADEX-AI C1** : Le dashboard TRADEX doit afficher les statistiques clés de la session courante (range GC vs ATR habituel, volume relatif, position dans le range Belkhayate) pour que le signal soit interprété dans son contexte intraday, pas en isolation.
*Catégorie : structure_marche*

### D6273 — L'investisseur long terme ne doit PAS surveiller les mouvements court terme
🔵 **ÉCOLE** (Source : market_stats.md) : Adam Grimes précise explicitement que les investisseurs "buy and hold" authentiques feraient mieux de ne rien faire sur une base quotidienne. Surveiller les mouvements court terme peut "faire plus de mal que de bien" pour ce profil. La discipline de l'horizon temporel est une compétence en soi.
**TRADEX-AI C1** : TRADEX est un système de trading actif, pas d'investissement long terme. Toute analogie avec le "buy and hold" est hors périmètre. Le système opère sur des horizons intraday à quelques jours (swing) sur des futures actifs — pas de position détenue plus de X jours sans révision.
*Catégorie : psychologie*

### D6274 — Les scans de marché doivent être construits autour d'éléments critiques ciblés
🟡 **SYNTHÈSE** (Source : market_stats.md) : Adam Grimes décrit avoir construit des scans "bouillis jusqu'à leur essence critique" — pas un tableau de bord de 200 indicateurs mais une sélection distillée des éléments vraiment déterminants. La valeur d'un scan est inversement proportionnelle à sa complexité si les éléments non pertinents sont éliminés.
**TRADEX-AI C1** : Le dashboard TRADEX doit afficher uniquement les 7 cercles d'intelligence dans un format lisible en 30 secondes. Tout indicateur supplémentaire non directement lié aux cercles C1-C7 est banni de l'interface principale. La densité d'information nuit à la décision rapide.
*Catégorie : psychologie*

### D6275 — Deux types de traders, deux besoins informationnels distincts
🔵 **ÉCOLE** (Source : market_stats.md) : Les besoins d'un day trader (mouvements en temps réel, secteurs actifs, breadth intraday) sont fondamentalement différents de ceux d'un swing trader intermédiaire (contexte, régime, positionnement relatif). Un même outil ne sert pas les deux de la même façon.
**TRADEX-AI C1** : Le mode Manuel de TRADEX (Abdelkrim décide) doit permettre de choisir l'horizon de décision (intraday vs swing multi-jours). Le signal Belkhayate doit préciser l'horizon pour lequel il est valide. Un signal valide pour un swing de 3 jours n'est pas automatiquement valide pour une entrée intraday.
*Catégorie : configuration*
