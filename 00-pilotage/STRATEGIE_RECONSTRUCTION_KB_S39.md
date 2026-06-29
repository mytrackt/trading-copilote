# STRATÉGIE INFAILLIBLE — Reconstruction KB TRADEX-AI
> Auteur : Cowork S39 | Date : 28/06/2026 | Statut : VALIDÉ GO

---

## 1. ANALYSE CAUSES RACINES

### RC-1 — Whisper = audio-only sans contexte visuel
Belkhayate enseigne en montrant son écran (NinjaTrader, TradingView). Whisper transcrit l'audio
mais ignore toutes les références visuelles ("vous voyez ici", "regardez là"). Résultat : les règles
visuelles ne sont pas capturées. La KB Whisper est incomplète par construction.

### RC-2 — Contamination Whisper (cause première d'élimination)
D-S30-9 verrouillée : Whisper éliminé car pas de synchro audio-image. Les transcripts Whisper
ne capturent pas les indicateurs à l'écran (COG, Belkhayate Trend, pivots). Méthode inadaptée.

### RC-3 — Double contamination Gemini existant (DÉCOUVERTE S39 🔴)
Les 121 transcripts Gemini dans `transcripts-gemini/` incluent :
- Contenu Belkhayate FR → valide
- **OFTC Lessons (Order Flow Trading Course)** → méthode d'un AUTRE trader → À EXCLURE
Ces fichiers OFTC ne doivent JAMAIS entrer dans la KB Belkhayate.

### RC-4 — Prompt [REGLE:] trop permissif
Constat sur V30_gemini.txt (23 règles) : les "règles" taguées sont des règles de prop trading firms,
pas des règles de la méthode Belkhayate. Le prompt actuel ne filtre pas sur la méthode Belkhayate.
Résultat : des règles parasites peuvent polluer la KB.

### RC-5 — Corpus MP3 mal caractérisé (DÉCOUVERTE S39)
Les 110 MP3 ne sont PAS tous des "Lessons". Composition réelle :
- ~25 "Lesson XX" (nommés explicitement)
- ~16 "Live" (sessions live trading)
- ~13 "Extrait" (courts clips)
- ~56 autres (Trading Videos, guides, présentations, crypto, etc.)
Priorité d'extraction des règles : Lessons > Videos > Lives > Extraits.

---

## 2. CONTRAINTES TECHNIQUES

| Contrainte | Valeur | Impact |
|---|---|---|
| Gemini audio-only | 32 tok/s | Limite ~8,7h → chunking inutile pour MP3 |
| Gemini video | 290 tok/s | Limite ~57 min → chunking actif |
| max_output_tokens | 32768 | ≈ 2h d'enseignement oral → suffisant |
| MP3 total | 1289 Mo | ~21,5h de contenu |
| Rate limit Gemini | géré (retry 60s) | Non bloquant |
| Noms accentués | risque codec | `_chemin_upload()` obligatoire → CONSERVER |
| Checkpoint | `if out_path.exists()` | Crash-safe → relançable sans perte |

---

## 3. STRATÉGIE — 5 PHASES SÉQUENTIELLES

### ─── PHASE 0 : PRE-FLIGHT (5 min — PowerShell) ───────────────────

**Objectif** : Archiver la KB actuelle + vérifier si MP4 disponibles.

```powershell
# Étape 0A — Archivage KB OBLIGATOIRE (D-S38-3)
git tag KB-WHISPER-1398
```
→ Confirme avant de continuer.

```powershell
# Étape 0B — Copie physique (double sécurité)
copy C:\trading-copilote\04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json C:\trading-copilote\04-cerveau-trading\KB_BACKUP_WHISPER_1398.json
```

```powershell
# Étape 0C — Vérifier si MP4 disponibles (clé stratégique)
dir D:\Belkhayate-Videos\*.mp4 | measure -Line
```
→ Si > 0 MP4 → lire §3.1 (stratégie VIDEO — qualité maximale)
→ Si 0 MP4 → lire §3.2 (stratégie AUDIO — bonne qualité)

---

### 3.1 — STRATÉGIE A : MP4 DISPONIBLES (qualité maximale)

Si les MP4 originaux existent encore sur D:\Belkhayate-Videos :

**Action** : Vérifier la correspondance entre MP3 (audio/) et MP4 (D:\) par YouTube ID.
Les MP3 ont le format `{youtube_id}_{titre}.mp3`. Chercher les MP4 correspondants.

