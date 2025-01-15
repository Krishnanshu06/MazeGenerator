#Doesnt Work
#Dont remember why
#iter 3)) Have to start fresh after Exams


import random

class Miner():
    def __init__(self , position):
        self.position = position

class Frontier():

    def __init__(self):
        self.frontier = []

    def add(self , cell):
        self.frontier.append(cell)

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
    def __init__(self , NoOfRows , NoOfColumns , StartCoords , FinishCoords):

        self.maze = []


        self.MazeHeight = NoOfRows
        self.MazeWidth = NoOfColumns



        for row in range(self.MazeHeight + 1):
            tempRow = []
            for col in range(self.MazeWidth + 1):
                tempRow.append('#')
            self.maze.append(tempRow)


        for row in self.maze:
            print(row)
        
        self.DugCells = set()

        self.startCoords = (StartCoords[0] , StartCoords[1])
        self.finishCoords = (FinishCoords[0] , FinishCoords[1])

        self.DugCells.add(self.finishCoords)
        self.DugCells.add(self.startCoords)



        print(self.startCoords , self.finishCoords)

        self.maze[int(self.startCoords[1])][int(self.startCoords[0])] = 'A'
        self.maze[int(self.finishCoords[1])][int(self.finishCoords[0])] = 'B'

        for row in self.maze:
            print(row)


        self.isBorder = []

        for r , row in enumerate(self.maze):
            tempRoww = []
            for c , col in enumerate(row):

                if r  == 0 or r == self.MazeHeight or c == 0 or c == self.MazeWidth:
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
            return True
        
        else:
            return False
    

    def conditionNeighbours(self,ranPos,pos):
        c = [
                0 < ranPos[0] <= self.MazeHeight ,#1
                0 < ranPos[1] <= self.MazeWidth , #2
                ranPos not in self.DugCells ,     #3
                

            ]

        if (c[0] and c[1]):
            if (self.isBorder[ranPos[0]][ranPos[1]] == False and c[2]):
                print('all conditions met')
                return True
            else:
                print('rejected 2 , 3')
                return False  
        else:
            print('Rejected 0 , 1')  
            return False



    def findingNeighbours(self , miner):
        (ro , co) = miner.position
        pos = (ro , co)

        print('current cell pos:' , pos)

        posNbr = {
            'up' : (ro - 1 , co),
            'down' : (ro + 1 , co),
            'left' : (ro , co - 1),
            'right' : (ro , co + 1)
        }

        randomSelectedNeighbour = []
        for c in self.getRandom():
            randomSelectedNeighbour.append(posNbr[c])
            
        print('RandomNeighbours list:' , randomSelectedNeighbour)

        selectedNeighbours = []
        for ranPos in randomSelectedNeighbour:
            print('random selected:',ranPos)
            if self.conditionNeighbours(ranPos,pos):
                
                selectedNeighbours.append(ranPos)
                print('selected: ',selectedNeighbours)
        return selectedNeighbours
           

    def generator(self):

        frontier = Queuefrontier()

        startMiner = Miner(self.startCoords)

        frontier.add(startMiner)

        while True:

            if frontier.isEmpty():
                print('Solved')
                for row in self.maze:
                    print(row)

            CurrentCell = frontier.remove()
            print(CurrentCell.position)
            if self.checkSquare(CurrentCell.position):
                continue

            self.DugCells.add(CurrentCell.position)

            print('Dug: ',self.DugCells)

            for location in self.findingNeighbours(CurrentCell):
                print(' ')
                if not frontier.checkForCell(CurrentCell):
                    print('loc : ',location)
                    frontier.add(Miner(position= location))
                    self.maze[location[0]][location[1]] = ' '
                    for row in self.maze:
                        print(row)







a = Maze(8,8,[1,1],[7,7])    # [5,5] --> 0 to 5 row and columns
b = Miner((1,1))
c = a.findingNeighbours(b)
d = a.maze

print(c)

#for k in c:
#    d[k[0]][k[1]] = ' '

for row in d:

    print (row)

a.generator()



# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 








