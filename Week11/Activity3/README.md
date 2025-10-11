# Week 11 — Activity 1 (Updated): Unittest **and** Doctest

This revision adds **doctests** to the existing `unittest` suite.

## How to run

### Doctest
```bash
python -m doctest -v math_ops.py
```

### Unittest
```bash
python -m unittest -v
# or
python test_math_ops.py
```

### Run both at once
```bash
python run_all_tests.py
```

## Quick comparison: Doctest vs Unittest

| Aspect | Doctest | Unittest |
|---|---|---|
| Primary use | Verify examples in docstrings | Structured, comprehensive test suite |
| Readability | Very high (examples double as docs) | Medium (assert-based) |
| Failure detail | Minimal diffs | Rich assertions, subTests, setup/teardown |
| Parametrization | Manual | Easy via loops/subTests |
| Best for | Small, illustrative examples & docs | Full coverage, edge cases, CI |

**Recommendation:** Use both — keep simple examples as doctests and rely on `unittest` for complete behavior checks.
