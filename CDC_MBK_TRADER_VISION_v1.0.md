═══════════════════════════════════════════════════════
CDC MBK TRADER ASSISTANT — VISION v1.0
═══════════════════════════════════════════════════════
📅 30/04/2026
Source : Extraction stricte du code source mbk-trader-v1.0.zip
Zéro hallucination — tout élément vient d'un fichier existant
═══════════════════════════════════════════════════════

🎯 PROJET
  Nom        : MBK Trader Assistant
  Slug       : mbk-trader
  Secteur    : TradingTech (assistance au trading algorithmique)
  Cible      : Trader solo, usage personnel, Windows uniquement
  Vision     : Détecter automatiquement les fausses cassures
               institutionnelles (Liquidity Grab) sur matières premières
               et intermarchés, et signaler l'entrée après pullback
               Fibonacci confirmé — usage strictement personnel.

👤 UTILISATEUR UNIQUE
  Type       : Trader solo — 1 seul compte, aucun multi-tenant
  Login      : Google OAuth 2.0 (popup Electron)
  Stockage   : Local PC uniquement — SQLite — zéro cloud

📡 SOURCE DE DONNÉES
  Broker/Platform : NinjaTrader 8 (installé localement)
  Connexion       : Add-on NinjaScript C# → WebSocket ws://localhost:8765
  Marchés couverts (déclarés dans le code) :
    - Gold  : XAUUSD
    - Silver: XAGUSD
    - Oil   : CL (Crude Oil)
    - Gas   : NG (Natural Gas)
    - Index : ES, NQ
    - FX    : DXY (corrélation uniquement)
  Timeframes actifs : M5, M15, H1
  Timeframes ignorés : M1 (bruit), D1+

⚙️ FONCTIONNALITÉS V1 (présentes dans le code)

  MODULE 1 — Détection fausses cassures (false_breakout.py)
    Étape 1 : Identification zone résistance/support (swing 20 bougies)
    Étape 2 : Détection cassure + ratio volume (seuil × 1.3)
    Étape 3 : Analyse retour dans zone ≤ 3 bougies
    Étape 4 : Pullback Fibonacci 50–61.8% + bougie de rejet
    Étape 5 : Validation multi-conditions → signal final

  MODULE 2 — Générateur de signaux (signal_generator.py)
    Statuts produits :
      TRADE_ALLOWED  🟢 — 7 conditions validées
      WAIT           🟡 — setup valide, hors session
      REDUCE_RISK    🟠 — ≥ 5/7 conditions, taille réduite 50%
      NO_TRADE       🔴 — news, circuit breaker, ou < 5 conditions

  MODULE 3 — Indicateurs MBK (mbk_indicators.py)
    MBKZoneEngine     : Order Blocks BULLISH_OB / BEARISH_OB / EXHAUSTION_ZONE
    MBKImpulseDetector: STRONG / WEAK / SPIKE selon amplitude ATR + volume
    MBKTimingFilter   : SESSION_OPEN / SETUP_WINDOW / CLOSE_WINDOW / OFF_SESSION

  MODULE 4 — Filtre sessions (MBK_SessionFilter.cs + mbk_indicators.py)
    Sessions GMT+1 (Maroc) :
      LONDON    : 09h00–12h00
      NEW_YORK  : 15h00–18h00
      OVERLAP   : 15h00–17h00
    Fenêtre setup : 30–90 min après open de session
    Hors session  : signal forcé WAIT automatiquement

  MODULE 5 — Gate News (news_gate.py)
    Source : ForexFactory RSS XML (gratuit)
    Blocage : ±30 min autour des news HIGH IMPACT
    Cache   : rafraîchi toutes les 15 minutes
    Si news active → statut forcé NO_TRADE

  MODULE 6 — Alertes temps réel (Dashboard.tsx)
    Notification Windows toast (via electronAPI)
    Alerte sonore (via electronAPI.playAlert)
    Badge coloré en temps réel dans le dashboard

  MODULE 7 — Backtesting (backtest_engine.py)
    Source données : CSV exporté depuis NinjaTrader 8
    Fenêtre glissante : 30 bougies
    Métriques calculées : Win Rate, Profit Factor, Max Drawdown,
                          R:R moyen, Sharpe Ratio, Total Return
    Seuils de validation :
      Win Rate minimum      : 45%
      Profit Factor minimum : 1.5
      Drawdown maximum      : 15%
      R:R moyen minimum     : 1.8
      Sharpe minimum        : 1.0
      Trades minimum        : 50
    Verdicts : VALIDATED / WEAK / REJECTED / DANGEROUS

🛡️ GARDE-FOUS TRADING (présents dans signal_generator.py)
  Stop-Loss    : 1.5 × ATR — aucun signal sans SL calculé
  Risk/Trade   : Max 1% du capital
  Circuit Breaker : 3 pertes consécutives → pause 4 heures forcée
  News Gate    : Bloque ±30 min autour des news HIGH IMPACT
  Filtrage session : Signaux ignorés hors LONDON / NEW_YORK / OVERLAP

🛠️ STACK RÉELLE (extraite de requirements.txt et package.json)
  Add-on broker : NinjaScript C# (.NET) — NinjaTrader 8
  Backend IA    : Python 3.11 + FastAPI 0.110 + uvicorn
  Données       : pandas 2.2.2, numpy 1.26.4, pandas-ta 0.3.14b
  ML            : scikit-learn 1.4.2
  WebSocket     : websockets 12.0
  BDD locale    : SQLite3 (Python stdlib)
  Desktop       : Electron.js 30 + React 18 + TypeScript
  Style         : Tailwind CSS 3.4
  Charts        : recharts 2.x
  Auth          : Google OAuth 2.0 (popup Electron)
  Build tool    : Vite 5.2
  Tests         : pytest 8.2

🗄️ BASE DE DONNÉES (structure réelle dans main.py)
  Table signals :
    id, timestamp, symbol, timeframe, direction, status,
    entry_price, stop_loss, take_profit, risk_pct, session, reason
  Table bars :
    id, symbol, timeframe, timestamp, open, high, low, close,
    volume, session — UNIQUE(symbol, timeframe, timestamp)

🌐 COMMUNICATION INTERNE (ports réels déclarés dans le code)
  ws://localhost:8765  → NinjaTrader 8 → Python (réception bougies)
  http://localhost:8000 → Python FastAPI (REST)
  ws://localhost:8000/stream → Python → Electron (diffusion signaux)
  http://localhost:5173 → Vite dev server (développement uniquement)

📦 PÉRIMÈTRE V1
  INCLUS   : Modules 1→7 ci-dessus + Google Auth + SQLite local
  HORS V1  : Mobile, cloud backup, multi-users, broker réel (exécution)
  HORS SCOPE DÉFINITIF : exécution automatique d'ordres (SaaS = assistance)

═══════════════════════════════════════════════════════
✅ CDC Vision basé à 100% sur le code source existant
   Aucune fonctionnalité inventée
═══════════════════════════════════════════════════════
