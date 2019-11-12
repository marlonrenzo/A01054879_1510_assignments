from unittest import TestCase
from unittest.mock import patch
from A3.SUD import heal


class TestHeal(TestCase):
    def test_heal_normal(self):
        actual = heal(5)
        expected = 7
        self.assertEqual(actual, expected)

    def test_heal_dont_heal(self):
        actual = heal(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_heal_dont_heal_over_10(self):
        actual = heal(9)
        expected = 10
        self.assertEqual(actual, expected)
