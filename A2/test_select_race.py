from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import select_race


class TestSelectClass(TestCase):
    @patch("builtins.input", side_effect=[5])
    def test_select_class_human(self, mock_input):
        actual_value = select_race()
        expected_value = "human"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[4])
    def test_select_class_dwarf(self, mock_input):
        actual_value = select_race()
        expected_value = "dwarf"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[10])
    def test_select_class_tiefling(self, mock_input):
        actual_value = select_race()
        expected_value = "tiefling"
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[5])
    def test_select_class_first_letter_lowercase(self, mock_input):
        string = select_race()
        expected_character = 'h'
        self.assertTrue(string[0], expected_character)


