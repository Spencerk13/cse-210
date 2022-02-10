class Parachute:
    def __init__(self):
        self._parachute = [
            "     ___     ",
            "    /___\    ",
            "    \   /    ",
            "     \ /     ",
            "      O      ",
            "     /|\     ",
            "     / \     ",
            "             ",
            "^^^^^^^^^^^^^"
        ]

    def _during_game_image(self):
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit + "\n"
        return parachute_text
    
    def _end_game_image(self):
        self._parachute[0] = "      x      " # My mans dead
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit+ "\n"
        return parachute_text

    def print_image(self):
        return (self._during_game_image())

    def update_image(self):
        self._parachute.remove(self._parachute[0])

    def print_end_image(self):
        self.update_image()
        return (self._end_game_image())
    