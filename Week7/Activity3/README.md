
# Week 7 – Activity 3: Singleton + Factory Design Pattern

## 🧠 Overview

This project demonstrates the use of **both the Factory and Singleton design patterns** to implement a scalable, extensible payment processing system in Python.

---

## 🏗️ Design Patterns Used

### ✅ 1. Factory Pattern
- **Goal**: Dynamically create objects for different payment types.
- **Implementation**: `PaymentProcessorFactory` holds a mapping of payment method names to their corresponding classes.
- **Extensible**: Add new methods like `ApplePay` or `AliPay` by simply adding a new class and entry in the dictionary.

### ✅ 2. Singleton Pattern
- **Goal**: Ensure only one instance of `PaymentGateway` exists — central point of control for all payment transactions.
- **Implementation**: Uses `__new__` and a class-level lock to ensure thread-safe singleton behavior.

---

## 💡 Benefits

| Design Goal          | Factory Pattern         | Singleton Pattern              |
|----------------------|-------------------------|--------------------------------|
| Decouples Instantiation | ✅ Yes                 | ❌ (not its purpose)           |
| Easy to Extend        | ✅ Add new class + map  | ✅ One place to handle payment |
| Global Access         | ❌                      | ✅ Yes, one instance only      |

---

## 🚀 How to Run

```bash
python payment_system.py
```

### Example Output:
```
Processing $150 via PayPal
Processing $220 via Google Pay
Processing $780 via Cryptocurrency
Same instance: True
```

---

## 🧩 Adding a New Payment Method

1. Create a new class implementing `PaymentProcessor`.
2. Register it in `PaymentProcessorFactory._processors`.

Done — no changes to the client code!

---

