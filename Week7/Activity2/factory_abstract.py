
from abc import ABC, abstractmethod

# Abstract base class
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete implementations
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

# Factory class
class PaymentProcessorFactory:
    _processors = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment
    }

    @classmethod
    def create_processor(cls, payment_method):
        processor_class = cls._processors.get(payment_method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {payment_method}")
        return processor_class()

# Clean client code
def checkout(payment_method, amount):
    processor = PaymentProcessorFactory.create_processor(payment_method)
    return processor.process_payment(amount)

# Usage
if __name__ == "__main__":
    print(checkout("paypal", 100))       # Processing $100 via PayPal
    print(checkout("stripe", 50))        # Processing $50 via Stripe
    print(checkout("credit_card", 300))  # Processing $300 via Credit Card
