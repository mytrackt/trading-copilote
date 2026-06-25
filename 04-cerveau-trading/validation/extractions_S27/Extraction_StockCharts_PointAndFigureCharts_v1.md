# Extraction StockCharts — Point and Figure Charts
**Source :** `bundles/stockcharts/point_and_figure_charts.md` (HTTP 200 · ~2 000 car. — page d'introduction) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 1/1 certifiée
**Décisions :** D3131 → D3138 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | P&F chart showing a trendline breakout. | Using P&F Charts To Identify Breakouts | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

> Page courte d'INTRODUCTION (présentation générale des P&F). Extraction des seuls concepts réellement présents — NON paddée (8 décisions).

### D3131 — Objet des P&F : visualiser les breakouts avec confiance
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md) : Les graphiques Point & Figure (P&F) facilitent la VISUALISATION des breakouts et donnent plus de confiance pour les décisions d'investissement/trading. Présentés comme outil pour qui attend qu'un titre casse à la hausse avant de l'ajouter au portefeuille.
**TRADEX-AI C1** : Type de graphique orienté DÉTECTION DE CASSURES ; valeur ajoutée = lisibilité des breakouts. Candidat comme couche de confirmation structurelle.
*Catégorie : structure_marche*

---

### D3132 — Colonnes X et O, type confirmant/complémentaire
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md) : Pour qui est habitué aux barres ou chandeliers, les P&F peuvent sembler inhabituels avec leurs colonnes de X et de O. Une fois compris, ils servent de type de graphique CONFIRMANT ou COMPLÉMENTAIRE.
**TRADEX-AI C1** : Positionnement architectural — le P&F est un graphique de CONFIRMATION/complément, pas un remplaçant des chandeliers (cohérent avec une couche C1 additionnelle).
*Catégorie : structure_marche*

---

### D3133 — Pas de temps sur l'axe X : précision et S/R
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md) : Premier aspect notable (outre les X/O) : il n'y a PAS de temps sur l'axe des X, contrairement aux barres/chandeliers traditionnels. En se familiarisant, on perçoit que les P&F peuvent être PLUS PRÉCIS que les autres types. Ils sont surtout utiles pour identifier les niveaux de support/résistance et reconnaître les breakouts et signaux de tendance.
**TRADEX-AI C1** : Caractéristique structurante — absence d'axe temps = filtrage du bruit temporel, focus prix pur. Force = identification S/R et breakouts. Pertinent pour GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D3134 — Identifier les breakouts via trend lines superposées
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md, image_01) : Le P&F illustré est superposé de trend lines, rendant facile l'identification de l'endroit où le prix a cassé une trend line descendante. Après le breakout, une LONGUE colonne de X indique que le prix a continué d'augmenter — moment idéal pour entrer en position longue.
**TRADEX-AI C1** : Schéma de signal — cassure de trend line descendante + longue colonne de X = entrée longue. Feature : détection de cassure de trend line P&F suivie d'une extension de colonne X.
*Catégorie : signal*

---

### D3135 — Opportunité ré-entrée : breakout dans la colonne X courante
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md, image_01) : Si l'on a manqué la première opportunité, une autre peut se présenter en cas de breakout haussier dans la colonne de X PRÉVALANTE (courante).
**TRADEX-AI C1** : Logique de ré-entrée — un nouveau breakout dans la colonne X en cours offre une seconde entrée. À encadrer par la gestion du risque (pas de poursuite tardive sans stop).
*Catégorie : gestion_risque_entree*

---

### D3136 — Flexibilité : valeur de box et nombre de boxes pour reversal
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md) : Les P&F sont flexibles : on peut changer la VALEUR DES BOXES et le NOMBRE DE BOXES requis pour un reversal (retournement de colonne). Ce paramétrage se règle selon le titre analysé — plus ou moins sensible selon le titre ou le timeframe utilisé.
**TRADEX-AI C1** : Deux paramètres clés codables — box size et reversal amount (nb de boxes). Contrôlent la sensibilité du chart ; à calibrer par actif/timeframe (cf. scaling, bundle basics).
*Catégorie : configuration*

---

### D3137 — Multiples usages, commencer par les bases
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md) : Comme les autres types de graphiques, il existe de nombreuses façons d'appliquer les P&F à l'analyse. Un bon point de départ est de comprendre les bases.
**TRADEX-AI C1** : Renvoi pédagogique vers la section « basics » (bundle `point_and_figure_basics`, D3111+). Pas de mécanique nouvelle ; positionne le P&F comme outil polyvalent.
*Catégorie : structure_marche*

---

### D3138 — Longue colonne de X post-breakout = continuation haussière
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_charts.md, image_01) : Après la cassure de la trend line descendante, l'apparition d'une LONGUE colonne de X traduit la CONTINUATION de la hausse du prix (le mouvement se poursuit dans la même direction).
**TRADEX-AI C1** : Feature de continuation — la longueur de la colonne X post-cassure mesure la force de la continuation haussière (symétrique : longue colonne O = continuation baissière). Indicateur de momentum structurel.
*Catégorie : signal*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3131 | Objet : visualiser breakouts | 🟢 | C1 | structure_marche |
| D3132 | X/O — type confirmant | 🟢 | C1 | structure_marche |
| D3133 | Pas de temps, précision, S/R | 🟢 | C1 | structure_marche |
| D3134 | Breakout via trend lines | 🟢 | C1 | signal |
| D3135 | Ré-entrée colonne X courante | 🟢 | C1 | gestion_risque_entree |
| D3136 | Box value + reversal (sensibilité) | 🟢 | C1 | configuration |
| D3137 | Polyvalence, commencer par bases | 🟢 | C1 | structure_marche |
| D3138 | Longue colonne X = continuation | 🟢 | C1 | signal |

**Liens Belkhayate :** le Point & Figure n'est PAS une méthode Belkhayate (⚫). Aucun lien direct revendiqué. Méthode Belkhayate = Pivots + BGC + Direction + Énergie (MFI), sans colonnes X/O. NON CONCERNÉ — aucun rapprochement à coder.

**À vérifier (humain) :**
- Page d'INTRODUCTION — 8 décisions seulement, NON paddée. Construction détaillée, S/R et signaux de cassure complets sont à chercher dans « Introduction to Point & Figure Charts » (déjà extrait : `Extraction_StockCharts_IntroductionToPointAndFigureCharts_v1.md`) ; éviter les doublons à la fusion.
- D3136 — box size et reversal amount à calibrer (walk-forward) sur la volatilité réelle des futures GC/HG/CL/ZW.
- D3134 / D3135 / D3138 — schémas de breakout/continuation illustrés sur actions ; revalider la fiabilité sur futures avant tout signal automatique.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
