# Extraction StockCharts — Chaikin Money Flow (CMF)
**Source :** `bundles/stockcharts/chaikin_money_flow_cmf.md` (HTTP 200 · ~17 300 car.) + 11 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 11/11 certifiées
**Décisions :** D1151 → D1170 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/chaikin-money-flow-cmf
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | CMF 20 et 60 jours (multi-timeframes) | What Is Chaikin Money Flow? | CERTIFIE (accord .md + HTML) |
| image_02.png | Table 1 - Chaikin Money Flow | Calculating Chaikin Money Flow | CERTIFIE (accord .md + HTML) |
| image_03.png | Prix et valeurs CMF (exemple tableur) | Calculating Chaikin Money Flow | CERTIFIE (accord .md + HTML) |
| image_04.png | Réduire les whipsaws CMF par buffer | Zero Line Crosses | CERTIFIE (accord .md + HTML) |
| image_05.png | Trader les pullbacks avec CMF haussier | Zero Line Crosses | CERTIFIE (accord .md + HTML) |
| image_06.png | CMF inefficace en conditions volatiles/choppy | Caveat: CMF in Volatile or Choppy Conditions | CERTIFIE (accord .md + HTML) |
| image_07.png | CMF trompeur après un down gap | Caveat: CMF and Gaps | CERTIFIE (accord .md + HTML) |
| image_08.png | CMF trompeur après un up gap | Caveat: CMF and Gaps | CERTIFIE (accord .md + HTML) |
| image_09.png | Using with SharpCharts (exemple) | Using with SharpCharts [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_10.png | Réglages SharpCharts CMF | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_11.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1151 — Nature et origine du Chaikin Money Flow
🔵 **ÉCOLE (Chaikin)** (Source : chaikin_money_flow_cmf.md, image_01) : Développé par Marc Chaikin, le CMF mesure la quantité d'argent entrant dans un actif sur une période donnée. Le Money Flow Volume forme la base de l'indicateur cumulatif Accumulation Distribution Line. Le CMF somme le Money Flow Volume sur une période de look-back (typiquement 20 ou 21 jours) au lieu d'un cumul total ; le résultat oscille au-dessus/dessous de la ligne zéro comme un oscillateur.
**TRADEX-AI C2** : Oscillateur de flux monétaire (order flow / buying-selling pressure) candidat comme couche de confirmation ; jamais standalone (cf. D1165).
*Catégorie : indicateurs_momentum*

---

### D1152 — Lecture : niveau absolu + croisements de la ligne zéro
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Les chartistes pèsent la balance pression acheteuse/vendeuse via le niveau absolu du CMF. Ils peuvent aussi chercher les croisements au-dessus/dessous de la ligne zéro pour identifier les changements de flux monétaire.
**TRADEX-AI C2** : Deux lectures combinables : niveau (intensité) et croisement zéro (basculement). Features distinctes pour le moteur.
*Catégorie : signal*

---

### D1153 — Formule de calcul (Money Flow Multiplier / Volume / CMF)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_02) : Calcul en quatre étapes (exemple 20 périodes) :
```
1. Money Flow Multiplier = [(Close - Low) - (High - Close)] / (High - Low)
2. Money Flow Volume = Money Flow Multiplier x Volume de la période
3. CMF 20 périodes = Somme(20) du Money Flow Volume / Somme(20) du Volume
```
**TRADEX-AI C2** : Formule déterministe implémentable telle quelle ; nécessite un flux volume fiable (NT8/ATAS) pour GC/HG/CL/ZW. Look-back par défaut = 20.
*Catégorie : indicateurs_momentum*

---

### D1154 — Mécanique du Money Flow Multiplier (position de la clôture)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_02) : Le multiplicateur est positif quand la clôture est dans la moitié HAUTE du range high-low, négatif dans la moitié basse. Il vaut +1 quand close = high, -1 quand close = low. Il ajuste la part du volume comptée dans le Money Flow Volume : le volume est réduit sauf si le multiplicateur est à ses extrêmes (+1 ou -1).
**TRADEX-AI C2** : La position de clôture dans le range pondère le flux ; cohérent avec une lecture order flow de la pression acheteuse/vendeuse. Identique au multiplicateur de l'ADL.
*Catégorie : indicateurs_momentum*

---

### D1155 — Exemples chiffrés du multiplicateur (proche +1, -0,97, ~0)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_03) : Exemples daily : multiplicateur proche de +1 le 5-Jan (clôture près du high) ; il chute à -0,97 le 18-Jan (clôture près du low) ; il finit proche de zéro (-0,07) le 29-Dec (clôture près du milieu du range).
**TRADEX-AI C2** : Illustration chiffrée validant la mécanique D1154 ; utile comme cas-test pour vérifier une implémentation.
*Catégorie : indicateurs_momentum*

---

### D1156 — Plage de l'oscillateur (-1 à +1, typiquement ±0,50)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Le CMF oscille entre -1 et +1, mais atteint rarement ces extrêmes (il faudrait 20 clôtures consécutives sur le high/low pour qu'un CMF 20 jours atteigne +1/-1). Typiquement il fluctue entre -0,50 et +0,50, avec 0 comme ligne médiane.
**TRADEX-AI C2** : Bornes connues et plage usuelle ±0,50 → utiles pour normaliser/seuiller le signal. Centre = 0.
*Catégorie : indicateurs_momentum*

---

### D1157 — Interprétation : confirmer/questionner la tendance
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Le CMF mesure la pression acheteuse/vendeuse de la période. Un passage en territoire positif indique une pression acheteuse, en territoire négatif une pression vendeuse. La valeur absolue sert à confirmer ou questionner l'action des prix : un CMF positif confirme un uptrend, un CMF négatif remet en question la force d'un uptrend (et inversement pour les downtrends).
**TRADEX-AI C2** : Feature de cohérence flux/prix : CMF du même signe que la tendance = confirmation ; signe opposé = alerte. Combinable avec la Direction Belkhayate.
*Catégorie : divergence*

---

### D1158 — Croisements de la ligne zéro = changement de pression
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Un croisement de la ligne zéro indique un changement de pression : CMF au-dessus de zéro = pression acheteuse plus forte ; en dessous = pression vendeuse plus forte.
**TRADEX-AI C2** : Signal binaire de basculement (cross zéro) codable directement ; à filtrer contre les whipsaws (cf. D1159).
*Catégorie : signal*

---

### D1159 — Filtrage des whipsaws par buffer ±0,05
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_04) : En réalité, le CMF franchit parfois la ligne zéro de façon brève et sans suite (whipsaw / mauvais signal). On filtre via des buffers : seuil haussier un peu au-dessus de zéro (+0,05), seuil baissier un peu en dessous (-0,05). Sur Freeport McMoran (FCX), ≥ 10 croisements de zéro entre février et décembre 2010 ; le buffer ±0,05 réduit à seulement trois signaux. Ces signaux arrivent plus tard mais la réduction des whipsaws en vaut la peine.
**TRADEX-AI C2** : Buffer ±0,05 = paramètre anti-whipsaw directement implémentable ; arbitrage réactivité vs fiabilité documenté.
*Catégorie : signal*

