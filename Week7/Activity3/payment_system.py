
from abc import ABC, abstractmethod
import threading

# ---- Abstract Base Class ----
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# ---- Concrete Implementations ----
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Bank Transfer"

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Cryptocurrency"

class GooglePayPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Google Pay"

# ---- Factory Pattern ----
class PaymentProcessorFactory:
    _processors = {
        "credit_card": CreditCardPayment,
        "paypal": PayPalPayment,
        "bank_transfer": BankTransferPayment,
        "crypto": CryptoPayment,
        "googlepay": GooglePayPayment
    }

    @classmethod
    def create_processor(cls, method):
        processor_class = cls._processors.get(method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {method}")
        return processor_class()

# ---- Singleton Pattern: PaymentGateway ----
class PaymentGateway:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process(self, method, amount):
        processor = PaymentProcessorFactory.create_processor(method)
        return processor.process_payment(amount)

# ---- Client Code ----
if __name__ == "__main__":
    gateway1 = PaymentGateway()
    gateway2 = PaymentGateway()

    print(gateway1.process("paypal", 150))
    print(gateway1.process("googlepay", 220))
    print(gateway1.process("crypto", 780))

    # Verify Singleton
    print("Same instance:", gateway1 is gateway2)
