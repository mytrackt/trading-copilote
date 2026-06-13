# README DE TRANSITION — TRADEX-AI
**Date :** 14/06/2026 | **Session :** S07 | **Mode :** Cowork + Claude Code

---

## 1. ÉTAT ACTUEL DU PROJET

Construction de l'**équipe de 10 agents Claude Code** (a0→a9) + squelette complet de l'application
de trading locale, livré en **9 phases** avec validation « OUI » entre chacune. **68 tests automatiques
verts** (8 Belkhayate + 16 signal + 21 risk + 13 brain + 10 API) + `npm run build` OK + `py_compile` OK.
Mode AUTO **bloqué** par défaut et non activable (UI + API + fallback). KB **provisoire**. Énergie **non codée**
(volontaire). Le code ne produit **aucun signal réel** tant que la KB n'est pas reconstruite et les paramètres
non backtestés. Commit final des Phases 1-9 **en attente** (confirmation `py_compile risk_manager` + `git push`).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| Audit stratégie 8 marchés vs projet | 5 conflits identifiés vs décisions verrouillées | — | ✅ |
| Prompt Claude Code équipe d'agents | `PROMPT_CLAUDE_CODE_EQUIPE_AGENTS_TRADEX.md` (A1+C4, 10 agents, défiance doc) | 96e9bbe | ✅ |
| MAJ CLAUDE.md score /10 | 17/21 remplacé par grille /10 (D2) | 96e9bbe | ✅ |
| Phase 1 — 10 agents + registre A9 | `.claude/agents/` + `REGISTRE_VALIDITE.md` | 28eca06 | ✅ |
| Phase 2 — data/ complété | `risk_state.json` + `signal_history.json` | 28eca06 | ✅ |
| Phase 3 — formules Belkhayate | `belkhayate_formulas.py` (COG+Timing, Énergie stub) — 8 tests | 28eca06 | ✅ |
| Phase 4 — moteur signal | `signal_engine.py` (Étape 0, score /10, R8-R10) — 16 tests | 28eca06 | ✅ |
| Phase 5 — garde-fous runtime | `risk_manager.py` + `circuit_breaker.py` — 21 tests | en attente | ✅ |
| Phase 6 — cerveau Claude | `claude_brain.py` (fallback /10, ≤65%, KB provisoire) — 13 tests | en attente | ✅ |
| Phase 7 — backend API | `api/` FastAPI 127.0.0.1 + SQLite — 10 tests | en attente | ✅ |
| Phase 8 — frontend | `frontend/` Vite+React 18+Tailwind 3.4 — build OK | en attente | ✅ |
| Phase 9 — QA/audit | `RAPPORT_QA_TRADEX_PHASE9.md` — conformité 15/15 | en attente | ✅ |

---

## 3. MISSION SUIVANTE

