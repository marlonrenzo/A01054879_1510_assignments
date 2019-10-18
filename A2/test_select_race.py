from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_race

class TestSelect_class(TestCase):
    @patch("builtins.input", side_effect=[5])
    def test_select_class_human(self, mock_input):
        actual_value = select_race()
        expected_value = "human"
        self.assertEqual(actual_value, expected_value)
