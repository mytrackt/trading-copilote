# PLAN 12 MISSIONS ATOMIQUES — MBK Trading SaaS
## Exécution Claude Code — Une mission à la fois
**Principe : 1 prompt = 1 fichier = 1 vérification**

---

## RÈGLES D'EXÉCUTION ABSOLUES

```
1. Exécuter UNE mission à la fois
2. Attendre la fin complète avant la suivante
3. Vérifier le fichier créé avant de continuer
4. Si erreur → corriger cette mission uniquement
5. Ne jamais donner 2 missions dans le même prompt
```

---

## STRUCTURE DES DOSSIERS À CRÉER D'ABORD

Coller dans Claude Code AVANT toute mission :

```
Crée la structure de dossiers suivante si elle n'existe pas :
C:\trading-copilote\
C:\trading-copilote\data\
C:\trading-copilote\engine\
C:\trading-copilote\utils\
C:\trading-copilote\config\
C:\trading-copilote\collectors\
C:\trading-copilote\execution\
C:\trading-copilote\api\
C:\trading-copilote\dashboard\
C:\trading-copilote\kb\
C:\trading-copilote\logs\
C:\trading-copilote\docs\
```

---

## PHASE 1 — FICHIERS INFRASTRUCTURE (5 missions)

---

### MISSION 1 — atomic_writer.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\utils\atomic_writer.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import os
import json
import tempfile
import time

def atomic_write_json(filepath: str, data: dict) -> None:
    """Écriture atomique — aucun lecteur ne voit un fichier partiel."""
    dir_path = os.path.dirname(filepath)
    with tempfile.NamedTemporaryFile(
        mode='w', dir=dir_path, suffix='.tmp',
        delete=False, encoding='utf-8'
    ) as tmp:
        json.dump(data, tmp, ensure_ascii=False, indent=2)
        tmp_path = tmp.name
    os.replace(tmp_path, filepath)

def safe_read_json(filepath: str, max_retries: int = 3) -> dict:
    """Lecture avec retry sur JSONDecodeError."""
    for attempt in range(max_retries):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            if attempt == max_retries - 1:
                raise
            time.sleep(0.1)
--- FIN CONTENU ---
```

**Vérification après Mission 1 :**
```
Lis C:\trading-copilote\utils\atomic_writer.py et confirme
que les 2 fonctions atomic_write_json et safe_read_json
sont bien présentes.
```

---

### MISSION 2 — staleness_monitor.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\staleness_monitor.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import os
from datetime import datetime, timedelta

STALENESS_LIMITS = {
    "NT8_data.csv":           timedelta(seconds=10),
    "ATAS_signals.json":      timedelta(seconds=10),
    "news_feed.json":         timedelta(minutes=10),
    "fear_greed_stocks.json": timedelta(minutes=15),
    "gdelt_signals.json":     timedelta(minutes=20),
    "events_calendar.json":   timedelta(hours=2),
    "macro.json":             timedelta(hours=6),
    "cot_data.json":          timedelta(days=8),
    "dark_pools.json":        timedelta(days=16),
}

DATA_DIR = "C:/trading-copilote/data"

def check_all_staleness() -> dict:
    status = {}
    for filename, limit in STALENESS_LIMITS.items():
        path = f"{DATA_DIR}/{filename}"
        try:
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            age = datetime.now() - mtime
            status[filename] = {
                "ok":          age < limit,
                "age_seconds": round(age.total_seconds()),
                "status":      "FRESH" if age < limit else "STALE"
            }
        except FileNotFoundError:
            status[filename] = {"ok": False, "status": "MISSING"}
    return status

def get_system_mode(staleness: dict) -> str:
    critical  = ["NT8_data.csv", "ATAS_signals.json"]
    important = ["news_feed.json", "fear_greed_stocks.json"]
    if any(not staleness.get(s, {}).get("ok", False) for s in critical):
        return "BLOCKED"
    if any(not staleness.get(s, {}).get("ok", False) for s in important):
        return "MANUAL_ONLY"
    return "OPERATIONAL"
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\staleness_monitor.py
et confirme que STALENESS_LIMITS contient bien 9 entrées
et que get_system_mode() retourne BLOCKED, MANUAL_ONLY ou OPERATIONAL.
```

