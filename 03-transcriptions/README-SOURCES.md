# SOURCES DE TRANSCRIPTIONS BELKHAYATE
> Derniere mise a jour : 23/06/2026 — Session S20

---

## ⚠️ AVERTISSEMENT GENERAL

Ces dossiers contiennent des transcriptions de videos de trading de Mustapha Belkhayate.
Belkhayate enseigne en partageant son ecran (NinjaTrader, TradingView).
Toute transcription AUDIO SEUL est structurellement incomplete :
elle ne capture pas ce qu'il montre a l'ecran.

**REGLE ABSOLUE : ne jamais integrer une regle en KB sans verifier
sa completude et sa coherence avec la methode Belkhayate.**

---

## SOURCE A — ARCHIVEE / NON FIABLE A 100%

```
03-transcriptions\transcripts-bruts\
```

- **Methode** : Whisper medium, depuis MP3 telecharges via yt-dlp (YouTube)
- **Fichiers** : 142 fichiers `whisper_[videoID].txt`
- **Format** : texte brut sans ponctuation, tout en minuscules
- **Statut** : 🗄️ ARCHIVEE — NON FIABLE A 100%

### Limites connues (SOURCE A)
- Hallucinations Whisper frequentes sur les termes techniques :
  "Belkhayate" → `belgrède` / `belgeat` / `bachiat`
  "VWAP" → `vivoirs` / `viwa` / `vivos`
  "squeeze" → `sprint box` / `springboks`
- Audio MP3 compresse → perte de qualite → plus d'erreurs de transcription
- Zero contexte visuel : les references ecran ("vous voyez ici", "regardez la")
  sont transcrites mais inutilisables sans la video
- Aucune ponctuation → lecture difficile, extraction de regles penible

### Usage autorise
- Comparaison et reference historique uniquement
- Ne jamais utiliser comme source unique pour la KB
- Ne jamais integrer un chiffre ou prix issu de cette source

---

## SOURCE B — ARCHIVEE / NON FIABLE A 100%

```
03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts\
```

- **Methode** : Whisper medium (FR), depuis MP4 locaux (D:\Belkhayate-Videos)
- **Fichiers** : 164 fichiers avec noms lisibles (`titre_video.txt`)
- **Format** : texte avec ponctuation et majuscules (plus lisible que SOURCE A)
- **Manifeste qualite** : `MANIFESTE_TRANSCRITS.csv` (109 VALIDE / 1 HORS_PERIMETRE)
- **Statut** : 🗄️ ARCHIVEE — NON FIABLE A 100%

### Limites connues (SOURCE B)
- Memes hallucinations Whisper que SOURCE A (meme moteur)
- Audio MP4 local de meilleure qualite → legerement moins d'erreurs qu'en A
- Zero contexte visuel : meme probleme fondamental qu'en A
- Les 110 videos presentes dans A et B ont ete comparees dans
  `00-pilotage\INVENTAIRE_TRANSCRITS_BELKHAYATE.md`

### Avantage sur SOURCE A
- Format plus lisible (ponctuation + majuscules)
- Noms de fichiers lisibles (titre de la video)
- A preferer sur SOURCE A pour l'audit manuel si Gemini indisponible

### Usage autorise
- Comparaison et reference historique uniquement
- Peut servir de fallback si SOURCE C (Gemini) echoue sur une video
- Ne jamais integrer un chiffre ou prix issu de cette source

---

## SOURCE C — SOURCE OFFICIELLE (en cours de constitution)

```
03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts-gemini\
```

- **Methode** : Gemini 1.5 Flash multimodal (audio + visuel simultanes)
- **Fichiers** : `[nom_video]_gemini.txt` (en cours de generation)
- **Format** : transcript enrichi avec balises :
  `[VISUEL: description de l'ecran]` — contexte visuel capture
  `[REGLE: formulation de la regle]` — regles trading identifiees
  `[ECRAN_CHANGE_RAPIDE]` — moment non capturé (videos live)
  `[QUALITE_VIDEO: FAIBLE/MOYENNE/BONNE_APPROX]` — qualite estimee
  `[TYPE: COURS_PEDAGOGIQUE / LIVE_TRADING]` — type de video
- **Rapport qualite** : `RAPPORT_QUALITE_GEMINI.md` (genere automatiquement)
- **Statut** : ✅ SOURCE OFFICIELLE — FIABLE (avec reserves ci-dessous)

### Limites connues (SOURCE C)
- Descriptions visuelles approximatives si video basse resolution
- Videos live : moments rapides marques `[ECRAN_CHANGE_RAPIDE]`
- Prix chiffrés visuels : interdits dans les descriptions (regles Belkhayate
  verbales uniquement) — seuls les prix prononces verbalement sont transcrits
- Modele IA = peut se tromper sur l'identification d'un indicateur
  si l'ecran est charge ou peu lisible

### Usage autorise
- Source principale pour enrichissement KB
- Les `[REGLE: ...]` sont directement exploitables pour la KB
- Les `[VISUEL: ...]` donnent le contexte sans les chiffres exacts
- Toujours croiser avec SOURCE B en cas de doute sur une regle

---

## TABLEAU DE SYNTHESE

| | SOURCE A | SOURCE B | SOURCE C |
|---|---|---|---|
| Methode | Whisper MP3 | Whisper MP4 | Gemini multimodal |
| Contexte visuel | ❌ Non | ❌ Non | ✅ Oui |
| Hallucinations Whisper | 🔴 Frequentes | 🟠 Rares | 🟢 Quasi nulles |
| Format | Brut | Lisible | Structure enrichi |
| Fiabilite KB | ❌ NON | ❌ NON | ✅ OUI (avec reserves) |
| Statut | 🗄️ Archive | 🗄️ Archive | ✅ Officiel |
| Usage | Reference seule | Fallback | Production |

---

## REFERENCE CROISEE

- Inventaire complet A+B : `00-pilotage\INVENTAIRE_TRANSCRITS_BELKHAYATE.md`
- Rapport audit comparaison A vs B : `00-pilotage\RAPPORT_AUDIT_COMPARAISON_TRANSCRITS.md`
- Rapport qualite Gemini : `RAPPORT_QUALITE_GEMINI.md` (genere par le pipeline)
- Prompt pipeline Gemini : `00-pilotage\_context\PROMPT_CLAUDE_CODE_GEMINI_PIPELINE.md`
- Prompt audit Whisper : `00-pilotage\_context\PROMPT_CLAUDE_CODE_AUDIT_V3_FINAL.md`
