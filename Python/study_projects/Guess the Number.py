import random
LOGO ="""
________                                 ___________.__               _______                  ___.                   
 ╱  _____╱  __ __   ____    ______  ______ ╲__    ___╱│  │__    ____    ╲      ╲   __ __   _____ ╲_ │__    ____ _______ 
╱   ╲  ___ │  │  ╲_╱ __ ╲  ╱  ___╱ ╱  ___╱   │    │   │  │  ╲ _╱ __ ╲   ╱   │   ╲ │  │  ╲ ╱     ╲ │ __ ╲ _╱ __ ╲╲_  __ ╲
╲    ╲_╲  ╲│  │  ╱╲  ___╱  ╲___ ╲  ╲___ ╲    │    │   │   Y  ╲╲  ___╱  ╱    │    ╲│  │  ╱│  Y Y  ╲│ ╲_╲ ╲╲  ___╱ │  │ ╲╱
 ╲______  ╱│____╱  ╲___  >╱____  >╱____  >   │____│   │___│  ╱ ╲___  > ╲____│__  ╱│____╱ │__│_│  ╱│___  ╱ ╲___  >│__│   
        ╲╱             ╲╱      ╲╱      ╲╱                  ╲╱      ╲╱          ╲╱              ╲╱     ╲╱      ╲╱        
"""
print(LOGO)
def lifes():
    values = input("Which difficulty level you want? Hard or easy!! \n").lower()
    status = True
    while status:
        if values == "easy":
            life = 10
            return life
        elif values == "hard":
            life = 5
            return life
        else:
            print("Retry")


def choices(true_number):
    health = lifes()
    while health > 0:
        guess_num = int(input("What is your guess?"))
        if guess_num == true_number:
            print(f"You guessed it right. The number is {true_number}")
            print(f"Your health is {health}")
            return
        elif guess_num > true_number:
            print(f"Your guess {guess_num} is too high!")
            health -= 1
            print(f"Your health is {health}")
        elif guess_num < true_number:
            print(f"Your guess {guess_num} is too low!")
            health -= 1
            print(f"Your health is {health}")
    print(f"You lost, the number was {true_number}")

def guess():

     print("Welcome to the Number Guessing Game!")
     print("I'm thinking of a number between 1 and 100.")
     number = random.randint(1,100)
     choices(true_number = number)
guess()