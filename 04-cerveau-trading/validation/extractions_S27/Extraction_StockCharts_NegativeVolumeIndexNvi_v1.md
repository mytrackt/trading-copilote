# Extraction StockCharts — Negative Volume Index (NVI)
**Source :** `bundles/stockcharts/negative_volume_index_nvi.md` (HTTP 200 · ~10 246 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D2771 → D2790 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/negative-volume-index-nvi
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 | SharpCharts Calculation | CERTIFIE (accord .md + HTML) |
| image_02.png | Spreadsheet 1 | SharpCharts Calculation | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 2 | Signal | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 3 | Fine Tuning | CERTIFIE (accord .md + HTML) |
| image_05.png | Chart 4 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |
| image_06.png | Chart 5 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D2771 — Nature du NVI : indicateur cumulatif de volume « smart money »
🔵 **ÉCOLE (Dysart)** (Source : negative_volume_index_nvi.md) : Le Negative Volume Index (NVI) est un indicateur cumulatif qui utilise le CHANGEMENT de volume pour décider quand le « smart money » est actif. Développé par Paul Dysart dans les années 1930. Il fonctionne sous l'hypothèse que le smart money est actif les jours où le volume DIMINUE, et le « not-so-smart money » les jours où le volume AUGMENTE.
**TRADEX-AI C2** : Indicateur de flux/volume cumulatif candidat comme couche de confirmation order flow ; logique inverse de l'OBV (s'intéresse aux jours de volume FAIBLE).
*Catégorie : indicateurs_tendance*

---

### D2772 — Deux versions : Dysart (Net Advances) vs Fosback (% prix)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Il existe deux versions. Version originale de Dysart : ligne cumulative formée en ajoutant les Net Advances (issues en hausse moins issues en baisse) quand le volume diminue. Norman Fosback (auteur de *Stock Market Logic*) a ajusté l'indicateur en substituant le pourcentage de variation du prix aux Net Advances. La formule SharpCharts utilise la version Fosback.
**TRADEX-AI C2** : La version implémentable sur un actif unique (GC/HG/CL/ZW) est la version Fosback (% prix), les Net Advances exigeant un univers de marché (breadth).
*Catégorie : indicateurs_tendance*

---

### D2773 — Formule SharpCharts (version Fosback)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_01) : Algorithme en 4 étapes :
```
1. NVI cumulatif démarre à 1000
2. Ajouter le % de variation du prix au NVI cumulatif quand le Volume DIMINUE
3. NVI cumulatif INCHANGÉ quand le Volume AUGMENTE
4. Appliquer une EMA 255 jours pour les signaux
```
**TRADEX-AI C2** : Formule déterministe implémentable telle quelle ; base de départ 1000, EMA de signal = 255 jours. Nécessite un flux volume fiable (NT8/ATAS).
*Catégorie : indicateurs_tendance*

---

### D2774 — Détail du calcul tableur (Volume %Change conditionne l'apport)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_02) : Dans l'exemple tableur, le Price %Change est multiplié par 100 pour réduire le nombre de décimales. Quand le Volume %Change est NÉGATIF, le % de variation du S&P 500 est inscrit dans la colonne NVI Value. Quand le Volume %Change est POSITIF, rien n'apparaît (NVI Value vide). Partant de 1000, les NVI Values s'appliquent à chaque période pour créer un indicateur cumulatif qui ne change QUE lorsque le volume diminue.
**TRADEX-AI C2** : Confirme la mécanique conditionnelle (apport uniquement si Volume %Change < 0) ; cas-test chiffré pour vérifier une implémentation.
*Catégorie : indicateurs_tendance*

---

### D2775 — Signal traditionnel : NVI vs EMA 255 jours
🔵 **ÉCOLE (Fosback)** (Source : negative_volume_index_nvi.md, image_03) : Selon Fosback, les probabilités favorisent un bull market quand le NVI est AU-DESSUS de son EMA 255 jours, et un bear market quand il est EN DESSOUS.
**TRADEX-AI C2** : Signal binaire (NVI au-dessus/dessous EMA255) directement codable comme feature de régime ; à filtrer (whipsaws, cf. D2777).
*Catégorie : signal*

