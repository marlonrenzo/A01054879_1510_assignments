from unittest import TestCase
from A3.SUD import check_at_exit_with_key


class TestCheckAtExitWithKey(TestCase):
    def test_check_at_exit_with_key_with_key(self):
        test = {'Name': 'Marlon', 'Alias': 'You', 'HP': [10, 10], 'Inventory': ['key'], 'position': {"x": 2, "y": 2}}
        actual = check_at_exit_with_key(test['position'], test['Inventory'])
        self.assertTrue(actual)

    def test_check_at_exit_with_key_no_key(self):
        test = {'Name': 'Marlon', 'Alias': 'You', 'HP': [10, 10], 'Inventory': [], 'position': {"x": 2, "y": 2}}
        actual = check_at_exit_with_key(test['position'], test['Inventory'])
        self.assertFalse(actual)
