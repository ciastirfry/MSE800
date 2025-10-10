import unittest
from decimal import Decimal
from expense_tracker import ExpenseTracker, Expense


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense_and_total(self):
        self.tracker.add_expense("Coffee", "4.50")
        self.tracker.add_expense("Sandwich", 7.25)
        self.assertEqual(self.tracker.total(), Decimal("11.75"))

    def test_add_expense_rounding(self):
        # values are rounded to 2 dp with HALF_UP
        self.tracker.add_expense("Item A", "1.005")
        self.assertEqual(self.tracker.total(), Decimal("1.01"))

    def test_add_multiple_and_list(self):
        self.tracker.add_expense("Bus", 2)
        self.tracker.add_expense("Book", 12.99)
        items = self.tracker.list_expenses()
        self.assertEqual(len(items), 2)
        self.assertIsInstance(items[0], Expense)

    def test_invalid_description(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("   ", 5)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Refund?", -1)

    def test_total_zero_when_empty(self):
        self.assertEqual(self.tracker.total(), Decimal("0.00"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
