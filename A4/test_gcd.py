from unittest import TestCase
from A4.Question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_9_and_9(self):
        test = 9
        actual = gcd(test, test)
        expected = 9
        self.assertEqual(actual, expected)

    def test_gcd_negative_9_and_9(self):
        test = 9
        actual = gcd(-test, test)
        expected = 9
        self.assertEqual(actual, expected)

    def test_gcd_negative_9_and_negative_9(self):
        test = -9
        actual = gcd(test, test)
        expected = 9
        self.assertEqual(actual, expected)

    def test_gcd_100_and_90(self):
        test_one = 100
        test_two = 90
        actual = gcd(test_one, test_two)
        expected = 10
        self.assertEqual(actual, expected)

    def test_gcd_negative_100_and_90(self):
        test_one = -100
        test_two = 90
        actual = gcd(test_one, test_two)
        expected = 10
        self.assertEqual(actual, expected)

    def test_gcd_negative_100_and_negative_90(self):
        test_one = -100
        test_two = -90
        actual = gcd(test_one, test_two)
        expected = 10
        self.assertEqual(actual, expected)
