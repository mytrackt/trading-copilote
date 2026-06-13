"""
test_signal_engine.py -- Tests deterministes pour A4 (signal_engine).
Verifie Etape 0, grille /10, NON-TRADE absolus, decisions, invalidations R8-R10,
et l'INDEPENDANCE du score vis-a-vis de l'Energie (volume et ATR comptes separement).
Runnable : `py test_signal_engine.py`  OU  `pytest`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import signal_engine as se


def _full_ctx_achat():
    """Setup ACHAT parfait -> score 10.0, decision SIGNAL."""
    return {
        "sens": "ACHAT",
        "trading_cog": {"GC": "bleu", "HG": "bleu", "CL": "bleu", "ZW": "bleu"},
        "confirmation": {"DX": True, "ES": True, "VX": True},
        "cog_couleur": "bleu",
        "timing": -6.0,
        "prix_bande_2_ou_3": True,
        "bandes_resserrees": True,
        "biais_h4_aligne": True,
        "volume_ratio": 1.5,
        "atr_ratio": 1.0,
        "structure_non_cassee": True,
        "news_clean": True,
        "rr": 2.5,
        "taille_contrats": 1,
        "in_news_window": False,
    }


def test_score_grid_sums_to_10():
    assert se.SCORE_MAX == 10.0


def test_full_setup_scores_10_and_signals():
    r = se.evaluate_signal(_full_ctx_achat())
    assert r["decision"] == "SIGNAL"
    assert r["score"] == 10.0
    assert r["validation_humaine_requise"] is True


def test_etape0_ko_trading():
    ctx = _full_ctx_achat()
    ctx["trading_cog"] = {"GC": "bleu", "HG": "bleu", "CL": "rouge", "ZW": "rouge"}  # 2/4
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "ETAPE_0_KO"


def test_etape0_ko_confirmation():
    ctx = _full_ctx_achat()
    ctx["confirmation"] = {"DX": True, "ES": False, "VX": False}  # 1/3
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "ETAPE_0_KO"


def test_cog_non_aligne_eliminatoire():
    ctx = _full_ctx_achat()
    ctx["cog_couleur"] = "rouge"  # contre le sens ACHAT (etape 0 passe encore via trading_cog)
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "COG_NON_ALIGNE"


def test_rr_insuffisant_bloque_meme_si_score_eleve():
    ctx = _full_ctx_achat()
    ctx["rr"] = 1.5
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "RR_INSUFFISANT"


def test_non_detecte_champ_manquant():
    ctx = _full_ctx_achat()
    ctx["timing"] = None
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "NON_DETECTE"
    assert "timing" in r["champs_manquants"]


def test_news_window_bloque():
    ctx = _full_ctx_achat()
    ctx["in_news_window"] = True
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "NEWS_WINDOW"


def test_taille_zero_bloque():
    ctx = _full_ctx_achat()
    ctx["taille_contrats"] = 0
    r = se.evaluate_signal(ctx)
    assert r["decision"] == "NON_TRADE" and r["raison"] == "TAILLE_ZERO"


def test_partial_setup_ignorer():
    ctx = _full_ctx_achat()
    ctx.update({
        "confirmation": {"DX": True, "ES": True, "VX": False},  # 2/3 -> etape 0 ok
        "timing": 0.0, "prix_bande_2_ou_3": False, "bandes_resserrees": False,
        "biais_h4_aligne": False, "volume_ratio": 1.0, "atr_ratio": 3.0,
        "structure_non_cassee": False, "news_clean": False,
    })
    r = se.evaluate_signal(ctx)
    assert r["score"] == 1.0 and r["decision"] == "IGNORER"   # seul confirmation_favorable = 1.0


def test_surveiller_band():
    ctx = _full_ctx_achat()
    ctx.update({
        "confirmation": {"DX": True, "ES": True, "VX": False},  # 2/3
        "timing": -6.0, "prix_bande_2_ou_3": True, "bandes_resserrees": False,
        "biais_h4_aligne": False, "volume_ratio": 1.0, "atr_ratio": 3.0,
        "structure_non_cassee": False, "news_clean": False,
    })
    r = se.evaluate_signal(ctx)
    assert r["score"] == 5.0 and r["decision"] == "SURVEILLER"  # prix 2 + timing 2 + conf 1


def test_score_independant_de_energie():
    """Volume OK mais ATR en choc : volume_ok=+1.0 ET atr_normal=0.0 INDEPENDAMMENT.
    Une formule Energie composite (Vol x ATR) annulerait les deux -> ici non."""
    ctx = _full_ctx_achat()
    ctx["volume_ratio"] = 1.5   # volume OK
    ctx["atr_ratio"] = 3.0      # choc -> atr_normal KO
    r = se.evaluate_signal(ctx)
    assert r["breakdown"]["volume_ok"] == 1.0
    assert r["breakdown"]["atr_normal"] == 0.0
    assert r["score"] == 9.5    # 10.0 - 0.5 (atr) seulement


def test_invalidation_r8_cog_change():
    out = se.check_invalidations({"tp1_atteint": False, "cog_couleur_entree": "bleu",
                                  "cog_couleur_courante": "rouge"})
    assert out["action_globale"] == "SORTIE_IMMEDIATE"
    assert any(code == "R8" for code, _, _ in out["invalidations"])


def test_invalidation_r9_bande3():
    out = se.check_invalidations({"cloture_au_dela_bande3": True})
    assert out["action_globale"] == "SORTIE_IMMEDIATE"
    assert any(code == "R9" for code, _, _ in out["invalidations"])


def test_invalidation_r10_news():
    out = se.check_invalidations({"news_majeure_imprevue": True})
    assert out["action_globale"] == "FERMETURE_OU_REDUCTION"
    assert any(code == "R10" for code, _, _ in out["invalidations"])


def test_no_invalidation():
    out = se.check_invalidations({"tp1_atteint": True, "cog_couleur_entree": "bleu",
                                  "cog_couleur_courante": "bleu"})
    assert out["action_globale"] == "AUCUNE" and out["invalidations"] == []


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
