# README DE TRANSITION — TRADEX-AI
**Date** : 29/06/2026 | **Session** : S39 | **Score projet** : N/A (session diagnostic)

---

## 1. ÉTAT ACTUEL DU PROJET

Diagnostic complet KB reconstruction terminé (3 rapports A/B/C validés). Verdict : **GO CONDITIONNEL — RISQUE MOYEN**. La reconstruction est réversible à 100% via git commit 2d20750 + 164 Whisper tracés + backup JSON Phase 0 (à créer). Aucun bloquant technique. 5 conditions obligatoires avant de commencer. Prochaine action = `git tag KB-WHISPER-1398` puis créer `extract_chapter_rules.py` (Phase 0).

---

## 2. MISSIONS TERMINÉES CETTE SESSION

- [x] **Analyse profonde** de la stratégie de reconstruction KB (6 causes racines, 14 risques)
- [x] **STRATEGIE_RECONSTRUCTION_KB_V2_S39.md** créé (10 phases + plan validation)
- [x] **Prompt Claude Code** rédigé + audit 12 passes (score 65/100 → 15 corrections appliquées)
- [x] **3 prompts décomposés** (A/B/C) créés avec corrections post-Rapport A
- [x] **Prompt A** exécuté par Claude Code → Rapport A (10 mesures M1-M10)
- [x] **Prompt B** exécuté → Rapport B (audit 10 phases, 7 phases À CORRIGER, 1 risque CRITIQUE)
- [x] **Prompt C** exécuté → Rapport C (conséquences complètes, GO CONDITIONNEL)
- [x] **DECISIONS_VEROUILLEES.md** mis à jour (D-S39-1 à D-S39-8)
- [x] **RAPPORT_C_CONSEQUENCES_S39.md** sauvegardé dans `_context`

---

## 3. MISSION SUIVANTE

**Démarrer la reconstruction KB — Phase 0 et Phase 1 (sécurité avant tout)**

