
import random 
<<<<<<< HEAD
words = ['nanometer','person','parachute', 'right', 'hair', 'snow','yellow','sunday','church',
'guess','python','prophet','student','rat', 'angel', 'earth','sun','jump','river','beach']
class Puzzle:
    def __init__(self):
        self._puzzle = words[random.randint(0,19)]
        self._puzzle_array = list(self._puzzle)
        self._puzzle_guess = []
    def _make_puzzle(self):
        length = len(self._puzzle)
        for i in range(0,length):
            self._puzzle_guess.append((" _ "))
        return(self._puzzle_guess)
    def _guess_right(self,guess):
        for i in range(len(self._puzzle)):
            if guess == self._puzzle_array[i]:
                self._puzzle_guess[i] = self._puzzle_array[i]
    def _game_done(self):
        for i in range(len(self._puzzle)):
            if self._puzzle_guess[i] == " _ ":
                return False
        return True
    def _display_puzzle(self):
        puzzle = ''
        for i in range(len(self._puzzle)):
            puzzle += self._puzzle_guess[i]
        print(puzzle)
puzzle = Puzzle()
puzzle._make_puzzle()
puzzle._display_puzzle()
=======

class Puzzle:
    def __init__(self):
        self._words = ['yes','no','maybe']
        self._puzzle = self._words[random.randint(0,2)]
    def get_puzzle(self):
        return 
    def puzzle_size(self):
        length = len(self._puzzle)
        return length
>>>>>>> samuel
