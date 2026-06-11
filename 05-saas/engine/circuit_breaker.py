import threading
from datetime import datetime, timedelta
from enum import Enum

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
