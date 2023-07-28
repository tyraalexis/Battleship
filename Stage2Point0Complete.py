from random import randrange
#BATTLESHIIIIIPP!!!!
class battleship:
    def __innit__(self, name, row, col, row2, col2, length):
        self.name = name
        self.row = row
        self.col = col
        self.coord1 = row, col
        self.row2 = row2
        self.col2 = col2
        self.coord2 = row2, col2
        self.hits = 0
        self.length = length
    def hit(battleship):
        battleship.hits += 1
        if (battleship.hits < battleship.length):
            return False
        return True
#Makes a random row and col value
def generate(board):
    row = randrange(0,len(board[0]))
    col = randrange(0,len(board[0]))
    return [row, col]
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
#Makes a second coord.
def expand0(board, choose_row, choose_col):
    returnable = []
    returnable.append([choose_row, choose_col])
    h_v = randrange(0,2)
    if h_v == 0:
        if choose_col == len(board[0])-1:
             returnable.append([choose_col - 1, choose_row])
        elif choose_col == 0:
             returnable.append([choose_col + 1, choose_row])
        else:
             returnable.append([choose_col - 1, choose_row])
    elif h_v == 1:
         if choose_row == len(board[0])-1:
             returnable.append([choose_col, choose_row - 1])
         elif choose_row == 0:
             returnable.append([choose_col, choose_row + 1])
         else:
             returnable.append([choose_col, choose_row - 1])
    return returnable
#IDK.
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
def draw_Y(board, ship1, ship2):
    board[ship1[0][0]-1][ship1[0][1]-1] = "[ I ]"  
    board[ship2[0][0]-1][ship2[0][1]-1] = "[ I ]" 
    board[ship1[1][0]-1][ship1[1][1]-1] = "[ I ]"
    board[ship2[1][0]-1][ship2[1][1]-1] = "[ I ]"
    PrintBoard(board)  
#Used in main method for cpu's turn. Returns True if it hits anything. False if it misses.
def cpu_turn(board):
    coords = generate(board)
    if(board[coords[0]][coords[1]] == "[   ]"):
        draw_O(board, coords[0], coords[1])
        return False
    elif(board[coords[0]][coords[1]] == "[ I ]"):
        draw_X(board, coords[0], coords[1])
        return True
    else:
        cpu_turn(board)
#Used in main method to recieve user input and to place their ships
def twosship():
    while True:
        size = 10
        board = MakeBoard(size)
        your_board = MakeBoard(size)
        PrintBoard(board)
        print("SHIP 1")
        name = input("What would you like to name your ship? ") 
        while True:
            try:
                #Asking user for the row and column for them to place their first ship
                row = (int(input("In what ROW would you like to place your ship? "))) - 1
                col = (int(input("In what COLUMN would you like to place your ship? "))) - 1
                if row not in range(len(board[0])):
                    print("Your point is our of range.")
                    continue
                if col not in range(len(board[0])):
                    print("Your point is our of range.")
                    continue
                
                def expand(your_board, choose_row, choose_col):
                    returnable = []
                    choose_row = row + 1
                    choose_col = col + 1
                    returnable.append([choose_row, choose_col])
                    v_h = randrange(0,2)
                    if v_h == 0:
                        if choose_col == len(your_board[0]):
                            returnable.append([choose_row, choose_col - 1 ])
                        elif choose_col == 0:
                            returnable.append([choose_row, choose_col + 1])
                        else:
                            returnable.append([choose_row, choose_col + 1])
                    elif v_h == 1:
                        if choose_row == len(your_board[0]):
                            returnable.append([choose_row - 1, choose_col])
                        elif choose_row == 0:
                            returnable.append([choose_row + 1, choose_col])
                        else:
                            returnable.append([choose_row + 1, choose_col])
                    return returnable
                
                
                
                #Asking the user for the coords for their second ship
                print ("SHIP 2")
                name2 = input("What would you like to name your ship? ") 
                row2 = int(input("In what ROW would you like to place your ship? ")) - 1
                col2 = (int(input("In what COLUMN would you like to place your ship? "))) - 1
                if row2 not in range(len(board[0])):
                    print("Your point is our of range")
                    continue
                if col2 not in range(len(board[0])):
                    print("Your point is our of range")
                    continue
                
                def expand2(your_board, choose_row, choose_col):
                    returnable = []
                    choose_row = row2 + 1
                    choose_col = col2 + 1
                    returnable.append([choose_row, choose_col])
                    h_v = randrange(0,2)
                    if h_v == 0:
                        if choose_col == len(your_board[0]):
                            returnable.append([choose_row, choose_col - 1 ])
                        elif choose_col == 0:
                            returnable.append([choose_row, choose_col + 1])
                        else:
                            returnable.append([choose_row, choose_col + 1])
                    elif h_v == 1:
                        if choose_row == len(your_board[0]):
                            returnable.append([choose_row - 1, choose_col])
                        elif choose_row == 0:
                            returnable.append([choose_row + 1, choose_col])
                        else:
                            returnable.append([choose_row + 1, choose_col])
                    return returnable
                
                
                #Printing the two coordinates on the user's board
                ship1 = expand(your_board, row, col)
                ship2 = expand2(your_board, row2 , col2)
                print(ship1)
                print(ship2)
                print ("The coordinates of the ships are",ship1, ship2,".")
                #draw_I(your_board, row, col, row2, col2)
                draw_Y(your_board, ship1, ship2)
                print("Here is your board!")
            except ValueError:
                print("Numbers only.")
                continue
            
            return ship1, ship2
