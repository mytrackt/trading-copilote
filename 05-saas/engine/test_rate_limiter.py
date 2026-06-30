"""
test_rate_limiter.py -- Tests unitaires RateLimiter
Couvre : reset journalier, quota, persistance, alerte, integration claude_brain.
"""
import json
import os
import sys
import tempfile
import pytest
from datetime import datetime, timezone

# Chemin absolu pour les imports
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(BASE_DIR))

from engine.rate_limiter import RateLimiter, RateLimitExceeded, MAX_CALLS_PER_DAY


# =============================================================================
# FIXTURE : RateLimiter avec fichier temp isole
# =============================================================================
@pytest.fixture
def limiter(tmp_path):
    """RateLimiter avec fichier de persistance temporaire (max=5 pour les tests)."""
    persist = str(tmp_path / "rate_limit.json")
    return RateLimiter(max_calls_per_day=5, persist_path=persist)


# =============================================================================
# T1 : Etat initial -- fichier absent
# =============================================================================
def test_initial_state(limiter):
    status = limiter.get_status()
    assert status["count"] == 0
    assert status["remaining"] == 5
    assert status["limit"] == 5
    today = datetime.now(timezone.utc).date().isoformat()
    assert status["date"] == today


# =============================================================================
# T2 : Increment normal
# =============================================================================
def test_increment_normal(limiter):
    limiter.check_and_increment()
    limiter.check_and_increment()
    status = limiter.get_status()
    assert status["count"] == 2
    assert status["remaining"] == 3


# =============================================================================
# T3 : Quota depasse leve RateLimitExceeded
# =============================================================================
def test_quota_exceeded(limiter):
    for _ in range(5):
        limiter.check_and_increment()
    with pytest.raises(RateLimitExceeded):
        limiter.check_and_increment()
    # Le compteur ne doit PAS depasser la limite
    assert limiter.get_status()["count"] == 5


# =============================================================================
# T4 : Persistance -- survie entre deux instances
# =============================================================================
def test_persistence(tmp_path):
    persist = str(tmp_path / "rate_limit.json")
    r1 = RateLimiter(max_calls_per_day=10, persist_path=persist)
    r1.check_and_increment()
    r1.check_and_increment()
    # Nouvelle instance, meme fichier
    r2 = RateLimiter(max_calls_per_day=10, persist_path=persist)
    assert r2.get_status()["count"] == 2


# =============================================================================
# T5 : Reset si nouveau jour
# =============================================================================
def test_reset_new_day(tmp_path):
    persist = str(tmp_path / "rate_limit.json")
    # Ecrire un fichier avec date d'hier
    old_data = {"date": "2020-01-01", "count": 9}
    with open(persist, "w", encoding="utf-8") as f:
        json.dump(old_data, f)
    r = RateLimiter(max_calls_per_day=10, persist_path=persist)
    status = r.get_status()
    today = datetime.now(timezone.utc).date().isoformat()
    assert status["date"] == today
    assert status["count"] == 0


# =============================================================================
# T6 : Fichier corrompu --> remise a zero sans exception
# =============================================================================
def test_corrupted_file(tmp_path):
    persist = str(tmp_path / "rate_limit.json")
    with open(persist, "w", encoding="utf-8") as f:
        f.write("NOT_JSON{{{{")
    r = RateLimiter(max_calls_per_day=10, persist_path=persist)
    status = r.get_status()
    assert status["count"] == 0


# =============================================================================
# T7 : Reset manuel
# =============================================================================
def test_reset(limiter):
    limiter.check_and_increment()
    limiter.check_and_increment()
    limiter.reset()
    assert limiter.get_status()["count"] == 0


# =============================================================================
# T8 : Constante MAX_CALLS_PER_DAY = 30 (D-S43-2)
# =============================================================================
def test_default_max():
    assert MAX_CALLS_PER_DAY == 30


# =============================================================================
# T9 : Atomic write -- fichier .tmp nettoye apres save
# =============================================================================
def test_atomic_write_no_tmp_left(tmp_path):
    persist = str(tmp_path / "rate_limit.json")
    r = RateLimiter(max_calls_per_day=5, persist_path=persist)
    r.check_and_increment()
    tmp_files = [f for f in os.listdir(tmp_path) if f.endswith(".tmp")]
    assert tmp_files == []


# =============================================================================
# T10 : get_status ne modifie pas le compteur
# =============================================================================
def test_get_status_no_side_effect(limiter):
    limiter.check_and_increment()
    limiter.get_status()
    limiter.get_status()
    assert limiter.get_status()["count"] == 1
