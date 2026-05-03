# FEUILLE DE ROUTE — TradEx AI

> Document de proposition uniquement — **aucun code créé** dans ce document.
> Source : `docs/MASTER_TRADEX_AI_v2.md` (Sections 1-12, calendrier SEMAINES 1-10)
> + `docs/APPORTS_GUIDE_EXTERNE.md` + corpus `01-methode-belkhayate/`
> + `GARDE_FOUS_PROPOSES.md` (32 garde-fous cibles).
>
> **Date** : 2026-05-03 — Phase 5 v4.0 (roadmap fusionnée).
> **Règle** : chaque phase est validée par toi avant de passer à la suivante.

---

## 🗺️ VISION GLOBALE

11 phases séquentielles (A → K) qui transforment l'existant (code engine + docs) en SaaS desktop opérationnel TradEx AI :

```
[A] Documentation & garde-fous              ← EN COURS (cette session)
        ↓
[B] KB Belkhayate (2337 règles JSON)        ← extraction transcripts
        ↓
[C] Collecteurs de données (5 modules)      ← NT8 / ATAS / news / COT / macro
        ↓
[D] Moteur Belkhayate Python                ← BGC + Direction + Énergie + Pivots
        ↓
[E] Signal Scorer + Régime + Walk-Forward   ← score 7 cercles + backtest
        ↓
[F] Trade Validator + Risk extensions       ← G1-G6 garde-fous bloquants
        ↓
[G] Client NT8 ATI port 36973 + Killswitch  ← exécution ordres + G8
        ↓
[H] FastAPI locale + Health monitoring      ← API REST + G10
        ↓
[I] Dashboard React 18 + 3 thèmes           ← UI + bouton 🛑 STOP ALL
        ↓
[J] Paper Trading 30 jours obligatoire      ← validation conditions Mode Auto
        ↓
[K] Activation Mode AUTO (conditionnel)     ← 6 conditions satisfaites + bouton
```

---

## ÉTAT ACTUEL (au 2026-05-03)

| Item | État | Source |
|------|------|--------|
| CLAUDE.md projet (décisions verrouillées) | ✅ | `CLAUDE.md` |
| Stack gelée (React 18 + FastAPI + SQLite + NT8 ATI + Rithmic) | ✅ | `CLAUDE.md` |
| Actifs verrouillés (GC/HG/CL/ZW + DX/ES/VX + MBT/6J réf) | ✅ | `settings.py:15-46` |
| `code/engine/` (6 modules : staleness, CB, risk, data_reader, correlations, claude_brain) | ✅ | — |
| `code/utils/atomic_writer.py` | ✅ | — |
| `code/config/settings.py` (actifs + seuils + paths + DD jour 3 % + Confiance Auto 85 %) | ✅ | corrections cette session |
| `docs/MASTER_TRADEX_AI_v2.md` (1101 lignes) | ✅ | mission 9-12 commitées |
| `docs/APPORTS_GUIDE_EXTERNE.md` (616 lignes) | ✅ | commit `faf0678` |
| `GARDE_FOUS_PROPOSES.md` (20 actifs + 10 à faire + 2 partiels) | ✅ | cette session |
| 152 transcripts `.txt` Belkhayate | ✅ | `code/transcripts/` |
| 46 PDF méthode + 37 .md docs | ✅ | corpus complet |
| KB Belkhayate JSON (2337 règles) | ❌ | `code/knowledge_base/` vide |
| Collecteurs (NT8, ATAS, news, COT, macro) | ❌ | `code/collectors/` vide |
| Client exécution NT8 ATI | ❌ | `code/execution/` vide |
| FastAPI locale | ❌ | `code/api/` vide |
| Dashboard React | ❌ | `code/frontend/` n'existe pas |
| Paper Trading 30 jours | ❌ | non commencé |
| Mode AUTO | 🔒 | BLOQUÉ par défaut (5/6 conditions non remplies) |

---

## PHASE A — Documentation & garde-fous (EN COURS)

**Objectif** : aligner l'utilisateur et l'IA sur tous les garde-fous + la roadmap **avant tout code futur**.

