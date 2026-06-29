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
# SPECS CONTRATS -- TICK SIZE / TICK VALUE (Couche C0)
# Source : PDF officiels CME Group (23/06/2026) -- KB D173-D176
# (04-cerveau-trading/cme/Extraction_CME_Specs_NQ_ES_GC_v1.md)
# Usage : conversion points/ticks -> USD pour P&L, sizing, stops, R/R.
#
# INCOHERENCE TRANCHEE (decision humaine 2026-05-02, ARCH-17) : actifs
#     verrouilles = TRADING GC/HG/CL/ZW + CONFIRMATION ES/DX/VX.
#     NQ RETIRE (orphelin, hors perimetre -- vestige blueprint Ortogonex).
#     GC (trading) et ES (confirmation) conserves : specs CME verifiees.
#     HG (Cuivre), CL (Petrole WTI), ZW (Ble) : specs NON encore extraites
#     -> TODO ci-dessous, NE PAS inventer. A completer via scraper_pdf + KB.
# =============================================================================
TICK_SPECS = {
    "ES": {
        "name":          "E-mini S&P 500",
        "contract_unit": "50 USD x S&P 500 Index",
        "tick_size":     0.25,      # points d'indice
        "tick_value":    12.50,     # USD par tick
        "settlement":    "cash",
        "product_code":  "ES",
        "source":        "cme_es_specs.pdf / KB D174",
    },
    "GC": {
        "name":          "Gold Futures",
        "contract_unit": "100 troy ounces",
        "tick_size":     0.10,      # USD par troy ounce
        "tick_value":    10.00,     # USD par tick
        "settlement":    "physical",  # /!\ livrable -> clore/rouler avant echeance
        "product_code":  "GC",
        "source":        "cme_gc_specs.pdf / KB D175",
    },
    # TODO (Backlog P1) : specs CME manquantes -- a extraire via scraper_pdf + KB,
    #                     NE PAS inventer les valeurs.
    # "HG": {...},  # Cuivre (COMEX) -- TRADING -- specs CME a extraire
    # "CL": {...},  # Petrole WTI (NYMEX) -- TRADING -- specs CME a extraire
    # "ZW": {...},  # Ble (CBOT) -- TRADING -- specs CME a extraire
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
    "cache_type":   "ephemeral",   # corrige S42 (commit da6e197)
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

# =============================================================================
# PHASE C — COLLECTEURS DE DONNÉES EXTERNES
# Clés API : jamais ici → os.getenv() uniquement
# =============================================================================

# Chemins sorties (écriture atomic_write_json)
COT_DATA_PATH   = os.path.join(DATA_DIR, "cot_data.json")
MACRO_DATA_PATH = os.path.join(DATA_DIR, "macro_data.json")
NEWS_DATA_PATH  = os.path.join(DATA_DIR, "news_data.json")

# Références clés API Phase C (lues depuis .env)
# Ajouter dans .env :
#   FRED_API_KEY=xxxx        (https://fred.stlouisfed.org → Compte gratuit)
#   EIA_API_KEY=xxxx         (https://www.eia.gov/opendata → Compte gratuit)
#   FINNHUB_API_KEY=xxxx     (https://finnhub.io → Plan gratuit suffisant)
#   CFTC : API publique — aucune clé requise

FRED_API_KEY    = os.getenv("FRED_API_KEY", "")
EIA_API_KEY     = os.getenv("EIA_API_KEY", "")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY", "")

# Staleness Phase C (compléter STALENESS existant)
STALENESS["cot_max_age_hours"]   = 168   # hebdomadaire
STALENESS["macro_max_age_hours"] = 24    # quotidien
STALENESS["news_max_age_min"]    = 5     # 5 minutes
