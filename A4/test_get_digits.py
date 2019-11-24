from unittest import TestCase
from A4.Question_8 import get_digits


class TestGetDigits(TestCase):
    def test_get_digits(self):
        test = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        actual = get_digits(test)
        expected = [1, 0, 0, 8]
        self.assertEqual(actual, expected)

    def test_get_digits_type(self):
        test = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        actual = type(get_digits(test))
        expected = list
        self.assertEqual(actual, expected)

    def test_get_digits_type_element(self):
        test = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        testing = get_digits(test)
        actual = True
        for i in testing:
            if type(i) != int:
                actual = False
        self.assertTrue(actual)