---

### D2776 — Probabilités asymétriques (96% bull vs 53% bear)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Fosback note que ces probabilités ne sont PAS symétriques : il y a 96% de chances de bull market quand le NVI est au-dessus de son EMA 255 jours, mais seulement 53% de chances de bear market quand le NVI est en dessous.
**TRADEX-AI C2** : Asymétrie critique — le signal HAUSSIER (NVI>EMA255) est nettement plus fiable que le signal baissier. Pondérer en conséquence ; le franchissement baissier ≈ coin flip.
*Catégorie : signal*

---

### D2777 — Whipsaws fréquents malgré l'EMA longue + lag
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_03) : Le graphique du Dow Industrials avec NVI montre, même avec une moyenne mobile longue, de nombreux whipsaws (mauvais signaux). L'indicateur a croisé l'EMA 255 jours plusieurs fois en 1998 (zigzag haussier) et en 2001-2002 (Dow volatil). Les signaux de fin 2002 furent moins sujets au whipsaw quand des tendances plus fortes émergèrent. Les chartistes doivent s'attendre à du lag car les moyennes mobiles retardent et une EMA 255 jours est utilisée.
**TRADEX-AI C2** : Garde-fou — NVI sujet aux whipsaws en marché volatil/sans tendance ; lag inhérent à l'EMA255. Coupler à un détecteur de régime tendance/range.
*Catégorie : signal*

---

### D2778 — Applicable au-delà des indices (ETF, actions, tout actif avec volume)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Bien que conçu pour un indice boursier majeur, le NVI peut s'utiliser avec des ETF, actions ou tout ce qui a du volume. La rationale reste un peu inhabituelle car les mouvements de prix sur volume CROISSANT sont essentiellement ignorés.
**TRADEX-AI C2** : Transposable à GC/HG/CL/ZW (actifs à volume) ; garder en tête que le NVI ignore par construction les jours de volume croissant.
*Catégorie : indicateurs_tendance*

---

### D2779 — Fine Tuning : NVI + double EMA (255 rouge / 100 jours)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_04) : Exemple Consumer Discretionary SPDR (XLY) avec NVI et deux EMA. Tendance générale haussière quand NVI au-dessus de son EMA 255 jours (rouge). Un passage SOUS l'EMA 100 jours signale une correction au sein de cet uptrend.
**TRADEX-AI C2** : Schéma à deux EMA (255 = tendance de fond, 100 = correction) codable comme deux features hiérarchisées (régime + pullback).
*Catégorie : indicateurs_tendance*

---

### D2780 — Trend lines sur le NVI : cassure = fin de correction
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_04) : On peut appliquer de l'analyse technique de base au NVI en traçant des trend lines. Sur XLY, trois périodes correctives de janvier 2010 à juillet 2012 (lignes bleues) ; une cassure AU-DESSUS de ces trend lines a signalé la fin d'une correction et la reprise de l'uptrend du NVI. Ces signaux de breakout ont aussi préfiguré des mouvements de prix significatifs du sous-jacent (XLY).
**TRADEX-AI C2** : Le NVI lui-même peut porter des trend lines ; une cassure haussière de trend line NVI = signal anticipateur du prix. Détection de cassure sur la courbe NVI exploitable.
*Catégorie : signal*

---

### D2781 — Hypothèse fondatrice : smart money sur volume décroissant
🔵 **ÉCOLE (Dysart/Fosback)** (Source : negative_volume_index_nvi.md) : Le NVI est un indicateur hybride combinant les apports de Paul Dysart et Norman Fosback. Il compte les variations de prix quand le volume DIMINUE et les ignore (discounts) quand le volume augmente. L'hypothèse : l'argent informé (smart money) travaille quand le volume diminue, l'argent non informé quand le volume augmente.
**TRADEX-AI C2** : Rationale théorique à mémoriser ; le NVI est un proxy de l'activité du smart money en sessions calmes (volume bas).
*Catégorie : indicateurs_tendance*

---

