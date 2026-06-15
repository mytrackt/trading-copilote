# PROMPT CLAUDE CODE — PHASE C : COLLECTEURS NT8/ATAS
> Mode : Claude Code (exécution)
> Session : S12 — 15/06/2026
> Règle absolue : py_compile obligatoire avant tout commit

---

## CONTEXTE

Tu travailles sur TRADEX-AI (`C:\trading-copilote\`).
NT8 n'est pas installé. On crée la structure de données complète avec des fichiers mock
(simulation) pour que tout le code Python soit testable dès maintenant.

**Dette technique résolue par cette phase :**
> Item 3 : Dossier `data\` inexistant (staleness_monitor, data_reader, settings)

---

## TÂCHES À EXÉCUTER (dans cet ordre exact)

---

### TÂCHE 1 — Créer les dossiers

```powershell
New-Item -ItemType Directory -Force -Path "C:\trading-copilote\data\live"
New-Item -ItemType Directory -Force -Path "C:\trading-copilote\data\mock"
```

Créer un fichier `.gitkeep` dans `data\live\` (pour que git suive le dossier vide) :

```powershell
New-Item -ItemType File -Force -Path "C:\trading-copilote\data\live\.gitkeep"
```

---

### TÂCHE 2 — Créer les fichiers mock NT8 (un JSON par actif)

Créer exactement ces 7 fichiers dans `C:\trading-copilote\data\mock\` :

**`data\mock\GC.json`** (Or — haussier)
```json
{
  "symbol": "GC",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "range_5",
  "close": 2351.10,
  "open": 2350.50,
  "high": 2352.80,
  "low": 2349.20,
  "volume": 1250,
  "cog_endpoint": 2348.50,
  "cog_band_618_up": 2353.20,
  "cog_band_618_dn": 2343.80,
  "cog_band_1618_up": 2358.40,
  "cog_band_1618_dn": 2338.60,
  "timing": 5.2,
  "energie": null,
  "direction": "HAUSSIER",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\HG.json`** (Cuivre — haussier)
```json
{
  "symbol": "HG",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "range_5",
  "close": 4.85,
  "open": 4.83,
  "high": 4.87,
  "low": 4.82,
  "volume": 850,
  "cog_endpoint": 4.82,
  "cog_band_618_up": 4.87,
  "cog_band_618_dn": 4.77,
  "cog_band_1618_up": 4.92,
  "cog_band_1618_dn": 4.72,
  "timing": 4.8,
  "energie": null,
  "direction": "HAUSSIER",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\CL.json`** (Pétrole — neutre)
```json
{
  "symbol": "CL",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "range_5",
  "close": 78.45,
  "open": 78.20,
  "high": 78.80,
  "low": 78.10,
  "volume": 2100,
  "cog_endpoint": 78.30,
  "cog_band_618_up": 79.10,
  "cog_band_618_dn": 77.50,
  "cog_band_1618_up": 79.80,
  "cog_band_1618_dn": 76.80,
  "timing": 1.5,
  "energie": null,
  "direction": "NEUTRE",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\ZW.json`** (Blé — haussier)
```json
{
  "symbol": "ZW",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "range_5",
  "close": 585.50,
  "open": 583.00,
  "high": 587.00,
  "low": 582.50,
  "volume": 620,
  "cog_endpoint": 582.00,
  "cog_band_618_up": 588.50,
  "cog_band_618_dn": 575.50,
  "cog_band_1618_up": 594.50,
  "cog_band_1618_dn": 569.50,
  "timing": 6.1,
  "energie": null,
  "direction": "HAUSSIER",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\DX.json`** (Dollar Index — baissier, bon pour l'Or)
```json
{
  "symbol": "DX",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "daily",
  "close": 104.20,
  "open": 104.50,
  "high": 104.65,
  "low": 104.10,
  "volume": 0,
  "cog_endpoint": 104.40,
  "cog_band_618_up": null,
  "cog_band_618_dn": null,
  "cog_band_1618_up": null,
  "cog_band_1618_dn": null,
  "timing": -3.5,
  "energie": null,
  "direction": "BAISSIER",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\ES.json`** (S&P 500 — haussier)
```json
{
  "symbol": "ES",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "daily",
  "close": 5285.50,
  "open": 5275.00,
  "high": 5290.00,
  "low": 5270.00,
  "volume": 125000,
  "cog_endpoint": 5270.00,
  "cog_band_618_up": null,
  "cog_band_618_dn": null,
  "cog_band_1618_up": null,
  "cog_band_1618_dn": null,
  "timing": 4.2,
  "energie": null,
  "direction": "HAUSSIER",
  "source": "NT8",
  "schema_version": "1.0"
}
```

**`data\mock\VX.json`** (VIX — neutre, pas de signaux de peur)
```json
{
  "symbol": "VX",
  "timestamp": "2026-06-15T10:30:00",
  "bar_type": "daily",
  "close": 18.50,
  "open": 18.20,
  "high": 18.80,
  "low": 18.10,
  "volume": 85000,
  "cog_endpoint": null,
  "cog_band_618_up": null,
  "cog_band_618_dn": null,
  "cog_band_1618_up": null,
  "cog_band_1618_dn": null,
  "timing": null,
  "energie": null,
  "vix_delta_pct": 0.016,
  "direction": "NEUTRE",
  "source": "NT8",
  "schema_version": "1.0"
}
```

---

### TÂCHE 3 — Créer le fichier mock ATAS

**`data\mock\ATAS_signals.json`**
```json
{
  "timestamp": "2026-06-15T10:30:00",
  "GC": {
    "delta": 125.5,
    "cum_delta": 450.0,
    "big_buy": 3,
    "big_sell": 1,
    "bid_ask_ratio": 1.2
  },
  "HG": {
    "delta": 85.0,
    "cum_delta": 280.0,
    "big_buy": 2,
    "big_sell": 1,
    "bid_ask_ratio": 1.1
  },
  "CL": {
    "delta": -15.0,
    "cum_delta": 50.0,
    "big_buy": 2,
    "big_sell": 2,
    "bid_ask_ratio": 0.98
  },
  "ZW": {
    "delta": 95.0,
    "cum_delta": 320.0,
    "big_buy": 3,
    "big_sell": 0,
    "bid_ask_ratio": 1.3
  },
  "source": "ATAS",
  "schema_version": "1.0"
}
```

---

### TÂCHE 4 — Réécrire `05-saas\config\settings.py`

Remplacer le contenu COMPLET du fichier par ceci :

```python
"""
settings.py -- Configuration centrale TRADEX-AI
Source de verite pour actifs, seuils, timeouts, chemins.
NE PAS mettre de cles API ici -> utiliser os.getenv()
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# CLASSIFICATION DES ACTIFS -- 3 CATEGORIES VERROUILLEE
# =============================================================================

ACTIFS_TRADABLES = ["GC", "HG", "CL", "ZW"]

ACTIFS_CONFIRMATION = {
    "DX": {"role": "Macro -- Dollar Index", "trade": False, "proxy": "DXY Alpha Vantage"},
    "ES": {"role": "Confirmation SP500 -- risk on/off", "trade": False},
    "VX": {"role": "Sentiment -- peur marche", "trade": False},
}

ACTIFS_REFERENCE = {
    "MBT": {"role": "Bitcoin Micro -- reference crypto", "trade": False, "note": "no trade"},
    "6J":  {"role": "Yen Japonais -- reference refuge", "trade": False, "note": "no trade"},
}

REGLE_ENTREE = {
    "trading_requis":      3,
    "trading_total":       4,
    "confirmation_requis": 2,
    "confirmation_total":  3,
}

# =============================================================================
# NINJATRADER 8 ATI -- CONNEXION TCP/IP
# =============================================================================
NT8_ATI = {
    "host":    "127.0.0.1",
    "port":    36973,
    "timeout": 5,
}

# =============================================================================
# CHEMINS FICHIERS
# =============================================================================
DATA_DIR      = os.path.join(os.path.dirname(BASE_DIR), "data")   # C:\trading-copilote\data
DATA_LIVE_DIR = os.path.join(DATA_DIR, "live")                     # NT8 ecrit ici (production)
DATA_MOCK_DIR = os.path.join(DATA_DIR, "mock")                     # Simulation (NT8 non installe)

# Mettre USE_MOCK_DATA = False quand NT8 installe et configure
USE_MOCK_DATA = True

_ACTIVE_DATA_DIR = DATA_MOCK_DIR if USE_MOCK_DATA else DATA_LIVE_DIR

KB_DIR   = os.path.join(os.path.dirname(BASE_DIR), "04-cerveau-trading")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

KB_PATH             = os.path.join(KB_DIR, "KNOWLEDGE_BASE_MASTER.json")
ATAS_DATA_PATH      = os.path.join(_ACTIVE_DATA_DIR, "ATAS_signals.json")
RISK_STATE_PATH     = os.path.join(DATA_DIR, "risk_state.json")
SIGNAL_HISTORY_PATH = os.path.join(DATA_DIR, "signal_history.json")

# Actifs NT8 (un fichier JSON par actif dans _ACTIVE_DATA_DIR)
NT8_ASSETS = ["GC", "HG", "CL", "ZW", "DX", "ES", "VX"]


def get_nt8_path(symbol: str) -> str:
    """Retourne le chemin absolu du fichier JSON pour un actif NT8."""
    return os.path.join(_ACTIVE_DATA_DIR, f"{symbol}.json")


# =============================================================================
# SEUILS DE RISQUE
# =============================================================================
RISK = {
    "dd_day_max":     0.03,
    "dd_week_max":    0.05,
    "vix_extreme":    35,
    "vix_warning":    25,
    "suspension_min": 15,
    "suspension_max": 60,
}

# =============================================================================
# SIGNAL ET CONFIANCE
# =============================================================================
SIGNAL = {
    "score_min":              7.0,   # /10 -- seuil signal valide (decision D2 13/06/2026)
    "confiance_min_auto":     85,
    "confiance_max_fallback": 65,
    "rate_limit_sec":         10,
    "max_tokens":             1000,
}

# =============================================================================
# STALENESS -- FRAICHEUR DES DONNEES
# =============================================================================
STALENESS = {
    "nt8_max_age_sec":   10,
    "atas_max_age_sec":  30,
    "cot_max_age_hours": 168,
    "news_max_age_min":  5,
}

# =============================================================================
# NEWS GATE
# =============================================================================
NEWS_GATE_MINUTES = 30
NEWS_EVENTS_CRITIQUES = ["NFP", "FOMC", "CPI", "GDP", "JOLTS", "PPI"]

# =============================================================================
# MODELES CLAUDE
# =============================================================================
CLAUDE = {
    "model_kb":     "claude-sonnet-4-6",
    "model_vision": "claude-sonnet-4-20250514",
    "cache_type":   "persistent",
    "max_tokens":   1000,
}

# =============================================================================
# CIRCUIT BREAKER
# =============================================================================
CIRCUIT_BREAKER = {
    "timeout_sec":       15,
    "retry_max":          2,
    "retry_delay_sec":    3,
    "open_duration_sec": 60,
}
```

---

### TÂCHE 5 — Réécrire `05-saas\engine\data_reader.py`

Remplacer le contenu COMPLET du fichier par ceci :

```python
"""
data_reader.py -- Lecture des donnees NT8 et ATAS via JSON
Architecture : un fichier JSON par actif dans data/live/ (ou data/mock/ si USE_MOCK_DATA=True)
NE PAS importer pandas ici -- lecture JSON pure via atomic_writer.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_nt8_asset(symbol: str) -> dict:
    """
    Lit le fichier JSON d'un actif NT8.
    Retourne {} si le fichier est absent ou corrompu.
    Passe par CB_NT8 (circuit breaker).
    """
    from engine.circuit_breaker import CB_NT8
    from utils.atomic_writer import safe_read_json
    from config.settings import get_nt8_path
    path = get_nt8_path(symbol)
    result = CB_NT8.call(lambda: safe_read_json(path))
    return result if isinstance(result, dict) else {}


def read_nt8_data() -> dict:
    """
    Retourne un dict {symbol: data} pour tous les actifs NT8.
    Exemple : {"GC": {...}, "HG": {...}, ...}
    """
    from config.settings import NT8_ASSETS
    return {s: read_nt8_asset(s) for s in NT8_ASSETS}


def read_atas_signals() -> dict:
    """
    Lit les signaux ATAS (un fichier global ATAS_signals.json).
    Retourne {} si absent ou corrompu.
    Passe par CB_ATAS (circuit breaker).
    """
    from engine.circuit_breaker import CB_ATAS
    from utils.atomic_writer import safe_read_json
    from config.settings import ATAS_DATA_PATH
    result = CB_ATAS.call(lambda: safe_read_json(ATAS_DATA_PATH))
    return result if isinstance(result, dict) else {}


def get_vix_delta_pct(minutes: int = 15) -> float:  # noqa: ARG001
    """
    Retourne la variation VIX (champ vix_delta_pct dans VX.json).
    Ce champ est calcule par NT8 (ou statique dans les mocks).
    Le parametre `minutes` est conserve pour compatibilite API.
    """
    try:
        data = read_nt8_asset("VX")
        return float(data.get("vix_delta_pct", 0.0))
    except Exception:
        return 0.0
```

---

### TÂCHE 6 — Réécrire `05-saas\engine\staleness_monitor.py`

Remplacer le contenu COMPLET du fichier par ceci :

```python
"""
staleness_monitor.py -- Surveillance de la fraicheur des donnees
Verifie que chaque source de donnees est recente avant tout signal.
"""
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Feeds secondaires (communs live et mock)
_OTHER_LIMITS = {
    "news_feed.json":         timedelta(minutes=10),
    "fear_greed_stocks.json": timedelta(minutes=15),
    "gdelt_signals.json":     timedelta(minutes=20),
    "events_calendar.json":   timedelta(hours=2),
    "macro.json":             timedelta(hours=6),
    "cot_data.json":          timedelta(days=8),
    "dark_pools.json":        timedelta(days=16),
}


def _check_file(path: str, limit: timedelta) -> dict:
    """Verifie l'age d'un fichier. Retourne MISSING si absent."""
    try:
        mtime = datetime.fromtimestamp(os.path.getmtime(path))
        age = datetime.now() - mtime
        return {
            "ok":          age < limit,
            "age_seconds": round(age.total_seconds()),
            "status":      "FRESH" if age < limit else "STALE",
        }
    except FileNotFoundError:
        return {"ok": False, "status": "MISSING"}


def check_all_staleness() -> dict:
    """
    Retourne un dict de statuts pour toutes les sources de donnees.
    Cles NT8 : "NT8_GC", "NT8_HG", etc.
    Cle ATAS  : "ATAS_signals"
    Autres    : nom du fichier.
    """
    from config.settings import (
        NT8_ASSETS, DATA_DIR, ATAS_DATA_PATH,
        USE_MOCK_DATA, DATA_MOCK_DIR, DATA_LIVE_DIR,
    )
    active_dir = DATA_MOCK_DIR if USE_MOCK_DATA else DATA_LIVE_DIR

    status = {}

    # NT8 : un fichier JSON par actif (max 10s)
    for symbol in NT8_ASSETS:
        path = os.path.join(active_dir, f"{symbol}.json")
        status[f"NT8_{symbol}"] = _check_file(path, timedelta(seconds=10))

    # ATAS (max 30s)
    status["ATAS_signals"] = _check_file(ATAS_DATA_PATH, timedelta(seconds=30))

    # Feeds secondaires
    for filename, limit in _OTHER_LIMITS.items():
        status[filename] = _check_file(os.path.join(DATA_DIR, filename), limit)

    return status


def get_system_mode(staleness: dict) -> str:
    """
    BLOCKED      : au moins un actif trading NT8 ou ATAS manquant/stale
    MANUAL_ONLY  : feeds importants (news, fear&greed) stale
    OPERATIONAL  : tout est frais
    """
    # Actifs trading critiques + ATAS
    critical = [f"NT8_{s}" for s in ["GC", "HG", "CL", "ZW"]] + ["ATAS_signals"]
    important = ["news_feed.json", "fear_greed_stocks.json"]

    if any(not staleness.get(s, {}).get("ok", False) for s in critical):
        return "BLOCKED"
    if any(not staleness.get(s, {}).get("ok", False) for s in important):
        return "MANUAL_ONLY"
    return "OPERATIONAL"
```

---

### TÂCHE 7 — Mettre à jour `.gitignore`

Ajouter ces lignes à la fin de `C:\trading-copilote\.gitignore` :

```
# Donnees live NT8/ATAS (ecrites en temps reel -- ne pas committer)
data/live/
# Fichiers etat runtime (generes par le moteur)
data/risk_state.json
data/signal_history.json
```

---

### TÂCHE 8 — Lint obligatoire

```powershell
python -m py_compile C:\trading-copilote\05-saas\config\settings.py
python -m py_compile C:\trading-copilote\05-saas\engine\data_reader.py
python -m py_compile C:\trading-copilote\05-saas\engine\staleness_monitor.py
```

Chaque commande doit terminer sans erreur (sortie vide = OK).

---

### TÂCHE 9 — Test de lecture rapide

```powershell
cd C:\trading-copilote
python -c "
import sys
sys.path.insert(0, '05-saas')
from engine.data_reader import read_nt8_data, read_atas_signals, get_vix_delta_pct
data = read_nt8_data()
print('NT8 assets lus:', list(data.keys()))
print('GC close:', data.get('GC', {}).get('close'))
atas = read_atas_signals()
print('ATAS timestamp:', atas.get('timestamp'))
vix = get_vix_delta_pct()
print('VIX delta pct:', vix)
"
```

**Résultat attendu :**
```
NT8 assets lus: ['GC', 'HG', 'CL', 'ZW', 'DX', 'ES', 'VX']
GC close: 2351.1
ATAS timestamp: 2026-06-15T10:30:00
VIX delta pct: 0.016
```

---

### TÂCHE 10 — Test staleness

```powershell
python -c "
import sys
sys.path.insert(0, '05-saas')
from engine.staleness_monitor import check_all_staleness, get_system_mode
s = check_all_staleness()
print('NT8_GC:', s.get('NT8_GC'))
print('ATAS:', s.get('ATAS_signals'))
print('Mode:', get_system_mode(s))
"
```

**Résultat attendu (les mocks sont récents → FRESH) :**
```
NT8_GC: {'ok': True, 'age_seconds': ..., 'status': 'FRESH'}
ATAS: {'ok': True, 'age_seconds': ..., 'status': 'FRESH'}
Mode: MANUAL_ONLY   ← normal (news_feed.json manquant)
```

---

### TÂCHE 11 — Commit git (ciblé, jamais git add .)

```powershell
cd C:\trading-copilote
git add data\mock\
git add data\live\.gitkeep
git add 05-saas\config\settings.py
git add 05-saas\engine\data_reader.py
git add 05-saas\engine\staleness_monitor.py
git add .gitignore
git commit -m "feat(phase-c): collecteurs NT8/ATAS - structure data mock + readers JSON"
```

---

## RÉCAPITULATIF DES CHANGEMENTS

| Fichier | Action | Raison |
|---|---|---|
| `data\live\.gitkeep` | CRÉÉ | Dossier production NT8 (vide pour l'instant) |
| `data\mock\*.json` (8 fichiers) | CRÉÉS | Données simulation pour tests |
| `settings.py` | RÉÉCRIT | `DATA_LIVE_DIR` + `DATA_MOCK_DIR` + `USE_MOCK_DATA` + `get_nt8_path()` + fix `score_min` 17→7.0 |
| `data_reader.py` | RÉÉCRIT | JSON par actif (fini CSV) + `read_nt8_asset()` + signatures conservées |
| `staleness_monitor.py` | RÉÉCRIT | Clés NT8_GC/HG/etc. (fini `NT8_data.csv`) |
| `.gitignore` | MODIFIÉ | `data/live/` ignoré (données runtime) |

---

## DÉCISIONS VERROUILLÉES PAR CETTE PHASE

- `USE_MOCK_DATA = True` jusqu'à NT8 installé et configuré
- Schema JSON v1.0 verrouillé — tout NinjaScript devra respecter ce format
- `data/live/` jamais commité dans git
- `data/mock/` commité (référence de test)

---

*Prompt généré par Cowork S12 — 15/06/2026*
*Exécuter dans Claude Code (VS Code) — PAS dans Cowork*
