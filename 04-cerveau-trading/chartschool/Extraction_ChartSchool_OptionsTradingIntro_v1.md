# Extraction KB — ChartSchool : Options Trading — Introduction to Options
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/options-trading/introduction-to-options  
**Version :** v1 enrichie (texte + descriptions visuelles 10 charts)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Pertinence TRADEX :** ⚠️ INDIRECTE — TRADEX cible les futures, pas les options. Valeur = concepts risk/reward, probabilité de profit, gestion du risque limité.  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS ANTI-HALLUCINATION

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart ou la source officielle lue |
| 🟡 | Interprétation plausible basée sur observation visuelle, non certaine |
| 🔵 | Règle générale citée par auteur reconnu |
| ⏳ | À vérifier dans une autre source avant usage en signal |
| 🔴 | Affirmation risquée ou non prouvée |
| ⚫ | Non auditable |

---

## 1. POSITIONNEMENT KB TRADEX

⚠️ **Cette page couvre les OPTIONS (calls/puts sur actions), non les FUTURES.** TRADEX ne tradant pas d'options, la valeur directe est limitée. Les concepts universellement applicables sont extraits et tagués explicitement.

🔵 **Valeur indirecte pour TRADEX :**
- Concepts de profil Profit/Loss → applicable à la gestion de chaque trade futures
- Notion de Probabilité de Profit (POP/POW) → à intégrer dans le scoring de signal
- Calcul du breakeven → applicable aux trades futures avec SL/TP
- Comparaison de stratégies par rapport rendement/risque → applicable à la sélection de setup

---

## 2. LES 4 POSITIONS OPTIONS DE BASE — DIAGRAMMES PROFIT/LOSS

### 2.1 Long Call (Achat de Call)

🟢 **Diagramme visuel :**
- Axe horizontal = prix de l'action
- Zone LOSS (rose/rouge) : **à gauche** du point de breakeven → **perte fixe et limitée** (prime payée)
- Zone PROFIT (vert) : **à droite** du breakeven → **gain illimité** théoriquement
- Ligne de payoff : flat en bas (perte max = prime), puis monte diagonalement vers la droite

