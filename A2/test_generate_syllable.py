from unittest import TestCase
from A2.dungeonsanddragons import generate_syllable


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_length(self):
        expected_value = 2
        actual_value = len(generate_syllable())
        self.assertEqual(actual_value, expected_value)

    def test_generate_syllable_consonant(self):
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        actual_value = generate_syllable()
        self.assertTrue(actual_value[0] in consonant)

    def test_generate_syllable_vowel(self):
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']
        actual_value = generate_syllable()
        self.assertTrue(actual_value[1] in vowel)