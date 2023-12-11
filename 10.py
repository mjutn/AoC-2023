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
            return (x,y)

def walk(lines, cur, dir):
    new = (cur[0]+dirs[dir][0], cur[1]+dirs[dir][1])
    if new == s:
        return new, dir
    connections = chars[lines[new[1]][new[0]]]
    if connections[0] == (dir-2)%4:
        dir = connections[1]
    else:
        dir = connections[0]
    return new, dir

global s
s = find_s(lines)
cur = s
dir = 0
count = 0
while True:
    count += 1
    cur, dir = walk(lines, cur, dir)
    if cur == s:
        break
print(int(count/2))