Ordre strict :
1. `git tag KB-WHISPER-1398` → filet de sécurité git
2. Créer `extract_chapter_rules.py` (avec fix 3× dirname) dans `05-saas\utils\`
3. Lancer `py 05-saas\utils\extract_chapter_rules.py` → vérifier "62 règles chapitres sauvegardées"
4. Copier `KNOWLEDGE_BASE_MASTER.json` → `KB_BACKUP_WHISPER_1398.json` dans `04-cerveau-trading\`

---

## 4. DÉCISIONS PRISES (D-S39-1 à D-S39-8)

| ID | Décision |
|----|----------|
| D-S39-1 | 62 règles chapitres à sauvegarder (14 `id_brique` + 48 `id`/`contenu`) — pas 14 |
| D-S39-2 | `rebuild_aggregated()` détruit les chapitres → Phase 8 = DERNIÈRE écriture KB |
| D-S39-3 | Bug BASE_DIR dans `05-saas/utils/` : toujours 3× dirname |
| D-S39-4 | Phase 4 : changer `VIDEO_DIR` ET `OUTPUT_DIR` dans `gemini_transcriber.py` |
| D-S39-5 | 21 fichiers OFTC à décontaminer (pas 5) — corpus épisodes, phase ultérieure |
| D-S39-6 | Baseline tests = 69/69 PASS (pas 37) — dossier `05-saas\tests\` n'existe pas |
| D-S39-7 | D-S31-12 non implémentée : SHA256 = registre manuel, TRADEX démarre sans vérification |
| D-S39-8 | 5 writers KB à désactiver pendant reconstruction (purge, b05, b06, apply_ambigu, processeur post-Ph.8) |

---

## 5. DÉCISIONS TEMPORAIRES

Aucune.

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité |
|---|----------|----------|
| 1 | `rebuild_aggregated()` fragilité permanente : efface les 62 chapitres à chaque exécution du processeur | P0 — mitigé par backup JSON |
| 2 | Phase 2 gate : si <60/110 vidéos YouTube disponibles → re-décision avant Phase 3 | P1 |
| 3 | D-S31-12 non implémentée (SHA256 gate de démarrage) | P2 — dette technique |
| 4 | `google-generativeai` 0.8.6 déprécié (FutureWarning) — migration vers `google-genai` partielle | P2 |

---

## 7. STACK TECHNIQUE GELÉE

```
TRADING    : GC · HG · CL · ZW
CONFIRM.   : DX · ES · VX
RÉFÉRENCE  : MBT · 6J (jamais d'ordre)
MODÈLE KB  : claude-sonnet-4-6
TRANSCRIPTION : gemini-2.5-flash (multimodal MP4)
PYTHON     : 3.x — BASE_DIR = 3× dirname depuis 05-saas/utils/
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Branche     : main (branch cassée → git status fonctionne)
KB règles   : 1398 (1336 vidéo + 62 chapitres)
SHA256 KB   : bcaaaeed6267aa9c24cd092e6c18881acf726a5b8ed9d2c72c5c0a023bf3f773
SHA256 registre : 4cc9f77a... (OBSOLÈTE — à mettre à jour Phase 9)
Tag KB-WHISPER-1398 : ABSENT (à créer IMMÉDIATEMENT)
KB_BACKUP_WHISPER_1398.json : ABSENT (à créer Phase 1)
KB_CHAPTER_RULES_BACKUP.json : ABSENT (à créer Phase 0)
Fichiers modifiés S39 :
  + 00-pilotage/_context/RAPPORT_C_CONSEQUENCES_S39.md
  + 00-pilotage/_context/PROMPT_A_ETAT_DES_LIEUX.md
  + 00-pilotage/_context/PROMPT_B_AUDIT_10_PHASES.md (corrigé)
  + 00-pilotage/_context/PROMPT_C_CONSEQUENCES_RECONSTRUCTION.md (corrigé)
  + 00-pilotage/_context/AUDIT_PROMPT_S39_RAPPORT.md
  + 00-pilotage/STRATEGIE_RECONSTRUCTION_KB_V2_S39.md
  M 00-pilotage/DECISIONS_VEROUILLEES.md (D-S39-1 à D-S39-8)
```

---

## 9. COMMANDES GIT

**Commande 1/3 — Stage les fichiers S39 :**
```powershell
git -C "C:\trading-copilote" add 00-pilotage\_context\README_FIN_SESSION_S39_20260629.md 00-pilotage\_context\RAPPORT_C_CONSEQUENCES_S39.md 00-pilotage\_context\PROMPT_B_AUDIT_10_PHASES.md 00-pilotage\_context\PROMPT_C_CONSEQUENCES_RECONSTRUCTION.md 00-pilotage\DECISIONS_VEROUILLEES.md
```

*(Attendre confirmation avant la commande suivante)*

**Commande 2/3 — Commit :**
```powershell
git -C "C:\trading-copilote" commit -m "chore: diagnostic KB reconstruction S39 - GO CONDITIONNEL RISQUE MOYEN"
```

*(Attendre confirmation — hash visible)*

**Commande 3/3 — Push :**
```powershell
git -C "C:\trading-copilote" push origin main
```

---

## 10. PRE-FLIGHT SESSION SUIVANTE

Avant toute action, lire dans l'ordre :
1. `C:\trading-copilote\CLAUDE.md`
2. `C:\trading-copilote\00-pilotage\DECISIONS_VEROUILLEES.md` (surtout D-S39-1 à D-S39-8)
3. `C:\trading-copilote\00-pilotage\_context\RAPPORT_C_CONSEQUENCES_S39.md` (verdict GO CONDITIONNEL)
4. `C:\trading-copilote\00-pilotage\DETTE_TECHNIQUE.md`

**Checklist Phase 0+1 (OBLIGATOIRE avant Phase 7) :**
- [ ] `git tag KB-WHISPER-1398` exécuté
- [ ] `extract_chapter_rules.py` créé avec 3× dirname
- [ ] `py extract_chapter_rules.py` → "62 règles chapitres sauvegardées" confirmé
- [ ] `KB_BACKUP_WHISPER_1398.json` créé

**⚠️ Writers KB à NE PAS lancer pendant la reconstruction :**
- `purge_kb.py` · `b05_lift_provisoire.py` · `b06_add_video10.py`
- `apply_ambigu_verdicts.py` · tout processeur après Phase 8

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Session S40 — TRADEX-AI — Reconstruction KB Phase 0+1.

Lire CLAUDE.md, DECISIONS_VEROUILLEES.md (D-S39-1 à D-S39-8),
et RAPPORT_C_CONSEQUENCES_S39.md avant toute action.

Verdict S39 : GO CONDITIONNEL — RISQUE MOYEN.
Première action : git tag KB-WHISPER-1398
Deuxième action : créer 05-saas\utils\extract_chapter_rules.py avec filtre
  `if "source_video_id" not in e` et BASE_DIR = 3× dirname.
Troisième action : py 05-saas\utils\extract_chapter_rules.py → vérifier "62".
```

---

## 12. ÉTAT KB

```
KNOWLEDGE_BASE_MASTER.json
  Règles totales    : 1398
  Format vidéo      : 1336 (source_video_id)
  Format chapitres  : 62 (14 id_brique + 48 id/contenu/source_origine)
  Catégories (11)   : saisonnalite · correlations · timing · indicateurs_tendance
                      indicateurs_momentum · gestion_risque_entree · gestion_position_active
                      structure_marche · macro_evenements · volume_liquidite · psychologie

SHA256_KB_MASTER.md
  Hash réel actuel  : bcaaaeed6267aa9c24cd092e6c18881acf726a5b8ed9d2c72c5c0a023bf3f773
  Hash "actif" reg. : 4cc9f77a... (OBSOLÈTE — à corriger Phase 9 après reconstruction)
  Vérification auto : AUCUNE (D-S31-12 non implémentée — registre manuel uniquement)

Sécurité reconstruction :
  Commit sauvegarde : 2d20750 (1398 règles — working tree propre)
  Restauration si nécessaire : git checkout 2d20750 -- 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json
  164 transcripts Whisper tracés git (double filet de sécurité)
```

---

*README S39 — TRADEX-AI — 29/06/2026*
*Prochaine session : S40 — Phase 0 reconstruction KB*
