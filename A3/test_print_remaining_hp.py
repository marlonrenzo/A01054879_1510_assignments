from unittest import TestCase
from A3.SUD import print_remaining_hp
from unittest.mock import patch
import io


class TestPrintRemainingHp(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_remaining_hp(self, mock_output):
        print_remaining_hp({'Name': 'Marlon', 'Alias': 'You', 'Class': 'Wizard', 'HP': [5, 10], 'Inventory': [],
                            'Spells': [], 'position': {"x": 2, "y": 2}, "Attack Roll": 0}, 5)
        actual = mock_output.getvalue()
        expected = 'The hit left You with 5/10 HP\n'
        self.assertEqual(actual, expected)


