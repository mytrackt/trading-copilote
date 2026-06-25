# Extraction StockCharts — Detrended Price Oscillator (DPO)
**Source :** `bundles/stockcharts/detrended_price_oscillator_dpo.md` (HTTP 200 · ~6 200 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D1491 → D1501 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/detrended-price-oscillator-dpo
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 | Displaced Moving Average | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 | What Does DPO Measure? | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 | Using DPO | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 | To Shift or Not to Shift | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 5 | To Shift or Not to Shift | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 6 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D1491 — Nature et objet du DPO
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md) : Le Detrended Price Oscillator (DPO) est un indicateur conçu pour retirer la tendance du prix afin de faciliter l'identification des cycles. Le DPO ne s'étend pas jusqu'à la date la plus récente car il repose sur une moyenne mobile décalée. L'alignement avec la date la plus récente n'est toutefois pas un problème car le DPO n'est PAS un oscillateur de momentum : il sert à identifier les sommets/creux de cycle et à estimer la longueur d'un cycle.
**TRADEX-AI C1** : Outil d'identification de **cycles** (timing), pas de momentum. À traiter comme estimateur de périodicité, jamais comme déclencheur d'entrée directionnel.
*Catégorie : timing*

---

### D1492 — Formule de calcul du DPO
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md) : Le DPO se calcule comme le prix d'il y a {X/2 + 1} périodes moins la moyenne mobile simple à X périodes. X est le nombre de périodes du DPO. Un DPO 20 jours utilise une SMA 20 jours décalée de 11 périodes {20/2 + 1 = 11} ; ce décalage déplace la SMA 20 jours de 11 jours vers la gauche, la plaçant au milieu de la fenêtre de calcul. En résumé, DPO(20) = prix d'il y a 11 jours moins la SMA 20 jours.
```
DPO(X) = Prix il y a {X/2 + 1} périodes - SMA(X)
DPO(20) = Prix il y a 11 jours - SMA(20)
```
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; nécessite une SMA(X) et un accès au prix décalé de {X/2 + 1} périodes. Paramètre par défaut X=20.
*Catégorie : indicateurs_tendance*

---

### D1493 — Moyenne mobile décalée (centrage)
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_01) : Le décalage de la moyenne mobile la centre en réalité. Une SMA 20 jours décalée de 11 jours vers la gauche a 10 jours devant, 1 jour à la moyenne, 9 jours derrière : elle se trouve au milieu de sa fenêtre de calcul, environ moitié des prix à droite et moitié à gauche. Sur l'exemple SPY, la SMA 20 jours (vert pointillé) et la SMA 20 jours décalée de 11 jours (rose) ont la même valeur finale (106,84) mais la rose se termine le 27 octobre et la verte le 11 novembre (dernière date du graphique) ; la moyenne « centrée » (rose) suit de plus près le tracé réel du prix.
**TRADEX-AI C1** : Le décalage est un centrage de la SMA, pas une projection prédictive. Précision technique pour coder correctement l'offset (vers la gauche).
*Catégorie : indicateurs_tendance*

---

### D1494 — Ce que mesure le DPO (au-dessus/en dessous de zéro)
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_02) : Le DPO mesure la différence entre un prix passé et une moyenne mobile. Le DPO est lui-même décalé vers la gauche. L'indicateur oscille au-dessus/en dessous de zéro à mesure que les prix passent au-dessus/en dessous de la moyenne mobile décalée : le DPO est positif quand le prix est au-dessus de la moyenne mobile décalée et négatif quand le prix est en dessous.
**TRADEX-AI C1** : Lecture binaire au-dessus/en dessous de zéro = position relative du prix vs sa SMA centrée. Information de structure, à interpréter en lecture de cycle, pas en signal d'achat/vente.
*Catégorie : indicateurs_tendance*

---

### D1495 — Usage du DPO : estimer la longueur d'un cycle
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_03) : Bien qu'il ressemble à un oscillateur classique, le DPO n'est PAS conçu pour des signaux de momentum (la moyenne mobile décalée est placée dans le passé, d'où l'affichage du DPO dans le passé). Malgré ce décalage, les sommets et creux du DPO servent à estimer la longueur d'un cycle ; le DPO filtre les tendances plus longues pour se concentrer sur les cycles plus courts. Exemple : un DPO(20) montre un cycle de 20 jours avec des creux début septembre, octobre, novembre, décembre (≈ 20 jours d'écart), le cycle ayant été manqué début janvier.
**TRADEX-AI C1** : Compter les périodes entre creux/sommets du DPO = mesure de périodicité du marché → utile pour caler une fenêtre temporelle d'analyse. Pas un signal d'entrée.
*Catégorie : timing*

---

### D1496 — Décaler ou non (« To Shift or Not to Shift »)
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_04) : Il est possible de décaler le DPO horizontalement vers la droite. Si le DPO est réglé à 20, un décalage de 11 périodes est nécessaire pour l'aligner sur le prix le plus récent (11 vient de la formule 20/2 + 1). Mais ce décalage, bien que séduisant, va à l'encontre de l'objectif de l'indicateur, qui est d'identifier les cycles.
**TRADEX-AI C1** : Garde-fou de conception : ne pas « réaligner » le DPO sur le présent si l'objectif est l'analyse de cycles. Choix de paramétrage à documenter.
*Catégorie : configuration*

---

