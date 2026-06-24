# RAPPORT — TRADEX-AI : VERS UNE APPLICATION DE TRADING PRESQUE PARFAITE
> Analyse technique en profondeur · Solutions innovantes et éprouvées · Plan de validation complet
> Auteur : Claude Sonnet 4.6 · Session S24 · 24/06/2026

---

## AVERTISSEMENT PRÉLIMINAIRE

Un système de trading "parfait" n'existe pas. Les marchés sont partiellement efficients et partiellement chaotiques. L'objectif atteignable est un système qui :
- Génère un **avantage statistique** reproductible (edge > 0)
- **Sait quand ne pas trader** (aussi important que quand trader)
- **Apprend de ses erreurs** sans être reprogrammé
- **Échoue en sécurité** lors de conditions anormales
- **S'améliore de lui-même** avec chaque trade réel

Ce document définit comment TRADEX-AI peut atteindre ce niveau. Il est ancré dans le code existant (risk_manager.py, staleness_monitor.py, claude_brain.py, settings.py) et dans les 12 phases de la FEUILLE_DE_ROUTE.md.

---

## PARTIE 1 — DIAGNOSTIC DU SYSTÈME ACTUEL

### 1.1 Ce qui existe et fonctionne

| Composant | Fichier | Force | Faiblesse |
|-----------|---------|-------|-----------|
| News Gate | risk_manager.py | NFP/FOMC/CPI bloqués 30min ET | Pas de blocage post-événement adaptatif |
| Staleness Monitor | staleness_monitor.py | 3 états (OPERATIONAL/MANUAL/BLOCKED) | Pas de reconnexion automatique |
| Circuit Breaker | circuit_breaker.py | 3 CB séparés (NT8/ATAS/Claude) | Pas de dégradation progressive |
| Risk Rules | risk_manager.py | 2%/trade, VIX gates, tweet suspension | Pas de Kelly, pas de sizing dynamique |
| KB + Claude Brain | claude_brain.py | Prompt caching, fallback local | Poids des règles statiques |
| Staleness | settings.py | Seuils configurables | TICK_SPECS incomplètes (HG/CL/ZW manquants) |
| Atomic Writes | atomic_writer.py | tempfile + os.replace | ✅ Correct |
| Classification actifs | settings.py | 3 catégories verrouilées | ✅ Correct |

### 1.2 Ce qui manque (bloquant pour la production)

1. **Add-on NinjaScript C#** : le fichier JSON source n'est pas écrit par NT8 encore
2. **Signal scorer réel** : la grille /10 n'est pas implémentée, seulement définie conceptuellement
3. **Régime marché** : aucune détection de régime (trending/ranging/volatile)
4. **Position sizing** : les règles existent dans RÈGLES_RISQUE mais ne calculent pas de taille réelle
5. **Loop 3 — Feedback post-trade** : aucune boucle d'apprentissage post-trade
6. **TICK_SPECS** : HG/CL/ZW manquants → impossible de calculer un P&L ou sizing correct
7. **Base de données** : aucun historique de signaux/trades en SQLite (SIGNAL_HISTORY_PATH = chemin mais vide)
8. **Dashboard** : maquettes existantes mais React non codé
9. **Orchestrateur** : pas de `main.py` — aucun point d'entrée qui démarre le système

### 1.3 Le diagnostic central

**Le système actuel est une excellente fondation mais c'est un moteur sans carrosserie.** Les garde-fous sont bien pensés. L'architecture 3 niveaux est correcte. Mais il n'y a pas encore de boucle fermée : signal → trade → résultat → apprentissage. Sans cette boucle, le système ne peut pas s'améliorer.

---

## PARTIE 2 — ARCHITECTURE CIBLE : LE SYSTÈME "PRESQUE PARFAIT"

### 2.1 La boucle ORAAD (fondation de tout)

Tout système de trading qui s'améliore repose sur une seule boucle :

```
OBSERVER   → Données NT8/ATAS/COT/Macro/News (Cercles C1→C7)
RAISONNER  → Analyse Belkhayate + KB + régime + corrélations
AGIR       → Signal affiché (Manuel) ou ordre envoyé (Auto)
MESURER    → Résultat du trade : prix entrée/sortie, P&L, durée
ADAPTER    → Mettre à jour poids des règles, seuils, position sizing
```

Chaque composant doit alimenter la boucle suivante. Sans le M et le A, le système reste statique.

### 2.2 Architecture en 8 couches (extension des 5 couches actuelles)

