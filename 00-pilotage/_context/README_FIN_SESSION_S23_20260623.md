# README DE TRANSITION — TRADEX-AI
Date : 23/06/2026 | Session : S23 (autonome) | KB pipeline : D1→D162

---

## 1. ÉTAT ACTUEL

Pipeline KB Phase 1 étendu en mode autonome. **3 adaptateurs de scraping construits et validés** (GitBook, HTML statique, PDF). **101 décisions ajoutées** (D62→D162). Couverture P1→P4 sur toutes les sources accessibles. Sources anti-bot/404 marquées extraction manuelle.

---

## 2. EXTRACTIONS RÉALISÉES CETTE SESSION

| Décisions | Source | Type | Images | Commit |
|-----------|--------|------|--------|--------|
| D62–D77 | ADX StockCharts | GitBook | 9/9 | `03c769e` |
| D78–D88 | Candlestick Bullish StockCharts | GitBook | 10/10 | `f8e74f0` |
| D89–D98 | Candlestick Bearish StockCharts | GitBook | 11/11 | — |
| D99–D111 | Wyckoff StockCharts | GitBook | 10/10 | — |
| D112–D120 | Footprint Optimus | StaticHTML | 7/7 (alt+filename) | — |
| D121–D130 | Behavioral Finance Cannon | PDF | 0 (texte) | — |
| D131–D134 | Market Profile Jim Dalton | StaticHTML | 0 (texte) | — |
| D135–D142 | Walk-Forward arXiv | StaticHTML | 0 (figures 404=manuel) | — |
| D143–D147 | Bollinger Bands | StaticHTML | 0 (texte) | — |
| D148–D155 | WindoTrader MP Glossary | StaticHTML | 0 (texte) | — |
| D156–D162 | CFTC COT | StaticHTML | 0 (texte) | — |
| D163–D167 | Volume Profile Shapes NinjaTrader | StaticHTML | 0 (texte) | — |
| D168–D172 | Price Action Gold Adam Grimes | StaticHTML | 1/1 (alt) | `9a2662c` |

---

## 3. OUTILS CONSTRUITS

| Fichier | Version | Rôle |
|---------|---------|------|
| `01-pipeline\scraper.py` | v3.3 | GitBook — fix unescape entités HTML titres (faux désaccord `&amp;`) |
| `01-pipeline\scraper_static.py` | v1.1 | HTML statique — ancrage figcaption / alt+filename · urljoin |
| `01-pipeline\scraper_pdf.py` | v1 | PDF — pdfplumber texte · images=manuel |

---

## 4. COUVERTURE PAR PRIORITÉ

- **P0** ✅ COMPLET : MA · RSI · MACD · ADX (D1–D77)
- **P1** : Candlestick Bull+Bear ✅ · COT ✅ · **CME specs 🚫 BLOQUÉ**
- **P2** : Footprint ✅ · Market Profile ✅ (Dalton + WindoTrader) · VWAP/Volume Profile ⚠️ (couvert indirectement)
- **P3** : Wyckoff ✅ · **Price Action 🚫** (Brooks=promo · Adam Grimes 404)
- **P4** : Behavioral Finance ✅ · Walk-Forward ✅ · **CME backtest PDF 🚫**

---

## 5. SOURCES BLOQUÉES → EXTRACTION MANUELLE REQUISE

| Source | Raison | Action |
|--------|--------|--------|
| CME specs NQ/ES/GC | 403 Akamai (requests + WebFetch timeout) | Download manuel des PDF de specs |
| CME backtesting PDF | 403 Akamai | Download manuel |
| Fidelity (RSI/MACD/ADX) | 403 anti-bot | Redondant avec D18-D77 → faible priorité |
| ~~NinjaTrader~~ | ✅ RÉCUPÉRÉ | Volume Profile Shapes D163-D167 |
| ~~Adam Grimes~~ | ✅ RÉCUPÉRÉ | Trend Gold D168-D172 |
| Brooks Price Action | page = promo podcast | URL d'article spécifique requise |
| Nison/candlecharts | page = catalogue de cours | Contenu derrière paywall course |
| Sierra Chart VWAP/VP | pages dédiées 404 (index géant) | Concepts déjà couverts (D120/D150-D151) |
| Investopedia RSI | accessible mais redondant D18-D39 | Non extrait (anti-doublon KB) |

---

## 6. DÉCISIONS PRISES

| Code | Décision |
|------|----------|
| — | Certification HTML statique = ancrage figcaption locale, ou alt+filename (double ancrage page unique). Texte = source littérale toujours certifiée. |
| — | Images PDF = manuel par défaut (pas de légende structurée fiable). |
| — | Sources promo/catalogue/paywall non extraites (pas de fabrication). |

---

## 7. PROBLÈMES OUVERTS

| # | Problème | Priorité |
|---|----------|----------|
| P1 | CME specs (contrats NQ/ES/GC) indisponibles automatiquement — données chiffrées critiques | Moyenne — download manuel |
| P2 | Price Action (Brooks/Grimes) : URLs de contenu à redécouvrir | Faible |
| P3 | scraper_static : certification image limitée (source unique, pas de double ancrage GitBook) | Connu, documenté |

---

## 8. PROCHAINE ACTION

Prochaine décision KB : **D163**. Options : (a) download manuel CME specs (saisie assistée), (b) redécouvrir URLs NinjaTrader/Adam Grimes via sitemaps, (c) passer à la Phase 2 pipeline (Agent 3 Formateur + Agent 4 Validateur /100).

---

## 9. PHRASE D'AMORÇAGE

> « TRADEX-AI · KB pipeline D1→D162. 3 scrapers validés (GitBook v3.3 · static v1.1 · pdf v1). P1–P4 couverts sur sources accessibles. Sources anti-bot (CME/Fidelity/NinjaTrader/Grimes) = manuel. Extractions dans `04-cerveau-trading\<source>\`. Prochaine décision : D163. »

---

*README_FIN_SESSION_S23_20260623 · TRADEX-AI · 23/06/2026*