#Main game loop.    
def play():
    y = 0
    while True:
        row_list = [] #List of the user's guessed row values
        column_list = [] #List of the user's guessed column values
        size = 10
        board = MakeBoard(size)
        your_board = MakeBoard(size)
        print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. Choose wisely and have fun!")
        twosship()
        cpu_ship1 = create(board)
        cpu_ship2 = create(board)
        PrintBoard(board)
        print(cpu_ship1)
        print(cpu_ship2)
        print("First Missile Launch")
        x = 0
        while True:
            try:
                L1 = int(input("Row: ")) 
                row_list.append(L1 - 1)
                if L1 not in range(len(board[0]) + 1): 
                    print("Your guess is out of range.")
                    continue
                else:
                    L1C = (int(input("Column: ")) - 1)
                    column_list.append(L1C)
                    if L1C not in range(len(board[0])+ 1):
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
                if (cpu_ship1[0][0] or cpu_ship1[0][1] or cpu_ship1[1][0] or cpu_ship1[1][1] == car):
                    print("CPU Board")
                    draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                    print("HIT!")
                    x = 0
                elif (cpu_ship2[0][0] or cpu_ship2[0][1] or cpu_ship2[1][0] or cpu_ship2[1][1] == car):
                    print("CPU Board")
                    draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                    print("HIT!")
                    x = 0
                elif (cpu_ship1[0][0] and cpu_ship1[0][1] and cpu_ship1[1][0] and cpu_ship1[1][1] == row_list, column_list):
                    print("CPU Board")
                    draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                    print("HIT!")
                    x = 0
                elif (cpu_ship2[0][0] and cpu_ship2[0][1] and cpu_ship2[1][0] and cpu_ship2[1][1] == row_list, column_list):
                    print("CPU Board")
                    draw_X(board, row_list[len(row_list) - 1], column_list[len(column_list) - 1])
                    print("HIT!")
                    x = 0
                elif (row_list, column_list) == cpu_ship1 and cpu_ship2:
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
                loser = input("The opponent hit one of your ships!")
                y = y + 1
            else:
                print("The opponent missed!")
                continue
            while y == 4:
                again = input("Would you like to play again? y/n? ")
                if again == "y":
                    play()
                if again == "n": 
                    print("Thanks for playing!")
                else:
                    again = input("y or n ... are you stupid? Try again. ")
    
#board = MakeBoard(3)
#board[1][1] = "[ X ]"
#PrintBoard(board)
#coords = create(board)
#OtherBoard = MakeReferenceBoard(board, coords)
#PrintBoard(OtherBoard)
#print(cpu_turn(board))
play()