```
COUCHE 0 — SOURCE (NT8 NinjaScript C#)
  Export OHLCV + COG Belkhayate + ADX + Volume à chaque bougie
  Écriture atomique JSON dans data\live\{SYMBOL}.json
  Watchdog C# : si écriture échoue 3x → log erreur + continuer

COUCHE 1 — INGESTION (Python, staleness_monitor + data_reader)
  ✅ Existant — amélioration : reconnexion exponentielle
  Ajout : validation schéma JSON strict avant lecture
  Ajout : métriques de qualité data (nb valeurs nulles, spikes)

COUCHE 2 — DÉTECTION ALGORITHMIQUE (Python pur, 0€)
  signal_scorer.py : calcule score /10 par cercle
  pattern_detector.py : swings, pivots, triangles, H&S
  regime_detector.py : NOUVEAU — classifie le régime marché
  → Si score ≥ 7.0 ET régime favorable → déclenche Couche 3
  → Si score < 5.0 → WAIT immédiat, pas d'appel Claude

COUCHE 3 — RAISONNEMENT KB (Claude API + prompt caching)
  ✅ claude_brain.py — amélioration : dual-Claude validation
  Ajout : context enrichment (régime actuel + corrélations live)
  Ajout : uncertainty scoring (intervalle de confiance, pas score seul)

COUCHE 4 — DÉCISION FINALE (Claude API, déclenché si ambigu)
  Appel uniquement si Couche 2 score entre 6.0 et 8.0 (zone grise)
  Score < 6.0 → NO_TRADE sans appel. Score ≥ 8.0 → TRADE sans double-check.
  Rate limiter : max 30 appels/jour paramétrable .env

COUCHE 5 — RISK GATE (existant + extensions)
  ✅ runtime_guardrails() — amélioration : Kelly position sizing
  Ajout : corrélation portfolio check (no double exposure)
  Ajout : slippage estimation avant envoi ordre
  Ajout : out-of-distribution detection (marché inhabituel)

COUCHE 6 — EXÉCUTION (NT8 ATI port 36973)
  nt8_ati_client.py — à construire Phase G
  Killswitch réseau — network_monitor.py
  Confirmation d'ordre obligatoire avant tout Mode Auto

COUCHE 7 — APPRENTISSAGE (NOUVEAU — Loop 3)
  feedback_engine.py : analyse chaque trade fermé
  rule_tracker.db (SQLite) : performance par règle KB
  threshold_adapter.py : ajuste score_min selon win rate rolling
  regime_memory.db : quel régime est profitable pour quel actif
  Weekly report auto : quelles règles fonctionnent, lesquelles dégradent
```

---

## PARTIE 3 — LES INNOVATIONS CLÉS

### 3.1 Détection de Régime Marché (CRITIQUE — manquant total)

C'est la pièce maîtresse de tout ce qui suit. Sans régime, on applique les mêmes règles en marché tendanciel et en marché en range — et ça échoue.

**4 régimes à détecter :**

```python
RÉGIMES = {
    "TRENDING_BULL": {
        "critères": "ADX > 25 + prix > COG + VIX < 20 + DX stable",
        "stratégie": "suivre la tendance, stops larges, profits larges",
        "actifs_favoris": ["GC", "CL"],
        "seuil_signal": 6.5,  # moins strict en tendance claire
    },
    "TRENDING_BEAR": {
        "critères": "ADX > 25 + prix < COG + VIX en hausse",
        "stratégie": "short uniquement, stops serrés",
        "actifs_favoris": ["GC", "ZW"],
        "seuil_signal": 7.0,
    },
    "RANGING": {
        "critères": "ADX < 20 + prix oscille autour COG + VIX stable",
        "stratégie": "acheter support, vendre résistance, profits courts",
        "actifs_favoris": ["HG", "ZW"],
        "seuil_signal": 7.5,  # plus strict en range (faux signaux fréquents)
    },
    "VOLATILE": {
        "critères": "VIX > 25 ou ATR > 2σ historique ou corrélations cassées",
        "stratégie": "REDUCE_RISK ou NO_TRADE",
        "actifs_favoris": [],
        "seuil_signal": 9.0,  # quasi-bloquant
    },
}
```

**Implémentation :**
```python
# regime_detector.py
def detect_regime(nt8_data: dict, vix: float, correlations: dict) -> str:
    adx = nt8_data.get("GC", {}).get("adx", 0)
    cog = nt8_data.get("GC", {}).get("cog", 0)
    close = nt8_data.get("GC", {}).get("close", 0)
    atr_zscore = compute_atr_zscore(nt8_data)  # vs 252 jours historique
    
    if vix > 30 or atr_zscore > 2.0 or correlation_breakdown(correlations):
        return "VOLATILE"
    elif adx > 25 and close > cog:
        return "TRENDING_BULL"
    elif adx > 25 and close < cog:
        return "TRENDING_BEAR"
    else:
        return "RANGING"
```

**Impact direct :** le seuil de signal n'est plus fixe à 7.0 — il s'adapte au régime. En marché volatil, il monte à 9.0 (quasi-bloquant). En tendance claire, il descend à 6.5.

### 3.2 Dual-Claude Validation (innovation anti-biais de confirmation)

Le problème des systèmes IA : ils ont un biais de confirmation — ils trouvent des arguments pour ce qu'ils cherchent. Solution éprouvée dans la finance quantitative : le "devil's advocate".

**Implémentation :**
```python
# claude_brain.py — extension
def get_signal_dual(context, kb_rules) -> dict:
    # Appel 1 : Claude joue "Bull Advocate"
    prompt_bull = f"""
    Tu es un analyste HAUSSIER. Tu cherches des arguments pour ACHETER {context['asset']}.
    Analyse le contexte suivant et donne le score /10 de conviction haussière.
    {context}
    """
    
    # Appel 2 : Claude joue "Bear Advocate"  
    prompt_bear = f"""
    Tu es un analyste BAISSIER. Tu cherches des arguments pour VENDRE {context['asset']}.
    Analyse le contexte suivant et donne le score /10 de conviction baissière.
    {context}
    """
    
    score_bull = call_claude(prompt_bull, kb_rules)
    score_bear = call_claude(prompt_bear, kb_rules)
    
    # Décision :
    # Bull > 7.0 ET Bear < 4.0 → LONG fort
    # Bear > 7.0 ET Bull < 4.0 → SHORT fort
    # Bull et Bear tous les deux > 6.0 → AMBIGUOUS → WAIT
    # Bull et Bear tous les deux < 6.0 → NO_TRADE
    return resolve_dual_signal(score_bull, score_bear)
```

