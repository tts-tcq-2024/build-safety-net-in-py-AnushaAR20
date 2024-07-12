import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
    
    def test_special_character(self):
        self.assertEqual(generate_soundex("#"), "#000")
        
    def test_word(self):
        self.assertEqual(generate_soundex("Ppndf"), "P531")

    def test_word2(self):
        self.assertEqual(generate_soundex("Lbrl"), "L164")
        
    def empty(self):
        self.assertEqual(generate_soundex(""), "0000")

    def empty(self):
        self.assertEqual(generate_soundex("Ltcvnrl"), "L321")
    
    
if __name__ == '__main__':
    unittest.main()
