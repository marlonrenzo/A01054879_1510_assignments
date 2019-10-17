from unittest import TestCase
from A2.dungeonsanddragons import print_character
from unittest.mock import patch
import io

class TestPrintCharacter(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_no_inventory(self, mock_output):
        char = {'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11, 'Dexterity': 12,
                'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13, 'XP': 0, 'Inventory': []}
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Qumerate\nRace: gnome\nClass: monk\nHP: [5, 5]\nStrength: 11\nDexterity: 12\n" \
                         "Constitution: 10\nIntelligence: 11\nWisdom: 10\nCharisma: 13\nXP: 0\n"
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_with_inventory(self, mock_output):
        char = {'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11, 'Dexterity': 12,
                'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13, 'XP': 0,
                'Inventory': ['Hello','World']}
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Qumerate\nRace: gnome\nClass: monk\nHP: [5, 5]\nStrength: 11\nDexterity: 12\n" \
                         "Constitution: 10\nIntelligence: 11\nWisdom: 10\nCharisma: 13\nXP: 0\nHere are your items:\n" \
                         "Hello\nWorld\n"
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_incorrect_format(self, mock_output):
        char = {'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11, 'Dexterity': 12,
                'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13, 'XP': 0, 'Inventory': []}
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Qumerate\nRace: gnome\nClass: monk\nHP: [5, 5]\nStrength: 11\nDexterity: 12\n" \
                         "Constitution: 10\nIntelligence: 11\nWisdom: 10\nCharisma: 13\nXP: 0\n"
        self.assertEqual(actual_value, expected_value)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_character_incorrect_format(self, mock_output):
        char = {'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11,
                'Inventory': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Warning: Error found with your list of character attributes\n"
        self.assertEqual(actual_value, expected_value)
