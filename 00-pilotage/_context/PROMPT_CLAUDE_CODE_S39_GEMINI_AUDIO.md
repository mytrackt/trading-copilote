# PROMPT CLAUDE CODE — S39 — Créer gemini_transcriber_audio.py
> Cowork → Claude Code | Date : 28/06/2026 | Session S39

---

## CONTEXTE

Projet : TRADEX-AI — `C:\trading-copilote\`
P4 GO/NO-GO validé : ✅ GO CONDITIONNEL.

**Décision D-S38-2 verrouillée** : Créer `gemini_transcriber_audio.py` (copie adaptée MP3).
NE JAMAIS modifier `gemini_transcriber.py` (original MP4 — intouchable).

---

## TA MISSION

Créer `C:\trading-copilote\05-saas\utils\gemini_transcriber_audio.py`
à partir de `C:\trading-copilote\05-saas\utils\gemini_transcriber.py`
en appliquant exactement les modifications listées ci-dessous.

---

## MODIFICATIONS OBLIGATOIRES (7 points)

### MOD-1 🔴 Source : VIDEO_DIR → audio/
```python
# REMPLACER :
VIDEO_DIR = Path(r"D:\Belkhayate-Videos")

# PAR :
AUDIO_DIR = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio")
```

### MOD-2 🔴 Extension : *.mp4 → *.mp3
Dans `main()`, remplacer :
```python
videos = sorted(VIDEO_DIR.glob("*.mp4"))
```
Par :
```python
audios = sorted(AUDIO_DIR.glob("*.mp3"))
```
Et adapter toutes les références `videos` → `audios`, `video` → `audio_file`, `VIDEO_DIR` → `AUDIO_DIR`.

### MOD-3 🔴 MIME type : video/mp4 → audio/mpeg
3 occurrences dans le code. Remplacer PARTOUT :
```python
"mime_type": "video/mp4"
```
Par :
```python
"mime_type": "audio/mpeg"
```
Dont dans `_chemin_upload()` : la copie temp doit s'appeler `_gemini_temp_audio.mp3` (pas `.mp4`).

### MOD-4 🟠 Prompt audio-only — SUPPRIMER les instructions visuelles
Remplacer la fonction `construire_prompt()` ENTIÈRE par cette version audio-only :

```python
def construire_prompt_audio(nom_fichier: str) -> str:
    """
    Prompt Gemini adapte aux MP3 audio-only (pas de video, pas d'ecran).
    INTERDIT : toute instruction de description visuelle (hallucination garantie).
    """
    return """Tu es un transcripteur expert de cours de trading financier en francais.
Transcris cet enregistrement audio de Mustapha Belkhayate.

REGLE FONDAMENTALE :
Tu n'as acces qu'a l'audio. Tu ne vois aucun ecran, aucun graphique, aucun indicateur.
N'invente JAMAIS une description visuelle. Ne mets JAMAIS de [VISUEL: ...] dans ta sortie.
Si Belkhayate dit "vous voyez ici" ou "regardez ca", transcris simplement ses mots — tu ne peux
pas decrire ce qu'il montre.

FORMAT OBLIGATOIRE :
- Transcris integralement tout ce que Belkhayate dit.
- Quand Belkhayate enonce une regle claire et complete, mets-la en evidence :
  [REGLE: formulation complete de la regle]
- Pour les prix et niveaux chiffres prononces verbalement : transcris-les fidelement.
- Ne pas tronquer, ne pas resumer — transcription exhaustive obligatoire.

Exemple de sortie attendue :
  "Quand l'indicateur est dans le vert et qu'on est au-dessus de la moyenne,"
  [REGLE: en tendance haussiere confirmee, on ne cherche que des signaux d'achat — jamais vendre contre la tendance]
  "donc vous voyez ici ce que je veux dire, c'est exactement ca la methode."

Transcris maintenant l'audio complet. Sois exhaustif.
"""
```

### MOD-5 🟢 Supprimer le chunking vidéo (inutile pour MP3)
Pour l'audio-only, la limite Gemini est ~8,7h (vs 50 min pour vidéo).
Supprimer les fonctions : `decouper_en_chunks()`, `_transcrire_par_chunks()`, `_transcrire_chunk()`.
Simplifier `transcrire_audio()` (renommer `transcrire_video()`) : supprimer le bloc `if duree > DUREE_MAX_DIRECTE`.
Conserver `get_duree_video()` renommée `get_duree_audio()` (ffprobe fonctionne sur MP3).

### MOD-6 🟢 Adapter detecter_qualite() → detecter_duree_approx()
La qualité vidéo (taille fichier) n'a pas de sens pour l'audio.
Remplacer `detecter_qualite()` par une simple détection de durée via `get_duree_audio()` :
```python
def detecter_type_audio(nom_fichier: str) -> str:
    nom_lower = nom_fichier.lower()
    if "lesson" in nom_lower:
        return "LESSON"
    elif "live" in nom_lower or "5 days" in nom_lower:
        return "LIVE"
    elif "extrait" in nom_lower:
        return "EXTRAIT"
    else:
        return "AUTRE"
```

### MOD-7 🟢 Nom de sortie et en-tête
Sortie vers le MÊME dossier `OUTPUT_DIR` (transcripts-gemini) avec le même schéma `{stem}_gemini.txt`.
En-tête : adapter `[TYPE: COURS_PEDAGOGIQUE]` → `[TYPE: AUDIO_ONLY]` + `[SOURCE_TYPE: {type_audio}]`.
Supprimer `[QUALITE_VIDEO: ...]` → remplacer par `[SOURCE_TYPE: LESSON/LIVE/EXTRAIT/AUTRE]`.

---

## COMMANDES D'EXÉCUTION

Après avoir créé le fichier :

**Étape 1 — Lint obligatoire :**
```powershell
# Dans : C:\trading-copilote\05-saas\utils\
py -m py_compile gemini_transcriber_audio.py
```
→ 0 erreur attendu

**Étape 2 — Test sur 1 seul MP3 :**
Modifier temporairement `main()` pour ne traiter que le 1er fichier (ajouter `audios = audios[:1]`).
```powershell
# Dans : C:\trading-copilote\
py 05-saas\utils\gemini_transcriber_audio.py
```
Vérifier la sortie dans `transcripts-gemini/` : pas de [VISUEL:], présence de [REGLE:].

**Étape 3 — Revenir au batch complet :**
Retirer `audios = audios[:1]` → relancer pour les 110 MP3.

---

## RÈGLES ABSOLUES

- `gemini_transcriber.py` original = INTOUCHABLE — ne pas modifier
- BASE_DIR obligatoire en tête de fichier
- `os.getenv("GEMINI_API_KEY")` — jamais hardcoder la clé
- Atomic writes conservés : `tmp_path.replace(out_path)`
- `_chemin_upload()` doit être adapté pour MP3 (pas supprimé — les noms accentués existent dans le corpus)

---

*Produit par Cowork S39 — 28/06/2026*
