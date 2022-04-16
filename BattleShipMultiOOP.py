
from random import randint
# Basic Introduction to the game
print()
print(" Welcome to the BattleShip Game !!")
print(" Rules are ")
print(" 1. There are only 4 ships containing 4 cells each. \n 2. The ships only expand horizontally or vertically. \n 3. No ship has any cell in common.")
print()

rows, cols = (8,8)  #declared the grid bounds   

class Cell:
        x = None
        y = None
        isHit = 0
  
class Ship:
        cellArray = []
        isSunk = 0

class User:
        array_of_ship_object = []
        flagmiss = 0
        shipSunk = 0  
        count = 0
        internal_board = [['0' for i in range(cols)] for j in range(rows) ]
        #board = [['0' for i in range(cols)] for j in range(rows) ]

#It validates whether the cell exists already or not                    
def check_collision(allShips,ship_row,ship_col):
        for ship in allShips:
                if(len(ship.cellArray) != 0):
                        for cell in ship.cellArray:
                                if (cell.x == ship_row and cell.y == ship_col): #If such cell is not present True is returned
                                        #print("collision")
                                        return False
                                # else:
                                #         print("no collision", ship_row,ship_col)
                                #         return True #If cell exists False returned
                else:
                        return True
        return True        

#It validates whether a ship is possible with the passed co ordinates or not  
# returns true if validation goes wrong                      
def validateShip(allShip,ship_row,ship_col,orientation):
        #print()
        #print("new ship")
        if (check_collision(allShip,ship_row,ship_col)):  # when the cell doesnot exist in the array
                #check whether the cell bounds are in orientation
                if orientation == 0: 
                        ship_colTest = ship_col + 3
                        if ship_colTest in range (8):
                                ship_col += 1
                                while(ship_col <= ship_colTest):
                                        if check_collision(allShip,ship_row,ship_col):
                                                ship_col += 1
                                        else:
                                                #print("Outofrange at 40")
                                                return True
                                return False
                        else:  #If the col test is not in range directly True is returned
                                #print("Collision at 43")
                                return True 
                else:
                        ship_rowTest = ship_row + 3
                        if ship_rowTest in range (8):
                                ship_row += 1
                                while(ship_row <= ship_rowTest):
                                        if check_collision(allShip,ship_row,ship_col):
                                                ship_row += 1
                                        else:
                                                #print("Outofrange at 53")
                                                return True
                                return False
                        else:  #If the row test is not in range directly True is returned
                                #print("collission at 55")
                                return True
        else:
                #print("collision at 60")
                return True
                             
# It creates the ships and returns the array of ship objects
def createShips():  
        allShips = []
        ship_objs = [Ship() for i in  range(4)] #create 4 ship objects
        #print("len of ship_objs",len(ship_objs))
        
        #for every ship create 4 cells
        for ship in ship_objs:
                cell_objs = [Cell() for i in range(4)]
                #print("len of cell_objs",len(cell_objs))
                arr = []
                for cell in  cell_objs:
                        arr.append(cell)
                ship.cellArray = arr
                allShips.append(ship)

        for ship in allShips:
                ship_row = randint(0, rows-1)
                ship_col = randint(0, cols-1)
                orientation = randint(0, 1)
                while( validateShip(allShips,ship_row,ship_col,orientation) == True):
                        ship_row = randint(0,rows-1)
                        ship_col = randint(0,cols-1)
                        orientation = randint(0, 1)
                        #print("out from validate", ship_row, ship_col , orientation)
                ship.cellArray[0].x = ship_row
                ship.cellArray[0].y = ship_col
                #print("new accepted", ship_row, ship_col, "orientation: " ,orientation)
                for i in range(1,4):
                        if orientation == 0:
                                ship_col += 1
                        else:
                                ship_row += 1
                        #print("incremented", ship_row, ship_col)
                        ship.cellArray[i].x = ship_row
                        ship.cellArray[i].y = ship_col

                #print("appending ship")
                #allShips.append(ship)  # appends the ship object to the ship array

        return allShips  
board1 = [['0' for i in range(cols)] for j in range(rows) ]
board2 = [['0' for i in range(cols)] for j in range(rows) ]


user1 = User()
user2 = User()

user1.array_of_ship_object = createShips()  # For User 1
user2.array_of_ship_object = createShips()  # For User 2

# #Prints the co ordinates of the ships
# for ship in user1.array_of_ship_object: 
#         print("cellarray length",len(ship.cellArray))
#         for cell in ship.cellArray:  
#                 print(cell.x , cell.y)
# print("user2")
# print()
# for ship in user2.array_of_ship_object: 
#         print("cellarray length",len(ship.cellArray))
#         for cell in ship.cellArray:  
#                 print(cell.x , cell.y)                

