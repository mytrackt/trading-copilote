# BRIEFING FIN DE PHASE A — 03 Mai 2026

> **À LIRE EN ENTIER avant toute action dans la prochaine session.**
> Ce fichier suit la convention `_context/briefing-YYYY-MM-DD-*.md` et est
> automatiquement repéré par la règle 0 de `CLAUDE.md` projet.
>
> Phase A (documentation + garde-fous) : ✅ **TERMINÉE et POUSSÉE sur GitHub**.
> Prochaine session : **Phase B — KB Belkhayate**.

---

## 1. ÉTAT GIT À LA FIN DE SESSION

```
Branch  : master
HEAD    : 9f31edd S02-docs - Garde-fous proposes + feuille de route
Sync    : ✅ up to date avec origin/master
Tree    : clean
```

4 commits poussés cette session :
```
9f31edd S02-docs - Garde-fous proposes + feuille de route (documents uniquement)
6e24070 chore: phase 0 backup - gitignore settings.local.json et pdf source externe
faf0678 docs: ajout APPORTS_GUIDE_EXTERNE - segments retenus du guide externe
51d44f1 chore: session 02-05-2026 terminee
```

Backup disque local : `C:\BACKUP_TRADEX_20260503_011804\` (913 MB, 2050 fichiers).

---

## 2. CE QUI A ÉTÉ FAIT EN PHASE A

### 2.1 — Apports guide externe (commit `faf0678`)
- `docs/APPORTS_GUIDE_EXTERNE.md` (616 lignes) — 6 sections retenues du PDF
  externe pour `signal_scorer.py` / `risk_manager.py` / `claude_brain.py` :
  walk-forward, hysteresis, régime marché, risk enrichi, prompt engineering,
  filtres anti-bruit. Source PDF ignorée du repo.

### 2.2 — Phase 0 v4.0 (commit `6e24070`)
- Backup disque créé.
- `.gitignore` enrichi : `.claude/settings.local.json` + PDF source +
  `BACKUP_*/` + (commit suivant) `PROMPT_TRADEX_AI_CLAUDE_CODE_v4.md`.
- `git rm --cached .claude/settings.local.json` (untracké, conservé sur disque).

### 2.3 — Phase 1-Light + corrections Risk Engine (inclus dans `9f31edd`)
- `code/config/settings.py` :
  - L.82 : `dd_day_max: 0.02 → 0.03` (aligné avec `risk_manager.py:drawdown_stop_jour`)
  - L.96 : `confiance_min_auto: 75 → 85` (signal ET exécution unifiés sur 85)

### 2.4 — Phase 2 v4.0 — SKIPPÉE
- Inventaire `C:\SaaS-workspace\` : **0 React/TS/Tailwind/FastAPI**.
- Décision Abdelkrim : skip (option a).
- Conclusion : dashboard React Phase I sera bootstrappé from scratch
  (`npm create vite@latest`).

### 2.5 — Phase 4-Light + Phase 5 v4.0 (commit `9f31edd`)
- `GARDE_FOUS_PROPOSES.md` (368 lignes) — 32 garde-fous cibles :
  - **20 actifs** dans le code aujourd'hui
  - **10 manquants haute priorité** (G1-G10) avec règle / justification /
    module cible / config recommandée
  - **2 partiels** (P1 invalidation Belkhayate, P2 OPEC calendrier)
- `FEUILLE_DE_ROUTE.md` (270 lignes) — 11 phases A→K séquentielles avec
  prérequis / livrables / critère validation / mapping garde-fous / effort.

### 2.6 — Documents supprimés en cours de route
- `ETAT_EXISTANT.md` et `RISK_ENGINE_VALIDATION.md` (générés Phase 1+4 puis
  supprimés sur demande Abdelkrim — leur contenu utile a été repris dans
  `GARDE_FOUS_PROPOSES.md` et `FEUILLE_DE_ROUTE.md`).

---

## 3. DÉCISIONS PRISES PENDANT LA SESSION

| # | Décision | Validée par |
|---|----------|-------------|
| 1 | DD jour 3 % (settings.py = risk_manager.py harmonisés) | Abdelkrim |
| 2 | Confiance Auto 85 % unifiée (signal ET exécution) | Abdelkrim |
| 3 | Risque max trade reste 2 % (rejet recommandation 1 % du guide externe) | Abdelkrim |
| 4 | Skip Phase 2 v4.0 (SaaS-workspace pas pertinent pour TradEx AI) | Abdelkrim |
| 5 | PDF source externe + PROMPT v4.0 → `.gitignore` | Abdelkrim |
| 6 | `_context/briefing-YYYY-MM-DD-*.md` reste la convention briefing | implicite |

---

## 4. CORRECTIONS À LA STRUCTURE PROJET (vs CLAUDE.md projet)

> ⚠️ **IMPORTANT** — `CLAUDE.md` projet (section ÉTAT ACTUEL) mentionne des
> chemins inexistants. Vérifié à la fin de cette session.

| Mention CLAUDE.md | Réalité disque |
|--------------------|----------------|
| `code/scraper/` | **N'existe pas** — le scraper est `04-kb-sources/youtube-a-scraper/whisper_pipeline.py` |
| `code/transcripts/` | **N'existe pas** — transcripts sont dans `04-kb-sources/youtube-a-scraper/transcripts/` |
| "152 transcripts" | **142 transcripts .txt** réellement (les 10 autres .txt sont dans `02-marches-trading/`, `04-kb-sources/pdfs-gardes/`, racine `04-kb-sources/`) |

→ **Action recommandée prochaine session** : mettre à jour CLAUDE.md pour
refléter la vraie arborescence avant de lancer Phase B.

---

## 5. ÉTAT EXACT DES MODULES

### Code Python (`code/`)
```
code/
├── __init__.py             ✅
├── engine/                 ✅ 6 modules
│   ├── staleness_monitor.py
│   ├── circuit_breaker.py
│   ├── risk_manager.py
│   ├── data_reader.py
│   ├── correlations.py
│   └── claude_brain.py     ⚠️ référence prompt_builder.py qui n'existe pas (claude_brain.py:129)
├── utils/atomic_writer.py  ✅
├── config/settings.py      ✅ corrigé cette session
├── api/                    ⏳ vide (Phase H)
├── collectors/             ⏳ vide (Phase C)
├── execution/              ⏳ vide (Phase G)
└── knowledge_base/         ⏳ vide (Phase B - cible KB JSON)
```

### Sources Belkhayate
```
04-kb-sources/
├── prompt-systeme-trading-intermarches.txt
├── pdfs-gardes/                                ← prompts garde-fous extraits
└── youtube-a-scraper/
    ├── whisper_pipeline.py                     ✅ pipeline transcription existant
    ├── methode-A-apify_w9bbZbBNHwM.txt
    ├── methode-B-whisper_w9bbZbBNHwM.txt
    ├── videos_a_transcrire.txt
    ├── w9bbZbBNHwM.webm                        ⚠️ vidéo binaire dans repo
    └── transcripts/                            ✅ 142 fichiers .txt
        └── whisper_*.txt
