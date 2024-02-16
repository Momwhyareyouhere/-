# guess_the_animal.py

import random

def guess_the_animal():
    animals = ['elephant', 'tiger', 'giraffe', 'lion', 'zebra', 'bear']  # Example animal list

    chosen_animal = random.choice(animals).lower()

    print("Welcome to Guess the Animal Game!")
    print("I'm thinking of an animal. Try to guess it!")

    attempts = 3

    while attempts > 0:
        guess = input("Enter your guess: ").lower()

        if guess == chosen_animal:
            print("Congratulations! You guessed the animal!")
            return

        print("Incorrect guess. Try again.")
        attempts -= 1

    print(f"Sorry, you've run out of attempts. The animal was '{chosen_animal}'. Try again!")

if __name__ == "__main__":
    guess_the_animal()
