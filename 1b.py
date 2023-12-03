file = open('1_input')
sum = 0
writtenNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
flag = 0
for line in file:
    for i in range(len(line)):
        if line[i].isdigit():
            first = line[i]
            break
        for x in range(9):
            if line[i:(i+len(writtenNumbers[x]))] == writtenNumbers[x]:
                first = digits[x]
                flag = 1
        if flag == 1:
            flag = 0
            break

    for i in range(len(line)):
        if line[-i].isdigit() and i != 0:
            last = line[-i]
            break
        if i == len(line)-1:
            last = line[0]
            break
        for x in range(9):
            if line[-(i+len(writtenNumbers[x])):-i] == writtenNumbers[x]:
                last = digits[x]
                flag = 1
        if flag == 1:
            flag = 0
            break

    sum += int(first + last)
        
print(sum)