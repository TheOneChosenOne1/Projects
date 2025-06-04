def Ask_question():
  with open("Quizz.txt", "r") as file:
    lines = file.readlines()
  question_number = 1
  score = 0
  counter = 0
  while question_number < 7:
    start = (question_number - 1) * 7
    end = start + 5
    score_list = []
    if question_number == 6:
      print("\nThis is the end of the quiz!\n")
      with open("Score.txt", "w") as file:
        score_list.append(score)
        maximum = max(score_list)
        file.write(f"Your best score is now {maximum}")
      if score == 5:
        break
      if play_again():
        counter += 1
        Ask_question()
      else:
        print("\nGoodbye!")
        break
    for line in lines[start:end]:
      print(line.strip())
    correct_answer = lines[end].split(": ")[1].strip()
    score = get_Answer(correct_answer, score)
    question_number+=1
    print(f"Your score is now {score}")
    if score == 5:
      print("\nGreat job, you did perfect!")

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