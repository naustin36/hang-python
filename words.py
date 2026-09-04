def get_words(word_list_path: str) -> list[str]:
    word_list: list[str] = []
    with open(word_list_path) as f:
        word_list = f.read().split()
    return word_list
