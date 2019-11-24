from unittest import TestCase
from A4.Question_1 import remove_multiples


class TestRemoveMultiples(TestCase):
    def test_remove_multiples_is_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = remove_multiples(test_list, 2)
        self.assertEqual(type(actual), list)

    def test_remove_multiples_removes_even(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = remove_multiples(test_list, 2)
        expected = True
        for i in actual:
            if i % 2 == 0 and i != 2:
                expected = False
        self.assertEqual(expected, True)

    def test_remove_multiples_is_list_multiples_of_3(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = remove_multiples(test_list, 3)
        expected = True
        for i in actual:
            if i % 3 == 0 and i != 3:
                expected = False
        self.assertEqual(expected, True)

    def test_remove_multiples_empty_list(self):
        test_list = []
        actual = remove_multiples(test_list, 10)
        expected = []
        self.assertEqual(expected, actual)

    def test_remove_multiples_does_not_remove_2(self):
        test_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        actual = remove_multiples(test_list, 2)
        expected = len(test_list)
        self.assertEqual(expected, len(actual))