---

### MISSION 3 — circuit_breaker.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\circuit_breaker.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import threading
from datetime import datetime, timedelta
from enum import Enum

class CircuitState(Enum):
    CLOSED    = "CLOSED"
    OPEN      = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker:
    def __init__(self, name: str, failure_threshold: int = 3,
                 recovery_timeout: int = 60):
        self.name              = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout  = recovery_timeout
        self.failure_count     = 0
        self.last_failure_time = None
        self.state             = CircuitState.CLOSED
        self._lock             = threading.Lock()

    def call(self, func, *args, **kwargs):
        with self._lock:
            if self.state == CircuitState.OPEN:
                elapsed = (datetime.now() - self.last_failure_time).total_seconds()
                if elapsed >= self.recovery_timeout:
                    self.state = CircuitState.HALF_OPEN
                else:
                    raise Exception(
                        f"[{self.name}] Circuit OPEN — reprise dans "
                        f"{self.recovery_timeout - elapsed:.0f}s"
                    )
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e

    def _on_success(self):
        with self._lock:
            self.failure_count = 0
            self.state = CircuitState.CLOSED

    def _on_failure(self):
        with self._lock:
            self.failure_count += 1
            self.last_failure_time = datetime.now()
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN

    def get_status(self) -> dict:
        return {
            "name":    self.name,
            "state":   self.state.value,
            "failures":self.failure_count,
        }

CB_NT8    = CircuitBreaker("NT8_data",     failure_threshold=3, recovery_timeout=30)
CB_ATAS   = CircuitBreaker("ATAS_signals", failure_threshold=3, recovery_timeout=30)
CB_CLAUDE = CircuitBreaker("Claude_API",   failure_threshold=2, recovery_timeout=60)

def get_all_circuit_status() -> dict:
    return {
        "NT8":    CB_NT8.get_status(),
        "ATAS":   CB_ATAS.get_status(),
        "Claude": CB_CLAUDE.get_status(),
    }
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\circuit_breaker.py
et confirme que CB_NT8, CB_ATAS et CB_CLAUDE
sont bien instanciés en bas du fichier.
```

---

### MISSION 4 — risk_manager.py (suspend_auto_mode)

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\risk_manager.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import threading
from datetime import datetime, timedelta

_lock = threading.Lock()
_auto_suspended_until = None
_reactivation_condition = None

RÈGLES_RISQUE = {
    "max_risque_trade":        0.02,
    "max_trades_simultanes":   2,
    "drawdown_stop_jour":      0.03,
    "vix_taille_reduite":      20,
    "vix_no_trade":            35,
    "marches_alignes_min":     3,
    "confirmations_min":       2,
    "confiance_auto_min":      85,
    "confiance_manuel_min":    65,
    "bloquer_si_fc":           True,
    "exiger_delta_confirm":    True,
    "zone_interdite_rouge":    30,
    "zone_alerte_rouge":       120,
    "eia_surprise_taille_red": 3.0,
    "gdelt_crise_stop_auto":   True,
}

RÈGLES_PSYCHOLOGIE = {
    "cooldown_post_stop_min":   15,
    "cooldown_3_pertes_heures": 2,
    "post_win_size_reduction":  0.50,
    "max_screen_hours_day":     8,
    "journal_required":         True,
}

SUSPENSION_DURATIONS = {
    "@federalreserve":   60,
    "@POTUS":            45,
    "@OPECSecretariat":  30,
    "@saylor":           20,
    "@elonmusk":         20,
    "@WSJmarkets":       15,
}

def suspend_auto_mode(minutes: int, condition=None) -> None:
    global _auto_suspended_until, _reactivation_condition
    with _lock:
        _auto_suspended_until = datetime.now() + timedelta(minutes=minutes)
        _reactivation_condition = condition

def is_auto_mode_suspended() -> bool:
    global _auto_suspended_until, _reactivation_condition
    with _lock:
        if _auto_suspended_until is None:
            return False
        if datetime.now() >= _auto_suspended_until:
            if _reactivation_condition and not _reactivation_condition():
                _auto_suspended_until += timedelta(minutes=5)
                return True
            _auto_suspended_until = None
            _reactivation_condition = None
            return False
        return True

def get_confiance_min(correlations: dict) -> int:
    nb_instables = sum(1 for c in correlations.values()
                       if c.get('unstable', False))
    if nb_instables >= 3: return 92
    elif nb_instables >= 1: return 90
    return 85

def can_send_auto_order(signal: dict) -> bool:
    if not signal.get('mode_auto_autorise', True):
        return False
    if is_auto_mode_suspended():
        return False
    if signal.get('confiance', 0) < RÈGLES_RISQUE['confiance_auto_min']:
        return False
    return True

def handle_critical_tweet(tweet_data: dict) -> None:
    from engine.data_reader import get_vix_delta_pct
    source   = tweet_data.get('account', 'unknown')
    duration = SUSPENSION_DURATIONS.get(source, 30)
    def vix_stable() -> bool:
        return get_vix_delta_pct(minutes=15) < 0.05
    suspend_auto_mode(minutes=duration, condition=vix_stable)
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\risk_manager.py
et confirme que suspend_auto_mode(),
is_auto_mode_suspended() et can_send_auto_order()
sont toutes les 3 définies.
```

