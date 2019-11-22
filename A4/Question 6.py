"""
from unittest import TestCase
from A4.question_6 import line_intersect


class TestLineIntersect(TestCase):
    def test_line_intersect(self):
        line_one = []
        line_two = []
        actual = line_intersect(line_one, line_two)
        expected = []
        self.assertTrue(actual, expected)
"""