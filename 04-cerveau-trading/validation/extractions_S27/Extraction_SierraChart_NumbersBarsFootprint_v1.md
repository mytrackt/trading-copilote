# Extraction Sierra Chart — Numbers Bars (Footprint)

**Source :** `bundles/sierrachart/numbers_bars_footprint.md` (page doc Sierra Chart, ~385 Ko · doc technique très volumineuse — extraction limitée au contenu TRADING : concepts order flow, lecture footprint, signaux ; les énumérations de paramètres logiciel/couleurs/menus sont IGNORÉES)
**Méthode images :** manifest `numbers_bars_footprint_manifest.txt` → **0 figure `<figure>+<figcaption>` sur la page** · 0 certifiée · 0 à vérifier (aucune image exploitable)
**Décisions :** D399 → D409 · **Page :** sierrachart.com/index.php?page=doc/NumbersBars.php
**Statut :** BRUT — zone `validation/`, NON fusionné dans le master (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 **Enjeu TRADEX-AI** : page **PRIORITAIRE** pour le **cercle C2 (order flow ATAS)**. Le « Numbers Bars » de Sierra Chart = le **Footprint** (terme employé par d'autres logiciels, dont ATAS). Définit rigoureusement Bid/Ask Volume, Delta, Volume at Price, Point of Control, dominance et imbalance — vocabulaire directement transposable à la lecture ATAS sur GC/HG/CL/ZW. La source illustre avec l'actif ES (Tick Size .25) : ES est un actif de **CONFIRMATION** côté projet, jamais tradable — l'exemple sert uniquement de référence technique.

---

## INVENTAIRE IMAGES

| Image | Statut | Note |
|-------|--------|------|
| (aucune) | — | Le manifest indique 0 figure `<figure>+<figcaption>` sur la page. Le contenu retenu est 100 % textuel ; les renvois visuels de la doc (charts d'exemple) ne sont pas extraits en images. |

---

## DÉCISIONS

### D399 — Numbers Bars = Footprint : définition
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : Le Numbers Bars est une étude Sierra Chart qui donne une vue très détaillée du **volume et de l'activité de trading à l'intérieur de chaque barre**. Les barres de prix classiques sont remplacées par jusqu'à 3 colonnes de chiffres ; il y a un nombre (ou une paire de nombres) **pour chaque niveau de prix de chaque barre**, détaillant l'activité volumique à ce niveau. Les chiffres peuvent représenter la différence Ask Volume − Bid Volume, le Volume total, le nombre de Trades, ou l'Ask Volume et le Bid Volume séparés.
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : « Numbers Bars is also known as "Footprint" in other charting programs. »
**TRADEX-AI C2** : Brique de base de la lecture order flow — le footprint décompose le volume par niveau de prix intrabar ; vocabulaire à mapper sur l'export ATAS pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D400 — Prérequis données : intraday, 1 Tick, PAS de market depth
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : Le Numbers Bars ne fonctionne correctement **que sur charts intraday** (jamais sur Daily historique). Les enregistrements du fichier intraday doivent être en **1 Tick**, sinon les données affichées seront moins précises. L'étude **ne requiert PAS de données Market Depth (carnet d'ordres)** : elle a seulement besoin du meilleur Bid et du meilleur Ask. « Any study in Sierra Chart that has a dependency on Bid Volume and Ask Volume, has no dependency on Market Depth data. »
**TRADEX-AI C0/C2** : Contrainte d'ingestion — le footprint exige un flux tick-by-tick (best bid/ask) ; inutile de capter la profondeur de marché. À aligner sur la collecte NT8/ATAS Phase C (données intraday, jamais Daily).
*Catégorie : structure_marche*

---

### D401 — Bid Trade vs Ask Trade : classification de chaque trade
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : Un **Bid Trade** est un trade considéré comme exécuté au prix Bid ; un **Ask Trade** au prix Ask. La détermination la plus fiable est quand l'exchange/data feed indique lui-même le côté — « In the case of the CME Group, EUREX, NASDAQ TotalView, CFE data from the Denali Exchange Data Feed, this is the method used. So there is 100% accuracy with this. » À défaut : prix ≤ Bid → Bid Trade, prix ≥ Ask → Ask Trade, ou classement par uptick/downtick. La détermination **n'est en aucun cas affectée par l'horodatage**.
**TRADEX-AI C2** : Fondement du delta — chaque trade est marqué acheteur (Ask) ou vendeur (Bid). ⚠️ Côté projet, les actifs tradables (GC/HG/CL/ZW) sont **CME/CBOT** → cas « 100 % de précision » d'après la source. Vérifier que le flux NTB/Rithmic fournit bien le marquage exchange (sinon fallback uptick/downtick, moins fiable).
*Catégorie : structure_marche*

---

### D402 — Bid Volume / Ask Volume / Delta : les 3 mesures clés
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : **Bid Volume** = somme du volume tradé (contrats/parts, pas le nombre de trades) classé Bid Trade pour un niveau de prix ou une période. **Ask Volume** = idem côté Ask. **Delta** : « Typically this means the difference between Ask Volume and Bid Volume at a particular Numbers Bar price level or for a period of time. » (Sierra évite ce terme jugé trop général, mais en donne la définition standard.)
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : **Volume** = quantité totale de contrats/parts tradés à un niveau de prix ou sur une période. Distinction explicite : **nombre de trades ≠ volume** (un trade peut avoir une quantité > 1).
**TRADEX-AI C2** : Trois grandeurs canoniques du footprint à exposer côté moteur — Bid Vol, Ask Vol, Delta = Ask Vol − Bid Vol. Le Delta positif = pression acheteuse, négatif = pression vendeuse, sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D403 — Point of Control (POC) : prix de plus fort volume
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : « The Point of Control in a Numbers Bar is the **price level where there is the greatest volume** among all of the other price levels. » Il est mis en évidence par un rectangle autour de ce niveau.
**TRADEX-AI C2/C1** : Le POC intrabar = niveau de prix où l'activité s'est concentrée → repère d'acceptation/valeur. À détecter par barre sur GC/HG/CL/ZW comme zone de référence (support/résistance intrabar), à recouper avec les pivots Belkhayate.
*Catégorie : structure_marche*

---

### D404 — Dominant Side : quel côté l'emporte à un niveau
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : **Dominant Side** = en comparant Bid Volume et Ask Volume à un niveau de prix, le côté à la **valeur la plus grande** est dominant.
🔵 **ÉCOLE** (Source : numbers_bars_footprint.md) : Le **Dominant Side Volume Percent** quantifie cette dominance — pourcentage positif quand l'Ask Volume > Bid Volume (part de l'Ask dans Ask+Bid), négatif quand le Bid Volume domine. Permet de lire l'intensité de la dominance, pas seulement son sens.
**TRADEX-AI C2** : Lecture niveau-par-niveau du rapport de force acheteurs/vendeurs ; signal de pression directionnelle à un prix donné sur GC/HG/CL/ZW.
*Catégorie : signal*

---

### D405 — Diagonal Dominant Side : la comparaison « footprint » correcte
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : **Diagonal Dominant Side** — au lieu de comparer Bid et Ask au même niveau, on compare le **Bid Volume d'un niveau à l'Ask Volume du niveau immédiatement supérieur**, et l'Ask Volume au Bid Volume du niveau inférieur. Le côté le plus grand est dominant. « Within a bar, the highest Bid Volume and lowest Ask Volume are never dominant because there is nothing to compare against. »
**TRADEX-AI C2** : Comparaison diagonale = la lecture footprint « académique » (les ordres au marché frappent le niveau adverse). Préférer la dominance **diagonale** pour juger l'agressivité réelle acheteurs/vendeurs sur GC/HG/CL/ZW, plutôt que la comparaison verticale brute.
*Catégorie : signal*

---

### D406 — Imbalance Bid/Ask : seuil de déséquilibre
🔵 **ÉCOLE** (Source : numbers_bars_footprint.md, section « Display Ask/Bid Imbalance ») : Une **imbalance** se colore quand la dominance d'un côté dépasse un **pourcentage seuil**. La doc utilise comme exemple un seuil exprimé en multiple : « 0, 0, 4 (last number is the imbalance percentage you want — 4 = 400%) », via la méthode *Based on Dominant Side AskVol/BidVol Percentage* (ou sa variante *Diagonal*).
🟡 **CONVENTION** : Le seuil d'imbalance (ex. 300 %/400 %) est un **paramètre de configuration**, pas une constante universelle ; à calibrer par actif.
**TRADEX-AI C2/C3** : Un empilement d'imbalances du même côté = pression directionnelle confirmée (signal d'order flow). Implémenter un détecteur d'imbalance paramétrable (ratio Ask/Bid ou Bid/Ask diagonal ≥ seuil) sur GC/HG/CL/ZW, à traiter en **confirmation**, jamais en entrée isolée.
*Catégorie : signal*