**Coût :** 2 appels Claude par signal au lieu de 1. Avec rate limit 30/jour, ça reste ~0.30$/jour max. La réduction des faux positifs compense largement.

### 3.3 Walk-Forward Optimization (standard or industrie — anti-overfitting)

Le backtesting simple est trompeur. On optimise sur les mêmes données qu'on teste → overfitting garanti.

La WFO est la solution standard dans les hedge funds :

```
Fenêtre IS (In-Sample) = 90 jours → on optimise les paramètres sur ces données
Fenêtre OOS (Out-of-Sample) = 30 jours → on teste les paramètres optimisés
On avance d'un mois et on répète.

IS: Jan-Mar → optimise → test Avr
IS: Fév-Avr → optimise → test Mai
IS: Mar-Mai → optimise → test Juin
...
```

**Paramètres à optimiser par WFO :**
- `score_min` (seuil signal) : testé de 6.0 à 8.5 par pas de 0.5
- Poids des 7 cercles dans le score total
- Durée du cooldown post-perte

**Critère d'arrêt :** si la performance OOS est < 70% de la performance IS → les paramètres overfit → ne pas les utiliser.

### 3.4 Kelly Criterion pour le Position Sizing (mathématiquement optimal)

Actuellement : `max_risque_trade = 0.02` (2% fixe). C'est sûr mais sous-optimal.

Le Critère de Kelly donne la taille optimale théorique :

```python
# Dans risk_manager.py
def kelly_fraction(win_rate: float, avg_win: float, avg_loss: float) -> float:
    """
    Fraction optimale à risquer par trade selon Kelly.
    win_rate : probabilité de gain (ex: 0.60 = 60%)
    avg_win  : gain moyen en R (ex: 1.5 pour 1.5R)
    avg_loss : perte moyenne en R (ex: 1.0 pour 1R)
    """
    if avg_loss == 0 or win_rate <= 0:
        return 0.0
    q = 1 - win_rate
    b = avg_win / avg_loss
    kelly = (win_rate * b - q) / b
    
    # Règle de sécurité : utiliser demi-Kelly (standard industrie)
    # Full Kelly est trop agressif et sensible aux erreurs d'estimation
    half_kelly = kelly / 2
    
    # Plancher et plafond absolus
    return max(0.005, min(half_kelly, 0.025))  # entre 0.5% et 2.5%

# Utilisation :
# Après 30 trades minimum en SQLite :
win_rate = db.compute_win_rate(last_n=50)
avg_win, avg_loss = db.compute_avg_rr(last_n=50)
fraction = kelly_fraction(win_rate, avg_win, avg_loss)
position_size = account_equity * fraction
```

**Important :** Kelly ne peut être calculé qu'après au moins 30 trades réels. Avant : utiliser 1% fixe (ultra-conservateur jusqu'à validation statistique).

### 3.5 Out-of-Distribution Detection (marché inhabituellement extrême)

Le système ne sait pas ce qu'il ne sait pas. Si le marché est dans un état qu'il n'a jamais vu, la KB ne s'applique pas — mais il continuera à générer des signaux.

Solution : détecter les états "hors distribution" avant l'analyse.

```python
# ood_detector.py
def is_out_of_distribution(current_state: dict, historical_db) -> dict:
    """
    Compare l'état actuel aux 252 derniers jours de trading.
    Si 3+ métriques dépassent 2.5σ → marché inhabituellement extrême.
    """
    metrics = {
        "vix_zscore":     zscore(current_state["vix"], historical_db["vix"]),
        "volume_zscore":  zscore(current_state["volume_gc"], historical_db["volume_gc"]),
        "atr_zscore":     zscore(current_state["atr"], historical_db["atr"]),
        "corr_deviation": correlation_deviation(current_state["corr_matrix"], 
                                                 historical_db["avg_corr_matrix"]),
        "spread_zscore":  zscore(current_state["spread"], historical_db["spread"]),
    }
    
    extreme_count = sum(1 for v in metrics.values() if abs(v) > 2.5)
    
    if extreme_count >= 3:
        return {
            "ood": True,
            "severity": "EXTREME",
            "action": "max_confiance_65_pct + bloquer_auto",
            "message": f"⚠️ Marché inhabituellement extrême ({extreme_count}/5 métriques > 2.5σ)"
        }
    elif extreme_count >= 2:
        return {"ood": True, "severity": "ELEVATED", "action": "reduire_taille_50pct"}
    else:
        return {"ood": False, "severity": "NORMAL"}
```

### 3.6 Ensemble de Signaux (3 générateurs en parallèle)

Concept éprouvé : un signal validé par 3 méthodes indépendantes est bien plus fiable qu'un signal d'une seule méthode.

```
Générateur A : Belkhayate COG (méthode principale)
               COG position + BGC + Timing + Pivots
               
Générateur B : Order Flow (ATAS data)
               Delta cumulatif + Big Trades + Absorption zones
               
Générateur C : Macro/COT (cycle hebdomadaire)
               COT net positions + DX tendance + VIX percentile 52w

Signal valide : 2/3 générateurs concordent en direction ET score ≥ seuil régime
Signal fort   : 3/3 générateurs concordent → autoriser taille maximale Kelly
Signal faible : 1/3 → NO_TRADE
```

