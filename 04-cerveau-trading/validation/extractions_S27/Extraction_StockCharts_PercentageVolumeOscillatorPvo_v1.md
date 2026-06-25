# Extraction StockCharts — Percentage Volume Oscillator (PVO)
**Source :** `bundles/stockcharts/percentage_volume_oscillator_pvo.md` (HTTP 200 · ~9 100 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D3091 → D3110 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/percentage-volume-oscillator-pvo
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | PVO - Chart 1 | Calculating the Percentage Volume Oscillator | CERTIFIE (accord .md + HTML) |
| image_02.png | PVO - Chart 2 | Validating Breaks | CERTIFIE (accord .md + HTML) |
| image_03.png | PVO - Chart 3 | Validating Breaks | CERTIFIE (accord .md + HTML) |
| image_04.png | PVO - Chart 4 | Fine-Tuning the PVO | CERTIFIE (accord .md + HTML) |
| image_05.png | PVO - Chart 5 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_06.png | PVO - Chart 6 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3091 — Nature du PVO : oscillateur de momentum appliqué au volume
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_01) : Le Percentage Volume Oscillator (PVO) est un oscillateur de momentum POUR le volume. Il mesure la différence entre deux moyennes mobiles de volume exprimée en POURCENTAGE de la plus grande des deux moyennes. Comme le MACD et le PPO, il s'affiche avec une ligne de signal, un histogramme et une ligne centrale (zéro). Le PVO est positif quand l'EMA courte de volume est au-dessus de l'EMA longue, négatif quand elle est en dessous.
**TRADEX-AI C2** : Indicateur de flux/volume (momentum du volume) candidat comme couche de confirmation order flow ; mesure relative (%) donc comparable inter-actifs contrairement à l'OBV (échelle absolue).
*Catégorie : indicateurs_momentum*

---

### D3092 — Formule de calcul du PVO et de ses composantes
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Formule déterministe :
```
PVO = ((EMA12 du Volume - EMA26 du Volume) / EMA26 du Volume) x 100
Ligne de signal = EMA9 du PVO
Histogramme PVO = PVO - Ligne de signal
```
Réglages par défaut (12,26,9), identiques au MACD/PPO. Le PVO est positif quand l'EMA12 de volume passe au-dessus de l'EMA26, négatif sinon. La multiplication par 100 décale la virgule de deux rangs.
**TRADEX-AI C2** : Formule implémentable telle quelle ; nécessite un flux volume fiable (NT8/ATAS) pour GC/HG/CL/ZW. La normalisation en % de l'EMA26 rend la valeur indépendante du niveau absolu de volume.
*Catégorie : indicateurs_momentum*

---

### D3093 — Lecture de l'amplitude : écart % entre les deux EMA
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Le degré positif/négatif du PVO dépend de l'éloignement de l'EMA12 par rapport à l'EMA26. Un PVO = 5 indique que l'EMA12 de volume est 5 % au-dessus de l'EMA26 ; un PVO = -3 indique que l'EMA12 est 3 % en dessous de l'EMA26.
**TRADEX-AI C2** : Interprétation directe de l'amplitude → feature « intensité de surge de volume » exprimée en % ; seuil paramétrable (ex. PVO > 20 = surge marqué, cf. D3097).
*Catégorie : indicateurs_momentum*

---

### D3094 — Histogramme PVO : croisement PVO / ligne de signal
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : L'histogramme PVO se comporte comme ceux du MACD et du PPO. Il est positif quand le PVO est au-dessus de sa ligne de signal (EMA9), négatif quand le PVO est en dessous.
**TRADEX-AI C2** : Feature de croisement codable (signe de PVO - signal) ; transition de signe = accélération/décélération du momentum de volume.
*Catégorie : indicateurs_momentum*

---

### D3095 — Interprétation : volume au-dessus/en dessous de la moyenne
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : En général, le volume est AU-DESSUS de la moyenne quand le PVO est positif et EN DESSOUS quand il est négatif. Un PVO négatif et montant indique des niveaux de volume qui AUGMENTENT ; un PVO positif et descendant indique des niveaux qui DIMINUENT. Sert à confirmer ou réfuter les mouvements du graphique de prix.
**TRADEX-AI C2** : Deux features — signe du PVO (volume vs moyenne) ET pente du PVO (volume croissant/décroissant). La pente prime sur le signe pour détecter une montée en volume précoce.
*Catégorie : signal*

---

