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
                'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13, 'XP': 0, 'Inventory': ['Hello','World']}
        print_character(char)
        actual_value = mock_output.getvalue()
        expected_value = "Name: Qumerate\nRace: gnome\nClass: monk\nHP: [5, 5]\nStrength: 11\nDexterity: 12\n" \
                         "Constitution: 10\nIntelligence: 11\nWisdom: 10\nCharisma: 13\nXP: 0\nHere are your items:\nHello\nWorld\n"
        self.assertEqual(actual_value, expected_value)

    # @patch("sys.stdout", new_callable=io.StringIO)
    # def test_print_character_with_inventory(self, mock_output):
    #     char = {'Name': 'Zony', 'Race': 'human', 'Class': 'bard', 'HP': [8, 8], 'Strength': 10, 'Dexterity': 13, 'Constitution': 8, 'Intelligence': 8, 'Wisdom': 7, 'Charisma': 6, 'XP': 0, 'Inventory': []}
    #     dummy_inventory = ["sword"]
    #     char.append(dummy_inventory)
    #     print_character(char)
    #     actual_value = mock_output.getvalue()
    #     expected_value = "Name: Jacilogo\nStrength: 7\nDexterity: 4\nConstitution: 8\nIntelligence: 14\nWisdom: 4\nCharisma: 13\n--Here are your inventory items--\nsword\n"
    #     self.assertEqual(actual_value, expected_value)
    #
    # @patch("sys.stdout", new_callable=io.StringIO)
    # def test_print_character_incorrect_format(self, mock_output):
    #     char = {'Name': 'Zony', 'Race': 'human', 'Class': 'bard', 'HP': [8, 8], 'Strength': 10, 'Dexterity': 13, 'Constitution': 8, 'Intelligence': 8, 'Wisdom': 7, 'Charisma': 6, 'XP': 0, 'Inventory': []}
    #     print_character(char)
    #     actual_value = mock_output.getvalue()
    #     expected_value = "Warning: Error found with your list of character attributes\n"
    #     self.assertEqual(actual_value, expected_value)
