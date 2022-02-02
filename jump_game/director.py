from jump_game.parachute import Parachute
from jump_game.terminal_service import Terminal_Service
from jump_game.puzzle import Puzzle
class Director:
    def __init__(self):
        self._is_playing = True
        self._guess =''
    def start_game(self):
        while self._is_playing:
            self.do_inputs()
            self.do_outputs()
    def do_inputs(self):
        guess = input("Guess a letter [A-Z]: ")
        self._guess=guess
    def do_outputs(self):
        print("done")