Ce concept mappe directement sur la règle existante "3/4 trading + 2/3 confirmation" mais l'enrichit avec une logique d'ensemble côté génération du signal.

### 3.7 Analyse de Survie pour les Take-Profits (innovation)

La plupart des systèmes utilisent un R/R fixe (1:2, 1:3). Mais en réalité, chaque marché a un profil de durée de trade différent.

La courbe de Kaplan-Meier (analyse de survie, empruntée à la médecine) modélise la probabilité qu'un trade soit encore ouvert après X minutes.

```python
# trade_analyzer.py
def compute_optimal_tp(asset: str, db) -> dict:
    """
    Sur les 100 derniers trades gagnants sur cet actif :
    Quand ont-ils atteint leur maximum ?
    """
    # Kaplan-Meier simplifié
    durations = db.get_winning_trade_durations(asset, n=100)
    
    p50 = np.percentile(durations, 50)  # 50% des trades gagnants se terminent avant X min
    p80 = np.percentile(durations, 80)  # 80% se terminent avant Y min
    
    return {
        "tp_agressif_min": p50,   # TP rapide, taux réalisation élevé
        "tp_optimal_min":  p80,   # TP équilibré
        "message": f"Sur {asset}: 80% des trades gagnants durent < {p80:.0f} min"
    }
```

En pratique : si l'historique montre que 80% des trades GC gagnants se terminent en < 4H, alors un TP à 6H est trop loin — on le rate souvent.

---

## PARTIE 4 — LE MOTEUR D'AUTO-AMÉLIORATION

### 4.1 Le Flywheel (la boucle qui fait tout progresser)

```
SEMAINE 1-4 : Paper trading → collecter 30+ trades dans SQLite
                ↓
SEMAINE 5-6 : Analyse : win rate, règles performantes, régimes rentables
                ↓
SEMAINE 7-8 : Walk-Forward Validation sur données collectées
                ↓
SEMAINE 9-12: Paramètres recalibrés → paper trading avec nouveaux params
                ↓
MOIS 4+     : Mode Auto activation (si 6 conditions Phase K satisfaites)
                ↓
EN CONTINU  : Loop 3 — chaque trade fermé alimente la base
                ↓
SEMAINE N   : Performance review hebdomadaire automatique
                ↓ (recommence)
```

Plus le système trade, plus il apprend. Plus il apprend, plus ses décisions s'améliorent.

### 4.2 Base SQLite — Schéma Complet

```sql
-- 05-saas/db/schema.sql

-- Signaux générés
CREATE TABLE signals (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp       TEXT NOT NULL,
    asset           TEXT NOT NULL,           -- GC, HG, CL, ZW
    direction       TEXT NOT NULL,           -- LONG, SHORT
    score_total     REAL NOT NULL,           -- /10
    score_bull      REAL,                    -- Dual-Claude bull score
    score_bear      REAL,                    -- Dual-Claude bear score
    confidence_pct  INTEGER NOT NULL,        -- 0-100
    regime          TEXT NOT NULL,           -- TRENDING_BULL/BEAR, RANGING, VOLATILE
    rules_fired     TEXT,                    -- JSON array d'IDs règles KB
    circles_scores  TEXT,                    -- JSON {C1:x, C2:y, ...}
    vix             REAL,
    cot_bias        TEXT,                    -- BULL, BEAR, NEUTRAL
    ood_flag        INTEGER DEFAULT 0,       -- 1 si out-of-distribution
    mode            TEXT NOT NULL            -- MANUEL, AUTO
);

-- Trades exécutés (Manuel ou Auto)
CREATE TABLE trades (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_id       INTEGER REFERENCES signals(id),
    asset           TEXT NOT NULL,
    direction       TEXT NOT NULL,
    entry_price     REAL NOT NULL,
    entry_time      TEXT NOT NULL,
    exit_price      REAL,
    exit_time       TEXT,
    exit_reason     TEXT,   -- TP, SL, MANUAL_CLOSE, TIMEOUT, CIRCUIT_BREAKER
    pnl_usd         REAL,
    pnl_r           REAL,   -- P&L en R (multiples de risque initial)
    slippage_ticks  INTEGER DEFAULT 0,
    duration_min    INTEGER,
    regime_at_entry TEXT,
    regime_at_exit  TEXT
);

-- Performance par règle KB
CREATE TABLE rule_performance (
    rule_id         TEXT NOT NULL,
    rule_category   TEXT,              -- categorie dans la KB
    times_fired     INTEGER DEFAULT 0,
    wins            INTEGER DEFAULT 0,
    losses          INTEGER DEFAULT 0,
    avg_pnl_r       REAL,
    last_fired      TEXT,
    last_updated    TEXT,
    PRIMARY KEY (rule_id)
);

-- Mémoire des régimes
CREATE TABLE regime_memory (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    asset           TEXT NOT NULL,
    regime          TEXT NOT NULL,
    signal_count    INTEGER DEFAULT 0,
    win_count       INTEGER DEFAULT 0,
    avg_rr          REAL,
    avg_duration    REAL
);

-- Calibration des paramètres (historique WFO)
CREATE TABLE parameter_history (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    score_min       REAL,
    kelly_fraction  REAL,
    win_rate        REAL,
    sharpe_ratio    REAL,
    max_dd          REAL,
    note            TEXT
);
```

