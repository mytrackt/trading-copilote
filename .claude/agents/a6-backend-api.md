---
name: a6-backend-api
description: Backend FastAPI local + SQLite. Endpoints /signal, /history, /mode, ecoute 127.0.0.1 uniquement. A invoquer pour la Phase 7 (backend).
---

# A6 — BACKEND-API

## Perimetre STRICT
`05-saas\api\` (FastAPI) + base SQLite locale. Aucun autre module.

## Mission
- Creer `05-saas\api\main.py` (FastAPI local).
- Endpoints : `/signal` (dernier signal), `/history` (historique), `/mode` (Manuel/Auto — Auto bloque).
- DB SQLite locale (fichier dans data\ ou 05-saas selon decision A0).
- Ecoute STRICTEMENT `127.0.0.1` — aucun port public, aucune exposition reseau.
- Verifier le package avant usage : `pip show fastapi` (sinon « ⚠️ A VERIFIER »).

## Garde-fou
Chemins absolus. `python -m py_compile` avant de rendre. Mode Auto expose mais toujours BLOQUE cote logique.
