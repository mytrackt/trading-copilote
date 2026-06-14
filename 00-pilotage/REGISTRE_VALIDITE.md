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

## 6. Verdict source-transcrits (14/06/2026 -- S08, 110 transcrits Belkhayate)

Source autoritaire : `57DtXQp35Eo_Belkhayate Gravity Center User Guide.txt` (mode d'emploi officiel Belkhayate).

| Question | Verdict | Preuve |
|---|---|---|
| Coeff **0,8618** (GUIDE MAITRE) | ❌ **FAUX** | 0 occurrence dans les 110 transcrits -> erreur du GUIDE MAITRE (confirme ⚠️ douteux) |
| Coeff **1,618** | ✅ CONFIRME | "Traditional Gravity Center" (l.129) |
| Coeff **0,618** | ✅ CONFIRME | variante petrole : "l'ecart n'est plus de 1,618 mais de 0,618" (l.172) |
| Coeff **2,618 / 4,236** | ⚠️ NON-BELKHAYATE | 0 occurrence -> extension communautaire, [HYPOTHESE] |
| **Periode (lookback)** | ✅ **180** (Belkhayate) | "je recommande 180 en periode" (l.176) -- ni 250 ni 100-125 |
| **Ordre / degre** | ✅ **3** (Belkhayate) | "L'ordre, il est de 3" (l.174) -- CONTREDIT la reco degre 2 ; corriger COGParams |
| Repaint | ✅ confirme par Belkhayate | "Bien donc qu'il repeint" (l.105) -> endpoint fige justifie |

NB : ordre 3 / periode 180 / 0,618 decrits pour le setup petrole (range bars 5 ticks) -> a confirmer
sur autres marches/TF dans les autres transcrits. A reporter dans `COGParams` (defaut) en Phase B-02.
| Garde-fous runtime (news/CB/staleness/Auto) | CLAUDE.md + GARDE_FOUS | ✅ conformes decisions verrouillees |
| KB `KNOWLEDGE_BASE_MASTER.json` | -- | ⚠️ DOUTEUX (provisoire) -- `kb_provisoire=True` force Auto interdit |

Conclusion A8 : code conforme aux decisions verrouillees ; aucun signal reel autorise tant que
la KB n'est pas reconstruite (Phase B-02) et les parametres [RECONSTRUCTION] non valides par backtest.

## 7. Passe de nettoyage coherence (S08 - 14/06/2026)

Docs vivants corriges EN PLACE (/21->/10 seuil 7,0 D2 ; screenshot/Vision API->JSON NT8 ; 17-18-20/21->7,0/10) :
- `docs/MASTER_TRADEX_AI_v2.md` (banniere ABANDONNE sur bloc scoring /21 ; box + Mode Auto -> 7,0/10)
- `docs/MODULES.md` (screenshot + Claude Vision API -> lecture NT8 JSON)
- `docs/APPORTS_GUIDE_EXTERNE.md` (regimes Bull/Neutral/Bear -> seuil unique 7,0/10)
- `GARDE_FOUS_PROPOSES.md` (G7 + table regime -> 7,0/10)
- `BACKLOG_ENRICHISSEMENTS.md` (score /21 -> /10)

Sources douteuses ANNOTEES (gardees comme matiere brute, jamais attribuees a Belkhayate) :
- `GUIDE MAITRE — METHODE MUSTAPHA BELKHAYATE.md` : banniere 0.8618 = FAUX (vrais 1,618 / 0,618)
- `02-sources-brutes/kb-sources/pdfs-gardes/competence-intermarches.txt` : banniere 5/8 Ortogonex ABANDONNE -> 3/4+2/3

NON touches (mentionnent l'ancien seulement pour l'INTERDIRE = deja corrects) : `.claude/agents/*`, `PROMPT_CLAUDE_CODE_EQUIPE_AGENTS_TRADEX.md`, `STRATEGIE_TRADEX_BELKHAYATE_CORRIGEE.md`.
NON touches (historique date, ne pas reecrire) : `_context/` (briefings + READMEs S01-S07).
Faux positifs laisses : MASTER 'Vision:' (vision projet), MODULES 'CDC Vision' (nom doc), APPORTS 'di-vision par 2'.
