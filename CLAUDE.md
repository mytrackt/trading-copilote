# TRADEX-AI — Index Claude Code
> Lis ce fichier EN ENTIER puis suis le protocole. Aucune exception.

---

## RÈGLE 0 — PROTOCOLE DE DÉMARRAGE (ordre strict)

1. Lire ce fichier
2. Lire `00-pilotage\DECISIONS_VEROUILLEES.md` (toutes les règles verrouillées)
3. Lire le fichier le plus récent dans `00-pilotage\_context\` (état de la dernière session)
4. Lire `00-pilotage\DETTE_TECHNIQUE.md` (bugs connus avant tout dev)
5. Lire `00-pilotage\CLAUDE_CAPABILITIES_TRADING.md` (nouvelles capacités Claude pour TRADEX)
6. Annoncer : "📍 État : [résumé 1 ligne] — Prochaine action : [action]"
7. Attendre confirmation avant toute exécution

---

## PROJET EN UNE LIGNE

**TRADEX-AI** : trading temps réel méthode Belkhayate → NinjaTrader 8 → Claude API.
Mode Manuel (Abdelkrim décide) + Mode Auto (bloqué par défaut).

```
NT8 JSON (2s) → Python Engine → 3/4+2/3 filtre → Claude API → Signal 15 champs
                                                              → Mode Manuel : afficher
                                                              → Mode Auto : BLOQUÉ
```

---

## FICHIERS DE RÉFÉRENCE — LIRE SELON LE CONTEXTE

| Fichier | Contenu | Quand le lire |
|---|---|---|
| `00-pilotage\DECISIONS_VEROUILLEES.md` | Toutes les décisions verrouillées datées | TOUJOURS en démarrage |
| `00-pilotage\ARCHITECTURE_CONSTRUCTION.md` | 7 modules + flux de travail + gates | Avant tout développement |
| `00-pilotage\FEUILLE_DE_ROUTE.md` | Phases + missions + état | Pour planifier |
| `00-pilotage\GARDE_FOUS.md` | 42 garde-fous trading | Avant tout signal ou ordre |
| `00-pilotage\DETTE_TECHNIQUE.md` | Bugs connus | TOUJOURS en démarrage |
| `00-pilotage\_context\[dernier].md` | État de la dernière session | TOUJOURS en démarrage |
| `04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json` | 4142+ règles Belkhayate | Pour le cerveau IA |
| `00-pilotage\CLAUDE_CAPABILITIES_TRADING.md` | Capacités Claude applicables à TRADEX | **TOUJOURS en démarrage** — mise à jour de Claude |
| `04-cerveau-trading\KB_CLAUDE_CAPABILITIES.json` | KB structurée des capacités Claude | Avant tout développement moteur IA |

---

## RÈGLES TECHNIQUES NON NÉGOCIABLES

```
RACINE      : C:\trading-copilote\ (chemins absolus toujours)
CODE PYTHON : uniquement dans 05-saas\ et sous-dossiers
COMMITS     : Conventional Commits — jamais d'accents
PYTHON      : python -m py_compile fichier.py AVANT exécution
API KEY     : jamais dans le code → os.getenv("ANTHROPIC_API_KEY")
BASE_DIR    : os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
.env        : git check-ignore .env avant tout push
MODE AUTO   : AUTO_MODE = False — jamais activer sans autorisation
BRANCHES    : feature/module-XX → jamais coder sur main directement
MODULES     : max 200 lignes par MODULE_XX.md
```

---

## SÉCURITÉS TRADING ABSOLUES

1. **News Gate** : bloquer 30min avant NFP/FOMC/CPI (timezone ET)
2. **Circuit Breaker** : timeout 15s → retry 2x → fallback ATTENDRE
3. **Staleness Monitor** : données périmées → BLOCKED
4. **Fallback local** : confiance MAX 65%, mode Auto INTERDIT
5. **Risque par trade** : 0,25% min — 0,50% max du capital
6. **R/R** : ≥ 1:2 sur GC/HG/CL — ≥ 1:1,5 sur ZW
7. **Atomic writes** : tempfile + os.replace — jamais json.dumps() direct
8. **Disclaimer légal** : visible en permanence dans l'interface

---

## ACTIFS VERROUILLÉS

```
TRADING     : GC (Or) · HG (Cuivre) · CL (Pétrole) · ZW (Blé)
CONFIRMATION: DX (Dollar) · ES (SP500) · VX (VIX)
RÉFÉRENCE   : MBT (Bitcoin) · 6J (Yen) — JAMAIS d'ordre sur ces deux
```

---

## STRUCTURE DU PROJET

```
C:\trading-copilote\
├── 00-pilotage\        ← Gouvernance (DECISIONS_VEROUILLEES, ARCHITECTURE, etc.)
│   └── _context\       ← READMEs de transition (état session par session)
├── 01-moteur-transvideo\ ← Pipeline transcription YouTube
├── 02-sources-brutes\  ← PDFs, méthode Belkhayate
├── 03-transcriptions\  ← Sorties Gemini (en cours — 203 vidéos)
├── 04-cerveau-trading\ ← KNOWLEDGE_BASE_MASTER.json (1313+ règles)
├── 05-saas\            ← TOUT le code Python (engine/, config/, utils/)
├── 06-skills\          ← Skills Belkhayate .md
├── _archive\           ← Gelé — ne pas réutiliser
└── _temp\              ← Temporaire
```

---

## MÉTHODE DE TRANSCRIPTION VIDÉO — DÉCISION VERROUILLÉE

> ⚠️ NE PLUS CHERCHER, NE PLUS COMPARER. Cette méthode est définitive.

**Méthode officielle : Gemini 2.5 Flash multimodal**

```
Vidéos MP4 (D:\Belkhayate-Videos ou autre dossier)
    ↓
