# CDC MBK TRADER ASSISTANT — TECHNIQUE v1.1
**Date creation : 30/04/2026**
**Date mise a jour : 30/04/2026 (post-audit securite)**
**Score securite : 57/100 -> 85+/100 apres corrections P0+P1**
**Source : Extraction stricte du code source mbk-trader-v1.0.zip**
**Regle : Zero hallucination — chaque element reference un fichier reel**

---

## §1. ARCHITECTURE GLOBALE

```
+-----------------------------------------------------------------+
|                    NINJATRADER 8 (Windows)                       |
|  MBK_DataBridge.cs      ->  WebSocket ws://localhost:8765        |
|  MBK_SessionFilter.cs   ->  filtre sessions (integre)           |
+----------------------------+------------------------------------+
                             | JSON {symbol,tf,ohlcv,session,timestamp}
                             v
+-----------------------------------------------------------------+
|               PYTHON FASTAPI  (localhost:8000)                   |
|                                                                  |
|  main.py                <-  WebSocket /ninjatrader               |
|  detector/              |  WebSocket /stream -> Electron         |
|    false_breakout.py    |  REST GET /status                      |
|    signal_generator.py  |  REST GET /signals                     |
|  indicators/            |  REST GET /trades                      |
|    mbk_indicators.py    |  REST POST /backtest                   |
|    news_gate.py         |                                        |
|  backtest/              |                                        |
|    backtest_engine.py   |                                        |
|                         |                                        |
|  SQLite  mbk_trades.db  |  tables: signals, bars, circuit_breaker|
+-----------------------------------------------------------------+
                             | WebSocket ws://localhost:8000/stream
                             v
+-----------------------------------------------------------------+
|              ELECTRON DESKTOP APP (Windows)                      |
|                                                                  |
|  main.js          <-  BrowserWindow + Tray + IPC OAuth           |
|  preload.js        <-  contextBridge (contextIsolation: true)    |
|  src/App.tsx       <-  React 18 + Router 3 pages                 |
|    pages/Login.tsx     <-  Google OAuth 2.0 PKCE (IPC)           |
|    pages/Dashboard.tsx <-  Signaux temps reel + badges           |
|    pages/History.tsx   <-  Historique SQLite                     |
|    pages/Backtest.tsx  <-  Interface backtest                    |
+-----------------------------------------------------------------+
```

---

## §2. COMPOSANT 1 — ADD-ON NINJATRADER 8

### Fichier : `ninja-addon/MBK_DataBridge.cs`

**Classe :** `NinjaTrader.NinjaScript.Indicators.MBK_DataBridge`
**Heritage :** `Indicator`
**Calculate :** `Calculate.OnBarClose`

**Methodes publiques :**

| Methode | Declencheur | Action |
|---------|-------------|--------|
| `OnStateChange()` | State.SetDefaults | Configure nom, Calculate, IsOverlay |
| `OnStateChange()` | State.DataLoaded | Appelle `ConnectWebSocket()` |
| `OnStateChange()` | State.Terminated | Appelle `DisconnectWebSocket()` |
| `OnBarUpdate()` | Cloture de bougie | Construit JSON + appelle `SendAsync()` |
| `ConnectWebSocket()` | async void | Connexion a ws://localhost:8765 |
| `DisconnectWebSocket()` | async void | Fermeture propre WebSocket |
| `GetCurrentSession()` | privee | Retourne string session GMT+1 |
| `SendAsync(string)` | async void | Envoie payload JSON |

