file = open('1_input')
sum = 0
writtenNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for line in file:
    first = ''
    last = ''
    for i in range(len(line)):
        if first != '' and last != '':
            break
        if line[i].isdigit() and first == '':
            first = line[i]
        for x in range(9):
            if line[i:(i+len(writtenNumbers[x]))] == writtenNumbers[x] and first == '':
                first = digits[x]
        if line[-i].isdigit() and i != 0 and last == '':
            last = line[-i]
        if i == len(line)-1 and last == '':
            last = line[0]
        for x in range(9):
            if line[-(i+len(writtenNumbers[x])):-i] == writtenNumbers[x] and last == '':
                last = digits[x]
    # concatenate the two strings, make number, add up, get result, delete the gym, marry facebook
    sum += int(first + last)
print(sum)