---

### MISSION 5 — data_reader.py (get_vix_delta_pct)

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\data_reader.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import pandas as pd
from datetime import datetime, timedelta

DATA_DIR = "C:/trading-copilote/data"

def get_vix_delta_pct(minutes: int = 15) -> float:
    """
    Calcule la variation absolue du VIX sur les N dernières minutes.
    Retourne 0.0 si données insuffisantes (conservatif).
    """
    try:
        df = pd.read_csv(f"{DATA_DIR}/NT8_data.csv")
        vix_df = df[df['symbol'] == 'VX'].copy()
        vix_df['timestamp'] = pd.to_datetime(vix_df['timestamp'])
        vix_df = vix_df.sort_values('timestamp')

        if len(vix_df) < 2:
            return 0.0

        cutoff = datetime.now() - timedelta(minutes=minutes)
        recent = vix_df[vix_df['timestamp'] >= cutoff]

        if len(recent) < 2:
            return 0.0

        vix_start = recent.iloc[0]['close']
        vix_end   = recent.iloc[-1]['close']

        if vix_start == 0:
            return 0.0

        return round(abs((vix_end - vix_start) / vix_start), 4)

    except Exception:
        return 0.0

def read_nt8_data() -> dict:
    """Lit NT8_data.csv avec circuit breaker."""
    from engine.circuit_breaker import CB_NT8
    from utils.atomic_writer import safe_read_json
    return CB_NT8.call(
        lambda: pd.read_csv(f"{DATA_DIR}/NT8_data.csv").to_dict('records')
    )

def read_atas_signals() -> dict:
    """Lit ATAS_signals.json avec circuit breaker."""
    from engine.circuit_breaker import CB_ATAS
    from utils.atomic_writer import safe_read_json
    return CB_ATAS.call(
        lambda: safe_read_json(f"{DATA_DIR}/ATAS_signals.json")
    )
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\data_reader.py
et confirme que get_vix_delta_pct() retourne 0.0
si les données sont insuffisantes.
```

---

## PHASE 2 — FICHIERS MOTEUR (3 missions)

---

### MISSION 6 — correlations.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\correlations.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import pandas as pd
from datetime import datetime

# PROVISOIRE — calibrer avec calibrate_bars_per_day.py en semaine 9
BARS_PER_DAY_ESTIMATES = {
    "GC":  150, "ES": 200, "CL": 180,
    "6J":  120, "HG": 100, "MBT": 160,
}

CORRELATION_PAIRS = [
    ("GC","DX"), ("ES","VX"), ("BTC","ES"),
    ("CL","DX"), ("HG","ES"), ("6J","VX"),
]

def calculate_live_correlations(
    historical_data: dict,
    window_days: int = 30,
    actif_principal: str = "ES"
) -> dict:
    closes = pd.DataFrame({
        actif: data['close'] for actif, data in historical_data.items()
    })

    bars_day = BARS_PER_DAY_ESTIMATES.get(actif_principal, 160)
    w30 = window_days * bars_day
    w7  = 7 * bars_day

    corr_30j = closes.tail(w30).corr()
    corr_7j  = closes.tail(w7).corr()

    result = {}
    for a, b in CORRELATION_PAIRS:
        try:
            v30 = round(corr_30j.loc[a, b], 3)
            v7  = round(corr_7j.loc[a, b], 3)
            result[f"{a}_{b}"] = {
                "value":    v30,
                "short":    v7,
                "unstable": abs(v30 - v7) > 0.20,
                "as_of":    datetime.utcnow().isoformat(),
            }
        except KeyError:
            result[f"{a}_{b}"] = {
                "value": 0, "unstable": True,
                "error": f"Actif {a} ou {b} absent"
            }
    return result

def check_portfolio_correlation(
    new_trade: dict,
    open_trades: list,
    live_correlations: dict
) -> bool:
    for open_trade in open_trades:
        k1 = f"{new_trade['actif']}_{open_trade['actif']}"
        k2 = f"{open_trade['actif']}_{new_trade['actif']}"
        corr = abs(
            live_correlations.get(k1, live_correlations.get(k2, {}))
            .get('value', 0)
        )
        if corr > 0.60:
            return False
    return True
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\correlations.py
et confirme que BARS_PER_DAY_ESTIMATES
et calculate_live_correlations() sont présents.
```

