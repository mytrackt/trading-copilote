# PROMPT CLAUDE CODE — Batch Transcription Gemini 203 vidéos (Session S30)

MODE CLAUDE CODE

---

## CONTEXTE

Projet TRADEX-AI. Tu dois préparer et lancer la transcription Gemini multimodal pour 203 vidéos YouTube.
Les transcriptions Whisper existantes (Trading Geek) sont non fiables car audio uniquement — Gemini voit les charts.

Racine projet : `C:\trading-copilote\`

---

## ÉTAPE 0 — LIRE EN PREMIER (obligatoire)

1. `C:\trading-copilote\CLAUDE.md` — règles absolues du projet
2. `C:\trading-copilote\05-saas\utils\gemini_transcriber.py` — interface exacte (arguments, comportement)
3. `C:\trading-copilote\00-pilotage\SOURCES_TRIAGE_S30.md` — liste complète des IDs par groupe

---

## ÉTAPE 1 — Archiver les Whisper Trading Geek (non fiables)

Déplacer TOUT le contenu de :
`C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts\`

Vers :
`C:\trading-copilote\_archive\trading-geek-whisper-elimine\`

⚠️ NE PAS déplacer le dossier `audio\` (MP3 conservés pour référence).

---

## ÉTAPE 2 — Vérifier les dépendances

```
yt-dlp --version
python -c "import google.generativeai; print('OK')"
```

Si yt-dlp absent : `pip install yt-dlp --break-system-packages`
Si google.generativeai absent : `pip install google-generativeai --break-system-packages`

Vérifier que la clé API Gemini est dans `.env` :
```
python -c "import os; from dotenv import load_dotenv; load_dotenv('C:/trading-copilote/.env'); print('GEMINI_KEY:', 'OK' if os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY') else 'MANQUANTE')"
```

---

## ÉTAPE 3 — Créer les dossiers de sortie

```
C:\trading-copilote\03-transcriptions\nouvelles-sources\Kasper Gold\
C:\trading-copilote\03-transcriptions\nouvelles-sources\TTrades\
C:\trading-copilote\03-transcriptions\nouvelles-sources\DaviddTech\
C:\trading-copilote\03-transcriptions\nouvelles-sources\Alex Carter\
C:\trading-copilote\03-transcriptions\nouvelles-sources\Lewis Jackson\
C:\trading-copilote\03-transcriptions\nouvelles-sources\Rayner Teo\
C:\trading-copilote\03-transcriptions\nouvelles-sources\Humbled Trader\
C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\transcripts-gemini\
C:\trading-copilote\_temp\videos_batch\
```

---

## ÉTAPE 4 — Créer `C:\trading-copilote\01-pipeline\batch_gemini.py`

Le script doit :

**a) Contenir la liste des vidéos par groupe et ordre de priorité :**

```
GROUPE 1 — Kasper Gold (5 vidéos) → dossier Kasper Gold
cPceiD1PWrI · 1SLbe0k6x4I · TXLqKZRx6hg · RQ36kizIDk0 · 6_BCuy5QYPc

GROUPE 2 — TTrades (40 vidéos) → dossier TTrades
q3nauvjT3q0 · -ocfPuD_oqE · v1X8UMWgWmI · HbOeD_JVens · yH4eYwUgdTY · 9BY-MQRNy-Y
PQiRV0JMhIQ · eywpZT3z6GQ · Kf4c41_qO1s · vn1RYjhJUnQ · -KKuZb5Z5aU · w-JekHg6Ldk
tyoxl1l-6iI · SlWxhzhLo3A · 3eVxTV_7L2U · FAKWJ-1NlLE · qdQYhePcvGE · MvD7fQQ0szE
m4k_1pF5zFI · 8BWkRGhuj1k · VD4xb9VfMHA · TNybDCtwBnc · 4Gm8p6O7Ebs · WFqLwOp2pXw
JHVaSKtE1Ys · -wr4xATE37g · r_UF8U-hsL8 · 5fnFOh5YuM0 · 4jU547ocod4 · iEaMbuFZb24
ubCe509_JLY · Ibw4saRtYMk · LKNQDAdId4s · TfHlNgAZ_II · caaS6_Q7O78 · sIcsLFSNoXM
EYzP7c24AwM · FGkb_50BfT8 · WwmS47Gb3M0 · mwmWNCTEYtY

