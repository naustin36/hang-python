# HangPython
# Selects random word from list and prompts user for letter guesses to solve the word
from words import *
from game import *
from game_files import *
import sys

def main():
    while True:
        print("\n\nWelcome to HangPython!")

        # Load word list
        config = load_config()
        wordlist_path = config["wordlist_path"]
        word_list: list[str] = load_words(wordlist_path)

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
                    config["wordlist_path"] = new_path
                    save_config(config)
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
