# hangman.py
import random

def hangman():
    words = ['apple', 'banana', 'orange', 'grape', 'melon']  # Example word list

    chosen_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        display = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)
        print(f"Word: {display}")
        print(f"Attempts left: {attempts}")

        if '_' not in display:
            print("Congratulations! You guessed the word!")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in chosen_word:
            attempts -= 1
            print("Incorrect guess!")

    print(f"Sorry, you've run out of attempts. The word was '{chosen_word}'.")