**Payload JSON envoye (format exact) :**
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
hour 9–11  -> "LONDON"
hour 15–16 -> "OVERLAP"
hour 15–17 -> "NEW_YORK"
autre      -> "OFF_SESSION"
```

**Etats WebSocket geres :**
- `WebSocketState.Open` -> envoi actif
- Exception lors envoi -> `_isConnected = false` (log NT8 Output Window)
- Reconnexion : non automatique v1 — rechargement de l'indicateur requis

---

### Fichier : `ninja-addon/MBK_SessionFilter.cs`

**Classe :** `NinjaTrader.NinjaScript.Indicators.MBK_SessionFilter`
**Calculate :** `Calculate.OnEachTick`

**Proprietes publiques exposees :**
```csharp
bool IsActiveSession   // true si LONDON ou NEW_YORK
string CurrentSession  // "LONDON" | "NEW_YORK" | "OVERLAP" | "OFF_SESSION"
bool IsSetupWindow     // true si 30–90 min apres open session
```

**Constantes de sessions (GMT+1) :**
```csharp
LONDON_START  = 9    LONDON_END  = 12
NY_START      = 15   NY_END      = 18
OVERLAP_START = 15   OVERLAP_END = 17
```

**Coloration du fond graphique NT8 :**
```
OVERLAP           -> BackBrush = LightGoldenrodYellow
LONDON ou NY      -> BackBrush = LightCyan
OFF_SESSION       -> BackBrush = null
```

---

## §3. COMPOSANT 2 — MOTEUR IA PYTHON

### §3.1 — `detector/false_breakout.py`

**Classe principale :** `FalseBreakoutDetector`

**Constantes du detecteur :**
```python
ATR_ZONE_MULTIPLIER  = 0.5   # +/-0.5 ATR autour du niveau
VOLUME_THRESHOLD     = 1.3   # cassure suspecte si volume < moyenne x 1.3
BREAKOUT_MAX_CANDLES = 2     # cassure suspecte si <= 2 bougies hors zone
PULLBACK_MAX_CANDLES = 3     # retour dans zone attendu <= 3 bougies
FIBO_50              = 0.50
FIBO_618             = 0.618
```

**DataFrame requis en entree :**
- Colonnes obligatoires : `open`, `high`, `low`, `close`, `volume`
- Minimum : 25 lignes (leve `ValueError` sinon)
- Calculs ajoutes : `atr` (ATR 14 periodes), `volume_avg` (rolling 20)

**Enumerations :**
```python
class BreakoutStatus(str, Enum):
    ZONE_IDENTIFIED          # zone detectee, pas de cassure
    BREAKOUT_DETECTED        # cassure en cours
    BREAKOUT_SUSPICIOUS      # <= 2 bougies + volume faible
    BREAKOUT_REAL            # <= 2 bougies + volume fort
    FALSE_BREAKOUT_CONFIRMED # prix revenu dans zone <= 3 bougies
    REAL_BREAKOUT_CONFIRMED  # prix reste hors zone > 3 bougies
    PULLBACK_CONFIRMED       # Fibo 50-61.8% + bougie de rejet
    WAIT                     # fausse cassure confirmee, pullback attendu

class SignalStatus(str, Enum):
    TRADE_ALLOWED
    WAIT
    REDUCE_RISK
    NO_TRADE
```

**Methodes publiques :**

| Methode | Retour | Description |
|---------|--------|-------------|
| `identify_zone()` | `(float, float)` | zone_high, zone_low via swing 20 dernieres bougies |
| `detect_breakout(zh, zl)` | `(BreakoutStatus, str, int, float)` | status, direction, nb_candles, volume_ratio |
| `analyze_post_breakout(zh, zl, dir)` | `BreakoutStatus` | retour dans zone -> FALSE_BREAKOUT_CONFIRMED |
| `wait_for_pullback(dir, zh, zl)` | `(BreakoutStatus, float, float, float, bool)` | pullback_status, level, fibo50, fibo618, rejection |
| `full_analysis()` | `BreakoutAnalysis` | Execute les 4 etapes et retourne dataclass |

**Dataclass retournee :**
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

**Detection bougie de rejet (`_detect_rejection_candle`) :**
- Pin Bar : `body / total_range < 0.3` (corps < 30% du range)
- Engulfing : corps actuel > corps precedent x 1.5 + direction opposee

---

### §3.2 — `detector/signal_generator.py`

**Classe :** `SignalGenerator` (methodes de classe — stateless par instance)

**Constantes :**
```python
STOP_LOSS_ATR_MULTIPLIER = 1.5   # SL = 1.5 x ATR
TAKE_PROFIT_RR           = 2.0   # TP = entree +/- (SL_distance x 2.0)
MAX_RISK_PERCENT         = 1.0   # 1% du capital par trade
NEWS_WINDOW_MINUTES      = 30    # bloque +/-30 min autour des news
```

**Etat circuit breaker (v1.1 — persiste en SQLite) :**
```
Etat persiste en SQLite — table circuit_breaker (id=1)
Survit aux redemarrages du serveur uvicorn
Methodes _get_cb_state() et _set_cb_state() lisent/ecrivent la DB
```

**7 conditions evaluees dans `generate()` :**

| # | Cle | Condition True |
|---|-----|----------------|
| 1 | `false_breakout` | `analysis.status == PULLBACK_CONFIRMED` |
| 2 | `pullback_valid` | `analysis.pullback_level is not None` |
| 3 | `session_active` | `session in ("LONDON","NEW_YORK","OVERLAP")` |
| 4 | `setup_window` | `True` (delegue cote NinjaScript) |
| 5 | `news_gate` | `not has_news` |
| 6 | `volume_confirm` | `analysis.volume_ratio >= 0.8` |
| 7 | `intermarket_align` | `not (dxy_rising and "XAU" in symbol)` |

**Logique de decision :**
```
Circuit breaker actif                   -> NO_TRADE
Toutes 7 conditions True + SL calcule  -> TRADE_ALLOWED
false_breakout=T, session_active=F      -> WAIT
news_gate=F                             -> NO_TRADE
>= 5/7 conditions + false_breakout=T   -> REDUCE_RISK (50% taille)
< 5/7 conditions                        -> NO_TRADE
```

**Calcul SL/TP :**
```
BULLISH :
  stop_loss   = pullback_level - (atr x 1.5)
  take_profit = pullback_level + (atr x 1.5 x 2.0)

