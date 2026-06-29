# PROMPT CLAUDE CODE — S39 — Transcription VIDEO (D:\ rebranché)
> Cowork → Claude Code | Date : 28/06/2026 | Session S39

---

## CONTEXTE

Projet : TRADEX-AI — `C:\trading-copilote\`
D:\ vient d'être rebranché — les MP4 originaux sont disponibles sur `D:\Belkhayate-Videos\`.
Stratégie A (VIDEO) activée : qualité maximale, audio + visuel.
NE PAS créer `gemini_transcriber_audio.py` — utiliser l'original `gemini_transcriber.py`.

---

## ÉTAPE 1 — Vérifier D:\ (obligatoire avant tout)

```powershell
dir D:\Belkhayate-Videos\*.mp4 | measure -Line
```
→ Confirme le nombre de MP4 disponibles. Si 0 → STOP et avertir Cowork.

---

## ÉTAPE 2 — Croiser les corpus (MP3 vs MP4)

Objectif : trouver lesquels des 110 MP3 du corpus Lessons ont un MP4 correspondant sur D:\.

Les MP3 sont dans :
`C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio\`

Format des noms : `{youtube_id}_{titre}.mp3`

Les MP4 sont sur : `D:\Belkhayate-Videos\`

Script à exécuter dans Claude Code :

```python
from pathlib import Path

mp3_dir = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio")
mp4_dir = Path(r"D:\Belkhayate-Videos")
gemini_out = Path(r"C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini")

# IDs YouTube des MP3 (11 premiers caractères du nom de fichier)
mp3_ids = {f.stem[:11]: f for f in mp3_dir.glob("*.mp3")}

# IDs YouTube des MP4
mp4_ids = {f.stem[:11]: f for f in mp4_dir.glob("*.mp4")}

# IDs déjà transcrits par Gemini
done_ids = {f.stem[:11]: f for f in gemini_out.glob("*.txt")}

# Correspondances
match = [vid for vid in mp3_ids if vid in mp4_ids]
no_mp4 = [vid for vid in mp3_ids if vid not in mp4_ids]
already_done = [vid for vid in match if vid in done_ids]
to_transcribe = [vid for vid in match if vid not in done_ids]

print(f"MP3 total        : {len(mp3_ids)}")
print(f"MP4 disponibles  : {len(mp4_ids)}")
print(f"Correspondances  : {len(match)}")
print(f"Déjà transcrits  : {len(already_done)}")
print(f"À transcrire VIDEO : {len(to_transcribe)}")
print(f"MP3 sans MP4     : {len(no_mp4)}")
print()
print("=== À TRANSCRIRE (VIDEO) ===")
for vid in sorted(to_transcribe):
    print(f"  {vid} → {mp4_ids[vid].name}")
print()
print("=== SANS MP4 (audio seulement) ===")
for vid in sorted(no_mp4):
    print(f"  {vid} → {mp3_ids[vid].name}")
```

→ Reporter le résultat complet avant de continuer.

---

## ÉTAPE 3 — Décision selon résultat

### CAS A : Correspondances ≥ 80 MP4 trouvés
→ Lancer `gemini_transcriber.py` directement sur `D:\Belkhayate-Videos\`
→ Le script est déjà configuré avec `VIDEO_DIR = Path(r"D:\Belkhayate-Videos")`
→ Le checkpoint `if out_path.exists(): SKIP` protège les 121 déjà faits
→ Seuls les nouveaux MP4 (correspondant aux MP3 Lessons) seront traités

```powershell
# Dans : C:\trading-copilote\
py -m py_compile 05-saas\utils\gemini_transcriber.py
```
→ 0 erreur attendu. Puis confirmer avant lancement.

### CAS B : Correspondances < 50 MP4 trouvés
→ Les Lessons MP3 n'ont pas de MP4 correspondant sur D:\
→ Revenir à la Stratégie B (audio) — avertir Cowork avant tout
→ Utiliser `gemini_transcriber_audio.py` (prompt du fichier PROMPT_CLAUDE_CODE_S39_GEMINI_AUDIO.md)

---

## ÉTAPE 4 — AVANT tout lancement batch

```powershell
# Archivage KB obligatoire (D-S38-3 non encore fait)
git tag KB-WHISPER-1398
```
→ Attendre confirmation

```powershell
copy C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json C:\trading-copilote\04-cerveau-trading\KB_BACKUP_WHISPER_1398.json
```
→ Attendre confirmation

---

## ÉTAPE 5 — Test sur 1 seul MP4 (obligatoire avant batch complet)

Modifier temporairement `main()` dans `gemini_transcriber.py` :
```python
videos = sorted(VIDEO_DIR.glob("*.mp4"))[:1]  # TEMPORAIRE — 1 seule vidéo
```
Lancer, vérifier la sortie dans `transcripts-gemini/` :
- Présence de [VISUEL:] → ✅ (preuve que le visuel est capturé)
- Présence de [REGLE:] → ✅
- Pas d'erreur MIME → ✅

Retirer `[:1]` → lancer le batch complet.

---

## RÈGLES ABSOLUES

- NE PAS modifier `gemini_transcriber.py` autrement que `[:1]` pour le test
- `git check-ignore .env` avant tout push
- Une commande à la fois, attendre confirmation entre chaque
- Si erreur → STOP, reporter à Cowork

---

*Produit par Cowork S39 — 28/06/2026*
