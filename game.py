class Game:
    def __init__(self, word: str):
        self.word = word
        self.obscured_word = ""
        self.python = ""
        self.guesses: list[str] = []
        self.round = 0

    def obscure_word(self, word: str) -> None:
        for letter in word:
            self.obscured_word += "_ "

    def guess_letter(self, letter):
        pass

    def game_state(self):
        print(f"Round {self.round}")
        print(f"Letters guessed: {" ".join(self.guesses)}\n")
        print(f"Python: {self.python}\n")
        print(self.obscured_word)
