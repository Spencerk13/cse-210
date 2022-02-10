# Jumper Specification
<<<<<<< HEAD
Second team activity (team 7) 
=======
Secdon team activity (team 7) 
>>>>>>> fd2f978eb9a6924bef7a430627e1f8e8df79d517

Names: Charlie Mitts mit18012@byui.edu, James Chan cha20009@byui.edu, Spencer Kingsbury kin20013@byui.edu, Samuel Casellas cas18010@byui.edu


Date: Feb 12, 2022

# Code Planning

There are four classes for this program:

1. Director
2. Terminal Service
3. Puzzle
4. Parachute

The following responsibilities, behaviors, and statuses are as follows:


- Director:
1. Responsibilities - Run the game by verifying the conditions of the game are always true before each guess. Keeps track of the players guesses. Asks the user two questions: if they want another turn and what their guess is for the card (whether higher or lower).

2. Behaviors:
    a. Initiate the game (main): start_game()
    b. Has the user guess a letter: guess_word()


3. Status:
    a. Dealer - self._dealer (class)
    c. Next Guess - self._guess (str)
    d. Playing? - self._is_playing (bool)
    e. Player's lives - dealer.life (int)

- Terminal Service:
1. Responsibilities - Get input entered by the user and send it to the director. Write out prompts for the user to enter information for.
2. Behavoir's:
    a. Read text entered by user: _read_text()
    b. Read the users guess they inputed: _read_guess()
    c. Prompt the user for another guess: _write_text()
3. Status:
    a. Terminal Service - self._display(class)

- Parachute:
1. Responsibilities - Display a person with a parachute with a certain a mount of lines. Keep track of how much of the parachute is left, and remove a line if the user guesses a wrong value.
2. Behavoir's: 
    a. Removes part of the person's parachute if they guess a value wrong: _disintegrate()
    b. Gets how much of the parachute is left and displays it to the director: _during_game_image()
    c. Finds out if the game is over if the parachute is gone: _end_game_image()
3. Status:
    a. Parachute - self._parachute(class)


- Puzzle:
1. Responsibilities - Randomly chooses a word from a list. Displays the length of the puzzle and puts the letter in everytime the user guesses a letter correctly.

2. Behavior's:
    a. Retrieve the word chosen - self._get_puzzle()
    b. Get the size of the puzzle - self._puzzle_size()
    c. Show the puzzle - display_puzzle()

3. Status:
    a. Puzzle - self._puzzle(class)

    
# Required software
- Python compiler (after 3.7 preferred)
- Your preferred IDE
