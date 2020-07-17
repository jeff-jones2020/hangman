import random

class Game:
    def __init__(self, chars):
        self.word = chars
        self.word_lower = self.word.lower()
        self.wrong_guesses = []
        self.rem_guesses = 5
        self.cur_guess = ''
        for char in chars:
            self.cur_guess += '_'

        self.has_won = False
        self.start_game()


    def start_game(self):
        print('You have ' + str(self.rem_guesses) + ' guesses.')
        self.print_cur_guesses()
        
        while not self.has_won:
            input_str = input('Guess a character: ')
            has_lost = self.make_guess(input_str) == -1
            if has_lost:
                break

        if self.has_won:
            print('You win!')


    def make_guess(self, char):
        char = char.lower()
        if not self.is_valid(char):
            pass
        elif char in self.cur_guess.lower() or char in self.wrong_guesses:
            print('You have already guessed "' + char + '". Try again.')
        elif char in self.word_lower:
            self.update_guess(char)
        else:
            if self.penalize(char) == -1:
                return -1

        print('\n')
        print('You have ' + str(self.rem_guesses) + ' guesses remaining.')
        self.print_cur_guesses()
        return 0
        
    @staticmethod
    def is_valid(char):
        if len(char) != 1:
            print('Please input a single character.')
            return False 
        elif not char.isalpha():
            print('Please enter an alphabetical character.')
            return False
        else:
            return True

        
    def penalize(self, invalid_char):
        self.wrong_guesses.append(invalid_char)
        self.rem_guesses -= 1
        print('"' + invalid_char + '" is not in the word.')

        if self.rem_guesses == 0:
            print('You have lost! Try again.')
            return -1

        return 0
        
    def update_guess(self, valid_char):
        for index in range(len(self.word)):
            cur_char = self.word[index]
            if cur_char.lower() == valid_char:
                self.cur_guess = self.cur_guess[:index] + cur_char + self.cur_guess[index + 1:]

        if self.cur_guess == self.word:
            self.has_won = True

    def print_cur_guesses(self):
        display = ''
        for char in self.cur_guess:
            display += char + ' '

        print('Incorrect guesses: ', self.wrong_guesses)
        print('Current guess: ', display , '\n')


words = ['draGons', 'BLASTERS', 'laZors', 'etCetera']

bored = True

while bored:
    new_game = Game(random.choice(words))
    bored = input('\nPlay again? y/n: ').lower() == 'y'
    print('\n')
    