# #For user1
# internal_board1 = [['0' for i in range(cols)] for j in range(rows) ] # creates an internal board to store ships
# board1 = [['0' for i in range(cols)] for j in range(rows) ] #For players to view

# #For User2
# internal_board2 = [['0' for i in range(cols)] for j in range(rows) ] # creates an internal board to store ships
# board2 = [['0' for i in range(cols)] for j in range(rows) ] #For players to view

#Assigns the stars to the board 
def assignBoard(array_Of_Ships_Objects):
        temp_board = [['0' for i in range(cols)] for j in range(rows) ]
        for ship in array_Of_Ships_Objects:
                for cell in ship.cellArray:
                        temp_board[cell.x][cell.y] = "*"
        return temp_board

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

#Assign and print board for User1
print("For User1")
user1.internal_board = assignBoard(user1.array_of_ship_object)
print_board(user1.internal_board)
print()

#Assign and print board for User2
print("For User2")
user2.internal_board = assignBoard(user2.array_of_ship_object)
print_board(user2.internal_board)
print()

#Checks whwther all cells of that ship are visited
def allCellOpened(ship):
        cellopen = 0
        for cell in ship.cellArray:
                if cell.isHit == 1:
                        cellopen += 1
        
        if cellopen == 4:
                return True
        else:
                return False

#Checks whwther all ships have sunk
def allShipSunk(allShips):
        shipSunk = 0
        for ship in allShips:
                if ship.isSunk == 1:
                        shipSunk += 1
        
        if shipSunk == 4:
                return True
        else:
                return False

#Check whether a ship has sunk or not
def shipSank(ship):
        if ship.isSunk == 1:
                return True # ship has sunk
        else:
                return False
#To set ships in the board for users to see
def setShipOnScreen(board,x,y):
        temp_board = [['0' for i in range(cols)] for j in range(rows) ]
        temp_board = board
        temp_board[x][y] = '*'   #S For Found ship
        #print_board(board)  
        print()
        return temp_board 

# print_board(user1.board)
# print_board(user2.board)

# shipSunk1 = 0     #To keep track of ship sunk for user1
# shipSunk2 = 0     #To keep track of ship sunk for user2 
# count1 = 0        #It keeps count of number of times the loop was executed for user1
# count2 = 0        #It keeps count of number of times the loop was executed for user2
user = User()
toggle = 1 # always start with User1
while(user1.shipSunk != 4 or user2.shipSunk != 4):
        #flagmiss = 0  # To denote cell exists but already opened
        #User1 plays first and identifies ships in internalboard2 (ie of User2)
        #the loop continues till user gets all new hits ie no already opened cell and complete miss
        if toggle == 1:
               user = user1
        else:
               user = user2

        if user == user1:
                internalboard = user2.internal_board
                array_of_ship_objects = user2.array_of_ship_object
                board = board1
        else:
                internalboard = user1.internal_board
                array_of_ship_objects = user1.array_of_ship_object
                board = board2

        user.flagmiss = 0
       
        while (user.flagmiss != 1  ):
                #flagmiss = 0
                #print("in loop1")
                # flag is used to terminate loop when the cell is already opened
                flag1 = 0 # To denote cell exists but already opened
                flag2 = 0 # To denote cell exists but not already opened
                flag3 = 0 # To denote cell exists but in an sunken ship

                # if flag1 == 1:
                #         print ("Try Again After User2.")
                #         break
               
                print_board(internalboard)
                print_board(board)
                print()
                try:
                        x = int(input("Enter row co-ordinate: "))
                        y = int(input("Enter col co-ordinate: "))
                except ValueError:
                        print("To play the game, Please Enter number between 0 and 7.")
                        continue
                user.count += 1  # To keep track of number of times input was taken for User1

                #check whether the co ordinates are not out of bound
                if x not in range(0,8):
                        while(x not in range(0,8)):
                                print("Please enter valid x co-ordinate.")
                                x = int(input("Enter row co-ordinate: "))
                
                if y not in range(0,8):
                        while(y not in range(0,8)):
                                print("Please enter valid y co-ordinate.")
                                y = int(input("Enter col co-ordinate: "))

                #For User1 we will check ships User2 ship array object
                for ship in array_of_ship_objects:
                        # cell exits then no need to go further
                        if flag1 == 1 or flag2 == 1:
                                break
                
                        #If ship is already sunken go to next ship
                        if shipSank(ship):
                                flag3 = 0
                                for cell in ship.cellArray:
                                        if cell.x == x and cell.y == y:
                                                print ("Cell already opened in a sunk ship..")
                                                flag3 = 1
                                                break
                                if flag3 == 1:
                                        break
                        else:
                                for cell in ship.cellArray:
                                        if cell.x == x and cell.y == y :
                                                if cell.isHit == 0: 
                                                        cell.isHit = 1
                                                        flag2 = 1
                                                        print("Hit!")
                                                        board = setShipOnScreen(board,x, y)
                                                        #Sunk the ship if all cells are opened
                                                        if allCellOpened(ship) :
                                                                ship.isSunk = 1
                                                                print("You sank a ship")
                                                                print()
                                                                user.shipSunk += 1 # increment the shipsunk variable which is used for the base case of while loop 
                                                        break # To terminate loop at 255
                                                else:   
                                                        flag1 = 1  # to terminate the while loop 
                                                        #flag = 1
                                                        print("Cell Already Opened!!")
                
                                                        break  # exit the loop at the line 255
                # if toggle == 1:
                #         toggle = 0
                # else:
                #         toggle = 1

                if flag1 == 1:
                        print("You Just Lost a Chance!!")
                        print ("Try Again After Other User.")
                        print()
                        break               
                        # No such cell exists then
                if flag1 != 1 and flag2 != 1 and flag3 != 1:
                        user.flagmiss = 1
                        print("Miss!")
                        print("Try Again after Other User...")
                        print()
                        break #when miss occurs immedietly the while loop at 202 terminates
                
                if allShipSunk(user.array_of_ship_object):
                        print("You win! All Ships Have sunk")
                        print("Game Over")
                        print("Chances taken: ", user.count)
                if toggle == 1:
                        toggle = 0
                else:
                        toggle = 1
