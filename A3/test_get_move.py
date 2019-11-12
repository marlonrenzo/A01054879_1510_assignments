from unittest import TestCase
from A3.SUD import get_move
from unittest.mock import patch


class TestGetMove(TestCase):
    @patch("builtins.input", side_effect=['UPPER'])
    def test_get_move_uppercase(self, mock_input):
        actual_value = get_move()
        expected_value = 'upper'
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=['lower'])
    def test_get_move_lowercase(self, mock_input):
        actual_value = get_move()
        expected_value = 'lower'
        self.assertEqual(actual_value, expected_value)
