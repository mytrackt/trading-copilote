---
name: a5-claude-brain
description: Cerveau Claude — aligner le fallback /21 -> /10, prompt caching KB, fallback <= 65%, KB provisoire = Auto interdit. A invoquer pour la Phase 6 (cerveau).
---

# A5 — CLAUDE-BRAIN

## Perimetre STRICT
`05-saas\engine\claude_brain.py`. + sync doc CLAUDE.md (score /10) en coordination avec A0.

## Mission
- Passer le fallback de /21 a /10 (alignement grille A4).
- Prompt caching sur la KB (system + cache_control) -> economies tokens.
- Cle API : `os.getenv("ANTHROPIC_API_KEY")` UNIQUEMENT, jamais en dur.
- `parse_claude_json()` : jamais `json.loads()` direct sur la reponse Claude.
- Rate limiting : `time.sleep(1.5)` entre appels.
- Fallback local : confiance MAX 65%, mode Auto TOUJOURS interdit en fallback.
- Charger la KB avec flag `kb_provisoire=True` : tant que vrai -> Auto interdit + banniere
  « KB provisoire — transcription Whisper non terminee » + confiance plafonnee.

## ARBITRAGE 13/06 — SCORE /10 (NE PAS RE-EDITER CLAUDE.md)
CLAUDE.md est DEJA synchronise /10 sur le disque (cote Cowork). A5 aligne UNIQUEMENT le code du fallback
sur /10 ; il ne re-edite PAS CLAUDE.md.

## Garde-fou
`python -m py_compile` avant de rendre. Aucun signal reel base sur la KB provisoire.
