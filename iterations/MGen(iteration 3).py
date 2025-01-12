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
    def __init__(self, NoOfRows , NoOfColumns , StartCoords ,FinalCoords):
        
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
        self.finishCoords = (FinalCoords[0] , FinalCoords[1])

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

        
    def possibleMoves(self , miner): 
        #This function will find the moves that can be taken following the rules
        (ro , co) = miner.position
        totalMoves = ["left" , "right" , "up" , "down"]
        moveCoords = {
            'up' : (ro - 1 , co),
            'down' : (ro + 1 , co),
            'left' : (ro , co - 1),
            'right' : (ro , co + 1)
        }
        PossibleMoves = []

        def checkForSquare(Posi):
            (row , col) = Posi

            adjUp = (row - 1 , col)
            adjRight = (row, col + 1)
            adjLeft = (row, col - 1)
            adjDown = (row + 1 , col )
            adjRigUp = (row - 1 , col + 1)
            adjLefUp = (row - 1 , col - 1)
            adjRigDown = (row + 1 , col + 1)
            adjLefDown = (row + 1 , col - 1)

            if adjUp in self.DugCells and adjRigUp in self.DugCells and adjRight in self.DugCells:
                return False
            if adjUp in self.DugCells and adjLefUp in self.DugCells and adjLeft in self.DugCells:
                return False
            if adjDown in self.DugCells and adjRigDown in self.DugCells and adjRight in self.DugCells:
                return False
            if adjDown in self.DugCells and adjLefDown in self.DugCells and adjLeft in self.DugCells:
                return False
            else:
                return True
                
        def conditions(posi):

            c = [
                    0 < posi[0] <= self.MazeHeight ,#1
                    0 < posi[1] <= self.MazeWidth , #2
                    posi not in self.DugCells ,     #3
                    self.isBorder[posi[0]][posi[1]] == False , #4
                    checkForSquare(posi)
                ]    

            if c[0] and c[1] and c[2] and c[3] and c[4]:
                return True
            else:
                return False


        for move in totalMoves:
            if conditions(moveCoords[move]):
                PossibleMoves.append(moveCoords[move])

        return PossibleMoves

    def randomizeMoves(self , PossibleMoves):

        lis = [1,2,3,4]
        k = random.choices(lis , weights = [6,5,5,4] , k = 1)
        k = k[0]
        k = int(k)
        if PossibleMoves != []:
            choices = random.choices(PossibleMoves ,k = k)
            choicesSet = set(choices)

            return list(choicesSet)     # returning final move set chosen          

        else:
            return list()


    def generator(self):

        frontier = Stackfrontier()

        startMiner = Miner(self.startCoords)

        frontier.add(startMiner)
        self.DugCells.add(startMiner.position)

        while True:

            if frontier.isEmpty():
               pass

            CurrentCell = frontier.remove()
            print(CurrentCell.position)

            for ToDigPos in self.randomizeMoves(self.possibleMoves(CurrentCell)):
                if not frontier.checkForCell(Miner(position=ToDigPos)):
                    frontier.add(Miner(position=ToDigPos))
                    self.maze[ToDigPos[0]][ToDigPos[1]] = ' '
                    self.DugCells.add(ToDigPos)



                    for row in self.maze:
                        for ele in row:
                            print(ele , end='')
                        print()





a = Maze(8,8,[1,1],[7,7])    # [5,5] --> 0 to 5 row and columns
b = Miner((1,1))
d = a.maze


#for k in c:
#    d[k[0]][k[1]] = ' '

for row in d:

    print (row)

a.generator()