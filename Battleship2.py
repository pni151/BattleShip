from random import randint

rows, cols = (8,8)  #declared the grid bounds   

class Cell:
        x = None
        y = None
        isHit = 0
  
class Ship:
        cellArray = []
        isSunk = 0

#It validates whether the cell exists already or not                    
def check_collision(allShip,ship_row,ship_col):
        for ship in allShip:
                if(len(ship.cellArray) != 0):
                        for cell in ship.cellArray:
                                if (cell.x == ship_row and cell.y == ship_col): #If such cell is not present True is returned
                                        return False
                                else:
                                        return True #If cell exists False returned
                else:
                        return True

#It validates whether a ship is possible with the passed co ordinates or not                        
def validateShip(allShip,ship_row,ship_col,orientation):
        if (check_collision(allShip,ship_row,ship_col)):  # when the cell doesnot exist already
                #check whether the cell bounds are in orientation
                if orientation == 0: 
                        ship_colTest = ship_col + 3
                        if ship_colTest < 8:
                                while(ship_col <= ship_colTest):
                                        if check_collision(allShip,ship_row,ship_col):
                                                ship_col += 1
                                        else:
                                                print("Outofrange at 40")
                                                return True
                                return False
                        else:  #If the col test is not in range directly False is returned
                                print("Collision at 43")
                                return True 
                else:
                        ship_rowTest = ship_row + 3
                        if ship_rowTest < 8:
                                while(ship_row <= ship_rowTest):
                                        if check_collision(allShip,ship_row,ship_col):
                                                ship_row += 1
                                        else:
                                                print("Outofrange at 53")
                                                return True
                                return False
                        else:  #If the row test is not in range directly False is returned
                                print("collission at 55")
                                return True
        else:
                print("collision at 60")
                return True
                             
# It creates the ships and returns the array of ship objects
def createShips():  
        allShips = []
        ship_objs = [Ship() for i in  range(4)]
        print("len of ship_objs",len(ship_objs))
        
        for ship in ship_objs:
                cell_objs = [Cell() for i in range(4)]
                #print("len of cell_objs",len(cell_objs))
                for cell in  cell_objs:
                        ship.cellArray.append(cell)
                        print("len of cell_objs",ship, len(ship.cellArray))
                        del cell
                allShips.append(ship)
                del ship
        for i in range(4):
               print(len(allShips[i].cellArray))

        for ship in allShips:
                ship_row = randint(0, rows-1)
                ship_col = randint(0, cols-1)
                orientation = randint(0, 1)
                while( validateShip(allShips,ship_row,ship_col,orientation)):
                        ship_row = randint(0,rows-1)
                        ship_col = randint(0,cols-1)
                        orientation = randint(0, 1)
                        print("out from validate", ship_col, ship_row)
                ship.cellArray[0].x = ship_row
                ship.cellArray[0].y = ship_col
                print("new accepted", ship_col, ship_row)
                for i in range(1,4):
                        if orientation == 0:
                                ship_col += 1
                        else:
                                ship_row += 1
                        print("incremented", ship_col, ship_row)
                        ship.cellArray[i].x = ship_row
                        ship.cellArray[i].y = ship_col

                #print("appending ship")
                #allShips.append(ship)  # appends the ship object to the ship array

        return allShips  

array_Of_Ships_Objects = createShips()  #places ships

print(len(array_Of_Ships_Objects))
#Prints the co ordinates of the ships
for ship in array_Of_Ships_Objects: 
        print("cellarray length",len(ship.cellArray))
        for cell in ship.cellArray:  
                print(cell.x , cell.y)


#internal_board = [['0' for i in range(cols)] for j in range(rows) ] # creates an internal board to store ships

# #Assigns the stars to the board 
# def assignBoard(array_Of_Ships_Objects,internal_board):
#         for ship in array_Of_Ships_Objects:
#                 for cell in ship.cellArray:
#                         internal_board[cell.x][cell.y] = "*"

# # For Printing the board values
# def print_board(board):
#     row_number = 0   
#     print('   0 1 2 3 4 5 6 7')
#     print('   ---------------')
#     for i in board:
#         print(row_number, end = "| ")
#         for j in i:
#             print(j,end = " ")
#         row_number += 1
#         print()

# assignBoard(array_Of_Ships_Objects,internal_board)
# print_board(internal_board)

                    

          
