# building a number guessing game in python as my first project

import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    else:
        print(f"Correct! You got it in {attempts} guesses.")
        break