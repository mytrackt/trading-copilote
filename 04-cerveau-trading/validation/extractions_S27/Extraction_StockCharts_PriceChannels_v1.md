# Extraction StockCharts — Price Channels (overlay Donchian, C1)
**Source :** `bundles/stockcharts/price_channels.md` (HTTP 200 · ~17 300 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende) · 6/6 certifiées
**Décisions :** D3211 → D3230 · **Page :** chartschool.stockcharts.com/.../technical-overlays/price-channels
**Statut :** BRUT — zone `validation/`, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Page = **overlay Donchian-like** (high/low sur x périodes), distinct du pattern de continuation « Price Channel » (autre bundle). Indicateur déterministe → C1.

---

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | An example of the Price Channels overlay in SharpCharts. | Calculating Price Channels | D3212 |
| image_02 | Price breaks out above upper channel (high based on previous bar) | Calculating Price Channels | D3214 |
| image_03 | How Price Channels can be applied (some whipsaws) | Identifying Trends With Price Channels | D3217 |
| image_04 | Close-only line plot helps filter signals/volatility | Identifying Trends With Price Channels | D3218 |
| image_05 | Chart comparing Price Channels with the Stochastic Oscillator | Price Channels Are Similar to Stochastics | D3221 |
| image_06 | Green arrows mark dips below the 20-day Price Channel | Identifying Overbought/Oversold Levels | D3224 |

---

## DÉCISIONS

### D3211 — Définition : bornes high/low sur x périodes
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Les Price Channels sont des lignes au-dessus et en dessous du prix : **upper = plus haut sur x périodes**, **lower = plus bas sur x périodes**. La **centerline pointillée** est le midpoint des deux. Ils repèrent les poussées (départ d'uptrend), les plongées (départ de downtrend), et les niveaux overbought/oversold dans une tendance.
**TRADEX-AI C1** : indicateur 100 % déterministe, calculable en Python sur barres clôturées GC/HG/CL/ZW.
*Catégorie : indicateurs_tendance*

### D3212 — Paternité Donchian
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_01) : Indicateur développé par **Richard Donchian**, parfois appelé **Donchian Channels**.
**TRADEX-AI C1** : tag 🔵 ÉCOLE (Donchian) ; nomme l'overlay sans ambiguïté vs le pattern oblique.
*Catégorie : indicateurs_tendance*

### D3213 — Formule de calcul (défaut 20)
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : `Upper = plus haut 20 jours` ; `Lower = plus bas 20 jours` ; `Centerline = (plus haut 20j + plus bas 20j)/2`. Défaut SharpCharts = 20, applicable intraday/daily/weekly/monthly. Look-back court (10) → canaux serrés ; long → canaux larges.
**TRADEX-AI C1** : formule directe ; le `period` est l'unique paramètre.
*Catégorie : indicateurs_tendance*

### D3214 — Exclusion de la période courante (anti-circularité)
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_02) : La formule **n'inclut pas la période courante** : un Price Channel pour le 21 oct. se base sur le high/low 20 jours **finissant la veille (20 oct.)**. Un break serait impossible si la période courante était incluse.
**TRADEX-AI C1** : **point d'implémentation critique** — fenêtre décalée d'une barre (`shift(1)`) sinon aucun breakout ne peut se produire.
*Catégorie : configuration*

### D3215 — Interprétation : surge/plunge = départ de tendance
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Un **surge au-dessus de l'upper** montre une force extraordinaire pouvant signaler un départ d'uptrend ; un **plunge sous le lower** montre une faiblesse sérieuse signalant un départ de downtrend.
**TRADEX-AI C1** : signal de breakout directionnel ; brique d'alignement de tendance.
*Catégorie : signal*

### D3216 — Pullbacks oversold/overbought dans une tendance
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Une fois l'uptrend démarré, passer à un timeframe plus court pour repérer les pullbacks : un **move sous le lower channel = oversold** (fin probable du pullback). Symétriquement, un **move au-dessus de l'upper = overbought** (fin probable du bounce dans un downtrend).
**TRADEX-AI C1** : double usage breakout/mean-reversion selon l'horizon — à paramétrer (tendance vs pullback).
*Catégorie : signal*

### D3217 — Identification de tendance + whipsaws assumés
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_03) : Move au-dessus du 20-day channel = nouveau plus haut 20 jours ; au-dessus du 20-week = nouveau plus haut 20 semaines (plus conséquent). Sur ~4,5 ans en hebdo, les breaks ont capté de bonnes tendances mais produit **deux whipsaws** : les signaux ne sont pas parfaits.
**TRADEX-AI C1** : faux signaux **inhérents** → nécessité d'un filtre de confirmation ; le choix du timeframe fixe la « conséquence » du signal.
*Catégorie : signal*

### D3218 — Filtre close-only pour réduire les whipsaws
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_04) : Un plot **close-only** élimine les highs/lows intra-période, réduit volatilité et signaux. Ex. : pas de clôture au-dessus de l'upper en mai 2008 ni sous le lower en mai 2010, supprimant ces signaux.
**TRADEX-AI C1** : option « breakout sur clôture vs sur extrême » à exposer comme réglage de robustesse.
*Catégorie : configuration*

### D3219 — Équivalence conceptuelle avec le Stochastic Oscillator
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Les Price Channels mesurent la même chose que le Stochastic Oscillator : la position de la clôture dans la range high-low sur x périodes (élevé près du haut, bas près du bas).
**TRADEX-AI C1** : lien indicateur connu ; permet réutiliser des seuils stochastiques comme proxy.
*Catégorie : indicateurs_tendance*

