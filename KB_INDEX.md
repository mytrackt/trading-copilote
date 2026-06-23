# KB_INDEX — TRADEX-AI · Base de Connaissances Trading
**Dernière mise à jour :** 23/06/2026 · Session S22 — P0 COMPLET (MA · RSI · MACD · ADX)
**Repo :** `C:\trading-copilote\` · branch `main`
**GitHub :** `mytrackt/trading-copilote`

---

## 1. COMPTEUR DE DÉCISIONS

```
Première décision  : D1
Dernière décision  : D120
Prochaine décision : D121
Total décisions    : 120
```

---

## 2. DOSSIER DE SORTIE — STRUCTURE

```
C:\trading-copilote\
├── 01-pipeline\bundles\[source]\[page]\images\  ← BRUT : images par page (v3.2)
├── 01-pipeline\bundles\[source]\                ← BRUT : .md + manifest
└── 04-cerveau-trading\[source]\                 ← TRAITÉ : extractions D### prêtes pour claude_brain.py
```

**Nommage extraction :** `Extraction_[Source]_[Sujet]_v1.md`

---

## 3. ÉTAT DES FICHIERS — PRODUITS

### StockCharts ChartSchool
| Fichier | Décisions | Catégories | Images | Statut |
|---------|-----------|------------|--------|--------|
| `moving_averages_v1.md` | D1–D17 | indicateurs_tendance (15) · indicateurs_momentum (1) · structure_marche (1) | 6/6 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_RSI_v1.md` | D18–D39 | indicateurs_momentum · indicateurs_tendance · structure_marche · timing · gestion_risque_entree | 15/15 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_MACD_v1.md` | D40–D61 | indicateurs_momentum · indicateurs_tendance · signal · divergence · configuration | 11/11 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_ADX_v1.md` | D62–D77 | indicateurs_tendance · signal · gestion_risque_entree · configuration | 9/9 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_Candlestick_Bullish_v1.md` | D78–D88 | structure_marche · signal · gestion_risque_entree · configuration | 10/10 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_Candlestick_Bearish_v1.md` | D89–D98 | structure_marche · signal · gestion_risque_entree · configuration | 11/11 ✅ | ✅ VALIDÉ |
| `Extraction_StockCharts_Wyckoff_v1.md` | D99–D111 | structure_marche · indicateurs_tendance · gestion_risque_entree · configuration | 10/10 ✅ | ✅ VALIDÉ |

### Autres sources
| Fichier | Décisions | Catégories | Images | Statut |
|---------|-----------|------------|--------|--------|
| `optimusfutures/Extraction_Optimus_Footprint_v1.md` | D112–D120 | structure_marche · signal · gestion_risque_entree | 7/7 ✅ (alt+filename) | ✅ VALIDÉ (Tier 2 broker) |

---

## 4. SOURCES VALIDÉES — TIER 1 : PRIMAIRES

| # | Source | URL | Thème | Dossier |
|---|--------|-----|-------|---------|
| 1 | StockCharts ChartSchool | https://chartschool.stockcharts.com | TA · indicateurs · patterns | stockcharts |
| 2 | CME Institute | https://www.cmegroup.com/education/courses | Futures NQ/ES/GC · specs | cme |
| 3 | CFTC COT | https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm | COT institutionnels | cftc |
| 4 | bollingerbands.com | https://www.bollingerbands.com/bollinger-bands | Bollinger (créateur) | bollinger |
| 5 | ThePatternSite | https://thepatternsite.com | Stats patterns Bulkowski | patternsite |
| 6 | Jim Dalton Trading | https://jimdaltontrading.com/what-is-the-market-profile-2/ | Market Profile / TPO | jimdalton |
| 7 | Sierra Chart docs | https://www.sierrachart.com/index.php?page=doc/TechnicalStudiesReference.php | Order flow · delta | sierrachart |
| 8 | Candlecharts (Nison) | https://candlecharts.com | Chandeliers (créateur) | nison |
| 9 | belkhayate.ma | https://belkhayate.ma/methode.html | COG (créateur) | belkhayate |

