from unittest import TestCase
from A2.dungeonsanddragons import get_character_name


class TestGetCharacterName(TestCase):
    def test_get_character_name_length(self):
        actual_value = get_character_name(18)
        name_length = len(actual_value)
        self.assertTrue(name_length == 36)

    def est_get_character_name_vowel(self):
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']
        actual_value = get_character_name(10)
        self.assertTrue(actual_value[0] in vowel)

    def est_get_character_name_consonant(self):
        consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
        actual_value = get_character_name(10)
        self.assertTrue(actual_value[4] in consonant)