### 4.3 feedback_engine.py — Le Cerveau de l'Apprentissage

```python
# 05-saas/engine/feedback_engine.py
"""
Loop 3 — Analyse chaque trade fermé et met à jour la base d'apprentissage.
Appelé automatiquement à la fermeture de chaque trade.
"""
import os
from datetime import datetime
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def analyze_closed_trade(trade_id: int) -> dict:
    """Point d'entrée principal. Appelé après fermeture de trade."""
    db = connect_db()
    
    trade = db.get_trade(trade_id)
    signal = db.get_signal(trade["signal_id"])
    
    # 1. Mettre à jour les performances par règle
    rules_fired = signal.get("rules_fired", [])
    outcome = "win" if trade["pnl_r"] > 0 else "loss"
    for rule_id in rules_fired:
        update_rule_performance(db, rule_id, outcome, trade["pnl_r"])
    
    # 2. Mettre à jour la mémoire de régime
    update_regime_memory(db, signal["asset"], signal["regime"], outcome, trade["pnl_r"])
    
    # 3. Vérifier si recalibration nécessaire
    recal = check_recalibration_needed(db)
    if recal["needed"]:
        trigger_recalibration(db, recal["reason"])
    
    # 4. Alertes
    alerts = generate_alerts(db, trade)
    
    return {"status": "analyzed", "alerts": alerts, "recalibration": recal}

def check_recalibration_needed(db) -> dict:
    """
    Détermine si les paramètres doivent être ajustés.
    Déclenche recalibration si :
    - Win rate sur 30 derniers trades < 45% (urgence)
    - Win rate sur 50 derniers trades < 50% (routine)
    - Max drawdown rolling > 8% (urgence)
    """
    stats_30 = db.compute_stats(last_n=30)
    stats_50 = db.compute_stats(last_n=50)
    
    if stats_30.get("win_rate", 1.0) < 0.45:
        return {"needed": True, "reason": "WIN_RATE_CRITIQUE", "urgency": "HIGH"}
    if stats_50.get("win_rate", 1.0) < 0.50:
        return {"needed": True, "reason": "WIN_RATE_FAIBLE", "urgency": "MEDIUM"}
    if stats_30.get("max_dd", 0) > 0.08:
        return {"needed": True, "reason": "DRAWDOWN_CRITIQUE", "urgency": "HIGH"}
    
    return {"needed": False}

def generate_weekly_report(db) -> str:
    """Génère le rapport hebdomadaire automatique."""
    stats = db.compute_stats(last_n=None, days=7)
    
    # Top 5 règles qui fonctionnent
    top_rules = db.get_top_rules(n=5, metric="avg_pnl_r")
    
    # Bottom 5 règles à auditer
    bad_rules = db.get_bottom_rules(n=5, min_fires=5)
    
    # Régimes rentables cette semaine
    regime_stats = db.get_regime_stats(days=7)
    
    report = f"""
# RAPPORT HEBDOMADAIRE TRADEX-AI
Semaine du {datetime.now().strftime('%d/%m/%Y')}

## Résumé
- Signaux générés : {stats['signal_count']}
- Trades exécutés : {stats['trade_count']}
- Win rate : {stats['win_rate']:.1%}
- P&L total : {stats['total_pnl_r']:+.2f}R
- Max drawdown : {stats['max_dd']:.1%}

## Règles les plus performantes (TOP 5)
{format_rules(top_rules)}

## Règles à auditer (BOTTOM 5 — ≥ 5 déclenchements)
{format_rules(bad_rules)}

## Performance par régime
{format_regime_stats(regime_stats)}

## Recommandations automatiques
{generate_recommendations(stats, top_rules, bad_rules, regime_stats)}
"""
    return report
```

### 4.4 Threshold Adapter — Auto-calibration du Seuil

```python
# 05-saas/engine/threshold_adapter.py
"""
Ajuste score_min selon les performances réelles.
ATTENTION : ne jamais descendre sous 6.0 ni monter au-dessus de 9.0.
"""

SCORE_MIN_ABSOLU_BAS = 6.0
SCORE_MIN_ABSOLU_HAUT = 9.0
SCORE_MIN_DEFAUT = 7.0

def compute_adapted_threshold(db, regime: str) -> float:
    """
    Règle d'adaptation :
    - Si win_rate(50 trades) > 65% ET régime actuel profitable → baisser seuil de 0.2
    - Si win_rate(50 trades) < 50% → monter seuil de 0.3
    - Toujours appliquer plancher/plafond
    """
    stats = db.compute_stats(last_n=50)
    regime_stats = db.get_regime_performance(regime)
    
    current = db.get_current_threshold(regime)
    
    if stats.get("win_rate", 0) > 0.65 and regime_stats.get("profitable", False):
        new_threshold = current - 0.2
    elif stats.get("win_rate", 1.0) < 0.50:
        new_threshold = current + 0.3
    else:
        new_threshold = current  # Pas de changement
    
    # Appliquer les bornes absolues
    new_threshold = max(SCORE_MIN_ABSOLU_BAS, min(new_threshold, SCORE_MIN_ABSOLU_HAUT))
    
    if new_threshold != current:
        db.log_threshold_change(regime, current, new_threshold, stats)
    
    return new_threshold
```

