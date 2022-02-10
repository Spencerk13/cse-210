from parachute import Parachute
from guess import Guess
from puzzle import Puzzle
from terminal_service import TerminalService

class Director:
    def __init__(self):
        self._is_playing = True
        self.parachute = Parachute()
        self.guess = Guess()
        self.puzzle = Puzzle()
        self.terminal_service = TerminalService()

    def start_game(self):
        while self._is_playing:
            self.puzzle._make_puzzle()
            self.puzzle._display_puzzle()
            self.parachute.print_image()
            self.do_inputs()
            self.do_outputs()
            if self.puzzle._game_done:
                self._is_playing = False
        
        self.parachute.print_end_image()
        print('Your dead!')



    def do_inputs(self):
        guess = self.terminal_service._read_guess('Guess a letter A-Z: ')
        if self.puzzle._guess_right(guess):
            self.parachute.update_image()
            
        

    def do_outputs(self):
        if not self.puzzle._game_done() and not self.puzzle._guess_right():
            self.parachute.update_image()
            self.puzzle._make_puzzle()
        



        print("done")