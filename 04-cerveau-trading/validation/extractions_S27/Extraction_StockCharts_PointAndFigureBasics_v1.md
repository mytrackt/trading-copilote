# Extraction StockCharts — Point and Figure Basics
**Source :** `bundles/stockcharts/point_and_figure_basics.md` (HTTP 200 · ~1 600 car. — page d'index/sommaire) + 0 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 0/0 — aucune image (page d'index)
**Décisions :** D3111 → D3116 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/point-and-figure-charts/point-and-figure-basics
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée. Le manifest signale « .md=0 figures vs HTML=0 images » — page de SOMMAIRE/index sans figure. Aucune image à intégrer.

## DÉCISIONS

> Page courte de type INDEX (sommaire de la sous-section P&F Basics). Extraction des seuls concepts réellement présents — NON paddée (6 décisions seulement, cohérent avec le contenu).

### D3111 — Principe P&F : colonnes de X et de O, focus sur le prix
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : Les graphiques Point & Figure (P&F) se concentrent sur le MOUVEMENT du prix via des colonnes de X et de O. Les colonnes de X représentent des prix EN HAUSSE, les colonnes de O des prix EN BAISSE. Ces colonnes facilitent l'identification des cassures (breakouts), qui peuvent à leur tour générer des signaux d'achat ou de vente.
**TRADEX-AI C1** : Type de graphique de STRUCTURE (prix pur, sans le temps) candidat comme couche d'analyse de breakouts. X = hausse, O = baisse. Pertinent pour visualiser les cassures sur GC/HG/CL/ZW.
*Catégorie : structure_marche*

---

### D3112 — Personnalisation des graphiques P&F (StockCharts)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : Les P&F de StockCharts.com sont modifiables : on peut changer les attributs du graphique, le scaling (échelle), et ajouter des overlays comme les trend lines, les moyennes mobiles et le Volume by Price.
**TRADEX-AI C1** : Détail outil — les paramètres P&F (échelle, overlays) sont configurables ; renvoie aux pages spécialisées (scaling/timeframes, trend lines, indicateurs) traitées dans les bundles voisins.
*Catégorie : configuration*

---

### D3113 — Sous-page « Introduction to P&F Charts » (construction pas-à-pas)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : La page renvoie à « Introduction to Point & Figure Charts » : apprend à construire un P&F via un exemple pas-à-pas, à identifier les niveaux de support/résistance et à tracer les trend lines P&F.
**TRADEX-AI C1** : Renvoi de structure documentaire — contenu détaillé couvert par le bundle `point_and_figure_charts` (construction, S/R, trend lines). Lien d'index, pas de fait technique nouveau.
*Catégorie : structure_marche*

---

### D3114 — Sous-page « P&F Scaling and Timeframes »
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : Renvoi à « P&F Scaling and Timeframes » : apprend à appliquer différents intervalles de prix pour choisir un timeframe. Les intervalles intraday servent aux timeframes moyen terme ; les intervalles quotidiens sont souvent les meilleurs pour les graphiques long terme.
**TRADEX-AI C1** : Fait exploitable — le choix de l'intervalle (box size) détermine le timeframe effectif : intraday → moyen terme, daily → long terme. Paramétrage à recalibrer par actif.
*Catégorie : configuration*

---

### D3115 — Sous-page « P&F Trend Lines » (angle fixe, 45°)
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : Renvoi à « P&F Trend Lines » : les trend lines P&F sont UNIQUES car tracées à un angle SPÉCIFIQUE représentant un taux d'ascension/descente donné. La page explique comment les trend lines automatiques apparaissent, quand elles s'inversent, et comment identifier une cassure.
**TRADEX-AI C1** : Fait exploitable — les trend lines P&F sont AUTOMATIQUES et à angle fixe (déterministe), contrairement aux trend lines discrétionnaires. Candidat pour un tracé S/R objectif/reproductible.
*Catégorie : structure_marche*

---

### D3116 — Objet de la section : créer, intervalles, timeframes, trend lines auto
🟢 **FAIT VÉRIFIÉ** (Source : point_and_figure_basics.md) : La section couvre « toutes les bases » des P&F : créer un P&F, utiliser les intervalles de prix et timeframes appropriés, et mieux comprendre les trend lines automatiques.
**TRADEX-AI C1** : Synthèse de périmètre de la section P&F Basics ; aucune mécanique chiffrée ici (page d'index) — le détail vit dans les bundles `point_and_figure_charts` et `point_and_figure_indicators`.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3111 | Principe X/O (hausse/baisse) | 🟢 | C1 | structure_marche |
| D3112 | Personnalisation P&F | 🟢 | C1 | configuration |
| D3113 | Renvoi Intro P&F (construction) | 🟢 | C1 | structure_marche |
| D3114 | Renvoi Scaling & Timeframes | 🟢 | C1 | configuration |
| D3115 | Renvoi Trend Lines (angle fixe) | 🟢 | C1 | structure_marche |
| D3116 | Périmètre section P&F Basics | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** le Point & Figure n'est PAS une méthode Belkhayate (⚫). Aucun lien direct revendiqué. La méthode Belkhayate repose sur Pivots + BGC + Direction + Énergie (MFI) et non sur les colonnes X/O. NON CONCERNÉ — aucun rapprochement à coder.

**À vérifier (humain) :**
- Page d'INDEX/sommaire — 6 décisions seulement, NON paddée. Le contenu technique réel (construction, S/R, breakouts, indicateurs) est dans les bundles `point_and_figure_charts` (D3131+) et `point_and_figure_indicators` (D3151+) ; éviter les doublons lors de la fusion.
- D3114 / D3115 — intervalle (box size) et angle des trend lines à recalibrer sur la volatilité réelle des futures GC/HG/CL/ZW (walk-forward).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