| Livrable | État |
|----------|------|
| `docs/APPORTS_GUIDE_EXTERNE.md` | ✅ commité `faf0678` |
| `GARDE_FOUS_PROPOSES.md` (32 garde-fous) | ✅ cette session |
| `FEUILLE_DE_ROUTE.md` (ce document) | ⏳ en cours |
| Commit final S02-docs | ⏳ tâche 5 |

**Critère de validation** : tu valides ce document.

**Garde-fous implémentés en Phase A** : aucun (documentation pure).

→ ⏸️ **Validation requise** : "OK FEUILLE_DE_ROUTE ✅"

---

## PHASE B — KB Belkhayate (2337 règles)

**Objectif** : extraire les règles Belkhayate depuis les 152 transcripts `.txt` vers `KNOWLEDGE_BASE_MASTER.json`, format consommable par `claude_brain.py:171` (`load_kb_rules`).

**Prérequis** : Phase A validée + transcripts présents ✅.

**Livrables** :
- Script `code/scraper/extract_rules.py` (parser règles depuis .txt structurés)
- `code/knowledge_base/KNOWLEDGE_BASE_MASTER.json` (~2337 règles structurées par catégorie)
- Validation manuelle : échantillon 50 règles aléatoires relues par Abdelkrim

**Critère de validation** : `claude_brain.load_kb_rules()` charge le JSON sans erreur ; le system prompt généré tient en < 50k tokens (caching efficient).

**Garde-fous implémentés en Phase B** : aucun.

**Estimation effort** : 2-3 sessions Claude Code.

---

## PHASE C — Collecteurs de données (5 modules)

**Objectif** : alimenter en continu les 7 cercles (Sections 3 master file).

**Prérequis** : Phase B + NinjaTrader 8 + ATAS configurés sur poste Windows.

**Livrables (5 modules dans `code/collectors/`)** :

| Module | Cercle | Source | Sortie |
|--------|--------|--------|--------|
| `nt8_collector.py` | C1 Prix | JSON exporté par NT8 ATI | `data/nt8_data.json` |
| `atas_collector.py` | C2 Order Flow | JSON exporté par ATAS Pro | `data/atas_data.json` |
| `cot_collector.py` | C3 Institutionnels | CFTC API hebdo | `data/cot_data.json` |
| `macro_collector.py` | C4 Macro + C7 régime | FRED + EIA + Alpha Vantage + **OPEC calendar (G9)** | `data/macro_data.json` |
| `news_collector.py` | C5 Sentiment + C6 Géopolitique | Finnhub WebSocket + GDELT + GetXAPI | `data/news_data.json` |

**Critère de validation** : chaque collecteur écrit son JSON avec timestamp respectant les seuils `STALENESS` (`settings.py:105-109`).

**Garde-fous implémentés en Phase C** :
- ✅ G9 — Calendrier OPEC programmé (dans `macro_collector.py`)
- ✅ Atomic writes (déjà actif via `atomic_writer.py`)

**Estimation effort** : 4-5 sessions Claude Code.

---

## PHASE D — Moteur Belkhayate Python

**Objectif** : recalculer les indicateurs Belkhayate en Python pour validation indépendante de NT8 (Section 5 master file SEMAINE 5).

**Prérequis** : Phase B (KB règles) + Phase C (`nt8_collector` opérationnel).

**Livrables (`code/engine/belkhayate.py`)** :
- Calcul **BGC** (Belkhayate Gravity Center) avec ratio 0.618 sur GC/HG/CL/ZW
- Calcul **Direction**, **Énergie**, **Pivots**
- Validation comparative Python vs indicateurs NT8 sur 50 bougies (écart attendu < 1 %)
- Condition d'**invalidation setup** (BGC franchi à contre-sens, énergie inversée, pivot stratégique cassé) → signal sortie immédiat

**Critère de validation** : comparaison Python vs NT8 sur GC + HG + CL + ZW (50 bougies par actif) → écart moyen < 1 %.

**Garde-fous implémentés en Phase D** :
- ✅ P1 — Invalidation setup Belkhayate

**Estimation effort** : 3 sessions Claude Code (méthode complexe + validation rigoureuse).

---

## PHASE E — Signal Scorer + Détection régime + Walk-Forward

