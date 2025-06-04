import unittest
from flashcard import Flashcard

class TestFlashcard(unittest.TestCase):
    def test_check_answer_exact(self):
        card = Flashcard("Capital of France?", "Paris")
        self.assertTrue(card.check_answer("Paris"))
    
    def test_check_answer_case_insensitive(self):
        card = Flashcard("Capital of France?", "Paris")
        self.assertTrue(card.check_answer("paris"))
    
    def test_check_answer_whitespace(self):
        card = Flashcard("Capital of France?", "Paris")
        self.assertTrue(card.check_answer("  Paris  "))

    def test_check_answer_wrong(self):
        card = Flashcard("Capital of France?", "Paris")
        self.assertFalse(card.check_answer("London"))

if __name__ == "__main__":
    unittest.main()