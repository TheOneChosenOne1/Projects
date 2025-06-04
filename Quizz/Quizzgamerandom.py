import random

def Ask_question():
  with open("Quizzy.txt", "r") as file:
    content = file.read()
  score = 0
  question_blocks = content.strip().split("\n\n")
  try:
      best_score = int(file.read().strip())
  except (FileNotFoundError, ValueError):
    best_score = 0
  print(f"Current best score: {best_score}")
  random.shuffle(question_blocks)
  for block in question_blocks:
    lines = block.strip().split("\n")
    question_text = lines[0]
    choices = lines[1:5]
    correct_answer = lines[5].split(": ")[1].strip().lower()
    print(f"Your score is now {score}")
    print(question_text)
    for line in choices:
      print(line)
    score =get_Answer(correct_answer, score)
  if score > best_score:
    print("🎉 New high score!")
    with open("score.txt", "w") as file:
        file.write(f"{score}")
  if score == len(question_blocks):
    print("\nGreat job, you did perfect!")
  if score != len(question_blocks):
    if play_again():
      Ask_question()
    else:
      print("\nGoodbye!")
  

def get_Answer(correct_answer, score):
  Answer = input("\nType your answer here: ").strip().lower()
  if correct_answer == Answer:
    print("\nYou are correct!\n")
    return score + 1
  elif correct_answer != Answer:
    print("Oops thats not the right answer")
    print(f"The correct answer was {correct_answer}\n")
    return score
  
def play_again():
  Playagain = input("Looking for a perfect score?! Yes/No: ").lower()
  return Playagain == "yes"



Ask_question()
