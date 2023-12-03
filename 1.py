file = open('1_input')
sum = 0
for line in file:
    string = ''.join(filter(str.isdigit, line))
    value = int(string[0] + string[-1])
    sum += value
print(sum)