---

### D1160 — Trader les pullbacks tant que CMF reste en mode bull
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_05) : Sur Harley-Davidson (HOG) : quelques bons signaux et un whipsaw au rebond de mai (CMF > +0,05 quelques jours puis échec, retour sous -0,05 début juin). Le CMF redevient haussier en juillet et le reste le reste de l'année. HOG forme un falling wedge retraçant un peu plus de 62 % en août pendant que le CMF est toujours en mode bull — ce pullback offre une seconde occasion de prendre le signal CMF.
**TRADEX-AI C2** : Tactique « acheter le repli tant que le flux reste positif » ; le maintien du CMF en territoire positif valide l'entrée sur pullback (recoupe la logique CCI Correction D1135-D1137).
*Catégorie : timing*

---

### D1161 — Caveat : CMF peu fiable en conditions volatiles/choppy
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_06) : Le CMF est moins fiable en périodes volatiles ou quand la tendance s'aplatit, à cause de sa sensibilité aux fluctuations de prix (whipsaws). Il n'est pas adapté à tous les titres, surtout ceux à tendance choppy. Sur P.F. Chang (PFCB), 18 croisements de +0,05/-0,05 produisent plusieurs whipsaws ; mieux vaut un autre indicateur pour ce titre.
**TRADEX-AI C2** : Garde-fou régime de marché — désactiver/dévaluer le CMF en marché choppy. À coupler à un détecteur de régime (range vs tendance).
*Catégorie : signal*

---

