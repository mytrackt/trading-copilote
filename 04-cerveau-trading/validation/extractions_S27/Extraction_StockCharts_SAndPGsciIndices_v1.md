# Extraction StockCharts — S&P GSCI Indices
**Source :** `bundles/stockcharts/s_and_p_gsci_indices.md` (HTTP 200 · ~1 500 car.) + 1 image certifiée
**Méthode images :** double ancrage (.md figcaption + HTML légende + section fallback) · 1/1 certifiée
**Décisions :** D3531 → D3537 · **Page :** https://chartschool.stockcharts.com/table-of-contents/index-and-market-indicator-catalog/s-and-p-gsci-indices
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

## INVENTAIRE IMAGES CERTIFIÉES

| Image | Label | Section | Statut |
|-------|-------|---------|--------|
| image_01.png | S&P GSCI Indices | Chart Example | CERTIFIE (accord .md + HTML) |

## DÉCISIONS

### D3531 — Définition du S&P GSCI (Goldman Sachs Commodities Index)
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : GSCI signifie Goldman Sachs Commodities Index ; S&P signifie Standard and Poor's. Goldman Sachs a originellement développé cette série d'indices de matières premières pour couvrir les principaux groupes de commodities. Aujourd'hui publié par S&P Dow Jones Indices.
**TRADEX-AI C4** : Indice macro de matières premières (référence inter-marché). Référence de contexte commodities pertinente pour le cadrage macro des actifs TRADING (GC/HG/CL/ZW). Donnée d'analyse, pas de signal direct.
*Catégorie : structure_marche*

---

### D3532 — Pondération selon la production mondiale
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : Ces indices sont pondérés selon la production mondiale, ce qui signifie que les commodities les plus répandues portent le plus de poids.
**TRADEX-AI C4** : Pondération production-mondiale → l'indice est dominé par les commodities à forte production (énergie en tête). Important : le GSCI n'est PAS un proxy équipondéré ; sa lecture macro est biaisée vers l'énergie (pertinent pour CL).
*Catégorie : structure_marche*

---

### D3533 — Couverture sectorielle (5 groupes de commodities)
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : Les indices S&P GSCI couvrent l'énergie, l'agriculture, les métaux précieux, le bétail (livestock) et les métaux industriels.
**TRADEX-AI C4** : Les 5 groupes couvrent les actifs TRADING TRADEX : énergie→CL (Pétrole), agriculture→ZW (Blé), métaux précieux→GC (Or), métaux industriels→HG (Cuivre). Permet un suivi sectoriel inter-marché (C7) par sous-indice.
*Catégorie : structure_marche*

---

### D3534 — Versions « Total Return » vs « Spot »
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : La version « Total Return » de ces indices mesure un investissement futures entièrement collatéralisé, roulé (rolled forward) chaque mois. Les indices basés sur les prix spot ne sont pas soumis aux problèmes de collatéral ou de rollover.
**TRADEX-AI C4** : Distinction de méthodologie : Total Return (intègre roll/collatéral) vs Spot (prix seul). Pour une lecture macro « prix pur » des commodities, privilégier la version Spot ; pour la performance investie, Total Return. Garde-fou de choix de série.
*Catégorie : structure_marche*

---

### D3535 — Détails publication (éditeur, fréquence)
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : Symbol Group : GSCI. Publisher : S&P Dow Jones Indices. Update Frequency : Intraday. Sources en ligne : S&P Dow Jones Indices (spglobal.com/spdji) et Goldman Sachs (goldmansachs.com).
**TRADEX-AI C4** : Métadonnées d'intégration : groupe symbole « GSCI », mise à jour intraday, éditeur S&P DJI. Fréquence intraday compatible avec une surveillance macro de contexte (non temps réel 2s).
*Catégorie : structure_marche*

---

### D3536 — Accès aux symboles (liste à jour StockCharts)
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md) : Les utilisateurs StockCharts accèdent à une liste à jour des symboles de tous les indices S&P GSCI. Depuis cette liste, l'icône « Mentions » à droite d'un symbole donne plus de détails et les mentions récentes (Public ChartLists, articles de blog, etc.).
**TRADEX-AI C4** : Voie d'accès aux symboles GSCI (dépend de StockCharts). Note d'intégration : la liste exacte des symboles n'est pas dans le bundle → à récupérer côté StockCharts si besoin d'un flux GSCI.
*Catégorie : structure_marche*

---

### D3537 — Exemple de graphique GSCI
🟢 **FAIT VÉRIFIÉ** (Source : s_and_p_gsci_indices.md, image_01) : Un exemple de graphique des indices S&P GSCI est fourni (légende « S&P GSCI Indices »), illustrant le rendu d'un indice GSCI sur StockCharts.
**TRADEX-AI C4** : Illustration du rendu graphique d'un indice GSCI. Valeur purement illustrative — aucun paramètre opérationnel.
*Catégorie : structure_marche*

---

## SYNTHÈSE

| D### | Titre | Tag | Cercle | Catégorie |
|------|-------|-----|--------|-----------|
| D3531 | Définition GSCI | 🟢 | C4 | structure_marche |
| D3532 | Pondération production mondiale | 🟢 | C4 | structure_marche |
| D3533 | Couverture 5 groupes commodities | 🟢 | C4 | structure_marche |
| D3534 | Total Return vs Spot | 🟢 | C4 | structure_marche |
| D3535 | Détails publication (éditeur/fréquence) | 🟢 | C4 | structure_marche |
| D3536 | Accès aux symboles | 🟢 | C4 | structure_marche |
| D3537 | Exemple de graphique | 🟢 | C4 | structure_marche |

**Liens Belkhayate :** le S&P GSCI n'a AUCUN lien avec la méthode Belkhayate (⚫ → NON CONCERNÉ). Pertinence projet **modérée** au titre du contexte macro/inter-marché (C4/C7) : indice de commodities couvrant les 4 actifs TRADING (énergie→CL, agri→ZW, précieux→GC, indus→HG), pondéré production mondiale (biais énergie), disponible en versions Total Return et Spot, mise à jour intraday. Utile comme JAUGE de régime commodities en toile de fond, JAMAIS comme déclencheur de signal. Aucune règle d'entrée ne dérive de cette page. Ne rien inventer côté méthode Belkhayate.

**À vérifier (humain) :**
- D3532 — biais de pondération (dominé par l'énergie) : une lecture « commodities » du GSCI sur/représente le pétrole. Pour un suivi équilibré GC/HG/CL/ZW, préférer les SOUS-indices sectoriels plutôt que l'indice global.
- D3534 — choix de série (Total Return vs Spot) à trancher selon l'usage (contexte prix pur → Spot ; performance investie → Total Return).
- D3536 — la liste exacte des symboles GSCI n'est pas dans le bundle ; à récupérer côté StockCharts/S&P DJI si un flux d'intégration est souhaité.
- Cohérence projet : usage strictement macro/contextuel (C4/C7), pas de signal — confirmer avant toute fusion.

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre. Extraction BRUT en zone validation/, NON fusionnée — attend OK utilisateur.
