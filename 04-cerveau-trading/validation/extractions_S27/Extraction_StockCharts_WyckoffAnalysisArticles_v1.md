# Extraction StockCharts — Wyckoff Analysis Articles
**Source :** `bundles/stockcharts/wyckoff_analysis_articles.md` (HTTP 200) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 images présentes dans le bundle · 0 à vérifier
**Décisions :** D4911 → D4930 · **Page :** https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : Page d'index des articles Wyckoff — contenu limité à 3 résumés de sous-articles (Market Analysis, Stock Analysis, Tutorial). Le contenu détaillé Wyckoff (phases, cycles prix, offre/demande) est dans les sous-pages non incluses dans ce bundle.

---

## NOTE D'EXTRACTION
Ce bundle est une **page d'index** contenant uniquement 3 liens vers des sous-articles avec leurs descriptions courtes. Le contenu substantiel Wyckoff (méthode complète, 5 étapes, cycles de prix, tests achat/vente, guide P&F) réside dans les sous-pages :
- `/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-market-analysis`
- `/table-of-contents/market-analysis/wyckoff-analysis-articles/wyckoff-stock-analysis`
- `/table-of-contents/market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial`

Ces sous-pages constituent 3 bundles distincts à scraper en priorité pour enrichir la KB Wyckoff.

---

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| *(aucune image dans le bundle)* | — | — | — |

---

## DÉCISIONS

### D4911 — Wyckoff Market Analysis : analyser la tendance large du marché
🔵 **ÉCOLE** (Source : wyckoff_analysis_articles.md) : L'approche Wyckoff d'analyse du marché global couvre : (1) définir la tendance large du marché, (2) identifier les tops et bottoms majeurs, (3) projeter les prix, (4) déterminer la position du prix dans le mouvement en cours.
**TRADEX-AI C3** : Applicable à TRADEX-AI via ES (S&P 500) comme indicateur de marché global — identifier les tops/bottoms Wyckoff sur ES constitue un filtre institutionnel (C3) : si ES est en phase de distribution Wyckoff, les signaux ACHETER sur GC/CL/ZW doivent être filtrés (contexte macro hostile).
*Catégorie : structure_marche*

---

### D4912 — Wyckoff Stock Analysis : isoler les groupes forts, sélectionner les meilleurs actifs
🔵 **ÉCOLE** (Source : wyckoff_analysis_articles.md) : La méthode Wyckoff de sélection d'actifs individuel couvre : (1) isoler les groupes les plus forts, (2) choisir les meilleurs actifs au sein de ces groupes, (3) gérer le trade une fois en position.
**TRADEX-AI C3** : Adapté à TRADEX-AI : parmi les 4 actifs tradables (GC/HG/CL/ZW), identifier lequel est dans la phase Wyckoff la plus favorable (accumulation) avant de prioriser son signal — si GC est en accumulation Wyckoff et HG en distribution, allouer la priorité à GC.
*Catégorie : structure_marche*

---

### D4913 — Wyckoff Method Tutorial : 5 étapes, cycle de prix, offre/demande
🔵 **ÉCOLE** (Source : wyckoff_analysis_articles.md) : Le tutoriel de la méthode Wyckoff couvre : (1) l'approche en 5 étapes de Wyckoff, (2) son cycle de prix, (3) l'analyse offre/demande, (4) les tests achat et vente, (5) le guide de comptage P&F. Ces 5 éléments forment la structure complète de la méthode.
**TRADEX-AI C3** : Les 5 étapes Wyckoff et le cycle de prix (accumulation → markup → distribution → markdown) sont directement applicables à GC/CL — intégrer dans la KB comme couche de contexte institutionnel C3. Les tests achat Wyckoff peuvent confirmer les signaux d'entrée Belkhayate.
*Catégorie : structure_marche*

---