---

### MISSION 7 — claude_brain.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\engine\claude_brain.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
import anthropic
import json
from engine.circuit_breaker import CB_CLAUDE
from engine.signal_scorer import calculate_7circles_score

client = anthropic.Anthropic()

def call_claude_kb(kb_rules: str, god_mode_prompt: str) -> dict:
    """
    Appelle Claude Sonnet 4.6 avec cache persistant sur la KB.
    Modèle : claude-sonnet-4-6 (Mai 2026)
    Cache  : persistent = 1 heure (économie 90% tokens KB)
    """
    def _call():
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=[
                {
                    "type": "text",
                    "text": kb_rules,
                    "cache_control": {"type": "persistent"}
                }
            ],
            messages=[
                {"role": "user", "content": god_mode_prompt}
            ]
        )
        content = response.content[0].text
        return json.loads(content)

    return CB_CLAUDE.call(_call)

def get_signal_with_fallback(context: dict, kb_rules: str) -> dict:
    """
    Tente Claude API → fallback déterministe si échec.
    Fallback : confiance max 65%, Auto toujours bloqué.
    """
    try:
        from engine.prompt_builder import build_god_mode_prompt
        prompt = build_god_mode_prompt(context)
        return call_claude_kb(kb_rules, prompt)

    except Exception as e:
        score = calculate_7circles_score(context)

        if score >= 17 and context['risk']['dd_today'] < 0.02:
            return {
                "signal":             context['c1']['direction'],
                "confiance":          min(score * 3, 65),
                "raison":             "FALLBACK_LOCAL",
                "taille":             "mini",
                "taille_contrats":    1,
                "mode_auto_autorise": False,
                "alerte":             f"Claude API indisponible: {str(e)[:80]}"
            }
        return {
            "signal":             "ATTENDRE",
            "confiance":          0,
            "raison":             "FALLBACK_LOCAL — score insuffisant",
            "mode_auto_autorise": False,
            "alerte":             "Claude API indisponible + conditions KO"
        }
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\engine\claude_brain.py et confirme :
1. Le modèle est bien "claude-sonnet-4-6"
2. cache_control est "persistent" (pas "ephemeral")
3. confiance max dans le fallback est bien 65
```

---

### MISSION 8 — settings.py

**Prompt Claude Code :**
```
Crée le fichier C:\trading-copilote\config\settings.py
avec exactement ce contenu. Ne modifie rien d'autre.

--- CONTENU ---
from zoneinfo import ZoneInfo

TIMEZONES = {
    "LOCAL":    ZoneInfo("Africa/Casablanca"),
    "EXCHANGE": ZoneInfo("America/New_York"),
    "UTC":      ZoneInfo("UTC"),
}

ACTIFS_TRADABLES   = ["GC", "HG", "CL", "ES", "MBT", "6J"]
ACTIFS_INDICATEURS = {
    "VX": {"role": "Sentiment", "trade": False},
    "DX": {"role": "Macro",     "trade": False, "proxy": "DXY Alpha Vantage"},
}

