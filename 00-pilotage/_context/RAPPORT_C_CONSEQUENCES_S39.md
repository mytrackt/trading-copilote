# RAPPORT C — CONSÉQUENCES RECONSTRUCTION KB — TRADEX-AI S39
> Date : 29/06/2026 | Claude Code → Cowork
> Pré-requis validés : Rapports A et B

---

## VERDICT FINAL

```
RISQUE GLOBAL       : MOYEN
RECOMMANDATION      : GO CONDITIONNEL
POINT DE NON-RETOUR : Phase 7 (premier save_kb_atomic)
```

---

## A — CE QUI SERA DÉTRUIT

### A1 — KNOWLEDGE_BASE_MASTER.json
- Règles écrasées : **1398**
- Détail par catégorie :
  - structure_marche 295 · indicateurs_tendance 247 · psychologie 242
  - gestion_risque_entree 188 · timing 106 · gestion_position_active 86
  - volume_liquidite 76 · indicateurs_momentum 56 · correlations 43
  - macro_evenements 36 · saisonnalite 23
- **Récupérable git : OUI à 100%** — commit 2d20750 (working tree propre)
- Restauration : `git checkout 2d20750 -- 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json`

### A2 — Règles chapitres (62)
- 62 règles = 14 `id_brique` + 48 `id`/`contenu`/`source_origine`
- Filtre corrigé `if "source_video_id" not in e` capture les 62 ✓ (après fix BASE_DIR 3× dirname)
- Sans Phase 0 : récupérables via git (commit 2d20750)
- Avec Phase 0 (backup JSON) : récupérables à 100%, indépendamment de git

### A3 — Transcripts Whisper
- 164 fichiers, tous tracés git (ls-files = 164)
- Archivés dans `_archive\whisper-lessons-elimine\` → double filet de sécurité

### A4 — MANIFESTE_TRANSCRITS.csv
- 110 lignes, pointe sur les .txt Whisper
- Après reconstruction : obsolète pour le flux Gemini. Reste valide comme registre Whisper.
- Le nouveau `transcript_processor_gemini.py` ne l'utilise pas.

---

## B — CE QUI VA CASSER IMMÉDIATEMENT

### B5 — claude_brain.py — NE CASSE PAS
- `load_kb_rules()` [l.201-243] : fallback `"KB non chargee"` si KB absente (pas d'exception)
- Écriture atomique garantit JSON toujours complet → JSONDecodeError impossible en pratique
- Lecture générique `for categorie, briques in aggregated.items()` → tolère n'importe quelles catégories

### B6 — SHA256_KB_MASTER.md oublié — AUCUN IMPACT RUNTIME
- Aucun code ne vérifie le SHA (M10 confirmé)
- TRADEX démarre même si registre désynchronisé
- Bloc `## Hash actif` déjà périmé (`4cc9f77a` vs réel `bcaaaeed`)

### B7 — Tests — NE CASSENT PAS
- Assertions `test_claude_brain.py` : structurelles uniquement (clés racine `{"rules","kb_provisoire","banniere"}`)
- Aucune assertion sur le nombre de règles ni sur le SHA
- 69/69 PASS attendus après reconstruction

### B8 — transcript_processor.py sans MANIFESTE
- `list_transcripts()` [l.173-175] : si MANIFESTE absent → `sys.exit(1)` (arrêt net, pas silencieux)
- ⚠️ **D17 confirmé** : `rebuild_aggregated()` [l.363] appelée après chaque vidéo, avant `save_kb_atomic()` [l.364]
  → Les 62 chapitres absents de `videos[]` sont effacés dès la 1ère vidéo traitée
  → **Parade** : KB_CHAPTER_RULES_BACKUP.json (Phase 0) = filet permanent

---

## C — CE QUI VA CHANGER

### C9 — Nombre de règles — AUCUN SEUIL
- Aucun `len(rules) >= N` dans le code. Moteur fonctionne avec N'IMPORTE quel compte.
- Objectif stratégie ≥800 règles — non mesurable a priori.

### C10 — Qualité des signaux
- Mécanisme : injection plein-texte KB dans le prompt Claude (pas de RAG)
- Si règles changent de contenu → signaux changent (non déterministe)

### C11 — Les 11 catégories — NON HARDCODÉES côté moteur
- `claude_brain.py` = lecture générique, aucune catégorie codée en dur
- Catégories hardcodées UNIQUEMENT dans `transcript_processor.py` (liste `CATEGORIES`) et `audit_kb.py`
- Le nouveau processeur doit conserver les 11 clés (conforme Phase 6)

### C12 — Mode Auto — RESTE BLOQUÉ
- `mode_auto_autorise = False` forcé dans tous les chemins [l.134, 166, 183, 193]
- Reconstruction KB n'affecte pas le blocage Auto (conforme D-F-07)

---

## D — RISQUES CACHÉS

### D13 — Writers KB à désactiver

| Fichier | Risque |
|---------|--------|
| `purge_kb.py` | 🔴 efface règles par texte exact |
| `b05_lift_provisoire.py` | 🔴 modifie MASTER |
| `b06_add_video10.py` | 🔴 modifie MASTER |
| `apply_ambigu_verdicts.py` | 🔴 `json.dump` + `os.replace` |
| `transcript_processor.py` (post-Ph.8) | 🔴 `rebuild_aggregated` efface chapitres |
| `audit_kb.py` | 🟡 écrit rapport (pas MASTER) |
| `validate_douteux.py` | 🟡 écrit KB_VALIDEE (pas MASTER) |
| `claude_brain.py` / `settings.py` | 🟢 lecture seule |

