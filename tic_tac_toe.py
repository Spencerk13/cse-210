# Tic Tac Toe Game
# Author: Spencer Kingbury

X = 'X'
O = 'O'
BLANK = ' '
board = [BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK,BLANK]

def main():
    print("Enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")
    while game_done(board,message=True) == False:
        display_board(board)
        is_x_turn(board)
        play_game(board)
    display_board(board)

def display_board(board):
    # Prints the board to the user.
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")
def is_x_turn(board):
    # Determines who turn it is.
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
    # Plays the game of tic tac toe.
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

if __name__ == "__main__":
    main()