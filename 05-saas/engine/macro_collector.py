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
# Dataset EIA "Weekly Stocks" -- filtrage par ID de serie exact (non ambigu).
EIA_BASE_URL  = "https://api.eia.gov/v2/petroleum/stoc/wstk/data/"

TIMEOUT_SEC = 15

# Series FRED ciblées
# ATTENTION : dtwexbgs_broad (panier large, ~120) != DXY/USDX ICE (~100).
# Ne pas comparer directement avec le futur DX de NT8 — indices differents.
FRED_SERIES = {
    "treasury_10y":             "DGS10",    # Rendement 10 ans US Treasury (quotidien)
    "fed_funds_rate":           "DFF",      # Taux Fed Funds effectif (quotidien)
    "dtwexbgs_broad":           "DTWEXBGS", # Dollar Trade-Weighted Broad Goods (PAS DXY)
    "inflation_expectation_5y": "T5YIFR",   # Inflation attendue 5 ans (quotidien)
    "m2_money_supply":          "M2SL",     # M2 money supply (mensuel -- delai ~6 semaines)
}


def _fetch_fred_series(series_id: str, api_key: str) -> tuple:
    """
    Retourne (valeur_float, date_observation_str) pour la derniere observation FRED.
    Retourne (None, None) en cas d'erreur ou de valeur manquante.
    La date permet de detecter les series avec delai de publication (ex: M2SL ~6 semaines).
    """
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
            return float(obs[0]["value"]), obs[0].get("date", "")
        return None, None
    except Exception as e:
        logger.warning(f"[macro_collector] FRED {series_id} : {e}")
        return None, None


def collect_fred(api_key: str) -> dict:
    """
    Collecte toutes les series FRED definies dans FRED_SERIES.
    Pour chaque serie 'name', ajoute aussi 'name_obs_date' (date de la derniere observation).
    Permet de detecter les series avec delai de publication (M2SL : ~6 semaines).
    """
    result = {}
    for name, series_id in FRED_SERIES.items():
        val, obs_date = _fetch_fred_series(series_id, api_key)
        result[name] = val
        result[f"{name}_obs_date"] = obs_date  # ex: "2026-06-20" ou None
        logger.info(f"[macro_collector] FRED {series_id} → {val} (obs: {obs_date})")
        time.sleep(0.5)  # Rate limiting FRED
    return result


def _fetch_eia_crude_inventory(api_key: str) -> float | None:
    """
    Retourne les inventaires petrole commerciaux US en milliers de barils (EIA, hebdo).
    Serie WCESTUS1 = "US Ending Stocks excluding SPR of Crude Oil" -- le chiffre commercial
    suivi par les traders (rapport hebdo EIA), hors reserve strategique (SPR).
    Verifie S36 : les facets product/process/duoarea renvoyaient WCRSTUS1 (TOTAL avec SPR,
    ~743M) au lieu de WCESTUS1 (hors SPR, ~412M) -> on filtre desormais par ID de serie exact.
    """
    params = {
        "api_key":  api_key,
        "data[0]":  "value",
        "facets[series][]": "WCESTUS1",
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
