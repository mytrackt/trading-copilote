# Extraction StockCharts — Bollinger BandWidth
**Source :** `bundles/stockcharts/bollinger_bandwidth.md` (HTTP 200 · ~6 900 car.) + 10 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 10/10 certifiées
**Décisions :** D931 → D944 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/bollinger-bandwidth
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart of Bollinger Bands, BandWidth, and Standard Deviation. | SharpCharts Bollinger BandWidth Calculation | CERTIFIE (accord .md + HTML) |
| image_02.png | Spreadsheet calculating BandWidth. | SharpCharts Bollinger BandWidth Calculation | CERTIFIE (accord .md + HTML) |
| image_03.png | BB Bandwidth applied to XLK. | Defining Narrowness | CERTIFIE (accord .md + HTML) |
| image_04.png | BB BandWidth applied to XLU. | Defining Narrowness | CERTIFIE (accord .md + HTML) |
| image_05.png | Bollinger BandWidth applied to Alaska Airlines. | Signal: The Squeeze | CERTIFIE (accord .md + HTML) |
| image_06.png | Bollinger Bandwidth applied to Aerospotale. | Signal: The Squeeze | CERTIFIE (accord .md + HTML) |
| image_07.png | Chart 6 | Signal: The Squeeze | CERTIFIE (accord .md + HTML) |
| image_08.png | Chart 7 | Signal: The Squeeze | CERTIFIE (accord .md + HTML) |
| image_09.png | Chart 8 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_10.png | Comparing BandWidths for stocks in the S&P 500 sectors. | Using with MarketCarpets | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D931 — Nature et origine du Bollinger BandWidth
🔵 **ÉCOLE (Bollinger)** (Source : bollinger_bandwidth.md) : Le Bollinger BandWidth est un indicateur dérivé des Bollinger Bands. Dans son livre *Bollinger on Bollinger Bands*, John Bollinger le présente comme l'un des deux indicateurs dérivables des Bollinger Bands (l'autre étant %B). Une Bollinger Band se compose d'une bande médiane (moyenne mobile simple, généralement 20 périodes) et de deux bandes externes (généralement à deux écarts-types au-dessus/dessous de la médiane).
**TRADEX-AI C1** : Indicateur de volatilité candidat pour qualifier l'état de compression/expansion de GC/HG/CL/ZW ; couche analytique, jamais déclencheur d'ordre.
*Catégorie : indicateurs_tendance*

---

### D932 — Définition : BandWidth mesure la volatilité relative
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md) : Le BandWidth mesure la différence en pourcentage entre la bande supérieure et la bande inférieure. Le BandWidth diminue quand les bandes se resserrent et augmente quand elles s'écartent. Comme les Bollinger Bands reposent sur l'écart-type, un BandWidth en baisse reflète une volatilité décroissante et un BandWidth en hausse reflète une volatilité croissante.
**TRADEX-AI C1** : Feature continue de volatilité ; corrélée à l'écart-type, utilisable pour détecter régimes de marché (calme/agité).
*Catégorie : indicateurs_tendance*

---

### D933 — Formule de calcul SharpCharts
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_01, image_02) : Formule déterministe :
```
( (Upper Band - Lower Band) / Middle Band) * 100
```
On soustrait d'abord la bande inférieure de la bande supérieure (différence absolue), puis on divise par la bande médiane pour normaliser. Ce BandWidth normalisé est alors comparable entre différents timeframes ou entre titres.
**TRADEX-AI C1** : Formule implémentable telle quelle ; sortie normalisée (%) comparable inter-actifs et inter-timeframes.
*Catégorie : indicateurs_tendance*

---

### D934 — Corrélation BandWidth / écart-type (volatilité)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_01) : Le BandWidth suit l'écart-type (volatilité) : les deux montent et descendent ensemble. Illustré sur le Nasdaq 100 ETF (QQQ) avec Bollinger Bands, BandWidth et écart-type.
**TRADEX-AI C1** : Confirme que BandWidth est un proxy direct de volatilité ; redondant avec une mesure d'écart-type déjà disponible.
*Catégorie : indicateurs_tendance*

---

