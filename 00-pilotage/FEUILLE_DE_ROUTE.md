# FEUILLE DE ROUTE — TradEx AI

> Source de vérité : `CLAUDE.md` (décisions verrouillées) + `00-pilotage\docs\MASTER_TRADEX_AI_v2.md`
> Documents KB : `STRATEGIE_KB_MASTER.md` + `RAPPORT_SOURCES_KB_2026.md`
>
> **Dernière mise à jour** : 2026-06-24 (S24) — Architecture 8 couches intégrée · Phase E/F/K enrichies · Pipeline Gemini multimodal actif.
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
[E] Signal Scorer + Régime + WFO + Loop3    ← score /10 + 4 régimes + feedback_engine
        ↓
[F] Trade Validator + Risk extensions       ← G1-G6 + Kelly + OOD + dual-Claude
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

## ETAT ACTUEL (mis à jour S43 — 29/06/2026)

> Dernière mise à jour réelle : S43, commit 689e452. Section S24 conservée pour historique.

### Avancement Phase C (S36→S43)

| Module | État | Commit | Note |
|--------|------|--------|------|
| cot_collector.py | ✅ FONCTIONNEL | S36 | CFTC OData v4 · filtrage code contrat exact |
| macro_collector.py | ✅ FONCTIONNEL | S36 | FRED + EIA (WCESTUS1 hors SPR) |
| news_collector.py | ✅ FONCTIONNEL | S38 | Finnhub ✅ · GDELT ⚠️ SSL côté serveur |
| data_collector_runner.py | ✅ FONCTIONNEL | da6e197 | run_all() · fraîcheur COT/Macro/News |
| prompt_builder.py | ✅ FONCTIONNEL | da6e197 | GOD_MODE 15 champs · 6 règles absolues |
| claude_brain.py | ✅ RÉPARÉ | da6e197 | load_kb_rules() + load_phase_c_data() + cache_control ephemeral |
| test_cycle_complet_api.py | ✅ PASS 5/5 | 689e452 | Claude API répond · 15 champs · confiance 72% · score_kb 7.4 |
| KNOWLEDGE_BASE_MASTER.json | ✅ 4142 règles | S40 | 100 vidéos Gemini + 62 chapitres |
| USE_MOCK_DATA | True (mock) | — | NT8 réel non encore connecté |

### Tableau d'état complet (depuis S24)

| Item | Etat | Note |
|------|------|------|
| Reorganisation structure 00→06 | OK | commit 960fe88 |
| CLAUDE.md a jour | OK | S43 — gemini-2.5-flash verrouille, architecture 8 couches |
| Moteur TRANSVIDEO | OK | 01-moteur-transvideo\scripts\ |
| Code SaaS migre 05-saas\ | OK | config, engine, KB, utils |
| Circuit breaker repare | OK | commits 75a517e + S36 (protected_call active) |
| KNOWLEDGE_BASE_MASTER.json | OK | **4 142 regles** (100 videos Gemini + 62 chapitres) · SHA256 31348bda |
| Pipeline Gemini multimodal | OK | 100 videos traitees · KB stable depuis S40 |
| Collecteurs Phase C | OK | cot ✅ · macro ✅ · news ✅ (GDELT SSL côté serveur, non bloquant) |
| data_collector_runner.run_all() | OK | S42 · fraîcheur COT 24h / Macro 24h / News 15min |
| prompt_builder.py (GOD_MODE) | OK | S42 · 15 champs JSON · sections NT8 + COT + Macro + News |
| Cycle complet API testé | **OK — 5/5 PASS** | S43 · commit 689e452 · HTTP 200 · 13.7s · confiance 72% |
| dossier data\ | OK | data/mock/ · data/live/ (vide — NT8 non connecté) |
| Mode AUTO | BLOQUE | BLOQUE par defaut — 8 conditions Phase K non remplies |
| NT8 live (USE_MOCK_DATA) | NON | Prochaine étape : basculer USE_MOCK_DATA = False + NT8 réel |
| regime_detector.py | NON | Phase E — nouveau fichier a creer |
| signal_scorer.py | NON | Phase E — grille /10 conceptuelle, pas codee |
| feedback_engine.py | NON | Phase E/F — Loop 3 absente |
| SQLite schema | NON | Phase E — schema defini dans rapport architecture |
| Kelly position sizing | NON | Phase F — actuellement 2% fixe |
| OOD detector | NON | Phase F — nouveau fichier a creer |
| Dual-Claude validation | NON | Phase F/L — 2 appels par signal |

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

