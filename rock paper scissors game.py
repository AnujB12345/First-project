import random
def main():
   Valid = False
   while Valid == False:
      user_choice = input("What is your choice(rock, paper, scissors): ").lower()
      if user_choice not in possible_choices:
         print(f"{user_choice} is not a valid choice, try again")
         Valid = False
      else:
         Valid = True
   computer_choice = random.choice(possible_choices)
   print("Computer chose: ",computer_choice)
   result(user_choice, computer_choice)

def result(user_choice, computer_choice):
   global user_score, computer_score
   if user_choice == computer_choice:
      print("It's a tie. You both chose the same thing!")
   elif user_choice == "rock":
      if computer_choice == "scissors":
         print("You won, well done.")
         user_score+=1
      else:
         print("You lost, unlucky")
         computer_score +=1
   elif user_choice == "scissors":
      if computer_choice == "paper":
         print("You won, well done.")
         user_score+=1
      else:
         print("You lost, unlucky")
         computer_score +=1
   elif user_choice == "paper":
      if computer_choice == "rock":
         print("You won, well done.")
         user_score+=1
      else:
         print("You lost, unlucky")
         computer_score +=1
   play_again()


def play_again():
   global computer_score, user_score
   again = input("Press any key to play again or 1 to quit: ")
   if again == "1":
      print(f"Your score: {user_score}")
      print(f"Computer score: {computer_score}")
      if user_score>computer_score:
         print("You won overall, well done.")
      elif user_score<computer_score:
         print("You lost overall. Unlucky.")
      else:
         print("You both drew.")
      print("Goodbye")
      exit()
   else:
      main()

possible_choices = ["rock", "paper", "scissors"]
name  = input("What is your name?: ").title()
print(f"Hello {name}, this is a game of rock, paper, scissors against the computer. Good luck!")
user_score = 0
computer_score =0 
main()