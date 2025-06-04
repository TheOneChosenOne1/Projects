#Challenge 1
numbers = [3, 5, 10, 12, 17, 20]
Numbers_odd = [i for i in numbers if i % 2!=0 ]


#Challenge 2
words = ["apple", "banana", "cherry", "date"]
Five_letters = [fruit for fruit in words if len(fruit) >= 5]


#Challenge 3
grades = [87, 65, 92, 70, 59]
Pass_fail = ["pass" if grade >= 70 else "fail" for grade in grades] 

#Challenge 4
lines = [
    "1. Question: What is 2 + 2?",
    "1. Answer: 4",
    "2. Question: What is the capital of Spain?",
    "2. Answer: Madrid"
    ]

lines = [line for line in lines if not line.startswith("2.")]
print(lines)

#Challenge 5
words_animals = ["cat", "elephant", "tiger", "a", "zebra"]
Short_long = ["long" if len(size) >= 5 else "sort" for size in words_animals] 

#Challenge 6
strings = ["ID123", "age=30", "score=85", "X42"]
digits_only = [''.join([char for char in s if char.isdigit()]) for s in strings]
print(digits_only)

#Challenge 7
nested = [[1, 2], [3, 4, 5], [6]]
def flatten(nested):
   return [i for column in nested for i in column]
nested = flatten(nested)
print(nested)

#Challenge 8 
nums = [4, -1, 9, -3, 2]
Transition = ["Neg" if number < 0 else number for number in nums] 
print(Transition)

#Challenge 9
lines = [
    "1. Question: What is 2 + 2?",
    "1. Answer: 4",
    "2. Question: What is the capital of Spain?",
    "2. Answer: Madrid"
    ]

questions = [line.split("Question: ")[1] for line in lines if "Question" in line]
print(questions)

#Challenge 10
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
nested = [i for column in nested for i in column if i%2 == 0]
print(nested)


#Challenge 11
names = ["Alice", "Bob"]
colors = ["Red", "Blue"]
tuples = [(i,j) for i in names for j in colors] 
print(tuples)

#Challenge 12
sentences = ["hello world", "flash cards", "python power"]
sentences = [column.split() for column in sentences]
sentences = [i for column in sentences for i in column]
sentences = [word[0] for word in sentences]
print(sentences)