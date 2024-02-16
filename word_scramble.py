# word_scramble.py

import random

def word_scramble():
    words = ['python', 'programming', 'algorithm', 'computer', 'science']  # Example word list

    chosen_word = random.choice(words)
    scrambled_word = ''.join(random.sample(chosen_word, len(chosen_word)))

    print("Welcome to the Word Scramble Game!")
    print(f"Unscramble the word: {scrambled_word}")

    attempts = 3

    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == chosen_word:
            print("Congratulations! You unscrambled the word!")
            return

        print("Incorrect guess. Try again.")
        attempts -= 1

    print(f"Sorry, you've run out of attempts. The word was '{chosen_word}'. Try again!")

if __name__ == "__main__":
    word_scramble()
