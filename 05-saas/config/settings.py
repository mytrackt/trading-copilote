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
