from unittest import TestCase
from A4.Question_8 import get_bars


class TestGetBars(TestCase):
    def test_get_bars(self):
        test_dict = {1: 1, 2: 2, 3: 3, 4: 4}
        test = [1, 2, 3, 4]
        actual = get_bars(test_dict, test)
        expected = 10
        self.assertEqual(actual, expected)

    def test_get_bars_negatives(self):
        test_dict = {1: -1, 2: -2, 3: -3, 4: -4}
        test = [1, 2, 3, 4]
        actual = get_bars(test_dict, test)
        expected = -10
        self.assertEqual(actual, expected)

    def test_get_bars_some_negative(self):
        test_dict = {1: -1, 2: 2, 3: 3, 4: -4}
        test = [1, 2, 3, 4]
        actual = get_bars(test_dict, test)
        self.assertFalse(actual)
