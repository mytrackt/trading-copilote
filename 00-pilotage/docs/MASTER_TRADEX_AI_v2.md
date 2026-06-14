╔══════════════════════════════════════════════════════════════════╗
║         DOCUMENT MASTER — TRADEX-AI — VERSION CONSOLIDÉE         ║
╚══════════════════════════════════════════════════════════════════╝

Version   : MASTER v2.0
Date      : 02 Mai 2026
Statut    : PLAN D'ACTION EXÉCUTABLE — PRODUCTION READY
Fusion de : Plan MBK v2.0 (ATAS) + OODA God Mode + GetXAPI + Stratégie 7 Cercles

---

# MÉTADONNÉES & DÉCISIONS GELÉES

## Stack technique (non négociable)
- **Plateforme trading**  : NinjaTrader 8 (Windows local)
- **Order flow**          : ATAS Pro (connecté Rithmic)
- **Data feed**           : Rithmic via broker NTB
- **Cerveau AI**          : Claude API claude-sonnet-4-6 (Anthropic)
- **Backend local**       : Python 3.11 + FastAPI
- **Dashboard**           : React + Vite + Tailwind (local)
- **DB locale**           : SQLite
- **Exécution ordres**    : NinjaTrader 8 ATI (TCP/IP local)
- **OS**                  : Windows 10/11

## Budget (non négociable)
- **Plafond absolu** : 200$/mois
- **Objectif cible** : ~150$/mois
- **Marge de sécurité** : ~50$/mois

## Actifs — 3 catégories (non négociables)
- **TRADING (ordres possibles)**         : GC (Or) · HG (Cuivre) · CL (Pétrole) · ZW (Blé)
- **CONFIRMATION (analyse uniquement)**  : DX (Dollar) · ES (S&P 500) · VX (VIX)
- **REFERENCE (corrélations, no trade)** : MBT (Bitcoin) · 6J (Yen)

## Méthode (non négociable)
- Indicateurs Belkhayate : BGC ratio 0.618, Direction, Energie, Pivots
- KB MBK : 2337 règles
- Règle 3/4 marchés alignés
- Règle 2/3 confirmations
- Détection Liquidity Grab + Fibonacci (MBK)
- Range Bars 5 ticks (configuration Belkhayate)

---

# SECTION 0 — VISION GLOBALE EN 1 SCHÉMA

```
╔══════════════════════════════════════════════════════════════════════╗
║  NIVEAU 1 — SOURCES DONNÉES TEMPS RÉEL                             ║
╠══════════════════════════════════════════════════════════════════════╣
║  NT8+Rithmic │ ATAS Pro │ 21 APIs gratuites │ GetXAPI (~1$)         ║
╠══════════════════════════════════════════════════════════════════════╣
║  NIVEAU 2 — 7 CERCLES D'INTELLIGENCE (Python local)                ║
╠══════════════════════════════════════════════════════════════════════╣
║  C1:Prix │ C2:OrderFlow │ C3:Institutionnels │ C4:Macro             ║
║  C5:Sentiment │ C6:Géopolitique │ C7:Corrélations                   ║
╠══════════════════════════════════════════════════════════════════════╣
║  NIVEAU 3 — CERVEAU AI (Claude API + KB 2337 règles)               ║
╠══════════════════════════════════════════════════════════════════════╣
║  Scoring 7 cercles → Signal JSON → Confiance % → Régime marché      ║
╠══════════════════════════════════════════════════════════════════════╣
║  NIVEAU 4 — EXÉCUTION                                               ║
╠══════════════════════════════════════════════════════════════════════╣
║  Mode Manuel : Dashboard → Tu décides → Clic exécution              ║
║  Mode Auto   : Règles risque → ATI → NT8 → Broker → Ordre           ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

# SECTION 1 — BUDGET FINAL CONSOLIDÉ

## Classification 3 catégories d'actifs (verrouillée)

| Catégorie | Actifs | Rôle | Source data |
|-----------|--------|------|-------------|
| **TRADING** | GC (Or), HG (Cuivre), CL (Pétrole WTI), ZW (Blé) | Ordres possibles | Rithmic CME (payant) |
| **CONFIRMATION** | DX (Dollar Index), ES (S&P 500), VX (VIX) | Analyse seule, pas d'ordres | Rithmic CME + CBOE (payant) |
| **RÉFÉRENCE** | MBT (Bitcoin Micro), 6J (Yen) | Corrélations inter-marché, no trade | Gratuit / inclus |

## Budget mensuel détaillé

| # | Poste | Source | Coût/mois |
|---|-------|--------|-----------|
| 1 | NinjaTrader 8 | Broker NTB (inclus) | **0$** |
| 2 | Data feed CME (GC, HG, CL, ZW + ES) | Rithmic via NTB | ~50$ |
| 3 | Exchange fee CBOE (VIX) | CBOE | ~10$ |
| 4 | ATAS Pro (order flow complet) | atas.net | ~70$ |
| 5 | Claude API (claude-sonnet-4-6 — cerveau KB) | Anthropic | ~15-20$ |
| 6 | GetXAPI (6 comptes X.com clés) | getxapi.com | ~1$ |
| 7 | **21 sources intelligence** | Toutes gratuites | **0$** |
| | **TOTAL** | | **~146-151$/mois** |
| | **Marge sur 200$** | | **~49-54$/mois** |

> **Note** : MBT (Bitcoin Micro) et 6J (Yen) ne sont PAS dans le data feed payant Rithmic. Leurs données arrivent via sources gratuites (cours spot publics) et servent uniquement à la matrice de corrélations inter-marchés (Cercle 7). Ils ne génèrent jamais d'ordre.

### Les 21 sources gratuites (0$ chacune)
```
MACRO & CALENDRIER     SENTIMENT              INSTITUTIONNELS
─────────────────────  ─────────────────────  ─────────────────────
FRED API (Fed)         Fear & Greed stocks    COT CFTC (vendredi)
EIA Oil API            Fear & Greed BTC       Dark Pools FINRA
Finnhub (news+cal)     AAII Sentiment         Put/Call CBOE
Alpha Vantage (DXY)    SKEW Index CBOE        
IMF Gold Data          VIX niveau             GÉOPOLITIQUE
Nasdaq Data Link COT                          GDELT Project
                       CORRÉLATIONS           MarineTraffic (base)
                       Python local (8 actifs)
