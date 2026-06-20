# Extraction KB — ChartSchool : Options Trading Strategies
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/options-trading/options-trading-strategies  
**Version :** v1 enrichie (Strategy Center réel + comparatif GM)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Pertinence TRADEX :** ⚠️ INDIRECTE — Valeur = système de scoring multi-critères, classification des stratégies par biais directionnel, concept de scanner de setups.  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart/tool lue |
| 🔵 | Règle générale reconnue |
| 🟡 | Interprétation plausible |
| ⏳ | À vérifier |
| 🔴 | Risqué/non prouvé |

---

## 1. CLASSIFICATION DES 9 STRATÉGIES OPTIONS PAR BIAIS

🟢 **Menu déroulant "Select Strategy" visible sur le Strategy Center :**

| Stratégie | Biais directionnel | Risque | Profit |
|-----------|------------------|--------|--------|
| **Covered Call** | Haussier / Neutre | Élevé (action chute) | Limité (prime) |
| **Short Puts** | Haussier / Neutre | Élevé (action chute) | Limité (prime) |
| **Long Calls** | Haussier ✓ | Limité (prime) | Illimité |
| **Long Puts** | Baissier ✓ | Limité (prime) | Élevé |
| **Bull Call Spread** | Haussier modéré | Limité | Limité |
| **Bear Put Spread** | Baissier modéré | Limité | Limité |
| **Bull Put Spread** | Haussier / Neutre | Limité | Limité (prime) |
| **Bear Call Spread** | Baissier / Neutre | Limité | Limité (prime) |
| **Iron Condor** | Neutre (range) | Limité | Limité (primes) |

🔵 **Règle de sélection de stratégie :** le biais directionnel prime. Identifier d'abord la direction (haussier / baissier / neutre), puis choisir la stratégie adaptée au niveau de conviction et au budget de risque.

---

## 2. STRATEGY CENTER — INTERFACE ET FILTRES

🟢 **Paramètres de configuration visibles :**

| Filtre | Valeur dans l'exemple | Signification |
|--------|----------------------|---------------|
| Trade Scans & Chartlists | **Bullish Trend Following** | Pré-filtre : seulement les stocks en tendance haussière |
| Strategy | **Long Puts** (sélectionné) | Biais baissier sur stocks en uptrend = stratégie de protection/contre-tendance |
| Timeframe | **30 Days** | Options expirant dans ~30 jours |
| Risk Profile | **Balanced** | Profil risque intermédiaire |
| Max Risk | **$2,500** | Coût maximum acceptable par trade |

🔵 **Logique du scanner :** combiner un scan technique (Bullish Trend Following) avec une stratégie options (Long Puts) = identifier les stocks haussiers sur lesquels acheter une protection baissière. C'est une stratégie de **hedging directionnel**.

🟡 **Note : SPOT "Max Risk Exceeded" :** Spotify dépasse le budget $2,500 → exclu automatiquement. Le filtre Max Risk évite les positions oversized. Équivalent TRADEX : le circuit breaker filtre les signaux en dehors des paramètres de taille de position.

---

## 3. RÉSULTATS DU SCANNER — 10 TRADES LONG PUTS DÉTECTÉS

🟢 **Résultats complets (scan "Bullish Trend Following" + Long Puts + 30j + $2,500 max) :**

| # | Symbol | Nom | Prix | Strike | Prime | Breakeven | Score | POP |
|---|--------|-----|------|--------|-------|-----------|-------|-----|
| 1 | **TFI** | SPDR Nuveen Bar... | $44.37 | $44 | $0.50 | $44.50 (0.29%) | **105** 🟢 | 50.87% |
| 2 | IYR | iShares US Real Estate | $95.28 | $95 | $2.30 | $97.30 (2.12%) | **83** 🟡 | 34.87% |
| 3 | XLRE | Real Estate SPDR | $41.57 | $41 | $1.25 | $42.25 (1.64%) | **81** 🟡 | 37.69% |
| 4 | LNG | Cheniere Energy | $232.50 | $230 | $9.90 | $239.90 (3.18%) | **81** 🟡 | 34.78% |
| 5 | BAC | Bank of America | $45.78 | $45 | $1.70 | $46.70 (2.01%) | **81** 🟡 | 37.26% |
| 6 | CMG | Chipotle Mexican Grill | $53.29 | $52.5 | $3.00 | $55.50 (4.15%) | **80** 🟡 | 34.25% |
| 7 | FFIV | F5 Networks | $292.61 | $290 | $14.40 | $304.40 (4.03%) | **79** 🟡 | 33.72% |
| 8 | QCOM | Qualcomm | $153.08 | $150 | $9.00 | $159.00 (3.87%) | **77** 🟡 | 34.60% |
| 9 | XLF | Financial SPDR | $51.86 | $51 | $1.70 | $52.70 (1.62%) | **76** 🟡 | 37.49% |
| 10 | SPOT | Spotify | — | — | **Max Risk Exceeded** | — | — | — |

---

