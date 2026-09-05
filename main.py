# HangPython
# Selects random word from list and prompts user for letter guesses to solve the word
from words import *
from game import *
from game_files import *
from pathlib import Path
import sys

def main():
    config = load_config()
    wordlist_path = config["wordlist_path"]
    word_list: list[str] = load_words(wordlist_path)

    while True:
        print("\n\nWelcome to HangPython!")

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

            record_stats(result)

        elif menu_choice == "2":
            show_stats()

        elif menu_choice == "3":
            print(f"Current word file: {wordlist_path}")
            choice = input("Change word file? Y/N >> ")
            if choice.lower() == "y":
                new_path = input("Please enter the new file path >> ")
                new_word_list = load_words(new_path)
                if not new_word_list:
                    print("No words found, reverting to previous file")
                    continue
                config["wordlist_path"] = new_path
                save_config(config)
                word_list = new_word_list
                print("Successfully loaded new file")
            else:
                continue

        elif menu_choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Please enter the number for the option you wish to select")
            input("Press any key to continue...")

def run_game(game: Game) -> str | None:
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
            return "loss"
        if game.has_won():
            game.game_state()
            print("You Won!")
            return "win"

def show_stats() -> None:
    stats = load_stats()
    print(f"Games Played: {stats["games_played"]}")
    print(f"Games Won: {stats["wins"]}")
    print(f"Games Lost: {stats["losses"]}")

def record_stats(result: str):
    stats = load_stats()
    if result == "win":
        stats["wins"] += 1
    elif result == "loss":
        stats["losses"] += 1
    else:
        raise ValueError("can only record 'win' or 'loss'")
    stats["games_played"] += 1
    save_stats(stats)

if __name__ == "__main__":
    main()
