import threading
import time
from datetime import datetime, timedelta
from enum import Enum
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout

class CircuitState(Enum):
    CLOSED    = "CLOSED"
    OPEN      = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker:
    def __init__(self, name: str, failure_threshold: int = 3,
                 recovery_timeout: int = 60):
        self.name              = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout  = recovery_timeout
        self.failure_count     = 0
        self.last_failure_time = None
        self.state             = CircuitState.CLOSED
        self._lock             = threading.Lock()

    def call(self, func, *args, **kwargs):
        with self._lock:
            if self.state == CircuitState.OPEN:
                elapsed = (datetime.now() - self.last_failure_time).total_seconds()
                if elapsed >= self.recovery_timeout:
                    self.state = CircuitState.HALF_OPEN
                else:
                    raise Exception(
                        f"[{self.name}] Circuit OPEN — reprise dans "
                        f"{self.recovery_timeout - elapsed:.0f}s"
                    )
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e

    def _on_success(self):
        with self._lock:
            self.failure_count = 0
            self.state = CircuitState.CLOSED

    def _on_failure(self):
        with self._lock:
            self.failure_count += 1
            self.last_failure_time = datetime.now()
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN

    def get_status(self) -> dict:
        return {
            "name":    self.name,
            "state":   self.state.value,
            "failures":self.failure_count,
        }

CB_NT8    = CircuitBreaker("NT8_data",     failure_threshold=3, recovery_timeout=30)
CB_ATAS   = CircuitBreaker("ATAS_signals", failure_threshold=3, recovery_timeout=30)
CB_CLAUDE = CircuitBreaker("Claude_API",   failure_threshold=2, recovery_timeout=60)

def get_all_circuit_status() -> dict:
    return {
        "NT8":    CB_NT8.get_status(),
        "ATAS":   CB_ATAS.get_status(),
        "Claude": CB_CLAUDE.get_status(),
    }


# =============================================================================
# A3 -- Timeout + retry + fallback ATTENDRE (Phase 5)
# Valeurs par defaut : 15s timeout / 2 retries / fallback ATTENDRE (cf. settings.CIRCUIT_BREAKER).
# =============================================================================
CB_TIMEOUT_SEC = 15
CB_RETRY_MAX = 2


def fallback_attendre(raison: str = "CIRCUIT_BREAKER_FALLBACK") -> dict:
    """Signal de repli sur : mode Auto interdit, aucune position prise."""
    return {
        "signal": "ATTENDRE",
        "confiance": 0,
        "mode_auto_autorise": False,
        "taille_contrats": 0,
        "raison": raison,
    }


def protected_call(cb, func, *, timeout_sec: int = CB_TIMEOUT_SEC,
                   retry_max: int = CB_RETRY_MAX, retry_delay_sec: float = 0.0,
                   fallback=None):
    """
    Enveloppe un CircuitBreaker avec timeout (s) + retry + fallback ATTENDRE.
    Sequence : timeout `timeout_sec` -> retry `retry_max` fois -> fallback ATTENDRE.
    Renvoie le resultat de `func`, ou le fallback (callable prenant une raison) en cas d'echec.
    """
    last_exc = None
    for attempt in range(retry_max + 1):              # 1 essai initial + retry_max retries
        ex = ThreadPoolExecutor(max_workers=1)
        try:
            fut = ex.submit(cb.call, func)
            return fut.result(timeout=timeout_sec)
        except FuturesTimeout as e:
            last_exc = e
            try:
                cb._on_failure()                       # un timeout compte comme un echec
            except Exception:
                pass
        except Exception as e:                         # echec applicatif ou circuit OPEN
            last_exc = e
        finally:
            ex.shutdown(wait=False, cancel_futures=True)
        if attempt < retry_max and retry_delay_sec:
            time.sleep(retry_delay_sec)

    fb = fallback or fallback_attendre
    nom = type(last_exc).__name__ if last_exc else "inconnu"
    return fb(f"CB_FALLBACK:{nom}")
