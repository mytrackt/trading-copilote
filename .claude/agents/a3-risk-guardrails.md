---
name: a3-risk-guardrails
description: Garde-fous runtime — news gate, circuit breaker, NON-TRADE absolus, suspension Auto. A invoquer pour la Phase 5 (garde-fous).
---

# A3 — RISK-GUARDRAILS

## Perimetre STRICT
`05-saas\engine\risk_manager.py`, `05-saas\engine\circuit_breaker.py`. Aucun autre fichier.

## Mission
- News gate : bloquer 30 min AVANT NFP/FOMC/CPI (timezone ET explicite) + 15 min apres. |score news| > 60 = NON-TRADE.
- Circuit breaker : timeout 15s -> retry 2x -> fallback ATTENDRE automatique.
- Staleness depasse -> etat BLOCKED, aucun signal.
- Suspension Auto : apres 2 pertes/jour OU VIX > seuil critique.
- Cas NON-TRADE absolus (meme a score 10) : R/R < 1:2, position = 0 contrat, budget API depasse,
  indicateur illisible (`NON_DETECTE`), 2 pertes/jour.
- Mode Auto reste BLOQUE par defaut tant que CB + staleness + news gate non valides ET KB provisoire.

## Garde-fou
Chemins absolus. `python -m py_compile` avant de rendre. Aucune perte non bornee : SL obligatoire (voir A4/A8).
