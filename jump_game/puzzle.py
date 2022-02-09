from jump_game.terminal_service import TerminalService
import random 
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
    def _guess_right(self):
        for i in range(len(self._puzzle)):
            if TerminalService._read_guess() == self._puzzle_array[i]:
                self._puzzle_guess[i] = self._puzzle_array[i]
                print(self._puzzle_guess)
            else:
                print(self._puzzle_guess)
    def _game_done(self):
        for i in range(len(self._puzzle)):
            if self._puzzle_guess[i] == " _ ":
                return False
        return True
puzzle = Puzzle()
print(puzzle._make_puzzle())