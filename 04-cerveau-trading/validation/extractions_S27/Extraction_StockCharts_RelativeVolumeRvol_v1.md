# Extraction StockCharts — Relative Volume (RVOL)
**Source :** `bundles/stockcharts/relative_volume_rvol.md` (HTTP 200 · ~13 500 car.) + 4 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D3411 → D3430 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-volume-rvol
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What Is the Relative Volume (RVOL) Indicator? | What Is the Relative Volume (RVOL) Indicator? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | Relative Volume Indicator (RVOL) applied to StockChartsACP | Relative Volume (RVOL) | CERTIFIE (accord .md + HTML) |
| image_03.png | Relative Volume - Price Plot (RVOL-PP) | Relative Volume - Price Plot (RVOL-PP) | CERTIFIE (accord .md + HTML) |
| image_04.png | Relative Volume - Time of Day (RVOL-TOD) | Relative Volume - Time of Day (RVOL-TOD) | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3411 — Définition : RVOL compare le volume de chaque barre à la moyenne des barres précédentes
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md, image_01) : « The Relative Volume (RVOL) indicator compares volume data for each price bar with the average volume over a specified number of prior bars. » Le ratio produit permet de repérer facilement les setups où un volume anormalement haut ou bas alimente un mouvement de prix. Valeur > 1 = volume supérieur à la moyenne ; valeur < 1 = volume inférieur à la moyenne.
**TRADEX-AI C2** : Indicateur de volume relatif (order flow / engagement) ; ratio normalisé exploitable comme filtre de conviction sur GC/HG/CL/ZW, jamais comme déclencheur d'ordre.
*Catégorie : indicateurs_momentum*

---

### D3412 — Formule : RVOL = volume courant / volume moyen sur la période de look-back
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : « RVOL = current volume / average volume over the look-back period ». Formule simple, déterministe, produisant un ratio.
**TRADEX-AI C2** : Calcul déterministe codable directement (division volume courant / moyenne mobile du volume) ; aucune ambiguïté de reconstruction.
*Catégorie : indicateurs_momentum*

---

### D3413 — Paramétrage par défaut : SMA 50 périodes, ajustable (périodes + type SMA/EMA)
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Par défaut le volume moyen est calculé avec une moyenne mobile simple à 50 périodes, mais le nombre de périodes et le type de moyenne (SMA ou EMA) peuvent être modifiés selon le timeframe analysé.
**TRADEX-AI C2** : Paramètres configurables (look-back, SMA vs EMA) à fixer pour TRADEX selon le timeframe Belkhayate (Standard 15min / Range Bar / Scalping 15s) ; défaut 50 SMA = point de départ.
*Catégorie : indicateurs_momentum*

---

### D3414 — Lecture du ratio : 2.5 = 2,5× le volume normal ; 1.0 = volume égal à la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Un RVOL de 2.5 signifie que le volume de la barre courante vaut 2,5 fois le volume normal de la période. Une valeur de 1.0 signifie que le volume courant est égal au volume moyen.
**TRADEX-AI C2** : Échelle de lecture directe (multiple du volume normal) ; sert de métrique d'intensité du volume à intégrer au scoring /10.
*Catégorie : indicateurs_momentum*

---

### D3415 — Bornes : limite basse 0 (volume nul) ; pas de limite haute théorique ; >4.0 = spike
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : La limite basse du ratio est zéro (volume courant nul). Il n'y a théoriquement pas de limite haute, mais en pratique tout ce qui dépasse 4.0 est considéré comme un volume spike et non une valeur RVOL typique.
**TRADEX-AI C2** : Seuil de spike (>4.0) borne déterministe utilisable comme garde-fou de détection d'anomalie de volume ; non plafonné par construction.
*Catégorie : indicateurs_momentum*

---

### D3416 — Usage : confirmer la tendance via le niveau d'engagement des traders
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Le but du RVOL est de déterminer si le volume est supérieur ou inférieur à l'habituel pour cette barre, ce qui montre l'engagement (« how committed traders are ») envers un mouvement de prix.
**TRADEX-AI C2** : RVOL = mesure d'engagement, à utiliser comme confirmation de tendance (C1) plutôt que signal autonome ; cohérent avec la logique Belkhayate Direction/Énergie.
*Catégorie : signal*