Si correspondance ≥ 80 MP4 trouvés → utiliser `gemini_transcriber.py` (version vidéo originale).
→ Qualité maximale : audio + visual + [VISUEL:] + [REGLE:]
→ Résultat attendu : 15-25 règles par Lesson (vs 5-10 en audio-only)

---

### 3.2 — STRATÉGIE B : MP3 UNIQUEMENT (audio optimisé)

Si MP4 non disponibles → créer `gemini_transcriber_audio.py` avec le prompt optimisé ci-dessous.

---

### ─── PHASE 1 : TRIAGE CORPUS (30 min — Claude Code) ──────────────

**Objectif** : Prioriser les 110 MP3 par densité de règles attendue.

Script à créer `05-saas/utils/triage_mp3.py` :
```python
# Classer les 110 MP3 en 4 catégories
# PRIORITÉ 1 — Lessons (contenu pédagogique concentré)
# PRIORITÉ 2 — Trading Videos (Vidéo 4, 5, 6, 9, 16, 25...) 
# PRIORITÉ 3 — Guides et présentations (Gravity Center guide, etc.)
# PRIORITÉ 4 — Lives, Extraits (densité de règles plus faible)
# EXCLURE — Crypto (hors scope Belkhayate Method sur futures)
```

**Fichiers suspects à vérifier manuellement** (hors scope potentiel) :
- `3750psYk1bo_le Cryptotrading, Chance pour le Maroc et l'Afrique ？ (Partie 1).mp3`
- `Akep8YPVvtw_le Cryptotrading, Chance pour le Maroc et l'Afrique ？ (Partie 2).mp3`
- `9azfF45PhRU_Arrêter de chercher à comprendre et Prendre l'Argent sur le Nasdaq.mp3`

→ Ces fichiers traitent de marchés HORS SCOPE (crypto, Nasdaq interdit par CLAUDE.md).
→ À décider : inclure (contient peut-être des règles de méthode) ou exclure (hors scope).

---

### ─── PHASE 2 : PROMPT AUDIO OPTIMISÉ ─────────────────────────────

**Le prompt est la clé de la fiabilité.** Version améliorée vs le prompt du PROMPT_CLAUDE_CODE_S39_GEMINI_AUDIO.md :

```python
def construire_prompt_audio(nom_fichier: str) -> str:
    """Prompt Gemini MP3 audio-only — Version infaillible S39."""
    return """Tu es un transcripteur expert spécialisé dans la méthode de trading Belkhayate.
Tu transcris un enregistrement audio de Mustapha Belkhayate (trader marocain, champion du monde 1999).

═══ RÈGLE 1 — FIDÉLITÉ ABSOLUE ═══
Transcris EXACTEMENT ce que Belkhayate dit. Pas de résumé, pas de paraphrase, pas de correction.
Si tu n'es pas sûr d'un mot, écris [INAUDIBLE] — jamais un mot inventé.
Temperature 0.0 appliqué : copie conforme de l'audio, rien d'autre.

═══ RÈGLE 2 — PAS DE VISUEL ═══
Tu n'as accès qu'à l'audio. Tu ne vois AUCUN écran, AUCUN graphique, AUCUN indicateur.
Quand Belkhayate dit "vous voyez ici", "regardez là", "ici on voit" :
→ Écris EXACTEMENT ses mots, puis ajoute [REF_ECRAN: description audio-seulement]
INTERDIT : inventer une description visuelle. INTERDIT : mettre [VISUEL: ...] dans la sortie.

═══ RÈGLE 3 — MARQUAGE DES RÈGLES BELKHAYATE ═══
Quand Belkhayate énonce une RÈGLE de SA méthode (indicateurs Belkhayate, COG, Gravity Center,
Belkhayate Trend, pivots Sol/Mi/Re/Do, Énergie, corrélations GC/HG/CL/ZW) :
→ Marque-la : [REGLE_BK: formulation complète et autonome de la règle]

Critères d'une vraie règle Belkhayate :
  ✅ Décrit un comportement du marché selon SES indicateurs
  ✅ Indique quand acheter, vendre, ou attendre selon SA méthode
  ✅ Donne une règle de gestion du risque ou de position
  ❌ PAS une règle générique de trading (type "gérer les émotions")
  ❌ PAS une règle de prop firm ou de plateforme tierce
  ❌ PAS une anecdote personnelle ou une histoire

═══ RÈGLE 4 — MARQUAGE DES CONCEPTS ═══
Quand Belkhayate définit ou explique un concept de sa méthode :
→ Marque-le : [CONCEPT_BK: nom du concept | définition donnée par Belkhayate]

═══ RÈGLE 5 — COMPLÉTUDE ═══
Transcris jusqu'à la FIN de l'audio. Ne t'arrête pas avant la fin.
Si la transcription est longue, continue — ne résume jamais les dernières minutes.
Marque la fin avec : [FIN_TRANSCRIPTION]

═══ RÈGLE 6 — LANGUES ═══
Belkhayate enseigne principalement en FRANÇAIS. Il peut alterner français/arabe/anglais.
Transcris dans la langue qu'il utilise à chaque moment. Ne traduis pas.

FORMAT DE SORTIE :
[DEBUT_AUDIO: {nom_fichier}]
... transcription ...
[FIN_TRANSCRIPTION]

Exemple correct :
"Quand vous voyez le Centre de Gravité" [REF_ECRAN: Belkhayate montre quelque chose à l'écran]
"...qui est dans le vert, et que le prix revient dessus,"
[REGLE_BK: En tendance haussière, quand le prix revient sur le COG vert, c'est une zone d'entrée achat potentielle selon la méthode Belkhayate]
"c'est exactement ce qu'on attendait."

Commence maintenant. Transcris l'audio complet sans interruption.
"""
```

