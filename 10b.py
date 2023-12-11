from collections import Counter

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

def beams(lines,seen):
    lines = [list(line) for line in lines]
    for x, y, dir in seen:
        if lines[y][x] == 'F' and dir == 1:
            orths = [(dir-1)%4, (dir-2)%4]
        elif lines[y][x] == 'J' and dir == 3:
            orths = [(dir-1)%4, (dir-2)%4]
        elif lines[y][x] == '7' and dir == 2:
            orths = [(dir-1)%4, (dir-2)%4]
        elif lines[y][x] == 'L' and dir == 0:
            orths = [(dir-1)%4, (dir-2)%4]
        else:
            orths = [(dir-1)%4]
        for orth in orths:
            if orth == 0:
                match = [yt for xt, yt, _ in seen if xt == x and yt < y]
                for i in range(y+1,max(match),1):
                    if lines[i][x] == 'I':
                        break
                    lines[i][x] = 'I'
            elif orth == 1:
                match = [xt for xt, yt, _ in seen if xt > x and yt == y]
                for i in range(x+1, min(match), 1):
                    if lines[y][i] == 'I':
                        break
                    lines[y][i] = 'I'
            elif orth == 2:
                match = [yt for xt, yt, _ in seen if xt == x and yt > y]
                for i in range(min(match)+1, y, 1):
                    if lines[i][x] == 'I':
                        break
                    lines[i][x] = 'I'
            elif orth == 3:
                match = [xt for xt, yt, _ in seen if xt < x and yt == y]
                for i in range(max(match)+1, x, 1):
                    if lines[y][i] == 'I':
                        break
                    lines[y][i] = 'I'
    for idx, line in enumerate(lines):
        line = ''.join(line)+'\n'
        lines[idx] = line
    return ''.join(lines)
        

global sx,sy
sx, sy = find_s(lines)
x, y = sx, sy
dir = 0
count = 0
seen = []
while True:
    count += 1
    x, y, dir = walk(lines, x, y, dir)
    seen.append((x,y,dir))
    if x == sx and y == sy:
        break
lines = beams(lines, seen)
icount = Counter(lines)['I']
print(icount)