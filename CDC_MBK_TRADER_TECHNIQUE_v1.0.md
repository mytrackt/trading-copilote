# CDC MBK TRADER ASSISTANT — TECHNIQUE v1.0
**Date : 30/04/2026**
**Source : Extraction stricte du code source mbk-trader-v1.0.zip**
**Règle : Zéro hallucination — chaque élément référence un fichier réel**

---

## §1. ARCHITECTURE GLOBALE

```
┌─────────────────────────────────────────────────────────────────┐
│                    NINJATRADER 8 (Windows)                       │
│  MBK_DataBridge.cs      →  WebSocket ws://localhost:8765         │
│  MBK_SessionFilter.cs   →  filtre sessions (intégré)             │
└──────────────────────────┬──────────────────────────────────────┘
                           │ JSON {symbol,tf,ohlcv,session,timestamp}
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│               PYTHON FASTAPI  (localhost:8000)                   │
│                                                                  │
│  main.py                ←  WebSocket /ninjatrader                │
│  detector/              │  WebSocket /stream → Electron           │
│    false_breakout.py    │  REST GET /status                       │
│    signal_generator.py  │  REST GET /signals                      │
│  indicators/            │  REST GET /trades                       │
│    mbk_indicators.py    │  REST POST /backtest                    │
│    news_gate.py         │                                         │
│  backtest/              │                                         │
│    backtest_engine.py   │                                         │
│                         │                                         │
│  SQLite  mbk_trades.db  │  tables: signals, bars                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ WebSocket ws://localhost:8000/stream
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              ELECTRON DESKTOP APP (Windows)                      │
│                                                                  │
│  main.js          ←  BrowserWindow + Tray                        │
│  preload.js        ←  contextBridge (contextIsolation: true)     │
│  src/App.tsx       ←  React 18 + Router 3 pages                  │
│    pages/Login.tsx     ←  Google OAuth 2.0 popup                 │
│    pages/Dashboard.tsx ←  Signaux temps réel + badges            │
│    pages/History.tsx   ←  Historique SQLite                      │
│    pages/Backtest.tsx  ←  Interface backtest                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## §2. COMPOSANT 1 — ADD-ON NINJATRADER 8

### Fichier : `ninja-addon/MBK_DataBridge.cs`

**Classe :** `NinjaTrader.NinjaScript.Indicators.MBK_DataBridge`
**Héritage :** `Indicator`
**Calculate :** `Calculate.OnBarClose`

**Méthodes publiques :**

| Méthode | Déclencheur | Action |
|---------|-------------|--------|
| `OnStateChange()` | State.SetDefaults | Configure nom, Calculate, IsOverlay |
| `OnStateChange()` | State.DataLoaded | Appelle `ConnectWebSocket()` |
| `OnStateChange()` | State.Terminated | Appelle `DisconnectWebSocket()` |
| `OnBarUpdate()` | Clôture de bougie | Construit JSON + appelle `SendAsync()` |
| `ConnectWebSocket()` | async void | Connexion à ws://localhost:8765 |
| `DisconnectWebSocket()` | async void | Fermeture propre WebSocket |
| `GetCurrentSession()` | privée | Retourne string session GMT+1 |
| `SendAsync(string)` | async void | Envoie payload JSON |

**Payload JSON envoyé (format exact) :**
```json
{
  "symbol":    "XAUUSD",
  "timeframe": "15Minute",
  "open":      2345.50000,
  "high":      2348.20000,
  "low":       2343.10000,
  "close":     2346.80000,
  "volume":    1542,
  "timestamp": "2026-04-30T10:15:00Z",
  "session":   "LONDON",
  "bar_index": 1247
}
```

**Logique session (GMT+1 Maroc) :**
```
hour 9–11  → "LONDON"
hour 15–16 → "OVERLAP"
hour 15–17 → "NEW_YORK"
autre      → "OFF_SESSION"
```

**États WebSocket gérés :**
- `WebSocketState.Open` → envoi actif
- Exception lors envoi → `_isConnected = false` (log NT8 Output Window)
- Reconnexion : non automatique v1 — rechargement de l'indicateur requis

---

### Fichier : `ninja-addon/MBK_SessionFilter.cs`

**Classe :** `NinjaTrader.NinjaScript.Indicators.MBK_SessionFilter`
**Calculate :** `Calculate.OnEachTick`

**Propriétés publiques exposées :**
```csharp
bool IsActiveSession   // true si LONDON ou NEW_YORK
string CurrentSession  // "LONDON" | "NEW_YORK" | "OVERLAP" | "OFF_SESSION"
bool IsSetupWindow     // true si 30–90 min après open session
```

**Constantes de sessions (GMT+1) :**
```csharp
LONDON_START  = 9    LONDON_END  = 12
NY_START      = 15   NY_END      = 18
OVERLAP_START = 15   OVERLAP_END = 17
```

**Coloration du fond graphique NT8 :**
```
OVERLAP           → BackBrush = LightGoldenrodYellow
LONDON ou NY      → BackBrush = LightCyan
OFF_SESSION       → BackBrush = null
```

---

## §3. COMPOSANT 2 — MOTEUR IA PYTHON

### §3.1 — `detector/false_breakout.py`

**Classe principale :** `FalseBreakoutDetector`

**Constantes du détecteur :**
```python
ATR_ZONE_MULTIPLIER  = 0.5   # ±0.5 ATR autour du niveau
VOLUME_THRESHOLD     = 1.3   # cassure suspecte si volume < moyenne × 1.3
BREAKOUT_MAX_CANDLES = 2     # cassure suspecte si ≤ 2 bougies hors zone
PULLBACK_MAX_CANDLES = 3     # retour dans zone attendu ≤ 3 bougies
FIBO_50              = 0.50
FIBO_618             = 0.618
```

**DataFrame requis en entrée :**
- Colonnes obligatoires : `open`, `high`, `low`, `close`, `volume`
- Minimum : 25 lignes (lève `ValueError` sinon)
- Calculs ajoutés : `atr` (ATR 14 périodes), `volume_avg` (rolling 20)

**Énumérations :**
```python
class BreakoutStatus(str, Enum):
    ZONE_IDENTIFIED          # zone détectée, pas de cassure
    BREAKOUT_DETECTED        # cassure en cours
    BREAKOUT_SUSPICIOUS      # ≤ 2 bougies + volume faible
    BREAKOUT_REAL            # ≤ 2 bougies + volume fort
    FALSE_BREAKOUT_CONFIRMED # prix revenu dans zone ≤ 3 bougies
    REAL_BREAKOUT_CONFIRMED  # prix resté hors zone > 3 bougies
    PULLBACK_CONFIRMED       # Fibo 50-61.8% + bougie de rejet
    WAIT                     # fausse cassure confirmée, pullback attendu

