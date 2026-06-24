# Extraction StockCharts — Volatility Indices (VIX)
**Source :** `bundles/stockcharts/volatility_indices.md` (HTTP 200) + 10 images certifiées
**Méthode images :** double ancrage v3 (.md figcaption + HTML légende + section-fallback) · 10/10 certifiées · 0 à vérifier
**Décisions :** D279 → D290 · **Page :** chartschool.stockcharts.com/.../market-indicators/volatility-indices
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI (page PRIORITAIRE)** : le VIX est le cœur du **cercle C5 (sentiment / peur)**. **VX** est un actif de **CONFIRMATION** du projet (analyse uniquement, jamais d'ordre direct). Lien direct avec le garde-fou « Suspension Auto » : VIX élevé / spike → suspension du mode Auto (15-60 min). Tous les faits littéraux ci-dessous sont 🟢 ; les seuils chiffrés (30/18, PPO 25/-10) sont datés et **contextuels** donc ⏳ VOLATILE.

---

## INVENTAIRE IMAGES CERTIFIÉES (traçabilité)

| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| image_01 | Volatility Index - Chart 1 | Calculation | D280 |
| image_02 | Volatility Index - Chart 2 | Calculation | D280 |
| image_03 | Volatility Index - Table 1 | Calculation | D281 |
| image_04 | Volatility Index - Chart 3 | Trends, Ranges and Spikes | D283 |
| image_05 | Volatility Index - Chart 4 | Sentiment Extremes | D284 |
| image_06 | Volatility Index - Chart 5 | Sentiment Extremes | D285 |
| image_07 | Volatility Index - Chart 6 | Detrending with the PPO | D286 |
| image_08 | Volatility Index - Chart 7 | Detrending with the PPO | D287 |
| image_09 | SharpCharts (section-fallback) | SharpCharts | D289 |
| image_10 | Volatility Index - SharpCharts | SharpCharts | D289 |

---

## DÉCISIONS

### D279 — VIX : définition et nature
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Les indices de volatilité mesurent la **volatilité implicite** d'un panier d'options put et call liées à un indice ou ETF. Le plus connu est le Cboe Volatility Index (**$VIX**), qui mesure la volatilité implicite d'un panier d'options out-of-the-money put/call sur le S&P 500 ; il est conçu pour mesurer la **volatilité attendue à 30 jours** du S&P 500.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Le Cboe calcule des indices de volatilité pour plusieurs ETF/indices (Gold SPDR, USO Oil, Euro Currency Trust, Dow, S&P 500, Nasdaq 100). Les chartistes utilisent le VIX pour **mesurer le sentiment** et repérer les extrêmes de sentiment qui peuvent précéder des retournements.
**TRADEX-AI C5** : VIX = brique centrale du sentiment / peur (cercle C5). Actif **VX** = CONFIRMATION uniquement (jamais d'ordre direct). Sert à anticiper les retournements de marché sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D280 — VIX : historique et méthodologies (original vs 2003)
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_01, image_02) : Créé en **1993**, le VIX utilisait à l'origine les options du S&P 100 et une méthodologie différente (options at-the-money) ; cette « formule originale » reste disponible sous le ticker **$VXO**. En **2003**, le Cboe a adopté une nouvelle méthodologie utilisant les options put/call near-term (≥ 1 semaine avant expiration) et next-term (1-2 mois) sur le S&P 500.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : La différence entre l'ancien et le nouvel indicateur est **négligeable à l'œil nu** (cf. graphiques). Chaque prix d'option porte une volatilité implicite (= écart-type) ; le Cboe calcule une moyenne pondérée pour obtenir la volatilité attendue à 30 jours.
**TRADEX-AI C5** : Utiliser le **$VIX** courant (méthode 2003) comme proxy sentiment VX ; $VXO non requis. Brancher la source de données VIX en lecture seule.
*Catégorie : structure_marche*

---

### D281 — VIX : lecture annualisée → mensuelle → quotidienne (4 étapes de calcul)
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_03) : Calcul en 4 étapes — (1) sélectionner les options put/call near-term et next-term ; (2) calculer la volatilité implicite de chaque option ; (3) calculer une moyenne pondérée de ces volatilités ; (4) multiplier cette moyenne par 100.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Le VIX donne l'écart-type pondéré à 30 jours du mouvement annuel du S&P 500. Une lecture de 20 % anticipe un mouvement de 20 % (haut ou bas) sur 12 mois. Conversion : nombre mensuel = annualisé ÷ √12 (~3,464) ; nombre quotidien = annualisé ÷ √252 (~15,874, soit le nombre de jours de bourse). On parle de **volatilité**, pas de rendement attendu ni de direction.
**TRADEX-AI C4/C5** : Si calcul d'une bande de mouvement attendu autour du S&P 500, appliquer ÷√252 pour le pas quotidien ; ne jamais confondre amplitude attendue et direction.
*Catégorie : structure_marche*

---

