# PROMPT CLAUDE CODE — S39 — Audit & Consolidation Stratégie Reconstruction KB
> Cowork → Claude Code | Date : 29/06/2026 | Session S39
> Version 2 — Post-audit Cowork (15 corrections appliquées)

---

## TA MISSION

Tu es l'auditeur hostile de la stratégie de reconstruction de la Knowledge Base TRADEX-AI.
Cowork a produit une stratégie en 10 phases. **Tu dois la lire, la challenger sur le code réel,
et rendre un verdict : CONFIRMÉE / AMENDÉE / BLOQUÉE — avec les corrections précises.**

Aucune politesse. Aucun résumé. Seulement les faits du code.

---

## ÉTAPE 1 — LIRE LES FICHIERS DE RÉFÉRENCE (ordre strict)

Lis ces fichiers **dans cet ordre** avant toute analyse :

```
1. C:\trading-copilote\CLAUDE.md
2. C:\trading-copilote\00-pilotage\DECISIONS_VEROUILLEES.md
3. C:\trading-copilote\00-pilotage\DETTE_TECHNIQUE.md
4. C:\trading-copilote\00-pilotage\STRATEGIE_RECONSTRUCTION_KB_V2_S39.md  ← LA STRATÉGIE À AUDITER
```

---

## ÉTAPE 2 — LIRE LE CODE RÉEL (audit exhaustif)

Lis **en entier** chaque fichier ci-dessous :

### Code du pipeline KB
```
C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py
C:\trading-copilote\05-saas\utils\gemini_transcriber.py
C:\trading-copilote\05-saas\engine\claude_brain.py
C:\trading-copilote\05-saas\config\settings.py
```

### Fichiers qui lisent la KB — TOUS les 8 (pas seulement claude_brain.py)
```
C:\trading-copilote\05-saas\engine\claude_brain.py
C:\trading-copilote\05-saas\knowledge_base\audit_kb.py
C:\trading-copilote\05-saas\knowledge_base\purge_kb.py
C:\trading-copilote\05-saas\knowledge_base\validate_douteux.py
C:\trading-copilote\05-saas\knowledge_base\b05_lift_provisoire.py
C:\trading-copilote\05-saas\knowledge_base\b06_add_video10.py
C:\trading-copilote\05-saas\knowledge_base\transcript_processor.py
C:\trading-copilote\05-saas\config\settings.py
```
⚠️ La reconstruction KB affecte ces 8 modules. Identifier lesquels peuvent modifier la KB
(purge_kb.py, b05, b06 notamment) et s'ils doivent être désactivés pendant la reconstruction.

### Registre SHA256 (PAS KB_HASH.txt — ce fichier n'existe pas)
```
C:\trading-copilote\04-cerveau-trading\SHA256_KB_MASTER.md
```
⚠️ SHA256_KB_MASTER.md est un REGISTRE MANUEL. Aucun code ne vérifie ce hash
automatiquement. Après reconstruction → mettre à jour la ligne "## Hash actif" manuellement.

### Tests — dans engine\ et api\ (PAS dans tests\ — ce dossier n'existe pas)
```
C:\trading-copilote\05-saas\engine\test_claude_brain.py
C:\trading-copilote\05-saas\engine\test_signal_engine.py
C:\trading-copilote\05-saas\engine\test_risk_guardrails.py
C:\trading-copilote\05-saas\engine\test_belkhayate_formulas.py
C:\trading-copilote\05-saas\api\test_api.py
```
Commande correcte :
```powershell
py -m pytest 05-saas\engine\test_claude_brain.py 05-saas\engine\test_signal_engine.py 05-saas\engine\test_risk_guardrails.py 05-saas\engine\test_belkhayate_formulas.py 05-saas\api\test_api.py -v
```