```

### Garde-fous (état au 2026-05-03)
- ✅ **20 actifs** (cf `GARDE_FOUS_PROPOSES.md` table « DÉJÀ IMPLÉMENTÉS »)
- ❌ **10 à coder** : G1 stop-loss / G2 slippage / G3 anti-doublon UUID /
  G4 dead zone / G5 rollover / G6 Mandatory Lock File / G7 régime marché /
  G8 killswitch Internet / G9 OPEC calendrier / G10 health FastAPI
- ⚠️ **2 partiels** : P1 invalidation Belkhayate / P2 OPEC blackout calendrier

### Mode AUTO
- 🔒 **BLOQUÉ par défaut** — 5/6 conditions non remplies
- Déverrouillage = Phase K (~3-4 mois calendaires)

---

## 6. PROCHAINE SESSION : PHASE B — KB BELKHAYATE

### Objectif
Extraire les règles Belkhayate depuis les **142 transcripts .txt** vers
`code/knowledge_base/KNOWLEDGE_BASE_MASTER.json` au format consommable par
`claude_brain.py:171` (`load_kb_rules`).

### Cible
Le doc `MASTER_TRADEX_AI_v2.md` mentionne **2337 règles** comme cible KB.
Ce nombre a été mentionné dans CLAUDE.md projet — **à vérifier en début de
Phase B** : est-ce un objectif documenté ou une estimation ? Source à
identifier (probablement extraction manuelle préalable des transcripts).

### Prérequis vérifiés
- ✅ 142 transcripts présents dans `04-kb-sources/youtube-a-scraper/transcripts/`
- ✅ Pipeline `whisper_pipeline.py` existant (à lire pour comprendre le format
  des .txt)
- ✅ `code/knowledge_base/` dossier existant et vide (cible)
- ✅ `claude_brain.load_kb_rules()` attend ce format :
  ```python
  {
      "rules": [
          {"categorie": "GENERAL|BGC|PIVOTS|...", "contenu": "..."},
          ...
      ]
  }
  ```
  (cf `claude_brain.py:188-191`)

### Livrables attendus Phase B
1. Lecture du pipeline existant + 5-10 transcripts pour comprendre la structure
2. Script `code/scraper/extract_rules.py` (à créer) — parser règles depuis .txt
3. `code/knowledge_base/KNOWLEDGE_BASE_MASTER.json` — règles structurées
4. Validation : `claude_brain.load_kb_rules()` charge sans erreur, échantillon
   50 règles aléatoires relues par Abdelkrim
5. Mesure tokens : le system prompt généré tient en < 50k tokens
   (sinon prompt caching inefficace)

### Critère de validation Phase B
- JSON valide structuré comme attendu
- Échantillon manuel OK
- Test d'appel Claude API mock avec ce KB → réponse JSON parsable

### Estimation effort
2-3 sessions Claude Code.

### Pièges à éviter
1. **Ne pas inventer de règles** — extraire littéralement depuis transcripts.
2. **Garde-fou linguistique** : transcripts français — vérifier qu'aucun
   filtre de tokens arabes (cf B7 PROMPT-GATE-AUDIT) ne supprime du contenu.
3. **Encoding UTF-8 obligatoire** — accents français dans les transcripts.
4. **Atomic writes** — utiliser `code/utils/atomic_writer.py` pour écrire le
   JSON final, pas `json.dumps()` direct.
5. **Pas de modification** des fichiers `code/engine/*` ou `code/config/*`
   en Phase B — purement extraction + génération JSON.

---

## 7. RAPPELS NON NÉGOCIABLES

### Décisions verrouillées (CLAUDE.md projet)
- Méthode : **Belkhayate** intouchable
- Stack : Python 3.11 + FastAPI + React 18 + Tailwind 3.4 + SQLite + NT8 ATI port 36973 + Rithmic via NTB
- Modèle Claude : **claude-sonnet-4-6** (KB + signaux)
- Actifs trading : **GC / HG / CL / ZW** (jamais SI, NQ, MBT, 6J)
- Actifs confirmation : DX / ES / VX
- Score signal valide : ≥ 17/21
- Confiance Mode Auto min : **85 %** (unifié cette session)
- DD jour stop : **3 %** (unifié cette session)
- Fallback max : 65 % (Auto interdit)
- VIX no-trade : > 35

### Règles techniques
- Tout code dans `code/` — JAMAIS à la racine
- Chemins absolus `C:\trading-copilote\`
- Conventional Commits, **JAMAIS d'accents** dans les messages
- `python -m py_compile fichier.py` AVANT toute exécution
- Clés API via `os.getenv()` — JAMAIS dans le code
- `.env` toujours dans `.gitignore`
- **PROMPT-GATE-AUDIT v3.1** obligatoire avant tout livrable > 20 lignes

### Protocole d'ouverture session
1. Lire `CLAUDE.md` projet
2. Lire **ce fichier** (briefing le plus récent dans `_context/`)
3. Annoncer : "📍 Phase B — État : KB extraction prête à démarrer — Prochaine action : [action]"
4. Attendre confirmation utilisateur

### Protocole fin de session
1. Générer `_context/briefing-YYYY-MM-DD-*.md`
2. Mettre à jour la section ÉTAT ACTUEL de `CLAUDE.md` projet
3. Proposer le commit final
4. Rappeler `git push origin master`

---

## 8. FICHIERS À LIRE EN PRIORITÉ — PROCHAINE SESSION

| # | Fichier | Pourquoi |
|---|---------|----------|
| 1 | `CLAUDE.md` projet | Décisions verrouillées + règles |
| 2 | Ce fichier | État exact de fin de Phase A |
| 3 | `FEUILLE_DE_ROUTE.md` | Phase B détaillée + dépendances |
| 4 | `GARDE_FOUS_PROPOSES.md` | 32 garde-fous cibles |
| 5 | `04-kb-sources/youtube-a-scraper/whisper_pipeline.py` | Pipeline existant (format transcripts) |
| 6 | `04-kb-sources/youtube-a-scraper/transcripts/whisper_*.txt` (5-10 échantillons) | Comprendre structure |
| 7 | `code/engine/claude_brain.py` lignes 171-193 | Format JSON attendu pour KB |
| 8 | `docs/MASTER_TRADEX_AI_v2.md` SEMAINE 5 (ligne 785+) | Spec moteur Belkhayate |

---

## 9. ACTIONS RECOMMANDÉES PROCHAINE SESSION

```
SESSION B-01 — Setup Phase B
  □ Confirmer cible 2337 règles (source ?) ou fixer une cible réaliste
  □ Lire whisper_pipeline.py + 5 transcripts échantillons
  □ Mettre à jour CLAUDE.md projet (chemins corrects + ÉTAT ACTUEL Phase A done)
  □ Concevoir le format de parsing (regex ? sectionnement ? LLM ?)

SESSION B-02 — Extraction
  □ Créer code/scraper/extract_rules.py
  □ Extraire 10 transcripts en mode pilote
  □ Validation manuelle qualité par Abdelkrim
  □ Itérer si nécessaire

SESSION B-03 — Génération KB complet
  □ Lancer extraction sur les 142 transcripts
  □ Générer KNOWLEDGE_BASE_MASTER.json via atomic_writer
  □ Test claude_brain.load_kb_rules() sans erreur
  □ Mesure tokens < 50k
  □ Commit : "feat: KB Belkhayate v1 - extraction 142 transcripts"
  □ git push
```

---

*Briefing généré le 2026-05-03 par Claude Code (Opus 4.7 1M context).*
*Phase A officiellement terminée et poussée sur origin/master.*
*Prochaine session : Phase B — KB Belkhayate.*
