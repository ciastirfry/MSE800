
# Week 7 – Activity 2: Refactored with Factory Design Pattern + Abstract Base Class

## 🧠 Overview
This Python example demonstrates how to refactor tightly coupled conditional code using the **Factory Design Pattern** combined with **Abstract Base Classes (ABC)**.

### 🚫 Before (Problem):
- `checkout()` had multiple `if`/`elif` to create instances for each payment method.
- Adding a new method required editing the client code — violating **Open-Closed Principle**.

### ✅ After (Solution):
- Defined an abstract base class `PaymentProcessor` with `process_payment()`.
- Created specific classes (`PayPalPayment`, `StripePayment`, `CreditCardPayment`) that inherit from it.
- Used a `PaymentProcessorFactory` to instantiate the correct class based on the string method.
- Now `checkout()` stays clean and extensible.

## 🔁 Extending
To add a new payment type:
1. Create a new class inheriting `PaymentProcessor`.
2. Add it to `_processors` dict in the factory.

## 🧪 Run

```bash
python factory_abstract.py
```

## 💡 Output

```
Processing $100 via PayPal
Processing $50 via Stripe
Processing $300 via Credit Card
```

## 📌 Pattern Used
- Factory Pattern (Creational)
- Abstract Base Class (OOP)
