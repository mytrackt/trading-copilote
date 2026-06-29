"""
staleness_monitor.py -- Surveillance de la fraicheur des donnees
Verifie que chaque source de donnees est recente avant tout signal.
"""
import os
from datetime import datetime, timedelta

# Feeds Phase C (collecteurs actifs — noms réels des fichiers écrits)
_OTHER_LIMITS = {
    "news_data.json":         timedelta(minutes=5),   # Phase C — news_collector.py (5 min)
    "macro_data.json":        timedelta(hours=24),     # Phase C — macro_collector.py (quotidien)
    "cot_data.json":          timedelta(days=8),       # Phase C — cot_collector.py (hebdo CFTC)
    # Feeds futurs (non encore produits — MISSING attendu, pas d'alerte bloquante)
    "fear_greed_stocks.json": timedelta(minutes=15),
    "events_calendar.json":   timedelta(hours=2),
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
    important = ["news_data.json"]  # Phase C actif -- macro_data.json non bloquant (quotidien)

    if any(not staleness.get(s, {}).get("ok", False) for s in critical):
        return "BLOCKED"
    if any(not staleness.get(s, {}).get("ok", False) for s in important):
        return "MANUAL_ONLY"
    return "OPERATIONAL"
