import random 

class Puzzle:
    def __init__(self):
        self._words = ['yes','no','maybe']
        self._puzzle = self._words[random.randint(0,2)]
    def get_puzzle(self):
        return 
    def puzzle_size(self):
        length = len(self._puzzle)
        return length
