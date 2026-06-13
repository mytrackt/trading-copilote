import threading
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

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
    if is_auto_globally_blocked():          # Auto BLOQUE par defaut (VERROUILLE)
        return False
    if not signal.get('mode_auto_autorise', True):
        return False
    if is_auto_mode_suspended():
        return False
    if signal.get('confiance', 0) < RÈGLES_RISQUE['confiance_auto_min']:
        return False
    return True

def handle_critical_tweet(tweet_data: dict) -> None:
    from engine.data_reader import get_vix_delta_pct
    source = tweet_data.get('account', 'unknown')
    duration = SUSPENSION_DURATIONS.get(source, 30)
    def vix_stable() -> bool:
        return get_vix_delta_pct(minutes=15) < 0.05
    suspend_auto_mode(minutes=duration, condition=vix_stable)


# =============================================================================
# A3 -- GARDE-FOUS RUNTIME (Phase 5)
# =============================================================================
ET = ZoneInfo("America/New_York")           # timezone des evenements macro US

# News gate : 30 min AVANT = VERROUILLE (D6, CLAUDE.md) ; APRES = configurable (defaut 15).
NEWS_GATE_BEFORE_MIN = 30
NEWS_GATE_AFTER_MIN_DEFAUT = 15
NEWS_EVENTS_CRITIQUES = ("NFP", "FOMC", "CPI", "GDP", "JOLTS", "PPI")  # miroir settings.NEWS_EVENTS_CRITIQUES

# Suspension Auto
MAX_PERTES_JOUR = 2
VIX_SUSPEND_SEUIL = RÈGLES_RISQUE["vix_no_trade"]   # 35

# Mode Auto : BLOQUE par defaut (VERROUILLE -- deverrouillage hors perimetre)
MODE_AUTO_ENABLED_DEFAUT = False


def news_gate_blocked(now, events, after_min: int = NEWS_GATE_AFTER_MIN_DEFAUT) -> dict:
    """
    Bloque 30 min AVANT (verrouille) et `after_min` min APRES un evenement critique.
    Timezone ET (America/New_York). `now` et `events[*]["time"]` doivent etre timezone-aware.
    events : [{"type": "NFP", "time": datetime_aware}, ...]. Seuls les types critiques bloquent.
    """
    now_et = now.astimezone(ET)
    for ev in events:
        if ev.get("type") not in NEWS_EVENTS_CRITIQUES:
            continue
        t = ev["time"].astimezone(ET)
        start = t - timedelta(minutes=NEWS_GATE_BEFORE_MIN)
        end = t + timedelta(minutes=after_min)
        if start <= now_et <= end:
            return {"blocked": True, "event": ev["type"], "fenetre": (start, end)}
    return {"blocked": False, "event": None, "fenetre": None}


def should_suspend_auto(pertes_jour: int, vix) -> dict:
    """Suspension Auto si 2 pertes/jour OU VIX > seuil critique."""
    raisons = []
    if pertes_jour >= MAX_PERTES_JOUR:
        raisons.append("2_PERTES_JOUR")
    if vix is not None and vix > VIX_SUSPEND_SEUIL:
        raisons.append("VIX_CRITIQUE")
    return {"suspendre": bool(raisons), "raisons": raisons}


def staleness_blocked(staleness_status: dict) -> dict:
    """Donnees perimees -> BLOCKED. staleness_status : {"NT8": bool_stale, "ATAS": ..., ...}."""
    stale = [src for src, est_stale in staleness_status.items() if est_stale]
    return {"blocked": bool(stale), "sources_stale": stale}


def is_auto_globally_blocked() -> bool:
    """True tant que le mode Auto n'est pas explicitement deverrouille (defaut : bloque)."""
    return not MODE_AUTO_ENABLED_DEFAUT


def runtime_guardrails(*, now, events, staleness_status, pertes_jour, vix,
                       after_min: int = NEWS_GATE_AFTER_MIN_DEFAUT) -> dict:
    """
    Porte runtime consolidee.
    - news gate / staleness  -> bloquent TOUT trade (manuel + auto).
    - suspension 2-pertes / VIX / blocage global / suspension tweet -> bloquent l'AUTO seulement.
    """
    blocages = []
    ng = news_gate_blocked(now, events, after_min=after_min)
    if ng["blocked"]:
        blocages.append(("NEWS_GATE", ng["event"]))
    st = staleness_blocked(staleness_status)
    if st["blocked"]:
        blocages.append(("STALENESS", st["sources_stale"]))

    susp = should_suspend_auto(pertes_jour, vix)
    auto_bloque = (is_auto_globally_blocked() or susp["suspendre"]
                   or is_auto_mode_suspended() or bool(blocages))
    return {
        "trade_autorise": not bool(blocages),
        "blocages": blocages,
        "mode_auto_autorise": not auto_bloque,
        "suspension_auto": susp,
    }