GROUPE 3 — DaviddTech + Alex Carter (15 vidéos) → dossiers DaviddTech / Alex Carter
h6qUy92Maco · G7zv25c7Z8M · 4z1I0u1UnXQ · cXhEw2jF4go · y_bsjZThP0o · EUSXhJNwRqI
vIX6ztULs4U · HfEu7XPUnAU · lH5wrfNwL3k · R7O2TaM709Y · tkAq6g2Gjz4 · 3IgYhw5WqTY
Ebzawm73H4I · jnJF0W2XgqA · GlkJMO_ufYA

GROUPE 4 — Lewis Jackson (5 vidéos) → dossier Lewis Jackson
ZVMTeDBmSrI · 6njREUQAFdg · 4vZZReXFKkQ · reiPfBnUBys · aDWJ6lLemJU

GROUPE 5 — Rayner Teo (9 vidéos) → dossier Rayner Teo
k1TKN8iGDao · lLOKH4ThTP0 · tAR_JREOjvE · pGO9MwMCJKo · ej1UdL-oj_o
YxiJRWBy8ZA · yF6fCCz3IJU · yKk_HmtE-Zc · M9DCW8TaWuE

GROUPE 6 — Humbled Trader (16 vidéos) → dossier Humbled Trader
IqvnryFzZD4 · Vxj7QD6Lbvk · YGpiVS8BNLw · i37xXd_wI5k · Eico0SYYNnk · vswa9HZv7q4
uV84kDLUgZ4 · GVbWx5x2i-Q · T3sCLOvsdus · UWKNLR4jOI0 · ZP_3AIko08w · _Dqiuf-9Lps
OLS9w6DOpOg · UpmJJjKvJxo · o4bB5UsgnX4 · IEu3NHVE_lQ

GROUPE 7 — Trading Geek re-transcription (113 vidéos) → dossier The Trading Geek/transcripts-gemini
[Lire les 113 IDs depuis C:\trading-copilote\03-transcriptions\nouvelles-sources\The Trading Geek\audio\
en extrayant les IDs des noms de fichiers MP3]
```

**b) Pour chaque vidéo :**
1. Vérifier si le transcript existe déjà → SKIP (idempotent)
2. Télécharger la vidéo en MP4 720p max dans `_temp\videos_batch\` via yt-dlp
3. Appeler `gemini_transcriber.py` sur le fichier vidéo local
4. Sauvegarder le transcript `.txt` dans le bon dossier de sortie
5. SUPPRIMER le fichier vidéo temporaire après transcription réussie (économie disque)
6. Logger `[OK]` ou `[ERREUR]` dans `01-pipeline\batch_gemini_log.txt`
7. `time.sleep(2)` entre chaque appel API

**c) Règles techniques :**
- `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
- Clé API via `os.getenv()` uniquement — jamais en dur
- `python -m py_compile batch_gemini.py` avant toute exécution
- En cas d'erreur réseau → retry 2x puis logger ERREUR et passer à la suivante

---

## ÉTAPE 5 — TEST SUR 1 VIDÉO AVANT BATCH COMPLET

Lancer uniquement sur `cPceiD1PWrI` (Kasper Gold, 1ère priorité).
Vérifier que le transcript `.txt` contient du contenu cohérent (pas vide, pas erreur).
Afficher les 10 premières lignes du transcript.

**⚠️ ATTENDRE MA VALIDATION avant de lancer le batch complet des 203 vidéos.**

---

## ÉTAPE 6 — Après validation du test

Lancer le batch complet :
```
python C:\trading-copilote\01-pipeline\batch_gemini.py
```

Le script peut tourner en arrière-plan plusieurs heures (203 vidéos).
Surveiller `01-pipeline\batch_gemini_log.txt` pour suivre l'avancement.

---

## ÉTAPE 7 — Commit

```
git add 01-pipeline/batch_gemini.py 01-pipeline/batch_gemini_log.txt _archive/trading-geek-whisper-elimine/
git commit -m "feat(transcription): batch gemini 203 videos pipeline setup + whisper archive"
```

---

## SÉCURITÉS ABSOLUES

- Jamais écrire GEMINI_API_KEY ou ANTHROPIC_API_KEY dans le code
- Vérifier `git check-ignore C:\trading-copilote\.env` avant tout push
- `python -m py_compile` obligatoire avant toute exécution
- Mode AUTO trading : BLOQUÉ (non concerné par cette mission)
