# Extraction StockCharts — Price Channel (pattern de continuation)
**Source :** `bundles/stockcharts/price_channel.md` (HTTP 200 · ~6 800 car.) + 2 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende) · 2/2 certifiées
**Décisions :** D3191 → D3210 · **Page :** chartschool.stockcharts.com/.../chart-analysis/chart-patterns/price-channel
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Page = **pattern de continuation** (deux trend lines obliques tracées à la main), à NE PAS confondre avec l'overlay « Price Channels » de Donchian (autre bundle, C1).

---

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Example of a price channel. | Price Channel | D3191 |
| image_02 | Example of a price channel in Cisco Systems (CSCO) stock. | Price Channel | D3205 |

---

## DÉCISIONS

### D3191 — Définition : continuation pattern oblique
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md, image_01) : Un price channel est un **pattern de continuation** qui slope vers le haut ou le bas, borné par une trend line supérieure et une inférieure. La trend line supérieure marque la **résistance**, l'inférieure le **support**.
**TRADEX-AI C1** : pattern de continuation directionnel à reconnaître sur GC/HG/CL/ZW ; deux droites obliques parallèles.
*Catégorie : structure_marche*

### D3192 — Polarité selon la pente
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Pente négative (down) → **bearish** ; pente positive (up) → **bullish**. « Bullish price channel » = canal à pente positive, « bearish price channel » = canal à pente négative.
**TRADEX-AI C1** : signe de la pente = variable d'état directionnelle du pattern.
*Catégorie : indicateurs_tendance*

### D3193 — Main Trend Line : construction
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Il faut **au moins deux points** pour tracer la main trend line, qui fixe le ton du trend et la pente. Bullish : la ligne monte, tracée sur **au moins deux reaction lows**. Bearish : la ligne descend, tracée sur **au moins deux reaction highs**.
**TRADEX-AI C1** : critère minimal (2 pivots) pour valider l'existence du canal — codable comme contrainte de détection.
*Catégorie : configuration*

### D3194 — Channel Line : parallèle à la main trend line
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : La channel line est tracée **parallèle** à la main trend line. Idéalement basée sur deux reaction highs/lows ; certains analystes la tracent à partir d'un seul reaction high/low après avoir fixé la main trend line. Elle marque le **support en canal bearish** et la **résistance en canal bullish**.
**TRADEX-AI C1** : la channel line est dérivée (parallèle) ; un seul point suffit en pratique → tolérance de tracé.
*Catégorie : configuration*

### D3195 — Bullish channel : trend intact tant que dans le canal
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Le trend reste bullish tant que les prix avancent et tradent **dans** le canal.
**TRADEX-AI C1** : condition de maintien de l'état haussier = prix contenu dans les bornes.
*Catégorie : indicateurs_tendance*

### D3196 — Bullish channel : premier avertissement (échec à la channel line)
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Premier avertissement de changement de trend bullish = les prix **n'atteignent plus** la résistance channel line (fall short).
**TRADEX-AI C1** : signal précoce d'affaiblissement = non-atteinte de la borne haute.
*Catégorie : signal*

### D3197 — Bullish channel : cassure de support = changement de trend
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Une **cassure sous la main trend line support** indique un changement de trend (bullish → autre).
**TRADEX-AI C1** : critère de sortie/invalidation du canal haussier.
*Catégorie : signal*

### D3198 — Bullish channel : break au-dessus = accélération
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Un **break au-dessus de la résistance channel line** est bullish et indique une **accélération** de l'avance.
**TRADEX-AI C1** : événement haussier renforçant (pas une sortie) ; à distinguer d'un break baissier.
*Catégorie : signal*

### D3199 — Bearish channel : trend intact tant que dans le canal
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Le trend reste bearish tant que les prix déclinent et tradent **dans** le canal.
**TRADEX-AI C1** : symétrique de D3195 pour l'état baissier.
*Catégorie : indicateurs_tendance*

### D3200 — Bearish channel : premier avertissement
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Premier avertissement de changement de trend bearish = le prix **n'atteint plus** le support channel line.
**TRADEX-AI C1** : signal précoce de retournement baissier = non-atteinte de la borne basse.
*Catégorie : signal*

### D3201 — Bearish channel : break au-dessus de la résistance = changement
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Un **break au-dessus de la main trend line résistance** indique un changement de trend (bearish → autre).
**TRADEX-AI C1** : critère de sortie/invalidation du canal baissier.
*Catégorie : signal*

