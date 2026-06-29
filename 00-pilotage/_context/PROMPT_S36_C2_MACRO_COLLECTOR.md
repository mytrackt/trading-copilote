# PROMPT CLAUDE CODE — S36 · C2 · macro_collector.py

> MODE CLAUDE CODE · Branche : `feature/phase-c-collectors`
> Commit cible : `feat(collector): macro_collector — FRED + EIA macro data`
> Exécuter APRÈS C1 (même branche)

---

## CONTEXTE

Collecteur macro — données FRED (Federal Reserve) + EIA (Energy Information Administration).
Cercles couverts : C4 (Macro/Monétaire) + C7 (Inter-marchés).
Clés API requises dans `.env` : `FRED_API_KEY` (gratuit) + `EIA_API_KEY` (gratuit).
Sortie : `C:\trading-copilote\data\macro_data.json` (atomic write).

---

## ÉTAPE 0 — Vérifier les clés API dans .env

```
python -c "
import os
fred = os.getenv('FRED_API_KEY','')
eia  = os.getenv('EIA_API_KEY','')
print('FRED_API_KEY:', 'PRESENT' if fred else 'ABSENT — ajouter dans .env')
print('EIA_API_KEY: ', 'PRESENT' if eia  else 'ABSENT — ajouter dans .env')
"
```

Si une clé est absente → stopper et ajouter dans `.env` avant de continuer.
- FRED : https://fred.stlouisfed.org/docs/api/api_key.html (gratuit)
- EIA  : https://www.eia.gov/opendata/register.php (gratuit)

---

## ÉTAPE 1 — Créer le fichier

Créer `C:\trading-copilote\05-saas\engine\macro_collector.py` :

```python
"""
macro_collector.py -- Collecteur macro FRED + EIA
Phase C TRADEX-AI -- Cercles C4 (Macro) + C7 (Inter-marches)
Sources :
  - FRED (Federal Reserve Bank of St. Louis) : taux, dollar, inflation
  - EIA  (US Energy Information Administration) : inventaires petrole
Sortie : C:/trading-copilote/data/macro_data.json (atomic write)

Frequence recommandee : 1x par jour (donnees quotidiennes/hebdomadaires).
"""
import os
import json
import time
import logging
import requests
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

FRED_BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
EIA_BASE_URL  = "https://api.eia.gov/v2/petroleum/sum/sndw/data/"

TIMEOUT_SEC = 15

# Series FRED ciblées
FRED_SERIES = {
    "treasury_10y":            "DGS10",     # Rendement 10 ans US Treasury
    "fed_funds_rate":          "DFF",        # Taux Fed Funds effectif (quotidien)
    "dollar_index_fred":       "DTWEXBGS",   # Dollar Index Trade-Weighted (proxy DXY)
    "inflation_expectation_5y": "T5YIFR",    # Inflation attendue 5 ans (breakeven)
    "m2_money_supply":         "M2SL",       # M2 (mensuel -- delai publication)
}


def _fetch_fred_series(series_id: str, api_key: str) -> float | None:
    """Retourne la dernière observation d'une série FRED (valeur numérique)."""
    params = {
        "series_id":    series_id,
        "api_key":      api_key,
        "file_type":    "json",
        "sort_order":   "desc",
        "limit":        "1",
        "observation_start": "2020-01-01",
    }
    try:
        resp = requests.get(FRED_BASE_URL, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        obs = resp.json().get("observations", [])
        if obs and obs[0].get("value") not in (".", None, ""):
            return float(obs[0]["value"])
        return None
    except Exception as e:
        logger.warning(f"[macro_collector] FRED {series_id} : {e}")
        return None


def collect_fred(api_key: str) -> dict:
    """Collecte toutes les séries FRED définies dans FRED_SERIES."""
    result = {}
    for name, series_id in FRED_SERIES.items():
        val = _fetch_fred_series(series_id, api_key)
        result[name] = val
        logger.info(f"[macro_collector] FRED {series_id} → {val}")
        time.sleep(0.5)  # Rate limiting FRED
    return result


def _fetch_eia_crude_inventory(api_key: str) -> float | None:
    """
    Retourne les inventaires pétrole US en barils (EIA, hebdomadaire).
    Serie : PET.WCESTUS1.W (US Ending Stocks of Crude Oil, weekly)
    ⚠️ À VÉRIFIER : paramètres API EIA v2 exacts
    """
    params = {
        "api_key":  api_key,
        "data[0]":  "value",
        "facets[product][]": "EPC0",
        "facets[process][]": "SAE",
        "facets[duoarea][]": "NUS",
        "frequency": "weekly",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "length": "1",
    }
    try:
        resp = requests.get(EIA_BASE_URL, params=params, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        data = resp.json().get("response", {}).get("data", [])
        if data:
            return float(data[0].get("value", 0))
        return None
    except Exception as e:
        logger.warning(f"[macro_collector] EIA crude inventory : {e}")
        return None


def collect_macro() -> dict:
    """Collecte FRED + EIA. Retourne un dict structuré."""
    from config.settings import FRED_API_KEY, EIA_API_KEY

    fred_key = FRED_API_KEY or os.getenv("FRED_API_KEY", "")
    eia_key  = EIA_API_KEY  or os.getenv("EIA_API_KEY", "")

    result = {
        "fred_disponible": bool(fred_key),
        "eia_disponible":  bool(eia_key),
    }

    if fred_key:
        fred_data = collect_fred(fred_key)
        result.update(fred_data)
    else:
        logger.warning("[macro_collector] FRED_API_KEY manquante — skip FRED")

    if eia_key:
        crude_inv = _fetch_eia_crude_inventory(eia_key)
        result["crude_inventory_barils"] = crude_inv
        logger.info(f"[macro_collector] EIA crude inventory → {crude_inv}")
    else:
        logger.warning("[macro_collector] EIA_API_KEY manquante — skip EIA")

    return result


def write_macro(data: dict) -> None:
    """Écrit atomiquement dans data/macro_data.json."""
    from utils.atomic_writer import atomic_write_json
    from config.settings import MACRO_DATA_PATH
    data["_collected_at"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(MACRO_DATA_PATH, data)
    logger.info(f"[macro_collector] Écrit → {MACRO_DATA_PATH}")


def run_once() -> dict:
    """1 cycle complet : collect + write."""
    try:
        data = collect_macro()
        write_macro(data)
        champs_valides = sum(1 for v in data.values() if v is not None and not isinstance(v, bool))
        logger.info(f"[macro_collector] TERMINÉ — {champs_valides} champs valides")
        return data
    except Exception as e:
        logger.error(f"[macro_collector] ERREUR run_once : {e}")
        return {}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_once()
    print(json.dumps(result, indent=2, default=str))
```

