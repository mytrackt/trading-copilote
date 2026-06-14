# README DE TRANSITION — TRADEX-AI
**Date :** 14/06/2026 | **Session :** S09 | **Mode :** Cowork (orchestration) + Claude Code (exécution)

---

## 1. ÉTAT ACTUEL DU PROJET

Phase **B-02 terminée et poussée** : KB canonique reconstruite depuis les 108 transcrits Belkhayate VALIDE.
`KNOWLEDGE_BASE_MASTER.json` = **108 vidéos / 1461 règles / modèle claude-sonnet-4-6** (remplace l'ancienne KB
provisoire 142 vidéos NotebookLM). En parallèle, transcription d'une chaîne externe **"The Trading Geek"**
(113 vidéos EN, Whisper local) **en cours** pour future couche d'enrichissement. Mode AUTO toujours **bloqué**,
KB toujours **provisoire** (1461 règles non relues), Énergie toujours **non codée**.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| Recon + design B-02 | Recon lecture seule `transcript_processor.py` + manifeste ; design + estimation coût | — | ✅ |
| Prompt Claude Code B-02 | Prompt complet (6 modifs, archive, run, rollback) | — | ✅ |
| Rebuild KB B-02 | KB 108 vidéos / 1461 règles / sonnet-4-6 ; bug `extract_video_id` corrigé (préfixe 11 car.) | **d5bc721** | ✅ poussé |
| Pipeline transcription Trading Geek | 113 URLs nettoyées + `01_download_audio.ps1` + `02_transcribe_whisper.ps1` (`--language en`) | — | ✅ lancé |

---

## 3. MISSION SUIVANTE

1. **Fin transcription "The Trading Geek"** (113 vidéos) → **Phase A** : audit hostile + classification de chaque transcript (CONVERGENT / COMPLÉMENTAIRE / CONTRADICTOIRE face à Belkhayate).
2. **Relecture des 1461 règles** de la KB → lever `kb_provisoire=True`.
3. **Énergie Belkhayate** : valider/coder depuis transcrits (conflit MFI 20/80 vs proxy ATR non tranché).
4. **Backtester params COG** (période 180 / ordre 3 / 0,618-1,618) sur GC/HG/ZW (confirmés pétrole seulement).
5. **Missions versioning + bug `py`** : décider du versioning des transcrits bruts ; corriger les scripts/hook appelant `python` au lieu de `py`.

---

## 4. DÉCISIONS PRISES CETTE SESSION (verrouillées)

| # | Décision | Statut |
|---|---|---|
| S09-1 | Rebuild KB = modèle **claude-sonnet-4-6**, périmètre **108 VALIDE** (2 A_VERIFIER exclus via manifeste), ancienne KB archivée + KB repartie vierge, prompt caching system | 🔒 |
| S09-2 | `extract_video_id` = **préfixe 11 caractères** (PAS `split('_',1)` : les IDs YouTube contiennent `_` ; 6 commencent par `_`) | 🔒 |
| S09-3 | Chaîne externe "The Trading Geek" = couche **`enrichissements_externes`**, JAMAIS versée dans la KB Belkhayate ni attribuée à Belkhayate ; sert de confirmation/contexte seulement | 🔒 |
| S09-4 | Objectif enrichissement = **rigoureux, audité, traçable** (le mot « infaillible » est rejeté ; aucune promesse de gain) ; audit Phase A obligatoire avant intégration | 🔒 |
| S09-5 | Transcription toujours **dans la langue de la vidéo** (`en` pour Trading Geek, `fr` pour Belkhayate) | 🔒 |

---

## 5. DÉCISIONS TEMPORAIRES (à valider/backtester)