### D2782 — Conçu pour indices larges, comportement variable sur titres isolés
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Le NVI a été conçu pour les indices de marché larges et le volume d'échange. Il peut s'utiliser sur actions et ETF mais n'agit pas toujours comme attendu. Il produit d'excellents signaux de divergence haussière/baissière sur certains titres mais peut être totalement désynchronisé sur d'autres.
**TRADEX-AI C2** : Garde-fou robustesse — fiabilité dépendante de l'actif ; à valider individuellement sur GC/HG/CL/ZW (walk-forward) avant tout usage.
*Catégorie : signal*

---

### D2783 — Règle : jamais utilisé seul
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Comme tous les indicateurs, le NVI ne doit PAS être utilisé seul ; les chartistes doivent l'employer conjointement avec d'autres techniques d'analyse.
**TRADEX-AI C2** : Règle architecturale — NVI = couche de confirmation (C2), jamais critère unique.
*Catégorie : signal*

---

### D2784 — Charting : NVI cumulatif non ajustable, EMA paramétrable
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Dans SharpCharts, le NVI est défini comme indicateur cumulatif et ne peut être ajusté. Les chartistes peuvent ajuster l'EMA en changeant le nombre dans la case Parameters. Mettre le paramètre à « 1 » supprime essentiellement la moyenne mobile. L'indicateur peut être positionné derrière, au-dessus ou en dessous de la fenêtre principale.
**TRADEX-AI C2** : Détail outil (UI) ; seul l'EMA de signal est paramétrable (défaut 255). Paramètre = 1 → NVI brut sans signal.
*Catégorie : indicateurs_tendance*

---

### D2785 — Indicateurs avancés applicables au NVI (ex. ROC)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Les chartistes peuvent appliquer une autre moyenne mobile ou un autre indicateur au NVI via les options « advanced ». L'exemple montre l'oscillateur Rate-of-Change (ROC) appliqué au NVI dans la fenêtre d'indicateur.
**TRADEX-AI C2** : Possibilité d'empiler un oscillateur (ROC) sur le NVI pour en mesurer le momentum ; idée exploitable côté moteur.
*Catégorie : indicateurs_tendance*

---

### D2786 — Exemple live NVI ($COMPQ)
🟡 **CONVENTION** (Source : negative_volume_index_nvi.md) : La page renvoie vers un exemple live du NVI en action sur le Nasdaq Composite ($COMPQ) via un lien StockCharts.
**TRADEX-AI C2** : Référence externe (lien live) ; aucune donnée exploitable, simple pointeur pédagogique.
*Catégorie : indicateurs_tendance*

---

### D2787 — Charts illustratifs additionnels (Chart 4 / Chart 5)
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md, image_05, image_06) : La section « Using with SharpCharts » fournit deux graphiques illustratifs supplémentaires (Chart 4 et Chart 5) accompagnant la configuration de l'indicateur.
**TRADEX-AI C2** : Supports visuels de configuration ; pas de règle nouvelle, valeur pédagogique uniquement.
*Catégorie : indicateurs_tendance*

---

### D2788 — Scan : Bullish NVI Signal Line Cross
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Scan révélant les actions où le NVI a croisé AU-DESSUS de sa ligne de signal (signal haussier), sur base liquide (volume SMA20 > 40000, close SMA60 > 20) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [NVI x NVI Signal(255)]
```
**TRADEX-AI C2** : Logique « NVI croise au-dessus de NVI Signal(255) » = entrée haussière ; transposable en condition Python, syntaxe de scan propre à StockCharts (non réutilisable telle quelle).
*Catégorie : signal*

---

### D2789 — Scan : Bearish NVI Signal Line Cross
🟢 **FAIT VÉRIFIÉ** (Source : negative_volume_index_nvi.md) : Scan symétrique baissier : NVI croise EN DESSOUS de sa ligne de signal. Même base de liquidité que D2788.
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 20]
AND [NVI Signal(255) x NVI]
```
**TRADEX-AI C2** : Symétrique baissier de D2788 (rappel D2776 : le signal baissier NVI n'est fiable qu'à ~53% — à pondérer).
*Catégorie : signal*

