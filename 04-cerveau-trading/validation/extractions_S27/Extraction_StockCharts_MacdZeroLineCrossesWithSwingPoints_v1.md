# Extraction StockCharts — MACD Zero-Line Crosses With Swing Points

**Source :** `bundles/stockcharts/macd_zero_line_crosses_with_swing_points.md` (HTTP 200 · ~9 939 car.) + 3 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende locale + section fallback) · 3/3 certifiées
**Décisions :** D2511 → D2521 · **Page :** chartschool.stockcharts.com/.../trading-strategies/macd-zero-line-crosses-with-swing-points
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Périmètre** : famille MACD — **stratégie de trading** (croisement ligne zéro filtré par swing points). CERCLE momentum **C3**. Le MACD de base est extrait ailleurs.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | MACD zero line cross in StockCharts.com | What Is the MACD Zero Line Cross? | D2512 |
| image_02 | False and ideal MACD trading signals. | Combining MACD Zero Line Cross With Swing Points | D2515 |
| image_03 | MACD zero crosses in SLV using StockCharts.com | Combining MACD Zero Line Cross With Swing Points | D2517 |

---

## DÉCISIONS

### D2511 — Key takeaways de la stratégie
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Points clés — (1) le croisement de ligne zéro du MACD est un outil populaire pour jauger le momentum et générer des signaux ; (2) sa **précision augmente** en tenant compte des **swing points** (briques de base des tendances) ; (3) le croisement donne le signal initial mais la **price action temps réel** guide la décision en analysant le contexte plus large du trade.
**TRADEX-AI C3** : Stratégie = croisement zéro MACD **filtré** par structure de swing — jamais le croisement seul. Aligné sur l'esprit Belkhayate (structure avant indicateur).
*Catégorie : configuration*

---

### D2512 — Définition du croisement de ligne zéro (bullish / bearish)
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md, image_01) : Le croisement de ligne zéro = quand le MACD et la ligne de signal croisent la ligne zéro. Deux types — **Positif (haussier)** : MACD et signal croisent **au-dessus** de zéro → momentum haussier. **Négatif (baissier)** : MACD et signal croisent **en dessous** de zéro → momentum baissier. La ligne zéro est le seuil.
**TRADEX-AI C3** : Détecter les deux croisements zéro comme signal de momentum directionnel brut sur GC/HG/CL/ZW (à filtrer, cf. D2513).
*Catégorie : signal*

---

### D2513 — Problème : autant de bruit que de signal
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Le problème du croisement zéro est qu'il produit **autant de bruit que de signal** ; il faut donc le **filtrer** pour augmenter les chances de succès. Comme le MACD repose sur des moyennes mobiles (indicateur retardé), un moyen efficace d'obtenir une lecture plus juste est d'utiliser la **price action temps réel**, notamment les swing points (swing highs / swing lows).
**TRADEX-AI C3** : Garde permanente — ne jamais armer un signal sur croisement zéro nu ; exiger filtre structurel sur GC/HG/CL/ZW (réduction du bruit).
*Catégorie : gestion_risque_entree*

---

### D2514 — Swing points = briques de base des tendances
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Les swing points sont les briques de base des tendances — **Uptrend** = plus hauts plus hauts (HH) et plus bas plus hauts (HL) ; **Downtrend** = plus bas plus bas (LL) et plus hauts plus bas (LH). Pour qu'un uptrend se maintienne, il faut des cassures haussières continues des swing highs précédents tandis que les bas ne doivent pas casser sous les swing lows précédents (et inversement en downtrend).
**TRADEX-AI C1** : Encoder la détection HH/HL/LL/LH (structure de marché) comme filtre déterministe du croisement zéro — base de la lecture de tendance Belkhayate (Direction).
*Catégorie : indicateurs_tendance*

---

### D2515 — Combinaison : exemples de signaux faux vs idéaux (chart 1)
🔵 **ÉCOLE** (Source : macd_zero_line_crosses_with_swing_points.md, image_02) : Lecture du 1er chart — (1) croisement zéro + croisement positif **dans la zone H–L** → aucune indication haussière (le prix est dans la congestion) ; (2) 2e croisement (négatif) = tendance mineure dans la congestion → signal pas le plus fort (rappel : un signal fort peut donner un mauvais résultat et inversement) ; (3) 3e croisement = scénario différent : le prix avait cassé sous la zone H–L initiale (downtrend LL/LH) puis a creusé au 2e LL avant de **casser au-dessus du LH récent** → retournement haussier potentiel, rallye jusqu'au croisement zéro suivant (sortie).
**TRADEX-AI C3** : Règle — invalider un croisement zéro survenant **à l'intérieur d'une zone de congestion H–L** ; ne valider qu'avec cassure d'un swing point structurant sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D2516 — Caveats sur les sorties et le régime de marché
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Deux mises en garde — (1) les **sorties ne peuvent pas toujours reposer sur le croisement zéro opposé** (cela peut effacer les profits) ; mieux vaut d'autres méthodes de sortie ; (2) certaines conditions de marché conviennent mieux aux **swing trades court terme** qu'aux détentions long terme.
**TRADEX-AI C3** : Découpler entrée et sortie — ne pas coder la sortie comme « croisement zéro opposé » par défaut ; prévoir stops/objectifs alternatifs (cf. D2517).
*Catégorie : gestion_risque_entree*

