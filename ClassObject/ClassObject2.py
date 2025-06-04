
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check_answer(self, user_input):
        return user_input.strip().lower() == self.answer.lower()

# 1. Create flashcards
card1 = Flashcard("What is the capital of France?", "Paris")
card2 = Flashcard("What is 5 * 3?", "15")
deck = [card1, card2]

# 2. Loop through and use check_answer
for card in deck:
    print(card.question)
    user = input("Your answer: ")
    if card.check_answer(user):
        print("Correct!")
    else:
        print(f"Wrong! The answer was: {card.answer}")