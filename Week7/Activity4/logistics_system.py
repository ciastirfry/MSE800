
from abc import ABC, abstractmethod
import threading

# --- Abstract Transport Mode ---
class TransportMode(ABC):
    @abstractmethod
    def deliver(self, cargo):
        pass

# --- Concrete Transport Modes ---
class RoadTransport(TransportMode):
    def deliver(self, cargo):
        return f"Delivering '{cargo}' via ROAD using trucks"

class SeaTransport(TransportMode):
    def deliver(self, cargo):
        return f"Delivering '{cargo}' via SEA using cargo ships"

# --- Factory for Logistics Modes ---
class LogisticsFactory:
    _modes = {
        "road": RoadTransport,
        "sea": SeaTransport
    }

    @classmethod
    def create_mode(cls, mode):
        transport_class = cls._modes.get(mode.lower())
        if not transport_class:
            raise ValueError(f"Unknown logistics mode: {mode}")
        return transport_class()

# --- Singleton for Auckland Logistics Center ---
class LogisticsCenter:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.dispatched = []

    def dispatch_cargo(self, mode, cargo):
        transporter = LogisticsFactory.create_mode(mode)
        result = transporter.deliver(cargo)
        self.dispatched.append((mode, cargo))
        return result

# --- Client Code ---
if __name__ == "__main__":
    center = LogisticsCenter()
    print(center.dispatch_cargo("road", "construction materials"))
    print(center.dispatch_cargo("sea", "containers"))
    print(center.dispatch_cargo("road", "timber"))
    print(center.dispatch_cargo("sea", "fuel tanks"))

    print("Dispatched history:")
    for mode, cargo in center.dispatched:
        print(f" - {cargo} via {mode.upper()}")
