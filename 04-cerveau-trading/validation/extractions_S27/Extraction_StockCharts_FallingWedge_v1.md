# Extraction StockCharts — Falling Wedge
**Source :** `bundles/stockcharts/falling_wedge.md` (HTTP 200 · ~6 300 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 2/2 certifiées
**Décisions :** D1711 → D1723 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns/falling-wedge
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Example of a Falling Wedge chart pattern. | Is the Falling Wedge a Reversal or Continuation Pattern? | CERTIFIE (accord .md + HTML) |
| image_02.png | A Falling Wedge reversal chart pattern in the stock price of Freeport McMoran. | What Are the Characteristics of a Falling Wedge? | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1711 — Nature : figure haussière, large au sommet et se contractant en baissant
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md, image_01) : « The Falling Wedge is a bullish pattern that begins wide at the top and contracts as prices move lower. » Le price action forme un cône orienté à la baisse à mesure que reaction highs et reaction lows convergent. Contrairement au triangle symétrique (sans pente ni biais définis), le falling wedge penche clairement vers le bas avec un biais haussier — réalisable seulement après une cassure de résistance.
**TRADEX-AI C1** : Figure chartiste à biais haussier, géométrie en cône descendant convergent ; candidate comme configuration analytique, jamais comme ordre automatique.
*Catégorie : configuration*

---

### D1712 — Double rôle : retournement OU continuation, mais toujours haussier
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : En figure de continuation, le falling wedge penche toujours vers le bas mais à contre-courant de l'uptrend dominant. En figure de retournement, il penche vers le bas dans le sens de la tendance dominante (baissière). « Regardless of the type (reversal or continuation), falling wedges are regarded as bullish patterns. »
**TRADEX-AI C1** : Biais haussier invariant quel que soit le contexte ; la distinction retournement/continuation dépend de la tendance préalable — à déterminer algorithmiquement avant scoring.
*Catégorie : configuration*

---

### D1713 — Tendance préalable : downtrend étendu, idéalement marquant le creux final
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Pour qualifier un retournement, il faut une tendance préalable à inverser. Idéalement le falling wedge se forme après un downtrend étendu et marque le creux final. La figure se forme typiquement sur 3 à 6 mois, et le downtrend précédent devrait avoir au moins 3 mois.
**TRADEX-AI C1** : Critères temporels déterministes (downtrend ≥ 3 mois ; figure 3-6 mois) ; à adapter au timeframe NT8 mais bornent la recherche de figure.
*Catégorie : timing*

---

### D1714 — Ligne de résistance haute : ≥ 2 reaction highs (idéalement 3), chacun plus bas
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Il faut au moins deux reaction highs (idéalement trois) pour former la ligne de résistance supérieure. Chaque reaction high doit être plus bas que les précédents.
**TRADEX-AI C1** : Condition de détection (≥2 sommets décroissants) codable comme garde-fou de validité de la ligne haute via régression sur sommets.
*Catégorie : structure_marche*

---

### D1715 — Ligne de support basse : ≥ 2 reaction lows, chacun plus bas
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Au moins deux reaction lows sont requis pour la ligne de support inférieure. Chaque reaction low doit être plus bas que les précédents.
**TRADEX-AI C1** : Condition de détection (≥2 creux décroissants) codable comme test sur la ligne basse.
*Catégorie : structure_marche*

---

### D1716 — Contraction : pénétrations de plus en plus faibles (baisse de la pression vendeuse)
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Les deux lignes convergent en cône à maturité. Les reaction lows pénètrent les plus bas précédents mais cette pénétration devient de plus en plus faible (shallower). Des creux moins profonds indiquent une baisse de pression vendeuse et créent une ligne de support à pente moins négative que la ligne de résistance.
**TRADEX-AI C1** : Critère discriminant clé (pente support > pente résistance, i.e. moins négative) ; mesurable par comparaison des pentes des deux droites de régression.
*Catégorie : structure_marche*

---

### D1717 — Cassure de résistance = confirmation haussière (attendre > reaction high précédent)
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : La confirmation haussière est établie une fois la ligne de résistance cassée « in a convincing fashion ». Il est parfois prudent d'attendre une cassure au-dessus du reaction high précédent pour confirmation supplémentaire. Une fois la résistance cassée, il peut y avoir une correction testant le nouveau support.
**TRADEX-AI C1** : Règle de déclenchement (cassure résistance + option : > reaction high précédent) + retest possible ; codable comme condition d'entrée et zone de stop.
*Catégorie : signal*

---

### D1718 — Volume : ingrédient essentiel pour confirmer la cassure du falling wedge
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Contrairement au rising wedge (où le volume importe peu), le volume est « an essential ingredient to confirm a falling wedge breakout ». Sans expansion de volume, la cassure manque de conviction et est vulnérable à l'échec.
**TRADEX-AI C2** : Confirmation par expansion de volume à la cassure = filtre order flow (ATAS) ; ici qualifié d'« essentiel » (plus fort que pour ascending triangle où c'était « préféré »). À noter dans la pondération.
*Catégorie : signal*

---

### D1719 — Interprétation : ralentissement de la baisse alerte sur un retournement potentiel
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : « The falling wedge indicates a decrease in downside momentum and alerts investors and traders to a potential trend reversal. » Même si la pression vendeuse diminue, la demande ne l'emporte qu'à la cassure de résistance. Comme pour la plupart des figures, il faut attendre la cassure et combiner d'autres outils techniques pour confirmer.
**TRADEX-AI C1** : Sémantique de la figure (perte de momentum baissier) ; la prudence « attendre la cassure + confirmer » est cohérente avec le biais ATTENDRE par défaut du projet.
*Catégorie : configuration*

---

