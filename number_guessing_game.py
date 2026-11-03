
# Codveda Technologies
# Python Development Internship
# Task 2: Number Guessing Game

import random

secret_number = random.randint(1, 100)

attempts = 7

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")
print("You have 7 attempts.")

for i in range(1, attempts + 1):

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", i)
        break

    elif guess < secret_number:
        print("Too low! Try a higher number.")
        print("Attempts left:", attempts - i)

    else:
        print("Too high! Try a lower number.")
        print("Attempts left:", attempts - i)

else:
    print("Sorry! You have used all attempts.")
    print("The correct number was:", secret_number)
