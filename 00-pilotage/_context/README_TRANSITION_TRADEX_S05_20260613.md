# README DE TRANSITION — TRADEX-AI
**Date** : 13/06/2026 | **Session** : S05 | **Projet** : trading-copilote

---

## 1. ÉTAT ACTUEL DU PROJET

Phase B en cours — KB Belkhayate rebuild depuis zéro.
Transcription Whisper des 110 vidéos @MostafaBelkhayate en cours (dernier état connu : ~36/110 transcrites, script 02_transcribe_whisper.ps1 relancé après interruption).
Décisions d'architecture C2 (JSON) et C3 (FastAPI) définitivement verrouillées et auditées.
Mode AUTO : BLOQUÉ. Code SaaS dans 05-saas\ : stable.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Comparaison architecture C2 | Screenshot NT8 vs JSON — analyse détaillée + reco | — | ✅ DÉCISION PRISE |
| Comparaison stack C3 | NestJS vs FastAPI — analyse détaillée + reco | — | ✅ DÉCISION PRISE |
| Audit architecture codebase | Prompt Claude Code — 6 points vérifiés dans le code réel | — | ✅ 6/6 OUI |
| Validation architecture | JSON + FastAPI confirmés sans régression depuis le README parallèle | — | ✅ VERROUILLÉ |

---

## 3. MISSION SUIVANTE

**Phase B — Deux options au choix d'Abdelkrim :**

**Option A (passive)** : Attendre fin Whisper → récupérer `AUDIT_QUALITE.md` → le partager → extraction KB Phase B-02.

**Option B (active)** : Démarrer Phase B-01 en parallèle — Academia.edu PDF "belkhayate gravity center" + Pine Script TradingView → coder `05-saas\engine\belkhayate_formulas.py`.

---

## 4. DÉCISIONS PRISES (VERROUILLÉES)

| # | Décision | Statut |
|---|----------|--------|
| C1 | Mode Auto via NT8 ATI port 36973 (confiance ≥ 85%) | ✅ GARDÉ |
| C2 | Architecture données : JSON fichiers locaux (PAS screenshot, PAS Vision API) | ✅ VERROUILLÉ |
| C3 | Backend : FastAPI Python (PAS NestJS, PAS TypeScript) | ✅ VERROUILLÉ |
| — | README parallèle (autre session claude.ai) ignoré pour C2/C3 — CLAUDE.md fait autorité | ✅ CONFIRMÉ |

---

## 5. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité | Action |
|---|----------|----------|--------|
| 1 | Transcription Whisper interrompue (PC en veille) | HAUTE | Relancer `.\02_transcribe_whisper.ps1` si pas terminée — script SKIP les fichiers déjà faits |
| 2 | GARDE_FOUS_PROPOSES.md ligne 19 | MOYENNE | "Ces 20 garde-fous sont présents dans le code et opérationnels" → reformuler via Claude Code |
| 3 | Branche Git (master vs main) | FAIBLE | Vérifier `git branch` — une session parallèle a pu changer la branche |
| 4 | KB Belkhayate INVALIDE | CRITIQUE | Toutes les sources existantes sont AI-generated — rebuild Phase B obligatoire |

---

## 6. PIPELINE WHISPER — ÉTAT

```
Script       : 02_transcribe_whisper.ps1
Modèle       : turbo | Langue : fr | Dernier état : ~36/110 transcrites
Comportement : SKIP automatique des fichiers déjà transcrits (Test-Path)
Relance      : .\02_transcribe_whisper.ps1 (sans risque de doublon)
Fin de script: lance 03_audit_qualite.py → génère AUDIT_QUALITE.md

Chemin audio     : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio\
Chemin transcripts: C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\
Chemin rapport   : C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\AUDIT_QUALITE.md
```

---

## 7. STACK TECHNIQUE GELÉE

```
Plateforme trading  : NinjaTrader 8 (Windows local)
Order flow          : ATAS Pro (connecté Rithmic)
Backend local       : Python 3.11 + FastAPI                ← VERROUILLÉ S05
Données NT8         : JSON fichiers locaux (pas screenshot) ← VERROUILLÉ S05
Exécution ordres    : NinjaTrader 8 ATI port 36973
Cerveau IA          : Claude API claude-sonnet-4-6
Transcription       : OpenAI Whisper turbo (local CPU)
Download audio      : yt-dlp
OS                  : Windows 11 + PowerShell 7.6.2
```

---

## 8. FICHIERS CLÉS À CONNAÎTRE

| Fichier | Rôle |
|---------|------|
| `C:\trading-copilote\CLAUDE.md` | Source de vérité absolue |
| `C:\trading-copilote\00-pilotage\FEUILLE_DE_ROUTE.md` | Phases A→K + état Phase B |
| `C:\trading-copilote\00-pilotage\GARDE_FOUS_PROPOSES.md` | 32 garde-fous (ligne 19 à corriger) |
| `C:\trading-copilote\05-saas\config\settings.py` | Actifs, NT8 ATI port 36973, seuils |
| `C:\trading-copilote\05-saas\engine\data_reader.py` | Lecture JSON/CSV NT8 + ATAS |
| `C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\` | Pipeline Whisper complet |

---

## 9. COMMANDES GIT (PowerShell — jamais &&)

```powershell
cd C:\trading-copilote
git add .
git commit -m "docs(session): README transition S05 + decisions C2 C3 verouillees"
git push origin main
```

Avant le push, vérifier :
```powershell
git check-ignore C:\trading-copilote\.env
git branch
```

---

## 10. PRE-FLIGHT SESSION S06

1. Lire `CLAUDE.md` en entier
2. Lire ce fichier (`README_TRANSITION_TRADEX_S05_20260613.md`)
3. Vérifier si Whisper a terminé : `ls C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\ | Measure-Object`
4. Si AUDIT_QUALITE.md existe → le partager dans la conversation
5. Annoncer : "📍 État : Phase B en cours, Whisper [X/110] — Prochaine action : [A ou B]"

---

## 11. PHRASE D'AMORÇAGE SESSION S06

```
Je reprends TRADEX-AI session S06. Lis CLAUDE.md + README_TRANSITION_TRADEX_S05_20260613.md.
Whisper est [terminé / toujours en cours à X/110].
[Si terminé : voici le rapport AUDIT_QUALITE.md : [coller contenu]]
Décisions verrouillées : JSON (pas screenshot) + FastAPI (pas NestJS) + port 36973.
Prochaine action : [Option A : extraction KB depuis transcripts] ou [Option B : B-01 Academia.edu + Pine Script]
```

---

*README généré par Cowork — Session S05 — 13/06/2026*