class SignalStatus(str, Enum):
    TRADE_ALLOWED
    WAIT
    REDUCE_RISK
    NO_TRADE
```

**Méthodes publiques :**

| Méthode | Retour | Description |
|---------|--------|-------------|
| `identify_zone()` | `(float, float)` | zone_high, zone_low via swing 20 dernières bougies |
| `detect_breakout(zh, zl)` | `(BreakoutStatus, str, int, float)` | status, direction, nb_candles, volume_ratio |
| `analyze_post_breakout(zh, zl, dir)` | `BreakoutStatus` | retour dans zone → FALSE_BREAKOUT_CONFIRMED |
| `wait_for_pullback(dir, zh, zl)` | `(BreakoutStatus, float, float, float, bool)` | pullback_status, level, fibo50, fibo618, rejection |
| `full_analysis()` | `BreakoutAnalysis` | Exécute les 4 étapes et retourne dataclass |

**Dataclass retournée :**
```python
@dataclass
class BreakoutAnalysis:
    status: BreakoutStatus
    zone_high: float
    zone_low: float
    breakout_candles: int
    volume_ratio: float
    pullback_level: Optional[float]
    fibo_50: Optional[float]
    fibo_618: Optional[float]
    rejection_candle: bool
    direction: str  # "BULLISH" | "BEARISH" | "NEUTRAL"
