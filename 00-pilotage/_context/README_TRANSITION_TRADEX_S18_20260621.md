# README DE TRANSITION — TRADEX-AI
Date : 2026-06-21 | Session : S18 | KB : 1279 règles

---

## 1. ÉTAT ACTUEL DU PROJET

KB à 1279 règles (1265 → +14 Chap5 Belkhayate, pipeline complet Étapes 5→6→7).
Architecture Vision-Décision 5 couches intégrée à la roadmap (Phase L ajoutée après Phase K).
Couche 3 verrouillée : claude_brain.py + prompt caching (Mistral/ChromaDB abandonnés — 06_RAG inexistant).
Script Whisper local en cours : ~44 vidéos traitées sur 54 — reste ~10.
Phase C (NT8) toujours bloquée jusqu'à KB complète.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Architecture Vision-Décision | Phase L ajoutée roadmap, 5 couches documentées, Couche 3 corrigée Mistral→claude_brain.py | c850ea1 | ✅ |
| Archive TA101 3 fichiers | Fichiers StockCharts dans playbook/, ticket 0.o BACKLOG P1 | (inclus c850ea1) | ✅ |
| Ticket 0.b Chap5 — Étape 5 | 14 briques JSON fabriquées dans validation/ | 551c95e | ✅ |
| Ticket 0.b Chap5 — Étape 6 | Audit automatique : 14/14 VALIDE (100%) | ba63597 | ✅ |
| Ticket 0.b Chap5 — Étape 7 | Fusion : KB 1265 → 1279 règles — ticket 🟢 INTÉGRÉ | b9d3055 | ✅ |

---

## 3. MISSION SUIVANTE

**Priorité 1 — Interstice suivant** : traiter ticket `0.c` (Chap4 AT, P1) via PIPELINE_ENRICHISSEMENT_KB.md
→ Lire `02-sources-brutes\methode-belkhayate\TRADEX_KB_Chap4_AT.md` → proposer N briques → attendre OK

**Priorité 2 — Dès que Whisper terminé** : audit qualité des ~10 nouvelles transcriptions
→ Vérifier doublons (fichiers `7.txt` + `7-Episode mp4.txt` pour la même vidéo)
→ Pipeline KB pour les nouvelles transcriptions valides

**Priorité 3 (en attente)** : déplacer dossier `01-pipeline/` (scraper ChartSchool hors structure)

---

## 4. DÉCISIONS PRISES CETTE SESSION

| # | Décision | Portée |
|---|----------|--------|
| D1 | Couche 3 architecture = claude_brain.py + prompt caching (pas Mistral/ChromaDB) | VERROUILLÉE |
| D2 | 01-pipeline/ à déplacer : scraper.py → 01-moteur-transvideo/scripts/, bundles → 02-sources-brutes/playbook/stockcharts-bundles/ | En attente exécution |
| D3 | Phase L ajoutée à la roadmap (Vision-Décision 5 couches post-paper-trading) | Intégrée |
| D4 | Nouveau schéma KB : champs type/fiabilite/id_brique coexistent avec anciens champs (à uniformiser ultérieurement) | Dette acceptée |

---

## 5. DÉCISIONS TEMPORAIRES

| # | Décision | Condition de révision |
|---|----------|-----------------------|
| T1 | CLAUDE.md indique encore 1265 règles | Mettre à jour à 1279 en début de S19 |
| T2 | Hétérogénéité schéma KB (nouveaux champs vs anciens) | Uniformisation lors d'une mission dédiée |
| T3 | Script Whisper local en cours (~10 restantes) | Vérifier statut début S19 |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Problème | Priorité | Action |
|----------|----------|--------|
| Doublons Whisper : `7.txt` + `7-Episode mp4.txt` (même vidéo) | P2 | Vérifier + dédoublonner avant pipeline KB |
| 5 règles AMBIGU dans KB : #011, #014, #026, #031, #033 | P2 | Vérification manuelle vidéos source |
| 01-pipeline/ hors structure (scraper ChartSchool) | P2 | 3 commandes PowerShell (voir §9) |
| CLAUDE.md KB encore à 1265 | P1 | Mettre à jour ligne "KB" en début S19 |
| Phase C (NT8) bloquée | bloqué | Attend KB complète (transcriptions Whisper + tickets backlog) |

