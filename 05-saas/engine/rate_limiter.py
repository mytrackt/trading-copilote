"""
rate_limiter.py -- Compteur d'appels API journalier TRADEX-AI
Prerequis obligatoire de Boucle 1 (scheduler automatique) -- D-S43-2.

Protege contre la facture API incontrôlee : MAX_CALLS_PER_DAY = 30.
Persistance dans data/rate_limit.json (atomic write -- survit aux redemarrages).
Reset automatique a minuit UTC.

Usage :
    from .rate_limiter import RATE_LIMITER, RateLimitExceeded
    RATE_LIMITER.check_and_increment()   # leve RateLimitExceeded si quota atteint
    RATE_LIMITER.get_status()            # {"date", "count", "remaining", "limit"}
"""
import json
import logging
import os
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)

# =============================================================================
# CONSTANTES
# =============================================================================
MAX_CALLS_PER_DAY: int = 30          # D-S43-2 : plafond journalier
ALERT_THRESHOLD: int = 5             # Alerte quand <= 5 appels restants


class RateLimitExceeded(Exception):
    """Quota journalier d'appels Claude API atteint."""


# =============================================================================
# CLASSE RATE LIMITER
# =============================================================================
class RateLimiter:
    """
    Compteur persistant d'appels API avec reset UTC quotidien.

    - Persistance : data/rate_limit.json (atomic write via tempfile + os.replace)
    - Thread-safety : non requise (moteur mono-thread par conception)
    - Reset : compare date UTC du jour au champ "date" du fichier
    """

    def __init__(self, max_calls_per_day: int = MAX_CALLS_PER_DAY,
                 persist_path: str = None):
        self.max_calls = max_calls_per_day
        if persist_path is None:
            # data/ est un niveau au-dessus de 05-saas/
            data_dir = os.path.join(os.path.dirname(BASE_DIR), "data")
            persist_path = os.path.join(data_dir, "rate_limit.json")
        self.persist_path = persist_path

    # ------------------------------------------------------------------
    # API PUBLIQUE
    # ------------------------------------------------------------------

    def check_and_increment(self) -> None:
        """
        Verifie le quota et incremente le compteur.
        Leve RateLimitExceeded si MAX_CALLS_PER_DAY atteint.
        Emet un WARNING si <= ALERT_THRESHOLD appels restants apres increment.
        """
        data = self._load()
        data = self._reset_if_new_day(data)

        if data["count"] >= self.max_calls:
            msg = (
                f"[RateLimit] Quota journalier atteint : {data['count']}/{self.max_calls} "
                f"appels Claude API aujourd'hui ({data['date']} UTC). "
                "Reprendra demain a minuit UTC."
            )
            logger.error(msg)
            raise RateLimitExceeded(msg)

        data["count"] += 1
        self._save(data)

        remaining = self.max_calls - data["count"]
        if remaining <= ALERT_THRESHOLD:
            logger.warning(
                f"[RateLimit] ALERTE : {remaining} appel(s) restant(s) aujourd'hui "
                f"({data['count']}/{self.max_calls})."
            )
        else:
            logger.debug(
                f"[RateLimit] Appel {data['count']}/{self.max_calls} "
                f"— {remaining} restant(s)."
            )

    def get_status(self) -> dict:
        """Retourne l'etat courant du compteur."""
        data = self._load()
        data = self._reset_if_new_day(data)
        return {
            "date":      data["date"],
            "count":     data["count"],
            "remaining": self.max_calls - data["count"],
            "limit":     self.max_calls,
        }

    def reset(self) -> None:
        """Remet le compteur a zero (usage : tests unitaires)."""
        today = datetime.now(timezone.utc).date().isoformat()
        self._save({"date": today, "count": 0})
        logger.info("[RateLimit] Compteur remis a zero.")

    # ------------------------------------------------------------------
    # PERSISTANCE (atomic write)
    # ------------------------------------------------------------------

    def _load(self) -> dict:
        """
        Charge le fichier de persistance.
        Retourne {"date": "", "count": 0} si inexistant ou corrompu.
        """
        if not os.path.exists(self.persist_path):
            return {"date": "", "count": 0}
        try:
            with open(self.persist_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Validation minimale
            if "date" not in data or "count" not in data:
                raise ValueError("Structure invalide")
            return data
        except (json.JSONDecodeError, ValueError, OSError) as e:
            logger.warning(f"[RateLimit] Fichier corrompu ({e}) — remise a zero.")
            return {"date": "", "count": 0}

    def _save(self, data: dict) -> None:
        """
        Sauvegarde atomique : ecriture dans un tempfile + os.replace.
        Jamais de json.dump() direct sur le fichier cible (risque corruption).
        """
        os.makedirs(os.path.dirname(self.persist_path), exist_ok=True)
        dir_path = os.path.dirname(self.persist_path)
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", dir=dir_path,
                delete=False, suffix=".tmp"
            ) as tmp:
                json.dump(data, tmp, ensure_ascii=False, indent=2)
                tmp_path = tmp.name
            os.replace(tmp_path, self.persist_path)
        except OSError as e:
            logger.error(f"[RateLimit] Echec sauvegarde : {e}")
            raise

    # ------------------------------------------------------------------
    # RESET JOURNALIER
    # ------------------------------------------------------------------

    def _reset_if_new_day(self, data: dict) -> dict:
        """
        Compare la date du fichier avec la date UTC du jour.
        Si different → reset le compteur a 0.
        """
        today = datetime.now(timezone.utc).date().isoformat()
        if data.get("date") != today:
            logger.info(
                f"[RateLimit] Nouveau jour UTC ({today}) — "
                f"compteur remis a zero (etait {data.get('count', 0)} le {data.get('date', '?')})."
            )
            data = {"date": today, "count": 0}
            self._save(data)
        return data


# =============================================================================
# SINGLETON -- importe par claude_brain
# =============================================================================
RATE_LIMITER = RateLimiter()
