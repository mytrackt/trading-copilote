# APPORTS GUIDE EXTERNE — Segments retenus pour TRADEX-AI

> Source : `Guide Stratégique Automatisation du Trading Boursier avec Claude AI.pdf` (40 pages).
> Filtre appliqué : seuls les concepts compatibles avec la méthode Belkhayate et l'architecture
> NinjaTrader 8 ATI sont retenus. Tout ce qui touche Alpaca, Yahoo Finance, Streamlit,
> options Wheel, Copy Trading Congrès, Claude Desktop, actions US, Pine Script et NinjaScript
> est volontairement écarté.

**Date d'extraction** : 2026-05-03
**Méthode prioritaire** : Belkhayate (intouchable). Tous les apports ci-dessous sont des
**filtres complémentaires en aval** des 7 cercles, jamais en remplacement.
**Actifs cibles** : GC / HG / CL / ZW (trading) + DX / ES / VX (confirmation).
**Modules cibles** : `code\engine\signal_scorer.py` (à créer), `code\engine\correlations.py`,
`code\engine\risk_manager.py`, `code\engine\claude_brain.py`.

---

## 1. Walk-Forward Backtesting → `code\engine\signal_scorer.py` (à créer)

### Concept extrait du PDF (pages 6, 8, 10)

> « Le modèle s'entraîne sur 252 jours (une année boursière) pour s'évaluer sur les 6 mois
> suivants de manière aveugle. Cette approche simule la réalité opérationnelle où le bot doit
> s'adapter à des données inédites. »
>
> « Trois benchmarks obligatoires : Buy & Hold, moyenne mobile simple SMA 200, stratégie à
> entrées aléatoires. »
>
> « Simulations de Monte Carlo : 10 000 variations en mélangeant l'ordre des trades. Métrique
> institutionnelle : Worst 5% Drawdown — pire scénario probable dans 95% des cas. »
>
> « Analyse de sensibilité : si une stratégie performe à 20 jours de look-back mais s'effondre
> à 18 ou 22 jours, elle est fragile et probablement victime d'overfitting. Une stratégie
> robuste doit présenter un plateau de performance stable. »
>
> « Look-ahead bias : assurez-vous que le modèle n'utilise jamais d'informations qui
> n'étaient pas disponibles au moment de la transaction simulée. »

### Adaptation à TRADEX-AI (méthode Belkhayate)

- Fenêtres roulantes : entraînement = 252 jours boursiers, test aveugle = 126 jours (6 mois).
- Appliqué au **score 7 cercles** (voir `_calculate_fallback_score` dans
  `claude_brain.py:82` et seuil `score_min_claude = 17` dans `settings.py:94`).
- Benchmarks à comparer pour valider que le score 7 cercles bat :
  1. Buy & Hold sur GC (or = baseline naturel)
  2. SMA 200 sur GC, HG, CL, ZW
  3. Entrées aléatoires (signal random respectant la fréquence moyenne)
- Stress test : injecter krachs artificiels de 10–15 % dans les flux historiques GC/CL.

### Spec d'implémentation `signal_scorer.py`

```python
def walk_forward_validate(
    score_function,           # ex: _calculate_fallback_score
    historical_data: dict,    # OHLC GC/HG/CL/ZW + DX/ES/VX
    train_days: int = 252,
    test_days: int = 126,
    step_days: int = 21,      # avance fenêtre tous les mois
) -> dict:
    """
    Retourne :
    {
        "windows_tested":   N,
        "median_return":    float,
        "worst_5_drawdown": float,
        "vs_buy_hold":      float (delta),
        "vs_sma200":        float (delta),
        "vs_random":        float (delta),
        "stable":           bool,   # plateau ±2 jours look-back tenu
    }
    """

def monte_carlo_stress(
    trades_log: list,
    n_simulations: int = 10000,
) -> dict:
    """
    Mélange l'ordre des trades, ré-échantillonne le timing.
    Retourne worst_5_drawdown, median_drawdown, max_drawdown.
    """
```

