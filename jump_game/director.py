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
            self.parachute.print_starting_image()
            self.do_inputs()
            self.do_outputs()
<<<<<<< HEAD
            if self.puzzle._game_done:
                self._is_playing = False



=======

            
>>>>>>> 96d18481e43a6206a2371b86436d1acc984d5a7a
    def do_inputs(self):
        self.guess = input("Guess a letter [A-Z]: ")

    def do_outputs(self):
        if not self.puzzle._game_done():
            self.parachute._during_game_image()
            

        print("done")