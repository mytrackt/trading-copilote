# Extraction StockCharts — Chart Annotation Tools
**Source :** `bundles/stockcharts/chart_annotation_tools.md` (HTTP 200 · ~1 500 car.) + 0 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 0/0 certifiée (page d'index sans figure)
**Décisions :** D1231 → D1237 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-annotation-tools
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

Aucune image certifiée. Manifest : `.md=0 figures vs HTML=0 images` — page d'index de navigation (table des outils d'annotation), pas de contenu illustré. Alignement non requis.

## DÉCISIONS

> ⚠️ Page d'INDEX uniquement : elle liste 9 outils d'annotation graphique avec une phrase descriptive chacun, sans formule ni règle de trading. Les décisions ci-dessous se limitent au contenu littéral présent (existence et fonction déclarée de chaque outil). Le détail opératoire de chaque outil vit sur sa propre page (à scraper séparément) — NE RIEN inventer ici.

### D1231 — Nature de la page (index des outils d'annotation)
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : La page « Chart Annotation Tools » est une page d'index recensant les outils d'annotation graphique de StockCharts, chacun renvoyant à sa propre page de documentation. Neuf outils sont listés : Andrews' Pitchfork, Cycles (Cycle Lines Tool), Fibonacci Retracements, Fibonacci Arcs, Fibonacci Fans, Fibonacci Time Zones, Quadrant Lines, Raff Regression Channel, Speed Resistance Lines.
**TRADEX-AI C1** : Inventaire d'outils de tracé/structure de marché ; sert de carte de sources à scraper individuellement, pas de règle exploitable en l'état.
*Catégorie : structure_marche*

---

### D1232 — Andrews' Pitchfork (canal de tendance)
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : Andrews' Pitchfork est décrit comme un outil de canal de tendance (« trend channel tool ») ; la page dédiée illustre comment le tracer, l'ajuster et l'interpréter.
**TRADEX-AI C1** : Outil de canal de tendance (3 lignes parallèles à partir de 3 pivots) ; pertinent comme structure de marché pour GC/HG/CL/ZW. Détail à extraire de sa page propre.
*Catégorie : structure_marche*

---

### D1233 — Cycles / Cycle Lines Tool
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : L'entrée « Cycles » présente les étapes pour trouver les cycles et utiliser le Cycle Lines Tool.
**TRADEX-AI C6** : Outil de repérage de cyclicité temporelle (timing) ; rôle potentiel de calendrier/cycle, faible priorité. Détail sur page propre.
*Catégorie : timing*

---

### D1234 — Famille Fibonacci (Retracements, Arcs, Fans, Time Zones)
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : Quatre outils Fibonacci sont listés : Retracements (définis comme servant à identifier des zones de retournement / reversal zones), Arcs (utilisés pour trouver des retournements), Fans (ce qu'ils sont et comment les utiliser), Time Zones (ce qu'ils sont et comment les utiliser).
**TRADEX-AI C1** : Famille d'outils de retracement/projection (niveaux de retournement potentiels) ; les Time Zones touchent au timing. Lien NOTABLE avec la méthode Belkhayate qui emploie des coefficients Fibonacci (0,618 / 1,618 figés dans COGParams) — voir section Liens Belkhayate. Détail formel sur pages propres.
*Catégorie : structure_marche*

---

### D1235 — Quadrant Lines
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : Les Quadrant Lines sont définies comme un outil servant à trouver de futures zones de support et résistance.
**TRADEX-AI C1** : Outil de découpage support/résistance ; structure de marché. Détail sur page propre.
*Catégorie : structure_marche*

---

### D1236 — Raff Regression Channel
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : Le Raff Regression Channel est décrit comme un outil de canal basé sur deux lignes de tendance équidistantes de part et d'autre d'une régression linéaire.
**TRADEX-AI C1** : Canal de régression linéaire ± largeur ; outil de structure/tendance déterministe. Détail sur page propre.
*Catégorie : structure_marche*

---

### D1237 — Speed Resistance Lines
🟢 **FAIT VÉRIFIÉ** (Source : chart_annotation_tools.md) : Les Speed Resistance Lines sont présentées comme des lignes de tendance basées sur le retracement (« retracement-based trend lines ») et leur usage sur les graphiques.
**TRADEX-AI C1** : Lignes de vitesse/retracement (proches des Fibonacci fans) ; structure de marché. Détail sur page propre.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D1231 | Nature index (9 outils listés) | 🟢 | C1 | structure_marche |
| D1232 | Andrews' Pitchfork (canal) | 🟢 | C1 | structure_marche |
| D1233 | Cycles / Cycle Lines Tool | 🟢 | C6 | timing |
| D1234 | Famille Fibonacci (4 outils) | 🟢 | C1 | structure_marche |
| D1235 | Quadrant Lines (S/R futurs) | 🟢 | C1 | structure_marche |
| D1236 | Raff Regression Channel | 🟢 | C1 | structure_marche |
| D1237 | Speed Resistance Lines | 🟢 | C1 | structure_marche |

**Liens Belkhayate :** la page elle-même n'est PAS Belkhayate (⚫). Lien INDIRECT à surveiller (D1234) : la méthode Belkhayate utilise des coefficients Fibonacci 0,618 / 1,618 (figés dans `COGParams`), donc les outils Fibonacci listés ici recoupent l'esprit fibonacci de la méthode — SANS que StockCharts ne fasse aucune référence à Belkhayate. À traiter comme convergence conceptuelle, jamais comme équivalence. Ne rien inventer : aucune formule Belkhayate n'est présente dans cette source.

**À vérifier (humain) :**
- Page d'INDEX seulement : faible densité d'information. Les 9 outils méritent chacun un scrape de leur page dédiée (`/chart-annotation-tools/<slug>.md`) pour en extraire les règles réelles (tracé, niveaux, interprétation). Priorité suggérée : Andrews' Pitchfork + Raff Regression Channel (canaux de tendance, directement utiles structure_marche) et les Fibonacci (lien Belkhayate).
- Manifest signale `0 figures / 0 images` (intégrité « A VERIFIER ») : c'est cohérent avec une page d'index, mais confirmer qu'aucune illustration n'a été perdue au scrape.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
