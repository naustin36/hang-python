import random

def get_words(word_list_path: str) -> list[str]:
    word_list: list[str] = []
    with open(word_list_path) as f:
        word_list = f.read().split()
    return word_list

def pick_word(word_list: list[str]) -> str:
    word: str = word_list[random.randrange(len(word_list))]
    return word