### D3220 — Correspondance seuils 80/20 et décalage d'une période
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Le Fast Stochastic 20j est généralement **> 80** quand les prix dépassent l'upper, et **< 20** quand ils passent sous le lower. Léger décalage de timing : les Price Channels finissent à la période précédente, le Stochastic à la période courante.
**TRADEX-AI C1** : équivalence quantifiée 80/20 ↔ bornes du canal ; rappelle le décalage de D3214.
*Catégorie : indicateurs_tendance*

### D3221 — Centerline ↔ niveau 50 du Stochastic
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_05) : Sur DIA, les prix passent au-dessus/en-dessous de la **centerline** quand le Stochastic franchit **50**. Rouge = overbought (près de l'upper), vert = oversold (près du lower).
**TRADEX-AI C1** : la centerline sert de seuil neutre directionnel (équivalent du 50).
*Catégorie : signal*

### D3222 — Overbought/oversold peut persister en tendance forte
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Mesurer overbought/oversold est délicat : en uptrend fort, le prix peut rester au-dessus de l'upper (qui monte avec lui) — **signe de force malgré l'apparence overbought** ; idem le Stochastic peut rester > 80 longtemps.
**TRADEX-AI C1** : garde-fou — ne pas traiter « overbought » comme signal de short en tendance forte.
*Catégorie : signal*

### D3223 — Dépendance à l'identification de tendance
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : L'usage réussi des niveaux overbought/oversold **dépend d'une identification de tendance réussie**. Identifier d'abord l'uptrend long terme, puis chercher l'oversold court terme (après pullback).
**TRADEX-AI C1** : workflow top-down obligatoire avant tout signal de pullback — cohérent avec l'alignement multi-actifs du projet.
*Catégorie : gestion_risque_entree*

### D3224 — Pullbacks daily sous canal hebdo bullish
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md, image_06) : Après un tournant bullish en hebdo (surge au-dessus de l'upper), passer au daily pour chercher les dips sous le 20-day Price Channel. Ex. : deux bons signaux (début juillet, début novembre) ; trois touches jan.–fév. (deux « early », une « direct hit »).
**TRADEX-AI C1** : enchaînement hebdo→daily concret ; signaux imparfaits (« early ») → tolérance de timing.
*Catégorie : configuration*

### D3225 — Logique inverse en downtrend + downtrends plus rapides
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : En downtrend (plunge hebdo sous le lower), chercher l'overbought en daily après un bounce. Les **downtrends sont plus rapides** que les uptrends → l'overbought peut ne pas apparaître ; ajuster les réglages ou utiliser la **centerline** (plus souvent touchée que l'upper).
**TRADEX-AI C1** : asymétrie haussier/baissier à coder ; centerline = repli quand l'extrême n'est pas atteint.
*Catégorie : signal*

### D3226 — Synthèse : high/low de période, centerline = midpoint
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Les Price Channels indiquent quand un titre atteint un plus haut/bas sur une période donnée (20-day → range 20 jours, 10-week → range 10 semaines) ; la centerline marque le midpoint.
**TRADEX-AI C1** : reformulation compacte de la sémantique des bornes.
*Catégorie : indicateurs_tendance*

### D3227 — Dépassements continus = force / faiblesse
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Dépasser continuellement l'upper = signe de **force** (forte pression acheteuse forgeant des higher highs) ; casser continuellement le lower = **faiblesse** (forte pression vendeuse, lower lows). Les Price Channels aident à identifier la force dominante (acheteurs vs vendeurs).
**TRADEX-AI C1** : indicateur de domination acheteurs/vendeurs ; alimente la lecture de pression.
*Catégorie : indicateurs_tendance*

### D3228 — Confirmation par d'autres outils requise
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Comme tout indicateur, **confirmer** avec d'autres techniques (chart patterns, indicateurs, analyse de base).
**TRADEX-AI C1** : interdit le signal mono-indicateur → cohérent avec « 3/4 + 2/3 alignés ».
*Catégorie : gestion_risque_entree*

### D3229 — Scans : oversold bounce / overbought decline (filtre SMA 200)
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Scan « Oversold Bounce in Larger Uptrend » : `Close > SMA(200)` ET croisement à la hausse du **Lower Price Chan(20)** ET `Close > clôture veille`. Scan « Overbought Decline in Larger Downtrend » : `Close < SMA(200)` ET `Upper Price Chan(20) crosses Close` (croisement baissier) ET `Close < clôture veille`.
**TRADEX-AI C1** : logique de filtre directionnel (SMA 200) + déclencheur de canal → transposable en règles déterministes pour GC/HG/CL/ZW.
*Catégorie : gestion_risque_entree*

### D3230 — Réglage par défaut 20, ajustable
🟢 **FAIT VÉRIFIÉ** (Source : price_channels.md) : Dans SharpCharts, Price Channels sont sous **Overlays**, paramètre par défaut **20**. Look-back plus court → canaux plus étroits ; plus long → canaux plus larges.
**TRADEX-AI C1** : confirme `period=20` comme valeur par défaut ; tag 🟡 (convention).
*Catégorie : configuration*

---

## SYNTHÈSE

| Élément | Valeur |
|---------|--------|
| Plage décisions | D3211 → D3230 (20) |
| Faits vérifiés 🟢 | 20 |
| Tags secondaires | 🔵 ÉCOLE (D3212 Donchian) · 🟡 CONVENTION (D3230) |
| Cercle dominant | C1 (Prix / overlay déterministe) |
| Images | 6/6 certifiées |
| Actifs cibles | GC · HG · CL · ZW |
| Belkhayate | NON CONCERNÉ (overlay Donchian, aucun lien propriétaire) |
| Point d'implémentation critique | D3214 — fenêtre décalée d'une barre (`shift(1)`), sinon aucun breakout possible |
| Cas à vérifier | Aucun (6/6 images certifiées ; 0 ambigu) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUTE non fusionnée.
