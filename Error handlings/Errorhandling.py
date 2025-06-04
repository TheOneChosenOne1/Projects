def calculator():
      while True:
          while True:
              try: 
                First_number= float(input("Enter a number:"))
                break
              except ValueError:
                print("This is not a number!")
          
          while True:
              try:
                  Second_number= float(input("Enter a second number:"))
                  if Second_number ==0:
                      print("You cannot divide by zero")
                  else:
                      break
              except ValueError:
                print("This is not a number!")
          print(First_number/Second_number)
          Goagain= input("Do more calculation Yes/No: ").lower()
          if Goagain !="yes":
              print("Goodbye!")
              break
      

        
calculator()              