### D1497 — Le DPO décalé ne correspond pas à l'action de prix courante
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_05) : Même avec un décalage positif, les fluctuations du DPO ne collent pas bien aux prix. La dernière valeur de DPO(20,11) reste basée sur la clôture d'il y a 11 jours et la valeur de la moyenne mobile : le DPO est devenu négatif quand le prix est passé sous la moyenne centrée il y a 11 jours, sans correspondre à l'action de prix courante.
**TRADEX-AI C1** : Avertissement explicite : un DPO décalé NE reflète PAS le surachat/survente courant. Ne pas l'utiliser comme tel dans le moteur.
*Catégorie : indicateurs_tendance*

---

### D1498 — DPO inadapté au surachat/survente : préférer le PPO
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_05) : Le Percentage Price Oscillator (PPO) est mieux adapté pour identifier les niveaux de surachat/survente. PPO(1,20,1) montre la différence en pourcentage entre le prix courant et la moyenne mobile exponentielle 20 jours normale ; les conditions de surachat/survente surviennent quand les prix s'éloignent relativement de leur EMA 20 jours.
**TRADEX-AI C1** : Si l'objectif est le surachat/survente (momentum), router vers PPO et non DPO. Aiguillage d'indicateur à respecter dans l'architecture C1.
*Catégorie : indicateurs_momentum*

---

### D1499 — Synthèse : DPO = outil de cycle, pas de momentum
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md) : Le DPO montre la différence entre un prix passé et une SMA. Contrairement aux autres oscillateurs de prix, ce n'est pas un indicateur de momentum : il sert simplement à identifier des cycles via ses sommets et creux. Les cycles s'estiment en comptant les périodes entre sommets ou creux. L'utilisateur peut expérimenter des réglages DPO plus courts ou plus longs pour trouver le meilleur ajustement.
**TRADEX-AI C1** : Confirme l'usage unique (cycle). Paramètre X ajustable empiriquement pour caler la périodicité dominante d'un actif.
*Catégorie : timing*

---

### D1500 — Paramétrage SharpCharts (défaut 20, décalage par virgule)
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md, image_06) : Le DPO se trouve dans la liste d'indicateurs de SharpCharts. Paramètre par défaut 20 périodes, ajustable pour trouver les cycles. On peut ajouter un second paramètre séparé par une virgule : une virgule plus un nombre positif décale l'indicateur vers la droite. Le DPO peut se positionner au-dessus, en dessous ou derrière le tracé du prix.
**TRADEX-AI C1** : Référence de paramétrage (défaut 20, option décalage). Détail UI ; seul X=20 et l'offset {X/2+1} importent pour le moteur.
*Catégorie : configuration*

---

### D1501 — DPO peu adapté aux scans (offset + niveaux absolus)
🟢 **FAIT VÉRIFIÉ** (Source : detrended_price_oscillator_dpo.md) : Le DPO est peu adapté aux scans car il repose sur une moyenne mobile décalée (un DPO 20 jours correspond à un prix d'il y a 11 jours, peu pratique pour un scan) et sur des niveaux absolus, ce qui le rend difficile à utiliser à des fins comparatives : une action à 100 $ aura une plage de DPO bien plus large qu'une action à 20 $ (exemple Google ~590 $ avec DPO ~21 vs Intel ~20,5 $ avec DPO ~0,20).
**TRADEX-AI C1** : Limite importante : DPO non comparable entre actifs (échelle absolue dépendant du prix). Pour comparer GC/HG/CL/ZW, normaliser ou préférer un oscillateur en pourcentage.
*Catégorie : configuration*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1491 | Nature et objet du DPO (cycle, pas momentum) | 🟢 | C1 | timing |
| D1492 | Formule DPO {X/2+1} - SMA(X) | 🟢 | C1 | indicateurs_tendance |
| D1493 | Moyenne mobile décalée (centrage) | 🟢 | C1 | indicateurs_tendance |
| D1494 | Mesure (au-dessus/en dessous de zéro) | 🟢 | C1 | indicateurs_tendance |
| D1495 | Estimer la longueur d'un cycle | 🟢 | C1 | timing |
| D1496 | Décaler ou non (objectif cycle) | 🟢 | C1 | configuration |
| D1497 | DPO décalé ≠ action de prix courante | 🟢 | C1 | indicateurs_tendance |
| D1498 | Surachat/survente → préférer PPO | 🟢 | C1 | indicateurs_momentum |
| D1499 | Synthèse (outil de cycle) | 🟢 | C1 | timing |
| D1500 | Paramétrage SharpCharts (défaut 20) | 🟢 | C1 | configuration |
| D1501 | Peu adapté aux scans (niveaux absolus) | 🟢 | C1 | configuration |

**Liens Belkhayate :** le DPO n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué. Pertinence projet **indirecte** : outil d'estimation de cycles (timing) pouvant aider à caler une fenêtre temporelle, sans se substituer aux Pivots/BGC/Direction/Énergie Belkhayate. Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D1492 / D1500 — réglage X=20 conçu pour barres journalières actions ; sur futures GC/HG/CL/ZW en Range Bars ou 15 min / 15 s, X doit être recalé empiriquement sur la périodicité observée (cf. D1495/D1499).
- D1497 / D1498 — ne JAMAIS utiliser le DPO comme indicateur de surachat/survente ; router vers un oscillateur en pourcentage (PPO) si besoin de momentum.
- D1501 — DPO non comparable entre actifs à prix différents : prévoir une normalisation avant toute lecture inter-marché (C7).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
