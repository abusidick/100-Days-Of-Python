rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

gesture = [rock,paper,scissors]
player_guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_guess = random.randint(0,2)
#checks for the winner
if player_guess < 0 or player_guess >2:
    print("Number out of range try again!")
elif player_guess == 0 and computer_guess == 1:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You lose ")
elif player_guess == 0 and computer_guess == 2:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You Win ")
elif player_guess == 1 and computer_guess == 2:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You lose ")
elif player_guess == 2 and computer_guess == 0:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You Lose ")
elif player_guess == 2 and computer_guess == 1:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You Win ")
elif player_guess == 1 and computer_guess == 0:
    print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You Win ")
elif player_guess == computer_guess:
     print(f"You Chose:\n{gesture[player_guess]}\nComputer chose:\n{gesture[computer_guess]}\n You Draw ")