**Améliorations vs version S38 :**
| Aspect | Version S38 | Version S39 (optimisée) |
|---|---|---|
| Fidélité | Non spécifiée | "Exactement" + [INAUDIBLE] |
| Références visuelles | Pas de marquage | [REF_ECRAN:] honnête |
| Filtre règles | Trop permissif | Critères Belkhayate stricts |
| Concepts | Non marqués | [CONCEPT_BK:] |
| Complétude | Non garantie | [FIN_TRANSCRIPTION] |
| Tag dédié | [REGLE:] générique | [REGLE_BK:] spécifique |

---

### ─── PHASE 3 : BATCH EXÉCUTION ────────────────────────────────────

**Ordre de traitement (par valeur KB décroissante) :**

```
BATCH 1 — Lessons numérotées (25 fichiers) — lancer en premier
  Ex: Lesson 27, 28, 30, 35, 38, 39, 41, 42, 43, 44, 45, 46...
  Résultat attendu : 5-15 règles Belkhayate par Lesson

BATCH 2 — Trading Videos Belkhayate (Vidéo 4, 5, 6, 9, 16, 25...) (~15 fichiers)
  + Guides spécifiques (Gravity Center, Belkhayate Trend, etc.)

BATCH 3 — Live sessions + 5 Days Challenge (~16 fichiers)
  Densité de règles variable selon le marché du jour

BATCH 4 — Autres vidéos thématiques (~40 fichiers)
  Décision manuelle sur les fichiers crypto/Nasdaq

SKIP — Extraits < 5 min (à décider manuellement si non informatifs)
```

**Checkpoint de validation après BATCH 1 (obligatoire) :**
- Inspecter 3 transcripts manuellement
- Vérifier : présence de [REGLE_BK:] · absence de [VISUEL:] · [FIN_TRANSCRIPTION] présent
- Si problème détecté → STOP · corriger le prompt · relancer

---

### ─── PHASE 4 : VALIDATION QUALITY GATE ─────────────────────────────

**Script de validation `05-saas/utils/validate_transcripts_audio.py` :**

```python
# Métriques par transcript :
# M1 — [REGLE_BK:] count (attendu > 0 pour Lessons, ≥ 1 pour videos)
# M2 — [VISUEL:] count (attendu = 0 STRICT — si > 0 → ALERTE HALLUCINATION)
# M3 — [FIN_TRANSCRIPTION] présent (attendu = True)
# M4 — [INAUDIBLE] count (info — si > 10% du texte → qualité audio faible)
# M5 — Longueur (< 200 mots → probablement intro/outro seulement)

# Seuils de qualité :
# VALIDÉ : M2=0 ET M3=True ET M1≥1 (pour Lessons)
# À VÉRIFIER : M2=0 ET M3=True ET M1=0 (pas de règle trouvée)
# REJETÉ : M2>0 (hallucination visuelle détectée)
```

**Critère GO pour KB reconstruction :**
- ≥ 80% des Lessons validées (M2=0, M3=True)
- Zéro transcript REJETÉ
- [REGLE_BK:] count total > 200 sur l'ensemble des Lessons