⚠️ **ThePatternSite** : interdit entraînement IA → RÉFÉRENCE seule.

---

## 5. SOURCES VALIDÉES — TIER 2 : SECONDAIRES FIABLES

| # | Source | URL | Thème | Dossier |
|---|--------|-----|-------|---------|
| 10 | NinjaTrader Learning | https://ninjatrader.com/learn | Plateforme · NinjaScript | ninjatrader |
| 11 | NinjaTrader Order Flow | https://ninjatrader.com/futures/blogs/ninjatrader-order-flow/ | Footprint · delta | ninjatrader |
| 12 | Investopedia TA | https://www.investopedia.com/technical-analysis-4689657 | Définitions TA | investopedia |
| 13 | Adam Grimes Blog | https://www.adamhgrimes.com | Price Action (S&P/Gold) | adamgrimes |
| 14 | Brooks Trading Course | https://brookstradingcourse.com | Price Action Al Brooks | brooks |
| 15 | QuantifiedStrategies | https://www.quantifiedstrategies.com | Backtesting chiffré | quantifiedstrat |
| 16 | Fidelity Learning | https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/RSI | RSI/MACD/ADX formules | fidelity |
| 17 | StockCharts Wyckoff | https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial | Wyckoff | wyckoff |
| 18 | Optimus Footprint | https://optimusfutures.com/blog/footprint-charts/ | Footprint · delta · DOM | optimusfutures |
| 19 | WindoTrader Glossaire | https://www.windotrader.com/market-profile/market-profile-glossary-index/ | Market Profile glossaire | jimdalton |

---

## 6. SOURCES VALIDÉES — TIER 3 : ACADÉMIQUES

| # | Source | URL | Thème | Statut |
|---|--------|-----|-------|--------|
| 20 | CME Backtesting (Harvey) | https://www.cmegroup.com/education/files/backtesting.pdf | Sharpe ratio haircut | Peer-reviewed |
| 21 | arXiv Walk-Forward | https://arxiv.org/html/2512.12924v1 | Walk-forward · overfitting | ⚠️ Preprint |
| 22 | Cannon Behavioral Finance | https://www.cannonfinancial.com/uploads/main/Behavioral_Finance-Theories_Evidence.pdf | Biais cognitifs | Académique |

---

## 7. MÉTHODE BELKHAYATE — RESSOURCES TECHNIQUES

| # | Source | URL | Apport |
|---|--------|-----|--------|
| B1 | ProRealCode COG | https://www.prorealcode.com/topic/center-of-gravity/ | Code source (LOWESS + ratio 1.618) |
| B2 | NinjaTrader Ecosystem COG | https://ninjatraderecosystem.com/user-app-share-download/belkhayate-cog/ | C# NinjaScript |
| B3 | belkhayate.ma | https://belkhayate.ma/methode.html | Source créateur |

### ⚠️ GARDES BELKHAYATE (obligatoires dans chaque extraction)
```
🔴 Formule jamais publiée → tout calcul = reconstruction communautaire
🔴 COG REPEINT → backtest historique trompeur
🔴 Performances auto-déclarées → non auditées indépendamment
```

---

## 8. SOURCES SUPPRIMÉES

```
❌ BabyPips · Charles Schwab · Trading in Zone résumé · Britannica Money
❌ QuantVPS Blog · Elite Trader · TradingView Ideas · OANDA Apprendre
❌ Revendeurs MT4/MT5 Belkhayate
```

---

## 9. SOURCES À FILTRER (pré-sélecteur Agent 1)

```
⚠️ Investopedia Trading · Earn2Trade · Insignia Futures
⚠️ Trading Setups Review · QuantStart · PyQuant News
⚠️ futures.io NexusFi · OrderFlow Labs
```

---

## 10. QUEUE D'EXTRACTION — PRIORITÉS

