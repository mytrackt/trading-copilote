# PROMPT A — ÉTAT DES LIEUX
> Cowork → Claude Code | S39 | 29/06/2026
> Étape 1/3 — Lis, mesure, rapporte. N'audite rien encore.

---

## TA MISSION UNIQUE

Collecter les faits réels du projet TRADEX-AI avant tout audit.
**Tu ne dois PAS auditer, corriger, ni proposer de solution dans ce prompt.**
Tu lis, tu exécutes, tu rapportes les chiffres. Rien d'autre.

Si tu trouves un bloquant → le signaler clairement et STOPPER.
Abdelkrim valide le rapport A avant de te donner le Prompt B.

---

## LECTURE OBLIGATOIRE (ordre strict)

```
1. C:\trading-copilote\CLAUDE.md
2. C:\trading-copilote\00-pilotage\DECISIONS_VEROUILLEES.md
3. C:\trading-copilote\00-pilotage\DETTE_TECHNIQUE.md
4. C:\trading-copilote\00-pilotage\STRATEGIE_RECONSTRUCTION_KB_V2_S39.md
```

---

## MESURES À EFFECTUER

### M1 — Structure de la KB

```python
import json
with open(r"C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json") as f:
    kb = json.load(f)

rules = kb.get("aggregated_rules", {})
total = sum(len(v) for v in rules.values())
video_fmt = chap_fmt = autre = 0
for cat, entries in rules.items():
    for e in entries:
        if "id_brique" in e:
            chap_fmt += 1
        elif "source_video_id" in e:
            video_fmt += 1
        else:
            autre += 1

print(f"TOP KEYS KB         : {list(kb.keys())}")
print(f"CATÉGORIES (11?)    : {list(rules.keys())}")
print(f"RÈGLES TOTALES      : {total}")
print(f"Format source_video_id : {video_fmt}")
print(f"Format id_brique       : {chap_fmt}")
print(f"Format autre           : {autre}")
print(f"\nDÉTAIL PAR CATÉGORIE :")
for cat, entries in rules.items():
    print(f"  {cat} : {len(entries)} règles")

print(f"\nRÈGLES CHAPITRES (id_brique) :")
for cat, entries in rules.items():
    for e in entries:
        if "id_brique" in e:
            print(f"  [{cat}] {e.get('regle','')[:100]}")
```

### M2 — SHA256 actuel

```python
import hashlib
with open(r"C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json", "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()
print(f"SHA256 réel KB : {sha}")
```

```powershell
# Contenu du registre SHA256_KB_MASTER.md
Get-Content "C:\trading-copilote\04-cerveau-trading\SHA256_KB_MASTER.md" | Select-Object -Last 10
```

→ Le SHA256 réel correspond-il au "Hash actif" dans SHA256_KB_MASTER.md ? OUI / NON

### M3 — Corpus audio et transcripts

```powershell
$audio = (Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio" -Filter "*.mp3" -ErrorAction SilentlyContinue).Count
$whisper = (Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts" -Filter "*.txt" -ErrorAction SilentlyContinue).Count
$gemini = (Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" -Filter "*.txt" -ErrorAction SilentlyContinue).Count
Write-Host "MP3 (Lessons)         : $audio"
Write-Host "Transcripts Whisper   : $whisper"
Write-Host "Transcripts Gemini    : $gemini"
```

```powershell
# Fichiers OFTC dans transcripts-gemini
Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" |
  Where-Object { $_.Name -like "*OFTC*" -or $_.Name -like "*Order Flow*" } |
  Select-Object Name
```

```python
# Vérifier format des IDs YouTube dans les MP3 (11 chars ?)
from pathlib import Path
audio_dir = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio")
mp3s = sorted(audio_dir.glob("*.mp3"))
print(f"Total MP3 : {len(mp3s)}")
for mp3 in mp3s[:5]:
    id_yt = mp3.stem[:11]
    print(f"  ID='{id_yt}' (len={len(id_yt)}) | fichier : {mp3.name[:50]}")
ids_minus = [mp3.stem[:11] for mp3 in mp3s if mp3.stem.startswith("-")]
print(f"IDs commençant par '-' : {len(ids_minus)} → {ids_minus[:3]}")
```

