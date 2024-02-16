# number_guessing.py

import random

def number_guessing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        attempts += 1
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            return

    print(f"Sorry, you've reached the maximum number of attempts. The number was {secret_number}. Try again!")

if __name__ == "__main__":
    number_guessing()
