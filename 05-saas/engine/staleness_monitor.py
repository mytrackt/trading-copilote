import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")  # C:\trading-copilote\data

STALENESS_LIMITS = {
    "NT8_data.csv":           timedelta(seconds=10),
    "ATAS_signals.json":      timedelta(seconds=10),
    "news_feed.json":         timedelta(minutes=10),
    "fear_greed_stocks.json": timedelta(minutes=15),
    "gdelt_signals.json":     timedelta(minutes=20),
    "events_calendar.json":   timedelta(hours=2),
    "macro.json":             timedelta(hours=6),
    "cot_data.json":          timedelta(days=8),
    "dark_pools.json":        timedelta(days=16),
}

def check_all_staleness() -> dict:
    status = {}
    for filename, limit in STALENESS_LIMITS.items():
        path = os.path.join(DATA_DIR, filename)
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            age = datetime.now() - mtime
            status[filename] = {
                "ok":          age < limit,
                "age_seconds": round(age.total_seconds()),
                "status":      "FRESH" if age < limit else "STALE"
            }
        except FileNotFoundError:
            status[filename] = {"ok": False, "status": "MISSING"}
    return status

def get_system_mode(staleness: dict) -> str:
    critical  = ["NT8_data.csv", "ATAS_signals.json"]
    important = ["news_feed.json", "fear_greed_stocks.json"]
    if any(not staleness.get(s, {}).get("ok", False) for s in critical):
        return "BLOCKED"
    if any(not staleness.get(s, {}).get("ok", False) for s in important):
        return "MANUAL_ONLY"
    return "OPERATIONAL"