### D3096 — Garde-fou : le PVO retarde (moyennes mobiles laggantes)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Bien que basé sur une formule de momentum, le PVO repose sur des moyennes mobiles qui RETARDENT. L'EMA12 inclut 12 jours de volume (données récentes pondérées davantage) ; l'EMA26 retarde encore plus (26 jours). Le PVO(12,26,9) peut donc être DÉSYNCHRONISÉ de l'action des prix.
**TRADEX-AI C2** : Garde-fou — le PVO est un indicateur RETARDÉ ; ne pas l'utiliser comme déclencheur d'entrée primaire mais comme confirmation. Risque de désynchronisation prix/volume à prendre en compte.
*Catégorie : gestion_risque_entree*

---

### D3097 — Validation de cassure : le volume valide le mouvement de prix
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_02, image_03) : Le PVO sert à confirmer une cassure de support/résistance. Une cassure de support sur volume CROISSANT a plus de crédibilité qu'une cassure sur faible volume ; une cassure de résistance sur volume en expansion montre plus d'intérêt acheteur, augmentant les chances de succès. Exemple VLO : le PVO(12,26,9) confirme un breakout de pennant ; le second croisement du PVO (passage en territoire positif) coïncide avec la cassure de résistance. Exemple ADM : breakout de résistance avec PVO surgissant en positif (surge à 20, soit EMA12 ≈ 20 % au-dessus de l'EMA26) puis cassure de support avec un gap et un nouveau surge du PVO.
**TRADEX-AI C2** : Règle de confirmation centrale — exiger un PVO positif/montant (ou surge ≥ seuil) pour valider une cassure S/R. Feature de filtrage des faux breakouts. Pertinent pour GC/HG/CL/ZW.
*Catégorie : signal*

---

### D3098 — Fine-tuning : long EMA = 250 (volume annuel moyen)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_04) : On peut ajuster le PVO pour mettre en évidence les surges de volume sur une période précise. ~250 jours de bourse par an : une EMA250 représente le volume annuel moyen (pondéré récent). Avec une EMA longue de 250 et une EMA courte, on isole les surges au-dessus de cette moyenne. PVO(1,250) est positif quand le volume d'1 jour dépasse l'EMA250 ; PVO(5,250) est positif quand l'EMA5 dépasse l'EMA250.
**TRADEX-AI C2** : Paramétrage alternatif pour détecter des surges de volume relatifs à une moyenne longue (annuelle) ; PVO(1,250)/PVO(5,250) = détecteur de volume anormalement élevé. À recalibrer pour la microstructure des futures (séances/roll).
*Catégorie : configuration*

---

### D3099 — Comparaison PVO(1,250) vs PVO(5,250) : réactivité
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_04) : Sur MRK, le PVO(1,250) tourne positif quand une barre de volume dépasse l'EMA250 (flèches vertes) ; le PVO(5,250) tourne positif quand l'EMA5 dépasse l'EMA250 (flèches bleues). Le PVO(1,250) croise la ligne zéro plus souvent et est légèrement plus rapide. En substance : volume au-dessus de la moyenne si PVO(1,250) positif, en dessous si négatif. Une cassure sur volume au-dessus de la moyenne est plus robuste.
**TRADEX-AI C2** : Arbitrage réactivité/bruit — EMA courte 1 = plus rapide mais plus de croisements (bruit) ; EMA 5 = plus lissé. Choix de la fenêtre courte selon tolérance au bruit.
*Catégorie : configuration*

---

### D3100 — Limites : divergences PVO mal adaptées (volume ne tend pas)
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Le PVO peut être très haché car le volume NE TEND PAS. Les divergences haussières et baissières sont MAL ADAPTÉES au PVO. À la place, les chartistes devraient chercher des signes de volume croissant avec un passage en territoire positif, et de volume décroissant avec un passage en négatif.
**TRADEX-AI C2** : Garde-fou critique — NE PAS coder de signaux de divergence sur le PVO (contrairement à l'OBV). Privilégier les signaux de signe/pente (volume croissant/décroissant).
*Catégorie : gestion_risque_entree*

---

### D3101 — Synthèse d'usage : validation de cassures, jamais standalone
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Le PVO est un indicateur de momentum appliqué au volume. Un volume croissant peut valider une cassure de support/résistance ; un surge ou une cassure significative sur FAIBLE volume est moins robuste. Comme tout indicateur technique, l'utiliser CONJOINTEMENT avec d'autres aspects de l'AT (chart patterns, oscillateurs de momentum).
**TRADEX-AI C2** : Règle architecturale — PVO = couche de confirmation volume (C2), jamais critère unique ; coupler à patterns/momentum (C1). Cohérent avec la règle 3/4 + 2/3 du projet.
*Catégorie : signal*

---

### D3102 — Charting SharpCharts : positionnable, options avancées
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_05, image_06) : Dans SharpCharts, le PVO se place au-dessus, en dessous ou derrière le tracé du prix. À la sélection, les paramètres par défaut (12,26,9) apparaissent et sont ajustables. « Advanced options » permet d'ajouter une moyenne mobile ou une ligne horizontale. Dans l'exemple, le volume est ajouté DEUX fois en indicateur pour afficher deux moyennes (la seconde placée « behind ind », EMA réglée à 250).
**TRADEX-AI C2** : Détail outil (UI) ; confirme la mécanique du paramétrage des deux EMA de volume utilisée pour le fine-tuning (D3098).
*Catégorie : configuration*

