# Extraction StockCharts — Average True Range (ATR)
**Source :** `bundles/stockcharts/average_true_range_atr.md` (HTTP 200 · ~10 800 car.) + 6 images certifiées
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 6/6 certifiées
**Décisions :** D791 → D803 · **Page :** https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-true-range-atr
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | ATR - True Range Image | True Range | CERTIFIE (accord .md + HTML) |
| image_02.png | How To Calculate ATR | How To Calculate ATR [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_03.png | ATR plotted on chart using StockCharts.com - Chart 1 | How To Calculate ATR | CERTIFIE (accord .md + HTML) |
| image_04.png | Absolute ATR | Absolute ATR [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_05.png | Absolute ATR | Absolute ATR [SECTION-FALLBACK] | CERTIFIE (accord .md + HTML) |
| image_06.png | ATR - SharpCharts | Using ATR with SharpCharts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D791 — Nature et origine de l'ATR (Wilder, volatilité)
🔵 **ÉCOLE (Wilder)** (Source : average_true_range_atr.md) : Développé par J. Welles Wilder, l'Average True Range (ATR) est un indicateur qui mesure la **volatilité**. Wilder l'a conçu avec les matières premières et les prix journaliers en tête, les commodities étant souvent plus volatiles que les actions et sujettes aux gaps et limit moves. Une formule basée uniquement sur le range haut-bas échouerait à capter la volatilité des gaps/limit moves : l'ATR capture cette volatilité « manquante ». Point essentiel : **l'ATR n'indique PAS la direction du prix, seulement la volatilité.**
**TRADEX-AI C1** : Mesure de volatilité non directionnelle, pertinente pour des commodities comme GC/HG/CL/ZW (sujettes aux gaps) ; à utiliser comme feature de risque/dimensionnement, jamais comme signal directionnel.
*Catégorie : indicateurs_momentum*

---

### D792 — Source historique : New Concepts in Technical Trading Systems (1978)
🔵 **ÉCOLE (Wilder)** (Source : average_true_range_atr.md) : Wilder présente l'ATR dans son livre de 1978 *New Concepts in Technical Trading Systems*, qui inclut aussi le Parabolic SAR, le RSI et le Directional Movement Concept (ADX). Bien que développés avant l'ère informatique, ces indicateurs restent extrêmement populaires.
**TRADEX-AI C1** : Provenance documentée (Wilder 1978) ; contextualise l'ATR au sein d'une famille d'indicateurs Wilder, valeur de traçabilité.
*Catégorie : indicateurs_momentum*

---

### D793 — Définition du True Range (TR) : le plus grand des 3
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_01) : Wilder part du **True Range (TR)**, défini comme le plus grand des trois éléments suivants :
* Méthode 1. Plus haut courant moins plus bas courant.
* Méthode 2. Plus haut courant moins clôture précédente (valeur absolue).
* Méthode 3. Plus bas courant moins clôture précédente (valeur absolue).
Les valeurs absolues garantissent des nombres positifs (mesure de distance, pas de direction).
**TRADEX-AI C1** : `TR = max(H−L, |H−Cprec|, |L−Cprec|)` — formule déterministe, brique de base de toute volatilité ATR/ATRP/Trailing Stop.
*Catégorie : indicateurs_momentum*

---

### D794 — Quand chaque méthode TR s'applique (outside / gap / inside)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_01) : Si le plus haut courant est au-dessus du plus haut précédent ET le plus bas en dessous du plus bas précédent, on utilise le range haut-bas courant (outside day → Méthode 1). Les méthodes 2 et 3 s'appliquent en cas de gap ou d'inside day. Un gap survient quand la clôture précédente est supérieure au plus haut courant (gap down/limit move potentiel) ou inférieure au plus bas courant (gap up/limit move potentiel). Exemples : (A) petit range haut-bas après gap up → TR = |H courant − clôture précédente| ; (B) petit range après gap down → TR = |L courant − clôture précédente| ; (C) clôture courante dans le range précédent mais petit range → TR = |H courant − clôture précédente|.
**TRADEX-AI C1** : Cas d'usage des 3 méthodes confirmant l'importance des gaps/limit moves sur commodities ; la formule max() couvre automatiquement tous les cas, pas de branchement à coder.
*Catégorie : indicateurs_momentum*

---

### D795 — Formule de lissage ATR (14 périodes, smoothing Wilder)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_02) : L'ATR est typiquement basé sur **14 périodes** (intraday, daily, weekly ou monthly). La première valeur TR = High − Low ; le premier ATR 14 jours = moyenne des TR des 14 derniers jours. Ensuite Wilder lisse en intégrant l'ATR précédent :
```
ATR courant = [(ATR précédent × 13) + TR courant] / 14
```
- Multiplier l'ATR 14 jours précédent par 13.
- Ajouter le TR du jour le plus récent.
- Diviser le total par 14.
**TRADEX-AI C1** : Lissage de Wilder (équivalent EMA de facteur 1/14) implémentable récursivement ; paramètre 14 reparamétrable selon timeframe Belkhayate.
*Catégorie : indicateurs_momentum*

---

### D796 — Dépendance aux données initiales et précision (≥250 périodes)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_03) : Comme pour les EMA, les valeurs d'ATR dépendent du point de départ du calcul. La « vraie » formule ATR démarre au jour 15 ; les deux premières valeurs (TR initial = H−L, premier ATR = moyenne des 14 TR) « persistent » et affectent légèrement les valeurs suivantes. Les valeurs d'un petit sous-ensemble peuvent ne pas correspondre exactement au graphique ; l'arrondi décimal influe aussi. StockCharts calcule sur **au moins 250 périodes** (souvent bien plus) pour assurer la précision.
**TRADEX-AI C1** : Garde-fou d'implémentation : prévoir un historique de warmup ≥250 périodes avant d'exploiter une valeur ATR ; ne pas trader sur un ATR sous-échantillonné.
*Catégorie : indicateurs_momentum*

---

### D797 — ATR absolu (non comparable entre titres)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_04, image_05) : L'ATR repose sur le True Range qui utilise des variations de prix **absolues** : l'ATR reflète la volatilité à un niveau absolu, **pas en pourcentage** de la clôture. Les titres à bas prix ont donc des ATR plus faibles que les titres à prix élevé (ex. un titre 20-30 $ aura un ATR bien plus bas qu'un titre 200-300 $). Les valeurs d'ATR ne sont **pas comparables** entre titres ; de grands mouvements (ex. 70 → 20) rendent les comparaisons long terme peu pratiques. Google montre des ATR à deux chiffres, Microsoft sous 1, mais leurs lignes ATR ont des formes similaires.
**TRADEX-AI C1** : Limite majeure : ne jamais comparer l'ATR brut entre actifs (GC vs HG vs CL vs ZW ont des échelles de prix différentes) → utiliser l'ATRP (% ) pour toute comparaison inter-actifs.
*Catégorie : indicateurs_momentum*

---

### D798 — The Bottom Line : ATR non directionnel, validateur de mouvement
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md) : L'ATR n'est pas un indicateur directionnel comme MACD ou RSI ; c'est un indicateur de volatilité unique qui reflète le degré d'intérêt/désintérêt pour un mouvement. De grands ranges/True Ranges accompagnent souvent les mouvements forts (dans les deux sens), surtout en début de mouvement ; des ranges relativement étroits accompagnent les mouvements de faible volatilité. L'ATR peut **valider l'enthousiasme** derrière un mouvement ou une cassure : un retournement haussier avec ATR accru montre une forte pression acheteuse et renforce le retournement ; une cassure de support baissière avec ATR accru montre une forte pression vendeuse.
**TRADEX-AI C3** : Rôle de confirmation/validation d'une cassure ou d'un retournement (force du mouvement), combinable avec la BGC/Direction Belkhayate ; ne génère pas seul de signal.
*Catégorie : signal*

