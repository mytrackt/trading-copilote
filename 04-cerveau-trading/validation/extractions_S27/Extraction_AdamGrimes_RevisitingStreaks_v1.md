# Extraction AdamGrimes — Revisiting Streaks
**Source :** `bundles/adamgrimes/revisiting_streaks.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6551 → D6562 · **Page :** https://www.adamhgrimes.com/revisiting-streaks/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Les séries de gains/pertes sont inévitables et statistiquement normales — le mode Manuel d'Abdelkrim doit rester ancré sur le plan, pas sur l'émotion du moment.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| — | Aucune image dans ce bundle | — | — |

## DÉCISIONS

### D6551 — Les séries (streaks) de gains et pertes sont inévitables et statistiquement normales
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : Les résultats de trading sont "streakier" (plus en séries) que ce qu'intuitivement on attend. De longues séries de pertes et de gains successifs apparaissent même dans des systèmes avec edge positif. Ce n'est pas un signal de bris du système, c'est de la variance normale.
**TRADEX-AI C5** : La suspension du mode Auto après pertes consécutives (garde-fou G-Suspension) est justifiée psychologiquement mais doit rester temporaire (15-60 min max). Le système n'est pas cassé pendant une série de pertes si le plan est respecté.
*Catégorie : psychologie*

### D6552 — Série de pertes : dangers psychologiques spécifiques
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : Pendant une série de pertes, les traders expérimentés tombent dans des pièges identifiés : désespoir, remise en question du système entier, extrapolation de la courbe d'équité vers la ruine, trades hors-plan pour "revenir à l'équilibre".
**TRADEX-AI C5** : En mode Manuel, si Abdelkrim observe 3+ pertes consécutives, le dashboard doit afficher un avertissement explicite : "Série de pertes normale — respecter le plan". Ne pas modifier les paramètres du système pendant une série.
*Catégorie : psychologie*

### D6553 — Série de gains : danger symétrique (sentiment d'invincibilité)
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : Une série de gains crée un sentiment d'invincibilité identifié par Grimes. Le trader sur-trade, augmente la taille, prend trop de risques, ou extrapole sa courbe d'équité. Il est "toujours à un mauvais trade" de la ruine.
**TRADEX-AI C5** : Après une série de 3+ gains, le mode Auto doit maintenir rigoureusement la taille de position standard. Aucune augmentation automatique de taille basée sur une performance récente positive.
*Catégorie : psychologie*

### D6554 — Solution : trader le plan, simplement
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : La solution aux deux dangers (série de pertes / série de gains) est identique et simple : "trade your plan / follow the plan". La discipline est le seul antidote. La solution est simple mais pas facile.
**TRADEX-AI C5** : Le disclaimer permanent dans l'interface TRADEX-AI doit rappeler ce principe. Le système ne doit jamais modifier ses règles d'entrée/sortie basées sur la performance récente (dernier N trades).
*Catégorie : psychologie*

### D6555 — Comprendre le hasard réduit l'impact psychologique des séries
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : Adam Grimes est "presque seul" dans la communauté d'éducation trading à insister sur l'importance de comprendre le hasard. Si on comprend que les données aléatoires produisent naturellement des séries, on ne s'étonne plus de voir des séries dans ses propres résultats. On ne les internalise pas comme signal.
**TRADEX-AI C5** : L'interface de reporting doit afficher les statistiques de séries attendues (max streak théorique pour win rate X%) en parallèle des séries réelles observées, pour ancrer la référence.
*Catégorie : psychologie*

### D6556 — Les résultats trading sont la moyenne de : actions + système + résultats de trades
🟡 **SYNTHÈSE** (Source : revisiting_streaks.md) : Grimes conclut que les résultats finaux sont la moyenne des actions du trader, du système, et des résultats individuels des trades. Le trader n'est jamais aussi bon qu'il le croit en série de gains, ni aussi mauvais qu'il le croit en série de pertes.
**TRADEX-AI C5** : Le reporting TRADEX-AI doit afficher la performance sur minimum 30 trades glissants (pas sur les 3 derniers). L'évaluation de la qualité du système doit ignorer les < 20 trades.
*Catégorie : psychologie*

### D6557 — Les données aléatoires produisent naturellement des séries (preuve mathématique)
🟢 **FAIT VÉRIFIÉ** (Source : revisiting_streaks.md) : Des données purement aléatoires (pile ou face) produisent des séries longues. Ne pas s'y attendre crée de la surprise et des réactions émotionnelles inappropriées lorsque ces séries surviennent dans le trading réel.
**TRADEX-AI C5** : La connaissance de la distribution statistique des séries pour un win rate donné (ex: 60% win rate → attendre des séries de pertes jusqu'à N) est une donnée de référence à intégrer dans la base de connaissances pour calibrer les attentes.
*Catégorie : psychologie*

### D6558 — Le drawdown est la conséquence objective des séries de pertes
🟡 **SYNTHÈSE** (Source : revisiting_streaks.md) : Les séries de pertes sont "challengeantes objectivement" (drawdown) ET psychologiquement. Le drawdown est la traduction financière d'une série de pertes normale. Il ne signifie pas que le système est cassé.
**TRADEX-AI C5** : Le Risk Manager (risk_manager.py) doit calculer le drawdown max théorique attendu pour le win rate historique du système. Si drawdown réel < drawdown théorique max → mode Auto maintenu. Si dépassement → suspension + alerte.
*Catégorie : gestion_risque_entree*
