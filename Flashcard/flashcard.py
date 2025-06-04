class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_input):
        return user_input.strip().lower() == self.answer.lower()
    
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}
    @staticmethod
    def from_dict(d):
        return Flashcard(d["question"], d["answer"])
    
    def check_flashcard(self, user_answer):
        if self.check_answer(user_answer):
            print("Correct!")
        else:
            print(f"Wrong! The answer was: {self.answer}")