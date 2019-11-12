from unittest import TestCase
from A3.SUD import check_alive


class TestCheckAlive(TestCase):
    def test_check_alive(self):
        actual = check_alive({'HP': [10, 10]})
        self.assertTrue(actual)

    def test_check_alive_not_alive(self):
        actual = check_alive({'HP': [0, 10]})
        self.assertFalse(actual)
