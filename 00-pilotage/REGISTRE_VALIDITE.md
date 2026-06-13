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
| `03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\*` | ⚠️ A ETIQUETER | Ajouter `source=` / `fiabilite=` / `methode=` (belkhayate / autre) |
| Chaines non-Belkhayate (Gigi, Trading Geek, Single Videos, etc.) | ⚠️ A ETIQUETER | Ranger en couche `enrichissements_externes` ; jamais attribuer a Belkhayate |

## 4. Documents ecartes

| Fichier | Statut | Raison |
|---|---|---|
| `prompt-systeme-trading-intermarches.txt` | ❌ INVALIDE | BTC+Yen tradables, score /100, non-Belkhayate (audit S06 batch 2) |
| `STRATEGIE_TRADEX_8_MARCHES-*.md` (v1.0) | ❌ OBSOLETE | Remplace par STRATEGIE_CORRIGEE v2.0 |

## 5. Audit QA Phase 9 (13/06/2026 -- agent A8)

Code produit Phases 3-7 : py_compile OK sur tout le SaaS, regression 5/5 suites vertes.
Statut documentaire des formules implementees (rappel -- rien n'est ✅ tant que non recoupe transcripts) :

| Element code | Source | Statut documentaire |
|---|---|---|
| `belkhayate_formulas.cog_endpoint` / `timing_oscillator` | STRATEGIE_CORRIGEE Piliers 1-2 | ⚠️ [RECONSTRUCTION] -- a valider contre vrais transcripts |
| `belkhayate_formulas.energie` | -- | ❌ NON CODEE (stub volontaire NotImplementedError) -- arbitrage 13/06 |
| `signal_engine` grille /10 + Etape 0 | STRATEGIE_CORRIGEE PARTIE 4 | ⚠️ [HYPOTHESE TESTABLE] -- seuils a backtester |
| Garde-fous runtime (news/CB/staleness/Auto) | CLAUDE.md + GARDE_FOUS | ✅ conformes decisions verrouillees |
| KB `KNOWLEDGE_BASE_MASTER.json` | -- | ⚠️ DOUTEUX (provisoire) -- `kb_provisoire=True` force Auto interdit |

Conclusion A8 : code conforme aux decisions verrouillees ; aucun signal reel autorise tant que
la KB n'est pas reconstruite (Phase B-02) et les parametres [RECONSTRUCTION] non valides par backtest.
