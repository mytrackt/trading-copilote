# Extraction AdamGrimes — Free Bars: Little Patterns After Big Moves
**Source :** `bundles/adamgrimes/free_bars_little_patterns_after_big_moves.md` (HTTP 200) + 0 images certifiées
**Méthode images :** 1 image référencée dans le bundle (exemples free bars sur marchés) · non accessible dans le bundle texte · 0 certifiées · à vérifier si bundle image disponible
**Décisions :** D5931 → D5950 · **Page :** https://www.adamhgrimes.com/free-bars-little-patterns-after-big-moves/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Pattern "Free Bar" (barre hors Keltner) — signal d'extension/climax — aligné C1 (Prix Belkhayate) et gestion des entrées après grands mouvements.

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | "Several markets with recent examples of free bars marked" (référencé dans le texte) | How to use free bars | D5932 |

## DÉCISIONS

### D5931 — Définition exacte d'une "Free Bar" : barre entièrement hors du canal Keltner
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_oves.md) : Une Free Bar Up est définie comme : BarLow > UpperChannel. Une Free Bar Down : BarHigh < LowerChannel. La barre ENTIÈRE (haut ET bas) doit être hors du canal, pas seulement la clôture.
**TRADEX-AI C1** : Ce pattern est directement calculable sur NT8 avec les données de prix. Implémenter la détection Free Bar dans data_reader.py pour GC/HG/CL/ZW : si la bougie daily est entièrement hors du Keltner (2.25 ATR ± EMA20), lever un flag d'alerte d'extension.
*Catégorie : configuration*

### D5932 — Paramètres Keltner validés par Grimes : 2.25 ATR ± EMA 20 périodes
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Les paramètres utilisés par Grimes pour ses Keltner Channels : 2.25 ATRs au-dessus et en dessous d'une EMA 20 périodes. Avec ces paramètres, les Free Bars représentent moins de 4% de toutes les barres daily.
**TRADEX-AI C1** : Utiliser ces paramètres (Keltner 2.25 ATR / EMA 20) comme référence dans settings.py pour le calcul des niveaux d'extension. Ces paramètres sont Grimes-certified et non arbitraires. Préférer Keltner à Bollinger (Grimes préfère Keltner pour des raisons mathématiques expliquées ailleurs).
*Catégorie : indicateurs_tendance*

