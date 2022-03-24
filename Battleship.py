
from random import randint


rows, cols = (8,8)  #declared the grid bounds   
shipNumbers = 4     #number of ships to be placed  
sunkenShips = 0     #Number of ships which sank
shipBody = 0        #For every ship to find entire ships body



board = [['0' for i in range(cols)] for j in range(rows) ] #For players to view
internal_board = [['0' for i in range(cols)] for j in range(rows) ] # For storing the changes made 

# For Printing the board values
def print_board(board):
    row_number = 0   
    print('   0 1 2 3 4 5 6 7')
    print('   ---------------')
    for i in board:
        print(row_number, end = "| ")
        for j in i:
            print(j,end = " ")
        row_number += 1
        print()

#To print the Display board
#print_board(board)

#To get the random row Co-ordinate
def random_row():
    return randint(0, rows - 1)

#To get the random column Co-ordinate
def random_col():
    return randint(0, cols - 1)

#Checks whether the rows are in bound and have no * already placed
def InRange(internal_board,ships_row,ships_col,orientation):
    if orientation == 1:
        ship_rowTest = ships_row + 3
        if ship_rowTest in range (0,8):
            while(ships_row <= ship_rowTest):
                if internal_board[ships_row][ships_col] != '*':
                    ships_row += 1
                else:
                    return False
            return True
        else:
            return False
    else:
        ship_colTest = ships_col + 3
        if ship_colTest in range(0,8):
            while(ships_col <= ship_colTest):
                if internal_board[ships_row][ships_col] != '*':
                    ships_col += 1
                else:
                    return False
            return True 
        else:
            return False  
   
def starAlready(internal_board, ship_row, ship_col):
    if internal_board[ship_row][ship_col] == '*':
        return True
    return False


#For placing the Ships
def place_ships(internal_board):
    shipsPlaced = 0     #used in place ship function to keep track of ships placed
    while(shipsPlaced < shipNumbers):
        ship_row = random_row()
        ship_col =  random_col()
        #if starAlready(internal_board, ship_row, ship_col) == True:
        while(starAlready(internal_board, ship_row, ship_col) == True):
            ship_row = random_row()
            ship_col = random_col()

        orientation = randint(0,1)  # 0 for horizontal  1 for vertical

        if InRange(internal_board,ship_row,ship_col, orientation) :
            track = 0
            #Expanding Ships towards Right
            while(track < 4 ): 
               
                internal_board[ship_row][ship_col] = '*'
                if orientation == 0: 
                    ship_col += 1
                else:
                    ship_row += 1
                track += 1
            
            shipsPlaced += 1 

def isStar(internal_board,x,y):
    if internal_board[x][y] == '*':
        return True
    return False           

def setShipOnScreen(board,x,y):
    board[x][y] = 'S'   #S For Found ship
    print_board(board)  
    print()
    return board   


place_ships(internal_board)
print_board(internal_board)

while(sunkenShips <= 4):
    
    #get input from User
    print_board(board)
    print("Enter co-ordintes between 0 to 7")
    x = int(input("Enter row co-ordinate: "))
    y = int(input("Enter col co-ordinate: "))

    #check whether the co ordinates are not out of bound
    if x not in range(0,8):
        while(x not in range(0,8)):
            print("Please enter valid x co-ordinate.")
            x = int(input("Enter row co-ordinate: "))
    
    if y not in range(0,8):
        while(y not in range(0,8)):
            print("Please enter valid y co-ordinate.")
            y = int(input("Enter col co-ordinate: "))

    if isStar(internal_board,x,y):
        board = setShipOnScreen(board,x,y)
        print("Find Adjacent Cells Containing Ships Body")
        print()
        while(shipBody < 3):
            x = int(input("Enter row co-ordinate: "))
            y = int(input("Enter col co-ordinate: "))
            print()

            if x not in range(0,8):
                while(x not in range(0,8)):
                    print("Please enter valid x co-ordinate.")
                    x = int(input("Enter row co-ordinate: "))
                    print()
    
            if y not in range(0,8):
                while(y not in range(0,8)):
                    print("Please enter valid y co-ordinate.")
                    y = int(input("Enter col co-ordinate: "))
                    print()

            if isStar(internal_board,x,y):
                print("Found a part of Ship's Body")
                print()
                board = setShipOnScreen(board,x,y)
                print()
                shipBody += 1
            else:
                print_board(board)
                print("Think More. Try Again")
                print("Ship Can only expand vertically or horizontally.")
                print()

        print("The Whole Ship Sank.")
        print("Go For the next one")
        print()
        sunkenShips += 1
    
    else:
        print("No Ship Found. Please try again.")
        print()

print("Congratulations !! You Have Sank All The ships.")
        



