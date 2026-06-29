# PROMPT B — AUDIT DES 10 PHASES
> Cowork → Claude Code | S39 | 29/06/2026
> Étape 2/3 — À lancer UNIQUEMENT après validation du Rapport A par Abdelkrim

---

## PRÉ-REQUIS

Avant de commencer, confirmer :
- Le Rapport A a été produit et validé par Abdelkrim
- Aucun bloquant marqué dans le Rapport A

Si un bloquant existe → STOP. Ne pas continuer.

---

## TA MISSION

Challenger chaque phase de la stratégie en 10 phases contre le code réel.
Pour chaque phase : CONFIRMÉE / À CORRIGER / BLOQUÉE + citation de code exacte.

Tu t'appuies sur les mesures du Rapport A (déjà connues).
Tu lis uniquement les fichiers nécessaires pour répondre aux questions ci-dessous.

---

## FICHIERS À LIRE (selon besoin)

```
C:\trading-copilote\05-saas\utils\gemini_transcriber.py
C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py
C:\trading-copilote\05-saas\engine\claude_brain.py
C:\trading-copilote\05-saas\knowledge_base\purge_kb.py
C:\trading-copilote\05-saas\knowledge_base\audit_kb.py
C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv
```

---

## AUDIT PHASE PAR PHASE

### PHASE 0 — Sauvegarder les règles chapitres

Q0.1 — Le script `extract_chapter_rules.py` existe-t-il ?
(réponse connue depuis Rapport A — confirmer)

Q0.2 — Si MANQUANT : le code fourni ci-dessous est-il syntaxiquement correct ?
Lancer : `py -m py_compile` sur ce code temporairement sauvegardé.

⚠️ CORRECTION RAPPORT A — La KB contient 62 règles chapitres (pas 14) :
  - 14 règles format `id_brique`
  - 48 règles format `id`/`contenu`/`source_origine` (3e format)
  Le filtre correct = tout ce qui N'A PAS `source_video_id` (= non vidéo = chapitre).

```python
# Code CORRIGÉ à valider (ne PAS l'exécuter — juste py_compile)
import json, os, pathlib
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_FILE     = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")
with open(KB_FILE, encoding="utf-8") as f:
    kb = json.load(f)
chapters = {}
count = 0
for cat, entries in kb.get("aggregated_rules", {}).items():
    for e in entries:
        # FILTRE CORRIGÉ : tout ce qui n'est pas une règle vidéo = chapitre
        if "source_video_id" not in e:
            if cat not in chapters:
                chapters[cat] = []
            chapters[cat].append(e)
            count += 1
tmp = pathlib.Path(BACKUP_FILE).with_suffix(".tmp")
with open(tmp, "w", encoding="utf-8") as f:
    json.dump({"chapter_rules": chapters, "total": count}, f, ensure_ascii=False, indent=2)
tmp.replace(BACKUP_FILE)
print(f"OK — {count} règles chapitres sauvegardées")
# Résultat attendu : 62 (14 id_brique + 48 format id/contenu)
```

Q0.3 — Confirmer que le script capture bien 62 règles (pas 14).
Vérifier que les 2 formats (id_brique et id/contenu) sont tous les deux présents dans le backup JSON.

**VERDICT PHASE 0 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 1 — Archivage

