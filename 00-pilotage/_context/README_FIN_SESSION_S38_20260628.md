# README DE TRANSITION — TRADEX-AI
Date : 28/06/2026 | Session : S38 | KB : 1398 règles (⚠️ CONTAMINATION CONFIRMÉE — reconstruction planifiée)

---

## 1. ÉTAT ACTUEL DU PROJET

Phase C Track A terminée (S37). En S38 : audit KB complet (P0→P3 exécutés, P4 reporté S39).
**Découverte critique S38** : la KB (1398 règles) est construite entièrement depuis des transcripts
Whisper (méthode éliminée). Les 121 fichiers Gemini existants couvrent un corpus **différent**
(épisodes FR vs Lessons EN). **Décision actée** : Option A — re-transcrire les 110 MP3 Lessons
avec Gemini, reconstruire KB propre. Mode AUTO toujours BLOQUÉ.

---

## 2. MISSIONS TERMINÉES CETTE SESSION

| Mission | Description | Commit | Statut |
|---------|-------------|--------|--------|
| §7.1 DETTE | Clé Finnhub régénérée + validée (`finnhub_disponible=True`, `count=2`) | 96a9b3d | ✅ |
| pytest | Installation pytest-9.1.1 | — | ✅ |
| P0 — Baseline | KB commitée · 37/37 tests PASS (21 guardrails + 16 signal + test_claude_brain) | — | ✅ |
| P1 — Dépendances KB | Cartographie : 1 lecteur runtime (`claude_brain.py`) · 14 fichiers dépendants · 11 catégories NON hardcodées moteur | — | ✅ |
| P2 — Snapshot KB | Corpus Whisper (110 MP3/Lessons EN) ≠ Corpus Gemini (121 fichiers/épisodes FR) — DISJOINTS | — | ✅ |
| Décision Option A | Re-transcrire 110 MP3 Lessons avec Gemini (iso-contenu · qualité Gemini) | — | ✅ VERROUILLÉ |
| P3 — Faisabilité | 110 MP3 · 1289 Mo · ~21,5h · coût $5–12 · 3 modifs transcripteur identifiées | — | ✅ |

