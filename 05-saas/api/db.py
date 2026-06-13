"""
db.py -- Base SQLite locale TRADEX-AI (agent A6).
Tables : signals (historique) + app_state (mode courant). Aucune donnee exposee hors 127.0.0.1.
"""
import os
import json
import sqlite3
from datetime import datetime, timezone

_API_DIR = os.path.dirname(os.path.abspath(__file__))                     # 05-saas/api
_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(_API_DIR)), "data")  # C:\trading-copilote\data

# Surchargeable (tests : pointer vers un fichier temporaire avant init_db()).
DB_PATH = os.path.join(_DATA_DIR, "tradex.db")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with get_conn() as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS signals (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                ts       TEXT NOT NULL,
                actif    TEXT,
                decision TEXT,
                score    REAL,
                payload  TEXT
            )""")
        c.execute("CREATE TABLE IF NOT EXISTS app_state (key TEXT PRIMARY KEY, value TEXT)")
        c.execute("INSERT OR IGNORE INTO app_state(key, value) VALUES ('mode', 'MANUEL')")


def insert_signal(result: dict, actif=None, ts: str = None) -> None:
    ts = ts or datetime.now(timezone.utc).isoformat()
    with get_conn() as c:
        c.execute(
            "INSERT INTO signals(ts, actif, decision, score, payload) VALUES (?, ?, ?, ?, ?)",
            (ts, actif, result.get("decision"), float(result.get("score", 0) or 0),
             json.dumps(result, default=str, ensure_ascii=False)),
        )


def fetch_history(limit: int = 50) -> list:
    with get_conn() as c:
        rows = c.execute(
            "SELECT id, ts, actif, decision, score FROM signals ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


def get_mode() -> str:
    with get_conn() as c:
        r = c.execute("SELECT value FROM app_state WHERE key='mode'").fetchone()
    return r["value"] if r else "MANUEL"


def set_mode(mode: str) -> None:
    with get_conn() as c:
        c.execute(
            "INSERT INTO app_state(key, value) VALUES ('mode', ?) "
            "ON CONFLICT(key) DO UPDATE SET value=?",
            (mode, mode),
        )