---

### D2517 — Étude SLV (chart 2) : gestion des sorties par stops et measured move
🔵 **ÉCOLE** (Source : macd_zero_line_crosses_with_swing_points.md, image_03) : Exemple SLV — (1) 1er croisement favorable grâce à la cassure au-dessus du HH, mais tenir jusqu'au croisement négatif aurait effacé une grande part des profits (placer le stop sous la zone de support/congestion) ; (2) trade short après cassure sous un rectangle, sortie via **measured move** = extension 100 % du risque (hauteur du rectangle) plutôt que d'attendre le croisement opposé ; (3) suivre le stop quelques points sous chaque swing low pour préserver les profits.
**TRADEX-AI C3** : Implémenter des sorties basées sur congestion/support, trailing stop sous swing lows, et measured move (extension 100 % de la hauteur du pattern) sur GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

---

### D2518 — Étude SLV : signal price action qui prime sur le croisement zéro
🔵 **ÉCOLE** (Source : macd_zero_line_crosses_with_swing_points.md, image_03) : (4) Attendre le croisement pour entrer un short aurait donné perte ou breakeven : une cassure sous la price action de sommet, MACD et signal clairement en baisse, **supplante** le croisement zéro (probabilité élevée de croisement négatif à venir). (5–6) Des croisements zéro **entre deux zones support/résistance (LL et LH)** font « jumper le départ » d'une cassure → mieux vaut attendre une cassure ou un autre driver avant d'entrer.
**TRADEX-AI C3** : Règle de priorité — une cassure structurelle confirmée peut **précéder/remplacer** le croisement zéro comme déclencheur ; ne pas entrer sur croisement zéro piégé entre support/résistance.
*Catégorie : signal*

---

### D2519 — Règle synthétique de trading du croisement zéro
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Règle simple — **attendre un croisement de ligne zéro** PUIS **vérifier les swing points (ou toute price action) qui soutient le cas haussier/baissier** ; sinon, s'appuyer sur le seul croisement zéro rend vulnérable aux **faux signaux**.
**TRADEX-AI C3** : Séquence d'armement Python — (1) détecter croisement zéro ; (2) exiger confirmation de swing point cohérent ; (3) seulement alors générer un signal candidat sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D2520 — Bottom line : le croisement n'est qu'un indice, la price action décide
🟢 **FAIT VÉRIFIÉ** (Source : macd_zero_line_crosses_with_swing_points.md) : Attraper un début de tendance est difficile et miné par les faux signaux. Le croisement zéro du MACD aide à identifier un shift de momentum, mais il faut le **filtrer** pour éviter le bruit. En combinant croisement zéro + swing points (price action temps réel), on augmente les chances de succès. Au final, le croisement zéro fournit **un indice** ; c'est la **price action sous-jacente** qui détermine plus précisément l'opportunité.
**TRADEX-AI C3** : Hiérarchie de décision — price action (structure) > croisement zéro (indice). Cohérent avec la primauté Belkhayate de la lecture de prix sur l'indicateur.
*Catégorie : configuration*

---

### D2521 — Filtre swing points ↔ lecture Direction Belkhayate
⚫🔴 **PROPRIÉTAIRE / NON VÉRIFIÉ (rattachement TRADEX-AI)** : La méthode (structure HH/HL/LL/LH primant sur l'indicateur) **converge** avec l'étape « Direction » de la lecture Belkhayate (Pivots → BGC → Direction → Énergie). La source StockCharts ne mentionne **pas** Belkhayate ; ce rapprochement est une hypothèse projet, non affirmée par la source.
**TRADEX-AI C1/C3** : Réutiliser le détecteur de swing points (D2514) comme brique commune au filtre du croisement zéro ET à l'étape Direction Belkhayate ; lien à valider humainement.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D2511 → D2521 (11) |
| Images certifiées citées | 3/3 |
| Catégories utilisées | configuration · signal · indicateurs_tendance · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · ⚫🔴 (rattachement Direction Belkhayate) |
| Belkhayate | **CONCERNÉ (hypothèse)** — filtre swing points ↔ étape Direction (D2521), non affirmé par la source |
| Cas à vérifier | D2521 : rapprochement swing points ↔ Direction Belkhayate = hypothèse projet à valider humainement |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