---

### D2790 — Further Study : références volume/breadth (Murphy, Pring)
🟡 **CONVENTION** (Source : negative_volume_index_nvi.md) : Pour approfondir, la page renvoie à *Technical Analysis of the Financial Markets* (John Murphy, chapitre volume + chapitre breadth indicators) et *Technical Analysis Explained* (Martin Pring, chapitre intégrant le volume à l'analyse).
**TRADEX-AI C2** : Références bibliographiques ; aucune règle codable, traçabilité documentaire.
*Catégorie : indicateurs_tendance*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D2771 | Nature NVI (smart money / volume) | 🔵 ÉCOLE | C2 | indicateurs_tendance |
| D2772 | Versions Dysart vs Fosback | 🟢 | C2 | indicateurs_tendance |
| D2773 | Formule SharpCharts (4 étapes) | 🟢 | C2 | indicateurs_tendance |
| D2774 | Détail calcul tableur | 🟢 | C2 | indicateurs_tendance |
| D2775 | Signal NVI vs EMA 255 | 🔵 ÉCOLE | C2 | signal |
| D2776 | Probabilités asymétriques 96/53 | 🟢 | C2 | signal |
| D2777 | Whipsaws + lag EMA255 | 🟢 | C2 | signal |
| D2778 | Applicable tout actif à volume | 🟢 | C2 | indicateurs_tendance |
| D2779 | Double EMA (255/100) | 🟢 | C2 | indicateurs_tendance |
| D2780 | Trend lines sur le NVI | 🟢 | C2 | signal |
| D2781 | Hypothèse smart money | 🔵 ÉCOLE | C2 | indicateurs_tendance |
| D2782 | Comportement variable par titre | 🟢 | C2 | signal |
| D2783 | Jamais standalone | 🟢 | C2 | signal |
| D2784 | Charting (cumulatif, EMA paramétrable) | 🟢 | C2 | indicateurs_tendance |
| D2785 | Indicateurs avancés (ROC) | 🟢 | C2 | indicateurs_tendance |
| D2786 | Exemple live $COMPQ | 🟡 CONVENTION | C2 | indicateurs_tendance |
| D2787 | Charts illustratifs 4/5 | 🟢 | C2 | indicateurs_tendance |
| D2788 | Scan bullish cross signal | 🟢 | C2 | signal |
| D2789 | Scan bearish cross signal | 🟢 | C2 | signal |
| D2790 | Further Study (Murphy/Pring) | 🟡 CONVENTION | C2 | indicateurs_tendance |

**Liens Belkhayate :** le Negative Volume Index n'est PAS un indicateur Belkhayate (⚫). Aucun lien direct revendiqué dans la source. Rapprochement possible (non affirmé) : le NVI est un indicateur de flux/volume dont l'esprit (activité du « smart money ») recoupe vaguement la notion d'« Énergie » Belkhayate ; or la mémoire projet établit que l'Énergie Belkhayate = MFI standard (Money Flow Index, seuils 20/80), un indicateur DIFFÉRENT du NVI (le NVI est cumulatif, basé sur les jours de volume décroissant ; le MFI est un oscillateur borné 0-100). Ne PAS assimiler NVI et MFI. ⚫🔴 Aucune équivalence à coder sans validation humaine.

**À vérifier (humain) :**
- D2773 / D2776 — EMA 255 jours et probabilités 96/53 calibrées sur indices boursiers larges (S&P, Dow) ; à revalider (walk-forward) sur les futures GC/HG/CL/ZW dont la microstructure volume diffère.
- D2772 — la version Dysart (Net Advances / breadth) n'est PAS calculable sur un actif unique ; n'implémenter que la version Fosback (% prix).
- D2778 / D2782 — la source avertit que le NVI peut être « totalement désynchronisé » sur certains titres : tester la corrélation NVI/prix par actif avant intégration.
- D2776 — exploiter prioritairement le signal HAUSSIER (96%) ; le signal baissier (~53%) est proche du hasard et ne doit pas déclencher seul.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