### Garde anti-look-ahead (non-négociable)

- À chaque pas de la fenêtre, n'utiliser que `data[:t]` (jamais `data[:]`).
- Aucune normalisation/feature engineering qui touche le futur (z-scores calculés sur
  fenêtre passée uniquement).
- Test unitaire : `assert score_at_t == score_at_t_recomputed_after_more_data` doit casser
  si on a fuité le futur.

---

## 2. Hysteresis + Cool-Down → `code\engine\signal_scorer.py`

### Concept extrait du PDF (pages 9, 13, 14)

> « Filtre de stabilité : un régime doit être détecté pendant au moins trois barres
> consécutives avant toute action. »
>
> « Si le système détecte plus de quatre changements de régime sur les 20 dernières barres,
> il génère une alerte d'incertitude qui réduit mécaniquement l'exposition du bot. »
>
> « Signal Hysteresis (Confirmation Lag) : Utilisation de jeux de temps pondérés.
> Le système ne rentre pas immédiatement lors d'un changement de régime pour éviter le
> choppy noise (bruit de transition). »
>
> « Cool Down : Période de gel de 48 heures après une sortie de position. »

### Valeurs numériques retenues

| Paramètre | Valeur PDF | Adaptation TRADEX-AI |
|-----------|-----------|----------------------|
| Confirmation barres consécutives | 3 | **3 barres** (timeframe primaire NT8) |
| Seuil ping-pong | > 4 changements / 20 barres | **identique** |
| Cool-down post-sortie | 48 h | **48 h** par défaut, **24 h** si gain > 2R |
| Réduction exposition si alerte | non chiffré | **−50 %** (aligné `RÈGLES_RISQUE['post_win_size_reduction']`) |

> ⚠️ La valeur 48 h vient du PDF qui parle de marchés crypto en 24/7. Pour les futures
> CME (GC/HG/CL) qui ont un break quotidien à 17h ET et un week-end fermé, 48 h se traduit
> par **2 sessions complètes**. Pour ZW (CBOT, plages plus restreintes), idem.

### Spec d'implémentation `signal_scorer.py`

```python
class HysteresisFilter:
    """
    Filtre anti-ping-pong sur les transitions de régime.
    À appeler AVANT que le score 7 cercles ne déclenche un signal trade.
    """

    def __init__(
        self,
        min_consecutive_bars: int = 3,
        max_transitions_window: int = 20,
        max_transitions_allowed: int = 4,
    ):
        self.history = []     # liste de régimes par barre

    def confirm(self, current_regime: str) -> tuple[bool, str]:
        """
        Retourne (autorisé, raison).
        - autorisé = False si < 3 barres consécutives identiques
        - autorisé = False si > 4 transitions sur 20 dernières barres
        """

class CoolDownGuard:
    """
    Bloque toute nouvelle entrée pendant N heures après une sortie.
    Lecture/écriture via atomic_writer pour persistance.
    """

    def __init__(self, default_hours: int = 48, fast_track_hours: int = 24):
        ...

    def can_enter(self, actif: str, last_trade_pnl_R: float) -> bool:
        """
        Si dernier trade > 2R → cool-down réduit à 24h
        Sinon → 48h obligatoires
        """
```

### Intégration dans le flux existant

- Insertion : entre `get_signal()` (`claude_brain.py:111`) et `can_send_auto_order()`
  (`risk_manager.py:70`).
- Si `HysteresisFilter.confirm()` retourne False → forcer `signal = "ATTENDRE"` même si
  Claude renvoie ACHETER/VENDRE.
- Si `CoolDownGuard.can_enter()` retourne False → bloquer ouverture nouvelle position
  sur cet actif (les sorties restent autorisées).

---

## 3. Régimes de Marché → `code\engine\correlations.py` + `code\engine\signal_scorer.py`