---

### D799 — Paramétrage SharpCharts (défaut 14, variante Wilder 8)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_06) : Sur SharpCharts, l'ATR figure dans le menu déroulant « Average True Range ». La boîte de paramètres contient la valeur par défaut **14** (nombre de périodes de lissage). Dans son travail, Wilder utilisait souvent un ATR **8 périodes**. L'indicateur peut être positionné au-dessus, en dessous ou derrière le tracé du prix ; une moyenne mobile peut être ajoutée pour repérer les hausses/baisses de l'ATR (via « advanced options »).
**TRADEX-AI C1** : Paramètres de référence (14 par défaut, 8 chez Wilder) ; une MA sur l'ATR sert à détecter les expansions/contractions de volatilité — feature exploitable comme filtre de régime.
*Catégorie : indicateurs_momentum*

---

### D800 — Scan « Weeding Out High Volatility » (ATR converti en %)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md) : L'ATR peut servir dans des scans pour écarter les titres à très haute volatilité. Exemple : titres S&P 600 en uptrend, dernière clause excluant la haute volatilité. L'ATR est converti en une sorte de pourcentage pour permettre la comparaison entre titres sur la même échelle :
```
[group is SP600]
AND [Daily EMA(50,close) > Daily EMA(200,close)]
AND [ATR(250) / SMA(20,Close) * 100 < 4]
```
**TRADEX-AI C1** : Confirme que la comparaison inter-titres exige une normalisation `ATR / prix × 100` ; logique transposable en filtre de régime de volatilité (la syntaxe de scan StockCharts n'est pas réutilisable telle quelle, seule la logique compte).
*Catégorie : structure_marche*

---

### D801 — Image 02 : illustration tabulaire du calcul ATR
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_02) : La feuille de calcul illustrée montre le début d'un calcul ATR : la première valeur True Range (0,91) = High − Low (cellules jaunes) ; le premier ATR 14 jours (0,56) = moyenne des 14 premières valeurs True Range (cellule bleue) ; les valeurs ATR suivantes sont lissées via la formule de Wilder.
**TRADEX-AI C1** : Valeurs numériques d'exemple (TR=0,91 ; ATR=0,56) confirmant la procédure d'initialisation ; valeur illustrative pour validation d'un prototype de calcul.
*Catégorie : indicateurs_momentum*

