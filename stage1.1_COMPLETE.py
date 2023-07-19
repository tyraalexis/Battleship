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
     returnable = choose_row, choose_col
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
def play():
    while True:
        row_list = []
        column_list = []
        print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. Choose wisely and have fun!")
        try:
            size = int(input("How big would you like your grid to be? "))
            board = MakeBoard(size)
            where = input("Would you like to place your ship(1) or allow it to be randomized(2)? 1 or 2? ")
            if where == "1":
                where_r = int(input("In what ROW would you like to place your ship? "))
                where_c = int(input("In what COLUMN would you like to place your ship? "))
                ship = (where_r, where_c)
                print("The coordinates of the ship are",ship,".")
            if where == "2":
                ship = create(board)
            else:
                print("Wrong answer. I guess I'll place it myself.")
        except ValueError:
            print("Numbers only.")
        else: 
            board = MakeBoard(size)
            PrintBoard(board)
            print("First Missile Launch")
            turn = 1
            while turn <= 5 :
                x = 0
                try:
                    L1 = int(input("Row: ")) 
                    row_list.append(L1)
                    if L1 not in range(len(board[0])): 
                        print("Your guess is out of range. You lose a turn!")
                        continue
                    else:
                        L1C = int(input("Column: "))
                        column_list.append(L1C)
                        if L1C not in range(len(board[0])):
                            print("Your guess is out of range. You lose a turn!")
                            continue
                        else: pass
                except ValueError:
                    print("Numbers only please")
                else:       
                    car = row_list[len(row_list)-1], column_list[len(row_list)-1]
                    print("Missile Launch")
                    if (ship == car):
                        draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                        print("HIT!")
                        x = 1
                    else:
                        print("MISS!")
                        draw_O(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                        x = 0
                        turn = turn + 1
                while x == 1:
                    again = input("Would you like to play again? y/n? ")
                    if again == "y":
                        play()
                    if again == "n": 
                        print("Thanks for playing!")
                    else:
                        again = input("y or n ... are you stupid? Try again. ")
            while turn >= 5:
                loser = input("You have run out of turns. Would you like to play again? y/n? ")
                if loser == "y":
                    play()
                    if loser == "n": 
                        print("Thanks for playing!")
                    else:
                        loser = input("y or n ... are you stupid? Try again. ")
                break

#board = MakeBoard(size)
#PrintBoard(board)
#coords = create(board)
#OtherBoard = MakeReferenceBoard(board, coords)
#PrintBoard(OtherBoard)
play()