### Concept extrait du PDF (pages 5, 7, 9, 14)

> « La priorité stratégique est la classification de l'environnement de marché. La détection
> de régime permet de quantifier la structure du marché afin d'accorder ou non une
> permission de trader à certains modèles. »
>
> « Régimes labellisés : Crash, Bear, Neutral, Bull, Euphoria. »
>
> « Détecteur de Rupture de Corrélation : Surveillance des paires historiques.
> Comparaison de la corrélation roulante sur 20 jours vs 60 jours. Une divergence brusque
> signale un changement de structure de marché. »
>
> « Sortie Immédiate : Clôture dès que le système détecte une transition vers un régime Bear
> ou Crash. »

### Adaptation à TRADEX-AI (alignée 7 cercles + actifs verrouillés)

> ⚠️ Le PDF utilise un HMM (Hidden Markov Model). **TRADEX-AI ne reprend QUE le concept de
> régime**, pas le HMM lui-même. La classification se fait par règles déterministes sur
> GC/HG/CL/ZW + DX/ES/VX, alignée sur le Cercle 7 (Corrélations) et les pivots Belkhayate
> (Cercle 1).

**Mapping 4 régimes (pas 5 — Euphoria fusionné dans Bull pour les futures matières premières)** :

| Régime | Critères (déterministes) | Conséquence trading |
|--------|-------------------------|---------------------|
| **Bull** | ES > SMA200 ET VIX < 20 ET GC trend ↑ ET corrélations stables | Score 7 cercles requis ≥ **17/21** (norme) |
| **Neutral** | ES dans ±5 % SMA200 ET VIX entre 20 et 30 | Score requis **18/21** + cool-down ×1.5 |
| **Bear** | ES < SMA200 ET VIX entre 25 et 35 ET corrélations instables | Score requis **20/21**, taille réduite −50 %, Mode Auto interdit |
| **Crash** | VIX > 35 OU DD compte > 2 % jour OU > 4 corrélations instables | **0 trade** — sortie immédiate des positions ouvertes |

### Évolution proposée pour `correlations.py`

