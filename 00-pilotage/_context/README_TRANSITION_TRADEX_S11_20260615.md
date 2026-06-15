# README DE TRANSITION — TRADEX-AI
**Date :** 15/06/2026 | **Session :** S11 | **Mode :** Cowork (orchestration) + Claude Code (exécution)

---

## 1. ÉTAT ACTUEL DU PROJET

KB canonique **1 265 règles** (post B-06) · 40 VALIDE / 1 225 DOUTEUX · **0 A_VERIFIER restant** sur les 110 transcrits Belkhayate · `kb_provisoire = False` · mode AUTO toujours **bloqué** (fallback hardcodé) · COGParams **verrouillés** (180/3/0,618-1,618) — backtest daily non concluant (timeframe ≠ range bars) · Trading Geek **31/113** toujours en cours.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| COG backtest hostile GC/HG/ZW | Script `cog_backtest.py` — 3 assets × 4 jeux de params — 180/3 non optimal sur daily (range bars requis) | `e45a0fe` | ✅ |
| Note NT8 Belkhayate | `docs\NOTE_INSTALLATION_NT8_BELKHAYATE.md` — Vidéo 2 (tuto install NT8/CQG mpfutur.com) documentée | `e718da5` | ✅ |
| B-06 intégration Vidéo 10 | 9 règles money management (psychologie ×5 + gestion_risque_entree ×4) → KB 1256→1265 | `c831af3` | ✅ |
| Clôture A_VERIFIER | MANIFESTE mis à jour (Vidéo 2 → HORS_PERIMETRE, Vidéo 10 → VALIDE) + REGISTRE_VALIDITE.md fermé | `a44c453` | ✅ |
| CLAUDE.md mis à jour | Section ÉTAT ACTUEL → S11 (KB 1265, 0 A_VERIFIER, COG backtest fait) | — | ✅ |

---

## 3. MISSION SUIVANTE

1. **Vérifier Trading Geek** : `(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\*.txt").Count` — doit atteindre 113.
2. **Si 113/113** → lancer Phase A (audit hostile + classification CONVERGENT/COMPLÉMENTAIRE/CONTRADICTOIRE vs Belkhayate).
3. **Si < 113** → préparer Phase C : architecture collecteurs NT8/ATAS (dossier `data\` inexistant — dette technique item 3).
4. **Énergie Belkhayate** : toujours bloquée — attendre Trading Geek pour trancher MFI 20/80 vs proxy ATR.

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| S11-1 | COGParams 180/3/0,618-1,618 **restent verrouillés** — test daily invalide pour trancher (timeframe ≠ range bars 5 ticks) | 🔒 |
| S11-2 | Ne pas relancer le test avec bande 1,618 seule — ne corrige pas le problème racine | 🔒 |
| S11-3 | Vraie validation COG = données NT8 range bars 5 ticks — à faire Phase C uniquement | 🔒 |
| S11-4 | 100/3 = piste à tester sur bon timeframe — pas une décision, juste une piste | 🔒 |
| S11-5 | Vidéo 2 → HORS_PÉRIMÈTRE (tuto installation NT8, pas de règles trading) | 🔒 |
| S11-6 | Vidéo 10 → VALIDE — 9 règles intégrées KB directement (B-06, source officielle vérifiée manuellement) | 🔒 |
| S11-7 | 0 A_VERIFIER restant — tous les 110 transcrits Belkhayate sont traités | 🔒 |

---

## 5. DÉCISIONS TEMPORAIRES (à valider)

| # | Décision temporaire | Condition de levée |
|---|---|---|
| T1 | 1 225 DOUTEUX conservés non relus | Relecture ciblée future (par catégorie) |
| T2 | COG defaults confirmés CL seulement | Backtest sur range bars NT8 (Phase C) |
| T3 | Énergie non codée (stub) — conflit MFI vs ATR non tranché | Transcrits Trading Geek + décision explicite |
| T4 | Phase A Trading Geek en attente | Fin transcription 113/113 |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🟡 P1 | Énergie non codée — conflit MFI 20/80 vs proxy ATR | OUI (signal réel) |
| 🟡 P1 | COG validé CL seulement — range bars NT8 requis pour GC/HG/ZW | OUI (signal réel) |
| 🟡 P2 | 1 225 DOUTEUX non relus | NON (bloquant progressif) |
| 🟡 P2 | Trading Geek Phase A — audit hostile | NON (en cours background) |
| ⚪ Info | Trading Geek 31/113 au moment de la clôture S11 | NON |
| ⚪ Info | Dette technique item 3 : dossier `data\` inexistant | NON (Phase C) |

---

## 7. STACK TECHNIQUE GELÉE

NinjaTrader 8 (JSON, port ATI 36973) · ATAS Pro/Rithmic · Claude **claude-sonnet-4-6** (KB + signaux) · Python 3.11 + FastAPI · React 18 + Vite + Tailwind 3.4 · SQLite · Windows 11 + PowerShell 7.6.2 · Transcription = Whisper local (modèle turbo) · prompt caching sur KB.

---

## 8. ÉTAT DES REPOS FIN SESSION

```
HEAD               : a44c453 (docs(registre): clos A_VERIFIER video2 HORS_PERIMETRE video10 VALIDE)
Commits S11        : e45a0fe · e718da5 · c831af3 · a44c453 (4 commits)
KB                 : 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json · 1 265 règles · JSON valide
Nouveaux fichiers  : 05-saas/engine/cog_backtest.py · cog_backtest_results.csv · cog_backtest_rapport.md
                     00-pilotage/docs/NOTE_INSTALLATION_NT8_BELKHAYATE.md
                     05-saas/knowledge_base/b06_add_video10.py
Trading Geek       : audio (~113 MP3) + 31 transcripts → ignorés via .gitignore
RAPPEL             : ne JAMAIS faire git add . — toujours git add ciblé
```

---

## 9. COMMANDES GIT (PowerShell — une par une, JAMAIS &&)

(Session déjà poussée — HEAD = a44c453 sur origin/main.)

```powershell
cd C:\trading-copilote
```
```powershell
git add 00-pilotage\_context\README_TRANSITION_TRADEX_S11_20260615.md
```
```powershell
git add CLAUDE.md
```
```powershell
git commit -m "docs(session): readme transition s11 + claude.md mis a jour"
```
```powershell
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE (S12)

1. Lire `CLAUDE.md` EN ENTIER.
2. Lire ce fichier (`README_TRANSITION_TRADEX_S11_20260615.md`).
3. Lire `00-pilotage\REGISTRE_VALIDITE.md`.
4. Vérifier Trading Geek : `(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\*.txt").Count`
5. Si 113 → Phase A (audit hostile Trading Geek).
6. Si < 113 → Phase C (architecture collecteurs NT8 — créer dossier `data\`).

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « Je reprends TRADEX-AI session S12. Lis CLAUDE.md + README_TRANSITION_TRADEX_S11_20260615.md + REGISTRE_VALIDITE.md.
> Règle de rôle : Cowork orchestre, Claude Code exécute.
> ÉTAT FIN S11 (HEAD=origin/main=a44c453) : KB 1 265 règles · 0 A_VERIFIER · COGParams verrouillés · Trading Geek 31/113 en cours.
> Priorité S12 : (1) vérifier fin transcription Trading Geek → Phase A si 113/113 ; (2) sinon Phase C collecteurs NT8 (créer dossier data\). »

---

*README_TRANSITION_TRADEX_S11_20260615.md — fin session S11*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
