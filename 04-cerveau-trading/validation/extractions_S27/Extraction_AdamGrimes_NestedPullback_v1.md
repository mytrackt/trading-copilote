# Extraction AdamGrimes — The Nested Pullback
**Source :** `bundles/adamgrimes/nested_pullback.md` (HTTP 200) + 0 images certifiées
**Méthode images :** aucune image dans le bundle · 0/0 certifiées · 0 à vérifier
**Décisions :** D6331 → D6345 · **Page :** https://www.adamhgrimes.com/nested-pullback/
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Le nested pullback est une configuration d'entrée secondaire directement applicable à GC, HG, CL, ZW — utile pour les signaux manqués et la gestion de position active (C1/structure_marche).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| aucune | — | — | — |

## DÉCISIONS

### D6331 — Définition du nested pullback : pullback dans un pullback
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : Le nested pullback se produit lorsque le marché fait un mouvement de tendance, une pause/pullback, puis une poussée de sortie du pullback — et sur CETTE poussée de sortie, il fait une autre pause plus petite (nested = imbriquée). C'est un pullback secondaire dans la jambe de sortie du pullback principal.
**TRADEX-AI C1** : Documenter ce pattern dans le dictionnaire de configurations de TRADEX-AI. Sur GC/HG/CL/ZW en mode Manuel, signaler à Abdelkrim quand un nested pullback se forme sur la jambe de sortie d'un pullback Belkhayate — c'est une opportunité d'entrée de qualité.
*Catégorie : configuration*

### D6332 — La jambe de sortie d'un pullback est l'un des mouvements directionnels les plus forts
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : Grimes affirme : "One of the strongest directional tendencies in the market happens on that leg out of the pullback; it is appropriate to think that the market is practically drawn to the target for the pullback, and there is a good probability of a clean move." La jambe de sortie d'un pullback a une forte probabilité directionnelle et une cible claire.
**TRADEX-AI C1** : Prioriser les setups où le signal Belkhayate intervient sur la jambe de sortie d'un pullback confirmé. C'est le contexte de plus forte probabilité directionnelle — renforce le score /10 si cette condition est remplie.
*Catégorie : structure_marche*

### D6333 — Nested pullback = deuxième chance d'entrée après avoir manqué le pullback initial
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : "It is not uncommon to miss the pullback entry, and when we do, the presence of a nested pullback can often give us a second chance to get in." Le nested pullback est explicitement identifié comme entrée secondaire de haute qualité pour les trades manqués.
**TRADEX-AI C1** : Dans le mode Manuel de TRADEX-AI, si Abdelkrim n'a pas pris le signal initial (pullback principal), la détection d'un nested pullback doit déclencher une nouvelle alerte "ENTRÉE SECONDAIRE disponible". Cette logique est à implémenter dans claude_brain.py.
*Catégorie : gestion_risque_entree*

### D6334 — Nested pullback confirme l'intégrité du mouvement, réduisant les sorties prématurées
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : "If we know that nested pullbacks are common and that they actually show a strong, intact move, we're less inclined to get out of the trade at the first pause, too early." Le nested pullback est un signal que le mouvement de tendance est intact — ne pas sortir à la première pause.
**TRADEX-AI C1** : Dans la gestion de position active, si un nested pullback se forme pendant un trade ouvert, l'interpréter comme confirmation que le mouvement est intact. Ne pas déclencher de sortie anticipée sur cette seule base. Applicable au mode Manuel comme information contextuelle.
*Catégorie : gestion_position_active*

### D6335 — Multi-timeframe : un pullback sur timeframe de trading est souvent un nested pullback sur TF supérieur
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : "A simple pullback on your trading timeframe will turn out to be a nested pullback on the higher timeframe." L'analyse multi-timeframe se simplifie : un pullback sur TF de trading = nested pullback sur TF supérieur, donc contexte directionnellement favorable sur les deux niveaux.
**TRADEX-AI C1** : Quand NT8 signale un pullback sur le timeframe d'analyse principal, vérifier si le TF supérieur est lui-même en train de sortir d'un pullback. Si oui, le signal est renforcé (nested pullback context = alignement multi-TF). Intégrer ce check dans la logique de scoring Phase C.
*Catégorie : structure_marche*

### D6336 — Les mouvements les plus forts émergent des sorties de pullback, sur tout timeframe
🟢 **FAIT VÉRIFIÉ** (Source : nested_pullback.md) : "Some of the strongest directional moves come on the turns out of pullbacks, on any timeframe." Ce principe est universel — s'applique au daily, hourly, range bars, etc. Si le TF supérieur sort d'un pullback, les patterns avec-tendance sur le TF de trading performent mieux.
**TRADEX-AI C1** : Règle opérationnelle : avant de scorer un signal, vérifier le contexte du TF supérieur. Si le TF supérieur est en "sortie de pullback", augmenter le poids du signal dans la grille /10. Si le TF supérieur est en pullback actif (contre-tendance), réduire le poids.
*Catégorie : timing*

### D6337 — Nested pullback : usage dual — entrée standalone ET outil de gestion
🔵 **ÉCOLE** (Source : nested_pullback.md) : Grimes identifie deux usages distincts du nested pullback : (1) comme pattern de trading autonome pour entrer directement, (2) comme outil de gestion de trade pour décider de rester en position lors de pauses. Les deux usages sont valides et complémentaires.
**TRADEX-AI C1** : Implémenter le nested pullback dans deux modules distincts de TRADEX-AI : dans le module de détection de signal (entrée) ET dans le module de gestion de position active (sortie/tenue). Un même pattern sert à deux décisions opposées selon le contexte.
*Catégorie : configuration*

### D6338 — Le nested pullback est souvent le premier pullback après un breakout
🔵 **ÉCOLE** (Source : nested_pullback.md) : Grimes note que ce pattern se retrouve souvent comme premier pullback après un breakout, mais encore plus communément caché "sur cette poussée de sortie d'un plus grand pullback". C'est un pattern discret qui nécessite de l'expérience pour être identifié.
**TRADEX-AI C1** : Sur GC/HG/CL/ZW, surveiller particulièrement les configurations post-breakout (cassure de résistance/support Belkhayate) : le premier pullback après un breakout est souvent un nested pullback — entrée qualitative haute probabilité.
*Catégorie : configuration*
