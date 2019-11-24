from unittest import TestCase
from A4.Question_5 import cash_money


class TestCashMoney(TestCase):
    def test_cash_money_one_hundred_one(self):
        test = 101.0
        actual = cash_money(test)
        expected = {100: 1, 1: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_4(self):
        test = 4.0
        actual = cash_money(test)
        expected = {2: 2}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_40_cents(self):
        test = 0.4
        actual = cash_money(test)
        expected = {0.25: 1, 0.1: 1, 0.05: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_90_cents(self):
        test = 0.4
        actual = cash_money(test)
        expected = {0.25: 1, 0.1: 1, 0.05: 1}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_9(self):
        test = 9.0
        actual = cash_money(test)
        expected = {5: 1, 2: 2}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_4_cents(self):
        test = 0.04
        actual = cash_money(test)
        expected = {0.01: 4}
        self.assertEqual(actual, expected)

    def test_breakdown_amount_int(self):
        test = 4
        expected = ValueError
        self.assertRaises(expected, cash_money, test)

    def test_breakdown_amount_string(self):
        test = 'five dollars'
        expected = TypeError
        self.assertRaises(expected, cash_money, test)
