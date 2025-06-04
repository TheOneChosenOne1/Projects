import json

flashcards = [
    {"question": "Capital of France?", "answer": "Paris"},
    {"question": "2+2", "answer": "4"}
]

with open("flashcards.json", "w") as file:
    json.dump(flashcards, file)


with open("flashcards.json", "r") as file:
    data = json.load(file)

for dictionary in data:
    print(f"Q. {dictionary['question']}\nA. {dictionary['answer']}\n")