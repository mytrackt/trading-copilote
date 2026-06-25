# Extraction StockCharts — Average True Range Percent (ATRP)
**Source :** `bundles/stockcharts/average_true_range_percent_atrp.md` (HTTP 200 · ~7 200 car.) + 3 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 3/3 certifiées
**Décisions :** D811 → D818 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-percent-atrp
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | What is Average True Range Percent (ATRP)? | What is Average True Range Percent (ATRP)? [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_02.png | ATRP increases during strong moves and decreases during trading ranges | Interpreting ATRP | CERTIFIE (accord .md + HTML) |
| image_03.png | Using with StockChartsACP | Using with StockChartsACP [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D811 — Nature de l'ATRP (volatilité normalisée)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md, image_01) : L'Average True Range Percent (ATRP) est un indicateur qui mesure la **volatilité** d'un titre. L'ATRP est plus faible quand le titre est en range et monte lors de changements de prix dramatiques dans l'une ou l'autre direction.
**TRADEX-AI C1** : Mesure de volatilité normalisée, candidate pour qualifier le régime de volatilité (range vs expansion) sur GC/HG/CL/ZW ; feature de risque, jamais déclencheur d'ordre.
*Catégorie : indicateurs_momentum*

---

### D812 — Origine : variante de l'ATR de Wilder, correction de la limite d'échelle
🔵 **ÉCOLE (Wilder, dérivé)** (Source : average_true_range_percent_atrp.md) : L'ATRP est une variante de l'Average True Range (ATR), indicateur de volatilité populaire développé par Welles Wilder. L'ATR a une limitation : ses valeurs sont liées au prix du sous-jacent, donc les titres à prix élevé ont toujours un ATR plus élevé que les titres à bas prix, indépendamment de leur volatilité relative. L'ATRP corrige cela en exprimant la valeur ATR en **pourcentage du prix**, plaçant toutes les mesures de volatilité sur la même échelle et facilitant la comparaison de titres aux prix très différents.
**TRADEX-AI C1** : Résout la non-comparabilité de l'ATR brut (cf. ATR D797) ; l'ATRP est l'outil adapté pour comparer la volatilité entre GC/HG/CL/ZW sur une échelle commune.
*Catégorie : indicateurs_momentum*

---

### D813 — Formule de calcul ATRP
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md) : L'ATRP se calcule en divisant la valeur ATR par le prix de clôture et en multipliant par 100.
```
ATRP = (ATR / Close) * 100
```
(Se référer à l'article ATR pour le calcul de la valeur ATR.)
**TRADEX-AI C1** : Formule déterministe implémentable telle quelle ; dépend du calcul ATR amont (True Range + lissage Wilder).
*Catégorie : indicateurs_momentum*

---

### D814 — Interprétation : bas en range, haut en mouvement fort
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md, image_02) : Comme l'ATR, l'ATRP reste bas pendant les ranges et monte lors de changements de prix dramatiques dans les deux sens. Exemple XLY : l'ATRP monte fortement à la chute du prix en mars-avril, culminant à **4,48 %** mi-avril. Le prix remonte lentement de mai à septembre dans un range si serré que la volatilité reste basse. La chute de mi-novembre n'est pas assez forte/soutenue pour provoquer plus qu'une petite hausse de l'ATRP, culminant à **1,99 %**.
**TRADEX-AI C1** : Confirme l'usage comme jauge de régime (range vs expansion) ; valeurs % directement interprétables comme seuils de volatilité.
*Catégorie : structure_marche*

---

### D815 — Comparabilité inter-titres (avantage clé du %)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md) : Parce que les valeurs ATRP sont exprimées en pourcentage du prix, elles peuvent être comparées aux pics de volatilité sur les graphiques d'autres symboles.
**TRADEX-AI C3** : Propriété de comparabilité essentielle pour une matrice de volatilité inter-actifs (GC/HG/CL/ZW + confirmation ES/VX) ; soutient une lecture relative du risque.
*Catégorie : indicateurs_momentum*

---

### D816 — The Bottom Line : ATRP non directionnel
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md) : Comme l'ATR, l'ATRP n'est **pas** un indicateur directionnel ; c'est un indicateur de volatilité unique reflétant le degré d'intérêt/désintérêt pour un mouvement. De grands ranges accompagnent souvent les mouvements forts (dans les deux sens), surtout en début de mouvement ; des ranges étroits accompagnent les mouvements de faible volatilité. Exprimé en % du prix, l'ATRP aide à comparer les valeurs de plusieurs titres pour déterminer lesquels sont les plus volatils.
**TRADEX-AI C1** : Réaffirme la nature non directionnelle ; rôle de feature de volatilité et de comparaison, jamais de signal directionnel.
*Catégorie : indicateurs_momentum*

---

### D817 — Paramétrage StockChartsACP (14 périodes par défaut)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md, image_03) : L'indicateur s'ajoute depuis le panneau Chart Settings d'un graphique StockChartsACP et peut être positionné au-dessus ou en dessous du tracé du prix. Par défaut, il est calculé sur **14 périodes** ; ce paramètre est ajustable selon les besoins d'analyse technique.
**TRADEX-AI C1** : Paramètre par défaut 14 (cohérent avec l'ATR) ; reparamétrable selon timeframe Belkhayate (15min / Range Bar).
*Catégorie : indicateurs_momentum*

---

### D818 — Scan « Weeding Out High Volatility » (ATRP < 4 %)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_percent_atrp.md) : L'ATRP peut servir dans des scans pour écarter les titres à très haute volatilité. Exemple : titres S&P 600 en uptrend, dernière clause excluant ceux dont l'ATRP moyen dépasse 4 % sur la dernière année. Comme l'ATRP est exprimé en % du prix, il est idéal pour comparer la volatilité de différents titres :
```
[group is SP600]
AND [Daily EMA(50,close) > Daily EMA(200,close)]
AND [ATRP(250) < 4]
```
**TRADEX-AI C1** : Logique de filtre de volatilité (seuil ATRP < 4 %) directement transposable en condition Python comme garde-fou ; la syntaxe de scan StockCharts n'est pas réutilisable telle quelle, seule la logique compte.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D811 | Nature ATRP (volatilité normalisée) | 🟢 | C1 | indicateurs_momentum |
| D812 | Origine / correction limite d'échelle ATR | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D813 | Formule ATRP = (ATR/Close)×100 | 🟢 | C1 | indicateurs_momentum |
| D814 | Interprétation range/mouvement (XLY) | 🟢 | C1 | structure_marche |
| D815 | Comparabilité inter-titres | 🟢 | C3 | indicateurs_momentum |
| D816 | Bottom Line : non directionnel | 🟢 | C1 | indicateurs_momentum |
| D817 | Paramétrage ACP (14) | 🟢 | C1 | indicateurs_momentum |
| D818 | Scan ATRP < 4 % | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** ⚫🔴 L'ATRP n'est PAS un indicateur Belkhayate. Lien indirect : volatilité normalisée permettant la comparaison inter-actifs (GC/HG/CL/ZW) — utile pour une matrice de risque/régime et le dimensionnement de position, sans assise dans la méthode Belkhayate. Ne rien inventer.

**À vérifier (humain) :**
- Catégorie « indicateurs_momentum » retenue par cohérence taxonomique du dépôt, mais l'ATRP est strictement un indicateur de **volatilité** non directionnel (cf. D816) ; arbitrage de catégorie côté humain.
- D818 — syntaxe de scan propre à StockCharts ; seule la logique (seuil ATRP %) est transposable.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
