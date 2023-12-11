with open('10_input') as file:
    text = file.read()
    s = text.index('S')
    linelength = text.index('\n')+1
leftChars = ['-','F', 'L']
rightChars = ['-', '7', 'J']
upChars = ['|', '7', 'F']
downChars = ['|', 'J', 'L']
cur = s
seen = [cur]
if text[s-1] in leftChars:
    cur = s-1
    seen.append(cur)
elif text[s+1] in rightChars:
    cur = s+1
    seen.append(cur)
elif text[s-linelength] in upChars:
    cur = s-linelength
    seen.append(cur)
elif text[s+linelength] in downChars:
    cur = s+linelength
    seen.append(cur)
prev = s
while cur != s:
    seen.append(cur)
    if text[cur] == '|':
        if prev == cur - linelength:
            prev = cur
            cur = cur + linelength
        else:
            prev = cur
            cur = cur - linelength
    elif text[cur] == '-':
        if prev == cur-1:
            prev = cur
            cur = cur+1
        else:
            prev = cur
            cur = cur-1
    elif text[cur] == '7':
        if prev == cur - 1:
            prev = cur
            cur = cur + linelength
        else:
            prev = cur
            cur = cur - 1
    elif text[cur] == 'J':
        if prev == cur - 1:
            prev = cur
            cur = cur - linelength
        else:
            prev = cur
            cur = cur - 1
    elif text[cur] == 'F':
        if prev == cur + linelength:
            prev = cur
            cur = cur + 1
        else:
            prev = cur
            cur = cur + linelength
    elif text[cur] == 'L':
        if prev == cur - linelength:
            prev = cur
            cur = cur + 1
        else:
            prev = cur
            cur = cur - linelength
print(int(len(seen)/2))