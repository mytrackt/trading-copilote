"""
settings.py — Configuration centrale TRADEX-AI
Source de vérité pour actifs, seuils, timeouts, chemins.
NE PAS mettre de clés API ici → utiliser os.getenv()
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# CLASSIFICATION DES ACTIFS — 3 CATÉGORIES VERROUILLÉES
# =============================================================================

# Catégorie 1 : TRADING — ordres possibles via NT8 ATI
ACTIFS_TRADABLES = ["GC", "HG", "CL", "ZW"]

# Catégorie 2 : CONFIRMATION — analyse uniquement, jamais d'ordres
ACTIFS_CONFIRMATION = {
    "DX": {
        "role":  "Macro — Dollar Index",
        "trade": False,
        "proxy": "DXY Alpha Vantage (futures DX indirect)"
    },
    "ES": {
        "role":  "Confirmation SP500 — risk on/off",
        "trade": False
    },
    "VX": {
        "role":  "Sentiment — peur marché",
        "trade": False
    },
}

# Catégorie 3 : RÉFÉRENCE — corrélations inter-marché, jamais d'ordres
ACTIFS_REFERENCE = {
    "MBT": {
        "role":  "Bitcoin Micro — référence crypto inter-marché",
        "trade": False,
        "note":  "Bitcoin supprimé des tradables — référence uniquement"
    },
    "6J": {
        "role":  "Yen Japonais — référence devise refuge",
        "trade": False,
        "note":  "Yen supprimé des tradables — référence uniquement"
    },
}

# Règle d'entrée Belkhayate
REGLE_ENTREE = {
    "trading_requis":     3,  # min 3/4 actifs trading alignés
    "trading_total":      4,
    "confirmation_requis": 2,  # min 2/3 actifs confirmation alignés
    "confirmation_total":  3,
}

# =============================================================================
# NINJATRADER 8 ATI — CONNEXION TCP/IP
# =============================================================================
NT8_ATI = {
    "host":    "127.0.0.1",
    "port":    36973,
    "timeout": 5,   # secondes
}

# =============================================================================
# CHEMINS FICHIERS
# =============================================================================
DATA_DIR = os.path.join(BASE_DIR, "data")
KB_DIR   = os.path.join(BASE_DIR, "kb")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

KB_PATH            = os.path.join(KB_DIR, "KNOWLEDGE_BASE_MASTER.json")
NT8_DATA_PATH      = os.path.join(DATA_DIR, "nt8_data.json")
ATAS_DATA_PATH     = os.path.join(DATA_DIR, "atas_data.json")
RISK_STATE_PATH    = os.path.join(DATA_DIR, "risk_state.json")
SIGNAL_HISTORY_PATH = os.path.join(DATA_DIR, "signal_history.json")

# =============================================================================
# SEUILS DE RISQUE
# =============================================================================
RISK = {
    "dd_day_max":    0.03,   # 3% drawdown journalier → STOP jour (aligne avec risk_manager.py:drawdown_stop_jour)
    "dd_week_max":   0.05,   # 5% drawdown semaine → arrêt complet
    "vix_extreme":   35,     # VIX > 35 → suspendre Auto
    "vix_warning":   25,     # VIX > 25 → réduire taille
    "suspension_min": 15,    # minutes suspension après perte
    "suspension_max": 60,    # minutes suspension si DD > 1.5%
}

# =============================================================================
# SIGNAL ET CONFIANCE
# =============================================================================
SIGNAL = {
    "score_min_claude":   17,   # /21 pts — minimum pour appel Claude
    "score_min_fallback": 17,   # /21 pts — minimum pour signal fallback
    "confiance_min_auto": 85,   # % minimum pour Mode Auto (signal ET execution unifies sur 85 - aligne risk_manager.py:confiance_auto_min)
    "confiance_max_fallback": 65,  # % MAX en fallback (Claude indisponible)
    "rate_limit_sec":     10,   # 1 analyse max / 10 secondes
    "max_tokens":         1000,
}

# =============================================================================
# STALENESS — FRAÎCHEUR DES DONNÉES
# =============================================================================
STALENESS = {
    "nt8_max_age_sec":    10,   # NT8 doit être < 10s
    "atas_max_age_sec":   30,   # ATAS < 30s
    "cot_max_age_hours":  168,  # COT hebdo = 7 jours
    "news_max_age_min":   5,    # News < 5 min
}

# =============================================================================
# NEWS GATE — BLOQUER AVANT ÉVÉNEMENTS MACRO
# =============================================================================
NEWS_GATE_MINUTES = 30  # Bloquer 30min avant NFP/FOMC/CPI

NEWS_EVENTS_CRITIQUES = [
    "NFP",          # Non-Farm Payrolls
    "FOMC",         # Fed interest rate decision
    "CPI",          # Consumer Price Index
    "GDP",          # PIB US
    "JOLTS",        # Job Openings
    "PPI",          # Producer Price Index
]

# =============================================================================
# MODÈLES CLAUDE
# =============================================================================
CLAUDE = {
    "model_kb":     "claude-sonnet-4-6",              # KB + signaux
    "model_vision": "claude-sonnet-4-20250514",        # Vision TradingView (optionnel)
    "cache_type":   "persistent",                      # Prompt caching KB
    "max_tokens":   1000,
}

# =============================================================================
# CIRCUIT BREAKER
# =============================================================================
CIRCUIT_BREAKER = {
    "timeout_sec":    15,    # timeout appel
    "retry_max":       2,    # nombre de retry
    "retry_delay_sec": 3,    # délai entre retry
    "open_duration_sec": 60, # durée circuit ouvert avant reset
}