🔵 **Règle Long Call :**
- Biais directionnel : **HAUSSIER**
- Risque maximum : prime payée uniquement (définie à l'achat)
- Profit potentiel : illimité (suit la hausse du sous-jacent)
- Gain seulement si le prix monte au-dessus du strike + prime

🟢 **Exemple réel — GM (General Motors) Long Call :**

| Paramètre | Valeur |
|-----------|--------|
| Instrument | GM Jan 24, 2025 — Strike 53 Call |
| Prix GM au moment de l'analyse | $53.39 |
| Coût (prime) | $283.00 |
| Risque maximum | $283.00 (prime seulement) |
| Profit potentiel | Illimité |
| Breakeven | $55.83 |
| POP (Probability of Profit) | 33.11% |
| Days to Expiry | 50 jours |
| Tendance 1M | Mildly Bearish |
| Tendance 6M | Bullish |
| OptionsPlay Score | **73/100** (rouge = moins recommandé) |
| Label | "Bullish w/ Limited risk" |

🟡 **Interprétation :** score 73 = stratégie valide mais sous-optimale. POP 33.11% = seulement 1 chance sur 3 de finir en profit à expiration. Le biais 6M Bullish vs 1M Mildly Bearish crée une ambiguïté directionnelle.

---

### 2.2 Long Put (Achat de Put)

🟢 **Diagramme visuel :**
- Zone PROFIT (vert) : **à gauche** (prix baisse) → gain croissant à mesure que l'action chute
- Zone LOSS (rose/rouge) : **à droite** → perte fixe (prime) si le prix monte
- Ligne de payoff : décroît de gauche à droite, plate à zéro au-delà du breakeven

🔵 **Règle Long Put :**
- Biais directionnel : **BAISSIER**
- Risque maximum : prime payée uniquement
- Profit potentiel : limité (action ne peut pas aller sous zéro) mais substantiel
- Gain seulement si le prix tombe sous le strike - prime

🟢 **Exemple réel — GM Long Put :**

| Paramètre | Valeur |
|-----------|--------|
| Instrument | GM Jan 24, 2025 — Strike 54 Put |
| Prix GM | $53.39 |
| Coût (prime) | $271.00 |
| Risque maximum | $271.00 |
| Profit maximum | $5,129.00 |
| Breakeven | $51.29 |
| POP | 36.81% |
| Days to Expiry | 50 jours |
| OptionsPlay Score | **84/100** (orange = acceptable) |
| Label | "Bearish w/ Limited risk" |

🟡 **Interprétation :** score 84 > 73 = le Put est plus adapté au contexte que le Call (tendance 1M Mildly Bearish). Ratio Max Reward / Cost = 5129/271 = **18.9x** — levier important si l'action chute significativement.

---

### 2.3 Covered Call (Call Couvert — position Income)

🟢 **Diagramme visuel :**
- Zone PROFIT (vert) : **à gauche et au centre** → profit flat plafonné
- Zone LOSS (rose/rouge) : **à droite** → faible, commence seulement si l'action monte trop
- Ligne de payoff : monte légèrement depuis la gauche, atteint un plafond, reste flat (profit capé)

🔵 **Règle Covered Call :**
- Biais directionnel : **LÉGÈREMENT HAUSSIER ou NEUTRE**
- Stratégie : détenir l'action + vendre un call contre elle → génère un revenu (prime reçue)
- Risque : perte si l'action chute fortement (pas protégé à la baisse au-delà de la prime reçue)
- Profit capé au niveau du strike vendu

🟢 **Exemple réel — GM Covered Call :**

| Paramètre | Valeur |
|-----------|--------|
| Instrument | Sell 1 GM Jan 24, 2025 — Strike 55 Covered Call |
| Prix GM | $53.39 |
| Crédit reçu | $175.00 |
| Profit maximum | $275.00 |
| Risque maximum | $5,225.00 |
| Annualized Return | **27.54%** / Raw: 3.39% |
| 12M Projected Yield | 28.21%* |
| POW (Probability of Win) | **61.80%** |
| Breakeven | $52.25 |
| Days to Expiry | 50 jours |
| Label | "Bullish w/ Limited risk" |

🔴 **Attention * :** les rendements annualisés (27.54%) sont des projections basées sur des renouvellements mensuels — **pas garantis**. Ils dépendent de la volatilité implicite future. À ne pas prendre comme rendement certain.

---

### 2.4 Cash-Secured Put (Short Put — position Income)

🟢 **Diagramme visuel :**
- Zone LOSS (rose/rouge) : **à gauche** → si l'action chute sous le strike → perte croissante
- Zone PROFIT (vert) : **à droite** → flat, plafonné à la prime reçue
- Ligne de payoff : commence bas à gauche, monte diagonalement, devient plate à droite

🔵 **Règle Short Put / Cash-Secured Put :**
- Biais directionnel : **HAUSSIER / NEUTRE**
- Stratégie : vendre un put → obligation d'acheter l'action au strike si assigné
- Revenu généré = prime reçue immédiatement
- Risque : perte si l'action chute significativement sous le strike

🟢 **Exemple réel — GM Short Put :**

| Paramètre | Valeur |
|-----------|--------|
| Instrument | Sell 1 GM Jan 24, 2025 — Strike 52 Put |
| Prix GM | $53.39 |
| Crédit reçu | $136.00 |
| Profit maximum | $136.00 |
| Risque maximum | $5,064.00 |
| Annualized Return | **21.34%*** / Raw: 2.69% |
| POW | **58.37%** |
| Breakeven | $50.64 |
| Days to Expiry | 50 jours |
| Label | "Bullish w/ Limited risk" |

---

## 3. CHAÎNE D'OPTIONS — LECTURE D'UNE OPTIONS CHAIN

🟢 **Options Chain GM (General Motors) — Expiration : Friday Jan 10, 2025 (Weekly) :**

| Colonne | Signification |
|---------|--------------|
| BID | Prix acheteur (prix auquel on peut vendre) |
| ASK | Prix vendeur (prix auquel on peut acheter) |
| MID | Point médian bid/ask |
| VOL | Volume journalier (contrats échangés) |
| OI | Open Interest (contrats ouverts en total) |
| IV | Implied Volatility (volatilité implicite du marché) |
| DELTA | Sensibilité du prix de l'option à 1$ de mouvement du sous-jacent |
| THETA | Perte de valeur temps par jour (toujours négatif pour les acheteurs) |
| GAMMA | Accélération du Delta |
| VEGA | Sensibilité à la volatilité implicite |
| RHO | Sensibilité aux taux d'intérêt |

🟢 **Observations sur la chain GM (jan 2025) :**
- IV constante à **29.59%** sur toutes les strikes deep ITM calls → volatilité implicite uniforme sur les calls profond ITM
- Delta calls deep ITM (~strike 30-41) : **0.9999** → pratiquement identiques à détenir l'action
- Theta calls deep ITM : entre **-0.0021 et -0.0033** → perte de valeur temps quotidienne
- Put ATM (strike ~53, proche du prix $51) : Delta visible autour de -0.33 à -0.46 (approximation)

🔵 **Règle Delta pour les futures :** bien que ce soit une options chain, le concept de Delta s'applique aussi aux futures de manière analogique. Delta = 1.0 pour un contrat futures (parfaite corrélation avec le sous-jacent). C'est pourquoi les futures sont des instruments directs : pas de time decay, pas de volatilité implicite à gérer.

---

## 4. COMPARAISON DE STRATÉGIES — OUTIL OPTIONSPLAY

🟢 **Comparatif stratégies baissières sur GM (biais Bearish choisi) :**

| Stratégie | Trade Cost | Profit max | Return max | OptionsPlay Score |
|-----------|------------|------------|------------|------------------|
| Sell 100 Shares (short action) | -$5,092 | $785 | 15.42% | 103 |
| Buy 1 Feb 28, 2025 52 Put | $360 | $533 | 148.06% | 99 (orange) |
| **Buy 1 Feb 28, 2025 52/43 Put Vertical** | **$323** | **$570** | **176.47%** | **115 ✓** (vert) |

🟢 **Score 115 recommandé** pour le Put Vertical : meilleur ratio rendement/coût + risque limité des deux côtés.

🔵 **Règle de comparaison de stratégies :** pour un même biais directionnel, comparer systématiquement :
- Coût engagé
- Profit maximum
- Return en % du capital risqué
- Probabilité de profit (POW/POP)

Le score composite (OptionsPlay Score) synthétise ces critères. **Score > 100 = stratégie recommandée.**

---

## 5. CONCEPTS CLÉS APPLICABLES AUX FUTURES (TRADEX)

🔵 **C1 — Profil Profit/Loss visuel :** chaque trade TRADEX a un profil analogue. Un signal COG long = profil similaire au Long Call : perte limitée (si SL respecté), gain potentiel supérieur. Le diagramme P/L doit être mental avant chaque entrée.

🔵 **C2 — Probability of Profit (POP) :** en options, le POP est calculable mathématiquement (~delta du strike). Pour les futures, la "probabilité" d'un signal Belkhayate correspond au taux de réussite historique du setup (non calculé encore). ⏳ À définir via backtest TRADEX.

🔵 **C3 — Breakeven explicite :** tout trade futures a un breakeven = prix d'entrée + frais (commissions, spread). Sous le breakeven = perte. Au-dessus = profit. Le connaître avant l'entrée est non négociable.

🔵 **C4 — R/R et "Return" :** le Return en % du capital risqué est l'équivalent du ratio R/R. Un Return de 176% (Put Vertical) = R/R d'environ 1.76. L'architecture TRADEX v2 exige R/R ≥ 1.5 — cohérent avec les meilleures stratégies ici.

🔵 **C5 — Avantage des futures vs options pour TRADEX :** pas de theta decay, pas de volatilité implicite à modéliser, prix direct, exécution simple. L'architecture TRADEX sur futures est plus lisible qu'une stratégie options multi-jambes.

---

## 6. MÉTRIQUES CLÉS OPTIONS (GLOSSAIRE COMPACT)

🟢 **Tableau de référence rapide :**

| Métrique | Définition | Valeur typique |
|----------|-----------|---------------|
| IV (Implied Volatility) | Volatilité anticipée par le marché | 20-40% stocks normaux |
| POP | Probability of Profit à expiration | Long options: 30-45% |
| POW | Probability of Winning | Short options: 55-70% |
| Delta | $ de variation option / $ variation sous-jacent | 0.0 à 1.0 (calls), -1.0 à 0 (puts) |
| Theta | Perte de valeur temps / jour | Toujours ≤ 0 pour acheteur |
| Breakeven | Prix sous-jacent pour atteindre 0 P/L | Strike ± prime |
| OptionsPlay Score | Score composite stratégie | > 100 = recommandé |

---

## 7. CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Calcul exact de la volatilité implicite → voir extraction indicateurs volatilité
⏳ Application des options comme couverture (hedging) sur futures → non couvert ici
⏳ Spreads complexes (condors, butterflies) → page séparée ChartSchool
⏳ Impact de l'IV sur la valeur des options au cours du temps → non détaillé ici

---

*Fin d'extraction — ChartSchool Options Trading Introduction — v1 enrichie visuellement (10 charts)*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
