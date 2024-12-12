import random as rnd
rows = int(input('Enter the Number of rows: '))
cols = int(input('Enter the Number of Columns: '))


maze = []

for row in range(rows):
    tempRow = []
    for col in range(cols):
        tempRow.append('#')
    maze.append(tempRow)

print(maze)

startX = input('Enter the start coordinates x : ')
startY = input('Enter the start coordinates y : ')
finishX = input('Enter the finish coordinates x : ')
finishY = input('Enter the finish coordinates y : ')

maze[int(startY) - 1][int(startX) - 1] = 'A'
maze[int(finishY) - 1][int(finishX) - 1] = 'B'

 
def printMaze(maze):
    for row in maze:
        print(row)

printMaze(maze)