# RAPPORT — Inventaire technique de `C:\codex-transvideo-safe`

> Mode : **LECTURE SEULE**. Aucune écriture, aucun déplacement, aucune suppression effectués dans le dossier source.
> Seul fichier créé : ce rapport (`C:\trading-copilote\transcription-engine\RAPPORT_codex-transvideo.md`, hors dossier source).
> Date : 2026-06-11.

---

## ÉTAPE 1 — Sortie terminal réelle (arborescence)

Commande exécutée :

```powershell
Get-ChildItem -Path "C:\codex-transvideo-safe" -Recurse | Select-Object FullName, Length, LastWriteTime | Format-Table -AutoSize
```

La sortie complète (427 lignes) a été capturée. Extrait fidèle et structure réelle (chemins tronqués par PowerShell remplacés par le nom complet vérifié) :

### Racine `C:\codex-transvideo-safe\`
```
.gitattributes
.gitignore
notebooklm_market_mechanics_ep1.txt
README.md
requirements.txt
TRANSVIDEO_CONTEXT.md
TRANSVIDEO_STATE.md
transvideo_pipeline.bat
```

### `scripts\`  (le vrai code du pipeline)
```
scripts\agent.py
scripts\channel_scraper.py
scripts\chunk_fuse.py
scripts\corpus_harness.py
scripts\video_filter.py
scripts\__pycache__\  (5 .pyc compilés cpython-312)
```

### `tests\`
```
tests\test_non_network.py
tests\__pycache__\test_non_network.cpython-312.pyc
```

### `07-nouvelles sources\Single Videos\`  (sorties Markdown générées — ~70 fichiers)
```
Market_Mechanics_Ep_1__How_to_Trade_Like_the_Top_1%.md
Market_Mechanics_Ep_1__How_to_Trade_Like_the_Top_1%_001.md … _023.md
Market_Structure__How_To_Know_When_To_Buy,_Sell,_Or_Stay_O….md
Moving_Average_Trading_Secrets_(This_is_What_You_Must_Know….md
Support_And_Resistance_Explained_(Video_4_Of_12).md
Support_and_Resistance_Secrets__Powerful_Strategies_… (plusieurs)
Technical_Analysis_For_Beginners_(The_Ultimate_Guide).md  + _001..._004.md
What_Is_Technical_Analysis__(Video_1_of_12).md  + _001..._015.md
AI_RENDER\  (4 fichiers Support_and_Resistance_Secrets…)
```

### `backups\`  (≈ 60 dossiers d'instantanés horodatés de phases)
```
FRAME-400-B_20260524_163153
GEMINI-VISION-A … G  (7 instantanés 20260524→20260526)
phase6c_b, _c, _d, _e, _f, _g, _h, _i, _i2, _j, _j2, _k, _n, _q  (+ sous-dossiers datés)
phase6d_b, 6e_b, 6f_b, 6g_b, 6l_b, 6m_b
phase6n_a, _b, _c, _e_a, _e_b, _e_c, _e_c_targeted_fix, _e_d ; phase6N-D
phase8c, 8g, 8j, 8l_language_trace, 8o_pedagogical_noise_filter,
phase8r / 8r_bis_pedagogical_grouping, 8u_fallback_grouping_consistency,
phase8w, 8y_a, 8y_c, 8z_b, 8z_d, 8z_e ; phase9a_b, 9a_c
safety_gemini_current\20260524_202400  (snapshot le plus complet : agent.py + chunk_fuse.py
   + README.md + requirements.txt + ROLLBACK_INSTRUCTIONS.md + transvideo_pipeline.bat + TRANSVIDEO_STATE.md)
state, state_b, state_c, state_after_6n_a/_c/_e_a, state_after_post_6n_c_real
```
Contenu type de chaque backup : `chunk_fuse.py` + `test_non_network.py` (parfois `agent.py`, `.bak`, ou `TRANSVIDEO_STATE.md`).

### `logs\`  (≈ 46 logs + ≈ 40 rapports JSON, du 2026-06-05 au 2026-06-10)
```
transvideo_YYYYMMDD_HHMMSS.log              (logs d'exécution datés)
transvideo_report_YYYYMMDD_HHMMSS_xxxxxx.json  (rapports JSON d'exécution)
logs\cache\   (cache scraper yt-dlp, TTL 24h — créé à l'exécution)
```

---

## ÉTAPE 2 — Tri par type

