import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    # def test_empty_string(self):
    #     self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
            self.assertEqual(generate_soundex("A"), "A000")
    
    def test_vowels(self):
            self.assertEqual(generate_soundex("AEIOU"), "A000")
    
    def test_specialchar(self):
            self.assertEqual(generate_soundex("#"), "#000")
        
    def test_word(self):
            self.assertEqual(generate_soundex("Pond"), "P530")


    
if __name__ == '__main__':
    unittest.main()
