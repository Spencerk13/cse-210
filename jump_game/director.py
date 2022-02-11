from parachute import Parachute
from terminal_service import Terminal_Service
from puzzle import Puzzle

class Director:

    def __init__(self):
        self._is_playing = True
        self._guess = ''
        self.parachute = Parachute()
        self.terminal_service = Terminal_Service()
        self.puzzle = Puzzle()

    def start_game(self):
        while self._is_playing:
            self.parachute.print_image()
            self.do_inputs()
            self.do_outputs()
            self._is_playing = self.puzzle.


    def do_inputs(self):
        self._guess = input("Guess a letter [A-Z]: ")
        self.puzzle.something(self._guess)

    def do_outputs(self):
        print(f"Guessed: {self._guess}")
        if not self.puzzle._correct :
            print('Youre guess was incorrect!')
            self.parachute.update_image()
        print("done")