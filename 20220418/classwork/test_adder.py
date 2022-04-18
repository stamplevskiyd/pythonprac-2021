import unittest
from unittest.mock import MagicMock
import adder


class TestAdder(unittest.TestCase):

    def setUp(self):
        import random
        self.A, self.B = random.randrange(0, 100), random.randrange(0, 100)
        self.C = self.A + self.B
        self.S, self.T = "QWE", "rty"
        adder.curses = MagicMock()

    def test_numbers(self):
        self.assertEqual(adder.adder(self.A, self.B), self.C)

    def test_string(self):
        self.assertEqual(adder.adder(self.S, self.T), "QWErty")

    def test_exception(self):
        with self.assertRaises(TypeError):
            adder.adder(123)

    def test_shower(self):
        adder.shower(123)
        print(adder.curses.initscr.mock_calls)
        adder.curses.initscr().addstr.assert_called_once_with(10, 20, '123')