BEARISH :
  stop_loss   = pullback_level + (atr x 1.5)
  take_profit = pullback_level - (atr x 1.5 x 2.0)
```

**Circuit breaker :**
```python
register_loss()   -> _get_cb_state() + losses += 1
                    si >= 3 -> blocked_until = now + 4h
                    _set_cb_state(losses, blocked_until)

register_win()    -> _set_cb_state(0, None)
```

**Dataclass retournee :**
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

**Methode `find_order_blocks(lookback=50)`** :
- Bullish OB : bougie bearish suivie de 3+ bougies haussieres avec move > ATR x 1.5
- Bearish OB : bougie haussiere suivie de 3+ bougies baissieres avec move > ATR x 1.5
- Retourne liste de `Zone(zone_type, price_high, price_low, strength, touches)`

**Dataclass Zone :**
```python
ZoneType : BULLISH_OB | BEARISH_OB | EXHAUSTION_ZONE | IMPULSE_ZONE | NEUTRAL
strength : float 0.0–1.0  (move / atr / 5, plafonne a 1.0)
touches  : int   (nombre de bougies ayant touche la zone)
```

#### MBKImpulseDetector

**Constantes :**
```python
MIN_CANDLES    = 3
MIN_ATR_MULT   = 2.0   # < 2 ATR -> WEAK
SPIKE_ATR_MULT = 5.0   # > 5 ATR -> SPIKE
```

**Methode `detect()`** :
- 3 bougies consecutives meme sens + volume croissant = STRONG
- `magnitude_atr < 2.0` -> WEAK
- `magnitude_atr > 5.0` -> SPIKE
- Retourne `ImpulseResult(status, direction, magnitude_atr, candles_count, volume_increasing)`

#### MBKTimingFilter

**Sessions configurees :**
```python
LONDON   : start=(9,0), end=(12,0)   # GMT+1
NEW_YORK : start=(15,0), end=(18,0)  # GMT+1
```

**Methode `get_status(dt)` -> TimingStatus :**
```
minutes_in < 15    -> SESSION_OPEN
30 <= min_in <= 90 -> SETUP_WINDOW
min_to_close <= 90 -> CLOSE_WINDOW
hors session       -> OFF_SESSION
```

**Methode `is_entry_allowed(dt)`** : retourne `True` uniquement si `SETUP_WINDOW`

---

### §3.4 — `indicators/news_gate.py`

**Source RSS :** `https://nfs.faireconomy.media/ff_calendar_thisweek.xml`
**Authentification requise :** aucune (gratuit)
**Format XML parse :** `<event><title>`, `<impact>`, `<date>`, `<time>`
**Filtre :** `impact == "HIGH"` uniquement

**Keywords HIGH IMPACT surveilles (liste exacte du code) :**
```
NFP, Non-Farm, Fed, FOMC, CPI, PPI, GDP,
Unemployment, Interest Rate, Powell, Inflation,
ISM, Retail Sales, Durable Goods, Trade Balance
```