### D14 — Cache KB : AUCUN (pas de .pkl/.cache). Rien à invalider.

### D15 — Clés API : FRED/EIA/FINNHUB = 0 occurrence dans `transcript_processor.py`. Non bloquant.

### D16 — google SDK : `google-genai` déjà utilisé. FutureWarning non bloquant.

### D17 — 🔴 rebuild_aggregated() : RISQUE CRITIQUE

```python
# transcript_processor.py l.282-294
def rebuild_aggregated(kb: dict) -> None:
    agg = empty_rules()
    seen = {cat: set() for cat in CATEGORIES}
    for vid in kb["videos"].values():
        rules = vid.get("rules", {})
        for cat in CATEGORIES:
            for rule in rules.get(cat, []):
                key = rule.lower().strip()
                if key and key not in seen[cat]:
                    seen[cat].add(key); agg[cat].append(rule)
    kb["aggregated_rules"] = agg     # ← écrase TOUT, chapitres inclus
```

- Appelée [l.363] après CHAQUE vidéo, avant `save_kb_atomic()` [l.364]
- Fragilité permanente : toute exécution du processeur efface les chapitres
- **Parade** : `KB_CHAPTER_RULES_BACKUP.json` (Phase 0) → relancer `inject_chapter_rules.py` si nécessaire

---

## E — TABLEAU AVANT/APRÈS

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVANT RECONSTRUCTION              APRÈS RECONSTRUCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KB source         : Whisper        KB source         : Gemini multimodal
Règles totales    : 1398           Règles totales    : DONNÉES INSUFFISANTES (obj. ≥800)
Règles vidéo      : 1336           Règles vidéo      : DONNÉES INSUFFISANTES
Règles chapitres  : 62 (14+48)     Règles chapitres  : 62 (si Ph.0+Ph.8 OK)
SHA256 actif      : bcaaaeed...    SHA256 actif      : NOUVEAU (mise à jour manuelle)
Tests baseline    : 69/69 PASS     Tests             : 69/69 attendu
TRADEX démarre    : OUI            TRADEX démarre    : OUI (SHA = manuel)
Mode Auto         : BLOQUÉ         Mode Auto         : BLOQUÉ (inchangé)
Modules lisant KB : 8              Modules lisant KB : 8 (inchangé)
Writers à désactiver : 5           Writers à désactiver : 5 (inchangé)
Cache KB          : aucun          Cache à invalider  : aucun
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## F — VERDICT RISQUE

```
RISQUE GLOBAL       : MOYEN
  Reconstruction 100% réversible (git 2d20750 + 164 Whisper tracés + backup JSON Phase 0).
  Aucun gate de démarrage, aucun test dépendant du compte, Auto reste bloqué.
  MOYEN (pas FAIBLE) car : LLM non déterministe + dépendance YouTube (Phase 2 ≥60/110).

POINT DE NON-RETOUR : Phase 7 (1er save_kb_atomic)
  → Avant Phase 7 : rollback trivial (git checkout, KB jamais touchée)
  → Après Phase 7  : rollback via KB_BACKUP_WHISPER_1398.json ou git checkout 2d20750

BACKUP SUFFISANT    : NON (pas encore créé) → OUI une fois Phase 0+1 exécutées
  → git tag KB-WHISPER-1398     : ABSENT (à créer Ph.1 — PREMIÈRE ACTION)
  → KB_BACKUP_WHISPER_1398.json : ABSENT (à créer Ph.1)
  → KB_CHAPTER_RULES_BACKUP.json : sera créé en Phase 0
  → Filet existant immédiat     : commit 2d20750 + 164 Whisper tracés

MODULES À DÉSACTIVER pendant la reconstruction :
  → purge_kb.py, b05_lift_provisoire.py, b06_add_video10.py
  → apply_ambigu_verdicts.py
  → transcript_processor.py / _gemini APRÈS Phase 8 (rebuild_aggregated efface chapitres)

RECOMMANDATION      : GO CONDITIONNEL

CONDITIONS OBLIGATOIRES (dans l'ordre) :
  1. Phase 0 AVANT TOUT : backup 62 chapitres (script 3× dirname) — vérifier "62"
  2. Phase 1 AVANT Phase 7 : git tag KB-WHISPER-1398 + KB_BACKUP_WHISPER_1398.json
  3. Bug BASE_DIR corrigé dans extract/inject (3× dirname — CRITIQUE)
  4. Phase 4 : changer VIDEO_DIR ET OUTPUT_DIR dans gemini_transcriber.py
  5. Phase 8 = DERNIÈRE écriture KB — ne relancer aucun processeur après
  6. Phase 2 gate : si <60/110 vidéos dispo → re-décision Abdelkrim

PREMIÈRE COMMANDE DANS POWERSHELL (C:\trading-copilote) :
  git tag KB-WHISPER-1398
```

---

*Rapport C — 3/3 — Produit par Claude Code S39 — 29/06/2026*
*Aucun fichier modifié par ce prompt.*
