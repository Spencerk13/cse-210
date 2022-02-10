from parachute import Parachute
from terminal_service import TerminalService
from puzzle import Puzzle
class Director:
    def __init__(self):
        self._is_playing = True
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._lives = 5
    def start_game(self):
        self._puzzle._make_puzzle()
        self._terminal_service._write_text(self._puzzle.display_puzzle())
        self._terminal_service._write_text(self._parachute.print_image())
        while self._is_playing:
            self.do_inputs()
            self.do_outputs()
            self.done()
    def do_inputs(self):
        guess = self._terminal_service._read_guess("\nTry to guess a letter (a-z) ")
        right = self._puzzle.guess_right(guess)
        if right == False:
            self._lives -=1
            self._parachute.update_image()
    def do_outputs(self):
        if self._lives !=0:
            self._terminal_service._write_text(self._puzzle.display_puzzle())
            self._terminal_service._write_text(self._parachute.print_image())
        elif self._lives ==0:
            self._terminal_service._write_text(self._parachute.print_end_image())
    def done(self):
        if self._puzzle.game_done() == True:
            self._is_playing = False
            print("You solved the puzzle ")
        elif self._lives == 0:
            self._is_playing = False
            print(f"The word was {self._puzzle.get_puzzle()}, better luck next time")

            
