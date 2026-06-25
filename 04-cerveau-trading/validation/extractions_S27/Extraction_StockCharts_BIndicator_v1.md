# Extraction StockCharts — %B Indicator
**Source :** `bundles/stockcharts/b_indicator.md` (HTTP 200 · ~10 700 car.) + 4 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 4/4 certifiées
**Décisions :** D831 → D843 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/b-indicator
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | Chart 1 | Signals: Overbought/Oversold | CERTIFIE (accord .md + HTML) |
| image_02.png | Chart 2 | Signals: Overbought/Oversold | CERTIFIE (accord .md + HTML) |
| image_03.png | Chart 3 | Signals: Trend Identification | CERTIFIE (accord .md + HTML) |
| image_04.png | Chart 4 | Using with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D831 — Nature du %B (position du prix dans les bandes de Bollinger)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Le %B mesure le prix d'un titre **par rapport aux bandes de Bollinger** supérieure et inférieure. Il sert à identifier les conditions de surachat/survente et à jauger la force de la tendance. Combiné à d'autres indicateurs comme le Money Flow Index (MFI), il aide à repérer des points d'entrée au sein d'une tendance. C'est un outil polyvalent pour analyser et réagir aux marchés.
**TRADEX-AI C1** : Indicateur dérivé des bandes de Bollinger (volatilité/écart-type) ; couche analytique de surachat/survente, jamais déclencheur autonome.
*Catégorie : indicateurs_momentum*

---

### D832 — Six niveaux de relation %B / bandes
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Six niveaux de relation de base :
* %B < 0 quand le prix est **sous** la bande inférieure.
* %B = 0 quand le prix est **à** la bande inférieure.
* %B entre 0 et 0,50 quand le prix est entre bande inférieure et bande médiane (SMA 20).
* %B entre 0,50 et 1 quand le prix est entre bande médiane (SMA 20) et bande supérieure.
* %B = 1 quand le prix est **à** la bande supérieure.
* %B > 1 quand le prix est **au-dessus** de la bande supérieure.
**TRADEX-AI C1** : Échelle de lecture déterministe (bornes 0 / 0,5 / 1) ; permet de coder des zones discrètes de position prix/bandes.
*Catégorie : indicateurs_momentum*

---

### D833 — Formule de calcul du %B
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Formule :
```
%B = (Prix - Bande inférieure) / (Bande supérieure - Bande inférieure)
```
Le réglage par défaut du %B repose sur celui des bandes de Bollinger (20,2) : bandes à deux écarts-types au-dessus et en dessous de la SMA 20 jours (qui est aussi la bande médiane). Le prix du titre est la clôture ou la dernière transaction.
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; dépend du calcul amont des bandes de Bollinger (SMA20 ± 2σ).
*Catégorie : indicateurs_momentum*

---

### D834 — Surachat/survente : toujours dans le sens de la grande tendance
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Le %B identifie surachat/survente, mais il faut savoir lequel chercher : comme la plupart des oscillateurs de momentum, on cherche des situations de **survente court terme quand la tendance moyen terme est haussière**, et de **surachat court terme quand la tendance moyen terme est baissière**. Autrement dit, chercher les opportunités dans le sens de la plus grande tendance (ex. un pullback dans un uptrend). Il faut définir la grande tendance avant de chercher surachat/survente.
**TRADEX-AI C3** : Règle de filtrage directionnel cohérente avec « trader dans le sens de la tendance » ; combinable avec la Direction Belkhayate comme contexte obligatoire avant tout signal %B.
*Catégorie : signal*

---

### D835 — « Walking the band » en tendance forte (Chart 1, AAPL)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md, image_01) : Apple (AAPL) en fort uptrend : le %B est passé au-dessus de 1 plusieurs fois, mais ces lectures « surachat » n'ont pas produit de bons signaux de vente (pullbacks superficiels, AAPL repartant bien au-dessus de la bande inférieure). John Bollinger appelle cela « walking the band » : en forte tendance, les prix peuvent longer la bande supérieure et toucher rarement l'inférieure (et inversement en downtrend fort).
**TRADEX-AI C1** : Garde-fou anti-faux-signal : ne pas vendre sur %B>1 en tendance haussière forte (walking the band) ; éviter les contre-tendances mécaniques.
*Catégorie : signal*

---

