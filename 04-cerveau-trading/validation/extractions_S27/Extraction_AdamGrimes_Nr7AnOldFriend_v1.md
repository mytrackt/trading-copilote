# Extraction AdamGrimes — NR7: An Old Friend
**Source :** `bundles/adamgrimes/nr7_an_old_friend.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6351 → D6365 · **Page :** https://www.adamhgrimes.com/nr7-an-old-friend/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : NR7 est un filtre de timing puissant pour anticiper les journées de tendance — applicable à GC, HG, CL, ZW comme condition de probabilité renforcée avant signal.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D6351 — Définition NR7 : session au range le plus étroit des 7 dernières sessions
🟢 **FAIT VÉRIFIÉ** (Source : nr7_an_old_friend.md) : NR7 (Narrow Range 7) signifie que la session courante a le range le plus étroit (high - low) des 7 dernières sessions. Concept documenté par Toby Crabel dans "Day Trading with Short Term Price Patterns and Opening Range Breakout".
**TRADEX-AI C1** : Implémenter le calcul NR7 dans le moteur Python de TRADEX-AI pour GC, HG, CL, ZW. Calcul simple : (high_today - low_today) < min(high-low for past 6 sessions). Flag NR7 = True/False par actif.
*Catégorie : configuration*

### D6352 — NR7 prédit une journée de tendance le lendemain avec probabilité élevée
🟢 **FAIT VÉRIFIÉ** (Source : nr7_an_old_friend.md) : "This condition sets the market up for a trend day; there is a higher probability of the following day 1) having a larger than normal range and 2) having more directional intraday action." NR7 est un signal de setup pour un trend day — pas pour un range day.
**TRADEX-AI C1** : Le jour suivant un NR7 sur GC, HG, CL ou ZW, augmenter le score de probabilité directionnelle dans la grille /10. La compression de range est un accumulateur d'énergie directionnelle — corrèle avec la philosophie Belkhayate sur l'Énergie.
*Catégorie : timing*

### D6353 — NR7 seul : indicateur pour les intraday traders de se préparer à un trend day
🟢 **FAIT VÉRIFIÉ** (Source : nr7_an_old_friend.md) : "Used alone, this pattern can tell intraday traders when they should be focusing on potential trend days the following day." NR7 utilisé seul est suffisant pour orienter la stratégie du lendemain (mode trend day plutôt que scalp/range).
**TRADEX-AI C1** : Dans les alertes mode Manuel de TRADEX-AI, inclure un flag "NR7 détecté hier sur [actif] — probabilité accrue de trend day aujourd'hui". Abdelkrim peut ainsi préparer sa journée de trading différemment. Information contextuelle à afficher dans le dashboard.
*Catégorie : timing*

### D6354 — NR7 en combinaison avec d'autres conditions : signal encore plus puissant
🟢 **FAIT VÉRIFIÉ** (Source : nr7_an_old_friend.md) : "Used in conjunction with other conditions and patterns, it becomes even more powerful." Grimes affirme explicitement que NR7 combiné avec d'autres éléments dépasse sa valeur standalone.
**TRADEX-AI C1** : Dans la grille de scoring /10, NR7 doit être un facteur booléen de renforcement — s'il est présent ET que d'autres cercles (C2 Order Flow, C3 COT, C5 Sentiment) sont alignés, le score global doit être amplifié. NR7 alone ne déclenche pas de signal.
*Catégorie : gestion_risque_entree*

### D6355 — NR7 applicable à l'entrée, la gestion du risque ET autres aspects du trading
🔵 **ÉCOLE** (Source : nr7_an_old_friend.md) : Grimes précise que NR7 a de la valeur "for trade entry, risk management, and for many other aspects of the trading process." Ce n'est pas uniquement un signal d'entrée — c'est aussi un outil de gestion.
**TRADEX-AI C1** : Usage dual de NR7 dans TRADEX-AI : (1) Entrée : probabilité accrue de trend day → favoriser les signaux directionnels. (2) Gestion du risque : le jour après NR7, s'attendre à des ranges plus larges → ajuster les stops en conséquence (stops plus larges que la normale car ATR sera plus grand).
*Catégorie : gestion_position_active*

### D6356 — NR7 : outil pour "technical or tactical traders"
🔵 **ÉCOLE** (Source : nr7_an_old_friend.md) : Grimes qualifie NR7 de "powerful tool that probably should be in your toolkit as a technical or tactical trader." Il souligne que malgré son apparence simpliste ("not exciting or sexy"), c'est un outil qui "demands attention."
**TRADEX-AI C1** : Valider empiriquement NR7 sur les données historiques NT8 pour GC et CL (les 2 actifs les plus liquides du portefeuille TRADEX). Si la distribution post-NR7 confirme un range plus large et une directionnalité plus forte sur ces futures, intégrer NR7 comme feature dans le scoring.
*Catégorie : indicateurs_momentum*

### D6357 — NR7 origine : Toby Crabel, méthode statistique sur données réelles
🟢 **FAIT VÉRIFIÉ** (Source : nr7_an_old_friend.md) : Le pattern NR7 a été documenté par Toby Crabel dans "Day Trading with Short Term Price Patterns and Opening Range Breakout" — un livre devenu rarissime (copies à plus de 1000$ avant impression). La réputation du livre repose sur le fait qu'il se base sur "real stats and what actually works in the market."
**TRADEX-AI C1** : NR7 est une règle testée statistiquement sur données réelles, pas une théorie. Sa présence dans la KB de TRADEX-AI est justifiée (🟢 FAIT VÉRIFIÉ). Elle s'inscrit dans la philosophie de TRADEX-AI : règles à avantage statistique prouvé.
*Catégorie : configuration*
