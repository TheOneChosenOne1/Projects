class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check_answer(self, user_input):
        return user_input.strip().lower() == self.answer.lower()

def practice(deck):
        for card in deck:
             print(card.question)
             user = input("Your answer: ")
             if card.check_answer(user):
                 print("Correct!")
             else:
               print(f"Wrong! The answer was: {card.answer}")


with open("Classobject.txt", "r") as file:
      content = file.read()
      question_blocks = content.strip().split("\n\n")
      deck = []
      for block in question_blocks:
         lines = block.strip().split("\n")
         card = Flashcard(lines[0], lines[1].strip().lower())
         if len(lines) == 2:
                deck.append(card)

practice(deck)