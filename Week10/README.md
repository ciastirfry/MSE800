
# Week 10 - Activity 1: OO Analyzer + Pylint

This mini project reads **either a string or a list of strings** and computes:
1. **Total length**
   - For a string: number of characters.
   - For a list: number of items.
2. **Uppercase characters**
   - For a string: count of A–Z characters.
   - For a list: *sum* of uppercase characters across all string items.

It is implemented with an OO design (separate input wrapper, analyzers, and a processor).

## Run
```bash
python -m oo_analyzer.main --string "Hello World!"
python -m oo_analyzer.main --list '["Hello","Yoobee","NZ"]'
```

## Pylint
```bash
pip install pylint
pylint src/oo_analyzer tests --fail-under=9.5
```
A `.pylintrc` is provided. Depending on your Pylint version, the score should be around **10.00/10**.

## Tests (optional)
```bash
pip install pytest
pytest -q
```