### P0 — Bloque Couche 0 NinjaScript ✅ COMPLET
| # | Page | Source | Décisions | Statut |
|---|------|--------|-----------|--------|
| 1 | Moving Averages | StockCharts | D1–D17 | ✅ FAIT |
| 2 | RSI | StockCharts + Fidelity | D18–D39 | ✅ FAIT |
| 3 | MACD | StockCharts + Fidelity | D40–D61 | ✅ FAIT |
| 4 | ADX | StockCharts | D62–D77 | ✅ FAIT |

### P1 — Chandeliers + Futures specs
| # | Page | Source | Statut |
|---|------|--------|--------|
| 5 | Specs NQ/ES/GC | CME | ⏳ |
| 6a | Candlestick Bullish | StockCharts | ✅ FAIT (D78–D88) |
| 6b | Candlestick Bearish | StockCharts | ✅ FAIT (D89–D98) |
| 7 | COT introduction | CFTC | ⏳ |

### P2 — Order flow + Market Profile
| # | Page | Source | Statut |
|---|------|--------|--------|
| 8a | Footprint charts | Optimus | ✅ FAIT (D112–D120) |
| 8b | Footprint charts | NinjaTrader | 🚫 URL 404 — à redécouvrir |
| 9 | Market Profile | Jim Dalton | ⏳ |
| 10 | VWAP / Volume Profile | Sierra Chart | ⏳ |

### P3 — Price Action + Wyckoff
| # | Page | Source | Statut |
|---|------|--------|--------|
| 11 | Wyckoff Method | StockCharts | ✅ FAIT (D99–D111) |
| 12 | Price Action | Adam Grimes + Brooks | ⏳ |

### P4 — Backtesting + Psychologie
| # | Page | Source | Statut |
|---|------|--------|--------|
| 13 | Walk-forward / overfitting | CME PDF + arXiv | ⏳ |
| 14 | Biais cognitifs | Cannon Behavioral | ⏳ |

---

## 11. PIPELINE OPTION B — ÉTAT

```
Phase 1 ✅ VALIDÉE
  - Agent 1 : scraper.py v3.2 DOUBLE ANCRAGE + SECTION FALLBACK + IMAGES PAR PAGE
              commit ee0f679 (v3.1) → 03c769e (v3.2 fix anti-écrasement)
              .md figcaption + HTML légende locale · accord 2 sources sinon manuel
              Pattern B : figcaption vide → titre section ## parent (ARCH-15)
              Filtre images inline hors <figure> (v3.1)
              Fix v3.2 : images → bundles\<source>\<nom_page>\images\
              backup : scraper_backup_v1.py · scraper_backup_v2.py
  - Agent 2 : analyse native Claude (extraction D### + tags + categorie réelle)
  - Tests    : MA (6/6) · RSI (15/15) · MACD (11/11) · ADX (9/9) · 0 manuel

Phase 2 ⏳ À CONSTRUIRE
  - Agent 3 : Formateur (template KB automatique)
  - Agent 4 : Validateur (score /100)
  - Archiviste : git commit auto

Phase 3 ⏳ À CONSTRUIRE
  - Agent 0 : Cartographe (sitemap.xml → urls_queue.json)
  - Orchestrateur : queue multi-pages multi-sites
```

### CRITÈRES PRÉ-SÉLECTEUR (Agent 1 actif)
```
✅ GARDER : TA · indicateurs · futures · patterns · price action · risk management · backtesting
❌ REJETER : forex-only · crypto · marketing broker · opinions forum
```

### ⚠️ LIMITES SCRAPER v3.2
```
Calibré pour la structure GitBook de StockCharts.
Pattern A : figcaption non vide → comportement standard double ancrage.
Pattern B : figcaption vide → titre section ## parent (ARCH-15).
  ⚠️ Labels non uniques possibles → désambiguïsation côté Agent 2.
Images inline hors <figure> → ignorées (décoratives).
Fix v3.2 : images dans bundles\<source>\<nom_page>\images\ (anti-écrasement).
Chaque nouvelle source (CME, CFTC, etc.) exige son propre résolveur d'images.
Stratégie 22 sources : 00-pilotage\STRATEGIE_MULTI_AGENTS_SCRAPING.md
```

