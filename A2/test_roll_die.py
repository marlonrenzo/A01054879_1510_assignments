from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", return_value=2)
    def test_roll_die_middle(self, mock_output):
        expected_value = 8
        actual_value = roll_die(4, 6)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=12)
    def test_roll_die_upper(self, mock_output):
        expected_value = 2304
        actual_value = roll_die(192, 17)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=1)
    def test_roll_die_lower(self, mock_output):
        expected_value = 1
        actual_value = roll_die(1, 1)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=5)
    def test_roll_die_middle_two(self, mock_output):
        expected_value = 15
        actual_value = roll_die(3, 12)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=5)
    def test_roll_die_zero_rolls(self, mock_output):
        expected_value = 0
        actual_value = roll_die(0, 22)
        self.assertEqual(actual_value, expected_value)

    @patch("random.randint", return_value=1)
    def test_roll_die_zero_sided_die(self, mock_output):
        expected_value = 0
        actual_value = roll_die(25, 0)
        self.assertEqual(actual_value, expected_value)