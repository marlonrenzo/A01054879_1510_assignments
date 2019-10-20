from unittest import TestCase
from A2.dungeonsanddragons import attack
from A2.dungeonsanddragons import create_character
from unittest.mock import patch


class TestAttack(TestCase):
    @patch("random.randint", return_value=5)
    @patch("builtins.input", side_effect=[1])
    @patch("builtins.input", side_effect=[2])
    def test_attack(self, mock_class, mock_race):
        char_one = create_character(4)
        char_two = create_character(4)
        actual_value = attack(char_one, char_two)

