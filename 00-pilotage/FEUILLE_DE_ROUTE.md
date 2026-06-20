# FEUILLE DE ROUTE — TradEx AI

> Source de vérité : `CLAUDE.md` (décisions verrouillées) + `00-pilotage\docs\MASTER_TRADEX_AI_v2.md`
> Documents KB : `STRATEGIE_KB_MASTER.md` + `RAPPORT_SOURCES_KB_2026.md`
>
> **Dernière mise à jour** : 2026-06-12 — Phase B révisée (KB rebuild depuis sources primaires).
> **Règle** : chaque phase est validée par Abdelkrim avant de passer à la suivante.

---

## 🗺️ VISION GLOBALE

12 phases séquentielles (A → L) :

```
[A] Documentation & garde-fous              ✅ TERMINÉE
        ↓
[B] KB Belkhayate — REBUILD depuis zéro    ← EN COURS (stratégie révisée 12/06/2026)
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
[I] Dashboard React 18 + 3 thèmes           ← UI + bouton STOP ALL
        ↓
[J] Paper Trading 30 jours obligatoire      ← validation conditions Mode Auto
        ↓
[K] Activation Mode AUTO (conditionnel)     ← 6 conditions satisfaites + bouton
        ↓
[L] Integration Vision-Decision 5 couches  ← pipeline complet + 8 tests validation
```

---

## 🏗️ ARCHITECTURE VISION-DÉCISION TEMPS RÉEL (référence)

> Source : `Prompt_Cowork_TRADEX_Vision_Decision_v2_corrige.md` — integre S18 · 2026-06-20
> ⚠️ ADAPTATION STACK : le prompt source proposait Mistral local + ChromaDB (Couche 3).
> Stack TRADEX verrouilee Claude API + KB JSON → Couche 3 = prompt caching claude_brain.py.

### 5 Couches (flux de traitement)

```
COUCHE 0 — SOURCE (NinjaTrader 8, NinjaScript C#)
  Add-on NinjaScript : exporte OHLCV + COG Belkhayate + ADX a chaque bougie (OnBarUpdate)
  Canal local : WebSocket ou HTTP localhost | Debut progressif : CSV simple d'abord
  Fichier cible : Add-on NT8 C# (Phase C)

COUCHE 1 — INGESTION (FastAPI local, Python)
  Recoit flux bougies temps reel depuis NT8
  Latence cible < 50ms (a mesurer, pas supposee)
  Buffer glissant N dernieres bougies
  CIRCUIT BREAKER FEED : derniere donnee > X secondes → etat NO_TRADE force
  Fichier cible : nt8_ingestion.py (Phase C)

COUCHE 2 — DETECTION ALGORITHMIQUE (Python pur, 0€)
  Detecte patterns sur NOMBRES (swing highs/lows, triangles, flags, H&S, S/R, trendlines)
  Utilise les regles TA101 / Belkhayate extraites comme REGLES DE VALIDATION
  Produit un SCORE DE CONFIANCE 0-100% par pattern detecte
  Si score >= 70% → pattern clair, pas d'appel Claude (0 cout)
  Si score < 70% → declenche Couche 4 (ambiguite = vision/decision Claude)
  Fichier cible : pattern_detector.py + signal_scorer.py (Phase D+E)

COUCHE 3 — KB BELKHAYATE (Claude API + prompt caching sur KB JSON)
  ⚠️ ADAPTATION : Mistral/ChromaDB remplace par claude_brain.py existant + prompt caching
  Interroge KNOWLEDGE_BASE_MASTER.json : regles Belkhayate, psychologie, discipline
  Repond aux questions de connaissance (criteres pattern valide, regles Rhodes, anti-FOMO)
  Couts quasi-nuls grace au prompt caching (>= 90% cache hits attendu)
  Fichier cible : claude_brain.py etendu (Phase B+D)

COUCHE 4 — VISION + DECISION FINALE (Claude API, claude-sonnet-4-6)
  DECLENCHEE, JAMAIS EN CONTINU. Appel uniquement si score Couche 2 < 70%
  Volume estime : 5-20 appels/jour | Budget cible : 20-50 $/mois
  RATE LIMITER : hard stop N appels Claude/jour (parametre .env, ex 30/jour)
  CIRCUIT BREAKER COUT : depassement seuil → NO_TRADE + alerte utilisateur

  Ordre obligatoire avant toute decision :
  1. NEWS GATE : NFP/FOMC/CPI/EIA/OPEP+ → NO_TRADE / WAIT / REDUCE_RISK
  2. CONTEXTE INTERMARCHE + COT : biais de fond hebdo uniquement (INTERDIT trigger intraday)
  3. CROISEMENT DECISIONNEL : pattern + COG + KB + macro
     Imposer : stop defini AVANT entree, taille calculee, R/R >= 1.5, scenario oppose etudie
  4. COUTS REELS : spread, slippage, commissions, rollover futures (GC/CL/ES par contrat actif)
  5. EXECUTION GATEKEEPER : sortie = NO_TRADE / WAIT / REDUCE_RISK / TRADE_ALLOWED
     Etat par defaut = NO_TRADE. TRADE_ALLOWED uniquement si TOUTES conditions reunies.

COUCHE TRANSVERSALE — AUDIT & MONITORING
  AUDIT LOG : historiser chaque decision IA (inputs 4 couches + output gatekeeper + timestamp)
  MONITORING : health check des 5 couches, alerte si module tombe
  MODEL VERSION CONTROL : version Claude gelee et loguee dans les commits
  Fichiers cibles : audit_log.py + monitoring.py (Phase H)
```

