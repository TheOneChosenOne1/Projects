import unittest
from FlashcardProjectModularized import FlashcardApp
from flashcard import Flashcard
from Exceptions import (
    DuplicateFlashcardError,
    QuestionTooLongError,
    AnswerTooLongError,
    EmptyFieldError,
    EmptyDeckError,
    NotANumberError,
    OutOfRangeError,
    NeedConfirmationError
)


class TestFlashcardApp(unittest.TestCase):
    def test_add_flashcard(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        app.add_flashcard("Largest animal", "Whale")
        self.assertEqual(len(app.deck), 1)
        self.assertEqual(app.deck[0].question, "Largest animal")

    def test_add_empty_question(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        with self.assertRaises(EmptyFieldError):
            app.add_flashcard("", "Meow")


    def test_add_question_length(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        with self.assertRaises(QuestionTooLongError):
            app.add_flashcard("word"*200, "Whale")
    
    def test_add_answer_length(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        with self.assertRaises(AnswerTooLongError):
            app.add_flashcard("word", "Whale"*200)
    
    def test_add_duplicate(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        app.add_flashcard("Largest animal", "Whale")
        with self.assertRaises(DuplicateFlashcardError):
            app.add_flashcard("Largest animal", "Whale")

    def test_delete_from_empty(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        with self.assertRaises(EmptyDeckError):
            app.delete_flashcard(0)

    def test_delete_invalid_index(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        app.add_flashcard("Largest animal", "Whale")
        with self.assertRaises(OutOfRangeError):
            app.delete_flashcard(1)
    
    def test_delete_not_number(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        app.add_flashcard("Largest animal", "Whale")
        with self.assertRaises(NotANumberError):
             app.delete_flashcard("ok")

    def test_delete_success(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        app.add_flashcard("Largest animal", "Whale")
        app.delete_flashcard(0, force=True)
        self.assertEqual(len(app.deck), 0)

    def test_check_flashcard_empty(self):
        app = FlashcardApp("dummy.json")
        app.deck = []
        result = app.check_flashcard_from_input()
        self.assertEqual(result, "empty")
    
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