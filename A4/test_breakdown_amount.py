from unittest import TestCase
from A4.Question_5 import breakdown_amount


class TestBreakdownAmount(TestCase):
    def test_breakdown_amount_one_hundred_one(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 101.0
        actual = breakdown_amount(test, test_amount)
        expected = {100: 1, 1: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_4(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 4.0
        actual = breakdown_amount(test, test_amount)
        expected = {2: 2}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_40_cents(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 0.4
        actual = breakdown_amount(test, test_amount)
        expected = {0.25: 1, 0.1: 1, 0.05: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_90_cents(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 0.4
        actual = breakdown_amount(test, test_amount)
        expected = {0.25: 1, 0.1: 1, 0.05: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_9(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 9.0
        actual = breakdown_amount(test, test_amount)
        expected = {5: 1, 2: 2}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_4_cents(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 0.04
        actual = breakdown_amount(test, test_amount)
        expected = {0.01: 4}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_int(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 4
        expected = TypeError
        self.assertRaises(expected, breakdown_amount, test)

    def test_breakdown_amount_string(self):
        test = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        test_amount = 'five dollars'
        expected = TypeError
        self.assertRaises(expected, breakdown_amount, test, test_amount)
