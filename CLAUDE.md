# TRADING-COPILOTE — Instructions Claude Code
> Lis ce fichier EN ENTIER avant toute action. Aucune exception.

---

## RÈGLE 0 — PROTOCOLE DE DÉMARRAGE OBLIGATOIRE

Chaque nouvelle session suit cet ordre exact :

1. Lire ce fichier (CLAUDE.md) — déjà fait
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
**MBK Trader** (projet Electron, 60% fait, en pause) est distinct — TRADEX-AI le remplace.

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
| Code Python | Toujours dans `C:\trading-copilote\code\` — JAMAIS à la racine |
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
TOUT fichier .py vit dans code\ et ses sous-dossiers. JAMAIS à la racine.
```

### Arborescence complète
```
C:\trading-copilote\
│
├── code\                        ← TOUT LE CODE ICI
│   ├── engine\                  ← Moteur principal
│   │   ├── staleness_monitor.py ← Fraîcheur 15 sources de données
│   │   ├── circuit_breaker.py   ← CB_NT8 + CB_ATAS + CB_CLAUDE
│   │   ├── risk_manager.py      ← Règles risque + suspend_auto_mode
│   │   ├── data_reader.py       ← Lecture NT8 / ATAS via JSON
│   │   ├── correlations.py      ← Corrélations live 30j (GC/HG/CL/ZW/ES/VX)
│   │   ├── claude_brain.py      ← Appel Claude API + prompt caching + fallback
│   │   └── signal_scorer.py     ← Score 7 cercles (à créer)
│   │
│   ├── utils\                   ← Utilitaires
│   │   └── atomic_writer.py     ← Écritures JSON atomiques
│   │
│   ├── config\                  ← Configuration
│   │   └── settings.py          ← Actifs, seuils, timeouts, chemins
│   │
│   ├── collectors\              ← Collecteurs de données
│   │   └── (à créer)
│   │
│   ├── execution\               ← Exécution ordres NT8 ATI
│   │   └── (à créer)
│   │
│   ├── api\                     ← API FastAPI locale
│   │   └── (à créer)
│   │
│   ├── scraper\                 ← Scraping YouTube (KB phase)
│   ├── transcripts\             ← Fichiers .txt vidéos
│   └── knowledge_base\          ← KNOWLEDGE_BASE_MASTER.json
│
├── data\                        ← Données JSON live (NT8, ATAS, etc.)
├── kb\                          ← Knowledge Base Belkhayate (2337 règles)
├── logs\                        ← Logs système
├── docs\                        ← Documentation
│   ├── MODULES.md
│   ├── MASTER_TRADEX_AI_v2.md   ← Document master (à créer mission 9)
│   └── (docs SaaS-workspace copiés)
├── 05-skills\                   ← 10 skills Belkhayate .md générés
└── _context\                    ← Briefings de session
```

---

## ARCHITECTURE ÉVÉNEMENTIELLE (coût Claude maîtrisé)

```
NIVEAU 1 — Python (0$) : surveiller NT8/ATAS toutes les 2 secondes
              → 3/4 actifs trading alignés ET 2/3 confirmation alignés ?
              → Non → attendre. Oui → passer niveau 2

NIVEAU 2 — Python (0$) : vérifier news gate + DD + VIX + staleness
              → Conditions KO → bloquer. OK → passer niveau 3

NIVEAU 3 — Claude API (~0.01$) : analyser via KB 2337 règles
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
OS                  : Windows 11 + PowerShell
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

## ÉTAT ACTUEL (mis à jour le 02/05/2026 — fin de session Claude Code)

| Élément | État |
|---------|------|
| CLAUDE.md | ✅ À jour — vision TRADEX-AI verrouillée |
| Migration code\ | ✅ Terminée — 6 modules Python migrés depuis racine |
| Mission 7 — claude_brain.py | ✅ Créé dans code\engine\ |
| Mission 8 — settings.py | ✅ Créé dans code\config\ |
| Mission 9 — MASTER_TRADEX_AI_v2.md | ✅ Créé dans docs\ (1101 lignes) |
| Mission 10 — Section 1 Budget | ✅ Corrigée (3 catégories + claude-sonnet-4-6) |
| Mission 11 — Sections 10/11/12 | ✅ Réécrites (Mode Manuel/Auto + Risque + Checklist) |
| Mission 12 — Cercles 6 et 7 | ✅ Corrigés (CORRELATION_PAIRS + detect_regime + GEOPOLITIQUE_IMPACT) |
| .gitignore Python | ✅ Configuré (pycache, .env, IDE) |
| KB Belkhayate | ⏳ 2337 règles à extraire des transcripts |
| code\collectors\ | ⏳ Vide — à créer (collecteurs NT8/ATAS/news/COT) |
| code\execution\ | ⏳ Vide — à créer (interface NT8 ATI port 36973) |
| code\api\ | ⏳ Vide — à créer (FastAPI locale + dashboard) |

### Actifs décidés définitivement
```
TRADING     : GC (Or), HG (Cuivre), CL (Pétrole), ZW (Blé)
CONFIRMATION: DX (Dollar), ES (SP500), VX (VIX)
REFERENCE   : MBT (Bitcoin — no trade), 6J (Yen — no trade)
```

### Structure code\ actuelle
```
code\
├── engine\         ✅ staleness_monitor, circuit_breaker, risk_manager,
│                      data_reader, correlations, claude_brain
├── utils\          ✅ atomic_writer.py
├── config\         ✅ settings.py
├── collectors\     ⏳ vide
├── execution\      ⏳ vide
├── api\            ⏳ vide
├── scraper\        (KB phase)
├── transcripts\    (.txt vidéos)
└── knowledge_base\ (KNOWLEDGE_BASE_MASTER.json)
```

### Commits de la session
```
a1e5205  refactor: migrate python modules from root to code/ directory
6e12b5c  docs: master TRADEX-AI v2 - missions 9-12 (budget, modes, risque, checklist, correlations)
```

---

## PROTOCOLE FIN DE SESSION OBLIGATOIRE

```
1. Générer _context/briefing-[YYYY-MM-DD].md (résumé complet)
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
- **OS** : Windows 11 — PowerShell — chemins backslash

---

## FICHIERS CLÉS — LIRE DANS CET ORDRE

| Priorité | Fichier | Contenu |
|----------|---------|---------|
| 1 | `_context/[le plus récent]` | État exact de la session précédente |
| 2 | `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | Blueprint complet TRADEX-AI |
| 3 | `docs/MASTER_TRADEX_AI_v2.md` | Document master corrigé (après mission 9) |
| 4 | `PROMPT_1_SCRAPING_YOUTUBE_SKILLS.md` | Spec KB + 10 skills |

---

*Ce fichier est la source de vérité absolue du projet.*
*En cas de doute entre ce fichier et une conversation : ce fichier a priorité.*
*Dernière mise à jour : 02/05/2026 — Abdelkrim*

---

## 🔢 GUARDRAIL COMPTEUR DE MESSAGES

- Après 20 messages dans une session → générer README de transition IMMÉDIATEMENT
- Renouveler la session après le README
- README obligatoirement : précis, concis, zéro blabla, strict minimum de tokens
  → Interdit : introductions, conclusions, reformulations inutiles
  → Autorisé : état, missions, décisions, problèmes ouverts, phrase d'amorçage