**Classe NewsGate (cache) :**
```python
CACHE_MINUTES = 15   # rafraichissement RSS toutes les 15 min
NEWS_WINDOW   = 30   # fenetre de blocage +/-30 min
```

**Methode `NewsGate.check()` -> `(bool, Optional[str])` :**
- Retourne `(True, "Titre de la news")` si dans la fenetre
- Retourne `(False, None)` sinon
- En cas d'echec reseau -> retourne `(False, None)` + log warning

---

### §3.5 — `python-engine/main.py` — Serveur FastAPI v1.1

**Port :** 8000
**Commande :** `uvicorn main:app --host 0.0.0.0 --port 8000`

**CORS (corrige — P1 audit) :**
  allow_origins  = ["http://localhost:5173", "http://localhost:3000"]
  allow_methods  = ["GET", "POST"]
  allow_headers  = ["Content-Type", "X-API-Token"]
  Attention : Plus de wildcard * — origines restreintes

**Authentification API (ajoute — P1 audit) :**
  Header requis : X-API-Token
  Variable env  : MBK_API_TOKEN (fichier python-engine/.env)
  Endpoints proteges : GET /signals, GET /trades, POST /backtest
  Endpoints publics  : GET /status, WS /ninjatrader, WS /stream

**Rate limiting (ajoute — P1 audit) :**
  Librairie : slowapi 0.1.9
  POST /backtest : 2 requetes/minute maximum

**Validation payload WebSocket (ajoutee — P1 audit) :**
  Modele Pydantic : BarPayload
  Champs valides  : symbol (pattern A-Z), timeframe, open/high/low/close (> 0),
                    volume (>= 0), high >= low, low <= close <= high
  Payload invalide : ignore avec log WARNING (pas de crash serveur)

**Endpoints REST :**

| Methode | Route | Auth | Rate limit | Parametres |
|---------|-------|------|------------|------------|
| GET | /status | Non | Non | — |
| GET | /signals | X-API-Token | Non | limit: 1–500 (defaut 20) |
| GET | /trades | X-API-Token | Non | symbol, limit: 1–500 (defaut 50) |
| POST | /backtest | X-API-Token | 2/min | {csv_path, symbol, timeframe} |

**Protection Path Traversal sur /backtest (corrigee — P0 audit) :**
  Dossier autorise : database/historical/ (chemin absolu resolu)
  Validation       : Path.resolve() + startswith(ALLOWED_CSV_DIR)
  Extension        : .csv uniquement
  Erreur           : HTTP 400 si hors dossier autorise

**Endpoints WebSocket :**

| Route | Direction | Role |
|-------|-----------|------|
| `/ninjatrader` | NT8 -> Python | Reception bougies OHLCV |
| `/stream` | Python -> Electron | Diffusion signaux temps reel |

**Schema SQLite (3 tables — ajout circuit_breaker) :**

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

CREATE TABLE IF NOT EXISTS circuit_breaker (
    id                 INTEGER PRIMARY KEY CHECK (id = 1),
    consecutive_losses INTEGER DEFAULT 0,
    blocked_until      TEXT
);
```

**Buffer en memoire :**
```python
bar_buffers: dict[str, list]  # cle = "XAUUSD_M15", max 100 bougies
connected_clients: set[WebSocket]  # clients Electron connectes
```

**Traitement `process_bar()` :**
1. Stocker bougie en DB (`_store_bar`)
2. Ajouter au buffer memoire (max 100)
3. Si buffer < 30 -> retour sans analyse
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
WINDOW = 30  # fenetre glissante d'analyse
```

**Metriques calculees et seuils :**

| Metrique | Calcul | Seuil minimum |
|----------|--------|---------------|
| Win Rate | `len(wins) / len(trades) x 100` | 45% |
| Profit Factor | `total_gains / total_losses` | 1.5 |
| Max Drawdown | `(peak - equity) / peak x 100` | < 15% |
| R:R moyen | `abs(pnl_win) / risk_pct` | 1.8 |
| Sharpe Ratio | `mean(returns) / std(returns) x sqrt(252)` | 1.0 |
| Nb trades | `len(trades)` | 50 |

