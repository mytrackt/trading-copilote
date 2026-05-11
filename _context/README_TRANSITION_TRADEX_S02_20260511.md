# README DE TRANSITION — TRADEX-AI
**Date** : 11 Mai 2026 | **Session** : S02 | **Score projet** : 52/100

---

## ÉTAT ACTUEL DU PROJET

TRADEX-AI est un système de trading temps réel basé sur la méthode Belkhayate, connecté à NinjaTrader 8.
Session S02 = Z1 + Y + Z2 exécutés et pushés. Workspace épuré (388 MB libérés, racine passée de 28 à 7 fichiers/14 dossiers).
CLAUDE.md est maintenant la source de vérité fiable — chemins corrigés, Phase A reflétée, arborescence post-Y à jour.
Prochaine étape : Phase B (extraction KB Belkhayate — 142 transcripts → JSON).

---

## MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| PDF Audit | Extraction segments utiles Guide Stratégique Trading Claude AI → docs/APPORTS_GUIDE_EXTERNE.md | faf0678 (S01) | ✅ |
| Stratégie S02 | Analyse Z1→Y→Z2→X — risques, séquence, estimation 5 sessions | — | ✅ |
| Z1 | CLAUDE.md corrigé : chemins inexistants supprimés, 142 transcripts, Phase A reflétée, 7 commits journée | a6f99c1 | ✅ |
| Y — G1 | Nettoyage racine (dossiers vides + .tmp.driveupload) | 26b711b | ✅ |
| Y — G2 | Archive MBK (projet en pause) | 5ddfb6c | ✅ |
| Y — G3 | Archive méthodes externes hors scope | 535ec05 | ✅ |
| Y — G4 | Rangement corpus Belkhayate | 3183d38 | ✅ |
| Y — G5 | Organisation scripts Windows + PROMPT_1 vers docs/ | 1df60f5 | ✅ |
| Y — G6/G6b | Archive audits + README contexte + PDF source + .gitignore | 914e976 / 73c54e3 | ✅ |
| Z2 | CLAUDE.md mis à jour post-Y (arborescence finale + état actuel) | 76114d8 | ✅ |
| Briefing S02 | _context/briefing-2026-05-11-fin-session.md généré | f6a6d32 | ✅ |

---

## MISSION SUIVANTE — Phase B (KB Belkhayate)

### Pré-requis (début de session)
- [ ] Trancher D1 : `kb/` racine (vide) vs `code/knowledge_base/` (a transcript_processor.py skel) — recommandation : option c = utiliser `code/knowledge_base/`, supprimer `kb/` racine
- [ ] Décider si `CONTEXT_TRADEX_v1.md` + `README_TRANSITION_TRADEX_S01_20260503.md` doivent être commités (actuellement non-trackés)

### Phase B — B-01 (Session S03)
- Lire `whisper_pipeline.py` existant (`04-kb-sources/youtube-a-scraper/`)
- Lire 5 transcripts échantillons pour comprendre la structure
- Concevoir `transcript_processor.py` dans `code/knowledge_base/`
- Parser les 50 premiers transcripts → JSON partiel

### Phase B — B-02 (Session S04)
- Parser les 92 transcripts restants
- Déduplication des règles extraites

### Phase B — B-03 (Session S05)
- Structuration JSON final (`KNOWLEDGE_BASE_MASTER.json`)
- Validation + intégration `claude_brain.py` (fonction `load_kb_rules()`)

---

## DÉCISIONS PRISES CETTE SESSION

| # | Décision | Valeur |
|---|---|---|
| 1 | Ordre exécution S02 | Z1 → Y → Z2 (pas Z → Y → X directement) |
| 2 | .tmp.driveupload/ | Laisser tel quel (recréé par Google Drive, gitignored) |
| 3 | Racine cible atteinte | 6 fichiers stratégiques + 14 dossiers fonctionnels |
| 4 | Arborescence post-Y | Gelée — ne plus toucher avant Phase B |

---

## ⚠️ DÉCISIONS TEMPORAIRES