### D4914 — Wyckoff : analyse top-down (marché → secteur → actif)
🟡 **SYNTHÈSE** (Source : wyckoff_analysis_articles.md) : La méthode Wyckoff s'applique de manière hiérarchique — d'abord le marché global (broad market trend), puis les groupes sectoriels les plus forts, enfin les actifs individuels au sein de ces groupes. Cette approche top-down garantit que l'actif sélectionné bénéficie d'un vent favorable à tous les niveaux.
**TRADEX-AI C3** : Dans TRADEX-AI, l'architecture respecte cette logique top-down : (1) ES/VX pour le contexte global (C5 sentiment + C4 macro), (2) DX pour le secteur commodités-dollar (C4), (3) GC/HG/CL/ZW pour le signal actif individuel (C1). Wyckoff valide cette hiérarchie.
*Catégorie : structure_marche*

---

### D4915 — Wyckoff : identifier tops et bottoms majeurs
🔵 **ÉCOLE** (Source : wyckoff_analysis_articles.md) : L'analyse Wyckoff inclut des méthodes pour identifier les tops (phases de distribution) et les bottoms majeurs (phases d'accumulation) du marché — essentiels pour éviter d'acheter en haut d'une distribution ou de vendre en bas d'une accumulation.
**TRADEX-AI C1** : Les tops et bottoms Wyckoff sur GC (Or) correspondent souvent aux zones de pivots Belkhayate et aux niveaux de support/résistance clés — une convergence Wyckoff + pivot Belkhayate renforce la qualité du signal (score /10 augmenté).
*Catégorie : structure_marche*

---

### D4916 — Wyckoff : projection de prix et position dans le mouvement
🔵 **ÉCOLE** (Source : wyckoff_analysis_articles.md) : La méthode Wyckoff permet de projeter des objectifs de prix et de déterminer à quelle position dans un mouvement on se trouve — essentiel pour le calcul du R/R (Risk/Reward).
**TRADEX-AI C1** : Règle critique TRADEX-AI : signal valide si R/R ≥ 1:2. La projection Wyckoff de l'objectif de prix (fin de markup) fournit une estimation du target — si le target Wyckoff donne un R/R < 1:2, le signal est invalide même si tous les autres critères sont réunis.
*Catégorie : gestion_risque_entree*

---

### D4917 — Wyckoff : analyse offre/demande comme fondement
🟡 **SYNTHÈSE** (Source : wyckoff_analysis_articles.md) : L'analyse Wyckoff est fondée sur l'offre et la demande — les phases de prix (accumulation, markup, distribution, markdown) reflètent les changements dans l'équilibre offre/demande. La lecture des volumes accompagnant les mouvements de prix est centrale à la méthode.
**TRADEX-AI C2** : Lien direct avec l'Order Flow (C2) dans TRADEX-AI — les données ATAS (footprint, delta, big trades) mesurent exactement cet équilibre offre/demande en temps réel sur GC/HG/CL/ZW. Un signal de demande ATAS en phase d'accumulation Wyckoff est doublement confirmé.
*Catégorie : volume_liquidite*

---

### D4918 — PRIORITÉ SCRAPING : 3 sous-pages Wyckoff manquantes
⚫ **HYPOTHÈSE PROJET** (Source : wyckoff_analysis_articles.md — analyse index) : Ce bundle est une page d'index uniquement. Les 3 sous-articles Wyckoff substantiels sont non-scraped dans ce bundle :
- `wyckoff-market-analysis` → analyse marché global, tops/bottoms, projection
- `wyckoff-stock-analysis` → sélection actifs, gestion trade
- `the-wyckoff-method-a-tutorial` → 5 étapes, cycle prix, tests achat/vente, P&F counting

Ces 3 pages représentent un gisement prioritaire pour la KB TRADEX-AI (contexte institutionnel C3, structure de marché C1).
**TRADEX-AI C3** : Ajouter ces 3 URLs à la file de scraping StockCharts pour la prochaine session — estimation : 30 à 50 décisions KB supplémentaires sur la méthode Wyckoff complète.
*Catégorie : structure_marche*
