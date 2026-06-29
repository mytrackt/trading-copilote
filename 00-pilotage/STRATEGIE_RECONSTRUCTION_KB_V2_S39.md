# STRATÉGIE INFAILLIBLE — Reconstruction KB TRADEX-AI
> Version 2 — Cowork S39 | 28/06/2026 | Analyse profonde complète

---

## 1. CAUSES RACINES (6 identifiées)

| ID | Cause | Impact |
|----|-------|--------|
| RC-1 | Whisper = audio-only, méthode éliminée (D-S30-9) | 1384 règles vidéo potentiellement incomplètes |
| RC-2 | MP4 Lessons inexistants localement (D:\ = corpus épisodes) | Oblige re-téléchargement depuis YouTube |
| RC-3 | Corpus Gemini existant contaminé (5 fichiers OFTC) | Ces règles ne doivent jamais entrer dans la KB |
| RC-4 | Prompt [REGLE:] trop permissif (capturait prop firms) | Règles parasites dans KB actuelle |
| RC-5 | KB a 2 sources distinctes (vidéos + chapitres) | 14 règles chapitres précieuses à préserver |
| RC-6 | transcript_processor.py couplé à MANIFESTE Whisper | Le pipeline KB doit être adapté pour Gemini |

---

## 2. CONTRAINTES TECHNIQUES

| Contrainte | Détail |
|---|---|
| KB structure | 2 formats coexistants : `source_video_id` (vidéos) + `id_brique` (chapitres) |
| 14 règles chapitres | Contenu riche : COG structure · Timing oscillateur · Setup 3 confluences · Objectifs OBJ1/2/3 |
| 11 catégories KB | Fixes et verrouillées — jamais modifier les clés |
| transcript_processor.py | Lit MANIFESTE_TRANSCRITS.csv → `transcripts/` (Whisper) → doit être adapté |
| SHA256 (D-S31-12) | KB_HASH.txt doit être mis à jour sinon TRADEX refuse de démarrer |
| Gemini Files API | Limite 1M tokens ≈ 57 min vidéo → chunking auto déjà en place |
| yt-dlp | Installé sur Windows (a déjà servi pour les MP3) — vérifier version |
| YouTube | Peut bloquer les téléchargements en masse — rate limiting obligatoire |

---

## 3. RESSOURCES DISPONIBLES

| Ressource | Localisation | État |
|---|---|---|
| 110 IDs YouTube | Dans les noms des MP3 (11 premiers chars) | Disponibles |
| gemini_transcriber.py | 05-saas\utils\ | Validé, opérationnel |
| transcript_processor.py | 05-saas\knowledge_base\ | Opérationnel — à adapter |
| 14 règles chapitres | Dans KB actuelle (format id_brique) | À extraire AVANT tout |
| 121 transcripts Gemini épisodes | transcripts-gemini\ | Disponibles (après décontamination OFTC) |
| KB_BACKUP à créer | 04-cerveau-trading\ | Action Phase 1 |
| GEMINI_API_KEY | .env | Présente et valide |
| yt-dlp | Windows PATH | À vérifier |

---

## 4. MATRICE DES RISQUES (14 risques)

| ID | Risque | Prob | Sévérité | Mesure corrective |
|----|--------|------|----------|-------------------|
| R1 | Certaines Lessons supprimées de YouTube | MOYENNE | HAUTE | Pre-check `--simulate` avant tout téléchargement |
| R2 | YouTube bloque les téléchargements en masse | MOYENNE | MOYENNE | Rate limit 3M/s + délai 5s entre vidéos |
| R3 | yt-dlp non installé ou obsolète | FAIBLE | HAUTE | Vérifier + `pip install yt-dlp` si besoin |
| R4 | MP4 trop longs (> 57 min) → dépassement Gemini | FAIBLE | MOYENNE | gemini_transcriber.py gère le chunking auto |
| R5 | 14 règles chapitres perdues lors reconstruction | HAUTE si non géré | CRITIQUE | Extraire en JSON séparé AVANT toute action |
| R6 | KB_HASH.txt non mis à jour → TRADEX bloqué | CERTAINE si oubli | HAUTE | Étape dédiée dans le plan (Phase 9) |
| R7 | transcript_processor.py incompatible Gemini | MOYENNE | HAUTE | Créer `transcript_processor_gemini.py` adapté |
| R8 | MANIFESTE Whisper pointe sur anciens fichiers | CERTAINE | HAUTE | Nouveau processeur sans MANIFESTE |
| R9 | 37 tests échouent après reconstruction | FAIBLE | HAUTE | Relancer tests obligatoires Phase 10 |
| R10 | Règles OFTC entrent dans la KB | HAUTE si non géré | CRITIQUE | Décontamination avant intégration (Phase 7) |
| R11 | Coût Gemini dépassé | FAIBLE | FAIBLE | Estimé $5-12 pour 110 vidéos |
| R12 | Moins de règles qu'avant (régression) | POSSIBLE | MOYENNE | Objectif : qualité > quantité (800 règles qualifiées BK > 1398 non filtrées) |
| R13 | crash batch Gemini en cours de route | FAIBLE | FAIBLE | Checkpoint existant → relançable sans perte |
| R14 | Nouveau format Gemini incompatible avec load_kb_rules() | FAIBLE | HAUTE | Utiliser les mêmes 11 clés + format JSON identique |