### Structure KB réelle
```python
# Exécute ce script pour voir la structure réelle de la KB :
import json
with open(r"C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json") as f:
    kb = json.load(f)

print("TOP KEYS:", list(kb.keys()))
print("TOTAL RÈGLES:", sum(len(v) for v in kb.get('aggregated_rules', {}).values()))
print("CATÉGORIES:", list(kb.get('aggregated_rules', {}).keys()))

# Compter les 2 formats
video_fmt = chap_fmt = 0
for cat, entries in kb.get('aggregated_rules', {}).items():
    for e in entries:
        if 'id_brique' in e:
            chap_fmt += 1
        elif 'source_video_id' in e:
            video_fmt += 1
print(f"Format vidéo (source_video_id): {video_fmt}")
print(f"Format chapitre (id_brique): {chap_fmt}")

# Afficher les règles chapitres complètes
print("\n=== RÈGLES CHAPITRES ===")
for cat, entries in kb.get('aggregated_rules', {}).items():
    for e in entries:
        if 'id_brique' in e:
            print(f"[{cat}] {e.get('regle','')[:120]}")
```

### Manifeste et corpus
```
C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\MANIFESTE_TRANSCRITS.csv
```
```powershell
# Compter les fichiers des corpus :
(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio" -Filter "*.mp3").Count
(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" -Filter "*.txt").Count
(Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts" -Filter "*.txt").Count
```

### Vérifier yt-dlp
```powershell
yt-dlp --version
```
→ Si non installé → STOP immédiat. Reporter à Cowork. Ne pas continuer.

### Vérifier espace disque D:\ (110 MP4 ≈ 5-30 Go selon durée)
```powershell
Get-PSDrive D
```
→ Indiquer l'espace libre disponible.

### Vérifier migration Gemini (DETTE §5 — BLOQUANT POTENTIEL PHASE 4)
```powershell
py -c "import google.generativeai; print(google.generativeai.__version__)"
```
→ Si ImportError OU version insuffisante → **STOP IMMÉDIAT. Reporter à Cowork.
   Ne pas continuer vers Phase 4.**
→ Solution si bloquant : `pip install google-generativeai --upgrade --break-system-packages`

---

## ÉTAPE 3 — AUDITER LA STRATÉGIE (10 phases à challenger)

Pour chaque phase de `STRATEGIE_RECONSTRUCTION_KB_V2_S39.md`, réponds à ces questions :

### PHASE 0 — Sauvegarder les règles chapitres
- Combien de règles chapitres existent dans la KB avec le format `id_brique` ? (lancer le script ci-dessus)
- Le script `extract_chapter_rules.py` existe-t-il dans `05-saas\utils\` ?
  → S'il n'existe pas, voici le code EXACT à créer (ne pas inventer une variante) :

```python
# C:\trading-copilote\05-saas\utils\extract_chapter_rules.py
import json, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_FILE     = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")

with open(KB_FILE, encoding="utf-8") as f:
    kb = json.load(f)

chapters = {}
count = 0
for cat, entries in kb.get("aggregated_rules", {}).items():
    for e in entries:
        if "id_brique" in e:
            if cat not in chapters:
                chapters[cat] = []
            chapters[cat].append(e)
            count += 1

import tempfile, pathlib
tmp = pathlib.Path(BACKUP_FILE).with_suffix(".tmp")
with open(tmp, "w", encoding="utf-8") as f:
    json.dump({"chapter_rules": chapters, "total": count}, f, ensure_ascii=False, indent=2)