COULOIRS_HORAIRES = {
    "GC":  [("08:20", "10:30", "ET"), ("13:30", "14:00", "ET")],
    "HG":  [("08:20", "11:00", "ET")],
    "CL":  [("09:00", "10:30", "ET"), ("14:30", "15:00", "ET")],
    "ES":  [("09:30", "11:00", "ET"), ("14:30", "16:00", "ET")],
    "6J":  [("08:00", "10:00", "ET"), ("14:30", "15:30", "ET")],
    "MBT": [("09:00", "11:00", "ET"), ("14:30", "17:00", "ET")],
}

HEURES_INTERDITES = [("23:00", "00:30", "ET")]

EVENT_WINDOWS = {
    "NFP":  {"avant": 30, "apres": 60,  "actifs": ["ES","GC","DX","6J"]},
    "CPI":  {"avant": 30, "apres": 60,  "actifs": ["ES","GC","DX"]},
    "FOMC": {"avant": 60, "apres": 180, "actifs": ["TOUS"]},
    "BOJ":  {"avant": 30, "apres": 120, "actifs": ["6J","GC"]},
    "OPEC": {"avant": 30, "apres": 120, "actifs": ["CL","GC"]},
    "GDP":  {"avant": 15, "apres": 45,  "actifs": ["ES","DX"]},
    "EIA":  {"avant": 15, "apres": 30,  "actifs": ["CL"]},
}

ATI_CONFIG = {
    "port":                  36973,
    "timeout_send":          5,
    "retry_max":             3,
    "retry_backoff":         [1, 2, 4],
    "heartbeat_interval":    10,
    "slippage_max_ticks":    2,
    "partial_fill_min":      0.80,
    "confirmation_timeout":  8,
    "doublon_guard_seconds": 30,
    "taille_mini_contrats":  1,
}

X_COM_CONFIG = {
    "enabled": True,
    "fallback": "SKIP",
    "comptes": [
        "@federalreserve", "@POTUS",
        "@OPECSecretariat", "@saylor",
        "@elonmusk", "@WSJmarkets",
    ]
}

def is_in_couloir(actif: str) -> bool:
    from datetime import datetime
    now_et = datetime.now(TIMEZONES["EXCHANGE"])
    current = now_et.strftime("%H:%M")
    for start, end, _ in COULOIRS_HORAIRES.get(actif, []):
        if start <= current <= end:
            return True
    return False

def validate_trade_actif(actif: str) -> bool:
    if actif in ACTIFS_INDICATEURS:
        raise ValueError(f"BLOQUÉ : {actif} est un indicateur, pas tradable")
    return actif in ACTIFS_TRADABLES
--- FIN CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\config\settings.py et confirme :
1. ACTIFS_TRADABLES contient bien 6 actifs
2. ACTIFS_INDICATEURS contient VX et DX
3. EVENT_WINDOWS contient FOMC avec apres=180
```

---

## PHASE 3 — DOCUMENT MASTER (4 missions)

---

### MISSION 9 — Créer la structure docs

**Prompt Claude Code :**
```
Copie le fichier C:\Users\mytra\Downloads\MASTER_MBK_TRADING_SAAS_COMPLET.md
vers C:\trading-copilote\docs\MASTER_MBK_v2.md
sans le modifier. Confirme que la copie est faite.
```

---

### MISSION 10 — Réécrire Section 1 Budget

**Prompt Claude Code :**
```
Dans C:\trading-copilote\docs\MASTER_MBK_v2.md,
remplace UNIQUEMENT la section intitulée
"SECTION 1 — BUDGET FINAL CONSOLIDÉ"
par le contenu suivant. Ne touche à rien d'autre.

--- NOUVEAU CONTENU SECTION 1 ---
# SECTION 1 — BUDGET FINAL CONSOLIDÉ

## Architecture événementielle — Claude appelé sur signal qualifié uniquement

