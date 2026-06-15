# README DE TRANSITION — TRADEX-AI
**Date :** 15/06/2026 | **Session :** S14 | **HEAD :** 8dceff0

---

## 1. ÉTAT ACTUEL DU PROJET

KB revalidée à 92.2% (1166/1265 règles VALIDE) grâce à la passe3 Sonnet sur 63 "Pas de réponse API".
+55 règles récupérées. 45 AMBIGU restants dans A_VERIFIER_HUMAIN.md pour revue humaine.
Trading Geek 38/113 — transcription toujours en background. Mode AUTO bloqué.
Incident git résolu : commit catastrophique e10ad5a (552 suppression) annulé via force push.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Passe3 Sonnet | 63 règles "Pas de réponse API" → 55 VALIDE / 5 AMBIGU / 3 INVALIDE | 8dceff0 | ✅ |
| KB_VALIDEE.json | 1111 → 1166 VALIDE, 103 → 45 AMBIGU, 51 → 54 INVALIDE | 8dceff0 | ✅ |
| A_VERIFIER_HUMAIN.md | Mis à jour : 45 cas restants (était 103) | 8dceff0 | ✅ |
| revalider_passe3_resume.py | Script cache par transcript — contourne timeout 45s bash | 8dceff0 | ✅ |
| passe3_cache.json | Cache des résultats passe3 (63 règles) — sauvegardé | 8dceff0 | ✅ |
| Incident git | Commit e10ad5a (552 deletions) annulé → force push 8dceff0 | 8dceff0 | ✅ |
| CLAUDE.md | Section ÉTAT ACTUEL mis à jour S14 | local | ✅ |

---

## 3. MISSION SUIVANTE

**Option A — Revue humaine des 45 AMBIGU restants**
Ouvrir `04-cerveau-trading/validation/A_VERIFIER_HUMAIN.md`.
8 catégories : structure_marche (10), volume_liquidite (8), indicateurs_tendance (6),
indicateurs_momentum (5), gestion_risque_entree (5), timing (4), gestion_position_active (4), psychologie (3).
Pour chaque cas : lien YouTube fourni, écouter 2-3 min, noter VALIDE ou INVALIDE.
→ Objectif : atteindre 95%+ (1202/1265 VALIDE).

**Option B — Attendre Trading Geek 113/113 → Phase A**
```powershell
ls "C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\" | Measure-Object
```
Si 113 → Phase A : audit + intégration KB couche 3 (pipeline validate_douteux.py).

**Option C — Phase C suite (NT8 installé)**
4 collecteurs restants : COT, macro, news, fear&greed.

---

## 4. DÉCISIONS PRISES

| Décision | Valeur |
|----------|--------|
| Stratégie passe3 | 1 transcript par bash call (cache passe3_cache.json) — contourne timeout 45s |
| Seuil passe3 | Concept présent = VALIDE (paraphrase OK) / trop vague = AMBIGU |
| MAX_RULES_PER_CALL | 25 règles par appel API |
| MAX_TRANSCRIPT_CHARS | 14 000 caractères par transcript |
| Git corruption | index.lock invisible sur Windows → écrire index vide valide en Python |
| Git disaster | Jamais utiliser GIT_INDEX_FILE pour git add/commit (crée arbre tronqué) |

---

## 5. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Impact | Action |
|---|---------|--------|--------|
| 1 | 45 règles AMBIGU non résolues | KB à 92.2% (objectif 95%+) | Revue humaine ou 4e passe |
| 2 | 54 règles INVALIDE dans KB_VALIDEE.json | Qualité signaux | Pas urgent — bucket séparé |
| 3 | NT8 non installé | Phase C live bloquée | Planifier installation NT8 |
| 4 | Trading Geek 38/113 | Phase A en attente | Continue en background |
| 5 | Énergie Belkhayate non codée (stub) | C1 incomplet | Conflit MFI vs ATR non tranché |
| 6 | Write tool génère null bytes | Script tronqué si non nettoyé | Strip obligatoire post-Write |