### A. Scripts (code Python) — `scripts\`
| Fichier | Lignes | Rôle (1 phrase) |
|---|---|---|
| `agent.py` | 753 | **Orchestrateur principal / CLI** : parse les arguments (`--url`, `--channel`, `--max-videos`, `--limit`, `--diagnostic`), configure le logging daté, enchaîne scraping → filtrage → traitement vidéo, écrit le rapport JSON et gère un checkpoint. |
| `channel_scraper.py` | 318 | **Scraper de chaîne YouTube** via `yt-dlp` : récupère titre/durée/description des vidéos d'une chaîne, avec cache disque déterministe (clé SHA-256, TTL 24h) dans `logs\cache\`. |
| `chunk_fuse.py` | 8073 | **Cœur du pipeline « Chunk & Fuse »** (5 phases : download yt-dlp → extraction keyframes ffmpeg → transcription SRT/Whisper → N appels vision API ciblés → fusion Markdown). Contient toute la logique anti-hallucination, l'extraction pédagogique transcript-first, le scoring et la détection de dérive linguistique. |
| `video_filter.py` | 53 | **Filtre de durée** : ne retient que les vidéos de 3 à 50 min (rejette durée 0 = live/playlist). |
| `corpus_harness.py` | 582 | **Harnais de validation corpus non-réseau** : lit les rapports JSON locaux et rend un verdict (`CORPUS_VALIDÉ` / `NON_VALIDÉ` / `REVUE_HUMAINE_REQUISE` / `INSUFFISANT`) en validant le schéma de chaque rapport. |

### B. Scripts batch / lanceurs
| Fichier | Rôle |
|---|---|
| `transvideo_pipeline.bat` | Lanceur Windows double-clic : vérifie `agent.py`, `py`, `ffmpeg`, `yt-dlp`, demande la clé API en saisie masquée, propose menu (1 chaîne / 2 vidéo unique), appelle `agent.py`. ⚠️ cette version du `.bat` redemande `ANTHROPIC_API_KEY` alors que le défaut du code est désormais **Gemini**. |

### C. Configs / dépendances
| Fichier | Rôle |
|---|---|
| `requirements.txt` | **Vide de packages tiers** : le code n'utilise que la bibliothèque standard Python + modules locaux. `ffmpeg`/`ffprobe`/`yt-dlp` sont des CLI externes, pas des imports. |
| `.gitignore` / `.gitattributes` | Ignorent logs, backups, sorties générées, caches. |

### D. Bases de connaissances / docs de pilotage (`.md`)
| Fichier | Rôle |
|---|---|
| `TRANSVIDEO_STATE.md` | **Source de vérité opérationnelle** (maj 2026-05-27) : état des phases, dernier test réel, réserves qualité, règles obligatoires. Prévaut sur tout autre doc en cas de contradiction. |
| `TRANSVIDEO_CONTEXT.md` | Contexte/objectif historique : pipeline transcription pédagogique anti-hallucination, objectif 95 % d'affirmations sourcées, garde-fous. |
| `README.md` | Documentation utilisateur complète (prérequis, install, variables `TRANSVIDEO_*`, usages, dépannage, limites). |

### E. Transcriptions / sorties déjà produites
| Élément | Rôle |
|---|---|
| `07-nouvelles sources\Single Videos\*.md` (~70) | Markdown pédagogiques générés (résumé, concepts, règles, statut CONFIRMÉ/INFÉRENCE/NON VÉRIFIÉ). |
| `notebooklm_market_mechanics_ep1.txt` | Transcription/notes externes (NotebookLM) de la vidéo de référence — utilisée comme comparatif, **jamais comme vérité absolue** (cf. garde-fous). |
| `logs\transvideo_report_*.json` (~40) | Rapports d'exécution structurés (compteurs, statuts, scores qualité). |

### F. Tests
| Fichier | Rôle |
|---|---|
| `tests\test_non_network.py` | 8753 lignes — **suite de tests unittest 100 % hors-réseau** (≈144 tests à la dernière phase consignée), couvrant fallback frame/API, neutralisation des setups, classification d'erreurs, etc. |

