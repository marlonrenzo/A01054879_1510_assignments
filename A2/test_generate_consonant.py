from unittest import TestCase
from A2.dungeonsanddragons import generate_consonant


class TestGenerateConsonant(TestCase):
    def test_generate_consonant(self):
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        actual_value = generate_consonant()
        self.assertTrue(actual_value in consonant)
