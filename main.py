# HangPython
# Selects random word from list and prompts user for letter guesses to solve the word
from words import *

word_list_path = "word_list.txt"

def main():
    print("Welcome to HangPython!")
    word_list: list[str] = []
    try:
        word_list = get_words(word_list_path)
        print(f"Loaded the word library located at {word_list_path}")
    except OSError:
        print(f"Error opening file: {word_list_path}")
    except Exception as e:
        print(e)

    print(f"All words found: {word_list}")

    print(f"Pikcing a random word from {word_list_path}...")
    word = pick_word(word_list)
    print(f"{word} is the word!")


if __name__ == "__main__":
    main()