### D836 — Survente en uptrend : %B ≤ 0 (Chart 2, QQQQ)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md, image_02) : Après identification d'un grand uptrend, le %B peut être considéré comme **survendu** quand il atteint 0 ou descend en dessous (le prix touche/passe sous la bande inférieure = mouvement à 2 écarts-types sous la SMA 20). Sur le Nasdaq 100 ETF (QQQQ) en uptrend depuis mars 2009, le %B est passé sous zéro trois fois ; les lectures de survente début juillet et début novembre ont fourni de bons points d'entrée (flèches vertes) dans le grand uptrend.
**TRADEX-AI C1** : Seuil de survente %B≤0 en contexte uptrend = point d'entrée pullback ; codable comme déclencheur conditionnel à la tendance dominante.
*Catégorie : signal*

---

### D837 — Système trend-following %B + MFI (Bollinger)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : John Bollinger décrit un système suiveur de tendance avec %B + Money Flow Index (MFI). Un **uptrend** commence quand %B > 0,80 ET MFI(10) > 80 (MFI borné 0-100 ; >80 = haut 20 % de sa plage, lecture forte). Les **downtrends** sont identifiés quand %B < 0,20 ET MFI(10) < 20.
**TRADEX-AI C3** : Règle composite de confirmation de tendance (double condition %B + MFI) ; cohérente avec l'usage du MFI déjà présent dans la KB (Énergie Belkhayate = MFI standard). Filtre, pas déclencheur autonome.
*Catégorie : signal*

---

### D838 — Exemple FedEx %B + MFI(10) et limite risk-reward (Chart 3)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md, image_03) : Sur FedEx (FDX) avec %B et MFI(10) : un uptrend démarre fin juillet quand %B > 0,80 et MFI > 80, confirmé par deux signaux supplémentaires début septembre et mi-novembre. Bons pour l'identification de tendance, mais les traders auraient eu un problème de **risk-reward** après de si grands mouvements : il faut une forte poussée de prix pour pousser %B > 0,80 et MFI(10) > 80 simultanément. Bollinger suggère d'utiliser cette méthode pour identifier la tendance, puis de chercher des niveaux surachat/survente appropriés pour de meilleurs points d'entrée.
**TRADEX-AI C3** : Avertissement R/R explicite : le signal %B+MFI arrive tard dans le mouvement → l'utiliser pour le contexte de tendance, pas pour l'entrée ; cohérent avec le critère R/R ≥ 1:2 du projet.
*Catégorie : signal*

---

