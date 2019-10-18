from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_class


class TestSelectClass(TestCase):
    @patch("builtins.input", side_effect=[3])
    def test_select_class_cleric(self, mock_input):
        actual_value = select_class()
        expected_value = "cleric"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[1])
    def test_select_class_barbarian(self, mock_input):
        actual_value = select_class()
        expected_value = "barbarian"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[12])
    def test_select_class_wizard(self, mock_input):
        actual_value = select_class()
        expected_value = "wizard"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[7])
    def test_select_class_paladin(self, mock_input):
        actual_value = select_class()
        expected_value = "paladin"
        self.assertEqual(actual_value, expected_value)

