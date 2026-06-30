"""
news_collector.py -- Collecteur actualites macro/marche
Phase C TRADEX-AI -- Cercles C5 (Sentiment) + C6 (Catalyseurs)
Sources :
  - Finnhub (FINNHUB_API_KEY dans .env) : news marche en temps reel
  - GDELT   (API publique, pas de cle) : evenements macro monde
Sortie : C:/trading-copilote/data/news_data.json (atomic write)

Frequence recommandee : toutes les 5 minutes en session.
Rate limit Finnhub gratuit : 60 req/min.
"""
import os
import json
import time
import logging
import requests
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

FINNHUB_BASE_URL = "https://finnhub.io/api/v1"
GDELT_BASE_URL   = "https://api.gdeltproject.org/api/v2/doc/doc"

TIMEOUT_SEC = 10

KEYWORDS_MARCHE = [
    "gold", "crude oil", "copper", "wheat",
    "dollar", "DXY", "federal reserve", "fed",
    "FOMC", "NFP", "CPI", "inflation", "interest rate",
]

MAX_ARTICLES = 20

_PRE_KEYWORDS = {
    "preview", "ahead", "upcoming", "expected", "forecast", "before",
    "anticipat", "await", "watch", "scheduled", "outlook", "estimate",
    "consensus", "predict", "will report", "prepare", "wednesday",
}
_POST_KEYWORDS = {
    "released", "beat", "miss", "fell", "rose", "came in", "result",
    "higher than", "lower than", "above estimate", "below estimate",
    "surpris", "final", "revised", "shows", "revealed", "reported",
    "actual", "print", "reading", "comes in", "posts",
}


def _fetch_finnhub_news(api_key, category="general"):
    url = f"{FINNHUB_BASE_URL}/news"
    params = {"category": category, "token": api_key}
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        articles = resp.json()
        if not isinstance(articles, list):
            return [], True
        filtres = []
        kw_lower = [k.lower() for k in KEYWORDS_MARCHE]
        for art in articles[:50]:
            headline = (art.get("headline") or "").lower()
            summary  = (art.get("summary")  or "").lower()
            if any(kw in headline or kw in summary for kw in kw_lower):
                filtres.append({
                    "headline":  art.get("headline", ""),
                    "source":    art.get("source", ""),
                    "datetime":  art.get("datetime", 0),
                    "url":       art.get("url", ""),
                    "origine":   "finnhub",
                    "categorie": category,
                })
        return filtres[:MAX_ARTICLES], True
    except Exception as e:
        logger.warning(f"[news_collector] Finnhub {category} : {e}")
        return [], False


def _fetch_gdelt_headlines():
    params = {
        "query":      "economy OR gold OR oil OR copper OR wheat OR federal reserve OR inflation",
        "mode":       "artlist",
        "maxrecords": str(MAX_ARTICLES),
        "format":     "json",
        "timespan":   "4h",
    }
    try:
        resp = requests.get(GDELT_BASE_URL, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        data = resp.json()
        articles = data.get("articles", [])
        return [
            {
                "headline":  art.get("title", ""),
                "source":    art.get("domain", ""),
                "datetime":  art.get("seendate", ""),
                "url":       art.get("url", ""),
                "origine":   "gdelt",
                "categorie": "macro",
            }
            for art in articles[:MAX_ARTICLES]
        ], True
    except Exception as e:
        logger.warning(f"[news_collector] GDELT : {e}")
        return [], False


def _detect_event_timing(headline_lower):
    """
    Retourne pre / post / unknown selon les mots-cles.
    P2-1 correctif S45.
    """
    if any(kw in headline_lower for kw in _PRE_KEYWORDS):
        return "pre"
    if any(kw in headline_lower for kw in _POST_KEYWORDS):
        return "post"
    return "unknown"


def _detect_news_gate_events(articles):
    """
    Detecte les evenements critiques NFP/FOMC/CPI/GDP/JOLTS/PPI.
    Retourne list[dict] : [{"event": "NFP", "timing": "pre|post|unknown", "headline": "..."}]
    Deduplique par event (1er match gagne).
    P2-1 correctif S45.
    """
    from config.settings import NEWS_EVENTS_CRITIQUES
    detectes = {}
    for art in articles:
        headline = art.get("headline") or ""
        headline_upper = headline.upper()
        headline_lower = headline.lower()
        for event in NEWS_EVENTS_CRITIQUES:
            if event in headline_upper and event not in detectes:
                detectes[event] = {
                    "event":    event,
                    "timing":   _detect_event_timing(headline_lower),
                    "headline": headline[:120],
                }
    return list(detectes.values())


def collect_news():
    """Collecte Finnhub (general + forex) + GDELT. Retourne un dict structure."""
    from config.settings import FINNHUB_API_KEY
    finnhub_key = FINNHUB_API_KEY or os.getenv("FINNHUB_API_KEY", "")

    articles = []
    finnhub_ok = False

    if finnhub_key:
        general, ok1 = _fetch_finnhub_news(finnhub_key, category="general")
        time.sleep(1.0)
        forex, ok2 = _fetch_finnhub_news(finnhub_key, category="forex")
        articles += general + forex
        finnhub_ok = ok1 or ok2
        logger.info(f"[news_collector] Finnhub : {len(articles)} articles filtres ok={finnhub_ok}")
    else:
        logger.warning("[news_collector] FINNHUB_API_KEY absente -- mode degrade GDELT uniquement")

    gdelt_articles, gdelt_ok = _fetch_gdelt_headlines()
    articles += gdelt_articles
    logger.info(f"[news_collector] GDELT : {len(gdelt_articles)} articles ok={gdelt_ok}")

    seen_urls = set()
    articles_uniques = []
    for art in articles:
        url = art.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            articles_uniques.append(art)

    detected = _detect_news_gate_events(articles_uniques)
    news_gate_events = [d["event"] for d in detected]
    news_gate_details = detected

    return {
        "articles":           articles_uniques[:MAX_ARTICLES],
        "count":              len(articles_uniques),
        "finnhub_disponible": finnhub_ok,
        "gdelt_disponible":   gdelt_ok,
        "news_gate_events":   news_gate_events,
        "news_gate_details":  news_gate_details,
        "alerte_news_gate":   len(news_gate_events) > 0,
        "_collected_at":      datetime.now(timezone.utc).isoformat(),
    }


def write_news(data):
    """Ecrit atomiquement dans data/news_data.json."""
    from utils.atomic_writer import atomic_write_json
    from config.settings import NEWS_DATA_PATH
    data["_collected_at"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(NEWS_DATA_PATH, data)
    logger.info(f"[news_collector] Ecrit -> {NEWS_DATA_PATH}")


def run_once():
    """1 cycle complet : collect + write."""
    try:
        data = collect_news()
        write_news(data)
        logger.info(
            f"[news_collector] TERMINE --- {data['count']} articles "
            f"news_gate_events={data['news_gate_events']}"
        )
        return data
    except Exception as e:
        logger.error(f"[news_collector] ERREUR run_once : {e}")
        return {}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_once()
    summary = {k: v for k, v in result.items() if k != "articles"}
    summary["articles_extrait"] = result.get("articles", [])[:3]
    import json
    print(json.dumps(summary, indent=2, default=str))
