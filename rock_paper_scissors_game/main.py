import random

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

game_images = [rock, paper, scissors]


players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if players_choice >= 0 and players_choice <= 2:
    print(game_images[players_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose : \n {game_images[computer_choice]}")



if players_choice == 0 and computer_choice == 2:
    print("You win!")
elif players_choice >= 3 or players_choice < 0:
    print("You typed an invalid number. You lose!")
elif computer_choice == 0 and players_choice == 2:
    print("You lose!")
elif computer_choice > players_choice:
    print("You lose!")
elif players_choice > computer_choice:
    print("You win!")
elif computer_choice == players_choice:
    print("It's a draw!")