```

---

# SECTION 2 — ARCHITECTURE TECHNIQUE COMPLÈTE

## Flux de données (lecture de haut en bas)

```
[MARCHÉS RÉELS]
CME · COMEX · NYMEX · CBOE · ICE
         │ tick-by-tick
         ▼
[NINJATRADER 8]──────────────────[ATAS PRO]
 OHLCV + Volume + DOM base         Footprint + Smart DOM
 Indicateurs Belkhayate            Delta + Big Trades
 Range Bars 5 ticks                Cale + Fausse Cassure + Squeeze
         │                                  │
         │ NinjaScript → NT8_data.csv        │ → ATAS_signals.json
         │ (toutes les 2 secondes)           │ (toutes les 2 secondes)
         └──────────────┬───────────────────┘
                        ▼
              [ORCHESTRATEUR PYTHON]
              ┌─────────────────────────────────────────┐
              │  Lecteur NT8_data.csv                   │
              │  Lecteur ATAS_signals.json               │
              │                                         │
              │  Collecteurs APIs (toutes les N min) :  │
              │  ├── FRED (macro, taux, DXY)            │
              │  ├── EIA (stocks pétrole mercredi)      │
              │  ├── CFTC COT (vendredi 19h30)          │
              │  ├── FINRA ATS (dark pools, J-14)       │
              │  ├── CBOE P/C + SKEW (quotidien)        │
              │  ├── Finnhub (news + calendrier éco)    │
              │  ├── Fear & Greed × 2 (toutes les 5min) │
              │  ├── AAII Sentiment (jeudi)             │
              │  ├── GDELT (toutes les 15 min)          │
              │  ├── GetXAPI (6 comptes, toutes les 5min│
              │  └── IMF Gold (mensuel)                 │
              │                                         │
              │  Moteurs de calcul :                    │
              │  ├── Belkhayate (BGC, Dir, Energie)     │
              │  ├── Règle 3/4 marchés                  │
              │  ├── Règle 2/3 confirmations            │
              │  ├── Matrice corrélations glissante     │
              │  ├── Régime marché (Risk-On/Off/etc.)   │
              │  ├── Inter-market Analysis              │
              │  └── Scoring 7 Cercles                  │
              │                                         │
              │  Gestionnaire de risque (règles dures)  │
              └─────────────────────────────────────────┘
                        │
                        ▼
              [CLAUDE API — KB 2337 RÈGLES]
              Prompt 7 cercles → JSON signal
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
      [DASHBOARD REACT]    [RÈGLES RISQUE]
      Mode Manuel           Blocages automatiques
      Mode Auto  ──────────→ [ATI NT8] → [BROKER]
```

---

# SECTION 3 — LES 7 CERCLES : SOURCES ET RÈGLES

## CERCLE 1 — LE PRIX
**Source : NinjaTrader 8 (NT8_data.csv)**
Fréquence : toutes les 2 secondes

| Données collectées | Format |
|-------------------|--------|
| OHLCV (8 actifs) | Float |
| BGC valeur + zone (verte/rouge/neutre) | Enum |
| Direction (haussière/baissière/neutre) | Enum |
| Energie (0-100%) | Int |
| Pivot Haut + Pivot Bas | Float |
| Range Bar actuel (ticks) | Int |
| Couloir horaire actif (O/N) | Bool |
| Règle 3/4 nb alignés | Int |
| Règle 2/3 nb confirmations | Int |

---

## CERCLE 2 — L'ORDER FLOW
**Source : ATAS Pro (ATAS_signals.json)**
Fréquence : toutes les 2 secondes

| Données collectées | Format |
|-------------------|--------|
| Cale détectée (O/N) + force (x2/x3/x5) | Bool + Int |
| Delta barre (volume ask - volume bid) | Int |
| Fausse cassure (O/N) | Bool |
| Squeeze (O/N) | Bool |
| Déséquilibre DOM (ratio bid/ask) | Float |
| Mur acheteur (niveau prix) | Float |
| Mur vendeur (niveau prix) | Float |

**Règles ATAS intégrées dans Python (codées en dur) :**
```python
RÈGLES_ATAS = {
    "cale": {
        "trigger": "lots_niveau >= lots_moyen * 2",
        "ET": "volume_barre >= volume_moyen_20 * 1.5",
        "signal": "CALE_DETECTEE",
        "action": "alerte + boost confiance +10pts"
    },
    "fausse_cassure": {
        "trigger": "prix casse pivot ET delta_negatif",
        "signal": "FAUSSE_CASSURE",
        "action": "BLOQUER signal dans direction cassure"
    },
    "squeeze": {
        "trigger": "volume > 3× moy ET mèche > 2× corps",
        "ET": "delta_diverge_direction_trade",
        "signal": "SQUEEZE",
        "action": "alerte sortie position"
    }
}
```

---

## CERCLE 3 — POSITIONS INSTITUTIONNELLES
**Sources : CFTC + FINRA + CBOE**

### 3A — COT CFTC
- URL : `https://www.cftc.gov/dea/futures/deacmesf.htm`
- Fréquence : vendredi 19h30 EST
- Données : Net position Non-Commercials (Or, CL, 6J, ES, HG)

```python
COT_CODES = {
    "GC": "088691",  # Or
    "HG": "085692",  # Cuivre
    "CL": "067651",  # Pétrole
    "ES": "13874+",  # S&P 500
    "6J": "097741",  # Yen japonais
}
# net_position = Long - Short Non-Commercials
# >+100k = haussier institutionnel fort
# <-100k = baissier institutionnel fort
```

### 3B — Dark Pools FINRA
- URL : `https://www.finra.org/sites/default/files/ATS_Weekly.csv`
- Fréquence : hebdomadaire (délai 2 semaines)
- Proxy ETFs : GLD (Or), USO (Pétrole), SPY (ES), IBIT (BTC)

```python
# Ratio dark pool = volume_ATS / volume_total
# > 55% sur 2 semaines = accumulation institutionnelle silencieuse
```

### 3C — Put/Call Ratio CBOE
- URL : `https://cdn.cboe.com/api/global/us_indices/daily_prices/`
- Fréquence : quotidien fin de journée
- Seuils : >1.3 = panique, <0.7 = euphorie

### 3D — SKEW Index CBOE
- URL : `https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv`
- Fréquence : quotidien
- Seuils : >140 = institutionnels couverts contre crash

---

## CERCLE 4 — MACRO
**Sources : FRED + EIA + IMF + Finnhub**

### 4A — FRED API (gratuit, clé gratuite)
```python
FRED_SERIES = {
    "FEDFUNDS":  "Taux Fed",
    "CPIAUCSL":  "CPI Inflation",
    "T10Y2Y":    "Courbe des taux (inversion = alerte)",
    "DTWEXBGS":  "Dollar Index proxy",
}
# Fréquence : quotidien (données fin de journée)
```

### 4B — EIA Oil API (gratuit, clé gratuite sur eia.gov)
```python
EIA_URL = "https://api.eia.gov/v2/petroleum/sum/sndw/data/"
# Stocks pétrole → publié chaque MERCREDI 15h30 EST
# Si variation vs consensus > +/-3M barils → SIGNAL FORT CL
```

### 4C — Finnhub Calendrier Économique (gratuit)
```python
import finnhub
client = finnhub.Client(api_key="CLE_GRATUITE")
calendar = client.economic_calendar()
# Impact 3 = rouge = ZONE INTERDITE trading
# Règle : si événement rouge dans < 30 min → bloquer mode Auto
```

### 4D — IMF Gold Reserves (gratuit, mensuel)
```
URL : https://www.imf.org/external/np/sta/ir/IRProcessWeb/
Indicateur : achats banques centrales > 1000 tonnes/an = haussier GC
```

---

## CERCLE 5 — SENTIMENT
**Sources : Fear&Greed + AAII + CBOE SKEW**

### 5A — Fear & Greed Marchés
```python
FG_URL = "https://feargreedchart.com/api/"
# 0-24 = Extreme Fear (contrarian achat)
# 25-44 = Fear
# 45-55 = Neutral
# 56-74 = Greed
# 75-100 = Extreme Greed (contrarian vente)
```

### 5B — Fear & Greed Bitcoin
```python
FG_BTC_URL = "https://api.alternative.me/fng/"
# Même échelle 0-100
```

### 5C — AAII Sentiment Survey (jeudi)
```python
AAII_URL = "https://www.aaii.com/sentimentsurvey/sent.zip"
# Bullish > 55% = signal contrarian baissier
# Bearish > 50% = signal contrarian haussier
```

---

## CERCLE 6 — CATALYSEURS EXOGÈNES
**Sources : Finnhub News + GetXAPI + GDELT**

### 6A — Finnhub News + Sentiment
```python
client = finnhub.Client(api_key="CLE_GRATUITE")
# WebSocket temps réel pour news avec sentiment score
# Filtrer : |sentiment| > 0.70 + mots-clés critiques
MOTS_CLÉS = ["Fed","FOMC","CPI","NFP","Gold","OPEC","Iran",
             "Bitcoin ETF","JPY","DXY","China PMI","Oil supply"]
```

### 6B — GetXAPI (6 comptes X.com — ~1$/mois)
```python
GET_X_URL = "https://api.getxapi.com/v1/timeline"
COMPTES_SURVEILLÉS = [
    "@federalreserve",   # Fed officiel
    "@POTUS",            # Décisions géopolitiques
    "@saylor",           # Bitcoin institutionnel
    "@elonmusk",         # Bitcoin (1 tweet = ±5%)
    "@OPECSecretariat",  # Pétrole officiel
    "@WSJmarkets",       # Breaking news marchés
]
# Coût estimé : 6 comptes × 50 tweets/jour × 30j / 20 = ~0.45$/mois
# Règle : si tweet critique détecté → alerte + suspendre Auto 10 min
```

### 6C — GDELT Project (gratuit, illimité)
```python
GDELT_URL = "https://api.gdeltproject.org/api/v2/doc/doc"
# Toutes les 15 minutes, requête :
QUERIES = {
    "GC_CL": "oil OR gold OR 'Middle East' OR Iran OR OPEC",
    "HG":    "China copper OR 'copper demand' OR 'China PMI'",
    "ES":    "US economy OR 'Federal Reserve' OR recession",
    "6J":    "Japan OR BOJ OR 'yen intervention'",
    "BTC":   "Bitcoin OR crypto OR 'BTC ETF'",
}
# Mapping tensions → impact actif :
GÉOPOLITIQUE_IMPACT = {
    # Impact = signal d'orientation pour actifs TRADABLES (GC, HG, CL, ZW)
    # MBT et 6J n'apparaissent pas — ce sont des références seules.
    "Moyen-Orient_tension": {"GC": +1, "CL": +1, "ES": -1},
    "USA_Chine_tension":    {"HG": -1, "ES": -1},
    "Crise_bancaire":       {"GC": +2, "ES": -2},
    "OPEC_cut":             {"CL": +1, "ES": -0.5},
}
```

---

## CERCLE 7 — CORRÉLATIONS & RÉGIME
**Source : calcul Python local — 0$**

### 7A — Matrice corrélations glissantes (30 jours)

Source de vérité : `code\engine\correlations.py` — calcul live sur fenêtre 30j et 7j.

```python
import pandas as pd
# Calculé sur les données NT8 historiques (alignement strict avec correlations.py)
CORRELATION_PAIRS = [
    ("GC",  "DX"),   # Or vs Dollar — corrélation inverse classique
    ("GC",  "ES"),   # Or vs SP500 — risk on/off
    ("HG",  "ES"),   # Cuivre vs SP500 — indicateur croissance
    ("CL",  "DX"),   # Pétrole vs Dollar — corrélation inverse
    ("ZW",  "DX"),   # Blé vs Dollar — NOUVEAU
    ("ES",  "VX"),   # SP500 vs VIX — toujours inverse
    ("GC",  "MBT"),  # Or vs BTC — RÉFÉRENCE seul (pas d'ordre sur MBT)
    ("DX",  "6J"),   # Dollar vs Yen — RÉFÉRENCE seul (pas d'ordre sur 6J)
]

# RÈGLE : MBT et 6J apparaissent UNIQUEMENT dans les paires de référence.
#         Ils ne génèrent JAMAIS de signal d'ordre.
```

### 7B — Détecteur de régime de marché
```python
def detect_regime(vix, sp500_slope, gold_slope, dollar_slope, oil_slope):
    """
    Régimes de marché → orientation des actifs TRADABLES uniquement (GC, HG, CL, ZW).
    MBT et 6J ne sont JAMAIS des cibles d'ordre — ce sont des références.
    """
    if vix < 15 and sp500_slope > 0:
        return "RISK_ON"      # Favoriser HG, CL (cycliques) — éviter GC
    elif vix > 20 and gold_slope > 0:
        return "RISK_OFF"     # Favoriser GC — réduire HG, CL
    elif gold_slope > 0 and oil_slope > 0:
        return "INFLATION"    # Favoriser GC, CL, ZW (matières premières)
    elif vix > 35:
        return "CRISE"        # STOPPER mode Auto immédiatement
    else:
        return "NEUTRE"
```

### 7C — Inter-market Analysis (John Murphy)
```python
RÈGLES_INTERMARKET = {
    "dollar_fort_+1pct":  {"GC": -1, "CL": -1, "HG": -1, "6J": -1},
    "vix_spike_+15pct":   {"action": "ALERTE_ROUGE + taille ÷2"},
    "or_hausse_+2pct":    {"6J": +0.5, "ES": -0.3},
    "petrole_hausse_+3pct": {"ES": -0.4, "6J": -0.5, "GC": +0.3},
}
```

---

# SECTION 4 — MOTEUR DE DÉCISION CLAUDE AI

## Le prompt GOD MODE (template Python)

```python
GOD_MODE_PROMPT = """
Tu es le cerveau du système MBK Trading.
Applique les 2337 règles de la Knowledge Base.

═══════════════════════════════════════
ANALYSE GOD MODE — {timestamp}
Actif : {actif} | Régime : {regime}
═══════════════════════════════════════

[C1 — PRIX & TECHNIQUE]
BGC : {bary_zone} | Energie : {energie}% | Direction : {direction}
Pivot H : {pivot_h} | Pivot B : {pivot_b}
Marchés alignés : {alignes}/4 | Confirmations : {conf}/3
Couloir horaire : {couloir_actif}

[C2 — ORDER FLOW ATAS]
Cale : {cale} ({cale_force}×) | Fausse cassure : {fc}
Delta : {delta} | Squeeze : {sq}
DOM déséquilibre : {dom_ratio}× → {dom_dir}

[C3 — INSTITUTIONNELS]
COT {actif} net : {cot_net} lots → {cot_signal}
Dark Pool ratio (J-14) : {dp_ratio}%
Put/Call CBOE : {pc_ratio} | SKEW : {skew}

[C4 — MACRO]
Taux Fed : {fed}% | CPI : {cpi}%
Courbe 10Y-2Y : {curve} | DXY : {dxy}
Prochain événement rouge : {event} dans {time_event}
EIA stocks (dernier) : {eia}M barils (surprise: {eia_surprise}M)

[C5 — SENTIMENT]
F&G marchés : {fg_mkt}/100 | F&G BTC : {fg_btc}/100
AAII Bullish : {aaii_bull}% | VIX : {vix} (pct: {vix_pct}%)

[C6 — CATALYSEURS]
Dernière news critique : "{news_headline}" (sent: {news_sent})
GDELT tension : {gdelt}
X.com alerte : {x_alert}

[C7 — CORRÉLATIONS]
GC/DX : {corr_gc_dx} | ES/VX : {corr_es_vx} | BTC/ES : {corr_btc_es}
Inter-market actifs : {intermarket}

═══════════════════════════════════════
RÈGLES RISQUE :
Capital : {capital}$ | DD jour : {dd}%
Trades ouverts : {open}/2 | VIX filtre : {vix_ok}
Événement imminent : {event_bloq}
═══════════════════════════════════════

Réponds UNIQUEMENT en JSON strict :
{
  "signal": "ACHETER|VENDRE|ATTENDRE",
  "confiance": 0-100,
  "raison": "max 15 mots",
  "cercles_ok": [1,2,3,...],
  "cercles_ko": [4,5,...],
  "stop_loss": float,
  "take_profit": float,
  "taille": "normale|réduite|mini",
  "alerte": "texte ou null",
  "regime": "RISK_ON|RISK_OFF|INFLATION|NEUTRE|CRISE"
}
"""
```

## Système de scoring des 7 cercles

> ABANDONNE (D2 13/06) : le scoring /21 ci-dessous (7 cercles x 3) est remplace par une grille deterministe /10, seuil >= 7,0. Les 7 cercles restent des sources d'intelligence, ils ne sont plus une note /21. Voir CLAUDE.md.

```python
SCORE_CERCLES = {
    "C1_PRIX":           {"max": 3, "poids": "fondation"},
    "C2_ORDER_FLOW":     {"max": 3, "poids": "trigger"},
    "C3_INSTITUTIONNELS":{"max": 3, "poids": "direction"},
    "C4_MACRO":          {"max": 3, "poids": "contexte"},
    "C5_SENTIMENT":      {"max": 3, "poids": "timing"},
    "C6_CATALYSEURS":    {"max": 3, "poids": "urgence"},
    "C7_CORRÉLATIONS":   {"max": 3, "poids": "validation"},
}
# Score total : /21  [ABANDONNE -> /10 seuil 7,0, voir banniere ci-dessus]

DÉCISION_SCORE = {
    "18-21": "Signal ULTRA → Auto confiance ≥ 95%",
    "14-17": "Signal Fort → Auto si confiance ≥ 85%",
    "10-13": "Signal Moyen → Manuel uniquement",
    "7-9":   "Signal Faible → ATTENDRE",
    "< 7":   "Contradiction → NE PAS TRADER",
}
```

---

# SECTION 5 — RÈGLES DE RISQUE (inviolables — codées en dur)

```python
RÈGLES_RISQUE = {
    # === CAPITAL ===
    "max_risque_trade":        0.02,   # 2% max du capital
    "max_trades_simultanes":   2,
    "drawdown_stop_jour":      0.03,   # -3% → arrêt total journée

    # === VIX FILTRE ===
    "vix_taille_reduite":      20,     # VIX > 20 → taille ÷ 2
    "vix_no_trade":            35,     # VIX > 35 → aucun trade

    # === SIGNAUX MINIMUM ===
    "marchés_alignés_min":     3,      # règle 3/4
    "confirmations_min":       2,      # règle 2/3
    "confiance_auto_min":      85,     # mode auto
    "confiance_manuel_min":    65,     # mode manuel (affichage)

    # === ATAS BLOQUEURS ===
    "bloquer_si_fc":           True,   # fausse cassure → pas d'ordre
    "exiger_delta_confirm":    True,   # delta doit confirmer

    # === CATALYSEURS ===
    "zone_interdite_rouge":    30,     # min avant événement rouge
    "zone_alerte_rouge":       120,    # min → taille ÷ 2
    "x_alerte_suspend_auto":   10,     # min après tweet critique

    # === EIA PÉTROLE ===
    "eia_surprise_taille_red": 3.0,    # M barils → taille ÷ 2

    # === GÉOPOLITIQUE ===
    "gdelt_crise_stop_auto":   True,   # crise détectée → mode Manuel

    # === COULOIRS HORAIRES ===
    "couloirs": {
        "GC": ["08:20-10:30", "13:30-14:00"],
        "CL": ["09:00-10:30", "14:30-15:00"],
        "ES": ["09:30-11:00", "14:30-16:00"],
        "HG": ["09:00-11:00"],
        "6J": ["08:00-10:00", "14:30-15:30"],
        "MBT": ["09:00-11:00", "14:30-17:00"],
        "TOUS": ["16:30-16:35"],        # Blé + autres
    },
    "heures_interdites":       ["23:00-00:30"],  # rollover futures
}
```

---

# SECTION 6 — DASHBOARD

## Maquette Mode Manuel

```
╔═══════════════════════════════════════════════════════════════════╗
║  MBK GOD MODE v1.0          🟢 NT8  🟢 ATAS  🌐 7 CERCLES ACTIFS ║
╠══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════════╣
║      ║  GC  ║  HG  ║  CL  ║  ES  ║  VX  ║  BTC ║  6J  ║  MODE   ║
║ ACTIF║ 2847 ║ 4.23 ║ 72.1 ║ 5248 ║ 18.2 ║97400 ║ 0.67 ╠══════════╣
║      ║  ▲   ║  ▲   ║  ▼   ║  ▲   ║  ▼   ║  ▲   ║  ▲   ║ ●MANUEL ║
╠══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╣  ○AUTO  ║
║                                                        ╠══════════╣
║  🟢 SIGNAL : ACHETER GC (Or)                           ║ CONFIANCE║
║  Entrée  : 2 847 $                                     ║   91%    ║
║  Stop    : 2 831 $  (-16$ / -0.56%)                   ╠══════════╣
║  Objectif: 2 879 $  (+32$ / +1.12%)                   ║  R:R 1:2 ║
║  Taille  : NORMALE                                     ╠══════════╣
║  Raison  : BGC vert + COT institutionnels longs        ║ SCORE    ║
║                                                        ║  7,0/10  ║
║  ─── 7 CERCLES ────────────────────────────────        ╠══════════╣
║  C1 Prix         ✅ BGC vert + 3/4 alignés            ║[EXÉCUTER]║
║  C2 Order Flow   ✅ Cale ×3 + Delta positif           ║[IGNORER] ║
║  C3 Institutionnels ✅ COT +187k lots + DP 58%        ║          ║
║  C4 Macro        ✅ CPI stable + courbe ok             ║          ║
║  C5 Sentiment    ⚠️ F&G 62 (léger greed)              ║          ║
║  C6 Catalyseurs  ✅ GDELT calme + pas de news rouge   ║          ║
║  C7 Corrélations ✅ Dollar stable + régime RISK_ON    ║          ║
╠════════════════════════════════════════════════════════╩══════════╣
║ ALERTES : ⚠️ NFP dans 2h14 — Réduire taille de 50% après entrée  ║
║ JOURNAL JOUR  : 3 trades | +4.5 ticks | DD: 0.8% | EMR: +1.5t/trade║
╚════════════════════════════════════════════════════════════════════╝
```

---

# SECTION 7 — CALENDRIER D'INSTALLATION (10 semaines)

## ⚠️ AVANT DE COMMENCER : Prérequis à installer une fois

```
□ Python 3.11       → python.org (gratuit)
□ Node.js 18+       → nodejs.org (gratuit)
□ Git               → git-scm.com (gratuit)
□ NinjaTrader 8     → déjà installé
□ ATAS Pro          → trial 14 jours gratuit sur atas.net
□ Compte Rithmic    → via broker NTB (déjà si tu trades)
```

---

## SEMAINE 1 — FONDATION NT8

**Objectif : NinjaTrader exporte ses données vers Python**

```
Jour 1-2 :
□ Créer dossier projet : C:\MBK-SaaS\
□ Installer Python 3.11 dans C:\Python311\
□ Tester : ouvrir cmd → taper python --version

Jour 3-4 :
□ Dans NinjaTrader 8, créer un nouvel indicateur NinjaScript
   Menu : Tools → Edit NinjaScript → New → Indicator
   Nom : MBK_DataExporter
□ L'indicateur doit écrire un fichier CSV toutes les 2 secondes :
   C:\MBK-SaaS\data\NT8_data.csv

   Colonnes à exporter (pour chaque actif) :
   timestamp, symbol, open, high, low, close, volume,
   bgc_value, bgc_zone, direction, energie, pivot_h, pivot_b

□ Tester : ouvrir le fichier CSV et vérifier qu'il se met à jour

Jour 5-7 :
□ Tester connexion ATI NinjaTrader
   Menu NT8 : Tools → Options → Trading → Automated Trading Interface
   Activer l'ATI sur le port 36973 (défaut)
□ Écrire un script Python test qui envoie un ordre fictif via ATI
   (sur compte SIM NT8, jamais sur compte réel pendant les tests)
```

---

## SEMAINE 2 — INTÉGRATION ATAS

**Objectif : ATAS exporte ses signaux vers Python**

```
Jour 1-2 :
□ Télécharger ATAS Pro (trial 14 jours) → atas.net
□ Connecter ATAS au même feed Rithmic que NT8
□ Ouvrir les 8 actifs dans ATAS (même symboles que NT8)

Jour 3-4 :
□ Dans ATAS, configurer les 3 alertes :
   Alerte 1 : Big Trades (lots ≥ 2× normale)
   Alerte 2 : Delta divergence sur cassure pivot
   Alerte 3 : Volume × 3 + mèche × 2 (Squeeze)
□ Paramétrer export ATAS → fichier JSON :
   C:\MBK-SaaS\data\ATAS_signals.json

Jour 5-7 :
□ Écrire script Python qui lit NT8_data.csv + ATAS_signals.json
□ Afficher les données fusionnées dans la console
□ Valider : les données des 2 fichiers sont synchronisées (même timestamp)
```

---

## SEMAINE 3 — APIs GRATUITES (PRIORITÉ 1)

**Objectif : collecter les 4 sources les plus impactantes**

```
Jour 1 — FRED API :
□ Créer compte gratuit sur fred.stlouisfed.org → obtenir API Key
□ Script Python : fred_collector.py
   → Récupère FEDFUNDS, CPIAUCSL, T10Y2Y, DTWEXBGS
   → Sauvegarde dans C:\MBK-SaaS\data\macro.json
   → Fréquence : quotidienne (pas besoin de temps réel)

Jour 2 — Finnhub Calendar + News :
□ Créer compte gratuit sur finnhub.io → obtenir API Key
□ Script Python : finnhub_collector.py
   → Calendrier économique (events_calendar.json)
   → News avec sentiment (news_feed.json)
   → Fréquence : toutes les 5 minutes

Jour 3 — Fear & Greed :
□ Script Python : sentiment_collector.py
   → feargreedchart.com/api/ → fear_greed_stocks.json
   → api.alternative.me/fng/ → fear_greed_btc.json
   → Fréquence : toutes les 5 minutes

Jour 4 — GDELT Géopolitique :
□ Script Python : gdelt_collector.py
   → Requête toutes les 15 minutes
   → Filtrer par actif concerné
   → Sauvegarder dans gdelt_signals.json

Jour 5-7 :
□ Tester tous les collecteurs ensemble
□ Valider que les fichiers JSON se créent et se mettent à jour
□ Aucun collecteur ne doit planter les autres si erreur réseau
   (try/except sur chaque appel API)
```

---

## SEMAINE 4 — APIs GRATUITES (PRIORITÉ 2)

**Objectif : compléter les sources institutionnelles**

```
Jour 1 — EIA Oil API :
□ Créer compte gratuit sur eia.gov → obtenir API Key
□ Script : eia_collector.py
   → Actif uniquement mercredi 15h30 EST
   → Stocks pétrole vs consensus → eia_stocks.json

Jour 2 — CBOE Put/Call + SKEW :
□ Script : cboe_collector.py
   → CSV public Put/Call quotidien
   → CSV public SKEW Index
   → Fréquence : fin de journée

Jour 3 — CFTC COT Report :
□ Script : cot_collector.py
   → Actif uniquement vendredi 19h30 EST
   → Télécharge le CSV CFTC
   → Calcule net_position pour les 5 actifs cibles
   → Sauvegarde cot_data.json

Jour 4 — GetXAPI (6 comptes X.com) :
□ Créer compte sur getxapi.com (~1$/mois)
□ Script : x_collector.py
   → Surveille 6 comptes toutes les 5 minutes
   → Si tweet contient mot-clé critique → alerte dans x_alerts.json
□ Test : tweeter simulé → vérifier que l'alerte apparaît

Jour 5-7 :
□ Intégrer AAII Sentiment (téléchargement zip hebdomadaire jeudi)
□ Intégrer FINRA Dark Pools (CSV hebdomadaire)
□ Valider tous les collecteurs : 12 fichiers JSON bien présents
```

---

## SEMAINE 5 — MOTEUR BELKHAYATE PYTHON

**Objectif : recalculer les indicateurs Belkhayate en Python**

```
□ Implémenter BGC (Belkhayate Gravity Center) avec ratio 0.618
   Formule : centre de gravité statistique sur N périodes
□ Implémenter Direction + Energie
□ Implémenter Pivots Belkhayate
□ Implémenter règle 3/4 marchés (comparer 8 actifs)
□ Implémenter règle 2/3 confirmations
□ Implémenter détection couloirs horaires
□ Implémenter régime de marché (Risk-On/Off/Inflation/Crise)
□ Implémenter matrice corrélations glissantes (30J)

VALIDATION OBLIGATOIRE :
□ Comparer résultats Python vs résultats NinjaTrader sur 100 barres
   → Tolérance : ≤ 0.1% d'écart
   → Si écart > 0.1% → corriger le code Python
```

---

## SEMAINE 6 — INTÉGRATION CLAUDE API

**Objectif : le cerveau KB répond correctement**

```
Jour 1-2 :
□ Créer compte Anthropic → obtenir clé API (console.anthropic.com)
□ Script : claude_brain.py
   → Charge le prompt GOD MODE (Section 4 de ce document)
   → Fusionne les 12 fichiers JSON en un seul contexte
   → Envoie le prompt à Claude Sonnet
   → Parse le JSON retourné

Jour 3-4 :
□ Encoder les 2337 règles KB dans le system prompt Claude
   Structure recommandée :
   ├── Règles Belkhayate (BGC, Pivots, Direction, Energie)
   ├── Règles MBK (Liquidity Grab, Fibonacci, Fausse cassure)
   ├── Règles 3/4 marchés
   ├── Règles 2/3 confirmations
   ├── Règles inter-marchés
   └── Règles gestion du risque

□ IMPORTANT : le system prompt contenant les 2337 règles
   doit être envoyé une seule fois par session (économie tokens)

Jour 5-7 :
□ Tester 50 scénarios historiques connus
   (tu sais ce qui s'est passé → vérifier si Claude aurait donné le bon signal)
□ Calibrer les seuils de confiance
□ Vérifier que le JSON retourné est toujours valide (jamais de texte libre)
```

---

## SEMAINE 7 — DASHBOARD REACT

**Objectif : interface visuelle fonctionnelle**

```
□ Initialiser projet React + Vite + Tailwind :
   cmd → cd C:\MBK-SaaS → npm create vite@latest dashboard
□ Créer composants :
   ├── Header (NT8/ATAS status + mode Manuel/Auto)
   ├── ActifGrid (8 actifs en tableau)
   ├── SignalBox (signal actif + 7 cercles détaillés)
   ├── RiskPanel (capital, DD, trades ouverts)
   ├── AlertBar (alertes en temps réel)
   └── JournalTable (historique trades du jour)

□ Connecter au backend Python via WebSocket local
   (FastAPI + websockets library)
□ Tester : le dashboard se met à jour en temps réel
```

---

## SEMAINE 8 — MODE AUTOMATIQUE

**Objectif : le système exécute ses propres ordres**

```
□ Implémenter envoyeur d'ordres ATI :
   ati_sender.py → connexion TCP/IP locale port 36973
   → Commandes : PLACE, CANCEL, CLOSEALL

□ Implémenter toutes les règles de risque (Section 5)
   → Chaque règle doit bloquer ou permettre l'envoi

□ Implémenter circuit breaker :
   → Si 3 pertes consécutives → pause 2 heures
   → Si DD > 2% en journée → passage forcé en Mode Manuel
   → Si erreur ATI → alerte + blocage Auto

□ VALIDER chaque règle de risque sur simulation :
   Tester les 12 cas de blocage un par un
```

---

## SEMAINES 9-10 — PAPER TRADING OBLIGATOIRE

**Objectif : valider les métriques avant tout argent réel**

```
CONFIGURATION :
□ NT8 en mode SIM (compte simulation, zéro argent réel)
□ Tous les autres systèmes en mode production (vraies données)
□ Durée minimum : 2 semaines = ~10 jours de trading

MÉTRIQUES À VALIDER (toutes les 8 obligatoires) :

| Métrique            | Seuil minimum | Ta mesure | OK ? |
|---------------------|---------------|-----------|------|
| Win Rate            | ≥ 55%         |           |      |
| EMR (esperance)     | ≥ +1.5 ticks  |           |      |
| Profit Factor       | ≥ 1.5         |           |      |
| Max Drawdown/jour   | ≤ 3%          |           |      |
| Faux positifs ATAS  | ≤ 30%         |           |      |
| F. cassures évitées | ≥ 70%         |           |      |
| Score moyen signaux | ≥ 7/10        |           |      |
| Amélioration EMR/7C | ≥ +0.5 tick   |           |      |

→ Si UNE métrique non atteinte : ajuster KB + retester
→ NE JAMAIS passer en live sans 8/8 métriques validées
```

---

# SECTION 8 — CALENDRIER GLOBAL SYNTHÈSE

```
SEMAINE 1  ─ Fondation NT8 (export CSV + ATI test)
SEMAINE 2  ─ ATAS intégration (export JSON + alertes)
SEMAINE 3  ─ 4 APIs gratuites priorité 1 (FRED, Finnhub, F&G, GDELT)
SEMAINE 4  ─ 4 APIs gratuites priorité 2 (EIA, CBOE, COT, GetXAPI)
SEMAINE 5  ─ Moteur Belkhayate Python (validation vs NT8)
SEMAINE 6  ─ Claude API + KB 2337 règles (50 tests historiques)
SEMAINE 7  ─ Dashboard React (interface Manuel + Auto)
SEMAINE 8  ─ Mode Automatique (ATI + règles risque + circuit breaker)
SEMAINE 9  ─ Paper Trading semaine 1 (mesure métriques)
SEMAINE 10 ─ Paper Trading semaine 2 + validation 8 métriques
                      │
              ⬇ 8/8 métriques OK ⬇
                      │
              ════ LIVE TRADING ════
```

---

# SECTION 9 — STRUCTURE DES FICHIERS DU PROJET

```
C:\MBK-SaaS\
├── data\                          ← Fichiers JSON/CSV (mise à jour auto)
│   ├── NT8_data.csv               ← NinjaTrader 8 (toutes les 2 sec)
│   ├── ATAS_signals.json          ← ATAS Pro (toutes les 2 sec)
│   ├── macro.json                 ← FRED API (quotidien)
│   ├── events_calendar.json       ← Finnhub (toutes les 5 min)
│   ├── news_feed.json             ← Finnhub news (toutes les 5 min)
│   ├── fear_greed_stocks.json     ← F&G (toutes les 5 min)
│   ├── fear_greed_btc.json        ← Alternative.me (toutes les 5 min)
│   ├── gdelt_signals.json         ← GDELT (toutes les 15 min)
│   ├── x_alerts.json              ← GetXAPI (toutes les 5 min)
│   ├── eia_stocks.json            ← EIA (mercredi 15h30)
│   ├── cboe_pc_skew.json          ← CBOE (quotidien fin de journée)
│   ├── cot_data.json              ← CFTC (vendredi 19h30)
│   ├── dark_pools.json            ← FINRA (hebdomadaire)
│   ├── aaii_sentiment.json        ← AAII (jeudi)
│   └── imf_gold.json              ← IMF (mensuel)
│
├── collectors\                    ← Scripts Python collecteurs
│   ├── fred_collector.py
│   ├── finnhub_collector.py
│   ├── sentiment_collector.py
│   ├── gdelt_collector.py
│   ├── eia_collector.py
│   ├── cboe_collector.py
│   ├── cot_collector.py
│   ├── x_collector.py
│   ├── aaii_collector.py
│   ├── finra_collector.py
│   └── imf_collector.py
│
├── engine\                        ← Cerveau Python
│   ├── belkhayate.py              ← Calculs BGC, Direction, Energie
│   ├── rules_34.py                ← Règle 3/4 marchés + 2/3 conf.
│   ├── correlations.py            ← Matrice + régime + inter-market
│   ├── risk_manager.py            ← Toutes les règles de risque
│   ├── signal_scorer.py           ← Scoring 7 cercles
│   └── claude_brain.py            ← Appel Claude API + parse JSON
│
├── execution\                     ← Envoi ordres
│   └── ati_sender.py              ← Connexion ATI NT8
│
├── api\                           ← Serveur FastAPI local
│   └── server.py                  ← WebSocket + endpoints Dashboard
│
├── dashboard\                     ← Interface React
│   └── src\
│       ├── App.jsx
│       ├── components\
│       │   ├── Header.jsx
│       │   ├── ActifGrid.jsx
│       │   ├── SignalBox.jsx
│       │   ├── RiskPanel.jsx
│       │   ├── AlertBar.jsx
│       │   └── JournalTable.jsx
│
├── kb\                            ← Knowledge Base
│   └── mbk_rules_2337.txt         ← Tes 2337 règles formatées
│
├── logs\                          ← Journaux
│   ├── trades_history.db          ← SQLite
│   └── signals_log.json
│
└── config\                        ← Configuration
    ├── .env                       ← Clés API (jamais commiter)
    ├── settings.py                ← Paramètres globaux
    └── risk_rules.py              ← Règles risque (source de vérité)
```

---

# SECTION 10 — MODE MANUEL vs MODE AUTO

## Mode Manuel
- Signal affiché dans le dashboard avec score /10 et confiance %
- Abdelkrim décide : **EXÉCUTER** ou **IGNORER**
- Disponible dès confiance ≥ 65%
- Aucune exécution automatique

## Mode Auto
- **Conditions d'éligibilité** : confiance ≥ 75% ET score ≥ 7,0/10 (D2) ET DD_jour < 2%
- **Exécution** via NT8 ATI (TCP/IP local port 36973)
- **Bloqué automatiquement** si :
  - Claude API indisponible (fallback max 65% → Auto interdit)
  - VIX > 35
  - Événement rouge dans < 30 min
  - DD journalier > 2%
  - Circuit breaker ouvert
  - Fausse cassure détectée par ATAS
- **Suspension** : 15 min après perte normale, 60 min si DD > 1.5%

## Bascule Manuel ↔ Auto
- **Manuel → Auto** : bouton dans dashboard, confirmation requise
- **Auto → Manuel** : automatique si l'une des conditions de blocage devient active

---

# SECTION 11 — RÈGLES RISQUE COMPLÈTES

## Seuils de risque (`code\config\settings.py` — source de vérité)

```python
max_risque_trade        = 0.02   # 2% du capital
max_trades_simultanes   = 2
drawdown_stop_jour      = 0.03   # 3% → arrêt total journée
vix_taille_reduite      = 25     # VIX > 25 → taille ÷ 2
vix_no_trade            = 35     # VIX > 35 → aucun trade
confiance_min_auto      = 0.75   # 75%
confiance_max_fallback  = 0.65   # 65% (Claude API indisponible)
zone_interdite_rouge    = 30     # min avant NFP/FOMC/CPI
suspension_min          = 15     # min après perte
suspension_max          = 60     # min si DD > 1.5%
```

## Circuit Breaker (`code\engine\circuit_breaker.py`)
- **CB_NT8** : timeout 15s → retry 2× → `BLOCKED` si NT8 planté
- **CB_ATAS** : timeout 15s → retry 2× → `MANUAL_ONLY` si ATAS planté
- **CB_CLAUDE** : timeout 15s → retry 2× → `FALLBACK_LOCAL` si Claude planté

## Staleness Monitor (`code\engine\staleness_monitor.py`)
- **NT8_data** : stale si > 10s → `BLOCKED`
- **ATAS_data** : stale si > 30s → `MANUAL_ONLY`
- **COT CFTC** : stale si > 168h (7 jours) → `WARNING`

## Atomic Writes (`code\utils\atomic_writer.py`)
- Toutes les écritures JSON passent par `atomic_write()`
- `tempfile` + `os.replace` — jamais `json.dumps()` direct sur fichier live

---

# SECTION 12 — CHECKLIST DÉMARRAGE PRODUCTION

## Avant chaque session de trading
- [ ] NT8 ouvert + indicateurs Belkhayate chargés (GC, HG, CL, ZW)
- [ ] ATAS Pro connecté à Rithmic + 4 actifs ouverts
- [ ] Python engine démarré : `python code\engine\main_loop.py`
- [ ] Dashboard React ouvert : `http://localhost:5173`
- [ ] Vérifier : `staleness_monitor` → tous les actifs `OPERATIONAL`
- [ ] Vérifier : `circuit_breaker` → tous CB `CLOSED` (= opérationnel)
- [ ] Vérifier : `ANTHROPIC_API_KEY` présente dans `.env`
- [ ] Vérifier : pas d'événement rouge dans les 30 prochaines minutes

## En cas de problème
| Défaillance | Effet | Action |
|-------------|-------|--------|
| NT8 planté | CB_NT8 OPEN → BLOCKED | Attendre reconnexion |
| ATAS planté | CB_ATAS OPEN → MANUAL_ONLY | Signaux sans order flow |
| Claude planté | CB_CLAUDE OPEN → FALLBACK_LOCAL | Max 65%, Auto interdit |
| DD > 3% | Arrêt total | Fermer positions, ne pas re-trader ce jour |

## Fin de session
- [ ] Fermer toutes les positions ouvertes
- [ ] `git add . && git commit -m "chore: session YYYY-MM-DD terminee"`
- [ ] `git push origin main`
- [ ] Mettre à jour `_context\briefing-[date].md`

---

*DOCUMENT MASTER v2.0 — TRADEX-AI*
*Vision : NinjaTrader 8 + ATAS Pro + Python 3.11 + Claude API claude-sonnet-4-6*
*Méthode Belkhayate | 7 Cercles | Mode Manuel + Mode Auto*
*Budget ~146-151$/mois | 10 semaines de déploiement | Sources vérifiées*
