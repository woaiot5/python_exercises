from os import system, name
import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
game_on = True

while game_on:
    system('cls' if name == 'nt' else 'clear')
    print(logo)
    number = random.randint(1, 100)
    level = {"easy": 10, "medium": 7, "hard": 5}

    attempts = level[input("Select difficulty level: easy/medium/hard\n").lower()]
    print(f"You have {attempts} attempts!")
    messages = {0: "Guess a number from 1 to 100:\n",
                1: "Incorrect, your number is too high. Guess again:\n",
                2: "Incorrect, your number is too low. Guess again:\n"}
    i = 0
    while attempts > 0:
        guess = int(input(f"{messages[i]}"))
        if number == guess:
            attempts = 0
        if attempts >= 1:
            if guess > number:
                i = 1
            else:
                i = 2
            attempts -=1

    if number == guess:
        print("\nCorrect! You won!")
    else:
        print(f"\nNo more attempts. You lose. Correct number was {number}")

    game_on = (input("Do you want to play again? y/n:\n").lower() == "y")

system('cls' if name == 'nt' else 'clear')
print(logo)
print("\nThank you for playing, have a good one!")