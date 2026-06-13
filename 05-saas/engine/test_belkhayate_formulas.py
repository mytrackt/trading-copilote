"""
test_belkhayate_formulas.py -- Tests numeriques (donnees synthetiques) pour A1.
Verifie COG (endpoint fige + anti-repaint), Timing, et le stub Energie.
Runnable : `py test_belkhayate_formulas.py`  OU  `pytest`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import belkhayate_formulas as bf

TOL = 1e-6


def test_cog_linear_increasing_is_bleu():
    closes = [10 + 2 * i for i in range(10)]          # droite croissante parfaite
    p = bf.COGParams(lookback_N=10, degree=2)
    r = bf.cog_endpoint(closes, p)
    assert r is not None
    assert abs(r["cog"] - closes[-1]) < TOL           # endpoint = derniere valeur
    assert r["sigma"] < TOL                            # residus quasi nuls
    assert r["slope"] > 0 and r["couleur"] == "bleu"


def test_cog_linear_decreasing_is_rouge():
    closes = [100 - 3 * i for i in range(10)]
    p = bf.COGParams(lookback_N=10, degree=2)
    r = bf.cog_endpoint(closes, p)
    assert r["slope"] < 0 and r["couleur"] == "rouge"


def test_cog_bands_spacing_equals_k_sigma():
    closes = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]            # non ajustable en deg2 -> sigma > 0
    p = bf.COGParams(lookback_N=10, degree=2, k_bands=(1.618, 2.618, 4.236))
    r = bf.cog_endpoint(closes, p)
    assert r["sigma"] > 0
    for k in (1.618, 2.618, 4.236):
        assert abs((r["bandes"][f"+{k}"] - r["cog"]) - k * r["sigma"]) < TOL
        assert abs((r["cog"] - r["bandes"][f"-{k}"]) - k * r["sigma"]) < TOL
    # ordre des bandes
    assert r["bandes"]["+4.236"] > r["bandes"]["+2.618"] > r["bandes"]["+1.618"] > r["cog"]


def test_cog_insufficient_data_returns_none():
    assert bf.cog_endpoint([1, 2, 3], bf.COGParams(lookback_N=10)) is None


def test_cog_anti_repaint_value_is_frozen():
    closes = list(range(1, 21))
    p = bf.COGParams(lookback_N=5, degree=2)
    full = bf.cog_series_endpoint(closes, p)
    partial = bf.cog_series_endpoint(closes[:11], p)   # historique tronque a t=10
    assert full[10] is not None
    # la valeur en t=10 est IDENTIQUE qu'on connaisse ou non les barres futures -> pas de repaint
    assert abs(full[10]["cog"] - partial[10]["cog"]) < TOL


def test_timing_extremes_and_center():
    p = bf.TimingParams(lookback_n=5, scale=10.0)
    highs_top = [10, 10, 10, 10, 10]
    lows_top = [0, 0, 0, 0, 10]                        # median courant = 10 -> haut du range
    assert abs(bf.timing_oscillator(highs_top, lows_top, p) - 10.0) < TOL

    highs_mid = [10, 10, 10, 10, 5]
    lows_mid = [0, 0, 0, 0, 5]                         # median courant = 5 -> centre
    assert abs(bf.timing_oscillator(highs_mid, lows_mid, p) - 0.0) < TOL

    highs_bot = [10, 10, 10, 10, 0]
    lows_bot = [0, 0, 0, 0, 0]                         # median courant = 0 -> bas du range
    assert abs(bf.timing_oscillator(highs_bot, lows_bot, p) - (-10.0)) < TOL


def test_timing_insufficient_data_returns_none():
    assert bf.timing_oscillator([1, 2], [0, 1], bf.TimingParams(lookback_n=5)) is None


def test_energie_is_not_implemented():
    try:
        bf.energie([1], [1], [1])
    except NotImplementedError as e:
        assert "[NON DOCUMENTE]" in str(e)
    else:
        raise AssertionError("energie() aurait du lever NotImplementedError")


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
