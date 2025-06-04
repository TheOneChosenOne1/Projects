class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check_answer(self, user_input):
        return user_input.strip().lower() == self.answer.lower()

card = Flashcard("What is 2 + 2?", "4")


if card.check_answer(" 4 "):
    print("Correct!")