---

## 6. INCIDENT GIT S14 (POST-MORTEM)

**Cause** : `.git/index` corrompu (NTFS + montage Linux). Tentative de contournement
avec `GIT_INDEX_FILE=/tmp/new git add` → commit `e10ad5a` avec seulement 5 fichiers
→ 552 suppressions en apparence.

**Fix** :
1. `git reset --hard 2e18744` (bon commit précédent)
2. Copier les 5 fichiers depuis backup `C:\temp_tradex_backup\`
3. `git add` des 5 fichiers uniquement
4. `git commit` → `8dceff0`
5. `git push --force` → remote corrigé

**Leçon** : JAMAIS utiliser GIT_INDEX_FILE. En cas de corruption git.index :
```python
import hashlib
header = b'DIRC' + (2).to_bytes(4,'big') + (0).to_bytes(4,'big')
checksum = hashlib.sha1(header).digest()
open('.git/index','wb').write(header + checksum)
```
Puis `Remove-Item .git\HEAD.lock -Force` depuis PowerShell.

---

## 7. FICHIERS CLÉS PRODUITS CETTE SESSION

```
05-saas/knowledge_base/revalider_passe3_resume.py    <- Script passe3 avec cache (VERSION ACTIVE)
05-saas/knowledge_base/revalider_passe3.py           <- Version monolithique (archive)
04-cerveau-trading/validation/KB_VALIDEE.json         <- KB mise a jour (1166 VALIDE)
04-cerveau-trading/validation/A_VERIFIER_HUMAIN.md   <- 45 cas restants
04-cerveau-trading/validation/passe3_cache.json       <- Cache 63 regles traitees
```

---

## 8. STACK TECHNIQUE GELÉE

```
Python          : py (Windows)
Modele signaux  : claude-sonnet-4-6
Modele KB valid : claude-haiku-4-5-20251001 (erreurs API simples)
Modele revalid  : claude-sonnet-4-6 (passe semantique)
Actifs trading  : GC, HG, CL, ZW
Confirmation    : DX, ES, VX
Reference       : MBT, 6J (NO TRADE)
Regle entree    : 3/4 trading + 2/3 confirmation alignes
Score signal    : >= 7.0/10 + aucun critere eliminatoire + R/R >= 1:2
Mode AUTO       : BLOQUE (permanent jusqu'a Phase K)
```

---

## 9. ÉTAT GIT FIN SESSION

```
HEAD    : 8dceff0
Message : feat(kb): passe3 S14 - 1166 VALIDE 54 INVALIDE 45 AMBIGU (+55 valide)
Remote  : origin/main = 8dceff0 (force push confirme)
```

---

## 10. COMMANDES GIT PROCHAINE SESSION

```powershell
cd C:\trading-copilote
git log --oneline -5
git status
```

---

## 11. PRE-FLIGHT PROCHAINE SESSION

```
[ ] Lire CLAUDE.md en entier
[ ] Lire ce fichier README_TRANSITION_TRADEX_S14_20260615.md
[ ] Lire 00-pilotage\DETTE_TECHNIQUE.md
[ ] git log --oneline -3 (verifier HEAD = 8dceff0)
[ ] Choisir Option A (revue 45 AMBIGU) ou B (Trading Geek) ou C (NT8)
[ ] Verifier : py --version (doit afficher 3.12+)
```

---

## 12. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Je reprends TRADEX-AI session S15. Lis CLAUDE.md + README_TRANSITION_TRADEX_S14_20260615.md.
HEAD=8dceff0. KB : 1166 VALIDE / 45 AMBIGU / 54 INVALIDE (92.2%).
Priorite : (1) verifier Trading Geek 113/113 -> Phase A si done ;
(2) sinon revue humaine 45 AMBIGU dans A_VERIFIER_HUMAIN.md (objectif 95%+).
```
