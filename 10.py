with open('10_input') as file:
    lines = file.read().split('\n')

chars = {
    'L':[0,1],
    '|':[0,2],
    'J':[0,3],
    'F':[1,2],
    '-':[1,3],
    '7':[2,3]
}

dirs = [
    (0,-1), # up    ^
    (1,0),  # right >
    (0,1),  # down  v
    (-1,0)  # left  <
]

def find_s(lines):
    for y, line in enumerate(lines):
        x = line.find('S')
        if x != -1:
            return x,y

def walk(lines, x, y, dir):
    newx, newy = x+dirs[dir][0], y+dirs[dir][1]
    if newx == sx and newy == sy:
        return newx, newy, dir
    connections = chars[lines[newy][newx]]
    if connections[0] == (dir-2)%4:
        dir = connections[1]
    else:
        dir = connections[0]
    return newx, newy, dir

global sx, sy
sx,sy = find_s(lines)
x, y = sx, sy
dir = 0
count = 0
while True:
    count += 1
    x, y, dir = walk(lines, x, y, dir)
    if x == sx and y == sy:
        break
print(int(count/2))