### D839 — The Bottom Line : seuils 0,80 / 0,20 et usage combiné
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Le %B quantifie la relation prix/bandes de Bollinger. Lectures > 0,80 = prix près de la bande supérieure ; lectures < 0,20 = prix près de la bande inférieure. Les poussées vers la bande supérieure montrent de la force (parfois interprétables comme surachat) ; les plongées vers l'inférieure montrent de la faiblesse (parfois survente). Beaucoup dépend de la tendance sous-jacente et des autres indicateurs. Le %B a une valeur propre mais est **meilleur combiné** à d'autres indicateurs ou à l'analyse de prix.
**TRADEX-AI C1** : Seuils opérationnels 0,80 / 0,20 ; règle de non-autonomie confirmée (%B = couche d'appoint, jamais signal seul).
*Catégorie : signal*

---

### D840 — Paramétrage SharpCharts (20,2) (Chart 4)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md, image_04) : Le %B figure dans la liste d'indicateurs de SharpCharts. Paramètres par défaut (20,2) basés sur ceux des bandes de Bollinger : 20 = périodes de la SMA, 2 = nombre d'écarts-types pour bandes supérieure/inférieure (modifiables). Le %B peut être positionné au-dessus, en dessous ou derrière le tracé du prix.
**TRADEX-AI C1** : Paramètres de référence (20,2) ; reparamétrables selon timeframe Belkhayate, à figer par backtest.
*Catégorie : indicateurs_momentum*

---

### D841 — Scan %B Uptrend (%B > 0,80 + croisement MFI > 80)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Scan filtrant les titres où %B > 0,80 et MFI vient de croiser au-dessus de 80 (selon Bollinger, possibles débuts de nouvelles hausses) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]
AND [Daily %B(20,2.0,Daily Close) > 0.8]
AND [Daily MFI(14) > 80]
AND [Yesterday's Daily MFI(14) < 80]
```
**TRADEX-AI C3** : Logique de déclenchement haussier (%B haut + croisement MFI) transposable en condition Python comme filtre de confirmation ; syntaxe StockCharts non réutilisable telle quelle. Noter MFI(14) dans le scan vs MFI(10) dans le texte.
*Catégorie : signal*

---

### D842 — Scan %B Downtrend (%B < 0,20 + croisement MFI < 20)
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Scan filtrant les titres où %B < 0,20 et MFI vient de croiser sous 20 (possibles débuts de nouvelles baisses) :
```
[type = stock] AND [country = US]
AND [Daily SMA(20,Daily Volume) > 40000]
AND [Daily SMA(60,Daily Close) > 5]
AND [Daily %B(20,2.0,Daily Close) < 0.2]
AND [Daily MFI(14) < 20]
AND [Yesterday's Daily MFI(14) > 20]
```
**TRADEX-AI C3** : Logique de déclenchement baissier symétrique ; transposable en filtre de confirmation, syntaxe propre à StockCharts (seule la logique compte).
*Catégorie : signal*

---

### D843 — FAQ : synthèse des règles %B
🟢 **FAIT VÉRIFIÉ** (Source : b_indicator.md) : Les FAQ confirment : %B quantifie le prix vs bandes de Bollinger ; il faut identifier d'abord la grande tendance (en uptrend, %B survendu à 0 ou moins ; en downtrend fort, %B suracheté quand il approche/dépasse 1) ; uptrend identifié quand %B > 0,80 et MFI(10) > 80, downtrend quand %B < 0,20 et MFI(10) < 20 ; le système %B + MFI (Bollinger) aide à identifier les directions de tendance significatives ; %B ne signifie pas toujours surachat/survente et est meilleur combiné à d'autres indicateurs ou à l'analyse de prix.
**TRADEX-AI C1** : Récapitulatif cohérent des règles déjà extraites (D831-D839) ; aucun paramètre nouveau, valeur de consolidation.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D831 | Nature %B (position dans bandes) | 🟢 | C1 | indicateurs_momentum |
| D832 | Six niveaux de relation | 🟢 | C1 | indicateurs_momentum |
| D833 | Formule %B = (P−Binf)/(Bsup−Binf) | 🟢 | C1 | indicateurs_momentum |
| D834 | Surachat/survente dans le sens tendance | 🟢 | C3 | signal |
| D835 | Walking the band (AAPL) | 🟢 | C1 | signal |
| D836 | Survente %B≤0 en uptrend (QQQQ) | 🟢 | C1 | signal |
| D837 | Système %B + MFI (Bollinger) | 🟢 | C3 | signal |
| D838 | Exemple FedEx + limite R/R | 🟢 | C3 | signal |
| D839 | Bottom Line : seuils 0,80/0,20 | 🟢 | C1 | signal |
| D840 | Paramétrage SharpCharts (20,2) | 🟢 | C1 | indicateurs_momentum |
| D841 | Scan %B Uptrend | 🟢 | C3 | signal |
| D842 | Scan %B Downtrend | 🟢 | C3 | signal |
| D843 | FAQ : synthèse des règles | 🟢 | C1 | signal |

**Liens Belkhayate :** ⚫🔴 Le %B n'est PAS un indicateur Belkhayate (dérivé des bandes de Bollinger / Bollinger). Lien indirect notable : le système %B + **MFI** rejoint l'usage du MFI dans la KB (mémoire projet : « Énergie Belkhayate = MFI standard, seuils 20/80 ») — convergence d'outil (MFI) mais non d'origine méthodologique. À traiter comme couche de confirmation, jamais substitut à la méthode Belkhayate. Ne rien inventer.

**À vérifier (humain) :**
- Incohérence source MFI(10) vs MFI(14) : le texte (D837/D843) cite MFI(10), mais les scans (D841/D842) utilisent MFI(14). À trancher avant tout codage du paramètre MFI.
- D841/D842 — syntaxe de scan propre à StockCharts ; seule la logique (%B + croisement MFI) est transposable, pas le code.
- Seuil de référence Bollinger %B = 0,80/0,20 vs seuils MFI 80/20 : vérifier la cohérence avec les seuils MFI 20/80 déjà fixés dans la KB Belkhayate.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