### M4 — Fichiers qui lisent la KB

```powershell
Select-String -Path "C:\trading-copilote\05-saas\**\*.py" `
  -Pattern "KNOWLEDGE_BASE_MASTER" -Recurse |
  Select-Object Filename, LineNumber, Line |
  Format-Table -AutoSize
```

→ Lister tous les fichiers trouvés (attendu : 8 fichiers).

### M5 — Scripts existants ou manquants

```powershell
$scripts = @(
    "C:\trading-copilote\05-saas\utils\extract_chapter_rules.py",
    "C:\trading-copilote\05-saas\utils\inject_chapter_rules.py",
    "C:\trading-copilote\05-saas\utils\gemini_transcriber.py",
    "C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py",
    "C:\trading-copilote\05-saas\engine\claude_brain.py",
    "C:\trading-copilote\05-saas\knowledge_base\purge_kb.py",
    "C:\trading-copilote\05-saas\knowledge_base\audit_kb.py",
    "C:\trading-copilote\05-saas\config\settings.py"
)
foreach ($s in $scripts) {
    $exists = Test-Path $s
    $status = if ($exists) { "✓ EXISTE" } else { "✗ MANQUANT" }
    Write-Host "$status | $s"
}
```

### M6 — Tests (baseline avant reconstruction)

```powershell
# Lister les fichiers de tests
Get-ChildItem "C:\trading-copilote\05-saas" -Recurse -Filter "test_*.py" | Select-Object FullName

# Compter les fonctions test
Select-String -Path "C:\trading-copilote\05-saas\engine\test_*.py" -Pattern "^def test_" | Measure-Object | Select-Object Count
Select-String -Path "C:\trading-copilote\05-saas\api\test_api.py" -Pattern "^def test_" | Measure-Object | Select-Object Count
```

```powershell
# Lancer les tests — baseline AVANT reconstruction
cd C:\trading-copilote
py -m pytest 05-saas\engine\test_claude_brain.py `
             05-saas\engine\test_signal_engine.py `
             05-saas\engine\test_risk_guardrails.py `
             05-saas\engine\test_belkhayate_formulas.py `
             05-saas\api\test_api.py -v --tb=short 2>&1
```

→ Reporter : X/Y PASS, liste des tests KO si existants.

### M7 — Archivage existant

```powershell
git -C "C:\trading-copilote" tag -l
Test-Path "C:\trading-copilote\04-cerveau-trading\KB_BACKUP_WHISPER_1398.json"
Test-Path "C:\trading-copilote\_archive\whisper-lessons-elimine"
(Get-ChildItem "C:\trading-copilote\_archive\whisper-lessons-elimine" -ErrorAction SilentlyContinue).Count
```

### M8 — Outils et dépendances

```powershell
# yt-dlp
try { yt-dlp --version } catch { Write-Host "yt-dlp : NON INSTALLÉ ⚠️ BLOQUANT PHASE 2" }

# Python Gemini lib
py -c "import google.generativeai; print('google-generativeai :', google.generativeai.__version__)" 2>&1
if ($LASTEXITCODE -ne 0) { Write-Host "⚠️ BLOQUANT PHASE 4 — migration google-generativeai requise" }

# Espace disque D:\
Get-PSDrive D -ErrorAction SilentlyContinue | Select-Object Name, Used, Free
```

### M9 — Variables d'environnement

```powershell
Get-Content "C:\trading-copilote\.env" |
  Select-String "ANTHROPIC_API_KEY|GEMINI_API_KEY|FRED_API_KEY|EIA_API_KEY|FINNHUB_API_KEY" |
  ForEach-Object { $line = $_.Line; if ($line -match "=(.+)") { $key = $line.Split("=")[0]; Write-Host "$key = [PRÉSENTE]" } else { Write-Host "$line = [VIDE]" } }