---

### ─── PHASE 5 : DÉCONTAMINATION GEMINI EXISTANT ──────────────────

**Action obligatoire AVANT d'intégrer les 121 transcripts Gemini existants dans la KB :**

Fichiers à EXCLURE définitivement (méthode AUTRE que Belkhayate) :
```
OFTC Lesson 4 - Order Flow Terms_gemini.txt
OFTC Lesson 11 - Order Flow Price Rejection_gemini.txt
OFTC Lesson 16 - Order Flow Reversal Setups_gemini.txt
OFTC Lesson 17 - Order Flow Continuation Setups_gemini.txt
OFTC Lesson 19 Part A..._gemini.txt
```
→ Créer un dossier `transcripts-gemini/_EXCLURE/` et y déplacer ces fichiers.
→ Ne JAMAIS les envoyer à transcript_processor.py.

Fichiers V30, V27 etc. → vérifier le contenu : V30 parle de "prop firms" → règles de prop firm ≠ règles Belkhayate → filtrées par [REGLE_BK:] dans le nouveau prompt.

---

## 4. PLAN DE VALIDATION FINAL

| Étape | Mesure | Seuil GO |
|---|---|---|
| Post-BATCH 1 (25 Lessons) | [REGLE_BK:] total | ≥ 50 règles |
| Post-BATCH complet | [VISUEL:] dans sorties | 0 (zéro tolérance) |
| Post-BATCH complet | [FIN_TRANSCRIPTION] présents | ≥ 90% des fichiers |
| Post-KB reconstruction | Règles totales | ≥ 800 (règles qualifiées BK) |
| Post-KB reconstruction | SHA256 mis à jour | Obligatoire |
| Tests | 37/37 PASS | Obligatoire avant commit |

---

## 5. RISQUES RÉSIDUELS ET MESURES CORRECTIVES

| Risque | Probabilité | Mesure corrective |
|---|---|---|
| Gemini tronque avant la fin | FAIBLE | [FIN_TRANSCRIPTION] absent → détecter → retranscrire |
| Contenu hors scope (crypto) | CERTAINE | Exclure manuellement les 2-3 fichiers crypto |
| Règles de qualité inégale entre Lessons | MOYENNE | Spot-check manuel 5 règles par Lesson |
| Durée batch > 21h (crash) | FAIBLE | Checkpoint existant → relancer sans perte |
| MP4 disponibles sur D:\ ignorés | POSSIBLE | Vérification OBLIGATOIRE Phase 0C avant tout |

---

## 6. DÉCISIONS À PRENDRE (Abdelkrim)

1. **D-S39-1 (à valider)** : Fichiers crypto hors scope → INCLURE ou EXCLURE du batch ?
2. **D-S39-2 (à valider)** : Si MP4 disponibles sur D:\ → stratégie VIDEO (qualité max) ou rester sur AUDIO (simplicité) ?
3. **D-S39-3 (à valider)** : Remplacer `[REGLE:]` par `[REGLE_BK:]` dans `transcript_processor.py` aussi ?

---

## 7. RÉSUMÉ EXÉCUTIF

```
ÉTAT : KB contaminée Whisper (1398 règles) + corpus Gemini contaminé OFTC
PLAN : MP3 audio → Gemini optimisé → validation quality gate → KB propre

SÉQUENCE :
  ✋ Phase 0 : git tag + copie KB + vérifier D:\ MP4 (5 min)
  ↓  Phase 1 : Triage corpus MP3 (30 min Claude Code)
  ↓  Phase 2 : Créer gemini_transcriber_audio.py + prompt optimisé
  ↓  Phase 3 : Batch 25 Lessons → validate → continuer
  ↓  Phase 4 : Quality gate → VALIDÉ ou CORRIGÉ
  ↓  Phase 5 : Décontamination OFTC Gemini existant
  ↓  Rebuild : transcript_processor.py → nouvelle KB propre

RÉSULTAT ATTENDU : KB > 800 règles Belkhayate qualifiées (vs 1398 Whisper non filtrées)
NOTE : 800 règles qualifiées > 1398 non filtrées en termes de fiabilité
```

---

*TRADEX-AI · Stratégie KB S39 · 28/06/2026*
*À lire avant toute action : vérifier D:\Belkhayate-Videos d'abord (Phase 0C)*