### Regle de repartition des modeles

| Tache | Outil | Cout |
|-------|-------|------|
| Detection patterns (nombres) | Python algo Couche 2 | 0€ |
| KB Belkhayate (texte) | Claude API + prompt caching | ~0€ (cache hits) |
| Vision charts (ambiguite score < 70%) | claude-sonnet-4-20250514 | payant si declenche |
| Decision finale (croisement) | claude-sonnet-4-6 | ~0.01$/signal |

### 11 Fichiers a creer (phase d'appartenance)

| # | Fichier | Phase |
|---|---------|-------|
| 1 | Add-on NinjaScript C# (export NT8 → canal local) | C |
| 2 | nt8_ingestion.py (FastAPI + circuit breaker feed) | C + H |
| 3 | pattern_detector.py (detection algo patterns + score confiance) | D + E |
| 4 | claude_brain.py etendu (KB JSON + prompt caching) | B + D |
| 5 | vision_client.py (Claude API vision/decision + rate limiter + CB cout) | E + F |
| 6 | news_gate.py (calendrier CL/GC/ES + blocage NFP/FOMC/EIA) | F |
| 7 | execution_gatekeeper.py (NO_TRADE → TRADE_ALLOWED) | F |
| 8 | audit_log.py + monitoring.py (health check 5 couches) | H |
| 9 | prompt_vision.txt (lecture chart structuree) | B |
| 10 | prompt_decision.txt (croisement Belkhayate multi-facteurs) | B |
| 11 | schemas/couches_format.json (JSON standardise inter-couches) | C |

### Dependencies (ordre obligatoire)

1. KB COMPLETE AVANT couches 3-4 (zero valeur si KB incomplete)
2. Couche 0 (NinjaScript) + Couche 2 (detection algo) → demarrage PARALLELE possible
3. News Gate + Gatekeeper AVANT premier test decision reelle
4. Ordre : Couche 0 → 1 → 2 → 3 → News Gate → Gatekeeper → 4 → Audit/Monitoring

### Plan de validation (8 tests obligatoires)

| # | Test | Critere |
|---|------|---------|
| 1 | Detection algo : 50 bougies historiques CL | Swing points + patterns + score corrects |
| 2 | Circuit breaker feed | Couper flux → NO_TRADE automatique |
| 3 | KB Claude : 10 questions Belkhayate | Bons passages recuperes |
| 4 | Vision Claude : 5 screenshots | Identification coherente vs detection algo |
| 5 | News Gate : simuler FOMC imminent | Sortie NO_TRADE confirmee |
| 6 | Gatekeeper : signal sans stop | Refus confirme (NO_TRADE par defaut) |
| 7 | Decision complete : 1 signal reel passe en 5 couches | Coherence + couts reels presents |
| 8 | Rate limiter : simuler 31 appels/jour | Hard stop au seuil confirme |

---

## ETAT ACTUEL (au 2026-06-12)

