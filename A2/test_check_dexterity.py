from unittest import TestCase
from A2.dungeonsanddragons import check_dexterity

class TestCheckDexterity(TestCase):
    def test_check_dexterity_killed_first_attack(self):
        test_dictionary = {'Name': 'Qumerate', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11,
                           'Dexterity': 12, 'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13,
                           'XP': 0, 'Inventory': ['Hello','World']}
        actual_value = check_dexterity(13, test_dictionary, 5)
        expected_value = test_dictionary['HP'][1] - 5
        self.assertEqual(actual_value, expected_value)

    def test_check_dexterity_attack_misses(self):
        test_dictionary = {'Name': 'Yujikigo', 'Race': 'gnome', 'Class': 'monk', 'HP': [5, 5], 'Strength': 11,
                           'Dexterity': 1, 'Constitution': 10, 'Intelligence': 11, 'Wisdom': 10, 'Charisma': 13,
                           'XP': 0, 'Inventory': ['Hello','World']}
        actual_value = check_dexterity(0, test_dictionary, 100)
        expected_value = test_dictionary['HP'][1]
        self.assertEqual(actual_value, expected_value)