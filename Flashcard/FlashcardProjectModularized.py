"""
Flashcard App
------------------
A simple terminal-based flashcard application to add, practice, delete, export and import flashcards.
Data is stored in JSON or CSV.
"""


from flashcard import Flashcard
from FlashcardJsonio import load_deck, save_deck
import csv
import random
from Exceptions import (
    DuplicateFlashcardError,
    QuestionTooLongError,
    AnswerTooLongError,
    EmptyFieldError,
    EmptyDeckError,
    NotANumberError,
    OutOfRangeError,
    NeedConfirmationError,
)

class FlashcardApp:
    max_q = 120
    max_a = 60
    def __init__(self, file_name):
        self.file_name = file_name
        self.deck = load_deck(self.file_name)

    def add_flashcard(self, question, answer, force = False):     
          if not question or not answer:
                raise EmptyFieldError("Question and answer cannot be empty.")
          if len(question) > self.max_q:
                raise QuestionTooLongError
          if len(answer) > self.max_a:
                raise AnswerTooLongError
          if any(card.question.lower() == question.lower() for card in self.deck) and not force:
                raise DuplicateFlashcardError    
          self.deck.append(Flashcard(question, answer))
          save_deck(self.file_name, self.deck)
    
    def add_flashcard_from_input(self):  
            while True:
                question= input("Enter a new question or press E to exit: ").strip()
                if question.lower() == "e":
                     print("Exiting adding mode")
                     break
                answer = input("Enter answer: ").strip()
                try:
                     self.add_flashcard(question, answer)
                     print("Card added!")
                except QuestionTooLongError:
                     print(f"Your question is too long (max {self.max_q} characters).")
                     continue
                except AnswerTooLongError:
                     print(f"Your answer is too long (max {self.max_a} characters).")
                     continue
                except EmptyFieldError:
                     print("Question and answer cannot be empty")
                     continue
                except DuplicateFlashcardError:
                     print("You have two identical questions")
                     keep_anyway = self.get_input(f"Duplicate found! Do you still wish to keep the following flashcard\n Question: {question}\n Answer: {answer}\nyes/no: ", valid={"yes", "no"})
                     if keep_anyway == "yes":
                         self.add_flashcard(question, answer, force = True)
                     else:
                         print("The flashcard was not added")
                         continue
                keep_going = self.get_input("Do you wish to keep adding more flashcards?  yes/no :", valid={"yes", "no"})
                if keep_going == "no":
                    break

    def delete_flashcard(self, index, force=False):
        if not self.deck:
            raise EmptyDeckError
        elif not isinstance(index, int):
            raise NotANumberError
        elif not (0 <= index < len(self.deck)):
            raise OutOfRangeError
        elif not force: 
            raise NeedConfirmationError
        del self.deck[index]
        save_deck(self.file_name, self.deck)

                    
    def delete_flashcard_from_input(self):
        while True:
            if not self.deck:
                print("There is no more flashcard to delete")
                break
            for i, card in enumerate(self.deck):
                print(f"{i+1}. {card.question}")
            user_input = input("Choose which number flashcard you wish to delete or press E to exit the mode: ")
            if user_input.lower() == "e":
                print("Exiting deleting mode")
                break
            try:
                index = int(user_input) - 1 
                self.delete_flashcard(index)
            except NotANumberError:
                print("This is not a number, please enter a number this time")
                continue
            except EmptyDeckError:
                print("There is no more flashcard to delete")
                continue
            except OutOfRangeError:
                print(f"Please choose a number between 1 and {len(self.deck)}.")
                continue
            except NeedConfirmationError:
                card = self.deck[index]
                are_you_sure = self.get_input(f"Are you certain you wish to delete flashcard\n{index+1}. Question: {card.question}\n{index+1}. Answer: {card.answer}\n  yes/no: ", valid = {"yes", "no"})
                if are_you_sure == "yes":
                    self.delete_flashcard(index, force=True)
                else:
                    print("No flashcard was deleted")
                    continue
            cont = self.get_input("Delete more flashcards yes/no: ", valid = {"yes", "no"})
            if cont == "no":
                break
    
    def check_flashcard_from_input(self):
        if not self.deck:
            print("No flashcards to practice.")
            return "empty"
        random.shuffle(self.deck)
        for i, card in enumerate(self.deck):
            print(f"Question {i+1}: {card.question}")
            user_answer = input("Your answer: ")
            card.check_flashcard(user_answer)
    
    def export_csv(self):
        with open('flashcard.csv', 'w', newline='') as csvfile:
            try:
                deck_writer = csv.writer(csvfile)
                deck_writer.writerow(["question", "answer"])
                for card in self.deck:
                    deck_writer.writerow([card.question, card.answer])
                print("Deck exported to flashcard.csv!")
            except FileNotFoundError:
                print("There is no file at this location")
            except UnicodeDecodeError:
                print("The file could not be decoded")
            

    def import_csv(self):
        imported = 0
        skipit = 0
        with open('flashcard.csv', 'r', newline='', encoding="utf-8") as csvfile:
            deck_reader = csv.reader(csvfile)
            next(deck_reader)
            startanew = self.get_input("Do you wish to start a new empty deck? yes/no", valid = {"yes", "no"})
            if startanew == "yes":
                self.deck = []
                print("Empty deck created")

            try:
                for row in deck_reader:
                    question = row[0]
                    answer = row[1]
                    if not question or not answer:
                        skipit += 1
                        continue
                    if len(question) > self.max_q or len(answer) > self.max_a:
                        print(f"Skipped long entry: '{question[:30]}...'")
                        skipit += 1
                        continue
                    if any(card.question.lower() == question.lower() for card in self.deck):
                        print(f"Skipped duplicate: '{question[:30]}...'")
                        skipit += 1
                        continue

                    self.deck.append(Flashcard(question, answer))
                    imported += 1
                print(f"{imported} flashcard successfully added to your deck!\n{skipit} flashcard were invalid") 
            except FileNotFoundError:
                print("CSV file not found.")
            except csv.Error as e:
                print(f"CSV error: {e}")

    @staticmethod
    def get_input(prompt, valid=None, lowercase=True):
        while True:
            response = input(prompt).strip()
            if lowercase:
                response = response.lower()
            if valid is None or response in valid:
                return response
            print("Invalid input.")
   
    def run(self):
        while True:
            print("""
                  1. Add a flashcard
                  2. Practice
                  3. Delete a flashcard
                  4. Export to CSV
                  5. Import from CSV
                  6. Exit
                  """)
            choice = self.get_input("Choose (1-6): ", valid={"1", "2", "3", "4", "5", "6"})
            if choice == "1":
                self.add_flashcard_from_input()
            elif choice == "2":
                self.check_flashcard_from_input()
            elif choice == "3":
                self.delete_flashcard_from_input()
            elif choice == "4":
                self.export_csv()
            elif choice =="5":
                self.import_csv()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    try:
        app = FlashcardApp("Project.json")
        app.run()
    except KeyboardInterrupt:
        print("Goodbye!")
