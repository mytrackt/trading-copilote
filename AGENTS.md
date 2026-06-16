# TRADING-COPILOTE — Instructions Claude Code
> Lis ce fichier EN ENTIER avant toute action. Aucune exception.

---

## RÈGLE 0 — PROTOCOLE DE DÉMARRAGE OBLIGATOIRE

Chaque nouvelle session suit cet ordre exact :

1. Lire ce fichier (AGENTS.md) — déjà fait
2. Lire le fichier le plus récent dans `_context/` (date la plus récente)
3. Annoncer exactement : "📍 Phase X — État : [résumé 1 ligne] — Prochaine action : [action]"
4. Attendre confirmation de l'utilisateur avant toute exécution

Ne jamais sauter une étape. Ne jamais supposer l'état du projet sans lire `_context/`.

---

## PROJET EN UNE LIGNE

Construire **TRADEX-AI** : un système de trading temps réel basé sur la méthode Belkhayate,
connecté à NinjaTrader 8, avec mode Manuel (Abdelkrim décide) et mode Auto (exécution automatique).

---

## VISION SYSTÈME

```
NinjaTrader 8 (données live) → Python Engine (surveillance 2s) → Claude API (signal)
                                        ↓
                          Mode Manuel : afficher signal → Abdelkrim décide
                          Mode Auto   : exécuter ordre via NT8 ATI (port 36973)
```

