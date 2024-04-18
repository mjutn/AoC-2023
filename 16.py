# idea is this:
# save path taken so far, coords plus direction
# create branches for splitting lines
# if square is energized in the direction that you are going; kill branch
# otherwise you have cases:
# . -> newcoords = oldcoords + direction;
# /,\ -> newcoords = oldcoords + lut denk ik;
# -,| -> if pointy then . else create new branch
# if newcoords outside of area: kill branch
# branches kan gewoon een stack zijn; gooi nieuwe branch bovenop
# naam branch = coords?
# kan ook gewoon elke movement een nieuw iets op de stack laten zijn; elke movement in een queue gooien, queue afwerken
# moet ondertussen alleen dus wel een dict bijhouden met welke coords gezien zijn.


# new idea
# create dict with every coord in it, save dir to coord entry in dict for knowing what tiles are energized and in which direction
# every movement thrown in a queue
# work through queue front to bottom
# new movement not in queue if:
#   new coords outside area
#   new coords already energized tile with path going same direction
# calc new movement, check if outside area, check if in dict, if not throw in dict & queue.

# grid[y][x]
# '0000' up right down left
# 0 up 1 right 2 down 3 left

def createGrid(width, depth):
    grid = []
    for i in range(depth):
        grid.append([])
        for j in range(width):
            grid[i].append([])
    return grid

# check if new coord is in grid: True if it is, False if it isnt
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

grid = createGrid(width, depth)

queue = [(0,0,1)]

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
    stront = ''
    for thing in line:
        if thing != []:
            stront += '#'
            total += 1
        else:
            stront += '.'
    print(stront)
print(total)