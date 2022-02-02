def main():
    file_name = input("Where is your board located? ")
    read_board(file_name)
    
def read_board(file_name):
    try: 
        file = open(file_name,"r")
        board = file.read()
        return board
    except: 
        print("not a valid name")
def play_game(board):
    row = input("What row would you like to place the number value: ")
    column = input("What column would you like to place the number value: ")
    number = input("What number do you want to place there? ")
    valid =  valid_place(board,number,row,column)
    if valid:
        board[row][column] = number
        
def valid_place(board,number,row,column):
    return True
def parse_input(coordinate):
    for letter in range(len(coordinate)):
        if  "A"<=letter<="Z":
            column = ord(letter) - ord("A")
        if 1<= letter<=9:
            row = letter -1
    return(row,column)
def display_board(board):
    print("A B C D E F G H I ")
    for row in range(0,8):
        if row == 3 or row == 6:
            print("--+--+--+")
        for column in range (0,8):
            seperate = "  |  |  \n"
            print( board[row][column] or ' ')
            print( seperate[column])
def update_board(board):

