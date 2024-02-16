# dice_rolling.py

import random

def roll_dice():
    print("Welcome to the Dice Rolling Game!")
    print("Roll the dice and see what you get.")

    while True:
        input("Press Enter to roll the dice...")
        result = random.randint(1, 6)
        print(f"You rolled: {result}")

        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    roll_dice()
