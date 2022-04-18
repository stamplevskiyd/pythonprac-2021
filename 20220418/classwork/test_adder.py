import unittest
import adder


class TestAdder(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(adder.adder(100500, 42), 100542)

    def test_string(self):
        self.assertEqual(adder.adder("QWE", "rty"), "QWErty")

    def test_exception(self):
        with self.assertRaises(TypeError):
            adder.adder(123)
