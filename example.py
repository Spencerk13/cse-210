"""
class student:
    def __init__(self,fname,lname):
        self._fristname= fname
        self._lastname = lname
    def show_name(self):
        return (f"{self._fristname} {self._lastname}")
    @property
    def firstname(self):
        return self._fristname
    @firstname.setter
    def firstname(self,fname):
        self._firstname = fname
spencer = student("Spencer", "Kingsbury")
spencer._firstname = "bob"

print(spencer.show_name())
"""
puzzle_guess=[]
for i in range(0,3):
    puzzle_guess.append((" _ "))
print(puzzle_guess)