# #flagmiss = 0

#         #User2 plays first and identifies ships in internalboard1 (ie of User1)
#         #the loop continues till user gets all new hits ie no already opened cell and complete miss
#         print("2nd loop")
#         flagmiss2 = 0  # To denote cell exists but already opened
#         while (flagmiss2 != 1):
#                 #flagmiss2 = 0
#                 print("in loop2")
#                 # flag is used to terminate loop when the cell is already opened
#                 flag1 = 0  # To denote cell exists but already opened
#                 flag2 = 0 # To denote cell exists but not already opened
#                 flag3 = 0 # To denote cell exists but in an sunken ship
               
#                 print_board(internal_board1)
#                 print_board(board2)
#                 print()
#                 try:
#                         x = int(input("Enter row co-ordinate: "))
#                         y = int(input("Enter col co-ordinate: "))
#                 except ValueError:
#                         print("To play the game, Please Enter number between 0 and 7.")
#                         continue
#                 count1 += 1  # To keep track of number of times input was taken for User1

#                 #check whether the co ordinates are not out of bound
#                 if x not in range(0,8):
#                         while(x not in range(0,8)):
#                                 print("Please enter valid x co-ordinate.")
#                                 x = int(input("Enter row co-ordinate: "))
                
#                 if y not in range(0,8):
#                         while(y not in range(0,8)):
#                                 print("Please enter valid y co-ordinate.")
#                                 y = int(input("Enter col co-ordinate: "))

#                 #For User1 we will check ships User2 ship array object
#                 for ship in array_Of_Ships_Objects1:
#                         # cell exits then no need to go further
#                         if flag1 == 1 or flag2 == 1:
#                                 break
                
#                         #If ship is already sunken go to next ship
#                         if shipSank(ship):
#                                 flag3 = 0
#                                 for cell in ship.cellArray:
#                                         if cell.x == x and cell.y == y:
#                                                 print ("Cell already opened in a sunk ship..")
#                                                 flag3 = 1
#                                                 break
#                                 if flag3 == 1:
#                                         break
#                                 else:
#                                         continue
#                         else:
#                                 for cell in ship.cellArray:
#                                         if cell.x == x and cell.y == y :
#                                                 if cell.isHit == 0: 
#                                                         cell.isHit = 1
#                                                         flag2 = 1
#                                                         print("Hit!")
#                                                         board2 = setShipOnScreen(board2,x, y)
#                                                         #Sunk the ship if all cells are opened
#                                                         if allCellOpened(ship) :
#                                                                 ship.isSunk = 1
#                                                                 print("You sank a ship")
#                                                                 print()
#                                                                 shipSunk2 += 1 # increment the shipsunk variable which is used for the base case of while loop 
#                                                         break # To terminate loop at 207
#                                                 else:   
#                                                         flag1 = 1  # to terminate the while loop 
#                                                         #flag = 1
#                                                         print("Cell Already Opened!!")
#                                                         break  # exit the loop at the line 247
#                 if flag1 == 1:
#                         print ("Try Again After User1.")
#                         break               
#                 # No such cell exists then
#                 if flag1 != 1 and flag2 != 1 and flag3 != 1:
#                         flagmiss2 = 1
#                         print("Miss!")
#                         print("Try Again after User1...")
#                         break #when miss occurs immedietly the while loop at 202 terminates
                
#                 if allShipSunk(array_Of_Ships_Objects1):
#                         print("You win! All Ships Have sunk")
#                         print("Game Over")
#                         print("Chances taken: ", count2)        
#         #flagmiss2 = 0