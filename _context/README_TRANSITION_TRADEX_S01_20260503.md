# README DE TRANSITION — TRADEX AI
**Date** : 03 Mai 2026 | **Session** : S01 | **Score projet** : 45/100 (Phase A terminée)

---

## ÉTAT ACTUEL DU PROJET

TradEx AI est un SaaS Desktop Trading assisté par IA Claude, en cours de construction.
Phase A (documentation fondatrice) officiellement terminée et poussée sur GitHub.
Le projet n'a pas encore de code frontend ni de dashboard — uniquement la documentation
stratégique et les fichiers de configuration backend existants.
Prochaine étape recommandée : Z → Y → X (MAJ CLAUDE.md → Réorganisation → Phase B).

---

## MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| Backup Phase 0 | Backup 913 MB + .gitignore enrichi | `6e24070` | ✅ |
| Audit workspace | Belkhayate vérifié (14 mentions), 142 transcripts lus | Phase 1-Light | ✅ |
| Risk Engine validation | 12 paramètres audités, 2 corrections settings.py | Phase 4-Light | ✅ |
| GARDE_FOUS_PROPOSES.md | 32 garde-fous (20 actifs + 10 manquants + 2 partiels) | `9f31edd` | ✅ |
| FEUILLE_DE_ROUTE.md | 11 phases A→K de construction du SaaS | `9f31edd` | ✅ |
| CHECKLIST_FICHIERS_INUTILES.md | 29 items, ~402 MB récupérables | `2fd06ba` | ✅ |
| RAPPORT_REORGANISATION.md | Plan réorg : 28 fichiers → 6 fichiers à la racine | `2fd06ba` | ✅ |
| Briefing fin Phase A | 9 sections, 290 lignes | `95c2e8f` | ✅ |
| Briefing fin session | Journée complète documentée | `4edaccf` | ✅ |

---

## MISSION SUIVANTE (ordre recommandé Z → Y → X)

### Z — Mettre à jour CLAUDE.md (priorité absolue)
Corriger les 2 chemins inexistants dans CLAUDE.md :
- `code/scraper/` → n'existe pas (transcripts dans `04-kb-sources/youtube-a-scraper/transcripts/`)
- `code/transcripts/` → n'existe pas
- Mettre à jour la section ÉTAT ACTUEL (Phase A done)

### Y — Réorganisation workspace
Exécuter le plan de `RAPPORT_REORGANISATION.md` :
- Supprimer `.tmp.driveupload/` (~400 MB)
- Créer 6 groupes G1→G6
- Passer de 28 fichiers / 22 dossiers à 6 fichiers / 14 dossiers à la racine

### X — Phase B : KB Belkhayate
Extraire les règles Belkhayate depuis 142 transcripts → JSON structuré
(prévu : 3 sessions B-01 → B-03)

---

## DÉCISIONS PRISES

| # | Décision | Valeur | Source |
|---|---|---|---|
| 1 | DD journalier max | 3% | `risk_manager.py:drawdown_stop_jour=0.03` |
| 2 | Confiance AUTO (signal + exécution) | 85% | Unifié `settings.py` + `risk_manager.py` |
| 3 | Risque max par trade | 2% | `risk_manager.py:max_risque_trade=0.02` |
| 4 | Mode AUTO | BLOQUÉ par défaut | 5/6 conditions non validables |
| 5 | Actifs tradés | GC/HG/CL/ZW | Confirmé CLAUDE.md |
| 6 | SI et NQ | Hors scope | Confirmé CLAUDE.md |
| 7 | Broker | Rithmic via NTB | Confirmé CLAUDE.md |
| 8 | Stack | Python 3.11 + FastAPI + React 18 + SQLite + NT8 ATI 36973 | Gelée CLAUDE.md |
| 9 | SaaS-workspace | 0 asset utile pour TradEx | Skip Phase 2 validé |

---

