from unittest import TestCase
from A4.Question_8 import find_largest


class TestFindLargest(TestCase):
    def test_find_largest(self):
        test_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
        actual = find_largest(test_dict, 1, 5)
        expected = 4
        self.assertEqual(actual, expected)

    def test_find_largest_negatives(self):
        test_dict = {0: 0, 1: 1, 2: -2, 3: -3, 4: -4}
        actual = find_largest(test_dict, 1, 5)
        expected = 1
        self.assertEqual(actual, expected)

    def test_find_largest_zeroes(self):
        test_dict = {0: 0, 1: 0, 2: 1, 3: 0, 4: 0}
        actual = find_largest(test_dict, 1, 5)
        expected = 2
        self.assertEqual(actual, expected)