| Item | Etat | Note |
|------|------|------|
| Reorganisation structure 00→06 | OK | commit 960fe88 |
| CLAUDE.md a jour | OK | reflète structure 00→06 |
| Moteur TRANSVIDEO | OK | 01-moteur-transvideo\scripts\ |
| Code SaaS migre 05-saas\ | OK | config, engine, KB, utils |
| Circuit breaker repare | OK | commit 75a517e |
| KB Belkhayate JSON | INVALIDE | 142 whisper_*.txt = NotebookLM (hallucinations confirmees) |
| PDFs methode-belkhayate | INVALIDE | generes par generateur-prompts-pro (mentions modele inexistant) |
| KNOWLEDGE_BASE_MASTER.json | INVALIDE | double hallucination — a reconstruire |
| Strategie KB rebuild | OK | STRATEGIE_KB_MASTER.md + RAPPORT_SOURCES_KB_2026.md |
| Collecteurs (NT8, ATAS, news, COT, macro) | NON | Phase C (en attente Phase B) |
| data\NT8_data.csv + data\ATAS_signals.json | OK | fichiers exemples crees |
| dossier data\ | A CREER | Phase C |
| Mode AUTO | BLOQUE | BLOQUE par defaut |

---

## PHASE A — Documentation & garde-fous — TERMINEE

Livrables commites : GARDE_FOUS_PROPOSES.md + FEUILLE_DE_ROUTE.md + MASTER_TRADEX_AI_v2.md + APPORTS_GUIDE_EXTERNE.md

---

## PHASE B — KB Belkhayate (REBUILD depuis sources primaires)

> DECISION DU 12/06/2026 : toutes les sources existantes sont invalides (AI-generated).
> La KB est reconstruite DEPUIS ZERO avec des sources primaires verifiees.
> Documents de reference : STRATEGIE_KB_MASTER.md + RAPPORT_SOURCES_KB_2026.md

### Architecture KB — 3 couches

```
Couche 1 — Code Python (PAS de JSON)
  Formules mathematiques exactes : BGC, Timing, Pivots, regle 3/4+2/3
  Fichier : 05-saas\engine\belkhayate_formulas.py
  Source : Pine Script TradingView (open-source, code verifie)

Couche 2 — Regles Belkhayate (JSON structure)
  UNIQUEMENT regles de trading de Mustapha Belkhayate
  Source : YouTube @MostafaBelkhayate (yt-dlp + Whisper reel)
  Fichier : 04-cerveau-trading\KNOWLEDGE_BASE_MASTER.json
  Schema obligatoire : id, couche, categorie, texte, actifs,
    source_url, source_timestamp, verbatim, belkhayate_specifique,
    confirme_multi_source, confiance, validated_by_human

Couche 3 — Connaissances trading universelles (JSON)
  Order Flow, COT, Wyckoff, SMC, Macro, Inter-marches
  Source : YouTube chaines verifiees (millions abonnes)
  Fichier : 04-cerveau-trading\KNOWLEDGE_BASE_LAYER3.json
```

### Plan d'action en 4 etapes

#### Etape B-01 — Academia.edu + TradingView Pine Script (Couches 1+2 base)
- Telecharger PDF Academia.edu : recherche "belkhayate gravity center"
- Extraire formules BGC, Timing, Pivots → belkhayate_formulas.py
- Extraire Pine Script open-source TradingView → valider formules
- Extraire regles de trading → Couche 2 JSON (base)
- Livrable : 05-saas\engine\belkhayate_formulas.py + regles Couche 2 (base)
- Critere : python -m py_compile belkhayate_formulas.py sans erreur

#### Etape B-02 — YouTube @MostafaBelkhayate → Couche 2 (pipeline Whisper)
- Installer yt-dlp + OpenAI Whisper (modele large)
- Telecharger audio MP3 des videos @MostafaBelkhayate
- Transcrire avec Whisper large (95-98% precision, accent marocain)
- Extraire regles Belkhayate → enrichir Couche 2 JSON
- Pipeline : yt-dlp → MP3 → Whisper → Claude extraction → JSON valide
- Critere : minimum 50 regles Couche 2 avec source_url + verbatim reels

#### Etape B-03 — Autres chaines YouTube → Couche 3
- Chaines cibles (millions abonnes, verifiees) :
  - The Trading Geek, Gigi Trading, Anton Kreil, ICT Michael Huddleston
  - LuxAlgo (Order Flow), ThinkingAnts (macro)
- Meme pipeline : yt-dlp → Whisper → extraction → Couche 3 JSON
- Domaines : Order Flow, COT, Wyckoff, SMC, Inter-marches, Macro/News
- Critere : 7 domaines couverts, minimum 20 regles par domaine

