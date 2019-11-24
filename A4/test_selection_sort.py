from unittest import TestCase
from A4.Question_4 import selection_sort


class TestSelectionSort(TestCase):
    def test_selection_sort_integers(self):
        test = [5, 4, 3, 2, 1]
        actual = selection_sort(test)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_selection_sort_negative_integers(self):
        test = [-1, -2, -3, -4, -5]
        actual = selection_sort(test)
        expected = [-5, -4, -3, -2, -1]
        self.assertEqual(actual, expected)

    def test_selection_sort_strings(self):
        test = ['aa', 'aaaaa', 'aaa', 'a', 'aaaa']
        actual = selection_sort(test)
        expected = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
        self.assertEqual(actual, expected)

    def test_selection_sort_floats(self):
        test = [5.2, 5.1, 3.9, 2.3, 1.0]
        actual = selection_sort(test)
        expected = [1.0, 2.3, 3.9, 5.1, 5.2]
        self.assertEqual(actual, expected)

    def test_selection_sort_non_sortable(self):
        test = [5.2, 5, 'hey']
        expected = ValueError
        self.assertRaises(expected, selection_sort, test)

    def test_selection_sort_empty(self):
        test = []
        expected = ValueError
        self.assertRaises(expected, selection_sort, test)

    def test_selection_sort_non_sortable_string_float(self):
        test = [5.2, '5.7', 5.0, 5.1, 5.4]
        expected = ValueError
        self.assertRaises(expected, selection_sort, test)
