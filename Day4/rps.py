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
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice  = random.randint(0,2)

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
else:
    print(scissors)

if computer_choice == 0:
    print("Computer chose\n",rock)
elif computer_choice == 1:
    print("Computer chose\n",paper)
else:
    print("Computer chose\n",scissors)

if (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
    print("You lose")
elif (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1) or (player_choice == 0 and computer_choice == 2):
    print("You win")
elif player_choice == computer_choice:
    print("Draw") 