Q1.1 — `git tag KB-WHISPER-1398` existe-t-il ? (depuis Rapport A)
Q1.2 — `KB_BACKUP_WHISPER_1398.json` existe-t-il ? (depuis Rapport A)
Q1.3 — `_archive\whisper-lessons-elimine\` existe-t-il ? (depuis Rapport A)
Q1.4 — Y a-t-il un risque à archiver les transcripts Whisper maintenant ?
  → Vérifier : `transcript_processor.py` utilise-t-il `transcripts/` en dur ?
  → Lire les lignes 44-50 de `transcript_processor.py` et citer exactement.

**VERDICT PHASE 1 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 2 — Pre-check YouTube

Q2.1 — yt-dlp installé ? Version ? (depuis Rapport A)
Q2.2 — IDs YouTube = 11 chars confirmé ? (depuis Rapport A)
Q2.3 — IDs commençant par `-` : la syntaxe `yt-dlp -- {ID}` est-elle documentée dans yt-dlp ?

```powershell
yt-dlp --help | Select-String "\-\-" | Select-Object -First 5
```

Q2.4 — La commande `--simulate` existe-t-elle dans yt-dlp ?
```powershell
yt-dlp --help | Select-String "simulate"
```

**VERDICT PHASE 2 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]
→ Si yt-dlp absent → BLOQUÉE — STOP

---

### PHASE 3 — Téléchargement MP4

Q3.1 — D:\ existe-t-il ? Espace libre suffisant pour 110 MP4 ? (depuis Rapport A)
Q3.2 — `D:\Belkhayate-Lessons-MP4\` vs `D:\Belkhayate-Videos\` : noms différents = pas de conflit ?

```powershell
Test-Path "D:\Belkhayate-Lessons-MP4"
Test-Path "D:\Belkhayate-Videos"
```

Q3.3 — La syntaxe yt-dlp suivante est-elle valide ?
```
bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]
```
Vérifier dans `yt-dlp --help | Select-String "format"` si cette syntaxe est supportée.

**VERDICT PHASE 3 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 4 — Transcription Gemini

Q4.1 — Lire `gemini_transcriber.py` : quelle est la valeur exacte de `VIDEO_DIR` ? (citer la ligne)
Q4.2 — Quelle est la valeur exacte de `OUTPUT_DIR` ? (citer la ligne)
Q4.3 — Le script peut-il pointer vers `D:\Belkhayate-Lessons-MP4\` en modifiant UNIQUEMENT `VIDEO_DIR` ?
  → Y a-t-il d'autres références hardcodées à `D:\Belkhayate-Videos` dans le script ?
  ```powershell
  Select-String -Path "C:\trading-copilote\05-saas\utils\gemini_transcriber.py" -Pattern "Belkhayate-Videos"
  ```
Q4.4 — La fonction `_chemin_upload()` est-elle présente ? Citer les lignes exactes.
Q4.5 — Le checkpoint `if out_path.exists()` est-il présent ? Citer les lignes exactes.
Q4.6 — La limite de chunking est-elle ≤ 57 min ? Citer la constante exacte dans le code.
Q4.7 — google-generativeai : installé et fonctionnel ? (depuis Rapport A — si BLOQUANT → STOP)

**VERDICT PHASE 4 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 5 — Décontamination OFTC

Q5.1 — Rapport A M3 confirme 21 fichiers OFTC (pas 5 comme prévu initialement).
Lister leurs noms exacts :

```powershell
Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" |
  Where-Object { $_.Name -like "*OFTC*" -or $_.Name -like "*Order Flow*" } |
  Select-Object Name | Sort-Object Name
```

→ Confirmer : 21 fichiers OFTC Lesson 1→20 présents.

Q5.2 — Y a-t-il d'autres fichiers visiblement non-Belkhayate au-delà des 21 OFTC ?

```powershell
Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" |
  Where-Object { $_.Name -notlike "*Belkhayate*" -and $_.Name -notlike "*belkhayate*" } |
  Select-Object Name | Sort-Object Name
```

→ Signaler tout fichier dont le nom n'est visiblement pas un titre Belkhayate.

**VERDICT PHASE 5 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 6 — transcript_processor_gemini.py

Q6.1 — Lire `transcript_processor.py` lignes 44-55 : citer TRANSCRIPTS_DIR et MANIFEST_FILE exactement.
Q6.2 — Combien d'occurrences de MANIFEST_FILE dans le fichier ?

```powershell
Select-String -Path "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py" -Pattern "MANIFEST_FILE" | Select-Object LineNumber, Line
```

Q6.3 — Le format de sortie JSON (clés : regle, statut, source_video_id, confiance, categorie, note) :
  Lire `claude_brain.py` → quelle fonction charge la KB ? Citer le code exact.
  Ces clés sont-elles toutes lues par `claude_brain.py` ou seulement certaines ?

Q6.4 — `load_kb_rules()` dans `claude_brain.py` : existe-t-elle ? Gère-t-elle les 2 formats (id_brique + source_video_id) ?
  Citer le code exact de cette fonction.

Q6.5 — `purge_kb.py` : que fait-il exactement ? Peut-il effacer des règles de la KB reconstruite si lancé accidentellement ?
  Lire les 30 premières lignes de `purge_kb.py`.

**VERDICT PHASE 6 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 7 — Reconstruction KB

Q7.1 — `transcript_processor.py` : combien d'appels API Claude par vidéo ? (lire la boucle principale)
Q7.2 — Y a-t-il un rate limiting (time.sleep) entre les appels ? Citer la ligne.
Q7.3 — La clé `ANTHROPIC_API_KEY` est-elle dans `.env` ? (depuis Rapport A)
Q7.4 — Les 3 clés manquantes (FRED, EIA, FINNHUB) bloquent-elles `transcript_processor.py` ou seulement le moteur live ?
  ```powershell
  Select-String -Path "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py" -Pattern "FRED|EIA|FINNHUB"
  ```
Q7.5 — `transcript_processor.py` produit-il un checkpoint (skip vidéos déjà traitées) ? Citer la ligne.

**VERDICT PHASE 7 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 8 — Réinjection chapitres

Q8.1 — `inject_chapter_rules.py` existe-t-il ? (depuis Rapport A)
Q8.2 — Le code fourni est-il syntaxiquement correct ? (py_compile)

```python
# Code à valider
import json, os, pathlib
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_FILE     = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")
with open(KB_FILE, encoding="utf-8") as f:
    kb = json.load(f)
with open(BACKUP_FILE, encoding="utf-8") as f:
    backup = json.load(f)