tmp.replace(BACKUP_FILE)
print(f"OK — {count} règles chapitres sauvegardées dans KB_CHAPTER_RULES_BACKUP.json")
```

- Confirmer : `py -m py_compile 05-saas\utils\extract_chapter_rules.py` → 0 erreur ?

### PHASE 1 — Archivage
- `git tag -l` → le tag `KB-WHISPER-1398` existe-t-il déjà ? (depuis `C:\trading-copilote\`)
- `KB_BACKUP_WHISPER_1398.json` existe déjà dans `04-cerveau-trading\` ?
- Le dossier `_archive\whisper-lessons-elimine\` existe ? Combien de fichiers dedans ?

### PHASE 2 — Pre-check YouTube
- yt-dlp est installé ? Quelle version ?
- Vérifier sur 5 exemples que les IDs YouTube font bien 11 caractères :
  ```python
  from pathlib import Path
  audio_dir = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio")
  for mp3 in list(audio_dir.glob("*.mp3"))[:5]:
      print(f"ID='{mp3.stem[:11]}' len={len(mp3.stem[:11])} | fichier={mp3.name[:40]}")
  ```
- Les IDs commençant par `-` existent-ils ? Si oui, confirmer que `yt-dlp -- {ID}` (avec `--`) gère ce cas.

### PHASE 3 — Téléchargement MP4
- `D:\Belkhayate-Lessons-MP4\` n'entre pas en conflit avec `D:\Belkhayate-Videos\` ? (noms différents = OK)
- Espace disque D:\ suffisant ? (résultat de `Get-PSDrive D` ci-dessus)
- Le format yt-dlp `bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]` est-il disponible sur des vidéos YouTube standard ? (répondre OUI/NON sur la syntaxe — ne pas inventer de test live)

### PHASE 4 — Transcription Gemini
- `gemini_transcriber.py` : quelles sont les valeurs actuelles de `VIDEO_DIR` et `OUTPUT_DIR` ?
- Le script **peut-il** pointer vers `D:\Belkhayate-Lessons-MP4\` sans modifier autre chose que `VIDEO_DIR` ?
- La fonction `_chemin_upload()` est-elle présente ? Cite les lignes exactes.
- Le checkpoint `if out_path.exists(): SKIP` est-il bien en place ? Cite les lignes exactes.
- La migration `google-generativeai` (DETTE §5) est-elle bloquante ? (résultat du test ci-dessus)

### PHASE 5 — Décontamination OFTC
- Lister les fichiers exacts dans `transcripts-gemini\` contenant "OFTC" dans leur nom :
  ```powershell
  Get-ChildItem "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini" | Where-Object { $_.Name -like "*OFTC*" }
  ```
- Y a-t-il d'autres fichiers non-Belkhayate visibles dans ce dossier ?

### PHASE 6 — transcript_processor_gemini.py
- `transcript_processor.py` : quelles sont exactement les lignes 44-50 (TRANSCRIPTS_DIR, MANIFEST_FILE) ?
- Quelles autres dépendances au MANIFESTE existent dans le fichier ? (toutes les occurrences de MANIFEST_FILE)
- Le format de sortie JSON (clés : regle, statut, source_video_id, confiance) est-il identique à ce que `claude_brain.py` attend ? Cite la fonction qui lit la KB dans claude_brain.py.

### PHASE 7 — Reconstruction KB
- `transcript_processor.py` → combien d'appels Claude API par vidéo ? (lire la fonction principale)
- Coût estimé : → **DONNÉES INSUFFISANTES si les MP4 n'ont pas encore été téléchargés**. Ne pas inventer un chiffre.
- La clé `ANTHROPIC_API_KEY` est-elle dans `.env` ? (`Get-Content C:\trading-copilote\.env | Select-String "ANTHROPIC"`)
- `purge_kb.py` et `b05_lift_provisoire.py` modifient-ils la KB ? Doivent-ils être désactivés pendant la reconstruction ?

### PHASE 8 — Réinjection chapitres
- Le script `inject_chapter_rules.py` existe-t-il dans `05-saas\utils\` ?
  → S'il n'existe pas, voici le code EXACT à créer :

```python
# C:\trading-copilote\05-saas\utils\inject_chapter_rules.py
import json, os, pathlib, tempfile
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_FILE     = os.path.join(BASE_DIR, "04-cerveau-trading", "KNOWLEDGE_BASE_MASTER.json")
BACKUP_FILE = os.path.join(BASE_DIR, "04-cerveau-trading", "KB_CHAPTER_RULES_BACKUP.json")