## ⚠️ DÉCISIONS TEMPORAIRES

| # | Décision temporaire | Condition de révision |
|---|---|---|
| 1 | Réorganisation NON exécutée | À faire en session suivante (option Y) |
| 2 | 10 garde-fous manquants dans code | À implémenter en Phase F (Risk Engine complet) |
| 3 | `RAPPORT_REORGANISATION.md` = proposition uniquement | Exécuter après validation CLAUDE.md |
| 4 | Transcripts = 142 (pas 2337 comme annoncé dans docs) | Corriger dans CLAUDE.md |

---

## PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Gravité | Action requise |
|---|---|---|---|
| 1 | CLAUDE.md : chemins `code/scraper/` + `code/transcripts/` inexistants | 🔴 URGENT | Corriger en session Z |
| 2 | Conflit structurel `kb/` racine vs `code/knowledge_base/` | 🟠 À trancher | Décision Phase B (recommandation : option c) |
| 3 | `.tmp.driveupload/` : 400 MB non voulus sur disque | 🟠 URGENT | Supprimer en session Y |
| 4 | 6 dossiers vides à la racine (vestiges migration a1e5205) | 🟡 | Nettoyer en session Y |
| 5 | `CDC_MBK_TRADER v1.0` doublons obsolètes | 🟡 | Archiver en session Y |
| 6 | Mode AUTO : 5/6 conditions non validables aujourd'hui | 🟡 | Normal — déverrouillage prévu Phase K |

---

## STACK TECHNIQUE GELÉE

```
Frontend Desktop   : React 18 + Tailwind CSS (à bootstrapper — npm create vite@latest)
Backend IA         : Python 3.11 + FastAPI (existant dans code/)
Base de données    : SQLite (local desktop)
Plateforme trading : NinjaTrader 8 — ATI port 36973
Broker / données   : Rithmic via NTB
OS                 : Windows 11
Méthode trading    : Belkhayate (centre de gravité, oscillateur, niveaux d'équilibre)
Actifs             : GC / HG / CL / ZW (futures CME/CBOT)
```

---

## ÉTAT DES FICHIERS FIN SESSION

```
C:\trading-copilote\
├── GARDE_FOUS_PROPOSES.md       ✅ créé (32 garde-fous)
├── FEUILLE_DE_ROUTE.md          ✅ créé (11 phases A→K)
├── CHECKLIST_FICHIERS_INUTILES.md ✅ créé (29 items, 402 MB)
├── RAPPORT_REORGANISATION.md    ✅ créé (409 lignes, plan complet)
├── code/config/settings.py      ✅ modifié (DD 3%, confiance 85%)
├── .gitignore                   ✅ enrichi (PDF, settings.local, BACKUP_*)
└── _context/
    ├── briefing-2026-05-03-fin-phase-A.md  ✅ pushé
    └── briefing-2026-05-03-fin-session.md  ✅ pushé
```

**Git** : working tree clean | up to date avec origin/master | 6 commits cette session

---

## COMMANDES GIT (PowerShell)

```powershell
cd C:\trading-copilote
git log --oneline -6
git status
```

---

## PRE-FLIGHT SESSION SUIVANTE

```
[ ] Lire CLAUDE.md en entier
[ ] Lire _context/briefing-2026-05-03-fin-session.md en entier
[ ] Vérifier git status (doit être clean)
[ ] Choisir l'ordre : Z (MAJ CLAUDE.md) → Y (Réorg) → X (Phase B)
[ ] NE PAS commencer Y avant Z
[ ] NE PAS commencer X avant Y
```

---

## PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Lis CLAUDE.md + _context/briefing-2026-05-03-fin-session.md en entier.

Résume en 5 lignes l'état du projet TradEx AI.
Ensuite propose : dois-je commencer par Z (MAJ CLAUDE.md), Y (Réorganisation) ou X (Phase B Belkhayate) ?
Attends ma décision avant toute action.
```
