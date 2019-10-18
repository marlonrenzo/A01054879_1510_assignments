from unittest import TestCase
from A2.dungeonsanddragons import create_character
from unittest.mock import patch


class TestCreateCharacter(TestCase):
    @patch("builtins.input", side_effect=[4, 4])
    def test_create_character_length(self, mock_input):
        actual_value = create_character(10)
        self.assertTrue(len(actual_value) == 12)

    @patch("builtins.input", side_effect=[1, 3])
    def test_create_character_attributes(self, mock_input):
        attributes = ['Name', 'Race', 'Class', 'HP', 'Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom',
                      'Charisma', 'XP', 'Inventory']
        actual_value = create_character(10)
        for key in range(0, len(attributes)):
            self.assertTrue(attributes[key] in actual_value)

    @patch("builtins.input", side_effect=[4, 5])
    def test_create_character_empty_inventory(self, mock_input):
        actual_value = create_character(10)
        inventory = actual_value['Inventory']
        expected_value = []
        self.assertEqual(inventory, expected_value)
