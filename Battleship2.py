from random import randint
from tkinter.tix import INTEGER
# Basic Introduction to the game
print(" Welcome to the BattleShip Game !!")
print(" Rules are ")
print(" 1. There are only 4 ships containing 4 cells each. \n 2. The ships only expand horizontally or vertically. \n 3. No ship has any cell in common. \n 4. Only integer values will be accpeted.")

rows, cols = (8,8)  #declared the grid bounds   

class Cell:
        x = None
        y = None
        isHit = 0
  
class Ship:
        cellArray = []
        isSunk = 0

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

array_Of_Ships_Objects = createShips()  #places ships

# print(len(array_Of_Ships_Objects))
# #Prints the co ordinates of the ships
# for ship in array_Of_Ships_Objects: 
#         print("cellarray length",len(ship.cellArray))
#         for cell in ship.cellArray:  
#                 print(cell.x , cell.y)


internal_board = [['0' for i in range(cols)] for j in range(rows) ] # creates an internal board to store ships
board = [['0' for i in range(cols)] for j in range(rows) ] #For players to view

#Assigns the stars to the board 
def assignBoard(array_Of_Ships_Objects,internal_board):
        for ship in array_Of_Ships_Objects:
                for cell in ship.cellArray:
                        internal_board[cell.x][cell.y] = "*"

# For Printing the board values
def print_board(board):
    row_number = 0   
    print()
    print('   0 1 2 3 4 5 6 7')
    print('   ---------------')
    for i in board:
        print(row_number, end = "| ")
        for j in i:
            print(j,end = " ")
        row_number += 1
        print()

assignBoard(array_Of_Ships_Objects,internal_board)
print_board(internal_board)

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
    board[x][y] = '*'   #S For Found ship
    #print_board(board)  
    print()
    return board 

shipSunk = 0     #To keep track of ship sunk 
count = 0        #It keeps count of number of times the loop was executed     
while(shipSunk != 4):
        # flag is used to terminate loop when the cell is already opened
        flag = 0  # To denote cell exists but already opened
        flag2 = 0 # To denote cell exists but not already opened
        flag3 = 0
        print_board(board)
        print()
        print("Enter co-ordintes between 0 to 7")

        try:
                x = int(input("Enter row co-ordinate: "))
                y = int(input("Enter col co-ordinate: "))
        except ValueError:
                print("Please Enter number between 0 and 7 only to playthe game")
                continue

        count += 1  # To keep track of number of times input was taken
        # if isinstance(x,int) == False:
        #         while (isinstance(x,int) == False):
        #                 print("Please Enter number between 0 and 7 only to play")
        #                 x = int(input("Enter row co-ordinate: "))

        #check whether the co ordinates are not out of bound
        if x not in range(0,8):
                while(x not in range(0,8)):
                        print("Please enter valid x co-ordinate.")
                        x = int(input("Enter row co-ordinate: "))
        
        if y not in range(0,8):
                while(y not in range(0,8)):
                        print("Please enter valid y co-ordinate.")
                        y = int(input("Enter col co-ordinate: "))

        for ship in array_Of_Ships_Objects:
                # cell exits then no need to go further
                if flag == 1 or flag2 == 1:
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
                                continue
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
                                                        shipSunk += 1 # increment the shipsunk variable it is used for the base case of while loop 
                                                break # To terminate loop at 240
                                        else:   
                                                flag = 1  # to terminate the loop at 224
                                                print("Cell Already Opened!!")
                                                break  # exit the loop at the line 240
                                # print("Oops, no cell Found!")
                                # print("Try Again...")
        # No such cell exists then
        if flag != 1 and flag2 != 1 and flag3 != 1:
                print("Miss!")
                print("Try Again...")

                        
                                                
        if allShipSunk(array_Of_Ships_Objects):
                print("You win! All Ships Have sunk")
                print("Game Over")
                print("Chances taken: ", count)