```

**Détection bougie de rejet (`_detect_rejection_candle`) :**
- Pin Bar : `body / total_range < 0.3` (corps < 30% du range)
- Engulfing : corps actuel > corps précédent × 1.5 + direction opposée

---

### §3.2 — `detector/signal_generator.py`

**Classe :** `SignalGenerator` (méthodes de classe — stateless par instance)

**Constantes :**
```python
STOP_LOSS_ATR_MULTIPLIER = 1.5   # SL = 1.5 × ATR
TAKE_PROFIT_RR           = 2.0   # TP = entrée ± (SL_distance × 2.0)
MAX_RISK_PERCENT         = 1.0   # 1% du capital par trade
NEWS_WINDOW_MINUTES      = 30    # bloqué ±30 min autour des news
```

**Variables de classe (état global) :**
```python
_consecutive_losses    = 0         # compteur pertes consécutives
_circuit_breaker_until = None      # datetime ou None
```

**7 conditions évaluées dans `generate()` :**

| # | Clé | Condition True |
|---|-----|----------------|
| 1 | `false_breakout` | `analysis.status == PULLBACK_CONFIRMED` |
| 2 | `pullback_valid` | `analysis.pullback_level is not None` |
| 3 | `session_active` | `session in ("LONDON","NEW_YORK","OVERLAP")` |
| 4 | `setup_window` | `True` (délégué côté NinjaScript) |
| 5 | `news_gate` | `not has_news` |
| 6 | `volume_confirm` | `analysis.volume_ratio >= 0.8` |
| 7 | `intermarket_align` | `not (dxy_rising and "XAU" in symbol)` |

**Logique de décision :**
```
Circuit breaker actif                   → NO_TRADE
Toutes 7 conditions True + SL calculé  → TRADE_ALLOWED
false_breakout=T, session_active=F      → WAIT
news_gate=F                             → NO_TRADE
≥ 5/7 conditions + false_breakout=T    → REDUCE_RISK (50% taille)
< 5/7 conditions                        → NO_TRADE
```

**Calcul SL/TP :**
```
BULLISH :
  stop_loss   = pullback_level - (atr × 1.5)
  take_profit = pullback_level + (atr × 1.5 × 2.0)

BEARISH :
  stop_loss   = pullback_level + (atr × 1.5)
  take_profit = pullback_level - (atr × 1.5 × 2.0)
```

**Circuit breaker :**
```python
register_loss()   → _consecutive_losses += 1
                    si >= 3 → _circuit_breaker_until = now + 4h

register_win()    → _consecutive_losses = 0
```

**Dataclass retournée :**
```python
@dataclass
class SignalResult:
    status: SignalStatus
    direction: str
    symbol: str
    timeframe: str
    session: str
    timestamp: str
    entry_price: Optional[float]
    stop_loss: Optional[float]
    take_profit: Optional[float]
    risk_percent: float
    conditions: dict
    reason: str
    risk_reward: Optional[float]
```

---

### §3.3 — `indicators/mbk_indicators.py`

#### MBKZoneEngine

**Constante :** `MIN_IMPULSE_CANDLES = 3`

**Méthode `find_order_blocks(lookback=50)`** :
- Bullish OB : bougie bearish suivie de 3+ bougies haussières avec move > ATR × 1.5
- Bearish OB : bougie haussière suivie de 3+ bougies baissières avec move > ATR × 1.5
- Retourne liste de `Zone(zone_type, price_high, price_low, strength, touches)`

**Dataclass Zone :**
```python
ZoneType : BULLISH_OB | BEARISH_OB | EXHAUSTION_ZONE | IMPULSE_ZONE | NEUTRAL
strength : float 0.0–1.0  (move / atr / 5, plafonné à 1.0)
touches  : int   (nombre de bougies ayant touché la zone)
```

#### MBKImpulseDetector

**Constantes :**
```python
MIN_CANDLES    = 3
MIN_ATR_MULT   = 2.0   # < 2 ATR → WEAK
SPIKE_ATR_MULT = 5.0   # > 5 ATR → SPIKE
```

**Méthode `detect()`** :
- 3 bougies consécutives même sens + volume croissant = STRONG
- `magnitude_atr < 2.0` → WEAK
- `magnitude_atr > 5.0` → SPIKE
- Retourne `ImpulseResult(status, direction, magnitude_atr, candles_count, volume_increasing)`

#### MBKTimingFilter

**Sessions configurées :**
```python
LONDON   : start=(9,0), end=(12,0)   # GMT+1
NEW_YORK : start=(15,0), end=(18,0)  # GMT+1
```

**Méthode `get_status(dt)` → TimingStatus :**
```
minutes_in < 15    → SESSION_OPEN
30 ≤ min_in ≤ 90   → SETUP_WINDOW
min_to_close ≤ 90  → CLOSE_WINDOW
hors session       → OFF_SESSION
```

**Méthode `is_entry_allowed(dt)`** : retourne `True` uniquement si `SETUP_WINDOW`

---

### §3.4 — `indicators/news_gate.py`

**Source RSS :** `https://nfs.faireconomy.media/ff_calendar_thisweek.xml`
**Authentification requise :** aucune (gratuit)
**Format XML parsé :** `<event><title>`, `<impact>`, `<date>`, `<time>`
**Filtre :** `impact == "HIGH"` uniquement