## 4. DÉCODAGE DU SYSTÈME DE SCORING OPTIONSPLAY

🟢 **Code couleur observé :**

| Score | Couleur | Interprétation |
|-------|---------|---------------|
| ≥ 100 | 🟢 Vert | Recommandé — meilleur rapport risque/récompense |
| 75-99 | 🟡 Orange | Acceptable — viable mais sous-optimal |
| 50-74 | ⚪ Gris/blanc | Faible — à éviter sauf conviction forte |
| < 50 | 🔴 Rouge | Non recommandé |

🟢 **Seul TFI score ≥ 100 (score 105)** dans ce scan = seule recommandation "verte" sur 10 résultats.

🔵 **Facteurs qui composent le score OptionsPlay (déduits des exemples) :**
- Probabilité de Profit (POP/POW)
- Ratio Profit max / Coût (Return %)
- Breakeven % par rapport au prix actuel (plus proche = mieux)
- Adéquation stratégie/tendance sous-jacente
- Liquidité (OI, volume)

🟡 **TFI score 105 expliqué :** breakeven à seulement **0.29%** au-dessus du prix actuel ($44.37 → $44.50) = l'action n'a besoin de monter que de $0.13 pour être profitable. POP 50.87% = quasi-pile-ou-face. Prime très faible ($0.50). Risque minimal, mais also profit limité.

---

## 5. COMPARATIF STRATÉGIES GM — ANALYSE BEARISH

🟢 **Comparatif 3 stratégies baissières GM (même data que session précédente, confirmée ici) :**

| Stratégie | Trade Cost | Profit max | Return | Score |
|-----------|------------|------------|--------|-------|
| Sell 100 Shares | -$5,092 | $785 | 15.42% | **103** |
| Buy 1 Feb 28, 2025 52 Put | $360 | $533 | 148.06% | **99** 🟡 |
| **Buy 1 Feb 28, 2025 52/43 Put Vertical** | **$323** | **$570** | **176.47%** | **115 ✓** 🟢 |

🔵 **Règle de sélection entre 3 stratégies baissières :**
- **Short action** : capital élevé ($5,092), risque illimité à la hausse, return faible (15%)
- **Long Put simple** : coût modéré ($360), return élevé (148%), mais perd toute la prime si erroné
- **Put Vertical (spread)** : coût le plus faible ($323), return le plus élevé (176%), risque bilatéral défini → **recommandé**

🔵 **Règle Put Vertical (Bear Put Spread) :** acheter un put + vendre un put à strike inférieur. Réduit le coût net. Plafonne le profit mais plafonne aussi la perte. Meilleur R/R quand conviction baissière modérée (pas catastrophiste).

---

## 6. RÈGLES GÉNÉRALES DÉDUITES (APPLICABLES TRADEX)

🔵 **R1 — Scanner de setups = priorité à l'efficacité :** le Strategy Center scanne des centaines de stocks en secondes et ne présente que les 10 meilleures opportunités. TRADEX fait l'équivalent pour les futures : le système de scoring (couches 1-4) filtre les signaux et ne présente que ceux à confiance ≥ seuil. Même philosophie.

🔵 **R2 — Score composite > décision manuelle :** un score qui synthétise POP + R/R + breakeven + liquidité est plus fiable qu'une décision intuitive sur un seul critère. L'architecture TRADEX v2 doit produire un score composite par signal (non encore défini formellement). ⏳ À formaliser.

🔵 **R3 — Breakeven % = filtre clé :** TFI score 105 car breakeven à 0.29%. Plus le breakeven est proche du prix actuel, plus la probabilité de profit est élevée. Pour TRADEX : le breakeven d'un signal futures = Prix d'entrée + spread + commissions. Le système doit calculer ce % avant validation du signal.

🔵 **R4 — Max Risk comme garde-fou absolu :** SPOT exclu automatiquement pour Max Risk Exceeded. TRADEX doit avoir un paramètre équivalent : taille de position maximale par signal, calculée avant exécution et bloquante si dépassée.

🔵 **R5 — Stratégie neutre (Iron Condor) = régime range :** l'Iron Condor est la stratégie options pour les marchés sans direction. Son équivalent TRADEX = absence de signal (NO_TRADE par défaut quand ADX < 20). Ne pas forcer un trade en range.

🔵 **R6 — Adéquation stratégie/tendance :** Long Puts sur "Bullish Trend Following" = protection sur des stocks forts. La stratégie doit être cohérente avec le contexte. TRADEX : signal COG long dans une tendance baissière hebdomadaire = score réduit automatiquement (contra-tendance).

---

## 7. CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Construction détaillée de chaque spread (comment choisir les strikes du vertical) → non expliqué ici
⏳ Ajustement des positions en cours de trade → non couvert
⏳ Impact du rollover sur les spreads options → non couvert
⏳ Équivalence futures des spreads → à construire dans l'architecture TRADEX

---

*Fin d'extraction — ChartSchool Options Trading Strategies — v1 enrichie (Strategy Center + comparatif GM)*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
