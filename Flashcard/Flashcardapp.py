import random

def Add_flashcard():
  with open("flashcard.txt", "r") as file:
     content = file.read()
     Number_card = len(content.strip().split("\n\n"))
  with open("flashcard.txt", "a") as file:
    Add = input("Enter a new question: ")
    Answer = input("Enter the answer to your question:").strip().lower()
    if Add and Answer:
         file.write(f"{Number_card}. Question: {Add}\n")
         file.write(f"{Number_card}. Answer: {Answer}\n\n")
         print("\nYour question was successfully added!")
    else:
       print("You have not written a question or there is no answer")

def Delete_flashcard():
   with open("flashcard.txt", "r") as file:
        View = file.readlines()
        for line in View:
          print(line.strip())
   with open("flashcard.txt", "w") as file:
      try:
        Delete = int(input("Select the number of the question you wish to delete").strip())
        for number in View[:]:
            if number.startswith(str(Delete) + "."):
                View.remove(number)
        file.writelines(View)
        print("\nThis flashcard was successfully deleted!")
      except (FileNotFoundError, ValueError):
         print("\nThe file is empty or this is not a number")

def Practice_flashcard():
   with open("flashcard.txt", "r") as file:
      content = file.read()
      question_blocks = content.strip().split("\n\n")
      random.shuffle(question_blocks)
      for block in question_blocks:
         lines = block.strip().split("\n")
         question_text = lines[0]
         Answer = lines[1].split(": ")[1].strip().lower()
         print(question_text)
         check_Answer(Answer)

def check_Answer(Answer):
   Practice_answer = input("\nType your answer here: ").strip().lower()
   if Practice_answer == Answer:
     print("\nYou are correct!\n")
   elif Practice_answer != Answer:
      print("Oops thats not the right answer")
      print(f"The correct answer was {Answer}\n")

def main():
   while True:
      print("""
    1.Add a flashcard
    2.Go through your flashcard
    3.Delete a flashcard
    4.Exit
    """)
      Choice =input("Choose your option between 1-4?\n").strip()
      if Choice == "1":
         Add_flashcard()
      elif Choice == "2":
         Practice_flashcard()
      elif Choice == "3":
         Delete_flashcard()
      elif Choice == "4":
         print("Goodbye!")
         break
      else:
         print("Invalid choice")


main()
