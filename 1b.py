file = open('1_input')
sum = 0
# Make lists of possible numbers
writtenNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for line in file:
    # init to empty to check whether first or last number has been found
    first = ''
    last = ''
    for i in range(len(line)):
        if first != '' and last != '':
            break
        # if digit easy we done
        if line[i].isdigit() and first == '':
            first = line[i]
        # if not digit check against strings
        for x in range(9):
            if line[i:(i+len(writtenNumbers[x]))] == writtenNumbers[x] and first == '':
                first = digits[x]
        # for the last we do the same, just with reversed indices. -0 is 0 so we gotta skip that one
        if line[-i].isdigit() and i != 0 and last == '':
            last = line[-i]
        # except after we checked everything else, then it must be at index 0.
        if i == len(line)-1 and last == '':
            last = line[0]
        # check for number strings
        for x in range(9):
            if line[-(i+len(writtenNumbers[x])):-i] == writtenNumbers[x] and last == '':
                last = digits[x]
    # concatenate the two strings, make number, add up, get result, delete the gym, marry facebook
    sum += int(first + last)
# i gotta see my man
print(sum)