---

### D3103 — Scan : PPO bullish cross AVEC PVO positif
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Scan révélant les actions où le PPO(12,26,9) passe au-dessus de sa ligne de signal ET le PVO(12,26,9) passe en territoire positif (volume croissant) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily PPO Line(12,26,9,Daily Close) crosses Daily PPO Signal(12,26,9,Daily Close)]
AND [Daily PVO Line(12,26,9) crosses 0]
```
Présenté comme point de départ à raffiner.
**TRADEX-AI C2** : Logique « croisement momentum prix (PPO) confirmé par surge de volume (PVO) » = double confirmation haussière ; transposable en condition Python. Syntaxe de scan propre à StockCharts.
*Catégorie : signal*

---

### D3104 — Scan : PPO bearish cross AVEC PVO positif
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Scan symétrique : le PPO(12,26,9) passe SOUS sa ligne de signal ET le PVO(12,26,9) passe en positif (volume croissant) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [Daily PPO Signal(12,26,9,Daily Close) crosses Daily PPO Line(12,26,9,Daily Close)]
AND [Daily PVO Line(12,26,9) crosses 0]
```
**TRADEX-AI C2** : Symétrique baissier de D3103 ; volume croissant valide aussi une cassure baissière (un mouvement à la baisse confirmé par du volume).
*Catégorie : signal*

---

### D3105 — Garde-fou scan : volume intraday incomplet → Last Market Close
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Pour le scanning, les données de volume quotidiennes sont INCOMPLÈTES en séance. Avec les indicateurs volume comme le PVO, baser le scan sur la dernière clôture de marché (« Last Market Close »). Autres indicateurs volume concernés cités : Accumulation/Distribution, Chaikin Money Flow, On Balance Volume.
**TRADEX-AI C2** : Garde-fou data cohérent avec staleness_monitor — ne pas signaler sur volume non clos. À intégrer si calcul sur barres journalières.
*Catégorie : gestion_risque_entree*

---

### D3106 — Filiation MACD/PPO : trois composantes communes
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Le PVO partage exactement la structure du MACD et du PPO (ligne, signal EMA9, histogramme, ligne centrale). La seule différence est la donnée d'entrée : VOLUME au lieu du prix de clôture. Le PPO mentionné est référencé comme indicateur frère appliqué au prix.
**TRADEX-AI C2** : Réutilisation de code — un module MACD/PPO générique paramétré sur la série de volume produit le PVO. Mutualisation possible dans le moteur (DRY).
*Catégorie : indicateurs_momentum*

---

### D3107 — PVO positif = confirmation privilégiée de breakout valide
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md) : Le texte d'introduction pose la règle générale : « Typiquement, une cassure (breakout) ou une cassure de support est VALIDÉE quand le PVO est montant ou positif. » C'est l'usage central revendiqué de l'indicateur.
**TRADEX-AI C2** : Critère de validation explicite → condition booléenne « PVO montant OU positif » à attacher à tout signal de breakout dans le moteur (filtre de qualité de cassure).
*Catégorie : signal*

---

