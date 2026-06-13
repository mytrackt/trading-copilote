"""
test_claude_brain.py -- Tests deterministes A5 (Phase 6).
Fallback aligne /10 (sans Energie), confiance <= 65% + Auto interdit, KB provisoire
(Auto interdit + banniere), parse_claude_json, load_kb_rules.
Runnable : `py test_claude_brain.py`  OU  `pytest`.

NB : ANTHROPIC_API_KEY factice posee AVANT import pour que l'init du client n'echoue pas ;
client force a None ensuite pour garantir le chemin fallback (aucun appel reseau).
prompt_builder etant absent, get_signal tombe de toute facon en fallback (etat connu du projet).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("ANTHROPIC_API_KEY", "test-dummy-key")

import claude_brain as cb

cb.client = None   # force le fallback, aucun appel reseau


def _ctx(**over):
    base = {
        "c1": {"bgc_signal": True, "direction": "LONG", "direction_ok": True},
        "c2": {"delta_positif": True, "big_trades_ok": True},
        "risk": {"dd_today": 0.0},
        "vix": 15,            # < 18 -> vix_favorable plein
        "no_news_gate": True,
    }
    base.update(over)
    return base


# ---- Bareme fallback /10 ----
def test_fallback_score_max_10():
    assert cb._calculate_fallback_score(_ctx()) == 10.0


def test_fallback_score_ignore_energie():
    # energie_ok True mais tout le reste faux -> 0 (l'Energie n'entre PAS dans le score)
    ctx = {"c1": {"energie_ok": True}, "c2": {}, "vix": 30, "no_news_gate": False}
    assert cb._calculate_fallback_score(ctx) == 0.0


def test_fallback_score_seuil_7():
    # bgc(3) + direction(2) + vix<18(2) = 7.0 ; reste faux
    ctx = {"c1": {"bgc_signal": True, "direction_ok": True, "direction": "LONG"},
           "c2": {}, "vix": 15, "no_news_gate": False, "risk": {"dd_today": 0.0}}
    assert cb._calculate_fallback_score(ctx) == 7.0


# ---- get_signal : fallback ----
def test_get_signal_fallback_signal_auto_interdit():
    r = cb.get_signal(_ctx(), kb_rules="(provisoire)", kb_provisoire=True)
    assert r["signal"] == "LONG"
    assert r["mode_auto_autorise"] is False        # Auto interdit
    assert r["confiance"] <= 65                     # plafond
    assert r["banniere"] == cb.BANNIERE_KB_PROVISOIRE
    assert r["kb_provisoire"] is True


def test_get_signal_confiance_jamais_sup_65():
    # score 10 -> confiance plafonnee a 65 (pas plus)
    r = cb.get_signal(_ctx(), kb_rules="(provisoire)")
    assert r["confiance"] == 65


def test_get_signal_fallback_attendre_si_score_faible():
    ctx = _ctx(c1={"bgc_signal": False, "direction_ok": False, "direction": "LONG"},
               c2={}, vix=30, no_news_gate=False)
    r = cb.get_signal(ctx, kb_rules="(provisoire)")
    assert r["signal"] == "ATTENDRE" and r["confiance"] == 0
    assert r["mode_auto_autorise"] is False


def test_get_signal_dd_eleve_bloque_meme_si_score_ok():
    ctx = _ctx(risk={"dd_today": 0.05})            # DD 5% >= 2% -> ATTENDRE
    r = cb.get_signal(ctx, kb_rules="(provisoire)")
    assert r["signal"] == "ATTENDRE"


# ---- Enforcement KB provisoire (chemin direct) ----
def test_enforce_kb_provisoire_force_auto_off_et_banniere():
    fake_success = {"signal": "LONG", "confiance": 90, "mode_auto_autorise": True}
    out = cb._enforce_kb_provisoire(fake_success, kb_provisoire=True)
    assert out["mode_auto_autorise"] is False
    assert out["banniere"] == cb.BANNIERE_KB_PROVISOIRE


def test_enforce_kb_non_provisoire_ne_touche_pas():
    res = {"signal": "LONG", "mode_auto_autorise": True}
    out = cb._enforce_kb_provisoire(res, kb_provisoire=False)
    assert out["mode_auto_autorise"] is True and "banniere" not in out


# ---- parse_claude_json ----
def test_parse_claude_json_bloc_fence():
    txt = 'Voici:\n```json\n{"signal": "ACHAT", "confiance": 80}\n```\nfin'
    assert cb.parse_claude_json(txt) == {"signal": "ACHAT", "confiance": 80}


def test_parse_claude_json_texte_autour():
    txt = 'bla {"a": 1} bla'
    assert cb.parse_claude_json(txt) == {"a": 1}


# ---- load_kb_rules ----
def test_load_kb_rules_renvoie_flag_provisoire():
    kb = cb.load_kb_rules()
    assert set(kb.keys()) == {"rules", "kb_provisoire", "banniere"}
    assert kb["kb_provisoire"] is True
    assert kb["banniere"] == cb.BANNIERE_KB_PROVISOIRE
    assert isinstance(kb["rules"], str)


def test_load_kb_rules_fichier_absent():
    kb = cb.load_kb_rules(kb_path=r"C:\trading-copilote\data\__inexistant__.json")
    assert "KB non chargee" in kb["rules"] and kb["kb_provisoire"] is True


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