---

## PARTIE 5 — PLAN DE VALIDATION ET TESTS

### 5.1 Les 4 niveaux de test (pyramide de confiance)

```
NIVEAU 4 — LIVE TRADING (Mode Auto)
          Jamais avant niveaux 1-2-3 validés
          ↑
NIVEAU 3 — SHADOW TRADING (signaux live, exécution manuelle)
          30 jours minimum, win rate > 55%
          ↑
NIVEAU 2 — PAPER TRADING (simulation complète)
          30 jours minimum, N ≥ 50 trades
          ↑
NIVEAU 1 — BACKTESTING (données historiques)
          Walk-Forward, 3 mois minimum, N ≥ 200 signaux
```

### 5.2 Tests Unitaires (30 tests minimum avant intégration)

| # | Module | Test | Critère de réussite |
|---|--------|------|---------------------|
| U01 | staleness_monitor | Fichier manquant | Retourne MISSING, pas d'exception |
| U02 | staleness_monitor | Fichier stale | Retourne STALE, système → BLOCKED |
| U03 | risk_manager | News Gate NFP | Bloque 30min avant, débloque après |
| U04 | risk_manager | VIX > 35 | Auto suspendu, Manuel autorisé |
| U05 | risk_manager | 2 pertes consécutives | Auto suspendu 15min minimum |
| U06 | circuit_breaker | Timeout 15s | Retry 2x puis fallback |
| U07 | data_reader | JSON corrompu | Retourne {} sans crash |
| U08 | signal_scorer | Score 5 cercles alignés | Score ≥ 7.0 attendu |
| U09 | signal_scorer | Zéro cercle aligné | Score ≤ 3.0 attendu |
| U10 | regime_detector | ADX > 25, prix > COG | TRENDING_BULL retourné |
| U11 | regime_detector | VIX > 30 | VOLATILE retourné |
| U12 | kelly_criterion | win_rate=0.60, RR=1.5 | Fraction entre 0.5-2.5% |
| U13 | ood_detector | VIX zscore > 3σ | OOD=True, severity=EXTREME |
| U14 | feedback_engine | Trade gagnant | rule_performance.wins += 1 |
| U15 | feedback_engine | 30 trades, WR < 45% | recalibration déclenché |
| U16 | threshold_adapter | WR 30j < 50% | score_min monte de 0.3 |
| U17 | threshold_adapter | Plafond absolu | Jamais > 9.0 |
| U18 | dual_claude | Bull > 7 ET Bear < 4 | Signal LONG retourné |
| U19 | dual_claude | Bull et Bear tous deux > 6 | AMBIGUOUS → WAIT |
| U20 | atomic_writer | Crash mid-write | Fichier original intact |
| U21 | news_gate | FOMC dans 25min | BLOCKED retourné |
| U22 | news_gate | FOMC dans 35min | NON bloqué (hors fenêtre) |
| U23 | correlation_check | 2 actifs corrélés > 0.8 | Second trade bloqué |
| U24 | slippage_estimator | Spread élevé | Trade annulé si slippage > 33% profit |
| U25 | risk_manager | Mode Auto défaut | is_auto_globally_blocked() = True |

### 5.3 Tests d'Intégration (scénarios complets)

**Scénario 1 — Signal valide en marché tendanciel**
```
Input  : GC trending, 3/4 actifs alignés, 2/3 confirmations, VIX=18, score=7.8
Attendu: Signal LONG GC, confidence 82%, position size Kelly, Telegram notif
```

**Scénario 2 — Blocage News Gate**
```
Input  : Signal score=8.2, NFP dans 22 minutes
Attendu: Signal BLOQUÉ, raison "NEWS_GATE_NFP", log SQLite, NO action
```

**Scénario 3 — Dégradation en cascade**
```
Input  : NT8 offline depuis 12s (> 10s seuil)
Attendu: ATAS_signals = STALE → système = BLOCKED → tout stop
```

**Scénario 4 — Marché out-of-distribution**
```
Input  : VIX=45 (3.2σ), Volume 2.8σ, ATR 3.1σ, Corr breakdown
Attendu: OOD=True, confiance max 65%, Mode Auto bloqué, alerte utilisateur
```

**Scénario 5 — Walk-Forward Validation**
```
IS: Janv-Mar 2024 → optimise score_min=7.2, kelly=1.8%
OOS: Avr 2024 → win rate OOS vs IS doit être > 70%
Si OOS < 70% IS → rejeter ces paramètres → garder défauts
```

### 5.4 Stress Tests Historiques (scénarios extrêmes)

Ces 8 scénarios doivent être rejoués sur données historiques réelles :

| # | Scénario | Période | Comportement attendu |
|---|----------|---------|----------------------|
| S1 | COVID crash | Mars 2020 | VOLATILE détecté → NO_TRADE ou REDUCE |
| S2 | Ukraine invasion | Fév 2022 | News gate + VOLATILE |
| S3 | FED pivot surprise | Nov 2022 | News gate FOMC + OOD si VIX spike |
| S4 | Or ATH | Mar 2024 | TRENDING_BULL → signaux LONG correctement générés |
| S5 | Or -8% en 1 jour | Oct 2023 | ATR zscore élevé → VOLATILE → stop |
| S6 | Corrélation GC/HG cassée | Données réelles | correlation_breakdown détecté |
| S7 | Flash crash CL | Avr 2020 | OOD + BLOCKED + zéro ordre envoyé |
| S8 | Blé spike geopolitique | Fév 2022 | News gate + VOLATILE → WAIT |

