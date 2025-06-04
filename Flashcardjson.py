import json


def flashcards():
      try:
          with open("flashcards.json", "r") as file:
              flashcards = json.load(file)
      except FileNotFoundError:
          flashcards = []

      q = input("Enter question: ")
      a = input("Enter answer: ")

      flashcards.append({"question": q, "answer": a})

      with open("flashcards.json", "w") as file:
          json.dump(flashcards, file, indent=2)

      print("Card added!")    

flashcards()