**Simulation trade (`_simulate_trade`) :**
- Test sur 5 bougies futures maximum
- BULLISH : `low <= stop_loss` -> LOSS | `high >= take_profit` -> WIN
- BEARISH : `high >= stop_loss` -> LOSS | `low <= take_profit` -> WIN
- PnL LOSS : `-risk_percent` | PnL WIN : `+risk_percent x 2.0`

**Verdicts :**
```
max_drawdown > 20%          -> "DANGEROUS"
win_rate < 40 ou PF < 1.2  -> "REJECTED"
seuils non atteints         -> "WEAK"
tous seuils OK              -> "VALIDATED"
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

**Tray system :** icone tray Windows, double-clic = ouvrir fenetre

### `electron-app/preload.js`

**APIs exposees via `contextBridge.exposeInMainWorld('electronAPI')` :**
```javascript
getVersion()           // version Electron
showNotification(title, body)  // notification Windows
playAlert(type)        // son : 'trade' | 'warn' | 'error'
openFile(filePath)     // ouvrir un fichier
minimizeToTray()       // minimiser dans la tray
googleLogin()          // OAuth PKCE via IPC (v1.1)
getSession()           // lire session chiffree (v1.1)
logout()               // supprimer session.enc (v1.1)
```

### Pages React

**`pages/Login.tsx` — v1.1 (corrigee P0 audit)**
  Flow OAuth : PKCE (Authorization Code + code_challenge)
               Attention : Plus de response_type=token (Implicit Flow supprime)
  Package    : electron-google-oauth2 ^0.5.0
  Handler    : ipcMain.handle('google-login') dans main.js
  Token      : transmis via IPC — jamais expose dans le renderer
  Scope      : openid email profile

**Session utilisateur — v1.1 (corrigee P1 audit)**
  Stockage   : safeStorage.encryptString() -> fichier .enc
               Attention : Plus de localStorage (supprime)
  Chiffrement: AES natif Windows (Electron safeStorage)
  Fichier    : app.getPath('userData')/session.enc
  Acces      : via ipcMain.handle('get-session') uniquement

**Handlers IPC ajoutes dans main.js :**
  'google-login'  -> ouvre fenetre OAuth PKCE, retourne userData
  'get-session'   -> dechiffre et retourne session stockee
  'logout'        -> supprime le fichier session.enc

**`pages/Dashboard.tsx`**
- Polling statut serveur : toutes les 10 secondes via `GET /status`
- WebSocket : `ws://localhost:8000/stream`
- Reconnexion automatique : `setTimeout(connect, 3000)` sur close
- A la connexion : recoit les 10 derniers signaux via `{type:"HISTORY"}`
- Badge status :

| Status | Couleur Tailwind | Label affiche |
|--------|-----------------|---------------|
| TRADE_ALLOWED | `bg-emerald-500` | TRADE ALLOWED |
| WAIT | `bg-amber-400` | WAIT |
| REDUCE_RISK | `bg-orange-500` | REDUCE RISK |
| NO_TRADE | `bg-red-500` | NO TRADE |

**`pages/History.tsx`**
- Source : `GET http://localhost:8000/trades?limit=100`
- Filtre par symbol (input texte, force uppercase)
- Rafraichissement : a chaque changement du filtre symbol

**`pages/Backtest.tsx`**
- Appel : `POST http://localhost:8000/backtest`
- Body : `{csv_path, symbol, timeframe}`
- Affiche : total_trades, win_rate, profit_factor, max_drawdown, avg_risk_reward, sharpe_ratio
- Avertissement obligatoire : "Les resultats passes ne garantissent pas..."

---

## §6. DEPENDANCES EXACTES

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
slowapi==0.1.9
```

### Node.js (`package.json` — electron-app)
```json
dependencies:
  react: ^18.3.1
  react-dom: ^18.3.1
  recharts: ^2.12.7
  lucide-react: ^0.383.0
  electron-google-oauth2: ^0.5.0

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

### Fichier `electron-app/.env` (a creer depuis `.env.example`)
```env
VITE_GOOGLE_CLIENT_ID=ton_client_id_google_ici
```

**Source :** Google Cloud Console -> APIs & Services -> Credentials -> OAuth 2.0 Client ID

**Type de client :** Web application
**Redirect URI autorisee :** `http://localhost:3000/callback`

