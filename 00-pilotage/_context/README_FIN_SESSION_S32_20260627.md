# README DE TRANSITION — TRADEX-AI
**Date :** 2026-06-27 · **Session :** S32 · **Score projet :** N/A (Phase B en cours)

---

## 1. ÉTAT ACTUEL DU PROJET

KB Belkhayate à **1331 règles / 108 vidéos** (objectif : maximiser avant développement Phase C).
Pipeline KB P1 en cours : Chap12 ✅ intégré (+18 règles). Chap9 / Chap8 / Chap6 en attente (Task #7).
Décision verrouillée S32 : ADX_SEUIL_OPÉRATIONNEL = **25** (plus jamais 20 dans le code).
Commit `0346b49` poussé ✅. DECISIONS_VEROUILLEES.md **pas encore mis à jour pour S31/S32** — à faire.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| # | Mission | Résultat |
|---|---|---|
| #5 | Validation ADX seuil Chap9 | ✅ ADX=25 verrouillé + note §9.2.2 ajoutée (sed -i) |
| #6 | Pipeline KB Chap12 (18 briques) | ✅ KB 1313→1331 · macro_evenements 13→24 |
| - | Analyse technique Pipeline KB P1 | ✅ ANALYSE_TECHNIQUE_PIPELINE_KB_P1.md créé |
| - | Batch Layer3 NinjaTrader | ✅ 4/5 OK · 1 erreur 503 (RtHca3NU-D4) |
| - | Commit S32 poussé | ✅ `0346b49` — 8 fichiers, 871 insertions |
| - | Vérif transcriptions nouvelles-sources | ✅ 108/109 VALIDE en KB · 1 manquante : `enG01BznN_M` |

---

## 3. MISSION SUIVANTE

**Task #7 — Pipeline KB Chap9 (priorité 2)**
Lire `TRADEX_KB_Chap9_Construire_Strategie.md` → Fabriquer `validation/KB_CHAP9_STRATEGIE.json`
→ Audit auto → Fusion → Commit.
Estimation : 8–10 briques · catégories : `gestion_risque_entree`, `structure_marche`, `psychologie`, `indicateurs_tendance`.

---

## 4. DÉCISIONS PRISES

| Code | Décision | Date |
|---|---|---|
| D-S32-1 | ADX_SEUIL_OPÉRATIONNEL = **25** (moteur). §9.2.2 conserve 20/40 (référence Wilder). Ne jamais utiliser 20 dans le code. | 2026-06-27 |
| D-S32-2 | Toute règle `macro_evenements` DOIT avoir `note` avec `"ROLE: BLOCAGE_SEUL"` ou `"ROLE: CONTEXTE_FILTRE"` pour distinguer des règles Belkhayate signal | 2026-06-27 |
| D-S32-3 | Chap12 intégré avec `source_video_id = "CHAP12_MENTOR_BELKHAYATE_2026"` | 2026-06-27 |

⚠️ **DETTE GOV** : D-S31 (16 décisions) et D-S32 (3 décisions) ne sont **PAS encore écrites** dans `DECISIONS_VEROUILLEES.md`. À faire en priorité avant Phase C.

---

## 5. DÉCISIONS TEMPORAIRES

| Sujet | Valeur provisoire | À confirmer |
|---|---|---|
| Tag → confiance mapping | 🟢=0.95 · 🟡=0.80 · 🔵=0.70 · ⏳=0.65 · 🔴=0.55 | Avant Phase C |
| Nb briques Chap9 | 8–10 estimé | Après lecture complète |
| NinjaTrader RtHca3NU-D4 | Skip (erreur 503 Gemini) | Retry quand Gemini disponible |

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| Priorité | Problème | Solution |
|---|---|---|
| ⚠️ P0 | **Circuit Breaker INACTIF** — mode AUTO strictement interdit | Réparer avant toute activation AUTO |
| ⚠️ P0 | **DECISIONS_VEROUILLEES.md** non mis à jour S31/S32 | Ajouter D-S31-1→16 + D-S32-1→3 |
| P1 | `test_write.tmp` + `.bak_s32_chap12` commités par erreur | Ajouter `*.tmp` et `*.bak*` au `.gitignore` |
| P1 | Video KB manquante : `enG01BznN_M` (Belkhayate Vidéo 10) | Lancer `transcript_processor.py` |
| P1 | 54 transcriptions Whisper hors manifeste (orphelines) | Audit + ajout au manifeste si VALIDE |
| P2 | 7 chapitres P2 non audités (Chap7/10/11/13/14/CHAP01/CHAP02) | Mode RAPIDE — audit hostile |
| P2 | Gemini RtHca3NU-D4 (503 overload) | Retry `batch_gemini_nt8_layer3.py` |
| P3 | Phase B-03 (nouvelles-sources → KB) | Après Task #7 terminé |

---

## 7. STACK TECHNIQUE GELÉE

```
Python 3.11 · Anthropic SDK (claude-sonnet-4-6)
Windows 11 + PowerShell 7.6.2
KNOWLEDGE_BASE_MASTER.json → atomic write (.tmp + os.replace)
Validation/ → zone tampon obligatoire avant fusion KB
Backups → *.bak_[session] (hors git idéalement)
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Branche : main
Dernier commit : 0346b49 feat(kb): integration Chap12 macro_evenements +18 regles (1313->1331) + corrections ADX Chap9 + Chap8 30min
Fichiers en attente de commit : AUCUN (état propre)
KB : 1331 règles · 108 vidéos
```

**Fichiers modifiés/créés S32 :**
- `00-pilotage/ANALYSE_TECHNIQUE_PIPELINE_KB_P1.md` (nouveau)
- `02-sources-brutes/methode-belkhayate/TRADEX_KB_Chap9_Construire_Strategie.md` (note ADX §9.2.2)
- `02-sources-brutes/methode-belkhayate/TRADEX_KB_Chap8_Patterns_Setups.md` (30min §8.6.3)
- `04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json` (1313→1331)
- `04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json.bak_s32_chap12` (backup — ⚠️ commité par erreur)
- `04-cerveau-trading/validation/KB_CHAP12_MACRO.json` (18 briques)
- `04-cerveau-trading/validation/REGISTRE_VALIDITE.md` (ticket 0.l ajouté)
- `04-cerveau-trading/validation/test_write.tmp` (⚠️ commité par erreur)

---

## 9. COMMANDES GIT (PowerShell — UNE à la fois)

Tout est déjà commité + pushé ✅

Pour la prochaine session (après Task #7 Chap9) :
```powershell
# Depuis C:\trading-copilote
git add .
git commit -m "feat(kb): pipeline KB Chap9 +X regles (1331->XXXX)"
git push origin main
```

Nettoyage .gitignore (à faire prochaine session) :
```powershell
# Ajouter dans .gitignore :
# *.tmp
# *.bak*
git add .gitignore
git commit -m "chore: add *.tmp and *.bak* to gitignore"
git push origin main
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

- [ ] Lire `CLAUDE.md` en entier
- [ ] Lire ce README (S32)
- [ ] Lire `00-pilotage/DECISIONS_VEROUILLEES.md`
- [ ] Lire `00-pilotage/DETTE_TECHNIQUE.md`
- [ ] Vérifier git status (propre)
- [ ] Confirmer KB = 1331 règles avant de continuer

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Session S33 — TRADEX-AI
État : KB 1331 règles (108 vidéos). Commit 0346b49 pushé ✅.
Prochaine action : Task #7 — Pipeline KB Chap9.
Lire Chap9 → fabriquer validation/KB_CHAP9_STRATEGIE.json (8-10 briques, 
catégories : gestion_risque_entree + structure_marche + psychologie + indicateurs_tendance).
ADX_SEUIL_OPÉRATIONNEL = 25 (D-S32-1 verrouillé).
DETTE : ajouter *.tmp et *.bak* au .gitignore. 
DETTE GOV : écrire D-S31 et D-S32 dans DECISIONS_VEROUILLEES.md.
```

---

## 12. ÉTAT KB — Session S32

| Catégorie | Règles | Δ S32 |
|---|---|---|
| indicateurs_tendance | 236 | — |
| structure_marche | 279 | — |
| psychologie | 237 | — |
| timing | 106 | — |
| gestion_risque_entree | 177 | — |
| gestion_position_active | 85 | — |
| volume_liquidite | 72 | +2 |
| correlations | 39 | +4 |
| indicateurs_momentum | 54 | — |
| saisonnalite | 22 | +1 |
| **macro_evenements** | **24** | **+11** |
| **TOTAL** | **1331** | **+18** |

**Source intégrée S32 :** CHAP12_MENTOR_BELKHAYATE_2026 (18 briques, audit 100/100)
**Vidéo manquante :** `enG01BznN_M` (Belkhayate Vidéo 10) — 1 VALIDE non encore en KB
**Pipeline P1 restant :** Chap9 (priorité 2) → Chap8 (P3) → Chap6 (P4)
**Pipeline P2 :** Chap7/10/11/13/14/CHAP01/CHAP02 (mode RAPIDE)

---

*README généré automatiquement — Session S32 — 2026-06-27*
*Outil : readme-transition v3.3*
