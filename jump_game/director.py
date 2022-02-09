from jump_game.parachute import Parachute
from jump_game.guess import Guess
from jump_game.puzzle import Puzzle
class Director:
    def __init__(self):
        self._is_playing = True
        self.parachute = Parachute()
        self.guess = Guess()
        self.puzzle = Puzzle()

    def start_game(self):
        while self._is_playing:
            self.do_inputs()
            self.do_outputs()

    def do_inputs(self):
        self.guess = input("Guess a letter [A-Z]: ")

    def do_outputs(self):
        print("done")