from unittest import TestCase
from A3.SUD import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_right_valid(self):
        actual_value = validate_move({"x": 0, "y": 2}, 'd')
        self.assertTrue(actual_value)

    def test_validate_move_down(self):
        actual_value = validate_move({"x": 0, "y": 4}, 's')
        self.assertFalse(actual_value)

    def test_validate_move_right_invalid(self):
        actual_value = validate_move({"x": 4, "y": 2}, 'd')
        self.assertFalse(actual_value)

    def test_validate_move_right_valid_2(self):
        actual_value = validate_move({"x": 3, "y": 2}, 'd')
        self.assertTrue(actual_value)
