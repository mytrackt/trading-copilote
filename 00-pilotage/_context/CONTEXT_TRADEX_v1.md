# CONTEXT — TRADEX AI
**Version** : v1.0 | **Date** : 03 Mai 2026 | **Post-Session** : S01

> ⚠️ À LIRE EN ENTIER avant toute action dans ce projet.

---

## 1. IDENTITÉ DU PROJET

**Nom**          : TradEx AI
**Type**         : SaaS Desktop Trading assisté par IA Claude
**Workspace**    : `C:\trading-copilote\`
**GitHub**       : origin/master (up to date)
**OS**           : Windows 11
**Juridiction**  : Maroc (AMMC + CNDP applicables)

**Objectif** : Construire un assistant de trading qui fait les tâches d'un trader
professionnel de 30 ans d'expérience — basé sur la méthode Belkhayate.

---

## 2. STACK TECHNIQUE GELÉE (NE PAS MODIFIER)

```
Frontend   : React 18 + Tailwind CSS (pas encore bootstrappé)
Backend IA : Python 3.11 + FastAPI (existant dans code/)
DB         : SQLite (local desktop)
Trading    : NinjaTrader 8 — ATI port 36973
Broker     : Rithmic via NTB
Actifs     : GC / HG / CL / ZW uniquement
            (SI et NQ sont HORS SCOPE)
Méthode    : Belkhayate (centre de gravité, oscillateur, niveaux équilibre)
```

---

## 3. ÉTAT ACTUEL — PHASE A TERMINÉE ✅

```
✅ FAIT :
  - Backup complet (C:\BACKUP_TRADEX_20260503_011804\ — 913 MB)
  - Risk Engine existant validé (risk_manager.py + settings.py)
  - GARDE_FOUS_PROPOSES.md (32 garde-fous documentés)
  - FEUILLE_DE_ROUTE.md (11 phases A→K)
  - CHECKLIST_FICHIERS_INUTILES.md (29 items, 402 MB récupérables)
  - RAPPORT_REORGANISATION.md (plan complet — proposition uniquement)
  - .gitignore enrichi
  - 6 commits poussés sur GitHub

❌ PAS ENCORE FAIT :
  - Réorganisation physique des fichiers (plan existe, pas exécuté)
  - Frontend React (à bootstrapper Phase D)
  - Dashboard (Phase D — après choix thème)
  - Phase B : KB Belkhayate (extraction 142 transcripts → JSON)
  - Correction CLAUDE.md (chemins inexistants)
```

---

## 4. PARAMÈTRES RISK ENGINE VALIDÉS

```python
dd_day_max          = 0.03   # 3% DD journalier max
confiance_min_auto  = 0.85   # 85% confiance signal + exécution AUTO
max_risque_trade    = 0.02   # 2% risque max par trade
mode_auto           = BLOQUÉ # 5/6 conditions non validées
```

**Fichiers** :
- `code/config/settings.py` — configuration
- `code/engine/risk_manager.py` — logique runtime

---

## 5. DÉCISIONS VERROUILLÉES

- Actifs : GC/HG/CL/ZW — SI et NQ **définitivement hors scope**
- Broker : Rithmic via NTB
- Stack : gelée (voir §2)
- Mode AUTO : bloqué jusqu'à 6 conditions remplies (voir GARDE_FOUS_PROPOSES.md)
- Méthode : Belkhayate est la fondation de tous les signaux

---

## 6. FICHIERS CLÉS À LIRE EN PRIORITÉ

```
1. C:\trading-copilote\CLAUDE.md                          ← règles projet
2. C:\trading-copilote\_context\briefing-2026-05-03-fin-session.md ← état journée
3. C:\trading-copilote\FEUILLE_DE_ROUTE.md                ← 11 phases A→K
4. C:\trading-copilote\GARDE_FOUS_PROPOSES.md             ← 32 garde-fous
5. C:\trading-copilote\RAPPORT_REORGANISATION.md          ← plan réorg
6. C:\trading-copilote\CHECKLIST_FICHIERS_INUTILES.md     ← 29 items à nettoyer
7. C:\trading-copilote\docs\MASTER_TRADEX_AI_v2.md        ← fichier maître
```

---

## 7. PROBLÈMES OUVERTS CRITIQUES

| # | Problème | Action |
|---|---|---|
| 1 | `CLAUDE.md` contient chemins inexistants (`code/scraper/`, `code/transcripts/`) | Corriger en **priorité Z** |
| 2 | `.tmp.driveupload/` : 400 MB parasites sur disque | Supprimer en priorité Y |
| 3 | Conflit `kb/` racine vs `code/knowledge_base/` vides | Trancher en Phase B |
| 4 | 142 transcripts réels (pas 2337 comme indiqué dans certains docs) | Corriger dans CLAUDE.md |

---

## 8. PROCHAINES ACTIONS (ordre obligatoire)

```
Z — MAJ CLAUDE.md (corriger chemins + état actuel)    ← PRIORITÉ 1
Y — Réorganisation workspace (exécuter RAPPORT_REORGANISATION.md)
X — Phase B : KB Belkhayate (3 sessions B-01 → B-03)
D — Dashboard React (après Phase B, choix thème design-themes.md)
```

> ⚠️ NE PAS commencer Y avant Z.
> ⚠️ NE PAS commencer X avant Y.
> ⚠️ NE PAS commencer le code React avant Phase B terminée.

---

## 9. RÈGLES ABSOLUES DU PROJET

1. **Zéro code créé sans validation** — proposer d'abord, coder après OK
2. **Zéro modification de `code/`** sans backup Git préalable
3. **Stack gelée** — aucune dépendance ajoutée sans discussion
4. **Actifs fixes** — GC/HG/CL/ZW uniquement, jamais SI ou NQ
5. **Mode AUTO bloqué** — ne jamais déverrouiller sans les 6 conditions
6. **Méthode Belkhayate** — tout signal doit être validé par au moins 2 indicateurs Belkhayate
7. **Zéro hallucination données** — API down → "DONNÉES INDISPONIBLES" en rouge
8. **Secrets** dans `.env.local` uniquement — jamais dans le code
9. **Réorganisation** — uniquement après MAJ CLAUDE.md (ordre Z → Y)
10. **Commit après chaque mission** — jamais de working tree sale en fin de session

---

## 10. PHRASE D'AMORÇAGE

```
Lis CLAUDE.md + _context/briefing-2026-05-03-fin-session.md en entier.
Résume en 5 lignes l'état du projet TradEx AI.
Ensuite propose : dois-je commencer par Z (MAJ CLAUDE.md),
Y (Réorganisation) ou X (Phase B Belkhayate) ?
Attends ma décision avant toute action.
```

---

*CONTEXT v1.0 — TradEx AI — Post-Session S01 — 03/05/2026*
