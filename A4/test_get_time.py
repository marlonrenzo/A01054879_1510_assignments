from unittest import TestCase
from A4.Question_8 import get_time


class TestGetTime(TestCase):
    def test_get_time_1_to_4(self):
        test = [1, 2, 3, 4]
        actual = get_time(test)
        expected = '12:34'
        self.assertEqual(actual, expected)

    def test_get_time_4_to_1(self):
        test = [4, 3, 2, 1]
        actual = get_time(test)
        expected = '43:21'
        self.assertEqual(actual, expected)

    def test_get_time_big_numbers(self):
        test = [10000, 20000, 30000, 40000]
        actual = get_time(test)
        expected = '1000020000:3000040000'
        self.assertEqual(actual, expected)

    def test_get_time_negative_numbers(self):
        test = [-1, -2, -3, -4]
        actual = get_time(test)
        expected = '-1-2:-3-4'
        self.assertEqual(actual, expected)