---

## 7. STACK TECHNIQUE GELÉE

```
Trading       : NinjaTrader 8 ATI — TCP/IP local port 36973
IA signaux    : claude-sonnet-4-6
IA vision     : claude-sonnet-4-20250514
KB Couche 3   : claude_brain.py + prompt caching sur KB JSON (PAS Mistral/ChromaDB)
Backend       : Python 3.11 + FastAPI
DB locale     : SQLite
OS            : Windows 11 — PowerShell 7.6.2
```

---

## 8. ÉTAT DES REPOS FIN SESSION

| Fichier | État |
|---------|------|
| KNOWLEDGE_BASE_MASTER.json | 1279 règles (1265 + 14 Chap5) — commit b9d3055 |
| FEUILLE_DE_ROUTE.md | Phase L ajoutée, 12 phases A→L — commit c850ea1 |
| BACKLOG_ENRICHISSEMENTS.md | Ticket 0.b 🟢 INTÉGRÉ — ticket 0.o 📥 À TRAITER (TA101) |
| 04-cerveau-trading/validation/KB_CHAP5_BELKHAYATE.json | 14 briques — conservées en validation |
| 04-cerveau-trading/validation/REGISTRE_VALIDITE.md | Audit + fusion documentés |
| 01-pipeline/ | ⚠️ Hors structure — à déplacer (non urgent) |
| Backup KB | KNOWLEDGE_BASE_MASTER.bak_chap5_20260620.json (local, non commité) |
| Scripts Whisper | En cours — ~10 vidéos restantes sur D:\Belkhayate-Videos\ |

Commits session S18 (chronologique) :
- `c850ea1` feat(roadmap): architecture vision-decision 5 couches + phase L
- `551c95e` feat(KB): ticket 0.b Chap5 Belkhayate 14 briques en validation
- `ba63597` feat(KB): audit ticket 0.b Chap5 - verdict VALIDE 14/14
- `b9d3055` feat(KB): integration ticket 0.b Chap5 Belkhayate 14 briques valide

---

## 9. COMMANDES EN ATTENTE (PowerShell — C:\trading-copilote)

**Déplacer 01-pipeline/ (priorité P2) :**
```powershell
Move-Item 01-pipeline\scraper.py 01-moteur-transvideo\scripts\chartschool_scraper.py
```
```powershell
Move-Item 01-pipeline\bundles\stockcharts 02-sources-brutes\playbook\stockcharts-bundles
```
```powershell
Remove-Item -Recurse -Force 01-pipeline
```
```powershell
git add .
```
```powershell
git commit -m "refactor: deplace scraper chartschool dans moteur-transvideo, bundles dans sources-brutes"
```

**Push en attente :**
```powershell
git push
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

```
[ ] 1. Lire CLAUDE.md EN ENTIER
[ ] 2. Lire ce README (README_TRANSITION_TRADEX_S18_20260621.md)
[ ] 3. Mettre à jour CLAUDE.md : KB 1265 → 1279 règles
[ ] 4. Vérifier si Whisper est terminé :
        ls 03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\ | wc -l
        (154 actuellement — si > 154, des vidéos supplémentaires ont été transcrites)
[ ] 5. Lire DETTE_TECHNIQUE.md
[ ] 6. Traiter ticket 0.c (Chap4 AT) — 1er interstice S19
```

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Je démarre la session S19 de TRADEX-AI.
Lis CLAUDE.md + README_TRANSITION_TRADEX_S18_20260621.md.
KB à 1279 règles (Chap5 Belkhayate intégré en S18 — pipeline 5→6→7 complet).
Actions immédiates :
1. Mettre à jour CLAUDE.md : KB 1265 → 1279
2. Vérifier si Whisper est terminé (54 vidéos locales)
3. Traiter ticket 0.c (Chap4 AT, P1) — interstice S19
Phase C (NT8) reste bloquée jusqu'à KB complète.
```

---

*README généré par Cowork — Session S18 · 2026-06-21*
*Prochaine session : S19 — Ticket 0.c Chap4 AT + vérif Whisper*