injected = 0
for cat, entries in backup.get("chapter_rules", {}).items():
    if cat not in kb["aggregated_rules"]:
        kb["aggregated_rules"][cat] = []
    kb["aggregated_rules"][cat].extend(entries)
    injected += len(entries)
tmp = pathlib.Path(KB_FILE).with_suffix(".tmp")
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(kb, f, ensure_ascii=False, indent=2)
tmp.replace(KB_FILE)
print(f"OK — {injected} règles réinjectées")
```

Q8.3 — `load_kb_rules()` dans `claude_brain.py` lira-t-elle les règles `id_brique` réinjectées ?
(basé sur Q6.4 — confirmer OUI/NON)

**VERDICT PHASE 8 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 9 — Mise à jour SHA256

Q9.1 — Confirmer : aucun code dans `claude_brain.py` ne vérifie le SHA256 automatiquement ? (depuis Rapport A M10)
Q9.2 — `SHA256_KB_MASTER.md` : la procédure PowerShell de mise à jour est-elle correcte ?

```powershell
# Procédure proposée par Cowork — valider la syntaxe :
$hash = (Get-FileHash "C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json" -Algorithm SHA256).Hash
Write-Host "Nouveau SHA256 : $hash"
```

Q9.3 — `SHA256_KB_MASTER.md` : quel est le format du tableau ? La procédure de mise à jour manuelle est-elle claire ?
Lire les 5 dernières lignes du fichier.

**VERDICT PHASE 9 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

### PHASE 10 — Tests

Q10.1 — Nombre total de fonctions test trouvées ? (depuis Rapport A M6)
Q10.2 — Y a-t-il une fonction test qui vérifie le nombre de règles ou le SHA256 ?

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\test_claude_brain.py" -Pattern "sha256|hash|nb_rules|count|total|1398|1300" -CaseInsensitive | Select-Object LineNumber, Line
```

Q10.3 — Rapport A M6 confirme : 69/69 PASS (pas 37 comme prévu initialement). C'est le baseline.
  → La cible après reconstruction est 69/69 PASS.

Q10.4 — Y a-t-il des tests qui vont nécessairement échouer si le nombre de règles change ?
  Citer les assertions numériques dans `test_claude_brain.py` :

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\test_claude_brain.py" `
  -Pattern "assert|assertEqual|>=|rules|count|total|1398|1300|minimum" -CaseInsensitive |
  Select-Object LineNumber, Line
```

Q10.5 — Note Rapport A : `apply_ambigu_verdicts.py` dans `04-cerveau-trading\` lit aussi la KB.
  Peut-il modifier la KB ? Vérifier :

```powershell
Select-String -Path "C:\trading-copilote\04-cerveau-trading\apply_ambigu_verdicts.py" `
  -Pattern "json.dump|open.*w|replace|atomic" | Select-Object LineNumber, Line
```

→ Si ÉCRITURE → l'ajouter à la liste "à désactiver" pendant reconstruction.

**VERDICT PHASE 10 :** [CONFIRMÉE / À CORRIGER / BLOQUÉE]

---

## FORMAT DU RAPPORT B

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPPORT B — AUDIT DES 10 PHASES — TRADEX-AI S39
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VERDICT GLOBAL    : [CONFIRMÉE / AMENDÉE / BLOQUÉE]
PHASES CONFIRMÉES : [liste]
PHASES À CORRIGER : [liste + correction exacte par phase]
PHASES BLOQUÉES   : [liste + raison]

━━━ DÉTAIL PAR PHASE ━━━

PHASE 0 : [CONFIRMÉE / À CORRIGER / BLOQUÉE]
  Preuve : [citation de code ou mesure]
  Correction : [si nécessaire]

PHASE 1 : ...
PHASE 2 : ...
PHASE 3 : ...
PHASE 4 : ...
PHASE 5 : ...
PHASE 6 : ...
PHASE 7 : ...
PHASE 8 : ...
PHASE 9 : ...
PHASE 10 : ...

━━━ RISQUES NON VUS PAR COWORK ━━━
[Ce que tu as trouvé en lisant le code que Cowork n'avait pas anticipé]

━━━ ORDRE D'EXÉCUTION FINAL CORRIGÉ ━━━
[Séquence des 10 phases avec les corrections appliquées]
[Commande exacte pour chaque phase]

━━━ PRÊT POUR PROMPT C ? ━━━
[OUI — audit terminé, aucun bloquant / NON — voir phases bloquées]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## RÈGLES ABSOLUES

- Citer les lignes exactes du code pour chaque CONFIRMÉE ou CORRECTION
- Ne jamais inventer une fonction ou un mécanisme non trouvé dans le code
- Si un fichier est illisible ou vide → le signaler
- Ne modifier aucun fichier dans ce prompt

---

*Prompt B — 2/3 — Cowork S39 — 29/06/2026*
*Pré-requis : Rapport A validé par Abdelkrim*
