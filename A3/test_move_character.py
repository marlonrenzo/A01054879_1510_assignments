from unittest import TestCase
from A3.SUD import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_right(self):
        actual_value = move_character({"x": 0, "y": 0}, 'd')
        expected_value = {'x': 1, 'y': 0}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_up(self):
        actual_value = move_character({"x": 3, "y": 3}, 'w')
        expected_value = {'x': 3, 'y': 2}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_left(self):
        actual_value = move_character({"x": 1, "y": 1}, 'a')
        expected_value = {'x': 0, 'y': 1}
        self.assertEqual(actual_value, expected_value)

    def test_move_character_down(self):
        actual_value = move_character({"x": 0, "y": 1}, 's')
        expected_value = {'x': 0, 'y': 2}
        self.assertEqual(actual_value, expected_value)
