"""
test_api.py -- Tests deterministes A6 (Phase 7).
/signal via garde-fous runtime + signal_engine ; /mode jamais Auto ; persistance SQLite ;
ecoute 127.0.0.1. Base SQLite temporaire (la vraie data\tradex.db n'est pas touchee).
Runnable : `py test_api.py`  OU  `pytest`.
"""
import os
import sys
import tempfile
from datetime import datetime

# 05-saas sur le path pour importer les packages `engine` et `api`.
_SAAS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _SAAS)

from api import db                                   # noqa: E402
db.DB_PATH = os.path.join(tempfile.mkdtemp(), "tradex_test.db")   # base isolee
db.init_db()

from api import service                              # noqa: E402
from engine.risk_manager import ET                   # noqa: E402


def _full_signal():
    return {
        "sens": "ACHAT", "actif": "GC",
        "trading_cog": {"GC": "bleu", "HG": "bleu", "CL": "bleu", "ZW": "bleu"},
        "confirmation": {"DX": True, "ES": True, "VX": True},
        "cog_couleur": "bleu", "timing": -6.0, "prix_bande_2_ou_3": True,
        "bandes_resserrees": True, "biais_h4_aligne": True, "volume_ratio": 1.5,
        "atr_ratio": 1.0, "structure_non_cassee": True, "news_clean": True,
        "rr": 2.5, "taille_contrats": 1, "in_news_window": False,
    }


def _clean_guardrails():
    return {"events": [], "staleness_status": {"NT8": False, "ATAS": False},
            "pertes_jour": 0, "vix": 20}


NOW_CLEAN = datetime(2026, 6, 5, 12, 0, tzinfo=ET)
NFP = {"type": "NFP", "time": datetime(2026, 6, 5, 8, 30, tzinfo=ET)}


# ---- /mode : Auto jamais activable ----
def test_mode_defaut_manuel():
    s = service.get_mode_state()
    assert s["mode"] == "MANUEL" and s["auto_locked"] is True and s["auto_actif"] is False


def test_set_mode_auto_refuse():
    r = service.set_mode("AUTO")
    assert r["ok"] is False and r["raison"] == "AUTO_VERROUILLE" and r["auto_locked"] is True
    assert db.get_mode() == "MANUEL"               # inchange


def test_set_mode_manuel_ok():
    assert service.set_mode("MANUEL")["ok"] is True


def test_set_mode_invalide_refuse():
    assert service.set_mode("XYZ")["ok"] is False


# ---- /signal : garde-fous puis signal_engine ----
def test_signal_complet_signal_mais_auto_off():
    r = service.process_signal({"signal": _full_signal(), "guardrails": _clean_guardrails()}, now=NOW_CLEAN)
    assert r["decision"] == "SIGNAL" and r["score"] == 10.0
    assert r["mode_auto_autorise"] is False         # l'API n'active jamais l'Auto


def test_signal_news_bloque_avant_engine():
    g = _clean_guardrails()
    g["events"] = [NFP]
    now_in_window = datetime(2026, 6, 5, 8, 10, tzinfo=ET)
    r = service.process_signal({"signal": _full_signal(), "guardrails": g}, now=now_in_window)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "GARDE_FOUS_RUNTIME"
    assert any(code == "NEWS_GATE" for code, _ in r["blocages"])


def test_signal_staleness_bloque():
    g = _clean_guardrails()
    g["staleness_status"] = {"NT8": True}
    r = service.process_signal({"signal": _full_signal(), "guardrails": g}, now=NOW_CLEAN)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "GARDE_FOUS_RUNTIME"
    assert any(code == "STALENESS" for code, _ in r["blocages"])


def test_signal_etape0_ko_passe_par_engine():
    sig = _full_signal()
    sig["trading_cog"] = {"GC": "bleu", "HG": "bleu", "CL": "rouge", "ZW": "rouge"}  # 2/4
    r = service.process_signal({"signal": sig, "guardrails": _clean_guardrails()}, now=NOW_CLEAN)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "ETAPE_0_KO"
    assert r["mode_auto_autorise"] is False


def test_historique_persiste():
    avant = len(service.get_history(1000))
    service.process_signal({"signal": _full_signal(), "guardrails": _clean_guardrails()}, now=NOW_CLEAN)
    service.process_signal({"signal": _full_signal(), "guardrails": _clean_guardrails()}, now=NOW_CLEAN)
    apres = service.get_history(1000)
    assert len(apres) == avant + 2
    assert apres[0]["id"] > apres[1]["id"]          # plus recent en premier


# ---- Smoke tests HTTP (FastAPI TestClient, ecoute 127.0.0.1) ----
def test_http_endpoints():
    from fastapi.testclient import TestClient
    from api import main                            # db.init_db() utilise deja DB_PATH temporaire
    assert main.HOST == "127.0.0.1"                 # ecoute strictement locale
    client = TestClient(main.app)

    assert client.get("/health").json()["auto_locked"] is True
    assert client.get("/mode").json()["mode"] == "MANUEL"
    assert client.post("/mode", json={"mode": "AUTO"}).json()["raison"] == "AUTO_VERROUILLE"

    body = {"signal": _full_signal(), "guardrails": _clean_guardrails()}
    r = client.post("/signal", json=body).json()
    assert r["mode_auto_autorise"] is False
    assert "history" in client.get("/history").json()


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
