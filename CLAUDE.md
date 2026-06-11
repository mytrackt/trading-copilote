# TRADING-COPILOTE — Instructions Claude Code
> Lis ce fichier EN ENTIER avant toute action. Aucune exception.

---

## RÈGLE 0 — PROTOCOLE DE DÉMARRAGE OBLIGATOIRE

Chaque nouvelle session suit cet ordre exact :

1. Lire ce fichier (CLAUDE.md) — déjà fait
2. Lire le fichier le plus récent dans `00-pilotage\_context\` (date la plus récente)
3. Annoncer exactement : "📍 État : [résumé 1 ligne] — Prochaine action : [action]"
4. Attendre confirmation de l'utilisateur avant toute exécution

Ne jamais sauter une étape. Ne jamais supposer l'état du projet sans lire `00-pilotage\_context\`.

---

## PROJET EN UNE LIGNE

Construire **TRADEX-AI** : un système de trading temps réel basé sur la méthode Belkhayate,
connecté à NinjaTrader 8, avec mode Manuel (Abdelkrim décide) et mode Auto (exécution automatique).
Le moteur **TRANSVIDEO** (transcription YouTube → règles de trading) alimente le cerveau du SaaS.

---

## VISION SYSTÈME

```
NinjaTrader 8 (données live) → Python Engine (surveillance 2s) → Claude API (signal)
                                        ↓
                          Mode Manuel : afficher signal → Abdelkrim décide
                          Mode Auto   : exécuter ordre via NT8 ATI (port 36973)
```

**Ce n'est PAS un système screenshot.** La donnée vient directement de NinjaTrader 8 via fichiers JSON.
**MBK Trader** (projet Electron, en pause) est archivé dans `_archive\MBK\` — TRADEX-AI le remplace.

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
| Objectif moteur | **Fidélité des règles de trading** (transcript-first), PAS le WER mot-à-mot. Usage personnel. |

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

## ARCHITECTURE DU PROJET (STRUCTURE RÉELLE 00→06)

### Règle de structure unique
```
TOUT fichier .py du SaaS vit dans 05-saas\ et ses sous-dossiers. JAMAIS à la racine.
```

### Arborescence complète (à jour 11/06/2026)
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
│   ├── RAPPORT_codex-transvideo.md
│   ├── RAPPORT_COMPARAISON_TRADEX.md
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
│   ├── KNOWLEDGE_BASE_MASTER.json ← Base de connaissances Belkhayate (~2337 règles)
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
└── _temp\                         ← Temporaire (audio 121 Mo — supprimable sur confirmation)
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

NIVEAU 3 — Claude API (~0.01$) : analyser via KB (~2337 règles)
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

**Score signal valide** : minimum 17/21 points (7 cercles × max 3 pts chacun)

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

## ÉTAT ACTUEL (Réorganisation pro terminée 11/06/2026)

| Élément | État |
|---------|------|
| Réorganisation pro 00→06 | ✅ Terminée — commit `960fe88` poussé sur GitHub |
| CLAUDE.md | ✅ À jour — reflète la structure 00→06 (11/06/2026) |
| Moteur TRANSVIDEO | ✅ Consolidé en une seule version vivante (`01-moteur-transvideo\scripts\`) |
| Cerveau trading (KB) | ✅ Séparé du code (`04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json`) |
| Code SaaS | ✅ Migré dans `05-saas\` (config, engine, knowledge_base, utils, maquettes) |
| Dette technique | ⚠️ Documentée mais NON réparée → `00-pilotage\DETTE_TECHNIQUE.md` |
| Fiabilité moteur | ⏳ NON validée (objectif > 90/95 % non prouvé, dernier test = success_partial) |
| Instructions projet Cowork | ⏳ À vérifier — peuvent encore référencer l'ancienne structure |
| Mode AUTO | 🔒 BLOQUÉ par défaut |

### ⚠️ DETTE TECHNIQUE CONNUE (détails dans 00-pilotage\DETTE_TECHNIQUE.md)
```
1. Circuit breaker inactif en silence : claude_brain.py importe l'ancien
   paquet `code.engine.circuit_breaker` → garde-fou de sécurité KO. CRITIQUE.
2. Chemins doublés `code\code\` (claude_brain, settings) → modules pas en service.
3. Dossier `data\` référencé mais inexistant (staleness_monitor, data_reader, settings).
   → À réparer AVANT de lancer le SaaS, pas urgent tant que modules hors service.
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
2. Mettre à jour la section ÉTAT ACTUEL de ce fichier (CLAUDE.md)
3. Proposer le commit : git add . && git commit -m "chore: session [date] terminee"
4. Rappeler à l'utilisateur de faire git push
```

---

## PROFIL UTILISATEUR

- **Nom** : Abdelkrim
- **Niveau technique** : débutant — expliquer chaque commande comme à un élève du primaire
- **Objectif** : faire du trading un métier rentable avec la méthode Belkhayate
- **Approche** : l'IA comme copilote, l'utilisateur qui décide
- **OS** : Windows 11 — PowerShell 7.6.2 — chemins backslash

---

## FICHIERS CLÉS — LIRE DANS CET ORDRE

| Priorité | Fichier | Contenu |
|----------|---------|---------|
| 1 | `00-pilotage\_context\README_TRANSITION_TRADEX_S02_20260511.md` | Dernier état de session |
| 2 | `00-pilotage\DETTE_TECHNIQUE.md` | Bugs à réparer (contexte indispensable) |
| 3 | `00-pilotage\FEUILLE_DE_ROUTE.md` | Phases du projet |
| 4 | `00-pilotage\GARDE_FOUS_PROPOSES.md` | 32 garde-fous trading |
| 5 | `00-pilotage\docs\MASTER_TRADEX_AI_v2.md` | Document master |
| 6 | `00-pilotage\RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | Blueprint d'origine |

---

*Ce fichier est la source de vérité absolue du projet.*
*En cas de doute entre ce fichier et une conversation : ce fichier a priorité.*
*Dernière mise à jour : 11/06/2026 — Structure 00→06 reflétée + dette technique documentée*

---

## 🔢 GUARDRAIL COMPTEUR DE MESSAGES

- Après 20 messages dans une session → générer README de transition IMMÉDIATEMENT
- Renouveler la session après le README
- README obligatoirement : précis, concis, zéro blabla, strict minimum de tokens
  → Interdit : introductions, conclusions, reformulations inutiles
  → Autorisé : état, missions, décisions, problèmes ouverts, phrase d'amorçage
