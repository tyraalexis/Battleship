from random import randrange
#Creates a board. Returns a board of the specified length. If the value inputed is less than three, it auto-picks three, as the game NEEDS the board to be at least 3X3.
def MakeBoard(board_size):
    board = []
    if board_size < 3:
        for i in range(3):
            board.append(["[   ]"] * 3)
    elif(board_size > 10):
        for i in range(10):
            board.append(["[   ]"] * 10)  
    else:
        for i in range(board_size):
            board.append(["[   ]"] * board_size)
    return board
#Method which prints the game board with labels. Key word: PRINTS!
def PrintBoard(board):
    y = "+   1"
    for i in range(len(board[0])-1):
        y = y + "    " + str(i + 2)
    print(y)
    for row in range(len(board[0])):
        if (row >= 9):
            y = str(row + 1)
        else:
            y = str(row + 1) + " "
        for col in range(len(board[0])):
            y = y + board[row][col]
        print(y)
#Randomizes a new battleship point and returns a 1D array that acts as a 2D array. 
def create(board):
     returnable = []
     choose_col = randrange(0, len(board[0]))
     choose_row = randrange(0, len(board[0]))
     if(board[choose_col][choose_row] != "[   ]"):
        create(board)
     h_v = randrange(0,2)
     if h_v == 0:
        if(board[choose_col - 1][choose_row] != "[   ]" or board[choose_col + 1][choose_row] != "[   ]"):
            create(board)
        if choose_col == len(board[0])-1:
             returnable.append([choose_col - 1, choose_row])
             returnable.append([choose_col, choose_row])
        elif choose_col == 0:
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col + 1, choose_row])
        else:
             returnable.append([choose_col + 1, choose_row])
             returnable.append([choose_col, choose_row])
     elif h_v == 1:
         if(board[choose_col][choose_row + 1] != "[   ]" or board[choose_col][choose_row - 1] != "[   ]"):
             create(board)
         if choose_row == len(board[0])-1:
             returnable.append([choose_col, choose_row - 1])
             returnable.append([choose_col, choose_row])
         elif choose_row == 0:
             returnable.append([choose_col, choose_row])
             returnable.append([choose_col, choose_row + 1])
         else:
             returnable.append([choose_col, choose_row + 1])
             returnable.append([choose_col, choose_row])
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
#Adds an I to the board on the specified coords.
def draw_I(board, row, col):
    board[row][col] = "[ I ]"  
    PrintBoard(board)
#Used in main method for cpu's turn. Returns True if it hits anything. False if it misses.
def cpu_turn(board):
    coords = create(board)
    if(board[coords[0]][coords[1]] == "[   ]"):
        draw_O(board, coords[0], coords[1])
        return False
    elif(board[coords[0]][coords[1]] == "[ I ]"):
        draw_X(board, coords[0], coords[1])
        return True
    else:
        cpu_turn(board)
#Main game loop.
def play():
    while True:
        row_list = [] #List of the user's guessed row values
        column_list = [] #List of the user's guessed column values
        print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. Choose wisely and have fun!")
        try:
            size = int(input("How big would you like your grid to be? "))
            board = MakeBoard(size)
            your_board = MakeBoard(size)
            PrintBoard(board)
            where_r = int(input("In what ROW would you like to place your ship? "))-1
            if where_r not in range(len(board[0])):
                print("Your point is out of range.")
                continue
            else:
                where_c = int(input("In what COLUMN would you like to place your ship? "))-1
                if where_c not in range(len(board[0])):
                    print("Your point is out of range.")
                    continue
                else:
                    pass
            ship1 = (where_r, where_c)
            print("The coordinates of the ship are",ship1[0] + 1, ",", ship1[1] + 1, ".")
            draw_I(your_board, where_r, where_c)
            print("Here is your board!")
           
            ship = create(board)
            
        except ValueError:
            print("Numbers only.")
        else: 
            board = MakeBoard(size)
            PrintBoard(board)
            print("First Missile Launch")
            x = 0
            while True:
                try:
                    L1 = int(input("Row: "))-1
                    row_list.append(L1)
                    if L1 not in range(len(board[0])): 
                        print("Your guess is out of range.")
                        continue
                    else:
                        L1C = int(input("Column: "))-1
                        column_list.append(L1C)
                        if L1C not in range(len(board[0])):
                            print("Your guess is out of range.")
                            continue
                        else:
                            pass
                except:  
                    print("Numbers only please")
                    continue
                else:       
                    car = row_list[len(row_list)-1], column_list[len(column_list)-1]
                    print("Missile Launch")
                    if (ship == car):
                        print("CPU Board")
                        draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                        print("HIT!")
                        x = 1
                    else:
                        print("CPU Board")
                        draw_O(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                        print("MISS!")
                        x = 0
                if(x == 1):
                    while x == 1:
                        again = input("Would you like to play again? y/n? ")
                        if again == "y":
                            play()
                        if again == "n": 
                            print("Thanks for playing!")
                    else:
                        again = input("y or n ... are you stupid? Try again. ")
                print("Your Board")
                if(cpu_turn(your_board) == True):
                    loser = input("The opponent hit all of your ships!")
                    x = 1
                else:
                    print("The opponent missed!")
                    continue
                while x == 1:
                    again = input("Would you like to play again? y/n? ")
                    if again == "y":
                        play()
                    if again == "n": 
                        print("Thanks for playing!")
                    else:
                        again = input("y or n ... are you stupid? Try again. ")
                break

#board = MakeBoard(size)
#PrintBoard(board)
#coords = create(board)
#OtherBoard = MakeReferenceBoard(board, coords)
#PrintBoard(OtherBoard)
play()