### D1162 — Caveat : quirk des gaps (down gap)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_07) : Le multiplicateur ne regarde que la position de la clôture dans le range high-low, pas le changement close-à-close. Un titre peut gapper À LA BAISSE et clôturer nettement plus bas, mais le multiplicateur MONTE si la clôture est au-dessus du milieu du range. Exemple Clorox (CLX) : gros gap baissier, clôture près du haut du range du jour → CMF monte malgré une clôture fortement en baisse sur gros volume. Ignorer le close-à-close peut déconnecter le CMF du prix.
**TRADEX-AI C2** : Garde-fou data critique — le CMF peut donner un signal acheteur sur une journée baissière (gap). Détecter les gaps et invalider/pondérer le signal CMF en conséquence.
*Catégorie : divergence*

---

### D1163 — Caveat : quirk des gaps (up gap)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_08) : Cas inverse : un titre gappe À LA HAUSSE et clôture près du low du jour. Exemple Travellers (TRV) : gap haussier, clôture > 1 % plus haut sur la journée mais près du low → multiplicateur proche de -1, presque tout le volume compté en flux négatif, et le CMF BAISSE malgré la hausse du jour.
**TRADEX-AI C2** : Symétrique de D1162 — signal vendeur CMF sur une journée haussière (gap). Même garde-fou gap obligatoire avant exploitation du CMF.
*Catégorie : divergence*

---

### D1164 — Divergences haussières/baissières et leur limite
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Les chartistes cherchant des changements de flux plus rapides peuvent guetter divergences haussières et baissières. Mais attention : en territoire négatif, la pression vendeuse garde l'avantage même en cas de divergence haussière ; cette divergence montre seulement MOINS de pression vendeuse. Il faut un passage en territoire positif pour indiquer une réelle pression acheteuse.
**TRADEX-AI C2** : La divergence CMF est une alerte précoce, PAS une confirmation ; exiger le franchissement de zéro (territoire positif) avant de valider un retournement haussier.
*Catégorie : divergence*

---

### D1165 — Synthèse : oscillateur de flux, jamais standalone
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Le CMF favorise les bulls quand positif, les bears quand négatif. En tant qu'oscillateur de flux monétaire, il s'utilise conjointement avec des oscillateurs de prix pur tels que MACD ou RSI. Comme tous les indicateurs, le CMF ne doit PAS être utilisé seul (stand-alone).
**TRADEX-AI C2** : Règle architecturale — CMF = couche de confirmation flux (C2), jamais critère unique ; coupler à RSI/MACD (prix, C1).
*Catégorie : signal*

---

### D1166 — Charting : format aire, placement au-dessus/dessous du prix
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_09, image_10) : Le CMF se place au-dessus ou en dessous du tracé principal. Affiché en format aire, il n'est pas adapté derrière le prix. Réglage par défaut = 20 périodes, ajustable pour augmenter/diminuer la sensibilité. On peut ajouter lignes horizontales, moyennes mobiles, ou tracer un second CMF plus long par-dessus le premier : les zones de chevauchement montrent un flux fort sur deux périodes différentes.
**TRADEX-AI C2** : Détail outil StockCharts (UI) ; valeur de référence du défaut (20). Idée exploitable : superposer deux look-backs (court + long) pour confirmer le flux multi-horizon (cf. image_01, 20/60).
*Catégorie : configuration*

---

### D1167 — StockChartsACP : ajout depuis Chart Settings, défaut 20
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md, image_11) : Dans StockChartsACP, l'indicateur s'ajoute depuis le panneau Chart Settings, positionnable au-dessus ou en dessous du prix. Par défaut il est calculé sur 20 périodes, ajustable selon les besoins.
**TRADEX-AI C2** : Détail outil (UI) ; confirme le look-back par défaut de 20. Sans impact moteur direct.
*Catégorie : configuration*

---

