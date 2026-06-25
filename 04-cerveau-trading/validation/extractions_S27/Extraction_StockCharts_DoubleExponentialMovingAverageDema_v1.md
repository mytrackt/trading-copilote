# Extraction StockCharts — Double Exponential Moving Average (DEMA)
**Source :** `bundles/stockcharts/double_exponential_moving_average_dema.md` (HTTP 200 · ~5 100 car.) + 3 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D1551 → D1561 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/double-exponential-moving-average-dema
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Double Exponential Moving Average (DEMA) Indicator? | What Is the DEMA Indicator? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart with the Double Exponential Moving Average | Interpreting DEMA | CERTIFIE (accord .md + HTML) |
| image_03.png | StockChartsACP Chart showing DEMA Overlay | Charting with DEMA | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1551 — Nature et objet du DEMA (réduction du lag)
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md, image_01) : La Double Exponential Moving Average (DEMA) est un indicateur technique qui réduit le retard (lag) des EMA traditionnelles, la rendant plus réactive. Elle utilise la différence de lag entre une EMA simplement lissée et une EMA doublement lissée pour décaler l'EMA simplement lissée, produisant une moyenne mobile qui reste plus proche des barres de prix que les EMA traditionnelles.
**TRADEX-AI C1** : Overlay de tendance à lag réduit. À traiter comme moyenne mobile réactive (suivi de tendance), pas comme déclencheur d'entrée autonome.
*Catégorie : indicateurs_tendance*

---

### D1552 — Origine (Patrick Mulloy, 1994)
🔵 **ÉCOLE (Patrick Mulloy)** (Source : double_exponential_moving_average_dema.md) : La DEMA a été développée par Patrick Mulloy et introduite dans le numéro de janvier 1994 du magazine *Technical Analysis of Stocks & Commodities*.
**TRADEX-AI C1** : Attribution/origine documentée. Contexte historique, sans implication directe sur le moteur.
*Catégorie : indicateurs_tendance*

---

### D1553 — Principe : compensation du lag par décalage
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : L'overlay utilise la différence de lag entre une EMA simplement lissée et une EMA doublement lissée pour décaler l'EMA simplement lissée. Ce décalage produit une moyenne mobile qui reste lisse mais plus proche des barres de prix que l'EMA simple ou double traditionnelle.
**TRADEX-AI C1** : Précision de conception : la DEMA n'est pas une double EMA naïve mais une correction de lag par soustraction. Nécessaire pour coder correctement la formule (D1554).
*Catégorie : indicateurs_tendance*

---

### D1554 — Formule de calcul du DEMA
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : La formule prend la différence de lag entre l'EMA simplement lissée (EMA1, un peu en retard) et l'EMA doublement lissée (EMA2, encore plus en retard), puis soustrait cette différence d'EMA1, produisant une ligne lissée bien plus proche des barres de prix qu'EMA1 ou EMA2.
```
EMA1 = EMA du prix
EMA2 = EMA de l'EMA1
DEMA = (2 x EMA1) - EMA2
```
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; nécessite deux EMA chaînées. Directement codable.
*Catégorie : indicateurs_tendance*

---

### D1555 — Interprétation : confirmer/repérer un changement de tendance
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : La DEMA s'interprète de façon similaire aux EMA traditionnelles, mais réagit plus rapidement. Comme les autres EMA, elle sert à confirmer une tendance ou à repérer un changement de tendance.
**TRADEX-AI C1** : Usage = confirmation/détection de tendance (plus réactive). À combiner avec d'autres outils, jamais isolément.
*Catégorie : indicateurs_tendance*

---

### D1556 — Signal le plus courant : le croisement DEMA
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : Le signal le plus couramment utilisé est le croisement DEMA. Surveiller la ligne DEMA croisant les barres de prix, ou une DEMA court terme croisant une DEMA long terme, pour indiquer un changement de tendance. Exemple : la DEMA 20 jours croisant au-dessus de la DEMA 50 jours serait un signal haussier.
**TRADEX-AI C1** : Logique de croisement (prix×DEMA ou DEMA courte×DEMA longue) transposable en condition Python. Ex. haussier : DEMA(20) > DEMA(50). À traiter comme signal de tendance, à confirmer par le reste du score.
*Catégorie : signal*

---

