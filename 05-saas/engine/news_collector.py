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

# Mots-clés marché à surveiller
KEYWORDS_MARCHE = [
    "gold", "crude oil", "copper", "wheat",
    "dollar", "DXY", "federal reserve", "fed",
    "FOMC", "NFP", "CPI", "inflation", "interest rate",
]

MAX_ARTICLES = 20  # Limiter le volume de données


def _fetch_finnhub_news(api_key: str, category: str = "general") -> tuple:
    """
    Récupère les dernières actualités Finnhub.
    Retourne (list_articles, success_bool).
    success=False si l'appel HTTP échoue (réseau, 401, 500...).
    success=True si l'API répond correctement, même si 0 articles après filtrage.
    category : 'general' | 'forex' | 'crypto' | 'merger'
    """
    url = f"{FINNHUB_BASE_URL}/news"
    params = {
        "category": category,
        "token":    api_key,
    }
    try:
        resp = requests.get(url, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        articles = resp.json()
        if not isinstance(articles, list):
            return [], True  # Réponse valide mais format inattendu
        # Filtrer par pertinence (mots-clés)
        filtres = []
        kw_lower = [k.lower() for k in KEYWORDS_MARCHE]
        for art in articles[:50]:  # Limiter la recherche
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


def _fetch_gdelt_headlines() -> tuple:
    """
    Récupère les événements macro récents via GDELT v2 Doc API.
    Retourne (list_articles, success_bool).
    success=False si l'appel échoue (erreur réseau, SSL, 429, etc.).
    success=True uniquement si la réponse HTTP est valide, même si 0 articles.
    """
    params = {
        "query":  "economy OR gold OR oil OR copper OR wheat OR federal reserve OR inflation",
        "mode":   "artlist",
        "maxrecords": str(MAX_ARTICLES),
        "format": "json",
        "timespan": "4h",  # 4h (robustesse si collecteur tombe 1h+)
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


def _detect_news_gate_events(articles: list) -> list:
    """
    Détecte les événements critiques pour le News Gate (NFP, FOMC, CPI...).
    Retourne la liste des types d'événements détectés dans les headlines.
    """
    from config.settings import NEWS_EVENTS_CRITIQUES
    detectes = []
    for art in articles:
        headline_upper = (art.get("headline") or "").upper()
        for event in NEWS_EVENTS_CRITIQUES:
            if event in headline_upper and event not in detectes:
                detectes.append(event)
    return detectes


def collect_news() -> dict:
    """Collecte Finnhub (général + forex) + GDELT. Retourne un dict structuré."""
    from config.settings import FINNHUB_API_KEY
    finnhub_key = FINNHUB_API_KEY or os.getenv("FINNHUB_API_KEY", "")

    articles = []
    finnhub_ok = False

    if finnhub_key:
        general, ok1 = _fetch_finnhub_news(finnhub_key, category="general")
        time.sleep(1.0)  # Rate limiting Finnhub
        forex,   ok2 = _fetch_finnhub_news(finnhub_key, category="forex")
        articles += general + forex
        finnhub_ok = ok1 or ok2  # True si au moins 1 appel a réussi
        logger.info(f"[news_collector] Finnhub : {len(articles)} articles filtrés · ok={finnhub_ok}")
    else:
        logger.warning("[news_collector] FINNHUB_API_KEY absente — mode dégradé GDELT uniquement")

    gdelt_articles, gdelt_ok = _fetch_gdelt_headlines()
    articles += gdelt_articles
    logger.info(f"[news_collector] GDELT : {len(gdelt_articles)} articles · ok={gdelt_ok}")

    # Déduplication sur URL
    seen_urls = set()
    articles_uniques = []
    for art in articles:
        url = art.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            articles_uniques.append(art)

    news_gate_events = _detect_news_gate_events(articles_uniques)

    return {
        "articles":          articles_uniques[:MAX_ARTICLES],
        "count":             len(articles_uniques),
        "finnhub_disponible": finnhub_ok,   # True si au moins 1 appel Finnhub a réussi
        "gdelt_disponible":   gdelt_ok,    # True uniquement si l'appel GDELT a réussi
        "news_gate_events":   news_gate_events,
        "alerte_news_gate":   len(news_gate_events) > 0,
    }


def write_news(data: dict) -> None:
    """Écrit atomiquement dans data/news_data.json."""
    from utils.atomic_writer import atomic_write_json
    from config.settings import NEWS_DATA_PATH
    data["_collected_at"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(NEWS_DATA_PATH, data)
    logger.info(f"[news_collector] Écrit → {NEWS_DATA_PATH}")


def run_once() -> dict:
    """1 cycle complet : collect + write."""
    try:
        data = collect_news()
        write_news(data)
        logger.info(
            f"[news_collector] TERMINE --- {data['count']} articles · "
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