### D3202 — Bearish channel : break sous le support = accélération
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Un **break sous le support channel line** est bearish et indique une **accélération** du déclin.
**TRADEX-AI C1** : événement baissier renforçant (pas une sortie).
*Catégorie : signal*

### D3203 — Scaling semi-log recommandé
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Les trend lines collent mieux aux reaction highs/lows en échelle **semi-log** (semi-logarithmic / percentage). En semi-log, un mouvement 50→100 occupe la même distance que 100→200.
**TRADEX-AI C1** : tag 🟡 (convention de tracé) ; impacte la détection visuelle mais pas la logique d'ordre.
*Catégorie : configuration*

### D3204 — Entrées/sorties pratiques + confirmation requise
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : En canal bullish, certains traders **achètent** au contact du support main trend line ; en canal bearish, certains **vendent/shortent** au contact de la résistance main trend line. Comme pour la plupart des patterns, **d'autres outils d'AT doivent confirmer** les signaux.
**TRADEX-AI C1** : règle d'entrée mean-reversion dans le canal, **sous réserve de confirmation** — cohérent avec la règle projet « 3/4 + 2/3 alignés ». Tag 🔵 ÉCOLE (pratique discrétionnaire « some traders »).
*Catégorie : gestion_risque_entree*

### D3205 — Exemple CSCO : main trend line construite par lows successifs
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md, image_02) : Sur Cisco (CSCO), canal bullish de ~11 mois en 1999. La main trend line débute sur les lows de janvier/février/mars, **confirmée** par les lows d'avril, mai et août.
**TRADEX-AI C1** : illustre l'ajout de points de confirmation renforçant la fiabilité du tracé.
*Catégorie : configuration*

### D3206 — Channel line dérivée du high de départ
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Une fois la main trend line en place, la channel line a été tracée depuis le high de janvier ; inspection visuelle = lignes parallèles. Une analyse plus précise testerait la pente, mais l'inspection visuelle suffit généralement à garantir l'« essence » du pattern.
**TRADEX-AI C1** : tolérance de parallélisme (visuelle) ; pas d'exigence d'égalité stricte des pentes.
*Catégorie : configuration*

### D3207 — Touches successives = opportunités d'achat
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Sur CSCO, les touches successives de la main trend line ont offert de **bonnes opportunités d'achat** (mi-avril, fin mai, mi-août).
**TRADEX-AI C1** : confirme la logique d'entrée au support (D3204) par l'exemple.
*Catégorie : gestion_risque_entree*

### D3208 — Échec proche de la channel line jugé insignifiant
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Le high de septembre est tombé **juste en deçà** de la résistance channel line, d'une marge « probablement insignifiante » ; le high de juillet avait atteint la channel line (reaction high significatif).
**TRADEX-AI C1** : nécessité d'une **tolérance/seuil** pour qualifier « atteinte » vs « échec » de la channel line — paramètre de robustesse.
*Catégorie : configuration*

### D3209 — Break au-dessus = accélération (exemple déc. 1999)
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Le break au-dessus de la channel line en décembre 1999 a marqué une **accélération** de l'avance. Le titre pouvait paraître overextended, mais l'avance fut puissante et le trend n'est jamais devenu bearish.
**TRADEX-AI C1** : confirme D3198 par l'exemple ; un break haussier ≠ signal de sortie.
*Catégorie : signal*

### D3210 — Durée de vie limitée mais trend présumé jusqu'à invalidation
🟢 **FAIT VÉRIFIÉ** (Source : price_channel.md) : Les price channels « ne durent pas éternellement », mais le **trend sous-jacent reste valable jusqu'à preuve du contraire**. L'AT est autant art que science → flexibilité dans la pertinence et le placement des lignes.
**TRADEX-AI C1** : principe de persistance du trend (présomption de continuation) ; tag 🟡 (jugement discrétionnaire sur le tracé).
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D3191 → D3210 (20) |
| Faits vérifiés 🟢 | 20 |
| Tags secondaires | 🔵 ÉCOLE (D3204) · 🟡 CONVENTION (D3203, D3208, D3210) |
| Cercle dominant | C1 (Prix / pattern de continuation) |
| Images | 2/2 certifiées |
| Actifs cibles | GC · HG · CL · ZW |
| Belkhayate | NON CONCERNÉ (pattern d'AT classique, aucun lien propriétaire) |
| Cas à vérifier | Aucun (2/2 images certifiées ; 0 ambigu) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