---

## ÉTAPE 2 — Lint

```
python -m py_compile 05-saas\engine\macro_collector.py
```
→ 0 erreur

---

## ÉTAPE 3 — Test (avec clés API présentes dans .env)

```
cd 05-saas
python -c "
import sys; sys.path.insert(0,'.')
import engine.macro_collector as m
r = m.collect_macro()
print('treasury_10y:', r.get('treasury_10y'))
print('fed_funds_rate:', r.get('fed_funds_rate'))
print('dollar_index_fred:', r.get('dollar_index_fred'))
print('fred_disponible:', r.get('fred_disponible'))
print('eia_disponible:', r.get('eia_disponible'))
"
```
→ `treasury_10y` doit être un float (ex: 4.25) si FRED_API_KEY présente

Si les clés sont absentes → les champs retournent None, pas d'erreur crash. OK.

---

## ÉTAPE 4 — Vérifier l'écriture atomic

```
python -c "
import sys; sys.path.insert(0,'05-saas')
import engine.macro_collector as m
r = m.run_once()
import json, os
from config.settings import MACRO_DATA_PATH
if os.path.exists(MACRO_DATA_PATH):
    d = json.load(open(MACRO_DATA_PATH, encoding='utf-8'))
    print('Fichier écrit OK — champs:', list(d.keys()))
else:
    print('ERREUR : fichier non créé')
"
```
→ doit afficher les champs + `_collected_at`

---

## COMMIT

```
git add 05-saas\engine\macro_collector.py
git commit -m "feat(collector): macro_collector — FRED + EIA macro data"
```
(Ne pas push encore — attendre C3)

---

## ROLLBACK SI ÉCHEC

```
git checkout -- 05-saas\engine\macro_collector.py
```

---

*TRADEX-AI · S36 · C2 · 27/06/2026*
