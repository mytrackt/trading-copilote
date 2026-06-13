"""
test_risk_guardrails.py -- Tests deterministes A3 (Phase 5).
News gate (30 avant verrouille / apres configurable, timezone ET), suspension Auto,
staleness BLOCKED, Auto bloque par defaut, circuit breaker timeout/retry/fallback ATTENDRE.
Runnable : `py test_risk_guardrails.py`  OU  `pytest`.
"""
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import risk_manager as rm
import circuit_breaker as cbm

ET = rm.ET
NFP = {"type": "NFP", "time": datetime(2026, 6, 5, 8, 30, tzinfo=ET)}   # NFP 8h30 ET


# ---- News gate ----
def test_news_gate_30_avant_bloque():
    now = datetime(2026, 6, 5, 8, 10, tzinfo=ET)        # 20 min avant
    assert rm.news_gate_blocked(now, [NFP])["blocked"] is True


def test_news_gate_avant_la_fenetre_ok():
    now = datetime(2026, 6, 5, 7, 50, tzinfo=ET)        # 40 min avant -> hors 30
    assert rm.news_gate_blocked(now, [NFP])["blocked"] is False


def test_news_gate_apres_defaut_15_bloque_puis_libere():
    assert rm.news_gate_blocked(datetime(2026, 6, 5, 8, 40, tzinfo=ET), [NFP])["blocked"] is True   # +10
    assert rm.news_gate_blocked(datetime(2026, 6, 5, 8, 50, tzinfo=ET), [NFP])["blocked"] is False  # +20


def test_news_gate_apres_configurable():
    now = datetime(2026, 6, 5, 8, 50, tzinfo=ET)        # +20 min
    assert rm.news_gate_blocked(now, [NFP], after_min=15)["blocked"] is False
    assert rm.news_gate_blocked(now, [NFP], after_min=25)["blocked"] is True   # apres elargi -> bloque


def test_news_gate_avant_30_verrouille_non_parametrable():
    assert rm.NEWS_GATE_BEFORE_MIN == 30                # base verrouillee D6


def test_news_gate_timezone_conversion():
    now_utc = datetime(2026, 6, 5, 12, 10, tzinfo=timezone.utc)  # = 8h10 ET (EDT UTC-4)
    assert rm.news_gate_blocked(now_utc, [NFP])["blocked"] is True


def test_news_gate_ignore_evenement_non_critique():
    speech = {"type": "SPEECH", "time": datetime(2026, 6, 5, 8, 30, tzinfo=ET)}
    now = datetime(2026, 6, 5, 8, 10, tzinfo=ET)
    assert rm.news_gate_blocked(now, [speech])["blocked"] is False


# ---- Suspension Auto ----
def test_suspension_2_pertes_jour():
    r = rm.should_suspend_auto(pertes_jour=2, vix=20)
    assert r["suspendre"] is True and "2_PERTES_JOUR" in r["raisons"]


def test_suspension_vix_critique():
    r = rm.should_suspend_auto(pertes_jour=0, vix=40)
    assert r["suspendre"] is True and "VIX_CRITIQUE" in r["raisons"]


def test_pas_de_suspension_si_ok():
    assert rm.should_suspend_auto(pertes_jour=1, vix=30)["suspendre"] is False


# ---- Staleness ----
def test_staleness_bloque():
    r = rm.staleness_blocked({"NT8": False, "ATAS": True, "COT": False})
    assert r["blocked"] is True and r["sources_stale"] == ["ATAS"]


def test_staleness_ok():
    assert rm.staleness_blocked({"NT8": False, "ATAS": False})["blocked"] is False


# ---- Auto bloque par defaut ----
def test_auto_bloque_par_defaut():
    assert rm.is_auto_globally_blocked() is True


def test_can_send_auto_order_refuse_meme_haute_confiance():
    assert rm.can_send_auto_order({"mode_auto_autorise": True, "confiance": 99}) is False


# ---- Porte runtime consolidee ----
def test_runtime_clean_autorise_manuel_mais_pas_auto():
    out = rm.runtime_guardrails(
        now=datetime(2026, 6, 5, 12, 0, tzinfo=ET), events=[NFP],
        staleness_status={"NT8": False, "ATAS": False}, pertes_jour=0, vix=20)
    assert out["trade_autorise"] is True            # manuel ok (hors fenetre news, donnees fraiches)
    assert out["mode_auto_autorise"] is False       # auto bloque par defaut
    assert out["blocages"] == []


def test_runtime_news_bloque_tout():
    out = rm.runtime_guardrails(
        now=datetime(2026, 6, 5, 8, 10, tzinfo=ET), events=[NFP],
        staleness_status={"NT8": False}, pertes_jour=0, vix=20)
    assert out["trade_autorise"] is False
    assert any(code == "NEWS_GATE" for code, _ in out["blocages"])


def test_runtime_staleness_bloque_tout():
    out = rm.runtime_guardrails(
        now=datetime(2026, 6, 5, 12, 0, tzinfo=ET), events=[NFP],
        staleness_status={"NT8": True}, pertes_jour=0, vix=20)
    assert out["trade_autorise"] is False
    assert any(code == "STALENESS" for code, _ in out["blocages"])


# ---- Circuit breaker : timeout / retry / fallback ATTENDRE ----
def test_cb_success():
    cb = cbm.CircuitBreaker("ok", failure_threshold=3)
    assert cbm.protected_call(cb, lambda: 42, timeout_sec=5) == 42


def test_cb_exception_fallback_attendre():
    cb = cbm.CircuitBreaker("err", failure_threshold=10)
    def boom():
        raise ValueError("boom")
    r = cbm.protected_call(cb, boom, timeout_sec=5, retry_max=2)
    assert r["signal"] == "ATTENDRE" and r["mode_auto_autorise"] is False


def test_cb_retry_count_est_3():
    cb = cbm.CircuitBreaker("retry", failure_threshold=10)
    calls = {"n": 0}
    def fail():
        calls["n"] += 1
        raise RuntimeError("ko")
    cbm.protected_call(cb, fail, timeout_sec=5, retry_max=2, retry_delay_sec=0.0)
    assert calls["n"] == 3                          # 1 initial + 2 retries


def test_cb_timeout_fallback_attendre():
    cb = cbm.CircuitBreaker("slow", failure_threshold=10)
    def slow():
        time.sleep(0.5)
        return "trop tard"
    r = cbm.protected_call(cb, slow, timeout_sec=0.1, retry_max=0)
    assert r["signal"] == "ATTENDRE" and "CB_FALLBACK" in r["raison"]


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"[PASS] {t.__name__}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"[FAIL] {t.__name__} -> {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests PASS")
    sys.exit(1 if failed else 0)