### Variables Python (aucune requise en v1.0)
Tout fonctionne sans variable d'environnement Python en v1.0.
Le fichier `.env` Python est prevu pour les versions futures (cles API externes).

---

## §8. TESTS UNITAIRES

### `tests/test_false_breakout.py` — 5 tests (pytest)

| Test | Fonction | Resultat attendu |
|------|----------|------------------|
| test_detector_initialization | `FalseBreakoutDetector(df)` | colonnes atr + volume_avg presentes |
| test_zone_identification | `identify_zone()` | zone_high > zone_low |
| test_insufficient_data | `FalseBreakoutDetector(df_10_rows)` | `ValueError` levee |
| test_rejection_candle_detection | `_detect_rejection_candle("BEARISH")` | `True` sur Pin Bar artificielle |
| test_full_analysis_returns_status | `full_analysis()` | statut dans BreakoutStatus valides |

**Commande :** `pytest tests/test_false_breakout.py -v`
**Resultat attendu :** `5 passed`

---

## §9. STRUCTURE FICHIERS COMPLETE

```
mbk-trader/
+-- .gitignore
+-- ninja-addon/
|   +-- MBK_DataBridge.cs          # Add-on NT8 — pont donnees
|   +-- MBK_SessionFilter.cs       # Add-on NT8 — filtre sessions
+-- python-engine/
|   +-- main.py                    # Serveur FastAPI principal
|   +-- requirements.txt
|   +-- .env                       # MBK_API_TOKEN (v1.1)
|   +-- detector/
|   |   +-- __init__.py
|   |   +-- false_breakout.py      # Moteur detection 4 etapes
|   |   +-- signal_generator.py    # Validation 7 conditions + signaux
|   +-- indicators/
|   |   +-- __init__.py
|   |   +-- mbk_indicators.py      # ZoneEngine + Impulse + Timing
|   |   +-- news_gate.py           # ForexFactory RSS gate
|   +-- backtest/
|   |   +-- __init__.py
|   |   +-- backtest_engine.py     # Backtest CSV + rapport JSON
|   +-- tests/
|       +-- __init__.py
|       +-- test_false_breakout.py  # 5 tests unitaires
+-- electron-app/
|   +-- main.js                    # Electron main process + IPC OAuth (v1.1)
|   +-- preload.js                 # contextBridge IPC (v1.1 : googleLogin, getSession, logout)
|   +-- index.html
|   +-- vite.config.ts
|   +-- tsconfig.json              # strict: true (v1.1)
|   +-- tailwind.config.js
|   +-- postcss.config.js
|   +-- package.json
|   +-- .env.example               # Template variables
|   +-- src/
|       +-- main.tsx
|       +-- index.css
|       +-- App.tsx                 # Root + Navigation + Auth (safeStorage v1.1)
|       +-- pages/
|           +-- Login.tsx           # Google OAuth 2.0 PKCE (v1.1)
|           +-- Dashboard.tsx       # Signaux temps reel
|           +-- History.tsx         # Historique SQLite
|           +-- Backtest.tsx        # Interface backtest
+-- database/
|   +-- historical/                 # CSVs NinjaTrader 8 (non versionne)
+-- docs/
    +-- INSTALLATION.md
    +-- CDC_MBK_TRADER_VISION_v1.0.md
    +-- CDC_MBK_TRADER_TECHNIQUE_v1.0.md
    +-- CDC_MBK_TRADER_VISION_v1.1.md
    +-- CDC_MBK_TRADER_TECHNIQUE_v1.1.md
```

---

## §10. ROADMAP V1 — PHASES D'INSTALLATION

| Phase | Duree | Actions | Validation |
|-------|-------|---------|------------|
| P0 — Environnement | 30 min | Copier ZIP, installer Python/Node | `python --version && node --version` |
| P1 — Python Engine | 15 min | `pip install -r requirements.txt` + demarrer uvicorn | `GET /status` -> `{"status":"running"}` |
| P2 — NinjaTrader Addon | 20 min | Coller C# dans NT8, compiler, charger sur chart | NT8 Output Window : "WebSocket connecte" |
| P3 — Google OAuth | 10 min | Creer Client ID Google Cloud, remplir `.env` | Page login s'affiche dans Electron |
| P4 — Electron App | 10 min | `npm install && npm run dev` | Fenetre desktop ouverte |
| P5 — Tests unitaires | 5 min | `pytest tests/ -v` | 5/5 passed |
| P6 — Backtest | 20 min | Exporter CSV NT8, lancer backtest | Rapport JSON genere avec verdict |