### D1720 — Difficulté de reconnaissance : figure parmi les plus dures à trader
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Comme les rising wedges, le falling wedge « can be one of the most difficult chart patterns to recognize and trade accurately ». Le titre baisse avec lower highs et lower lows comme dans un falling wedge.
**TRADEX-AI C1** : Avertissement de fiabilité — pondérer la confiance de détection à la baisse ; recoupe la prudence du projet sur les signaux isolés.
*Catégorie : configuration*

---

### D1721 — Exemple Freeport McMoran (FCX) : 4 sommets/4 creux décroissants, divergence PPO
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md, image_02) : Cas d'école FCX en fin de long downtrend (débuté T3 1997). Ligne de résistance formée par quatre sommets successivement plus bas ; ligne de support par quatre plus bas successifs. Chaque creux à peine plus bas (demande intervenant presque immédiatement). Le bas de fin février était plat (consolidation juste au-dessus de 9 quelques semaines) ; cassure en mars avec une série d'avances fortes ET divergence positive du PPO.
**TRADEX-AI C1** : Cas pédagogique confirmant la séquence contraction → consolidation → cassure ; la divergence PPO ajoute une confirmation momentum optionnelle. Aucun paramètre nouveau.
*Catégorie : configuration*

---

### D1722 — Confirmation volume et money flow sur l'exemple FCX
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md, image_02) : Après le gros volume baissier du 24 février (flèche rouge), le volume haussier a commencé à augmenter ; volume au-dessus de la moyenne sur les jours haussiers et à la cassure de la trend line. Les money flows ont confirmé la force en dépassant leur plus haut de novembre 1998. Après la cassure, bref pullback vers le support de l'extension de trend line, consolidation quelques semaines, puis avance sur volume accru.
**TRADEX-AI C2** : Illustre la confirmation conjointe volume + money flow + retest ; recoupe la logique order flow / pullback du projet. Valeur illustrative.
*Catégorie : signal*

---

### D1723 — Cible et synthèse FAQ : projection, durée, conditions de qualification
🟢 **FAIT VÉRIFIÉ** (Source : falling_wedge.md) : Synthèse (« The Bottom Line » + FAQ) : figure haussière suggérant un mouvement haussier, signalant un retournement ou une continuation probable ; peut se développer sur plusieurs mois, culminant en cassure haussière quand le prix dépasse convaincamment la résistance, idéalement avec forte hausse du volume. FAQ : (1) retournement vs continuation = dépend de la tendance préalable ; (2) confirmation = cassure convaincante de la résistance souvent avec volume accru, prudent d'attendre > reaction high précédent ; (3) volume essentiel = démontre la conviction du marché ; (4) trader = repérer lower highs/lower lows, identifier le ralentissement de la baisse, attendre la cassure de la résistance et valider avec d'autres outils ; (5) durée = downtrend ≥ 3 mois, figure 3-6 mois.
**TRADEX-AI C1** : Consolide les règles déjà extraites en check-list opérationnelle (qualification + confirmation + volume + durée) ; aucune cible chiffrée n'est donnée par la source (pas de formule de projection explicite ici, contrairement à l'ascending triangle).
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1711 | Figure haussière, cône descendant convergent | 🟢 | C1 | configuration |
| D1712 | Retournement OU continuation, toujours haussier | 🟢 | C1 | configuration |
| D1713 | Downtrend ≥ 3 mois, figure 3-6 mois | 🟢 | C1 | timing |
| D1714 | ≥ 2 reaction highs décroissants | 🟢 | C1 | structure_marche |
| D1715 | ≥ 2 reaction lows décroissants | 🟢 | C1 | structure_marche |
| D1716 | Contraction : pente support moins négative | 🟢 | C1 | structure_marche |
| D1717 | Cassure résistance = confirmation + retest | 🟢 | C1 | signal |
| D1718 | Volume essentiel pour confirmer la cassure | 🟢 | C2 | signal |
| D1719 | Baisse du momentum baissier = alerte retournement | 🟢 | C1 | configuration |
| D1720 | Figure difficile à reconnaître/trader | 🟢 | C1 | configuration |
| D1721 | Exemple FCX (4/4, divergence PPO) | 🟢 | C1 | configuration |
| D1722 | Confirmation volume + money flow (FCX) | 🟢 | C2 | signal |
| D1723 | Synthèse + FAQ (qualification/confirmation/durée) | 🟢 | C1 | configuration |

**Liens Belkhayate :** Le falling wedge est une figure chartiste classique (StockCharts), PAS un élément de la méthode Belkhayate (⚫ — NON CONCERNÉ). Rapprochement indirect possible : la zone de cassure et le retest recoupent l'usage des pivots/zones Belkhayate comme niveaux opératoires, mais l'attribuer à Belkhayate serait une hypothèse projet non affirmée par la source (⚫🔴). NB : Freeport McMoran (FCX) est un producteur de cuivre/or — lien thématique avec GC/HG mais l'exemple reste une action, pas le futures TRADEX.

**À vérifier (humain) :**
- D1718 — la source qualifie le volume d'« essentiel » (plus fort que « préféré » pour l'ascending triangle) : arbitrer si TRADEX en fait un critère éliminatoire pour le falling wedge spécifiquement.
- Pas de formule de cible chiffrée dans cette page (contrairement à l'ascending triangle) : si une projection est souhaitée, elle devra venir d'une autre source.
- D1721/D1722 — chiffres FCX (consolidation vers 9, T3 1997, fév-mars 1999, PPO, money flow nov-98) = valeurs historiques illustratives, non transposables en paramètres.
- Durées 3-6 mois / downtrend ≥ 3 mois calibrées sur du daily action : revalider sur range bars NT8 (GC/HG/CL/ZW).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
