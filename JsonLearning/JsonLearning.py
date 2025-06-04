import json

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=2)


with open("contacts.json", "r") as file:
    data = json.load(file)
print(data)