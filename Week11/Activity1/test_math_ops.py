import unittest
from math_ops import add, mul


class TestMathOperations(unittest.TestCase):
    # Existing tests for add()
    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # New tests for mul()
    def test_mul_basic(self):
        # integers
        cases = [
            (2, 3, 6),
            (-1, 5, -5),
            (-4, -2, 8),
            (7, 0, 0),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(mul(a, b), expected)

    def test_mul_with_large_numbers(self):
        self.assertEqual(mul(10**6, 10**3), 10**9)

    def test_mul_commutativity(self):
        # a*b should equal b*a
        for a, b in [(2, 5), (-3, 4), (0, 9)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(mul(a, b), mul(b, a))

if __name__ == "__main__":
    unittest.main(verbosity=2)
