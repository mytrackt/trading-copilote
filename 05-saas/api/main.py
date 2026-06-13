"""
main.py -- Application FastAPI locale TRADEX-AI (agent A6).

ECOUTE STRICTEMENT 127.0.0.1 (aucun port public). Endpoints : /signal, /history, /mode.
Mode Auto VERROUILLE (jamais activable via /mode). Cle API jamais en dur (os.getenv cote engine).

Lancement : py main.py   (uvicorn sur 127.0.0.1:8000)
"""
import os

from fastapi import FastAPI
from pydantic import BaseModel

from api import db, service

HOST = "127.0.0.1"   # STRICTEMENT local -- jamais d'exposition reseau publique
PORT = 8000

# Rappel : la cle API n'est JAMAIS en dur -> lue via os.getenv (engine.claude_brain).
_API_KEY_PRESENTE = bool(os.getenv("ANTHROPIC_API_KEY"))

db.init_db()

app = FastAPI(
    title="TRADEX-AI API (local)",
    description="Backend local 127.0.0.1 -- mode Auto verrouille, usage prive.",
)


class SignalRequest(BaseModel):
    signal: dict = {}
    guardrails: dict = {}


class ModeRequest(BaseModel):
    mode: str


@app.get("/health")
def health():
    return {"status": "ok", "host": HOST, "auto_locked": True, "api_key_presente": _API_KEY_PRESENTE}


@app.post("/signal")
def post_signal(req: SignalRequest):
    """Evalue un signal via garde-fous runtime + signal_engine ; persiste l'historique."""
    return service.process_signal(req.model_dump())


@app.get("/history")
def get_history(limit: int = 50):
    return {"history": service.get_history(limit)}


@app.get("/mode")
def get_mode():
    return service.get_mode_state()


@app.post("/mode")
def post_mode(req: ModeRequest):
    """MANUEL seulement. Toute demande d'AUTO est refusee (mode Auto verrouille)."""
    return service.set_mode(req.mode)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)   # 127.0.0.1 uniquement
