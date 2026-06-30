"""
test_news_collector_p2.py -- Tests correctifs P2 (S45)
P2-1 : _detect_news_gate_events() retourne dicts avec timing pre/post/unknown
P2-2 : collect_news() inclut _collected_at dans le dict en memoire
"""
import sys
import os

# Chemin pour import config/settings sans avoir besoin de ANTHROPIC_API_KEY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "05-saas"))

from engine.news_collector import (
    _detect_event_timing,
    _detect_news_gate_events,
)


# ---------------------------------------------------------------------------
# Tests P2-1 : _detect_event_timing
# ---------------------------------------------------------------------------

def test_timing_pre_keyword_expected():
    assert _detect_event_timing("nfp expected to show 200k jobs") == "pre"

def test_timing_pre_keyword_ahead():
    assert _detect_event_timing("markets await fomc decision ahead of wednesday") == "pre"

def test_timing_pre_keyword_forecast():
    assert _detect_event_timing("cpi forecast higher than previous month") == "pre"

def test_timing_post_keyword_beat():
    assert _detect_event_timing("nfp beat expectations with 300k jobs") == "post"

def test_timing_post_keyword_released():
    assert _detect_event_timing("cpi data released showing 3.1% inflation") == "post"

def test_timing_post_keyword_shows():
    assert _detect_event_timing("fomc minutes shows hawkish tone") == "post"

def test_timing_unknown_no_keywords():
    assert _detect_event_timing("gold prices rise on geopolitical fears") == "unknown"

def test_timing_neutral_mention():
    assert _detect_event_timing("nfp and fomc in focus for traders") == "unknown"


# ---------------------------------------------------------------------------
# Tests P2-1 : _detect_news_gate_events retourne list[dict]
# ---------------------------------------------------------------------------

def test_detect_returns_list_of_dicts():
    articles = [{"headline": "NFP beats expectations", "url": "http://a.com"}]
    result = _detect_news_gate_events(articles)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], dict)
    assert result[0]["event"] == "NFP"
    assert "timing" in result[0]
    assert "headline" in result[0]

def test_detect_timing_post_beat():
    articles = [{"headline": "NFP beats expectations with 250k jobs", "url": "http://a.com"}]
    result = _detect_news_gate_events(articles)
    assert result[0]["timing"] == "post"

def test_detect_timing_pre_ahead():
    articles = [{"headline": "CPI upcoming: economists forecast 3%", "url": "http://b.com"}]
    result = _detect_news_gate_events(articles)
    assert result[0]["timing"] == "pre"

def test_detect_deduplication():
    """Deux articles sur NFP -> 1 seul entry dans result."""
    articles = [
        {"headline": "NFP beats 300k", "url": "http://a.com"},
        {"headline": "NFP jobs report released", "url": "http://b.com"},
    ]
    result = _detect_news_gate_events(articles)
    events = [d["event"] for d in result]
    assert events.count("NFP") == 1

def test_detect_multiple_events():
    articles = [
        {"headline": "NFP and CPI both released today", "url": "http://a.com"},
        {"headline": "FOMC minutes expected", "url": "http://b.com"},
    ]
    result = _detect_news_gate_events(articles)
    events = [d["event"] for d in result]
    assert "NFP" in events or "CPI" in events
    assert "FOMC" in events

def test_detect_empty_articles():
    assert _detect_news_gate_events([]) == []

def test_detect_no_relevant_articles():
    articles = [{"headline": "Gold rallies on safe haven demand", "url": "http://a.com"}]
    assert _detect_news_gate_events(articles) == []

def test_detect_headline_truncated_to_120():
    long_headline = "NFP " + "x" * 200
    articles = [{"headline": long_headline, "url": "http://a.com"}]
    result = _detect_news_gate_events(articles)
    assert len(result[0]["headline"]) <= 120


# ---------------------------------------------------------------------------
# Tests P2-1 backward compat : news_gate_events toujours list[str]
# ---------------------------------------------------------------------------

def test_backward_compat_news_gate_events_are_strings():
    """
    collect_news() doit retourner news_gate_events = list[str] (pas list[dict]).
    Test sans appel reseau : on verifie juste la structure de sortie.
    """
    # On mock directement _detect_news_gate_events en injectant via import
    import engine.news_collector as nc

    _orig = nc._detect_news_gate_events
    try:
        # Simuler detection : 1 event NFP post-event
        nc._detect_news_gate_events = lambda arts: [
            {"event": "NFP", "timing": "post", "headline": "NFP released"}
        ]
        # collect_news() appelle aussi Finnhub/GDELT, on mock aussi
        nc._fetch_finnhub_news = lambda *a, **kw: ([], True)
        nc._fetch_gdelt_headlines = lambda: ([], True)

        # Les mocks reseau suffisent — aucun appel reel fait
        data = nc.collect_news()

        # P2-1 backward compat : news_gate_events est list[str]
        assert isinstance(data["news_gate_events"], list)
        assert all(isinstance(e, str) for e in data["news_gate_events"])
        assert "NFP" in data["news_gate_events"]

        # P2-1 richer info : news_gate_details est list[dict]
        assert isinstance(data["news_gate_details"], list)
        assert data["news_gate_details"][0]["timing"] == "post"

        # P2-2 : _collected_at present dans le dict en memoire
        assert "_collected_at" in data
        assert data["_collected_at"].startswith("202")  # ISO format UTC

    finally:
        nc._detect_news_gate_events = _orig


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
