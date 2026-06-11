# README DE TRANSITION — TRADEX-AI
**Date** : 11 Juin 2026 | **Session** : S04 | **Score projet** : 58/100

---

## ÉTAT ACTUEL DU PROJET

TRADEX-AI est un système de trading temps réel basé sur la méthode Belkhayate, connecté à NinjaTrader 8.
Session S04 = réparation de la dette technique CRITIQUE (circuit breaker + chemins KB).
Les 3 bugs prioritaires listés dans DETTE_TECHNIQUE.md sont réparés (bugs 1+2) ou documentés pour Phase C (bug 3 DATA_DIR).
Le SaaS ne tourne pas encore en production — les modules sont en place mais les collecteurs NT8/ATAS n'existent pas.
Prochaine étape : Phase C — collecteurs de données NT8/ATAS + création dossier `data\`.

---

## MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---|---|---|---|
| Copie README S03 | README_TRANSITION_TRADEX_S03_20260611.md copié dans _context\ | a34be7c | ✅ |
| D-01 circuit breaker | claude_brain.py:25 — `from code.engine.` → `from .` (import relatif) | 75a517e | ✅ |
| D-01 KB path | claude_brain.py:177 — chemin KB corrigé → `04-cerveau-trading\` | 75a517e | ✅ |
| D-01 prompt_builder | claude_brain.py:129 — import relatif corrigé | 75a517e | ✅ |
| D-02 settings.py | KB_DIR + KB_PATH corrigés → `04-cerveau-trading\` | 75a517e | ✅ |
| Lint vérification | py_compile OK sur les 2 fichiers + test import settings | 75a517e | ✅ |
| DETTE_TECHNIQUE.md | Bugs 1+2 marqués ✅ RÉPARÉ | 4121982 | ✅ |
| CLAUDE.md | Section état actuel + dette technique mis à jour | 4121982 | ✅ |

---

## MISSION SUIVANTE — Phase C (collecteurs NT8/ATAS)

### Objectif Phase C
Créer les collecteurs qui alimentent le moteur en données live.

### C-01 — Créer le dossier `data\` et les collecteurs (Session S05)
- Décider l'emplacement définitif de `data\` (recommandé : `C:\trading-copilote\data\` à la racine)
- Harmoniser les 4 références dans : `staleness_monitor.py`, `data_reader.py`, `settings.py` (×2)
- Créer `data_reader.py` opérationnel (lecture JSON NT8 + ATAS)
- Créer le format JSON attendu par NT8 (côté NinjaTrader — script .cs ou fichier export)
- Tester la lecture d'un fichier JSON statique avant de connecter NT8 live

### C-02 — Connecter NinjaTrader 8 (Session S06)
- Configurer l'export JSON automatique depuis NT8 (indicateurs Belkhayate : BGC, Direction, Energie, Pivots)
- Tester la fraîcheur des données (staleness_monitor.py)
- Valider le circuit complet : NT8 → JSON → data_reader → signal engine

---

## DÉCISIONS PRISES CETTE SESSION

| # | Décision | Valeur |
|---|---|---|
| 1 | Mode d'import Python | Import relatif (`.circuit_breaker`) — pas d'import absolu style paquet |
| 2 | Emplacement KB | `C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` — définitif |
| 3 | DATA_DIR | Laissé pour Phase C — décision emplacement en S05 |

---

## DÉCISIONS TEMPORAIRES

| # | Décision temporaire | Condition de révision |
|---|---|---|
| 1 | `data\` inexistant — DATA_DIR pas corrigé | Début Phase C (S05) — choisir emplacement définitif |
| 2 | `prompt_builder.py` inexistant — import relatif en place mais module absent | À créer Phase E (Prompt Engine) |
| 3 | Mode AUTO bloqué | Normal — déverrouillage Phase K (~3-4 mois) |

---

## PROBLÈMES OUVERTS

| # | Problème | Gravité | Action |
|---|---|---|---|
| 1 | `data\` inexistant — 4 références cassées | 🟡 | Phase C (S05) — pas bloquant tant que NT8 non connecté |
| 2 | `prompt_builder.py` absent — `get_signal()` tombe en fallback | 🟡 | Phase E |
| 3 | `chunk_fuse.py:1178` SyntaxWarning `\[` non échappé | 🟢 | Cosmétique — à nettoyer à l'occasion |
| 4 | Fiabilité moteur TRANSVIDEO non validée (> 90/95 %) | 🟡 | Après Phase C |

---

## STACK TECHNIQUE GELÉE

```
Méthode trading    : Belkhayate (intouchable)
Plateforme         : NinjaTrader 8 — ATI port 36973
Broker / données   : Rithmic via NTB
Cerveau IA         : Claude API claude-sonnet-4-6
Backend            : Python 3.11 + FastAPI
Dashboard          : React 18 + Vite + Tailwind 3.4 (Phase D)
DB locale          : SQLite
OS                 : Windows 11 + PowerShell
Actifs trading     : GC / HG / CL / ZW
Actifs confirmation: DX / ES / VX
Actifs référence   : MBT / 6J (no trade)
Règle entrée       : 3/4 trading + 2/3 confirmation alignés
Score signal valide: ≥ 17/21 points
Confiance AUTO min : 85%
Fallback max       : 65% (Auto interdit)
```

---

## ÉTAT GIT FIN SESSION

```
Branch  : master
HEAD    : 4121982  docs: marque dette technique CRITIQUE comme reparee
Sync    : ✅ poussé sur GitHub
```

### 3 commits cette session
```
4121982  docs: marque dette technique CRITIQUE comme reparee
75a517e  fix(engine): repare circuit breaker import + chemins KB corrects
a34be7c  docs: readme transition session S03
```

---

## COMMANDES GIT (PowerShell)

```powershell
cd C:\trading-copilote
git log --oneline -5
git status
```

---

## PRE-FLIGHT SESSION SUIVANTE (S05)

```
[ ] Lire CLAUDE.md en entier
[ ] Lire ce README (README_TRANSITION_TRADEX_S04_20260611.md) en entier
[ ] Vérifier git status (doit être clean)
[ ] Décider emplacement définitif de data\ AVANT tout code Phase C
[ ] NE PAS créer de collecteurs sans valider l'emplacement data\ d'abord
```

---

## PHRASE D'AMORÇAGE SESSION S05

```
Lis CLAUDE.md + 00-pilotage\_context\README_TRANSITION_TRADEX_S04_20260611.md en entier.

Prochaine étape : Phase C — collecteurs NT8/ATAS.
Avant de commencer : propose 2 options pour l'emplacement du dossier data\
(racine projet vs 05-saas\data) avec avantages/inconvénients en 3 lignes chacune.
Attends mon choix avant toute action.
```

---

*README_TRANSITION_TRADEX_S04 — 11/06/2026 — Session S04 bouclée*
*Dette technique CRITIQUE réparée — circuit breaker actif — KB chargeable*
*Prochaine session = Phase C (collecteurs NT8/ATAS — dossier data\)*
