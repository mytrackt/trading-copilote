"""
data_collector_runner.py -- Orchestrateur Phase C TRADEX-AI
Exécute les 3 collecteurs (COT / Macro / News) en séquence.
Chaque collecteur est indépendant : une erreur n'en bloque pas les autres.

Logique de fraîcheur :
  - COT   : rafraîchit si données > 24h (CFTC publie 1x/semaine)
  - Macro : rafraîchit si données > 24h (FRED/EIA : quotidien/hebdo)
  - News  : rafraîchit si données > 15min (Finnhub temps réel)

Usage :
  Importé par claude_brain.py via load_phase_c_data()
  Exécutable directement : python data_collector_runner.py [--force]
"""
import os
import sys
import json
import logging
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

# Seuils de fraîcheur (secondes)
MAX_AGE_COT_SEC   = 86_400   # 24h — données hebdo CFTC
MAX_AGE_MACRO_SEC = 86_400   # 24h — données quotidiennes FRED/EIA
MAX_AGE_NEWS_SEC  =    900   # 15min — news temps réel Finnhub


def _data_age_seconds(data_path: str) -> float | None:
    """
    Retourne l'âge en secondes du fichier JSON (via champ _collected_at).
    Retourne None si le fichier est absent, illisible, ou sans _collected_at.
    """
    if not os.path.exists(data_path):
        return None
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        collected_at = data.get("_collected_at")
        if not collected_at:
            return None
        ts = datetime.fromisoformat(collected_at)
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - ts).total_seconds()
    except Exception as e:
        logger.warning(f"[runner] Impossible de lire l'âge de {data_path} : {e}")
        return None


def _needs_refresh(data_path: str, max_age_sec: float) -> bool:
    """True si le fichier est absent ou périmé (> max_age_sec)."""
    age = _data_age_seconds(data_path)
    if age is None:
        return True   # absent → refresh obligatoire
    return age > max_age_sec


def run_all(force: bool = False) -> dict:
    """
    Exécute les 3 collecteurs Phase C en séquence.

    force=True → ignore les seuils de fraîcheur, recollecte tout.

    Retourne :
    {
        "cot"    : dict (résultat cot_collector) ou {} si erreur/skipped,
        "macro"  : dict (résultat macro_collector) ou {},
        "news"   : dict (résultat news_collector) ou {},
        "errors" : [str, ...],
        "skipped": [str, ...],
        "_run_at": ISO timestamp
    }
    """
    # Import lazy des settings (évite l'import circulaire au niveau module)
    sys.path.insert(0, BASE_DIR)
    from config.settings import COT_DATA_PATH, MACRO_DATA_PATH, NEWS_DATA_PATH

    results: dict = {"errors": [], "skipped": []}

    # ---- COT ----
    try:
        if force or _needs_refresh(COT_DATA_PATH, MAX_AGE_COT_SEC):
            from engine.cot_collector import run_once as _cot_run
            logger.info("[runner] COT : collecte en cours...")
            results["cot"] = _cot_run()
            actifs_ok = sum(
                1 for v in results["cot"].values()
                if isinstance(v, dict) and v.get("disponible")
            )
            logger.info(f"[runner] COT terminé — {actifs_ok}/4 actifs disponibles")
        else:
            age_h = (_data_age_seconds(COT_DATA_PATH) or 0) / 3600
            logger.info(f"[runner] COT skipped (données fraîches, âge={age_h:.1f}h)")
            results["skipped"].append("COT")
            results["cot"] = {}
    except Exception as e:
        logger.error(f"[runner] COT ERREUR : {e}")
        results["errors"].append(f"COT: {e}")
        results["cot"] = {}

    # ---- MACRO ----
    try:
        if force or _needs_refresh(MACRO_DATA_PATH, MAX_AGE_MACRO_SEC):
            from engine.macro_collector import run_once as _macro_run
            logger.info("[runner] MACRO : collecte en cours...")
            results["macro"] = _macro_run()
            logger.info("[runner] MACRO terminé")
        else:
            age_h = (_data_age_seconds(MACRO_DATA_PATH) or 0) / 3600
            logger.info(f"[runner] MACRO skipped (données fraîches, âge={age_h:.1f}h)")
            results["skipped"].append("MACRO")
            results["macro"] = {}
    except Exception as e:
        logger.error(f"[runner] MACRO ERREUR : {e}")
        results["errors"].append(f"MACRO: {e}")
        results["macro"] = {}

    # ---- NEWS ----
    try:
        if force or _needs_refresh(NEWS_DATA_PATH, MAX_AGE_NEWS_SEC):
            from engine.news_collector import run_once as _news_run
            logger.info("[runner] NEWS : collecte en cours...")
            results["news"] = _news_run()
            count = results["news"].get("count", 0)
            gate = results["news"].get("news_gate_events", [])
            logger.info(f"[runner] NEWS terminé — {count} articles, gate_events={gate}")
        else:
            age_m = (_data_age_seconds(NEWS_DATA_PATH) or 0) / 60
            logger.info(f"[runner] NEWS skipped (données fraîches, âge={age_m:.1f}min)")
            results["skipped"].append("NEWS")
            results["news"] = {}
    except Exception as e:
        logger.error(f"[runner] NEWS ERREUR : {e}")
        results["errors"].append(f"NEWS: {e}")
        results["news"] = {}

    results["_run_at"] = datetime.now(timezone.utc).isoformat()

    n_ok     = 3 - len(results["errors"]) - len(results["skipped"])
    n_skip   = len(results["skipped"])
    n_err    = len(results["errors"])
    logger.info(
        f"[runner] Bilan : {n_ok} collectés | {n_skip} skipped | {n_err} erreurs"
    )
    return results


def load_current_phase_c() -> dict:
    """
    Charge les données Phase C depuis les fichiers JSON existants (sans recollecte).
    Retourne {"cot": dict, "macro": dict, "news": dict}.
    Utilisé par claude_brain.py avant l'appel Claude API.
    """
    sys.path.insert(0, BASE_DIR)
    from config.settings import COT_DATA_PATH, MACRO_DATA_PATH, NEWS_DATA_PATH

    data = {"cot": {}, "macro": {}, "news": {}}

    for key, path in (("cot", COT_DATA_PATH), ("macro", MACRO_DATA_PATH), ("news", NEWS_DATA_PATH)):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data[key] = json.load(f)
            except Exception as e:
                logger.warning(f"[runner] Impossible de charger {path} : {e}")
        else:
            logger.warning(f"[runner] Fichier absent : {path}")

    return data


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    force_flag = "--force" in sys.argv
    print(f"\n{'='*60}")
    print(f"DATA COLLECTOR RUNNER — force={force_flag}")
    print(f"{'='*60}\n")
    result = run_all(force=force_flag)
    print("\n--- RÉSUMÉ ---")
    print(f"Collecteurs actifs : {[k for k in ('cot','macro','news') if result.get(k)]}")
    print(f"Skipped            : {result.get('skipped', [])}")
    print(f"Erreurs            : {result.get('errors', [])}")
    print(f"Run at             : {result.get('_run_at', '')}")