### D282 — Relation inverse VIX ↔ marché actions (indicateur coïncident)
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Le VIX a typiquement une **relation inverse** avec le marché actions : il monte quand les actions baissent et baisse quand elles montent. Un marché haussier est perçu comme moins risqué, un marché baissier comme plus risqué ; plus le risque perçu est élevé, plus la volatilité implicite est haute. Une baisse augmente la demande de puts → hausse des prix des puts → hausse de la volatilité implicite.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : De nombreux analystes considèrent le VIX comme un **indicateur coïncident** : il bouge quand les actions bougent, pas indépendamment. Il peut servir d'indicateur **confirmant la tendance** car il évolue souvent en sens opposé du marché actions.
**TRADEX-AI C5/C7** : Traiter VX comme confirmation coïncidente (inverse de ES), pas comme indicateur avancé indépendant. Intégrer la corrélation inverse VIX/ES dans la matrice C7.
*Catégorie : structure_marche*

---

### D283 — Tendances, ranges et spikes du VIX ; « fear index »
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_04) : Sur longue période, le VIX montre des tendances prolongées, des ranges définis et des spikes intermittents. Exemple : VIX dans la zone 10-15 fin 2006 (bas), range plus haut de juillet 2007 à octobre 2008 (ne passe pas sous 15, se retourne après avoir dépassé 30), puis surge au-dessus de 75 au T4 2008.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Le pic VIX de fin 2008 a **précédé** le creux du S&P 500 (mars 2009). Le spike au-dessus de 40 début mai 2010 coïncide avec le **flash crash** du 6 mai 2010 — simple blip sur le S&P 500 mais énorme spike sur le VIX. Ces surges de panique valent au VIX le surnom de **« fear index »**.
**TRADEX-AI C5** : Un **spike de VIX** = signal de panique/peur extrême → déclencheur du garde-fou « Suspension Auto » (mode Auto bloqué 15-60 min). Distinguer spike (panique ponctuelle) de range/tendance.
*Catégorie : signal*

---

### D284 — Extrêmes de sentiment dans un range (anticipation de retournement)
🔵 **ÉCOLE** (Source : volatility_indices.md, image_05) : Les extrêmes de sentiment se repèrent quand le VIX évolue dans un range ou en spike. Dans le range de juillet 2007 à octobre 2008, les mouvements vers le **haut du range (30-32)** signalaient un excès de pessimisme annonçant des retournements **haussiers** ; les mouvements vers le **bas du range (16-18)** signalaient un excès d'optimisme annonçant des retournements **baissiers**. Sur 10 mois : 4 extrêmes baissiers et 2 haussiers, « pas parfait mais assez efficace ».
⏳ **VOLATILE** : Les niveaux 30-32 / 16-18 sont **spécifiques au régime 2007-2008** ; la source précise que la plupart des ranges sont moins bien définis et se décalent dans le temps (cf. D285). À ne pas figer en dur.
**TRADEX-AI C5** : Détecter les extrêmes VIX **relatifs au range courant**, pas via des seuils absolus codés en dur. Extrême haut VIX → pré-alerte retournement haussier ES → contexte favorable longs GC/HG/CL/ZW (confirmation seulement).
*Catégorie : signal*

---

### D285 — Les ranges se décalent ; un spike isolé peut marquer un creux
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_06) : La plupart des ranges ne sont pas bien définis et se décalent. De 2004 à 2006, le range a **dérivé vers le bas** jusqu'à VIX 10 (juillet 2005). Un spike au-dessus de 20 en juin 2006 n'a **pas** annoncé de downtrend prolongé : il a signalé un excès de pessimisme/panique marquant un **creux majeur**. Autre spike au-dessus de 18 = autre creux majeur du S&P 500.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Un « couplage » anormal a eu lieu d'avril à octobre 2007 — actions ET VIX montant ensemble (au lieu de la relation inverse normale). « Quelque chose ne va pas quand le VIX et le S&P 500 montent ensemble » : ce couplage anormal a servi d'**avertissement** précédant un déclin prolongé (octobre 2007 → février 2009).
**TRADEX-AI C5/C7** : Garde — un seuil VIX absolu ne suffit pas (range mobile). Surveiller le **couplage anormal VIX↑ + ES↑** comme signal d'alerte de retournement baissier (rupture de la corrélation inverse attendue).
*Catégorie : signal*

---

### D286 — Détrendage du VIX via le PPO (10,50,1)
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_07) : Le VIX tendant souvent, il est difficile d'y repérer extrêmes ou cycles. On peut **détrender** le VIX en lui appliquant le Percent Price Oscillator (PPO). `PPO = (EMA 10 jours − EMA 50 jours) / EMA 50 jours` ; il représente l'écart en % entre les deux EMA. PPO positif quand l'EMA 10j du VIX > EMA 50j, négatif sinon. L'exemple utilise PPO(10,50,1) — le « 1 » fusionne la ligne de signal avec l'indicateur.
**TRADEX-AI C5** : Si besoin de comparer des extrêmes VIX entre régimes, calculer un **VIX PPO(10,50,1)** côté Python pour neutraliser la tendance et obtenir un oscillateur centré sur zéro.
*Catégorie : structure_marche*

