from unittest import TestCase
from A3.SUD import fight_or_run
from unittest.mock import patch


class TestFightOrRun(TestCase):
    @patch('builtins.input', side_effect=[0])
    def test_fight_or_run_zero(self, mock_input):
        actual = fight_or_run()
        expected = 0
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[1])
    def test_fight_or_run_one(self, mock_input):
        actual = fight_or_run()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[10])
    def test_fight_or_run_10(self, mock_input):
        actual = fight_or_run()
        expected = 10
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=[100])
    def test_fight_or_run_100(self, mock_input):
        actual = fight_or_run()
        expected = 100
        self.assertEqual(actual, expected)
