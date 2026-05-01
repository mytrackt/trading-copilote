===============================================================
CDC MBK TRADER ASSISTANT — VISION v1.1
===============================================================
Date creation : 30/04/2026
Date mise a jour : 30/04/2026 (post-audit securite)
Source : Extraction stricte du code source mbk-trader-v1.0.zip
Zero hallucination — tout element vient d'un fichier existant
===============================================================

PROJET
  Nom        : MBK Trader Assistant
  Slug       : mbk-trader
  Secteur    : TradingTech (assistance au trading algorithmique)
  Cible      : Trader solo, usage personnel, Windows uniquement
  Vision     : Detecter automatiquement les fausses cassures
               institutionnelles (Liquidity Grab) sur matieres premieres
               et intermarches, et signaler l'entree apres pullback
               Fibonacci confirme — usage strictement personnel.

UTILISATEUR UNIQUE
  Type       : Trader solo — 1 seul compte, aucun multi-tenant
  Login      : Google OAuth 2.0 (popup Electron)
  Stockage   : Local PC uniquement — SQLite — zero cloud

SOURCE DE DONNEES
  Broker/Platform : NinjaTrader 8 (installe localement)
  Connexion       : Add-on NinjaScript C# -> WebSocket ws://localhost:8765
  Marches couverts (declares dans le code) :
    - Gold  : XAUUSD
    - Silver: XAGUSD
    - Oil   : CL (Crude Oil)
    - Gas   : NG (Natural Gas)
    - Index : ES, NQ
    - FX    : DXY (correlation uniquement)
  Timeframes actifs : M5, M15, H1
  Timeframes ignores : M1 (bruit), D1+

FONCTIONNALITES V1 (presentes dans le code)

  MODULE 1 — Detection fausses cassures (false_breakout.py)
    Etape 1 : Identification zone resistance/support (swing 20 bougies)
    Etape 2 : Detection cassure + ratio volume (seuil x 1.3)
    Etape 3 : Analyse retour dans zone <= 3 bougies
    Etape 4 : Pullback Fibonacci 50–61.8% + bougie de rejet
    Etape 5 : Validation multi-conditions -> signal final

  MODULE 2 — Generateur de signaux (signal_generator.py)
    Statuts produits :
      TRADE_ALLOWED  — 7 conditions validees
      WAIT           — setup valide, hors session
      REDUCE_RISK    — >= 5/7 conditions, taille reduite 50%
      NO_TRADE       — news, circuit breaker, ou < 5 conditions

  MODULE 3 — Indicateurs MBK (mbk_indicators.py)
    MBKZoneEngine     : Order Blocks BULLISH_OB / BEARISH_OB / EXHAUSTION_ZONE
    MBKImpulseDetector: STRONG / WEAK / SPIKE selon amplitude ATR + volume
    MBKTimingFilter   : SESSION_OPEN / SETUP_WINDOW / CLOSE_WINDOW / OFF_SESSION

  MODULE 4 — Filtre sessions (MBK_SessionFilter.cs + mbk_indicators.py)
    Sessions GMT+1 (Maroc) :
      LONDON    : 09h00–12h00
      NEW_YORK  : 15h00–18h00
      OVERLAP   : 15h00–17h00
    Fenetre setup : 30–90 min apres open de session
    Hors session  : signal force WAIT automatiquement

  MODULE 5 — Gate News (news_gate.py)
    Source : ForexFactory RSS XML (gratuit)
    Blocage : +/-30 min autour des news HIGH IMPACT
    Cache   : rafraichi toutes les 15 minutes
    Si news active -> statut force NO_TRADE

  MODULE 6 — Alertes temps reel (Dashboard.tsx)
    Notification Windows toast (via electronAPI)
    Alerte sonore (via electronAPI.playAlert)
    Badge colore en temps reel dans le dashboard

  MODULE 7 — Backtesting (backtest_engine.py)
    Source donnees : CSV exporte depuis NinjaTrader 8
    Fenetre glissante : 30 bougies
    Metriques calculees : Win Rate, Profit Factor, Max Drawdown,
                          R:R moyen, Sharpe Ratio, Total Return
    Seuils de validation :
      Win Rate minimum      : 45%
      Profit Factor minimum : 1.5
      Drawdown maximum      : 15%
      R:R moyen minimum     : 1.8
      Sharpe minimum        : 1.0
      Trades minimum        : 50
    Verdicts : VALIDATED / WEAK / REJECTED / DANGEROUS

GARDE-FOUS TRADING (presents dans signal_generator.py)
  Stop-Loss    : 1.5 x ATR — aucun signal sans SL calcule
  Risk/Trade   : Max 1% du capital
  Circuit Breaker : 3 pertes consecutives -> pause 4 heures forcee
                    Persiste en SQLite (survit au redemarrage serveur)
  News Gate    : Bloque +/-30 min autour des news HIGH IMPACT
  Filtrage session : Signaux ignores hors LONDON / NEW_YORK / OVERLAP
  API Token    : X-API-Token partage Electron <-> FastAPI
  Path Traversal : CSV limite a database/historical/ uniquement
  CORS         : origins restreints localhost:5173 + localhost:3000

STACK REELLE (extraite de requirements.txt et package.json)
  Add-on broker : NinjaScript C# (.NET) — NinjaTrader 8
  Backend IA    : Python 3.11 + FastAPI 0.110 + uvicorn
  Donnees       : pandas 2.2.2, numpy 1.26.4, pandas-ta 0.3.14b
  ML            : scikit-learn 1.4.2
  WebSocket     : websockets 12.0
  BDD locale    : SQLite3 (Python stdlib)
  Desktop       : Electron.js 30 + React 18 + TypeScript
  Style         : Tailwind CSS 3.4
  Charts        : recharts 2.x
  Auth          : Google OAuth 2.0 PKCE + safeStorage (AES natif Windows)
  Build tool    : Vite 5.2
  Tests         : pytest 8.2
  Rate limiting : slowapi 0.1.9
  Validation payload : Pydantic BarPayload (FastAPI)

BASE DE DONNEES (structure reelle dans main.py)
  Table signals :
    id, timestamp, symbol, timeframe, direction, status,
    entry_price, stop_loss, take_profit, risk_pct, session, reason
  Table bars :
    id, symbol, timeframe, timestamp, open, high, low, close,
    volume, session — UNIQUE(symbol, timeframe, timestamp)

COMMUNICATION INTERNE (ports reels declares dans le code)
  ws://localhost:8765  -> NinjaTrader 8 -> Python (reception bougies)
  http://localhost:8000 -> Python FastAPI (REST)
  ws://localhost:8000/stream -> Python -> Electron (diffusion signaux)
  http://localhost:5173 -> Vite dev server (developpement uniquement)

PERIMETRE V1
  INCLUS   : Modules 1->7 ci-dessus + Google Auth + SQLite local
  HORS V1  : Mobile, cloud backup, multi-users, broker reel (execution)
  HORS SCOPE DEFINITIF : execution automatique d'ordres (SaaS = assistance)

===============================================================
CDC Vision v1.1 base a 100% sur le code source existant
Aucune fonctionnalite inventee
Mis a jour apres audit securite — score 57/100 -> 85+/100
===============================================================