---

### D3417 — RVOL élevé = engagement → continuation probable de la tendance
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : « In general, a higher RVOL value shows a level of commitment to the price move; the current trend will likely continue. »
**TRADEX-AI C2** : Règle de continuation (RVOL haut → poursuite probable) intégrable comme critère pondéré favorable dans le scoring de signal.
*Catégorie : signal*

---

### D3418 — RVOL faible = manque d'engagement → reversal possible ou début de range
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Un RVOL inférieur à la normale démontre un manque d'engagement et peut indiquer un retournement de tendance à venir ou le début d'un trading range.
**TRADEX-AI C2** : RVOL faible = signal d'alerte (reversal/range) ; complète D3417, à pondérer comme critère défavorable à la continuation.
*Catégorie : signal*

---

### D3419 — Validation d'un changement de tendance : pullback faible RVOL vs nouvelle tendance forte RVOL
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Un pullback à faible RVOL est probablement juste un pullback ; mais si un volume supérieur à l'habituel accompagne une baisse de prix, les traders peuvent être suffisamment engagés pour maintenir la nouvelle tendance baissière.
**TRADEX-AI C2** : Discriminant pullback simple vs vrai retournement via le RVOL accompagnant le mouvement ; recoupe la logique de correction mineure sur niveau de support (cf. règles Rhodes).
*Catégorie : signal*

---

### D3420 — Seuils : 1.0 = moyenne ; >1.0 au-dessus ; <1.0 en-dessous ; 1.1 souvent négligeable
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : RVOL de 1.0 = exactement la moyenne ; au-dessus de 1.0 = « above average » ; en-dessous = « below average ». En pratique, un RVOL de 1.1 peut ne pas valoir la peine d'agir.
**TRADEX-AI C2** : Seuils de référence ; la zone proche de 1.0 (≈1.1) à considérer comme bruit non actionnable lors du paramétrage du filtre RVOL.
*Catégorie : indicateurs_momentum*

---

### D3421 — Seuil « significatif » subjectif ; nombre de day traders cherchent RVOL > 2.0
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Le seuil « significativement » au-dessus de la moyenne diffère selon chaque investisseur. Beaucoup de day traders cherchent un RVOL supérieur à 2.0 avant d'investir.
**TRADEX-AI C2** : Seuil pratique 2.0 = repère de référence pour un filtre RVOL day-trading ; à arbitrer pour TRADEX (paramètre, non règle absolue).
*Catégorie : indicateurs_momentum*

---

### D3422 — Attention aux extrêmes : spike ≥ 4.0 en overbought/oversold peut annoncer un retournement
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Si le RVOL spike soudainement à 4.0 ou plus, surtout pendant que le titre est overbought/oversold, cela peut présager un retournement de tendance — l'effet exactement opposé d'un RVOL plus modérément au-dessus de la moyenne.
**TRADEX-AI C2** : Non-monotonie clé : RVOL très haut + condition extrême = inverse du signal de continuation. Garde-fou contre une lecture naïve « plus de volume = plus de continuation ».
*Catégorie : signal*

---

### D3423 — Conclusion : RVOL confirme un mouvement, n'est pas un signal autonome
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : « Remember that just like volume, Relative Volume (RVOL) is used to confirm a price trend. This indicator is intended to be used in conjunction with other indicators and analysis techniques, not on its own. » Au-dessus de la moyenne = continuation généralement ; en-dessous = retournement ou range émergent.
**TRADEX-AI C2** : Cadre d'usage : RVOL = confirmateur, jamais déclencheur isolé ; cohérent avec la règle multi-cercles 3/4 + 2/3 du projet.
*Catégorie : signal*

---

### D3424 — Variante RVOL classique : positionnable au-dessus/dessous/derrière le price plot
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md, image_02) : L'indicateur RVOL classique peut être positionné au-dessus, en-dessous ou derrière le price plot du titre. Calculé par défaut sur SMA 50, ajustable (périodes + type de MA).
**TRADEX-AI C2** : Variante d'affichage propre à StockChartsACP ; sans portée algorithmique pour TRADEX (donnée d'outil), conservée pour traçabilité.
*Catégorie : indicateurs_momentum*