**Ce n'est PAS un système screenshot.** La donnée vient directement de NinjaTrader 8 via fichiers JSON.
**MBK Trader** (projet Electron, en pause — archivé dans `_archive\MBK\`) est distinct — TRADEX-AI le remplace.

---

## DÉCISIONS VERROUILLÉES — NE JAMAIS ROUVRIR

| Décision | Valeur verrouillée |
|----------|--------------------|
| Méthode | **Belkhayate exactement** — intouchable |
| Architecture exécution | **NinjaTrader 8 ATI** — TCP/IP local port 36973 |
| Mode Manuel | Signal affiché → Abdelkrim décide |
| Mode Auto | Exécution dès opportunité détectée |
| Règle d'entrée | **3/4 trading + 2/3 confirmation alignés = signal valide** |
| Architecture | **1 seul projet** : tout dans `C:\trading-copilote\` |
| Code Python du SaaS | Toujours dans `C:\trading-copilote\05-saas\` — JAMAIS à la racine |
| Modèle Claude | **claude-sonnet-4-6** (KB + signaux) |
| Modèle Vision | **claude-sonnet-4-20250514** (si screenshot TradingView) |

---

## CLASSIFICATION DES ACTIFS — 3 CATÉGORIES

### Catégorie 1 — TRADING (ordres possibles)
| Code | Actif | Bourse |
|------|-------|--------|
| GC | Or | CME |
| HG | Cuivre | CME |
| CL | Pétrole WTI | CME |
| ZW | Blé | CBOT |

### Catégorie 2 — CONFIRMATION (analyse uniquement, pas d'ordres)
| Code | Actif | Rôle |
|------|-------|------|
| DX | Dollar Index | Macro — proxy via DXY Alpha Vantage |
| ES | S&P 500 | Confirmation marchés |
| VX | VIX | Sentiment / peur |

### Catégorie 3 — RÉFÉRENCE INTER-MARCHÉ (corrélations, pas d'ordres)
| Code | Actif | Rôle |
|------|-------|------|
| MBT | Bitcoin Micro | Référence crypto inter-marché |
| 6J | Yen Japonais | Référence devise refuge |

**Règle absolue** : MBT et 6J n'apparaissent JAMAIS dans ACTIFS_TRADABLES.
Bitcoin et Yen sont **définitivement supprimés** des actifs tradables.

---

## ARCHITECTURE DU CODE

### Règle de structure unique
```
TOUT fichier .py du SaaS vit dans 05-saas\ et ses sous-dossiers. JAMAIS à la racine.
```

### Arborescence complète (à jour 15/06/2026)
```
C:\trading-copilote\
│
├── .claude\                       ← Config Claude Code (settings, etc.)
│
├── 00-pilotage\                   ← PILOTAGE : docs de gouvernance + contexte
│   ├── DETTE_TECHNIQUE.md         ← ⚠️ Bugs connus à réparer (lire avant tout dev)
│   ├── FEUILLE_DE_ROUTE.md        ← Phases du projet
│   ├── GARDE_FOUS_PROPOSES.md     ← 32 garde-fous trading
│   ├── GUIDE MAÎTRE — MÉTHODE MUSTAPHA BELKHAYATE.md
│   ├── MBK-deep-research-report.md
│   ├── MISSION_TRANSVIDEO.md
│   ├── RAPPORT_ORTOGONEX_V4_POST_AUDIT.md   ← Blueprint d'origine
│   ├── RAPPORT_trading-copilote.md
│   ├── docs\                      ← MASTER, MODULES, analyses-belkhayate (3 .md)
│   └── _context\                  ← Briefings + READMEs de transition (source d'état)
│
├── 01-moteur-transvideo\          ← MOTEUR de transcription (version vivante unique)
│   ├── transvideo_pipeline.bat
│   └── scripts\                   ← agent.py, channel_scraper.py, chunk_fuse.py,
│                                     video_filter.py, disable-sleep.ps1, restore-sleep.ps1
│
├── 02-sources-brutes\             ← Matières premières (PDF, méthode, marchés)
│   ├── kb-sources\                ← pdfs-gardes + youtube-a-scraper
│   ├── marches-trading\           ← or (et autres marchés)
│   ├── methode-belkhayate\        ← pdfs-references + principes + timing
│   └── playbook\
│
├── 03-transcriptions\             ← Sorties brutes du moteur
│   ├── nouvelles-sources\         ← Gigi Trading, Single Videos, The Trading Geek
│   └── transcripts-bruts\
│
├── 04-cerveau-trading\            ← LE CERVEAU (KB séparée du code)
│   ├── KNOWLEDGE_BASE_MASTER.json ← Base de connaissances Belkhayate (1265 règles)
│   └── processor_status.json
│
├── 05-saas\                       ← TOUT LE CODE DU SAAS ICI
│   ├── __init__.py
│   ├── config\
│   │   ├── __init__.py
│   │   └── settings.py            ← Actifs, seuils, timeouts, chemins
│   ├── engine\                    ← Moteur principal
│   │   ├── __init__.py
│   │   ├── staleness_monitor.py   ← Fraîcheur des sources de données
│   │   ├── circuit_breaker.py     ← CB_NT8 + CB_ATAS + CB_CLAUDE
│   │   ├── risk_manager.py        ← Règles risque + suspend_auto_mode
│   │   ├── data_reader.py         ← Lecture NT8 / ATAS via JSON
│   │   ├── correlations.py        ← Corrélations live 30j
│   │   └── claude_brain.py        ← Appel Claude API + prompt caching + fallback
│   ├── knowledge_base\
│   │   └── transcript_processor.py
│   ├── utils\
│   │   ├── __init__.py
│   │   └── atomic_writer.py       ← Écritures JSON atomiques
│   └── maquettes\                 ← f1.jpg → f8.jpg (maquettes interface)
│
├── 06-skills\                     ← Skills Belkhayate .md
│
├── _archive\                      ← Gelé (ne pas réutiliser comme source vivante)
│   ├── audits-prompts\
│   ├── external-methods\
│   ├── MBK\                       ← Projet MBK en pause
│   ├── old-logs\
│   ├── transcription-engine\      ← Ancien moteur (codex-transvideo-safe gelé)
│   └── _backup_transvideo_phase1_20260518_234159\
│
└── _temp\                         ← Temporaire (audio — supprimable sur confirmation)
    └── temp_audio\
```

---

## ARCHITECTURE ÉVÉNEMENTIELLE (coût Claude maîtrisé)

```
NIVEAU 1 — Python (0$) : surveiller NT8/ATAS toutes les 2 secondes
              → 3/4 actifs trading alignés ET 2/3 confirmation alignés ?
              → Non → attendre. Oui → passer niveau 2

NIVEAU 2 — Python (0$) : vérifier news gate + DD + VIX + staleness
              → Conditions KO → bloquer. OK → passer niveau 3

NIVEAU 3 — Claude API (~0.01$) : analyser via KB 1265 règles
              → Signal ACHETER / VENDRE / ATTENDRE + confiance %
              → Mode Manuel → afficher
              → Mode Auto → exécuter via NT8 ATI si confiance ≥ seuil
```

---

## STACK TECHNIQUE

```
Plateforme trading  : NinjaTrader 8 (Windows local)
Order flow          : ATAS Pro (connecté Rithmic)
Data feed           : Rithmic via broker NTB
Cerveau IA          : Claude API claude-sonnet-4-6 (Anthropic)
Backend local       : Python 3.11 + FastAPI
Dashboard           : React 18 + Vite + Tailwind 3.4 (local)
DB locale           : SQLite
Exécution ordres    : NinjaTrader 8 ATI (TCP/IP local port 36973)
OS                  : Windows 11 + PowerShell 7.6.2
Prompt caching      : cache_control: persistent sur KB (~90% économies tokens)
```

---

## 7 CERCLES D'INTELLIGENCE

| Cercle | Nom | Sources |
|--------|-----|---------|
| C1 | Prix (Belkhayate) | NT8 : BGC, Direction, Energie, Pivots |
| C2 | Order Flow | ATAS : Footprint, Delta, Big Trades |
| C3 | Institutionnels | COT (CFTC hebdo) + Open Interest |
| C4 | Macro | DX, taux Fed, événements NFP/FOMC/CPI |
| C5 | Sentiment | VIX + Put/Call ratio + Fear&Greed |
| C6 | Géopolitique | News API + calendrier événements |
| C7 | Corrélations | Matrice live 30j GC/HG/CL/ZW/ES/VX/MBT/6J |

**Score signal valide** : score ≥ 7,0/10 ET aucun critère éliminatoire ET R/R ≥ 1:2 (décision verrouillée S06 13/06/2026 — remplace l'ancien 17/21)

---

## SÉCURITÉS OBLIGATOIRES

1. **News Gate** : bloquer signaux 30min avant NFP/FOMC/CPI (timezone ET explicite)
2. **Circuit Breaker** : timeout 15s → retry 2x → fallback ATTENDRE automatique
3. **Staleness Monitor** : données > seuil → BLOCKED, pas de signal
4. **Fallback local** : confiance MAX 65%, mode Auto INTERDIT
5. **Suspension Auto** : 15-60 min après perte + VIX > seuil critique
6. **Atomic writes** : tempfile + os.replace — jamais json.dumps() direct
7. **Rate Limiting** : max 1 analyse/10s
8. **Disclaimer légal** : visible en permanence dans l'interface

---

## RÈGLES TECHNIQUES NON NÉGOCIABLES

```
CHEMINS     : toujours absolus C:\trading-copilote\
COMMITS     : Conventional Commits stricts, JAMAIS d'accents dans les messages
PYTHON      : python -m py_compile fichier.py AVANT toute exécution
API KEY     : JAMAIS dans le code → toujours os.getenv("ANTHROPIC_API_KEY")
BASE_DIR    : = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
.env        : vérifier git check-ignore .env avant tout push
LINT        : obligatoire avant tout push
ROLLBACK    : documenter avant chaque phase risquée
```

---

## ÉTAT ACTUEL (Session S14 terminée 15/06/2026)

| Élément | État |
|---------|------|
| Squelette app trading (10 agents + 9 phases) | ✅ Livré S07 — 68 tests verts, `npm run build` OK |
| Transcrits Belkhayate Whisper | ✅ 110 audités — 109 VALIDE / 1 HORS_PERIMETRE / 0 A_VERIFIER (clos S11) |
| Cohérence docs | ✅ Nettoyée S08 (/21→/10, screenshot→JSON NT8, 5/8→3/4+2/3) |
| Paramètres COG (`COGParams`) | ✅ Figés — période 180, ordre 3, coeffs 0,618/1,618 — backtest daily invalide (S11) — validation réelle = range bars NT8 Phase C |
| Énergie Belkhayate | 🔒 NON codée (stub) — attendre fin Trading Geek (conflit MFI vs proxy ATR non tranché) |
| KB (`KNOWLEDGE_BASE_MASTER.json`) | ✅ CANONIQUE — **1 265 règles** (1166 VALIDE / 45 AMBIGU / 54 INVALIDE). S14 : passe3 Sonnet +55 VALIDE récupérés. 45 AMBIGU dans A_VERIFIER_HUMAIN.md. KB à 92.2%. |
| COG backtest hostile GC/HG/ZW | ✅ Fait S11 — 180/3 non validé sur daily (timeframe ≠ range bars) — commit `e45a0fe` |
| Formules COG/Timing | ⚠️ [RECONSTRUCTION] non validées (structure jamais divulguée) |
| Mode AUTO | 🔒 BLOQUÉ par défaut (non activable : UI + API + fallback) |
| Trading Geek transcription | ⏳ ~52/113 — en cours en background |

### Dette technique restante (détails dans 00-pilotage\DETTE_TECHNIQUE.md)
```
✅ 1. Circuit breaker RÉPARÉ — import relatif .circuit_breaker (commit 75a517e)
✅ 2. Chemins KB RÉPARÉS — claude_brain.py + settings.py pointent vers 04-cerveau-trading
⏳ 3. Dossier data\ inexistant (staleness_monitor, data_reader, settings) → à créer Phase C
```

### Actifs décidés définitivement
```
TRADING     : GC (Or), HG (Cuivre), CL (Pétrole), ZW (Blé)
CONFIRMATION: DX (Dollar), ES (SP500), VX (VIX)
REFERENCE   : MBT (Bitcoin — no trade), 6J (Yen — no trade)
```

---

## PROTOCOLE FIN DE SESSION OBLIGATOIRE

```
1. Générer 00-pilotage\_context\README_TRANSITION_[date].md (résumé complet)
2. Mettre à jour la section ÉTAT ACTUEL de ce fichier (AGENTS.md)
3. Proposer le commit : git add . && git commit -m "chore: session [date] terminee"
4. Rappeler à l'utilisateur de faire git push
```

---

## PROFIL UTILISATEUR

- **Nom** : Abdelkrim
- **Niveau technique** : débutant — expliquer chaque commande comme à un élève du primaire
- **Objectif** : faire du trading un métier rentable avec la méthode Belkhayate
- **Approche** : l'IA comme copilote, l'utilisateur qui décide
- **OS** : Windows 11 — PowerShell — chemins backslash

---

## FICHIERS CLÉS — LIRE DANS CET ORDRE

| Priorité | Fichier | Contenu |
|----------|---------|---------|
| 1 | `00-pilotage\_context\README_TRANSITION_TRADEX_S14_20260615.md` | Dernier état de session |
| 2 | `00-pilotage\DETTE_TECHNIQUE.md` | Bugs à réparer (contexte indispensable) |
| 3 | `00-pilotage\FEUILLE_DE_ROUTE.md` | Phases du projet |
| 4 | `00-pilotage\GARDE_FOUS_PROPOSES.md` | 32 garde-fous trading |
| 5 | `00-pilotage\docs\MASTER_TRADEX_AI_v2.md` | Document master |
| 6 | `00-pilotage\RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | Blueprint d'origine |

---

*Ce fichier est la source de vérité absolue du projet.*
*En cas de doute entre ce fichier et une conversation : ce fichier a priorité.*
*Dernière mise à jour : 16/06/2026 (S15) — alignement S14 : Claude Code, arborescence 00→06, KB 1265 règles / 1166 VALIDE, score /10*

---

## 🔢 GUARDRAIL COMPTEUR DE MESSAGES

- Après 20 messages dans une session → générer README de transition IMMÉDIATEMENT
- Renouveler la session après le README
- README obligatoirement : précis, concis, zéro blabla, strict minimum de tokens
  → Interdit : introductions, conclusions, reformulations inutiles
  → Autorisé : état, missions, décisions, problèmes ouverts, phrase d'amorçage
