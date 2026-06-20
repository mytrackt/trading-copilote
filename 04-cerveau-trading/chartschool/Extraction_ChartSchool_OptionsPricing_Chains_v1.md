# Extraction KB — ChartSchool : Options Pricing & Options Chains
**Source :** https://chartschool.stockcharts.com/table-of-contents/overview/options-trading/options-pricing-and-options-chains  
**Version :** v1 enrichie (données réelles AAPL + GM chains)  
**Date extraction :** 20/06/2026  
**Tagger :** Claude Sonnet 4.6  
**Usage :** KB TRADEX-AI — contexte Claude API (prompt caching)  
**Pertinence TRADEX :** ⚠️ INDIRECTE — Les Greeks et IV sont concepts options. Valeur = comprendre Delta/Theta/Vega pour calibrer la probabilité et le timing des signaux futures.  
**Disclaimer :** Document éducatif uniquement. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.

---

## SYSTÈME DE TAGS

| Tag | Signification |
|-----|--------------|
| 🟢 | Vérifiable directement sur le chart/chain lue |
| 🔵 | Règle générale reconnue |
| 🟡 | Interprétation plausible |
| ⏳ | À vérifier |
| 🔴 | Risqué/non prouvé |

---

## 1. LECTURE D'UNE OPTIONS CHAIN — COLONNES ET SIGNIFICATION

🔵 **Structure d'une chain (Straddle View) :**
- **Calls à gauche**, **Puts à droite**, **Strike au centre**
- Chaque ligne = un strike price
- Les colonnes sont symétriques entre calls et puts

🟢 **Colonnes complètes visibles sur AAPL chain :**

