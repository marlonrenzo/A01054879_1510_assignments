from unittest import TestCase
from A4.Question_1 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes_negative_number(self):
        try:
            test = eratosthenes(-5)
        except ValueError:
            test = False
        self.assertFalse(test)

    def test_eratosthenes_float_number(self):
        try:
            test = eratosthenes(5.0)
        except ValueError:
            test = False
        self.assertFalse(test)

    def test_eratosthenes_string(self):
        try:
            test = eratosthenes('string')
        except ValueError:
            test = False
        self.assertFalse(test)

    def test_eratosthenes_negative_number(self):
        try:
            test = eratosthenes('string')
        except ValueError:
            test = False
        self.assertFalse(test)
