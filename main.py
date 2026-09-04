# HangPython
# Selects random word from list and prompts user for letter guesses to solve the word
from mimetypes import guess_extension

from words import *
from game import *
import sys

def main():
    word_list_path: str = "word_list.txt"
    while True:
        print("\n\nWelcome to HangPython!")

        # Load word list
        word_list: list[str] = load_words(word_list_path)

        # Main Menu
        print("Main Menu")
        print("1. Start Game")
        print("2. View Stats")
        print("3. Change Word File")
        print("4. Quit")
        menu_choice = input(">> ")

        if menu_choice == "1":
            print("Starting game...")
            # Create game object
            game = Game(pick_word(word_list))
            # Run the game and store the outcome
            result = run_game(game)
            if not result:
                print("Game ended early")
                continue

        elif menu_choice == "2":
            print("coming soon")
            input("Press any key to continue...")
        elif menu_choice == "3":
            choice = input("Update word file? Y/N >> ")
            if choice.lower() == "y":
                new_path = input("Please enter the new file path >> ")
                try:
                    validate_file(new_path)
                    word_list_path = new_path
                except ValueError as e:
                    print(e)
                    input("Press any key to continue...")
                    continue
            else:
                continue
        elif menu_choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Please enter the number for the option you wish to select")
            input("Press any key to continue...")
            continue

def load_words(word_list_path):
    try:
        print(f"Loaded the word library located at {word_list_path}")
        return get_words(word_list_path)
    except OSError as e:
        print(f"Error opening {word_list_path}: {e.strerror}")
        return []

def validate_file(file_path: str) -> bool | None:
    if not file_path.endswith(".txt"):
        raise ValueError("Filetype must be .txt")
    if len(file_path[0:-4]) == 0:
        raise ValueError("File name must not be blank")
    return True

def run_game(game: Game) -> dict | None:
    game.obscure_word(game.word)
    while True:
        game.game_state()
        guess = input("Guess a letter (1 to quit) >> ").lower()
        if guess == "1":
            return None
        try:
            game.guess_letter(guess)
        except ValueError as e:
            print(e)
            continue
        if game.has_lost():
            game.game_state()
            print("You Lost!")
            return game.game_over("loss")
        if game.has_won():
            game.game_state()
            print("You Won!")
            return game.game_over("win")

if __name__ == "__main__":
    main()
