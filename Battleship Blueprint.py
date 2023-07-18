from random import randrange
#Creates a board. Returns a board of the specified length. If the value inputed is less than three, it auto-picks three, as the game NEEDS the board to be at least 3X3.
def MakeBoard(board_size):
    board = []
    if board_size < 3:
        for i in range(3):
            board.append(["[   ]"] * 3)
    else:
        for i in range(board_size):
            board.append(["[   ]"] * board_size)
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
    
     h_v = randrange(0,2)
     if h_v == 0:
        if choose_col == len(board[0])-1:
             returnable.append([choose_col - 2, choose_row])
             returnable.append([choose_col - 1, choose_row])
             returnable.append([choose_col, choose_row])
        elif choose_col == 0:
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col + 1, choose_row])
             returnable.append([choose_col + 2, choose_row])
        else:
             returnable.append([choose_col + 1, choose_row])
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col - 1, choose_row])
     elif h_v == 1:
         if choose_row == len(board[0])-1:
             returnable.append([choose_col, choose_row - 2])
             returnable.append([choose_col, choose_row - 1])
             returnable.append([choose_col, choose_row])
         elif choose_row == 0:
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col, choose_row + 1])
             returnable.append([choose_col, choose_row + 2])
         else:
             returnable.append([choose_col, choose_row + 1])
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col, choose_row - 1])
     return returnable
#Creates a Reference-Board that has the ships
def MakeReferenceBoard(board, coords):
    a = int(coords[0][0])
    b = int(coords[0][1])
    c = int(coords[1][0])
    d = int(coords[1][1])
    e = int(coords[2][0])
    f = int(coords[2][1])
    
    newBoard = board
    newBoard[a][b] = "[ X ]"
    newBoard[c][d] = "[ X ]"
    newBoard[e][f] = "[ X ]"
    return newBoard
#Adds a miss to the board on the specified coords.
def draw_O(board, row, col):
    
    board[row][col] = "[ O ]"   
       
    PrintBoard(board)
#Adds an X to the board on the specified coords.
def draw_X(board, row, col):
    
    board[row][col] = "[ X ]"  
    PrintBoard(board)
#Main game loop.
def play(board, returnable):
    row_list = []
    column_list = []
    print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. You will get 5 chances to sink my ship. Colomns and rows are labled 0-5. Choose wisely and have fun!")
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
        except:
            print("Numbers only please")
        else:       
            print("Missile Launch")
        if (returnable[0] == row_list[len(row_list)-1], column_list[len(row_list)-1]) or (returnable[1] == row_list[len(row_list)-1], column_list[len(row_list)-1]) or (returnable[2] == row_list[len(row_list)-1], column_list[len(row_list)-1]):
            print("HIT!")
            draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
            print("Just pretend we put an X where you just hit lmao")
        else:
            print("MISS!")
            draw_O(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
            print("Just pretend we put an O where you just missed lmao")
        turn = turn + 1
    while turn >= 5:
        print("You have run out of turns.")
        break

board = MakeBoard(10)
#PrintBoard(board)
coords = create(board)
OtherBoard = MakeReferenceBoard(board, coords)
PrintBoard(OtherBoard)
play(board, coords)