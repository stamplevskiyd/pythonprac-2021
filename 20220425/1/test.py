import unittest
from solver import solve


class TestSolver(unittest.TestCase):

    def test_a_not_equal_zero(self):
        self.assertEqual(solve(5, 5), -1)

    def test_a_is_zero(self):
        self.assertEqual(solve(0, -4), None)

    def test_b_is_zero(self):
        self.assertEqual(solve(1, -6), 6)


if __name__ == "__main__":
    unittest.main()