### D935 — Définir la « étroitesse » (narrowness) est relatif
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md) : L'étroitesse du BandWidth est relative et doit être jaugée par rapport aux valeurs antérieures de BandWidth sur une période. Un graphique de 8 à 12 mois permet de définir la plage de BandWidth (hauts/bas) pour un titre donné. Le BandWidth est « étroit » quand il approche les bas de cette plage, « large » quand il approche le haut.
**TRADEX-AI C1** : Imposer un look-back (8-12 mois) pour normaliser le seuil « squeeze » par actif ; pas de seuil absolu universel.
*Catégorie : structure_marche*

---

### D936 — BandWidth dépend de la volatilité intrinsèque du titre
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_03, image_04) : Les titres à faible volatilité ont des BandWidth plus bas que les titres à forte volatilité. Exemple : Utilities SPDR (XLU, faible volatilité) a une MM200 de BandWidth sous 5, tandis que Technology SPDR (XLK, forte volatilité) a une MM200 de BandWidth au-dessus de 7.
**TRADEX-AI C7** : Tout seuil de squeeze doit être calibré par actif (GC vs CL vs ZW ont des volatilités différentes) ; comparaison inter-marché nécessite normalisation.
*Catégorie : structure_marche*

---

### D937 — Signal principal : « The Squeeze »
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md) : Le BandWidth est surtout connu pour identifier **The Squeeze** : la volatilité chute à un bas niveau, matérialisé par des bandes qui se resserrent. La théorie : les périodes de basse volatilité sont suivies de périodes de haute volatilité. Un BandWidth relativement étroit (le Squeeze) peut préfigurer une avance ou un déclin significatif. Après un Squeeze, une poussée du prix et une cassure de bande signalent le début d'un nouveau mouvement.
**TRADEX-AI C1** : Détecteur de compression de volatilité ; alerte de mouvement imminent, mais ne donne PAS la direction (voir D938).
*Catégorie : signal*

---

### D938 — Direction donnée par la cassure de bande, pas par le Squeeze
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md) : Une nouvelle avance démarre par un Squeeze suivi d'une cassure au-dessus de la bande supérieure. Un nouveau déclin démarre par un Squeeze suivi d'une cassure sous la bande inférieure. Le Squeeze seul est neutre directionnellement ; c'est la cassure ultérieure qui donne la direction.
**TRADEX-AI C1** : Machine à états en 2 temps : (1) détecter squeeze, (2) attendre cassure bande haute/basse pour direction ; ne jamais inférer la direction du squeeze seul.
*Catégorie : configuration*

---

### D939 — Exemple ALK : seuil 10 (= 10% de la médiane)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_05) : Sur Alaska Airlines (ALK), un Squeeze mi-juin : le BandWidth passe sous 10, déclenchant le Squeeze. 10 signifie 10% (la largeur des bandes = 10% de la médiane). Bien que ce niveau paraisse élevé, il était en réalité très bas pour ALK (titre à 15-16$, BandWidth < 10%, plus bas niveau en plus d'un an). La poussée ultérieure au-dessus de la bande supérieure a déclenché une avance prolongée.
**TRADEX-AI C1** : Confirme que le seuil de squeeze est relatif au titre (10% bas pour ALK) ; calibrer par actif via look-back.
*Catégorie : signal*

---

### D940 — Exemple ARO : seuil 8 et squeezes haussier puis baissier
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_06) : Sur Aeropostale (ARO), une ligne horizontale à 8 marque un niveau bas relatif selon la plage historique. Le BandWidth alerte mi-août d'un mouvement à venir ; le titre franchit la bande supérieure (avance jusqu'en septembre). L'avance cale fin septembre, le BandWidth se resserre à nouveau en octobre sous les bas d'août puis s'aplatit ; la cassure sous la bande inférieure déclenche un signal baissier fin octobre.
**TRADEX-AI C1** : Illustration qu'un même actif enchaîne squeezes haussiers et baissiers ; la direction vient toujours de la cassure.
*Catégorie : configuration*

---

### D941 — Application multi-timeframe (hebdo / long terme)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_07, image_08) : Le Squeeze s'applique aussi aux graphiques hebdomadaires ou plus longs. La volatilité et le BandWidth sont typiquement plus élevés en hebdomadaire qu'en journalier (mouvements plus amples attendus sur des horizons plus longs). Exemple Barrick Gold (ABX) : consolidation 2006-2007 en triangle, BandWidth sous 10 en janvier 2007, signal haussier à la cassure de juillet 2007. Exemple Honeywell (HON) : range 50-55$, cassure baissière sous la bande inférieure en juin 2007.
**TRADEX-AI C1** : Seuil de squeeze à recalibrer par timeframe (15min / Range Bar / hebdo) ; BandWidth hebdo structurellement plus haut que daily.
*Catégorie : configuration*

