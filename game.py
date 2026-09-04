class Game:
    def __init__(self, word: str):
        self.word = word
        self.obscured_word = []
        self.python = ""
        self.complete_python = "-====o-<"
        self.guesses: list[str] = []
        self.round = 1

    def obscure_word(self, word: str) -> None:
        for letter in word:
            self.obscured_word.append("_")

    def guess_letter(self, letter):
        if not letter.isalpha() or len(letter) > 1 or len(letter) < 1:
            raise ValueError("Guess must be a single letter A-Z\n")

        if letter in self.guesses:
            raise ValueError("Letter already guessed\n")

        self.guesses.append(letter)

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.obscured_word[i] = letter
        else:
            self.python += self.complete_python[0+len(self.python)]

    def has_lost(self):
        return self.python == self.complete_python
    def has_won(self):
        return "".join(self.obscured_word) == self.word

    def game_over(self, result: str) -> dict:
        return {
            "result":result,
            "word":"".join(self.obscured_word),
            "python":self.python,
            "guesses":" ".join(self.guesses)
        }

    def game_state(self):
        print(f"Round {self.round}")
        print(f"Letters guessed: {" ".join(self.guesses)}\n")
        print(f"Python: {self.python}\n")
        print(" ".join(self.obscured_word))
