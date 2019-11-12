from unittest import TestCase
from unittest.mock import patch
from A3.SUD import one_in_x_chance


class TestOneInXChance(TestCase):
    @patch("random.randint", return_value=1)
    def test_one_in_10_chance_false(self, mock_output):
        actual_value = one_in_x_chance(10)
        self.assertFalse(actual_value)

    @patch("random.randint", return_value=50)
    def test_one_in_50_chance_true(self, mock_output):
        actual_value = one_in_x_chance(50)
        self.assertTrue(actual_value)

    @patch("random.randint", return_value=2)
    def test_one_in_2_chance_true(self, mock_output):
        actual_value = one_in_x_chance(2)
        self.assertTrue(actual_value)

    @patch("random.randint", return_value=99)
    def test_one_in_100_chance_false(self, mock_output):
        actual_value = one_in_x_chance(100)
        self.assertFalse(actual_value)

    @patch("random.randint", return_value=99)
    def test_one_in_x_chance_true(self, mock_output):
        actual_value = one_in_x_chance(99)
        self.assertTrue(actual_value)
