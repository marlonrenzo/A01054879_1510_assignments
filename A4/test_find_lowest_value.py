from unittest import TestCase
from A4.Question_4 import find_lowest_value


class TestFindLowestValue(TestCase):
    def test_find_lowest_value_one(self):
        test = [100, 12244, 2323425, 5345, 43, 1]
        actual = find_lowest_value(test)
        self.assertTrue(actual)

    def test_find_lowest_value_one_negative(self):
        test = [100, 12244, -2323425, 5345, 43, 1]
        actual = find_lowest_value(test)
        expected = -2323425
        self.assertEqual(actual, expected)

    def test_find_lowest_value_three_negative(self):
        test = [100, 12244, -2323425, 5345, 43, 1]
        actual = find_lowest_value(test)
        expected = -2323425
        self.assertEqual(actual, expected)

    def test_find_lowest_value_all_negative(self):
        test = [-100, -12244, -2323425, -5345, -43, -1]
        actual = find_lowest_value(test)
        expected = -2323425
        self.assertEqual(actual, expected)

    def test_find_lowest_value_zero(self):
        test = [1, 1, 1, 1, 1, 0, 1, 1]
        actual = find_lowest_value(test)
        self.assertFalse(actual)
