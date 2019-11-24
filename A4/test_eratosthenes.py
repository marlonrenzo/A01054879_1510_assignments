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
        except TypeError:
            test = False
        self.assertFalse(test)

    def test_eratosthenes_is_below_upperbound(self):
        test = 50
        actual = eratosthenes(test)
        if actual[-1] < 50:
            test = True
        self.assertTrue(test)

    def test_eratosthenes_has_a_2(self):
        test = 2
        actual = eratosthenes(test)
        if test in actual:
            test = True
        self.assertTrue(test)

    def test_eratosthenes_has_no_0(self):
        test = 0
        actual = eratosthenes(1999)
        if test not in actual:
            test = True
        self.assertTrue(test)

    def test_eratosthenes_30(self):
        test = 30
        actual = eratosthenes(test)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(actual, expected)

    def test_eratosthenes_100(self):
        test = 100
        actual = eratosthenes(test)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(actual, expected)