**Keywords HIGH IMPACT surveillés (liste exacte du code) :**
```
NFP, Non-Farm, Fed, FOMC, CPI, PPI, GDP,
Unemployment, Interest Rate, Powell, Inflation,
ISM, Retail Sales, Durable Goods, Trade Balance
```

**Classe NewsGate (cache) :**
```python
CACHE_MINUTES = 15   # rafraîchissement RSS toutes les 15 min
NEWS_WINDOW   = 30   # fenêtre de blocage ±30 min
```

**Méthode `NewsGate.check()` → `(bool, Optional[str])` :**
- Retourne `(True, "Titre de la news")` si dans la fenêtre
- Retourne `(False, None)` sinon
- En cas d'échec réseau → retourne `(False, None)` + log warning

---

### §3.5 — `main.py` (Serveur FastAPI)

**Port :** 8000
**Host :** 0.0.0.0 (accessible sur réseau local si besoin)
**Commande de démarrage :** `uvicorn main:app --host 0.0.0.0 --port 8000`

**Endpoints REST :**

| Méthode | Route | Paramètres | Retour |
|---------|-------|------------|--------|
| GET | `/status` | — | `{status, engine, time, clients}` |
| GET | `/signals` | `limit=20` | Liste signaux depuis SQLite |
| GET | `/trades` | `symbol`, `limit=50` | Historique filtré |
| POST | `/backtest` | `{csv_path, symbol, timeframe}` | Rapport + chemin fichier |

**Endpoints WebSocket :**

| Route | Direction | Rôle |
|-------|-----------|------|
| `/ninjatrader` | NT8 → Python | Réception bougies OHLCV |
| `/stream` | Python → Electron | Diffusion signaux temps réel |

