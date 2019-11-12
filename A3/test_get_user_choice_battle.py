from unittest import TestCase
from A3.SUD import get_user_choice_battle
from unittest.mock import patch


class TestGetUserChoiceBattle(TestCase):
    @patch('builtins.input', side_effect=[1])
    def test_get_user_choice_battle_fight(self, mock_input):
        actual = get_user_choice_battle()
        self.assertTrue(actual)

    @patch('builtins.input', side_effect=[0])
    def test_get_user_choice_battle_run(self, mock_input):
        actual = get_user_choice_battle()
        self.assertFalse(actual)
