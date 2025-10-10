# Week 11 — Activity 2: Personal Expense Tracker (OOP + Unittest)

This project implements a simple personal expense tracker in Python using:
- **OOP** (`Expense` dataclass and `ExpenseTracker` aggregate class)
- **`unittest`** for automated tests
- **`decimal.Decimal`** for correct money math and 2‑dp rounding (HALF_UP).

## Project layout
```
expense_tracker.py          # app code (includes a tiny CLI demo)
tests/
  test_expense_tracker.py   # unit tests
```

## Run the tests
```bash
python -m unittest -v
# or
python tests/test_expense_tracker.py
```

## Quick demo (optional)
```bash
python expense_tracker.py
```

## Push to GitHub (example)
```bash
git init
git add .
git commit -m "Week11 Activity2: OOP Expense Tracker with unit tests"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