---

### D3425 — Baseline et échelle : défaut 1.0 (ratio), couleurs vert/rouge, échelle Ratio ou Percentage
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Baseline par défaut 1.0 (volume courant = moyenne), modifiable. Valeurs au-dessus typiquement en vert, en-dessous en rouge. Échelle par défaut Ratio ; en Percentage la baseline passe automatiquement à 0.0 (volume égal à la moyenne) ; -20 fixe la baseline à 20 % sous la moyenne.
**TRADEX-AI C2** : Conventions d'affichage (baseline, ratio vs pourcentage) ; utile si conversion ratio↔pourcentage codée, mais sans règle de trading nouvelle. 🟡 CONVENTION d'outil.
*Catégorie : indicateurs_momentum*

---

### D3426 — Variante RVOL-PP : flèches sur le price plot selon un seuil (ex. 1.3)
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md, image_03) : Le RVOL-PP marque les valeurs RVOL au-dessus/en-dessous d'un seuil directement sur le price plot. Exemple : baseline à 1.3 ; flèches vertes où RVOL > 1.3, rouges où RVOL < 1.3. Affichage des flèches au-dessus, en-dessous ou des deux côtés de la baseline au choix.
**TRADEX-AI C2** : Variante de visualisation par seuil ; concept de « marquage barre par seuil RVOL » transposable comme flag interne, mais l'affichage flèches reste propre à l'outil.
*Catégorie : indicateurs_momentum*

---

### D3427 — Variante RVOL-TOD : volume comparé à la moyenne à une heure précise (intraday)
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md, image_04) : Alors que le RVOL classique agrège le volume sur toute la journée, le RVOL-TOD compare le volume à la moyenne à un moment précis. Utile pour le court terme car le volume peut être bien plus élevé en début/fin de séance. Exemple : sur un chart 5 min, la valeur du bar 9:30 d'aujourd'hui est comparée à la moyenne des bars 9:30 précédents.
**TRADEX-AI C2** : Notion clé pour l'intraday (saisonnalité horaire du volume) ; pertinente pour le mode Scalping 15s / Range Bar où le volume d'ouverture/fermeture biaise un RVOL agrégé.
*Catégorie : indicateurs_momentum*

---

### D3428 — RVOL-TOD : SMA 50 par défaut, périodes ajustables, type de MA NON modifiable
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md, image_04) : Calculé par défaut sur SMA 50, le nombre de périodes est ajustable mais le type de moyenne ne peut PAS être modifié pour le RVOL-TOD. La valeur du bar courant est affichée dans la légende ; Scale en Percentage pour l'afficher en pourcentage.
**TRADEX-AI C2** : Contrainte technique (SMA imposée pour RVOL-TOD) ; à retenir si TRADEX réimplémente la variante time-of-day. Spécificité d'outil.
*Catégorie : indicateurs_momentum*

---

### D3429 — Scans RVOL : uptrend (>200 SMA, RVOL SMA50 entre 2.0 et 3.0) / downtrend (<200 SMA, RVOL EMA20 entre 2.0 et 3.0)
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : Scan « above average RVOL in an uptrend » : Close > SMA(200) ET RVOL SMA(50) entre 2.0 et 3.0. Scan downtrend : Close < SMA(200) ET RVOL EMA(20) entre 2.0 et 3.0 (EMA pour un timeframe plus court). « This scan is just a starting point. Further refinement and analysis are required. »
**TRADEX-AI C2** : Combinaison opérationnelle volume + tendance (RVOL 2.0–3.0 borné pour éviter les spikes >4 reversal) ; logique transposable comme préfiltre, mais bornes calibrées sur actions US daily — à revalider.
*Catégorie : signal*

---