with open(KB_FILE, encoding="utf-8") as f:
    kb = json.load(f)
with open(BACKUP_FILE, encoding="utf-8") as f:
    backup = json.load(f)

chapters = backup.get("chapter_rules", {})
injected = 0
for cat, entries in chapters.items():
    if cat not in kb["aggregated_rules"]:
        kb["aggregated_rules"][cat] = []
    kb["aggregated_rules"][cat].extend(entries)
    injected += len(entries)

tmp = pathlib.Path(KB_FILE).with_suffix(".tmp")
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(kb, f, ensure_ascii=False, indent=2)
tmp.replace(KB_FILE)
print(f"OK — {injected} règles chapitres réinjectées dans KNOWLEDGE_BASE_MASTER.json")
```

- `load_kb_rules()` dans `claude_brain.py` gère-t-il les 2 formats (`source_video_id` + `id_brique`) simultanément ? Cite le code exact de cette fonction.

### PHASE 9 — Mise à jour SHA256
⚠️ `KB_HASH.txt` N'EXISTE PAS. Le registre est `SHA256_KB_MASTER.md`.
⚠️ Aucun code dans `claude_brain.py` ne vérifie automatiquement ce hash.
   SHA256_KB_MASTER.md est un REGISTRE MANUEL de traçabilité, pas un garde-fou automatique.

- Confirmer : aucune vérification SHA256 dans `claude_brain.py` ? (grep ci-dessous)
  ```powershell
  Select-String -Path "C:\trading-copilote\05-saas\engine\claude_brain.py" -Pattern "SHA256|hash|KB_HASH|verify|integrite"
  ```
- Après reconstruction, la mise à jour correcte est :
  ```powershell
  # Calculer le nouveau hash
  $hash = (Get-FileHash "C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json" -Algorithm SHA256).Hash
  echo "Nouveau SHA256 : $hash"
  # Puis mettre à jour manuellement la ligne "## Hash actif" dans SHA256_KB_MASTER.md
  ```
- Hash actif actuel dans SHA256_KB_MASTER.md : `4cc9f77a0fe188871b945574e3b46c237e8fdc4713b5cde0ea751cc3517eb821`
  → Confirmer que c'est bien la valeur présente dans le fichier.

### PHASE 10 — Tests
- Compter les fonctions test dans chaque fichier :
  ```powershell
  Select-String -Path "C:\trading-copilote\05-saas\engine\test_*.py" -Pattern "^def test_" | Measure-Object
  Select-String -Path "C:\trading-copilote\05-saas\api\test_api.py" -Pattern "^def test_" | Measure-Object
  ```
- Y a-t-il une fonction test qui vérifie le SHA256 ? (`Select-String ... -Pattern "SHA256|hash"`)
- Y a-t-il une fonction test qui vérifie le nombre de règles ? Avec quel seuil minimum ?
- La commande pytest correcte depuis `C:\trading-copilote\` :
  ```powershell
  py -m pytest 05-saas\engine\test_claude_brain.py 05-saas\engine\test_signal_engine.py 05-saas\engine\test_risk_guardrails.py 05-saas\engine\test_belkhayate_formulas.py 05-saas\api\test_api.py -v
  ```
  → Lancer cette commande pour avoir le baseline AVANT la reconstruction.

---

## ÉTAPE 4 — RAPPORT DES CONSÉQUENCES DE LA RECONSTRUCTION KB

**Abdelkrim doit savoir exactement ce qui va changer, ce qui va casser, et ce qui va disparaître
avant de donner le GO. Réponds à chacun de ces points en te basant UNIQUEMENT sur le code réel.**

### A — CE QUI SERA DÉTRUIT (irréversible si pas de backup)

1. `KNOWLEDGE_BASE_MASTER.json` sera écrasé → combien de règles perdues ? Quelles catégories ?
2. Les règles chapitres (`id_brique`) → sont-elles récupérables depuis git ?
   ```powershell
   git log --oneline -- 04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json
   ```
3. Les transcripts Whisper dans `transcripts/` → combien de fichiers ? Si archivés, peut-on les restaurer ?
4. Le `MANIFESTE_TRANSCRITS.csv` → quelles colonnes contient-il ?
   (`Get-Content ... | Select-Object -First 5`)

### B — CE QUI VA CASSER IMMÉDIATEMENT (avant correction)

5. `claude_brain.py` → aucun check SHA256 automatique (confirmé ci-dessus). Que se passe-t-il réellement si la KB change de structure ? Y a-t-il une validation du JSON au chargement ?
6. `SHA256_KB_MASTER.md` → si on oublie de le mettre à jour, TRADEX démarre-t-il quand même ? (réponse attendue : OUI car c'est manuel)
7. Lesquels des 5 fichiers de tests vont échouer si la KB change de structure ou de nombre de règles ?
8. `transcript_processor.py` → si lancé sans modifier MANIFESTE, que se passe-t-il exactement ?
   (FileNotFoundError ? Résultat vide ? 0 règles ? — lire le code de la fonction lisant le manifeste)

### C — CE QUI VA CHANGER (comportement du moteur)

9. Nombre de règles : 1398 → X inconnu. Y a-t-il un seuil minimum dans `claude_brain.py` ou dans les tests ?
10. Comment `claude_brain.py` utilise-t-il les règles KB ? (RAG ? Injection directe dans prompt ?) Citer la fonction exacte.
11. Si une des 11 catégories disparaît ou change de nom → quel module casse en premier ?
12. Mode Manuel vs Mode Auto → même impact sur les deux ?

### D — RISQUES CACHÉS

13. Grep complet — tous les fichiers qui lisent la KB :
    ```powershell
    Select-String -Path "C:\trading-copilote\05-saas\**\*.py" -Pattern "KNOWLEDGE_BASE_MASTER" -Recurse | Select-Object Filename, LineNumber, Line
    ```
    → Lister les 8 fichiers attendus + tout fichier supplémentaire non prévu.

14. Y a-t-il un cache KB quelque part (`.pkl`, `.cache`, Redis, ou autre) ?
    ```powershell
    Get-ChildItem "C:\trading-copilote" -Recurse -Include "*.pkl","*.cache","*.pickle" 2>$null
    ```

15. Les 3 clés API manquantes (FRED_API_KEY, EIA_API_KEY, FINNHUB_API_KEY) — bloquent-elles la reconstruction KB ou seulement le mode live ?

16. Migration `google-generativeai → google-genai` (DETTE §5) → bloquante pour Phase 4 ?
    (résultat du test `py -c "import google.generativeai..."` de l'Étape 2)
    → Si bloquante : **STOP — ne pas continuer, reporter à Cowork.**

### E — TABLEAU AVANT/APRÈS (compléter avec les valeurs réelles du code)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AVANT RECONSTRUCTION              APRÈS RECONSTRUCTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KB source      : Whisper           KB source      : Gemini multimodal
Règles totales : [compter]         Règles totales : [INCONNU — estimé]
Règles vidéo   : [compter]         Règles vidéo   : [INCONNU]
Règles chap.   : [compter]         Règles chap.   : [N] (si Phase 0 OK)
SHA256 actif   : 4cc9f77a...       SHA256 actif   : [NOUVEAU — manuel]
Tests baseline : [X/Y PASS]        Tests           : [À CONFIRMER]
TRADEX démarre : OUI               TRADEX démarre : OUI (SHA256 = manuel)
Signaux        : basés Whisper     Signaux        : basés Gemini
Modules lisant KB : 8              Modules lisant KB : 8 (inchangé)
Mode Auto      : BLOQUÉ            Mode Auto      : BLOQUÉ (inchangé)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### F — VERDICT RISQUE RECONSTRUCTION

```
RISQUE GLOBAL       : [FAIBLE / MOYEN / ÉLEVÉ / CRITIQUE]
POINT DE NON-RETOUR : [Phase X — après cette phase, difficile de revenir en arrière]
BACKUP SUFFISANT    : [OUI / NON — et pourquoi]
RECOMMANDATION      : [GO / GO CONDITIONNEL / NO-GO — avec condition précise]
```

---

## ÉTAPE 5 — FORMAT DU RAPPORT FINAL

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AUDIT STRATÉGIE RECONSTRUCTION KB — TRADEX-AI S39
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VERDICT GLOBAL    : [CONFIRMÉE / AMENDÉE / BLOQUÉE]
CONFIANCE         : [X/10]
PHASES OK         : [liste]
PHASES À CORRIGER : [liste]
BLOQUANTS GO/NO-GO : [liste]

━━━ CORRECTIONS OBLIGATOIRES ━━━
[Pour chaque phase à corriger : citation du code exact + correction précise]

━━━ PHASES CONFIRMÉES ━━━
[Pour chaque phase OK : preuve dans le code + extrait de ligne]

━━━ RISQUES NON VUS PAR COWORK ━━━
[Tout ce que tu as trouvé que Cowork n'avait pas anticipé]

━━━ AMÉLIORATIONS SUGGÉRÉES ━━━
[Optimisations basées sur le code réel uniquement]

━━━ ORDRE D'EXÉCUTION FINAL ━━━
[La séquence corrigée et validée — avec la commande exacte pour chaque étape]

━━━ PROCHAINE COMMANDE ━━━
[La toute première commande à exécuter sur Windows PowerShell dans C:\trading-copilote\]

━━━ RAPPORT CONSÉQUENCES RECONSTRUCTION ━━━

A — CE QUI SERA DÉTRUIT :
[Réponses A1-A4 avec valeurs réelles]

B — CE QUI VA CASSER :
[Réponses B5-B8 avec lignes de code exactes]

C — CE QUI VA CHANGER :
[Réponses C9-C12]

D — RISQUES CACHÉS :
[Réponses D13-D16]

E — TABLEAU AVANT/APRÈS :
[Tableau complété avec valeurs réelles du code]

F — VERDICT RISQUE :
RISQUE GLOBAL       :
POINT DE NON-RETOUR :
BACKUP SUFFISANT    :
RECOMMANDATION      :
```

