#Main game loop.
def play():
    row_list = []
    column_list = []
    print("Welcome to BATTLESHIP! My battleship is placed randomly on the board. Choose wisely and have fun!")
    size = int(input("How big would you like your grid to be? "))
    board = MakeBoard(size)
    ship = create(board)
    PrintBoard(board)
    print(ship)
    print("First Missile Launch")
    turn = 1
    while turn <= 5 :
        x = 0
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
        while x == 1:
            again = input("Would you like to play again? y/n? ")
            if again == "y":
             play()
            if again == "n": 
                 print("Thanks for playing!")
            else:
                again = input("y or n ... are you stupid? Try again. ")
            turn = turn + 1
    while turn >= 5:
        print("You have run out of turns.")
        break