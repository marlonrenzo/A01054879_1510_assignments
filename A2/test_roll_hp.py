from unittest import TestCase
from A2.dungeonsanddragons import roll_hp
from unittest.mock import patch


class TestRollHp(TestCase):
    @patch("random.randint", return_value=12)
    def test_roll_hp_barbarian_upper(self, mock_output):
        actual_value = roll_hp("barbarian")
        expected_value = 12
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=1)
    def test_roll_hp_barbarian_lower(self, mock_output):
        actual_value = roll_hp("barbarian")
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=17)
    def test_roll_hp_not_a_class(self, mock_output):
        actual_value = roll_hp("Spiderman")
        expected_value = "Error in inputted class."
        self.assertEqual(actual_value, expected_value)
