# README DE TRANSITION — TRADEX-AI
Date : 22/06/2026 | Session : S21 | KB : 61 décisions

---

## 1. ÉTAT ACTUEL DU PROJET

Pipeline Phase 1 en cours. Scraper v3.1 validé (3 tests PASS). Trois indicateurs P0 extraits et certifiés : MA (D1–D17), RSI (D18–D39), MACD (D40–D61). Prochain P0 : ADX (D62+). Phase 2 pipeline non commencée.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Migration P1 | `moving_averages_v1.md` → `04-cerveau-trading\chartschool\` | `caa0e8d` | ✅ |
| Scraper v3.1 | Section-fallback (ARCH-15) + filtre images inline | `ee0f679` | ✅ |
| Validation scraper | T1 MA (14 cert.) · T2 RSI (16 cert.) · T3 MACD (11 cert.) | `ee0f679` | ✅ |
| Extraction MACD | D40–D61 · 22 décisions · 11/11 images certifiées | `3ce2635` | ✅ |
| KB_INDEX MAJ | Compteur D39 → D61 · MACD ajouté · ARCH-15 documenté | cette session | ✅ |

---

## 3. MISSION SUIVANTE

**P0 — Extraction ADX (D62+)**  
Source : StockCharts ChartSchool  
URL : https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/average-directional-index-adx  
Commande : `py scraper.py "<URL_ADX>" stockcharts adx`

---

## 4. DÉCISIONS PRISES

| Code | Décision |
|------|----------|
| ARCH-15 | Pattern B : figcaption vide → titre section ## parent comme label KB · blacklist sections génériques |
| — | Option 2 retenue pour scraper v3.1 : restreindre `images_html()` aux images dans `<figure>` (non-régression MA/RSI garantie) |

---

## 5. DÉCISIONS TEMPORAIRES

| # | Décision | Condition de levée |
|---|----------|--------------------|
| T1 | Labels non uniques via section-fallback (ex: 4 images "Centerline Crossovers") | Agent 2 désambiguïse au moment de l'extraction D### par contexte paragraphe |

---

## 6. PROBLÈMES OUVERTS

| # | Problème | Priorité |
|---|----------|----------|
| P1 | Labels non uniques section-fallback → désambiguïsation côté Agent 2 | Faible — n'impacte pas la certification |
| P2 | ADX URL à vérifier avant scraping (pattern Page Not Found en 200 possible) | À vérifier en début S22 |

---

## 7. STACK TECHNIQUE GELÉE

```
Scraper    : scraper.py v3.1 (double ancrage + section-fallback ARCH-15)
Python     : py (Windows)
Source KB  : StockCharts ChartSchool (GitBook)
Dossiers   : 01-pipeline\bundles\ (BRUT) · 04-cerveau-trading\chartschool\ (TRAITÉ)
Git        : branch main · GitHub mytrackt/trading-copilote
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Dernier commit  : 3ce2635 — feat(kb): extraction MACD D40-D61 StockCharts
Branch          : main (synchronisé GitHub)
Fichiers propres : ✅ (0 unstaged)
```

---

## 9. COMMANDES GIT SESSION SUIVANTE (PowerShell)

```powershell
cd C:\trading-copilote
git pull origin main
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

```
[ ] Vérifier compteur KB_INDEX : prochaine = D62
[ ] Tester URL ADX avant scraping (python -c "import requests; ...")
[ ] Lancer scraper ADX
[ ] Vérifier manifest : 0 "à vérifier"
[ ] Extraire D62+ · committer · pusher
```

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « TRADEX-AI · Pipeline Phase 1 validée. Scraper v3.1 DOUBLE ANCRAGE + SECTION FALLBACK opérationnel (commit ee0f679). Moving Averages D1–D17 ✅ · RSI D18–D39 ✅ (15/15) · MACD D40–D61 ✅ (11/11 images). Prochaine décision : D62. Extractions traitées : `04-cerveau-trading\chartschool\`. Prochain P0 : ADX (D62+). »

---

## 12. ÉTAT KB FIN SESSION

```
Compteur : D39 → D61 (cette session : +22 décisions MACD)
Fichiers produits cette session :
  - 04-cerveau-trading\chartschool\Extraction_StockCharts_MACD_v1.md  ✅
  - 01-pipeline\scraper.py (v3.1 patch)  ✅
KB_INDEX régénéré : OUI → à ré-uploader dans le projet Claude.ai
```

---

*README_FIN_SESSION_S21_20260622 · TRADEX-AI · 22/06/2026*
