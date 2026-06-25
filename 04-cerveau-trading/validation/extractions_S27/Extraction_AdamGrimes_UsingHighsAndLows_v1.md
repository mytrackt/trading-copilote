# Extraction AdamGrimes — Using Highs and Lows
**Source :** `bundles/adamgrimes/using_highs_and_lows.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image exploitable dans ce bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D7271 → D7285 · **Page :** https://www.adamhgrimes.com/using-highs-and-lows/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Les hauts et bas de la veille comme niveaux clés de structure — applicable directement à GC/HG/CL/ZW pour qualifier les setups d'entrée.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune image extraite) | — | — | — |

## DÉCISIONS

### D7271 — Règle : évaluer la force d'un marché par son mouvement depuis l'ouverture, pas depuis la clôture précédente
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : La meilleure évaluation de la force ou faiblesse d'un marché sur une journée vient de l'analyse de son mouvement depuis l'ouverture du jour, et non depuis la clôture de la veille.
**TRADEX-AI C1** : Les données NT8 transmises à claude_brain.py doivent systématiquement inclure le prix d'ouverture du jour comme référence de force/faiblesse intraday pour GC, HG, CL et ZW.
*Catégorie : structure_marche*

### D7272 — Règle fondamentale : toujours connaître le haut et le bas de la veille
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Le haut et le bas de la séance précédente sont des niveaux critiques à connaître en permanence, à la fois pour les marchés larges (indices) et pour chaque actif tradé individuellement.
**TRADEX-AI C1** : data_reader.py doit extraire et exposer systématiquement le Previous_High et le Previous_Low pour GC, HG, CL, ZW (et actifs de confirmation : ES, DX) à chaque cycle de lecture NT8.
*Catégorie : structure_marche*

### D7273 — Concept : le haut/bas de la veille marquent les points où bulls/bears ont capitulé
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Les hauts et bas de la veille représentent les niveaux où une des deux forces (bulls ou bears) a perdu la bataille et le marché s'est retourné. Ces niveaux restent pertinents le jour suivant comme zones de résistance/support.
**TRADEX-AI C1** : Dans le prompt Claude, mentionner explicitement si le prix actuel approche du Previous_High ou Previous_Low de la veille — cela constitue un critère de structure (C1) dans la grille /10.
*Catégorie : structure_marche*

### D7274 — Signal haussier : le haut tient mais le prix revient à l'ouverture en clôture (cas A)
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Configuration A — Le haut de la veille tient comme résistance, mais le prix revient fermer à (ou proche de) l'ouverture du jour. Ce pattern indique une pression haussière significative sous-jacente malgré l'échec à casser le haut.
**TRADEX-AI C1** : Ce pattern (résistance tenue + retour clôture sur ouverture) doit contribuer positivement au score C1 de la grille /10, signalant un biais haussier potentiel pour le lendemain.
*Catégorie : configuration*

### D7275 — Signal mixte : haut tient + cassure de 2 bas précédents (cas B)
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Configuration B — Le haut de la veille tient, mais le prix casse les bas de deux journées consécutives. Une vente à découvert intraday sous ces bas était une trade réaliste. Le biais de fin de journée reste neutre/incertain.
**TRADEX-AI C1** : La cassure de plusieurs bas consécutifs (N ≥ 2) est un signal de faiblesse structurelle à intégrer dans C1 — augmente la probabilité d'un signal VENDRE sur GC/CL/HG/ZW.
*Catégorie : configuration*

### D7276 — Setup haussier : inside day + clôture sur les hauts (cas C → D)
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Configuration C — La majorité de la journée est un "inside day" (range inférieur à celui de la veille), et le prix clôture sur ses hauts. C'est un excellent setup haussier pour une "trend day" le lendemain.
**TRADEX-AI C1** : Un inside day qui clôture sur ses hauts sur GC ou ZW est un signal de compression précédant une expansion — à inclure dans le critère de structure C1 comme signal d'alerte pré-signal.
*Catégorie : configuration*

### D7277 — Alerte : momentum adverse rapide depuis l'ouverture peut invalider le setup (cas D)
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Configuration D — Un fort momentum dès l'ouverture peut rapidement invalider un setup haussier du jour précédent (comme C). Dans ce cas, la pression s'accumule contre le bas de la veille, créant une opportunité short sur la cassure de ce niveau.
**TRADEX-AI C1/C2** : Le staleness_monitor doit détecter les mouvements brusques dès l'ouverture (delta order flow ATAS > seuil) qui pourraient invalider un signal calculé en pré-marché.
*Catégorie : gestion_risque_entree*

### D7278 — Règle d'entrée : vente à découvert sur cassure du bas de la veille
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : La cassure du bas de la veille est une entrée short réaliste et exploitable. La deuxième journée en arrière (J-2) peut également servir de niveau de support/résistance secondaire.
**TRADEX-AI C1** : Pour GC, HG, CL, ZW — la cassure du Previous_Low avec confirmation order flow (C2) constitue un signal d'entrée VENDRE valide dans la grille /10 de TRADEX.
*Catégorie : gestion_risque_entree*

### D7279 — Règle : les gaps à l'ouverture sont un concept distinct à traiter séparément
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Les gaps (écarts à l'ouverture par rapport à la clôture précédente) sont des événements significatifs qui méritent une analyse séparée et ne rentrent pas directement dans la logique haut/bas de la veille.
**TRADEX-AI C1** : Créer un champ "gap_ouverture" dans les données NT8 pour GC/HG/CL/ZW — les gaps significatifs (> 0,3% de la valeur) doivent être signalés séparément dans le prompt Claude.
*Catégorie : structure_marche*

### D7280 — Principe : même les traders long terme doivent surveiller les niveaux de haut/bas de la veille
🟡 **SYNTHÈSE** (Source : using_highs_and_lows.md) : Les traders positionnels (horizons jours/semaines/mois) ont tendance à ignorer les mouvements journaliers, mais ils doivent connaître les hauts/bas de la veille pour savoir quand "payer attention" — quand quelque chose d'important se passe réellement.
**TRADEX-AI C1** : Même en mode Manuel avec des signaux sur timeframe supérieur, TRADEX doit alerter Abdelkrim si le prix teste le Previous_High ou Previous_Low de la veille — c'est un signal que "ça bouge vraiment".
*Catégorie : psychologie*

### D7281 — Outil d'évaluation : mesurer l'importance d'un mouvement par rapport à la norme de volatilité
🟡 **SYNTHÈSE** (Source : using_highs_and_lows.md) : Pour savoir si un mouvement de marché "compte vraiment", il faut comprendre comment les marchés bougent en temps normal et repérer ce qui sort de ces ranges habituels. La question n'est pas "combien de points ?" mais "est-ce anormal ?"
**TRADEX-AI C5** : L'Énergie Belkhayate (stub actuellement) devra comparer les mouvements actuels à la norme de volatilité historique des 20 derniers jours — un mouvement > 2 écarts-types vaut un signal d'attention.
*Catégorie : indicateurs_momentum*

### D7282 — Application pratique : construire un programme de trading autour des hauts/bas
🟡 **SYNTHÈSE** (Source : using_highs_and_lows.md) : Pour les traders intraday, il est possible de construire un programme de trading complet et fiable basé uniquement sur les hauts et bas de la veille comme niveaux de référence. C'est un outil simple mais robuste.
**TRADEX-AI C1** : Les niveaux Previous_High et Previous_Low constituent à eux seuls une grille de niveaux clés valide pour TRADEX — à afficher en permanence dans le dashboard pour chaque actif TRADING.
*Catégorie : structure_marche*

### D7283 — Limite : les marchés sont parfois eux-mêmes "confus"
🟡 **SYNTHÈSE** (Source : using_highs_and_lows.md) : Les concepts de haut/bas de la veille ne répondent pas à toutes les questions. Parfois le marché lui-même manque de direction claire, et aucun outil ne peut lever cette ambiguïté.
**TRADEX-AI C1** : Quand les données NT8 montrent un Inside Day sans direction claire ET que les actifs de confirmation (ES, DX) sont aussi indécis, le signal TRADEX doit sortir ATTENDRE — c'est un critère d'exclusion valide.
*Catégorie : gestion_risque_entree*

### D7284 — Concept : l'évaluation de "l'importance" d'un mouvement passe par la comparaison à la normale
🟡 **SYNTHÈSE** (Source : using_highs_and_lows.md) : Les questions pertinentes pour évaluer un mouvement de marché sont : "est-ce important ?", "est-ce que ça change quelque chose ?" Ces questions ne peuvent être répondues qu'avec une référence de normalité (niveaux, ranges, hauts/bas).
**TRADEX-AI C1** : Le prompt Claude de TRADEX doit systématiquement inclure le contexte de normalité (ATR sur 14j, range moyen sur 5j) pour que l'IA puisse évaluer si le mouvement actuel est significatif ou dans la norme.
*Catégorie : structure_marche*

### D7285 — Règle : timing des entrées et sorties amélioré par les niveaux haut/bas
🟢 **FAIT VÉRIFIÉ** (Source : using_highs_and_lows.md) : Avec les hauts/bas de la veille comme référence, le timing des entrées, la décision de tenir une position ou de sortir deviennent beaucoup plus faciles. Ces niveaux fournissent des "guidelines" claires.
**TRADEX-AI C1** : Pour le mode Manuel TRADEX, afficher toujours la distance du prix actuel par rapport aux Previous_High/Low pour GC, HG, CL, ZW — cela aide Abdelkrim à décider d'entrer, tenir ou sortir.
*Catégorie : gestion_position_active*
