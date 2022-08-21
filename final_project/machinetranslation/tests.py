import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hot weather')['translations'][0]['translation'],'Temps chaud')
    #def test_english_to_french(self):
        self.assertEqual(english_to_french('artificial intelligence')['translations'][0]['translation'], 'Intelligence artificielle')
        self.assertEqual(english_to_french('hello')['translations'][0]['translation'], 'Bonjour')
        self.assertEqual(english_to_french(''), None)


    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('temps chaud')['translations'][0]['translation'], 'Warm weather')
        self.assertEqual(french_to_english('intelligence artificielle')['translations'][0]['translation'], 'Artificial intelligence')
        self.assertEqual(french_to_english('bonjour')['translations'][0]['translation'], 'Hello')
        self.assertEqual(french_to_english(''), None)

if __name__ == '__main__':
    unittest.main()