| Colonne | Définition complète |
|---------|-------------------|
| BID | Prix auquel on peut VENDRE l'option (prix acheteur du market maker) |
| BID SIZE | Quantité de contrats disponibles au BID |
| ASK | Prix auquel on peut ACHETER l'option (prix vendeur du market maker) |
| ASK SIZE | Quantité disponible à l'ASK |
| MID | (BID + ASK) / 2 — prix de référence pour les ordres limites |
| VOL | Volume du jour (contrats échangés aujourd'hui) |
| OI | Open Interest — total des contrats ouverts (tous jours confondus) |
| IV | Implied Volatility — volatilité implicite du marché sur ce strike |
| DELTA | Δ — variation du prix option / variation 1$ du sous-jacent |
| THETA | Θ — perte de valeur temps par jour |
| GAMMA | Γ — variation du Delta / variation 1$ du sous-jacent |
| VEGA | V — sensibilité à 1% de variation de la volatilité implicite |
| RHO | Ρ — sensibilité aux taux d'intérêt |

---

## 2. DONNÉES RÉELLES — AAPL OPTIONS CHAIN (16 JUILLET 2025)

🟢 **Informations générales AAPL :**

| Paramètre | Valeur |
|-----------|--------|
| Ticker | AAPL (Nasdaq) |
| Secteur | Technology / Computer Hardware |
| Prix au 16 Jul 2025 | **$210.16** (+1.05, +0.50%) |
| Market Cap | **3.139 Trillion $** |
| Volume journalier | 47,220,817 actions |
| Prochains résultats | 2025-07-31 |
| Derniers résultats | 2025-05-01 |
| Expiration analysée | Vendredi 22 août 2025 (37 jours) |

### 2.1 Strikes clés AAPL — Tableau de référence

🟢 **Sélection de strikes stratégiques (ATM + environs) :**

| Strike | Type | BID | ASK | IV | DELTA | THETA | GAMMA | VEGA | OI |
|--------|------|-----|-----|----|-------|-------|-------|------|----|
| 195 | Call ITM | 18.05 | 18.45 | 30.69% | 0.8033 | -0.0923 | 0.0185 | 0.1852 | 225 |
| 200 | Call ITM | 14.15 | 14.65 | 29.81% | 0.7288 | -0.1035 | 0.0168 | 0.2215 | 47 |
| **205** | **Call légèr. ITM** | **11.00** | **11.15** | **29.44%** | **0.6378** | **-0.1124** | **0.0190** | **0.2507** | **138** |
| **210** | **Call ATM** | **8.05** | **8.20** | **28.58%** | **0.5381** | **-0.1134** | **0.0208** | **0.2656** | **910** |
| **215** | **Call OTM** | **5.65** | **5.75** | **27.99%** | **0.4332** | **-0.1083** | **0.0210** | **0.2631** | **1040** |
| 220 | Call OTM | 3.75 | 3.90 | 27.44% | 0.3313 | -0.0968 | 0.0197 | 0.2426 | 910 |
| 225 | Call OTM | 2.35 | 2.58 | 27.07% | 0.2407 | -0.0812 | 0.0172 | 0.2083 | 593 |
| 230 | Call OTM | 1.49 | 1.53 | 26.72% | 0.1653 | -0.0635 | 0.0139 | 0.1663 | 1854 |

🟢 **Puts correspondants :**

| Strike | BID | ASK | IV | DELTA | THETA | OI |
|--------|-----|-----|----|-------|-------|----|
| **210** | **7.05** | **7.35** | **28.80%** | **-0.4615** | **-0.0924** | **397** |
| 215 | 9.75 | 10.15 | 28.90% | -0.5631 | -0.0894 | 33 |
| 200 | 3.45 | 3.65 | 30.15% | -0.2727 | -0.0842 | 375 |
| 195 | 2.38 | 2.45 | 31.06% | -0.1988 | -0.0737 | 669 |

---

## 3. LES GREEKS — ANALYSE DÉTAILLÉE SUR DONNÉES RÉELLES

### 3.1 DELTA (Δ)

🔵 **Définition :** variation du prix de l'option pour 1$ de mouvement du sous-jacent.

🟢 **Observations sur AAPL :**
- Call ATM (strike 210, prix $210.16) : Delta = **0.5381** → si AAPL monte de 1$, le call 210 gagne ~$0.54
- Call deep ITM (strike 150) : Delta = **0.9999** → quasiment identique à détenir l'action
- Call deep OTM (strike 230) : Delta = **0.1653** → très faible sensibilité au mouvement
- Put ATM (strike 210) : Delta = **-0.4615** → si AAPL monte de 1$, le put 210 perd ~$0.46

🔵 **Règle Delta ATM :** Delta ≈ 0.50 pour les options ATM (call) et ≈ -0.50 (put). C'est aussi une approximation de la **probabilité que l'option expire dans la monnaie**. Delta 0.50 = 50% de chance de finir ITM.

🔵 **Application TRADEX :** le Delta est l'analogue de la **conviction directionnelle**. Un signal COG Belkhayate avec fort alignement multi-indicateurs = "Delta élevé" (haute conviction). ⏳ À formaliser dans le scoring TRADEX.

### 3.2 THETA (Θ) — Érosion temporelle

🔵 **Définition :** perte de valeur de l'option par jour qui passe (toujours négatif pour les acheteurs).

🟢 **Observations sur AAPL :**
- Call ATM 210 : Theta = **-0.1134** → perd ~$0.11/jour si tout reste stable
- Call 215 OTM : Theta = **-0.1083** → perd légèrement moins (moins de valeur temps)
- Call 205 ITM : Theta = **-0.1124** → perd autant que l'ATM
- Les Thetas **les plus élevés (en valeur absolue)** sont autour de l'ATM

🔵 **Règle Theta ATM :** la perte temporelle est maximale pour les options ATM. Elle décroît vers l'ITM et l'OTM.

🔵 **Application TRADEX :** les futures n'ont PAS de theta. C'est l'avantage décisif des futures vs options pour TRADEX. Aucune perte de valeur "automatique" si le trade stagne.

### 3.3 GAMMA (Γ)

🔵 **Définition :** vitesse d'accélération du Delta. Mesure combien le Delta change pour 1$ de mouvement.

🟢 **Observations sur AAPL :**
- Call ATM 210 : Gamma = **0.0208** — le plus élevé
- Call OTM 215 : Gamma = **0.0210** — légèrement supérieur (pic juste OTM)
- Call ITM 195 : Gamma = **0.0185** — décroît en s'éloignant ATM
- Call deep ITM 150 : Gamma ≈ **0** — stable (Delta ne change plus, proche de 1.0)

🔵 **Règle Gamma :** maximum autour de l'ATM. Plus le Gamma est élevé, plus le Delta change rapidement → position plus risquée et plus réactive.

### 3.4 VEGA (V)

🔵 **Définition :** variation du prix de l'option pour 1% de hausse de la volatilité implicite.

🟢 **Observations sur AAPL :**
- Call ATM 210 : Vega = **0.2656** → si IV monte de 1%, le call gagne $0.27
- Vega maximum autour de l'ATM, décroît vers ITM et OTM
- Call 205 : Vega = 0.2507 ; Call 215 : 0.2631 ; Call 220 : 0.2426

🔵 **Règle Vega :** maximum ATM. Acheter une option = être "long Vega" (bénéficie si IV monte). Vendre une option = être "short Vega" (bénéficie si IV baisse).

🔵 **Application TRADEX :** avant un événement à fort impact (Fed meeting, NFP, rapport économique majeur) → IV monte → valeur des options monte. Pour les futures, cela se traduit par une **extension des spreads bid-ask** et une **volatilité accrue**. Le News Gate TRADEX v2 couvre exactement ce risque.

### 3.5 RHO (Ρ)

🟢 **Call ATM 210 AAPL :** Rho = **0.1064** → faible impact des taux sur ce timeframe (37 jours).

🔵 **Règle Rho :** faible importance pour les options court terme (< 60 jours). Plus impactant sur les LEAPS (long terme > 1 an). Pour TRADEX (intraday/swing), Rho = négligeable.

---

## 4. VOLATILITÉ IMPLICITE — IV SMILE / SKEW

🟢 **IV par strike sur AAPL (calls, Aug 22, 2025) :**

| Strike | IV Call | IV Put | Observation |
|--------|---------|--------|-------------|
| 195 (ITM) | 30.69% | 31.06% | IV élevée côté put OTM |
| 200 | 29.81% | 30.15% | Légèrement décroissante |
| 205 | 29.44% | 29.69% | Vers ATM |
| **210 (ATM)** | **28.58%** | **28.80%** | **IV minimum local** |
| 215 | 27.99% | 28.90% | IV call baisse, put monte |
| 220 | 27.44% | 29.33% | Skew put > call |
| 225 | 27.07% | 29.33% | Skew accentué |
| 230 | 26.72% | 27.28% | - |

🟡 **IV Skew visible :** les puts OTM (strike < 210) ont une IV légèrement plus élevée que les calls OTM (strike > 210). C'est le "volatility skew" ou "smirk" caractéristique des actions — les investisseurs paient plus cher la protection baissière (puts OTM) que le potentiel haussier (calls OTM).

🔵 **Règle IV Skew :** IV skew élevé = le marché anticipe un risque baissier asymétrique. Pour les futures (notamment or), une IV skew prononcée sur les puts peut signaler une attente de correction. ⏳ À surveiller via VIX et GVZ (Gold Volatility Index) pour TRADEX.

---

## 5. DONNÉES RÉELLES — GM OPTIONS CHAIN (8 JANVIER 2025)

🟢 **Informations générales GM :**

| Paramètre | Valeur |
|-----------|--------|
| Ticker | GM (NYSE) |
| Secteur | Consumer Discretionary / Automobiles |
| Prix au 8 Jan 2025 | **$51.00** (-0.98, -1.89%) |
| Market Cap | 56.049 Milliards $ |
| Volume | 7,240,816 |
| Prochains résultats | 2025-01-28 |
| Derniers résultats | 2024-10-22 |
| Expiration analysée | Vendredi 10 Jan 2025 (2 jours) (Weekly) |

🟢 **Observations spécifiques GM chain (2 jours avant expiration) :**
- IV constante à **29.59%** sur tous les calls deep ITM (strikes 30-41)
- Delta calls deep ITM : **0.9999** → comportement identique à l'action
- Volume très faible (1 à 13 contrats) sur ces strikes → **liquidité quasi nulle**
- Put strike 41 (ATM approximatif) : BID 0.01, ASK 0.12, Delta 46 contrats, IV 33.11%

🔵 **Règle expiration proche :** à J-2 avant expiration (comme GM ici), les options OTM perdent presque toute leur valeur (Theta élevé). Seuls les strikes proche du prix actuel ont encore de la valeur temps. Les deep OTM deviennent quasi sans valeur (bid 0.01).

---

## 6. COMPARAISON AAPL vs GM — INSIGHTS CLÉS

🟢 **Tableau comparatif :**

| Paramètre | AAPL | GM |
|-----------|------|-----|
| Prix action | $210.16 | $51.00 |
| Market Cap | $3.14T | $56B |
| IV ATM | ~28.58% | ~29.59% |
| Delta call ATM | 0.5381 | 0.9999 (deep ITM mesuré) |
| Jours à expiration | 37 | 2 |
| Volume journalier | 47M | 7.2M |
| Liquidité options | Très haute (OI 910-1854) | Faible (OI 1-14 deep ITM) |

🟡 **AAPL = actif très liquide :** OI de 910 pour les calls ATM 210 → prix d'exécution fiable. Spread bid-ask étroit (8.05/8.20 = $0.15). GM sur expiration court terme = illiquidité (spread 0.01/0.12 sur deep OTM puts = 1100% de spread).

---

## 7. CONCEPTS CLÉS APPLICABLES AUX FUTURES (TRADEX)

🔵 **C1 — IV = mesure de l'incertitude du marché :** quand IV monte avant un signal TRADEX, la probabilité de fort mouvement est élevée (favorable si dans le bon sens). Le VIX (pour ES/NQ) et le GVZ (pour or) sont les équivalents futures de l'IV options.

🔵 **C2 — Delta ≈ probabilité implicite :** Delta 0.50 ATM = 50% de chance de finir gagnant. Pour TRADEX, un signal COG seul sans confluence = "Delta 50%" (pile ou face). Avec 3 confirmateurs alignés = "Delta 70%+" (signal de haute confiance).

🔵 **C3 — Theta = urgence temporelle :** les futures n'ont pas de Theta, mais les contrats ont une date d'expiration. Position maintenue pendant un rollover = risque de gap. Équivalent TRADEX : ne pas maintenir une position overnight sur futures sans raison forte.

🔵 **C4 — Vega = sensibilité à la volatilité :** quand la volatilité implicite monte (avant NFP, Fed), les marchés futures deviennent plus nerveux. Le News Gate TRADEX v2 bloque les signaux dans ces fenêtres. Justification : Vega élevée = prix moins prévisible.

🔵 **C5 — Liquidité = fiabilité du signal :** un actif avec OI faible (comme GM deep OTM à J-2) a des prix peu fiables. Même logique pour les futures : éviter les contrats peu liquides (micro-contrats obscurs, mois d'expiration lointains peu tradés).

---

## 8. CE QUE CETTE PAGE NE COUVRE PAS (Gaps KB)

⏳ Modèle Black-Scholes et calcul théorique des primes → non détaillé ici
⏳ Volatility smile complet (toute la surface de volatilité) → partiellement visible
⏳ Impact des résultats (earnings) sur l'IV → à extraire depuis page dédiée ChartSchool
⏳ Application VIX/GVZ pour TRADEX → voir extraction indicateurs volatilité

---

*Fin d'extraction — ChartSchool Options Pricing & Options Chains — v1 enrichie (2 chains réelles AAPL + GM)*  
*Tous les livrables sont éducatifs. Jamais du conseil financier. TRADEX = outil décisionnel, aucune exécution automatique d'ordre.*
