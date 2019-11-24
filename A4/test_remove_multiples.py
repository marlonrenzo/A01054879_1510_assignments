from unittest import TestCase
from A4.Question_1 import remove_multiples


class TestRemoveMultiples(TestCase):
    def test_remove_multiples_is_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = remove_multiples(test_list, 2)
        self.assertEqual(type(actual), list)