---

## 5. STRATÉGIE — 10 PHASES SÉQUENTIELLES

---

### ━━ PHASE 0 ━━ SAUVEGARDER LES 14 RÈGLES CHAPITRES (priorité absolue)
> Durée : 5 min | Exécutant : Claude Code

**Pourquoi en premier :** Ces 14 règles (COG, Timing, Setup 3 confluences, OBJ1/2/3) sont les règles les plus précises de la KB. Elles ont été extraites manuellement depuis les chapitres Belkhayate (Chap5, Chap9). Si la KB est reconstruite sans elles, c'est une perte irréversible.

**Action :**
```python
# Script : 05-saas\utils\extract_chapter_rules.py
# Lit KNOWLEDGE_BASE_MASTER.json
# Filtre les règles avec clé 'id_brique' (format chapitre)
# Sauvegarde dans : 04-cerveau-trading\KB_CHAPTER_RULES_BACKUP.json
# Format conservé intact (ne pas modifier la structure)
```

**Vérification :** 14 règles sauvegardées dans KB_CHAPTER_RULES_BACKUP.json ✓

---

### ━━ PHASE 1 ━━ ARCHIVAGE COMPLET (sécurité)
> Durée : 5 min | Exécutant : Claude Code (1 commande à la fois)

```powershell
git tag KB-WHISPER-1398
```
```powershell
copy C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json C:\trading-copilote\04-cerveau-trading\KB_BACKUP_WHISPER_1398.json
```
```powershell
# Archiver les transcripts Whisper (ne pas supprimer — déplacer)
mkdir C:\trading-copilote\_archive\whisper-lessons-elimine
move C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\*.txt C:\trading-copilote\_archive\whisper-lessons-elimine\
```

**Vérification :** git tag listé · KB_BACKUP.json présent · dossier whisper archivé ✓

---

### ━━ PHASE 2 ━━ PRE-CHECK YOUTUBE (évite téléchargements inutiles)
> Durée : 15-30 min | Exécutant : Claude Code

**Extraire les 110 IDs YouTube** depuis les noms MP3 (les 11 premiers caractères) :
```python
# Script : 05-saas\utils\check_youtube_availability.py
# Pour chaque MP3 → extraire l'ID (stem[:11])
# yt-dlp --simulate --no-warnings {ID} → AVAILABLE ou UNAVAILABLE
# Génère : availability_report.json
# Catégories : AVAILABLE / PRIVATE / DELETED / AGE_RESTRICTED / ERROR
```

