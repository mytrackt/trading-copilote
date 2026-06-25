# Extraction AdamGrimes — This Is How Breakouts Work (Lessons From The S&P 500)
**Source :** `bundles/adamgrimes/this_is_how_breakouts_work_lessons_from_the_sp_500.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6971 → D6990 · **Page :** https://www.adamhgrimes.com/this-is-how-breakouts-work-lessons-from-the-sp-500/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Mécanique réelle des breakouts (vs. breakouts textuels idéaux) — clé pour filtrer les faux signaux de cassure sur GC/HG/CL/ZW.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| (aucune) | — | — | — |

## DÉCISIONS

### D6971 — Contexte macro comme premier filtre avant tout signal
🟢 **FAIT VÉRIFIÉ** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Avant d'analyser un pattern de prix, le contexte macro directeur doit être établi. Dans l'exemple S&P 500, trois contextes ont été identifiés : (1) tendance haussière existante depuis le creux de mars 2020 (intégrité de tendance), (2) ATH comme point d'attraction magnétique pour les indices, (3) régime de basse volatilité saisonnière attendu.
**TRADEX-AI C1** : Pour GC/HG/CL/ZW, avant tout signal, établir le contexte : (1) tendance de fond (C1 — Direction Belkhayate), (2) niveaux d'attraction proches (pivots, ATH/ATL), (3) régime de volatilité courant (C5 VX). Ces 3 éléments constituent le "contexte de validation" obligatoire.
*Catégorie : structure_marche*

### D6972 — Intégrité de tendance : critère de fiabilité des signaux
🔵 **ÉCOLE** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : "Trend integrity matters" — une tendance établie de longue date (ici depuis mars 2020) augmente la fiabilité des signaux dans sa direction. Les signaux contre-tendance doivent faire face à un biais structurel défavorable.
**TRADEX-AI C1** : Dans le scoring /10, la cohérence avec la tendance de fond (Direction Belkhayate C1) doit peser significativement. Un signal contre la tendance majeure exige un score plus élevé (ex. ≥ 8,0 vs seuil standard 7,0) pour déclencher un ordre.
*Catégorie : indicateurs_tendance*

### D6973 — ATH/ATL comme niveaux d'attraction magnétique
🟢 **FAIT VÉRIFIÉ** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Les sommets/creux historiques exercent un effet d'attraction sur les prix. Un marché en tendance avec un ATH légèrement au-dessus a une probabilité accrue d'atteindre ce niveau. Ce n'est pas de la résistance — c'est une cible.
**TRADEX-AI C1** : Pour GC (Or), les ATH historiques sont des cibles momentum prioritaires, pas des résistances à shorter. Dans le prompt Claude Brain, lorsque le prix est à moins de 1,5× ATR de l'ATH, le biais est haussier jusqu'à preuve du contraire.
*Catégorie : structure_marche*

### D6974 — Régime de basse volatilité saisonnière : adapter les attentes
🟡 **SYNTHÈSE** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Certaines périodes de l'année présentent structurellement une volatilité plus faible et un suivi intraday moindre. Cela ne rend pas les grands mouvements impossibles, mais l'espérance statistique des mouvements est réduite. Adapter la taille des positions en conséquence.
**TRADEX-AI C5** : Le moteur doit inclure un facteur de saisonnalité de volatilité. Pendant les périodes historiquement basses (ex. fin juillet-août), réduire la taille cible des positions et élever le seuil de score minimum pour les signaux Auto.
*Catégorie : saisonnalite*

### D6975 — Marché parabolic = signal d'alerte d'excès (point A)
🟢 **FAIT VÉRIFIÉ** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Une courbe parabolique ascendante (accélération de la hausse en forme de courbe) suivie d'un effondrement immédiat indique que le marché "s'est mis en avance sur lui-même". Ce pattern est identifiable en temps réel et signale une correction imminente probable.
**TRADEX-AI C1** : Sur les actifs GC/HG/CL/ZW, détecter les rallies paraboliques (N barres de hausse accélérée avec slope croissante). Lorsque ce pattern est détecté, bloquer les signaux ACHAT et activer la surveillance VENTE/mean reversion.
*Catégorie : configuration*

### D6976 — Après effondrement parabolique : mode information-gathering (point B)
🔵 **ÉCOLE** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Après un effondrement post-parabolic, la réaction du marché (snapback ou continuation à la baisse) est l'information déterminante. Un snapback rapide (récupération forte) signale de rester loin des positions short. Ce n'est pas un signal d'achat — c'est un signal de neutralité.
**TRADEX-AI C1** : Après un pullback violent post-parabolic, TRADEX-AI doit passer en mode ATTENDRE pendant N barres (ex. 3-5 barres de confirmation) avant d'émettre tout nouveau signal. Le snapback rapide invalide les signaux VENTE potentiels.
*Catégorie : gestion_risque_entree*

### D6977 — Le breakout réel est rarement "propre" (point C)
🟢 **FAIT VÉRIFIÉ** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Les breakouts textuels (test propre, cassure nette, momentum franc) sont rares. Le comportement "normal" d'un breakout fonctionnel sur timeframe journalier inclut des hésitations, des faux tests, et des mouvements non linéaires autour du niveau de breakout pendant plusieurs jours.
**TRADEX-AI C1** : Ne pas exiger un breakout "parfait" pour valider un signal momentum. Un breakout fonctionnel peut se construire sur 3-5 barres avec des mouvements erratiques autour du niveau. La validation se fait sur la clôture au-dessus/en-dessous du niveau, pas sur la forme intraday.
*Catégorie : configuration*

### D6978 — Patterns universels : valables sur tout marché et tout timeframe
🔵 **ÉCOLE** (Source : this_is_how_breakouts_work_lessons_from_the_sp_500.md) : Les leçons extraites de l'analyse du S&P 500 (tendance de fond, attraction des ATH, comportement des breakouts) sont applicables sur tout marché et tout timeframe. La physique des prix est la même.
**TRADEX-AI C1** : Les règles de breakout extraites de l'analyse de l'ES (S&P 500, actif de CONFIRMATION) sont directement transposables aux actifs TRADING (GC, HG, CL, ZW). L'ES peut servir de laboratoire observable pour calibrer la KB sur les breakouts.
*Catégorie : structure_marche*
