import unittest, doctest, math_ops

if __name__ == "__main__":
    print("Running doctests...")
    doctest.testmod(math_ops, verbose=True)
    print("\nRunning unittests...")
    unittest.main(module='test_math_ops', verbosity=2, exit=False)