```
NIVEAU 1 — SURVEILLANCE Python (0 coût API)
Toutes les 2 secondes : lire NT8 + ATAS → vérifier 3/4 + 2/3
→ Si non rempli : ATTENDRE (aucun appel Claude)

NIVEAU 2 — PRÉ-QUALIFICATION Python (0 coût API)
Si 3/4 + 2/3 OK : vérifier event rouge + DD + VIX
→ Si l'un échoue : ATTENDRE (aucun appel Claude)

NIVEAU 3 — DÉCISION Claude AI (coût réel)
Uniquement si niveaux 1 ET 2 passent → appel API
```

## Estimation coût Claude API

| Scénario | Fréquence signal | Appels/mois | Coût (avec cache) |
|----------|-----------------|-------------|-------------------|
| Marché calme | 1/30 min | ~352 | ~8-12$ |
| Marché actif (session US) | 1/5 min | ~2 112 | ~25-50$ |
| **Réserver dans le budget** | | | **50$/mois** |

Note : calibrer la fréquence réelle en paper trading semaine 9-10.

## Budget mensuel

| # | Poste | Coût/mois |
|---|-------|-----------|
| 1 | NinjaTrader 8 (broker NTB inclus) | 0$ |
| 2 | Data feed CME (Rithmic via NTB) | ~50$ |
| 3 | Exchange fee CBOE (VIX) | ~10$ |
| 4 | ATAS Pro (order flow) | ~70$ |
| 5 | Claude API (Sonnet 4.6 + cache) | ~15-50$ |
| 6 | GetXAPI (6 comptes X.com) | ~1$ |
| 7 | 21 sources intelligence | 0$ |
| **TOTAL** | | **~146-181$/mois** |
| **Marge sur 200$** | | **~19-54$/mois** |
--- FIN NOUVEAU CONTENU ---
```

**Vérification :**
```
Lis C:\trading-copilote\docs\MASTER_MBK_v2.md
et confirme que la Section 1 contient maintenant
"Architecture événementielle" et les 3 NIVEAUX.
```

---

### MISSION 11 — Ajouter Sections 10, 11, 12

**Prompt Claude Code :**
```
Dans C:\trading-copilote\docs\MASTER_MBK_v2.md,
ajoute à la FIN du fichier (après la dernière section)
le contenu suivant. N'efface rien d'existant.

--- CONTENU À AJOUTER ---

# SECTION 10 — ROBUSTESSE INFRASTRUCTURE

## Modules obligatoires
- `engine/staleness_monitor.py` : vérifie fraîcheur des 15 sources
- `engine/circuit_breaker.py`   : CB_NT8, CB_ATAS, CB_CLAUDE
- `utils/atomic_writer.py`      : écritures JSON atomiques
- Endpoint `/health` FastAPI     : status système temps réel

## Règle staleness
- NT8 + ATAS > 10s → BLOCKED (aucun trade)
- News + F&G > 10-15min → MANUAL_ONLY
- Autres sources → signal dégradé mais non bloquant

---

# SECTION 11 — CONFORMITÉ JURIDICTIONNELLE

**Profil : Résident fiscal Maroc | Comptes FR + MA | Broker US**

> "Utiliser compte bancaire français pour alimenter le broker US
> (hors périmètre Office des Changes).
> Gains à déclarer au Maroc (résidence fiscale) — taux 15% RCM
> ou IR selon requalification possible en activité commerciale.
> Formulaire 3916 si compte broker déclaré via France.
> Consulter expert-comptable marocain avant live trading."

**PRIORITÉ 1 — Avant de déposer 1 dirham :**
- Consulter expert-comptable marocain
- Ouvrir compte broker NTB avec IBAN français
- Ne jamais utiliser le compte marocain pour le broker US

**PRIORITÉ 2 — Dès le premier trade réel :**
- Tenir un registre détaillé : (date, actif, P&L, frais) → SQLite du SaaS
- Conserver tous les relevés broker mensuels (PDF archivés)

---

# SECTION 12 — PSYCHOLOGIE ET DISCIPLINE