---

## RÈGLES ABSOLUES POUR CET AUDIT

- **Ne jamais inventer** un chiffre, une fonction, un fichier qui n'existe pas dans le code réel
- **Citer les lignes exactes** du code quand tu confirmes ou corriges une phase
- **Si un fichier n'existe pas** → le dire clairement avec le chemin exact testé
- **Si yt-dlp n'est pas installé** → STOP Phase 2, reporter à Cowork
- **Si migration Gemini bloquante** → STOP immédiat, ne pas continuer vers Phase 4
- **DONNÉES INSUFFISANTES** obligatoire si une mesure nécessite des fichiers non encore créés (MP4)
- **Ne pas modifier le code** dans cet audit — seulement lire, analyser, rapporter
- **`05-saas\tests\`** → ce dossier n'existe pas, ne pas l'utiliser
- **`KB_HASH.txt`** → ce fichier n'existe pas, ne pas l'utiliser

---

## CRITÈRE DE SUCCÈS

Tu as réussi quand Abdelkrim peut copier-coller la première commande et démarrer Phase 0
avec une confiance totale que chaque étape a été validée sur le code réel.

---

*Produit par Cowork S39 — 29/06/2026 | Version 2 post-audit*
*Stratégie à auditer : STRATEGIE_RECONSTRUCTION_KB_V2_S39.md*
*Corrections appliquées : 15/15 (audit Cowork AUDIT_PROMPT_S39_RAPPORT.md)*