## PHASE E — Signal Scorer + Detection regime + Walk-Forward + Loop 3

**Objectif** : scoring /10 + 4 regimes + WFO anti-overfitting + boucle apprentissage.

**Prerequis** : Phases C + D.

**Livrables** :
- 05-saas\engine\signal_scorer.py : score_7_cercles(), HysteresisFilter, CoolDownGuard, AntiNoiseFilter, walk_forward_validate, monte_carlo_stress
- 05-saas\engine\regime_detector.py : detect_regime() — 4 regimes (TRENDING_BULL, TRENDING_BEAR, RANGING, VOLATILE)
  - ADX + ATR zscore + VIX + correlation_breakdown
  - seuil_signal adaptatif par regime (7.0 defaut · 7.5 RANGING · 9.0 VOLATILE · 7.0→6.5 TRENDING_BULL apres unlock)
  - GC comme reference regime (+ option cross-asset Phase E+)
  - Bootstrap : charger 252j de donnees historiques NT8 (CSV) avant live
- 05-saas\engine\feedback_engine.py : Loop 3 — analyse chaque trade ferme
  - update_rule_performance(), update_regime_memory(), check_recalibration_needed()
  - generate_weekly_report() auto
- 05-saas\engine\threshold_adapter.py : auto-calibration score_min
  - Bornes absolues : 6.0 ≤ score_min ≤ 9.0. Defaut : 7.0. Jamais en dehors.
- 05-saas\db\schema.sql : 5 tables SQLite (signals, trades, rule_performance, regime_memory, parameter_history)
- Extension correlations.py : detect_correlation_break(), detect_market_regime()

**Critere** : backtest WFO 3 mois minimum (IS 90j + OOS 30j), win rate superieur a 55%, OOS/IS >= 0.70.

**Garde-fous Phase E** : G7 (regime marche) + filtres anti-bruit + seuil_signal verrouille >= 6.0.

**Estimation** : 4-5 sessions.

---

## PHASE F — Trade Validator + Risk Engine extensions + Intelligence Couche 5

**Objectif** : couche bloquante pre-ordre + position sizing intelligent + anti-biais IA.

**Prerequis** : Phase E.

**Livrables** :
- 05-saas\engine\trade_validator.py : check_stop_loss, check_anti_doublon, check_dead_zone, check_rollover, validate_order
- Extensions risk_manager.py : LEVIER_PAR_REGIME, adjust_position_size, check_drawdown_breakers, write_mandatory_lock, is_trading_locked
- kelly_fraction() dans risk_manager.py :
  - Half-Kelly (standard industrie) · plafond 2.0% (=max_risque_trade) · plancher 0.5%
  - Garde-fou : N < 50 trades → 1% fixe. kelly_valide = (n >= 50 AND CI_95_lower > 0.45)
- 05-saas\engine\ood_detector.py : is_out_of_distribution()
  - 5 metriques zscore (VIX, volume, ATR, corr, spread) vs 252j historique
  - >= 3 metriques > 2.5σ → OOD=EXTREME → confiance max 65% + Auto bloque
  - >= 2 metriques > 2.5σ → OOD=ELEVATED → taille reduite 50%
- portfolio_heat_check() : corrélation entre actifs ouverts > 0.7 → bloquer second trade
- slippage_estimator() : si slippage > 33% profit attendu → annuler
- Extensions claude_brain.py : dual-Claude validation (get_signal_dual)
  - Bull advocate + Bear advocate (2 appels par signal Mode Auto)
  - AMBIGUOUS (bull > 6 ET bear > 6) → WAIT automatique
  - Compte comme 2 appels sur rate limiter quotidien (max 15 cycles dual/jour)

**Garde-fous Phase F** : G1, G2, G3, G4, G5, G6, G11 (OOD), G12 (Kelly), G14 (dual-Claude), G15 (portfolio heat).

**Estimation** : 3-4 sessions.

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

