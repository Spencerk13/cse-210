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
    
    def disintegrate(self):
        self._parachute.remove(self._parachute[0])

    def show_parachute(self):
        parachute_text = ""
        for unit in self._parachute:
            parachute_text += unit + "\n"
        return parachute_text

"""
parachute = Parachute()

for _ in range(4):
    print(parachute.show_parachute())
    parachute.disintegrate()
"""