---

### D802 — Image 03 : ATR tracé sur QQQ (surge en mai)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_03) : Les valeurs de la feuille de calcul correspondent à la zone jaune du graphique ; l'ATR a fortement augmenté lorsque QQQ a plongé en mai avec de nombreuses longues bougies (longs candlesticks).
**TRADEX-AI C1** : Confirme empiriquement le lien « chute marquée + grandes bougies → expansion ATR » ; renforce l'usage de l'ATR comme détecteur d'expansion de volatilité.
*Catégorie : indicateurs_momentum*

---

### D803 — Images 04/05 : comparaison Google vs Microsoft (échelles)
🟢 **FAIT VÉRIFIÉ** (Source : average_true_range_atr.md, image_04, image_05) : Les graphiques comparent un titre à ATR à deux chiffres (Google) et un titre à ATR sous 1 (Microsoft) ; malgré des valeurs très différentes, leurs lignes ATR ont des formes similaires, illustrant la non-comparabilité des niveaux absolus mais la similarité des dynamiques.
**TRADEX-AI C1** : Illustration de la limite « niveau absolu non comparable / forme comparable » ; appuie le passage à l'ATRP pour comparer GC/HG/CL/ZW.
*Catégorie : indicateurs_momentum*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D791 | Nature/origine ATR (Wilder, volatilité) | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D792 | Source New Concepts (1978) | 🔵 ÉCOLE | C1 | indicateurs_momentum |
| D793 | Définition True Range (max des 3) | 🟢 | C1 | indicateurs_momentum |
| D794 | Application des 3 méthodes TR | 🟢 | C1 | indicateurs_momentum |
| D795 | Formule lissage ATR (14) | 🟢 | C1 | indicateurs_momentum |
| D796 | Précision / warmup ≥250 | 🟢 | C1 | indicateurs_momentum |
| D797 | ATR absolu non comparable | 🟢 | C1 | indicateurs_momentum |
| D798 | Bottom Line : validateur non directionnel | 🟢 | C3 | signal |
| D799 | Paramétrage SharpCharts (14 / 8) | 🟢 | C1 | indicateurs_momentum |
| D800 | Scan high volatility (ATR en %) | 🟢 | C1 | structure_marche |
| D801 | Image 02 : calcul tabulaire | 🟢 | C1 | indicateurs_momentum |
| D802 | Image 03 : ATR sur QQQ | 🟢 | C1 | indicateurs_momentum |
| D803 | Images 04/05 : Google vs Microsoft | 🟢 | C1 | indicateurs_momentum |

**Liens Belkhayate :** ⚫🔴 L'ATR n'est PAS un indicateur Belkhayate. Lien indirect : volatilité non directionnelle utile au dimensionnement de position et au placement de stops (cf. ATR Trailing Stops) ; pertinent pour des commodities sujettes aux gaps (GC/HG/CL/ZW) mais sans assise dans la méthode Belkhayate. Ne rien inventer.

**À vérifier (humain) :**
- D793 — la catégorie est « indicateurs_momentum » par cohérence taxonomique du dépôt, mais l'ATR est strictement un indicateur de **volatilité** (non momentum/non directionnel, cf. D791/D798) ; le choix de catégorie est à arbitrer côté humain.
- D800 — syntaxe de scan propre à StockCharts ; seule la logique `ATR/prix×100` est transposable.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