**8 conditions satisfaites** → bouton "J'ACTIVE LE MODE AUTO" + mot de passe + log date SQLite.
*(Remplace les 6 conditions initiales — version plus rigoureuse adoptee en S24 apres rapport architecture.)*

| # | Condition | Mesure | Seuil | Phase |
|---|-----------|--------|-------|-------|
| 1 | Win rate Paper Trading | SQLite analytics | >= 55% sur 50+ trades | E + J |
| 2 | Drawdown max | SQLite analytics | <= 5% du capital | E + J |
| 3 | Sharpe ratio | SQLite analytics | >= 1.0 | E + J |
| 4 | OOS/IS ratio WFO | walk_forward_validate() | >= 0.70 | E |
| 5 | NT8 ATI stable | 48h sans deconnexion | 0 perte de connexion | G + J |
| 6 | Rithmic demo 48H | Test execution | 0 ordre fantome | G + J |
| 7 | Tous stress tests passes | 8 scenarios historiques | Comportement correct 8/8 | E + G |
| 8 | Validation explicite Abdelkrim | Bouton + mot de passe | Log SQLite avec timestamp | I + K |

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

| Phase | Sessions estimees | Duree min | Nouveautes S24 |
|-------|-------------------|-----------|---------------|
| A — Documentation | Terminee | — | — |
| B — KB Rebuild (4 etapes) | 4-6 | 2-3 semaines | Gemini batch + KB_INDEX D1→D172 |
| C — Collecteurs | 4-5 | 2 semaines | Bootstrap 252j historique NT8 (OOD) |
| D — Moteur Belkhayate | 3 | 1-2 semaines | — |
| E — Signal Scorer + Regime + WFO + Loop3 | 4-5 | 2-3 semaines | +regime_detector, feedback_engine, threshold_adapter, SQLite |
| F — Trade Validator + Kelly + OOD + Dual-Claude | 3-4 | 2 semaines | +kelly, ood_detector, portfolio_heat, dual_claude |
| G — NT8 ATI + Killswitch | 3-4 | 1-2 semaines | — |
| H — FastAPI | 2 | 1 semaine | — |
| I — Dashboard React | 4-5 | 2-3 semaines | — |
| J — Paper Trading | 0 (passif) | 30 jours minimum + WFO | WFO apres mois 3 |
| K — Mode AUTO | 1 | 1 jour | 8 conditions (etait 6) |
| L — Vision-Decision Integration | 3-4 | 2 semaines | — |
| Total | 32-42 sessions | 4-6 mois | — |

---

## CRITÈRES GO / NO-GO PAR PHASE (D-S31-4 — 26/06/2026)

> Format : chaque phase doit satisfaire TOUS les critères GO avant de démarrer la suivante.
> Validé par Abdelkrim. Aucune exception.

---

### PHASE A — Documentation & Garde-fous
**Statut : ✅ TERMINÉE — GO acquis**

---

### PHASE B — KB Belkhayate