### 5.5 Critères Go/No-Go pour Mode Auto

Avant d'activer le Mode Auto, les 8 conditions suivantes doivent toutes être vraies :

| # | Condition | Mesure | Seuil |
|---|-----------|--------|-------|
| 1 | Win rate Paper Trading | SQLite analytics | ≥ 55% sur 50+ trades |
| 2 | Drawdown max | SQLite analytics | ≤ 5% du capital |
| 3 | Sharpe ratio | SQLite analytics | ≥ 1.0 |
| 4 | OOS/IS ratio WFO | walk_forward_validate() | ≥ 0.70 |
| 5 | NT8 ATI stable | 48h sans déconnexion | 0 perte de connexion |
| 6 | Rithmic demo 48H | Test execution | 0 ordre fantôme |
| 7 | Tous stress tests passés | 8/8 scénarios | Comportement correct 8/8 |
| 8 | Validation explicite Abdelkrim | Bouton + mot de passe | Log SQLite avec timestamp |

---

## PARTIE 6 — OBSTACLES ANTICIPÉS ET MESURES CORRECTIVES

### 6.1 Obstacles Techniques

**OBS-01 : Données NT8 corrompues ou vides**
- Cause : NT8 crash, écriture partielle, accès concurrent
- Symptôme : `data_reader` retourne {} pour un actif critique
- Correction : staleness_monitor détecte (MISSING) → BLOCKED automatique. NT8 C# doit écrire atomiquement (temp → rename).
- Mesure préventive : validator JSON strict sur chaque lecture

**OBS-02 : Claude API rate limit ou timeout**
- Cause : trop de signaux en même temps (corrélation forte entre actifs)
- Symptôme : circuit_breaker CB_CLAUDE s'ouvre
- Correction : file d'attente prioritaire (score desc). Si queue > 5 → clear, retourner WAIT pour tous. Ne jamais forcer un appel.
- Mesure préventive : max 1 analyse/10s déjà en place. Ajouter max 30/jour avec compteur SQLite.

**OBS-03 : Overfitting du Walk-Forward**
- Cause : trop de paramètres optimisés, fenêtre IS trop courte
- Symptôme : Performance OOS << IS
- Correction : si OOS/IS < 0.70 → rejet automatique, garder paramètres précédents
- Mesure préventive : principe de parcimonie — optimiser max 3 paramètres à la fois

**OBS-04 : Drift de la KB (règles Belkhayate obsolètes)**
- Cause : le marché évolue, certaines règles de 2018 ne fonctionnent plus
- Symptôme : rule_performance.avg_pnl_r < 0 sur > 20 déclenchements
- Correction : flag automatique dans weekly report. Human review par Abdelkrim. Si confirmé → poids à zéro dans le scoring.
- Mesure préventive : date-weighting des règles (règles récentes > règles anciennes)

**OBS-05 : Corrélation breakdown inattendue**
- Cause : événement géopolitique, crise financière, "black swan"
- Symptôme : corrélation GC/HG passe de 0.75 à -0.20 en 48H
- Correction : correlation_breakdown detector → VOLATILE régime → score_min = 9.0
- Mesure préventive : recalcul corrélations toutes les 4H, pas hebdomadaire

**OBS-06 : Double exposure sur actifs corrélés**
- Cause : GC signal + HG signal simultanément (corrélation > 0.7)
- Symptôme : exposition réelle 2x plus grande que prévue
- Correction : portfolio_heat_check() avant chaque ordre. Si corrélation > 0.7 → bloquer second trade.
- Règle : deux actifs avec corrélation > 0.7 = 1 seul trade autorisé à la fois

**OBS-07 : Exécution NT8 ATI échoue silencieusement**
- Cause : ordre envoyé au port 36973 mais NT8 ne confirme pas
- Symptôme : le système croit avoir exécuté mais NT8 n'a rien fait
- Correction : confirmation obligatoire après chaque ordre (ACK NT8). Sans ACK 5s → circuit breaker → alerte.
- Mesure préventive : jamais supposer qu'un ordre est passé — toujours vérifier la position réelle

**OBS-08 : Biais d'estimation Kelly**
- Cause : 30 trades insuffisants pour estimer win rate fiable
- Symptôme : Kelly calcule fraction erronée (trop agressive)
- Correction : si N < 50 trades → utiliser 1% fixe (ultra-conservateur). Bootstrapping CI sur win_rate : si IC 95% inclut 0.5 → Kelly non fiable, garder 1%.
- Formule : `kelly_valide = (n_trades >= 50 AND CI_95_lower > 0.45)`

### 6.2 Obstacles Méthodologiques

**OBS-09 : Surcharge de signaux**
- Cause : marchés très actifs, trop de signaux simultanés
- Correction : max 3 signaux/jour/actif, max 5 signaux/jour total. Garder uniquement le meilleur score.

**OBS-10 : Régression psychologique algorithmique**
- Traduction : après 3 wins consécutifs, le système peut paraître "trop confiant" (seuil trop bas). Après 3 losses, trop conservateur.
- Correction : anti-recency bias dans le threshold_adapter. Utiliser rolling window de 50 trades, pas les 5 derniers.

