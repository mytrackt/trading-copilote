# Extraction StockCharts — US Treasury Yields
**Source :** `bundles/stockcharts/us_treasury_yields.md` (HTTP 200) + 1 image certifiée
**Méthode images :** double ancrage · 1/1 certifiée · 0 à vérifier
**Décisions :** D4791 → D4793 · **Page :** https://chartschool.stockcharts.com/table-of-contents/index-and-market-indicator-catalog/us-treasury-yields

**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
> 🔎 Pertinent TRADEX : les rendements Treasury sont des indicateurs macro C4 (taux Fed, contexte macro) influençant GC (or — corrélation inverse taux réels) et DX (Dollar Index).

## INVENTAIRE IMAGES CERTIFIÉES
| Image | Label certifié | Section | Décision liée |
|-------|----------------|---------|---------------|
| /files/SkPkjBGJo6KGji3yho2T | US Treasury Yields — $UST5Y avec MA50 et MA200 | Chart Example | D4791 |

---

## DÉCISIONS

### D4791 — Relation inverse prix/rendement Treasury
🟢 **FAIT VÉRIFIÉ** (Source : us_treasury_yields.md, /files/SkPkjBGJo6KGji3yho2T) : Les rendements des Treasury (Bills court terme, Notes moyen terme, Bonds long terme) évoluent en sens inverse des prix des Treasury. Quand les prix des Treasury baissent, les rendements montent ; quand les prix montent, les rendements baissent. Source officielle : US Treasury, données End-of-Day.
**TRADEX-AI C4** : Sur GC (or), les rendements réels des Treasury 10Y ($UST10Y) évoluent en corrélation inverse avec l'or — hausse des rendements réels = pression baissière sur GC. Intégrer ce signal dans le Cercle C4 (Macro) comme filtre de confirmation.
*Catégorie : macro_evenements*

### D4792 — Symboles disponibles StockCharts pour les Treasury Yields
🟢 **FAIT VÉRIFIÉ** (Source : us_treasury_yields.md) : StockCharts publie les rendements Treasury sous la série de symboles "US Treasury Yield Indicators" (groupe de symboles $UST). Exemple : $UST5Y = rendement 5 ans avec possibilité d'appliquer MA50 et MA200. Mise à jour End-of-Day uniquement, données publiées par le US Treasury (home.treasury.gov).
**TRADEX-AI C4** : Dans TRADEX-AI, utiliser $UST10Y (rendement 10 ans) et $UST2Y (rendement 2 ans) comme indicateurs macro du Cercle C4. La courbe de taux (spread 10Y-2Y) est un indicateur avancé de récession influençant GC et ES.
*Catégorie : macro_evenements*

### D4793 — Utilisation des moyennes mobiles sur les rendements Treasury
🟢 **FAIT VÉRIFIÉ** (Source : us_treasury_yields.md, /files/SkPkjBGJo6KGji3yho2T) : L'exemple de chart montre $UST5Y avec MA50 et MA200 comme outil standard d'analyse de tendance sur les rendements. La MA200 délimite le régime haussier ou baissier des taux.
**TRADEX-AI C4** : Appliquer MA50/MA200 sur $UST10Y dans le contexte TRADEX-AI — si $UST10Y > MA200 (tendance de taux haussière), le contexte macro est défavorable à l'or (GC) en biais long ; favoriser les signaux Belkhayate courts sur GC ou attendre confirmation supplémentaire.
*Catégorie : correlations*

