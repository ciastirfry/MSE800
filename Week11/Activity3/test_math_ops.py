import unittest
from math_ops import add, mul


class TestMathOperations(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_mul_basic(self):
        for a, b, expected in [(2, 3, 6), (-1, 5, -5), (-4, -2, 8), (7, 0, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(mul(a, b), expected)

    def test_mul_commutativity(self):
        self.assertEqual(mul(3, 7), mul(7, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
