import random

class Miner():
    def __init__(self , position):
        self.position = position

class Maze():
    def __init__(self , NoOfRows , NoOfColumns ,StartCoords , FinishCoords ):
        
        self.maze = []

        self.DugCells = []

        self.MazeHeight = NoOfRows + 2   # this is the number of cells including the borders
        self.MazeWidth = NoOfColumns + 2  # this also includes the borders


        for row in range(self.MazeHeight):
            tempRow = []
            for col in range(self.MazeWidth): 
                tempRow.append('#') 
            self.maze.append(tempRow)


        for row in self.maze:                     ##########
            print(row)

        self.startCoords = [StartCoords[0] + 1 , StartCoords[1] + 1]
        self.finishCoords = [FinishCoords[0] + 1 , FinishCoords[1] + 1]
        
        print(self.startCoords , self.finishCoords)  ###########

        self.maze[int(self.startCoords[1])][int(self.startCoords[0])] = 'A'
        self.maze[int(self.finishCoords[1])][int(self.finishCoords[0])] = 'B'

        for row in self.maze:                     ##############
            print(row)


        self.isBorder = []
        
        for r, row in enumerate(self.maze):
            tempRoww = []
            for c , col in enumerate(row):
                
                if r == 0 or r == self.MazeHeight - 1 or c == 0 or c == self.MazeWidth - 1:
                    tempRoww.append(True)
                else:
                    tempRoww.append(False)
            self.isBorder.append(tempRoww)
    
        for row in self.isBorder:
            print(row)
    
    def getRandom(self):
        mylist = ["left","right", "down", "up"]
        lis = [1,2,3,4]
        k = random.choices(lis , weights = [7,4,4,4] , k = 1)
        k = k[0]

        choices = random.choices(mylist ,k = k)
        choicesSet = set(choices)
        return list(choicesSet)


    def findingNeighbours(self , miner):

        row , col = miner.position

        possibleNeighbours = {
            'up' : (row - 1 , col),
            'down' : (row + 1 , col),
            'left' : (row , col - 1),
            'right' : (row , col + 1)
        }

        randomSelectedNeighbour = []
        for c in self.getRandom():
            randomSelectedNeighbour.append(possibleNeighbours[c])\
            
        selectedNeighbours = []

        # have to implement the selection , dugcells has been created , checkAdjecent fn needed
        # if 











a = Maze(5,5,[0,0],[4,4])