**3 modifications nécessaires dans `gemini_transcriber.py` avant lancement :**
1. 🔴 Source : `VIDEO_DIR` → `audio\` + `*.mp4` → `*.mp3`
2. 🔴 MIME : `video/mp4` → `audio/mpeg`
3. 🟠 Prompt : retirer `[VISUEL:]` → variante audio-only (sinon hallucinations sur MP3)

**Point positif** : le checkpoint existant (`if out_path.exists(): SKIP`) rend le run crash-safe.
Les sorties seront nommées `{ID}_{titre}_gemini.txt` → l'ID YouTube revient dans le nom (problème jointure P2 résolu).

---

## 3. MISSION SUIVANTE

**P4 — Analyse risques + GO/NO-GO** (reporté de S38)

Prompt P4 prêt — à lancer dans Claude Code :
- R1 : hallucination prompt visuel sur MP3 (BLOQUANT si non corrigé)
- R2 : perte KB actuelle → archivage git obligatoire
- R3 : qualité Gemini audio seul vs vidéo (indicateurs visuels COG/bandes)
- R4 : compatibilité format sortie Gemini → `transcript_processor.py`
- R5 : quota Files API sur 110 uploads séquentiels
- R6 : MP3 corrompus / silencieux
- R7 : divergence règles Gemini vs Whisper → tests après chaque batch de 10
- R8 : durée 21,5h → crash-safe via checkpoint

Après P4 : si GO → créer `gemini_transcriber_audio.py` (copie adaptée, ne pas écraser l'original MP4) → test sur 1 MP3 → lancement batch.

---

## 4. DÉCISIONS PRISES EN S38

| ID | Décision | Statut |
|----|----------|--------|
| D-S38-1 | Option A — re-transcrire 110 MP3 Lessons avec Gemini (pas Gemini-only épisodes FR, pas fusion) | VERROUILLÉ |
| D-S38-2 | Créer `gemini_transcriber_audio.py` (copie adaptée MP3) — ne JAMAIS modifier l'original MP4 | VERROUILLÉ |
| D-S38-3 | KB Whisper archivée avant tout remplacement (`git tag KB-WHISPER-1398` + copie physique) | À FAIRE P4 |

---

## 5. DÉCISIONS TEMPORAIRES

Aucune.

---

## 6. PROBLÈMES OUVERTS / BLOCAGES

| # | Problème | Priorité | Action requise |
|---|----------|----------|----------------|
| 🔴 KB | 1398 règles construites sur Whisper (méthode éliminée) — reconstruction nécessaire | CRITIQUE | Exécuter P4 → P5 → lancement batch Gemini |
| ⏳ 5 | Migration `google-generativeai` → `google-genai` | P2 | Avant mise en prod — voir DETTE §5 |
| ⏳ 7.2 | GDELT 429 transitoire | BAS | Code gère déjà ; se résorbe en prod |

---

## 7. STACK TECHNIQUE GELÉE

```
Python 3.12 / NinjaTrader 8 ATI port 36973
claude-sonnet-4-6 (KB + signaux) / gemini-2.5-flash (transcription)
FRED API · EIA API v2 · CFTC OData v4 · Finnhub · GDELT
Atomic writes : tempfile + os.replace
SDK installé : google-genai 2.9.0 (actif) + google-generativeai 0.8.6 (ancien — DETTE §5)
```

---

## 8. ÉTAT DES REPOS FIN SESSION

```
Branche active  : main
Dernier commit  : 96a9b3d — docs(debt): §7.1 Finnhub résolu (S38)
KB              : 1398 règles · SHA256 = bcaaaeed... · ⚠️ CONTAMINATION WHISPER
Tests           : 37/37 PASS (21 guardrails + 16 signal + test_claude_brain)
.env            : 5 clés présentes · gitignore ✅
data/           : gitignore (cot/macro/news_data.json)
MP3             : 110 fichiers dans 03-transcriptions\nouvelles-sources\belkhayate-youtube\audio\
Gemini existants: 121 fichiers dans transcripts-gemini\ (corpus FR différent — à intégrer plus tard)
```

---

## 9. COMMANDES GIT (PowerShell — JAMAIS &&)

```powershell
git add 00-pilotage\_context\README_FIN_SESSION_S38_20260628.md
```
→ Attendre confirmation

```powershell
git commit -m "docs(session): README S38 - audit KB contamination + plan reconstruction Gemini"
```
→ Attendre confirmation

```powershell
git push origin main
```
→ Attendre confirmation

---

## 10. PRE-FLIGHT SESSION SUIVANTE

- [ ] Lire `CLAUDE.md` en entier
- [ ] Lire ce fichier (`README_FIN_SESSION_S38_20260628.md`)
- [ ] Lire `DETTE_TECHNIQUE.md` (§5 + §7.2)
- [ ] Confirmer que le dernier commit est `96a9b3d` ou le commit du README S38
- [ ] Mode AUTO = False — ne pas toucher
- [ ] Lancer **P4** dans Claude Code (prompt disponible dans ce README §3)
- [ ] Après GO P4 : créer `gemini_transcriber_audio.py` → tester sur 1 seul MP3 avant batch

---

## 11. PHRASE D'AMORÇAGE SESSION SUIVANTE

```
Session S39 — TRADEX-AI.
Dernier commit main = [hash commit README S38].
KB Master = 1398 règles · SHA256 = bcaaaeed · ⚠️ CONTAMINATION WHISPER confirmée (S38).
Option A validée : re-transcrire 110 MP3 Lessons avec Gemini.
P4 à lancer (analyse risques R1-R8 + GO/NO-GO) avant création gemini_transcriber_audio.py.
```

---

## 12. ÉTAT KB

| Indicateur | Valeur |
|-----------|--------|
| Règles totales | 1398 |
| Vidéos dans KB | 108 |
| SHA256 actif | `bcaaaeed...` (complet dans SHA256_KB_MASTER.md) |
| Statut KB | ⚠️ CONTAMINATION — construite sur Whisper (méthode éliminée) |
| Dernière modif KB | S35 — fusion Chap5 (+14 briques) |
| KB modifiée S38 | ❌ Non — audit uniquement, aucune modif |
| Prochaine cible KB | Re-transcription 110 MP3 avec Gemini → rebuild complet |
| Corpus Gemini dispo | 121 fichiers (épisodes FR) — contenu neuf, à intégrer APRÈS reconstruction Lessons |
| MP3 disponibles | 110 fichiers (corpus Lessons EN) — prêts pour Gemini |

*Source : `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` · `04-cerveau-trading\SHA256_KB_MASTER.md`*

---

*TRADEX-AI · README de transition S38 · 28/06/2026*