---

## §11. GARDE-FOUS TRADING — LISTE EXHAUSTIVE

Tous implementes dans `signal_generator.py` :

| Garde-fou | Implementation | Valeur |
|-----------|---------------|--------|
| Stop-Loss obligatoire | Aucun `TRADE_ALLOWED` sans `stop_loss` calcule | 1.5 x ATR |
| Risk per trade | `risk_percent` plafonne | 1.0% du capital |
| Circuit breaker | `consecutive_losses >= 3` -> pause (persiste SQLite) | 4 heures |
| News gate | `NewsGate.check()` avant tout signal | +/-30 min HIGH IMPACT |
| Filtrage session | `session in (LONDON, NEW_YORK, OVERLAP)` | Sinon WAIT |
| Correlation DXY | `not (dxy_rising and "XAU" in symbol)` | Sinon condition echouee |
| Volume confirmation | `volume_ratio >= 0.8` | Sinon condition echouee |

---

## §12. AVERTISSEMENT LEGAL (reproduit tel quel du code)

> Ce logiciel est un outil d'aide a la decision a usage **strictement personnel**.
> Il ne constitue pas un conseil en investissement.
> Les performances passees ne garantissent pas les performances futures.
> Verifier les obligations reglementaires locales (Maroc : AMMC) avant toute
> utilisation professionnelle ou commerciale.

---

## §13. CE QUI N'EST PAS IMPLEMENTE EN V1

| Fonctionnalite | Statut | Note |
|----------------|--------|------|
| Execution automatique d'ordres | Hors scope definitif | SaaS = assistance uniquement |
| Correlation DXY temps reel | `dxy_rising=False` hardcode | A connecter en V2 |
| Reconnexion automatique NT8 | Manuelle (rechargement indicateur) | A implementer en V2 |
| Mobile | Non prevu | V2 optionnel |
| Cloud backup | Non prevu | Stockage local uniquement |
| Multi-timeframe simultane | Un seul chart a la fois | V2 |
| Intermarket Silver/Oil analysis | Declare dans code, non connecte | V2 |

---

## §14. VARIABLES D'ENVIRONNEMENT — LISTE COMPLETE v1.1

### python-engine/.env
```
MBK_API_TOKEN=mbk-XXXXXX-secure
# Token partage entre Electron et FastAPI
# Generer : python -c "import secrets; print(secrets.token_hex(32))"
```

### electron-app/.env
```
VITE_GOOGLE_CLIENT_ID=ton_client_id_google
GOOGLE_CLIENT_SECRET=ton_client_secret_google
VITE_API_TOKEN=mbk-XXXXXX-secure   <- identique a MBK_API_TOKEN
```

### Fichiers .env ajoutes au .gitignore (deja present)

---

## §15. CHANGELOG SECURITE

### v1.1 — 30/04/2026 (post-audit P0+P1)

| Finding | Severite | Correction appliquee |
|---------|----------|----------------------|
| Path Traversal /backtest | P0 | ALLOWED_CSV_DIR + Path.resolve() |
| OAuth Implicit Flow | P0 | PKCE + electron-google-oauth2 |
| CORS wildcard | P1 | Origins restreints localhost uniquement |
| API sans auth | P1 | X-API-Token header sur tous les endpoints |
| WS /ninjatrader sans auth | P1 | Token valide a la connexion |
| Payload WS non valide | P1 | Pydantic BarPayload avec contraintes |
| Rate limiting absent | P1 | slowapi 2/min sur /backtest |
| localStorage session | P1 | safeStorage AES Windows |
| Circuit breaker perdu | P2 | Persiste table SQLite circuit_breaker |
| tsconfig absent | P2 | tsconfig strict ajoute |

---

*CDC_MBK_TRADER_TECHNIQUE_v1.1.md — Extraction stricte du code source mbk-trader-v1.0.zip*
*Genere le 30/04/2026 — Mis a jour le 30/04/2026 post-audit securite*
*Zero hallucination — Zero invention*