---

### D287 — Signaux du VIX PPO et timing par confirmation de retour
🔵 **ÉCOLE** (Source : volatility_indices.md, image_08) : Le VIX PPO(10,50,1) oscille au-dessus/au-dessous de zéro. Range assez défini de 2006 à mi-2008 ; expansion fin 2008 (PPO > 50 en octobre 2008, puis < -17 en janvier 2009). Surge à 40 en avril-mai 2010 = extrême baissier.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Le timing s'améliore en **attendant un retour** sous l'extrême : passer haussier dès le premier franchissement au-dessus de 25 aurait été coûteux (le PPO est resté > 25 plusieurs semaines en septembre 2008 pendant que le marché continuait de chuter). Après le creux de mars 2009, les signaux d'excès d'optimisme (PPO < -10) n'ont **pas** fonctionné durant le fort uptrend.
⏳ **VOLATILE** : Les seuils PPO 25 / -10 sont **datés et contextuels** ; la source montre qu'ils échouent en régime de forte tendance. Ne pas coder en dur.
**TRADEX-AI C5/D2 (timing)** : Règle de timing — n'armer un signal d'extrême VIX/PPO qu'**après retour** sous le seuil (confirmation), jamais au franchissement initial. Désactiver le signal « excès d'optimisme » en uptrend fort.
*Catégorie : timing*

---

### D288 — Conclusions : indicateur de sentiment, jamais utilisé seul
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Les indices de volatilité sont des **indicateurs de sentiment** réactifs, **pas prédictifs** : ils identifient des extrêmes de sentiment, baissant pendant les avancées et montant pendant les baisses. Les déclins brusques produisent des spikes exagérés (panique) ; un spike au-dessus de niveaux spécifiques suggère un excès de pessimisme pouvant mener à un rally. L'excès d'optimisme est souvent **difficile à définir** quand les actions montent.
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md) : Comme la plupart des indicateurs de sentiment, le VIX **doit être utilisé conjointement** à d'autres indicateurs pour le market timing. Les chances de retournement augmentent avec les extrêmes de sentiment, mais il faut recourir aux **oscillateurs de momentum, patterns graphiques ou autres formes d'analyse technique** pour confirmer ou timer un retournement.
**TRADEX-AI C5** : Guard permanent — le VIX (VX) ne fournit jamais une entrée seul ; il alimente C5 et doit être confirmé par price action / momentum sur GC/HG/CL/ZW. Cohérent avec la règle d'entrée projet (3/4 trading + 2/3 confirmation alignés).
*Catégorie : gestion_risque_entree*

---

### D289 — Affichage / paramétrage SharpCharts (référence)
🟢 **FAIT VÉRIFIÉ** (Source : volatility_indices.md, image_09, image_10) : Le VIX peut être ajouté comme indicateur au-dessus/au-dessous du graphique principal (S&P 500 dans la fenêtre principale, VIX dessous, ou inverse). Pour l'afficher en PPO(10,50,1) : créer un graphique $VIX, type « Invisible », ajouter « Price » avec $SPX en « Behind Price », ajouter le PPO avec paramètres « 10,50 » en « Below », hauteur 1.0.
**TRADEX-AI C0** : Référence d'affichage/paramétrage ; exposer dans l'UI le couple $VIX brut + option VIX PPO(10,50,1) ; aligner les défauts PPO 10/50.
*Catégorie : structure_marche*

---

### D290 — Rattachement Belkhayate (hypothèse projet)
⚫🔴 **PROPRIÉTAIRE / NON VÉRIFIÉ (rattachement TRADEX-AI)** : La source ne mentionne ni Belkhayate ni l'« Énergie ». Le VIX n'apparaît dans aucun élément documenté de la méthode Belkhayate (Pivots, BGC, Direction, Énergie/MFI). Son usage comme filtre de sentiment / déclencheur de suspension Auto est une **hypothèse projet TRADEX-AI, non affirmée par la source**.
**TRADEX-AI C5** : VX reste un actif de CONFIRMATION (cercle C5), greffé en surcouche de la méthode Belkhayate, et non un composant de la méthode elle-même. Garde-fou : VIX élevé / spike → suspension mode Auto (15-60 min).
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D279 → D290 (12) |
| Images certifiées citées | 10/10 |
| Catégories utilisées | structure_marche · signal · timing · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · ⏳ VOLATILE · ⚫🔴 (rattachement Belkhayate) |
| Cercle dominant | **C5 (sentiment / peur)** — page PRIORITAIRE |
| Actif projet concerné | **VX** (CONFIRMATION, jamais d'ordre direct) ; lien garde-fou Suspension Auto (VIX élevé/spike) |
| Belkhayate | **NON concerné par la source** — usage VIX = hypothèse projet, non affirmée (D290) |

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
