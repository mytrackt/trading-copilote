# README DE TRANSITION — TRADEX-AI
**Date :** 15/06/2026 | **Session :** S10 | **Mode :** Cowork (orchestration) + Claude Code (exécution)

---

## 1. ÉTAT ACTUEL DU PROJET

KB canonique **1 256 règles** (post-purge B-04) · `kb_provisoire = False` (levé B-05) · mode AUTO toujours **bloqué** (fallback hardcodé `mode_auto_autorise=False`) · transcription "The Trading Geek" **en cours** (~29/113 au moment de la clôture) · énergie toujours **non codée** · COG confirmé pétrole seulement.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| Nettoyage git | reset HEAD~1 · .gitignore (audio/MP3/bak/settings) · git rm --cached · push propre | `6ae1c83` `faf496b` | ✅ |
| B-03 audit KB | 1 461 règles auditées · claude-sonnet-4-6 · $1.89 · 29 VALIDE / 1228 DOUTEUX / 165 INVALIDE / 39 DOUBLON | `04269cc` | ✅ |
| B-04 purge KB | 204 règles supprimées (INVALIDE + DOUBLON) → 1 256 règles propres | `5e8c8d6` | ✅ |
| B-05 lever kb_provisoire | Validation 5% (7,9% désaccord · seuil OK) · #8 supprimée · #29/#60 → VALIDE · `KB_PROVISOIRE_DEFAUT = False` · 14/14 tests verts | `9c337e4` | ✅ |
| Fix python → py | `02_transcribe_whisper.ps1:49` + `transcript_processor.py:16-17` | `2a122de` | ✅ |

---

## 3. MISSION SUIVANTE

1. **Attendre fin transcription Trading Geek** (~84 vidéos restantes, plusieurs heures) → vérifier `03-transcriptions/nouvelles-sources/The Trading Geek/transcripts/*.txt` (doit atteindre 113).
2. **Phase A** : audit hostile + classification de chaque transcript Trading Geek (CONVERGENT / COMPLÉMENTAIRE / CONTRADICTOIRE face à Belkhayate).
3. **COG backtest** GC/HG/ZW : params (période 180 / ordre 3 / ×0,618-1,618) confirmés CL seulement → backtester les 3 actifs restants.
4. **Énergie Belkhayate** : conflit MFI 20/80 vs proxy ATR — trancher après Trading Geek (attendre transcrits EN).

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| S10-1 | `KB_PROVISOIRE_DEFAUT = False` dans `claude_brain.py` (seul vrai flag moteur — ni `settings.py` ni `processor_status.json`) | 🔒 |
| S10-2 | 84% DOUTEUX = **conservés** : le prompt hostile était délibérément sévère ("préfère DOUTEUX si <90% certain") — DOUTEUX ≠ mauvais, seulement non vérifiable contre whitelist étroite | 🔒 |
| S10-3 | Mode AUTO reste bloqué par fallback hardcodé même après levée de `kb_provisoire` — aucun déverrouillage auto | 🔒 |
| S10-4 | Sweep global `python → py` sur tout le repo = **NON fait** : les appels `python` dans Claude Code sandbox (Linux) sont intentionnels | 🔒 |
| S10-5 | Audio MP3 Trading Geek + `.bak.json` + `.claude/settings.json` exclus de git via `.gitignore` | 🔒 |

---

## 5. DÉCISIONS TEMPORAIRES (à valider)

| # | Décision temporaire | Condition de levée |
|---|---|---|
| T1 | 1 225 DOUTEUX conservés non relus | Relecture ciblée future (par catégorie, pas en masse) |
| T2 | COG defaults confirmés CL seulement | Backtest GC / HG / ZW |
| T3 | Énergie non codée (stub) — conflit MFI vs ATR non tranché | Transcrits Trading Geek + décision explicite |
| T4 | Phase A Trading Geek en attente | Fin transcription 113/113 |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🟡 P1 | Énergie non codée — conflit MFI 20/80 vs proxy ATR | OUI (signal réel) |
| 🟡 P1 | COG params confirmés CL seulement | OUI (signal réel GC/HG/ZW) |
| 🟡 P2 | 1 225 DOUTEUX non relus — base de signaux à affiner | NON (bloquant progressif) |
| 🟡 P2 | Trading Geek Phase A audit | NON (en cours en background) |
| ⚪ Info | Trading Geek transcription ~29/113 au moment de la clôture S10 | NON |
| ⚪ Info | 2 transcrits Belkhayate A_VERIFIER (Video 1, Video 2) non intégrés KB | NON |

---

## 7. STACK TECHNIQUE GELÉE

NinjaTrader 8 (JSON, port ATI 36973) · ATAS Pro/Rithmic · Claude **claude-sonnet-4-6** (KB + signaux) · Python 3.11 + FastAPI · React 18 + Vite + Tailwind 3.4 · SQLite · Windows 11 + PowerShell 7.6.2 · Transcription = Whisper local (modèle turbo) · prompt caching sur KB.

---

## 8. ÉTAT DES REPOS FIN SESSION

```
HEAD               : 2a122de (fix(scripts): python vers py Windows launcher) — poussé sur origin/main
Commits S10        : 6ae1c83 · faf496b · 04269cc · 5e8c8d6 · 9c337e4 · 2a122de (6 commits)
Working tree       : 110 transcrits Belkhayate untracked (non commités, non ignorés, intentionnel)
                     Trading Geek audio (~113 MP3) + transcripts en cours → ignorés via .gitignore
KB                 : 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json · 1 256 règles · JSON valide (null bytes purgés)
Artefacts audit    : AUDIT_KB_RESULTS.json · AUDIT_KB_RAPPORT_20260614_2316.md · PURGE_KB_LOG_20260614_2323.md
.env               : ignoré · aucune clé API en dur (os.getenv)
RAPPEL             : ne JAMAIS faire git add . — toujours git add ciblé
```

---

## 9. COMMANDES GIT (PowerShell — une par une, JAMAIS &&)

(Session déjà poussée. Commandes ci-dessous = pour committer ce README.)

```powershell
cd C:\trading-copilote
```
```powershell
git add 00-pilotage\_context\README_TRANSITION_TRADEX_S10_20260615.md
```
```powershell
git commit -m "docs(session): readme transition s10"
```
```powershell
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE (S11)

1. Lire `CLAUDE.md` EN ENTIER.
2. Lire ce fichier (`README_TRANSITION_TRADEX_S10_20260615.md`).
3. Lire `00-pilotage\REGISTRE_VALIDITE.md`.
4. Vérifier nb transcrits Trading Geek : `(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\*.txt").Count` — doit être 113.
5. Si 113 → lancer Phase A (audit hostile Trading Geek).
6. Sinon → lancer COG backtest GC/HG/ZW (ne dépend pas de Trading Geek).

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « Je reprends TRADEX-AI session S11. Lis CLAUDE.md + README_TRANSITION_TRADEX_S10_20260615.md + REGISTRE_VALIDITE.md.
> Règle de rôle : Cowork orchestre, Claude Code exécute.
> ÉTAT FIN S10 (HEAD=origin/main=2a122de) : KB 1 256 règles · kb_provisoire LEVÉ (B-05) · mode AUTO bloqué (fallback hardcodé) · fix python→py fait · Trading Geek transcription ~29/113 en cours.
> Priorité S11 : (1) vérifier fin transcription Trading Geek → Phase A audit/classif si 113/113 ; (2) sinon COG backtest GC/HG/ZW ; (3) Énergie Belkhayate après Trading Geek. »

---

*README_TRANSITION_TRADEX_S10_20260615.md — fin session S10*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
