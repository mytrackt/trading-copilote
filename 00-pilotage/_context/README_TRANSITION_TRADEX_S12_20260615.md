# README DE TRANSITION — TRADEX-AI
**Date :** 15/06/2026 | **Session :** S12 | **HEAD :** 71cee21

---

## 1. ÉTAT ACTUEL DU PROJET

Phase B (KB rebuild) avancée. Script de validation automatique des règles DOUTEUX livré et exécuté.
835/1265 règles confirmées VALIDE par Claude contre les 110 transcripts Belkhayate réels.
Phase C (collecteurs NT8) terminée en mode mock (commit 0797fbc).
Mode AUTO toujours BLOQUÉ. Trading Geek transcription ~33/113 en cours en background.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| Phase C mock | Dossier data\ + 8 JSON mock + data_reader/staleness/settings réécrits | 0797fbc | ✅ |
| validate_douteux.py | Script 3-passes anti-hallucination, 108 appels groupés par transcript | 71cee21 | ✅ |
| Validation KB | 1265 règles classées VALIDE/INVALIDE/AMBIGU contre 110 transcripts réels | 71cee21 | ✅ |

---

## 3. MISSION SUIVANTE

**Option A — Revue humaine des 388 AMBIGU**
Ouvrir `04-cerveau-trading/validation/A_VERIFIER_HUMAIN.md` et vérifier les cas douteux
en regardant les liens YouTube fournis dans le fichier. Pas besoin de voir la vidéo en entier —
juste confirmer si le concept est présent.

**Option B — Continuer Trading Geek**
Vérifier si la transcription est terminée (113/113) :
```
ls C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\ | Measure-Object
```
Si 113/113 → Phase A (audit + intégration KB couche 3).

**Option C — Phase C suite (quand NT8 installé)**
4 collecteurs restants : COT, macro, news, fear&greed.

---

## 4. DÉCISIONS PRISES

| Décision | Valeur |
|----------|--------|
| Commande Python sur Windows | `py` (pas `python`) |
| Validation KB | 3 passes : groupée/transcript → orphelines → rapports |
| Modèle validation | claude-haiku-4-5-20251001 (moins cher, tâche classification) |
| Seuil verbatim | Citation doit exister mot-à-mot dans le transcript sinon → AMBIGU auto |
| Score fix | score_min corrigé 17 → 7.0 (était de l'ère /21) |
| USE_MOCK_DATA | True jusqu'à installation NT8 |

---

## 5. RÉSULTATS KB VALIDATION S12

| Verdict | Règles | % | Action |
|---------|--------|---|--------|
| VALIDE | 835 | 66.0% | Alimentent les signaux |
| INVALIDE | 42 | 3.3% | À supprimer de KB |
| AMBIGU | 388 | 30.7% | Revue humaine (fichier .md fourni) |
| **TOTAL** | **1265** | | |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Impact | Action |
|---|---------|--------|--------|
| 1 | 388 règles AMBIGU non résolues | KB incomplète | Revue humaine ou nouvelle passe avec Sonnet |
| 2 | 42 règles INVALIDE encore dans KB | Qualité signaux | Supprimer manuellement ou via script |
| 3 | NT8 non installé | Phase C live bloquée | Planifier installation NT8 |
| 4 | Trading Geek ~33/113 | Phase A en attente | Continue en background |
| 5 | Énergie Belkhayate non codée (stub) | C1 incomplet | Conflit MFI vs ATR non tranché |
| 6 | COGParams validés daily uniquement | Range bars NT8 = Phase C | Backtest hostile concluant : non validé daily |

---

## 7. FICHIERS CLÉS PRODUITS CETTE SESSION

```
05-saas/knowledge_base/validate_douteux.py           ← Script 3-passes
04-cerveau-trading/validation/RAPPORT_VALIDATION.json ← Stats complètes
04-cerveau-trading/validation/KB_VALIDEE.json         ← KB avec statuts
04-cerveau-trading/validation/A_VERIFIER_HUMAIN.md   ← 388 cas + liens YouTube
05-saas/config/settings.py                            ← score_min 7.0 + USE_MOCK_DATA
05-saas/engine/data_reader.py                         ← JSON par actif
05-saas/engine/staleness_monitor.py                   ← clés NT8_GC/HG/CL/ZW/DX/ES/VX
data/mock/*.json                                      ← 8 fichiers mock NT8/ATAS
```

---

## 8. STACK TECHNIQUE GELÉE

```
Python          : py (Windows)
Modèle signaux  : claude-sonnet-4-6
Modèle vision   : claude-sonnet-4-20250514
Modèle KB valid : claude-haiku-4-5-20251001
Actifs trading  : GC, HG, CL, ZW
Confirmation    : DX, ES, VX
Référence       : MBT, 6J (NO TRADE)
Règle entrée    : 3/4 trading + 2/3 confirmation alignés
Score signal    : ≥ 7.0/10 + aucun critère éliminatoire + R/R ≥ 1:2
Mode AUTO       : BLOQUÉ (permanent jusqu'à Phase K)
```

---

## 9. ÉTAT GIT FIN SESSION

```
HEAD    : 71cee21
Remote  : origin/main = 71cee21 (sync ✅)
Commits : 0797fbc (Phase C mock) → 71cee21 (validate_douteux)
```

---

## 10. COMMANDES GIT PROCHAINE SESSION

```powershell
cd C:\trading-copilote
git pull
git log --oneline -5
```

---

## 11. PRE-FLIGHT PROCHAINE SESSION

```
[ ] Lire CLAUDE.md en entier
[ ] Lire ce fichier README_TRANSITION_TRADEX_S12_20260615.md
[ ] Lire 00-pilotage\DETTE_TECHNIQUE.md
[ ] Choisir Option A (revue AMBIGU) ou Option B (Trading Geek) ou Option C (NT8)
[ ] Vérifier : py --version (doit afficher 3.12+)
```

---

## 12. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Je reprends TRADEX-AI session S13. Lis CLAUDE.md + README_TRANSITION_TRADEX_S12_20260615.md.
HEAD=71cee21. KB : 835 VALIDE / 388 AMBIGU / 42 INVALIDE.
Priorité : (1) vérifier Trading Geek 113/113 → Phase A si done ;
(2) sinon revue AMBIGU dans A_VERIFIER_HUMAIN.md.
```