**OBS-11 : Backtesting look-ahead bias**
- Cause : utiliser inconsciemment des données futures dans le backtest
- Correction : strict timestamp ordering. Jamais utiliser une bougie fermée dans la même seconde. Simuler latence réaliste (50ms NT8 + 2s Python + 3s Claude = 5s total).

### 6.3 Obstacles Opérationnels

**OBS-12 : Windows crash, redémarrage machine**
- Correction : orchestrateur.py se relance via Task Scheduler Windows. État persisté en SQLite (pas en mémoire vive). Au redémarrage : lire dernier état SQLite, pas supposer état clean.

**OBS-13 : Rithmic disconnect pendant un trade ouvert**
- Correction : si connexion perdue ET trade ouvert → ordre de clôture en attente dans queue. Dès reconnexion → envoyer clôture. Log + alerte.

**OBS-14 : Coût API dépasse budget**
- Correction : compteur d'appels Claude dans SQLite. Alerte à 80% du budget. Hard stop à 100%. Fallback local obligatoire.

---

## PARTIE 7 — ROADMAP PRIORISÉE VERS LE SYSTÈME "PRESQUE PARFAIT"

### Horizon 1 — Fondations (Phase B-C en cours, 1-2 mois)

1. Compléter KB avec transcripts Gemini (batch en cours)
2. Ajouter TICK_SPECS manquantes (HG/CL/ZW) dans settings.py
3. Créer schema SQLite de base (signals + trades)
4. Add-on NinjaScript C# (export JSON par actif)
5. Orchestrateur `main.py` (point d'entrée unique)

### Horizon 2 — Intelligence (Phase D-E, 2-3 mois)

6. regime_detector.py (4 régimes, ADX + ATR zscore + VIX)
7. signal_scorer.py avec poids adaptatifs par régime
8. feedback_engine.py (Loop 3 — analyse post-trade)
9. rule_tracker.db (performance par règle KB)
10. Walk-Forward Validation (Phase E)

### Horizon 3 — Exécution (Phase F-G, 3-4 mois)

11. Kelly position sizing (avec garde-fou N < 50 → 1%)
12. Portfolio heat check (no double exposure)
13. nt8_ati_client.py (Phase G)
14. Slippage estimator
15. OOD detector

### Horizon 4 — Auto-amélioration (Phase H-K, 4-6 mois)

16. Dual-Claude validation
17. Threshold adapter (auto-calibration score_min)
18. Weekly report automatique
19. Dashboard React (maquettes existantes)
20. Paper trading 30 jours obligatoire
21. Mode Auto activation (6 conditions + validation Abdelkrim)

### Horizon 5 — Excellence (Post Phase K, 6+ mois)

22. Kaplan-Meier TP optimization
23. Ensemble de 3 générateurs de signaux
24. Synthetic data augmentation (Monte Carlo)
25. Adversarial testing automatique (8 scénarios historiques)
26. Walk-Forward mensuel automatique
27. Rapport de performance trimestriel

---

## PARTIE 8 — DÉFINITION DE "PRESQUE PARFAIT"

Un système de trading "presque parfait" n'est pas un système qui gagne toujours. C'est un système qui :

| Critère | Mesure | Seuil cible |
|---------|--------|-------------|
| Edge statistique | Win rate rolling 100 trades | ≥ 55% |
| Protection capital | Max drawdown annuel | ≤ 10% |
| Qualité des gains | Sharpe ratio annualisé | ≥ 1.5 |
| Robustesse | Performance OOS / IS (WFO) | ≥ 0.70 |
| Adaptabilité | Fonctionne dans 3 régimes | Trending + Ranging + Volatile adapté |
| Dégradation gracieuse | Comportement en régime VOLATILE | REDUCE ou WAIT (jamais forcer) |
| Auto-amélioration | Score_min delta sur 3 mois | Calibré sur données réelles |
| Fiabilité système | Uptime / disponibilité | ≥ 99% pendant les heures de marché |
| Discipline | Ratio signaux filtrés | ≥ 80% des signaux bruts filtrés (PAS DE TRADE > MAUVAIS TRADE) |
| Apprentissage | KB enrichie / trimestre | ≥ 10 nouvelles règles validées |

---

## CONCLUSION

L'architecture décrite dans ce document n'est pas révolutionnaire. Elle s'appuie sur des techniques éprouvées dans la finance quantitative (Walk-Forward, Kelly, Kaplan-Meier, régimes de marché) et les intègre dans la structure spécifique de TRADEX-AI (méthode Belkhayate, 7 cercles, grille /10, NT8 + ATAS).

**La vraie innovation de TRADEX-AI est la combinaison unique de :**
- La méthode Belkhayate (edge méthodologique + psychologique)
- Claude API avec KB ~1300 règles (edge analytique)
- La Loop 3 feedback post-trade (edge adaptatif)
- Les garde-fous robustes (protection du capital)

Le chemin vers "presque parfait" est long (6-12 mois de développement + paper trading + Mode Auto progressif). Mais chaque phase apporte de la valeur immédiate. Et surtout : **la discipline de ne pas trader quand le système n'est pas confiant est elle-même une forme de perfection.**

> "The best trade is often no trade." — principe fondamental de TRADEX-AI

---

*Rapport généré le 24/06/2026 · Session S24 · À archiver dans 00-pilotage\_context\ après validation*
*Prochaine mise à jour : après Phase E (Signal Scorer + WFO) — mesures réelles disponibles*
