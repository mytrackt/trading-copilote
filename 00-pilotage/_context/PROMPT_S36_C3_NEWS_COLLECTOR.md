# PROMPT CLAUDE CODE — S36 · C3 · news_collector.py

> MODE CLAUDE CODE · Branche : `feature/phase-c-collectors`
> Commit cible : `feat(collector): news_collector — Finnhub + GDELT headlines`
> Exécuter APRÈS C2 (même branche)

---

## CONTEXTE

Collecteur d'actualités macro et marché — Finnhub + GDELT.
Cercles couverts : C5 (Sentiment/News) + C6 (Catalyseurs d'événements).
Clé API Finnhub requise dans `.env` : `FINNHUB_API_KEY` (plan gratuit suffisant).
GDELT : API publique, aucune clé requise.
Sortie : `C:\trading-copilote\data\news_data.json` (atomic write).

Ce collecteur alimente aussi le News Gate (filtrage NFP/FOMC/CPI).

---

## ÉTAPE 0 — Vérifier clé Finnhub dans .env

```
python -c "import os; print('FINNHUB:', 'PRESENT' if os.getenv('FINNHUB_API_KEY') else 'ABSENT — ajouter dans .env')"
```
Inscription gratuite : https://finnhub.io/register
En cas d'absence → le collecteur utilisera GDELT seul (mode dégradé, pas d'erreur crash).

---

## ÉTAPE 1 — Créer le fichier

Créer `C:\trading-copilote\05-saas\engine\news_collector.py` :

```python
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


def _fetch_finnhub_news(api_key: str, category: str = "general") -> list:
    """
    Récupère les dernières actualités Finnhub.
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
            return []
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
        return filtres[:MAX_ARTICLES]
    except Exception as e:
        logger.warning(f"[news_collector] Finnhub {category} : {e}")
        return []


def _fetch_gdelt_headlines() -> list:
    """
    Récupère les événements macro récents via GDELT v2 Doc API.
    Recherche sur les thèmes marché/économie.
    """
    params = {
        "query":  "economy OR gold OR oil OR copper OR wheat OR federal reserve OR inflation",
        "mode":   "artlist",
        "maxrecords": str(MAX_ARTICLES),
        "format": "json",
        "timespan": "1h",  # dernière heure
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
        ]
    except Exception as e:
        logger.warning(f"[news_collector] GDELT : {e}")
        return []


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

    if finnhub_key:
        articles += _fetch_finnhub_news(finnhub_key, category="general")
        time.sleep(1.0)  # Rate limiting Finnhub
        articles += _fetch_finnhub_news(finnhub_key, category="forex")
        logger.info(f"[news_collector] Finnhub : {len(articles)} articles filtrés")
    else:
        logger.warning("[news_collector] FINNHUB_API_KEY absente — mode dégradé GDELT uniquement")

    gdelt_articles = _fetch_gdelt_headlines()
    articles += gdelt_articles
    logger.info(f"[news_collector] GDELT : {len(gdelt_articles)} articles")

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
        "finnhub_disponible": bool(finnhub_key),
        "gdelt_disponible":   True,
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
            f"[news_collector] TERMINÉ — {data['count']} articles · "
            f"news_gate_events={data['news_gate_events']}"
        )
        return data
    except Exception as e:
        logger.error(f"[news_collector] ERREUR run_once : {e}")
        return {}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_once()
    # Afficher sans les articles complets pour lisibilité
    summary = {k: v for k, v in result.items() if k != "articles"}
    summary["articles_extrait"] = result.get("articles", [])[:3]
    print(json.dumps(summary, indent=2, default=str))
```

---

## ÉTAPE 2 — Lint

```
python -m py_compile 05-saas\engine\news_collector.py
```
→ 0 erreur

---

## ÉTAPE 3 — Test 1 cycle

```
cd 05-saas
python -c "
import sys; sys.path.insert(0,'.')
import engine.news_collector as n
r = n.collect_news()
print('count:', r.get('count',0))
print('finnhub_disponible:', r.get('finnhub_disponible'))
print('gdelt_disponible:', r.get('gdelt_disponible'))
print('news_gate_events:', r.get('news_gate_events'))
print('alerte_news_gate:', r.get('alerte_news_gate'))
if r.get('articles'):
    print('1er article:', r['articles'][0].get('headline','')[:80])
"
```
→ `count` ≥ 0 · `gdelt_disponible: True` · pas de crash

---

## ÉTAPE 4 — Vérifier l'écriture atomic

```
python -c "
import sys; sys.path.insert(0,'05-saas')
import engine.news_collector as n
r = n.run_once()
import json, os
from config.settings import NEWS_DATA_PATH
if os.path.exists(NEWS_DATA_PATH):
    d = json.load(open(NEWS_DATA_PATH, encoding='utf-8'))
    print('Fichier écrit OK — count:', d.get('count'), '· _collected_at:', d.get('_collected_at'))
else:
    print('ERREUR : fichier non créé')
"
```
→ fichier présent avec `count` et `_collected_at`

---

## COMMIT FINAL + PUSH de la branche

```
git add 05-saas\engine\news_collector.py
git commit -m "feat(collector): news_collector — Finnhub + GDELT headlines"
git push origin feature/phase-c-collectors
```

Ensuite, ouvrir une PR (ou merger directement sur main après validation) :
```
git checkout main
git merge feature/phase-c-collectors
git push origin main
```

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\engine\news_collector.py
```
Ou revenir en arrière sur la branche :
```
git checkout main
git branch -D feature/phase-c-collectors
```

---

## CHECKLIST FINALE PHASE C TRACK A

Après les 3 collecteurs :

- [ ] `cot_collector.py` : `python -m py_compile` → 0 erreur · 3 cycles sans crash
- [ ] `macro_collector.py` : `python -m py_compile` → 0 erreur · FRED répond
- [ ] `news_collector.py` : `python -m py_compile` → 0 erreur · GDELT répond
- [ ] `data/cot_data.json` créé
- [ ] `data/macro_data.json` créé
- [ ] `data/news_data.json` créé
- [ ] 21/21 tests `test_risk_guardrails.py` toujours PASS
- [ ] Branch `feature/phase-c-collectors` mergée sur `main`

---

*TRADEX-AI · S36 · C3 · 27/06/2026*
