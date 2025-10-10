from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from typing import List


TWOPLACES = Decimal('0.01')


def _to_amount(value) -> Decimal:
    """Convert value to a Decimal monetary amount rounded to 2 dp."""
    if isinstance(value, Decimal):
        amount = value
    else:
        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise ValueError(f"Invalid amount: {value!r}") from exc

    # Normalize to 2 decimal places
    return amount.quantize(TWOPLACES, rounding=ROUND_HALF_UP)


@dataclass(frozen=True, slots=True)
class Expense:
    description: str
    amount: Decimal

    def __post_init__(self):
        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError("Description must be a non-empty string.")
        if self.amount < Decimal('0.00'):
            raise ValueError("Amount cannot be negative.")


class ExpenseTracker:
    """OOP Expense tracker holding a collection of Expense items."""
    def __init__(self) -> None:
        self._items: List[Expense] = []

    def add_expense(self, description: str, amount) -> Expense:
        amt = _to_amount(amount)
        expense = Expense(description=description.strip(), amount=amt)
        self._items.append(expense)
        return expense

    def total(self) -> Decimal:
        total_amt = sum((e.amount for e in self._items), Decimal('0.00'))
        # ensure 2 dp
        return total_amt.quantize(TWOPLACES, rounding=ROUND_HALF_UP)

    def list_expenses(self) -> List[Expense]:
        return list(self._items)

    # Optional: string representation for quick display
    def __str__(self) -> str:
        lines = [f"{e.description}: {e.amount}" for e in self._items]
        lines.append(f"TOTAL: {self.total()}")
        return "\n".join(lines)


if __name__ == "__main__":
    # Tiny CLI demo
    tracker = ExpenseTracker()
    print("Personal Expense Tracker (type 'q' to quit)\n")
    while True:
        desc = input("Description: ").strip()
        if desc.lower() in {"q", "quit", "exit"}:
            break
        amt = input("Amount: ").strip()
        if amt.lower() in {"q", "quit", "exit"}:
            break
        try:
            tracker.add_expense(desc, amt)
            print("Added! Current total:", tracker.total())
        except Exception as e:
            print("Error:", e)
    print("\nSummary:\n" + str(tracker))
