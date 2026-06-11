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
    source = tweet_data.get('account', 'unknown')
    duration = SUSPENSION_DURATIONS.get(source, 30)
    def vix_stable() -> bool:
        return get_vix_delta_pct(minutes=15) < 0.05
    suspend_auto_mode(minutes=duration, condition=vix_stable)