**Note importante sur les IDs :**
Certains IDs commencent par `-` (ex: `-OIGv5rLLV8`). yt-dlp les accepte via :
`yt-dlp -- {ID}` (le `--` empêche l'interprétation du tiret comme option)

**Résultat attendu :** Liste des vidéos disponibles vs indisponibles.
Si < 60 disponibles → décider avec Abdelkrim si on continue ou on adapte.

---

### ━━ PHASE 3 ━━ TÉLÉCHARGEMENT MP4 LESSONS
> Durée : 2-5h selon connexion | Exécutant : Claude Code + PowerShell

**Dossier de destination (NOUVEAU — séparé des épisodes) :**
`D:\Belkhayate-Lessons-MP4\` (sur D:\ rebranché)

**Commande yt-dlp optimisée :**
```powershell
# Pour chaque ID AVAILABLE issu du rapport Phase 2
yt-dlp `
  --format "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]" `
  --output "D:\Belkhayate-Lessons-MP4\%(id)s_%(title)s.%(ext)s" `
  --limit-rate 5M `
  --sleep-interval 5 `
  --retries 3 `
  --continue `
  -- {YOUTUBE_ID}
```

**Points de sécurité :**
- `--continue` : reprend les téléchargements interrompus (crash-safe)
- `--sleep-interval 5` : 5s entre chaque vidéo (anti-blocage YouTube)
- `--limit-rate 5M` : évite la saturation réseau
- `--` avant l'ID : gère les IDs commençant par `-`

**Vérification :** Compter les MP4 dans D:\Belkhayate-Lessons-MP4\ = nombre attendu ✓

---

### ━━ PHASE 4 ━━ TRANSCRIPTION GEMINI MULTIMODAL
> Durée : 3-8h selon nb vidéos | Exécutant : Claude Code

**Modifier temporairement `gemini_transcriber.py` :**
```python
# Changer UNIQUEMENT VIDEO_DIR et OUTPUT_DIR
VIDEO_DIR = Path(r"D:\Belkhayate-Lessons-MP4")
OUTPUT_DIR = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini-lessons")
```

**Important :**
- Nouveau dossier `transcripts-gemini-lessons\` (SÉPARÉ de `transcripts-gemini\` qui contient les épisodes)
- Le checkpoint `if out_path.exists(): SKIP` protège contre les crashes
- Tester sur 1 seul MP4 avant le batch complet

**Vérification :** Présence de [VISUEL:] ET [REGLE:] dans les sorties → méthode multimodale confirmée ✓

---

### ━━ PHASE 5 ━━ DÉCONTAMINATION CORPUS GEMINI ÉPISODES
> Durée : 10 min | Exécutant : Claude Code

Déplacer les 5 fichiers OFTC hors du corpus :
```powershell
mkdir C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini\_EXCLURE
```
Fichiers à déplacer :
- `OFTC Lesson 4 - Order Flow Terms_gemini.txt`
- `OFTC Lesson 11 - Order Flow Price Rejection_gemini.txt`
- `OFTC Lesson 16 - Order Flow Reversal Setups_gemini.txt`
- `OFTC Lesson 17 - Order Flow Continuation Setups_gemini.txt`
- `OFTC Lesson 19 Part A..._gemini.txt`

**Vérification :** Aucun fichier `OFTC` dans `transcripts-gemini\` ✓

---

### ━━ PHASE 6 ━━ ADAPTER LE PIPELINE KB
> Durée : 30 min | Exécutant : Claude Code

**Problème :** `transcript_processor.py` lit depuis `transcripts/` via `MANIFESTE_TRANSCRITS.csv`.
Le nouveau corpus Gemini est dans `transcripts-gemini-lessons/` sans manifeste.

**Solution : Créer `transcript_processor_gemini.py`** (copie adaptée — NE PAS modifier l'original) :

Modifications :
```python
# 1. Supprimer la dépendance au MANIFESTE
# 2. Changer TRANSCRIPTS_DIR vers transcripts-gemini-lessons\
TRANSCRIPTS_DIR = PROJECT_ROOT / "03-transcriptions" / "nouvelles-sources" / "belkhayate-youtube" / "transcripts-gemini-lessons"
# 3. Lire tous les .txt du dossier directement (sans filtre fiabilite==VALIDE)
# 4. Conserver les 11 catégories identiques
# 5. Conserver le format de sortie identique (source_video_id, confiance, etc.)
# 6. Conserver l'écriture atomique et le checkpoint
```

**Vérification :** `py -m py_compile transcript_processor_gemini.py` → 0 erreur ✓

---

### ━━ PHASE 7 ━━ RECONSTRUCTION KB
> Durée : 2-4h (appels Claude API) | Exécutant : Claude Code

```powershell
py 05-saas\knowledge_base\transcript_processor_gemini.py
```

**Surveillance :**
- Règles ajoutées après chaque vidéo (log en temps réel)
- Si erreur API → retry automatique (déjà en place)
- Sauvegarde atomique après chaque vidéo (pas de perte si crash)

**Objectif :** ≥ 800 règles BK qualifiées (qualité > quantité)

---

### ━━ PHASE 8 ━━ RÉINJECTION DES 14 RÈGLES CHAPITRES
> Durée : 5 min | Exécutant : Claude Code

```python
# Script : 05-saas\utils\inject_chapter_rules.py
# Charge KB_CHAPTER_RULES_BACKUP.json (Phase 0)
# Charge KNOWLEDGE_BASE_MASTER.json reconstruit (Phase 7)
# Merge les 14 règles chapitres dans les catégories correspondantes
# Sauvegarde atomique (tempfile + os.replace)
```

**Vérification :** Règles totales = règles Gemini + 14 chapitres ✓

---

### ━━ PHASE 9 ━━ MISE À JOUR SHA256 + KB_HASH.txt
> Durée : 2 min | Exécutant : Claude Code

**CRITIQUE — sans cette étape, TRADEX refuse de démarrer (D-S31-12)**

```python
import hashlib, json
with open(r"C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json", "rb") as f:
    sha256 = hashlib.sha256(f.read()).hexdigest()
with open(r"C:\trading-copilote\04-cerveau-trading\KB_HASH.txt", "w") as f:
    f.write(sha256)
print(f"Nouveau SHA256 : {sha256[:8]}...")
```

Mettre à jour aussi `SHA256_KB_MASTER.md`.

**Vérification :** KB_HASH.txt contient le nouveau hash ✓

---

### ━━ PHASE 10 ━━ VALIDATION FINALE + COMMIT
> Durée : 15 min | Exécutant : Claude Code

```powershell
# Tests obligatoires
py -m pytest 05-saas\tests\ -v
```
→ 37/37 PASS obligatoire avant commit.

```powershell
git add .
```
→ Attendre confirmation
```powershell
git commit -m "feat(kb): reconstruction KB Gemini multimodal - Lessons corpus"
```
→ Attendre confirmation
```powershell
git push origin main
```

---

## 6. ARCHITECTURE FINALE KB

```
KNOWLEDGE_BASE_MASTER.json
├── metadata (videos_processed, date, sha256...)
├── videos (liste des vidéos sources)
└── aggregated_rules (11 catégories)
    ├── règles Gemini multimodal Lessons (format source_video_id) ← NOUVELLES
    ├── règles Gemini multimodal Épisodes ← PHASE ULTÉRIEURE (après décontamination)
    └── règles chapitres Chap5/Chap9 (format id_brique) ← PRÉSERVÉES Phase 0
```

---

## 7. PLAN DE VALIDATION

| Phase | Mesure | Seuil GO |
|---|---|---|
| Phase 0 | Règles chapitres sauvegardées | 14 règles dans JSON ✓ |
| Phase 2 | Vidéos disponibles YouTube | ≥ 60/110 pour continuer |
| Phase 4 | Qualité transcriptions | [VISUEL:] présent + [REGLE:] présent |
| Phase 7 | Règles reconstruites | ≥ 800 règles BK qualifiées |
| Phase 8 | Chapitres réinjectés | Total = Gemini + 14 |
| Phase 9 | SHA256 mis à jour | KB_HASH.txt ≠ bcaaaeed |
| Phase 10 | Tests | 37/37 PASS strict |

---

## 8. OBSTACLES ET MESURES CORRECTIVES

| Obstacle | Détection | Mesure |
|---|---|---|
| < 60 vidéos disponibles YouTube | Phase 2 pre-check | Décision Abdelkrim : continuer ou re-chercher les MP4 |
| YouTube bloque yt-dlp | Erreur 403/429 en Phase 3 | Réduire rate-limit + augmenter sleep-interval |
| Gemini tronque une transcription | Absence de [FIN] dans output | Re-transcrire cette vidéo uniquement (checkpoint SKIP protège les autres) |
| transcript_processor_gemini.py génère 0 règle | Phase 7 log | Vérifier format des transcripts Gemini + adapter le parsing |
| 37 tests échouent | Phase 10 pytest | Identifier le test en échec → corriger → relancer (ne pas committer si tests KO) |
| Règles chapitres absentes après réinjection | Compter règles format id_brique | Relancer inject_chapter_rules.py |

---

## 9. RÉSUMÉ EXÉCUTIF

```
PROBLÈME  : KB 1398 règles construite sur Whisper (méthode éliminée)
            + 14 règles chapitres précieuses à préserver
            + Corpus Gemini existant contaminé (OFTC)
            + Pipeline KB couplé à Whisper

SOLUTION  : Reconstruire depuis zéro avec Gemini multimodal (méthode validée D-F-06)
            en préservant les 14 règles chapitres

SÉQUENCE  :
  Ph.0  Sauvegarder 14 règles chapitres (JSON séparé)           ← 5 min
  Ph.1  Archiver KB Whisper + transcripts Whisper               ← 5 min
  Ph.2  Pre-check disponibilité 110 Lessons sur YouTube         ← 30 min
  Ph.3  Télécharger MP4 disponibles (yt-dlp)                   ← 2-5h
  Ph.4  Transcrire avec gemini_transcriber.py (multimodal)     ← 3-8h
  Ph.5  Décontaminer corpus Gemini épisodes (OFTC)             ← 10 min
  Ph.6  Créer transcript_processor_gemini.py                   ← 30 min
  Ph.7  Reconstruire KB                                         ← 2-4h
  Ph.8  Réinjecter 14 règles chapitres                         ← 5 min
  Ph.9  Mettre à jour SHA256 + KB_HASH.txt                     ← 2 min
  Ph.10 37 tests PASS + commit                                  ← 15 min

RÉSULTAT  : KB propre · Gemini multimodal · chapitres préservés · tests PASS
DURÉE TOT : 8-18h (selon connexion et nb vidéos disponibles)
```

---

*TRADEX-AI · Stratégie KB V2 · S39 · 28/06/2026*
*Décision clé : Phase 2 pre-check détermine la viabilité avant tout téléchargement*
