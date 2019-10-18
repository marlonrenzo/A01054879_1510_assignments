from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_class

class TestSelect_class(TestCase):
    @patch("builtins.input", side_effect=[3])
    def test_select_class(self, mock_input):
        actual_value = select_class()
        expected_value = "cleric"
        self.assertEqual(actual_value, expected_value)
