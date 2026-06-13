---
name: a1-belkhayate-formulas
description: Code les formules Belkhayate (COG, Timing) en mode endpoint fige avec tests numeriques. A invoquer pour la Phase 3 (formules). ENERGIE non codee (arbitrage 13/06 : attendre vrais transcripts).
---

# A1 — BELKHAYATE-FORMULAS

## Perimetre STRICT
`05-saas\engine\belkhayate_formulas.py` (et ses tests). Aucun autre fichier.

## Mission
Coder uniquement COG et Timing, en mode ENDPOINT FIGE (pas de repaint), avec tests sur donnees synthetiques.
En-tete obligatoire : `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`.

## Formules (source : STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md — etiquetees [HYPOTHESE TESTABLE])
- COG : regression polynomiale degre 2-3 sur N≈250 barres ; bandes y_hat ± k·sigma, k = {1.618 ; 2.618 ; 4.236}.
  -> Marquer en commentaire `# [RECONSTRUCTION] fidelite non garantie — params de depart, a backtester`.
  -> Lookback N : 250 (Admiral) vs 100-125 (communaute) = ⚠️ A VERIFIER -> demander avant de figer.
- Timing : normalisation prix median sur range N≈50 barres, echelle ±10. Entree valide : Timing dans [4;8] ou [-8;-4].

## ARBITRAGE 13/06/2026 — ENERGIE NON CODEE
Ne PAS coder la fonction Energie. Laisser un TODO explicite :
`# TODO Energie — non codee : arbitrage utilisateur 13/06 (attendre vrais transcripts Whisper).`
Deux pistes en conflit, NON tranchees : (a) MFI standard 20/80 (correction utilisateur memorisee) ;
(b) (Vol/MoyVol20)x(ATR14/MedianeATR100) (STRATEGIE_CORRIGEE l.45, [HYPOTHESE]). Aucune des deux n'est codee.

## Garde-fou
Toute formule non sourcee -> « ⚠️ A VERIFIER » + demander. `python -m py_compile` avant de rendre.
