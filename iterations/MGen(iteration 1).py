#Just Doesnt Work

import random

class Miner():
    def __init__(self , position):
        self.position = position

class Frontier():

    def __init__(self):
        self.frontier = []

    def add(self , Cell):
        self.frontier.append(Cell)
    
    def checkForCell(self , Cell):
        return any(cell.position == Cell.position for cell in self.frontier)
    
    def isEmpty(self):
        if len(self.frontier) == 0:
            return True
        else:
            return False
    
class Stackfrontier(Frontier):

    def remove(self):
        if self.isEmpty():
            raise Exception('Empty Frontier')
        else:
            selectedCell = self.frontier[-1]
            self.frontier = self.frontier[:-1]   
            return selectedCell

class Queuefrontier(Frontier):

    def remove(self):
        if self.isEmpty():
            raise Exception('Empty Frontier')
        else:
            selectedCell = self.frontier[0]
            self.frontier = self.frontier[1:]   
            return selectedCell

class Maze():
    def __init__(self , NoOfRows , NoOfColumns ,StartCoords , FinishCoords ):
        
        self.maze = []


        self.MazeHeight = NoOfRows + 2   # this is the number of cells including the borders
        self.MazeWidth = NoOfColumns + 2  # this also includes the borders


        for row in range(self.MazeHeight):
            tempRow = []
            for col in range(self.MazeWidth): 
                tempRow.append('#') 
            self.maze.append(tempRow)


        for row in self.maze:                     ##########
            print(row)

        self.DugCells = []

        self.startCoords = (StartCoords[0] + 1 , StartCoords[1] + 1)
        self.finishCoords = (FinishCoords[0] + 1 , FinishCoords[1] + 1)
        
        self.DugCells.append(self.finishCoords)
        self.DugCells.append(self.startCoords)
        


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
        k = int(k)

        choices = random.choices(mylist ,k = k)
        choicesSet = set(choices)
        return list(choicesSet)

    def checkAdjecent(self , miner):

        (row , col) = miner.position

        adjUp = (row - 1 , col)
        adjRight = (row, col + 1)
        adjLeft = (row, col - 1)
        adjDown = (row + 1 , col)

        adjCells = []

        if self.isBorder[adjUp[0]][adjUp[1]] != True and adjUp not in self.DugCells:
            adjCells.append(adjUp)
        if self.isBorder[adjDown[0]][adjDown[1]] != True and adjDown not in self.DugCells:
            adjCells.append(adjDown)
        if self.isBorder[adjLeft[0]][adjLeft[1]] != True and adjLeft not in self.DugCells:
            adjCells.append(adjLeft)
        if self.isBorder[adjRight[0]][adjRight[1]] != True and adjRight not in self.DugCells:
            adjCells.append(adjRight)

        return adjCells
    
    def checkSquare(self,pos):         # have to fix this
        
        (row , col) = pos

        adjUp = (row - 1 , col)
        adjRight = (row, col + 1)
        adjLeft = (row, col - 1)
        adjDown = (row + 1 , col )
        adjRigUp = (row - 1 , col + 1)
        adjLefUp = (row - 1 , col - 1)
        adjRigDown = (row + 1 , col + 1)
        adjLefDown = (row + 1 , col - 1)

        #print(adjDown,adjLefDown,adjLeft,adjLefUp,adjRigDown,adjRight,adjRigUp,adjUp)

        canDoDR,canDoDL,canDoUL,canDoUR = True,True,True,True

        if adjUp in self.DugCells and adjRigUp in self.DugCells and adjRight in self.DugCells:
            canDoUR = False
        if adjUp in self.DugCells and adjLefUp in self.DugCells and adjLeft in self.DugCells:
            canDoUL = False
        if adjDown in self.DugCells and adjRigDown in self.DugCells and adjRight in self.DugCells:
            canDoDR = False
        if adjDown in self.DugCells and adjLefDown in self.DugCells and adjLeft in self.DugCells:
            canDoDL = False
        
        if [canDoUR,canDoDR,canDoUL,canDoDL] == [False , False , False , False]:
            return False
        
        else:
            return True

    def conditionNeighbours(self,ranPos,pos):
        c = [
                0 < ranPos[0] < self.MazeHeight ,#1
                0 < ranPos[1] < self.MazeWidth , #2
                ranPos not in self.DugCells ,    #3
                self.checkSquare(pos) == True    #4

            ]
        
        

        if (c[0] and c[1]):
            if (self.isBorder[ranPos[0] - 1][ranPos[1] - 1] == False and c[2] and c[3]):
                print('all conditions met')
                return True
            else:
                print('rejected 2 , 3')
                return False
        

        else:
            print('Rejected 0 , 1')
            return False
        
    def findingNeighbours(self , miner):
        (row , col) = miner.position
        pos = (row + 1 ,col + 1 )

        print('current cell pos:' , pos)


        row = row + 1
        col = col + 1

        posNbr = {
            'up' : (row - 1 , col),
            'down' : (row + 1 , col),
            'left' : (row , col - 1),
            'right' : (row , col + 1)
        }

        randomSelectedNeighbour = []
        for c in self.getRandom():
            randomSelectedNeighbour.append(posNbr[c])
            

        selectedNeighbours = []
        for ranPos in randomSelectedNeighbour:
            print('RandomNeighbours list:' , randomSelectedNeighbour)
            print('random selected:',ranPos)
            if self.conditionNeighbours(ranPos,pos):
                
                selectedNeighbours.append(ranPos)
                print('selected: ',selectedNeighbours)
        return selectedNeighbours
    

    def generator(self):

        frontier = Queuefrontier()

        startMiner = Miner(self.startCoords)

        frontier.add(startMiner)

        self.exploredSet = set()

        while True:

            if frontier.isEmpty():
                print('Solved')
                for row in self.maze:
                    print(row)

            CurrentCell = frontier.remove()

            self.exploredSet.add(CurrentCell.position)
            self.DugCells.append(CurrentCell.position)
            print('dug:' ,self.exploredSet)


            for location in self.findingNeighbours(CurrentCell):
                if location not in self.exploredSet and not frontier.checkForCell(CurrentCell):
                    frontier.add(Miner(position = location ))
                    self.maze[location[0]][location[1]] = ' '
                    for row in self.maze:
                        print(row)
                




        
        










a = Maze(5,5,[1,1],[4,4])
b = Miner((1,1))
c = a.findingNeighbours(b)
d = a.maze
print(d)
print(c)

for k in c:
    d[k[0]][k[1]] = ' '

for row in d:

    print (row)

a.generator()