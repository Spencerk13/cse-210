# 1. Name:
#      Spencer Kingsbury
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was trying to figure out how to quit the game mid game.
#      I could figure out how put all the X's and O's down until the game was over, but
#      I couldn't figure out a way for a while to find away to make the game quit.
# 5. How long did it take for you to complete the assignment?
#      I spent 4 hours on this lab. 

import json
from os import read

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    with open(filename) as blank_board:
        board_data = json.load(blank_board)
        return board_data['board']
def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    with open(filename,'r+') as updated_board:
        json_data = json.load(updated_board)
        json_data["board"]=board
        updated_board.seek(0)
        json.dump(json_data,updated_board)
        updated_board.truncate()
def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")
def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    x_total = 0
    o_total = 0
    for index in range(len(board)):
        if board[index] == "X":
            x_total +=1
        elif board[index] == "O":
            o_total +=1
    if x_total > o_total:
        return False
    else:
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    if is_x_turn(board):
        x_input = (input('X>'))
        while board[int(x_input)-1] != BLANK:
            print("Already taking try again! ")
            x_input = (input('X>'))
        board[int(x_input)-1] = X
        return False
    else:
        o_input = int(input('O>'))
        while board[o_input-1] != BLANK:
            print("Already taking try again! ")
            o_input = int(input('O>'))
        board[o_input-1] = O
        return False

def game_done(board, message=True):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
board = read_board("./modular Design/blank_board.json")
#display_board(board)
if game_done(board,message=False) == True:
    with open("./modular Design/blank_board.json",'r+') as updated_board:
        json_data = json.load(updated_board)
        json_data["board"]=blank_board["board"]
        updated_board.seek(0)
        json.dump(json_data,updated_board)
        updated_board.truncate()
board = read_board("./modular Design/blank_board.json")
while game_done(board,message=True) == False:
    display_board(board)
    is_x_turn(board)
    play_game(board)
    save_board("./modular Design/blank_board.json",board)
display_board(board)