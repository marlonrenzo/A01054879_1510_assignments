from unittest import TestCase
from A3.SUD import check_position


class TestCheckPosition(TestCase):
    def test_check_position_doesnt_match_positive(self):
        actual_value = check_position({"x": 0, "y": 0}, 123, 456)
        self.assertFalse(actual_value)

    def test_check_position_match_positive(self):
        actual_value = check_position({"x": 99, "y": 99}, 99, 99)
        self.assertTrue(actual_value)

    def test_check_position_match_negative(self):
        actual_value = check_position({"x": -456, "y": -123}, -456, -123)
        self.assertTrue(actual_value)

    def test_check_position_doesnt_match_negative_one_match(self):
        actual_value = check_position({"x": -123, "y": -321}, -321, -321)
        self.assertTrue(actual_value)