**Objectif** : moteur de scoring 7 cercles + classification régime + backtesting rigoureux.

**Prérequis** : Phases C + D.

**Livrables (2 modules nouveaux)** :

### `code/engine/signal_scorer.py`
- `score_7_cercles(context)` → 0-21 pts (Section 4 master file)
- `HysteresisFilter` (3 barres consécutives — APPORTS section 2)
- `CoolDownGuard` (48 h post-sortie — APPORTS section 2)
- `AntiNoiseFilter` (anti-flip-flop max 2/h — APPORTS section 6)
- `walk_forward_validate(252j entraînement / 126j test)` (APPORTS section 1)
- `monte_carlo_stress(n=10000)` → worst 5 % drawdown (APPORTS section 1)

### Extension `code/engine/correlations.py`
- `detect_correlation_break(20j vs 60j)` (APPORTS section 3)
- `detect_market_regime()` → BULL / NEUTRAL / BEAR / CRASH

**Critère de validation** :
- Backtest ≥ 3 mois données historiques (condition Mode Auto #1)
- Win rate ≥ 55 % (condition Mode Auto #2)
- Plateau stable ±2 jours look-back (sinon overfitting)

**Garde-fous implémentés en Phase E** :
- ✅ G7 — Détection régime marché (BULL/NEUTRAL/BEAR/CRASH)
- ✅ Hysteresis + Cool-down + Anti-flip-flop (filtres anti-bruit)

**Estimation effort** : 3-4 sessions Claude Code.

---

## PHASE F — Trade Validator + Risk Engine extensions

**Objectif** : couche de validation pré-ordre qui peut REJETER tout ordre non conforme.

**Prérequis** : Phase E (signal scoré et régime connu).

**Livrables (1 module nouveau + extensions)** :

### `code/engine/trade_validator.py` (nouveau)
- `check_stop_loss_obligatoire()` → G1
- `check_anti_doublon(uuid, window=60s)` → G3
- `check_dead_zone(actif, now)` → G4
- `check_rollover(actif, now)` → G5
- `validate_order(signal)` → orchestre toutes les vérifs, retourne (OK, raison)

### Extensions `code/engine/risk_manager.py`
- `LEVIER_PAR_REGIME` dict (G7)
- `adjust_position_size(base, confiance, regime, dd_today)` → applique levier + score confiance
- `check_drawdown_breakers(dd_today, dd_week, dd_total)` → palier MANDATORY_LOCK à 10 %
- `write_mandatory_lock(reason)` → crée `data/TRADING_LOCKED.lock`
- `is_trading_locked()` → bool — appelé par tout module avant envoi ordre

### Extensions `code/config/settings.py`
- `SLIPPAGE_BUFFER_TICKS` (G2)
- `DEAD_ZONE` (G4)
- `ROLLOVER_BLOCK_HOURS` (G5)
- `OPEC_BLACKOUT_MINUTES` (G9)
- `ORDER_RULES` (G1, G3)
- `PALIERS_DD_TOTAL`, `LOCK_FILE_PATH` (G6)

**Critère de validation** : tests unitaires `pytest` couverture 100 % sur `trade_validator.py`.

**Garde-fous implémentés en Phase F** :
- ✅ G1, G2, G3, G4, G5, G6 (6 garde-fous bloquants — sécurité maximale)

**Estimation effort** : 2-3 sessions Claude Code.

---

## PHASE G — Client NT8 ATI port 36973 + Killswitch Internet

**Objectif** : exécution réelle des ordres via NinjaTrader 8 ATI + protection déconnexion.

**Prérequis** : Phase F (trade_validator opérationnel) + NT8 ATI activé sur poste.

**Livrables (3 modules dans `code/execution/` + 1 dans `code/engine/`)** :
- `code/execution/nt8_ati_client.py` (TCP/IP `127.0.0.1:36973`, timeout 5 s)
- `code/execution/order_manager.py` (envoi ordre conditionné par `trade_validator.validate_order()`)
- `code/engine/network_monitor.py` (ping `8.8.8.8` toutes les 5 s, déclenche GTC close all si 3 échecs consécutifs)

**Critère de validation** : 48 h de test simulation sur compte demo Rithmic NTB sans erreur (condition Mode Auto #4).

**Garde-fous implémentés en Phase G** :
- ✅ G8 — Killswitch Internet

**Estimation effort** : 3-4 sessions Claude Code.

---

## PHASE H — FastAPI locale + Health monitoring

**Objectif** : exposer une API REST locale pour le dashboard React.

**Prérequis** : Phases C + E + F + G (toute la chaîne backend opérationnelle).

**Livrables (`code/api/`)** :
- `main.py` (uvicorn entrypoint, FastAPI app)
- `routes/signals.py` (`GET /signals` → signaux temps réel)
- `routes/modes.py` (`POST /modes/{manuel|auto}` — bascule, conditionné par `is_trading_locked()`)
- `routes/risk.py` (`GET /risk` → état actuel DD + circuit breakers + lock file)
- `health.py` (`GET /healthz` → status backend pour dashboard)

**Critère de validation** : ping `/healthz` toutes les 5 s pendant 24 h sans interruption.

**Garde-fous implémentés en Phase H** :
- ✅ G10 — Monitoring santé FastAPI

**Estimation effort** : 2 sessions Claude Code.

---

## PHASE I — Dashboard React 18

**Objectif** : interface visuelle pour Mode Manuel (Section 6 master file + Phase 6+7 prompt v4.0).

**Prérequis** : Phase H (API disponible) + choix thème par Abdelkrim parmi 3 propositions extraites de `design-themes.md`.

**Sous-étapes** :

### I.1 — Bootstrap projet React (1 session)
- `npm create vite@latest` dans `code/frontend/`
- React 18 + Vite + Tailwind 3.4 (stack gelée CLAUDE.md)
- ESLint + Prettier + TypeScript

### I.2 — Choix thème (3 propositions, 1 session)
Shortlist depuis `design-themes.md` (18 thèmes, fichier 15 KB) :
- **Thème 7** — SaaS Dark Analytics (`#3B82F6` + dark)
- **Thème 9** — DIFAI Style (`#1E3A8A` + or `#D4A017`)
- **Thème 11** — Smart Home Minimal (gris + or chaud)

### I.3 — Composants (2 sessions)
Ordre de création (Phase 7.2 prompt v4.0) :
1. `RiskGuard` (wrappeur bloquant — affiche `is_trading_locked()`)
2. `ModeExecution` (toggle MANUEL/AUTO + 6 conditions visibles si BLOQUÉ)
3. `KPIBar` (P&L / Win Rate / Risk %)
4. `StrategiesPanel` (3 stratégies IA : Type / TF / Confiance / Entrée / SL / TP / RR / Belkhayate / Invalidation)
5. `BelkhayateLevels` (BGC + Pivots + Direction + Énergie temps réel)
6. `VolumeOI` (Volume CME ⚠️ ≠ tick volume + Open Interest)
7. `IntermarketPanel` (DXY + TLT + VIX + COT + News countdown)
8. `DisciplineLog` (pertes consécutives + pause forcée + journal)
9. `Dashboard` principal (assemblage + 🛑 STOP ALL toujours visible + disclaimer AMMC permanent)

**Critère de validation** : les 9 KPI obligatoires (master file Section 6 + prompt v4.0 Phase 7) sont affichés temps réel sans erreur sur 1 h continue.

**Garde-fous implémentés en Phase I** : aucun nouveau code backend, **intègre G7 + G10 visuels** + bouton 🛑 STOP ALL réactif < 2 s + disclaimer AMMC.

**Estimation effort** : 4-5 sessions Claude Code.

---

## PHASE J — Paper Trading 30 jours obligatoire

**Objectif** : valider l'ensemble du système en conditions réelles **sans risque capital**.

**Prérequis** : Phases A → I terminées + compte demo Rithmic NTB opérationnel.

**Protocole** :
- 30 jours calendaires consécutifs
- Mode MANUEL uniquement
- Log session quotidien (JSON + .md)
- Métriques suivies : win rate, drawdown jour/semaine/total, latence ordre, déconnexions NT8/ATAS, faux signaux

**Critères de validation** :
- 0 déconnexion NT8/ATAS > 60 s pendant 24 h continues (condition Mode Auto #5)
- Win rate ≥ 55 % sur 30 jours (condition Mode Auto #2)
- Drawdown total < 5 %
- Aucun ordre rejeté par `trade_validator` non justifié

**Garde-fous testés en Phase J** : **TOUS** (test global du système).

**Estimation effort** : 30 jours réels (passifs).

---

## PHASE K — Activation Mode AUTO (conditionnel)

**Objectif** : déverrouiller le Mode AUTO uniquement si les **6 conditions** sont satisfaites.

**Mapping conditions Mode Auto ↔ phases** :

| # | Condition | Phase qui la satisfait |
|---|-----------|------------------------|
| 1 | Backtest validé ≥ 3 mois | Phase E |
| 2 | Win rate backtest ≥ 55 % | Phase E + Phase J |
| 3 | Risk Engine validé | Phase F |
| 4 | Broker Rithmic/NTB testé 48 h sans erreur | Phase G + Phase J |
| 5 | NinjaTrader 8 ATI stable 24 h | Phase G + Phase J |
| 6 | Validation explicite trader (bouton + log daté) | Phase I + ce déverrouillage |

**Livrable Phase K** :
- Bouton "J'ACTIVE LE MODE AUTO" dans dashboard (composant `ModeExecution`)
- Confirmation modal avec mot de passe + horodatage signé dans journal
- Activation effective — drapeau persisté dans SQLite

**Critère de validation** : utilisateur Abdelkrim valide explicitement avec mot de passe ; entrée journal datée signée.

**Garde-fous implémentés en Phase K** : aucun nouveau, **active** tous les garde-fous Mode AUTO codés en Phase F (G1-G8) + monitoring G10 + STOP ALL réactif G8.

---

## 📊 SYNTHÈSE EFFORT ESTIMÉ

| Phase | Sessions Claude Code estimées | Durée calendaire min |
|-------|-------------------------------|----------------------|
| A — Documentation | 1 (cette session) | 1 jour |
| B — KB Belkhayate | 2-3 | 1 semaine |
| C — Collecteurs (5 modules) | 4-5 | 2 semaines |
| D — Moteur Belkhayate Python | 3 | 1-2 semaines |
| E — Signal Scorer + Régime + Walk-Forward | 3-4 | 2 semaines |
| F — Trade Validator + Risk extensions | 2-3 | 1 semaine |
| G — Client NT8 ATI + Killswitch | 3-4 | 1-2 semaines |
| H — FastAPI + Health | 2 | 1 semaine |
| I — Dashboard React 18 | 4-5 (3 sous-étapes) | 2-3 semaines |
| J — Paper Trading 30 jours | 0 (monitoring passif) | **30 jours** |
| K — Activation Mode AUTO | 1 | 1 jour |
| **Total avant Mode AUTO** | **~25-30 sessions** | **~3-4 mois** |

---

## ⚠️ RÈGLES NON NÉGOCIABLES (rappel)

1. **Mode AUTO BLOQUÉ par défaut** jusqu'à Phase K validée par les 6 conditions.
2. **Chaque phase est validée par Abdelkrim** avant la suivante.
3. **Aucune décision verrouillée CLAUDE.md ne peut être rouverte** (stack, actifs, broker, méthode Belkhayate).
4. **Méthode Belkhayate prioritaire** sur tout concept extérieur (APPORTS_GUIDE_EXTERNE = filtres complémentaires).
5. **PROMPT-GATE-AUDIT v3.1 obligatoire** avant tout livrable > 20 lignes (CLAUDE.md global).
6. **Disclaimer AMMC + données SQLite locales (CNDP)** présents en permanence.

---

## 📌 PROCHAINE ÉTAPE IMMÉDIATE

Tâche 5 du prompt actuel :
1. Ajouter `PROMPT_TRADEX_AI_CLAUDE_CODE_v4.md` à `.gitignore`
2. `git add .` puis `git commit -m "S02-docs - Garde-fous proposes + feuille de route (documents uniquement)"`

Une fois commité, **Phase A est terminée**. Phase B (KB Belkhayate) peut commencer la prochaine session si tu valides.

---

*Phase 5 v4.0 — `FEUILLE_DE_ROUTE.md` généré le 2026-05-03.*
