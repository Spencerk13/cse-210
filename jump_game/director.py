from jump_game.parachute import Parachute
from jump_game.terminal_service import TerminalService
from jump_game.puzzle import Puzzle
class Director:
    def __init__(self):
        self._is_playing = True
        self._guess =''
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        while self._is_playing:
            self.do_inputs()
            self.do_outputs()
    def do_inputs(self):
<<<<<<< HEAD
        guess = self._terminal_service.read_number("\nTry to guess a letter ")

=======
        guess = input("Guess a letter [A-Z]: ")
        
>>>>>>> samuel
    def do_outputs(self):
        print("done")