### D3108 — Cas VLO : double croisement, second confirme le pennant
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_02) : Sur VLO, le volume décline en août (PVO descendant jusqu'à mi-septembre), puis le PVO remonte mais n'entre en positif que fin octobre (l'EMA12 de volume croise enfin au-dessus de l'EMA26). VLO restait coincé dans le pennant au premier croisement du PVO ; il casse la résistance du pennant au SECOND croisement. Le volume confirme le breakout et VLO poursuit son avance.
**TRADEX-AI C2** : Cas d'école — le passage effectif en positif (et non la simple remontée) est le déclencheur de confirmation. Distinguer « PVO montant mais négatif » de « PVO positif » dans la logique de validation.
*Catégorie : configuration*

---

### D3109 — Cas ADM : surge à 20 sur breakout ET sur cassure de support
🟢 **FAIT VÉRIFIÉ** (Source : percentage_volume_oscillator_pvo.md, image_03) : Sur ADM, cassure de résistance début août avec PVO surgissant en positif (surge marqué). Après une avance de trois mois, cassure de support avec un GAP et un nouveau surge du PVO. Le PVO surge à 20 dans les deux cas (EMA12 de volume ≈ 20 % au-dessus de l'EMA26). Une expansion de volume sur breakout haussier est haussière.
**TRADEX-AI C2** : Confirme que le PVO valide AUSSI les cassures baissières (volume sur gap baissier), pas uniquement les hausses. Seuil de surge ~20 % observé comme repère empirique (non normatif).
*Catégorie : signal*

---

### D3110 — Référence d'approfondissement : John Murphy (volume/OI)
🔵 **ÉCOLE (Murphy)** (Source : percentage_volume_oscillator_pvo.md) : Le livre de John Murphy *Technical Analysis of the Financial Markets* couvre l'analyse technique avec des sections expliquant le volume, l'open interest et les indicateurs de volume ; Murphy discute l'importance du volume avec de nombreux exemples graphiques.
**TRADEX-AI C2** : Source bibliographique pour approfondir le rôle du volume/OI ; cohérent avec le Cercle C3 (institutionnels : open interest) du projet.
*Catégorie : indicateurs_momentum*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3091 | Nature PVO (momentum du volume) | 🟢 | C2 | indicateurs_momentum |
| D3092 | Formule de calcul | 🟢 | C2 | indicateurs_momentum |
| D3093 | Amplitude = écart % EMA | 🟢 | C2 | indicateurs_momentum |
| D3094 | Histogramme (croisement signal) | 🟢 | C2 | indicateurs_momentum |
| D3095 | Volume vs moyenne (signe/pente) | 🟢 | C2 | signal |
| D3096 | Garde-fou : indicateur retardé | 🟢 | C2 | gestion_risque_entree |
| D3097 | Validation de cassure (VLO/ADM) | 🟢 | C2 | signal |
| D3098 | Fine-tuning EMA 250 | 🟢 | C2 | configuration |
| D3099 | PVO(1,250) vs PVO(5,250) | 🟢 | C2 | configuration |
| D3100 | Garde-fou : divergences inadaptées | 🟢 | C2 | gestion_risque_entree |
| D3101 | Synthèse — jamais standalone | 🟢 | C2 | signal |
| D3102 | Charting SharpCharts | 🟢 | C2 | configuration |
| D3103 | Scan PPO bull cross + PVO+ | 🟢 | C2 | signal |
| D3104 | Scan PPO bear cross + PVO+ | 🟢 | C2 | signal |
| D3105 | Garde-fou volume intraday | 🟢 | C2 | gestion_risque_entree |
| D3106 | Filiation MACD/PPO | 🟢 | C2 | indicateurs_momentum |
| D3107 | PVO+ = breakout validé | 🟢 | C2 | signal |
| D3108 | Cas VLO (second croisement) | 🟢 | C2 | configuration |
| D3109 | Cas ADM (surge 20) | 🟢 | C2 | signal |
| D3110 | Référence Murphy | 🔵 ÉCOLE | C2 | indicateurs_momentum |

**Liens Belkhayate :** le Percentage Volume Oscillator n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé) : le PVO est un indicateur de FLUX de volume dont l'esprit recoupe la notion d'« Énergie » Belkhayate ; or la mémoire projet établit que l'Énergie Belkhayate = MFI standard (Money Flow Index, seuils 20/80), indicateur DIFFÉRENT du PVO (le PVO est un oscillateur de momentum non borné basé UNIQUEMENT sur le volume ; le MFI est un oscillateur borné 0-100 intégrant prix typique ET volume). Ne PAS assimiler PVO et MFI. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D3092 / D3098 / D3103 / D3104 — formule et scans calibrés sur actions liquides US ; à revalider (walk-forward) sur les futures GC/HG/CL/ZW (microstructure volume différente, séances et roll des contrats).
- D3096 / D3100 — le PVO retarde ET ses divergences sont inadaptées : exiger une confirmation par signe/pente (passage en positif, cf. D3107/D3108) avant exploitation, jamais de signal de divergence PVO.
- D3098 / D3099 — paramétrage EMA250 ≈ « 250 jours/an » ; le nombre de séances et le roll des contrats futures faussent cette équivalence → recalibrer la fenêtre longue.
- D3105 — interdiction de signaler sur volume non clos : aligner avec staleness_monitor pour les calculs sur barres journalières.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
