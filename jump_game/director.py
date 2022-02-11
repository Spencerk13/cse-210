from parachute import Parachute
from terminal_service import TerminalService
from puzzle import Puzzle

class Director:

    def __init__(self):
        self._is_playing = True
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._lives = 8
        self._guesses = []

    def start_game(self):
        self._puzzle.make_puzzle()
        while self._is_playing:
            self._terminal_service.write_text(f"\n\n{self._parachute.image()}")
            self._terminal_service.write_text(self._puzzle.display_puzzle())
            self._do_outputs(self._do_inputs())
            self._is_playing = self._still_playing()

    def _do_inputs(self):
        guess = self._terminal_service.read_guess("\nTry to guess a letter (a-z) ")
        if guess not in self._guesses:
            self._guesses.append(guess)
        return guess

    def _do_outputs(self, guess):
        right = self._puzzle.guess_right(guess)
        if not right:
            self._lives -= 1
            if self._lives % 2 == 0:
                self._parachute.update_image()
            self._terminal_service.write_text("No matches.")
        else:
             self._terminal_service.write_text("Match!")
        if self._lives == 0:
            self._terminal_service.write_text(f"\n{self._parachute.game_over_image()}")
        self._terminal_service.write_text("Guessed: ", newline=False)
        for letter in self._guesses:
            self._terminal_service.write_text(f"{letter} ", newline=False)

    def _still_playing(self):
        if self._puzzle.game_done() == True:
            self._terminal_service.write_text(f"\n\n{self._parachute.image()}")
            self._terminal_service.write_text(self._puzzle.display_puzzle())
            print("\n\nYou solved the puzzle!\n")
            return False
        elif self._lives == 0:
            self._is_playing = False
            print(f"\n\nThe word was {self._puzzle.get_puzzle()}, better luck next time!\n")
            return False
        else:
            return True

            
