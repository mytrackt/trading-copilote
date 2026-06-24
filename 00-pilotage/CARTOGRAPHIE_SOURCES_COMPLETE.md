# CARTOGRAPHIE SOURCES COMPLÈTE — TRADEX-AI

**Date :** 24/06/2026 (S25) · **Méthode :** reconnaissance web parallèle (14 agents), AUCUN scrape effectué
**Périmètre :** sources Tier 1 + Tier 2 de `KB_INDEX.md` (14 sites demandés)
**Critères GARDER :** TA · indicateurs · futures · patterns · price action · risk management · backtesting · order flow · market profile · COG Belkhayate
**Critères REJETER :** forex-only · crypto · marketing broker · opinions forum · paywall · 403/anti-bot

> ⚠️ Ce document est une CARTOGRAPHIE (liste d'URLs + statut). Il ne remplace pas l'audit de fiabilité (A9) ni le pré-sélecteur Agent 1. Toute URL marquée "à revalider" doit être vérifiée (code HTTP + contenu réel) au moment du scrape.

---

## 0. SYNTHÈSE GÉNÉRALE

| # | Site | Tier | Statut accès | Utiles NON scrapés | Note |
|---|------|------|--------------|--------------------|------|
| 1 | StockCharts ChartSchool | T1 | ✅ accessible (llms.txt) | **154** | GitBook · le gisement #1 · scraper v3.x prêt |
| 2 | BollingerBands.com | T1 | ✅ accessible (Wix) | 7 (+4 PDF image-only OCR) | cœur HTML = `bollinger-band-rules` |
| 3 | CFTC COT | T1 | ✅ accessible | 11 (dont 2 PDF) | méthodo COT + glossaire + data historique |
| 4 | Jim Dalton Trading | T1 | ✅ partiel (blog JS) | 8 (~5 solides) | reste = funnel commercial |
| 5 | Sierra Chart docs | T1 | ✅ accessible | **35** | ⚠️ CORRECTION : le "404" était un mauvais slug |
| 6 | Candlecharts (Nison) | T1 | 🟡 1 page gratuite | 1 | reste = promo/paywall |
| 7 | belkhayate.ma | T1 | ✅ accessible (FR) | 1 | `methode.html` seule · formule COG jamais publiée |
| 8 | Investopedia TA | T2 | 🔴 bloque le crawler | 65 (à REVALIDER) | URLs schéma canonique non confirmées |
| 9 | Adam Grimes Blog | T2 | ✅ accessible (WP) | **118** | gisement price action/stats #2 |
| 10 | Brooks Trading Course | T2 | 🔴 403 anti-bot | 8 (BLOQUÉS) | ⚠️ CORRECTION : vrai corpus gratuit existe |
| 11 | QuantifiedStrategies | T2 | 🔴 anti-bot + freemium | 56 | contournement requis (classe Akamai) |
| 12 | NinjaTrader Learn+OF | T2 | ✅ accessible | 36 | order flow / footprint / delta riche |
| 13 | Optimus Futures Blog | T2 | ✅ accessible | 36 | cluster order flow + ATAS |
| 14 | WindoTrader | T2 | 🟡 faible densité | 2 | glossaire mono-page déjà scrapé |

**TOTAL utiles non scrapés (estimation) : ≈ 538 pages** réparties sur 14 sites.

### 🔴 3 CORRECTIONS À REPORTER DANS KB_INDEX
1. **Sierra Chart** n'est PAS en 404 : le slug TPO `TPOProfileCharts.php` est obsolète, la vraie page est `doc/StudiesReference/TimePriceOpportunityCharts.html`. Site **accessible**, 500+ études via `StudiesReference.php&ID=N`. → 35 pages exploitables (`scraper_static.py` adapté).
2. **Brooks Trading Course** : la note "promo/podcast — rien d'exploitable" est **fausse sur le fond**. Il existe un manuel price action gratuit (~12 chapitres) + glossaire + articles. MAIS tout le domaine renvoie **403 anti-bot (Akamai)** → à classer "GARDER mais BLOQUÉ" (adaptateur anti-403 ou manuel), pas "rien d'exploitable".
3. **Investopedia** : le crawler Anthropic est **bloqué** (WebFetch "unable to fetch", WebSearch rejette le domaine). Les 65 URLs listées suivent le schéma canonique `/terms/<lettre>/<slug>.asp` mais **aucune n'a pu être confirmée** — à revalider empiriquement (risque 403 Cloudflare comme CME/Fidelity).

### Priorités recommandées (hors décision roadmap)
- **Haute valeur / accès facile :** StockCharts (indicateurs/overlays/patterns manquants), Adam Grimes (stats/backtest/price action), Sierra Chart (order flow/delta), NinjaTrader + Optimus (order flow).
- **Bloqué → contournement :** Brooks (403), QuantifiedStrategies (anti-bot), Investopedia (à revalider).
- **Faible reliquat :** WindoTrader (2), Candlecharts (1), Belkhayate (1), Bollinger (7).

---

## 1. StockCharts ChartSchool — T1 — ✅ ACCESSIBLE

**Index utilisé :** https://chartschool.stockcharts.com/llms.txt (index machine GitBook ; version `.md` en suffixe d'URL)
**Déjà scrapé (7) :** Moving Averages · RSI · MACD · ADX · Candlestick Bullish · Candlestick Bearish · Wyckoff Tutorial.

| URL (préfixe `chartschool.stockcharts.com/table-of-contents/`) | Thème | G/R | Scrapé |
|------|-------|-----|--------|
| overview/technical-analysis.md | Fondements AT | G | non |
| overview/random-walk-vs.-non-random-walk.md | Efficience marché | G | non |
| overview/john-murphys-10-laws-of-technical-trading.md | Règles AT Murphy | G | non |
| overview/technical-analysis-101/ta-101-part-1.md → part-17.md | Cours AT 17 parties | G (partiel S19) | partiel |
| overview/cognitive-biases.md | Psychologie | G | non |
| overview/multicollinearity.md | Corrélation indicateurs | G | non |
| overview/the-traders-journal-.../stage-1-money-management.md | Money management | G | non |
| overview/the-traders-journal-.../stage-6-stalking-your-trade.md | Timing entrée | G | non |
| overview/the-traders-journal-.../stage-9-selling.md | Sortie position | G | non |
| overview/bob-farrells-10-rules.md | Règles marché | G | non |
| overview/richard-rhodes-trading-rules.md | Règles trading | G | non |
| overview/donchian-trading-guidelines.md | Donchian (trend futures) | G | non |
| overview/why-and-how-to-use-correlation.md | Corrélation inter-marché | G | non |
| chart-analysis/support-and-resistance.md | Supports/résistances | G | non |
| chart-analysis/trend-lines.md | Lignes de tendance | G | non |
| chart-analysis/gaps-and-gap-analysis.md | Gaps | G | non |
| chart-analysis/introduction-to-chart-patterns.md | Intro patterns | G | non |
| chart-patterns/broadening-top-or-megaphone-top.md | Megaphone | G | non |
| chart-patterns/double-top-reversal.md | Double top | G | non |
| chart-patterns/double-bottom-reversal.md | Double bottom | G | non |
| chart-patterns/head-and-shoulders-top.md | Tête-épaules | G | non |
| chart-patterns/head-and-shoulders-bottom.md | Tête-épaules inversée | G | non |
| chart-patterns/falling-wedge.md | Biseau descendant | G | non |
| chart-patterns/rising-wedge.md | Biseau ascendant | G | non |
| chart-patterns/rounding-bottom.md | Soucoupe | G | non |
| chart-patterns/triple-top-reversal.md | Triple top | G | non |
| chart-patterns/triple-bottom-reversal.md | Triple bottom | G | non |
| chart-patterns/bump-and-run-reversal.md | Bump-and-run | G | non |
| chart-patterns/flag-pennant.md | Drapeaux/fanions | G | non |
| chart-patterns/symmetrical-triangle.md | Triangle symétrique | G | non |
| chart-patterns/ascending-triangle.md | Triangle ascendant | G | non |
| chart-patterns/descending-triangle.md | Triangle descendant | G | non |
| chart-patterns/rectangle.md | Rectangle | G | non |
| chart-patterns/price-channel.md | Canal de prix | G | non |
| chart-patterns/measured-move-bullish.md | Measured move haussier | G | non |
| chart-patterns/measured-move-bearish.md | Measured move baissier | G | non |
| chart-patterns/cup-with-handle.md | Tasse avec anse | G | non |
| chart-types/elder-impulse-system.md | Elder Impulse | G | non |
| chart-types/heikin-ashi-candlesticks.md | Heikin-Ashi | G | non |
| chart-types/kagi-charts.md | Kagi | G | non |
| chart-types/renko-charts.md | Renko | G | non |
| chart-types/three-line-break-charts.md | Three-line break | G | non |
| chart-types/relative-rotation-graphs-rrg-charts.md | RRG inter-marché | G | non |
| chart-types/seasonality-charts.md | Saisonnalité | G | non |
| candlestick-charts/introduction-to-candlesticks.md | Intro chandeliers | G | non |
| candlestick-charts/candlesticks-and-support.md | Chandeliers + support | G | non |
| candlestick-charts/candlesticks-and-resistance.md | Chandeliers + résistance | G | non |
| candlestick-charts/candlestick-bullish-reversal-patterns.md | Chand. haussiers | R doublon | OUI |
| candlestick-charts/candlestick-bearish-reversal-patterns.md | Chand. baissiers | R doublon | OUI |
| candlestick-charts/candlestick-pattern-dictionary.md | Dico chandeliers complet | G | non |
| point-and-figure-charts/.../introduction-to-point-and-figure-charts.md | P&F base | G | non |
| point-and-figure-charts/classic-patterns/* (6 pages) | Patterns P&F | G | non |
| point-and-figure-charts/p-and-f-price-objectives/* (3 pages) | Objectifs prix P&F | G | non |
| chart-annotation-tools/andrews-pitchfork.md | Andrews Pitchfork | G | non |
| chart-annotation-tools/fibonacci-retracements.md | Fibonacci retracements | G | non |
| chart-annotation-tools/fibonacci-arcs.md | Fibonacci arcs | G | non |
| chart-annotation-tools/fibonacci-fans.md | Fibonacci fans | G | non |
| chart-annotation-tools/fibonacci-time-zones.md | Fibonacci time zones | G | non |
| chart-annotation-tools/raff-regression-channel.md | Canal régression Raff | G | non |
| chart-annotation-tools/speed-resistance-lines.md | Speed resistance lines | G | non |
| chart-annotation-tools/stock-market-cycles.md | Cycles de marché | G | non |
| technical-indicators/accumulation-distribution-line.md | A/D Line (volume) | G | non |
| technical-indicators/aroon.md + aroon-oscillator.md | Aroon | G | non |
| technical-indicators/atr-bands.md | ATR Bands | G | non |
| technical-indicators/atr-trailing-stops.md | Stops ATR (risk) | G | non |
| technical-indicators/average-directional-index-adx.md | ADX | R doublon | OUI |
| technical-indicators/average-true-range-atr.md | ATR | G | non |
| technical-indicators/average-true-range-percent-atrp.md | ATRP | G | non |
| technical-indicators/balance-of-power-bop.md | Balance of Power | G | non |
| technical-indicators/bollinger-bandwidth.md | BB BandWidth | G | non |
| technical-indicators/b-indicator.md | %B Bollinger | G | non |
| technical-indicators/chaikin-money-flow-cmf.md | Chaikin Money Flow | G | non |
| technical-indicators/chaikin-oscillator.md | Chaikin Oscillator | G | non |
| technical-indicators/chande-trend-meter-ctm.md | Chande Trend Meter | G | non |
| technical-indicators/cmb-composite-index.md | Composite Index | G | non |
| technical-indicators/commodity-channel-index-cci.md | CCI (commodities) | G | non |
| technical-indicators/connorsrsi.md | ConnorsRSI | G | non |
| technical-indicators/coppock-curve.md | Coppock Curve | G | non |
| technical-indicators/correlation-coefficient.md | Coeff. corrélation | G | non |
| technical-indicators/decisionpoint-price-momentum-oscillator-pmo.md | PMO | G | non |
| technical-indicators/detrended-price-oscillator-dpo.md | DPO | G | non |
| technical-indicators/ease-of-movement-emv.md | Ease of Movement | G | non |
| technical-indicators/force-index.md | Force Index | G | non |
| technical-indicators/mass-index.md | Mass Index | G | non |
| technical-indicators/macd-...-oscillator.md | MACD | R doublon | OUI |
| technical-indicators/macd-histogram.md | MACD Histogram | G | non |
| technical-indicators/macd-v.md + macd-v-histogram.md | MACD-V | G | non |
| **technical-indicators/money-flow-index-mfi.md** | **MFI = Énergie Belkhayate** | **G PRIORITAIRE** | non |
| technical-indicators/negative-volume-index-nvi.md | NVI | G | non |
| technical-indicators/on-balance-volume-obv.md | OBV | G | non |
| technical-indicators/percentage-price-oscillator-ppo.md | PPO | G | non |
| technical-indicators/percentage-volume-oscillator-pvo.md | PVO | G | non |
| technical-indicators/price-relative-relative-strength.md | Force relative | G | non |
| technical-indicators/prings-know-sure-thing-kst.md | KST | G | non |
| technical-indicators/prings-special-k.md | Special K | G | non |
| technical-indicators/rate-of-change-roc.md | ROC | G | non |
| technical-indicators/relative-strength-index-rsi.md | RSI | R doublon | OUI |
| technical-indicators/relative-volume-rvol.md | Relative Volume | G | non |
| technical-indicators/slope.md | Slope | G | non |
| technical-indicators/standard-deviation-volatility.md | Écart-type / volatilité | G | non |
| technical-indicators/stochastic-oscillator-fast-slow-and-full.md | Stochastique | G | non |
| technical-indicators/stochrsi.md | StochRSI | G | non |
| technical-indicators/trix.md | TRIX | G | non |
| technical-indicators/true-range.md | True Range | G | non |
| technical-indicators/true-strength-index.md | TSI | G | non |
| technical-indicators/ttm-squeeze.md | TTM Squeeze | G | non |
| technical-indicators/ulcer-index.md | Ulcer Index (drawdown) | G | non |
| technical-indicators/ultimate-oscillator.md | Ultimate Oscillator | G | non |
| technical-indicators/vortex-indicator.md | Vortex | G | non |
| technical-indicators/williams-r.md | Williams %R | G | non |
| technical-overlays/alligator.md | Williams Alligator | G | non |
| **technical-overlays/anchored-vwap.md** | **Anchored VWAP** | **G PRIORITAIRE** | non |
| technical-overlays/bollinger-bands.md | Bandes Bollinger | G (compléter D143) | non |
| technical-overlays/chandelier-exit.md | Chandelier Exit (stops) | G | non |
| technical-overlays/double-exponential-moving-average-dema.md | DEMA | G | non |
| technical-overlays/hull-moving-average-hma.md | HMA | G | non |
| technical-overlays/ichimoku-cloud.md | Ichimoku | G | non |
| technical-overlays/kaufmans-adaptive-moving-average-kama.md | KAMA | G | non |
| technical-overlays/keltner-channels.md | Keltner Channels | G | non |
| technical-overlays/linear-regression-forecast.md | Régression linéaire | G | non |
| technical-overlays/moving-averages-simple-and-exponential.md | MA simples/expo | R doublon | OUI |
| technical-overlays/moving-average-ribbon.md | MA Ribbon | G | non |
| technical-overlays/moving-average-envelopes.md | MA Envelopes | G | non |
| technical-overlays/parabolic-sar.md | Parabolic SAR | G | non |
| **technical-overlays/pivot-points.md** | **Points pivots (Belkhayate)** | **G PRIORITAIRE** | non |
| technical-overlays/price-channels.md | Price Channels | G | non |
| technical-overlays/triple-exponential-moving-average-tema.md | TEMA | G | non |
| **technical-overlays/volume-by-price.md** | **Volume by Price** | **G PRIORITAIRE** | non |
| **technical-overlays/volume-weighted-average-price-vwap.md** | **VWAP** | **G PRIORITAIRE** | non |
| technical-overlays/zigzag.md | ZigZag | G | non |
| market-indicators/arms-index-trin.md | TRIN (breadth) | G | non |
| market-indicators/bullish-percent-index-bpi.md | Bullish Percent Index | G | non |
| market-indicators/mcclellan-oscillator.md | McClellan Oscillator | G | non |
| market-indicators/mcclellan-summation-index.md | McClellan Summation | G | non |
| **market-indicators/put-call-ratio.md** | **Put/Call (sentiment C5)** | **G PRIORITAIRE** | non |
| **market-indicators/volatility-indices.md** | **VIX (C5)** | **G PRIORITAIRE** | non |
| market-indicators/advance-decline-line.md (+ variantes) | Breadth A/D | G | non |
| market-indicators/high-low-index.md / high-low-percent.md | Breadth highs/lows | G | non |
| market-analysis/dow-theory.md | Théorie de Dow | G | non |
| market-analysis/sector-rotation-analysis.md | Rotation sectorielle | G | non |
| **market-analysis/intermarket-analysis.md** | **Inter-marchés (C7)** | **G PRIORITAIRE** | non |
| market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial.md | Wyckoff tutoriel | R doublon | OUI |
| market-analysis/wyckoff-analysis-articles/wyckoff-market-analysis.md | Wyckoff analyse marché | G | non |
| market-analysis/wyckoff-analysis-articles/wyckoff-stock-analysis.md | Wyckoff analyse titre | G | non |
| market-analysis/elliott-wave-analysis-articles/introduction-to-elliott-wave-theory.md | Elliott intro | G | non |
| market-analysis/elliott-wave-analysis-articles/identifying-elliott-wave-patterns.md | Patterns Elliott | G | non |
| market-analysis/elliott-wave-analysis-articles/guidelines-for-applying-elliott-wave-theory.md | Règles Elliott | G | non |
| trading-strategies/bollinger-band-squeeze.md | BB Squeeze | G | non |
| trading-strategies/cci-correction.md | Stratégie CCI | G | non |
| trading-strategies/cvr3-vix-market-timing.md | Timing VIX | G | non |
| trading-strategies/gap-trading-strategies.md | Stratégies gaps | G | non |
| trading-strategies/harmonic-patterns.md | Patterns harmoniques | G | non |
| trading-strategies/ichimoku-cloud-trading-strategies.md | Stratégies Ichimoku | G | non |
| trading-strategies/the-last-stochastic-technique.md | Stratégie stochastique | G | non |
| trading-strategies/macd-zero-line-crosses-with-swing-points.md | MACD swing | G | non |
| trading-strategies/moving-average-trading-strategies/*.md (7 pages) | Stratégies MA (Guppy, golden/death cross, 5-8-13 EMA…) | G | non |
| trading-strategies/moving-momentum.md | Moving Momentum | G | non |
| trading-strategies/narrow-range-day-nr7.md | NR7 (breakout) | G | non |
| trading-strategies/percent-b-money-flow.md | %B + Money Flow | G | non |
| trading-strategies/rsi-2.md | RSI(2) Connors | G | non |
| trading-strategies/six-month-cycle-macd.md | Cycle 6 mois MACD | G | non |
| trading-strategies/stochastic-pop-and-drop.md | Stochastic Pop & Drop | G | non |
| trading-strategies/swing-charting.md | Swing charting | G | non |
| trading-strategies/trend-quantification-and-asset-allocation.md | Quantification tendance | G | non |
| index-and-market-indicator-catalog/cme-futures-and-spot-prices.md | Symboles futures CME (GC/HG/CL) | G PRIORITAIRE | non |
| index-and-market-indicator-catalog/ice-futures-and-spot-prices.md | Symboles futures ICE | G | non |
| index-and-market-indicator-catalog/s-and-p-gsci-indices.md | Indices commodities GSCI | G | non |
| index-and-market-indicator-catalog/us-treasury-yields.md | Taux US (C4 macro) | G | non |
| index-and-market-indicator-catalog/economic-indicators.md | Indicateurs éco (macro) | G | non |

**Rejeté (hors périmètre) :** tout `/glossary/*`, `why-analyze-securities`, `fundamental-analysis`, `asset-allocation`, catalogues de symboles équités (`dow-jones-*`, `stockcharts-*`, MSCI/NYSE/sectors), `marketcarpets`, DecisionPoint niche, `hindenburg-omen` (équités-only).
**TOTAL utiles non scrapés : 154.**

---

## 2. BollingerBands.com — T1 — ✅ ACCESSIBLE (Wix)

**Statut :** HTTP 200, pas de 403/paywall sur le contenu. Sitemaps `/pages-sitemap.xml`, `/blog-posts-sitemap.xml`. Articles PDF = scans **image-only → OCR/manuel**.
**Déjà scrapé :** `bollinger-bands` (D143-D147).

| URL | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /bollinger-band-rules | **22 règles officielles** (%b 15-17, BandWidth/Squeeze 18-19) | G ⭐ | non |
| /tradestation-methods | Méthodes I-IV (Volatility Breakout, Trend, Reversals, Confirmed) | G | non |
| /tradestation-squeeze | Concept Squeeze (low BandWidth → prévision volatilité) | G | non |
| /market-timing-guidelines | Lignes directrices timing (à revalider — rendu JS Wix) | G | non |
| /videos-articles-interviews | Index articles/vidéos (liens) | G index | non |
| /reading-list | Bibliographie | G | non |
| 4 PDF S&C/FX Magazine (`_files/ugd/...`) | Articles TA (BB, volume, rational analysis) | G mais **image-only → OCR** | non |
| /bb-platforms, /shop, /bollinger-band-letter, /*-bbtk, DVD, /about, /contact | Marketing/boutique/corporate | R | — |

**TOTAL utiles non scrapés : 7** (cœur HTML prioritaire = `bollinger-band-rules`, `tradestation-methods`, `tradestation-squeeze`).

---

## 3. CFTC COT — T1 — ✅ ACCESSIBLE

**Statut :** accès total, HTML public, aucun 403/paywall. Cercle C3 (Institutionnels).
**Déjà scrapé :** page explicative COT (D156-D162).

| URL (préfixe `cftc.gov`) | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /MarketReports/CommitmentsofTraders/AbouttheCOTReports/index.htm | Présentation COT, types de rapports, catégories, calendrier | G | non |
| /MarketReports/CommitmentsofTraders/ExplanatoryNotes/index.htm | Notes explicatives (OI, delta options→futures, classification) | G | non |
| .../documents/file/disaggregatedcotexplanatorynot.pdf | Notes Disaggregated (Producer/Swap/Managed Money/Other) | G PDF | non |
| .../documents/file/tfmexplanatorynotes.pdf | Notes TFF (Dealer/Asset Mgr/Leveraged) — ES/VX/DX | G PDF | non |
| /ConsumerProtection/EducationCenter/CFTCGlossary/index.htm | Glossaire CFTC (OI, commercial, hedging, basis…) | G | non |
| /MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm | Archives 1986→2026 (data backtest GC/HG/CL/ZW) | G data | non |
| .../HistoricalViewable/cotvariableslegacy.html | Dictionnaire variables Legacy | G | non |
| .../HistoricalViewable/CFTC_023168.html | Dictionnaire variables Disaggregated | G | non |
| .../HistoricalViewable/cotvariablestfm.html | Dictionnaire variables TFF | G | non |
| .../HistoricalViewable/cotvariablescitsupplement.html | Dictionnaire variables Supplemental | G | non |
| https://publicreporting.cftc.gov/ | Portail interactif (export CSV/XML/RSS) | G data | non |
| .../HistoricalViewable/index.htm | Page-index navigation | R redondant | — |

**TOTAL utiles non scrapés : 11.**

---

## 4. Jim Dalton Trading — T1 — ✅ PARTIEL (blog JS, funnel commercial)

**Statut :** vitrine commerciale (cours 400-1400 $) + blog éducatif gratuit. Contenu réutilisable concentré sur ~5 articles. Blog paginé/JS.
**Déjà scrapé :** `what-is-the-market-profile-2` (D131-D134).

| URL (préfixe `jimdaltontrading.com`) | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /tpo-vs-volume-profile/ | TPO vs Volume Profile, Prix/Temps/Volume | G ⭐ | non |
| /top-ten-resolutions-traders/ | Auction theory, opening range, inventory, day types | G | non |
| /successful-traders-mindset-thinking-terms-concepts-rather-price/ | Excess/balance/gaps, trend days, trade location | G | non |
| /ive-learned-jim-dalton-market-profile-theory/ | Auction theory, valeur, multi-timeframe | G | non |
| /discretionary-trading-vs-rules-based-trading/ | Discrétionnaire vs règles, MGI | G marginal | non |
| /misdirection/ | Value-based, gap rules, tempo | G marginal | non |
| /glossarypage/ | Glossaire MP A-Z (index JS — à revalider rendu) | G à valider | non |
| /products/, /courses/, /product/*, /public-webinars/, posts motivation | Cours payants / webinars / psycho | R commercial | — |

**TOTAL utiles non scrapés : 8** (5 articles techniques solides).

---

## 5. Sierra Chart docs — T1 — ✅ ACCESSIBLE (⚠️ correction "404")

**Statut :** accessible, HTML statique serveur (`scraper_static.py` adapté), pas de JS anti-bot. Le "404" rapporté venait d'un slug obsolète. Catalogue 500+ études. Pattern d'URL étude : `?page=doc/StudiesReference.php&ID=N`.
**Déjà scrapé :** RIEN.

### Hubs
| URL | Thème | G/R |
|-----|-------|-----|
| ?page=doc/TechnicalStudiesReference.php | Index 500+ études | G hub |
| ?page=doc/NumbersBars.php | Footprint / Numbers Bars (bid/ask, POC, imbalance) | G ⭐ |
| ?page=doc/StudiesReference/TimePriceOpportunityCharts.html | TPO / Market Profile (POC, VA) | G ⭐ |

### Études individuelles prioritaires (`StudiesReference.php&ID=`)
| ID | Étude | Thème |
|----|-------|-------|
| 292/296/323 | Cumulative Delta (Volume/Trades/Tick) | order flow / delta |
| 444 | Bar Delta Below Bar | delta |
| 368 | Numbers Bars Avg Volume Per Price | footprint |
| 141 | Volume by Price | volume profile |
| 209/471 | Volume Value Area Lines / For Bars | VA |
| 158 | TPO Value Area Lines | market profile |
| 108/352 | VWAP (+ Rolling) Std Dev | VWAP |
| 38/504/180/500 | RSI / Connors / StochRSI / Laguerre | oscillateurs |
| 32/248 | MACD / Volume Weighted | momentum |
| 13/16/197 | ADX / ADXR / DMI | tendance |
| 19/428 | ATR / Normalized | volatilité |
| 14/135/221 | Bollinger Bands / BandWidth / Squeeze | volatilité |
| 35/188/435/255/62 | Momentum / Chande / PMO / RMI / Momentum Trend | momentum |
| 408 | Point and Figure Box Count | order flow |
| — | Moving Averages (30+ variantes) | tendance |

**Rejeté :** `SupportBoard.php` (forum), `TPOProfileCharts.php` (404 obsolète), licence/install/comptes.
**TOTAL utiles non scrapés : 35** (3 hubs + 32 études/collections).

---

## 6. Candlecharts (Nison) — T1 — 🟡 1 PAGE GRATUITE

**Statut :** majoritairement promotionnel (vente formations Nison). UNE page glossaire gratuite (HTTP 200).
**Déjà scrapé :** RIEN.

| URL | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /candlestick-patterns/ | Glossaire ~52 patterns chandeliers (doji, hammer, engulfing, stars, harami, dark cloud, soldiers/crows, tweezers, windows…) + images, définitions Nison | G ⭐ | non |
| / , /course/free-candlesticks-training/ (verrouillé), /live-charts/, /about/, specials.candlecharts.com/programs/, /my-account/ | Promo / paywall / outil / boutique | R | — |

**Verdict :** 1 seule page exploitable (tout inline, pas de sous-pages). Reste = promo/payant.
**TOTAL utiles non scrapés : 1.**

---

## 7. belkhayate.ma — T1 — ✅ ACCESSIBLE (FR)

**Statut :** HTML statique, FR, pas d'anti-bot (paywall seulement sur l'achat formations). Funnel commercial. ⚫🔴 **Formule COG jamais publiée → reconstruction communautaire.**
**Déjà scrapé :** RIEN.

| URL | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /methode.html | Centre de Gravité (régression polynomiale), Belkhayate Timing, force de rappel, seuil >80%, gestion risque — **descriptif uniquement, aucune formule/seuil/calcul Énergie** | G (créateur, garde repaint) | non |
| /index.html, /biographie.html, /ia-innovation.html, /formations.html, /contact.html, /blog.html | Marketing / bio / vente / Springbox AI | R | — |

**Notes :** Énergie = AUCUNE mention sur le site · Pivots = AUCUNE mention · Money mgmt = allusif (règle 80%). methode.html sert de cadre conceptuel créateur, pas de source de formule.
**TOTAL utiles non scrapés : 1.**

---

## 8. Investopedia TA — T2 — 🔴 BLOQUE LE CRAWLER (à REVALIDER)

**Statut :** WebFetch "unable to fetch" + WebSearch rejette le domaine (400). Hub `/technical-analysis-4689657` NON lisible. URLs ci-dessous = schéma canonique `/terms/<lettre>/<slug>.asp`, **non confirmées** — revalider code HTTP + contenu au scrape (risque 403 Cloudflare type CME/Fidelity).
**Déjà scrapé :** RSI (`investopedia/rsi`).

**Indicateurs :** macd · adx · dmi · bollingerbands · stochasticoscillator · atr · onbalancevolume · vwap · movingaverage · sma · ema · movingaveragecrossover · rsi *(scrapé)* · ichimoku-cloud · fibonacciretracement · parabolicindicator · commoditychannelindex · **mfi (≈ Énergie)** · williamsr · rateofchange · accumulationdistribution · chaikinoscillator · keltnerchannel · donchianchannels · **pivotpoint** · standarddeviation.
**Concepts/patterns :** technicalanalysis · technicalindicator · chart-pattern · head-shoulders · doubletop · triangle · flag · cupandhandle · candlestick · doji · engulfingpattern · hammer · support · resistance · trendline · breakout · price-action · volume-analysis · marketprofile · order-flow *(slug à confirmer)* · level2 · timeandsales · divergence · overbought.
**Backtest/risk :** backtesting · walk-forward-analysis *(à confirmer)* · riskmanagement · riskrewardratio · stop-lossorder · positionsizing *(à confirmer)* · drawdown.
**Futures/macro :** futures · futurescontract · contango · backwardation · openinterest · cot · dollarindex (DX) · vix (VX).

Tous = **Garder** (définitions TA de référence, aucun forex-only/crypto/broker-review).
**TOTAL utiles non scrapés : 65** (RSI exclu). ⚠️ accès réel INCONNU.

---

## 9. Adam Grimes Blog — T2 — ✅ ACCESSIBLE (WordPress)

**Statut :** WP entièrement accessible, sitemap public, pas de paywall. Gisement price action/stats/backtest #2. ~400+ posts ; rejet en masse des `chart-of-the-day-*` (~140), podcast `ml*`/`marketlife-*`, méditation/lifestyle, annonces marketing, analyses datées d'un actif.
**Déjà scrapé :** `trading-a-powerful-trend-in-gold` (D168-D172).

**Séries/clusters GARDER (118 articles, tous non scrapés sauf indiqué) :**
- **First Principles of TA** (5 parties) · **Two modes of market behavior** · `toward-a-simple-model-of-price-behavior` · `the-two-forces`
- **Volatilité :** compression (×2) · clustering · forecasting · the-volatility-game · how-to-calculate-volatility-in-excel · how-to-calculate-sigmaspikes · spikes-in-the-vix (×2)
- **Tendance :** 200-day-moving-average-work · moving-averages-digging-deeper · death-cross (×2) · trend-indicator-helping-hurting · grimes-efficiency-ratio · reading/measuring trend-days (×4) · trend-following-futures · the-trend-is-your-friend-except-at-the-end
- **Patterns/price action :** failure-test · trade-pullbacks · nested-pullback (×2) · choosing-best-pullbacks · complex-consolidations · the-power-channel · inside-bar (×2) · nr7 · free-bars · ranges-and-measured-moves · the-anti · using-highs-and-lows · reading-inside-the-bars
- **Trendlines/niveaux :** draw-trend-lines · trendlines-101 · trendlines-djia · slide/slip-along-the-bands (×2) · support-and-resistance · what-we-learned-about-price-levels
- **Breakouts :** this-is-how-breakouts-work · breakouts-and-breakout-failures
- **Momentum/indicateurs :** what-is-momentum · putting-momentum-work · is-vwap-useful · overbought-oversold · how-to-learn-about-indicators · market-stress-index · RVOL (from-noise-to-signal)
- **Fibonacci (critique stat) :** whats-wrong-fibonacci · testing-fibonaccis · fibonacci-thinking-deeper · fibonacci-conclusions
- **Corrélations/intermarché :** careful-with-correlations · correlated-risk-or-opportunity · intermarket-scatterplots · relative-performance (×2) · spreads (four-reasons + using-spread-charts)
- **Risk management :** know-your-risk · six-keys · cutting-losses · position-size-matters · riskreward · trailing-stops · adding-to-positions · trade-exits · short-volatility · slippage · futures-rolls
- **Quant/backtest :** quant-101 · quant-primer · common-sense-checks · **backtesting-in-excel (7 parties)** · how-to-backtest · trading-edge (×3) · bad-statistics (×2) · law-of-small-numbers · what-are-the-odds · market-stats (×3) · streaks · when-percents-fail · understanding-returns · human-vs-machine · co-authored-paper-2006
- **Intraday/saisonnalité :** map-the-trading-day · intraday-tendencies-sp · activity-by-time-of-day · currencies-time-of-day · daytrading-sp-500-structure · roadmap-for-the-trading-day · post-big-down-day · seasonality (×2) · you-get-paid-to-hold-overnight
- **Setups/divers :** avoid-some-losses · avoid-bad-trades · when-good-setups-go-bad · gap-and-go (+ gaps-and-context · managing-gap-openings) · multi-timeframe (×2) · thinking-in-categories · manipulation/liquidity (×2) · reader-question-volume · SigmaSpikes-ethereum (méthode)
- **À explorer pour compléter :** `/whitepapers/`, `/indicators/`, `/market-structure/`, `/all-posts/` (sitemap tronqué au fetch).

**Rejeté :** `chart-of-the-day-*`, `ml*`/podcast, méditation/lifestyle, annonces cours/livre, analyses datées d'un actif.
**TOTAL utiles non scrapés : 118.**

---

## 10. Brooks Trading Course — T2 — 🔴 403 ANTI-BOT (⚠️ correction)

**Statut :** vrai corpus gratuit price action (manuel ~12 chapitres publics + glossaire + articles), MAIS **tout le domaine = HTTP 403 (Akamai)** à WebFetch. → "GARDER mais BLOQUÉ" (adaptateur anti-403 / curl_cffi / manuel). Corrige la note "promo/podcast — rien d'exploitable".
**Déjà scrapé :** RIEN.

| URL (préfixe `brookstradingcourse.com`) | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /how-to-trade-price-action-manual/ | Manuel 26 000 mots, sommaire + chapitres publics | G ⭐ BLOQUÉ | non |
| /how-to-trade-manual/trading-ranges/ | Trading ranges / market cycle | G BLOQUÉ | non |
| /how-to-trade-manual/price-action-genetically-based/ | Nature du price action | G BLOQUÉ | non |
| /price-action/10-best-price-action-trading-patterns/ | Wedges, double top/bottom, patterns clés | G BLOQUÉ | non |
| /price-action-trading-terms-glossary/ | Glossaire price action | G BLOQUÉ | non |
| /futures-market/trade-trend-channels/ | Trend channels | G BLOQUÉ | non |
| /blog/price-action/ + /tag/price-action-patterns/ | Index articles price action | G index BLOQUÉ | non |
| /, /price-action-trading-books/, /video/*, /members-resources/ | Promo / livres / vidéo sans transcript / paywall | R | — |

**Verdict :** socle gratuit réel mais verrouillé 403 → contournement requis.
**TOTAL utiles non scrapés : 8** (BLOQUÉS).

---

## 11. QuantifiedStrategies — T2 — 🔴 ANTI-BOT + FREEMIUM

**Statut :** corps d'articles + stats backtest lisibles via index de recherche, MAIS fetch direct **bloqué (mur "Verifying you are not a robot", classe Akamai)** → contournement requis. Freemium : beaucoup gratuit, "many detailed trading rules require membership". Pages `/shop`, `/single-strategies-order/`, `/backtested-futures-strategies-shop/` = payant.
**Déjà scrapé :** RIEN.

**Backtest/overfitting (P4 cœur, ~13) :** curve-fitting-trading · backtesting-done-wrong · out-of-sample-backtesting · backtesting-trading-strategies · how-to-backtest-a-trading-strategy · how-to-backtest-futures-strategy · backtesting · trading-strategy-optimization · survivorship-bias-in-backtesting · monte-carlo-simulation-in-trading · backtest-vs-live · machine-learning-trading-strategies.
**Métriques/risk/sizing :** trading-performance · system-performance-metrics · profit-factor · mar-ratio · drawdown · math-of-trading · kelly-criterion-position-sizing · kelly-dangerous · kelly-vs-optimal-f · position-sizing-strategies · maximum-drawdown-position-sizing · equity-curve-position-sizing · breakout-system-sizing · arithmetic-geometric-averages.
**Stratégies indicateurs chiffrées :** rsi-trading-strategy · rsi-2-strategy · rsi-mean-reversion · rsi2-on-spy · macd-trading-strategy · macd-and-bollinger-bands · mean-reversion (×4) · ibs-indicator-strategy · trend-following · moving-average-strategy · sma-strategy · adaptive-ma · ma-slope · trend-reversal · williams-r · pair-trading · quantitative-trading-strategies · algorithmic-trading-strategies.
**Futures actifs TRADING (haute priorité) :** crude-oil-futures · crude-oil-trading-strategies · crude-oil-futures-trading · **commodity-trading-strategies** (or/cuivre/blé) · futures-trading-strategies.
**Hub :** /trading-strategies-free/ (à crawler).
**Rejeté :** shop / single-strategies-order / backtested-futures-shop (payant) · bitcoin-rsi (crypto).

**TOTAL utiles non scrapés : 56** (dédoublonner profit-factor & backtesting-trading-2).

---

## 12. NinjaTrader Learn + Order Flow — T2 — ✅ ACCESSIBLE

**Statut :** HTTP 200, pas de paywall/403. Blog ~470 résultats. Forums support exclus (bruit). Pages compte/courtage/produit rejetées.
**Déjà scrapé :** `trade-futures-understanding-the-4-common-volume-profile-shapes` (D163-D167).

| URL (préfixe `ninjatrader.com`) | Thème | G/R |
|-----|-------|-----|
| /futures/blogs/ninjatrader-order-flow/ | Footprint / order flow (entrée) | G |
| /futures/blogs/footprint-charts-guide/ | Footprint: absorption, exhaustion, imbalance | G |
| /learn/order-flow-indicators/ | Order flow: tape, L2, DOM, footprint, delta, profile | G |
| /futures/blogs/what-is-cumulative-delta-in-order-flow-trading/ | Cumulative Delta | G |
| /futures/blogs/track-buying-selling-pressure-with-order-flow-cumulative-delta/ | Delta (pression) | G |
| /futures/blogs/order-flow-trading-with-volumetric-bars/ | Volumetric bars | G |
| /futures/blogs/use-volume-profile-to-track-order-flow-on-charts/ | Volume Profile + order flow | G |
| /futures/blogs/how-to-trade-with-volume-profile-part-1/ | Volume Profile (VAH/VAL, HVN/LVN) | G |
| /futures/blogs/what-is-volume-weighted-average-price-vwap/ | VWAP | G |
| /futures/blogs/volume-analysis-in-futures-trading/ | Analyse de volume | G |
| /futures/blogs/how-to-identify-entry-zones-with-volume-analysis-trading-guide/ | Zones d'entrée (absorption) | G |
| /learn/technical-analysis/analyze-volume-in-futures-markets/ | Volume (learn) | G |
| /futures/blogs/volume-spread-analysis-and-fomo-of-strong-directional-moves/ | VSA / Wyckoff | G |
| /futures/blogs/best-futures-trading-indicators/ | 5 indicateurs futures | G |
| /futures/blogs/5-key-indicators-for-day-trading-futures/ | 5 indicateurs day trading | G |
| /futures/blogs/common-mistakes-when-using-rsi-indicators-in-futures/ | RSI (erreurs) | G |
| /learn/technical-analysis/momentum-as-indicator-in-futures-trading/ | Momentum | G |
| /learn/technical-analysis/use-volatility-as-indicator-in-futures-trading/ | Volatilité | G |
| /learn/technical-analysis/identifying-trends-in-futures-markets/ | Tendances | G |
| /learn/technical-analysis/identify-chart-patterns-on-futures-trading-charts/ | Figures chartistes | G |
| /futures/blogs/chart-patterns-trading/ | Chart patterns | G |
| /futures/blogs/price-action-trading-strategies/ | Price action | G |
| /futures/blogs/how-to-identify-intraday-support-and-resistance-levels-in-your-trading/ | Support/résistance + pivots | G |
| /futures/blogs/supply-demand-zones-futures/ | Zones supply/demand | G |
| /futures/blogs/trade-trend-reversals-futures/ | Renversements | G |
| /futures/blogs/how-to-trade-liquidity-traps-in-futures/ | Liquidity traps | G |
| /futures/blogs/futures-trading-risk-management-margin-leverage-stops-position-sizing/ | Risk mgmt (4 piliers) | G |
| /futures/blogs/mastering-risk-management-in-futures-trading/ | Risk mgmt (approfondi) | G |
| /futures/blogs/stop-loss-strategies/ | Stop-loss | G |
| /futures/futures-trading-basics/risk-management/ | Risk mgmt (basics) | G |
| /futures/blogs/how-to-use-the-superdom-price-ladder-for-order-entry/ | SuperDOM / ladder | G |
| /futures/blogs/intro-to-the-ninjatrader-desktop-superdom/ | SuperDOM (intro) | G |
| /futures/blogs/ninjascript-best-practices/ | NinjaScript | G |
| /futures/blogs/z-score-futures-trading-strategy/ | Z-Score | G |
| /futures/blogs/how-to-read-a-futures-trading-chart/ | Lire un graphique | G |
| /learn/building-a-trading-strategy/ | Construire une stratégie | G |
| /futures/blogs/how-to-use-automated-trade-management-strategies-on-ninjatrader/ | ATM strategies | G |
| /futures/blogs/futures-trading-strategies-ranked-difficulty/ | 10 stratégies classées | G |
| nasdaq-futures (NQ), produits, crypto-futures, limit-order basique, forum.ninjatrader.com | NQ hors actifs / produit / crypto / basique / forum | R |

**TOTAL utiles non scrapés : 36.**

---

## 13. Optimus Futures Blog — T2 — ✅ ACCESSIBLE

**Statut :** HTTP 200, pas de 403/paywall. `sitemap.xml` (~180 URLs). Cluster order flow aligné C2 (ATAS).
**Déjà scrapé :** `footprint-charts` (D112-D120).

| URL (préfixe `optimusfutures.com/blog/`) | Thème | G/R |
|-----|-------|-----|
| order-flow-trading/ · order-flow-analysis/ · order-flow-software/ · best-order-flow-indicators/ · order-flow-imbalance/ · technical-analysis-with-order-flow/ · how-to-set-up-your-trading-charts-for-order-flow-trading/ · order-flow-in-tradingview/ | Order flow (8) | G |
| volume-profile-trading/ · tpo-charts-explained-for-beginners-market-profile-guide/ · atas-order-flow-...-footprint-and-market-profile-charts/ · see-inside-the-candle-...-footprint-...-quantower/ · volume-and-open-interest/ | Volume/Market Profile/footprint (5) | G |
| anchored-vwap/ · best-indicators-for-day-trading-futures/ · average-true-range-indicator/ · best-tradingview-indicators/ | Indicateurs / VWAP / ATR (4) | G |
| support-and-resistance-trading-guide/ · breakout-trading/ · day-trading-chart-patterns/ · gap-trading-strategies/ · how-to-trade-fair-value-gaps/ · mean-reversion-trading/ · sideways-markets-...-futures-traders/ · end-of-day-trading-strategies/ · futures-trading-scalping-strategy/ | Patterns/stratégies | G |
| stop-loss-orders-in-futures-trading/ · day-trading-risk-management/ | Risk management | G |
| backtesting-trading-strategies-in-futures-markets/ · how-to-backtest-on-tradingview/ | Backtesting | G |
| vix-futures-guide/ (VX) · what-es-futures-tell-you-before-market-opens/ (ES) · how-to-read-stock-market-futures/ · tradingview-tick-charts/ · index-futures-trading/ | Futures confirmation/lecture | G |
| reviews plateformes, order-flow-trading-platform (promo), best-*-platforms/vps, chatgpt-trading, *-vs-* comparatifs, ouverture compte, horaires fériés, tutos UI TradingView mobile, micro-emini/paper intro | Marketing/forex/crypto/UI/actualités | R |

**TOTAL utiles non scrapés : 36.**

---

## 14. WindoTrader — T2 — 🟡 FAIBLE DENSITÉ

**Statut :** HTTP 200, pas de Cloudflare. Contenu texte concentré dans le glossaire (déjà scrapé, mono-page). Vidéos = video-only. Webinaires = login-gated.
**Déjà scrapé :** glossaire MP (D148-D155).

| URL (préfixe `windotrader.com`) | Thème | G/R | Scrapé |
|-----|-------|-----|--------|
| /market-profile/ | Présentation MP : auction process, time/price/volume, biais directionnel | G (léger) | non |
| /market-profile/market-profile-glossary-index/ | Glossaire 25 termes (Balance, Excess, IB, POC, VA, day/open types) | G | OUI |
| /market-profile/market-profile-faq/ | FAQ 5 concepts d'interprétation (renvoie au livre Dalton) | G (faible) | non |
| /market-profile-video-series/, /recorded-webinar-archive-page/, /windo-views/, pages produit/témoignages, /WTB_CME.pdf | Vidéo sans transcript / login / commercial / juridique | R | — |

**Note :** glossaire mono-page (aucune sous-page cachée). Les 2 pages neuves sont de faible densité (renvoient à *Mind over Markets*, déjà source canonique D131-D134).
**TOTAL utiles non scrapés : 2.**

---

## 15. NOTES MÉTHODE & SUITE

- Reconnaissance via WebFetch/WebSearch uniquement — **aucune page scrapée**, aucun fichier `bundles/` modifié.
- Sites à **contournement anti-bot** (à traiter comme CME/Akamai) : Brooks (403), QuantifiedStrategies (mur robot), Investopedia (crawler bloqué — à revalider).
- Sites **GitBook/statique prêts** au scraper existant : StockCharts (`scraper.py` v3.x), Sierra Chart (`scraper_static.py`), CFTC (PDF → `scraper_pdf.py`).
- **Ne pas relancer** sans décision roadmap : ce document est une carte, pas une file d'extraction. La file `KB_INDEX §10` reste la source de priorisation officielle.

---

*CARTOGRAPHIE_SOURCES_COMPLETE · TRADEX-AI · 24/06/2026 (S25) · 14 sites · ≈538 pages utiles non scrapées*
*⚠️ Outil éducatif · Jamais du conseil financier · Reconnaissance seule, validité documentaire A9 non statuée ici*
