import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = input("Enter your guess (or 'exit' to end the game): ")

        if user_guess.lower() == 'exit':
            print(f"The number was {number_to_guess}. Better luck next time!")
            break

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_number()