### D1557 — Avance temporelle du croisement DEMA vs EMA
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md, image_02) : Les croisements DEMA (de prix ou d'une autre DEMA) se produisent typiquement bien plus tôt que le croisement EMA traditionnel correspondant. Sur l'exemple, les flèches vertes marquent les croisements DEMA et les flèches bleues les croisements EMA correspondants : dans les deux cas, le croisement DEMA précède le croisement EMA.
**TRADEX-AI C1** : Avantage = signal plus précoce, mais contrepartie implicite = plus de bruit/faux signaux possibles (réactivité accrue). À pondérer dans le score.
*Catégorie : signal*

---

### D1558 — Adapter les stratégies à la réactivité accrue
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : Parce que la DEMA réagit plus vite que les EMA traditionnelles, il peut être nécessaire d'ajuster ses stratégies de trading pour l'utiliser.
**TRADEX-AI C1** : Avertissement : la réactivité impose une recalibration des règles (seuils, filtres). À ne pas substituer aux EMA sans réajustement.
*Catégorie : configuration*

---

### D1559 — Synthèse : pour qui et avec quelles limites
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : Les croisements de prix et autres signaux surviennent généralement plus tôt avec la DEMA qu'avec les EMA traditionnelles. Le lag réduit et la réactivité accrue séduisent les investisseurs court terme, mais les investisseurs long terme peuvent trouver les moyennes mobiles traditionnelles plus utiles. Comme tout indicateur technique, la DEMA doit s'utiliser avec d'autres indicateurs et techniques d'analyse.
**TRADEX-AI C1** : Cadre d'emploi : DEMA = court terme (cohérent avec timeframes rapides du projet : Range Bars / 15 s). Toujours combiner à d'autres signaux. Jamais seule.
*Catégorie : indicateurs_tendance*

---

### D1560 — Paramétrage et disponibilité (ACP, défaut 20 périodes)
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md, image_03) : L'overlay DEMA se trace sur StockChartsACP après installation du Advanced Indicator Pack gratuit ; il s'ajoute depuis le panneau Chart Settings et peut être superposé au tracé du prix ou sur un panneau d'indicateur. Par défaut, la moyenne mobile est calculée sur 20 périodes, ajustable selon les besoins.
**TRADEX-AI C1** : Référence de paramétrage (défaut 20 périodes). Détail plateforme ; seul le paramètre période importe pour le moteur.
*Catégorie : configuration*

---

### D1561 — Scans croisement DEMA haussier/baissier (5/35 + filtre tendance/volume)
🟢 **FAIT VÉRIFIÉ** (Source : double_exponential_moving_average_dema.md) : Scan haussier : SMA 150 jours en hausse (au-dessus de sa valeur d'il y a 5 jours) ET croisement haussier DEMA(5) au-dessus de DEMA(35) sur volume au-dessus de la moyenne. Scan baissier : SMA 150 jours en baisse ET DEMA(5) sous DEMA(35) sur volume au-dessus de la moyenne.
```
[type = stock] AND [country = US]
AND [SMA(20,Volume) > 40000]
AND [SMA(60,Close) > 20]
AND [SMA(150,Close) > 5 days ago SMA(150,Close)]   # haussier (< pour baissier)
AND [DEMA(5,Close) > DEMA(35,Close)]               # < pour baissier
AND [Yesterday's DEMA(5,Close) < Yesterday's DEMA(35,Close)]  # > pour baissier
AND [Volume > SMA(200,Volume)]
```
**TRADEX-AI C1** : Logique transposable : croisement DEMA(5)/DEMA(35) FILTRÉ par tendance de fond (SMA 150 montante/descendante) et par volume en expansion. La syntaxe StockCharts n'est pas réutilisable telle quelle, mais le triple filtre (croisement + tendance + volume) l'est.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1551 | Nature DEMA (réduction du lag) | 🟢 | C1 | indicateurs_tendance |
| D1552 | Origine (Mulloy, 1994) | 🔵 ÉCOLE | C1 | indicateurs_tendance |
| D1553 | Principe (compensation du lag) | 🟢 | C1 | indicateurs_tendance |
| D1554 | Formule (2×EMA1 − EMA2) | 🟢 | C1 | indicateurs_tendance |
| D1555 | Interprétation (confirmer/repérer tendance) | 🟢 | C1 | indicateurs_tendance |
| D1556 | Croisement DEMA (signal principal) | 🟢 | C1 | signal |
| D1557 | Croisement DEMA précède EMA | 🟢 | C1 | signal |
| D1558 | Adapter stratégies à la réactivité | 🟢 | C1 | configuration |
| D1559 | Synthèse (court terme + combiner) | 🟢 | C1 | indicateurs_tendance |
| D1560 | Paramétrage ACP (défaut 20) | 🟢 | C1 | configuration |
| D1561 | Scans croisement 5/35 + filtres | 🟢 | C1 | signal |

**Liens Belkhayate :** la DEMA n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué. Pertinence projet **modérée** : moyenne mobile à lag réduit, adaptée aux timeframes rapides du projet (Range Bars / 15 s pour le pétrole), avec formule déterministe et logique de croisement transposables (C1), en complément — non substitution — des règles Belkhayate (Pivots/BGC/Direction/Énergie). Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D1554 — la formule nécessite de fixer la période de l'EMA (non précisée dans la formule générique) ; défaut 20 (cf. D1560) à recaler par actif et par timeframe.
- D1556 / D1557 / D1561 — la réactivité accrue augmente le risque de faux croisements (whipsaws) : tout signal de croisement DEMA doit être filtré (tendance de fond + volume, cf. D1561) avant d'entrer dans le score /10.
- D1561 — paramètres 5/35/150 conçus pour barres journalières actions ; à recalibrer pour futures GC/HG/CL/ZW en Range Bars / 15 min / 15 s ; syntaxe de scan non réutilisable telle quelle.
- Cohérence projet : valider que l'ajout d'une moyenne mobile réactive ne crée pas de redondance/conflit avec les MA déjà figées côté Belkhayate avant fusion.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
