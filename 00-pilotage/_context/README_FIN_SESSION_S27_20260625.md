# README DE TRANSITION — TRADEX-AI
**Date :** 25/06/2026 · **Session :** S27 · **Score projet :** N/A

---

## 1. ÉTAT ACTUEL
Phase B (KB). **Scraping de masse 6 sources COMPLET** (479 bundles bruts, 0 erreur) + **extraction prioritaire + bulk lots 1-2 en cours** (63 fichiers / 721 décisions en `validation/`, AUCUNE fusion master). Compteur master inchangé **D176** (rien fusionné). Plages d'extraction provisoires D177→D1410 (renumérotation contigue à la fusion).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Détail | Commits |
|---------|--------|---------|
| Scraping 6 sources | StockCharts 236 · Adam Grimes 130 · NinjaTrader 38 · Optimus 32 · Sierra 34 · CFTC 9 = **479 bundles** · 0 ERR | `31b78ee` `a775717` `ebe060d` `e8891ce` `7c0ed70` `9f7003c` + 6 KB_INDEX |
| Outils pipeline | `build_queue_sc.py` (file GARDER via llms.txt) · `run_queue.py` (runner reprise) · `build_queues_static.py` · `build_queue_adamgrimes/optimus/cftc.py` · `build_worklist_bulk.py` · `build_assignment_bulk.py` | inclus ci-dessus |
| Extraction prioritaire | 15 fichiers (MFI=Énergie, Pivots, VWAP×2, Vol-by-Price×2, PutCall C5, VIX C5, Intermarket C7, Footprint/Delta Sierra/NT, CME) · 158 déc. | `7005386` `a9c9ddb` |
| Extraction bulk lots 1-2 | 48 fichiers StockCharts (A/D → Correlation) · D451-1410 | lot1, lot2 |

---

## 3. MISSION SUIVANTE (REPRISE BULK — déterministe)
Continuer l'extraction bulk : **413 bundles restants**, plages D### figées dans `01-pipeline\assignment_bulk.tsv` (**idx 48 = D1411+**).
```
Prochaine tranche : awk -F'\t' 'NR>=49 && NR<=84' assignment_bulk.tsv   (idx 48-83)
```
Méthode validée : sous-agents groupés (4 bundles/agent, ~9 agents/lot = 36 pages), spec compacte embarquée, écriture dans `04-cerveau-trading\validation\extractions_S27\`, **JAMAIS de fusion master sans OK**. Skip si fichier sortie déjà présent. Commit + MAJ KB_INDEX par lot.
Ordre restant : StockCharts (~180) → Adam Grimes (127) → NinjaTrader (35) → Optimus (31) → Sierra (31) → CFTC (9).

---

## 4. DÉCISIONS PRISES
- Scraper depuis `llms.txt` (URLs réelles) et NON les chemins simplifiés de la cartographie (404 sinon). Univers GARDER StockCharts réel = **237** (vs « 154 » cartographie, globs expansés).
- Extraction « bundles + extraction sans fusion » (décision utilisateur) : tout en `validation/`, master intouché.
- Format extraction validé utilisateur (étalon MFI/Pivots) : en-tête + inventaire images certifiées + décisions taguées 🟢🔵🟡⏳🔴⚫ + mapping Cn + catégorie réelle KB + synthèse.
- Prudence Belkhayate : tout rattachement méthode = ⚫🔴 « hypothèse projet, non affirmée par la source », jamais d'équivalence inventée.
- Plages D### figées déterministes (20/page) → reprenable ; renumérotation contigue reportée à la fusion.

## 5. DÉCISIONS TEMPORAIRES
- Numérotation D### avec gaps (réserves de 20) → à compacter lors de la fusion master.

---

## 6. PROBLÈMES OUVERTS / BLOCAGES
- **scraper_static.py** ne capture pas les accordéons JS de certaines pages NinjaTrader → contenu tagué 🔴 (formules VWAP/tape/L2 manquantes). Re-scrape JS ou source alternative requis.
- Sources anti-bot non scrapées (respecté) : Brooks · QuantifiedStrategies · Investopedia.
- 3 entrées Optimus à ellipse écartées (slugs non reconstructibles).
- Granularité variable selon sous-agent (7 à 20 décisions/page) — à harmoniser éventuellement à la fusion.
- **FUSION MASTER non faite** (volontaire) : 721 décisions en attente d'audit + OK avant entrée dans `KNOWLEDGE_BASE_MASTER.json`.

---

## 7. STACK / OUTILS
Scrapers : `scraper.py` v3.2 (GitBook) · `scraper_static.py` v1.1 (HTML) · `scraper_pdf.py` v1 (PDF). Runner `run_queue.py`. Files : `queue_*.tsv` · `worklist_bulk.tsv` · `assignment_bulk.tsv`. Extractions : `04-cerveau-trading\validation\extractions_S27\`.

---

## 8. ÉTAT REPO FIN SESSION
Branch `main`. Commits S27 : scraping (6 src + 6 KB_INDEX) + extraction (priorités `7005386` `a9c9ddb`, bulk lot1, lot2) + KB_INDEX suivi. **Push à faire par l'utilisateur.**

---

## 9. COMMANDES GIT
```
git add 00-pilotage\_context\README_FIN_SESSION_S27_20260625.md CLAUDE.md KB_INDEX.md
git commit -m "docs(session): README S27 scraping 6 sources + extraction 63 fichiers (validation/)"
git push origin main
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE
1. Lire CLAUDE.md + ce README.
2. `01-pipeline\assignment_bulk.tsv` : reprise idx 48 (D1411+).
3. Décider : continuer bulk (413 restants) OU lancer l'AUDIT + FUSION des 721 décisions déjà extraites (validation → master, avec OK).

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE
> « TRADEX-AI S28. Scraping 6 sources COMPLET (479 bundles). Extraction S27 = 63 fichiers / 721 décisions en `validation/extractions_S27/` (D177-1410, AUCUNE fusion, master reste D176). Reprise bulk déterministe : `assignment_bulk.tsv` idx 48 = D1411+ (413 bundles restants, ordre StockCharts→AdamGrimes→NT→Optimus→Sierra→CFTC). Alternative : audit+fusion des 721 décisions. Sous-agents groupés 4/agent, spec compacte, zéro fusion sans OK. »

---

## 12. ÉTAT KB FIN SESSION
- Master `KNOWLEDGE_BASE_MASTER.json` : **NON touché** (D176, 1 313 règles).
- `validation/extractions_S27/` : 63 fichiers · 721 décisions provisoires (D177→D1410).
- Bundles bruts : `01-pipeline/bundles/` (479 nouveaux, 6 sources).
