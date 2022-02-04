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
    
    def _disintegrate(self):
        self._parachute.remove(self._parachute[0])

    def _during_game_image(self):
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit + "\n"
        return parachute_text
    
    def _end_game_image(self):
        self._parachute[0] = "      x      " # My mans dead
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit + "\n"
        return parachute_text





# Test code

parachute = Parachute()

for _ in range(4):
    print(parachute._during_game_image())
    parachute._disintegrate()

print(parachute._end_game_image())

