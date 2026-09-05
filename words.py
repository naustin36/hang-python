import random
from pathlib import Path

def pick_word(word_list: list[str]) -> str:
    word: str = word_list[random.randrange(len(word_list))].lower()
    return word

def load_words(word_list_file_path: str) -> list[str]:
    file_path = Path(word_list_file_path).expanduser()
    if not file_path.is_file():
        print(f"Unable to load file at: '{file_path}'")
        return []

    word_list = file_path.read_text().split()
    print(f"Loaded the word library located at '{file_path}'")
    return clean_word_list(word_list)

def clean_word_list(word_list: list[str]):
    # Strip all words containing special characters or words that are too short
    # For user submitted files
    cleaned_list = []
    for word in word_list:
        if len(word) > 5 and word.isalpha():
            cleaned_list.append(word)
    return cleaned_list
