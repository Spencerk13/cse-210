# Jumper Specification
Second team activity (team 7) 

Names: Charlie Mitts mit18012@byui.edu, James Chan cha20009@byui.edu, Spencer Kingsbury kin20013@byui.edu, Samuel Casellas cas18010@byui.edu


Date: Feb 12, 2022

# Code Planning

There are four classes for this program:

1. Director
2. Terminal Service
3. Parachute
4. Puzzle

The following responsibilities, behaviors, and statuses are as follows:

- Director:
1. Responsibilities - Run the game by verifying the conditions of the game are always true before each guess. Keeps track of the players guesses. Asks the user for the next letter.

2. Behaviors:
    a. Initiate the game (main) - start_game()
    b. Has the user guess a letter - _do_inputs()
    c. Contain conditions for and show the outputs of if the guess is right or not, update the image accordingly, and display guessed letters - _do_outputs()
    d. Check to see if the player is still playing - _still_playing()

3. Status:
    a. Playing? - self._is_playing (bool)
    b. Knows a parachute - self._parachute (class)
    c. Knows a puzzle - self._puzzle (class)
    d. Knows a terminal service - self._terminal_service (class)
    e. Player's lives - self._lives (int)
    f. Player's guesses - self._guesses (list)

- Terminal Service:

1. Responsibilities - Get input entered by the user and send it to the director. Write out prompts for the user to enter information for.
2. Behavoirs:
    a. Read the users guess they inputed: read_guess()
    c. Prompt the user for another guess: write_text()
3. Status:
    (None)

- Parachute:

1. Responsibilities - Display a person with a parachute with a certain amount of lines. Keep track of how much of the parachute is left, and remove a line if the user guesses a wrong letter.
2. Behaviors: 
    a. Return the current image - image()
    b. Removes a layer from the top of the parachute - update_image()
    c. Return the game over image - game_over_image()
3. Status:
    a. Parachute image - self._parachute (list)


- Puzzle:

1. Responsibilities - Randomly chooses a word from a list. Displays the length of the puzzle and puts the letter in everytime the user guesses a letter correctly.

2. Behaviors:
    a. Make the puzzle: - make_puzzle()
    b. Check to see if the letter selected is correct - guess_right(guess)
    a. Retrieve the word chosen - get_puzzle()
    d. Check if the game is done - game_done()
    c. Show the puzzle - display_puzzle()

3. Status:
    a. List of words to pick from - self._words (list)
    b. The word to solve - self._puzzle (str)
    c. The puzzle in the form of an array - self._puzzle_array (list)
    d. The players correctly guessed letters matching with the spaces of the puzzle - self._puzzle_guess (list)

    
# Required software
- Python compiler (after 3.7 preferred)
- Your preferred IDE