---

## 12. DÉCISIONS ARCHITECTURALES

| Code | Décision | Date |
|------|----------|------|
| ARCH-1 | Stack : Claude API + claude_brain.py + prompt caching | Session initiale |
| ARCH-2 | Architecture 7 Cercles (C1-C7) + KB 3 couches + Runtime 0-8 | Session initiale |
| ARCH-3 | Actifs : NQ · ES · Gold | Session initiale |
| ARCH-4 | Formule COG : polynomial degree-3 ± résidus | Source primaire |
| ARCH-5 | Actifs exclus : Bitcoin · Yen | Session initiale |
| ARCH-8 | KB remise à zéro · D1 = Moving Averages | 21/06/2026 |
| ARCH-9 | ~~Liaison image : texte ALT~~ → SUPERSEDÉ par ARCH-14 | 21/06/2026 |
| ARCH-10 | Étiquetage : `categorie` seule (champ réel KB) | 21/06/2026 |
| ARCH-11 | Dossier : BRUT `01-pipeline/bundles/` · TRAITÉ `04-cerveau-trading/[source]/` | 22/06/2026 |
| ARCH-12 | Sources Tier 1 : 9 primaires | 21/06/2026 |
| ARCH-13 | Belkhayate : toujours ⚫ + 🔴 | 21/06/2026 |
| ARCH-14 | Liaison image : DOUBLE ANCRAGE (.md figcaption + HTML légende locale) · accord 2 sources sinon manuel | 22/06/2026 |
| ARCH-15 | Pattern B : figcaption vide → titre section ## parent comme label · blacklist sections génériques | 22/06/2026 |
| ARCH-16 | Images scraper → `bundles\<source>\<nom_page>\images\` (sous-dossier par page, anti-écrasement) | 23/06/2026 |

---

## 13. TAGS ANTI-HALLUCINATION

```
🟢 FAIT VÉRIFIÉ  — visible dans source (texte officiel + image à légende certifiée)
🟡 CONVENTION    — règle TA classique acceptée
🔵 ÉCOLE         — méthodologie spécifique (StockCharts, Wilder, Brown, Cardwell, Belkhayate)
⏳ VOLATILE      — donnée changeante (prix, %, statistiques)
🔴 NON VÉRIFIÉ  — à confirmer source primaire
⚫ PROPRIÉTAIRE  — méthode Belkhayate exclusive
```

---

## 14. RÈGLE D'OR EXTRACTION

```
1. Lancer scraper.py → bundle texte + images + manifest (double ancrage v3.2)
2. Vérifier manifest : 0 "à vérifier" · sinon traiter manuellement (URL + section fournies)
3. Agent 2 lit bundle → D### avec tags + categorie réelle KB
4. 🟢 UNIQUEMENT si visible dans le texte/image officiel · citer fichier.md + image_XX
5. Belkhayate → toujours ⚫ + 🔴 + mention repaint
6. Prochaine D### = vérifier §1 (compteur) avant chaque session
7. Chaque fichier produit → MAJ §3 et §10 (statut queue → ✅)
8. Git commit + push après chaque session
9. Un doute = STOP · jamais continuer dans l'incertitude
```

---

## 15. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « TRADEX-AI · P0 COMPLET. Scraper v3.2 opérationnel (commit 03c769e). MA D1–D17 ✅ · RSI D18–D39 ✅ · MACD D40–D61 ✅ · ADX D62–D77 ✅. Prochaine décision : D78. Stratégie multi-agents scraping 22 sources disponible dans `00-pilotage\STRATEGIE_MULTI_AGENTS_SCRAPING.md`. Prochain choix : Wyckoff / Candlestick (GitBook, sans code) ou scraper_static.py (gate STRICT). »

---

*KB_INDEX · TRADEX-AI · Mis à jour le 23/06/2026 · D1→D77 · P0 COMPLET (MA ✅ · RSI ✅ · MACD ✅ · ADX ✅)*
*⚠️ Outil éducatif · Jamais du conseil financier · Aucune exécution automatique d'ordre*