#### Etape B-04 — Validation et nettoyage
- Supprimer : 142 whisper_*.txt (NotebookLM) + 6 PDFs invalides (generateur-prompts-pro)
- Supprimer : KNOWLEDGE_BASE_MASTER.json actuel (double hallucination)
- Validation manuelle : relecture 50 regles aleatoires par Abdelkrim
- Test claude_brain.load_kb_rules() → charge sans erreur, moins de 50k tokens

**Critere de validation Phase B** : claude_brain.load_kb_rules() charge sans erreur ; systeme de prompt moins de 50k tokens ; zero regle sans source_url reelle.

**Estimation effort** : 4-6 sessions Claude Code + Cowork.

---

## PHASE C — Collecteurs de données (5 modules)

**Objectif** : alimenter les 7 cercles en continu.

**Prerequis** : Phase B + NinjaTrader 8 + ATAS configures.

Note : creer C:\trading-copilote\data\ en debut de Phase C.

| Module | Cercle | Source | Sortie |
|--------|--------|--------|--------|
| nt8_collector.py | C1 Prix | JSON NT8 ATI | data\nt8_data.json |
| atas_collector.py | C2 Order Flow | JSON ATAS Pro | data\atas_data.json |
| cot_collector.py | C3 Institutionnels | CFTC API hebdo | data\cot_data.json |
| macro_collector.py | C4+C7 | FRED + EIA + Alpha Vantage + OPEC | data\macro_data.json |
| news_collector.py | C5+C6 | Finnhub + GDELT | data\news_data.json |

**Garde-fous Phase C** : G9 (calendrier OPEC) + Atomic writes (deja actif).

**Estimation** : 4-5 sessions.

---

## PHASE D — Moteur Belkhayate Python

**Objectif** : recalculer indicateurs Belkhayate en Python (validation independante NT8).

**Prerequis** : Phase B (couche 1 belkhayate_formulas.py) + Phase C (nt8_collector).

**Livrable** : 05-saas\engine\belkhayate.py
- BGC (ratio 0.618) + Direction + Energie + Pivots
- Validation Python vs NT8 : ecart moins de 1% sur 50 bougies par actif

**Garde-fous Phase D** : P1 (invalidation setup Belkhayate).

**Estimation** : 3 sessions.

---

## PHASE E — Signal Scorer + Detection regime + Walk-Forward

**Objectif** : scoring 7 cercles + classification regime + backtesting.

**Prerequis** : Phases C + D.

**Livrables** :
- 05-saas\engine\signal_scorer.py : score_7_cercles(), HysteresisFilter, CoolDownGuard, AntiNoiseFilter, walk_forward_validate, monte_carlo_stress
- Extension correlations.py : detect_correlation_break, detect_market_regime

**Critere** : backtest 3 mois minimum, win rate superieur a 55%.

**Garde-fous Phase E** : G7 (regime marche) + filtres anti-bruit.

**Estimation** : 3-4 sessions.

---

## PHASE F — Trade Validator + Risk Engine extensions

**Objectif** : couche bloquante pre-ordre.

**Prerequis** : Phase E.

**Livrables** :
- 05-saas\engine\trade_validator.py : check_stop_loss, check_anti_doublon, check_dead_zone, check_rollover, validate_order
- Extensions risk_manager.py : LEVIER_PAR_REGIME, adjust_position_size, check_drawdown_breakers, write_mandatory_lock, is_trading_locked

**Garde-fous Phase F** : G1, G2, G3, G4, G5, G6.

**Estimation** : 2-3 sessions.

---

## PHASE G — Client NT8 ATI port 36973 + Killswitch Internet

**Prerequis** : Phase F + NT8 ATI active.

**Livrables** : nt8_ati_client.py + order_manager.py + network_monitor.py

**Critere** : 48h test simulation demo Rithmic sans erreur.

**Garde-fous Phase G** : G8 (killswitch internet).

**Estimation** : 3-4 sessions.

---

## PHASE H — FastAPI locale + Health monitoring

**Prerequis** : Phases C + E + F + G.

**Livrables** : 05-saas\api\main.py + routes signals / modes / risk + health.py

**Garde-fous Phase H** : G10 (monitoring sante).

**Estimation** : 2 sessions.

---

## PHASE I — Dashboard React 18