| Critère GO | Mesure | Seuil |
|---|---|---|
| Batch Gemini (partiel OK) | `ls 03-transcriptions\nouvelles-sources\` | ≥ 42 fichiers (complet requis Phase E uniquement) |
| KB fusion terminée | `python -c "import json; d=json.load(open('04-cerveau-trading/KNOWLEDGE_BASE_MASTER.json')); print(len(d['rules']))"` | ≥ 1 461 règles |
| KB chargeable sans erreur | `python -m py_compile 05-saas/engine/claude_brain.py` + `load_kb_rules()` | 0 erreur |
| KB < 55k tokens | Script compact (C0A) | < 55 000 tokens (prompt caching OK) |
| Zéro règle sans source_url | Script audit source_url | 0 règle sans URL réelle |
| Validation humaine | Relecture 50 règles aléatoires par Abdelkrim | OK confirmé |

**NO-GO si :** batch incomplet · KB plante au chargement · règles sans source · tokens > 55k
**Rollback :** relancer batch Gemini sur vidéos manquantes · supprimer règles non sourcées
**Validé par :** Abdelkrim ✋

---

### PHASE C — Collecteurs de données

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase B partielle validée | KB chargeable + tokens < 55k + dossier data\ créé | ✅ |
| NinjaTrader 8 actif | NT8 ouvert + ATI activé port 36973 | Connecté |
| ATAS configuré | ATAS Pro ouvert + export JSON actif | Connecté |
| Dossier `data\` créé | `Test-Path C:\trading-copilote\data` | True |
| 5 collecteurs compilent | `python -m py_compile` sur chacun | 0 erreur |
| 10 cycles sans crash | Lancer chaque collecteur 10 itérations | 0 crash |
| Atomic writes actifs | Vérifier tempfile + os.replace dans chaque fichier | Présent |

**NO-GO si :** NT8 ou ATAS non disponibles · un collecteur crash sur 10 cycles · atomic writes absents
**Rollback :** corriger le collecteur fautif · ne pas avancer tant que les 5 ne tournent pas
**Validé par :** Abdelkrim ✋

---

### PHASE D — Moteur Belkhayate Python

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase B + C validées | GO Phase B + C | ✅ |
| belkhayate_formulas.py compile | `python -m py_compile belkhayate_formulas.py` | 0 erreur |
| BGC calculé | Test sur 50 bougies GC | Valeur != 0 |
| Direction calculée | Test sur 50 bougies | Valeur dans [-1, 0, 1] |
| Energie calculée | Test sur 50 bougies | Valeur numérique |
| Pivots calculés | Test sur 50 bougies | PP + R1-R3 + S1-S3 |
| Écart Python vs NT8 < 1% | Comparaison sur 50 bougies × 4 actifs (GC/HG/CL/ZW) | < 1% sur chaque actif |

**NO-GO si :** écart > 1% sur un actif · formule ne compile pas · valeur absurde détectée
**Rollback :** revoir formule concernée · re-sourcer dans Pine Script TradingView
**Validé par :** Abdelkrim ✋

---

### PHASE E — Signal Scorer + Régime + WFO + Loop3

| Critère GO | Mesure | Seuil |
|---|---|---|
| Batch Gemini terminé | `ls 03-transcriptions\nouvelles-sources\` | 203 fichiers |
| Phase C + D validées | GO Phase C + D | ✅ |
| signal_scorer.py compile | `python -m py_compile` | 0 erreur |
| regime_detector.py compile | `python -m py_compile` | 0 erreur |
| feedback_engine.py compile | `python -m py_compile` | 0 erreur |
| threshold_adapter.py compile | `python -m py_compile` | 0 erreur |
| SQLite schema créé | `db\schema.sql` exécuté + 5 tables présentes | OK |
| WFO 3 mois (IS 90j + OOS 30j) | walk_forward_validate() | Pas d'erreur |
| Win rate backtest | SQLite analytics | ≥ 55% sur 50+ signaux |
| OOS/IS ratio | walk_forward_validate() | ≥ 0.70 |
| Seuil score_min dans bornes | threshold_adapter | 6.0 ≤ score_min ≤ 9.0 |

**NO-GO si :** WFO échoue · win rate < 55% · OOS/IS < 0.70 · score_min hors bornes [6.0–9.0]
**Rollback :** revoir paramètres · relancer WFO · ne pas activer le scorer sur live
**Validé par :** Abdelkrim ✋

---

### PHASE F — Trade Validator + Risk Engine + OOD + Dual-Claude

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase E validée | GO Phase E | ✅ |
| trade_validator.py compile | `python -m py_compile` | 0 erreur |
| Blocage ordre sans stop | Test : envoyer signal sans SL → validator doit refuser | REFUSÉ confirmé |
| Kelly fraction dans bornes | kelly_fraction() avec N >= 50 trades | 0.5% ≤ Kelly ≤ 2.0% |
| OOD detector testé | 5 métriques zscore sur données historiques 252j | Détecte EXTREME + ELEVATED |
| Dual-Claude testé | 10 signaux tests bull/bear advocates | AMBIGUOUS → WAIT |
| Portfolio heat testé | 2 trades corrélés > 0.7 → bloquer le 2e | BLOQUÉ confirmé |
| Risque journalier actif (D-S31-3) | kill switch déclenché si perte > max/jour | BLOQUÉ confirmé |
| Anti-martingale actif (D-S31-3) | Tentative d'augmenter taille après perte → refus | REFUSÉ confirmé |

**NO-GO si :** un ordre sans SL passe · Kelly hors bornes · dual-Claude non testé · kill switch inactif
**Rollback :** corriger le validateur · ne pas toucher au live tant que tous les tests ne passent pas
**Validé par :** Abdelkrim ✋

---

### PHASE G — NT8 ATI port 36973 + Killswitch Internet

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase F validée | GO Phase F | ✅ |
| NT8 ATI active port 36973 | Connexion TCP/IP locale | Connecté |
| nt8_ati_client.py compile | `python -m py_compile` | 0 erreur |
| 48h simulation demo Rithmic | Test continu | 0 erreur · 0 déconnexion |
| Zéro ordre fantôme | Log order_manager.py sur 48h | 0 ordre non voulu |
| Killswitch internet testé | Couper réseau → vérifier blocage immédiat | BLOQUÉ confirmé |

**NO-GO si :** déconnexion NT8 non gérée · ordre fantôme détecté · killswitch inactif
**Rollback :** corriger client NT8 · répéter 48h test depuis zéro
**Validé par :** Abdelkrim ✋

---

### PHASE H — FastAPI locale + Health monitoring

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phases C + E + F + G validées | GO phases | ✅ |
| FastAPI démarre sans erreur | `uvicorn main:app` | 0 erreur au démarrage |
| Routes testées | 100 requêtes sur chaque route | 0 crash · latence < 200ms |
| Health check actif | `/health` renvoie statut 5 couches | OK |
| Monitoring 5 couches actif | Alerte si une couche tombe | Alerte confirmée |

**NO-GO si :** un endpoint crash sur 100 requêtes · health check absent · monitoring inactif
**Rollback :** corriger l'endpoint fautif · ne pas avancer avant 100 requêtes sans erreur
**Validé par :** Abdelkrim ✋

---

### PHASE I — Dashboard React 18

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase H validée | GO Phase H | ✅ |
| `npm run build` sans erreur | Build production | 0 erreur |
| 9 composants rendus | Visite manuelle de chaque écran | OK visuel |
| Signal 18 champs affiché (D-S31-1) | Écran opportunité de trade | 18 champs visibles |
| STOP ALL fonctionnel | Clic → toutes actions bloquées | BLOQUÉ confirmé |
| Disclaimer AMMC visible | Présent sur TOUS les écrans | Visible en permanence |
| Aucun bouton d'ordre réel | Audit UI | 0 bouton ordre réel |

**NO-GO si :** STOP ALL non fonctionnel · disclaimer absent · bouton ordre réel présent
**Rollback :** corriger composant · ne pas livrer l'UI tant que les 3 conditions critiques ne sont pas OK
**Validé par :** Abdelkrim ✋

---

### PHASE J — Paper Trading 30 jours

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase I validée | GO Phase I | ✅ |
| 30 jours de trading accomplis | Journal JSON + .md quotidien | 30 entrées |
| Win rate | SQLite analytics | ≥ 55% sur 50+ trades |
| Drawdown total | SQLite analytics | ≤ 5% du capital paper |
| Stabilité connexion | Logs NT8/ATAS | 0 déconnexion > 60s sur 24h |
| Kill switch testé en conditions réelles | Déclenché au moins 1 fois | Log SQLite |
| Mode AUTO resté bloqué | Vérification code + logs | AUTO_MODE = False tout le long |

**NO-GO si :** win rate < 55% · DD > 5% · déconnexion non gérée · mode AUTO activé
**Rollback :** reprendre paper trading · corriger le problème · repartir de zéro sur les 30 jours
**Validé par :** Abdelkrim ✋

---

### PHASE K — Activation Mode AUTO

| Critère GO | Mesure | Seuil |
|---|---|---|
| Les 8 conditions K (tableau existant) | Voir section PHASE K ci-dessus | 8/8 satisfaites |
| Bouton activé + mot de passe | Action manuelle Abdelkrim | Log SQLite avec timestamp |
| Circuit Breaker ACTIF | Test timeout 15s → retry 2x → ATTENDRE | Comportement confirmé |
| Risque journalier/hebdo actif (D-S31-3) | Vérification settings.py | Valeurs configurées |

**NO-GO si :** UNE seule des 8 conditions non remplie → blocage total · pas de dérogation possible
**Rollback :** identifier la condition manquante · la corriger · re-valider toutes les 8
**Validé par :** Abdelkrim ✋ (bouton physique + mot de passe)

---

### PHASE L — Intégration Vision-Décision 5 couches

| Critère GO | Mesure | Seuil |
|---|---|---|
| Phase J validée (30j paper) | GO Phase J | ✅ |
| Phase B complète (KB) | GO Phase B | ✅ |
| vision_pipeline.py compile | `python -m py_compile` | 0 erreur |
| rate_limiter.py actif | Test 31 appels → hard stop au seuil | BLOQUÉ confirmé |
| Audit log opérationnel | Vérification 10 décisions loguées | OK |
| Les 8 tests de validation passent | Plan de validation (section Architecture) | 8/8 |

**NO-GO si :** un test sur 8 échoue · rate limiter inactif · audit log absent
**Rollback :** corriger le test fautif · ne pas passer en production avant 8/8
**Validé par :** Abdelkrim ✋

---

---

## VEILLE TECHNO S43 — APPORTS VÉRIFIÉS (29/06/2026)

> Sources vérifiées par screenshot direct le 29/06/2026. Zéro hallucination.
> Rapport complet : `00-pilotage\_context\RAPPORT_SESSION_VEILLE_TECHNO_20260629.md`

### 1. Loop Engineering — Maker + Checker (Boris Cherny / Anthropic)

**Source vérifiée** : Boris Cherny = créateur de Claude Code (Anthropic). Concept publié juin 2026.

**Concept clé** : un seul agent = biais de confirmation. Solution : 2 agents séparés.
- **MAKER** : produit le signal → `claude_brain.get_signal()` — DÉJÀ CODÉ Phase C
- **CHECKER** : valide le signal contre les règles — **MANQUANT dans TRADEX**

**Impact Phase F** : le dual-Claude existant (bull/bear advocates) couvre l'angle marché.
Le CHECKER Belkhayate est différent : il valide le signal sorti contre les **42 garde-fous**
(`00-pilotage\GARDE_FOUS.md`) via un second appel Claude avec prompt checker dédié.
→ Ajouter `checker_agent.py` en Phase F comme sous-tâche de dual-Claude.

**Boucle 1 (heartbeat 15min)** : déjà implémentée → `data_collector_runner.run_all()`.
Fraîcheur : COT 24h · Macro 24h · News 15min. Rien à construire.

**À faire en Phase F** : `checker_agent.py` — valide signal contre 42 garde-fous (1 appel Claude,
prompt checker, compte sur le rate limiter). Distinct de dual-Claude bull/bear.

#### Loop 4 — Couche d'exécution Scénario B v1.1

```
[Loop 4 — Exécution]  Couche d'exécution Scénario B v1.1
  - Schéma JSON figé carte de confirmation v1.0 ............ SPÉCIFIÉ
  - Module execution_guardrails_v1_1.py .................... CODÉ (post-audit)
  - Brancher broker_send_fn sur pont NinjaTrader ........... À FAIRE
  - Tests unitaires garde-fous ............................. À FAIRE
  - Valider GUARDRAILS + passer config_validated = True .... À FAIRE (Abdelkrim)
  KB : non impactée | Stack : non impactée | Tiers : aucun
