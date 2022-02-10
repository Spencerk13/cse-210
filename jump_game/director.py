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
            self.parachute.print_image()
            self.do_inputs()
            self.do_outputs()
            if self.puzzle._game_done:
                self._is_playing = False



    def do_inputs(self):
        self.guess = input("Guess a letter [A-Z]: ")

    def do_outputs(self):
        if not self.puzzle._game_done() and not self.puzzle._guess_right():
            self.parachute.update_image()
        



        print("done")