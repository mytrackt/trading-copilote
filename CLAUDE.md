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
│   ├── knowledge_base\          ← transcript_processor.py (skel) + KB JSON cible (Phase B)
│   ├── collectors\              ← Collecteurs de données (vide — Phase C)
│   ├── execution\               ← Exécution ordres NT8 ATI (vide — Phase G)
│   └── api\                     ← API FastAPI locale (vide — Phase H)
│
├── 04-kb-sources\               ← Sources KB (scraper + 142 transcripts)
│   └── youtube-a-scraper\
│       ├── whisper_pipeline.py  ← Pipeline scraping YouTube (existant)
│       └── transcripts\         ← 142 fichiers .txt à parser (Phase B)
│
├── data\                        ← Données JSON live (NT8, ATAS, etc.)
├── kb\                          ← (vide — conflit avec code\knowledge_base\, à trancher Phase B)
├── logs\                        ← Logs système
├── docs\                        ← Documentation
│   ├── MODULES.md
│   ├── MASTER_TRADEX_AI_v2.md   ← Document master (1101 lignes)
│   └── APPORTS_GUIDE_EXTERNE.md ← Apports guide externe (Phase A)
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

## ÉTAT ACTUEL (Phase A terminée 03/05/2026 — chemins corrigés Z1 09/05/2026)

| Élément | État |
|---------|------|
| CLAUDE.md | ✅ À jour — chemins corrigés Z1 (09/05/2026) |
| Phase A | ✅ Terminée et poussée (commits faf0678 → ce620dd) |
| Migration code\ | ✅ Terminée — 6 modules Python migrés depuis racine |
| code\engine\ | ✅ 6 modules : staleness_monitor, circuit_breaker, risk_manager, data_reader, correlations, claude_brain |
| code\config\settings.py | ✅ Phase A : DD jour 3 % + confiance Auto 85 % |
| code\utils\atomic_writer.py | ✅ Créé |
| code\knowledge_base\ | ⏳ transcript_processor.py (skel) — Phase B |
| code\collectors\ | ⏳ Vide — Phase C (NT8/ATAS/news/COT) |
| code\execution\ | ⏳ Vide — Phase G (NT8 ATI port 36973) |
| code\api\ | ⏳ Vide — Phase H (FastAPI + dashboard) |
| docs\MASTER_TRADEX_AI_v2.md | ✅ 1101 lignes (sections 1/10/11/12 corrigées) |
| GARDE_FOUS_PROPOSES.md | ✅ 32 garde-fous (20 actifs / 10 manquants / 2 partiels) |
| FEUILLE_DE_ROUTE.md | ✅ 11 phases A→K |
| CHECKLIST_FICHIERS_INUTILES.md | ✅ 29 items (~402 MB récupérables) — exécution Phase Y |
| RAPPORT_REORGANISATION.md | ✅ Plan 6 groupes G1→G6 — exécution Phase Y |
| .gitignore Python | ✅ Configuré (pycache, .env, IDE, BACKUP_*, PDF source) |
| KB Belkhayate | ⏳ 142 transcripts à parser (Phase B, 2-3 sessions) |
| Mode AUTO | 🔒 BLOQUÉ par défaut (5/6 conditions non remplies) |

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
├── config\         ✅ settings.py (DD 3% + confiance 85% — Phase A)
├── knowledge_base\ ⏳ transcript_processor.py (skel — Phase B)
├── collectors\     ⏳ vide (Phase C)
├── execution\      ⏳ vide (Phase G)
└── api\            ⏳ vide (Phase H)
```

### Commits Phase A (03/05/2026)
```
faf0678  docs: APPORTS_GUIDE_EXTERNE - segments retenus du guide externe
6e24070  chore: phase 0 backup - gitignore settings.local.json + pdf source externe
9f31edd  S02-docs - Garde-fous proposes + feuille de route
95c2e8f  docs: briefing fin de phase A
2fd06ba  docs: checklist fichiers inutiles + rapport reorganisation
4edaccf  docs: briefing fin de session 2026-05-03
ce620dd  chore(claude): add message counter guardrail to CLAUDE.md
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
| 1 | `_context/briefing-2026-05-03-fin-session.md` | État global fin Phase A |
| 2 | `_context/CONTEXT_TRADEX_v1.md` | Context projet v1 (post-S01) |
| 3 | `FEUILLE_DE_ROUTE.md` | 11 phases A→K |
| 4 | `GARDE_FOUS_PROPOSES.md` | 32 garde-fous (20 actifs / 10 manquants / 2 partiels) |
| 5 | `RAPPORT_REORGANISATION.md` | Plan réorg 6 groupes (Phase Y) |
| 6 | `docs/MASTER_TRADEX_AI_v2.md` | Document master |
| 7 | `RAPPORT_ORTOGONEX_V4_POST_AUDIT.md` | Blueprint d'origine |

---

*Ce fichier est la source de vérité absolue du projet.*
*En cas de doute entre ce fichier et une conversation : ce fichier a priorité.*
*Dernière mise à jour : 09/05/2026 — Z1 chemins corrigés + Phase A reflétée*

---

## 🔢 GUARDRAIL COMPTEUR DE MESSAGES

- Après 20 messages dans une session → générer README de transition IMMÉDIATEMENT
- Renouveler la session après le README
- README obligatoirement : précis, concis, zéro blabla, strict minimum de tokens
  → Interdit : introductions, conclusions, reformulations inutiles
  → Autorisé : état, missions, décisions, problèmes ouverts, phrase d'amorçage
