import json

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
class FlashcardApp:
    def __init__(self, file_name):
        self.file_name = file_name
        self.deck = self.load_deck()

    def load_deck(self):
        try:
            with open(self.file_name, "r") as file:
                return [Flashcard.from_dict(d) for d in json.load(file)]
        except (json.JSONDecodeError):
            print(f"[Error] The file '{self.file_name}' is corrupted or not a valid JSON file!")
            return []
        except (FileNotFoundError):
            print(f"[Info] No existing flashcard file found at '{self.file_name}'. Starting with an empty deck.")
            return []  

    def save_deck(self):
        with open(self.file_name, "w") as file:
              json.dump([c.to_dict() for c in self.deck], file, indent=2)


    def add_flashcard(self, question, answer):
          self.deck.append(Flashcard(question, answer))
          self.save_deck()
          print("Card added!")  
    
    def add_flashcard_from_input(self):
            question = input("Enter question: ").strip()
            answer = input("Enter answer: ").strip().lower()
            self.add_flashcard(question, answer)
        

    def delete_flashcard(self, delete_num):
        if 0 <= delete_num < len(self.deck):
            del self.deck[delete_num]
            self.save_deck()
            print("Flashcard deleted!")
        else:
            print(f"Please choose a number between 1 and {len(self.deck)}")

    def delete_flashcard_from_input(self):
        for i, card in enumerate(self.deck):
            print(f"{i+1}. {card.question}")
        try:
            delete_num = int(input("Choose which number flashcard you wish to delete:")) -1
            self.delete_flashcard(delete_num)
        except ValueError:
            print("This is not a number")

    def check_flashcard_from_input(self):
        if not self.deck:
            print("No flashcards to practice.")
            return
        for card in self.deck:
            print(card.question)
            user_answer = input("Your answer: ")
            card.check_flashcard(user_answer)


    def run(self):
        while True:
            print("""
                  1. Add a flashcard
                  2. Practice
                  3. Delete a flashcard
                  4. Exit
                  """)
            choice = input("Choose (1-4): ").strip()
            if choice == "1":
                self.add_flashcard_from_input()
            elif choice == "2":
                self.check_flashcard_from_input()
            elif choice == "3":
                self.delete_flashcard_from_input()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

app = FlashcardApp("Project.json")
app.run()