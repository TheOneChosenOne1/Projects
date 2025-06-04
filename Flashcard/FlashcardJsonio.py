import json
from flashcard import Flashcard

def load_deck(file_name):
        try:
            with open(file_name, "r") as file:
                return [Flashcard.from_dict(d) for d in json.load(file)]
        except (json.JSONDecodeError):
            print(f"[Error] The file '{file_name}' is corrupted or not a valid JSON file!")
            return []
        except (FileNotFoundError):
            print(f"[Info] No existing flashcard file found at '{file_name}'. Starting with an empty deck.")
            return []  

def save_deck(file_name, deck):
    with open(file_name, "w") as file:
          json.dump([c.to_dict() for c in deck], file, indent=2)