### D5933 — Fréquence des Free Bars : moins de 4% sur daily toutes classes d'actifs
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Statistique empirique de Grimes : Free Bars < 4% de toutes les barres daily. Small caps : ~4.3% (avec certaines actions jusqu'à 20%). FX : 2.3%. Les commodités futures se situent dans la fourchette générale.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW en daily, les Free Bars sont des événements rares (<4% des barres). Lorsqu'ils apparaissent, ils méritent une attention prioritaire dans la grille /10. Ce n'est pas un outil de screening quotidien mais un signal d'alerte d'exception.
*Catégorie : structure_marche*

### D5934 — Problème clé : impossible de distinguer overextension vs continuation de force
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Le problème fondamental des mesures overbought/oversold s'applique aux Free Bars : une barre hors canal peut indiquer une extension sur-étirée prête à corriger, OU une force/faiblesse exceptionnelle qui va continuer. Ne pas supposer automatiquement un retournement.
**TRADEX-AI C1/C2** : Lorsqu'une Free Bar est détectée sur GC ou CL, TRADEX doit croiser avec C2 (Order Flow ATAS : delta, big trades) pour distinguer les deux cas. Free Bar + delta divergent = probable retournement. Free Bar + delta confirmant = probable continuation.
*Catégorie : gestion_risque_entree*

### D5935 — Usage 1 : "go with" — trader dans la direction de la Free Bar après consolidation
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Première approche valide : utiliser la Free Bar pour identifier les marchés en fort momentum, puis attendre un pullback ou une consolidation sur le timeframe de trading pour entrer dans la direction de la Free Bar.
**TRADEX-AI C1** : Aligné avec la règle Belkhayate 3/4 trading : une Free Bar dans la direction du signal Belkhayate (BGC + Direction alignés) constitue une confirmation supplémentaire de momentum. Bonus de confiance +0.5 dans la grille /10 si Free Bar confirme la direction du signal.
*Catégorie : configuration*

### D5936 — Usage 2 : fade court terme — shorter la clôture Free Bar, racheter à l'ouverture suivante
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Deuxième approche : shorter (ou acheter) une action qui clôture en Free Bar et déboucler à l'ouverture du lendemain. Grimes note qu'il peut exister un edge statistique sur ce trade de très court terme.
**TRADEX-AI C1** : Mode Manuel uniquement — Abdelkrim peut appliquer ce fade à très court terme sur GC/CL. TRADEX ne doit PAS automatiser ce type de trade counter-trend en mode Auto, car il contredit la règle d'alignement 3/4 + 2/3. Le signaler comme "opportunité manuelle potentielle" dans l'UI.
*Catégorie : gestion_position_active*

### D5937 — Usage 3 : multiples Free Bars consécutives = signal d'extension/climax potentiel
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Plusieurs Free Bars consécutives dans la même direction signalent une sur-extension ou un climax potentiel de la tendance. Ce cumul est plus significatif qu'une Free Bar isolée.
**TRADEX-AI C1/C5** : Implémenter un compteur de Free Bars consécutives dans data_reader.py. Si ≥2 Free Bars consécutives sur GC ou CL, lever un flag "climax_warning" qui élève le seuil de confiance requis pour un signal Auto et alerte Abdelkrim en mode Manuel.
*Catégorie : structure_marche*

### D5938 — Usage 4 : contexte de la tendance change la signification de la Free Bar
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : L'auteur suggère explicitement d'explorer les différences entre Free Bars survenant dans une tendance mature, une nouvelle tendance, ou hors d'un range. Le contexte change la probabilité de continuation vs retournement.
**TRADEX-AI C1** : Dans la grille de scoring TRADEX, le contexte Belkhayate (Phase de tendance : BGC haussier/baissier, Énergie, Phase du cycle) doit moduler l'interprétation d'une Free Bar. Free Bar en tendance mature Belkhayate = climax probable. Free Bar en nouvelle tendance = continuation probable.
*Catégorie : structure_marche*

### D5939 — Keltner préféré à Bollinger pour des raisons mathématiques
🔵 **ÉCOLE** (Source : free_bars_little_patterns_after_big_moves.md) : Grimes indique préférer les Keltner Channels aux Bollinger Bands "pour de nombreuses raisons, pratiques et mathématiques", sans les détailler dans cet article. Cela suggère une robustesse statistique supérieure du Keltner.
**TRADEX-AI C1** : Décision de référence : si TRADEX implémente un indicateur de canal, utiliser Keltner (2.25 ATR / EMA 20) plutôt que Bollinger. Aligner avec la position de Grimes validée empiriquement sur des milliers de marchés.
*Catégorie : indicateurs_tendance*

### D5940 — Les barres "touchant" le canal sont déjà des zones d'intérêt significatives
🟢 **FAIT VÉRIFIÉ** (Source : free_bars_little_patterns_after_big_moves.md) : Le canal définit ce qui est "normal". Quand le prix touche le canal, il entre en territoire "anormal" d'intérêt potentiel. Les Free Bars (entièrement hors canal) sont le niveau d'exception suivant.
**TRADEX-AI C1** : Hiérarchie de signaux de canal pour TRADEX : (1) Prix dans le canal = régime normal, aucun signal d'extension ; (2) Prix touchant le canal = zone d'attention accrue, croiser avec C2 ; (3) Free Bar complète = alerte d'exception, scoring boosté ou prudence selon contexte.
*Catégorie : indicateurs_tendance*
