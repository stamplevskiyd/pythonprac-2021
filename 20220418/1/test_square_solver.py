import unittest
from square_solver import solveSquare


class TestSolver(unittest.TestCase):

    def test_00(self):
        self.assertEqual(solveSquare(a=1, b=-3, c=2), (1.0, 2.0))

    def test_01(self):
        self.assertEqual(solveSquare(a=1, b=-4, c=4), 2.0)

    def test_02(self):
        self.assertEqual(solveSquare(a=1, b=0, c=1), None)
