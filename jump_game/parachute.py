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

    def image(self):
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit + "\n"
        return parachute_text

    def update_image(self):
        self._parachute.remove(self._parachute[0])

    def game_over_image(self):
        self._parachute[0] = "      x      " # My mans dead
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit+ "\n"
        return parachute_text
    
