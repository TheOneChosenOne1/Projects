class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_input):
        return user_input.strip().lower() == self.answer.lower()

class FlashcardApp:
    def __init__(self, file_name):
        self.file_name = file_name
        self.deck = self.load_deck()

    def load_deck(self):
        deck = []
        try:
            with open(self.file_name, "r") as file:
                content = file.read()
                question_blocks = content.strip().split("\n\n")
                for block in question_blocks:
                    lines = block.strip().split("\n")
                    if len(lines) == 2:
                        card = Flashcard(lines[0], lines[1].strip().lower())
                        deck.append(card)
        except FileNotFoundError:
            print("No flashcard file found yet.")
        return deck

    def add_flashcard(self):
        question = input("Enter a new question: ").strip()
        answer = input("Enter the answer: ").strip().lower()
        if question and answer:
            with open(self.file_name, "a") as file:
                file.write(f"{len(self.deck)}. Question: {question}\n")
                file.write(f"{len(self.deck)}. Answer: {answer}\n\n")
            print("Flashcard added!")
            self.deck.append(Flashcard(question, answer))
        else:
            print("You must provide both question and answer.")

    def delete_flashcard(self):
        for line in open(self.file_name, "r").readlines():
            print(line.strip())

        try:
            delete_num = int(input("Which number do you want to delete? "))
        except ValueError:
            print("That's not a valid number.")
            return

        with open(self.file_name, "r") as file:
            lines = file.readlines()

        lines = [line for line in lines if not line.startswith(f"{delete_num}.")]

        with open(self.file_name, "w") as file:
            file.writelines(lines)

        print("Flashcard deleted!")
        self.deck = self.load_deck()

    def practice(self):
        if not self.deck:
            print("No flashcards to practice.")
            return
        for card in self.deck:
            print(card.question)
            user = input("Your answer: ")
            if card.check_answer(user):
                print("Correct!")
            else:
                print(f"Wrong! The answer was: {card.answer}")

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
                self.add_flashcard()
            elif choice == "2":
                self.practice()
            elif choice == "3":
                self.delete_flashcard()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

app = FlashcardApp("Classobject.txt")
app.run()