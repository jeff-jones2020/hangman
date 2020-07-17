class Word():
    def __init__(self, chars):
        self.word = chars
        self.cur_guess = ''
        self.display = ''
        for char in chars:
            self.guess = '_'

    def make_guess(self, char):
        if char in self.guess:
            print('You have already guessed "' + char + '". Try again.')
        elif char in self.word:
            self.update_guess(char)


    def update_guess(self, valid_char):
        for index in range(len(self.word)):
            if self.word[index] == valid_char:
                self.guess[index] = valid_char

        print('Updated guess:' + self.guess)


wut = Word('booyah')
print(type(wut))
wut.make_guess('o')
