#Contact book 
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(contacts.get("Bob", "Not found"))
contacts["Diana"] = "555-0000"
contacts["Alice"] = "555-1111"

for name, number in contacts.items():
    print(name,":", number)

#Letter counter
word = "banana"
letter_count = {}

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)

#Challenge C
sentence = "the cat chased the mouse and the cat won"
sentence = sentence.split()
word_count = {}
for word in sentence:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)