| Règle | Valeur | Conséquence |
|-------|--------|-------------|
| Cooldown post-stop | 15 min | Trade bloqué |
| Cooldown 3 pertes | 2 heures | Auto désactivé |
| Post-win size | -50% taille 24h si gain > 5% | Taille auto réduite |
| Max heures écran | 8h/jour | Session arrêtée |
| Journal obligatoire | Après chaque trade | Trade suivant bloqué si vide |
--- FIN CONTENU À AJOUTER ---
```

**Vérification :**
```
Lis les 50 dernières lignes de C:\trading-copilote\docs\MASTER_MBK_v2.md
et confirme que les Sections 10, 11 et 12 sont présentes.
```

---

### MISSION 12 — Réécrire Cercle 7 Corrélations

**Prompt Claude Code :**
```
Dans C:\trading-copilote\docs\MASTER_MBK_v2.md,
trouve la section contenant les corrélations figées
(lignes avec "ρ ~ -0.85", "ρ ~ -0.90" etc.)
et remplace-la par ce contenu. Ne touche à rien d'autre.

--- NOUVEAU CONTENU CERCLE 7 ---
## CERCLE 7 — CORRÉLATIONS & RÉGIME
**Source : calcul Python local — 0$**

### 7A — Corrélations glissantes 30 jours (LIVE — jamais figées)

```python
# Valeurs calculées en temps réel par correlations.py
# Toutes les corrélations sont DYNAMIQUES (fenêtre 30j en Range Bars)
# Une corrélation figée = signal potentiellement faux

CORRELATION_PAIRS = [
    ("GC","DX"),  # Or / Dollar — typiquement inverse
    ("ES","VX"),  # SP500 / VIX — typiquement inverse
    ("BTC","ES"), # Bitcoin / SP500 — instable selon régime
    ("CL","DX"),  # Pétrole / Dollar — typiquement inverse
    ("HG","ES"),  # Cuivre / SP500 — typiquement positif
    ("6J","VX"),  # Yen / VIX — typiquement positif (risk-off)
]
# Les valeurs réelles sont dans correlations.json
# Recalculées toutes les 30 minutes
```

⚠️ RÈGLE ABSOLUE : Ne jamais coder de valeur ρ en dur.
Toujours lire correlations.json → valeur live → si instable : confiance_min +5pts.

### 7B — Détecteur de régime de marché
[inchangé — voir code dans settings.py]

### 7C — Inter-market Analysis
[inchangé — voir RÈGLES_INTERMARKET dans settings.py]
--- FIN NOUVEAU CONTENU ---
```

**Vérification finale :**
```
Lis C:\trading-copilote\docs\MASTER_MBK_v2.md
et confirme qu'il n'y a plus aucune valeur
"ρ ~ -0.85" ou "ρ ~ -0.90" dans le fichier.
```

---

## RÉCAPITULATIF — ORDRE D'EXÉCUTION

```
AVANT LES MISSIONS :
□ Créer la structure de dossiers

PHASE 1 — Infrastructure :
□ Mission 1  → utils/atomic_writer.py
□ Mission 2  → engine/staleness_monitor.py
□ Mission 3  → engine/circuit_breaker.py
□ Mission 4  → engine/risk_manager.py
□ Mission 5  → engine/data_reader.py

PHASE 2 — Moteur :
□ Mission 6  → engine/correlations.py
□ Mission 7  → engine/claude_brain.py
□ Mission 8  → config/settings.py

PHASE 3 — Document :
□ Mission 9  → Copier MASTER → docs/MASTER_MBK_v2.md
□ Mission 10 → Réécrire Section 1 Budget
□ Mission 11 → Ajouter Sections 10, 11, 12
□ Mission 12 → Réécrire Cercle 7 Corrélations

APRÈS LES 12 MISSIONS :
□ Relancer audit 11 passes dans Claude Code
   sur C:\trading-copilote\docs\MASTER_MBK_v2.md
   Cible : score ≥ 90/100
```

---

## RÈGLE D'OR FINALE

```
UN prompt = UNE mission = UN fichier = UNE vérification

Jamais :
❌ "Applique toutes les corrections..."
❌ "Crée tous les fichiers..."
❌ "Mets à jour le document entier..."

Toujours :
✅ "Crée CE fichier avec CE contenu exact"
✅ "Remplace UNIQUEMENT cette section"
✅ "Confirme que X est bien présent"
```

---

*Plan 12 Missions Atomiques v1.0 — MBK Trading SaaS*
*Stratégie infaillible : atomique + vérification + déterministe*
*Date : 02 Mai 2026*