```

Fichiers : `docs/architecture/execution/` (spec + schéma) · `05-saas/engine/execution_guardrails_v1_1.py` (module)

#### Prompt Caching — Modification 3/3 (DIFFÉRÉE S47)

```
[Prompt Caching — Mod 3/3]  Brancher KB_CAPABILITIES dans get_signal()
  - TTL 1h bloc KB Belkhayate (ligne 107) .................. ✅ FAIT
  - Logging [CACHE] read/write/input (ligne 127-131) ........ ✅ FAIT (S47)
  - Bloc cache KB_CAPABILITIES (lignes 110-115) ............. ✅ CODE EN PLACE
  - Passer kb_capabilities= dans get_signal() ............... ⏳ DIFFÉRÉ (S47)
    → Charger 82 règles prioritaires (fiabilite_hallucinations +
      gestion_risque_llm) depuis KB_CLAUDE_CAPABILITIES.json
    → Les passer à call_claude_kb(kb_rules, prompt, kb_capabilities=...)
    → Sans ce branchement, le 2e bloc cache n'est JAMAIS activé
  Fichier : 05-saas/engine/claude_brain.py · Fonction : get_signal()
```

---

### 2. GStack (Garry Tan / CEO Y Combinator)

**Source vérifiée** : `github.com/garrytan/gstack` — 118k stars · 17.6k forks · actif (4 jours)
· 306 branches · MIT License. Confirmé par screenshot 29/06/2026.

**Utilité pour TRADEX** : faible — GStack est un outil de workflow de développement logiciel
(plan, review, ship), pas un outil de trading.

**Utilité pour DIFAI/CARIO** : forte — `/plan-ceo-review`, `/review`, `/ship` pertinents
pour les phases de développement SaaS. À installer sur DIFAI quand Phase I TRADEX terminée.

**Action TRADEX** : aucune action requise maintenant. Bookmark pour DIFAI.

---

### 3. Garde-fous boucles agentiques — 3 règles impératives

> Source : Loop Engineering (Boris Cherny / Anthropic) + retour terrain juin 2026.
> Sans ces garde-fous : risque de boucle infinie → facture API incontrôlée.
> **À implémenter AVANT toute automatisation scheduler dans TRADEX-AI.**

| Règle | Principe | Équivalent TRADEX-AI (Python) | État |
|---|---|---|---|
| **1. Condition de sortie explicite** | Définir `/goal` avec critère précis et vérifiable avant de lancer toute boucle | `while not signal_valid and iterations < MAX_ITER` — condition de sortie codée, jamais implicite | ❌ À coder avant Boucle 1 |
| **2. Plafond d'itérations** | Toujours `max_turns` — ex: `max_turns=10` pour éviter les boucles infinies | `MAX_CALLS_PER_DAY = 30` dans `settings.py` + compteur dans `rate_limiter.py` (Phase L) + `MAX_ITERATIONS = 10` dans tout futur scheduler | ❌ `rate_limiter.py` absent |
| **3. Human gate sur irréversible** | Validation humaine obligatoire avant tout ordre réel ou commit prod | Mode Manuel (Abdelkrim décide chaque signal) + Mode AUTO = False par défaut + bouton physique + mot de passe Phase K | ✅ DÉJÀ EN PLACE |

**Règle absolue TRADEX** : `rate_limiter.py` avec `MAX_CALLS_PER_DAY` doit être codé
**AVANT** tout scheduler automatique — pas en Phase L, mais comme prérequis de Boucle 1.

---

### 4. OpenAlice — Agent trading autonome open-source

**Source** : `github.com/TraderAlice/OpenAlice` — ⚠️ NON VÉRIFIÉ PAR SCREENSHOT.
À vérifier avant toute installation.

**Architecture confirmée dans le rapport** : Node.js · fichiers locaux · Web UI + Telegram + MCP.
**Brokers supportés** : Alpaca, Interactive Brokers, CCXT (crypto). **NinjaTrader = absent**.

**Point bloquant pour TRADEX** : NinjaTrader 8 n'est pas supporté nativement.
Intégration NT8 ↔ OpenAlice nécessiterait un pont custom (non trivial).

**Modèle IA configuré dans le rapport** : `claude-opus-4-7` → confirmé existant (screenshot claude.ai).

**Décision provisoire** :
- Si TRADEX reste sur NT8 → OpenAlice = couche exécution non prioritaire (Phase G déjà prévue avec NT8 ATI)
- Si migration vers Interactive Brokers envisagée → OpenAlice devient pertinent en Phase G

**Action Phase G** : évaluer OpenAlice vs NT8 ATI natif lors de la décision broker.
**Prérequis absolu** : paper trading validé (Phase J) avant toute connexion broker réel.

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

Derniere mise a jour : 2026-06-24 (S24) — Architecture 8 couches (RAPPORT_ARCHITECTURE_TRADEX_PARFAIT.md audit + corrections).
Phase E enrichie : regime_detector, feedback_engine, threshold_adapter, SQLite schema.
Phase F enrichie : kelly, OOD detector, dual-Claude, portfolio_heat, slippage_estimator.
Phase K : 6 → 8 conditions Go/No-Go Mode Auto.
Documents gouvernants : STRATEGIE_KB_MASTER.md + RAPPORT_SOURCES_KB_2026.md + RAPPORT_ARCHITECTURE_TRADEX_PARFAIT.md
