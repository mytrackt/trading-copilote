"""
data_reader.py -- Lecture des donnees NT8 et ATAS via JSON
Architecture : un fichier JSON par actif dans data/live/ (ou data/mock/ si USE_MOCK_DATA=True)
NE PAS importer pandas ici -- lecture JSON pure via atomic_writer.
"""
def read_nt8_asset(symbol: str) -> dict:
    """
    Lit le fichier JSON d'un actif NT8.
    Retourne {} si le fichier est absent ou corrompu.
    Passe par CB_NT8 (circuit breaker).
    """
    from engine.circuit_breaker import CB_NT8
    from utils.atomic_writer import safe_read_json
    from config.settings import get_nt8_path
    path = get_nt8_path(symbol)
    try:
        result = CB_NT8.call(lambda: safe_read_json(path))
    except Exception:
        return {}
    return result if isinstance(result, dict) else {}


def read_nt8_data() -> dict:
    """
    Retourne un dict {symbol: data} pour tous les actifs NT8.
    Exemple : {"GC": {...}, "HG": {...}, ...}
    """
    from config.settings import NT8_ASSETS
    return {s: read_nt8_asset(s) for s in NT8_ASSETS}


def read_atas_signals() -> dict:
    """
    Lit les signaux ATAS (un fichier global ATAS_signals.json).
    Retourne {} si absent ou corrompu.
    Passe par CB_ATAS (circuit breaker).
    """
    from engine.circuit_breaker import CB_ATAS
    from utils.atomic_writer import safe_read_json
    from config.settings import ATAS_DATA_PATH
    try:
        result = CB_ATAS.call(lambda: safe_read_json(ATAS_DATA_PATH))
    except Exception:
        return {}
    return result if isinstance(result, dict) else {}


def get_vix_delta_pct(minutes: int = 15) -> float:  # noqa: ARG001
    """
    Retourne la variation VIX (champ vix_delta_pct dans VX.json).
    Ce champ est calcule par NT8 (ou statique dans les mocks).
    Le parametre `minutes` est conserve pour compatibilite API.
    """
    try:
        data = read_nt8_asset("VX")
        return float(data.get("vix_delta_pct", 0.0))
    except Exception:
        return 0.0