**Prerequis** : Phase H.

**Sous-etapes** : I.1 Bootstrap Vite + I.2 Choix theme + I.3 Composants (9 composants).

**Composants cles** : RiskGuard, ModeExecution, KPIBar, BelkhayateLevels, IntermarketPanel, DisciplineLog, Dashboard (STOP ALL permanent + disclaimer AMMC).

**Estimation** : 4-5 sessions.

---

## PHASE J — Paper Trading 30 jours obligatoire

**Protocole** : 30 jours, Mode MANUEL uniquement, logs quotidiens JSON+.md.

**Criteres** : win rate superieur a 55%, DD total moins de 5%, zero deconnexion NT8/ATAS plus de 60s sur 24h.

---

## PHASE K — Activation Mode AUTO (conditionnel)

6 conditions satisfaites → bouton "J'ACTIVE LE MODE AUTO" + mot de passe + log date SQLite.

| # | Condition | Phase |
|---|-----------|-------|
| 1 | Backtest 3 mois valide | E |
| 2 | Win rate superieur a 55% | E + J |
| 3 | Risk Engine valide | F |
| 4 | Broker Rithmic teste 48h | G + J |
| 5 | NT8 ATI stable 24h | G + J |
| 6 | Validation explicite Abdelkrim | I + K |

---

## PHASE L — Integration Vision-Décision (Post-Paper Trading)

**Objectif** : câbler les 5 couches en pipeline complet et tester end-to-end.

**Prerequis** : Phase J (Paper Trading 30j valide) + KB complete (Phase B terminee).

**Livrables** :
- vision_pipeline.py (orchestration 5 couches en pipeline)
- rate_limiter.py (hard stop N appels Claude/jour, parametre .env)
- Audit log + monitoring cables et operationnels
- Format JSON standardise inter-couches (schemas/couches_format.json)
- Prompts vision et decision finalises et geles

**Tests de validation** : les 8 tests du plan ci-dessus (section Architecture).

**Garde-fous Phase L** : Rate limiter hard stop + circuit breaker cout actifs depuis le premier test.

**Estimation** : 3-4 sessions.

---

## SYNTHESE EFFORT ESTIME

| Phase | Sessions estimees | Duree min |
|-------|-------------------|-----------|
| A — Documentation | Terminee | — |
| B — KB Rebuild (4 etapes) | 4-6 | 2-3 semaines |
| C — Collecteurs | 4-5 | 2 semaines |
| D — Moteur Belkhayate | 3 | 1-2 semaines |
| E — Signal Scorer | 3-4 | 2 semaines |
| F — Trade Validator | 2-3 | 1 semaine |
| G — NT8 ATI + Killswitch | 3-4 | 1-2 semaines |
| H — FastAPI | 2 | 1 semaine |
| I — Dashboard React | 4-5 | 2-3 semaines |
| J — Paper Trading | 0 (passif) | 30 jours |
| K — Mode AUTO | 1 | 1 jour |
| L — Vision-Decision Integration | 3-4 | 2 semaines |
| Total | 30-38 sessions | 3-5 mois |

---

## REGLES NON NEGOCIABLES

1. Mode AUTO BLOQUE jusqu'a Phase K + 6 conditions.
2. Chaque phase validee par Abdelkrim avant la suivante.
3. Aucune decision CLAUDE.md ne peut etre rouverte (stack, actifs, broker, methode).
4. Methode Belkhayate prioritaire — Couche 2 = Belkhayate UNIQUEMENT.
5. Zero regle sans source primaire verifiable (URL + timestamp).
6. Disclaimer AMMC + SQLite local (CNDP) permanents dans l'interface.

---

## PROCHAINE ETAPE IMMEDIATE

Phase B — Etape B-01 : Academia.edu PDF + TradingView Pine Script

Commandes a executer dans PowerShell :
1. Verifier yt-dlp : yt-dlp --version
2. Verifier Whisper : whisper --help
3. Chercher PDF Academia.edu "belkhayate gravity center"
4. Extraire formules → 05-saas\engine\belkhayate_formulas.py

---

Derniere mise a jour : 2026-06-20 (S18) — Architecture Vision-Decision 5 couches integree (Phase L ajoutee). Stack adaptee : Mistral/ChromaDB → Claude API + KB JSON.
Documents gouvernants : STRATEGIE_KB_MASTER.md + RAPPORT_SOURCES_KB_2026.md