05-saas\utils\gemini_transcriber.py  → Gemini 2.5 Flash
    (voit audio + écran simultanément)
    (produit *_gemini.txt avec [VISUEL:] [REGLE:] [QUALITE_VIDEO:])
    ↓
05-saas\knowledge_base\transcript_processor_gemini_batch.py → Claude Batch API  ← DÉFAUT (-50% coût)
    (traitement parallèle, résultats < 1h, résumable avec --resume)
    ↓   si erreurs sur certaines vidéos → repasser ces vidéos avec :
05-saas\knowledge_base\transcript_processor_gemini.py → Claude API synchrone (fallback)
    ↓
04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
```

**Pourquoi Gemini et pas les autres :**
- Gemini voit **audio + écran simultanément** (multimodal natif)
- Détecte les règles visuelles (graphiques, indicateurs à l'écran)
- Résultat prouvé : 4080 règles vs 1398 avec Whisper (×3 de richesse)
- Décision prise en S35-S40, validée sur 100 vidéos Belkhayate

**Méthodes abandonnées — NE PAS réutiliser :**
- ~~yt-dlp + Whisper + Claude~~ → ancien TRANSVIDEO (1398 règles, qualité faible)
- ~~watch skill~~ → interactif seulement, pas de pipeline batch
- ~~SRT YouTube + ffmpeg~~ → pas de contenu visuel

**Clé requise :** `GEMINI_API_KEY` dans `.env`
**Modèle :** `gemini-2.5-flash` (stable, pas experimental)

**Pour nouvelles vidéos (hors Belkhayate) :**
Adapter `gemini_transcriber.py` → changer VIDEO_DIR + prompt Gemini + OUTPUT_DIR

---

## [EXÉCUTION] Carte de confirmation & garde-fous chiffrés (Scénario B — v1.1)

- Toute sortie d'ordre du Checker DOIT respecter le schéma JSON figé confirmation_card v1.0.
- Aucun ordre ne passe en SENT sans : stop présent + execution_guardrails.validate_order() OK
  + approbation humaine explicite (tap).
- validate_order() ne renvoie JAMAIS SENT. STAGED -> SENT = send_order() uniquement, déclenché par l'humain.
- Verdict NO_TRADE obligatoire si COG ambigu OU filtre Belkhayate non passé. Jamais de trade forcé.
- Interdiction averaging down maintenue (décision verrouillée).
- Coupe-circuit journalier + news blackout actifs.
- Instruments : NQ, ES uniquement.
- Tant que GUARDRAILS["config_validated"] = False : tout ordre est bloqué (volontaire).

---

## PROTOCOLE FIN DE SESSION

```
1. Générer 00-pilotage\_context\README_TRANSITION_[date].md
2. Mettre à jour DECISIONS_VEROUILLEES.md si nouvelles décisions
3. git add . && git commit -m "chore: session [date] terminee"
4. git push origin main
```

---

## PROFIL UTILISATEUR

Abdelkrim — débutant technique — Windows 11 — PowerShell 7.6.2
Expliquer chaque commande comme à un élève du primaire. Une commande à la fois.

---

## GUARDRAIL COMPTEUR DE MESSAGES

Après 20 messages dans une session → générer README de transition IMMÉDIATEMENT.

---

*Source de vérité : `00-pilotage\DECISIONS_VEROUILLEES.md`*
*Architecture : `00-pilotage\ARCHITECTURE_CONSTRUCTION.md`*
*Dernière mise à jour : 30/06/2026 — Session S46*
