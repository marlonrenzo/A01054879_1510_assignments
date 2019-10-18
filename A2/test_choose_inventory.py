from unittest import TestCase
from A2.dungeonsanddragons import choose_inventory
from unittest.mock import patch
import io


class TestChooseInventory(TestCase):
    @patch("builtins.input", side_effect=[-1])
    def test_choose_inventory_no_items_bought(self, mock_input):
        actual_value = choose_inventory()
        expected_value = []
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[1, 1, 1, 1, -1])
    def test_choose_inventory_duplicate_items(self, mock_input):
        actual_value = choose_inventory()
        expected_value = ["sword", "sword", "sword", "sword"]
        self.assertEqual(actual_value, expected_value)

    @patch("builtins.input", side_effect=[1, 2, 3, -1])
    def test_choose_inventory_number_of_items(self, mock_input):
        actual_value = choose_inventory()
        self.assertTrue(len(actual_value) == 3)