### D3430 — Garde-fou scan : volume intra-journée incomplet → baser les scans sur « Last Market Close »
🟢 **FAIT VÉRIFIÉ** (Source : relative_volume_rvol.md) : « For scanning purposes, daily volume data is incomplete during the trading day. When running scans with volume-based indicators like RVOL, base the scan on the "Last Market Close." » Idem pour Accumulation/Distribution, OBV, PVO.
**TRADEX-AI C2** : Garde-fou de fraîcheur des données volume = recoupe directement le Staleness Monitor du projet (volume partiel intra-séance = donnée non fiable pour décision). Important pour la cohérence des collecteurs NT8/ATAS.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3411 | Définition RVOL (volume vs moyenne barres précédentes) | 🟢 | C2 | indicateurs_momentum |
| D3412 | Formule RVOL = vol courant / vol moyen look-back | 🟢 | C2 | indicateurs_momentum |
| D3413 | Défaut SMA 50, ajustable (SMA/EMA + périodes) | 🟢 | C2 | indicateurs_momentum |
| D3414 | Lecture ratio (2.5 = 2,5× ; 1.0 = moyenne) | 🟢 | C2 | indicateurs_momentum |
| D3415 | Bornes (0 / pas de max ; >4.0 = spike) | 🟢 | C2 | indicateurs_momentum |
| D3416 | Usage : confirmer tendance via engagement | 🟢 | C2 | signal |
| D3417 | RVOL élevé → continuation probable | 🟢 | C2 | signal |
| D3418 | RVOL faible → reversal/range possible | 🟢 | C2 | signal |
| D3419 | Pullback faible vs nouvelle tendance forte RVOL | 🟢 | C2 | signal |
| D3420 | Seuils (1.0 moyenne ; 1.1 négligeable) | 🟢 | C2 | indicateurs_momentum |
| D3421 | Day traders : RVOL > 2.0 | 🟢 | C2 | indicateurs_momentum |
| D3422 | Spike ≥ 4.0 + extrême → retournement (non-monotonie) | 🟢 | C2 | signal |
| D3423 | RVOL = confirmateur, pas signal autonome | 🟢 | C2 | signal |
| D3424 | RVOL classique : positionnement sur price plot | 🟢 | C2 | indicateurs_momentum |
| D3425 | Baseline 1.0, échelle Ratio/Percentage (🟡) | 🟢 | C2 | indicateurs_momentum |
| D3426 | RVOL-PP : flèches par seuil sur price plot | 🟢 | C2 | indicateurs_momentum |
| D3427 | RVOL-TOD : volume vs moyenne à une heure donnée | 🟢 | C2 | indicateurs_momentum |
| D3428 | RVOL-TOD : SMA imposée, périodes ajustables | 🟢 | C2 | indicateurs_momentum |
| D3429 | Scans RVOL uptrend/downtrend (2.0–3.0) | 🟢 | C2 | signal |
| D3430 | Garde-fou : volume intra incomplet → Last Close | 🟢 | C2 | gestion_risque_entree |

**Liens Belkhayate :** Le RVOL est un indicateur de volume StockCharts, PAS un élément de la méthode Belkhayate (⚫ — NON CONCERNÉ au sens strict). Rapprochement indirect : l'« Énergie » Belkhayate = MFI standard (mémoire projet), indicateur volume/flux ; le RVOL pourrait servir de filtre de conviction complémentaire au MFI, mais l'assimiler à Belkhayate serait une hypothèse projet non affirmée par la source (⚫🔴).

**À vérifier (humain) :**
- Seuils 2.0 / 2.0–3.0 / spike 4.0 calibrés sur actions US daily — revalider sur range bars NT8 (GC/HG/CL/ZW) où la distribution du volume diffère.
- Choix paramètre TRADEX : look-back (défaut 50) et SMA vs EMA selon timeframe Belkhayate (15min / Range Bar 4-5t / 15s).
- D3422 non-monotonie (spike + overbought/oversold = reversal) : décider si TRADEX en fait un critère éliminatoire ou un simple modulateur de confiance.
- D3430 recoupe le Staleness Monitor : confirmer que les collecteurs NT8/ATAS n'utilisent pas un volume intra-barre incomplet pour décider.
- D3427/D3428 RVOL-TOD : pertinence pour le mode Scalping 15s à arbitrer (saisonnalité horaire du volume des futures CME ≠ actions US).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
