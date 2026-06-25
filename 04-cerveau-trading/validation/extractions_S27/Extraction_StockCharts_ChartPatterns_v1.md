# Extraction StockCharts — Chart Patterns (page index)

**Source :** `bundles/stockcharts/chart_patterns.md` (HTTP 200 · ~7 880 car.) + 0 images certifiées
**Méthode images :** double ancrage · 0/0 certifiées (.md=0 figures vs HTML=0 images)
**Décisions :** D1251 → D1255 · **Page :** https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-patterns
**Statut :** BRUT — zone validation/, NON fusionné (attend OK utilisateur)
> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.

> **NATURE DE LA PAGE :** page d'INDEX (liste de liens vers chaque pattern). Contenu propre faible. NON PADDÉ — seules les définitions/taxonomie réellement présentes sur la page sont extraites. Les patterns individuels (Double Top, H&S, etc.) ont leurs propres pages non incluses dans ce bundle.

## INVENTAIRE IMAGES CERTIFIÉES
Aucune image certifiée (manifest : .md=0 figures vs HTML=0 images — alignement impossible).

## DÉCISIONS

### D1251 — Définition d'un chart pattern (supply/demand visuel)
🟢 **FAIT VÉRIFIÉ** (Source : chart_patterns.md) : « Chart patterns provide a visual representation of the battle between buyers and sellers so you see if a market is trending higher, lower, or moving sideways. » Les prix sont déterminés par les forces d'offre et de demande.
**TRADEX-AI C1** : Un pattern graphique = lecture visuelle du rapport de force acheteurs/vendeurs sur GC·HG·CL·ZW. Sert à qualifier l'état directionnel (haussier / baissier / range) en amont d'un signal.
*Catégorie : structure_marche*

---

### D1252 — Deux familles : reversal vs continuation
🟢 **FAIT VÉRIFIÉ** (Source : chart_patterns.md) : « Most can be divided into two broad categories—reversal and continuation patterns. Reversal patterns indicate a trend change, whereas continuation patterns indicate the price trend will continue after a brief consolidation. »
**TRADEX-AI C1** : Taxonomie de classification des patterns à coder pour le moteur de structure : un pattern détecté doit être typé `reversal` ou `continuation`, ce qui conditionne le biais directionnel post-cassure.
*Catégorie : structure_marche*

---

### D1253 — Liste des patterns de retournement (reversal) référencés
🟢 **FAIT VÉRIFIÉ** (Source : chart_patterns.md, section Reversal Patterns) : patterns listés = Broadening Top, Double Top Reversal, Double Bottom Reversal, Head and Shoulders Top, Head and Shoulders Bottom, Falling Wedge, Rising Wedge, Rounding Bottom, Triple Top Reversal, Triple Bottom Reversal, Bump and Run Reversal.
**TRADEX-AI C1** : Catalogue de référence des configurations de retournement à reconnaître. Aucun détail opératoire ici (pages dédiées non scrapées) — sert d'index de couverture pour l'enrichissement futur.
*Catégorie : configuration*

---

### D1254 — Liste des patterns de continuation référencés
🟢 **FAIT VÉRIFIÉ** (Source : chart_patterns.md, section Continuation Patterns) : patterns listés = Flag/Pennant, Symmetrical Triangle, Ascending Triangle, Descending Triangle, Rectangle, Price Channel, Measured Move Bullish, Measured Move Bearish, Cup with Handle.
**TRADEX-AI C1** : Catalogue de référence des configurations de continuation (pauses dans la tendance). Index de couverture pour enrichissement futur ; détails opératoires hors bundle.
*Catégorie : configuration*

---

### D1255 — Limites et subjectivité des patterns (garde-fou)
🟢 **FAIT VÉRIFIÉ** (Source : chart_patterns.md, section Limitations) : « Chart patterns are subjective and can be misinterpreted… Sometimes, a chart pattern may fail to do what you expect. » La classification reversal/continuation n'est que *typique* : « many of these patterns can indicate either a reversal or continuation, depending on the circumstances. »
**TRADEX-AI C1** : Garde-fou — un pattern n'est jamais déterministe. Le moteur ne doit pas émettre de signal sur le seul pattern : confirmation requise (cassure + alignement multi-cercles), cohérent avec la règle 3/4 trading + 2/3 confirmation.
*Catégorie : gestion_risque_entree*

---

## SYNTHÈSE

| D### | Sujet | Cercle | Catégorie | Tag |
|------|-------|--------|-----------|-----|
| D1251 | Définition pattern (supply/demand) | C1 | structure_marche | 🟢 |
| D1252 | Taxonomie reversal / continuation | C1 | structure_marche | 🟢 |
| D1253 | Liste patterns reversal | C1 | configuration | 🟢 |
| D1254 | Liste patterns continuation | C1 | configuration | 🟢 |
| D1255 | Limites / subjectivité (garde-fou) | C1 | gestion_risque_entree | 🟢 |

**Lien Belkhayate :** NON CONCERNÉ (taxonomie générique de chart patterns ; aucun lien explicite à la méthode Belkhayate dans la page).
**Images :** 0/0. **Cas à vérifier :** aucun (page index, 5 décisions, non paddée).

> ⚠️ Outil éducatif · jamais conseil financier · aucune exécution automatique d'ordre.
