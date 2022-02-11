import random

class Puzzle:
    def __init__(self):
        self._words = ['nanometer','person','parachute', 'right', 'hair', 'snow','yellow','sunday','church','guess','python','prophet','student','rat', 'angel', 'earth','sun','jump','river','beach']
        self._puzzle = self._words[random.randint(0,19)]
        self._puzzle_array = list(self._puzzle)
        self._puzzle_guess = []

    def make_puzzle(self):
        length = len(self._puzzle)
        for i in range(0,length):
            self._puzzle_guess.append("_")
        return(self._puzzle_guess)

    def guess_right(self,guess):
        match_found = False
        for i in range(len(self._puzzle)):
            if guess.lower() == self._puzzle_array[i]:
                self._puzzle_guess[i] = self._puzzle_array[i]
                match_found = True
        return match_found

    def get_puzzle(self):
        return self._puzzle
        
    def game_done(self):
        for i in range(len(self._puzzle)):
            if self._puzzle_guess[i] == "_":
                return False
        return True

    def display_puzzle(self):
        puzzle = ""
        for i in range(len(self._puzzle)):
            puzzle += self._puzzle_guess[i] + " "
        return puzzle