```

→ Reporter : présente / absente / vide pour chaque clé.
→ Ne jamais afficher la valeur des clés.

### M10 — SHA256 vérifié par le code ?

```powershell
Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" `
  -Pattern "SHA256|KB_HASH|hash|verify|integrite|checksum" |
  Select-Object LineNumber, Line
```

→ Si 0 résultat → confirmer : "SHA256_KB_MASTER.md est un registre MANUEL, aucun code ne le vérifie automatiquement."

---

## FORMAT DU RAPPORT A

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RAPPORT A — ÉTAT DES LIEUX TRADEX-AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BLOQUANTS DÉTECTÉS : [OUI / NON]
→ Si OUI : lister + STOP — ne pas continuer vers Prompt B

M1 — KB
  Règles totales     :
  Format vidéo       :
  Format chapitre    :
  Catégories (liste) :
  Règles chapitres   : [liste courte]

M2 — SHA256
  SHA256 réel        :
  SHA256 registre    :
  Cohérence          : [OUI / NON]
  Vérification auto  : [OUI / NON]

M3 — Corpus
  MP3 Lessons        :
  Transcripts Whisper:
  Transcripts Gemini :
  Fichiers OFTC      : [liste noms exacts]
  IDs YouTube 11 ch  : [OUI / NON + exemples]
  IDs avec '-'       : [N exemples]

M4 — Lecteurs KB
  Fichiers trouvés   : [liste]
  Nombre total       :

M5 — Scripts
  extract_chapter_rules.py : [EXISTE / MANQUANT]
  inject_chapter_rules.py  : [EXISTE / MANQUANT]
  gemini_transcriber.py    : [EXISTE]
  transcript_processor.py  : [EXISTE]
  claude_brain.py          : [EXISTE]
  purge_kb.py              : [EXISTE / MANQUANT]
  audit_kb.py              : [EXISTE / MANQUANT]

M6 — Tests baseline
  Fichiers tests     : [liste]
  Fonctions test     :
  Résultat pytest    : [X/Y PASS]
  Tests KO           : [liste si existants]

M7 — Archivage
  Tag KB-WHISPER-1398      : [EXISTE / ABSENT]
  KB_BACKUP_WHISPER_1398   : [EXISTE / ABSENT]
  _archive\whisper         : [EXISTE / ABSENT + nb fichiers]

M8 — Outils
  yt-dlp version     : [version / NON INSTALLÉ ⚠️]
  google-generativeai: [version / ERREUR ⚠️]
  Espace disque D:\  : [X Go libres / ABSENT]

M9 — Clés API
  ANTHROPIC_API_KEY  : [PRÉSENTE / ABSENTE]
  GEMINI_API_KEY     : [PRÉSENTE / ABSENTE]
  FRED_API_KEY       : [PRÉSENTE / ABSENTE]
  EIA_API_KEY        : [PRÉSENTE / ABSENTE]
  FINNHUB_API_KEY    : [PRÉSENTE / ABSENTE]

M10 — SHA256 dans code
  Vérification auto  : [OUI lignes X / NON — registre manuel uniquement]

━━━ BLOQUANTS ━━━
[Lister tout ce qui doit être résolu avant de lancer la reconstruction]

━━━ PRÊT POUR PROMPT B ? ━━━
[OUI — aucun bloquant / NON — voir bloquants ci-dessus]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## RÈGLES ABSOLUES

- Ne jamais inventer un chiffre → DONNÉES INSUFFISANTES si non mesurable
- Ne jamais afficher la valeur des clés API
- Si yt-dlp absent → marquer BLOQUANT et STOPPER
- Si google-generativeai absent/erreur → marquer BLOQUANT et STOPPER
- Ne modifier aucun fichier dans ce prompt

---

*Prompt A — 1/3 — Cowork S39 — 29/06/2026*