1. **Confirmer + commit final + `git push`** (Phases 5-9 encore en working tree).
2. **Phase B-02** : reconstruction de la KB depuis les **vrais transcripts Whisper** (en cours, multi-sources).
3. **Valider l'Énergie** Belkhayate depuis les transcripts réels (aujourd'hui stub `NotImplementedError`).
4. **Backtester** les paramètres COG (`lookback_N` 100-125 vs 250, degré 2 vs 3) + seuils grille /10.
5. **Phase C** : collecteurs data NT8/ATAS (créer `cot_data.json` etc.).
6. **Phase E** : créer `prompt_builder.py` (chemin Claude réel — aujourd'hui toujours en fallback).

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| S07-1 | Stratégie « 8 marchés » : 5 conflits tranchés EN FAVEUR des décisions verrouillées (JSON NT8, GC/HG/CL/ZW+DX/ES/VX, MBT/6J zéro ordre, news 30 min, 3/4+2/3) | 🔒 |
| S07-2 | Score signal = /10 ; CLAUDE.md synchronisé (17/21 supprimé) ; 7 cercles = sources d'intelligence | 🔒 |
| S07-3 | Énergie Belkhayate = [NON DOCUMENTÉ] → NON codée, stub. Ni MFI ni proxy ATR prouvés | 🔒 |
| S07-4 | GUIDE MAÎTRE = ⚠️ DOUTEUX (non sourcé, coeff 0.8618 vs 1.618, claims 80% invérifiables) | 🔒 |
| S07-5 | Défiance documentaire : aucun fichier cru par défaut ; A9 valide ; contenu non-Belkhayate = couche `enrichissements_externes` (provenance tracée, jamais attribuée à Belkhayate) | 🔒 |

---

## 5. DÉCISIONS TEMPORAIRES (à valider/backtester)

| # | Décision temporaire | Condition de levée |
|---|---|---|
| T1 | COG : couleur = signe de la pente à l'endpoint | Valider contre vrais transcripts |
| T2 | Timing : normalisation `((pos×2)−1)×10` | Valider contre vrais transcripts |
| T3 | COG : degré 2 par défaut (3 dispo), N=250 | Backtest walk-forward |
| T4 | Grille /10 : seuils 7,0 / 5,0, pondérations | Backtest |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🔴 P0 | KB invalide (synthèses NotebookLM) → reconstruire depuis Whisper avant tout signal réel | OUI (trading réel) |
| 🟡 P1 | `prompt_builder.py` absent → `get_signal` toujours en fallback (Phase E) | NON (Auto reste bloqué) |
| 🟡 P1 | Whisper toujours en cours (multi-sources) — transcripts arrivent | NON |
| 🟡 P1 | Formules COG/Timing [RECONSTRUCTION] non validées | OUI (trading réel) |
| 🟡 P2 | Collecteurs data NT8/ATAS absents (`cot_data.json`) → Phase C | NON |
| ⚪ Info | `py_compile risk_manager.py` : OK chez Abdelkrim (21 tests verts) ; vérificateur sandbox Cowork voyait une version tronquée (décalage de montage) — à reconfirmer avant commit | NON |
| 🟡 P1 | **Docs incohérents** (audit S07) : MASTER_TRADEX_AI_v2, AGENTS.md, GARDE_FOUS, APPORTS_GUIDE_EXTERNE, BACKLOG, MODULES, competence-intermarches, GUIDE MAÎTRE portent encore /21, Vision/screenshot, 5/8 ou 0,8618 → passe de nettoyage PRIORITAIRE S08 (corriger ou archiver) | NON (CLAUDE.md a priorité) |

---

## 7. STACK TECHNIQUE GELÉE

```
Plateforme trading  : NinjaTrader 8 (port 36973 ATI)
Backend             : Python 3.11 + FastAPI 0.136 + uvicorn 0.49 (127.0.0.1 strict)
Frontend            : Vite 5 + React 18.3 + Tailwind 3.4
DB                  : SQLite (data/tradex.db)
Cerveau IA          : Claude API claude-sonnet-4-6 (prompt caching persistent)
OS                  : Windows 11 + PowerShell
Actifs : TRADING GC/HG/CL/ZW · CONFIRMATION DX/ES/VX · RÉFÉRENCE (zéro ordre) MBT/6J
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Commits poussés/faits : 96e9bbe (docs energie + guide douteux) ; 28eca06 (agents + phases 1-4)
En attente            : commit final Phases 5-9 (ajout ciblé) + git push
.env                  : ignoré (git check-ignore .env ✅) ; aucune clé API en dur (os.getenv)
node_modules/ + dist/ : gitignorés
```

---

## 9. COMMANDES GIT (PowerShell — jamais &&)

```powershell
cd C:\trading-copilote
py -m py_compile 05-saas\engine\risk_manager.py
git add .claude/agents/ 00-pilotage/REGISTRE_VALIDITE.md 00-pilotage/RAPPORT_QA_TRADEX_PHASE9.md 00-pilotage/_context/README_TRANSITION_TRADEX_S07_20260614.md data/risk_state.json data/signal_history.json 05-saas/engine/ 05-saas/api/ 05-saas/frontend/
git commit -m "feat(tradex): equipe agents app trading locale phase initiale terminee"
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE (S08)

1. Lire `CLAUDE.md` EN ENTIER (score /10 à jour)
2. Lire CE fichier (`README_TRANSITION_TRADEX_S07_20260614.md`)
3. Lire `00-pilotage\REGISTRE_VALIDITE.md` (statuts de fiabilité)
4. Vérifier état Whisper (X/110) + nouveaux transcripts arrivés
5. Confirmer que le commit final Phases 5-9 est bien poussé
6. Choisir : Phase B-02 (reconstruction KB) ou Phase C (collecteurs data)

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « Je reprends TRADEX-AI session S08. Lis CLAUDE.md + README_TRANSITION_TRADEX_S07_20260614.md + REGISTRE_VALIDITE.md. Décisions verrouillées : JSON NT8, port 36973, BTC/Yen = référence zéro ordre, score /10, précondition 3/4+2/3, Énergie non codée, mode AUTO bloqué, KB provisoire. L'app (9 phases, 68 tests verts) est commitée. **PRIORITÉ S08 — passe de nettoyage de cohérence** : corriger ou archiver les docs qui portent encore des règles abandonnées — `docs/MASTER_TRADEX_AI_v2.md` et `AGENTS.md` (Vision/screenshot + score /21), `GARDE_FOUS_PROPOSES.md`, `docs/APPORTS_GUIDE_EXTERNE.md`, `BACKLOG_ENRICHISSEMENTS.md` (score /21), `docs/MODULES.md` (Vision/screenshot), `competence-intermarches.txt` (5/8), `GUIDE MAÎTRE` (coeff 0,8618) → aligner sur /10, JSON NT8, 3/4+2/3 ou déplacer vers `_archive\`, puis mettre à jour `REGISTRE_VALIDITE.md`. Whisper est [terminé X/110 / en cours à X/110]. Ensuite je veux démarrer [Phase B-02 reconstruction KB / Phase C collecteurs data]. »

---

*README_TRANSITION_TRADEX_S07_20260614.md — fin session S07*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