---

### D407 — Volume Profile intrabar & Ask/Bid Split Profile
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : Le **Volume Profile** (fond de barre) remplit chaque niveau selon son volume **comparé au volume maximum** parmi les niveaux de la barre. Le **Ask Bid Difference Profile** colore la largeur selon la différence Ask−Bid relative à la différence max. Le **Ask/Bid Volume Split Profile** trace deux profils séparés : Bid Volume à gauche, Ask Volume à droite, chacun bâti indépendamment vs son propre max.
**TRADEX-AI C2** : Outils visuels de répartition du volume/delta dans la barre → identifier où l'agression se concentre (haut vs bas de barre). Concept réutilisable pour qualifier absorption (gros volume sans progression du prix) vs initiative sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D408 — Tick Size : granularité des niveaux du footprint
🟢 **FAIT VÉRIFIÉ** (Source : numbers_bars_footprint.md) : **Tick Size** = valeur minimale de variation du prix d'un symbole ; chaque niveau du Numbers Bar correspond à un tick. Exemple littéral de la source : « the S&P ES futures has a Tick Size of .25. » Pour FX/crypto, un Tick Size trop petit multiplie les niveaux et ralentit la construction (la doc conseille un Tick Size plus large via le *Volume at Price Multiplier*).
**TRADEX-AI C2** : ⚠️ L'exemple ES est purement technique — ES est un actif de **CONFIRMATION** côté projet (jamais tradable). Pour le footprint sur GC/HG/CL/ZW, paramétrer le bon Tick Size par actif (lisibilité des niveaux) ; un multiplicateur d'agrégation peut être nécessaire si trop de niveaux.
*Catégorie : structure_marche*

