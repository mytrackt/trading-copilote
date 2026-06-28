"""
cot_collector.py -- Collecteur COT (Commitments of Traders) CFTC
Phase C TRADEX-AI -- Cercle C3 Institutionnels
Source : CFTC API OData publique (pas de cle API)
Sortie : C:/trading-copilote/data/cot_data.json (atomic write)

ATTENTION : donnees hebdomadaires (publiees chaque vendredi 15h30 ET).
Usage : biais de fond uniquement -- INTERDIT comme trigger intraday.
"""
import os
import json
import time
import logging
import requests
from urllib.parse import urlencode, quote
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

# API CFTC OData v4 (verifie S36). Doc : https://publicreporting.cftc.gov/
# Table jun7-fc8e = "Legacy Combined" (Futures + Options) -- rapport COT hebdomadaire.
# NB : ce serveur Socrata exige l'encodage des espaces en %20 (le '+' renvoie 400).
CFTC_API_BASE = "https://publicreporting.cftc.gov/api/odata/v4"
CFTC_TABLE    = "jun7-fc8e"

# Correspondance actif NT8 -> code contrat CFTC (cftc_contract_market_code).
# Le CODE est STABLE et NON AMBIGU ; le nom (market_and_exchange_names) varie dans
# le temps et 'contains(nom)' attrape les mauvais contrats (MICRO GOLD, WTI ICE, etc.).
# Codes verifies S36 via l'API CFTC :
#   GC 088691 = GOLD - COMMODITY EXCHANGE INC.
#   HG 085692 = COPPER- #1 - COMMODITY EXCHANGE INC.
#   CL 067651 = WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (WTI NYMEX physique)
#               (nom historique avant 2022 : "CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE")
#   ZW 001602 = WHEAT-SRW - CHICAGO BOARD OF TRADE
CFTC_CONTRACT_CODES = {
    "GC": "088691",
    "HG": "085692",
    "CL": "067651",
    "ZW": "001602",
}

TIMEOUT_SEC = 15


def _fetch_cot_for_market(contract_code: str) -> dict | None:
    """
    Récupère les dernières données COT CFTC pour un code contrat.
    Retourne None si l'appel échoue ou si aucune donnée trouvée.
    """
    params = {
        "$filter": f"cftc_contract_market_code eq '{contract_code}'",
        "$orderby": "report_date_as_yyyy_mm_dd desc",
        "$top": "1",
        "$select": (
            "market_and_exchange_names,"
            "cftc_contract_market_code,"
            "report_date_as_yyyy_mm_dd,"
            "noncomm_positions_long_all,"
            "noncomm_positions_short_all,"
            "comm_positions_long_all,"
            "comm_positions_short_all,"
            "change_in_noncomm_long_all,"
            "change_in_noncomm_short_all"
        ),
    }
    # encodage manuel : space -> %20 (requis par le serveur Socrata CFTC)
    url = f"{CFTC_API_BASE}/{CFTC_TABLE}?{urlencode(params, quote_via=quote)}"
    try:
        resp = requests.get(url, timeout=TIMEOUT_SEC)
        resp.raise_for_status()
        data = resp.json()
        values = data.get("value", [])
        if not values:
            logger.warning(f"[cot_collector] Aucune donnée pour code='{contract_code}'")
            return None
        return values[0]
    except requests.RequestException as e:
        logger.error(f"[cot_collector] Erreur CFTC API pour code '{contract_code}' : {e}")
        return None


def collect_cot() -> dict:
    """
    Collecte les données COT pour les 4 actifs trading : GC, HG, CL, ZW.
    Retourne un dict structuré avec positions nettes et biais.
    """
    result = {}
    for symbol, contract_code in CFTC_CONTRACT_CODES.items():
        raw = _fetch_cot_for_market(contract_code)
        time.sleep(1.0)  # Rate limiting CFTC API
        if raw is None:
            result[symbol] = {
                "disponible": False,
                "erreur": "Aucune donnée CFTC",
            }
            continue

        long_nc  = int(raw.get("noncomm_positions_long_all",  0) or 0)
        short_nc = int(raw.get("noncomm_positions_short_all", 0) or 0)
        net      = long_nc - short_nc
        change_l = int(raw.get("change_in_noncomm_long_all",  0) or 0)
        change_s = int(raw.get("change_in_noncomm_short_all", 0) or 0)
        net_change = change_l - change_s

        result[symbol] = {
            "disponible":       True,
            "date_rapport":     raw.get("report_date_as_yyyy_mm_dd", ""),
            "long_nc":          long_nc,
            "short_nc":         short_nc,
            "net_speculateur":  net,
            "variation_nette":  net_change,
            "biais":            "LONG" if net > 0 else "SHORT" if net < 0 else "NEUTRE",
            "biais_croissant":  net_change > 0,
            "nom_cftc":         raw.get("market_and_exchange_names", ""),
        }
        logger.info(f"[cot_collector] {symbol} — net={net:+d} · biais={result[symbol]['biais']}")

    return result


def write_cot(data: dict) -> None:
    """Écrit atomiquement dans data/cot_data.json."""
    from utils.atomic_writer import atomic_write_json
    from config.settings import COT_DATA_PATH
    data["_collected_at"] = datetime.now(timezone.utc).isoformat()
    atomic_write_json(COT_DATA_PATH, data)
    logger.info(f"[cot_collector] Écrit → {COT_DATA_PATH}")


def run_once() -> dict:
    """1 cycle complet : collect + write."""
    try:
        data = collect_cot()
        write_cot(data)
        actifs_ok = sum(1 for v in data.values() if isinstance(v, dict) and v.get("disponible"))
        logger.info(f"[cot_collector] TERMINÉ — {actifs_ok}/4 actifs disponibles")
        return data
    except Exception as e:
        logger.error(f"[cot_collector] ERREUR run_once : {e}")
        return {}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = run_once()
    print(json.dumps(result, indent=2, default=str))