**Schéma SQLite (créé à l'init) :**
```sql
CREATE TABLE IF NOT EXISTS signals (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp   TEXT NOT NULL,
    symbol      TEXT NOT NULL,
    timeframe   TEXT,
    direction   TEXT,
    status      TEXT NOT NULL,
    entry_price REAL,
    stop_loss   REAL,
    take_profit REAL,
    risk_pct    REAL,
    session     TEXT,
    reason      TEXT
);

CREATE TABLE IF NOT EXISTS bars (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol    TEXT NOT NULL,
    timeframe TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    open      REAL, high REAL, low REAL, close REAL, volume REAL,
    session   TEXT,
    UNIQUE(symbol, timeframe, timestamp)
);
```

**Buffer en mémoire :**
```python
bar_buffers: dict[str, list]  # clé = "XAUUSD_M15", max 100 bougies
connected_clients: set[WebSocket]  # clients Electron connectés
```

**Traitement `process_bar()` :**
1. Stocker bougie en DB (`_store_bar`)
2. Ajouter au buffer mémoire (max 100)
3. Si buffer < 30 → retour sans analyse
4. Construire DataFrame pandas
5. Appeler `NewsGate.check()`
6. Appeler `FalseBreakoutDetector.full_analysis()`
7. Appeler `SignalGenerator.generate()`
8. Stocker signal en DB (`_store_signal`)
9. Diffuser aux clients Electron (`broadcast()`)

---

## §4. COMPOSANT 3 — BACKTEST ENGINE

### `backtest/backtest_engine.py`

**Classe :** `BacktestEngine`

**Format CSV attendu (export NinjaTrader 8) :**
```
Date, Time, Open, High, Low, Close, Volume
04/30/2026, 09:15:00, 2340.5, 2345.0, 2339.0, 2343.2, 1245
```

**Constantes de simulation :**
```python
WINDOW = 30  # fenêtre glissante d'analyse
```

**Métriques calculées et seuils :**

| Métrique | Calcul | Seuil minimum |
|----------|--------|---------------|
| Win Rate | `len(wins) / len(trades) × 100` | 45% |
| Profit Factor | `total_gains / total_losses` | 1.5 |
| Max Drawdown | `(peak - equity) / peak × 100` | < 15% |
| R:R moyen | `abs(pnl_win) / risk_pct` | 1.8 |
| Sharpe Ratio | `mean(returns) / std(returns) × √252` | 1.0 |
| Nb trades | `len(trades)` | 50 |

**Simulation trade (`_simulate_trade`) :**
- Test sur 5 bougies futures maximum
- BULLISH : `low ≤ stop_loss` → LOSS | `high ≥ take_profit` → WIN
- BEARISH : `high ≥ stop_loss` → LOSS | `low ≤ take_profit` → WIN
- PnL LOSS : `-risk_percent` | PnL WIN : `+risk_percent × 2.0`

**Verdicts :**
```
max_drawdown > 20%          → "DANGEROUS"
win_rate < 40 ou PF < 1.2  → "REJECTED"
seuils non atteints         → "WEAK"
tous seuils OK              → "VALIDATED"
```

**Sauvegarde rapport :**
- Format : JSON
- Chemin : `database/backtest_results/backtest_{symbol}_{tf}_{datetime}.json`

---

## §5. COMPOSANT 4 — DASHBOARD ELECTRON

### `electron-app/main.js`

**Configuration BrowserWindow :**
```javascript
width: 1280, height: 800, minWidth: 1024, minHeight: 600
contextIsolation: true   // OBLIGATOIRE
nodeIntegration: false   // OBLIGATOIRE
backgroundColor: '#0f172a'
```

**Environnements :**
- Dev : charge `http://localhost:5173` + DevTools ouvert
- Prod : charge `dist/index.html`

**Tray system :** icône tray Windows, double-clic = ouvrir fenêtre

### `electron-app/preload.js`

**APIs exposées via `contextBridge.exposeInMainWorld('electronAPI')` :**
```javascript
getVersion()           // version Electron
showNotification(title, body)  // notification Windows
playAlert(type)        // son : 'trade' | 'warn' | 'error'
openFile(filePath)     // ouvrir un fichier
minimizeToTray()       // minimiser dans la tray
```

### Pages React

**`pages/Login.tsx`**
- Google OAuth 2.0 via popup window
- URL construite : `https://accounts.google.com/o/oauth2/auth?...`
- `redirect_uri` : `http://localhost:3000/callback`
- Scope : `openid email profile`
- Token récupéré depuis `popup.location.href` (fragment `#access_token=...`)
- Userinfo : `https://www.googleapis.com/oauth2/v3/userinfo`
- Stockage session : `localStorage('mbk_user')`
- Variable requise : `VITE_GOOGLE_CLIENT_ID` (fichier `.env`)

**`pages/Dashboard.tsx`**
- Polling statut serveur : toutes les 10 secondes via `GET /status`
- WebSocket : `ws://localhost:8000/stream`
- Reconnexion automatique : `setTimeout(connect, 3000)` sur close
- À la connexion : reçoit les 10 derniers signaux via `{type:"HISTORY"}`
- Badge status :

| Status | Couleur Tailwind | Label affiché |
|--------|-----------------|---------------|
| TRADE_ALLOWED | `bg-emerald-500` | 🟢 TRADE ALLOWED |
| WAIT | `bg-amber-400` | 🟡 WAIT |
| REDUCE_RISK | `bg-orange-500` | 🟠 REDUCE RISK |
| NO_TRADE | `bg-red-500` | 🔴 NO TRADE |

**`pages/History.tsx`**
- Source : `GET http://localhost:8000/trades?limit=100`
- Filtre par symbol (input texte, forcé uppercase)
- Rafraîchissement : à chaque changement du filtre symbol

**`pages/Backtest.tsx`**
- Appel : `POST http://localhost:8000/backtest`
- Body : `{csv_path, symbol, timeframe}`
- Affiche : total_trades, win_rate, profit_factor, max_drawdown, avg_risk_reward, sharpe_ratio
- Avertissement obligatoire : "Les résultats passés ne garantissent pas..."

---

## §6. DÉPENDANCES EXACTES

### Python (`requirements.txt`)
```
fastapi==0.110.0
uvicorn[standard]==0.29.0
websockets==12.0
pandas==2.2.2
numpy==1.26.4
pandas-ta==0.3.14b
scikit-learn==1.4.2
pydantic==2.7.0
python-dotenv==1.0.1
loguru==0.7.2
pytest==8.2.0
httpx==0.27.0
```

### Node.js (`package.json` — electron-app)
```json
dependencies:
  react: ^18.3.1
  react-dom: ^18.3.1
  recharts: ^2.12.7
  lucide-react: ^0.383.0

devDependencies:
  electron: ^30.0.0
  electron-builder: ^24.13.3
  vite: ^5.2.11
  @vitejs/plugin-react: ^4.3.1
  tailwindcss: ^3.4.3
  typescript: ^5.4.5
  concurrently: ^8.2.2
  wait-on: ^7.2.0
```

### NinjaTrader 8 (C# NinjaScript)
```
System.Net.WebSockets
System.Threading
NinjaTrader.Cbi
NinjaTrader.NinjaScript.Indicators
System.Windows.Media  (MBK_SessionFilter)
```

---

## §7. VARIABLES D'ENVIRONNEMENT

### Fichier `electron-app/.env` (à créer depuis `.env.example`)
```env
VITE_GOOGLE_CLIENT_ID=ton_client_id_google_ici
```

**Source :** Google Cloud Console → APIs & Services → Credentials → OAuth 2.0 Client ID

**Type de client :** Web application
**Redirect URI autorisée :** `http://localhost:3000/callback`

### Variables Python (aucune requise en v1.0)
Tout fonctionne sans variable d'environnement Python en v1.0.
Le fichier `.env` Python est prévu pour les versions futures (clés API externes).

---

## §8. TESTS UNITAIRES

### `tests/test_false_breakout.py` — 5 tests (pytest)

| Test | Fonction | Résultat attendu |
|------|----------|------------------|
| test_detector_initialization | `FalseBreakoutDetector(df)` | colonnes atr + volume_avg présentes |
| test_zone_identification | `identify_zone()` | zone_high > zone_low |
| test_insufficient_data | `FalseBreakoutDetector(df_10_rows)` | `ValueError` levée |
| test_rejection_candle_detection | `_detect_rejection_candle("BEARISH")` | `True` sur Pin Bar artificielle |
| test_full_analysis_returns_status | `full_analysis()` | statut dans BreakoutStatus valides |

**Commande :** `pytest tests/test_false_breakout.py -v`
**Résultat attendu :** `5 passed`

---

## §9. STRUCTURE FICHIERS COMPLÈTE

```
mbk-trader/
├── .gitignore
├── ninja-addon/
│   ├── MBK_DataBridge.cs          # Add-on NT8 — pont données
│   └── MBK_SessionFilter.cs       # Add-on NT8 — filtre sessions
├── python-engine/
│   ├── main.py                    # Serveur FastAPI principal
│   ├── requirements.txt
│   ├── detector/
│   │   ├── __init__.py
│   │   ├── false_breakout.py      # Moteur détection 4 étapes
│   │   └── signal_generator.py   # Validation 7 conditions + signaux
│   ├── indicators/
│   │   ├── __init__.py
│   │   ├── mbk_indicators.py     # ZoneEngine + Impulse + Timing
│   │   └── news_gate.py          # ForexFactory RSS gate
│   ├── backtest/
│   │   ├── __init__.py
│   │   └── backtest_engine.py    # Backtest CSV + rapport JSON
│   └── tests/
│       ├── __init__.py
│       └── test_false_breakout.py # 5 tests unitaires
├── electron-app/
│   ├── main.js                   # Electron main process
│   ├── preload.js                # contextBridge IPC
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── package.json
│   ├── .env.example              # Template variables
│   └── src/
│       ├── main.tsx
│       ├── index.css
│       ├── App.tsx               # Root + Navigation + Auth
│       └── pages/
│           ├── Login.tsx         # Google OAuth 2.0
│           ├── Dashboard.tsx     # Signaux temps réel
│           ├── History.tsx       # Historique SQLite
│           └── Backtest.tsx      # Interface backtest
├── database/
│   └── historical/               # CSVs NinjaTrader 8 (non versionné)
└── docs/
    ├── INSTALLATION.md
    ├── CDC_MBK_TRADER_VISION_v1.0.md
    └── CDC_MBK_TRADER_TECHNIQUE_v1.0.md
```

---

## §10. ROADMAP V1 — PHASES D'INSTALLATION

| Phase | Durée | Actions | Validation |
|-------|-------|---------|------------|
| P0 — Environnement | 30 min | Copier ZIP, installer Python/Node | `python --version && node --version` |
| P1 — Python Engine | 15 min | `pip install -r requirements.txt` + démarrer uvicorn | `GET /status` → `{"status":"running"}` |
| P2 — NinjaTrader Addon | 20 min | Coller C# dans NT8, compiler, charger sur chart | NT8 Output Window : "WebSocket connecté" |
| P3 — Google OAuth | 10 min | Créer Client ID Google Cloud, remplir `.env` | Page login s'affiche dans Electron |
| P4 — Electron App | 10 min | `npm install && npm run dev` | Fenêtre desktop ouverte |
| P5 — Tests unitaires | 5 min | `pytest tests/ -v` | 5/5 passed |
| P6 — Backtest | 20 min | Exporter CSV NT8, lancer backtest | Rapport JSON généré avec verdict |

---

## §11. GARDE-FOUS TRADING — LISTE EXHAUSTIVE

Tous implémentés dans `signal_generator.py` :

| Garde-fou | Implémentation | Valeur |
|-----------|---------------|--------|
| Stop-Loss obligatoire | Aucun `TRADE_ALLOWED` sans `stop_loss` calculé | 1.5 × ATR |
| Risk per trade | `risk_percent` plafonné | 1.0% du capital |
| Circuit breaker | `_consecutive_losses >= 3` → pause | 4 heures |
| News gate | `NewsGate.check()` avant tout signal | ±30 min HIGH IMPACT |
| Filtrage session | `session in (LONDON, NEW_YORK, OVERLAP)` | Sinon WAIT |
| Corrélation DXY | `not (dxy_rising and "XAU" in symbol)` | Sinon condition échouée |
| Volume confirmation | `volume_ratio >= 0.8` | Sinon condition échouée |

---

## §12. AVERTISSEMENT LÉGAL (reproduit tel quel du code)

> Ce logiciel est un outil d'aide à la décision à usage **strictement personnel**.
> Il ne constitue pas un conseil en investissement.
> Les performances passées ne garantissent pas les performances futures.
> Vérifier les obligations réglementaires locales (Maroc : AMMC) avant toute
> utilisation professionnelle ou commerciale.

---

## §13. CE QUI N'EST PAS IMPLÉMENTÉ EN V1

| Fonctionnalité | Statut | Note |
|----------------|--------|------|
| Exécution automatique d'ordres | Hors scope définitif | SaaS = assistance uniquement |
| Corrélation DXY temps réel | `dxy_rising=False` hardcodé | À connecter en V2 |
| Reconnexion automatique NT8 | Manuelle (rechargement indicateur) | À implémenter en V2 |
| Mobile | Non prévu | V2 optionnel |
| Cloud backup | Non prévu | Stockage local uniquement |
| Multi-timeframe simultané | Un seul chart à la fois | V2 |
| Intermarket Silver/Oil analysis | Déclaré dans code, non connecté | V2 |

---

*CDC_MBK_TRADER_TECHNIQUE_v1.0.md — Extraction stricte du code source mbk-trader-v1.0.zip*
*Généré le 30/04/2026 — Zéro hallucination — Zéro invention*
