#rock paper scissor game
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

import random
choice_comp = random.randint(0,2)
user_1 = int(input("What do you choose? type 0 for Rock, 1 for Paper and 2 for Scissors"))
if user_1 == 0:
    print(f"Your choice: \n{rock}")
elif user_1 == 1:
    print(f"Your choice: \n{paper}")
else:
    print(f"Your choice: \n{scissors}")
list_1 = [rock,paper,scissors]
print("computer choice: \n")
print(list_1[choice_comp])

if user_1 == 0 and choice_comp == 0:
    print("Draw")
if user_1 == 1 and choice_comp == 1:
    print("Draw")
if user_1 == 2 and choice_comp == 2:
    print("Draw")

if user_1 == 0 and choice_comp == 1:
    print("Computer Wins")
elif user_1 == 1 and choice_comp == 0:
    print("User Wins")
elif user_1 == 0 and choice_comp == 2:
    print("Computer Wins")
elif user_1 == 2 and choice_comp == 0:
    print("Computer Wins")

