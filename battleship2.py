# len(board[0])

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

    
 
def play(board):
    row_list = []
    column_list = []
    print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. You will get 3 chances to sink my ship. Colomns and rows are labled 0-5. Choose wisely and have fun!")
    print("First Missile Launch")
    turn = 1
    while turn <= 5 :
        try:
            L1 = int(input("Row: ")) 
            row_list.append(L1)
            if L1 not in range(len(board[0])): 
                print("Your guess is out of range. You lose a turn!")
            else:
                L1C = int(input("Column: "))
                column_list.append(L1C)
                if L1C not in range(len(board[0])):
                    print("Your guess is out of range. You lose a turn!")        
        except ValueError:
            print("Numbers only please")
        else:       
            print("Missile Launch")
        turn = turn + 1
    while turn >= 5:
        print("You have run out of turns.")
        break
     
    
board = MakeBoard(5)
play(board)



























