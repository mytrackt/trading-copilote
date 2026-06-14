# REGISTRE DE VALIDITE DOCUMENTAIRE — TRADEX-AI (tenu par A9)

> Defiance documentaire : aucun fichier cru par defaut. Aucune regle de trading ne derive d'un doc non ✅ VALIDE.
> Statuts : ✅ VALIDE (source verifiable) · ⚠️ DOUTEUX (origine/fiabilite incertaine) · ❌ INVALIDE (interdit comme source).
> Initialise le 13/06/2026 (Phase 1, agent A9).

## 1. Documents centraux

| Fichier | Statut | Source / raison | Action A9 |
|---|---|---|---|
| `CLAUDE.md` | ✅ VALIDE | Source de verite absolue du projet | A synchroniser : score 17/21 -> /10 (arbitrage 13/06) |
| `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` | ⚠️ DOUTEUX | 142 fichiers = syntheses NotebookLM, PAS de vrais transcripts | PROVISOIRE — rebuild Phase B-02 ; aucun signal reel ne s'en sert |
| `00-pilotage\STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md` | ⚠️ DOUTEUX (partiel) | Formules COG/Timing/Energie etiquetees [HYPOTHESE TESTABLE]/[RECONSTRUCTION] | Valider via sources externes (Academia.edu « belkhayate gravity center », Pine Script) avant de figer |
| `00-pilotage\GUIDE MAITRE — METHODE MUSTAPHA BELKHAYATE.md` | ⚠️ DOUTEUX | Marque douteux (commit 96e9bbe) ; Squeeze/Tir-a-l'arc, VWAP+MFI a valider | Recouper avec vrais transcripts |

## 2. Formules de trading (statut de codage)

| Formule | Statut | Decision |
|---|---|---|
| COG (regression deg 2-3, N≈250, bandes k={1.618;2.618;4.236}) | ⚠️ [RECONSTRUCTION] | Codable par A1 avec flag explicite + endpoint fige ; lookback N a backtester |
| Timing (echelle ±10, entree [4;8]/[-8;-4]) | ⚠️ [DOCUMENTE] | Codable par A1 |
| **Energie** | ❌ NON CODEE | Arbitrage 13/06 : attendre vrais transcripts. Conflit non tranche : MFI 20/80 (memoire utilisateur) vs (Vol/MoyVol20)x(ATR14/MedianeATR100) (doc, [HYPOTHESE]) |

## 3. Transcripts a etiqueter (couche enrichissement)

| Lot | Statut | Action |
|---|---|---|
| `03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\*` | ✅ ETIQUETE (S08 14/06) | Manifeste `MANIFESTE_TRANSCRITS.csv` : 110 fichiers, 0 hallucination, 108 VALIDE / 2 A_VERIFIER. Provenance 100% chaine officielle Belkhayate (dossier) ; 41/110 ont un titre sans 'Belkhayate'. Langues : 106 FR, 3 EN, 1 mixte. Audit complet `AUDIT_QUALITE.md` |
| 2 transcrits `A_VERIFIER` | ⚠️ A CONFIRMER | "Belkhayate Trading Video 2" (466 mots) et "Video 10" (1101 mots) : 0 terme Belkhayate detecte -> verif manuelle avant integration KB. Les 108 autres = VALIDE |
| Chaines non-Belkhayate (Gigi, Trading Geek, Single Videos, etc.) | ⚠️ A ETIQUETER | 0 transcrit pour l'instant ; ranger en couche `enrichissements_exte