`calculate_live_correlations()` calcule actuellement 30 j vs 7 j (`correlations.py:51-55`).
Le PDF préconise **20 j vs 60 j**. Recommandation : ajouter une **seconde mesure**
(ne pas remplacer l'existante car elle sert à `check_portfolio_correlation`).

```python
def detect_correlation_break(
    historical_data: dict,
    short_window_days: int = 20,
    long_window_days: int = 60,
    threshold: float = 0.30,
) -> dict:
    """
    Détecte les ruptures de corrélation 20j vs 60j.
    Retourne pour chaque paire CORRELATION_PAIRS :
        {
            "corr_20j":   float,
            "corr_60j":   float,
            "delta":      float,
            "broken":     bool,    # True si abs(delta) > 0.30
        }
    Une rupture sur >= 2 paires GC/HG/CL/ZW vs DX/ES = signal de changement
    de régime → forcer re-classification immédiate.
    """

def detect_market_regime(
    historical_data: dict,
    vix: float,
    dd_today: float,
    correlation_breaks: dict,
) -> str:
    """
    Retourne 'BULL' | 'NEUTRAL' | 'BEAR' | 'CRASH' selon la table ci-dessus.
    Source de vérité unique pour signal_scorer.py et risk_manager.py.
    """
```

### Intégration dans `signal_scorer.py`

- Avant tout calcul de score, appeler `detect_market_regime()` → applique le seuil de score
  approprié et la réduction de taille.
- Si `regime == "CRASH"` → `signal = "ATTENDRE"` immédiatement, sans appel Claude API
  (économie tokens + sécurité).

---

## 4. Risk Management enrichi → `code\engine\risk_manager.py`

### Concept extrait du PDF (pages 9, 10)

> « Régime → Levier Maximum : Bull 1.0x, Neutral 1.0x, Bear/Volatile < 0.5x, Crash 0x. »
>
> « Score de confiance : si la probabilité statistique du régime actuel est faible,
> la taille des positions est automatiquement réduite. »
>
> « Hiérarchie de disjoncteurs (Circuit Breakers) :
> - Perte quotidienne 2 % → réduction immédiate de 50 % de la taille des positions
> - Perte quotidienne 3 % → fermeture totale et arrêt de l'activité pour la journée
> - Perte hebdomadaire 5 % → redimensionnement forcé des limites de risque
> - Drawdown 10 % depuis le sommet → arrêt définitif du bot et activation du Mandatory
>   Lock File. Le bot écrit un fichier de verrouillage et refuse de redémarrer. Le trader
>   doit procéder à une analyse manuelle et supprimer physiquement ce fichier. »
>
> « Au niveau de la position, le risque est limité à 1 % par transaction, avec une
> vérification systématique de la corrélation pour éviter toute surexposition sectorielle. »

### Audit de l'existant `risk_manager.py`

| Règle PDF | Présent dans `risk_manager.py` ? | Action |
|-----------|----------------------------------|--------|
| Risque max 1 % par trade | `max_risque_trade: 0.02` (2 %) | À discuter — passer à 1 % en mode Bear |
| Réduction 50 % si DD jour 2 % | absent | **À ajouter** (palier intermédiaire) |
| Stop jour si DD 3 % | `drawdown_stop_jour: 0.03` ✅ | OK |
| Redim si DD semaine 5 % | absent | **À ajouter** |
| Mandatory Lock File à 10 % | absent | **À ajouter** |
| Levier par régime | absent | **À ajouter** |
| Vérif corrélation pré-trade | `check_portfolio_correlation` (`correlations.py:75`) ✅ | OK |
| Sortie immédiate Bear/Crash | absent | **À ajouter** |
| Score confiance → réduction taille | partiel (`get_confiance_min`) | **Étendre** |

### Spec ajouts `risk_manager.py`

```python
LEVIER_PAR_REGIME = {
    "BULL":    1.00,
    "NEUTRAL": 1.00,
    "BEAR":    0.50,    # taille divisée par 2
    "CRASH":   0.00,    # aucun nouveau trade
}

PALIERS_DD_JOUR = {
    0.02: "REDUCE_50",       # -50% taille des positions ouvertes
    0.03: "STOP_DAY",        # arrêt complet jour
}

PALIERS_DD_SEMAINE = {
    0.05: "RESIZE_LIMITS",   # division par 2 de tous les seuils
}

PALIERS_DD_TOTAL = {
    0.10: "MANDATORY_LOCK",  # fichier .lock à supprimer manuellement
}


def adjust_position_size(
    base_contracts: int,
    confiance: int,           # 0-100, sortie Claude
    regime: str,              # BULL | NEUTRAL | BEAR | CRASH
    dd_today: float,
) -> int:
    """
    Applique successivement :
    1. Levier par régime → base_contracts × LEVIER_PAR_REGIME[regime]
    2. Score confiance < 75% → réduction linéaire (taille × confiance/100)
    3. Si DD jour > 2% → ×0.5
    Retourne le nb final de contrats (entier, jamais < 0).
    """


def check_drawdown_breakers(
    dd_today: float,
    dd_week: float,
    dd_total_from_peak: float,
) -> dict:
    """
    Retourne :
    {
        "action":      "OK" | "REDUCE_50" | "STOP_DAY" | "RESIZE_LIMITS"
                       | "MANDATORY_LOCK",
        "lock_file":   chemin si MANDATORY_LOCK,
        "raison":      message lisible,
    }
    """


def write_mandatory_lock(reason: str, dd_value: float) -> str:
    """
    Crée C:\\trading-copilote\\data\\TRADING_LOCKED.lock via atomic_writer.
    Le fichier contient horodatage + raison + DD atteint.
    Retourne le chemin du fichier.
    """


def is_trading_locked() -> bool:
    """
    Vérifie l'existence de TRADING_LOCKED.lock.
    Tout module qui veut envoyer un ordre doit appeler cette fonction
    en premier — retour True bloque toute action.
    """


def force_exit_on_regime_change(
    old_regime: str,
    new_regime: str,
    open_positions: list,
) -> list:
    """
    Si transition vers BEAR ou CRASH → retourne la liste des ordres
    de sortie à envoyer immédiatement via NT8 ATI (port 36973).
    """
```

### Cohérence avec décisions verrouillées

- `RÈGLES_RISQUE['drawdown_stop_jour'] = 0.03` ✅ aligné PDF.
- `RISK['vix_extreme'] = 35` (`settings.py:84`) → utilisé pour passer en régime CRASH.
- `confiance_max_fallback = 65` (`settings.py:97`) → en mode Bear ET fallback,
  refuser tout signal (double sécurité).

---

## 5. Prompt Engineering → `code\engine\claude_brain.py`

### Concept extrait du PDF (pages 5, 13)

> « Logic de Prompting : le prompt doit suivre une hiérarchie logique stricte :
> 1. Data Source
> 2. Feature Engineering
> 3. Modélisation
> 4. Précision Algorithmique
> 5. UI Layout »
>
> « Master Prompt pour l'Implémentation :
> Build a professional regime-based trading application.
> Core Engine: [...]
> Features: [...]
> Auto-Labeling: [...]
> Structure: [...]
> Constraint: Implement Signal Hysteresis to prevent over-trading. »
>
> « Pour initier une position longue dans un régime Bull Run, 7 des 8 indicateurs suivants
> doivent être alignés. »

### Audit de l'existant `claude_brain.py`

`claude_brain.py:50-79` (`call_claude_kb`) utilise déjà :
- ✅ Prompt caching `cache_control: persistent` sur la KB (économies ~90 % tokens)
- ✅ `model = "claude-sonnet-4-6"` (verrouillé)
- ✅ `max_tokens = 1000`
- ✅ Rate limiting `time.sleep(1.5)`
- ✅ Circuit breaker via `CB_CLAUDE`
- ✅ Parsing JSON sécurisé (`_parse_claude_json`)

Manque : **structure du `god_mode_prompt`** elle-même (importée de `prompt_builder` qui
n'existe pas encore — voir `claude_brain.py:129`).

### Structure de prompt recommandée pour `prompt_builder.py` (à créer)

Adapter la hiérarchie PDF au contexte TRADEX-AI :

```
1. CONTEXTE MARCHÉ
   - Actif analysé : {actif} (GC | HG | CL | ZW)
   - Timeframe primaire : {timeframe}
   - Timestamp : {iso}
   - Régime détecté : {BULL | NEUTRAL | BEAR | CRASH}

2. DONNÉES 7 CERCLES (snapshot)
   - C1 Prix Belkhayate : BGC={...}, Direction={...}, Énergie={...}, Pivots={...}
   - C2 Order Flow ATAS : Delta={...}, Big Trades={...}, Footprint={...}
   - C3 Institutionnels : COT={...}, OI={...}
   - C4 Macro : DX={...}, prochains événements={...}
   - C5 Sentiment : VIX={...}, Put/Call={...}
   - C6 Géopolitique : alertes News={...}
   - C7 Corrélations : breaks={...}, instables={...}

3. CONTRAINTES NON NÉGOCIABLES (rappel à Claude)
   - Méthode Belkhayate exclusivement (KB en cache)
   - Règle d'entrée : 3/4 actifs trading + 2/3 confirmation alignés
   - Score signal valide : >= 17/21
   - Hysteresis : pas d'entrée si transition régime < 3 barres
   - Cool-down : 48h après sortie de position
   - Mode Auto interdit si confiance < 75% ou régime BEAR/CRASH

4. SCHÉMA DE SORTIE STRICT (JSON)
   {
     "signal":             "ACHETER" | "VENDRE" | "ATTENDRE",
     "confiance":          0-100,
     "raison":             "...",  // <= 200 caractères
     "taille_contrats":    int,
     "stop_loss_pivot":    float,
     "take_profit_1":      float,
     "take_profit_2":      float,
     "mode_auto_autorise": bool,
     "cercles_alignes":    int,    // 0-7
     "score_total":        int,    // 0-21
   }

5. PRÉCISION ALGORITHMIQUE
   - Utiliser uniquement les chiffres du contexte ci-dessus.
   - Aucune extrapolation. Aucune valeur inventée.
   - Si données manquantes ou staleness détectée → signal = "ATTENDRE".
```

### Spec implémentation `prompt_builder.py`

```python
def build_god_mode_prompt(context: dict) -> str:
    """
    Construit le prompt utilisateur (le system = KB est déjà en cache).
    Toutes les contraintes Belkhayate sont rappelées en section 3.
    Le schéma JSON strict est imposé en section 4 pour parsing fiable.
    """
```

### Bénéfice mesurable

- Sortie déterministe (schéma JSON strict) → `_parse_claude_json` ne casse plus.
- Champs obligatoires explicites → `result.setdefault(...)` (`claude_brain.py:133-137`)
  devient redondance défensive, plus correctif principal.
- Économie tokens : tout le contexte 7 cercles tient en < 800 tokens (vs KB en cache).

---

## 6. Filtres Anti-Bruit → `code\engine\signal_scorer.py`

### Concept extrait du PDF (pages 6, 13, 14)

> « Filtres de stabilité : ces filtres évitent le ping-pong entre deux régimes lors de
> phases de transition incertaines, stabilisant ainsi les signaux de trading. »
>
> « Confirmation Lag : le système ne rentre pas immédiatement lors d'un changement de
> régime pour éviter le choppy noise. »
>
> « Plateau de performance stable : si une stratégie performe à 20 jours de look-back mais
> s'effondre à 18 ou 22 jours, elle est fragile. »

### Règles + valeurs recommandées

| Filtre | Règle | Valeur |
|--------|-------|--------|
| Lag confirmation entrée | N barres consécutives même direction avant entrée | **3 barres** |
| Lag confirmation sortie | M barres consécutives signal opposé avant sortie | **2 barres** |
| Plateau look-back | Score reste stable ±1 sur look-back ±2 jours | **stable obligatoire** |
| Anti-flip-flop intra-séance | Pas plus de **2 inversions de signal / heure** sur même actif | hard cap |
| Filtre staleness | Tout cercle avec data > seuil (`STALENESS` settings.py:105) | exclu du score |
| Filtre VIX-spike | Si ΔVIX > +15 % en < 5 min → ATTENDRE forcé | proxy crash |

### Spec d'implémentation (consolidée avec section 2)

```python
class AntiNoiseFilter:
    """
    Couche finale entre score 7 cercles et émission du signal trade.
    À appeler APRÈS HysteresisFilter et CoolDownGuard.
    """

    def __init__(
        self,
        entry_lag_bars: int = 3,
        exit_lag_bars: int = 2,
        max_flips_per_hour: int = 2,
        vix_spike_threshold: float = 0.15,  # +15% en 5min
    ):
        ...

    def validate_entry(self, signal_history: list, current_signal: str) -> bool:
        """N dernières barres doivent confirmer la même direction."""

    def validate_exit(self, signal_history: list, current_signal: str) -> bool:
        """M dernières barres doivent confirmer le retournement."""

    def check_flip_flop(self, signal_history_1h: list) -> bool:
        """Retourne False si > 2 changements direction sur 1h."""

    def check_vix_spike(self, vix_history_5min: list) -> bool:
        """Retourne False si ΔVIX > +15% en 5 minutes."""

    def passes(self, context: dict) -> tuple[bool, str]:
        """Retourne (True, '') si tous les filtres passent, sinon (False, raison)."""


def stability_check_lookback(
    score_function,
    historical_data: dict,
    base_lookback: int,
    window: int = 2,        # ±2 jours
    tolerance: float = 0.10,  # 10% écart toléré
) -> bool:
    """
    Vérifie qu'aux look-backs base ±1, base ±2, le score reste dans ±10%.
    Si NON → la stratégie est fragile, marquer le signal comme suspect.
    """
```

### Intégration finale (chaîne complète)

```
NIVEAU 1 (Python, 0$)
  staleness_monitor.is_fresh()
  → KO : ATTENDRE
  → OK :
    detect_market_regime()
    → CRASH : ATTENDRE forcé, sortie positions
    → autres : continue

NIVEAU 2 (Python, 0$)
  HysteresisFilter.confirm()
  → KO : ATTENDRE
  → OK :
    CoolDownGuard.can_enter()
    → KO : ATTENDRE
    → OK :
      news_gate + DD + corrélations
      → KO : ATTENDRE
      → OK : continue

NIVEAU 3 (Claude API, ~0.01$)
  call_claude_kb(KB_cache, build_god_mode_prompt(context))
  → JSON parsé strict

NIVEAU 4 (Python, 0$)
  AntiNoiseFilter.passes()
  → KO : ATTENDRE
  → OK :
    adjust_position_size(confiance, regime, dd_today)
    → si Mode Auto + can_send_auto_order() True → exécution NT8 ATI
    → sinon → affichage Mode Manuel
```

---

## RÉCAPITULATIF — Modifications fichiers

| Fichier | État | Action |
|---------|------|--------|
| `code\engine\signal_scorer.py` | ⏳ à créer | Nouveau — abrite Walk-Forward, Hysteresis, AntiNoise |
| `code\engine\correlations.py` | ✅ existe | Ajouter `detect_correlation_break()` + `detect_market_regime()` |
| `code\engine\risk_manager.py` | ✅ existe | Ajouter `LEVIER_PAR_REGIME`, `adjust_position_size()`, `check_drawdown_breakers()`, `write_mandatory_lock()`, `is_trading_locked()`, `force_exit_on_regime_change()` |
| `code\engine\claude_brain.py` | ✅ existe | Inchangé — utilisera `prompt_builder.py` à créer |
| `code\engine\prompt_builder.py` | ⏳ à créer | Nouveau — fonction `build_god_mode_prompt()` |
| `code\config\settings.py` | ✅ existe | Ajouter constantes : seuils Hysteresis, Cool-down, AntiNoise |

## RÉCAPITULATIF — Concepts ignorés (hors scope)

- ❌ HMM (Hidden Markov Model) — TRADEX-AI utilise règles déterministes
- ❌ Alpaca, Yahoo Finance, IBKR — broker = NinjaTrader 8 ATI port 36973
- ❌ Streamlit — dashboard sera React 18 + Vite + Tailwind
- ❌ Options Wheel, Cash Secured Put, Covered Call — TRADEX-AI = futures only
- ❌ Copy Trading Congrès, Capital Trades — méthode = Belkhayate exclusivement
- ❌ Claude Desktop, Claude Pro, MCP TradingView — TRADEX-AI = Python + Claude API
- ❌ Pine Script, NinjaScript C# — TRADEX-AI = données via JSON, pas scripting plateforme
- ❌ Actions US (NVDA, TSLA, RIVN) — TRADEX-AI = futures CME (GC/HG/CL) + CBOT (ZW)
- ❌ Range Bars, DOM scraping détaillé — déjà couverts par C2 Order Flow ATAS

---

*Document généré le 2026-05-03 par audit du PDF source — version 1.0.*
*Méthode Belkhayate prioritaire sur tout concept extérieur.*
*Tout ajout doit repasser par PROMPT-GATE-AUDIT v3.1 avant implémentation.*