---

### D942 — Synthèse opératoire (The Bottom Line) et avertissement fiabilité
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md) : Le BandWidth identifie les périodes de basse/haute volatilité, donnant un aperçu des mouvements potentiels. Le Squeeze (BandWidth historiquement bas) suggère un mouvement significatif imminent ; on surveille ensuite une cassure au-dessus (tendance haussière) ou en-dessous (tendance baissière). Avertissement explicite : les signaux doivent être abordés avec prudence, car les cassures initiales peuvent échouer et tous les signaux ne sont pas fiables.
**TRADEX-AI C1** : Intégrer un garde-fou anti-faux-signal ; BandWidth = alerte de régime, jamais un ordre seul.
*Catégorie : signal*

---

### D943 — Paramètres par défaut SharpCharts (20,2)
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_09) : Les paramètres par défaut sont (20,2), basés sur les défauts des Bollinger Bands : 20 = moyenne mobile simple, 2 = nombre d'écarts-types pour les bandes supérieure/inférieure. Le BandWidth peut être positionné au-dessus, en-dessous ou derrière le tracé du prix.
**TRADEX-AI C1** : Paramètres (20,2) implémentables par défaut ; à reparamétrer selon le timeframe Belkhayate (15min / Range Bar).
*Catégorie : indicateurs_tendance*

---

### D944 — Scan suggéré « Bollinger Band Breakout » et comparaison MarketCarpet
🟢 **FAIT VÉRIFIÉ** (Source : bollinger_bandwidth.md, image_10) : Scan StockCharts repérant les titres dont les Bollinger Bands viennent de s'élargir rapidement après 5 jours ou plus de contraction :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily BB Width(20,2) > Yesterday's max(5, BB Width(20,2)) * 2]
```
Le MarketCarpet permet de comparer le BandWidth normalisé de plusieurs titres (vert foncé = large, plus clair = étroit).
**TRADEX-AI C1** : Logique « BandWidth aujourd'hui > 2× le max des 5 derniers jours = expansion » transposable en condition Python ; syntaxe de scan propre à StockCharts (non réutilisable telle quelle), seule la logique compte.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D931 | Nature et origine BandWidth | 🔵 ÉCOLE | C1 | indicateurs_tendance |
| D932 | BandWidth = volatilité relative | 🟢 | C1 | indicateurs_tendance |
| D933 | Formule de calcul SharpCharts | 🟢 | C1 | indicateurs_tendance |
| D934 | Corrélation BandWidth / écart-type | 🟢 | C1 | indicateurs_tendance |
| D935 | « Étroitesse » relative (look-back 8-12 mois) | 🟢 | C1 | structure_marche |
| D936 | Dépend de la volatilité du titre | 🟢 | C7 | structure_marche |
| D937 | Signal principal : The Squeeze | 🟢 | C1 | signal |
| D938 | Direction via cassure, pas le squeeze | 🟢 | C1 | configuration |
| D939 | Exemple ALK / seuil 10 = 10% | 🟢 | C1 | signal |
| D940 | Exemple ARO / seuil 8 / squeezes | 🟢 | C1 | configuration |
| D941 | Application multi-timeframe | 🟢 | C1 | configuration |
| D942 | Synthèse + avertissement fiabilité | 🟢 | C1 | signal |
| D943 | Paramètres défaut (20,2) | 🟢 | C1 | indicateurs_tendance |
| D944 | Scan breakout / MarketCarpet | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** Le Bollinger BandWidth n'est PAS un indicateur Belkhayate (⚫). Lien indirect possible : son rôle de détecteur de compression/expansion de volatilité recoupe la logique « ne pas trader en range / attendre l'expansion » et peut servir de filtre de cohérence amont, sans jamais s'y substituer.

**À vérifier (humain) :**
- D936 — valeurs MM200 (XLU < 5 / XLK > 7) propres à des ETF actions US ; aucun seuil futures GC/HG/CL/ZW n'en découle directement (calibration empirique requise).
- D944 — la syntaxe de scan est propre à StockCharts ; seule la **logique** (expansion = BandWidth > 2× max des 5 jours) est transposable, pas le code.
- D939/D940 — les seuils numériques (10, 8) sont des exemples relatifs à des actions précises, NON des seuils universels ; ne pas coder en dur sans recalibration par actif.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