---

### D409 — Le footprint seul ne donne pas un signal d'entrée
🔵 **ÉCOLE** (Source : numbers_bars_footprint.md) : La doc présente le Numbers Bars comme un **outil de visualisation détaillée** de l'activité (volume, delta, dominance, imbalance, POC) — un instrument de lecture, hautement configurable, **sans règle d'entrée/sortie prescrite**. Les valeurs (delta, imbalance, POC) décrivent l'activité, elles ne constituent pas en soi une consigne d'ordre.
🟡 **CONVENTION** (rattachement TRADEX-AI) : Les signaux footprint (delta, imbalance, dominance, POC) sont des **confirmations C2**, à combiner avec le prix Belkhayate (C1 : pivots, BGC, direction) et les autres cercles avant tout signal.
**TRADEX-AI C2/C3** : Guard permanent — aucun ordre sur la seule base d'un déséquilibre footprint ; exiger l'alignement multi-cercles (3/4 trading + 2/3 confirmation, score /10) sur GC/HG/CL/ZW. Mode AUTO reste bloqué par défaut.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| Compteur | Valeur |
|----------|--------|
| Décisions ajoutées | D399 → D409 (11) |
| Images certifiées citées | 0/0 (manifest : aucune figure exploitable sur la page) |
| Catégories utilisées | structure_marche · signal · gestion_risque_entree |
| Tags employés | 🟢 FAIT VÉRIFIÉ · 🔵 ÉCOLE · 🟡 CONVENTION |
| Cercle dominant | **C2 (order flow ATAS)** — page PRIORITAIRE footprint/numbers bars |
| Belkhayate | NON concerné directement (le footprint C2 vient en confirmation du prix Belkhayate C1) ; POC à recouper avec pivots Belkhayate |

### Cas « à vérifier » (humain)
- **Exemple ES (Tick Size .25)** : conservé comme citation technique littérale de la source, mais ES = actif de **CONFIRMATION**, jamais tradable. Vérifier qu'aucune lecture ne le traite comme tradable. (D408)
- **Marquage Bid/Ask du flux** : la source garantit 100 % de précision pour CME/CBOT quand l'exchange marque le côté. À confirmer que le flux NTB/Rithmic transmet bien ce marquage pour GC/HG/CL/ZW (sinon fallback uptick/downtick, moins fiable). (D401)
- **Seuils d'imbalance** : valeur exemple (400 %) = configuration, non universelle ; à calibrer par actif avant usage signal. (D406)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> Fichier en `validation/` — aucune fusion master sans OK utilisateur.
