from unittest import TestCase
from A4.Question_8 import im_not_sleepy


class TestImNotSleepy(TestCase):
    def test_im_not_sleepy(self):
        actual = im_not_sleepy()
        expected = "The time requiring the most amount of bars is:\n10:08 with 21 bars"
        self.assertEqual(actual, expected)

    def test_im_not_sleepy_type(self):
        actual = type(im_not_sleepy())
        expected = str
        self.assertEqual(actual, expected)
