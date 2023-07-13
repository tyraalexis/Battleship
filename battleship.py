from random import randrange


def create():
    choose_col = randrange(0,5)
    choose_row = randrange(0,5)
    
    create_ship = choose_col, choose_row
    
    h_v = randrange(0,2)
    if h_v == 0:
        if choose_col == 4:
             print ((choose_col - 2, choose_row),(choose_col - 1, choose_row),(create_ship))
        elif choose_col == 0:
            print ((create_ship),(choose_col + 1, choose_row),(choose_col + 2, choose_row))
        else:
            print ((choose_col + 1, choose_row), (create_ship), (choose_col - 1, choose_row))
    elif h_v == 1:
         if choose_row == 4:
            print ((choose_col, choose_row - 2),(choose_col, choose_row - 1),(create_ship))
         elif choose_row == 0:
            print ((create_ship),(choose_col, choose_row + 1),(choose_col, choose_row + 2))
         else:
            print ((choose_col, choose_row + 1), (create_ship), (choose_col, choose_row - 1))
create()

