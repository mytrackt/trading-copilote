---
name: a4-signal-scoring
description: Moteur de signal — precondition 3/4+2/3 (Etape 0) puis grille de score deterministe /10, invalidations R8-R10. A invoquer pour la Phase 4 (scoring).
---

# A4 — SIGNAL-SCORING

## Perimetre STRICT
`05-saas\engine\signal_engine.py` (nouveau). Aucun autre fichier.

## Mission
- Step 0 (eliminatoire, AVANT tout score) : 3/4 actifs TRADING alignes (COG meme couleur) ET 2/3 CONFIRMATION favorables. Sinon NON-TRADE.
- Score 0-10 DETERMINISTE (source STRATEGIE_CORRIGEE PARTIE 4) :
  - COG couleur alignee au sens du trade (R1) = ELIMINATOIRE (score 0 si non).
  - Timing dans [4;8]/[-8;-4] (R3) = 2.0 ; bande extreme touchee = 2.0 ; ATR normal (pas de choc) = 0.5 ;
    news clean = 0.5 ; etc. (reprendre la grille exacte du doc).
  - Signal propose si Score >= 7.0 ET aucun critere eliminatoire ET R/R >= 1:2 (validation humaine obligatoire en Manuel).
- Invalidations R8-R10 : ex. COG change de couleur avant TP1 -> sortie immediate.
- Cas NON-TRADE absolus (cf. A3).

## ARBITRAGE 13/06 — SCORE /10
Score sur /10 (pas /21). CLAUDE.md est DEJA synchronise /10 cote Cowork — ne pas le re-editer. Ne pas coder de /21.

## Garde-fou
Aucune formule inventee. `python -m py_compile` avant de rendre.
