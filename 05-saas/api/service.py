"""
service.py -- Logique metier de l'API TRADEX-AI (agent A6), independante de FastAPI (testable).

/signal : garde-fous runtime (news/staleness/auto) PUIS signal_engine, puis persistance historique.
/mode   : ne permet JAMAIS d'activer l'Auto (verrouille).
"""
from datetime import datetime, timezone

from engine.signal_engine import evaluate_signal
from engine.risk_manager import runtime_guardrails

from api import db

ALLOWED_MODES = ("MANUEL",)   # AUTO jamais activable via l'API


def process_signal(payload: dict, now=None) -> dict:
    """
    payload = {
        "signal": { ... contexte signal_engine ... },
        "guardrails": {events, staleness_status, pertes_jour, vix, after_min?}
    }
    """
    now = now or datetime.now(timezone.utc)
    g = payload.get("guardrails") or {}

    guard = runtime_guardrails(
        now=now,
        events=g.get("events", []),
        staleness_status=g.get("staleness_status", {}),
        pertes_jour=g.get("pertes_jour", 0),
        vix=g.get("vix"),
        after_min=g.get("after_min", 15),
    )

    # news / staleness bloquent TOUT trade -> NON_TRADE sans appeler signal_engine.
    if not guard["trade_autorise"]:
        result = {
            "decision": "NON_TRADE",
            "raison": "GARDE_FOUS_RUNTIME",
            "blocages": guard["blocages"],
            "score": 0.0,
        }
    else:
        result = evaluate_signal(payload.get("signal") or {})

    # L'API n'active JAMAIS l'Auto : il reste gouverne par les garde-fous (defaut bloque).
    result["mode_auto_autorise"] = guard["mode_auto_autorise"]   # False par defaut
    result["guardrails"] = guard

    db.insert_signal(result, actif=(payload.get("signal") or {}).get("actif"))
    return result


def get_history(limit: int = 50) -> list:
    return db.fetch_history(limit)


def get_mode_state() -> dict:
    return {"mode": db.get_mode(), "auto_locked": True, "auto_actif": False}


def set_mode(mode: str) -> dict:
    mode = (mode or "").upper()
    if mode == "AUTO":
        return {"ok": False, "raison": "AUTO_VERROUILLE", "mode": db.get_mode(),
                "auto_locked": True, "auto_actif": False}
    if mode not in ALLOWED_MODES:
        return {"ok": False, "raison": "MODE_INVALIDE", "mode": db.get_mode()}
    db.set_mode(mode)
    return {"ok": True, "mode": mode, "auto_locked": True, "auto_actif": False}