### G. Backups & logs (volumineux, non réutilisables tels quels)
- `backups\` : ~60 snapshots de phases (historique de développement, rollback). Le plus complet : `safety_gemini_current\20260524_202400`.
- `logs\` : logs + rapports JSON d'exécution (06/2026).

---

## ÉTAPE 3 — Éléments RÉUTILISABLES pour un projet de transcription YouTube fiable

Classés du plus directement réutilisable au plus accessoire.

### 1. `scripts\chunk_fuse.py` — réservoir de fonctions (le plus précieux)
Le fichier est un **monolithe de ~130 fonctions** directement pertinentes pour de la transcription/extraction fiable. Briques notables (par nom de fonction vérifié) :

**Transcription (sous-titres + Whisper)**
- `get_segments()` — orchestration transcript : natif → auto → Whisper.
- `_try_native_subs()`, `_try_auto_subs()` — sous-titres YouTube via yt-dlp.
- `_parse_srt_files()` — parsing SRT → segments timestampés.
- `_try_whisper()`, `_whisper_transcribe()`, `_whisper_transcribe_chunked()` — fallback Whisper avec **chunking audio** (`_segment_audio_by_duration`, `_initial_whisper_segment_time`) pour contourner la limite ~20 Mo d'OpenAI.
- `_build_transcript_source_diagnostic()`, `get_last_whisper_language_trace()` — **détection de dérive linguistique** (utile : évite les transcripts Whisper qui partent en indonésien, etc.).
- `get_window()` — fenêtre de transcript alignée sur un timestamp.

**Frames / vision**
- `download_video()`, `get_duration()`, `extract_frames()` — yt-dlp + ffmpeg keyframes à intervalle dynamique.
- `analyze_frame()`, `_run_pass_b()`, `call_api()` / `call_gemini_api()` / `call_anthropic_api()` — appels vision **multi-provider** (Gemini par défaut, Anthropic optionnel) avec retry/backoff (`compute_api_retry_delay`) et **redaction des clés** dans les erreurs (`_redact_api_error_detail`).
- `classify_frame_api_error()` — classification d'erreurs (`provider_overloaded`, `rate_limited`, `timeout`…).

**Scoring & extraction pédagogique (anti-hallucination)**
- `make_pedagogical_windows()`, `validate_pedagogical_items()`, `pedagogical_status_for_item()` — extraction transcript-first avec statut CONFIRMÉ/INFÉRENCE/NON VÉRIFIÉ.
- `source_text_in_transcript()`, `categorize_pedagogical_text()`, `is_promotional_or_performance_claim()` — vérification preuve + filtrage des claims promotionnels.
- `detect_forbidden_trading_fields()`, `find_sltp_in_transcript()`, `has_price_levels()` — **détection/extraction de setups trading** (SL/TP/niveaux) et garde-fous anti-invention.

> Réutilisation : ces fonctions sont **autonomes (stdlib only)** et copiables fonction par fonction. Particulièrement utiles : le chunking Whisper, le parsing SRT, la détection de dérive linguistique, l'abstraction multi-provider vision, et le scoring « preuve transcript ».

### 2. `scripts\channel_scraper.py`
Scraping d'une chaîne YouTube + **cache disque** (SHA-256, TTL 24h) → évite de re-scraper et de cogner les quotas. Réutilisable tel quel pour alimenter une file de vidéos à transcrire.

### 3. `scripts\agent.py`
Squelette d'**orchestrateur CLI + logging daté + rapport JSON + checkpoint** : bon point de départ pour un runner de transcription batch (reprise sur erreur, sortie auditable).

### 4. `scripts\corpus_harness.py`
Validateur **non-réseau** de rapports JSON → utile pour un **CI/QA** : vérifier qu'un corpus transcrit respecte des seuils qualité (couverture preuve, hallucinations, scores) avant publication.

### 5. `scripts\video_filter.py`
Filtre de durée trivial (3–50 min) — réutilisable directement pour écarter lives/playlists/vidéos hors-format.

### 6. `tests\test_non_network.py`
~144 tests hors-réseau → modèle de **harnais de test déterministe** (mocks API) pour sécuriser tout refactor du pipeline sans appeler YouTube/Gemini.

### 7. Sorties `*.md` + rapports JSON
Jeu de **données de référence réelles** (vidéos trading déjà transcrites + métriques) pour benchmarker un nouveau pipeline (golden files).

### Garde-fous réutilisables (de `TRANSVIDEO_STATE.md` / `CONTEXT.md`)
Principes directement transposables : transcript d'abord puis frames ; toute affirmation importante = preuve ou « NON VÉRIFIÉ » ; ne jamais inventer SL/TP/timeframe/signal ; séparer claim pédagogique vs setup tradable ; ne jamais déclarer `success_total` si une erreur API persiste.

---

## ÉTAPE 4 — Rapport

Ce document **EST** le livrable de l'étape 4 (`C:\trading-copilote\transcription-engine\RAPPORT_codex-transvideo.md`).

---

## ÉTAPE 5 — Anti-triche (sortie terminal réelle)

Vérifié par exécution réelle :
- `Get-ChildItem -Recurse` → **427 lignes** de sortie capturées (sauvegardées par le harness, lues intégralement).
- `wc -l` sur les scripts → **valeurs réelles** :
```
   753 agent.py
   318 channel_scraper.py
  8073 chunk_fuse.py
   582 corpus_harness.py
    53 video_filter.py
  8753 tests/test_non_network.py
 18532 total
```
- Cartographie des fonctions de `chunk_fuse.py` extraite par `grep -n '^def |^class '` (réelle, pas supposée).

Aucune supposition « ça devrait contenir » : tous les contenus cités ont été lus.

---

## Notes / incohérences détectées (non corrigées, lecture seule)
1. **Provider par défaut = Gemini** dans le code (`DEFAULT_VISION_PROVIDER = "gemini"`, `claude-sonnet-4-6` seulement si `TRANSVIDEO_VISION_PROVIDER=anthropic`), mais `transvideo_pipeline.bat` réclame encore `ANTHROPIC_API_KEY`. Le mode terminal avec `GEMINI_API_KEY` est à privilégier.
2. **État opérationnel** (`TRANSVIDEO_STATE.md`) : dernière phase consignée 6N-E-A ; dernier test réel `success_partial` (échec frame Gemini HTTP 503, fallback transcript-first OK). **Objectif fiabilité 95 % NON VALIDÉ**, robustesse corpus large NON VÉRIFIÉE.
3. Les en-têtes de fichiers indiquent un ancien chemin `C:\trading-copilote\scripts\…` (projet TRADEX-AI), alors que le code tourne réellement depuis `C:\codex-transvideo-safe\scripts\` — `BASE_DIR` est dérivé dynamiquement, donc sans impact fonctionnel.
