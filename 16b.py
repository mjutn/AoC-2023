def createGrid(width, depth):
    grid = []
    for i in range(depth):
        grid.append([])
        for j in range(width):
            grid[i].append([])
    return grid

def checkGrid(x, y, dir):
    if x >= width:
        return False
    if x < 0:
        return False
    if y < 0:
        return False
    if y >= depth:
        return False
    return True

def checkEnergise(x, y, dir):
    if dir in grid[y][x]:
        return True
    else:
        grid[y][x].append(dir)
        return False

def queueAdd(x, y, dir):
    if dir == 0:
        queue.append((x, y-1, dir))
    elif dir == 1:
        queue.append((x+1, y, dir))
    elif dir == 2:
        queue.append((x, y+1, dir))
    elif dir == 3:
        queue.append((x-1, y, dir))

with open('16_input') as file:
    input = file.read().split('\n')

width = len(input[0])
depth = len(input)

horizontal = [i for i in range(width)]+[width-1]*(depth-2)+[0]*(depth-2)+[i for i in range(width)]
vertical = [0]*(width-1)+[i for i in range(1,depth)]+[i for i in range(1,depth)]+[depth-1]*(width-1)
dir = [2]*(width-1)+[3]*(depth-2)+[1]*(depth-2)+[0]*(width-1)
edges = tuple(zip(horizontal,vertical,dir))

results = []

for start in edges:
    grid = createGrid(width, depth)

    queue = [start]

    slashLUT = [1, 0, 3, 2]
    backLUT = [3, 2, 1, 0]

    while queue != []:
        x, y, dir = queue.pop()

        if checkGrid(x, y, dir) is False:
            continue
        if checkEnergise(x,y,dir) is True:
            continue

        currentchar = input[y][x]

        if currentchar == '.':
            queueAdd(x, y, dir)
        elif currentchar == '/':
            queueAdd(x, y, slashLUT[dir])
        elif currentchar == '\\':
            queueAdd(x, y, backLUT[dir])
        elif currentchar == '-' and dir%2 == 1:
            queueAdd(x, y, dir)
        elif currentchar == '-' and dir%2 == 0:
            queueAdd(x, y, 1)
            queueAdd(x, y, 3)
        elif currentchar == '|' and dir%2 == 0:
            queueAdd(x, y, dir)
        elif currentchar == '|' and dir%2 == 1:
            queueAdd(x, y, 0)
            queueAdd(x, y, 2)

    total = 0

    for line in grid:
        for thing in line:
            if thing != []:
                total += 1
    results.append((start,total))

from operator import itemgetter
print(max(results, key=itemgetter(1)))