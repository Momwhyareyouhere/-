# main.py
from hangman import hangman
from tic_tac_toe import tic_tac_toe
from number_guessing import number_guessing
from password_generator import generate_password
from dice_rolling import roll_dice
from word_scramble import word_scramble
from rock_paper_scissors import play_rock_paper_scissors  # Importing the 'play_rock_paper_scissors' function

def main_menu():
    print("Welcome to the Mini-Game Collection!")
    print("[1] Hangman")
    print("[2] Tic Tac Toe")
    print("[3] Number Guessing")
    print("[4] Generate Password")
    print("[5] Dice Rolling")
    print("[6] Word Scramble")
    print("[7] Rock, Paper, Scissors")  # Adding the new game to the menu
    print("[0] Exit")

    choice = input("Choose a game to play (1-7), or 0 to exit: ")

    if choice == '1':
        hangman()
    elif choice == '2':
        tic_tac_toe()
    elif choice == '3':
        number_guessing()
    elif choice == '4':
        length = int(input("Enter the length for the password: "))
        print(f"Generated Password: {generate_password(length)}")
    elif choice == '5':
        roll_dice()
    elif choice == '6':
        word_scramble()
    elif choice == '7':
        play_rock_paper_scissors()  # Trigger the 'play_rock_paper_scissors' function
    elif choice == '0':
        print("Exiting the Mini-Game Collection. Goodbye!")
    else:
        print("Invalid choice. Please select a game from 1 to 7.")

if __name__ == "__main__":
    main_menu()
