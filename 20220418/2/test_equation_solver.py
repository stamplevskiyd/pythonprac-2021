import unittest
from unittest.mock import MagicMock

import equation_solver

eps = pow(10, -7)


def check(coefficients, answer):
    equation_solver.SquareIO.inputCoeff = MagicMock(side_effect=coefficients)
    equation_solver.SquareIO.printResult = MagicMock()
    equation_solver.solveSquare()
    res = equation_solver.SquareIO.printResult.call_args.args[0]
    if type(res) != type(answer):
        assert False
    elif res is None or type(res) is str:
        assert res == answer
    else:  # иначе только float
        if len(res) == len(answer):
            if len(res) == 2:  # квадратное уравнение
                assert abs(res[0] - answer[0]) < eps and abs(res[1] - answer[1]) < eps
            elif len(res) == 1:  # линейное уравнение
                assert abs(res[0] - answer[0]) < eps
            else:  # Нечто иное. Но вообще в программе встретиться не может
                assert False
        else:
            assert False


class TestSolver(unittest.TestCase):

    def test_00(self):
        """Quadratic. Discriminant > 0."""

        check((1, -3, 2), (1.0, 2.0))

    def test_01(self):
        """Quadratic. Discriminant == 0."""

        check((1, -4, 4), (2.0, 2.0))

    def test_02(self):
        """Quadratic. Discriminant < 0."""

        check((1, 0, 1), None)

    def test_03(self):
        """Linear."""

        check((0, 5, -5), (1.0,))

    def test_04(self):
        """Degenerate equation (5 = 0)."""

        check((0, 0, 5), None)

    def test_05(self):
        """Sameness (0 = 0)."""

        check((0, 0, 0), (0.0,))

    def test_06(self):
        """Wrong input."""

        check(("qwerty", 0, 0), "Unable to convert coefficients to float")

