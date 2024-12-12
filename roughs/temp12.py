import random

class Miner():
    def __init__(self , position):
        self.position = position

class Maze():
    def __init__(self,rows,cols,start,finish):
        self.maze = []

        for row in range(rows + 2):
            tempRow = []
            for col in range(cols + 3):
                tempRow.append('#')
            self.maze.append(tempRow)

        self.mazeHeight = rows
        self.mazeWidth = cols

        self.startCoords = start
        self.finishCoords = finish

        self.createdWalls = []


        self.maze[int(start[1]) + 1][int(start[1]) + 1] = 'A'
        self.maze[int(finish[0])][int(finish[0] + 1)] = 'B'
        for row in self.maze:
            print(row)                            # temp

        self.isBorder = []

        for r in range(self.mazeHeight + 2):
            tempR = []
            for c in range(self.mazeWidth + 2):

                if r == 0 or r == self.mazeHeight + 1 or c == 0 or c == self.mazeWidth + 1:
                    tempR.append(True)
                else:
                    tempR.append(False)

            self.isBorder.append(tempR)
        for row in self.isBorder:                  # temp
            print(row)

    def findingNeighbours(self , miner):

        row , col = miner.position

        possibleNeighbours = [
            ('up' , (row - 1 , col)),
            ('down' , (row + 1 , col)),
            ('left' , (row , col - 1)),
            ('right' , (row , col + 1))
        ]



    def generate(self):
        print('Generating...')



    def print(self):
        
        for r , row in enumerate(self.isBorder):
            for c , column in enumerate(row):

                if column == True:
                    print('█' , end = '')
                elif column == False and [r-1,c-1] == self.startCoords:
                    print('A' , end = '')
                elif column == False and [r+2,c+2] == self.finishCoords:
                    print('B' , end = '')
                elif column == False and [r,c] in self.createdWalls:
                    print('#' , end = '')
                else:
                    print(' ' , end = '')
            print()
        print()



a = Maze(12,12,[0,0],[12,12]) 
a.print()



