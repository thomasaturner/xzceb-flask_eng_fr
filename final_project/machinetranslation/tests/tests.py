
import unittest

from translator import english_to_french, french_to_english

class TestE2f(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestF2e(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