### D1168 — Scan : CMF positif + RSI > 50 (accumulation/achat)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Scan d'accumulation : le CMF(20) passe en territoire positif (pression acheteuse) confirmé par le RSI franchissant 50 (médiane). Base : actifs ≥ 10 $ et ≥ 100 000 de volume quotidien moyen sur 60 jours.
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [Daily CMF(20) crosses 0]
AND [Daily RSI(14,Daily Close) crosses 50]
```
**TRADEX-AI C2** : Logique « CMF > 0 ET RSI > 50 » (double confirmation flux + prix) transposable en condition Python ; syntaxe de scan propre à StockCharts (non réutilisable telle quelle).
*Catégorie : signal*

---

### D1169 — Scan : CMF négatif + RSI < 45 (distribution/vente)
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Scan de distribution : le CMF(20) passe en territoire négatif (pression vendeuse) confirmé par le RSI passant sous 50. Même base de liquidité que D1168.
```
[type = stock] AND [country = US]
AND [Daily SMA(60,Daily Volume) > 100000]
AND [Daily SMA(60,Daily Close) > 10]
AND [0 crosses Daily CMF(20)]
AND [50 crosses Daily RSI(14,Daily Close)]
```
**TRADEX-AI C2** : Symétrique baissier de D1168 (NB : le texte annonce « RSI < 45 » mais la syntaxe du scan teste le franchissement de 50 ; voir À vérifier). Double confirmation flux + prix.
*Catégorie : signal*

---

### D1170 — Garde-fou : volume intraday incomplet pour le scanning
🟢 **FAIT VÉRIFIÉ** (Source : chaikin_money_flow_cmf.md) : Pour le scanning, les données de volume quotidiennes sont incomplètes en séance. Avec les indicateurs volume comme le CMF, baser le scan sur la dernière clôture de marché (« Last Market Close »). Autres indicateurs volume concernés : Accumulation/Distribution, On Balance Volume, PVO.
**TRADEX-AI C2** : Garde-fou data cohérent avec staleness_monitor — ne pas signaler sur volume non clos. À intégrer si calcul sur barres journalières.
*Catégorie : timing*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1151 | Nature et origine CMF | 🔵 ÉCOLE | C2 | indicateurs_momentum |
| D1152 | Lecture niveau + cross zéro | 🟢 | C2 | signal |
| D1153 | Formule de calcul (3 étapes) | 🟢 | C2 | indicateurs_momentum |
| D1154 | Mécanique du Money Flow Multiplier | 🟢 | C2 | indicateurs_momentum |
| D1155 | Exemples chiffrés du multiplicateur | 🟢 | C2 | indicateurs_momentum |
| D1156 | Plage -1/+1, usuel ±0,50 | 🟢 | C2 | indicateurs_momentum |
| D1157 | Confirmer/questionner la tendance | 🟢 | C2 | divergence |
| D1158 | Croisements ligne zéro | 🟢 | C2 | signal |
| D1159 | Buffer ±0,05 anti-whipsaw | 🟢 | C2 | signal |
| D1160 | Trader les pullbacks en mode bull | 🟢 | C2 | timing |
| D1161 | Caveat conditions volatiles/choppy | 🟢 | C2 | signal |
| D1162 | Caveat down gap | 🟢 | C2 | divergence |
| D1163 | Caveat up gap | 🟢 | C2 | divergence |
| D1164 | Divergences et leur limite | 🟢 | C2 | divergence |
| D1165 | Synthèse — jamais standalone | 🟢 | C2 | signal |
| D1166 | Charting SharpCharts (format aire) | 🟢 | C2 | configuration |
| D1167 | StockChartsACP / défaut 20 | 🟢 | C2 | configuration |
| D1168 | Scan CMF+ / RSI>50 | 🟢 | C2 | signal |
| D1169 | Scan CMF- / RSI<45 (vs syntaxe 50) | 🟢 | C2 | signal |
| D1170 | Garde-fou volume intraday incomplet | 🟢 | C2 | timing |

**Liens Belkhayate :** le Chaikin Money Flow n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé par Belkhayate) : le CMF est un oscillateur de flux monétaire (buying/selling pressure) dont l'esprit recoupe l'« Énergie » Belkhayate ; or la mémoire projet établit que l'Énergie Belkhayate = MFI standard (Money Flow Index, seuils 20/80), un indicateur DIFFÉRENT du CMF (formules et bornes distinctes : CMF ∈ [-1;+1] centré sur 0 vs MFI ∈ [0;100]). Ne PAS assimiler CMF et MFI. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D1169 — incohérence interne de la source : le titre/texte annonce « RSI < 45 » mais le code du scan teste `[50 crosses Daily RSI(14,...)]` (donc 50, pas 45). Trancher le seuil exact avant tout codage.
- D1159 / D1168 / D1169 — buffer ±0,05 et seuils de scan calibrés sur actions liquides ; à revalider (walk-forward) sur GC/HG/CL/ZW.
- D1162 / D1163 — le quirk des gaps est critique pour le trading temps réel (un signal CMF peut contredire le sens du jour) : un filtre gap est requis avant d'utiliser le CMF dans le moteur.
- D1151 vs Énergie Belkhayate — ne pas confondre CMF et MFI (cf. Liens Belkhayate) ; confirmation humaine nécessaire.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
