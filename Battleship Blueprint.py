from random import randrange
#Creates a board. Returns a board of the specified length.
def MakeBoard(square):
    board = [["[   ]"]*square]*square
    return board
#Method which prints the game board with labels. Key word: PRINTS!
def PrintBoard(board):
    y = "+  0"
    for i in range(len(board[0])-1):
        y = y + "    " + str(i + 1)
    print(y)
    for row in range(len(board[0])):
        y = str(row)
        for col in range(len(board[0])):
            y = y + board[row][col]
        print(y)
#Randomizes a new battleship point and returns a 1D array that acts as a 2D array. 
def create(board):
     returnable = []
     choose_col = randrange(0, len(board[0]))
     choose_row = randrange(0, len(board[0]))
    
     create_ship = choose_col, choose_row
    
     h_v = randrange(0,2)
     if h_v == 0:
        if choose_col == len(board[0])-1:
             returnable.append([choose_col - 2, choose_row])
             returnable.append([choose_col - 1, choose_row])
             returnable.append([create_ship])
        elif choose_col == 0:
             returnable.append([create_ship])
             returnable.append([choose_col + 1, choose_row])
             returnable.append([choose_col + 2, choose_row])
        else:
             returnable.append([choose_col + 1, choose_row])
             returnable.append([create_ship])
             returnable.append([choose_col - 1, choose_row])
     elif h_v == 1:
         if choose_row == len(board[0])-1:
             returnable.append([choose_col, choose_row - 2])
             returnable.append([choose_col, choose_row - 1])
             returnable.append([create_ship])
         elif choose_row == 0:
             returnable.append([create_ship])
             returnable.append([choose_col, choose_row + 1])
             returnable.append([choose_col, choose_row + 2])
         else:
             returnable.append([choose_col, choose_row + 1])
             returnable.append([create_ship])
             returnable.append([choose_col, choose_row - 1])
     return returnable
#Creates a Reference-Board that has the ships
def ReferenceBoard(board):
    newBoard = [["[   ]"]*len(board[0])]*len(board[0])
    