| # | Décision temporaire | Condition de révision |
|---|---|---|
| 1 | `kb/` racine vide conservée | Trancher en début Phase B (D1) |
| 2 | `CONTEXT_TRADEX_v1.md` non-commité | Décider S03 : commit ou ignore |
| 3 | `README_TRANSITION_TRADEX_S01_20260503.md` non-commité | Décider S03 |
| 4 | Mode AUTO bloqué | Normal — déverrouillage Phase K (~3-4 mois) |

---

## PROBLÈMES OUVERTS

| # | Problème | Gravité | Action |
|---|---|---|---|
| 1 | D1 non tranché : `kb/` vs `code/knowledge_base/` | 🟠 | Début Phase B |
| 2 | 10 garde-fous manquants dans code (G1→G10) | 🟡 | Phase F (Risk Engine complet) |
| 3 | signal_scorer.py non créé | 🟡 | Phase B-03 ou C |
| 4 | collectors/ execution/ api/ vides | 🟡 | Phases C, G, H |

---

## STACK TECHNIQUE GELÉE

```
Méthode trading    : Belkhayate (intouchable)
Plateforme         : NinjaTrader 8 — ATI port 36973
Broker / données   : Rithmic via NTB
Cerveau IA         : Claude API claude-sonnet-4-6
Backend            : Python 3.11 + FastAPI
Dashboard          : React 18 + Vite + Tailwind 3.4 (à bootstrapper Phase D)
DB locale          : SQLite
OS                 : Windows 11 + PowerShell
Actifs trading     : GC / HG / CL / ZW (jamais SI, NQ, MBT, 6J)
Actifs confirmation: DX / ES / VX
Score signal valide: ≥ 17/21 points
Confiance AUTO min : 85%
DD jour stop       : 3%
Fallback max       : 65% (Auto interdit)
```

---

## ÉTAT GIT FIN SESSION

```
Branch  : master
HEAD    : f6a6d32 docs: briefing fin de session 2026-05-11
Sync    : ✅ up to date avec origin/master (10 commits poussés)
Tree    : CLAUDE.md M (si Z2 pas encore commité)
```

### 10 commits cette session
```
f6a6d32  docs: briefing fin de session 2026-05-11 - Z1 Y Z2 executes
76114d8  docs(claude): Z2 - mise a jour arborescence + etat actuel post-Phase Y
73c54e3  chore: G6b update .gitignore - nouveau chemin PDF source
914e976  chore: G6 archive audits + README contexte + PDF source
1df60f5  chore: G5 organisation - scripts windows + prompt_1 KB vers docs
3183d38  chore: G4 rangement corpus belkhayate
535ec05  chore: G3 archive methodes externes hors scope TRADEX-AI
5ddfb6c  chore: G2 archive MBK - projet en pause
26b711b  chore: G1 nettoyage racine - dossiers vides + .tmp.drive cleanup
a6f99c1  docs(claude): Z1 - corrige chemins inexistants et reflete fin Phase A
```

---

## COMMANDES GIT (PowerShell)

```powershell
cd C:\trading-copilote
git log --oneline -10
git status
```

---

## PRE-FLIGHT SESSION SUIVANTE

```
[ ] Lire CLAUDE.md en entier
[ ] Lire _context/briefing-2026-05-11-fin-session.md en entier
[ ] Vérifier git status (doit être clean)
[ ] Trancher D1 (kb/ vs code/knowledge_base/) — AVANT tout code Phase B
[ ] NE PAS créer de code sans valider D1 d'abord
```

---

## PHRASE D'AMORÇAGE SESSION S03

```
Lis CLAUDE.md + _context/briefing-2026-05-11-fin-session.md en entier.

Prochaine étape : Phase B — KB Belkhayate.
Avant de commencer : trancher D1 (kb/ racine vide vs code/knowledge_base/).
Montre-moi les 2 options avec avantages/inconvénients en 3 lignes chacune.
Attends mon choix avant toute action.
```

---

*README_TRANSITION_TRADEX_S02 — 11/05/2026 — Session S02 bouclée*
*Z1 + Y(G1→G6b) + Z2 exécutés — 388 MB libérés — racine épurée*
*Prochaine session = Phase B (KB Belkhayate — 142 transcripts → JSON)*