| # | Décision temporaire | Condition de levée |
|---|---|---|
| T1 | KB 1461 règles = **provisoire** (`kb_provisoire=True`) | Relecture qualité des règles |
| T2 | COG defaults (180/ordre 3/0,618-1,618) = confirmés PÉTROLE | Backtest GC/HG/ZW |
| T3 | 2 transcrits Belkhayate A_VERIFIER (`enG01BznN_M` Vidéo 1, `StGyS6POO_Q` Vidéo 2) exclus | Vérif manuelle avant éventuelle intégration |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Bloquant ? |
|---|---|---|
| 🟡 P1 | KB 1461 règles non relues → KB provisoire, mode AUTO interdit | OUI (signal réel) |
| 🟡 P1 | Énergie non codée (conflit MFI vs proxy ATR) | OUI (signal réel) |
| 🟡 P1 | Params COG confirmés pétrole seulement | OUI (signal réel) |
| 🟡 P2 | Bug `python` vs `py` : l'audit auto du script transcription plante (`Python est introuvable`) | NON |
| ⚪ Info | Transcrits bruts untracked (110 Belkhayate + Trading Geek audio/transcripts) + `.claude/settings.json` | NON |
| ⚪ Info | Transcription "The Trading Geek" en cours (113 vidéos, plusieurs heures) | NON |

---

## 7. STACK TECHNIQUE GELÉE

NinjaTrader 8 (JSON, port ATI 36973) · ATAS Pro/Rithmic · Claude **claude-sonnet-4-6** (KB + signaux) ·
Python 3.11 + FastAPI · React 18 + Vite + Tailwind 3.4 · SQLite · Windows 11 + PowerShell 7.6.2 ·
Transcription = Whisper local (modèle turbo) · prompt caching sur KB.

---

## 8. ÉTAT DES REPOS FIN SESSION

```
HEAD               : d5bc721 (feat kb: phase b-02 rebuild) — poussé sur origin/main
Commits en attente : aucun (main...origin/main, 0 ahead)
Working tree       : 110 transcrits Belkhayate untracked + The Trading Geek (audio 3,9 Go + transcripts) untracked
                     + .claude/settings.json modifié + KB .bak hors versioning (.notebooklm / .broken_103)
                     + ce README S09 (nouveau, à committer)
.env               : ignoré ; aucune clé API en dur (os.getenv)
RAPPEL             : ne JAMAIS faire git add . — toujours git add ciblé
```

---

## 9. COMMANDES GIT (PowerShell — une par une, JAMAIS &&)

(Session déjà poussée. Commandes ci-dessous = pour committer ce README.)

```
cd C:\trading-copilote
```
```
git add 00-pilotage\_context\README_TRANSITION_TRADEX_S09_20260614.md
```
```
git commit -m "docs(session): readme transition s09"
```
```
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE (S10)

1. Lire `CLAUDE.md` EN ENTIER (score /10, décisions verrouillées).
2. Lire ce fichier (`README_TRANSITION_TRADEX_S09_20260614.md`).
3. Lire `00-pilotage\REGISTRE_VALIDITE.md`.
4. Vérifier l'avancement de la transcription "The Trading Geek" (`transcripts/` *.txt sur 113).
5. Décider : Phase A (audit externe) si transcription finie, OU relecture des 1461 règles KB.

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

> « Je reprends TRADEX-AI session S10. Lis CLAUDE.md + README_TRANSITION_TRADEX_S09_20260614.md + REGISTRE_VALIDITE.md.
> Règle de rôle : Cowork orchestre et n'édite aucun fichier → produit des prompts ; Claude Code exécute (05-saas/ toujours via Claude Code).
> Décisions verrouillées : JSON NT8, port 36973, BTC(MBT)/Yen(6J) = référence zéro ordre, score /10 seuil 7,0 (D2),
> précondition 3/4 trading + 2/3 confirmation, Énergie non codée (stub), mode AUTO bloqué, KB provisoire (kb_provisoire=True).
> ÉTAT FIN S09 (HEAD=origin/main=d5bc721) : Phase B-02 FAITE — KB canonique 108 vidéos / 1461 règles / claude-sonnet-4-6
> (bug extract_video_id corrigé = préfixe 11 car. ; anciennes KB archivées hors git). Transcription externe "The Trading Geek"
> (113 vidéos EN, Whisper local) lancée → couche enrichissements_externes, jamais dans la KB Belkhayate, Phase A audit avant intégration.
> Ordre des missions S10 : (1) fin transcription Trading Geek → Phase A audit/classif ; (2) relecture des 1461 règles → lever provisoire ;
> (3) Énergie depuis transcrits ; (4) backtest COG GC/HG/ZW ; (5) versioning transcrits bruts + correction bug python/py. »

---

*README_TRANSITION_TRADEX_S09_20260614.md — fin session S09*
*Source de vérité : CLAUDE.md — En cas de conflit, CLAUDE.md a priorité*
